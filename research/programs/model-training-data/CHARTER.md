# Model-Training Dataset Architecture, Engineering, and Governance — Research Charter

Status: **bootstrap-aligned placeholder / HELD / research not authorized**  
Parent research constitution: `RESEARCH.md`  
Controlling contract: `BOOTSTRAP.md`  
Related progression: `ROADMAP.md`  
Prospective gate: **`DATASET-ARCHITECTURE-G0`**  
Program role: **reserve, structure, and later execute the research required to make J-Editorial datasets trustworthy inputs to evaluation and model improvement**

This document is the placeholder charter for the full model-training dataset engineering research program discussed during J-Editorial bootstrap design.

It deliberately exists **before** the research is executed because dataset assumptions can contaminate the editorial semantic model, benchmark design, storage architecture, governance model, and eventual model-training strategy if they are allowed to emerge accidentally from implementation.

It is not a completed research plan and does not select a storage system, file format, dataset registry, data-lake technology, curation stack, training framework, model family, or cloud architecture.

## Bootstrap dependency alignment — 2026-09-04

Terminology/dependencies only; no source collection, dataset design, experiment,
format choice, storage choice, budget research or training is executed here.

The upstream editorial research shape now distinguishes identity-bearing data,
causal transactions, time-scoped conditions, exact checkpoints and versioned
projections. The Amnesia/About fixtures are architecture probes, not a corpus.
Any future program must consume reviewed editorial identity, goal/prior, history,
rights, retention and evaluation contracts. Historical acceptance is not automatic
training eligibility or a preferred/rejected label. This charter remains a placeholder;
its detailed tracks below must be rescoped at the separately authorized session.

## 0. Bootstrap revision rule

This charter is a **bootstrap input**.

When bootstrap executes, this document is expected to be revised materially in scope and shape before the research program is released.

Bootstrap should determine whether to:

- keep this as one program;
- split it into several research programs;
- merge tracks that prove inseparable;
- remove tracks that are premature;
- add missing tracks;
- reorder dependencies;
- rename concepts to match the accepted J-Editorial vocabulary;
- change the gate;
- define research budgets;
- define required reviewers/validators;
- translate the final fan-out into Beads;
- decide which questions must be answered during bootstrap itself and which can wait.

The expected sequence is:

```text
PRE-BOOTSTRAP PLACEHOLDER — this file
        ↓
BOOTSTRAP EXECUTION
        ↓
revised / executable research charter
        ↓
Beads fan-out + dependencies + gate
        ↓
LATER DATASET RESEARCH EXECUTION
        ↓
results / experiments / synthesis
        ↓
DATASET-ARCHITECTURE-G0
        ↓
ADR and specification candidates
        ↓
implementation
```

Deep SOTA reconnaissance, dataset experiments, proxy training runs, tool bake-offs, and final architecture selection are expected **after** bootstrap has scoped the program, unless bootstrap determines that a bounded investigation is necessary to resolve a bootstrap-level ambiguity.

## 1. Mission

Determine the data architecture, governance model, lifecycle, canonical semantics, physical representations, I/O contracts, curation pipeline, quality controls, lineage model, scale boundaries, cost model, training/evaluation isolation, and learning-oriented transformations required for J-Editorial to convert provenance-rich editorial histories into trustworthy datasets for:

- evaluation;
- benchmark construction;
- regression testing;
- grader calibration;
- supervised fine-tuning;
- preference optimization;
- reward modeling;
- reinforcement learning with verifiable or bounded rewards where justified;
- process/trajectory supervision;
- distillation;
- future specialist-model training and adaptation.

The program must answer not merely:

> **Where do we save examples?**

but:

> **What is a J-Editorial dataset, how does it acquire identity and lineage, what transformations are legitimate, what role is it allowed to serve, how do we know it is useful, and how can a future model-training run reproduce exactly what data and policy produced a checkpoint?**

## 2. Why this is a separate research program

Dataset engineering affects several architectural layers simultaneously:

```text
editorial semantics
       │
       ▼
production / historical observations
       │
       ▼
canonical episodes / learning records
       │
       ▼
dataset versions
       │
       ├────────────► held-out evals
       ├────────────► regression suites
       ├────────────► adjudication / calibration
       └────────────► training views
                         │
                         ▼
                   model adaptation
                         │
                         ▼
                   frozen evaluation
```

A premature choice in dataset representation can distort:

- the canonical editorial event model;
- what provenance survives;
- contamination controls;
- training/eval eligibility;
- reproducibility;
- storage and I/O costs;
- downstream model-learning methods;
- privacy and deletion behavior;
- benchmark credibility.

