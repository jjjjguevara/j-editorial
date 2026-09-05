# history — Results

Entries are dated and cite their packet. Verdicts use the vocabulary of `RESEARCH.md` section 3.

## 2026-09-04 — Phase 1: history-guarantee decision packet

Packet: [`2026-09-04-phase-1-adversarial-review`](../../packets/2026-09-04-phase-1-adversarial-review/README.md), review section 7  
Verdict: PASS (argumentative) for separating the minimum guarantee from the backend; `D-04B` recorded as a paraphrased owner direction.

## 2026-09-04 — Phase 2: workload, acceptance metrics, backend-exit contract

Packet: [`2026-09-04-phase-2-foundations`](../../packets/2026-09-04-phase-2-foundations/README.md)  
Where: [`representation/REPRESENTATION-HISTORY-RESULT.md`](../representation/REPRESENTATION-HISTORY-RESULT.md) sections 8 to 12

| Obligation | Verdict | Evidence |
|---|---|---|
| Workload and acceptance metrics defined | PASS (as specification) | sections 10 and 11 |
| Substrate roles compared | NARROW | a table of roles and burdens, no measurement |
| Bake-off | DEFER (not executed) | |
| Preference among options A to E | RETURN-WITH-FINDINGS | stated as "appear most capable" without executed evidence |

## 2026-09-04 — Phase 3: native Git and SQLite probes

Packet: [`2026-09-04-phase-3-behavioral-probes`](../../packets/2026-09-04-phase-3-behavioral-probes/README.md)  
Reproduced locally on 2026-09-04.

| Obligation | Verdict | Evidence |
|---|---|---|
| Git object fidelity and single-ref compare-and-swap | PASS (bounded) | `N-git-*` |
| Interrupted SQLite transaction exposes no partial rows | PASS (bounded to process exit) | `N-sqlite-interrupted-transaction` |
| Logical deletion is not erasure; VACUUM clears the current file only | PASS (bounded) | `N-logical-delete-not-erasure`, `N-vacuum-sentinel-scan` |
| Tamper detection on sealed export | PASS (trivial) | `N-tamper-detection` |
| Anything about Dolt, PostgreSQL, temporal stores, CRDTs, or DeltaDB | DEFER (not executed) | |

## Open gates

`HIST-G1`, tracked in Beads under epic `j-editorial-dta`.
