# j-editorial — Bootstrap Contract

Status: **pre-implementation / adversarial review**  
Current gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Repository: `jjjjguevara/j-editorial`  
Contract role: **architecture boundary, review charter, and implementation hold**

This document records the working product model, architectural invariants, unresolved hypotheses, falsification questions, and review gates for `j-editorial` before implementation begins.

It is deliberately more detailed than a project brief and deliberately less final than an implementation specification. Its purpose is to make assumptions visible before code, schema, package structure, persistence decisions, benchmark corpora, or ADRs harden them accidentally.

No technical choice is accepted merely because it appears in this file. Where this document uses words such as *candidate*, *proposal*, *hypothesis*, *should*, or *current model*, the item remains subject to adversarial review unless explicitly identified as a bootstrap invariant or owner-imposed constraint.

## Accepted research scope — 2026-09-04

The owner's accepted directions supersede older candidate wording in this document:

- D-01C: Amnesia API reference and portfolio About prose are co-gating research slices.
- D-02R: the Editorial Construction Space is a cross-cutting analytic scaffold;
  typed plural records are logical distinctions, not mandatory separate objects.
- D-03: causal event transactions, time-scoped facts/fluents, exact checkpoints,
  and versioned projections are the accepted research shape, not a storage choice.
- D-04B: meaningful semantic operations plus checkpoints; keystroke capture is optional.
- AMN-01: pinned product inspection and isolated tests are permitted, without source mutation.
- D-01P: only `sci-jjjjguevara/src/pages/about.astro` at the accepted immutable revision
  is target prose; supporting profile/brief/history records are evidence or norms.

Scope authorities: [D-03 acceptance](research/phase-2/D-03-ACCEPTANCE.md),
[D-01P acceptance](research/phase-2/D-01P-ACCEPTANCE.md), and
[Phase 2 gates](research/phase-2/STAGE-GATE.md). PR #2 was merged at
`0d24e78713ed7a2c04810ce9961e5c28ab3da096` following owner approval.

Phase 3 tests behavioral integrity, targeting, representation alternatives and
research protocols. It does not select production representation, persistence,
a programming language, or an ADR. The implementation gate remains closed.
Model-training dataset research is explicitly held for a separate session.

## 0. How to read this contract

This contract distinguishes four classes of statement.

### 0.1 Bootstrap invariant

A bootstrap invariant is a design constraint that implementation must not silently violate while the review gate is open. An invariant can still be challenged during the review, but changing it requires an explicit revision of this contract or a later accepted ADR.

### 0.2 Provisional direction

A provisional direction is the current favored model. It exists so that review has something concrete to attack. It is not permission to implement it.

### 0.3 Open question

An open question must be answered, narrowed, or explicitly deferred before the relevant implementation vertical is released.

### 0.4 Forbidden assumption

A forbidden assumption is something agents and contributors must not infer from repository state. In particular:

- Beads uses Dolt; **that does not select Dolt for the product**.
- Markdown appears in the design discussion; **that does not make Markdown the canonical document model**.
- A structured document model is favored; **that does not mean it is accepted**.
- DeltaDB is architecturally interesting; **that does not make it a production dependency**.
- A `0..1` editorial score motivated the original scenario; **that does not make a scalar quality score canonical**.
- Historical human edits exist; **that does not make every accepted historical edit a unique gold answer**.
- A style guide can seed ontology rules; **that does not make guide text redistributable or universally applicable**.
- A benchmark score improves; **that does not prove production quality improved**.

## 1. Mission

`j-editorial` is an editorial framework for representing, versioning, evaluating, and improving artifacts across a Document Development Lifecycle.

The initial motivating environment is docs-as-code, but the framework must be reusable in non-code contexts, including writing products that want Git-like history, structured editorial provenance, agent-assisted editing, and benchmarkable editorial workflows without making files, line numbers, or Git commits the canonical domain model.

The central product opportunity is to make editorial state machine-legible enough that humans and specialist agents can reason about:

- what an artifact is trying to accomplish;
- what standards, policies, and editorial priors apply;
- what is missing, unsupported, wrong, stale, ambiguous, structurally weak, or release-blocking;
- what evidence supports a change;
- what action was taken and by whom;
- what the action resolved or regressed;
- whether the artifact is ready for a given lifecycle transition;
- how a specialist agent performs on these judgments under controlled evaluation.

The editorial framework must remain useful independently of ML, evals, or agentic workflows. The eval/benchmarking substrate is a consumer of editorial state and history, not the reason the editorial core exists.

## 2. Explicit non-goals for the bootstrap phase

The bootstrap phase is **not** intended to:

- build a text editor;
- clone Git, Dolt, DeltaDB, or a CRDT system;
- define one universal theory of writing quality;
- encode every rule from AP, CMOS, Wikipedia, or another guide;
- treat style-guide compliance as equivalent to correctness;
- choose a programming language or web framework;
- choose a canonical persistence engine;
- create production APIs;
- create training corpora;
- train or fine-tune a model;
- publish leaderboard claims;
- produce a universal scalar score for documents;
- define an immutable repository tree before the architecture review;
- make copyrighted editorial-guide content part of the repository without a licensing determination;
- treat the first specialist agent as a general-purpose autonomous editor.

## 3. Accepted research hypothesis

The current research model is:

`Goal + Norms + Exact Artifact Checkpoints + Typed Editorial Data + Evidence + Causal Transactions + Time-scoped Conditions + Versioned Projections`

One datum may simultaneously participate in constructive, referential, and
pragmatic/governance relations. These are not mutually exclusive storage layers.

`decide(S, command) -> proposed/accepted transaction | rejection | abstention`

`evolve(S, transaction, reducer_version) -> S'`

`project(S', goal_version, projection_version) -> findings/gaps/readiness/report`

An observation records that an evaluator produced a result; it does not by itself
make the conclusion true. An obligation is not a finding, and an accepted proposal
is not proof of a successful operation. A condition may hold between events.
Exact source reconstruction requires available material checkpoints.

`GapField = unresolved adverse findings or unsatisfied applicable obligations`

Gap is a derived view under a particular goal, norm, evidence and interpretation,
not the universal ontology root. Historical transitions still retain before/after,
intent, evidence, authority, outcomes, rejection, failure and uncertainty.

