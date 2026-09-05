# Causal event–fluent editorial state — Charter

Slug: `event-state`  
Alias: `BR-EVENT-STATE`  
Beads epic: `j-editorial-t2j`  
Lifecycle: **ACTIVE**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`  
Decisions relied on: `D-03` challenge (verbatim), `D-03` acceptance (no preserved statement; recorded direction), `D-04` (paraphrased); see [`DECISION-LOG.md`](../../decisions/DECISION-LOG.md)

## 1. Authority and status

Logical research shape only. No event store, database, serialization, reducer framework, CRDT, or event-sourcing architecture is selected. The `D-03` acceptance record preserves no owner statement; until confirmed, this program works under the owner's verbatim instruction to research further before locking.

## 2. Mission

Test whether typed occurrences and atomic transactions can evolve a heterogeneous multidimensional editorial state while preserving time-scoped facts, exact material checkpoints, causal parentage with branch, conflict, and merge, and versioned projections; and compare the event-first, fact-first, event–fluent hybrid, and checkpoint+journal candidates.

## 3. Why the program is separate

It owns the answer to "what is canonical, what is observed, what is derived, and what cannot be reconstructed", which representation and history research must consume rather than decide.

## 4. Decisions or specification questions it informs

`BOOTSTRAP.md` ADR queue items 18, 19, 20, 21, and the later `D-03R` packet.

## 5. In scope / out of scope

In scope: events versus fluents; transactions; checkpoints; projections; causal order versus storage order; named times; replay classes; reducer evolution; erasure semantics.  
Out of scope: backend selection, physical topology, serialization, performance claims.

## 6. Dependencies on other programs

Upstream: `frame-domain`, `D-04B`. Downstream: `representation`, `history`.

## 7. Hypotheses under attack

- H1. One transaction can change several state dimensions atomically while leaving others unchanged. Status: shown by construction.
- H2. Occurrences and continuing conditions need distinct records. Status: argued; fixture fluents are author-declared.
- H3. The event–fluent hybrid is preferable to the other three candidates. Status: unsupported; Phase 3 showed the four encodings are informationally equivalent on the available fixtures, so the fixtures cannot discriminate between them.

## 8. Required current / SOTA reconnaissance

Re-date the state-machine, event-calculus, causal-order, temporal-database, and event-sourcing sources in the ledger at execution. Add at least one production system that combines checkpoints with a semantic journal.

## 9. Required primary-source classes

Class 5.1 (SCXML, Datomic and XTDB documentation, event-sourcing guidance), 5.2 (Moore, Harel, Kowalski and Sergot, Lamport, Winskel, Shapiro et al.), 5.5 for the discriminating workload once it runs.

## 10. Comparison set

Pure event-first; temporal fact/datom-first; event–fluent hybrid with causal DAG; checkpoint plus semantic journal as the simplicity control.

## 11. Experiments or bake-offs

`ES-G1`: a discriminating workload of queries the candidates should answer differently, implemented in genuinely different substrates rather than one interpreter. Candidate queries: what held at time t under knowledge as of a later time; which branch's disposition is visible at a head; replay after payload erasure; reducer version two over history recorded under version one. If the candidates still tie, the preference is dropped.

## 12. Representative workloads or fixtures

[`fixtures/amnesia-notes-event-fluent.json`](fixtures/amnesia-notes-event-fluent.json), 13 transactions, hash-pinned; the prose fixture in `prose/`; the fifteen-step workload in [`representation/REPRESENTATION-HISTORY-RESULT.md`](../representation/REPRESENTATION-HISTORY-RESULT.md) section 10.

## 13. Scale and budget analysis

Not yet specified. Phase 3 byte counts measure JSON nesting only and must not be cited as storage cost.

## 14. Security, privacy, licensing, governance

Erasure must be representable as declared replay loss; see `security/`.

## 15. Interoperability and migration

Backend-exit contract in the representation result, section 8; export must be readable without the originating server.

## 16. Deliverables

Formal candidate models; discriminating workload results; replay-class contract; `D-03R` decision packet.

## 17. Falsification criteria

From [`EVENT-FLUENT-EXPERIMENT.md`](EVENT-FLUENT-EXPERIMENT.md) section 9 and the sixteen tests in [`D-03-EVENT-STATE-REVIEW.md`](D-03-EVENT-STATE-REVIEW.md) section 14. Added 2026-09-04: the hybrid is rejected as favored if `ES-G1` shows no query on which it outperforms checkpoint plus journal.

## 18. Gate criteria

- `ES-G1` `j-editorial-t2j.1`: discriminating workload across candidate models.
- `ES-G2` `j-editorial-t2j.2`: `D-03R` decision packet, issued only after `ES-G1` and `HIST-G1`.

## 19. Downstream ADR or specification candidates

Semantic-event model; snapshot/checkpoint semantics; exact versus semantic reconstruction guarantees.

## 20. Residual risk and revisit policy

The event-stream analogy may be attractive rather than necessary. Revisit after `ES-G1`.

## 21. Independence declaration

Review, fixture, validator, and Phase 3 probes share one author lineage. Phase 3 red-teamed the Phase 2 validator and found four blind spots; no red team has attacked the model itself.
