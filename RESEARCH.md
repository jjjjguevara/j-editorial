# j-editorial — Research Charter

Status: **bootstrap-scoped / research executed in packets / architecture held**  
Authority: **subordinate to `BOOTSTRAP.md`; complementary to `ROADMAP.md`**  
Current gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Charter role: **repository-wide research method, evidence standard, program registry, and research-to-decision boundary**  
Layout: **program-major under `research/`; start at [`research/README.md`](research/README.md)**

This document defines how substantial research inside `j-editorial` should be scoped, executed, reviewed, synthesized, and converted into architectural decisions.

It is not the charter for any one research subject. Each program has its own charter under `research/programs/<slug>/`. This file exists so that dataset engineering, persistence, ontology design, evaluation science, agent design, and future research programs do not each invent incompatible evidence standards or research workflows.

## Accepted research scope — 2026-09-04

The accepted research directions are recorded once, in the section of the same name in [`BOOTSTRAP.md`](BOOTSTRAP.md), and with the owner's verbatim statements and their provenance in [`research/decisions/DECISION-LOG.md`](research/decisions/DECISION-LOG.md). This charter does not restate them. The merged PR #3 reconciliation recovered prior-acceptance excerpts for D-01, D-03, and D-04 with a transcript-authentication limitation; the controlling scope block preserves that qualification. Research-scope acceptance does not pass an empirical gate.

## 0. Status and revision history

This file was written as a pre-bootstrap scaffold, revised by the Phase 3 alignment script, and revised again on 2026-09-04 during the program-major restructure. Sections 1 to 20 keep their original numbering because other documents cite them; sections 21 to 28 were added by the restructure. Earlier scaffolding language describes the revision process and is not a prohibition on already authorized research.

| Revision | Change | Basis |
|---|---|---|
| Initial | Pre-bootstrap scaffold: method, evidence taxonomy, lifecycle, program contract, single-program registry | pre-bootstrap authoring |
| 2026-09-04, Phase 3 | Status line, accepted-scope block, section 0 lead sentence, and section 17 registry table rewritten by an alignment script committed from CI | `PR-2-MERGE` statement; automated authorship now prohibited by section 21 |
| 2026-09-04, restructure | Program-major layout; section 17 generated from Beads; section 18 updated; sections 21 to 28 added; accepted-scope block replaced by a pointer; every section 1 to 20 otherwise retained | `RESTRUCTURE-1` (verbatim in the decision log) |
| 2026-09-05, contract review | Scope provenance qualification and section 26.1 explicit gate aggregation; previous scope sentence preserved in section 29 | `BOOTSTRAP-REVIEW-2`; proposed for external revision, no gate released |

When bootstrap work executes, it is expected to revise the **scope, structure, terminology, authority relationships, research-program decomposition, gates, and deliverables** of this file and every program charter. That revision is part of bootstrap work, and a detailed charter is not accepted merely because it exists.

The temporal separation, with execution now recorded in dated packets:

```text
pre-bootstrap research scaffolds
  ↓
BOOTSTRAP EXECUTION  (recorded in research/packets/)
  ├── adversarially revise research scope
  ├── merge/split/reorder programs
  ├── normalize terminology and authority
  ├── establish dependencies and gates
  ├── decide what research is actually required
  ├── define budgets / evidence thresholds
  └── register accepted programs and gates in Beads  (done 2026-09-04; section 17)
  ↓
PROGRAMS BECOME READY  (per program; lifecycle in section 3)
  ↓
RESEARCH EXECUTION  (pre-registered; sections 23 to 25)
  ├── current SOTA reconnaissance
  ├── primary-source collection into research/LEDGER.md
  ├── experiments / bake-offs
  ├── empirical analysis
  └── synthesis
  ↓
PROGRAM GATE  (five verdicts only; section 26)
  ↓
ADR CANDIDATES
  ↓
IMPLEMENTATION
```

Bootstrap may decide that a proposed research program is too broad, too narrow, incorrectly sequenced, unnecessary, or missing dependencies. Deleting, splitting, or materially rewriting a charter is a successful bootstrap outcome, provided the superseded text is preserved per section 21.

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
research/programs/<slug>/CHARTER.md
program question / fan-out / gate
        │
        ▼
research/programs/<slug>/RESULTS.md + research/packets/<date>-<name>/
dated results, frozen execution records
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
- program `RESULTS.md`: **What did the evidence establish, fail to establish, or falsify?**
- `research/LEDGER.md`: **Which sources were inspected, at which version, establishing what?**
- `research/decisions/DECISION-LOG.md`: **What did the owner actually decide, in their own words?**
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