For that reason, dataset architecture must not be reduced to a single ADR such as `Use Parquet` or `Use lakeFS` without first establishing the semantic and operational requirements those tools are meant to satisfy.

## 3. Central hypothesis to attack

The current favored hypothesis is that J-Editorial should distinguish at least five layers:

```text
LEVEL 0 — SOURCE ASSETS
original documents, histories, evidence, reviews, operation streams

LEVEL 1 — CANONICAL NORMALIZED EDITORIAL RECORDS
artifacts, states, claims, gaps/findings, evidence, actions, outcomes, provenance

LEVEL 2 — CANONICAL EPISODE / LEARNING CORPUS
provenance-rich transitions and episodes suitable for controlled derivation

LEVEL 3 — LOGICAL DATASET VERSIONS
immutable selections + transformations + eligibility + lineage

LEVEL 4 — TRAINING / EVAL VIEWS
SFT, preference, reward, RL, trajectory, benchmark, regression projections

LEVEL 5 — EXECUTION LAYOUTS
Parquet/Arrow/shards/tokenized binaries/streaming layouts optimized for consumers
```

This layering must be challenged.

The research must determine whether:

- the levels are materially distinct;
- some belong in J-Editorial core versus the dataset subsystem;
- canonical episode records are sufficient or too opinionated;
- logical dataset identity should be independent of physical storage;
- execution layouts should be disposable derivatives;
- the architecture can remain small at initial scale without blocking later growth.

## 4. Dataset role is first-class metadata

A major working invariant to test is:

> **A dataset's operational role must be explicit and cannot be inferred from a folder name or file path.**

Candidate roles include:

- raw production observation;
- normalized canonical record;
- candidate curated episode;
- training candidate;
- supervised fine-tuning set;
- preference set;
- reward-model set;
- RL/verifiable-reward set;
- development eval;
- regression suite;
- grader-calibration set;
- human-adjudication set;
- frozen held-out benchmark;
- public benchmark;
- internal benchmark;
- excluded/contaminated data;
- withdrawn data.

The research must determine whether role is:

- a property of records;
- a property of logical dataset versions;
- a separate eligibility policy;
- or some combination.

An example may be valuable for training and disallowed for holdout evaluation. A severe historical regression may be poor SFT data but excellent negative or preference supervision.

## 5. Required industry/SOTA reconnaissance

At research execution time, this program must perform a **fresh** review of current frontier and production practice. The named systems below are starting points, not an exhaustive or frozen comparison set.

### 5.1 Large-scale corpus design and curation

Investigate current methods and lessons from projects such as:

- DataComp / DCLM;
- FineWeb / FineWeb2;
- Dolma / OLMo data work;
- RedPajama and comparable open corpus projects;
- RefinedWeb-like pipelines;
- other current open training-corpus efforts that expose reproducible data recipes.

Study:

- source composition;
- filtering;
- deduplication;
- quality classifiers;
- mixture experiments;
- proxy-model ablations;
- benchmark decontamination;
- documentation and licensing;
- storage layout;
- reproducibility.

### 5.2 Post-training dataset engineering

Investigate current post-training practice from projects such as:

- Tülu-family releases;
- Nemotron post-training datasets;
- open instruction/preference/RLVR corpora;
- other state-of-the-art specialist and reasoning post-training programs available at execution time.

Study:

- prompt/source provenance;
- human versus synthetic ratios;
- SFT construction;
- preference-pair construction;
- judge/critic filtering;
- verifiable reward construction;
- reasoning/trajectory data;
- decontamination;
- skill taxonomy;
- difficulty sampling;
- synthetic-data governance.

### 5.3 Dataset metadata/governance standards

Investigate:

- MLCommons Croissant and successors;
- dataset/data cards;
- model-provider training-content disclosure practices;
- relevant NIST guidance;
- relevant EU AI Act / GPAI disclosure and high-risk data-governance obligations where useful as design priors;
- provenance standards;
- rights/consent metadata standards;
- reproducibility metadata.

### 5.4 Dataset storage/versioning systems

Investigate current capabilities and tradeoffs of categories including:

- object storage + immutable manifests;
- lakeFS;
- DVC;
- Apache Iceberg;
- Delta Lake;
- Dolt where structured/versioned semantic metadata is relevant;
- PostgreSQL/temporal/event systems;
- content-addressed storage;
- Hugging Face Hub dataset revisions;
- other current dataset registries/lakehouse systems.

Do not assume one system must serve semantic state, large payload storage, and version identity simultaneously.

### 5.5 Data-processing and curation systems

Investigate current versions of systems such as:

- Hugging Face Datasets;
- PyArrow;
- Polars;
- DuckDB;
- NVIDIA NeMo Curator;
- Ray Data;
- Spark where scale warrants comparison;
- other current distributed/streaming data-processing frameworks.

