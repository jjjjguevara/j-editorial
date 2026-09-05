# Bootstrap next-phase contract

Status: **proposed / blocked by D-02R, D-01P, and AMN-01**  
Authority: subordinate to `BOOTSTRAP.md`, the decision addendum, and explicit owner answers  
D-01: paired proof selected  
D-03: deferred  
D-04: semantic operations plus checkpoints provisionally selected  
Dataset research: **held**

This document defines the next non-implementation research phase. It is not a task tracker, ADR, schema, or implementation authorization.

## 1. Controlling-document revision gate

After the revised owner answers, update these documents in one consistency commit:

| Document | Required revision |
|---|---|
| `BOOTSTRAP.md` | Replace the unresolved D-01/D-02/D-04 text with accepted research directions; state D-03's remaining boundary; preserve all invariants and the implementation hold. |
| `ROADMAP.md` | Make the paired Amnesia/prose proof the first product proof; make both slices co-gating rather than sequential decoration. |
| `RESEARCH.md` | Register the semantic-frame, Amnesia, prose, representation, history, evaluation, priors, and security programs with common result/gate contracts. |
| `research/programs/model-training-data/CHARTER.md` | Terminology and dependency alignment only; retain held status and prohibit execution. |
| `research/packets/2026-09-04-phase-1-adversarial-review/*` | Move from revised decision hold to active phase-2 research and preserve owner answers verbatim. |

An owner choice narrows research. It does not validate the selected hypothesis or release implementation.

## 2. Program fan-out

Program labels are planning identifiers, not Beads IDs.

| Program | Question | Required output | Gate dependency |
|---|---|---|---|
| `BR-FRAME` — editorial construction space | Does the three-axis scaffold expose missing operations, referents, actors, dialogue, and norms across both slices? | figure glossary, cross-axis cases, counterexamples, falsification report | D-02R |
| `BR-DOM` — typed editorial records | Which distinctions are irreducible in the paired fixtures, and can `Gap` remain derived? | relationship model, invariants, reduction attempts, negative cases, Doc Doctor mapping | `BR-FRAME` reconnaissance |
| `BR-GOAL` — goal contracts | How are purpose, audience, scope, obligations, waivers, accepted uncertainty, and release policy expressed? | contract requirements, decomposition rules, ambiguity handling, paired examples | D-01P + `BR-DOM` |
| `BR-AMN` — Amnesia technical proof | Can docs claims be evaluated reproducibly against pinned product types, runtime behavior, tests, and human tasks? | oracle contract, fixture, raw checks, adjudication packet | AMN-01 |
| `BR-PROSE` — general-prose proof | Can the same domain grammar represent evidence, rhetoric, structure, audience fitness, disagreement, and multiple acceptable edits? | rights/purpose packet, fixture, review protocol, alternative resolutions | D-01P |
| `BR-REP` — representation and authority | Which source/semantic/projection authority model meets fidelity, identity, targeting, partial-update, and reconciliation requirements? | round-trip/reconciliation experiments, selector tests, recommendation packet | `BR-DOM`, `BR-GOAL`, `BR-SEC` |
| `BR-HIST` — history and persistence | Which backend-neutral history model can reconstruct D-04B episodes and checkpoints? | workload, backend comparison, replay/recovery/redaction tests, recommendation packet | `BR-REP` requirements |
| `BR-EVAL` — evaluation science | Which objective, human, and model grader contracts produce valid obligation-level evidence in both slices? | eval-instance contract, grader taxonomy, calibration/meta-eval, reporting contract | `BR-AMN`, `BR-PROSE`, `BR-DOM` |
| `BR-PRIORS` — normative priors | How are guides and rules scoped, licensed, versioned, conflicted, and applied? | prior contract, provenance, precedence and exception cases | `BR-GOAL`, `BR-DOM` |
| `BR-SEC` — security/privacy | What trust, authorization, erasure, retention, provider, and hostile-content boundaries are required? | threat model, authority matrix, deletion/redaction tests | begins in parallel; gates `BR-REP` |
| `BR-INT-DD` — Doc Doctor migration | How can current stubs, refinement, vectors, and Git history import without becoming core truth? | mapping, incompatibility ledger, fixture adapter, rollback plan | paired-proof synthesis |

The model-training-data program remains held and downstream of accepted outputs. No corpus work belongs in these programs.

## 3. Dependency shape

```text
D-02R ─────► BR-FRAME ─────► BR-DOM ─────┐
                                           │
D-01P ─────► BR-PROSE ──────┐              ├──► BR-GOAL
                             ├── paired ────┤
AMN-01 ────► BR-AMN ─────────┘              │
                                           ▼
BR-SEC ─────────────────────────────────► BR-REP
                                           │
                         D-04B ───────────► BR-HIST
                                           │
                     ┌─────────────────────┴────────────┐
                     ▼                                  ▼
                  BR-EVAL                           BR-PRIORS
                     └──────────────┬───────────────────┘
                                    ▼
                          paired-proof synthesis
                                    │
                                    ▼
                               BR-INT-DD
                                    │
                                    ▼
                         bootstrap adversarial gate
```

Reconnaissance may overlap, but no downstream recommendation may silently settle an upstream semantic or authority question.

## 4. Paired-proof rule

The technical and prose slices are co-gating. A model that succeeds only on Amnesia cannot be declared general; a model that succeeds only on prose cannot substantiate deterministic parity or executable evidence.

