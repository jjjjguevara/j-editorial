# J-Editorial bootstrap adversarial review — phase 1

Status: **research synthesis / owner-decision hold / not an ADR**  
Controlling gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Implementation: **blocked**  
Dataset research: **not executed**

Source identifiers resolve in [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md).

## 1. Executive result

The core product hypothesis survives, but not in its most scalar or gap-centered form.

A defensible minimum is:

```text
Artifact representation
  + purpose-specific Goal Contract
  + versioned Normative Priors
  + addressable Obligations
  + Findings attached to artifact regions or obligations
  + Evidence and provenance
  + explicit Editorial Operations
  + Verification / adjudication / release outcomes
  + reconstructable history
```

This is a **candidate**, not an accepted model.

The strongest first proof is a bounded Markdown API-reference document evaluated against a versioned OpenAPI description, explicit release obligations, executable structural/style checks, and human review. It supplies objective evidence without pretending that technical documentation is wholly objective. [VERT-01, VERT-02, VERT-03, VERT-04]

Four owner choices determine whether this becomes the bootstrap direction. They are separated in `OWNER-DECISIONS.md`.

## 2. Principal findings

### F-01 — Lifecycle, quality, and release readiness must remain independent

**Finding.** Doc Doctor currently uses one `0..1` refinement value to represent a path from stub through draft/review/publication to polished quality. Audience usefulness is then determined by comparing that same scalar to audience thresholds. [DD-03, DD-05, DD-07]

**Challenge.** A document can become more complete while becoming less accurate; become stylistically better while failing a release obligation; be publishable with explicitly accepted gaps; or be revised after publication without moving “backward” in a universal quality scale.

**Interpretation.** J-Editorial should treat:

- lifecycle/progress as author or workflow state;
- quality as a multidimensional, goal-relative evaluation;
- release readiness as an explicit gate over obligations and risk;
- publication as an event/decision, not the numeric endpoint.

This confirms a central bootstrap invariant rather than creating a new decision. [R-01]

### F-02 — A goal contract must decompose into addressable obligations

**Finding.** A free-text purpose statement is useful but insufficient for deterministic evaluation. OpenAPI demonstrates how a domain contract can expose individual operations, inputs, outputs, examples, security requirements, and extensions; MCJudgeBench and RubricEval independently show why constraint/rubric-level evaluation is more diagnostic than only assigning an overall score. [VERT-01, EVAL-07, EVAL-08]

**Interpretation.** The Goal Contract should not merely contain “document the v1 API.” It should be capable of yielding obligations such as:

- every in-scope operation is represented;
- method/path identity matches the authoritative interface description;
- required parameters and response families are covered;
- examples are present and testable where required;
- audience, scope exclusions, and accepted exceptions are explicit.

An overall readiness judgment may be derived from these records, but the obligation-level evidence remains primary.

### F-03 — `Gap` is important, but too narrow to be the ontology root

**Finding.** A citation request, contradiction, unresolved reviewer objection, release waiver, style warning, and verified improvement are not all naturally “gaps.” W3C Web Annotation supplies a general body/target/motivation pattern; PROV-O supplies entity/activity/agent provenance. Neither requires every observation to be a deficit. [REP-01, REP-02]

**Interpretation.** A more general `Finding` can express positive, negative, uncertain, contradictory, or informational observations. A `Gap` can remain a recognized finding family or a projection meaning “an unsatisfied obligation or unresolved adverse finding.”

This avoids forcing accepted exceptions, positive evidence, or reviewer disagreement into deficit semantics.

### F-04 — Artifact source and semantic records have different fidelity obligations

**Finding.** CommonMark can precisely parse a bounded Markdown dialect, and structured editor models can represent schema-governed trees and operations. Pandoc demonstrates the value of AST-based conversion but also the risk of losing source-specific constructs. [REP-03, REP-04, REP-05]

**Interpretation.** One representation should not silently claim all of these properties:

- exact byte fidelity;
- semantic addressability;
- format-neutral transformation;
- human-friendly authoring;
- stable identity through edits;
- lossless export to every source dialect.

J-Editorial needs an explicit authority decision. The strongest candidate is split authority by concern: exact source snapshots are authoritative for what the artifact contained; a semantic record is authoritative for obligations, findings, provenance, operations, and evaluation. Consistency between the two must be checkable, not assumed.

### F-05 — Raw offsets are not stable identity

**Finding.** W3C selectors combine text quote, position, range, and resource state; ProseMirror remaps positions through transactions; Yjs relative positions retain contextual association but depend on document identity and can become unresolved after deletion. [REP-01, REP-04, REP-06]

**Interpretation.** Every target reference needs:

- artifact/state identity;
- selector type and value;
- resolution status;
- confidence or ambiguity;
- a re-anchoring history when it moves;
- a preserved original selector for audit.

“Line 42” is a display locator, not a durable domain identifier.

### F-06 — History granularity is a product guarantee, not a database feature

**Finding.** Git captures content-addressed snapshots and commit parentage; Dolt exposes queryable versioned tables and diffs; PostgreSQL can expose row changes; DeltaDB claims operation-level identity and code/conversation history between commits. [HIST-01, HIST-02, HIST-03, HIST-04, HIST-05, HIST-07]

**Interpretation.** The decision order must be:

```text
required editorial questions
  → required history granularity
  → required identity/reconstruction semantics
  → representative workload
  → storage bake-off
  → persistence decision
```

Selecting Dolt because it is “Git for data,” or DeltaDB because it preserves operations, reverses this order.

### F-07 — Accepted history is evidence, not gold

**Finding.** Human reviewers disagree; model judges can be biased or unstable; an accepted change can be expedient, politically constrained, later reverted, or simply wrong. Existing LLM-judge work reports position/verbosity/self-preference problems and motivates judge-level meta-evaluation. [EVAL-05, EVAL-06, EVAL-07, EVAL-08]

**Interpretation.** An accepted operation should record:

- who or what proposed it;
- who accepted it and under which authority;
- evidence considered;
- policy/goal versions in force;
- dissent and unresolved objections;
- verification results;
- later reversal or supersession;
- confidence and intended downstream eligibility.

No downstream consumer should infer `accepted == correct == reusable == training-eligible`.

### F-08 — Evaluation must be layered and typed

**Finding.** HELM, OpenAI Evals, and Inspect AI separate scenarios/tasks, inputs, execution, scoring, and reports; NIST emphasizes context-specific measurement. [EVAL-01, EVAL-02, EVAL-03, EVAL-04]

**Interpretation.** A J-Editorial eval instance should bind:

```text
artifact state
+ goal-contract version
+ prior/rule version
+ target obligation(s)
+ grader specification/version
+ evidence inputs
+ result
+ uncertainty/disagreement
+ execution provenance
```

Objective checks, human judgment, and model grading must be separately identified. A weighted aggregate cannot erase component failure, missing evidence, or disagreement.

### F-09 — Origin is not trust

**Finding.** Doc Doctor currently maps authorship origin directly to trust values, including fixed lower values for AI and higher values for human authorship. [DD-05, DD-07]

**Challenge.** Human-authored content may be unsupported; imported content may be authoritative; AI-assisted content may be fully verified; a collaborative origin says little about evidence quality.

**Interpretation.** `origin` is provenance. Trust or confidence must be claim/finding-specific and derived from evidence, verification, reviewer authority, recency, and relevant failure history. Universal origin-based trust weights should not enter the J-Editorial core.

### F-10 — Immutable history and deletion must be designed together

**Finding.** Article 17 creates erasure obligations in applicable circumstances; append-only histories can preserve references to deleted payloads; SPDX and PROV provide priors for retaining integrity/provenance metadata separately from content. [SEC-05, SEC-06, REP-02]

**Interpretation.** The framework must distinguish:

- immutable event identity and non-sensitive audit metadata;
- redactable or cryptographically erasable content payloads;
- tombstones and reason codes;
- derived indexes that must be purged;
- exports/caches/model-provider copies;
- legal hold or exception handling outside the core evaluator.

“Never delete history” is not an acceptable blanket invariant.

### F-11 — Editorial content is hostile input to an agent

**Finding.** OWASP documents direct, indirect, persistent, encoded, HTML/Markdown, RAG, and agent-specific prompt-injection paths, and recommends least privilege and human approval for consequential actions. [SEC-03, SEC-04]

**Interpretation.** Imported artifacts, citations, style guides, comments, and historical operations must never be concatenated into privileged instructions without trust-boundary handling. An agent can propose an operation; publication, disclosure, deletion, rule installation, external retrieval, and history mutation need explicit authorization policies.

## 3. Doc Doctor inheritance audit

Doc Doctor is the first integration candidate, but its current domain model is prior art, not the J-Editorial specification. [R-03, DD-01]

| Existing behavior | Reusable value | Bootstrap objection | Candidate treatment |
|---|---|---|---|
| One `refinement: 0..1` | Captures an author/workflow signal | Conflates progress, quality, usefulness, and release state | Preserve only as an explicitly named, sourced progress signal; never universal truth |
| Stub list | Makes editorial demand visible | “Gap” cannot express every positive, neutral, waived, or disputed observation | Map stubs to typed Findings; Gap becomes a finding family/projection |
| Fixed stub penalties | Simple prioritization | No calibration; context and goal severity differ | Policy/version-specific impact functions outside the core record |
| Five vector families | Useful seed taxonomy | Hard-coded mapping; unknowns default to Creation | Treat as a versioned taxonomy candidate; allow unknown/extension types |
| Origin-based trust | Records provenance category | Provenance does not establish correctness | Retain origin; replace trust scalar with evidence/verification model |
| Health formula | Quick dashboard signal | Arbitrary weights hide component failures | Experimental derived view only, with full component provenance |
| Audience thresholds | Forces audience consideration | Audience is not reducible to a progress threshold | Bind audience needs to Goal Contract obligations and human evidence |
| Freshness half-lives | Recognizes time dependence | “Canonical never stale” is unsafe; cadence is domain-specific | Prior/version-specific review policy, never universal core default |
| Compliance/coverage = `1.0` placeholders | Reserves dimensions | False certainty | Unknown/not-evaluated must be explicit; never encode missing as pass |
| “Vector physics” | Memorable prioritization metaphor | Quantities lack demonstrated construct validity | Keep outside normative core until empirically justified |
| Git milestones | Existing workflow and fixtures | Commits omit many editorial operations | Use as one import adapter and test fixture, not storage decision |
| MCP/AI operations | Valuable agent surface | Content-to-command boundary is security-sensitive | Typed, least-privilege proposed operations with approval and audit |

No change to Doc Doctor is authorized by this review.

## 4. Candidate first product proof

The first proof should expose the whole framework while keeping the ground truth and scope inspectable.

| Candidate | Objective obligations | Human judgment | Existing fixtures/integration | Main risk | Assessment |
|---|---|---|---|---|---|
| Markdown API-reference document + OpenAPI contract | Strong: operation coverage, identifiers, parameters, responses, links, examples, syntax | Still needed for explanation, usability, prioritization, accepted exceptions | Strong fit with docs-as-code and Doc Doctor | Overfitting core to technical docs | **Recommended bounded first proof** |
| General Markdown knowledge article in Doc Doctor | Moderate: structure, citations, links, style | Dominant for quality and purpose | Direct product fit | Weak oracle; subjective debates may obscure core semantics | Valuable second slice |
| Long-form editorial/essay | Weak to moderate | Dominant | Demonstrates non-code generality | Difficult first benchmark; purpose and acceptance highly contextual | Defer |
| Policy/compliance document | Potentially strong | High-stakes expert adjudication | Tests priors/versioning | Legal/compliance risk and inaccessible ground truth | Defer |
| Two simultaneous slices | Strong generality test | Mixed | Reduces overfitting | Doubles ontology and fixture complexity before core is stable | Use as an early generalization gate, not initial slice |