### 5.6 Training-time physical formats and loaders

Investigate:

- Parquet;
- Arrow;
- JSON/JSONL;
- WebDataset;
- Mosaic Streaming / MDS or successors;
- Lance or related random-access/multimodal formats;
- memory-mapped/tokenized binary formats used by major training stacks;
- model-framework-specific sharding formats.

The program must explicitly separate **logical canonical semantics** from **physical training layout**.

### 5.7 Training and post-training stack

Investigate only to the extent required to understand dataset contracts and downstream I/O:

- PyTorch;
- Transformers;
- PEFT / LoRA / QLoRA;
- TRL;
- Axolotl;
- Accelerate;
- FSDP / FSDP2;
- DeepSpeed;
- Megatron-family systems when scale makes them relevant;
- vLLM/SGLang or other rollout/inference engines;
- experiment/model registries such as MLflow, W&B, or current alternatives.

The dataset program does not choose the final training stack; it defines what the data subsystem must provide to credible training stacks.

## 6. Research fan-out

The current fan-out uses aliases `DG-00` through `DG-14`. Bootstrap may rename, split, merge, or reorder them.

```text
DG-00 Dataset charter / vocabulary
        │
        ├──► DG-01 Dataset ontology & lifecycle
        ├──► DG-02 Canonical logical data model
        ├──► DG-03 Identity, provenance & lineage
        ├──► DG-04 Canonical storage semantics
        ├──► DG-05 Physical formats & I/O
        ├──► DG-06 Curation & data quality
        ├──► DG-07 Train/eval isolation & contamination
        ├──► DG-08 Sampling, mixtures & curricula
        ├──► DG-09 Synthetic & human data
        ├──► DG-10 Governance/privacy/licensing
        ├──► DG-11 Budgets & material scale
        ├──► DG-12 Training-view compilation
        ├──► DG-13 Dataset evaluation / ablations
        └──► DG-14 Tool & substrate bake-off
                      │
                      ▼
              DATASET-ARCHITECTURE-G0
```

Dependencies will not actually be this flat. Bootstrap should derive the executable DAG.

## 7. DG-00 — Dataset charter and vocabulary

### Question

What objects deserve the name `dataset`, `corpus`, `record`, `episode`, `view`, `split`, `manifest`, `shard`, `source`, and `derivative` in J-Editorial?

### Must distinguish

At minimum:

- source asset;
- normalized record;
- canonical editorial episode;
- logical dataset;
- dataset version;
- selection;
- transformation;
- training view;
- eval view;
- physical materialization;
- shard;
- cache;
- split;
- eligibility state;
- exposure state;
- lineage family;
- contamination cluster.

### Output

A glossary and boundary model that later tracks must use.

### Failure condition

If the program cannot distinguish semantic dataset identity from physical file layout, later storage/tool ADRs are premature.

## 8. DG-01 — Dataset ontology and lifecycle

### Questions

- What states can source data and derived data occupy?
- What transitions require review or approval?
- When does a production observation become eligible for curation?
- When does an item become ineligible for a held-out benchmark?
- How is withdrawal/deletion represented?
- How are superseded datasets retained for reproducibility?

### Candidate lifecycle to test

```text
INGESTED
   ↓
NORMALIZED
   ↓
VALIDATED
   ↓
CURATED
   ↓
ELIGIBLE
   ↓
ASSIGNED
   ├── TRAIN
   ├── DEV
   ├── REGRESSION
   ├── HOLDOUT
   ├── ADJUDICATION
   └── EXCLUDED
   ↓
FROZEN VERSION
   ↓
MATERIALIZED
   ↓
CONSUMED BY RUN
   ↓
RETAINED / SUPERSEDED / WITHDRAWN
```

This state machine is provisional.

### Required outputs

- lifecycle model;
- state-transition rules;
- eligibility semantics;
- exposure semantics;
- withdrawal semantics;
- audit requirements.

## 9. DG-02 — Canonical logical data model

### Questions

- What is the smallest lossless learning/eval record J-Editorial needs?
- Is the canonical unit an editorial episode, transition, event graph, artifact lineage, or several related units?
- Which fields belong in canonical semantic records versus derived annotations?
- How are multiple acceptable outcomes represented?
- How are rejected, reverted, superseded, or ambiguous edits represented?

### Candidate episode primitive

```text
Goal / Objective
Applicable Priors
Artifact State Before
Findings / Gaps / Obligations Before
Evidence Context
Actor(s)
Editorial Action / Intervention
Review / Disposition
Outcome
Artifact State After
Findings / Gaps / Obligations After
Verification
Provenance
Eligibility / Rights / Exposure Metadata
```