The logical shape is authorized for falsification research only. Physical event-first,
fact-first, event–fluent and checkpoint+journal alternatives remain open. Semantic
replay, portable encoding and storage-order independence require execution evidence.

## 4. Bootstrap invariants

Until explicitly revised, the following constraints govern the design.

### 4.1 Lifecycle, quality, and release readiness are distinct

`lifecycle stage != quality != release readiness`

A draft can be excellent. A published artifact can contain an error. A review can discover a severe problem and reduce confidence. A source-of-truth change can make a previously correct artifact stale without changing the artifact itself.

Editorial progress must therefore be allowed to be non-monotonic:

`Q_(t+1) < Q_t`

is a valid historical outcome.

### 4.2 Publication means release acceptance, not perfection

`published` means that the applicable release gate was satisfied under a specific contract and evidence state. It does not mean `quality = 1`, final truth, or permanent correctness.

Post-publication errata, deprecation, supersession, staleness, and reopened gaps must be representable.

### 4.3 Aggregate scores are derived views

Per-instance observations, evidence, grader outputs, and provenance are primary evaluation data. Aggregate benchmark scores are derived representations and must never be the only persisted result.

### 4.4 Historical acceptance is evidence, not automatic ground truth

A human-approved edit may be useful supervision, but it can later be reverted, contradicted, superseded, stylistically arbitrary, or one of many acceptable solutions.

Historical state transitions should preserve review and outcome context rather than being flattened into `before = bad`, `after = good`.

### 4.5 Normative priors are scoped and conditional

No editorial guide, style rule, publication convention, or heuristic applies universally. Applicability, precedence, exceptions, provenance, and version must remain observable.

### 4.6 Objective and subjective graders must not be conflated

Where a property can be measured directly with deterministic or executable checks, a subjective model judge should not replace the direct measurement without a documented reason.

Where a property is inherently preference-based, the system must not disguise it as objective fact merely because a grader emits a number.

### 4.7 Evaluation isolation is mandatory

Training, development, and held-out evaluation data must be separable by lineage and provenance. Neighboring snapshots from the same artifact must not be randomly scattered across train and test sets in ways that make test performance meaningless.

### 4.8 Score-affecting components require provenance and versions

If a component can materially change a benchmark result, the run must be able to identify the component version or immutable content reference. This includes datasets, split definitions, goal contracts, ontology/prior bundles, prompt/scaffold configuration, graders, harnesses, models, tools, execution environments, and aggregation logic.

### 4.9 Editorial core cannot depend on eval infrastructure

The intended dependency direction is:

`eval / benchmark / agent infrastructure -> editorial core`

not:

`editorial core -> eval / benchmark / agent infrastructure`

The editorial framework must remain independently useful for a writing product, CMS, newsroom, research workflow, legal-document process, documentation platform, or other editorial system.

## 5. Domain vocabulary under review

The review must produce a precise glossary before implementation. The following vocabulary is the current candidate set.

### Artifact

A document-like editorial object whose state evolves over time. It may eventually project to Markdown, HTML, PDF, structured data, or another representation.

### Artifact state

A materializable state of the artifact and its editorial metadata at a defined point in history.

### Semantic node

A candidate stable-addressable element such as a section, paragraph, claim, example, code block, citation, table, or other editorial unit. Whether all such nodes require durable identities is unresolved.

### Claim

A proposition in an artifact that may be supported, contradicted, qualified, attributed, or superseded by evidence. Not every sentence is necessarily a claim.

### Goal contract

A versioned statement of what an artifact is intended to accomplish and what conditions govern acceptance for a particular lifecycle or release target.

### Prior

A versioned rule, convention, requirement, heuristic, or expectation that may apply to an artifact in context.

### Gap

A candidate first-class representation of an unresolved editorial condition. It is broader than a typo and may include epistemic, completeness, structural, usability, style, lifecycle, or release deficiencies.

### Finding

An observation produced by a reviewer, detector, grader, or agent. A finding may lead to a gap but should not automatically be treated as a validated gap.

### Obligation

A requirement that the artifact is expected to satisfy. The review must decide whether obligations are distinct from gaps. A missing obligation may produce a gap, but the concepts are not obviously identical.

### Evidence item

A source, test result, authoritative record, executable check, citation target, or other observation used to support or challenge a claim, gap, or editorial action.

### Editorial operation

A typed action intended to change document state or editorial metadata.

### Editorial event

A historical event with actor, cause/context, operation, evidence, and outcome semantics. A low-level text insertion and a high-level `RESOLVE_GAP` event may exist at different layers.

### Snapshot / checkpoint

A materializable semantic state preserved at a meaningful boundary.

### Release

A lifecycle checkpoint whose applicable release contract passed. Releases may later be superseded, deprecated, or amended by errata.

### Eval instance

One controlled evaluation unit containing enough state, context, budgets, and grading rules to measure a defined capability.

### Benchmark suite

A versioned collection of eval instances, graders, aggregation rules, slice definitions, and execution constraints intended to make results comparable.

## 6. Artifact representation vertical

The representation decision must be driven by capabilities, not convenience.

### 6.1 Research direction: authority by concern

Exact material state, editorial-semantic assertions and derived projections answer
different authority questions over one multidimensional state. They do not require
three stores, three exclusive layers, or a structured-first canonical document.

Source-first, structured-first, and composed representations remain alternatives.
Stable identity, source fidelity, opaque-syntax preservation, reconciliation and
migration evidence must precede a physical representation decision.

### 6.2 Representation requirements to test

Any candidate representation must be evaluated against at least these requirements:

- stable references through movement and restructuring;
- provenance at useful granularity;
- exact or well-defined reconstruction of historical states;
- semantic diffing;
- partial updates;
- branching or alternate proposed states;
- concurrent editing compatibility if collaboration is in scope;
- deterministic import/export behavior;
- preservation of unsupported syntax or extensions where round-tripping requires it;
- machine-addressable claims, gaps, evidence links, and review findings;
- compatibility with batch eval generation;
- human-readable disaster recovery or export path;
- content hashing or another integrity mechanism.

### 6.3 Source-text alternative must be taken seriously

The adversarial review must test whether stable semantic identities can be layered over source text instead of making a structured document graph canonical.