### Recommended bounded scenario

```text
Input artifact:
  one Markdown API-reference page

Authoritative interface evidence:
  one versioned OpenAPI description

Goal Contract:
  named audience, product/version, in-scope operations,
  required sections/examples, explicit exclusions and release policy

Normative Priors:
  bounded CommonMark profile, selected versioned Vale rules,
  explicit organization-specific terminology rules

History:
  imported initial state, deliberate defects, typed operations,
  review decisions, verification, release decision

Evaluation:
  deterministic obligation checks + human review rubric
  + optional model grader treated as experimental
```

This is a recommendation only. D-01 decides it.

## 5. Domain-model decision packet

### Alternative A — Gap-centered

```text
Goal → Gaps → Operations → Resolved gaps → score/release
```

**Strengths:** intuitive; close to Doc Doctor; actionable backlog.  
**Failure modes:** positive findings, waivers, conflicts, and evidence do not fit cleanly; “no gaps” can be misread as “good”; may bias the system toward deficit detection.

### Alternative B — Obligation/Finding-centered

```text
Goal Contract → Obligations
Artifact State → Findings
Findings ↔ obligations / artifact targets / evidence
Operations → verification/outcomes
```

**Strengths:** handles positive, negative, uncertain, waived, and disputed observations; makes completeness and release logic inspectable; aligns with constraint-level evaluation and annotation/provenance priors. [REP-01, REP-02, EVAL-07, EVAL-08]  
**Failure modes:** more explicit records; obligation extraction may be difficult; weak goal contracts still produce weak evaluations.

### Alternative C — Event-centered

```text
Events as canonical facts → projections for artifact, findings, obligations, release
```

**Strengths:** maximum auditability and reconstructability; natural temporal model.  
**Failure modes:** high implementation and migration cost; semantic queries depend on projections; event-version evolution becomes central before the domain is stable.

**Non-binding recommendation:** Alternative B, with explicit operations/events as first-class records but not the sole ontology root.

## 6. Representation-authority decision packet

### Alternative A — Source-first

Exact Markdown/source bytes are canonical. Semantic structures are derived and may be rebuilt.

- Best at: author familiarity, exact round-trip, Git interoperability.
- Weak at: stable node identity, semantic partial updates, cross-format operations.
- Critical experiment: parse/project/re-emit representative fixtures while retaining extensions and anchors.

### Alternative B — Structured-first

A typed semantic tree/graph is canonical. Markdown and other formats are projections.

- Best at: schema validation, structured editing, stable identity, transformations.
- Weak at: source-format fidelity and migration of unsupported constructs.
- Critical experiment: source → structure → source round trips across real Markdown extensions and manual formatting.

### Alternative C — Split authority by concern

- exact source snapshot is authoritative for artifact representation;
- semantic record is authoritative for goals, obligations, findings, evidence, provenance, operations, and evals;
- mappings between them are versioned, tested, and allowed to be partially unresolved.

- Best at: honest fidelity boundaries and incremental adoption.
- Weak at: consistency protocol, duplicate identity surfaces, more complex exports.
- Critical experiment: change source and semantic records independently, then test reconciliation, stale-target detection, reconstruction, and audit.

**Non-binding recommendation:** Alternative C. It avoids claiming that an AST can preserve every source detail or that source text can natively carry every semantic relation.

## 7. History-guarantee decision packet

