# General-prose proof on the portfolio About page — Charter

Slug: `prose`  
Alias: `BR-PROSE`  
Beads epic: `j-editorial-cz0`  
Lifecycle: **ACTIVE**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`  
Decisions relied on: `D-01P` (verbatim); scope record [`D-01P-ACCEPTANCE.md`](../../decisions/D-01P-ACCEPTANCE.md)

## 1. Authority and status

Research fixture on one public page at one immutable revision. No portfolio mutation, deployment, external disclosure, or dataset use. ACTIVE on representation evidence only.

## 2. Mission

Represent a real general-prose artifact whose obligations include factual consistency, rhetoric, structure, audience fitness, privacy, and several defensible resolutions, without converting historical acceptance, synthetic review, or internal consistency into truth.

## 3. Why the program is separate

It is the counterweight that keeps the framework from overfitting to technical documentation.

## 4. Decisions or specification questions it informs

Generality of the vocabulary; grader allocation for subjective obligations; disclosure versus truth; `BOOTSTRAP.md` ADR queue items 7, 13, 32, 33.

## 5. In scope / out of scope

In scope: `jjjjguevara/sci-jjjjguevara/src/pages/about.astro` at commit `1c93b60e75ce60203295a988b8125d44e6acb6bc`, blob `d56c560fc63569b471cc4e81a65daf52568fe754`, its two earlier checkpoints, and the supporting brief, profile, résumé, ledger, and validator records as evidence or norms.  
Out of scope: other pages, Field Notes, private records, independent biographical verification, employability judgments.

## 6. Dependencies on other programs

Upstream: `D-01P`. Downstream: `paired-synthesis`, `evaluation`, `goal-priors`.

## 7. Hypotheses under attack

- H1. The vocabulary represents prose obligations without a prose-specific canonical model. Status: shown by construction on one same-owner artifact.
- H2. Disagreement can remain inspectable state. Status: exercised only with two synthetic reviewer strings written by the fixture author.
- H3. Truth or support is independent of disclosure permission. Status: represented; not tested against a real disclosure decision.

## 8. Required current / SOTA reconnaissance

Human-evaluation methodology sources in the ledger must be re-dated; add reader-study protocols from a production documentation or newsroom context at execution.

## 9. Required primary-source classes

Class 5.4 (pinned repository states), 5.6 (human readers and adjudication, none yet), 5.2 (evaluation methodology).

## 10. Comparison set

Exact-match grading against the accepted text (rejected); rubric scoring; reader task completion; pairwise preference.

## 11. Experiments or bake-offs

`PR-G1` build parity at the pinned ref with deployment disabled, comparing visible text and heading structure to the fixture projection. `PR-G2` a recruited reader-task pilot under a pre-registered protocol; synthetic scenarios do not satisfy it.

## 12. Representative workloads or fixtures

[`fixtures/portfolio-about-event-fluent.json`](fixtures/portfolio-about-event-fluent.json), 22 transactions, hash-pinned; the three About fragments in `representation/fixtures/`.

## 13. Scale and budget analysis

Not yet specified; a reader pilot needs a participant budget and consent boundary before recruitment.

## 14. Security, privacy, licensing, governance

Only details already present on the pinned public page; redacted synthetic placeholders for private-detail scenarios; the owner alone authorizes disclosure and release.

## 15. Interoperability and migration

Astro source mixes prose and markup; the evaluated projection is visible text and semantic heading/list structure.

## 16. Deliverables

Rights and purpose packet; fixture; review protocol; alternative resolutions; build-parity report; reader-pilot report.

## 17. Falsification criteria

From [`PORTFOLIO-PROSE-EXPERIMENT.md`](PORTFOLIO-PROSE-EXPERIMENT.md) and the paired result: prose judgments require identities the model cannot express without ad hoc exceptions; real readers' disagreement cannot be represented as state; a build or live response contradicts the pinned projection and the framework cannot record the mismatch as a finding.

## 18. Gate criteria

- `PR-G1` `j-editorial-cz0.1`: portfolio build parity at the pinned ref.
- `PR-G2` `j-editorial-cz0.2`: empirical reader-task pilot.

## 19. Downstream ADR or specification candidates

Grader taxonomy for subjective obligations; disclosure/authority model.

## 20. Residual risk and revisit policy

The subject, author, editor, reviewer authority, and research sponsor are one person; the slice tests representation, not adversarial editorial judgment. Revisit when a second, independently owned prose artifact is available.

## 21. Independence declaration

Audit, fixture, validator, and result share one author lineage; reviewer disagreement is synthetic. The 2026-09-04 review independently verified the pinned refs and history in a local clone.
