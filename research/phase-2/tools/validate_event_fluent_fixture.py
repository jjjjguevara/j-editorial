#!/usr/bin/env python3
"""Validate the bounded J-Editorial Phase 2 event–fluent research fixture.

This is an experiment validator, not a production schema validator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

REQUIRED_DIMENSIONS = {"material", "goal", "normative", "epistemic", "operational", "authority", "release", "retention"}
EXPECTED_TESTS = [f"E-{n:02d}" for n in range(1, 11)]


def fail(message: str) -> None:
    raise ValueError(message)


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def by_id(rows: list[dict[str, Any]], label: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for row in rows:
        ident = row.get("id")
        if not isinstance(ident, str) or not ident:
            fail(f"{label} entry lacks id")
        if ident in result:
            fail(f"duplicate {label} id: {ident}")
        result[ident] = row
    return result


def effect_dimensions(tx: dict[str, Any]) -> set[str]:
    return {e.get("dimension") for e in tx.get("effects", []) if isinstance(e, dict)}


def validate(data: dict[str, Any]) -> tuple[dict[str, str], dict[str, int]]:
    cls = data.get("classification", {})
    if cls.get("training_eligibility") != "prohibited" or cls.get("benchmark_corpus_status") != "not-a-corpus":
        fail("fixture must remain prohibited for training and must not claim corpus status")

    model = data.get("model", {})
    if set(model.get("dimensions", [])) != REQUIRED_DIMENSIONS:
        fail("state dimensions do not match the accepted research model")
    if model.get("semantic_replay_can_reconstruct_source_bytes") is not False:
        fail("semantic replay must not claim exact source reconstruction")
    if model.get("storage_order_is_causal_order") is not False:
        fail("storage order must not be equated with causal order")

    sources = by_id(data.get("sources", []), "source")
    transactions = by_id(data.get("transactions", []), "transaction")
    fluents = by_id(data.get("fluents", []), "fluent")
    projections = by_id(data.get("projections", []), "projection")

    if len(transactions) != 13 or len(sources) != 5 or len(fluents) != 3 or len(projections) != 4:
        fail("fixture cardinalities changed")
    for source in sources.values():
        if not source.get("digest") or not source.get("algorithm"):
            fail(f"source {source['id']} lacks immutable identity")

    # Parent references must exist and the stored list must be topological.
    seen: set[str] = set()
    for tx in data["transactions"]:
        for parent in tx.get("parents", []):
            if parent not in transactions:
                fail(f"unknown parent {parent}")
            if parent not in seen:
                fail(f"transaction order is not topological at {tx['id']}")
        seen.add(tx["id"])

    checks: dict[str, str] = {}

    finding_tx = transactions["tx:record-finding"]
    dims = effect_dimensions(finding_tx)
    checks["E-01"] = "passed" if {"epistemic", "normative", "operational", "authority", "release"} <= dims else "failed"
    checks["E-02"] = "passed" if "material" not in dims and "material" in effect_dimensions(transactions["tx:apply-docs"]) else "failed"

    event_fluent_ok = all(f.get("initiated_by") in transactions and (f.get("terminated_by") is None or f.get("terminated_by") in transactions) for f in fluents.values())
    checks["E-03"] = "passed" if event_fluent_ok else "failed"

    finding = data.get("finding", {})
    checks["E-04"] = "passed" if len(set(finding.get("axes", []))) == 3 and len(set(finding.get("roles", []))) >= 5 else "failed"

    sibling_parent = "tx:record-finding"
    siblings = [t for t in transactions.values() if t.get("parents") == [sibling_parent] and t.get("type") == "proposal"]
    adjudication = transactions["tx:adjudicate"]
    checks["E-05"] = "passed" if len(siblings) == 3 and len(adjudication.get("parents", [])) == 3 else "failed"

    late = transactions["tx:external-change"]
    late_order = parse_time(late["effective_time"]) < parse_time(late["observed_at"]) <= parse_time(late["recorded_at"])
    checks["E-06"] = "passed" if late_order and late.get("docs_checkpoint_unchanged") is True else "failed"

    same_head = [p for p in projections.values() if p.get("state_head") == "tx:verify"]
    checks["E-07"] = "passed" if len(same_head) == 2 and len({p["reducer_version"] for p in same_head}) == 2 and same_head[0]["output"] != same_head[1]["output"] else "failed"

    evidence = data.get("evidence", {})
    evidence_fields = ["tool", "tool_version", "environment", "raw_output_sha256", "uncertainty", "abstentions"]
    checks["E-08"] = "passed" if all(evidence.get(k) not in (None, "", []) for k in evidence_fields) else "failed"

    erasure = data.get("erasure", {})
    erasure_ok = erasure.get("identity_retained") is True and erasure.get("exact_replay_possible") is False and str(erasure.get("semantic_replay", "")).startswith("partial")
    checks["E-09"] = "passed" if erasure_ok else "failed"

    checkpoint_ok = all(s.get("digest") for s in sources.values()) and model.get("semantic_replay_can_reconstruct_source_bytes") is False
    checks["E-10"] = "passed" if checkpoint_ok else "failed"

    if data.get("expected") != EXPECTED_TESTS:
        fail("expected test manifest must list E-01 through E-10")
    failed = [name for name, status in checks.items() if status != "passed"]
    if failed:
        fail("failed experiment obligations: " + ", ".join(failed))

    counts = {"transaction_count": len(transactions), "source_binding_count": len(sources), "fluent_count": len(fluents), "projection_count": len(projections)}
    return checks, counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    raw = args.fixture.read_bytes()
    data = json.loads(raw)
    checks, counts = validate(data)
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    result: dict[str, Any] = {
        "fixture_id": data["fixture_id"],
        "fixture_version": data["version"],
        "status": "pass",
        "checks": checks,
        **counts,
        "input_file_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_research_sha256": hashlib.sha256(canonical).hexdigest(),
        "canonicalization_note": "Python sorted-key compact JSON for this experiment; not an RFC 8785/JCS claim.",
        "scope_note": "Internal fixture consistency only; not production schema, runtime, persistence, corpus, or dataset validation."
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, json.JSONDecodeError, ValueError, KeyError, TypeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
