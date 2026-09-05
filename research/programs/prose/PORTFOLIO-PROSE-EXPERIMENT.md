# Portfolio About-page prose experiment

Status: **representation fixture passed / empirical prose evaluation open**  
Program: `BR-PROSE`  
Acceptance: [`D-01P-ACCEPTANCE.md`](../../decisions/D-01P-ACCEPTANCE.md)  
Fixture: [`fixtures/portfolio-about-event-fluent.json`](fixtures/portfolio-about-event-fluent.json)  
Validator: [`tools/validate_portfolio_prose_fixture.py`](tools/validate_portfolio_prose_fixture.py)  
Result: [`results/portfolio-about-event-fluent-validation.json`](results/portfolio-about-event-fluent-validation.json)  
Dataset research: **not executed**

## 1. Question

Can the Phase 2 event–fluent, exact-checkpoint, causal-history, and versioned-projection model represent a real general-prose artifact whose editorial obligations include factual consistency, rhetoric, structure, audience fitness, privacy, and several defensible resolutions—without converting historical acceptance, synthetic review, or internal consistency into universal truth?

## 2. Method

The experiment binds the accepted `/about` target and two earlier real checkpoints:

| State | Commit | About blob | Role |
|---|---|---|---|
| `about:p0-pre-audit` | `f66fa3d1b6c7b03ece46eb2f20d9089a51f02e2a` | `e11905e3db4591301c9bb17bed5a50490ba5bffb` | Before the prose audit |
| `about:p1-prose-audit` | `900483708d74e83c5f4acd3b308127f7fa430117` | `5d3d5007a6d2af82d8526e5862e87ec9dd239b26` | Accepted semantic/rhetorical rewrite |
| `about:p2-target` | `1c93b60e75ce60203295a988b8125d44e6acb6bc` | `d56c560fc63569b471cc4e81a65daf52568fe754` | Accepted target after structural simplification |

The fixture represents two distinct observed operation families:

1. **semantic/rhetorical rewrite** — vague career positioning, self-interpretive framing, and project-disfavored contrasts were replaced under the approved writing brief;
2. **structural/presentational simplification** — redundant eyebrow and section-index labels were removed while the biography and heading hierarchy remained.

Both operations are recorded as accepted into owner-controlled history. Neither is marked as a unique gold answer.

The current state is then tested against four additional concerns:

- owner-attested/internal-consistency evidence must not become independent substantiation;
- working-context sufficiency can remain a disputed, non-blocking finding;
- three different remedies may remain potentially acceptable;
- privacy can require rejection and erasure even when the truth status of a proposed detail is unknown.

A final counterfactual changes the profile referent while leaving the About checkpoint unchanged. It tests whether the current-state projection can become stale without falsely recording an About-page edit.

## 3. Fixture contents

```text
sources:       9
actors:        5
findings:      5
transactions: 22
fluents:       6
projections:   5
```

The actors separate owner authority, research observation, deterministic checking, and two synthetic professional-reader scenarios. Only the owner has release and disclosure authority.

The findings cover:

- pre-audit rhetorical problems supported by real history;
- project-scoped decorative-label treatment supported by real history;
- disputed working-context sufficiency;
- qualified owner-attested/internal-consistency evidence;
- a synthetic stale-profile scenario.

## 4. Multiple defensible resolutions

The working-context finding has no exact-match target. The fixture retains three proposals:

- retain concise summaries and let project pages carry detailed evidence;
- add one or two compact decision episodes;
- retain the summaries and link them to public decision evidence.

Each proposal includes conditions under which it could be acceptable. Two synthetic reader observations disagree. The owner decision is represented as deferred, and the unresolved finding remains non-blocking under `goal:portfolio-about-v1`.

This tests a required distinction: disagreement is state, not noise to average away. An eval can record reviewer rationale and authority without pretending that a mean score resolves the editorial question.

## 5. Evidence and privacy behavior

The evidence projection reports:

```text
source state:               established
internal consistency:       established
independent substantiation: not established
```

The private-detail branch contains only `[REDACTED_FIXTURE_PLACEHOLDER]`. It explicitly asserts no real personal detail. The proposal begins with unknown truth status and no disclosure permission; the owner rejects disclosure without claiming the detail false. The retention event removes the payload while retaining the existence and disposition of the proposal, so exact replay becomes impossible and the loss is explicit.

## 6. Validation obligations

| Check | Requirement | Result |
|---|---|---|
| `P-01` | Exact single-page, research-only, public-data boundary | passed |
| `P-02` | Pinned real checkpoint chain and accepted target identity | passed |
| `P-03` | Two distinct real operation families; no unique-gold claim | passed |
| `P-04` | Source/internal evidence cannot be upgraded to independent verification | passed |
| `P-05` | One disputed prose finding crosses axes, roles, and state dimensions | passed |
| `P-06` | Three potentially acceptable remedies; no exact-match gold | passed |
| `P-07` | Conflicting synthetic observations remain unresolved by authority | passed |
| `P-08` | Style evidence remains project-scoped and exception-bearing | passed |
| `P-09` | Truth/support, disclosure permission, rejection, and erasure remain distinct | passed |
| `P-10` | Counterfactual external fact change can stale an unchanged artifact | passed |
| `P-11` | Different goal/reducer versions can derive different readiness at one state | passed |
| `P-12` | Observation, review, disclosure, and release authorities remain separate | passed |

## 7. Deterministic result

```text
status:                    pass
input_file_sha256:         9c24cf03065f69aacaed4375c9830feeec0a78c8277e3a07c0b8f299147b4eb2
canonical_research_sha256: 74e0e3282596fd7ade8607c9a0ef40b82e096ad98840e157407e0c6b972f012e
```

The canonical research digest uses Python sorted-key compact JSON. It is not an RFC 8785/JCS claim.

## 8. Interpretation

The experiment supports the claim that the Phase 2 logical vocabulary can represent this general-prose history and its unresolved judgments without adding a prose-specific canonical state model.

It also forces refinements that the technical-reference slice alone did not require:

- truth/support and permission to disclose are separate;
- project norms require scope, precedence, and exception authority;
- non-blocking disagreement can remain open after release acceptance;
- historical acceptance is an authority-bearing event, not proof of a unique correct string;
- a reader observation is evidence about an evaluation event, not release authority;
- goal/reducer changes can change a readiness projection without rewriting history.

## 9. Limitations

This result does not establish:

- that the current About prose is globally or optimally good;
- that recruiters or technical readers complete a real task successfully;
- that either synthetic reviewer resembles a calibrated human population;
- that a model judge is reliable;
- that the public live route matches the pinned source;
- that the Astro build or accessibility checks passed in this environment;
- that owner-attested biography is independently substantiated;
- that the fixture schema should become a production schema;
- that a storage substrate has been selected;
- that this material is eligible for training or benchmark-corpus use.

## 10. Result

`BR-PROSE` passes its **representation adequacy** sub-gate with the stated constraints. Empirical reader-task design, human/model grader calibration, built-output equivalence, and independent-evidence policy remain downstream evaluation-science questions.
