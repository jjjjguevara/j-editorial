# j-editorial — Product Roadmap

Status: **provisional / bootstrap-gated**  
Authority: **subordinate to `BOOTSTRAP.md` until the bootstrap review gate closes**  
Current horizon: **bootstrap → specification → reusable core → Doc Doctor reference integration**  
Roadmap role: **product progression, capability gates, proof obligations, and pivot register**

This roadmap describes how `j-editorial` could progress from an editorial framework into reusable evaluation infrastructure and, if the evidence supports it, a backend platform for writing products.

It is intentionally detailed about **capabilities, boundaries, proof obligations, and possible product surfaces**, while remaining intentionally non-binding about implementation architecture. Nothing in this file selects a canonical document model, persistence engine, programming language, cloud architecture, agent framework, database, CRDT, model provider, deployment model, commercial packaging, or repository layout unless a later accepted decision explicitly does so.

`BOOTSTRAP.md` remains the controlling pre-implementation contract. If this roadmap conflicts with a bootstrap invariant, the bootstrap contract wins. If bootstrap review falsifies a roadmap assumption, the roadmap must change.

The roadmap therefore answers:

> **If the bootstrap hypotheses survive, what could `j-editorial` coherently become, in what order should those capabilities be proved, and what evidence should cause the project to change direction?**

It does **not** answer:

> **What must be implemented now?**

---

## 0. Roadmap contract

### 0.1 This is a capability roadmap, not a release calendar

Progression is defined by evidence and capability gates, not dates, quarters, promised versions, or feature-count milestones.

A later stage is not unlocked because an earlier stage shipped. It is unlocked when the earlier stage produces enough evidence that the next product hypothesis is worth testing.

### 0.2 Roadmap stages are hypotheses

The named stages in this document are working product boundaries. Bootstrap or later evidence may:

- merge stages;
- split stages;
- reorder stages;
- rename products;
- eliminate products;
- discover that an embedded library is sufficient where a hosted service had been imagined;
- discover that one universal abstraction should instead become several interoperable profiles;
- discover that Doc Doctor should remain the flagship product rather than merely a reference implementation;
- discover that benchmarking should become the product center rather than one downstream surface;
- discover that a control plane is unnecessary or belongs in a separate project.

No stage has existential priority over evidence.

### 0.3 Roadmap vocabulary

#### Hypothesis

A proposition the product progression currently assumes long enough to test.

#### Proof obligation

Evidence required before relying on a hypothesis downstream.

#### Capability gate

Conditions that should be satisfied before a downstream stage is treated as justified.

#### Pivot trigger

Evidence that should cause reconsideration, redesign, narrowing, or abandonment of a direction.

#### Deferred decision

A choice intentionally left unresolved because deciding it now would harden assumptions prematurely.

#### Validated direction

A direction promoted from hypothesis after review and evidence. Validation does not make it permanent; later evidence can reopen it.

#### Reference implementation

A product that demonstrates the framework in a real environment without becoming the canonical location of framework semantics.

### 0.4 Authority order during bootstrap

Until the bootstrap gate closes, authority is:

1. explicit owner constraints;
2. `BOOTSTRAP.md`;
3. accepted ADRs, when they begin to exist;
4. this `ROADMAP.md`;
5. issue/task descriptions;
6. incidental repository structure or implementation precedent.

An existing implementation is evidence, not automatic architecture.

---

## 1. Product thesis

Most writing software can represent text, metadata, and revisions. It usually represents much less about:

- what the artifact is trying to accomplish;
- which obligations apply to it;
- what is wrong, missing, unsupported, stale, ambiguous, structurally weak, or release-blocking;
- what evidence supports or contradicts a claim;
- why a change was proposed;
- what editorial operation the change attempted;
- whether an intervention resolved its target condition;
- what new regressions an intervention introduced;
- how reviewer disagreement should be represented;
- what conditions made an artifact acceptable for release;
- how an agent, prompt, policy, or model performs on those editorial judgments;
- whether quality improved across a sequence of interventions rather than at one snapshot;
- which parts of production history are useful as supervision and which are merely historical behavior.

The central `j-editorial` hypothesis is that there is a reusable semantic and evaluation layer between **raw text/history** and **writing-product behavior**.

The prospective progression is:

```text
editorial semantics
        ↓
reusable editorial runtime
        ↓
reference writing product
        ↓
reproducible evaluation infrastructure
        ↓
portable policy / benchmark ecosystem
        ↓
reusable writing-product backend
        ↓
production quality / eval control plane
```

The project should remain useful even if the final progression stops before the last stage.

A successful `j-editorial` core does not require a SaaS product. A successful evaluation framework does not require fine-tuning. A successful Doc Doctor integration does not prove generality. A successful benchmark does not prove production quality. Each claim requires its own evidence.

---

## 2. Product boundaries under consideration

The current product decomposition is provisional:

```text
J-Editorial Specification
        │
        ▼
J-Editorial Core / Engine
        │
   ┌────┼───────────────┐
   │    │               │
   ▼    ▼               ▼
Doc   Bench          SDK / CLI / MCP /
Doctor               other interfaces
   │                    │
   └──────────┬─────────┘
              ▼
       Policy / Benchmark Packs
              │
              ▼
        Server / Backend API
              │
              ▼
   Quality / Evaluation Control Plane
```

These boxes describe likely **responsibilities**, not required repositories, packages, processes, or commercial SKUs.

### 2.1 J-Editorial Specification

Prospective canonical language for editorial state, obligations, evidence, interventions, outcomes, provenance, and evaluation.

### 2.2 J-Editorial Core

Prospective deterministic or explicitly probabilistic runtime implementing the specification independently of a specific editor or application.

### 2.3 Doc Doctor

The first real writing-product environment expected to consume and pressure-test J-Editorial. The current Doc Doctor implementation already contains relevant precursor concepts such as typed stubs, lifecycle state, schema-driven prompts, quality calculations, historical snapshots, QA sampling, provider statistics, MCP integration, and editorial workflow mechanics.

The roadmap currently treats Doc Doctor as the **first reference product and dogfooding environment**, not as the permanent home of canonical J-Editorial semantics.

That role remains falsifiable.

### 2.4 J-Editorial Bench

Prospective evaluation harness for controlled editorial tasks and episodes, including deterministic checks, model/agent evaluation, human review, provenance, regression comparison, and dataset lineage.

### 2.5 Policy packs

Prospective portable bundles that describe editorial expectations, applicability, precedence, and domain rules.

### 2.6 Benchmark packs

Prospective portable eval suites containing tasks, datasets, graders, manifests, slices, and expected evaluation behavior.

Policy packs and benchmark packs are deliberately separate concepts. A rule defines an expectation; a benchmark tests capability. One may generate or inform the other without being identical.

### 2.7 Server / Backend

Possible service boundary that exposes J-Editorial capabilities to writing products that should not embed the full runtime locally.

A hosted server is not assumed to be necessary.

### 2.8 Quality / Eval Control Plane

Long-horizon possibility connecting production observations, human review, offline evals, policy changes, model changes, regression analysis, and release decisions.

This is the most speculative product boundary in the roadmap.

---

## 3. Product principles

These principles describe the current intended progression. They remain subordinate to bootstrap review.

### 3.1 Semantic core before product-specific affordances

An Obsidian sidebar, web editor, CI check, API endpoint, or dashboard should project shared semantics rather than silently inventing its own incompatible editorial model.

### 3.2 Doc Doctor should prove the framework, not define it

If a concept only makes sense inside Obsidian, that is evidence that it belongs in Doc Doctor rather than the canonical framework.

If a concept applies across editors, CI, agent evaluation, CMS workflows, and future writing backends, it is a candidate for J-Editorial.

### 3.3 Evaluation observations precede aggregate scores

Per-instance observations, grader outputs, evidence, provenance, disagreements, and episode traces are primary data. Aggregate scores are derived views.

### 3.4 Provenance precedes optimization

The system should know what generated a result before trying to optimize that result.

### 3.5 Direct measurement beats indirect model judgment where possible

Executable checks should remain executable. A model judge should not replace deterministic validation merely for interface uniformity.

### 3.6 Subjective judgment should remain visibly subjective