| Candidate | What it proves | What it does not prove | Bootstrap status |
|---|---|---|---|
| Git snapshots | Exact committed source states, branching, parentage, broad interoperability [HIST-01] | Accepted operation semantics, between-commit history, row/claim queries | Required baseline candidate, not sufficient conclusion |
| Dolt | Versioned/queryable relational records and diffs [HIST-02, HIST-03] | Correct editorial schema or stable semantic identity | Bake-off candidate |
| PostgreSQL + application events/logical decoding | Flexible transactional model and change stream [HIST-07, HIST-08] | Domain-event meaning without explicit application design | Bake-off candidate |
| DeltaDB | Stated fine-grained deltas, stable identities, evolving anchors, collaborative code/conversation [HIST-04, HIST-05, HIST-06] | General editorial fit, stable public dependency/API, independent performance | Inspiration/prototype comparator only |
| CRDT-backed operation log | Continuous collaboration and convergent edits [REP-06] | Goal/eval semantics, human approval, release authority | Include only if continuous collaboration is a first-slice requirement |

The key choice is not the backend. It is the minimum guarantee:

1. accepted checkpoints only;
2. accepted semantic operations plus checkpoints;
3. every edit/continuous collaborative history.

The non-binding recommendation is **accepted semantic operations plus checkpoints**. It captures causal editorial evidence without requiring keystroke-level or CRDT history in the first slice.

## 8. Evaluation contract candidate

A valid result should be inspectable without trusting an aggregate number.

```text
Eval Instance
├── artifact_state_id
├── goal_contract_id + version/hash
├── obligation_ids
├── prior/rule ids + versions/hashes
├── target selectors + resolution status
├── grader type
│   ├── deterministic
│   ├── human
│   └── model
├── grader implementation/model/prompt version
├── evidence inputs and provenance
├── component results
├── uncertainty / disagreement / abstention
├── execution environment
├── cost and latency
└── result status
```

Candidate evaluation rules:

- missing evidence is `unknown/not-evaluated`, never pass;
- deterministic checks report what they actually establish;
- human rubrics preserve reviewer role, instructions, disagreement, and adjudication;
- model graders are calibrated against held expert judgments before use as release evidence;
- model-judge correctness, consistency, and bias are separate measures;
- one obligation's failure cannot be hidden by averaging unrelated successes;
- release policy consumes typed results but is not identical to any one metric;
- every aggregate retains its formula, weights, inputs, versions, and confidence.

These rules are consistent with current evaluation harness separation and judge-reliability research, but require J-Editorial experiments before acceptance. [EVAL-01 through EVAL-08]

## 9. Scenario stress tests

### S-01 — Interface changed, prose did not

An OpenAPI operation is added. The page remains fluent and style-clean.

**Required behavior:** create an unmet coverage obligation with interface-version evidence; do not lower a universal “writing quality” scalar; block release only if the scoped release policy makes the operation mandatory. [VERT-01]

### S-02 — Citation exists, claim is still unsupported

A paragraph contains a URL, but the source does not support the claim.

**Required behavior:** link presence can pass while evidentiary entailment remains failed/unknown; selectors must bind the claim and evidence excerpt/version separately. [REP-01, REP-02]

### S-03 — Policy version changes

A style rule is accepted under one guide version and prohibited under the next.

**Required behavior:** retain both evaluations with prior versions; do not rewrite history; mark current applicability explicitly. [VERT-02, VERT-03]

### S-04 — Revision decreases completeness but improves safety

A reviewer removes an unsupported section before publication.

**Required behavior:** completeness may decrease while release readiness increases; preserve operation rationale and evidence; no monotonic quality invariant.

### S-05 — Target text moves and is rewritten

A cited paragraph is split and moved.

**Required behavior:** attempt selector resolution/re-anchoring; preserve original target and mapping evidence; surface ambiguity rather than attaching silently to the wrong text. [REP-01, REP-04, REP-06]

### S-06 — Two branches resolve the same finding differently

One branch deletes a claim; another adds evidence.

**Required behavior:** preserve both operation lineages; merge must reconcile semantic identity and policy state, not only textual conflict. [HIST-01, HIST-02]

### S-07 — Personal data must be erased