### Required tests

The model should represent:

- accepted factual correction;
- rejected stylistic suggestion;
- partially accepted model edit;
- revert;
- erratum;
- multiple valid resolutions;
- unresolved reviewer disagreement;
- synthetic seeded defect;
- deterministic verification;
- agent regression;
- no-op/abstention where no valid edit is required.

### Output

Logical schema candidates and counterexamples, not implementation migrations.

## 10. DG-03 — Identity, provenance, and lineage

### Questions

- How are source assets identified?
- How are normalized records linked to exact source versions?
- How are derivatives linked transitively?
- How is one editorial lineage prevented from leaking across split boundaries?
- How are generated/synthetic records linked to seeds, prompts, generators, critics, and filters?
- How is model exposure recorded?
- What is the identity of a dataset version?

### Candidate lineage relation types

- derived-from;
- normalized-from;
- selected-from;
- transformed-from;
- generated-from;
- perturbed-from;
- annotated-from;
- adjudicated-from;
- deduplicated-against;
- contaminated-by;
- supersedes;
- withdraws.

### Candidate identity mechanisms

- content hashes;
- stable J-Editorial IDs;
- source repository/commit IDs;
- object-store digests;
- immutable manifest hashes;
- dataset registry revisions.

### Output

A lineage graph/contract sufficient to reproduce membership and detect prohibited reuse.

## 11. DG-04 — Canonical storage semantics

### Core question

What does `canonical storage` actually mean for J-Editorial datasets?

The research must challenge the single-store assumption.

### Candidate separation

#### Semantic authority

Where canonical entities, provenance, lineage, eligibility, and dataset manifests live.

#### Payload authority

Where immutable/raw/large source objects live.

#### Dataset-version authority

What proves exactly which records and transformations constituted dataset version `X`.

#### Analytical derivative storage

Where large measurements, embeddings, features, and run outputs live.

#### Execution materialization

Disposable or reproducible shards optimized for training/eval consumers.

### Alternatives to compare

At minimum, compare credible combinations involving:

- relational/versioned relational systems;
- object storage + manifests;
- event/temporal models;
- lakehouse/versioned dataset systems;
- Git-like systems where appropriate;
- content-addressed approaches.

### Decision criteria

- semantic queryability;
- immutable version identity;
- branching/experimentation;
- lineage queries;
- local development;
- large-object handling;
- scale ceiling;
- transaction guarantees;
- deletion/redaction behavior;
- operational complexity;
- backup/restore;
- migration/export;
- analytical interoperability;
- cloud neutrality;
- cost.

### Output

Storage requirements and ranked architecture patterns. Tool selection remains downstream of evidence.

## 12. DG-05 — Physical formats and I/O

### Core question

Which formats are appropriate for which roles and access patterns?

### Roles to distinguish

- human-readable debugging/interchange;
- canonical metadata serialization;
- bulk structured corpus;
- in-memory interchange;
- lakehouse table;
- multimodal payload;
- streaming training input;
- random-access training input;
- tokenized training shard;
- eval-run artifact;
- immutable manifest.

### Candidate formats to investigate

- JSON;
- JSONL;
- YAML;
- Parquet;
- Arrow IPC;
- Iceberg table metadata;
- Delta tables;
- MDS;
- WebDataset/TAR shards;
- Lance;
- native binary/tokenized formats;
- SQLite/DuckDB exports where useful.

### I/O questions

- schema evolution;
- predicate pushdown;
- column pruning;
- random access;
- sequential streaming;
- shuffle semantics;
- remote object-store access;
- memory mapping;
- compression;
- shard size;
- small-file pathologies;
- partial reads;
- resume/checkpoint;
- loader interoperability;
- data-loader saturation of GPUs;
- local/offline operation.

### Required output

A role → format policy recommendation backed by representative access-pattern experiments.

No format should become `canonical` for all layers by convenience.

## 13. DG-06 — Curation and data quality

### Core question

How does raw or historical editorial material become trustworthy learning/evaluation material?

### Pipeline areas

- schema validation;
- corruption detection;
- normalization;
- language/domain classification;
- exact deduplication;
- near-duplicate deduplication;
- semantic deduplication;
- boilerplate detection;
- quality scoring;
- source-quality scoring;
- annotation-confidence scoring;
- PII/sensitive-data detection;
- license/rights filtering;
- contamination detection;
- difficulty estimation;
- capability/skill classification;
- policy applicability validation;
- outlier detection;
- human review.

### Key research principle

Where practical, retain quality/filter signals as versioned annotations before collapsing them into irreversible `keep/drop` decisions.

### Must compare

