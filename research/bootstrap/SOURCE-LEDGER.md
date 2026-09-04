# Bootstrap source ledger

Status: **phase-1 evidence record**  
Cutoff and retrieval date unless otherwise noted: **2026-09-04**  
Doc Doctor inspected commit: **`655c176f05a864887f03e0b392550ba2155a2e26`**  
Dataset-research evidence collection: **not performed**

This ledger records the evidence used in the phase-1 adversarial review. It is not a bibliography of everything relevant to J-Editorial. A source is included because it supports or challenges a specific bootstrap assumption.

## Source-quality rules applied

- Repository source and tests outrank product summaries for existing behavior.
- Standards and official documentation establish contracts and stated capabilities.
- Vendor material establishes vendor claims and maturity, not independent superiority.
- Research papers establish reported methods/results within their study scope.
- Preprints are explicitly marked.
- A source's presence does not imply adoption.

## Repository authority and prior-art evidence

### R-01 — J-Editorial bootstrap contract

- Source: [`BOOTSTRAP.md` at the inspected base](https://github.com/jjjjguevara/j-editorial/blob/fdfffb0da4eabd7c3db7d303013e0777db149e82/BOOTSTRAP.md)
- Supports: implementation hold; lifecycle/quality/readiness separation; goal contracts; normative priors; gap/evidence/operation/outcome hypothesis; aggregate-score caution; persistence neutrality; adversarial decision packets; exit criteria.
- Limitation: pre-bootstrap contract, intentionally provisional.

### R-02 — Repository research charter

- Source: [`RESEARCH.md`](https://github.com/jjjjguevara/j-editorial/blob/fdfffb0da4eabd7c3db7d303013e0777db149e82/RESEARCH.md)
- Supports: evidence taxonomy; current-source requirement; research-to-ADR boundary; negative evidence; reproducibility; program lifecycle.
- Limitation: explicitly requires material bootstrap revision.

### R-03 — Product roadmap

- Source: [`ROADMAP.md`](https://github.com/jjjjguevara/j-editorial/blob/fdfffb0da4eabd7c3db7d303013e0777db149e82/ROADMAP.md)
- Supports: framework-before-product progression; Stage 0 specification before executable core; Doc Doctor as later reference integration; server/control-plane deferral.
- Limitation: possibilities and sequence hypotheses, not commitments.

### R-04 — Model-training data research charter

- Source: [`research/model-training-data/CHARTER.md`](https://github.com/jjjjguevara/j-editorial/blob/fdfffb0da4eabd7c3db7d303013e0777db149e82/research/model-training-data/CHARTER.md)
- Supports: dataset program is held; bootstrap may only revise its scope, boundaries, dependencies, budgets, and gate; no corpus/schema/tool selection or dataset execution.
- Limitation: placeholder whose research questions have not been executed in this session.

### R-05 — Repository Beads configuration

- Source: [`.beads/config.yaml`](https://github.com/jjjjguevara/j-editorial/blob/fdfffb0da4eabd7c3db7d303013e0777db149e82/.beads/config.yaml)
- Supports: Dolt-backed Beads synchronization and prohibition on assuming JSONL-only operation.
- Limitation: configuration alone does not expose or mutate native work records.

### DD-01 — Doc Doctor product description

- Source: [`doc-doctor/README.md`](https://github.com/jjjjguevara/doc-doctor/blob/655c176f05a864887f03e0b392550ba2155a2e26/README.md)
- Supports: existing integration surface, Obsidian/Markdown focus, stubs as editorial demand signals, Git-backed milestones, CLI/MCP/AI-assisted workflow.
- Limitation: product documentation is not independent validation.

### DD-02 — Doc Doctor document entity

- Source: [`document.rs`](https://github.com/jjjjguevara/doc-doctor/blob/655c176f05a864887f03e0b392550ba2155a2e26/core/crates/doc-doctor-domain/src/entities/document.rs)
- Supports: current L1 model stores one refinement value plus origin, form, audience, and stubs.
- Limitation: implementation predates J-Editorial bootstrap decisions.

### DD-03 — Doc Doctor refinement semantics

- Source: [`refinement.rs`](https://github.com/jjjjguevara/doc-doctor/blob/655c176f05a864887f03e0b392550ba2155a2e26/core/crates/doc-doctor-domain/src/entities/refinement.rs)
- Supports: current scalar conflates progress, quality/completeness, review readiness, and publication readiness.
- Limitation: code comments and thresholds are design assertions, not calibrated measurements.

### DD-04 — Doc Doctor stub ontology

- Source: [`stub.rs`](https://github.com/jjjjguevara/doc-doctor/blob/655c176f05a864887f03e0b392550ba2155a2e26/core/crates/doc-doctor-domain/src/entities/stub.rs)
- Supports: current gap taxonomy, vector-family mapping, severity forms, fixed penalties, origins, anchors, dependencies, and prioritization fields.
- Limitation: unknown types default to `Creation`; fixed mappings and penalties are not empirically justified.

### DD-05 — Doc Doctor state calculations

- Source: [`state.rs`](https://github.com/jjjjguevara/doc-doctor/blob/655c176f05a864887f03e0b392550ba2155a2e26/core/crates/doc-doctor-domain/src/calculations/state.rs)
- Supports: current health/usefulness/freshness/trust formulas and placeholder compliance/coverage values.
- Limitation: formulas are implementation defaults; compliance and coverage are hard-coded placeholders.

### DD-06 — Doc Doctor trajectory calculations

- Source: [`trajectory.rs`](https://github.com/jjjjguevara/doc-doctor/blob/655c176f05a864887f03e0b392550ba2155a2e26/core/crates/doc-doctor-domain/src/calculations/trajectory.rs)
- Supports: current “vector physics” metaphor and formulae for potential energy, friction, magnitude, and completion forecasts.
- Limitation: metaphorical quantities do not have demonstrated measurement validity.

### DD-07 — Doc Doctor calculation defaults

- Source: [`config.rs`](https://github.com/jjjjguevara/doc-doctor/blob/655c176f05a864887f03e0b392550ba2155a2e26/core/crates/doc-doctor-domain/src/config.rs)
- Supports: current universal defaults for weights, audience gates, origin-based trust, stub penalties, and freshness half-lives.
- Limitation: “80/20 power law” is asserted without supporting calibration evidence.

## Representation, annotation, provenance, and addressing

### REP-01 — W3C Web Annotation Data Model

- Source: [W3C Recommendation](https://www.w3.org/TR/annotation-model/)
- Supports: annotation/body/target separation; motivations; rights; lifecycle metadata; selectors including text quote, text position, range, and state.
- Relevance: strong prior for findings attached to changing artifact regions.
- Limitation: does not define J-Editorial obligations, editorial outcomes, release gates, or persistence.

### REP-02 — W3C PROV-O

- Source: [PROV-O Recommendation](https://www.w3.org/TR/prov-o/)
- Supports: Entity, Activity, Agent, derivation, attribution, generation, and usage relations.
- Relevance: prior for evidence and operation provenance.
- Limitation: intentionally general; does not supply editorial domain semantics.

### REP-03 — CommonMark 0.31.2

- Source: [CommonMark specification](https://spec.commonmark.org/0.31.2/)
- Supports: precise Markdown parsing and conformance examples.
- Relevance: bounded, testable source format for an initial technical-doc slice.
- Limitation: many production Markdown dialects add non-portable extensions.

### REP-04 — ProseMirror document model and transactions

- Source: [official guide](https://prosemirror.net/docs/guide/)
- Supports: schema-governed immutable document trees, transactions, steps, position mapping, collaboration, and undo.
- Relevance: demonstrates structured operations and rebasing requirements.
- Limitation: editor-state positions are relative to a document state; ProseMirror is not a history or provenance specification.

### REP-05 — Pandoc AST and conversions

- Source: [Pandoc User’s Guide](https://pandoc.org/MANUAL.html)
- Supports: reader/AST/writer architecture and broad format conversion.
- Relevance: evidence for structured projections and format adapters.
- Limitation: conversions can be lossy when the source format has constructs the target/AST cannot preserve; it is not proof of exact round-trip fidelity.

### REP-06 — Yjs relative positions

- Source: [official Yjs documentation](https://docs.yjs.dev/api/relative-positions)
- Supports: positions that remain associated with context through collaborative edits and converge across replicas.
- Relevance: credible alternative to raw character offsets.
- Limitation: requires Yjs document identity/history; a position can resolve to null after deletion.

## History and persistence candidates

### HIST-01 — Git object model

- Source: [Pro Git, Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- Supports: content-addressed objects, trees, and commit snapshots.
- Relevance: exact source snapshots, branching, interoperability, and broad tooling.
- Limitation: does not natively model semantic operations, row-level queries, or continuous edits between commits.

### HIST-02 — Dolt “Git for data”

- Source: [official Dolt documentation](https://www.dolthub.com/docs/introduction/getting-started/git-for-data/)
- Supports: commits, branches, merges, and SQL tables under version control.
- Relevance: candidate for queryable domain records plus history.
- Limitation: row/cell history semantics depend on relational identity and schema design; it does not solve editorial identity by itself.

### HIST-03 — Dolt system tables

- Source: [official Dolt system-table documentation](https://www.dolthub.com/docs/sql-reference/version-control/dolt-system-tables/)
- Supports: commit, log, history, and diff query surfaces.
- Relevance: concrete evidence for queryable historical analysis.
- Limitation: database-level diffs are not automatically meaningful editorial operations.

### HIST-04 — DeltaDB early access

- Source: [DeltaDB early-access page](https://zed.dev/deltadb)
- Supports: Zed’s stated operation-level history, stable identity, branching from points in history, and code/conversation association.
- Relevance: important design prior for continuous editorial history.
- Limitation: early-access product material, not a stable public dependency contract or general-purpose editorial database.

### HIST-05 — DeltaDB design account

- Source: [“Software Is Made Between Commits,” 2026-06-11](https://zed.dev/blog/introducing-deltadb)
- Supports: fine-grained deltas, stable delta identity, CRDT worktrees, and references intended to survive movement.
- Relevance: strongest current argument for history below commit granularity.
- Limitation: vendor account centered on code and agent conversations; no independent workload evaluation.

### HIST-06 — Delta private beta

- Source: [“Introducing Delta,” 2026-08-12](https://zed.dev/blog/introducing-delta)
- Supports: private-beta status, Git interoperability, real-time replication, and review anchored to evolving code.
- Relevance: maturity check.
- Limitation: confirms that DeltaDB is not yet an appropriate assumed foundation for J-Editorial.

### HIST-07 — PostgreSQL logical decoding

- Source: [PostgreSQL 18 documentation](https://www.postgresql.org/docs/current/logicaldecoding.html)
- Supports: extraction of persistent table changes into an interpretable stream.
- Relevance: candidate building block for event/history projections.
- Limitation: change streams and old-row detail depend on schema and replica identity; application semantics remain external.

### HIST-08 — PostgreSQL temporal constraints

- Source: [PostgreSQL feature description](https://www.postgresql.org/about/featurematrix/detail/temporal-constraints/)
- Supports: time-range integrity constraints.
- Relevance: useful for validity periods and non-overlap.
- Limitation: temporal constraints do not by themselves provide system-versioned editorial history or event provenance.

## Evaluation and measurement

### EVAL-01 — HELM

- Source: [Stanford CRFM HELM](https://crfm.stanford.edu/helm/latest/)
- Supports: scenario-based, multi-metric, reproducible evaluation and explicit coverage limitations.
- Relevance: precedent for separating scenarios, adapters, metrics, and reports.
- Limitation: foundation-model evaluation framework, not an editorial ontology.

### EVAL-02 — OpenAI Evals registry

- Source: [official repository](https://github.com/openai/evals)
- Supports: sample inputs/ideal outputs and multiple grader styles.
- Relevance: simple prior for eval-instance and grader separation.
- Limitation: registry formats do not establish validity for editorial judgment.

### EVAL-03 — Inspect AI

- Source: [UK AI Security Institute repository](https://github.com/UKGovernmentBEIS/inspect_ai)
- Supports: task, solver, scorer composition; tool use; model-graded and multi-turn evaluations; reproducible logs.
- Relevance: current open evaluation harness prior.
- Limitation: a harness architecture does not determine J-Editorial semantics or suitable metrics.

### EVAL-04 — NIST AI Metrology and Evaluation

- Source: [NIST AI Metrology and Evaluation program](https://airc.nist.gov/metrology/)
- Supports: context-specific test/evaluation methods and metric selection.
- Relevance: reinforces that measures require a defined use context.
- Limitation: does not prescribe one editorial metric set.

### EVAL-05 — MT-Bench / Chatbot Arena judge study

- Source: [Zheng et al., 2023](https://arxiv.org/abs/2306.05685)
- Supports: reported human agreement and documented position, verbosity, self-enhancement, and reasoning limitations in LLM judges.
- Relevance: model graders require calibration and bias testing.
- Limitation: conversational preference setting; results do not transfer automatically to editorial obligations.

### EVAL-06 — JudgeBench

- Source: [Tan et al., 2024, preprint](https://arxiv.org/abs/2410.12784)
- Supports: direct meta-evaluation of LLM judges on objectively labeled hard pairs.
- Relevance: graders must themselves be benchmarked.
- Limitation: knowledge/reasoning/math/coding response pairs, not editorial workflows.

### EVAL-07 — RubricEval

- Source: [Pan et al., 2026, preprint](https://arxiv.org/abs/2603.25133)
- Supports: reported rubric-level judge failure and value of fine-grained meta-evaluation.
- Relevance: aggregate judge scores can conceal obligation-level failures.
- Limitation: recent preprint; findings require independent replication and domain-specific testing.

### EVAL-08 — MCJudgeBench

- Source: [Lee et al., 2026, preprint](https://arxiv.org/abs/2605.03858)
- Supports: constraint-level labels and separate correctness/inconsistency analysis.
- Relevance: close methodological analogue to goal-contract obligations.
- Limitation: recent preprint; instruction-following constraints are not identical to editorial obligations.

## Security, privacy, erasure, and integrity

### SEC-01 — NIST Generative AI Profile

- Source: [NIST AI 600-1](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- Supports: lifecycle governance, content provenance, pre-deployment testing, and incident handling as generative-AI risk concerns.
- Relevance: agent/model integration cannot be treated as a grader-only concern.
- Limitation: voluntary cross-sector guidance, not a product-specific control set.

### SEC-02 — NIST Secure Software Development Framework

- Source: [NIST SSDF project](https://csrc.nist.gov/projects/ssdf)
- Supports: protecting software/components, tracking requirements/risks/design decisions, provenance, secure environments, and vulnerability response.
- Relevance: bootstrap research and future implementation need security gates.
- Limitation: outcome framework requiring product-specific tailoring.

### SEC-03 — OWASP prompt-injection guidance

- Source: [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)
- Supports: external/editorial content can contain direct, indirect, persistent, encoded, Markdown/HTML, or RAG-poisoning instructions; recommends separation, validation, monitoring, and human controls.
- Relevance: documents, citations, priors, and imported histories are untrusted input.
- Limitation: practical guidance, not proof that prompt injection can be eliminated.

### SEC-04 — OWASP excessive agency

- Source: [OWASP LLM08](https://genai.owasp.org/llmrisk2023-24/llm08-excessive-agency/)
- Supports: least functionality, least privilege, and human approval for consequential actions.
- Relevance: editorial agents must not infer permission to publish, delete, disclose, or mutate history.
- Limitation: general threat category; controls must map to J-Editorial operations.

### SEC-05 — GDPR Article 17

- Source: [official EUR-Lex consolidated regulation text](https://eur-lex.europa.eu/eli/reg/2016/679/2016-05-04)
- Supports: circumstances in which personal data erasure is a right and controller obligation, subject to enumerated exceptions.
- Relevance: immutable history cannot be designed as “payloads are never deletable.”
- Limitation: legal applicability is contextual; this review makes no legal determination.

### SEC-06 — SPDX 3.0.1

- Source: [SPDX Specification 3.0.1](https://spdx.github.io/spdx-spec/)
- Supports: versioned provenance, licensing/composition metadata, external references, and integrity methods.
- Relevance: useful prior for machine-readable rights and source metadata.
- Limitation: software/supply-chain scope; editorial rights require their own profile and legal review.

## First-slice domain evidence

### VERT-01 — OpenAPI Specification 3.2.0

- Source: [official specification, 2025-09-19](https://spec.openapis.org/oas/latest.html)
- Supports: machine-readable HTTP API capabilities, operations, parameters, request/response models, examples, extensions, and explicit normative requirements.
- Relevance: creates objective obligations against which reference documentation can be evaluated.
- Limitation: API descriptions may themselves be incomplete or wrong; user comprehension is not reducible to conformance.

### VERT-02 — Vale

- Source: [official Vale site](https://vale.sh/)
- Supports: markup-aware, configurable prose rules and local linting across documentation formats.
- Relevance: executable normative-prior adapter for terminology/style findings.
- Limitation: rule hits are not equivalent to correctness, usefulness, or release readiness.

### VERT-03 — Redocly CLI lint

- Source: [official command documentation](https://redocly.com/docs/cli/commands/lint)
- Supports: configurable validation and lint rules over API descriptions.
- Relevance: existing deterministic checks can become evidence inputs rather than being reimplemented.
- Limitation: vendor rulesets contain opinions and must be scoped/versioned; passing lint does not prove documentation quality.

### VERT-04 — Diátaxis

- Source: [official framework map](https://diataxis.fr/map/)
- Supports: distinct tutorial, how-to, reference, and explanation purposes.
- Relevance: evidence that a goal contract must identify document purpose rather than use one quality rubric.
- Limitation: design framework, not a formal specification or empirical scoring system.
