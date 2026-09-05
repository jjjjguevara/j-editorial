#!/usr/bin/env python3
"""Verify Phase 3 records differ only by the declared migration of input paths.

This is a tooling integrity check, not a research gate. Both recorded hashes and
check counts are authenticated; all experiment fields and semantic limitations
must survive the migration. Environment observations may differ between runs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


class VerificationError(ValueError):
    """A record is malformed or not equivalent to its antecedent."""


def digest(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def authenticate(record: Any, name: str) -> dict:
    if not isinstance(record, dict) or not isinstance(record.get("experiment"), dict):
        raise VerificationError(f"{name}: missing experiment object")
    experiment = record["experiment"]
    if record.get("experiment_sha256") != digest(experiment):
        raise VerificationError(f"{name}: experiment_sha256 does not authenticate the record")
    inputs = experiment.get("inputs")
    if not isinstance(inputs, dict) or not inputs:
        raise VerificationError(f"{name}: missing input digests")
    if any(not isinstance(k, str) or not isinstance(v, str) for k, v in inputs.items()):
        raise VerificationError(f"{name}: input paths and digests must be strings")
    checks = experiment.get("checks")
    if not isinstance(checks, list) or not checks:
        raise VerificationError(f"{name}: no checks")
    ids: set[str] = set()
    for check in checks:
        if not isinstance(check, dict) or not isinstance(check.get("id"), str) or not check["id"]:
            raise VerificationError(f"{name}: malformed check")
        if check["id"] in ids:
            raise VerificationError(f"{name}: duplicate check id {check['id']}")
        ids.add(check["id"])
        if check.get("passed") is not True:
            raise VerificationError(f"{name}: check {check['id']} did not pass")
    for key in ("checks_passed", "checks_total"):
        if type(record.get(key)) is not int or record[key] != len(checks):
            raise VerificationError(f"{name}: {key} disagrees with the checks")
    return experiment


def verify(original: Any, rerun: Any, manifest: Any) -> dict:
    old = authenticate(original, "original")
    new = authenticate(rerun, "rerun")
    moves = manifest.get("moves") if isinstance(manifest, dict) else None
    if not isinstance(moves, dict) or not moves:
        raise VerificationError("move map must be a nonempty object")
    if any(not isinstance(k, str) or not k or not isinstance(v, str) or not v for k, v in moves.items()):
        raise VerificationError("move map paths must be nonempty strings")
    if len(set(moves.values())) != len(moves):
        raise VerificationError("move map is not one-to-one")
    reverse = {new_path: old_path for old_path, new_path in moves.items()}
    remapped = dict(new)
    inputs = {}
    for path, value in new["inputs"].items():
        old_path = reverse.get(path, path)
        if old_path in inputs:
            raise VerificationError(f"input path collision after remapping: {old_path}")
        inputs[old_path] = value
    remapped["inputs"] = inputs
    if remapped != old:
        raise VerificationError("experiment changed beyond the declared input path migration")
    # The digest intentionally excludes environment. Do not let that exclusion
    # also conceal changed constraints, status, or training eligibility.
    excluded = {"experiment", "experiment_sha256", "environment"}
    old_envelope = {k: v for k, v in original.items() if k not in excluded}
    new_envelope = {k: v for k, v in rerun.items() if k not in excluded}
    if old_envelope != new_envelope:
        raise VerificationError("record metadata or semantic limitations changed")
    return {
        "tooling_integrity": "verified",
        "research_gate_released": False,
        "original_experiment_sha256": original["experiment_sha256"],
        "rerun_experiment_sha256": rerun["experiment_sha256"],
        "rerun_digest_with_original_input_keys": digest(remapped),
        "checks_verified_in_each_record": len(old["checks"]),
        "entire_experiment_equivalent_up_to_input_paths": True,
        "semantic_envelope_unchanged": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("rerun", type=Path)
    parser.add_argument("move_map", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        paths = (args.original, args.rerun, args.move_map)
        result = verify(*(json.loads(p.read_text(encoding="utf-8")) for p in paths))
        text = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.output:
            if args.output.resolve() in {p.resolve() for p in paths}:
                raise VerificationError("output must not overwrite an input record")
            args.output.write_text(text, encoding="utf-8")
        print(text, end="")
        return 0
    except (OSError, ValueError) as exc:
        print(f"migration verification failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