A structured model should only be selected if it materially improves identity, provenance, collaboration, eval generation, or queryability enough to justify migration and round-trip complexity.

## 7. Goal-contract vertical

A free-text metadata `description` is useful as intent, but it is not sufficient by itself as an eval specification.

The current model is to refine or compile intent into a versioned goal contract.

A candidate goal contract may include:

- identity and version;
- purpose;
- intended audience;
- scope;
- required outcomes or coverage;
- hard requirements;
- release blockers;
- desirable but non-blocking properties;
- non-goals;
- authoritative sources or source classes;
- domain/jurisdiction constraints;
- allowed uncertainty or abstention behavior;
- applicable prior bundles;
- acceptance tests where deterministic checks exist;
- temporal validity or target product version.

Example motivating contract:

> A v1 API reference enables an external developer to correctly use every public v1 endpoint.

That intent might imply obligations such as endpoint coverage, parameter accuracy, response accuracy, authentication accuracy, executable examples, and source fidelity.

Open questions include:

- How much structure is the minimum useful contract?
- Can contracts inherit from document-type templates?
- Can a model propose a contract, and what human approval is required?
- How are conflicting goals represented?
- How are contract changes distinguished from artifact regressions?
- Can the same artifact be evaluated against several goal contracts simultaneously?

## 8. Lifecycle, quality, and release model

### 8.1 Lifecycle state

Candidate lifecycle states may include:

- conception;
- outline;
- draft;
- working copy;
- peer review;
- fact check;
- release candidate;
- published;
- erratum;
- deprecated;
- superseded.

The exact state machine is not accepted and may vary by vertical.

### 8.2 Heterogeneous quality observations

The current direction preserves typed multidimensional observations. Neither a scalar nor vector arithmetic defines canonical editorial state. Candidate observable concerns include:

- correctness;
- completeness / coverage;
- verifiability;
- usability / audience fitness;
- structural quality;
- style/conformance;
- freshness/currentness.

A domain-specific vector may be more precise. An API reference, for example, may expose endpoint coverage, parameter accuracy, response accuracy, example executability, link integrity, terminology consistency, and source fidelity.

### 8.3 Release readiness

Release readiness should be represented as a gate over requirements and blockers rather than as `quality == 1`.

A simple conceptual form is:

`ReleaseReady = all(required_conditions_pass) && no(open_release_blockers)`

The release decision must retain the contract, source/evidence state, grader versions, and unresolved non-blocking gaps that informed it.

### 8.4 Scalar summaries

If a scalar is useful for optimization or presentation, it must be derived from interpretable dimensions or gap liabilities and must not erase the underlying vector.

A simple weighted mean is not automatically appropriate because high style scores must not compensate for severe correctness failures. Weighted geometric means, hard gates, or risk-weighted liability functions may be better candidates, but none is accepted yet.

## 9. Editorial gap ontology vertical

Gap fields are derived views. Obligations, findings, evidence, decisions and continuing conditions remain distinguishable; the following gap families are classification candidates, not universal root objects.

### 9.1 Candidate gap families

#### Epistemic

- citation needed;
- source quality insufficient;
- fact-check required;
- unsupported claim;
- factual contradiction;
- unverifiable claim;
- stale claim;
- uncertain attribution;
- evidence conflict.

#### Correctness

- factual error;
- technical error;
- incorrect example;
- contradiction within artifact;
- schema/procedure mismatch;
- erratum.

#### Completeness

- stub;
- missing section;
- missing example;
- missing parameter or field;
- missing edge case;
- unresolved placeholder;
- incomplete procedural step;
- missing prerequisite.

#### Structural / information architecture

- hierarchy defect;
- misplaced content;
- duplication;
- missing cross-reference;
- navigation defect;
- poor ordering;
- orphaned concept.

#### Linguistic

- ambiguity;
- grammar defect;
- terminology inconsistency;
- unnecessary verbosity;
- readability problem;
- referential ambiguity.

#### Style / convention

- capitalization;
- punctuation;
- numeral/date treatment;
- citation style;
- terminology policy;
- house-style violation.

#### Audience / usability

- unexplained prerequisite;
- unexplained concept;
- task cannot be completed from the document;
- discoverability failure;
- wrong audience assumption;
- accessibility-related editorial deficiency.

#### Lifecycle / workflow

- unresolved review finding;
- approval pending;
- draft marker;
- deprecated content;
- unaddressed erratum;
- release blocker.

The review must determine which of these are true ontology classes, which are relationships, which are states, and which should be represented elsewhere.

### 9.2 Candidate gap record

A gap may require fields such as:

- stable gap identity;
- target artifact/node/claim identity;
- gap type and subtype;
- affected quality dimension;
- status;
- detector or origin;
- deterministic vs inferred detection mode;
- confidence that the gap exists;
- severity;
- goal relevance;
- evidence requirement;
- remediation policy;
- estimated remediation cost;
- release significance;
- prior/obligation violated;
- related or dependent gaps;
- creation provenance;
- verification provenance;
- resolution outcome;
- reopen/supersession history.

### 9.3 Detection mode matters

A broken link, missing endpoint, unresolved `TODO`, or schema mismatch may be mechanically detectable.

Clarity, audience mismatch, insufficient explanation, or whether a claim requires citation may require model or human judgment.

The system must preserve that distinction. A model-inferred gap should not masquerade as a deterministic fact.

### 9.4 Overlapping gaps are expected

A single paragraph may simultaneously contain:

- a factual claim needing verification;
- insufficient citation;
- ambiguous wording;
- terminology inconsistency.

The model must not assume one target can have only one gap or that all gaps collapse to one severity value.

### 9.5 Gap field

At state `S_t`, the artifact may be described by an unresolved gap field:

`G(S_t) = {g_1, g_2, ..., g_n}`

A derived remaining-liability function could eventually take a form such as:

`L(S) = Σ severity_i * confidence_i * goal_relevance_i * type_weight_i`

but the numerical policy is provisional. The individual typed gaps remain more interpretable than the scalar liability.

### 9.6 Expected value of correction

A prioritization layer may estimate something like:

`EVC_i = (impact_i * confidence_i * goal_relevance_i) / remediation_cost_i`

