# J-Editorial bootstrap adversarial review

Status: **PHASE 1.1 / PARTIAL OWNER DECISIONS / REVISED DECISION HOLD**  
Repository base: **`fdfffb0da4eabd7c3db7d303013e0777db149e82`**  
Research cutoff: **2026-09-04**  
Controlling contract: **`BOOTSTRAP.md`**  
Repository gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Implementation authorization: **not granted**  
Dataset-research execution: **not performed**

## Purpose

This directory records execution of the J-Editorial bootstrap contract before architecture or implementation. Phase 1 challenged the initial product model. Phase 1.1 records the owner's partial choices, audits the selected Amnesia technical use case, and researches D-02 beyond the original single-root alternatives.

## Current result

- D-01 selects a paired technical-reference and general-prose proof.
- `jjjjguevara/amnesia-docs` is the technical use case.
- The exact prose artifact remains open.
- D-02 no longer asks prematurely whether `Gap`, `Finding/Obligation`, or `Event` is the one semantic root.
- The current candidate is a three-axis Editorial Construction Space used to test a plural typed record family.
- D-03 remains deferred, with split authority by concern as a research hypothesis rather than an architecture.
- D-04 provisionally requires meaningful semantic operations plus checkpoints, without every-keystroke capture.
- The implementation and dataset-research gates remain closed.

## Work completed

### Phase 1

1. inspected the live repository and controlling documents;
2. audited Doc Doctor as prior art rather than normative specification;
3. tested the domain model against annotation, provenance, history, evaluation, security, and erasure standards;
4. compared representation and persistence strategies without selecting one;
5. stress-tested technical, subjective, branching, policy-version, deletion, and hostile-content cases;
6. opened draft PR #1 at the required owner-decision hold.

### Phase 1.1

1. recorded D-01C, the D-02 research instruction, the D-03 dependency, and provisional D-04B;
2. researched Gustavo Bueno's gnoseological space and translated it cautiously into an editorial completeness scaffold;
3. compared that scaffold with PROV, Web Annotation, SHACL, ODRL, TEI, IFLA LRM/LRMoo, CIDOC CRM, ICA Records in Contexts, nanopublications, IBIS/AIF, and RO-Crate;
4. separated analytic coordinates from canonical persisted record semantics;
5. derived a falsifiable typed-pluralism hypothesis and retained `Gap` as a candidate projection;
6. inspected pinned `amnesia-docs` and `amnesia` states;
7. found real API-documentation parity conflicts in `commands.notes` and `expandCapabilities`;
8. defined the candidate Amnesia goal contract, obligation families, graders, and D-04B history episode;
9. preserved unresolved product decisions rather than filling them implicitly.

## Work deliberately not performed

This work did not:

- implement framework code, schemas, APIs, adapters, editors, servers, or graders;
- modify `amnesia-docs`, `amnesia`, or Doc Doctor;
- select Git, Dolt, PostgreSQL, DeltaDB, a CRDT, event sourcing, a language, or a framework;
- accept an ADR;
- change or release the bootstrap gate;
- merge or modify `main`;
- acquire, generate, transform, label, split, benchmark, or train on a model-training dataset;
- manually edit `.beads` data.

## Artifact map

| Artifact | Role |
|---|---|
| [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md) | Phase-1 repository, standard, evaluation, persistence, and security evidence |
| [`ADVERSARIAL-REVIEW.md`](ADVERSARIAL-REVIEW.md) | Phase-1 findings, stress tests, and initial recommendations |
| [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md) | Binding record of partial owner decisions and their limits |
| [`D-02-SEMANTIC-CENTER-REVIEW.md`](D-02-SEMANTIC-CENTER-REVIEW.md) | Bueno translation, alternatives, typed-pluralism hypothesis, and revised D-02 packet |
| [`AMNESIA-DOCS-SLICE-AUDIT.md`](AMNESIA-DOCS-SLICE-AUDIT.md) | Pinned technical-use-case audit, concrete parity findings, and candidate goal/eval contract |
| [`PHASE-2-SOURCE-LEDGER.md`](PHASE-2-SOURCE-LEDGER.md) | Sources added for phase 1.1 and their limitations |
| [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md) | Remaining pivotal questions and exact answer form |
| [`NEXT-PHASE-CONTRACT.md`](NEXT-PHASE-CONTRACT.md) | Research fan-out, dependencies, gates, and stop conditions after the revised answers |

## Why execution halts again

Three choices now affect the validity of the paired proof and the next research graph:

- whether the candidate Editorial Construction Space plus typed plural records becomes the phase-2 falsifiable hypothesis;
- which exact general-prose artifact forms the other half of D-01C;
- whether the private Amnesia product repository can serve as a pinned, executable oracle for `amnesia-docs`.

The exact questions are in [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md).

## Tracking constraint

The repository requires Beads as the durable tracker. The available runtime still lacks compatible `bd` and `dolt` execution against the repository's Dolt-backed store. No direct database or JSONL mutation has been made. The native fan-out procedure remains specified in `NEXT-PHASE-CONTRACT.md` and must run in a compatible checkout.

## Resume condition

Execution resumes after D-02R, D-01P, and AMN-01 are answered. The next phase must revise `BOOTSTRAP.md`, `ROADMAP.md`, `RESEARCH.md`, the held dataset charter's terminology/scope only, and the bootstrap status packet together. Implementation, ADR acceptance, persistence selection, and dataset research remain blocked until their later gates explicitly pass.
