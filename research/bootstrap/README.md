# J-Editorial bootstrap adversarial review — phase 1

Status: **IN PROGRESS / OWNER-DECISION-HOLD**  
Repository base: **`fdfffb0da4eabd7c3db7d303013e0777db149e82`**  
Research cutoff: **2026-09-04**  
Controlling contract: **`BOOTSTRAP.md`**  
Repository gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Implementation authorization: **not granted**  
Dataset-research execution: **not performed**

## Purpose

This directory records the first execution phase of the J-Editorial bootstrap contract. It converts the pre-bootstrap hypotheses into an adversarial evidence packet without selecting an implementation stack, accepting an ADR, defining a production schema, constructing a corpus, or releasing the implementation gate.

The phase stops where the contract requires owner judgment. The unresolved choices are recorded in [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md).

## Work completed

This phase:

1. inspected the live `j-editorial` repository and its controlling documents;
2. inspected the current `doc-doctor` implementation as prior art and migration evidence;
3. tested the provisional domain model against standards for annotation, provenance, document structure, addressing, version history, evaluation, security, and erasure;
4. compared credible representation and history strategies without selecting one;
5. compared candidate first product proofs;
6. stress-tested the framework against technical-reference, subjective-review, branching, policy-version, deletion, round-trip, and hostile-content scenarios;
7. identified assumptions that should not be inherited from Doc Doctor without evidence;
8. framed the pivotal decisions that block authoritative revision of `BOOTSTRAP.md`, `ROADMAP.md`, `RESEARCH.md`, and the research-program charters.

## Work deliberately not performed

This phase did **not**:

- implement framework code, adapters, schemas, APIs, editors, servers, or graders;
- select Git, Dolt, PostgreSQL, DeltaDB, a CRDT, a language, or a framework;
- create an ADR;
- change the bootstrap gate;
- merge or modify `main`;
- execute the model-training dataset research program;
- inspect, acquire, generate, transform, label, split, or benchmark any training dataset;
- treat accepted editorial history as training truth;
- modify Doc Doctor;
- manually edit `.beads` data.

The dataset charter was read only to identify authority, overlap, dependencies, and work that must remain held.

## Why execution halts here

Four choices change the product's ontology, persistence requirements, and first proof. Choosing them implicitly would violate the bootstrap contract:

- **D-01 — first product proof:** API/technical reference, general Doc Doctor prose, or a paired slice;
- **D-02 — semantic center:** gap-centered, obligation/finding-centered, or event-centered;
- **D-03 — representation authority:** source-first, structured-first, or split authority by concern;
- **D-04 — minimum history guarantee:** checkpoints only, domain operations plus checkpoints, or continuous edit history.

The evidence and consequences are in [`ADVERSARIAL-REVIEW.md`](ADVERSARIAL-REVIEW.md); the exact questions are in [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md).

## Artifact map

| Artifact | Role |
|---|---|
| [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md) | Versioned sources, repository observations, supported claims, and source limitations |
| [`ADVERSARIAL-REVIEW.md`](ADVERSARIAL-REVIEW.md) | Findings, alternatives, failure modes, stress tests, and non-binding recommendations |
| [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md) | Pivotal product questions requiring explicit owner answers |
| [`NEXT-PHASE-CONTRACT.md`](NEXT-PHASE-CONTRACT.md) | Proposed post-decision document revisions, research fan-out, dependencies, gates, and execution constraints |

## Evidence conventions

- **Finding** means directly observed or strongly supported.
- **Interpretation** means an implication for J-Editorial.
- **Recommendation** is non-binding until accepted.
- **Decision** requires explicit owner acceptance and later ADR/specification treatment where appropriate.
- Source identifiers such as `R-01`, `REP-01`, or `EVAL-03` resolve in `SOURCE-LEDGER.md`.
- Current product documentation is evidence about a product's present claims, not proof that its design transfers to J-Editorial.
- Preprints are marked and are not treated as standards.
- Marketing claims are used only to establish a vendor's stated capabilities and maturity, not independent performance.

## Tracking constraint

The repository requires Beads as the task system. The available runtime had neither `bd` nor `dolt`; `.beads/config.yaml` uses a Dolt-backed remote. Installing the supported `bd` release was attempted, but binary transfer into the execution runtime was unavailable. No direct database or JSONL mutation was made.

This is a hard execution limitation, not authorization to substitute Markdown tasks or GitHub Issues. Native Beads fan-out remains blocked until a compatible checkout can run `bd` against `refs/dolt/data`.

## Resume condition

Bootstrap execution resumes after the owner answers D-01 through D-04. The next phase must preserve the answer verbatim in the review record, revise the controlling documents accordingly, create the non-dataset research programs and Beads dependency graph, and keep the implementation gate closed.