Preference, tone, voice, rhetoric, and taste should not be disguised as objective truth because a model emitted a scalar.

### 3.7 Policies are scoped, versioned, conditional, and composable

No style guide, ontology bundle, organization rule, or documentation convention applies universally.

### 3.8 Historical behavior is evidence, not automatic truth

Accepted edits, reviewer choices, and published states are valuable observations but not necessarily unique gold answers.

### 3.9 Production data and held-out evaluation data must remain distinguishable

The project must not create a data flywheel that invalidates its own benchmarks.

### 3.10 Storage systems should remain adapters unless evidence proves otherwise

Git, DeltaDB, SQL systems, event stores, content-addressed storage, CRDTs, and editor operation streams are candidate substrates. Repository precedent alone should not make one canonical.

### 3.11 Generality requires a second independent consumer

Doc Doctor can prove usefulness and coherence. It cannot alone prove framework generality.

A major platform proof obligation is that an unrelated second writing product can consume J-Editorial without inheriting Obsidian- or Doc-Doctor-specific assumptions.

### 3.12 The framework must retain non-LLM value

J-Editorial should still provide useful editorial state, workflow, provenance, policy, and evaluation primitives when no language model is present.

---

## 4. Progression at a glance

| Stage | Working surface | Primary question | Current certainty |
|---|---|---|---|
| Bootstrap | Architecture review | Is the underlying model defensible enough to implement? | Active / controlling |
| 0 | Specification | Can editorial/eval semantics exist independently of implementation? | Near-horizon hypothesis |
| 1 | Core / Engine / SDK | Can those semantics execute deterministically and portably? | Near-horizon hypothesis |
| 2 | Doc Doctor reference integration | Are the semantics useful under real editorial work? | Near-horizon hypothesis |
| 3 | J-Editorial Bench | Can editorial-agent behavior be evaluated reproducibly? | Conditional horizon |
| 4 | Policy / Benchmark Packs | Can domains extend the framework without core forks? | Conditional horizon |
| 5 | Server / Backend | Can another writing product consume J-Editorial as infrastructure? | Exploratory horizon |
| 6 | Quality / Eval Control Plane | Can runtime quality and offline evaluation form a trustworthy operational loop? | Long-horizon hypothesis |

The numbering describes conceptual progression, not mandatory release numbering.

---

# 5. Pre-stage — Bootstrap gate

## Status

**Active. No downstream implementation stage is authorized merely by appearing in this roadmap.**

## Purpose

Reduce the architectural uncertainty that would otherwise become expensive to reverse after schemas, persistence, package boundaries, benchmark corpora, or APIs begin to depend on it.

## Questions the bootstrap must attack

At minimum:

- Is `Gap` the correct central intermediate representation?
- Are `Finding`, `Gap`, `Obligation`, `Claim`, `Risk`, `Violation`, `Question`, and `Review Finding` distinct enough to require separate first-class semantics?
- What entities require stable identity across revision?
- Is canonical artifact state source-oriented, structured, hybrid, or something else?
- Can stable semantic identity be layered over source text without making a structured tree canonical?
- What constitutes an editorial event?
- What belongs in low-level operation history versus high-level semantic history?
- What constitutes an eval instance?
- Is the relevant unit a snapshot, transition, episode, task, or a family of units?
- How should human disagreement and adjudication be represented?
- What does historical acceptance actually tell us?
- What forms of ground truth are available for different editorial dimensions?
- What history granularity is useful for eval generation?
- What can Git provide adequately?
- When is an event log required?
- Could DeltaDB contribute useful operation-level provenance without becoming a core dependency?
- What must remain persistence-independent?
- Which current Doc Doctor calculations are semantically justified, and which are heuristic prototypes that require validation?
- How should copyrighted or licensed style-guide knowledge be referenced, derived, or represented?
- What constitutes leakage between historical neighboring states?
- Which observations should be deterministic, human-graded, model-graded, execution-graded, or composite?

## Exit condition

Bootstrap does not need to eliminate all uncertainty.

It should instead reach:

> **Enough semantic and architectural clarity that an initial specification can be implemented without silently encoding disputed assumptions as irreversible product contracts.**

## Evidence expected

Possible evidence includes:

- adversarial design review;
- representative editorial scenarios;
- counterexamples;
- ontology stress tests;
- Doc Doctor implementation archaeology;
- storage/history experiments;
- benchmark thought experiments;
- data-lineage analysis;
- licensing analysis;
- prototype fixtures that expose semantic ambiguity.

## Pivot allowance

Everything downstream remains open to revision while this gate is active.

---

# 6. Stage 0 — J-Editorial Specification

## Status

**Near-horizon hypothesis; bootstrap-gated.**

## Hypothesis

Editorial workflows contain reusable semantic primitives that can be defined independently of an editor, model, database, file format, or application.

## Problem being tested

Can J-Editorial define editorial work precisely enough to support several products without becoming either:

- so generic that it says nothing useful; or
- so specific that it merely formalizes Doc Doctor's current implementation?

## Intended users

Initially:

- framework maintainers;
- writing-tool developers;
- evaluation engineers;
- researchers exploring editorial agents;
- contributors defining policy and benchmark semantics.

The specification itself is not necessarily an end-user product.

## Product role

Establish the shared language and compatibility boundary for later implementations.

## Candidate primitives under review

The candidate set currently includes:

```text
Artifact
Artifact State
Semantic Node
Objective / Goal Contract
Claim
Evidence Item
Finding
Gap
Obligation
Policy / Prior
Editorial Operation
Editorial Event
Intervention
Outcome
Lifecycle Transition
Release Gate
Actor
Reviewer
Evaluation
Eval Instance
Episode
Dataset
Benchmark Suite
Provenance
```

This list is deliberately provisional.

Bootstrap may:

- collapse several primitives;
- split them further;
- reject `Gap` as the central representation;
- define profiles for different editorial domains;
- identify representations that belong only in adapters.

## Candidate specification outputs

Potential outputs include:

- normative glossary;
- entity schemas;
- relationship semantics;
- lifecycle semantics;
- event semantics;
- provenance semantics;
- policy composition model;
- goal-contract model;
- evaluation terminology;
- conformance fixtures;
- canonical examples and counterexamples;
- serialization examples;
- compatibility and versioning rules.

These outputs need not all use the same serialization format.

## Inputs

Representative source material may include:

- Doc Doctor's existing domain model;
- real editorial workflows;
- docs-as-code histories;
- review annotations;
- style/editorial guides as scoped priors;
- source-of-truth records;
- publication gates;
- benchmark/eval literature;
- human review and correction histories;
- Git or operation-level histories.

## Outputs

The stage should produce a specification precise enough that an implementation can distinguish:

- source state from derived state;
- fact from policy;
- observation from validated finding;
- finding from unresolved obligation;
- editorial operation from resulting outcome;
- release acceptance from universal quality;
- historical acceptance from ground truth;
- model judgment from deterministic evidence;
- runtime production record from benchmark instance.

## Proof obligations

The specification should successfully describe representative cases including:

1. a document moving from incomplete draft to release candidate;
2. a missing citation that is later resolved with evidence;
3. a factual claim contradicted by an authoritative source;
4. a stylistic finding that remains legitimately preference-based;
5. an accepted edit that is later reverted;
6. an edit that resolves one gap while introducing another;
7. a published document reopened by erratum;
8. two valid alternate editorial resolutions;
9. reviewer disagreement requiring adjudication;
10. an agent that detects a real issue but proposes a bad fix;
11. an agent that edits unnecessarily despite no valid finding;
12. a deterministic technical-doc check such as schema or example validation;
13. an artifact evaluated under two different goal contracts;
14. a policy rule whose applicability changes by audience or artifact type;
15. a historical episode useful for eval without asserting the final text is the only correct answer.

## Candidate success signals

- concepts remain interpretable across several editorial scenarios;
- minimal application-specific escape hatches;
- state transitions can be explained;
- provenance can be represented without selecting a storage engine;
- deterministic and subjective evaluation can coexist without conflation;
- version changes can be reasoned about explicitly.

## Graduation gate

Advance when:

> **The semantics can be instantiated, validated, and tested without relying on Doc Doctor-, Obsidian-, Git-, DeltaDB-, or model-provider-specific concepts.**

