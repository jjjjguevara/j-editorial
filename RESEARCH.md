# j-editorial — Research Charter

Status: **provisional / bootstrap-scoped / not yet an execution record**  
Authority: **subordinate to `BOOTSTRAP.md`; complementary to `ROADMAP.md`**  
Current gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Charter role: **repository-wide research method, evidence standard, program registry, and research-to-decision boundary**

This document defines how substantial research inside `j-editorial` should be scoped, executed, reviewed, synthesized, and converted into architectural decisions.

It is not the charter for any one research subject. Large subjects receive their own program charters under `research/`. This file exists so that dataset engineering, persistence, ontology design, evaluation science, agent design, and future research programs do not each invent incompatible evidence standards or research workflows.

## 0. Bootstrap status and mandatory revision rule

This file is a **pre-bootstrap scaffold**.

When the active bootstrap/adversarial-review work executes, it is expected to revise the **scope, structure, terminology, authority relationships, research-program decomposition, gates, and deliverables** of this file and every research charter that already exists.

That revision is part of bootstrap work.

The presence of a detailed charter before bootstrap execution does **not** mean its current shape is accepted. Its purpose is to make the research obligations visible early enough that bootstrap can challenge them deliberately instead of discovering them after implementation begins.

The intended temporal separation is:

```text
NOW
  ↓
pre-bootstrap research scaffolds
  ↓
BOOTSTRAP EXECUTION
  ├── adversarially revise research scope
  ├── merge/split/reorder programs
  ├── normalize terminology and authority
  ├── establish dependencies and gates
  ├── decide what research is actually required
  ├── define budgets / evidence thresholds
  └── translate accepted programs into executable Beads work
  ↓
BOOTSTRAP GATE CLOSES / PROGRAMS BECOME READY
  ↓
LATER RESEARCH EXECUTION
  ├── current SOTA reconnaissance
  ├── primary-source collection
  ├── experiments / bake-offs
  ├── empirical analysis
  └── synthesis
  ↓
PROGRAM GATE
  ↓
ADR CANDIDATES
  ↓
IMPLEMENTATION
```

Bootstrap may decide that a proposed research program is too broad, too narrow, incorrectly sequenced, unnecessary, or missing dependencies. Deleting, splitting, or materially rewriting a charter is a successful bootstrap outcome.

## 1. Research purpose

Research exists to reduce a concrete uncertainty that would otherwise be encoded prematurely in:

- the J-Editorial specification;
- architecture;
- schemas;
- storage contracts;
- evaluation claims;
- training data;
- APIs;
- model-training pipelines;
- product boundaries;
- operating assumptions;
- compliance/governance behavior.

Research is not a decorative bibliography and is not a mechanism for rationalizing a preferred tool after the fact.

Every material program should be able to answer:

> **What decision, specification boundary, capability gate, or product hypothesis becomes better informed if this work succeeds?**

If there is no answer, the research program should be narrowed or rejected.

## 2. Documentary authority and roles

During bootstrap, the intended relationship is:

```text
explicit owner constraints
        ↓
BOOTSTRAP.md
architecture invariants / implementation hold
        │
        ├───────────────┐
        ▼               ▼
RESEARCH.md         ROADMAP.md
research method     product progression
        │
        ▼
research/<program>/CHARTER.md
program question / fan-out / gate
        │
        ▼
research execution artifacts
        │
        ▼
RESULTS / synthesis
        │
        ▼
accepted ADR or specification revision
        │
        ▼
implementation
```

The documents answer different questions:

- `BOOTSTRAP.md`: **What must not be assumed before we build?**
- `RESEARCH.md`: **What constitutes adequate research in this repository?**
- `ROADMAP.md`: **What could become possible, and in what evidence-driven order?**
- program `CHARTER.md`: **What exactly must this research program discover?**
- program results: **What did the evidence establish, fail to establish, or falsify?**
- ADR: **What decision is implementation now authorized to rely on?**

A research charter is never itself an architecture decision.

## 3. Research lifecycle