These five verdicts are the only gate verdicts. Compound verdicts such as `pass-with-constraints` are retired as terminal states; a gate decomposes into obligations, each carrying one of the five verdicts (section 26). Packets written before 2026-09-04 keep their original wording; the program `RESULTS.md` files restate them.

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
20. residual-risk and revisit policy;
21. independence declaration: who authored each fixture, validator, and red-team pass, and confirmation that they were separate sessions (section 24).

The template is [`research/templates/CHARTER.md`](research/templates/CHARTER.md). A heading that cannot be filled is written as "not yet specified"; the gap is itself a finding about readiness.

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

Beads is the authoritative registry (section 18). The table below is rendered from the tracker by `research/tools/render_registry.py`; edit the tracker, then re-render. Program identifiers name research boundaries, not Beads issue IDs; a phase result never closes a whole program.

<!-- BEGIN GENERATED REGISTRY -->
| Program | Alias | Lifecycle | Beads epic | Epic status | Open gates | Closed gates | Charter | Results |
|---|---|---|---|---|---|---|---|---|
| `amnesia` | BR-AMN | ACTIVE | `j-editorial-47m` | open | `AMN-G1`, `AMN-G2` | — | [charter](research/programs/amnesia/CHARTER.md) | [results](research/programs/amnesia/RESULTS.md) |
| `doc-doctor-integration` | BR-INT-DD | PLACEHOLDER | `j-editorial-vht` | open | `DD-G1` | — | [charter](research/programs/doc-doctor-integration/CHARTER.md) | [results](research/programs/doc-doctor-integration/RESULTS.md) |
| `evaluation` | BR-EVAL | BOOTSTRAP-SCOPED | `j-editorial-k4f` | open | `EV-G1` | — | [charter](research/programs/evaluation/CHARTER.md) | [results](research/programs/evaluation/RESULTS.md) |
| `event-state` | BR-EVENT-STATE | ACTIVE | `j-editorial-t2j` | open | `ES-G1`, `ES-G2` | — | [charter](research/programs/event-state/CHARTER.md) | [results](research/programs/event-state/RESULTS.md) |
| `frame-domain` | BR-FRAME/BR-DOM | ACTIVE | `j-editorial-4lk` | open | `FD-G1`, `FD-G2` | — | [charter](research/programs/frame-domain/CHARTER.md) | [results](research/programs/frame-domain/RESULTS.md) |
| `goal-priors` | BR-GOAL/BR-PRIORS | BOOTSTRAP-SCOPED | `j-editorial-wd2` | open | `GP-G1` | — | [charter](research/programs/goal-priors/CHARTER.md) | [results](research/programs/goal-priors/RESULTS.md) |
| `history` | BR-HIST | BOOTSTRAP-SCOPED | `j-editorial-dta` | open | `HIST-G1` | — | [charter](research/programs/history/CHARTER.md) | [results](research/programs/history/RESULTS.md) |
| `model-training-data` | DG-00..DG-14 | HELD-PLACEHOLDER | `j-editorial-o3k` | open | `DG-G0` | — | [charter](research/programs/model-training-data/CHARTER.md) | [results](research/programs/model-training-data/RESULTS.md) |
| `paired-synthesis` | paired-proof synthesis | ACTIVE | `j-editorial-c8r` | open | `PS-G1`, `PS-G2` | — | [charter](research/programs/paired-synthesis/CHARTER.md) | [results](research/programs/paired-synthesis/RESULTS.md) |
| `prose` | BR-PROSE | ACTIVE | `j-editorial-cz0` | open | `PR-G1`, `PR-G2` | — | [charter](research/programs/prose/CHARTER.md) | [results](research/programs/prose/RESULTS.md) |
| `representation` | BR-REP | ACTIVE | `j-editorial-0te` | open | `REP-G1` | — | [charter](research/programs/representation/CHARTER.md) | [results](research/programs/representation/RESULTS.md) |
| `security` | BR-SEC | BOOTSTRAP-SCOPED | `j-editorial-8dd` | open | `SEC-G1` | — | [charter](research/programs/security/CHARTER.md) | [results](research/programs/security/RESULTS.md) |

Rendered from `bd list` by `research/tools/render_registry.py`; 12 programs. Edit the tracker, not this table.
<!-- END GENERATED REGISTRY -->

Programs are added only when a distinct research boundary is justified. Adding one means creating its epic and gates in Beads, its directory under `research/programs/`, and its charter from the template, then re-rendering this table.

## 18. Beads relationship

Beads is the durable task tracker and, since 2026-09-04, the program registry.