## Downstream capabilities unlocked

Potentially:

- a reusable engine;
- conformance testing;
- adapter interfaces;
- stable evaluation records;
- portable policy definitions.

## Pivot triggers

Reconsider the specification if:

- too many scenarios require exceptions;
- `Gap` or another central abstraction collapses materially different concepts;
- stable identity proves impossible or prohibitively complex at useful granularity;
- provenance cannot be modeled without selecting one backend;
- human disagreement is flattened into fake certainty;
- the specification becomes mostly an encoding of one product's UI state.

## Deferred decisions

Unless bootstrap resolves them:

- canonical artifact representation;
- canonical serialization format;
- implementation language;
- persistence backend;
- network protocol;
- cloud deployment;
- product packaging.

## Explicit non-goals

Stage 0 should not:

- build an editor;
- define a universal writing-quality score;
- require an LLM;
- encode entire proprietary style guides;
- define a SaaS architecture;
- claim benchmark validity before benchmarks exist.

---

# 7. Stage 1 — J-Editorial Core / Engine / SDK

## Status

**Near-horizon hypothesis; depends on a sufficiently stable Stage 0 semantic contract.**

## Hypothesis

The specification contains enough deterministic or explicitly parameterized structure to become reusable executable infrastructure.

## Problem being tested

Can J-Editorial become a runtime that several consumers can use without reproducing editorial logic locally?

## Intended users

- Doc Doctor;
- CLI / CI integrations;
- writing-tool developers;
- evaluation harnesses;
- future adapters;
- agent systems needing structured editorial state.

## Product role

Turn semantic contracts into executable behavior while preserving the distinction between:

- canonical state;
- observations;
- policy;
- probabilistic judgment;
- derived metrics;
- storage and interface concerns.

## Prospective runtime shape

```text
artifact state
+ goal contract
+ applicable policies
+ evidence
+ editorial events
+ evaluation context
        ↓
J-Editorial Core
        ↓
derived state
validated transitions
findings / gaps / obligations
release-gate results
evaluation observations
provenance records
```

This is conceptual, not an API contract.

## Candidate capability families

### Validation

- schema validation;
- referential integrity;
- lifecycle-state validation;
- policy compatibility checks;
- provenance completeness checks.

### State

- materialize editorial state;
- apply valid semantic events;
- derive current unresolved conditions;
- represent reopening and supersession;
- compare states semantically.

### Lifecycle

- evaluate transition preconditions;
- represent release gates;
- retain unresolved non-blocking conditions;
- support post-release errata and supersession.

### Policy

- resolve applicable policies;
- preserve precedence;
- expose conflicts;
- support local overrides without erasing provenance.

### Evaluation

- emit structured observations;
- preserve grader identity and version;
- distinguish deterministic, human, model, and execution-based evidence;
- support per-instance records before aggregation.

### Provenance

- identify actor/source;
- connect action to cause and target;
- retain relevant evidence;
- identify score-affecting versions;
- support reproducibility.

### Serialization and adapters

Potentially:

- JSON;
- YAML;
- native library types;
- CLI IO;
- WASM;
- FFI;
- MCP;
- editor adapters.

No one interface is guaranteed.

## LLM boundary

A major design principle to test is:

> **Models may produce observations, classifications, suggestions, and judgments; they should not silently own canonical state transitions or deterministic calculations.**

Examples of model-appropriate outputs may include:

- candidate finding detection;
- semantic classification;
- suggested editorial operation;
- subjective quality judgment;
- evidence retrieval proposal;
- adjudication aid.

Examples of logic that should remain deterministic when possible:

- event application;
- identity/reference validation;
- release blockers;
- schema conformance;
- benchmark manifests;
- aggregation formulas;
- known executable checks;
- data-split lineage;
- provenance/version accounting.

## Relationship to current Doc Doctor core

Doc Doctor already contains a Rust workspace separated into domain, application, parser/config, CLI, MCP, WASM, FFI, and other layers. It also contains current quality and trajectory calculations.

That existing architecture is useful evidence and likely extraction material, but Stage 1 must review each concept rather than bulk-renaming Doc Doctor crates into J-Editorial.

Current implementation should be treated as:

- working prior art;
- an empirical fixture source;
- a migration constraint;
- a source of concepts worth preserving or falsifying.

It is not automatic canonical architecture.

## Inputs

- Stage 0 semantic contracts;
- conformance fixtures;
- Doc Doctor archaeology;
- representative policy bundles;
- representative editorial histories;
- benchmark-shaped sample records.

## Outputs

Potentially:

- reusable engine;
- conformance test suite;
- adapter contracts;
- CLI or SDK surface;
- event/state materialization logic;
- deterministic metric primitives;
- migration path from Doc Doctor-owned semantics.

## Proof obligations

- deterministic replay where the chosen model requires it;
- stable results under identical inputs;
- explicit nondeterminism where model judgments are involved;
- no hidden dependency on Obsidian internals;
- policy versions influence outputs observably;
- provenance identifies score-affecting components;
- storage can be substituted through adapters where intended;
- unsupported application concerns remain outside the core.

## Candidate success signals

- Doc Doctor can call the core rather than duplicate logic;
- fixtures are reusable outside Doc Doctor;
- event/state logic is testable headlessly;
- multiple history sources can normalize into the same semantic layer;
- deterministic outputs are reproducible;
- model-derived outputs retain explicit provenance and uncertainty.

## Graduation gate

Advance when:

> **A consumer can use J-Editorial for meaningful editorial state/evaluation behavior without reimplementing the domain model locally.**

## Downstream capabilities unlocked

- Doc Doctor reference integration;
- headless evaluation;
- benchmark harness construction;
- policy portability experiments;
- second-consumer prototypes.

## Pivot triggers

Reconsider the core if:

- the engine becomes mostly application-specific;
- replay is meaningless for the chosen data model;
- semantic identities create excessive migration complexity;
- policies require hardcoded branches per application;
- deterministic and model-driven paths cannot be cleanly separated;
- the abstraction cost exceeds the reduction in duplicated logic.

## Deferred decisions

- exact package/crate layout;
- language bindings;
- service boundaries;
- long-term persistence;
- whether CLI/MCP/WASM are core or separate distributions;
- public SDK stability guarantees.

---

# 8. Stage 2 — Doc Doctor as first reference product

## Status

**Near-horizon hypothesis and primary product laboratory.**

## Hypothesis

J-Editorial semantics improve real editorial work rather than merely producing elegant abstractions.

## Problem being tested

Can a working writing tool consume J-Editorial in ways that make editorial state, gaps, lifecycle, evidence, review, and agent assistance more useful to humans?

## Intended users

Doc Doctor's actual users, including:

- individual writers;
- technical writers;
- researchers;
- knowledge workers;
- documentation maintainers;
- users coordinating human + AI editorial workflows.

## Product role

Doc Doctor becomes the first environment where J-Editorial is:

- exercised interactively;
- stressed by real documents;
- tested against imperfect workflows;
- exposed to human accept/reject behavior;
- used to generate authentic editorial history;
- evaluated for ergonomics rather than schema purity.

The current desired boundary is:

```text
Obsidian / Doc Doctor UX
        │
        ▼
Doc Doctor integration layer
        │
        ▼
J-Editorial Core
```

## Responsibilities Doc Doctor should likely own

Candidate application responsibilities include:

- Obsidian lifecycle hooks;
- workspace integration;
- commands;
- views and sidebars;
- inline annotations and decorations;
- selection handling;
- vault navigation;
- interactive review;
- accept/reject UX;
- card actions;
- editor-specific history visualization;
- application settings;
- Obsidian plugin compatibility;
- user-facing explanation and feedback.

## Responsibilities expected to move toward J-Editorial if validated

Candidate framework responsibilities include:

- artifact semantics;
- gap/finding semantics;
- policy applicability;
- lifecycle semantics;
- quality dimensions;
- evaluation observations;
- event/provenance semantics;
- benchmark event capture;
- goal contracts;
- release gates;
- reusable calculations.

The exact extraction boundary remains a bootstrap/ADR question.

## Existing Doc Doctor capabilities relevant to this stage

The current product already provides a substantial experimental base, including:

- typed editorial stubs;
- schema-driven prompts;
- configurable J-Editorial schema behavior;
- AI suggestions;
- lifecycle automation;
- milestone triggers;
- Git snapshots;
- time-travel/history views;
- QA sampling;
- provider statistics;
- acceptance tracking;
- MCP tools;
- a reusable Rust core decomposition.

This means Stage 2 is not a greenfield reference app. It is an extraction, validation, and product-hardening exercise.

## Real editorial episode model to test

A useful production record may resemble:

```text
artifact state
    ↓
finding detected
    ↓
finding validated / rejected
    ↓
editorial intervention proposed
    ↓
human accepts / edits / rejects / defers
    ↓
new artifact state
    ↓
follow-up evaluation
    ↓
outcome: resolved / reopened / regressed / superseded
```

The specific episode schema remains provisional.

## Data generated

Potential high-value observations include:

- finding type;
- true/false-positive disposition;
- suggestion acceptance;
- partial acceptance;
- manual rewrite after suggestion;
- rejection reason;
- correction after rejection;
- reopen rate;
- regression introduced;
- time or turns to resolution;
- policy invoked;
- evidence consulted;
- actor sequence;
- lifecycle transition;
- release disposition;
- later invalidation or erratum.

The product should avoid collecting data merely because it is available. Data capture should be justified by a known product or evaluation question.

## Candidate measures to explore

These are exploratory and should not become canonical KPIs without evidence:

- finding acceptance rate;
- false-positive rate;
- resolution rate;
- reopen rate;
- regression rate;
- human intervention rate;
- average attempts to acceptable resolution;
- time to resolution;
- policy-specific failure patterns;
- model/provider differences;
- proportion of deterministic versus subjective checks;
- unresolved blocking-gap duration.

## Key product questions

- Do users understand the difference between findings and validated gaps?
- Are typed gaps useful enough to maintain?
- Does provenance help users review AI edits?
- Do lifecycle gates reflect real practice or feel artificial?
- Are quality dimensions actionable?
- Does semantic history improve review compared with ordinary Git diffs?
- Which editorial events are worth capturing?
- Which events feel like telemetry noise?
- Do users want automatic scoring, explicit gates, or qualitative state explanations?
- How much ontology is visible in the UX versus hidden in the engine?

## Proof obligations

1. J-Editorial abstractions survive real document work.
2. Doc Doctor can consume the framework without owning canonical semantics.
3. Users can understand enough of the model to act on it.
4. Editorial episodes can be reconstructed reproducibly enough for later evaluation.
5. The system does not require an LLM to remain useful.
6. Human corrections can contradict framework assumptions and feed revision of the framework.

## Candidate success signals

- fewer duplicated domain rules inside Doc Doctor;
- real gaps map cleanly to framework concepts;
- human review outcomes retain useful provenance;
- history supports semantic queries impossible or awkward with plain diffs;
- lifecycle and release state correspond to user intent;
- users can reject framework findings without corrupting state;
- captured episodes are rich enough for replay/evaluation experiments.

## Graduation gate

Two conditions should hold:

### Gate A — reference-product separation

> **Doc Doctor consumes J-Editorial without remaining the canonical owner of the shared editorial domain model.**

### Gate B — authentic evaluation substrate

> **Real editorial workflows generate reproducible, interpretable records that can plausibly become evaluation episodes without flattening human judgment into fake gold labels.**

## Downstream capabilities unlocked

- J-Editorial Bench experiments;
- historical episode extraction;
- policy portability tests;
- second-consumer design;
- storage-adapter comparison using real workloads.

## Pivot triggers

The framework should change if:

- users consistently work around the ontology;
- common editorial states require application-specific hacks;
- quality dimensions do not correspond to meaningful decisions;
- event capture is too expensive or intrusive;
- provenance adds volume without improving review;
- `Gap` fails to match real editorial behavior;
- Doc Doctor's best UX requires semantics incompatible with the framework.

Doc Doctor is not obligated to conform to a bad framework. It is evidence against the framework when appropriate.

## Deferred decisions

- whether Doc Doctor remains the flagship user-facing product;
- whether J-Editorial branding is exposed to end users;
- whether history remains Git-backed or adopts richer optional adapters;
- whether evaluation capture is local-only, exportable, or service-backed;
- whether the reference integration is distributed as bundled core binaries, WASM, FFI, or another mechanism.

---

# 9. Stage 3 — J-Editorial Bench

## Status

**Conditional horizon. Requires evidence from authentic editorial episodes and a sufficiently stable evaluation model.**

## Hypothesis

Editorial behavior can be decomposed into reproducible evaluation tasks and episodes that meaningfully compare agents, prompts, models, policies, and workflows.

## Problem being tested

Can J-Editorial measure writing-system behavior in ways that are more informative than generic text-quality scoring or final-snapshot comparison?

## Intended users

- AI evaluation engineers;
- writing-tool developers;
- agent developers;
- model teams;
- documentation/platform teams;
- researchers studying editorial agents;
- maintainers of specialist writing systems.

## Product role

Turn J-Editorial from a runtime semantic layer into a reproducible evaluation framework.

## Candidate benchmark primitives

```text
Eval Instance
Dataset
Dataset Lineage
Split
Episode
Run
Run Manifest
Agent / Model Adapter
Tool Configuration
Grader
Rubric
Observation
Disposition
Slice
Aggregation
Benchmark Suite
Comparison
Regression
```

Final names remain open.

## Candidate evaluation modes

### Detection

Can the system find known editorial conditions?

Examples:

- missing citation;
- contradiction;
- omitted endpoint;
- ambiguous instruction;
- terminology violation;
- unsupported claim.

### Classification

Can the system identify the right condition type and severity?

### Resolution

Can the system propose or execute an acceptable intervention?

### Abstention

Can the system avoid editing when evidence is insufficient or no issue exists?

### Regression avoidance

Can it resolve a target issue without damaging unrelated content?

### Evidence use

Can it locate, cite, or rely on appropriate evidence?

### Feedback recovery

Can it respond appropriately after reviewer rejection or correction?

### Lifecycle / release judgment

Can it identify whether required release conditions are satisfied?

### End-to-end editorial episode

Can it move an artifact from a known initial state toward a valid target condition under controlled rules?

## Candidate execution sources

Benchmarks may eventually support:

- static datasets;
- historical editorial episodes;
- synthetic seeded defects;
- executable documentation fixtures;
- manually curated expert tasks;
- adversarial examples;
- controlled production-derived examples;
- mixed datasets.

No source should be assumed valid merely because it is convenient.

## Candidate grader families

### Deterministic

- schema conformance;
- parser checks;
- link integrity;
- endpoint coverage;
- executable examples;
- terminology exact-match rules;
- expected evidence references.

### Human

- expert review;
- preference comparison;
- adjudication;
- rubric scoring.

### Model judge

Potentially appropriate for bounded subjective judgments, provided:

- prompt/version provenance is preserved;
- reliability is measured;
- judge bias is evaluated;
- deterministic substitutes are not available;
- human calibration exists where necessary.

### Execution / environment grader

- code execution;
- API schema validation;
- generated procedure tests;
- simulator checks;
- rendered-document accessibility checks where executable.

### Composite

Combines several grader families while preserving per-component outputs.

## Candidate metrics

Metrics should be capability-specific. Possible examples:

- precision / recall / F1 for finding detection;
- false-positive rate;
- false-negative rate;
- exact or partial classification agreement;
- resolution acceptance rate;
- regression rate;
- unnecessary-edit rate;
- abstention correctness;
- evidence-source quality;
- reviewer intervention rate;
- turns to valid resolution;
- cost per successful episode;
- latency;
- release-gate accuracy;
- calibration;
- inter-grader agreement;
- pairwise preference;
- slice-specific performance.

A single global J-Editorial score is not presumed necessary or desirable.

## Episode-first evaluation principle

The benchmark should preserve the record underneath the metric:

```text
aggregate score
      ↓ derived from
per-instance observations
      ↓ derived from
editorial episode / task
      ↓ derived from
artifact state + context + interventions + evidence + outcomes
```

This allows later re-grading when:

- rubrics change;
- policies change;
- grader bugs are fixed;
- aggregation changes;
- new slices are defined.

## Data lineage requirements