A substantial research program should move through explicit states rather than silently becoming authoritative.

Candidate lifecycle:

```text
PLACEHOLDER
    ↓
BOOTSTRAP-SCOPED
    ↓
READY
    ↓
ACTIVE
    ↓
SYNTHESIS
    ↓
ADVERSARIAL-REVIEW
    ├── PASS
    ├── NARROW
    ├── RETURN-WITH-FINDINGS
    ├── DEFER
    └── REJECT
```

### Placeholder

A problem is important enough to reserve a research boundary, but its final scope has not survived bootstrap review.

### Bootstrap-scoped

Bootstrap has revised the charter enough to identify the actual questions, dependencies, and proof obligations. Deep research may still be deferred.

### Ready

Inputs, dependencies, source requirements, budgets, and gate criteria are sufficient for research execution.

### Active

Evidence collection and experiments are occurring.

### Synthesis

The program is reconciling evidence, alternatives, contradictions, cost, and residual uncertainty.

### Adversarial review

A reviewer tests the conclusions and asks whether the evidence actually justifies downstream decisions.

### Pass / narrow / return / defer / reject

Research can produce a useful non-selection. `No decision yet` is preferable to a false sense of certainty.

## 4. Research-program contract

A mature program charter should eventually define, at minimum:

1. authority and status;
2. mission;
3. why the program is separate;
4. decisions or specification questions it informs;
5. explicit in-scope and out-of-scope work;
6. dependencies on other research programs;
7. current hypotheses to attack;
8. required current/SOTA reconnaissance;
9. required primary-source classes;
10. industrial and academic comparison set;
11. empirical experiments or bake-offs;
12. representative workloads or fixtures;
13. material scale and budget analysis;
14. security/privacy/licensing/governance implications;
15. interoperability and migration requirements;
16. deliverables;
17. falsification criteria;
18. gate criteria;
19. downstream ADR/specification candidates;
20. residual-risk and revisit policy.

The exact template may be revised during bootstrap.

## 5. Evidence taxonomy

Research artifacts should distinguish evidence classes instead of blending them into undifferentiated notes.

### 5.1 Primary specification/documentation evidence

Examples:

- official technical documentation;
- standards;
- source repositories;
- implementation documentation;
- regulatory text;
- model/system cards;
- dataset cards;
- benchmark specifications;
- official architecture papers.

Primary sources are preferred for factual claims about a system's actual behavior or contract.

### 5.2 Peer-reviewed / archival research

Use for:

- methods;
- empirical results;
- statistical findings;
- benchmark design;
- data-quality research;
- training/data scaling behavior.

Publication prestige alone does not make a result applicable to J-Editorial.

### 5.3 Industrial/SOTA practice

Evidence from serious production or frontier-scale systems is required where the decision concerns operational data, model training, evaluation, distributed processing, or governance.

Examples may include public technical reports, engineering blogs with sufficient implementation detail, open datasets, open training recipes, and reproducible tooling from major model or infrastructure teams.

### 5.4 Repository observation

Direct inspection of source code, schemas, tests, issues, release histories, migrations, or real product behavior.

Existing implementation is evidence about what exists, not automatic authority about what should exist.

### 5.5 Experimental evidence

Evidence produced by a controlled J-Editorial prototype, benchmark, migration trial, storage bake-off, dataset ablation, or other reproducible experiment.

Where tool choice depends on workload behavior, experimental evidence should outrank feature-table comparison whenever feasible.

### 5.6 Expert / domain evidence

Human domain judgment, annotation studies, review outcomes, interviews, or structured adjudication.

Expert judgment should retain reviewer identity/role, instructions, disagreement, and adjudication where material.

### 5.7 Secondary synthesis

Useful for discovering the field and competing vocabulary. Important claims should be traced to primary or stronger sources when possible.

### 5.8 Hypothesis

An inference or working proposition that has not yet been established. Hypotheses must remain visibly distinct from evidence.

## 6. Source-quality rules

Research should normally:

- prefer primary sources for system behavior and specification;
- inspect current versions rather than relying on stale summaries;
- compare publication date with actual event/release date;
- preserve version identifiers where systems change rapidly;
- use archival sources when a historically important artifact is no longer live;
- distinguish benchmark authors' claims from independent validation;
- distinguish marketing claims from reproducible measurements;
- retain contradictory evidence rather than averaging it away;
- verify material quantitative claims against the underlying study when possible.

Named tools or projects in a pre-bootstrap charter are **research targets**, not endorsed selections. Their relevance must be rechecked at research-execution time.

## 7. SOTA / frontier requirement

Programs dealing with rapidly changing ML, data, storage, inference, collaboration, or evaluation technology must include a fresh reconnaissance at execution time.

A charter written months earlier must not freeze a stale comparison set.

The execution packet should state:

```text
research cutoff date:
versions/releases inspected:
major systems considered:
major systems excluded and why:
```

For model/data engineering, the comparison set should include both:

- frontier/large-scale practice that exposes scaling and governance problems; and
- smaller practical systems appropriate to J-Editorial's likely initial material scale.

The largest system is not automatically the relevant architecture.

## 8. Comparative research requirements

A program should not ask only, `Does candidate X work?`

It should establish credible alternatives.

Candidate comparison dimensions include:

- semantic fit;
- correctness guarantees;
- maturity;
- reversibility;
- operational complexity;
- local-first viability;
- scale ceiling/floor;
- developer ergonomics;
- portability;
- open standards;
- licensing;
- ecosystem health;
- observability;
- failure recovery;
- migration cost;
- security/privacy;
- total cost;
- vendor/dependency risk.

Comparison dimensions must be tailored to the program rather than copied mechanically.

## 9. Research experiments and bake-offs

Where an architecture decision depends on measurable behavior, the program should define a representative experiment before selecting a tool.

Examples:

- replay real editorial histories through competing persistence models;
- measure semantic-query complexity;
- test round-trip fidelity between document representations;
- compare dataset physical layouts under representative training access patterns;
- test lineage and rollback behavior;
- run proxy-model ablations against competing dataset curation strategies;
- compare deterministic versus model graders against expert labels;
- measure near-duplicate contamination across candidate splits;
- test local versus remote data-loader throughput;
- quantify storage amplification and egress.

Experiments must state what outcome would change the recommendation.

## 10. Quantitative claims and budgets

Research involving data or model systems should preserve material magnitudes rather than saying only `large`, `fast`, or `expensive`.

Relevant units may include:

- records;
- artifacts;
- episodes;
- tokens;
- bytes;
- storage amplification;
- object counts;
- throughput;
- latency percentiles;
- CPU/GPU hours;
- FLOPs;
- network/egress volume;
- annotation hours;
- model-generation tokens;
- dollars;
- human-review cost;
- wall-clock duration.

Budgets should be considered at several scales rather than extrapolating one scale indefinitely.

## 11. Research reproducibility

A research conclusion should preserve enough provenance to understand what was actually inspected or measured.

Depending on the program, this may include:

- source URLs and retrieval dates;
- source commit/release IDs;
- datasets and versions;
- scripts/notebooks;
- workload manifests;
- environment/container versions;
- configuration;
- random seeds;
- raw measurements;
- transformation steps;
- analysis logic;
- exclusions;
- known failures.

Research reproducibility requirements should be proportional to the consequence of the downstream decision.

## 12. Findings versus decisions

Research output should separate:

### Finding

A fact or empirically supported observation.

### Interpretation

What the finding may imply for J-Editorial.

### Recommendation

The research team's proposed direction.

### Decision

A later accepted architectural/specification choice.

A recommendation does not become binding until the relevant authority accepts it through the appropriate decision process.

## 13. Failure and negative evidence

Research is expected to retain:

- failed experiments;
- tools that were rejected;
- approaches that did not scale down or up;
- assumptions contradicted by real data;
- unresolved disagreements;
- incomplete source coverage;
- benchmark instability;
- uncertainty that remains material.

Negative evidence is useful because it prevents future contributors from repeating an abandoned path without understanding why.