This is useful as a candidate scheduling heuristic, not a normative truth. High-consequence release blockers may need hard precedence regardless of estimated cost efficiency.

## 10. Normative prior and ontology vertical

Style guides and editorial standards are strong ontology inputs precisely because they encode reusable distinctions, applicability conditions, exceptions, and treatment rules.

They must not be flattened into one global checklist.

### 10.1 Candidate prior classes

- product/domain hard requirement;
- law/regulation or jurisdictional requirement;
- publication policy;
- house style;
- technical-writing standard;
- Wikipedia-like sourcing/verifiability convention;
- Chicago Manual of Style-like editorial convention;
- AP-like journalistic convention;
- domain-specific editorial standard;
- descriptive corpus-derived convention;
- advisory heuristic.

### 10.2 Candidate prior record

A prior may need:

- identity and version;
- authority/source provenance;
- rule class: hard requirement / normative / advisory / descriptive / heuristic;
- applicability conditions;
- excluded contexts;
- document types;
- audience or publication contexts;
- jurisdiction/domain;
- precedence or override semantics;
- exceptions;
- effective dates;
- supersession relationships;
- licensing/redistribution status;
- machine-testable predicate where possible;
- remediation guidance where appropriate.

### 10.3 Precedence is contextual

A rough default ordering may be useful:

`product/domain requirement > publication policy > house style > external style guide > generic heuristic`

but this must not become a universal hard-coded ladder. A goal contract or jurisdictional rule may override it. Some authorities apply to different dimensions and do not conflict at all.

### 10.4 Guide content and licensing

The repository must distinguish:

- an ontology inspired by general editorial concepts;
- a citation to an external authority;
- a paraphrased rule permitted by license/fair-use analysis;
- copyrighted guide text that cannot be redistributed.

No proprietary guide corpus may be committed or shipped simply because it is useful training or ontology material.

### 10.5 Prior conflicts are data

Conflicts, exceptions, supersession, and ambiguity should be representable rather than silently normalized away. A specialist agent should eventually be evaluated on choosing the applicable authority, not merely on repeating a global style preference.

## 11. Evidence, claims, and provenance vertical

The framework should make epistemic editorial work explicit.

### 11.1 Claim/evidence relationships

Candidate evidence relations include:

- supports;
- contradicts;
- qualifies;
- attributes;
- supersedes;
- reproduces;
- fails to verify.

A citation is not automatically proof that a claim is adequately supported. Source authority, relevance, freshness, and claim/source alignment may matter.

### 11.2 Evidence requirements may be gap-specific

A citation-needed gap may require a suitable supporting source.

A factual-contradiction gap may require comparing authoritative sources.

An API example gap may be best resolved by executable tests against a reference implementation.

An erratum may require tracing affected releases and downstream copies.

### 11.3 Provenance requirements

The system should preserve enough information to answer:

- why was this gap opened?
- what rule, source, test, or reviewer finding motivated it?
- who or what made the judgment?
- which model/tool/version was involved?
- what action was taken?
- what evidence justified the action?
- who approved or rejected it?
- what changed afterward?
- was the change later reverted, superseded, or reopened?

Human, agent, deterministic-tool, external-system, and model-grader actors must remain distinguishable.

## 12. Temporal/versioning vertical

The current temporal model distinguishes at least three scales.

### 12.1 Fine-grained operations

High-frequency, actor-attributed operations may include text edits, structured-node changes, citation attachment, gap creation, gap classification, review responses, and agent actions.

These may require causal ordering, concurrency semantics, or CRDT-compatible identities if live collaboration enters scope.

### 12.2 Semantic checkpoints

Meaningful editorial boundaries may include:

- draft created;
- review requested;
- review round completed;
- fact check completed;
- release candidate formed;
- published;
- erratum issued.

These are likely better units for many historical queries and eval instances than every keystroke.

### 12.3 Lifecycle releases

A release is a coarse externally meaningful checkpoint with an acceptance contract and provenance.

### 12.4 Exact reconstruction versus semantic reconstruction

The review must determine what historical guarantees are required.

Questions include:

- Must every character state be reconstructable exactly?
- Is semantic reconstruction at meaningful checkpoints sufficient?
- Must cursor/selection state be preserved?
- Must concurrent edit causality be reproducible?
- Must semantic identity survive split/merge/move operations?
- What is the canonical meaning of revert?
- How are derived metadata and grader outputs recomputed versus persisted?

### 12.5 Stable identity

Line numbers and byte offsets are inadequate long-term anchors for many editorial relationships. The favored direction is durable semantic identity for at least some objects.

The review must test whether stable identity belongs in the core representation, an overlay, or the operation-history layer.

## 13. Persistence architecture hypotheses

No product persistence backend is selected by this contract.

### 13.1 Git

Strengths:

- mature ecosystem;
- portable text history;
- docs-as-code interoperability;
- CI and publication workflows;
- review familiarity;
- disaster-recovery readability.

Weaknesses for the proposed semantic system:

- commit granularity may be too coarse;
- line/position identity is unstable;
- semantic relationships require another representation;
- relational historical queries require substantial reconstruction/ETL;
- collaborative high-frequency editing is awkward.

Current direction: Git is likely valuable as an interchange/publication projection even if it is not canonical product storage.

### 13.2 Dolt

Dolt is a strong candidate for versioned relational semantic state because rows, branches, commits, and diffs can be queried as data.

If selected, a key design principle would be to store semantically meaningful entities as independently addressable rows/relations rather than one giant opaque document blob.

Important forbidden assumption: the repository already contains a Dolt-backed Beads database under `.beads`; **that tracker implementation must not be treated as evidence that j-editorial itself should use Dolt**. If the product later selects Dolt, its database boundary must remain distinct from Beads tracker state.

### 13.3 PostgreSQL + temporal/event model

This must be treated as a serious control candidate, not dismissed because it lacks Git-like branding.

The review should compare Dolt against alternatives such as:

- ordinary PostgreSQL with append-only events;
- bitemporal tables;
- immutable revisions plus materialized current state;
- branch/workspace tables;
- event sourcing with snapshots.

Dolt should only win if its native branching/version semantics materially reduce complexity or enable capabilities that justify its operational tradeoffs.

### 13.4 DeltaDB / Delta-like model

