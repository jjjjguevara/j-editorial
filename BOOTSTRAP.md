# j-editorial — Bootstrap Contract

Status: **pre-implementation / adversarial review**

This document records the initial product and architecture contract for `jjjjguevara/j-editorial`. It is intentionally a bootstrap boundary, not an implementation specification. No production directory tree, ADR set, schema, ontology, benchmark corpus, persistence layer, agent runtime, or application code should be created until the adversarial review cycle closes the material gaps and explicitly releases implementation.

## 1. Mission

`j-editorial` is an editorial framework for representing, versioning, evaluating, and improving artifacts across a Document Development Lifecycle. It is intended to support docs-as-code workflows and non-code writing products that need Git-like history without making files, lines, or Git commits the canonical domain model.

The framework should make editorial state machine-legible enough to support specialist agents, custom evals, benchmark generation, provenance, and release decisions while remaining useful independently of ML or agentic workflows.

## 2. Core model under review

The current working model is:

`Goal Contract + Normative Priors + Artifact State + Gap Field + Evidence + Editorial Operations + Outcomes`

This is a hypothesis to be challenged during review, not a frozen schema.

### 2.1 Artifact state

An artifact is not assumed to be canonically equivalent to one Markdown file. The current hypothesis is that meaningful document entities may require stable semantic identities so that sections, blocks, claims, citations, gaps, review findings, and related objects can survive movement and revision.

Markdown, HTML, Git repositories, and other formats are therefore candidate projections/import-export surfaces rather than automatically canonical storage.

### 2.2 Goal contracts

A free-text description of a document's purpose is useful but insufficient as an evaluation contract. The current proposal is to compile or refine that intent into an explicit, versioned goal contract describing at least:

- purpose;
- audience;
- required outcomes or coverage;
- release blockers;
- desirable but non-blocking properties;
- non-goals;
- authoritative sources or evidence classes where applicable.

Goal-contract design, authoring ergonomics, inheritance, and machine generation remain open questions.

### 2.3 Quality and release state

Lifecycle stage, document quality, and release readiness must remain distinct concepts.

The framework should not assume that editorial progress is monotonic or that publication means epistemic perfection. A published document may later receive errata, become stale, or regress relative to a changed source of truth.

The current proposal therefore favors multidimensional quality observations plus explicit release gates over a canonical scalar `0..1` quality score. Scalar summaries may be derived if they are useful and interpretable.

### 2.4 Editorial gaps

Editorial gaps are first-class candidate entities rather than generic deficiencies or scalar penalties. Examples include:

- citation needed;
- fact-check required;
- factual contradiction;
- erratum;
- stale claim;
- stub or missing section;
- missing example;
- structural defect;
- terminology inconsistency;
- style-rule violation;
- audience/usability deficiency;
- unresolved review finding;
- release blocker.

A gap may require dimensions such as type, target, affected quality dimension, severity, confidence, evidence requirement, remediation policy, expected cost, and release significance.

The ontology, taxonomy boundaries, inheritance model, weighting model, and representation of overlapping gaps are unresolved and must be reviewed adversarially before implementation.

### 2.5 Normative priors

Editorial/style authorities are a natural ontology/prior source, but they are not interchangeable and must not be flattened into one universal rule set.

Candidate prior families include:

- product/domain requirements;
- publication policy;
- house style;
- technical-writing standards;
- Wikipedia-like verifiability and sourcing principles;
- Chicago Manual of Style;
- AP style;
- domain-specific standards;
- advisory heuristics.

The system must preserve provenance, applicability, version, exceptions, and precedence. Conflicts between authorities must be explicit and resolvable by context rather than silently collapsed.

No external editorial guide is assumed to be freely redistributable; licensing and transformation rights must be reviewed before any guide-derived ontology is committed or shipped.

### 2.6 Evidence and provenance

The framework should preserve enough provenance to answer why a gap was opened, why an action was taken, which evidence supported it, who or what performed the action, how it was verified, and what outcome followed.