- deterministic filters;
- heuristic filters;
- learned classifiers;
- embedding-based methods;
- model-judge filters;
- human review;
- combinations.

### Output

A staged curation model with measured failure modes and provenance requirements.

## 14. DG-07 — Train/eval isolation and contamination

### Core question

How can J-Editorial learn from editorial history without invalidating its own benchmarks?

### Required concepts

- artifact lineage;
- near-duplicate cluster;
- semantic similarity cluster;
- source family;
- temporal cutoff;
- policy/template leakage;
- synthetic generator family;
- model exposure history;
- benchmark exposure;
- training exposure;
- retired/contaminated benchmark items.

### Split strategies to investigate

- random split as a negative/control case;
- artifact-level split;
- family/repository split;
- organization/team split;
- domain split;
- time-based split;
- difficulty split;
- mixed hierarchical split.

### Required tests

- quantify near-neighbor leakage;
- measure model performance changes when leakage is introduced deliberately;
- detect synthetic-template shortcuts;
- define what happens when a frozen benchmark item later becomes training data;
- define benchmark retirement/replacement policy.

### Output

A contamination model and lineage-aware split contract.

## 15. DG-08 — Sampling, mixtures, weighting, and curriculum

### Core question

How should training examples be selected and weighted rather than simply shuffled?

### Areas to research

- proportional sampling;
- inverse-frequency sampling;
- temperature sampling;
- quality weighting;
- confidence weighting;
- severity weighting;
- difficulty weighting;
- recency weighting;
- domain balancing;
- source balancing;
- human/synthetic balancing;
- positive/negative balancing;
- rare-gap oversampling;
- curricula;
- staged curricula;
- dynamic sampling;
- on-policy versus off-policy data.

### J-Editorial-specific question

Should higher editorial severity increase training probability, or would that teach a distorted world where severe defects are unrealistically common?

### Output

Sampling/mixture hypotheses with ablation plans rather than fixed weights invented from intuition.

## 16. DG-09 — Synthetic and human data

### Synthetic-data questions

- Which gaps can be injected deterministically?
- Which synthetic edits are too artificial?
- How are difficulty and realism measured?
- How are generator fingerprints prevented from becoming shortcuts?
- How are synthetic examples verified?
- When should a stronger model generate trajectories for distillation?

### Required synthetic provenance

Candidate fields:

```text
generator model/checkpoint
generation prompt/template
temperature / sampling config
source seed
derivation operation
critic/verifier
filter chain
human-review status
accept/reject reasons
rights/eligibility
```

### Human-data questions

- reviewer qualifications;
- annotation instructions;
- inter-rater agreement;
- disagreement retention;
- adjudication;
- compensation;
- privacy;
- labeling fatigue;
- expert/non-expert allocation.

### Output

Separate governance contracts for human-authored, production-derived, and synthetic supervision.

## 17. DG-10 — Governance, privacy, licensing, retention, and deletion

### Core question

What data is J-Editorial actually allowed to collect, transform, evaluate on, train on, redistribute, and retain?

### Required dimensions

- source ownership;
- source license;
- training permission;
- evaluation permission;
- redistribution permission;
- commercial-use permission;
- personal/sensitive data;
- confidentiality;
- client/tenant boundary;
- consent where applicable;
- data residency;
- provider exposure;
- retention period;
- deletion/withdrawal capability;
- generated-data rights;
- style-guide/copyright restrictions.

### Immutable lineage versus erasure

Research must address the tension between reproducible immutable dataset versions and legal/contractual physical deletion.

Potential patterns to investigate include:

- payload indirection;
- encryption-key destruction;
- tombstoning;
- manifest withdrawal;
- redacted reproducibility records;
- segregated sensitive stores;
- content hashes without retained content.

### Output

A governance model that constrains architecture rather than being added after implementation.

## 18. DG-11 — Budgets and material scale

### Purpose

Prevent architecture from being chosen for an imaginary scale while also identifying thresholds at which the initial design fails.

### Scale dimensions

#### Corpus

- records;
- source artifacts;
- editorial episodes;
- transitions;
- claims/gaps/events;
- tokens;
- raw bytes;
- normalized bytes;
- number/size of binary evidence assets.

#### Storage

- canonical storage;
- object storage;
- metadata/index storage;
- derived-materialization storage;
- replication;
- backups;
- retention amplification.

#### Curation

- CPU hours;
- GPU hours;
- embedding volume;
- classifier/model calls;
- dedup index size;
- temporary disk;
- wall time.

#### Human

- annotation hours;
- expert review hours;
- adjudication hours;
- cost per accepted example;
- review yield.

#### Synthetic

- generation input/output tokens;
- verification tokens;
- critic calls;
- acceptance yield;
- cost per retained example.