- Each research program is one epic labeled `research-program` with metadata `program_slug`, `alias`, `lifecycle`, `charter`, and `results`.
- Each remaining gate is one task labeled `gate`, child of its program epic, with metadata `gate` and `program_slug`.
- Dependencies between programs are Beads dependencies that follow the next-phase contract graph.
- Lifecycle changes (section 3) are made by updating the epic's `lifecycle` metadata and re-rendering section 17.
- A gate may be closed only with a `RESULTS.md` entry that carries its verdict decomposition (section 26).

Markdown never substitutes for the tracker: `BOOTSTRAP.md` section 28 forbids competing task systems, and the phase packets that deferred tracker registration are the reason this rule is now explicit. Do not manually edit Beads database state. Remote synchronization follows the active agent profile in `AGENTS.md`.

## 19. Bootstrap execution obligations for research documents

Before bootstrap can claim that the repository's research architecture is scoped, it should inspect and revise at least:

- `BOOTSTRAP.md`;
- `ROADMAP.md`;
- this `RESEARCH.md`;
- every existing `research/programs/*/CHARTER.md`;
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

No deep research program is authorized merely because a charter exists. Programs marked ACTIVE in section 17 hold executed representation fixtures and bounded probes; none has passed an empirical gate. The model-training-data program remains held; its charter is aligned in vocabulary only and its release requires a separately authorized session.

Current gate remains:

**`ADVERSARIAL-REVIEW-REQUIRED`**

## 21. Controlling-document discipline

Applies to `BOOTSTRAP.md`, `ROADMAP.md`, this file, and every program charter.

1. **Supersede, never delete.** Text removed from a controlling document is preserved verbatim in a superseded-formulations section of the same document, with the decision that superseded it. `ROADMAP.md` section 14 and this file's section 13 already required preserving rejected directions; this makes the mechanism explicit.
2. **No automated authorship.** No CI job, script, or unattended process commits changes to a controlling document. Scripts may propose diffs on a branch; a person reviews and merges them. The Phase 3 alignment commit from CI is the precedent this rule closes.
3. **Verbatim basis.** An amendment that rests on an owner decision cites a row of `research/decisions/DECISION-LOG.md` that preserves the owner's exact words. A paraphrased or summarized decision is a recorded direction and cannot amend a controlling document.
4. **One home per statement.** Accepted scope lives in `BOOTSTRAP.md`; other documents point to it. Duplicated blocks drift.
5. **Revision tables.** Each controlling document carries a revision table naming the change, its basis, and the affected sections.

## 22. Repository layout

```text
research/
  README.md                 map of the tree
  LEDGER.md                 unified source ledger; new work cites SRC-### only
  decisions/                owner decisions with verbatim statements; acceptance records
  programs/<slug>/          living state of one program
    CHARTER.md              section 4 contract, from research/templates/CHARTER.md
    RESULTS.md              dated entries, from research/templates/RESULTS-ENTRY.md
    COVERAGE.md             contract-case coverage, where the program owns one
    fixtures/ tools/ results/
  packets/<date>-<name>/    frozen record of one execution run (section 28)
  templates/                charter, pre-registration, results-entry, coverage
  tools/                    repository-wide checks: link check, registry rendering
```

Program directories hold living material. Phases are dated entries in `RESULTS.md` and frozen packets, never new directories under `research/`.

## 23. Pre-registration

Before a fixture, validator, or measurement is authored, the program commits a pre-registration from [`research/templates/PREREGISTRATION.md`](research/templates/PREREGISTRATION.md) stating the question, hypotheses in falsifiable form, the encoding or measurement protocol, predicted outcomes and their gate consequences, falsification criteria achievable with the planned material, controls, the independence plan, and the evidence-retention plan. Validators are written against the pre-registration, not against the fixture. A fixture or validator that predates its pre-registration cannot count toward a gate; it may be kept as exploratory material and must be labeled so. Deviations are recorded after execution.

Rationale: in Phases 1 to 3 the hypotheses, the fixtures that instantiate them, and the validators that check the fixtures were authored by one lineage in one day, and no check could have failed.

## 24. Independence

Fixture author, validator author, and red team are separate sessions at minimum, and separate people where available. A red-team pass attempts to construct a fixture that passes the validator while violating the intended semantics, and attempts to encode material the fixture author did not choose. No gate reads PASS without a red-team pass recorded in `RESULTS.md`. Every charter carries an independence declaration (section 4, item 21), and every results entry names who executed, who validated, and who red-teamed.

## 25. Evidence retention and method labels

