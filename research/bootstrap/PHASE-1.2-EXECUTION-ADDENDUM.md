# Phase 1.2 execution addendum

Status: **active research amendment / implementation blocked**  
Amends: [`NEXT-PHASE-CONTRACT.md`](NEXT-PHASE-CONTRACT.md)  
Date: **2026-09-04**  
Dataset research: **held**

This addendum changes the next-phase dependency graph after D-02R option A and AMN-01 option A were accepted. It also inserts a D-03 event/state research program. Unchanged constraints in `NEXT-PHASE-CONTRACT.md` remain in force.

## 1. Released research edges

The following are no longer blocked by owner choice:

- `BR-FRAME` may test the Editorial Construction Space.
- `BR-DOM` may test the typed plural vocabulary and reduction attempts.
- `BR-AMN` may inspect and execute pinned Amnesia product evidence under `AMNESIA-ORACLE-AUTHORIZATION.md`.
- `BR-SEC` may continue in parallel.
- D-03 event/state reconnaissance and fixture design may begin.

These releases authorize research outputs only. They do not release implementation.

## 2. Remaining blocked edges

- `BR-PROSE` remains blocked by D-01P.
- paired-proof synthesis remains blocked until both technical and prose fixtures exist.
- `BR-REP` and `BR-HIST` may conduct reconnaissance, but no recommendation can pass before D-03 experiments narrow the authoritative primitive and temporal/order model.
- D-03R is not yet ready for owner decision.
- persistence ADR work, implementation, and dataset research remain blocked.

## 3. New program: BR-EVENT-STATE

| Field | Contract |
|---|---|
| Question | Can typed editorial occurrences and transactions evolve a multidimensional state without erasing enduring facts, exact artifact states, causal concurrency, or authority? |
| Inputs | accepted D-02R hypothesis, D-04B history guarantee, Amnesia seed refs, D-03 source ledger |
| Required output | formal candidate models, Amnesia trace, counterexamples, replay tests, temporal model, branch/merge tests, erasure analysis, recommendation packet |
| Must compare | pure event-first, fact/datom-first temporal ledger, event–fluent hybrid, checkpoint+journal |
| Must not select | backend, event store, database, serialization, reducer framework, or CRDT |
| Releases | revised D-03R packet; authoritative-primitive and order/time requirements for `BR-REP` and `BR-HIST` |

## 4. Revised dependency shape

```text
D-02R accepted
      │
      ├────────► BR-FRAME ─────► BR-DOM ───────────┐
      │                                             │
AMN-01 accepted ───────────────► BR-AMN ────────────┤
                                                    ▼
D-03 challenge ────────────────► BR-EVENT-STATE ─► D-03R
                                                    │
BR-SEC ─────────────────────────────────────────────┤
                                                    ▼
                                                  BR-REP
                                                    │
D-04B ──────────────────────────────────────────────┤
                                                    ▼
                                                  BR-HIST

D-01P ─► BR-PROSE ───────────────────────────────► paired proof
BR-AMN ──────────────────────────────────────────► paired proof
```

`BR-EVAL`, `BR-PRIORS`, paired synthesis, and `BR-INT-DD` retain the downstream positions defined in the original contract.

## 5. Required D-03 experiments

### E-01 — multidimensional atomic transition

One accepted event/transaction changes epistemic, normative, workflow, and release state together while preserving one identity and one causal act.

### E-02 — unaffected dimensions

The same transition leaves material source state unchanged. A separate source checkpoint event changes material state without inventing an editorial decision.

### E-03 — event versus fluent

Represent an occurrence, an enduring condition, its initiation/termination, and a later observation without treating them as the same record.

### E-04 — simultaneous roles

One finding participates in constructive, referential, and pragmatic/governance relations without being duplicated into competing copies.

### E-05 — branch and causal concurrency

Two reviewers or agents work from one parent state. Their events retain causal independence, conflict, and alternative outcomes before merge/adjudication.

### E-06 — late and retroactive knowledge

A product change is learned later than it occurred. The model preserves effective/valid time and observation/recording time.

### E-07 — replay versioning

Replay the same history under two reducer/schema versions. Historical state and revised interpretation must be distinguishable rather than silently rewritten.

### E-08 — external and nondeterministic evidence

A test, human review, or model grader produces an observation. Reproduction requirements preserve raw output, version, environment, uncertainty, and abstention.

### E-09 — erasure

A payload must be deleted or redacted while permissible event identity, authority, and causal links remain. The result must not claim exact replay where it is no longer possible.

### E-10 — checkpoint fidelity

Semantic replay cannot substitute for exact source bytes. Material checkpoints and deltas must bind content identity and declare any lossy projection.

## 6. D-03R gate

A D-03R packet may be issued only when:

1. all four candidate models are tested against E-01 through E-10;
2. the Amnesia mismatch and at least one correction episode are represented;
3. one unchanged-doc/product-change staleness case is represented;
4. one branch/merge disagreement is represented;
5. reducer/schema evolution and erasure failure modes are explicit;
6. the recommendation states which facts are canonical, which are observations, which outputs are derived, and what cannot be reconstructed;
7. migration and backend-exit requirements are stated without selecting a backend.

## 7. Controlling-document boundary

`BOOTSTRAP.md`, `ROADMAP.md`, `RESEARCH.md`, and the model-training-data charter must eventually be revised consistently. Until D-01P and D-03R are resolved, this addendum and the decision records carry the accepted interim authority.

## 8. Tracking constraint

Native Beads fan-out remains required but unavailable in the current runtime. No direct `.beads` or Dolt mutation is authorized.
