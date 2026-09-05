"""Tooling regression tests; synthetic inputs, not research evidence or gate passes."""
from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


migration = load("verify_migration")
registry = load("render_registry")


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.old = {
            "experiment": {"inputs": {"old/input.json": "a" * 64},
                           "checks": [{"id": "check-1", "passed": True}], "extra": {"x": 1}},
            "checks_total": 1, "checks_passed": 1,
            "status": "exploratory", "training_eligibility": "held", "environment": {"python": "old"},
        }
        self.old["experiment_sha256"] = migration.digest(self.old["experiment"])
        self.new = copy.deepcopy(self.old)
        self.new["experiment"]["inputs"] = {"new/input.json": "a" * 64}
        self.new["environment"] = {"python": "new"}
        self.seal()
        self.moves = {"moves": {"old/input.json": "new/input.json"}}

    def seal(self):
        self.new["experiment_sha256"] = migration.digest(self.new["experiment"])

    def rejects(self):
        with self.assertRaises(migration.VerificationError):
            migration.verify(self.old, self.new, self.moves)

    def test_path_only_migration(self):
        self.assertFalse(migration.verify(self.old, self.new, self.moves)["research_gate_released"])

    def test_original_hash_is_authenticated(self):
        self.old["experiment_sha256"] = "forged"
        self.rejects()

    def test_rerun_hash_is_authenticated(self):
        self.new["experiment_sha256"] = "forged"
        self.rejects()

    def test_undeclared_section_change(self):
        self.new["experiment"]["extra"]["x"] = 2
        self.seal()
        self.rejects()

    def test_new_section_is_not_ignored(self):
        self.new["experiment"]["surprise"] = True
        self.seal()
        self.rejects()

    def test_counts_are_verified(self):
        self.new["checks_passed"] = 99
        self.rejects()

    def test_false_check_cannot_hide_behind_summary(self):
        self.new["experiment"]["checks"][0]["passed"] = False
        self.seal()
        self.rejects()

    def test_truthy_non_boolean_is_not_a_pass(self):
        self.new["experiment"]["checks"][0]["passed"] = "true"
        self.seal()
        self.rejects()

    def test_duplicate_check_ids(self):
        self.new["experiment"]["checks"] *= 2
        self.new["checks_passed"] = self.new["checks_total"] = 2
        self.seal()
        self.rejects()

    def test_non_injective_move_map(self):
        self.moves["moves"]["other.json"] = "new/input.json"
        self.rejects()

    def test_input_collision_after_mapping(self):
        self.new["experiment"]["inputs"]["old/input.json"] = "a" * 64
        self.seal()
        self.rejects()

    def test_semantic_limits_must_survive(self):
        self.new["training_eligibility"] = "released"
        self.rejects()

    def test_empty_checks_cannot_pass(self):
        self.new["experiment"]["checks"] = []
        self.new["checks_total"] = self.new["checks_passed"] = 0
        self.seal()
        self.rejects()

    def test_output_cannot_replace_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            paths = [Path(temp) / name for name in ("old.json", "new.json", "moves.json")]
            for path, value in zip(paths, (self.old, self.new, self.moves)):
                path.write_text(json.dumps(value))
            before = paths[0].read_bytes()
            argv = ["verify_migration.py", *map(str, paths), "--output", str(paths[0])]
            with patch.object(sys, "argv", argv), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(migration.main(), 1)
            self.assertEqual(paths[0].read_bytes(), before)


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        folder = self.root / "research/programs/example"
        folder.mkdir(parents=True)
        for name in ("CHARTER.md", "RESULTS.md"):
            (folder / name).write_text("# Synthetic tooling test\n")
        self.epic = {"id": "test-1", "issue_type": "epic", "status": "open", "labels": ["research-program"],
                     "metadata": {"program_slug": "example", "alias": "EX", "lifecycle": "ACTIVE",
                                  "charter": "research/programs/example/CHARTER.md",
                                  "results": "research/programs/example/RESULTS.md"}}
        self.gate = {"id": "test-1.1", "status": "open", "labels": ["gate"],
                     "metadata": {"program_slug": "example", "gate": "EX-G1"}}

    def render(self, epics=None, gates=None):
        with patch.object(registry, "bd", side_effect=[epics if epics is not None else [self.epic],
                                                      gates if gates is not None else [self.gate]]):
            return registry.render(self.root)

    def test_valid_registry(self):
        self.assertIn("`EX-G1`", self.render())

    def test_empty_registry_fails_closed(self):
        with self.assertRaises(registry.RegistryError):
            self.render(epics=[])

    def test_missing_program_is_not_silently_dropped(self):
        p = self.root / "research/programs/unregistered"
        p.mkdir()
        (p / "CHARTER.md").write_text("# Unregistered\n")
        with self.assertRaises(registry.RegistryError):
            self.render()

    def test_duplicate_program(self):
        other = copy.deepcopy(self.epic)
        other["id"] = "test-2"
        with self.assertRaises(registry.RegistryError):
            self.render(epics=[self.epic, other])

    def test_wrong_gate_owner(self):
        self.gate["metadata"]["program_slug"] = "wrong"
        with self.assertRaises(registry.RegistryError):
            self.render()

    def test_duplicate_gate(self):
        with self.assertRaises(registry.RegistryError):
            self.render(gates=[self.gate, self.gate])

    def test_missing_result_file(self):
        (self.root / "research/programs/example/RESULTS.md").unlink()
        with self.assertRaises(registry.RegistryError):
            self.render()

    def test_metadata_path_is_checked(self):
        self.epic["metadata"]["charter"] = "other.md"
        with self.assertRaises(registry.RegistryError):
            self.render()

    def test_gate_metadata_falls_back_to_native_show(self):
        incomplete = dict(self.gate, metadata=None)
        with patch.object(registry, "bd", side_effect=[[self.epic], [incomplete], [self.gate]]):
            self.assertIn("`EX-G1`", registry.render(self.root))

    def test_metadata_rejects_non_object(self):
        with self.assertRaises(registry.RegistryError):
            registry.metadata({"metadata": "[]"})

    def test_duplicate_markers_rejected(self):
        with self.assertRaises(registry.RegistryError):
            registry.split_registry(registry.BEGIN * 2 + registry.END)

    def test_reversed_markers_rejected(self):
        with self.assertRaises(registry.RegistryError):
            registry.split_registry(registry.END + registry.BEGIN)

    def test_bd_reads_selected_document_repository(self):
        done = subprocess.CompletedProcess([], 0, stdout="[]", stderr="")
        with patch.object(registry.subprocess, "run", return_value=done) as run:
            self.assertEqual(registry.bd(self.root, "list"), [])
            self.assertEqual(run.call_args.kwargs["cwd"], self.root)

    def test_check_never_writes_and_uses_document_root(self):
        path = self.root / "RESEARCH.md"
        content = f"preface\n{registry.BEGIN}\nold\n{registry.END}\ntail\n"
        path.write_text(content)
        with patch.object(sys, "argv", ["render_registry.py", "--file", str(path), "--check"]), \
             patch.object(registry, "render", return_value="new") as render, \
             contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(registry.main(), 1)
            render.assert_called_once_with(self.root)
        self.assertEqual(path.read_text(), content)

    def test_failed_native_read_does_not_overwrite_document(self):
        path = self.root / "RESEARCH.md"
        content = f"{registry.BEGIN}\nretained\n{registry.END}\n"
        path.write_text(content)
        with patch.object(sys, "argv", ["render_registry.py", "--file", str(path)]), \
             patch.object(registry, "bd", side_effect=FileNotFoundError("bd unavailable")), \
             contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(registry.main(), 2)
        self.assertEqual(path.read_text(), content)


if __name__ == "__main__":
    unittest.main()
