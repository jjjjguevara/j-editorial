# Editorial Construction Space and typed domain distinctions — Charter

Slug: `frame-domain`  
Alias: `BR-FRAME` / `BR-DOM`  
Beads epic: `j-editorial-4lk`  
Lifecycle: **ACTIVE**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`  
Decisions relied on: `D-02R` (verbatim), `D-02` (paraphrased); see [`DECISION-LOG.md`](../../decisions/DECISION-LOG.md)

## 1. Authority and status

Research hypothesis only. Nothing in this program is an ontology, schema, class hierarchy, serialization, or store decision. The program is ACTIVE because fixtures exist; it is not READY for a decision packet because no independent material has been encoded.

## 2. Mission

Test two claims together: that the three-axis Editorial Construction Space, translated from Gustavo Bueno's gnoseological space, works as a completeness scaffold that exposes omitted operations, referents, actors, dialogue, and norms; and that a typed plural record vocabulary preserves distinctions that any single root such as `Gap`, `Finding`, `Obligation`, or `Event` would erase.

## 3. Why the program is separate

It decides the vocabulary every other program uses. Without it, representation, history, evaluation, and goal/prior research each invent their own terms.

## 4. Decisions or specification questions it informs

`BOOTSTRAP.md` ADR queue items 1, 5, 6, 8, 10, and 11, and two review exit criteria in section 27: an accepted or explicitly provisional domain glossary, and a resolved boundary between artifact state, gaps/findings/obligations, priors, evidence, and operations.

## 5. In scope / out of scope

In scope: the analytic axes; the typed distinctions; reduction attempts; `Gap` as a derived projection; cross-slice falsification; the glossary.  
Out of scope: persistence, serialization, class design, event-store choice, any model-training use.

## 6. Dependencies on other programs

Upstream: `D-02R`. Downstream: `goal-priors`, `representation`, `evaluation`, `paired-synthesis`.

## 7. Hypotheses under attack

- H1. The three axes are non-exclusive coordinates and expose omissions in an editorial model. Status: never triggered; no omission has been found by the scaffold.
- H2. The fourteen record families listed in [`FRAME-DOMAIN-RESULT.md`](FRAME-DOMAIN-RESULT.md) section 5 are irreducible for representative cases. Status: shown by construction on two same-owner artifacts written by the hypothesis author.
- H3. `Gap` is derivable as an unresolved adverse finding or an unsatisfied applicable obligation. Status: defined; not exercised against a case where obligation and finding coincide.

## 8. Required current / SOTA reconnaissance

The comparative model set inspected in Phase 1.1 (PROV, Web Annotation, SHACL, ODRL, TEI, IFLA LRM/LRMoo, CIDOC CRM, Records in Contexts, nanopublications, IBIS/AIF, RO-Crate) must be re-dated at the next execution and extended with at least one editorial or review-workflow model in production use that was not chosen by this repository's agents.

## 9. Required primary-source classes

Class 5.1 for standards; 5.2 for annotation and agreement studies; 5.4 for Doc Doctor and Amnesia observations; 5.6 for expert adjudication, of which none exists yet. Cite `SRC-###` identifiers from [`LEDGER.md`](../../LEDGER.md).

## 10. Comparison set

Single-root `Gap`; obligation/finding-centered; event-centered; typed pluralism (favored); and the minimal control, plain Git history plus review comments.

## 11. Experiments or bake-offs

`FD-G1` adversarial encoding, pre-registered: a session without access to the design rationale encodes an independently chosen real editorial history in the vocabulary and records ad hoc fields, unrepresentable cases, and collapsed distinctions. Control: encode the same history in the minimal control representation and list the queries each cannot answer.

## 12. Representative workloads or fixtures

Existing: the `event-state` and `prose` fixtures, both hand-authored by the hypothesis author. Required: at least one history chosen by the red team, not the author; candidates are a Doc Doctor or `amnesia-docs` commit range.

## 13. Scale and budget analysis

Not yet specified.

## 14. Security, privacy, licensing, governance

Bueno's texts are cited, never reproduced. Any independent history needs its rights recorded in the ledger before encoding.

## 15. Interoperability and migration

Distinctions must map to PROV and Web Annotation terms where they overlap. The mapping table is not yet written.

## 16. Deliverables

Glossary; distinction-survival table with per-case evidence; rejected reductions with counterexamples; the `FD-G1` report.

## 17. Falsification criteria

Stated in [`D-02-ACCEPTANCE.md`](../../decisions/D-02-ACCEPTANCE.md) before the Phase 2 fixture was authored, which makes them the only partially pre-registered criteria in the bootstrap: distinctions cannot be applied consistently across technical reference and prose; cross-axis classification produces uncontrolled ambiguity; one datum cannot retain simultaneous dimensions without duplication; the vocabulary adds types that never change evaluation, authority, history, or action; a smaller model preserves all required counterexamples; event/state representation forces loss of exact source fidelity; disagreement, uncertainty, waiver, or branch divergence collapses into one truth value.

Added 2026-09-04: the scaffold is rejected as an analytic instrument if `FD-G1` finds no omission that a flat checklist would not also have found.

## 18. Gate criteria

- `FD-G1` `j-editorial-4lk.1`: broader falsification on independent material under a pre-registered protocol.
- `FD-G2` `j-editorial-4lk.2`: accepted domain glossary.

PASS on either requires a pre-registration, an independence declaration, and a red-team pass.

## 19. Downstream ADR or specification candidates

Domain glossary; `Gap` as projection; the finding, obligation, and evidence relation model.

## 20. Residual risk and revisit policy

The vocabulary may be a relabeling with no analytic yield. Revisit after `FD-G1`.

## 21. Independence declaration

The D-02 review, both fixtures, both validators, and the results were authored by the same agent lineage within one day. No red-team pass has run. The 2026-09-04 review was the first independent reading of the material.
