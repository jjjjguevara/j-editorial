# History and persistence — Charter

Slug: `history`  
Alias: `BR-HIST`  
Beads epic: `j-editorial-dta`  
Lifecycle: **BOOTSTRAP-SCOPED**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`  
Decisions relied on: `D-04` (paraphrased; "B for now")

## 1. Authority and status

No backend, event store, database, CRDT, or serialization is selected. The workload exists; no substrate experiment has run.

## 2. Mission

Determine which backend-neutral history model reconstructs `D-04B` episodes and checkpoints, and run the bake-off that any persistence decision must follow.

## 3. Why the program is separate

`BOOTSTRAP.md` section 13.8 and the Phase 1 review require workload experiments before any storage choice; this program owns them.

## 4. Decisions or specification questions it informs

`BOOTSTRAP.md` ADR queue items 22 to 29.

## 5. In scope / out of scope

In scope: the fifteen-step workload; acceptance metrics; export and backend-exit; recovery; erasure effectiveness; query cost.  
Out of scope: production deployment, hosting, tenancy.

## 6. Dependencies on other programs

Upstream: `representation`. Downstream: `evaluation`, `model-training-data` (held).

## 7. Hypotheses under attack

- H1. The event–fluent plus exact-checkpoint model is an adequate workload contract. Status: stated; untested against a substrate.
- H2. Composition of several substrate roles is likely. Status: hypothesis; composition risk untested.

## 8. Required current / SOTA reconnaissance

Git, Dolt, PostgreSQL logical decoding, Datomic, XTDB, event stores, Automerge, Yjs, DeltaDB are in the ledger. Re-date at execution; DeltaDB remains a comparator until an independently testable interface exists.

## 9. Required primary-source classes

Class 5.1 for substrate documentation; 5.5 for the bake-off; 5.3 for production practice.

## 10. Comparison set

Event ledger plus checkpoint store; temporal fact store plus transaction records; relational journal plus causal graph; checkpoint-first with a small semantic journal (control); a composition involving a CRDT or DeltaDB when testable.

## 11. Experiments or bake-offs

`HIST-G1`: run the fifteen-step workload in genuinely different candidate substrates with export, import, corruption recovery, redaction, and backend exit; report every hard requirement separately.

## 12. Representative workloads or fixtures

The workload in [`representation/REPRESENTATION-HISTORY-RESULT.md`](../representation/REPRESENTATION-HISTORY-RESULT.md) section 10 over both program fixtures.

## 13. Scale and budget analysis

Required by the charter template; not yet specified. Phase 3 JSON byte counts are not storage measurements.

## 14. Security, privacy, licensing, governance

Erasure effectiveness and residual data are hard requirements; licensing and long-term availability are acceptance metrics.

## 15. Interoperability and migration

The backend-exit contract must be demonstrated, not asserted.

## 16. Deliverables

Bake-off results per requirement; recommendation packet without an aggregate score.

## 17. Falsification criteria

A candidate is rejected if it fails any hard requirement in the acceptance list or cannot export the declared semantics without its own server.

## 18. Gate criteria

- `HIST-G1` `j-editorial-dta.1`: representation/history bake-off on the Phase 2 workload.

## 19. Downstream ADR or specification candidates

Persistence process or initial persistence ADR; Git interoperability boundary; object and analytical storage boundaries.

## 20. Residual risk and revisit policy

Beads' use of Dolt must not leak into the product decision; see `BOOTSTRAP.md` section 13.2.

## 21. Independence declaration

Workload and requirements share the author lineage of the other programs; nothing has been executed.