DeltaDB is a strong architectural prior for fine-grained operations, stable operation identities, causal history, and collaboration between humans and agents.

It is not assumed to be a production dependency. Standalone API maturity, operational model, portability, data ownership, and integration constraints must be verified before adoption.

The architectural lesson to retain is the possibility that the durable primitive should be a causal operation stream from which intermediate states can be materialized, rather than only coarse commits.

### 13.5 CRDT / collaboration layer

A CRDT or equivalent operation model may be required for live collaborative authoring. It may belong in the authoring/application layer rather than the editorial core.

This must not be selected before collaboration requirements are explicit.

### 13.6 Object storage

Large source bundles, PDFs, images, screenshots, audio/video, raw traces, execution artifacts, and benchmark payloads may belong in object storage referenced by immutable identifiers/hashes.

### 13.7 Analytical storage

Large result sets and longitudinal benchmark telemetry may be better exported to Parquet, DuckDB, ClickHouse, a warehouse, or another analytical substrate instead of burdening the operational history store.

### 13.8 Persistence decision criteria

Any backend review should explicitly score:

- semantic queryability;
- historical queryability;
- branch/workspace semantics;
- merge/conflict behavior;
- stable identity support;
- high-frequency write behavior;
- collaboration requirements;
- storage efficiency;
- exact reconstruction guarantees;
- operational complexity;
- backup/restore maturity;
- local-first viability;
- hosted deployment viability;
- licensing;
- ecosystem maturity;
- migration/export path;
- analytical interoperability;
- benchmark-data extraction ergonomics.

## 14. Eval architecture vertical

An eval is any measurement procedure for a defined system behavior. A benchmark is a standardized, versioned eval or eval suite intended to make results comparable.

The system should measure explicit specialist capabilities instead of only final-document quality.

### 14.1 Candidate capability suite

- goal-contract interpretation;
- prior applicability;
- gap detection;
- gap classification;
- gap localization;
- severity estimation;
- confidence calibration;
- evidence requirement selection;
- evidence/source selection;
- remediation-policy selection;
- change prioritization;
- patch/edit generation;
- deterministic verification;
- semantic verification;
- gap closure;
- regression detection;
- review-response handling;
- release-readiness decision;
- abstention under insufficient evidence;
- end-to-end lifecycle improvement.

### 14.2 Eval-instance contract

A serious eval instance may need:

- instance ID;
- task/capability ID;
- artifact lineage ID;
- goal-contract version;
- prior/ontology bundle version;
- artifact state or state reference;
- authoritative source/evidence bundle;
- known gaps/findings where appropriate;
- expected observable behavior;
- allowed tools;
- token/time/action budgets;
- grader specification;
- infrastructure specification;
- split membership and lineage boundary;
- difficulty/slice metadata;
- provenance and content hashes.

### 14.3 Grader hierarchy

The current preference is to use the strongest grader that directly measures the construct:

1. deterministic/executable checks;
2. structured comparison against authoritative state;
3. domain-specific validators;
4. model grading where direct measurement is unavailable;
5. human/expert judgment where preference, ambiguity, or high consequence requires it.

This is not a rigid ordering. Some tasks necessarily require humans; some model graders may be useful for scale; some deterministic checks may measure only superficial proxies.

### 14.4 Model graders require meta-evaluation

If an LLM judges clarity, source adequacy, remediation quality, or another property, the grader itself should be tested against human/expert labels, disagreement cases, perturbations, and known biases.

A grader-version change can invalidate direct score comparability.

### 14.5 Historical transitions are useful eval material

A real transition can produce tasks such as:

- detect the historical deficiency;
- classify the deficiency;
- choose among remediation candidates;
- identify the evidence required;
- distinguish an accepted correction from a regression;
- decide whether the artifact was release-ready.

The historical patch itself should not automatically be the exact-match target.

### 14.6 Synthetic perturbations

Controlled defect injection can complement real history.

Given a verified state `S*`, the benchmark may introduce known perturbations such as:

- delete a citation;
- alter a numeric fact;
- substitute stale terminology;
- remove an endpoint;
- corrupt an enum;
- break an executable example;
- introduce ambiguity;
- reorder procedural steps;
- add a style-rule violation.

Synthetic gaps provide exact intervention ground truth and systematic ontology coverage. They must be designed carefully enough to avoid artificial shortcuts.

## 15. Evaluation metrics under review

No single metric is sufficient.

### 15.1 Gap detection

`precision = valid_detected_gaps / all_reported_gaps`

`recall = detected_true_gaps / all_true_gaps`

False positives matter because an agent that constantly invents editorial problems creates unnecessary work and can damage correct content.

### 15.2 Gap typing

`typing_accuracy = correctly_typed_gaps / evaluated_gaps`

Hierarchical ontology metrics may be needed when a prediction is partially correct at a parent class.

### 15.3 Gap closure

`closure_rate = correctly_resolved_gaps / attempted_gaps`

### 15.4 Regression rate

`regression_rate = previously_passing_requirements_now_failing / previously_passing_requirements`

A specialist editor must be rewarded for preserving what was already correct.

### 15.5 Regression-adjusted progress

A candidate derived metric may resemble:

`RGC = (Σ weight(resolved_gaps) - λ * Σ weight(introduced_gaps)) / Σ weight(target_gaps)`

The exact weighting and penalty policy is unresolved and vulnerable to Goodharting.

### 15.6 Release decisions

Track false-release and false-hold errors separately.

For high-consequence documentation, a false release may be materially more costly than an unnecessary hold. The metric must preserve that asymmetry rather than burying it inside raw accuracy.

### 15.7 Calibration

Confidence should be evaluated, not merely displayed. If the agent assigns `0.9` confidence to a class of judgments, roughly comparable judgments should be correct near that frequency under a well-calibrated system.

### 15.8 Pairwise preference

Historical accepted/rejected alternatives and expert comparisons may support pairwise ranking metrics where exact-match grading is inappropriate.

### 15.9 Operational metrics

End-to-end agent benchmarks should also measure:

- wall-clock time;
- model/API cost;
- token consumption;
- number of actions;
- number of tool calls;
- human interventions;
- infrastructure failures;
- retries;
- abstention rate.

### 15.10 Statistical treatment