## 14. Security, privacy, licensing, and governance

These concerns are part of research scope whenever the program touches data, user content, proprietary documents, external models, executable content, or third-party standards.

A research program should identify, where relevant:

- data ownership;
- permitted use;
- training eligibility;
- evaluation eligibility;
- redistribution rights;
- retention;
- deletion/erasure requirements;
- sensitive categories;
- model-provider exposure;
- data residency;
- secrets;
- sandboxing;
- third-party licenses;
- supply-chain risk.

A technically attractive architecture that cannot satisfy data-governance constraints is not a successful result.

## 15. Research-to-ADR boundary

A program charter may enumerate **ADR candidates** but must not contain the accepted answer to those ADRs.

The intended chain is:

```text
research question
    ↓
evidence
    ↓
experiments
    ↓
synthesis / results
    ↓
adversarial review
    ↓
ADR candidate
    ↓
accepted decision
    ↓
implementation
```

Examples:

- a charter may require evaluating Parquet, Arrow, MDS, or WebDataset;
- results may find Parquet preferable for one role;
- only the accepted ADR says `Parquet is the required format for role X`.

This separation is mandatory for decisions with substantial lock-in.

## 16. Cross-program dependencies

Research programs may depend on one another and should not silently duplicate or preempt decisions.

Examples:

- dataset identity may depend on canonical editorial identity;
- training views may depend on the episode/transition model;
- contamination policy may depend on the benchmark specification;
- persistence research may provide candidate substrates for dataset metadata without defining dataset semantics;
- privacy research may constrain storage and training eligibility;
- agent evaluation may depend on stable tool and grader contracts.

Bootstrap should normalize these dependencies before deep research is launched.

## 17. Program registry

This registry is intentionally small. Programs should be added only when a distinct research boundary is justified.

| Program | Charter | Gate | Current state | Intended execution |
|---|---|---|---|---|
| Model-training dataset architecture, engineering, and governance | `research/model-training-data/CHARTER.md` | `DATASET-ARCHITECTURE-G0` | Placeholder / pre-bootstrap | After bootstrap scopes and releases the program |

Future candidate programs may include editorial ontology, history/persistence, evaluation science, or other architecture verticals. Their existence and boundaries should be decided during bootstrap rather than pre-created for symmetry.

## 18. Beads relationship

Beads remains the durable task tracker.

This document does not create a competing task list.

During bootstrap, accepted research programs should eventually be decomposed into Beads epics/tasks with:

- dependencies;
- research aliases;
- gate tasks;
- completion records or results expectations;
- review/validator steps where appropriate.

A Markdown charter describes the program contract. Beads records executable work and status.

Do not manually edit Beads database state.

## 19. Bootstrap execution obligations for research documents

Before bootstrap can claim that the repository's research architecture is scoped, it should inspect and revise at least:

- `BOOTSTRAP.md`;
- `ROADMAP.md`;
- this `RESEARCH.md`;
- every existing `research/*/CHARTER.md`;
- Beads research work created from those documents.

The review should ask:

1. Is this document still necessary?
2. Is its authority relationship correct?
3. Is its scope too broad or too narrow?
4. Does it duplicate another document?
5. Are its terms aligned with the accepted domain vocabulary?
6. Does it assume a decision that bootstrap has not accepted?
7. Are program dependencies explicit?
8. Should its gate change?
9. Which parts belong in a later research execution packet instead?
10. Which details should be deleted until evidence exists?

This means the current documents are **inputs to bootstrap**, not immutable outputs that bootstrap must preserve.

## 20. Current research hold

No deep research program is authorized merely because a charter exists.

For the model-training-data program specifically, the current document reserves and structures the problem because dataset architecture can affect the core semantic model and later training/evaluation validity. The substantive SOTA investigation, tool bake-offs, dataset experiments, budget measurements, and architecture synthesis are expected to occur after bootstrap has revised and released that research program.

Current gate remains:

**`ADVERSARIAL-REVIEW-REQUIRED`**
