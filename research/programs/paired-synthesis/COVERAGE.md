# Coverage matrix — paired proof

Rows are the cases the paired proof is accountable for. Columns name the fixture transactions, validator checks, or executed probes that exercise each case. "trivial" marks coverage that cannot fail as constructed; "doc-only" marks coverage present in prose but not in a fixture or executed check; "none" marks an uncovered case. An uncovered or trivial row blocks PASS for the gate that depends on it.

Compiled 2026-09-04 during the restructure from the fixtures, validators, and Phase 3 results. Nothing here is a new experiment.

## A. Shared minimum cases (next-phase contract, section 4)

| # | Case | Technical slice | Prose slice | Strength | Notes |
|---|---|---|---|---|---|
| 1 | Valid baseline with positive evidence | doc-only: positive findings listed in the oracle experiment section 4; the fixture's only finding is adverse | `finding:verification-boundary` polarity `qualified-positive`, `P-04` | partial | |
| 2 | Missing mandatory content | `finding:notes-signature` omits required `bookId`; `E-01` | none as "missing"; working-context finding is disputed, not missing | partial | |
| 3 | Present but contradictory content | async claim versus synchronous interface; `E-01` | none | partial | |
| 4 | Accepted exception or waiver | none | none | **none** | no transaction in either fixture contains a waiver |
| 5 | Uncertain or insufficient evidence | `evidence.uncertainty`, `abstentions`; `E-08` | `evidence_levels`, `P-04` | declarative | |
| 6 | Conflicting reviewer judgments | none | `tx:review-a`, `tx:review-b`; `P-07` | **trivial** | two strings written by the fixture author for synthetic actors |
| 7 | Target move, rewrite, delete | Phase 3 `T-reference-*` | Phase 3 `T-about-*`, `T-prose-*` | executed, bounded | literal Unicode-codepoint quote matching only; real label-removal history exercised once |
| 8 | Alternate valid resolution | three remedy proposals; `E-05` | three proposals; `P-06` | declarative | |
| 9 | Rule, goal, or evidence version change | reducer v1 and v2 projections; `E-07` | `P-11` | declarative | two projection records with different outputs, both author-written |
| 10 | Failed operation with no post-state | none | none | **none** | no failed operation in either fixture |
| 11 | Branch and merge disagreement | `tx:adjudicate` with three parents; `E-05` | `tx:defer-working-context`; `P-07`; Phase 3 `C-01` to `C-03` | declarative plus executed synthetic reducer probe | |
| 12 | Redacted payload with permissible audit metadata | `tx:redact`, `erasure`; `E-09` | `tx:redact-private-detail`; `P-09` | declarative | flags set by the author; Phase 3 `N-*` probes show logical deletion is not erasure in SQLite |
| 13 | Unsupported source construct or lossy projection | Phase 3 `T-opaque-inert` | same | **trivial** | a JSON round-trip of an opaque block |
| 14 | Hostile prompt-like text remains inert | Phase 3 `T-opaque-inert` | same | **trivial** | no agent or model was involved |

Abstention as a decision outcome, required by `BOOTSTRAP.md` section 18.2, appears only as `abstentions` lists inside evidence records; no transaction records an abstention.

## B. Stage 0 proof obligations (`ROADMAP.md` section 6)

| # | Obligation | Coverage | Strength |
|---|---|---|---|
| 1 | Document moving from incomplete draft to release candidate | prose checkpoints p0, p1, p2 and release projection `accepted-with-open-nonblockers` | partial; no lifecycle states |
| 2 | Missing citation later resolved with evidence | none | **none** |
| 3 | Factual claim contradicted by an authoritative source | technical docs versus pinned types | by reading; executed check pending `AMN-G1` |
| 4 | Stylistic finding that remains preference-based | `finding:decorative-labels`, project-scoped norm; `P-08` | declarative |
| 5 | Accepted edit later reverted | none | **none** |
| 6 | Edit resolves one gap while introducing another | none | **none** |
| 7 | Published document reopened by erratum | technical `tx:external-change` reopens; counterfactual | partial |
| 8 | Two valid alternate editorial resolutions | both slices | declarative |
| 9 | Reviewer disagreement requiring adjudication | prose synthetic reviewers | **trivial** |
| 10 | Agent detects a real issue but proposes a bad fix | none | **none** |
| 11 | Agent edits unnecessarily despite no valid finding | none | **none** |
| 12 | Deterministic technical-doc check | static comparison recorded as deterministic; performed by agent reading | mislabeled; pending `AMN-G1` |
| 13 | Artifact evaluated under two goal contracts | `P-11` goal v1 versus strict counterfactual | declarative |
| 14 | Policy rule whose applicability changes by audience or artifact type | norm scope declared portfolio-only | partial; no change case |
| 15 | Historical episode useful for eval without a unique correct answer | `P-03` `unique_gold_answer: false` | declarative |

## C. Consequences

- `PS-G1` must add cases A4, A10, and an abstention decision to both slices, and should add B2, B5, B6, B10, and B11 where a slice can support them.
- Rows marked trivial must be re-exercised with an agent or reader in the loop before they count.
- Declarative rows count for expressibility only; none of them can fail without an independent encoder.
