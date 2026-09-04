# Bootstrap next-phase contract

Status: **proposed / blocked by owner decisions D-01 through D-04**  
Authority: subordinate to `BOOTSTRAP.md` and explicit owner answers  
Dataset research: held

This document describes how bootstrap should continue after the pivotal choices are resolved. It is not a task tracker, an ADR, or implementation authorization.

## 1. Controlling-document revision

The first post-decision change should revise all controlling documents together so their terms and gates remain consistent.

| Document | Required revision |
|---|---|
| `BOOTSTRAP.md` | Record accepted first proof, semantic center, representation authority question, history guarantee, refined invariants, and explicit remaining unknowns |
| `ROADMAP.md` | Replace generic Stage 0 with the chosen vertical slice and early generalization gate; make history/collaboration scope explicit |
| `RESEARCH.md` | Register non-dataset research programs, normalize result/gate terminology, add decision-packet requirements used in phase 1 |
| `research/model-training-data/CHARTER.md` | Scope-only revision: align terminology and dependencies; keep status held and prohibit execution |
| `research/bootstrap/*` | Record owner answers verbatim and update status from owner-decision hold to phase-2 active |

No document should state that the chosen option is already validated. Owner selection narrows the research target; it does not substitute for evidence or experiments.

## 2. Proposed non-dataset research programs

Program identifiers below are provisional planning labels, not Beads IDs.

| Program | Question | Required output | Releases |
|---|---|---|---|
| `BR-DOM` — domain semantics | Do Obligation, Finding/Gap, Evidence, Operation, Verification, and Release cover the chosen scenarios without contradiction? | glossary, relationship model, counterexamples, first-slice semantics, migration mapping from Doc Doctor | representation and eval fixture finalization |
| `BR-GOAL` — goal contracts | How are purpose, audience, scope, obligations, waivers, and release policy expressed and versioned? | contract requirements, decomposition rules, ambiguity handling, examples/non-examples | first end-to-end scenario |
| `BR-REP` — artifact representation | Which source/semantic authority model meets fidelity, identity, addressing, partial-update, and extension requirements? | fixtures, round-trip/reconciliation experiments, target-resolution tests, recommendation packet | persistence workload and import/export contract |
| `BR-HIST` — history and persistence | Which history model can reconstruct accepted states and operations at required granularity? | workload, Git/Dolt/PostgreSQL/operation-log comparison, failure/recovery tests, recommendation packet | persistence ADR candidate |
| `BR-EVAL` — evaluation science | Which objective, human, and model grader contracts produce valid obligation-level evidence? | eval-instance contract, grader taxonomy, calibration/meta-eval protocol, reporting contract | benchmark/eval ADR candidates |
| `BR-PRIORS` — normative priors | How are guides/rules represented, scoped, licensed, versioned, conflicted, and applied? | prior contract, rule provenance, conflict/precedence cases, adapter requirements | first policy pack |
| `BR-SEC` — security/privacy | What trust boundaries, authorization, erasure, retention, and external-provider controls are required? | threat model, data-flow categories, operation authority matrix, deletion/redaction tests | safe agent/integration design |
| `BR-INT-DD` — Doc Doctor migration | How can current stubs/refinement/history import without becoming normative core semantics? | mapping, incompatibility ledger, fixture exporter, migration/rollback plan | Doc Doctor reference integration |

The model-training dataset program remains `PLACEHOLDER / PRE-BOOTSTRAP` or an equivalent held status. It may depend on accepted outputs from `BR-DOM`, `BR-GOAL`, `BR-REP`, `BR-HIST`, `BR-EVAL`, `BR-PRIORS`, and `BR-SEC`; it must not run as part of this bootstrap session.

## 3. Dependency shape

```text
owner decisions D-01..D-04
          │
          ▼
controlling-document revision
          │
          ├──────────────┬──────────────┐
          ▼              ▼              ▼
       BR-DOM         BR-GOAL         BR-SEC
          │              │              │
          └──────┬───────┘              │
                 ▼                      │
               BR-REP ◄─────────────────┘
                 │
                 ▼
               BR-HIST
                 │
          ┌──────┴──────┐
          ▼             ▼
       BR-EVAL       BR-PRIORS
          │             │
          └──────┬──────┘
                 ▼
          first-slice synthesis
                 │
                 ▼
             BR-INT-DD
                 │
                 ▼
       bootstrap adversarial gate
```

Some reconnaissance may run in parallel, but recommendations must honor upstream semantics.

## 4. Required experiment fixtures

The chosen first-slice program should create a small **evaluation fixture set**, not a model-training dataset.

Minimum cases:

1. a valid baseline artifact and goal contract;
2. a missing mandatory unit;
3. a structurally present but factually inconsistent unit;
4. a valid exception/waiver;
5. a positive finding and supporting evidence;
6. contradictory reviewer judgments;
7. a target moved/rephrased across states;
8. two branches with conflicting resolutions;
9. a rule/prior version change;
10. an erased/redacted payload with retained permissible audit metadata;
11. a source extension unsupported by the semantic projection;
12. hostile prompt-like content that must remain inert.

