#!/usr/bin/env python3
"""Validate the bounded J-Editorial portfolio About-page prose fixture.

This is a research-fixture validator. It does not validate prose quality,
biographical truth, a production schema, or a model grader.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

REQUIRED_DIMENSIONS = {
    "material",
    "goal",
    "normative",
    "epistemic",
    "operational",
    "authority",
    "release",
    "retention",
}
EXPECTED_TESTS = [f"P-{n:02d}" for n in range(1, 13)]
EXPECTED_TARGET = {
    "repository": "jjjjguevara/sci-jjjjguevara",
    "commit": "1c93b60e75ce60203295a988b8125d44e6acb6bc",
    "path": "src/pages/about.astro",
    "blob": "d56c560fc63569b471cc4e81a65daf52568fe754",
    "route": "/about",
}
EXPECTED_CHECKPOINTS = {
    "about:p0-pre-audit": {
        "commit": "f66fa3d1b6c7b03ece46eb2f20d9089a51f02e2a",
        "digest": "e11905e3db4591301c9bb17bed5a50490ba5bffb",
    },
    "about:p1-prose-audit": {
        "commit": "900483708d74e83c5f4acd3b308127f7fa430117",
        "digest": "5d3d5007a6d2af82d8526e5862e87ec9dd239b26",
    },
    "about:p2-target": {
        "commit": "1c93b60e75ce60203295a988b8125d44e6acb6bc",
        "digest": "d56c560fc63569b471cc4e81a65daf52568fe754",
    },
}


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
    return {
        effect.get("dimension")
        for effect in tx.get("effects", [])
        if isinstance(effect, dict)
    }


def material_transition(tx: dict[str, Any], path: str) -> tuple[Any, Any] | None:
    for effect in tx.get("effects", []):
        if (
            isinstance(effect, dict)
            and effect.get("dimension") == "material"
            and effect.get("path") == path
        ):
            return effect.get("before"), effect.get("after")
    return None


def validate(data: dict[str, Any]) -> tuple[dict[str, str], dict[str, int]]:
    classification = data.get("classification", {})
    if (
        classification.get("training_eligibility") != "prohibited"
        or classification.get("benchmark_corpus_status") != "not-a-corpus"
        or classification.get("source_mutation") != "none"
        or classification.get("architecture_selection") != "none"
    ):
        fail("fixture crossed the research-only, no-mutation, no-architecture boundary")

    model = data.get("model", {})
    if set(model.get("dimensions", [])) != REQUIRED_DIMENSIONS:
        fail("state dimensions do not match the accepted research model")
    required_false = [
        "semantic_replay_can_reconstruct_source_bytes",
        "storage_order_is_causal_order",
        "observations_are_automatic_truth",
        "historical_acceptance_is_unique_gold",
        "truth_implies_disclosure_permission",
        "reader_observation_is_release_authority",
    ]
    if any(model.get(field) is not False for field in required_false):
        fail("one or more non-collapse invariants were weakened")
    if model.get("projections_are_derived") is not True:
        fail("projections must remain derived")

    target = data.get("target", {})
    for key, expected in EXPECTED_TARGET.items():
        if target.get(key) != expected:
            fail(f"target {key} does not match accepted D-01P scope")
    excluded = set(target.get("excluded_surfaces", []))
    if "/" not in excluded or "/field-notes" not in excluded:
        fail("homepage and Field Notes exclusions must remain explicit")

    sources = by_id(data.get("sources", []), "source")
    actors = by_id(data.get("actors", []), "actor")
    obligations = by_id(data.get("obligations", []), "obligation")
    evidence = by_id(data.get("evidence", []), "evidence")
    findings = by_id(data.get("findings", []), "finding")
    transactions = by_id(data.get("transactions", []), "transaction")
    fluents = by_id(data.get("fluents", []), "fluent")
    projections = by_id(data.get("projections", []), "projection")

    for source in sources.values():
        if not source.get("digest") or not source.get("algorithm"):
            fail(f"source {source['id']} lacks immutable identity")
    for evidence_item in evidence.values():
        for field in (
            "method",
            "tool",
            "tool_version",
            "environment",
            "raw_output_sha256",
            "uncertainty",
            "abstentions",
        ):
            if evidence_item.get(field) in (None, "", []):
                fail(f"evidence {evidence_item['id']} lacks {field}")

    # Parent references must exist and the stored list must be topological.
    seen: set[str] = set()
    for tx in data.get("transactions", []):
        for parent in tx.get("parents", []):
            if parent not in transactions:
                fail(f"unknown parent {parent}")
            if parent not in seen:
                fail(f"transaction order is not topological at {tx['id']}")
        seen.add(tx["id"])

    for fluent in fluents.values():
        if fluent.get("initiated_by") not in transactions:
            fail(f"fluent {fluent['id']} has unknown initiator")
        terminated = fluent.get("terminated_by")
        if terminated is not None and terminated not in transactions:
            fail(f"fluent {fluent['id']} has unknown terminator")

    checks: dict[str, str] = {}

    # P-01: exact, bounded, research-only scope.
    checks["P-01"] = (
        "passed"
        if classification.get("target_scope") == "single-public-about-page"
        and target.get("evaluated_projection")
        == "visible-text-and-semantic-heading-list-structure"
        and classification.get("private_data_boundary")
        == "details-already-present-on-pinned-about-page-only"
        else "failed"
    )

    # P-02: exact real checkpoint chain and accepted target binding.
    checkpoints_ok = True
    for source_id, expected in EXPECTED_CHECKPOINTS.items():
        source = sources.get(source_id, {})
        checkpoints_ok = checkpoints_ok and all(
            source.get(key) == value for key, value in expected.items()
        )
        checkpoints_ok = checkpoints_ok and source.get("synthetic") is False
    checkpoints_ok = checkpoints_ok and (
        sources["about:p2-target"].get("introduced_by_commit")
        == "ddf0bcee6dc95d1deac016d8e47ee286d5c04055"
    )
    checks["P-02"] = "passed" if checkpoints_ok else "failed"

    # P-03: two distinct, real operation families with exact material transitions.
    rewrite = transactions["tx:apply-rhetoric-rewrite"]
    simplify = transactions["tx:apply-label-simplification"]
    operation_ok = (
        rewrite.get("operation_family") == "semantic-rhetorical-rewrite"
        and simplify.get("operation_family")
        == "structural-presentational-simplification"
        and material_transition(rewrite, "about")
        == ("about:p0-pre-audit", "about:p1-prose-audit")
        and material_transition(simplify, "about")
        == ("about:p1-prose-audit", "about:p2-target")
        and transactions["tx:observe-rewrite-acceptance"].get("unique_gold_answer")
        is False
        and transactions["tx:observe-label-acceptance"].get("unique_gold_answer")
        is False
    )
    checks["P-03"] = "passed" if operation_ok else "failed"

    # P-04: qualified evidence cannot be silently upgraded.
    levels = data.get("evidence_levels", {})
    evidence_boundary = findings["finding:verification-boundary"]
    qualified_ok = (
        levels.get("source_state") == "established-at-pinned-blobs"
        and levels.get("internal_consistency")
        == "established-at-pinned-representations"
        and levels.get("independent_substantiation") == "not-established"
        and evidence_boundary.get("creates_gap_under_goal_v1") is False
        and evidence_boundary.get("polarity") == "qualified-positive"
    )
    checks["P-04"] = "passed" if qualified_ok else "failed"

    # P-05: a disputed prose finding crosses axes, roles, and state dimensions.
    working = findings["finding:working-context-sufficiency"]
    working_tx = transactions["tx:record-working-context"]
    required_working_dims = {
        "epistemic",
        "normative",
        "operational",
        "authority",
        "release",
    }
    multidimensional_ok = (
        set(working.get("axes", []))
        == {"constructive", "referential", "pragmatic-governance"}
        and len(set(working.get("roles", []))) >= 5
        and required_working_dims <= effect_dimensions(working_tx)
        and working.get("polarity") == "disputed"
        and working.get("blocking_under_goal_v1") is False
    )
    checks["P-05"] = "passed" if multidimensional_ok else "failed"

    # P-06: exactly three potentially acceptable remedies; no exact-match gold.
    proposal_ids = {
        "tx:propose-retain",
        "tx:propose-episodes",
        "tx:propose-links",
    }
    proposals = [transactions[ident] for ident in proposal_ids]
    alternatives_ok = (
        all(tx.get("parents") == ["tx:record-working-context"] for tx in proposals)
        and len({tx.get("proposal") for tx in proposals}) == 3
        and all(tx.get("exact_match_gold") is False for tx in proposals)
        and all(tx.get("acceptable_if") for tx in proposals)
    )
    checks["P-06"] = "passed" if alternatives_ok else "failed"

    # P-07: conflicting reviewer observations remain unresolved by authority.
    review_a = transactions["tx:review-a"]
    review_b = transactions["tx:review-b"]
    deferred = transactions["tx:defer-working-context"]
    disagreement_fluent = fluents["fluent:working-context-disagreement"]
    disagreement_ok = (
        review_a.get("recommendation") != review_b.get("recommendation")
        and review_a.get("empirical") is False
        and review_b.get("empirical") is False
        and deferred.get("decision") == "deferred"
        and proposal_ids <= set(deferred.get("parents", []))
        and {"tx:review-a", "tx:review-b"} <= set(deferred.get("parents", []))
        and disagreement_fluent.get("terminated_by") is None
    )
    checks["P-07"] = "passed" if disagreement_ok else "failed"

    # P-08: style evidence remains project-scoped and non-universal.
    labels = findings["finding:decorative-labels"]
    norm = next(
        (
            row
            for row in data.get("norms", [])
            if row.get("id") == "norm:portfolio-creative-brief"
        ),
        {},
    )
    style_scope_ok = (
        labels.get("norm_scope") == "jjjjguevara-portfolio-only"
        and labels.get("non_universal") is True
        and labels.get("unique_gold_answer") is False
        and norm.get("scope") == "jjjjguevara-portfolio-only"
        and norm.get("non_universal") is True
        and norm.get("exception_authority") == "owner"
    )
    checks["P-08"] = "passed" if style_scope_ok else "failed"

    # P-09: truth/support and disclosure permission remain separate; payload is absent.
    private_source = sources["proposal:private-detail-redacted"]
    proposal = transactions["tx:propose-private-detail"]
    rejection = transactions["tx:reject-private-detail"]
    erasure = data.get("erasure", {})
    private_manifest = private_source.get("manifest", {})
    privacy_ok = (
        private_source.get("synthetic") is True
        and private_manifest.get("payload") == "[REDACTED_FIXTURE_PLACEHOLDER]"
        and private_manifest.get("asserts_real_personal_detail") is False
        and proposal.get("truth_status") == "unknown"
        and proposal.get("disclosure_permission") == "not-granted"
        and rejection.get("decision") == "rejected"
        and rejection.get("truth_status_after") == "unknown"
        and rejection.get("disclosure_permission_after") == "denied"
        and erasure.get("identity_retained") is True
        and erasure.get("payload_retained") is False
        and erasure.get("exact_replay_possible") is False
        and erasure.get("public_fixture_contains_real_private_detail") is False
    )
    checks["P-09"] = "passed" if privacy_ok else "failed"

    # P-10: an external fact change can stale an unchanged artifact.
    external = transactions["tx:external-profile-change"]
    time_ok = (
        parse_time(external["effective_time"])
        < parse_time(external["observed_at"])
        <= parse_time(external["recorded_at"])
    )
    external_dims = effect_dimensions(external)
    external_ok = (
        external.get("scenario") is True
        and external.get("asserts_real_world_change") is False
        and external.get("about_checkpoint_unchanged") is True
        and time_ok
        and material_transition(external, "profile")
        == ("profile:f0", "profile:f1-counterfactual")
        and {"material", "normative", "epistemic", "operational", "release"}
        <= external_dims
        and fluents["fluent:source-accepted"].get("terminated_by")
        == "tx:external-profile-change"
        and fluents["fluent:profile-stale-counterfactual"].get("initiated_by")
        == "tx:external-profile-change"
    )
    checks["P-10"] = "passed" if external_ok else "failed"

    # P-11: goal/policy versions can derive different readiness at the same state.
    same_head = [
        projection
        for projection in projections.values()
        if projection.get("state_head") == "tx:defer-working-context"
        and str(projection.get("id", "")).startswith("projection:readiness")
    ]
    projection_ok = (
        len(same_head) == 2
        and all(projection.get("derived") is True for projection in same_head)
        and len({projection.get("reducer_version") for projection in same_head}) == 2
        and len(
            {
                json.dumps(projection.get("output"), sort_keys=True)
                for projection in same_head
            }
        )
        == 2
        and any(projection.get("authoritative") is False for projection in same_head)
    )
    checks["P-11"] = "passed" if projection_ok else "failed"

    # P-12: observation, review, and release authorities stay separate.
    owner_authority = set(actors["owner"].get("authority", []))
    non_owner_release = [
        actor_id
        for actor_id, actor in actors.items()
        if actor_id != "owner" and "release" in set(actor.get("authority", []))
    ]
    authority_ok = (
        "release" in owner_authority
        and "authorize-disclosure" in owner_authority
        and not non_owner_release
        and actors["review-scenario-a"].get("synthetic") is True
        and actors["review-scenario-b"].get("synthetic") is True
        and obligations["working-context-sufficiency"].get("grader")
        == "human-review"
        and transactions["tx:verify-current-source"].get("built_output_equivalence")
        == "unknown"
    )
    checks["P-12"] = "passed" if authority_ok else "failed"

    if data.get("expected") != EXPECTED_TESTS:
        fail("expected test manifest must list P-01 through P-12")
    failed = [name for name, status in checks.items() if status != "passed"]
    if failed:
        fail("failed prose-fixture obligations: " + ", ".join(failed))

    counts = {
        "transaction_count": len(transactions),
        "source_binding_count": len(sources),
        "actor_count": len(actors),
        "finding_count": len(findings),
        "fluent_count": len(fluents),
        "projection_count": len(projections),
    }
    return checks, counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("fixture", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    raw = args.fixture.read_bytes()
    data = json.loads(raw)
    checks, counts = validate(data)
    canonical = json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    result: dict[str, Any] = {
        "fixture_id": data["fixture_id"],
        "fixture_version": data["version"],
        "status": "pass",
        "checks": checks,
        **counts,
        "input_file_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_research_sha256": hashlib.sha256(canonical).hexdigest(),
        "canonicalization_note": (
            "Python sorted-key compact JSON for this experiment; "
            "not an RFC 8785/JCS claim."
        ),
        "scope_note": (
            "Internal representation-fixture consistency only; not prose quality, "
            "biographical verification, live-site parity, grader calibration, "
            "production architecture, corpus, or dataset validation."
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
