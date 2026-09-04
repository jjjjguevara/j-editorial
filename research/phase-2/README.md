# Bootstrap Phase 2 foundations

Status: **technical/foundational research executed / next pivotal co-gate pending**  
Branch: `research/bootstrap-phase-2-foundations`  
Base: `70c8156cb52755ccffe4e9ed3049bd7f01f52297`  
Research cutoff: **2026-09-04**  
Implementation gate: **closed**  
Persistence/ADR gate: **closed**  
Dataset research: **not executed**

## Purpose

This directory executes the first research stage released by the merged bootstrap adversarial review. It tests the accepted Editorial Construction Space and causal event–fluent shape against a real Amnesia documentation contradiction, derives representation/history requirements, and establishes a security/authority baseline.

It does not bootstrap production code.

## Accepted inputs

- D-01: paired technical-reference and general-prose proof.
- D-02R: Editorial Construction Space plus typed plural records as a falsifiable research hypothesis.
- D-03: causal event–fluent multidimensional state with exact checkpoints and versioned projections is adequate for research.
- D-04: meaningful semantic operations plus checkpoints.
- AMN-01: pinned Amnesia product evidence may be used read/build/test-only in an isolated environment.
- Model-training dataset research remains held.

## Work executed

1. recorded the D-03 acceptance boundary;
2. refined the domain vocabulary through reduction tests;
3. bound current Amnesia Docs and Amnesia product refs;
4. retained static positive and adverse evidence separately;
5. constructed a 13-transaction causal event–fluent fixture;
6. represented multidimensional effects, fluents, three remedy branches, multi-parent adjudication, late knowledge, reducer divergence, erasure, and exact checkpoints;
7. implemented and ran a standard-library validator for E-01 through E-10;
8. derived representation, history, time, replay, target, evolution, erasure, and backend-exit requirements;
9. compared candidate substrate roles without selecting one;
10. established the minimum security and authority boundary for later agent/eval work.

## Result

The fixture validator passes all ten D-03 research obligations.

The favored logical hypothesis remains:

```text
typed event transactions
+ time-scoped facts/fluents
+ exact material checkpoints
+ causal parent graph
+ versioned projections
```

This result rejects:

- one scalar refinement score as canonical state;
- a Euclidean vector analogy as the complete data model;
- three mutually exclusive truth layers;
- pure event sourcing as a conclusion;
- semantic replay as a substitute for exact material state;
- one universal source of truth across all obligation types.

## Artifact map

| Artifact | Role |
|---|---|
| [`D-03-ACCEPTANCE.md`](D-03-ACCEPTANCE.md) | Binding scope of the owner's acceptance |
| [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md) | Primary/official sources, pinned repository evidence, and limitations |
| [`FRAME-DOMAIN-RESULT.md`](FRAME-DOMAIN-RESULT.md) | Cross-axis datum, surviving distinctions, rejected reductions, and candidate vocabulary |
| [`AMNESIA-ORACLE-EXPERIMENT.md`](AMNESIA-ORACLE-EXPERIMENT.md) | Pinned static product/docs evidence, history observations, execution limits, and sub-gate |
| [`EVENT-FLUENT-EXPERIMENT.md`](EVENT-FLUENT-EXPERIMENT.md) | Method, trace, E-01–E-10 results, comparison, and falsification conditions |
| [`REPRESENTATION-HISTORY-RESULT.md`](REPRESENTATION-HISTORY-RESULT.md) | Logical requirements, replay/time/target contracts, backend-exit contract, and bake-off workload |
| [`SECURITY-AUTHORITY-BASELINE.md`](SECURITY-AUTHORITY-BASELINE.md) | Trust zones, authority matrix, agent boundary, retention, erasure, and threat cases |
| [`REPRODUCE.md`](REPRODUCE.md) | Validator and isolated-oracle reproduction instructions |
| [`STAGE-GATE.md`](STAGE-GATE.md) | Phase result, released work, blocks, and next pivotal decision |
| [`fixtures/amnesia-notes-event-fluent.json`](fixtures/amnesia-notes-event-fluent.json) | Research-only machine-readable trace; explicitly not a corpus |
| [`tools/validate_event_fluent_fixture.py`](tools/validate_event_fluent_fixture.py) | Standard-library fixture validator |
| [`results/amnesia-notes-event-fluent-validation.json`](results/amnesia-notes-event-fluent-validation.json) | Committed deterministic validation output |

## Deliberate non-actions

This phase did not:

- modify Amnesia, Amnesia Docs, or Doc Doctor;
- invoke a workflow that could deploy;
- reproduce a private repository build without an isolated authenticated checkout;
- select a backend, event store, database, CRDT, canonical serialization, or implementation language;
- accept an ADR;
- create production schemas, APIs, packages, services, or agents;
- alter `.beads` directly;
- execute dataset/corpus research, labeling, training, or benchmarking.

## Tracking limitation

The repository's native Beads store is Dolt-backed. This runtime has neither `bd` nor `dolt`, and its container cannot reach external package/repository hosts. No tracker state was fabricated. The existing Beads fan-out contract remains the required procedure in a compatible checkout.

## Next stage

The technical foundation now supports:

- isolated Amnesia build/type-check/test reproduction;
- target-resolution experiments across real document edits;
- the representation/history substrate bake-off;
- implementation-neutral eval-instance design;
- selection and execution of the general-prose companion.

The last item is the next pivotal owner input because D-01 requires both halves to co-gate generality.