Human, agent, deterministic-tool, and model-grader actions must remain distinguishable.

## 3. Temporal model under review

The current design distinguishes three temporal scales:

1. **Fine-grained operations** — high-frequency, actor-attributed changes and actions.
2. **Semantic snapshots/checkpoints** — queryable editorial states at meaningful boundaries.
3. **Lifecycle releases** — coarse states such as draft, review, release candidate, publication, erratum, and deprecation.

The system should be able to materialize historical state and explain transitions without assuming that a Git commit is the only meaningful unit of change.

## 4. Persistence hypotheses — not final decisions

No persistence backend is selected by this bootstrap contract.

The current candidates and hypotheses are:

### Git

Useful for interoperability, publication, CI, external review, static artifacts, and portable exports. It is not currently favored as the sole canonical backend because commits and line-based diffs are too coarse for many semantic editorial and eval queries.

### Dolt

A strong candidate for versioned semantic state because structured entities, branches, history, and diffs can be queried relationally. If adopted, documents should not be reduced to giant opaque text rows; semantically meaningful entities should remain independently addressable.

### DeltaDB / Delta-like operation model

A strong architectural prior for fine-grained operations, stable identities, causal provenance, and collaborative/agentic editing. It is not assumed to be a deployable dependency until its standalone product/API maturity and integration model are verified.

### Operation/CRDT layer

A separate operation log or CRDT layer may be required for live collaborative editing and high-frequency changes even if Dolt or another database owns semantic checkpoints.

### Object and analytical storage

Large evidence bundles, binaries, traces, and benchmark payloads may belong in object storage. High-volume analytical telemetry may belong in Parquet/DuckDB/a warehouse rather than the operational history store.

All of these boundaries remain review items.

## 5. Eval and benchmark model under review

The evaluation system should measure explicit specialist capabilities rather than only final-document quality.

Candidate capabilities include:

- goal interpretation;
- prior applicability;
- gap detection;
- gap typing;
- severity/confidence estimation;
- evidence selection;
- remediation selection;
- patch/edit generation;
- verification;
- gap closure;
- regression detection;
- release-readiness decisions;
- calibrated abstention;
- end-to-end lifecycle improvement.

The strongest available grader should be used for each property. Deterministic and executable checks should be preferred where they measure the construct directly; structured comparison, model grading, and human review should be used where appropriate rather than forcing every criterion through an LLM judge.

Per-instance observations and provenance are primary data. Aggregate scores are derived views.

## 6. Training-data hypothesis

Historical editorial transitions may provide stronger supervision than absolute scalar quality labels.

A candidate training/eval unit is:

`state_before + gap_field_before + action + evidence + review/outcome + state_after`

Historical accepted edits are evidence of editorial decisions, not automatically unique gold completions. Multiple valid edits may exist.

Observed historical gaps and controlled synthetic perturbations should be considered complementary:

- observed gaps provide ecological validity;
- synthetic gaps provide exact labels, systematic ontology coverage, and controlled difficulty.

Training, development, and held-out evaluation data must be separated by lineage rather than random neighboring snapshots. Artifact family, project, and time are candidate split boundaries. Contamination policy remains to be specified.

## 7. Agent hypothesis

The specialist agent is currently modeled as a typed editorial state machine rather than an unconstrained prose generator:

`inspect -> diagnose -> prioritize -> source -> edit -> verify -> resolve / abstain`

Candidate typed operations include opening/classifying gaps, attaching evidence, revising claims, adding citations, moving structural blocks, resolving gaps, abstaining, and proposing release.

This state machine and operation vocabulary are provisional and must be challenged before implementation.

## 8. Architectural dependency direction

The editorial framework must remain useful without ML.

The current intended dependency direction is:

`eval/benchmarking -> editorial core`

and not:

`editorial core -> eval/benchmarking`

An eventual writing product, CMS, research workflow, newsroom system, legal-document workflow, or docs-as-code tool should be able to consume the editorial core without depending on agent/eval infrastructure.

## 9. Initial ADR queue for adversarial review