Benchmark reports should include uncertainty where sample sizes and task structure allow it. Paired comparisons on the same instances are generally more informative than comparing two isolated aggregate means.

Important slices should be reported separately rather than hidden by a global average.

## 16. Benchmark quality criteria

A benchmark is useful only if it supports a decision.

The review should require each benchmark to state:

- the construct being measured;
- the target population/distribution;
- whether it is representative, adversarial, synthetic, or mixed;
- the decision the benchmark informs;
- the grader and its known limitations;
- sample size and uncertainty;
- important slices;
- contamination controls;
- execution/scaffold configuration;
- failure/infrastructure separation;
- expected refresh/saturation policy.

Warning signs include:

- score saturation;
- tiny leaderboard differences relative to uncertainty;
- prompt-template sensitivity larger than model differences;
- obvious contamination;
- benchmark items appearing in training corpora;
- one aggregate hiding severe slice regressions;
- model-judge scores with no grader validation;
- synthetic items containing shortcuts;
- improvements that do not correlate with useful product behavior.

## 17. Training-data vertical

**Held:** this section reserves downstream questions. No dataset research, corpus construction, labeling, split generation, preference extraction or training is released by the Phase 2 merge or Phase 3 research.

### 17.1 Transition supervision

The favored historical training primitive is:

`state_before + gaps_before + evidence/context + action + outcome + state_after + gaps_after`

This supports more than prose imitation. It can teach diagnosis, prioritization, evidence selection, remediation, verification, and release judgment.

### 17.2 Pairwise supervision may be stronger than absolute labels

Many editorial histories support claims such as:

`state_after preferred_to state_before with respect to correctness`

or:

`accepted_patch preferred_to rejected_patch under goal_contract G`

This may be more defensible than assigning arbitrary absolute scores such as `0.638 -> 0.701`.

### 17.3 Negative and ambiguous examples matter

Useful historical signals include:

- accepted edits;
- rejected edits;
- reverts;
- post-publication errata;
- review findings;
- contradictory reviewer opinions;
- changes later superseded;
- agent regressions;
- unnecessary edits;
- valid alternative edits.

### 17.4 Train/dev/test isolation

Do not randomly split adjacent revisions.

Candidate split boundaries include:

- artifact;
- artifact family;
- repository/project;
- author/team where leakage is material;
- domain;
- time.

A temporal holdout is strongly favored for at least one final evaluation layer because it better tests performance on genuinely future editorial states.

### 17.5 Contamination policy

The review must define:

- what counts as contamination;
- how near-duplicate snapshots are detected;
- whether style-guide priors shared across train/test are acceptable;
- how synthetic perturbation templates are split;
- what happens when a held-out item enters training;
- how benchmark revisions preserve comparability.

## 18. Specialist-agent vertical

The initial specialist agent is currently modeled as a typed editorial workflow rather than an unconstrained text generator:

`inspect -> diagnose -> prioritize -> source -> edit -> verify -> resolve / abstain`

### 18.1 Candidate typed operations

- `OPEN_GAP`;
- `CLASSIFY_GAP`;
- `RECLASSIFY_GAP`;
- `ATTACH_EVIDENCE`;
- `REJECT_EVIDENCE`;
- `QUALIFY_CLAIM`;
- `REVISE_CLAIM`;
- `ADD_CITATION`;
- `REMOVE_CITATION`;
- `ADD_BLOCK`;
- `MOVE_BLOCK`;
- `REMOVE_BLOCK`;
- `RESPOND_TO_REVIEW`;
- `RESOLVE_GAP`;
- `REOPEN_GAP`;
- `ABSTAIN`;
- `PROPOSE_RELEASE`;
- `PROPOSE_HOLD`.

This vocabulary is provisional.

### 18.2 Behavioral constraints to test

A useful specialist agent should be evaluated on whether it:

- distinguishes fact verification from citation formatting;
- seeks evidence before making unsupported factual corrections;
- makes the smallest justified change where possible;
- preserves already-valid content;
- recognizes when a style rule is inapplicable;
- detects conflicts between priors;
- does not invent sources;
- does not convert uncertainty into false certainty;
- can abstain when evidence is insufficient;
- can explain what release condition remains unmet;
- can verify its own patch with independent checks where available.

### 18.3 Agent score is system score

An agent benchmark measures the configured system, including prompts, tools, retrieval, budgets, model version, execution environment, and verification scaffold. Results must not be attributed to the base model alone unless the experiment is designed to isolate it.

## 19. Data products and interchange formats

No canonical file layout is approved, but the following format roles are plausible and should be reviewed.

### Structured records

- JSON / JSONL for interoperable event and eval records;
- YAML or JSON for human-reviewed contracts/manifests;
- relational tables for operational semantic state;
- Parquet for large analytical/eval result exports.

### Text projections

- Markdown for docs-as-code publication/interchange;
- HTML for rendered output;
- unified diffs/patches where text-oriented tooling requires them.

### Large or binary evidence

- content-addressed object storage for PDFs, images, video, audio, source bundles, execution artifacts, and raw traces.

### Reproducibility metadata

- content hashes;
- commit/revision identifiers;
- container digests where execution matters;
- tool/model/grader versions;
- immutable benchmark manifests.

The review should distinguish **canonical state**, **portable export**, **analytical derivative**, and **cache**. A format may serve one role without serving the others.

## 20. Results processing and reporting

A benchmark run should retain enough detail to reconstruct the path from instance to aggregate.

Candidate per-instance output includes:

- instance ID;
- model/agent configuration;
- raw output or patch;
- normalized output;
- tool trace where policy permits;
- grader observations;
- deterministic test results;
- gap changes;
- regressions introduced;
- confidence;
- latency;
- token/cost data;
- infrastructure status;
- artifact references;
- provenance.

Aggregate reporting should be capable of showing:

- current result;
- baseline result;
- delta;
- uncertainty/confidence interval where appropriate;
- important slices;
- false-release/false-hold rates;
- gap precision/recall;
- regression rate;
- cost and latency;
- examples of representative failures;
- grader disagreement.

A single headline score must never be the only inspection surface.

## 21. Versioning and reproducibility vertical

The framework needs explicit version semantics for all score-affecting components.

