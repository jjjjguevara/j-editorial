# Representation, targeting, and authority — Charter

Slug: `representation`  
Alias: `BR-REP`  
Beads epic: `j-editorial-0te`  
Lifecycle: **ACTIVE**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`

## 1. Authority and status

Requirements and bounded probes only. Source-first, structured-first, and composed representations remain open alternatives; no canonical document model is selected.

## 2. Mission

Determine which authority model meets fidelity, identity, targeting, partial-update, and reconciliation requirements, and how targets survive real edits.

## 3. Why the program is separate

Representation decisions carry the highest lock-in in the queue; they must follow executed evidence on real syntax.

## 4. Decisions or specification questions it informs

`BOOTSTRAP.md` ADR queue items 1, 2, 3, 4, and 50.

## 5. In scope / out of scope

In scope: material checkpoints; target and selector bundles; resolution outcomes; correspondence across rewrites; round-trip fidelity; authority by concern.  
Out of scope: persistence engine selection (`history`).

## 6. Dependencies on other programs

Upstream: `frame-domain`, `goal-priors`, `security`, `event-state`. Downstream: `history`.

## 7. Hypotheses under attack

- H1. No single selector works across every representation and edit pattern. Status: supported by literature and by bounded probes.
- H2. Textual matching cannot justify semantic continuity across rewriting. Status: supported by bounded probes; abstention is the correct output.
- H3. Authority by concern does not require three stores or a structured-first canonical document. Status: argued; untested on real syntax.

## 8. Required current / SOTA reconnaissance

Web Annotation selectors, ProseMirror mapping, Tree-sitter incremental parsing, Yjs and Automerge positions are in the ledger; add an AST-diff and a DOM-visibility tool comparison at execution.

## 9. Required primary-source classes

Class 5.1 for selector and editor-model documentation; 5.5 for executed targeting probes.

## 10. Comparison set

Raw offsets; text quote with context; structural path; symbolic identifier; parser node identity; CRDT relative position; explicit correspondence record.

## 11. Experiments or bake-offs

`REP-G1`: targeting on real syntax with AST and DOM coordinates over real commit ranges; explicit correspondence records for split, merge, and rewrite; measured ambiguity and unresolved rates.

## 12. Representative workloads or fixtures

[`fixtures/target-fragments.json`](fixtures/target-fragments.json) with four pinned fragments and committed text beside digests; the fifteen-step workload in [`REPRESENTATION-HISTORY-RESULT.md`](REPRESENTATION-HISTORY-RESULT.md) section 10.

## 13. Scale and budget analysis

Not yet specified.

## 14. Security, privacy, licensing, governance

Text quotes may carry personal data; the fragment manifest limits itself to public About text and one public API page.

## 15. Interoperability and migration

Backend-exit contract, result section 8.

## 16. Deliverables

Authority model; selector bundle contract; replay-class contract; targeting evidence on real syntax.

## 17. Falsification criteria

Rejected or narrowed if real target movement causes systematic identity duplication, if exact checkpoints cannot be exported without lock-in, or if literal matching is the only available continuity mechanism.

## 18. Gate criteria

- `REP-G1` `j-editorial-0te.1`: real syntax, AST, DOM targeting and correspondence evidence.

## 19. Downstream ADR or specification candidates

Canonical editorial-state boundary; stable identity and anchor guarantees; import/export round-trip guarantees.

## 20. Residual risk and revisit policy

Probes so far operate on literal Unicode code points, not W3C selector conformance or DOM visibility.

## 21. Independence declaration

Requirements and probes share one author lineage; the fragment manifest is the one artifact whose bytes are committed beside their digests.