Shared minimum cases:

1. valid baseline with positive evidence;
2. missing mandatory content;
3. present but contradictory content;
4. accepted exception/waiver;
5. uncertain or insufficient evidence;
6. conflicting reviewer judgments;
7. target move/rewrite/delete;
8. alternate valid resolution;
9. rule/goal/evidence version change;
10. failed operation with no post-state;
11. branch and merge disagreement;
12. redacted payload with permissible audit metadata;
13. unsupported source construct or lossy projection;
14. hostile prompt-like text that remains inert.

These are evaluation/architecture fixtures, not a model-training corpus.

## 5. D-04B history contract

Every material editorial operation in the first proof must retain:

- immutable operation identity;
- proposal/performance status;
- actor, role, and authority;
- pre-state and resolved/ambiguous target;
- goal, norm, evidence, and grader versions;
- intended effect;
- acceptance, rejection, waiver, failure, or abstention;
- verification result and disagreement;
- post-state/checkpoint where one exists;
- supersession, reversal, branch, merge, and erasure relationships.

Every keystroke is out of scope. Fine-grained deltas may later be imported or linked, but they are not required to pass the first proof.

## 6. Amnesia experiment contract

Subject to AMN-01 authorization, `BR-AMN` begins with the pinned API root, capability model, and `commands.notes` surface identified in `AMNESIA-DOCS-SLICE-AUDIT.md`.

It must:

1. pin documentation and product refs;
2. define source precedence per obligation;
3. capture raw TypeScript/AST/build/test outputs;
4. test signatures, synchrony, capability hierarchy, error behavior, event payloads, readiness support, and examples;
5. preserve positive and adverse findings separately;
6. model at least two correction candidates where editorial choice exists;
7. rerun verification after the proposed state;
8. avoid changing either Amnesia repository during bootstrap research.

## 7. Prose experiment contract

`BR-PROSE` must record:

- exact artifact/ref and rights;
- purpose, audience, scope, and non-goals;
- evidence boundary and fact-check authority;
- style/norm applicability;
- at least one factual, structural, rhetorical, and audience-fit problem;
- at least two defensible resolutions for one problem;
- reviewer disagreement and adjudication protocol;
- no private personal information unless separately authorized and protected.

## 8. Program decision-packet gate

Every material program must produce:

1. decision boundary and challenged assumptions;
2. current primary sources and versions;
3. credible alternatives;
4. representative paired-fixture experiment where relevant;
5. raw results and reproduction instructions;
6. failure modes, negative evidence, and objections;
7. reversibility, migration cost, and exit path;
8. security, privacy, rights, licensing, and retention impact;
9. acceptance and falsification criteria;
10. recommendation: `accept`, `narrow`, `defer`, `reject`, or `research further`;
11. unresolved owner questions;
12. proposed ADR/specification changes only after review.

A feature table or philosophical analogy alone cannot pass.

## 9. Persistence bake-off boundary

No persistence candidate may be selected until `BR-DOM`, `BR-GOAL`, and `BR-REP` produce a representative D-04B workload.

The bake-off must test:

- exact source-checkpoint reconstruction;
- semantic episode reconstruction;
- proposal/accept/reject/fail histories;
- target identity through move/rewrite/delete;
- branch/merge and conflicting adjudication;
- goal/norm/evidence version changes;
- provenance queries from outcome to evidence and actor;
- partial erasure/redaction and index cleanup;
- corruption/interrupted-write recovery;
- deterministic export/import and backend exit;
- query cost at artifact, obligation, finding, operation, and episode levels.

Git, Dolt, PostgreSQL, operation logs, CRDTs, and DeltaDB remain candidates or comparators. Delta client access alone does not select DeltaDB.

## 10. Evaluation gate

`BR-EVAL` must distinguish construct validity, correctness, reliability, robustness, calibration, disagreement, abstention, leakage, cost, latency, and release-policy impact. Objective checks, human judgment, and model grading remain typed separately. Any model judge must pass an adversarial meta-eval before affecting a release gate.

## 11. Security and authority gate

Before any agent can execute consequential operations, `BR-SEC` must define authority for reading history, retrieving evidence, installing/changing priors, proposing/applying edits, accepting/rejecting, publishing, exporting, deleting/redacting, changing retention, and sending content to external providers. Imported content cannot grant authority.

## 12. Native Beads fan-out

The repository contract requires Beads. The current execution environment cannot run the repository's Dolt-backed `bd` workflow and must not edit `.beads` directly.

In a compatible checkout:

1. run `bd prime`, `bd ready`, and `bd list`;
2. create one bootstrap epic and children matching Section 2;
3. encode Section 3 dependencies;
4. mark the dataset program held/downstream;
5. link PR #1, the research commits, and pinned external refs;
6. push through the configured Beads/Dolt workflow.

Markdown tasks and GitHub Issues are not substitute sources of truth.

## 13. Stop conditions

Phase 2 halts when:

- a paired artifact, purpose, evidence boundary, or review authority is ambiguous;
- D-02R distinctions cannot survive representative cases;
- a source/semantic/projection mapping becomes architecture by accident;
- Amnesia source access or reproducibility is insufficient;
- rights or retention are unclear;
- a persistence or framework choice precedes the workload;
- a schema/API becomes production-binding;
- an ADR is accepted without an adversarial result;
- dataset research is activated;
- implementation authorization is implied rather than explicit.