#### Training

- effective examples;
- effective tokens;
- epochs;
- sampling amplification;
- GPU hours;
- checkpoint/storage size;
- training-data throughput.

#### Evaluation

- instances;
- repeats;
- model-judge tokens;
- human-review volume;
- wall time;
- infrastructure retries.

#### Movement

- object-store requests;
- network bytes;
- egress;
- cache hit rate;
- loader throughput;
- GPU idle time attributable to input starvation.

### Candidate scale classes

Bootstrap/research may define classes such as:

```text
fixture
local developer
single-team
specialist-model training
multi-tenant/institutional
large distributed
```

Each architecture recommendation should state which scale classes it supports credibly.

## 19. DG-12 — Training-view compilation

### Central principle

The canonical editorial corpus should not be rewritten into whatever schema one training algorithm expects.

Instead:

```text
canonical episode E
      │
      ├── φ_detection(E)
      ├── φ_classification(E)
      ├── φ_sft(E)
      ├── φ_preference(E)
      ├── φ_reward(E)
      ├── φ_rlvr(E)
      ├── φ_trajectory(E)
      └── φ_eval(E)
```

Each `φ` is a versioned, reproducible training/eval-view compiler.

### Training views to research

#### Detection/classification

Inputs may contain artifact state, goal, priors, and evidence; targets identify findings/gaps or labels.

#### SFT

Teach acceptable editorial actions, edits, evidence use, verification, or end-to-end responses.

#### Preference

Construct `chosen/rejected` or ranked alternatives from accepted/rejected edits, reviewers, counterfactuals, or synthetic negatives.

#### Reward modeling

Map state/action/outcome combinations to human or verified preferences while preserving uncertainty.

#### RL with verifiable rewards

Use deterministic criteria where the task genuinely supports them, such as schema correctness, executable examples, endpoint coverage, or regression checks.

#### Trajectory/process supervision

Preserve useful intermediate actions such as inspect → diagnose → source → edit → verify rather than supervising only final text.

#### Distillation

Derive verified trajectories from stronger systems for smaller specialist models, with explicit generator provenance and held-out separation.

### Required outputs

- training-view schema requirements;
- compiler versioning requirements;
- reproducibility rules;
- loss/weight metadata requirements;
- incompatibility/round-trip expectations.

## 20. DG-13 — Dataset evaluation and ablation methodology

### Core question

How do we know dataset version B is better than dataset version A?

File cleanliness or curator intuition is insufficient.

### Candidate method

```text
dataset candidate A
        │
dataset candidate B
        │
        ▼
controlled / identical training recipe
        │
        ▼
proxy specialist checkpoints
        │
        ▼
frozen J-Editorial eval suite
        │
        ▼
capability + slice + cost comparison
```

### Variables to ablate

- source composition;
- filters;
- dedup threshold;
- quality threshold;
- synthetic ratio;
- negative ratio;
- reviewer-confidence threshold;
- sampling weights;
- curriculum;
- training-view compiler;
- source recency;
- rare-gap oversampling.

### Required safeguards

- frozen evaluation;
- same base checkpoint;
- same training compute where isolating data effects;
- known stochastic variance;
- repeated runs where needed;
- lineage-separated holdout;
- slice analysis;
- practical as well as statistical significance.

### Output

A repeatable data-ablation protocol that can turn dataset engineering into empirical model development.

## 21. DG-14 — Tool and substrate bake-off

### Purpose

Select tools only after the preceding requirements are explicit enough to produce representative workloads.

### Candidate categories

#### Semantic metadata / operational state

- Dolt;
- PostgreSQL/temporal/event patterns;
- other relational/event candidates justified by research.

#### Dataset versioning / lakehouse

- immutable manifests;
- lakeFS;
- DVC;
- Iceberg;
- Delta Lake;
- hosted registries/hubs;
- other current alternatives.

#### Bulk processing

- Hugging Face Datasets;
- PyArrow;
- Polars;
- DuckDB;
- NeMo Curator;
- Ray Data;
- Spark where relevant.

#### Training layouts/loaders

- Parquet;
- Arrow;
- MDS;
- WebDataset;
- Lance;
- native/tokenized binary layouts.

#### Metadata interoperability

- Croissant;
- data cards;
- other current standards.

#### Experiment/model/data tracking

- MLflow;
- W&B;
- hub/registry systems;
- custom immutable manifests where simpler.

### Representative bake-off workloads

At minimum, later research should consider tests such as:

- ingest and normalize a representative editorial history;
- materialize a logical dataset version;
- query lineage and eligibility;
- create a held-out split by artifact family/time;
- perform exact and near-duplicate checks;
- export an SFT view;
- export a preference view;
- stream/shuffle the view through a representative loader;
- reproduce the dataset from its manifest;
- withdraw/redact one source item and observe consequences;
- compare two dataset versions;
- estimate storage and operational cost at several scale classes.

### Output

Evidence-backed tool recommendations by role, with migration/exit paths.

## 22. Dataset quality model

The research should treat dataset quality as multidimensional rather than a scalar.

Candidate dimensions include:

```text
source quality
label / outcome confidence
provenance completeness
coverage
skill coverage
diversity
difficulty distribution
novelty
redundancy
recency
rights confidence
privacy risk
contamination risk
synthetic proportion
human-review quality
verifiability
training usefulness
evaluation usefulness
```

A record can be:

- strong training data but invalid held-out data;
- weak SFT data but strong preference-negative data;
- realistic production evidence but too ambiguous for objective grading;
- excellent eval material but legally non-redistributable.

The system should preserve these distinctions.

## 23. Learning-value hypothesis

A central strategic hypothesis is:

> **Provenance-rich editorial datasets can be used not only to measure specialist models, but to abstract recurring editorial patterns and reinforce desirable behavior during model adaptation.**

Examples include learning to:

- detect the right kind of gap;
- distinguish citation need from factual uncertainty;
- choose appropriate evidence;
- choose minimal justified remediation;
- prefer accepted evidence-backed changes over unsupported rewrites;
- avoid known regression patterns;
- abstain under uncertainty;
- follow domain-specific policy correctly;
- verify outcomes before claiming closure;
- make release decisions under explicit contracts.

This hypothesis requires empirical validation through DG-13. The dataset program must not assume that richer semantic labels necessarily improve model performance.

## 24. Future specialist-model implications

If the framework and dataset program succeed, J-Editorial could support training or adapting specialist models.

Candidate progression:

```text
base open-weight model
      ↓
J-Editorial SFT
      ↓
preference / reward optimization
      ↓
verified or bounded RL where appropriate
      ↓
J-Editorial specialist checkpoint
      ↓
frozen J-Editorial Bench
```

Potential specialist models/components could include:

- gap detector;
- gap classifier;
- evidence ranker;
- editorial action planner;
- patch/editor model;
- verifier;
- preference/reward model;
- release-readiness classifier;
- integrated editorial agent model.

Training a foundation model from random initialization is not a current program requirement. The research should preserve compatibility with future model training without architecting the entire framework around that speculative endpoint.

## 25. Required research deliverables

If this program survives bootstrap substantially intact, later execution should produce at least:

1. dataset vocabulary and ontology;
2. dataset lifecycle/state model;
3. canonical-versus-derived data model;
4. logical episode/record schema candidates;
5. lineage/identity graph contract;
6. role/eligibility/exposure model;
7. contamination and split contract;
8. canonical storage requirements;
9. physical-format/I/O policy;
10. curation pipeline specification;
11. synthetic-data provenance/governance policy;
12. human-annotation/adjudication policy;
13. sampling/mixture/curriculum findings;
14. budget and scale model;
15. training-view compiler contract;
16. dataset-ablation methodology;
17. governance/privacy/licensing/deletion model;
18. interoperability metadata recommendation;
19. tool/substrate bake-off results;
20. migration/portability requirements;
21. unresolved-risk register;
22. ADR/specification candidates justified by evidence.

The final artifact names may change during bootstrap.

## 26. Prospective results packet

Later research may produce a program result such as:

`research/programs/model-training-data/RESULTS.md`

or a more structured results directory if bootstrap decides the program needs separate reports per workstream.

The results packet should distinguish:

```text
established findings
empirical measurements
falsified assumptions
unresolved questions
recommendations
rejected alternatives
residual risks
ADR candidates
```

No `RESULTS.md` is created now because the research has not occurred.

## 27. Prospective gate — DATASET-ARCHITECTURE-G0

This gate name is provisional until bootstrap accepts it.

A pass should require enough evidence to answer or consciously defer the material questions needed before dataset implementation becomes architectural authority.

Candidate pass conditions:

- dataset vocabulary is coherent;
- canonical versus derivative layers are explicit;
- dataset role/eligibility is explicit;
- lineage and identity requirements are defined;
- held-out isolation/contamination policy is defensible;
- storage requirements are separated from tool selection;
- physical formats are mapped to explicit roles/access patterns;
- governance/privacy/licensing requirements constrain the design;
- scale/budget boundaries are quantified enough to choose an initial architecture;
- training-view compilation is reproducible in principle;
- dataset evaluation/ablation methodology exists;
- tool recommendations have representative workload evidence;
- migration/exit paths are credible;
- downstream ADRs can state decisions without hiding unresolved research.