1. A digest is evidence only when the bytes it identifies are committed in the repository or retrievable from an authorized, pinned location named beside it. A digest without retrievable bytes is a claim, class 5.8, and is labeled so.
2. Raw outputs of executed checks are committed beside their digests, redacted where rights or privacy require, with the redaction recorded.
3. "Deterministic" is reserved for executed code with committed output and a pinned environment. An agent or person reading source through a connector is class 5.6 expert judgment or 5.7 secondary synthesis, never `deterministic-high`, whatever its confidence.
4. Tool names in evidence records name real executables with versions; a manual method is recorded as a manual method.
5. Synthetic actors, scenarios, and counterfactuals are labeled synthetic in the record itself and cannot satisfy an obligation that calls for observation.

The Phase 3 fragment manifest, which commits fragment text beside its SHA-256, is the retention pattern to follow.

## 26. Gate vocabulary and decomposition

A gate is decomposed into obligations. Each obligation receives exactly one verdict from section 3: `PASS`, `NARROW`, `RETURN-WITH-FINDINGS`, `DEFER`, or `REJECT`. `PASS` may carry a bounded scope in parentheses, such as "PASS (bounded to literal text matching)", but never a constraint that would change the verdict. A gate as a whole is `PASS` only when every obligation is `PASS`; otherwise it reports the lowest verdict present and lists the returned obligations. `pass-with-constraints` and similar compounds are retired. Verdicts are recorded in `RESULTS.md` using [`research/templates/RESULTS-ENTRY.md`](research/templates/RESULTS-ENTRY.md) and mirrored to the gate task in Beads when it closes.

### 26.1 Explicit aggregation and admission policy

This is a proposed method correction under `BOOTSTRAP-REVIEW-2`, for external revision. It defines the previously unspecified "lowest verdict" in section 26 as a gate-disposition policy, not an ordering of scientific certainty:

1. A missing/unapproved obligation inventory, a missing required verdict, invalid evidence admission, or uncovered required case yields `RETURN-WITH-FINDINGS`; missing evidence cannot disappear from the denominator.
2. Otherwise, a `REJECT` on a required obligation yields `REJECT` for the candidate under that gate's declared scope. Otherwise use `RETURN-WITH-FINDINGS` if present, then `DEFER` if present, then `NARROW` if present. Preserve every individual verdict and reason.
3. `PASS` requires a nonempty, approved required-obligation inventory and `PASS` on every required obligation, including coverage, pre-registration, independence, and red-team requirements. An explicitly authorized not-applicable disposition changes the scoped inventory with a recorded reason; it is not an automatic pass.

A missing or inadmissible result is not a falsification result. `DEFER` does not satisfy a required obligation, and `NARROW` does not release the original broader scope. Any release under a smaller scope requires explicit owner approval and a newly identified gate scope. A trivial round trip can pass a narrowly named serialization check but cannot pass a semantic or behavioral obligation by relabeling it.

Static contract review and repeated tooling checks must identify themselves as such. Neither is a new empirical fixture/validator experiment or an independent validation of amendments authored in the same session. A green CI job does not override the result decomposition or owner gate.

## 27. Coverage matrices

A program or synthesis that is accountable for a set of contract cases maintains a coverage matrix from [`research/templates/COVERAGE.md`](research/templates/COVERAGE.md) mapping each case to the fixture transactions, validator checks, or executed probes that exercise it, with a strength column. Rows marked `none` or `trivial` block `PASS` for any gate that depends on them. The paired proof's matrix is [`research/programs/paired-synthesis/COVERAGE.md`](research/programs/paired-synthesis/COVERAGE.md).

## 28. Packets

A packet under `research/packets/<date>-<name>/` is the frozen record of one execution run: its README, gate statements, reproduction instructions, cross-program results, runners, and the ledger additions it made. Once merged, a packet changes only by link maintenance and superseded banners; its verdict text is never edited. Program `RESULTS.md` files restate packet verdicts in the section 26 vocabulary and hold any reclassification. A new execution run creates a new packet and appends entries to the affected programs' results; it never creates a new phase directory.


## 29. Superseded formulations

### 2026-09-05 scope-provenance paragraph

Basis: proposed record correction under `BOOTSTRAP-REVIEW-2`, using the merged PR #3 receipt without upgrading the recovered transcript provenance. Preserved verbatim from `360d6ed15fbee7d38dc659f8324763bf637b3924`:

The accepted research directions are recorded once, in the section of the same name in [`BOOTSTRAP.md`](BOOTSTRAP.md), and with the owner's verbatim statements and their provenance in [`research/decisions/DECISION-LOG.md`](research/decisions/DECISION-LOG.md). This charter does not restate them. Note that the `D-03` acceptance preserves no owner statement and is a recorded research direction until confirmed.