These fixtures exist to falsify architecture and eval assumptions. They are outside the held training-dataset research program and must not be represented as a reusable corpus.

## 5. Decision-packet gate for each program

Every material program must produce:

1. problem and decision boundary;
2. challenged assumptions;
3. credible alternatives;
4. current primary sources and versions;
5. representative experiment;
6. raw results and reproduction instructions;
7. failure modes;
8. reversibility and migration cost;
9. security/privacy/licensing impact;
10. acceptance and falsification criteria;
11. objections and negative evidence;
12. recommendation: `accept`, `narrow`, `defer`, `reject`, or `research further`;
13. unresolved owner questions;
14. proposed ADR/specification changes only after review.

A feature table alone cannot pass a program gate.

## 6. Persistence bake-off requirements

No persistence candidate should be selected until `BR-DOM`, `BR-GOAL`, and the representation requirements are stable enough to produce a workload.

The bake-off must test, at minimum:

- exact reconstruction of source checkpoints;
- reconstruction of semantic state from accepted operations;
- branch creation and merge conflict representation;
- target identity across move/rewrite/delete;
- prior/goal version changes;
- provenance queries from outcome back to evidence and actor;
- partial erasure/redaction;
- corruption and interrupted-write recovery;
- deterministic export/import;
- query cost for artifact-, obligation-, finding-, and episode-level histories;
- migration/export without the selected backend.

DeltaDB remains an inspiration/comparator unless a stable, accessible interface and suitable licensing/deployment contract emerge. Git, Dolt, PostgreSQL, and operation-log/CRDT approaches remain candidates, not defaults.

## 7. Evaluation bake-off requirements

`BR-EVAL` must distinguish:

- construct validity: does the measure represent the intended obligation?
- correctness: does the grader label known cases correctly?
- reliability: does it reproduce results under controlled repetition?
- robustness: does irrelevant wording/order/style change the result?
- calibration: do confidence values match observed error?
- disagreement: how are reviewer/model conflicts preserved?
- abstention: can the grader state that evidence is insufficient?
- leakage: did the grader or model have access to the answer/history?
- cost and latency;
- release-policy impact.

At least one adversarial meta-eval must test any model grader before it can contribute to a release gate.

## 8. Security and authority gate

Before an agent can execute consequential editorial operations, `BR-SEC` must define an authority matrix for:

- read artifact/history;
- retrieve external evidence;
- install or change a prior/rule;
- propose an operation;
- apply an operation to a working state;
- accept/reject a proposal;
- publish/release;
- disclose/export;
- delete/redact;
- change retention;
- send content to an external model/provider.

Imported artifact content cannot grant these permissions.

## 9. Native Beads fan-out

The repository contract requires Beads for durable work tracking. Phase 1 did not create native work records because the execution environment lacked `bd` and `dolt`, while the repository is configured for Dolt-backed synchronization. Direct `.beads` edits are prohibited.

When a compatible environment is available, the first native tracking operation should:

1. run `bd prime`;
2. inspect existing records with `bd ready` and `bd list`;
3. create one bootstrap epic and program-level children matching the accepted fan-out;
4. encode dependencies from Section 3;
5. mark the dataset program held/dependent rather than ready;
6. link this phase-1 review branch/PR and base SHA;
7. push the Dolt remote with `bd dolt push`.

No Markdown checkbox list or GitHub Issue should be treated as the replacement source of truth.

## 10. Bootstrap exit-readiness matrix

| Obligation | Phase-1 status | What remains |
|---|---|---|
| Mission/non-goals/boundaries | **partially supported** | revise after D-01 |
| Glossary/domain semantics | **challenged, not accepted** | D-02 + `BR-DOM` |
| Goal-contract slice | **candidate identified** | D-01 + `BR-GOAL` |
| Representation/history requirements | **alternatives established** | D-03/D-04 + experiments |
| Persistence decision process | **defined** | execute `BR-HIST`; no backend choice yet |
| Version/provenance contract | **strong priors identified** | domain-specific specification |
| First ontology slice | **candidate identified** | owner choice + counterexample review |
| Eval-instance contract | **candidate identified** | `BR-EVAL` validation |
| Security/privacy/contamination | **baseline findings** | threat model and tests |
| Narrow end-to-end use case | **owner decision required** | D-01 |
| Research program graph | **proposed** | authoritative revision + native Beads records |
| Dataset research | **held as required** | different session after dependencies |
| Implementation authorization | **not granted** | full bootstrap adversarial pass + explicit owner release |

## 11. Stop conditions for phase 2

Phase 2 must halt again when:

- owner answers conflict with an existing invariant;
- a goal or obligation cannot be made testable without product-policy judgment;
- an experiment would require real proprietary/user data;
- rights or retention are unclear;
- a tool selection would become de facto architecture before bake-off;
- a schema/API choice would become production binding;
- an ADR would be accepted without an adversarial result;
- dataset research would be activated;
- the implementation gate would be implied rather than explicitly released.
