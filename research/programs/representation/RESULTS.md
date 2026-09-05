# representation — Results

Entries are dated and cite their packet. Verdicts use the vocabulary of `RESEARCH.md` section 3.

## 2026-09-04 — Phase 1: representation-authority decision packet

Packet: [`2026-09-04-phase-1-adversarial-review`](../../packets/2026-09-04-phase-1-adversarial-review/README.md), review section 6  
Verdict: PASS (argumentative) for stating three alternatives and their critical experiments; none executed.

## 2026-09-04 — Phase 2: representation and history requirements

Packet: [`2026-09-04-phase-2-foundations`](../../packets/2026-09-04-phase-2-foundations/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: none; red team: none

### What ran

Requirements for checkpoints, event transactions, fluents, projections, and target bundles; authority by question; named times; replay classes; schema evolution; erasure; backend-exit contract; bake-off workload. See [`REPRESENTATION-HISTORY-RESULT.md`](REPRESENTATION-HISTORY-RESULT.md).

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Logical requirements stated before any substrate choice | PASS (as specification) | result sections 2 to 8 |
| Reconciliation and round-trip experiments | DEFER (not executed) | |

## 2026-09-04 — Phase 3: targeting probes

Packet: [`2026-09-04-phase-3-behavioral-probes`](../../packets/2026-09-04-phase-3-behavioral-probes/README.md)  
Pre-registration: none  
Executed by: bootstrap agent session; validated by: CI and local reproduction; red team: none

### What ran

Fragment integrity checks, one real label-removal history case, one real rewrite case, and six constructed transformations per domain with quote and context matching (`T-*`). Reproduced on 2026-09-04.

### Gate decomposition

| Obligation | Verdict | Evidence |
|---|---|---|
| Raw offsets fail after real structural change; quotes recover | PASS (bounded) | `T-real-label-removal-*` |
| Rewrite produces `unresolved`, not a fabricated link | PASS (bounded) | `T-real-rewrite` |
| Constructed insert, move, duplicate, delete, rewrite, split behave as predicted | PASS (bounded; predictions written with the code) | `T-prose-*`, `T-reference-*` |
| Real syntax, AST, DOM, W3C selector conformance | DEFER (not executed) | packet results section 5 |

### Evidence retention

Fragment text is committed beside its SHA-256 in the manifest; this is the retention pattern the rest of the research should adopt.

## Open gates

`REP-G1`, tracked in Beads under epic `j-editorial-0te`.