Benchmarks must be able to identify:

- source dataset;
- source artifact lineage;
- neighboring snapshots/episodes;
- split membership;
- benchmark version;
- policy version;
- goal-contract version;
- grader version;
- prompt/scaffold version;
- model identity;
- tools;
- runtime/environment;
- aggregation logic.

Lineage-aware splitting is essential. Neighboring versions of the same artifact should not be scattered randomly across training and held-out evaluation if that makes the evaluation trivially leak editorial history.

## Candidate CLI experience

Illustrative only:

```bash
jedit eval corpus/api-reference \
  --agent <agent-config> \
  --policy <policy-pack> \
  --benchmark <suite>
```

Possible output categories:

```text
Detection recall
False-positive rate
Resolution acceptance
Regression rate
Human intervention rate
Turns to resolution
Cost
Latency
Slice breakdowns
```

The command name, interface, and packaging remain open.

## Proof obligations

- repeat runs are comparable under controlled conditions;
- expected stochastic variation is measurable;
- graders demonstrate acceptable reliability for their intended use;
- benchmarks distinguish meaningful model/agent differences;
- results remain interpretable at the per-instance level;
- benchmark improvements correlate with expert or task outcomes where such correlation is claimed;
- corpus leakage is controlled;
- benchmark definitions can be versioned independently of product versions;
- model-judge dependence does not dominate objective tasks.

## Candidate success signals

- stable rankings or explainable instability;
- regression detection catches known degradations;
- slice analysis reveals useful capability differences;
- benchmark output predicts human review behavior better than generic prose scores;
- historical episode metrics identify failures invisible in final snapshots;
- run manifests reproduce materially equivalent conditions.

## Graduation gate

Advance when:

> **Equivalent benchmark runs are reproducible enough to support meaningful comparisons, and their provenance explains the material causes of result differences.**

## Downstream capabilities unlocked

- portable benchmark packs;
- policy/benchmark ecosystem;
- CI evaluation;
- model/prompt regression testing;
- organization-specific suites;
- potential production quality integration.

## Pivot triggers

Reconsider Bench if:

- rankings are mostly noise;
- metrics do not correlate with expert judgment or task success;
- corpus leakage dominates results;
- eval construction cost exceeds value;
- model judges provide most of the signal on supposedly objective tasks;
- final-snapshot benchmarks perform just as well as full episodes for the target decisions;
- different editorial domains require fundamentally incompatible harnesses.

## Deferred decisions

- benchmark file format;
- orchestration framework;
- cloud versus local execution;
- distributed runners;
- leaderboard product;
- hosted result storage;
- model-provider integrations;
- public benchmark licensing.

---

# 10. Stage 4 — Policy packs and benchmark packs

## Status

**Conditional horizon. Depends on Stage 1–3 evidence that policies and evals are portable concepts.**

## Hypothesis

Domain knowledge and evaluation tasks can be extended without modifying J-Editorial core.

## Problem being tested

Can J-Editorial support different editorial domains while avoiding both extremes:

- one universal ontology that becomes vague or contradictory; or
- a core fork for every organization and writing domain?

## Intended users

- writing-product teams;
- documentation organizations;
- editorial teams;
- benchmark authors;
- researchers;
- domain experts;
- organizations with house rules.

## Product role

Create an extension ecosystem around stable core semantics.

## Policy pack — prospective definition

A policy pack describes expectations and applicability.

Potential contents:

- rules;
- ontology extensions;
- terminology;
- applicability conditions;
- severity defaults;
- precedence;
- exceptions;
- evidence expectations;
- lifecycle gates;
- organization-specific overrides;
- source/provenance metadata;
- licensing metadata.

## Benchmark pack — prospective definition

A benchmark pack describes controlled tests.

Potential contents:

- tasks;
- dataset references;
- expected conditions;
- graders;
- rubrics;
- environment requirements;
- slices;
- aggregation;
- run constraints;
- provenance;
- licensing metadata.

## Why policy and benchmark packs should remain distinct

A policy may say:

> Public API reference pages must document every supported authentication requirement.

A benchmark may test:

> Given 50 API reference artifacts with known authentication omissions, detect and resolve them without introducing unsupported requirements.

The first is normative. The second is evaluative.

## Candidate composition features

- inheritance;
- scoped extension;
- override;
- precedence;
- compatibility declaration;
- conflict detection;
- artifact-type applicability;
- audience applicability;
- jurisdiction/domain applicability;
- temporal/product-version applicability;
- provenance chaining.

## Candidate domains

Examples only:

- technical documentation;
- API reference;
- journalism;
- academic writing;
- reference/encyclopedic writing;
- UX writing;
- knowledge-base maintenance;
- internal policy documentation;
- organization-specific house style.

The project should not promise all of these.

## Style-guide handling

Industry-standard priors such as AP, CMOS, Wikipedia conventions, Microsoft style, Google developer documentation conventions, or internal house rules may inform policy bundles.

The project must distinguish:

- concepts derived from a guide;
- exact licensed guide content;
- publicly redistributable rules;
- organization-authored transformations;
- examples;
- citations/provenance.

No policy ecosystem should assume copyrighted guide text can be copied into redistributable packs.

## Proof obligations

- new domains can extend behavior without core forks;
- policy conflicts are visible;
- precedence is inspectable;
- the same artifact can be evaluated under different policy sets;
- benchmark packs remain reproducible under versioning;
- policy and benchmark versions can evolve independently;
- organizations can define local rules without losing provenance.

## Candidate success signals

- meaningful reuse across at least two domains;
- small extension surface for custom organizations;
- few hardcoded domain branches in core;
- conflicts are diagnosable;
- policy upgrades produce explainable result changes;
- benchmark packs can be run by an independent consumer.

## Graduation gate

Advance when:

> **A new domain or organization can meaningfully extend J-Editorial without forking its core semantic/runtime implementation.**

## Pivot triggers

Reconsider the pack model if:

- domain semantics differ too fundamentally;
- extension precedence becomes unintelligible;
- policy packs turn into arbitrary executable code with no interoperability;
- licensing prevents meaningful reusable bundles;
- benchmarks require application-specific harnesses despite shared core semantics.

Possible pivot outcomes include:

- domain profiles;
- narrower core ontology;
- multiple interoperable standards;
- executable policy plugins;
- separate vertical frameworks sharing only evaluation infrastructure.

## Deferred decisions

- package registry;
- marketplace;
- signing;
- paid/private packs;
- licensing model;
- distribution mechanism;
- pack language/DSL.

---

# 11. Stage 5 — J-Editorial Server / writing-product backend

## Status

**Exploratory horizon. A server should not be built merely because backend infrastructure is imaginable.**

## Hypothesis

Writing-product developers may benefit from consuming J-Editorial as reusable backend infrastructure rather than embedding all functionality locally.

## Critical platform proof

The most important proof obligation is a **second independent writing product**.

Without it:

> J-Editorial may simply be Doc Doctor factored into libraries.

With it:

> J-Editorial has evidence that its domain model and interfaces generalize beyond the reference implementation.

The second consumer should be meaningfully independent. A trivial CLI wrapper around the same Doc Doctor workflow is insufficient proof.

## Potential second-consumer classes

Examples only:

- ProseMirror/Tiptap-based editor;
- Lexical-based writing product;
- CMS;
- docs platform;
- newsroom workflow;
- research-writing environment;
- AI writing assistant;
- knowledge-management backend;
- CI-only documentation quality service.

## Problem being tested

Is there sufficient reusable state, collaboration, history, evaluation, or policy behavior to justify a service boundary?

## Intended users

- writing-product developers;
- platform engineers;
- AI-product teams;
- documentation tooling teams;
- organizations building specialized editorial workflows.

## Product role

Potentially provide reusable infrastructure for:

- artifacts;
- editorial state;
- semantic events;
- policies;
- evidence;
- evaluations;
- episodes;
- benchmark runs;
- provenance;
- history;
- release gates.

## Possible access surfaces

Illustrative only:

```text
SDK
HTTP API
MCP
Webhooks
Event stream
Batch jobs
Local daemon
Embedded service
```

The appropriate surface should follow actual consumer requirements.

## Candidate API shape

Conceptual only:

```text
create/read artifact
record observation
apply editorial event
evaluate artifact
materialize state
run benchmark
query history
resolve finding/gap
record review disposition
```

This is not permission to create REST endpoints during bootstrap.

## Major architectural questions deliberately deferred

- embedded versus hosted;
- local-first versus cloud-first;
- single-process versus distributed;
- SQL versus document/graph/event storage;
- CRDT requirements;
- DeltaDB integration;
- synchronization;
- tenancy;
- authentication;
- encryption model;
- region/data residency;
- pricing;
- cloud provider;
- event streaming;
- queueing;
- analytics store.

## Persistence hypothesis

The server, if it exists, should likely consume a semantic persistence interface rather than expose one storage implementation as the framework itself.

Potential adapters might include:

```text
Git
filesystem
SQL database
semantic event store
DeltaDB
editor-operation log
CMS history
custom enterprise source
```

This remains open.

## Delta / DeltaDB role under this roadmap

DeltaDB is currently interesting as a possible **provenance/history adapter or experimental capture system**, particularly because operation-level causal histories may contain signals that Git snapshots lose.

The roadmap does not currently treat DeltaDB as:

- the canonical J-Editorial backend;
- a required dependency;
- a replacement for Git;
- a replacement for relational data storage;
- an accepted production persistence choice.

Beta experiments may inform the required history interface.

## Proof obligations

- a second consumer integrates successfully;
- the consumer does not need Doc Doctor-specific semantics;
- server-side behavior materially reduces duplicated product work;
- remote state provides enough benefit to justify privacy/security complexity;
- API boundaries preserve framework semantics rather than flattening them;
- local/embedded use remains possible if required by privacy or latency.

## Candidate success signals

- low integration complexity for the second consumer;
- reusable policies across products;
- centralized evaluation without product-specific rewrites;
- provenance survives API boundaries;
- storage substitution is possible;
- server deployment solves a real need rather than adding architecture for its own sake.

## Graduation gate

Advance when:

> **An external application can treat J-Editorial as infrastructure rather than embedding or copying its internals, and the service boundary demonstrates material value.**

## Pivot triggers

Do not build or retain a server product if:

- an embedded SDK solves nearly all use cases;
- privacy requirements favor local-only execution;
- synchronization complexity exceeds platform value;
- server state merely mirrors editor state with no reusable behavior;
- the second consumer requires a fundamentally different semantic model.

A valid roadmap outcome is:

> **J-Editorial remains a local/open framework plus evaluation toolkit and never becomes a major hosted backend.**

## Deferred decisions

Everything operational until evidence requires it, including deployment, tenancy, billing, cloud architecture, database selection, and API style.

---

# 12. Stage 6 — Editorial quality / evaluation control plane

## Status

**Long-horizon hypothesis. Most speculative stage.**

## Hypothesis

The same semantic model may eventually connect production editorial behavior, human review, offline benchmarks, model changes, prompt changes, policy changes, and regression analysis into a coherent quality-control system.

## Problem being tested

Can organizations operate writing agents with the same discipline used for software/data systems:

- observable production behavior;
- controlled evals;
- change comparison;
- regression detection;
- release criteria;
- auditability?

## Intended users

Potentially:

- AI product teams;
- evaluation teams;
- documentation platforms;
- editorial organizations;
- organizations running specialist writing agents at scale.

## Product role

Potential control loop:

```text
production editorial work
          │
          ▼
structured observations
     ┌────┴────┐
     ▼         ▼
quality      candidate eval
analytics    material
     │         │
     ▼         ▼
regression   controlled benchmark
signals      construction
     │         │
     └────┬────┘
          ▼
model / prompt / policy comparisons
          │
          ▼
release / deployment decisions
```

## Candidate capabilities

- model/agent comparisons;
- prompt/scaffold comparisons;
- policy-version comparisons;
- regression monitoring;
- quality drift;
- slice analysis;
- human-review disagreement analysis;
- cost/latency/quality tradeoffs;
- release gates;
- benchmark history;
- dataset health;
- evaluation provenance;
- experiment tracking;
- production-to-eval candidate curation;
- controlled replay.

## Non-negotiable evaluation boundary

Production observations must not silently contaminate held-out evaluation data.

Any production-to-eval workflow should preserve:

- source lineage;
- exposure history;
- model contact history where relevant;
- split eligibility;
- curation provenance;
- contamination status;
- privacy/license constraints.

## Possible operating model

A mature system might distinguish:

```text
Production observations
Development evals
Regression suites
Held-out benchmarks
Human adjudication sets
Training / fine-tuning candidates
```

These sets may overlap in source lineage but must not be conflated operationally.

## Proof obligations

- production signals predict something operationally useful;
- offline eval changes predict downstream quality when such claims are made;
- contamination is controllable;
- human review remains available for ambiguous judgments;
- policy changes can be distinguished from model regressions;
- score movement can be explained by underlying observations;
- the system does not reward metric gaming at the expense of editorial outcomes.

## Candidate success signals

- known regressions are detected before production release;
- benchmark slices explain production failures;
- model/prompt changes can be compared reproducibly;
- reviewers can trace quality changes to specific policies, datasets, or model versions;
- production data produces new test cases without destroying held-out validity;
- organizations can make deployment decisions using evidence richer than generic text-quality ratings.

## Graduation gate

No fixed gate is defined yet. A later roadmap revision should add one only after Stages 3–5 produce evidence about actual operational needs.

## Pivot triggers

Split the product if:

- production monitoring and offline eval require incompatible data models;
- control-plane requirements overwhelm the editorial framework;
- organizations already have better experiment/observability systems that J-Editorial should integrate with rather than replace;
- evaluation data governance demands a separate trust boundary.

Possible outcome:

> Runtime quality monitoring and offline benchmarking become separate products sharing the J-Editorial specification rather than one unified control plane.

---

# 13. Cross-cutting capability tracks

Some concerns span every stage and should not be postponed until a later product surface appears.

Each track should eventually maintain:

```text
current hypothesis
current evidence
open questions
next proof obligation
affected stages
accepted decisions / ADRs
revisit triggers
```

## 13.1 Domain semantics

Questions include:

- artifact identity;
- semantic nodes;
- claims;
- goals;
- gaps/findings/obligations;
- evidence;
- lifecycle;
- release gates;
- editorial operations;
- outcomes.

## 13.2 Evaluation science

Questions include:

- task design;
- graders;
- reliability;
- metrics;
- confidence intervals;
- stochastic variance;
- dataset construction;
- split methodology;
- leakage;
- calibration;
- human disagreement;
- benchmark revision.

## 13.3 Provenance and history

Questions include:

- snapshot granularity;
- semantic events;
- causal relationships;
- reconstruction;
- identity across edits;
- branch/alternate-state behavior;
- operation-level histories;
- history compression;
- audit requirements.

## 13.4 Persistence

Questions include:

- content-addressing;
- relational state;
- event logs;
- Git;
- DeltaDB;
- local-first data;
- synchronization;
- retention;
- disaster recovery.

Persistence choices must follow required semantics.

## 13.5 Human review

Questions include:

- acceptance;
- rejection;
- partial acceptance;
- disagreement;
- adjudication;
- reviewer expertise;
- override authority;
- confidence;
- correction provenance.

## 13.6 Agent integration

Questions include:

- model providers;
- tool use;
- prompt/scaffold versioning;
- agent planning;
- evidence retrieval;
- structured outputs;
- retries;
- budgets;
- reviewer feedback loops;
- sandboxing.

No specific agent framework is assumed.

## 13.7 Interoperability

Potential surfaces include:

- Markdown;
- structured document models;
- HTML;
- editors;
- CMSes;
- Git;
- APIs;
- MCP;
- CI;
- external source-of-truth systems.

## 13.8 Developer experience

Questions include:

- CLI ergonomics;
- SDK design;
- schema validation;
- fixtures;
- debugging;
- explainability;
- migration;
- extension development;
- local test harnesses.

## 13.9 Security and privacy

Questions include:

- sensitive source material;
- external model-provider boundaries;
- local-only workflows;
- telemetry;
- sharing;
- repository exposure;
- access control;
- data residency;
- retention;
- secrets;
- sandboxing.

## 13.10 Licensing and governance

Questions include:

- style-guide derivation;
- corpus rights;
- benchmark redistribution;
- contributed policy ownership;
- organization-private policies;
- generated-data rights;
- governance of canonical ontology changes.

## 13.11 Observability

Potential observations include:

- run duration;
- cost;
- model/provider usage;
- failures;
- retries;
- tool calls;
- grader outcomes;
- event counts;
- history growth;
- system health.

Operational telemetry should not be confused with editorial evaluation data.

---

# 14. Major pivot register

The roadmap should preserve major forks until evidence closes them.

| Question | Candidate directions | Current status |
|---|---|---|
| Canonical artifact representation | source text / structured tree / hybrid / other | Open in bootstrap |
| Central semantic primitive | gap / finding+obligation / richer graph / other | Open in bootstrap |
| Stable identity granularity | file / block / semantic node / claim / hybrid | Open in bootstrap |
| History substrate | Git / semantic event log / database / DeltaDB adapter / hybrid | Open in bootstrap |
| Evaluation unit | snapshot / transition / episode / task family | Open in bootstrap |
| Quality representation | vector / gates / liabilities / scalar derivative / mixed | Open in bootstrap |
| Product center | framework-first / eval-first / application-first / mixed | Provisional framework-first progression |
| Deployment | local library / daemon / hosted backend / hybrid | Deferred |
| Doc Doctor role | reference client / flagship product / experimental harness / mixed | Provisional reference + laboratory |
| Data sources | curated / synthetic / historical / production-derived / mixed | Open |
| Policy representation | ontology / declarative rules / executable checks / mixed | Open |
| Agent boundary | external adapter / built-in orchestration / mixed | Open |
| Benchmark product | local CLI / CI library / hosted service / mixed | Open |
| Control plane | unified / split monitoring+eval / integration-only | Long-horizon open |

When a major pivot is resolved, record:

```text
status:
evidence:
decision:
ADR:
revisit trigger:
affected roadmap stages:
```

Do not remove rejected directions merely to make the roadmap look cleaner; preserve enough history to explain why a pivot occurred.

---

# 15. Product-thesis proof obligations

These questions are larger than any one stage. They should remain visible because they can invalidate major portions of the roadmap.

## 15.1 Semantic-value hypothesis

Can editorial state be represented usefully enough to justify its complexity?

Failure mode:

- the framework spends more effort classifying work than helping perform or evaluate it.

## 15.2 Provenance-value hypothesis

Does typed provenance improve review, evaluation, debugging, or specialist-agent development compared with ordinary diffs and comments?

Failure mode:

- richer history creates storage/UX cost without producing better decisions.

## 15.3 Gap-field hypothesis

Are editorial gaps/findings/obligations useful enough to deserve first-class representation?

Failure mode:

- the categories do not predict action or quality.

## 15.4 Human-judgment hypothesis

Can expert editorial judgment be represented without erasing disagreement, multiple valid answers, or context-specific preference?

Failure mode:

- the framework turns subjective editorial decisions into pseudo-objective labels.

## 15.5 Historical-supervision hypothesis

Can revision traces produce useful supervision without treating accepted history as unique ground truth?

Failure mode:

- training/evaluation simply imitates historical habits and errors.

## 15.6 Eval-validity hypothesis

Do J-Editorial evals predict human acceptance, release outcomes, task success, or another defensible target?

Failure mode:

- benchmark optimization improves scores but not writing-system quality.

## 15.7 Policy-composition hypothesis

Can policies compose without unmanageable conflicts?

Failure mode:

- every organization requires hardcoded core behavior.

## 15.8 Generality hypothesis

Can a second independent application use J-Editorial without inheriting Doc Doctor assumptions?

Failure mode:

- the framework is just a refactor of one plugin.

## 15.9 Continuous-history hypothesis

Does richer operation-level history materially improve evaluation or specialist-agent development compared with meaningful snapshots?

Failure mode:

- operation traces mostly add noise.

## 15.10 Non-LLM-value hypothesis

Does the framework provide clear value with no model attached?

Failure mode:

- J-Editorial is actually an agent wrapper rather than an editorial framework.

---

# 16. Candidate success signals

Hard numerical targets should not be invented before baselines exist. Early success signals are categories of evidence.

## 16.1 Framework validity

Potential evidence:

- broad semantic coverage;
- few application-specific escape hatches;
- stable schema evolution;
- conformance fixtures;
- deterministic behavior where expected;
- clear error/explanation surfaces.

## 16.2 Editorial usefulness

Potential evidence:

- structured findings lead to action;
- users retain and resolve gaps;
- lifecycle state reflects actual workflow;
- provenance helps review;
- release gates correspond to meaningful readiness decisions;
- framework concepts survive real documents.

## 16.3 Evaluation usefulness

Potential evidence:

- repeatable benchmark behavior;
- expert agreement or measurable disagreement;
- meaningful model differentiation;
- sensitivity to regressions;
- useful slice analysis;
- episode metrics explain failures hidden by aggregate text-quality scores.

## 16.4 Platform usefulness

Potential evidence:

- second consumer;
- manageable integration effort;
- policy reuse;
- domain portability;
- low duplication of domain logic;
- adapter substitution.

## 16.5 Operational usefulness

Potential evidence:

- production regressions detected;
- benchmark changes correlate with downstream outcomes where expected;
- model/prompt/policy effects can be distinguished;
- failures are traceable;
- evaluation data remains uncontaminated enough for claimed use.

Hard thresholds should be introduced only after empirical baselines and decision requirements are understood.

---

# 17. Data flywheel — hypothesis, not assumption

A potential long-term advantage is a controlled loop from real editorial work into evaluation and improved systems:

```text
real editorial work
        ↓
typed provenance
        ↓
human review / outcomes
        ↓
curated eval episodes
        ↓
benchmarking
        ↓
better models / agents / policies
        ↓
real editorial work
```

This is attractive but dangerous if treated as automatic.

## 17.1 Necessary caveats

- accepted edits are not automatically gold answers;
- production behavior is biased by existing tools and policies;
- user-specific style may not generalize;
- privacy may prohibit reuse;
- client data may not be available for training/evaluation;
- benchmark contamination must be tracked;
- repeated model exposure may make examples unsuitable for held-out use;
- model-generated text can recursively contaminate supervision;
- reviewer disagreement must not be erased;
- selection effects can distort what gets captured.

## 17.2 Data-state distinctions to preserve

Potential classifications include:

- raw production observation;
- candidate curated episode;
- development eval;
- regression test;
- held-out benchmark;
- adjudication set;
- training candidate;
- excluded/contaminated data.

Moving an item between states should be explicit and provenance-preserving.

## 17.3 Proof obligation

The data loop should only become a strategic product claim after evidence shows that curated production history improves decisions without destroying benchmark validity or privacy guarantees.

---

# 18. History and provenance adapter strategy

J-Editorial should model the semantics it requires from history before selecting the history system.

## 18.1 Candidate sources

```text
Git commits / diffs
filesystem snapshots
editor operations
semantic event log
Delta / DeltaDB
CMS revision history
database change history
API events
custom enterprise systems
```

## 18.2 Normalization concept

```text
history source
      ↓
adapter / normalization
      ↓
artifact states + editorial events + provenance
      ↓
J-Editorial semantics / evals
```

## 18.3 Git

Likely strengths:

- durable snapshots;
- human familiarity;
- distribution;
- content-addressed history;
- existing docs-as-code integration;
- release/checkpoint semantics.

Likely weaknesses for J-Editorial evaluation:

- commit granularity may be too coarse;
- intent and review causality are usually implicit;
- intermediate agent actions may be lost;
- semantic editorial operations require inference.

## 18.4 Delta / DeltaDB

Potentially useful for experiments involving:

- fine-grained worktree history;
- human/agent conversational provenance;
- operation sequences;
- intermediate states;
- review threads;
- causal reconstruction.

Open questions:

- stable public API/SDK availability;
- exportability;
- durability guarantees;
- operational/security model;
- long-term compatibility;
- data portability;
- whether fine-grained traces materially improve evals.

## 18.5 Event-store hypothesis

A semantic event store may eventually be useful even if the artifact content itself lives elsewhere.

The bootstrap must decide whether semantic events are:

- primary state;
- derived records;
- optional observability data;
- benchmark-only records;
- some combination.

## 18.6 Anti-lock-in rule

No storage adapter should become part of the core product identity until evidence shows that its semantics are essential rather than merely convenient.

---

# 19. Versioning and compatibility strategy

Evaluation and editorial systems require more version identities than a normal application release.

The roadmap anticipates independent versioning for at least:

- J-Editorial specification;
- ontology/schema bundles;
- lifecycle definitions;
- goal contracts;
- policies;
- datasets;
- split definitions;
- benchmark suites;
- graders;
- prompts/scaffolds;
- agent configurations;
- aggregation logic;
- runtime/engine;
- product integrations.

Therefore:

```text
product version
    != specification version
    != policy version
    != benchmark version
    != dataset version
    != grader version
```

## 19.1 Why this matters

A benchmark score cannot be meaningfully compared across runs if the system cannot identify whether changes came from:

- the model;
- the dataset;
- the grader;
- the policy;
- the prompt;
- the runtime;
- the aggregation formula;
- the execution environment.

## 19.2 Deferred details

This roadmap does not yet select:

- SemVer strategy;
- schema migration mechanism;
- compatibility window;
- registry format;
- content-addressing scheme;
- signature model.

Those decisions should follow actual compatibility requirements.

---

# 20. Explicit non-commitments

Until bootstrap or later accepted ADRs decide otherwise, this roadmap does **not** choose or promise:

- Git as the canonical history backend;
- DeltaDB as the canonical history backend;
- Dolt as the canonical product database;
- any SQL, graph, document, or event database;
- CRDTs;
- canonical Markdown;
- canonical structured document trees;
- ProseMirror, Lexical, Tiptap, or another editor model;
- Rust as the only implementation language;
- a particular SDK language;
- a cloud provider;
- a hosted SaaS product;
- self-hosting as the only deployment model;
- a public API shape;
- pricing;
- licensing strategy;
- a benchmark marketplace;
- a policy marketplace;
- model fine-tuning as a required capability;
- training infrastructure;
- a particular LLM provider;
- a particular agent framework;
- a universal scalar writing score;
- a universal ontology covering all writing domains;
- a fixed repository/package structure;
- a unified production/eval control plane;
- a leaderboard;
- collection of user content for training;
- telemetry by default.

Detailed roadmap language must not be mistaken for selection of these options.

---

# 21. Reusable stage template

Future roadmap stages or revisions should use a consistent structure where possible:

```text
## Stage N — Working Name

### Status
### Hypothesis
### Problem being tested
### Intended users
### Product role
### Capabilities under consideration
### Inputs
### Outputs
### Data generated
### Dependencies
### Proof obligations
### Experiments / evidence needed
### Candidate success signals
### Graduation gate
### Downstream capabilities unlocked
### Pivot triggers
### Deferred decisions
### Explicit non-goals
### Open questions
```

The purpose of this template is to force every proposed capability to sit beside:

- the hypothesis it serves;
- evidence required to justify it;
- conditions under which it should be redesigned or abandoned.

---

# 22. Roadmap change protocol

The roadmap is expected to change materially as bootstrap and product evidence accumulate.

Meaningful revisions should record:

1. What changed?
2. What evidence caused the change?
3. Which hypothesis changed?
4. Which stages are affected?
5. Does `BOOTSTRAP.md` require revision?
6. Is an ADR required?
7. Does existing work become invalid, deprecated, or migration-bound?
8. What would cause the decision to be revisited?

A lightweight revision table may be maintained here once changes begin:

| Revision | Change | Evidence / decision | Affected stages |
|---|---|---|---|
| Initial | Establish provisional product progression | Pre-bootstrap product analysis | All |

No heavy change process is required until the cost of roadmap drift justifies it.

---

# 23. Current horizon

The roadmap should not imply equal confidence across all stages.

## 23.1 Immediate horizon — bootstrap

Primary work:

- adversarial review;
- semantic-model stress testing;
- architecture boundary review;
- review of existing Doc Doctor assumptions;
- history/persistence requirement analysis;
- eval-validity analysis;
- identification of decisions requiring ADRs.

No major downstream architecture should be treated as fixed before this work closes the relevant gates.

## 23.2 Near horizon — specification → core → Doc Doctor reference integration

These stages have the strongest current evidence because:

- the J-Editorial conceptual model already exists;
- Doc Doctor already implements a precursor domain model;
- the project has a real initial product consumer;
- current logic can be audited and extracted rather than invented abstractly.

Likely near-horizon proof sequence:

```text
bootstrap model survives review
        ↓
formalize minimum semantic contract
        ↓
implement reusable core behavior
        ↓
move shared semantics out of Doc Doctor
        ↓
run Doc Doctor against the framework
        ↓
collect authentic editorial episodes
```

Even this sequence remains reversible if evidence indicates a different extraction order.

## 23.3 Conditional horizon — Bench and portable packs

These depend on proving:

- editorial episodes are reconstructable;
- benchmark tasks can be defined cleanly;
- graders are reliable enough;
- lineage can be controlled;
- policy semantics are portable.

The project should not build a benchmarking platform merely because Doc Doctor records metrics.

## 23.4 Exploratory horizon — Server / API

This depends on:

- a second consumer;
- a demonstrated need for shared remote infrastructure;
- evidence that a service boundary improves product construction;
- acceptable security/privacy architecture.

A local framework-only outcome remains valid.

## 23.5 Long horizon — Control plane

This depends on almost every prior hypothesis and should remain deliberately underspecified until real benchmark and production workloads exist.

---

# 24. Current product progression

Subject to bootstrap review, the current progression can be summarized as:

```text
0. J-Editorial Specification
        ↓
1. J-Editorial Core / Engine / SDK
        ↓
2. Doc Doctor — first reference product and data laboratory
        ↓
3. J-Editorial Bench — reproducible editorial evals
        ↓
4. Policy Packs + Benchmark Packs — portable domain extensions
        ↓
5. J-Editorial Server / Backend — infrastructure for independent writing products
        ↓
6. Editorial Quality / Eval Control Plane — production + offline evaluation loop
```

The intended graduation logic is:

```text
Bootstrap → Stage 0
Enough ambiguity is reduced to specify semantics without hardening disputed assumptions.

Stage 0 → Stage 1
The semantic model describes representative editorial workflows independently of one application.

Stage 1 → Stage 2
The reusable core can own shared behavior that Doc Doctor currently implements locally.

Stage 2 → Stage 3
Real editorial work produces interpretable, reproducible episodes suitable for controlled evaluation.

Stage 3 → Stage 4
Benchmark and policy definitions are reproducible, versioned, and portable enough to move between contexts.

Stage 4 → Stage 5
A second independent writing product can consume J-Editorial without a core fork, and a backend boundary solves a real integration problem.

Stage 5 → Stage 6
Production observations and controlled evals can interact without corrupting held-out validity, and organizations have an operational need for a shared quality-control layer.
```

None of these transitions is automatic.

---

# 25. Product thesis in one sentence

The current compact thesis is:

> **J-Editorial is a reusable semantic and evaluation layer for software that creates, reviews, and improves written artifacts—representing not only what text exists, but what it is trying to accomplish, what remains deficient, why changes occur, whether those changes improve the artifact, and how reliably humans or agents perform that work.**

Doc Doctor is the first environment expected to prove that thesis interactively.

J-Editorial Bench would test whether it can be proved quantitatively.

A second independent consumer would test whether it is genuinely reusable.

A server/backend would only follow if reusable infrastructure provides value beyond embedding the framework locally.

A control plane would only follow if production quality and offline evaluation can be connected without sacrificing provenance, validity, privacy, or interpretability.

---

# 26. Bootstrap relationship

This roadmap should remain subordinate to the bootstrap process.

`BOOTSTRAP.md` asks:

> **What must be true before we build?**

`ROADMAP.md` asks:

> **If those hypotheses survive, what could this coherently become?**

The repository should resist the temptation to convert roadmap detail into premature implementation commitments.

The correct next step after this roadmap is not automatically Stage 0 implementation.

The correct next step remains the active bootstrap/adversarial review gate, whose purpose is to decide which parts of this roadmap deserve to survive into architecture and execution.