A historical comment contains personal data subject to a valid deletion requirement.

**Required behavior:** erase/redact the payload and derived copies while preserving only legally permissible tombstone/audit metadata; history immutability applies to event identity, not an unconditional right to retain content. [SEC-05]

### S-08 — Imported content instructs the agent

A source document contains hidden Markdown/HTML instructing the model to publish secrets or alter rules.

**Required behavior:** content remains untrusted data; agent tools are least-privilege; consequential operations require policy and human authorization; logs record the attempted action. [SEC-03, SEC-04]

### S-09 — Accepted reviewer decision is later reversed

A senior reviewer approves an edit; a later correction establishes it was wrong.

**Required behavior:** preserve acceptance authority and later reversal; downgrade downstream eligibility; never erase dissent or treat original acceptance as permanent gold.

### S-10 — Format extension cannot round-trip

A Markdown plugin node is not represented by the candidate semantic model.

**Required behavior:** preserve the exact source and extension payload or reject the transformation; never silently normalize away information. [REP-03, REP-05]

## 10. Assumptions rejected or narrowed

| Assumption | Disposition | Reason |
|---|---|---|
| `0..1` is a universal quality trajectory | **Reject** | Conflates distinct constructs; no calibration |
| Quality should monotonically approach `1` | **Reject** | Real revisions trade dimensions and can expose regressions |
| Every gap has a fixed universal penalty | **Reject** | Severity is goal-, context-, policy-, and evidence-dependent |
| Human origin is intrinsically more trustworthy | **Reject** | Origin is provenance, not verification |
| Canonical artifacts never go stale | **Reject** | Canonical status does not freeze external facts or obligations |
| No open gaps means publication-ready | **Reject** | Missing detection and unmodeled obligations remain possible |
| Git commits capture the full editorial process | **Narrow** | Strong source checkpoints; weak between-commit/domain semantics |
| A structured AST guarantees lossless source round trip | **Reject** | Unsupported syntax and formatting can be lost |
| Accepted edits are training-grade positives | **Reject** | Acceptance authority and correctness differ |
| LLM graders can replace expert review once agreement is high | **Reject** | Agreement, validity, consistency, and bias are distinct |
| DeltaDB is ready to select as the backend | **Reject for bootstrap** | Private beta/early access and code-specific evidence |
| Every keystroke must be retained | **Defer** | Requirement depends on collaboration/product decision |
| One database must own source, semantic records, eval logs, and future datasets | **Reject as premise** | Different concerns may require different authorities and retention rules |

## 11. Candidate invariants pending owner direction

These are review recommendations, not accepted contract text:

1. `Artifact State`, `Goal Contract`, `Prior`, and every evaluator input are version-addressable.
2. Goal contracts decompose into addressable obligations.
3. `Finding` is general; `Gap` denotes an adverse/unresolved specialization or projection.
4. Artifact source fidelity and semantic-record fidelity have separate authority rules.
5. Operations record actor, authority, intent, pre/post state, evidence, and verification.
6. Release is an explicit policy decision over obligations, findings, evidence, and accepted risk.
7. Unknown/not-evaluated is distinct from pass.
8. Provenance is not a trust score.
9. Aggregates never replace component results.
10. Accepted history is evidence with authority and confidence, not automatic truth.
11. Target resolution can be ambiguous or stale and must say so.
12. Content payloads can be erasable even when event identity is retained.
13. Imported content cannot grant agent authority.
14. Backend selection follows representative workload experiments.
15. The core remains useful with deterministic and human evaluation only.

## 12. Blocking ambiguities

Authoritative revisions would be premature until D-01 through D-04 are answered. Their choices affect:

- the first ontology slice;
- the representation bake-off;
- history granularity;
- persistence workload;
- import/export guarantees;
- goal-contract decomposition;
- integration sequencing with Doc Doctor;
- the non-dataset research program graph;
- bootstrap exit criteria.

No ADR, implementation task, or backend selection should be created before those answers.
