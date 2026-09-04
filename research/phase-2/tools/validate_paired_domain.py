#!/usr/bin/env python3
"""Validate the Phase 2 paired-domain research result.

This validator binds two independently validated fixtures to a cross-domain
manifest. It does not replace either fixture validator and does not establish
human/model grader reliability.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

EXPECTED_C = [f"C-{n:02d}" for n in range(1, 8)]
EXPECTED_TECHNICAL = {
    "fixture_id": "je-fx-amnesia-notes-001",
    "fixture_version": "0.2.0",
    "input_file_sha256": "cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82",
    "canonical_research_sha256": "4035f6f544c08e6c8878b0e0bbc0a2a696a48501feab0f1ea554ae74c4450e8c",
}
EXPECTED_PROSE = {
    "fixture_id": "je-fx-portfolio-about-001",
    "fixture_version": "0.1.0",
    "input_file_sha256": "9c24cf03065f69aacaed4375c9830feeec0a78c8277e3a07c0b8f299147b4eb2",
    "canonical_research_sha256": "74e0e3282596fd7ade8607c9a0ef40b82e096ad98840e157407e0c6b972f012e",
}


def fail(message: str) -> None:
    raise ValueError(message)


def load(path: Path) -> tuple[dict[str, Any], bytes]:
    raw = path.read_bytes()
    value = json.loads(raw)
    if not isinstance(value, dict):
        fail(f"{path} must contain a JSON object")
    return value, raw


def check_result(
    result: dict[str, Any],
    expected: dict[str, str],
    prefix: str,
    count: int,
) -> bool:
    return (
        result.get("status") == "pass"
        and all(result.get(key) == value for key, value in expected.items())
        and result.get("checks")
        == {f"{prefix}-{n:02d}": "passed" for n in range(1, count + 1)}
    )


def validate(
    manifest: dict[str, Any],
    technical: dict[str, Any],
    prose: dict[str, Any],
) -> dict[str, str]:
    classification = manifest.get("classification", {})
    if (
        classification.get("training_eligibility") != "prohibited"
        or classification.get("benchmark_corpus_status") != "not-a-corpus"
        or classification.get("architecture_selection") != "none"
        or classification.get("source_mutation") != "none"
    ):
        fail("paired manifest crossed a held boundary")

    obligations = manifest.get("cross_domain_obligations", [])
    obligation_ids = [row.get("id") for row in obligations if isinstance(row, dict)]
    if obligation_ids != EXPECTED_C or manifest.get("expected") != EXPECTED_C:
        fail("paired manifest must list C-01 through C-07 exactly once and in order")

    technical_ok = check_result(technical, EXPECTED_TECHNICAL, "E", 10)
    prose_ok = check_result(prose, EXPECTED_PROSE, "P", 12)
    if not technical_ok:
        fail("technical fixture result does not match the pinned passing result")
    if not prose_ok:
        fail("prose fixture result does not match the pinned passing result")

    technical_binding = manifest.get("technical_slice", {})
    prose_binding = manifest.get("prose_slice", {})
    for key, value in EXPECTED_TECHNICAL.items():
        if technical_binding.get(key) != value:
            fail(f"technical manifest binding mismatch: {key}")
    for key, value in EXPECTED_PROSE.items():
        if prose_binding.get(key) != value:
            fail(f"prose manifest binding mismatch: {key}")
    if technical_binding.get("result_status") != "pass":
        fail("technical manifest result status is not pass")
    if prose_binding.get("result_status") != "pass":
        fail("prose manifest result status is not pass")

    tech_checks = set(technical["checks"])
    prose_checks = set(prose["checks"])

    checks: dict[str, str] = {}
    for row in obligations:
        ident = row["id"]
        technical_evidence = row.get("technical_evidence", [])
        prose_evidence = row.get("prose_evidence", [])
        if not row.get("claim") or not technical_evidence or not prose_evidence:
            checks[ident] = "failed"
            continue

        concrete_technical = [
            ref for ref in technical_evidence if isinstance(ref, str) and ref.startswith("E-")
        ]
        concrete_prose = [
            ref for ref in prose_evidence if isinstance(ref, str) and ref.startswith("P-")
        ]
        refs_ok = (
            all(ref in tech_checks for ref in concrete_technical)
            and all(ref in prose_checks for ref in concrete_prose)
            and all(technical["checks"][ref] == "passed" for ref in concrete_technical)
            and all(prose["checks"][ref] == "passed" for ref in concrete_prose)
        )
        checks[ident] = "passed" if refs_ok else "failed"

    conclusions = manifest.get("conclusions", {})
    boundary_ok = (
        conclusions.get("typed_vocabulary_generalization")
        == "supported-with-constraints"
        and conclusions.get("event_fluent_checkpoint_shape")
        == "supported-for-further-research"
        and conclusions.get("prose_grader_reliability") == "not-established"
        and conclusions.get("empirical_reader_task") == "not-executed"
        and conclusions.get("production_architecture") == "not-selected"
        and conclusions.get("persistence_adr") == "not-authorized"
        and conclusions.get("dataset_research") == "not-authorized"
        and conclusions.get("bootstrap_exit") == "not-passed"
    )
    if not boundary_ok:
        fail("paired conclusions overstate the executed evidence")

    failed = [name for name, status in checks.items() if status != "passed"]
    if failed:
        fail("failed paired-domain obligations: " + ", ".join(failed))
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("technical_result", type=Path)
    parser.add_argument("prose_result", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    manifest, manifest_raw = load(args.manifest)
    technical, technical_raw = load(args.technical_result)
    prose, prose_raw = load(args.prose_result)
    checks = validate(manifest, technical, prose)

    canonical = json.dumps(
        manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    result: dict[str, Any] = {
        "pair_id": manifest["pair_id"],
        "pair_version": manifest["version"],
        "status": "pass-with-constraints",
        "checks": checks,
        "manifest_file_sha256": hashlib.sha256(manifest_raw).hexdigest(),
        "canonical_research_sha256": hashlib.sha256(canonical).hexdigest(),
        "technical_result_file_sha256": hashlib.sha256(technical_raw).hexdigest(),
        "prose_result_file_sha256": hashlib.sha256(prose_raw).hexdigest(),
        "technical_fixture_input_sha256": technical["input_file_sha256"],
        "prose_fixture_input_sha256": prose["input_file_sha256"],
        "scope_note": (
            "Cross-result binding and manifest consistency only. Raw fixture semantics "
            "remain the responsibility of the E and P validators; empirical grader "
            "reliability, production architecture, persistence, and dataset use remain open."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