A gate should return with findings rather than pass if a tool has been selected but the semantic or governance contract remains unclear.

## 28. Candidate downstream ADR/specification areas

The program may eventually justify decisions around:

- dataset identity and versioning;
- canonical episode/learning record;
- dataset lifecycle and eligibility;
- lineage model;
- source/payload storage;
- semantic metadata storage;
- dataset-version authority;
- physical bulk format;
- training materialization format;
- I/O/loaders;
- curation/deduplication;
- contamination/split policy;
- synthetic-data provenance;
- rights/privacy governance;
- training-view compilation;
- dataset documentation/interchange standard;
- experiment/data/model registry integration;
- budget/retention policy.

Bootstrap should determine whether these are one ADR each, grouped decisions, specification sections, or some other decision structure.

## 29. Explicit non-decisions

This charter does **not** decide that J-Editorial will use:

- Dolt;
- PostgreSQL;
- S3 or a specific provider;
- Parquet;
- Arrow;
- Iceberg;
- Delta Lake;
- lakeFS;
- DVC;
- Hugging Face Hub;
- Croissant;
- NeMo Curator;
- Ray;
- Spark;
- Mosaic Streaming/MDS;
- WebDataset;
- Lance;
- PyTorch;
- Transformers;
- TRL;
- Axolotl;
- MLflow;
- W&B;
- vLLM;
- SGLang;
- a particular base model;
- a particular cloud;
- a particular distributed training stack.

Named systems are comparison targets only.

## 30. Explicit non-goals before research execution

Before bootstrap releases the program, do not:

- create a production dataset schema;
- create a training corpus;
- freeze holdout examples;
- ingest proprietary/client data;
- scrape or redistribute style-guide corpora;
- choose dataset storage;
- create cloud buckets for the product;
- choose a lakehouse stack;
- generate large synthetic corpora;
- launch model-training runs;
- claim that historical edits improve models;
- publish benchmark or training-performance claims;
- create ADRs that preempt the research.

Small bootstrap fixtures or bounded prototypes are allowed only if explicitly required to resolve a bootstrap question.

## 31. Relationship to Doc Doctor

Doc Doctor is expected to be an important future source of authentic editorial episodes and implementation prior art, but this research program must not assume:

- Doc Doctor's current snapshot format is canonical;
- Git history is sufficient;
- current quality calculations are valid labels;
- acceptance events are unique gold answers;
- Obsidian-specific metadata generalizes;
- existing telemetry was collected with training reuse rights;
- current history granularity is sufficient for learning.

Later research should inspect Doc Doctor as both:

- a real product/data source; and
- a source of counterexamples that may falsify J-Editorial abstractions.

## 32. Relationship to J-Editorial Bench

Dataset architecture and benchmark architecture are mutually constraining but must remain separable.

The dataset program must support:

- immutable benchmark membership;
- lineage-aware holdouts;
- benchmark retirement;
- re-grading without corrupting raw episodes;
- exposure tracking;
- comparison across benchmark versions.

J-Editorial Bench must not silently redefine canonical editorial episode data to suit one harness.

## 33. Relationship to future model training

The dataset subsystem should be able to tell a future training run:

```text
which exact logical dataset version
which exact records
which exact training-view compiler
which exact selection/filter policy
which exact sampling weights
which exact tokenizer/chat template where data-dependent
which exact rights/eligibility policy
which exact contamination exclusions
which exact materialization/shards
```

A future checkpoint should be able to point back to those immutable identities.

The eventual model-training stack may change repeatedly. Dataset semantics should not have to change every time a trainer changes.

## 34. Research quality standard

The eventual research must not be a tool roundup.

A credible result should combine:

- current primary-source research;
- frontier/industrial examples;
- open reproducible datasets/recipes where possible;
- governance/standards analysis;
- representative J-Editorial workloads;
- quantitative scale/cost analysis;
- experiments and bake-offs;
- failure cases;
- explicit alternatives;
- adversarial review.

The question is not `What is fashionable in MLOps?`

The question is:

> **What dataset architecture lets J-Editorial preserve trustworthy editorial meaning and provenance while supporting reproducible evaluation and empirically useful model learning at the scales the product is actually likely to encounter?**

## 35. Current hold

This program is presently a placeholder under the repository-wide bootstrap hold.

Current status:

**`BOOTSTRAP-ALIGNED PLACEHOLDER / HELD`**

Current controlling gate:

**`ADVERSARIAL-REVIEW-REQUIRED`**

Prospective later program gate:

**`DATASET-ARCHITECTURE-G0`**

The next authorized use of this file is bootstrap scoping and revision, not deep research execution.