Candidate versioned objects include:

- artifact schema;
- goal-contract schema and instances;
- gap ontology;
- prior bundles;
- evidence schemas;
- transition/event schema;
- dataset/corpus;
- split manifest;
- synthetic perturbation generator;
- benchmark suite;
- eval instance;
- grader;
- model-judge prompt;
- harness;
- aggregation logic;
- agent scaffold;
- model/checkpoint;
- tool interfaces;
- execution container/environment.

Version identity may use semantic versions, content hashes, commit IDs, or combinations depending on the object.

Rules to review:

- silently changing an eval and keeping the same benchmark identity is prohibited;
- results from materially different benchmark versions should not be treated as directly comparable without an explicit bridge analysis;
- label corrections should preserve audit history;
- migration logic should distinguish schema migration from semantic reinterpretation;
- generated results should reference immutable inputs whenever possible.

## 22. Security, privacy, licensing, and governance vertical

These are architecture requirements, not later compliance polish.

### 22.1 Sensitive source material

Editorial corpora may contain proprietary documents, personal information, unpublished drafts, legal records, customer data, or licensed reference material.

The review must define:

- access control;
- encryption requirements;
- retention policy;
- audit policy;
- redaction/anonymization;
- training eligibility;
- benchmark eligibility;
- export controls where applicable.

### 22.2 Right to erasure versus immutable history

Append-only provenance and regulatory/privacy deletion can conflict. The system must not promise both perfect immutability and guaranteed physical erasure without a concrete design.

Possible mechanisms to review include encryption-key destruction, indirection, tombstoning, redacted historical projections, or segregated sensitive payloads.

### 22.3 Copyright and editorial guides

The ontology layer must not become an unlicensed reproduction of proprietary style guides.

### 22.4 Executable graders

Code snippets, generated patches, examples, and validators may require sandboxing. Executable evals must define trust boundaries, network policy, filesystem policy, timeouts, resource limits, and secret handling.

### 22.5 Prompt injection and hostile documents

If agents inspect arbitrary documents or external sources, document content itself may be adversarial. Source text must not automatically be treated as trustworthy instructions to the evaluating/authoring agent.

### 22.6 Supply-chain integrity

Benchmark fixtures, tool dependencies, containers, external sources, and model endpoints may affect results and security. Provenance and integrity checks should be part of the design where material.

## 23. Logical module boundaries under review

No repository directories or packages are authorized by this section. These are conceptual boundaries only.

Candidate modules include:

- editorial/domain core;
- document representation;
- identities/anchors;
- operations/event history;
- goal-contract engine;
- gap ontology/engine;
- prior registry/applicability/conflict engine;
- evidence/claim verification;
- persistence adapters;
- import/export/projection;
- eval core;
- graders;
- benchmark manifests/suites;
- dataset builder;
- synthetic perturbation engine;
- contamination/split tooling;
- specialist-agent runtime;
- analytics/statistics/reporting;
- application/API surfaces.

The intended dependency direction should keep editorial semantics independent of eval and agent infrastructure.

## 24. Initial ADR queue for adversarial review

**Do not create ADR files yet.** This is the decision queue that the review must attack, merge, split, reorder, or delete.

### Domain and representation

1. Canonical editorial-state boundary.
2. Artifact versus document versus publication semantics.
3. Structured document representation versus canonical source text.
4. Stable semantic identity and anchor guarantees.
5. Claim model and claim granularity.
6. Gap versus finding versus obligation versus violation semantics.
7. Goal-contract schema, inheritance, and lifecycle.
8. Quality-vector semantics and whether any scalar is allowed.
9. Release-readiness and lifecycle-state model.

### Ontology, prior, and evidence

10. Editorial-gap ontology architecture.
11. Ontology extensibility across editorial verticals.
12. Normative-prior registry.
13. Prior applicability, precedence, exception, and conflict rules.
14. Style-guide licensing and derived-rule policy.
15. Evidence/source model.
16. Claim/evidence relation model.
17. Provenance and actor identity model.

### Temporal and persistence

18. Fine-grained operation model.
19. Semantic-event model.
20. Snapshot/checkpoint semantics.
21. Exact versus semantic historical reconstruction guarantees.
22. Concurrency/collaboration requirements.
23. CRDT requirement and boundary, if any.
24. Git interoperability/publication boundary.
25. Dolt versus PostgreSQL/event-store versus other semantic-history backends.
26. DeltaDB/Delta-like operation-layer applicability.
27. Object-storage boundary.
28. Analytical-storage/telemetry boundary.
29. Backup, restore, export, and migration guarantees.

### Eval, benchmark, and training

30. Eval-instance contract.
31. Benchmark-suite manifest and version model.
32. Grader taxonomy and selection policy.
33. Model-judge meta-evaluation policy.
34. Per-instance result/provenance contract.
35. Metric suite and statistical policy.
36. Historical-transition dataset contract.
37. Synthetic-gap generation and validation policy.
38. Train/dev/test lineage and temporal split policy.
39. Contamination detection and benchmark retirement policy.
40. Benchmark refresh/saturation policy.
41. Agent capability decomposition.
42. Typed specialist-agent operations.
43. Abstention and confidence-calibration policy.
44. End-to-end lifecycle benchmark contract.

### Security, governance, and interoperability

45. Sensitive-data classification and retention.
46. Deletion/right-to-erasure semantics.
47. Copyright/licensing governance.
48. Executable-grader sandbox boundary.
49. Hostile-content/prompt-injection boundary.
50. Import/export round-trip guarantees.
51. Public API/domain boundary.
52. Versioning policy for score-affecting components.

## 25. Required adversarial review questions

The review must attempt to falsify, not merely confirm, the current model.

### Representation

- Is a structured internal model actually necessary?
- Can stable semantic identity be layered over source text?
- What information would be lost by treating Markdown as canonical?
- What complexity is introduced by structured round-tripping?
- Which semantic entities truly require durable IDs?

### Gap model

- Are gaps the correct central intermediate representation?
- Are obligations, findings, claims, review comments, and risks materially different entities?
- Can overlapping and nested gaps be represented without combinatorial complexity?
- Can the ontology span technical docs, journalism, research, and general writing without becoming meaningless?
- Which gap classes are objective enough for deterministic detection?