No ADR files are to be created yet. The review cycle should decide whether the following proposed decision areas are valid, missing, incorrectly scoped, or prematurely coupled:

1. canonical editorial state;
2. structured document representation versus canonical source text;
3. stable semantic identity;
4. operation log versus snapshots;
5. semantic-history database selection;
6. Git interoperability/publication boundary;
7. editorial-gap ontology;
8. normative-prior registry and precedence;
9. goal-contract model;
10. multidimensional quality representation;
11. release-readiness gates;
12. evidence and provenance model;
13. deterministic/model/human grader hierarchy;
14. per-instance eval record contract;
15. historical transition model;
16. synthetic gap generation;
17. train/dev/test and contamination policy;
18. typed specialist-agent operations;
19. large-object/evidence storage;
20. analytical telemetry boundary;
21. versioning of every score-affecting component;
22. privacy, licensing, retention, and deletion semantics;
23. collaboration/concurrency semantics;
24. import/export fidelity and round-tripping;
25. security/trust boundaries for agents and executable graders.

## 10. Required adversarial review questions

Before implementation, the review should attempt to falsify at least these assumptions:

- Is a structured internal document model actually necessary, or can stable semantic identity be layered over source text?
- Are gaps truly the best intermediate representation, or are obligations, claims, findings, and unresolved states materially different entities?
- Can one ontology span prose, technical documentation, journalism, research, and other writing verticals without becoming meaningless?
- How should overlapping, nested, contradictory, or uncertain gaps be represented?
- Which priors are normative, descriptive, advisory, or jurisdiction/domain-specific?
- How are prior conflicts, exceptions, supersession, and licensing handled?
- What is the smallest useful goal-contract representation?
- What is the right unit of editorial history: character operation, semantic operation, review event, snapshot, or some combination?
- What guarantees are required for stable anchors through restructuring?
- Does Dolt materially improve the system over Postgres plus temporal/event tables, or only add operational complexity?
- Is a CRDT required in the core or only in collaborative authoring clients?
- What must be reconstructable exactly versus semantically?
- Which eval dimensions have defensible ground truth, and which are inherently preference judgments?
- What metrics are susceptible to Goodharting?
- How do we prevent benchmark history from contaminating specialist-agent training?
- How are human decisions treated when the historical edit was later reverted or contradicted?
- How do we distinguish accepted style preference from factual improvement?
- How are privacy-sensitive source materials and proprietary editorial guides handled?
- How should deletion/right-to-erasure interact with immutable provenance?
- What constitutes a release blocker across different editorial verticals?
- Which parts belong in `j-editorial`, and which should eventually become separate packages or repositories?

## 11. Bootstrap constraints

Until the adversarial review gate passes:

- do not create the proposed full repository structure;
- do not create ADR files;
- do not commit product implementation code;
- do not freeze a database or programming-language choice;
- do not ingest proprietary editorial-guide content;
- do not create training or held-out corpora;
- do not publish benchmark claims;
- do not represent provisional architecture as accepted design.

Permitted bootstrap artifacts are limited to repository metadata, Beads' own initialization artifacts, agent/tracker guidance produced by Beads, and this `BOOTSTRAP.md` contract unless the owner explicitly expands scope.

## 12. Beads workflow

This repository uses [Beads (`bd`)](https://github.com/gastownhall/beads) for issue/task tracking and durable agent workflow context.

After the repository exists locally with `bd` installed, initialize Beads with:

```bash
bd init
```

Use the Beads-generated agent guidance and tracker state as authoritative for task workflow. Do not manually edit Beads' generated database state or use Markdown TODO lists as a competing task tracker.

The adversarial review should be represented as Beads work only after the owner decides how to decompose and gate that review.

## 13. Bootstrap gate

**Current gate:** `ADVERSARIAL-REVIEW-REQUIRED`

No architecture decision in this document is accepted merely because it is recorded here.

Implementation is released only when the owner explicitly closes the adversarial review cycle and authorizes bootstrapping the accepted architecture.