### Priors

- Which priors are hard requirements, normative conventions, descriptive observations, or heuristics?
- How are conflicts and exceptions represented?
- How does scope inheritance work?
- Can generic style priors override domain language accidentally?
- What guide-derived material can legally be stored and redistributed?

### Evidence

- What makes a source authoritative for a particular claim?
- How are contradictory sources represented?
- How is source freshness tracked?
- When is a citation insufficient even if syntactically present?
- How is unresolved uncertainty preserved?

### History

- What is the minimum useful historical unit?
- What must be exactly reconstructable?
- Which high-frequency operations deserve durable storage?
- What happens when a semantic node is split, merged, or moved?
- How are reverted, cherry-picked, and concurrently authored changes represented?

### Storage

- Does Dolt materially outperform PostgreSQL plus temporal/event tables for the actual workload?
- Is branching semantic state a core product requirement or an attractive but unnecessary feature?
- Is a CRDT a core requirement or an authoring-client concern?
- What operational complexity does each backend introduce?
- What is the credible migration path if a storage choice is wrong?

### Evals

- Which capabilities have defensible ground truth?
- Which are preference judgments?
- What benchmark tasks can be gamed through artifacts or shortcuts?
- Which metrics are vulnerable to Goodharting?
- What sample size is needed for useful decisions?
- What are the expensive/rare failure modes that must be oversampled?
- How should infrastructure failures be separated from model failures?
- How do we know an eval predicts production usefulness?

### Training

- When is an accepted historical edit actually a useful target?
- How do we use rejected, reverted, and superseded edits?
- How do we prevent neighboring snapshot leakage?
- How do we prevent synthetic perturbation generators from creating trivial signatures?
- How are benchmarks refreshed after their examples become training data?

### Product boundary

- Which capabilities belong in `j-editorial` versus a downstream writing product?
- Which belong in the editorial framework versus the eval subsystem?
- Which should eventually be separate packages or repositories?
- Can the editorial core remain useful with no model provider configured?

## 26. Adversarial review protocol

The review phase should not merely produce comments. Each material architecture vertical should eventually produce a decision packet containing, at minimum:

1. the problem and decision to be made;
2. assumptions being challenged;
3. at least one credible alternative to the favored direction;
4. evidence or prototype results where needed;
5. failure modes and reversibility;
6. migration/exit path if the decision is wrong;
7. explicit acceptance criteria;
8. unresolved objections;
9. recommendation: accept / narrow / defer / reject / research further.

Storage decisions should be based on representative workload experiments rather than feature-table aesthetics where feasible.

Ontology decisions should be tested against examples from more than one editorial vertical before claiming generality.

Eval decisions should be tested against both real historical cases and controlled synthetic cases before claiming benchmark validity.

## 27. Review exit criteria

Implementation remains blocked until the owner explicitly closes the adversarial review and the review has produced enough resolution to support a minimal vertical slice.

At minimum, the implementation release should have:

- an accepted or explicitly provisional domain glossary;
- a resolved boundary between artifact state, gaps/findings/obligations, priors, evidence, and operations;
- a decision on the minimum canonical representation requirements;
- explicit historical reconstruction requirements;
- a persistence decision process or accepted initial persistence ADR;
- a versioning/provenance contract;
- a defined first ontology slice;
- a defined first goal-contract slice;
- a defined first eval-instance contract;
- a defined train/dev/test contamination policy for any model work;
- a defined security/privacy/licensing baseline;
- a narrowly scoped first end-to-end use case;
- explicit owner authorization to leave `ADVERSARIAL-REVIEW-REQUIRED`.

The review is allowed to simplify the architecture substantially. Deleting unnecessary machinery is a successful review outcome.

## 28. Bootstrap constraints

Until the adversarial review gate passes:

- do not create the proposed product repository tree;
- do not create ADR files merely to make the queue look complete;
- do not commit product implementation code;
- do not freeze a programming language or framework;
- do not freeze Dolt, PostgreSQL, Git, DeltaDB, or a CRDT as the product backend;
- do not create production schemas or migrations;
- do not ingest proprietary editorial-guide content;
- do not create training, development, or held-out corpora;
- do not publish benchmark scores or capability claims;
- do not represent provisional architecture as accepted design;
- do not use the Beads Dolt backend as the product database by accident;
- do not create competing Markdown TODO/task systems.

Permitted repository artifacts remain limited to:

- repository metadata;
- Beads initialization/integration artifacts;
- agent integration files produced by Beads or explicitly requested by the owner;
- this `BOOTSTRAP.md` contract;
- additional adversarial-review artifacts only when explicitly authorized by the owner.

## 29. Beads workflow

This repository uses [Beads (`bd`)](https://github.com/gastownhall/beads) for durable task tracking and agent workflow context.

Agents working from a local checkout should begin with:

```bash
bd prime
bd ready
```

Use:

```bash
bd show <id>
bd update <id> --claim
bd close <id>
bd remember "<durable project insight>"
```

as appropriate to the active work.

Do not manually edit Beads database state or treat `.beads/issues.jsonl` as the source of truth. Follow `AGENTS.md` and the Beads-generated integration guidance for sync/commit behavior.

Beads' own use of Dolt is infrastructure for the issue tracker and is architecturally separate from the unresolved product persistence decision described in this document.

## 30. Change control during bootstrap

While `ADVERSARIAL-REVIEW-REQUIRED` is active:

- `BOOTSTRAP.md` is the only architecture contract presently authorized;
- changes to this contract should preserve the distinction between invariants, provisional directions, and open questions;
- an agent may not convert a provisional direction into an implementation decision without explicit owner authority or a later accepted decision record;
- explicit owner instructions may amend this contract;
- if repository guidance, Beads work, and this file conflict, the conflict must be surfaced rather than silently resolved by implementation;
- every implementation agent must read this file before creating product structure or code once implementation is eventually released.

## 31. Current gate

**`ADVERSARIAL-REVIEW-REQUIRED`**

No architecture decision in this document is accepted merely because it is recorded here.

No full repository structure, production schema, benchmark corpus, agent runtime, or application implementation is authorized yet.

The gate is released only by explicit owner instruction after the adversarial review has either closed the material gaps above or consciously accepted the remaining risks.