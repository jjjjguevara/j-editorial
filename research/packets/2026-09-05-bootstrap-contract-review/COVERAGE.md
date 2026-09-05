# Contract coverage and ADR routing

Target: `BOOTSTRAP.md` at `360d6ed15fbee7d38dc659f8324763bf637b3924`. This is an audit map, not a task tracker or evidence of experimental coverage. Verdicts below are dispositions of the questions in this static review; none closes the named Beads gate. All training questions remain DEFER. Gate aliases resolve through the unchanged Beads program registry in `RESEARCH.md` section 17.

## All 47 section 25 questions

### Representation

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q01 | Is a structured internal model actually necessary? | NARROW | AR-02/05/08: Not established. Compare a minimal source/checkpoint-plus-annotations control before selecting a structured model. | REP-G1 |
| Q02 | Can stable semantic identity be layered over source text? | RETURN-WITH-FINDINGS | AR-05: Plausible, not proven. Duplicate text, split/copy/rewrite, and stale selectors need independent evidence. | REP-G1, FD-G2 |
| Q03 | What information would be lost by treating Markdown as canonical? | RETURN-WITH-FINDINGS | AR-05: Source fidelity and semantic annotations are separate; declare unsupported syntax and information-loss boundaries. | REP-G1 |
| Q04 | What complexity is introduced by structured round-tripping? | RETURN-WITH-FINDINGS | AR-05/08: Measure reconciliation, migration, opaque syntax, and exact-versus-semantic round-trip cost. | REP-G1, HIST-G1 |
| Q05 | Which semantic entities truly require durable IDs? | RETURN-WITH-FINDINGS | AR-02/05: Require durable identity only where independently exercised history/authority/references need it; no universal node IDs accepted. | FD-G2 |

### Gap model

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q06 | Are gaps the correct central intermediate representation? | NARROW | AR-02: A gap is a derived context-scoped view, not the ontology root; test a plural logical model. | FD-G1, FD-G2 |
| Q07 | Are obligations, findings, claims, review comments, and risks materially different entities? | RETURN-WITH-FINDINGS | AR-02: They differ logically; separate physical objects/services are not entailed. Test independently encoded cases. | FD-G1, FD-G2 |
| Q08 | Can overlapping and nested gaps be represented without combinatorial complexity? | RETURN-WITH-FINDINGS | AR-02/10: Deduplicate underlying conditions and preserve overlapping classifications; scalability is unmeasured. | FD-G1, EV-G1 |
| Q09 | Can the ontology span technical docs, journalism, research, and general writing without becoming meaningless? | NARROW | AR-02/11: The paired proof cannot establish those domains. Scope an extension claim to observed material. | FD-G1, PS-G2 |
| Q10 | Which gap classes are objective enough for deterministic detection? | RETURN-WITH-FINDINGS | AR-09/10: Only explicitly specified/executable properties with valid oracles; do not relabel source-reading as deterministic. | AMN-G1, EV-G1 |

### Priors

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q11 | Which priors are hard requirements, normative conventions, descriptive observations, or heuristics? | RETURN-WITH-FINDINGS | AR-04: Classify each prior by source, authority, applicability, and whether compliance is mandatory or preferential. | GP-G1 |
| Q12 | How are conflicts and exceptions represented? | RETURN-WITH-FINDINGS | AR-03/04: Record conflicting norms and authorized, scoped, expiring exceptions; conflict is not permission to choose a pass. | GP-G1 |
| Q13 | How does scope inheritance work? | RETURN-WITH-FINDINGS | AR-04: Inheritance needs explicit precedence and applicability decisions; no implied audience/jurisdiction extension. | GP-G1 |
| Q14 | Can generic style priors override domain language accidentally? | RETURN-WITH-FINDINGS | AR-04: Yes as a design failure: a generic rule can erase domain terms. Domain-specific exceptions and tests are required. | GP-G1 |
| Q15 | What guide-derived material can legally be stored and redistributed? | DEFER | AR-04/13: No blanket legal answer or rights determination here. Retain only permitted material; source-specific review must precede redistribution. | GP-G1, SEC-G1 |

### Evidence

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q16 | What makes a source authoritative for a particular claim? | RETURN-WITH-FINDINGS | AR-07: Authority is claim-, scope-, and time-specific; provenance alone does not establish support or truth. | GP-G1 |
| Q17 | How are contradictory sources represented? | RETURN-WITH-FINDINGS | AR-04/07: Keep support, contradiction, source dependence, and unresolved adjudication separately observable. | GP-G1 |
| Q18 | How is source freshness tracked? | RETURN-WITH-FINDINGS | AR-07: Bind source revision, observed/valid time, and revisit/invalidation policy; artifact bytes alone are insufficient. | GP-G1, ES-G1 |
| Q19 | When is a citation insufficient even if syntactically present? | NARROW | AR-04/07: Presence/valid URL is not entailment, relevance, authority, or independence. The oracle must test the intended property. | GP-G1, EV-G1 |
| Q20 | How is unresolved uncertainty preserved? | RETURN-WITH-FINDINGS | AR-03/07/10: Preserve unknown, disagreement, abstention, and missing evidence explicitly; never coerce them to pass/false. | GP-G1, EV-G1 |

### History

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q21 | What is the minimum useful historical unit? | NARROW | AR-01/06: D-04 B for now: meaningful semantic operations plus checkpoints; minimum operational granularity remains testable. | ES-G1, HIST-G1 |
| Q22 | What must be exactly reconstructable? | RETURN-WITH-FINDINGS | AR-05/07/13: Declare exact source versus semantic/projection scope; authorized byte availability and erasure can limit replay. | HIST-G1, SEC-G1 |
| Q23 | Which high-frequency operations deserve durable storage? | NARROW | AR-06/08: Keystrokes are optional, not a default storage commitment. Measure decision/provenance value versus cost. | HIST-G1 |
| Q24 | What happens when a semantic node is split, merged, or moved? | RETURN-WITH-FINDINGS | AR-05/06: Preserve correspondence/lineage evidence; split/copy/merge must not inherit identity or approval solely by matching text. | REP-G1, ES-G1 |
| Q25 | How are reverted, cherry-picked, and concurrently authored changes represented? | RETURN-WITH-FINDINGS | AR-06: Record causal parents and conflict outcomes; re-evaluate current goals/evidence/authority rather than reverse approval blindly. | ES-G1, HIST-G1 |

### Storage

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q26 | Does Dolt materially outperform PostgreSQL plus temporal/event tables for the actual workload? | DEFER | AR-08: No actual workload bake-off establishes superiority; compare simple and credible alternatives before deciding. | HIST-G1 |
| Q27 | Is branching semantic state a core product requirement or an attractive but unnecessary feature? | RETURN-WITH-FINDINGS | AR-08: Unproven requirement; scenario and cost evidence must distinguish proposal history from database branching. | HIST-G1 |
| Q28 | Is a CRDT a core requirement or an authoring-client concern? | NARROW | AR-08: No accepted core CRDT requirement. Determine collaboration boundary from use-case evidence. | HIST-G1 |
| Q29 | What operational complexity does each backend introduce? | DEFER | AR-08: Needs measured deployment, recovery, maintenance, migration, and resource budgets; no numbers invented. | HIST-G1 |
| Q30 | What is the credible migration path if a storage choice is wrong? | RETURN-WITH-FINDINGS | AR-05/08/13: Require portable export, stable references, restore/corruption tests, and explicit fidelity/erasure limits. | HIST-G1, REP-G1 |

### Evals

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q31 | Which capabilities have defensible ground truth? | RETURN-WITH-FINDINGS | AR-09/10: Bounded executable properties can have defensible oracles; seeded changes and historical acceptance alone cannot. | EV-G1, AMN-G1 |
| Q32 | Which are preference judgments? | NARROW | AR-10/11: Clarity, style, and audience preference require construct definitions, independent judgment, and disagreement accounting. | EV-G1, PR-G2 |
| Q33 | What benchmark tasks can be gamed through artifacts or shortcuts? | RETURN-WITH-FINDINGS | AR-09/11: Generator signatures, exact-patch matching, author-chosen examples, metadata labels, and no-op exclusions permit shortcuts. | EV-G1, PS-G1 |
| Q34 | Which metrics are vulnerable to Goodharting? | RETURN-WITH-FINDINGS | AR-03/04/10: Raw gap counts, coverage via scope changes, conditional closure, scalar quality, and unweighted release accuracy are vulnerable. | EV-G1, GP-G1 |
| Q35 | What sample size is needed for useful decisions? | DEFER | AR-10: No defensible universal sample size. Predeclare decision-relevant difference, clustering, variability, and stopping/power protocol. | EV-G1 |
| Q36 | What are the expensive/rare failure modes that must be oversampled? | RETURN-WITH-FINDINGS | AR-03/06/12: False release, wrong-target edit, unauthorized action, data disclosure, and irreversible loss warrant explicit stress slices. | EV-G1, SEC-G1 |
| Q37 | How should infrastructure failures be separated from model failures? | RETURN-WITH-FINDINGS | AR-06/10: Record environment/tool errors, failed attempts, retries, and model choices distinctly; retain them in run accounting. | EV-G1 |
| Q38 | How do we know an eval predicts production usefulness? | RETURN-WITH-FINDINGS | AR-11: Compare independent reader/developer task outcomes with no-edit/simple-checklist controls, not author-patch agreement alone. | AMN-G2, PR-G2, EV-G1 |

### Training

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q39 | When is an accepted historical edit actually a useful target? | DEFER | AR-09: Held training research; acceptance alone is insufficient, but eligibility policy is not executed or selected here. | DG-G0 |
| Q40 | How do we use rejected, reverted, and superseded edits? | DEFER | AR-09: Held training research; no labels, sampling recipe, or training target is approved by this review. | DG-G0 |
| Q41 | How do we prevent neighboring snapshot leakage? | DEFER | AR-10: Lineage isolation remains invariant; dataset split architecture and implementation await the separate session. | DG-G0 |
| Q42 | How do we prevent synthetic perturbation generators from creating trivial signatures? | DEFER | AR-09: Eval shortcut risk is recorded, but held training-generator/corpus research is not executed. | DG-G0 |
| Q43 | How are benchmarks refreshed after their examples become training data? | DEFER | AR-09/10: Benchmark refresh is required conceptually; training-contamination/retirement policy needs the held program and EV-G1. | DG-G0, EV-G1 |

### Product boundary

| ID | Contract question (verbatim) | Disposition | Finding and answer | Existing gate |
|---|---|---|---|---|
| Q44 | Which capabilities belong in `j-editorial` versus a downstream writing product? | RETURN-WITH-FINDINGS | AR-08/11: Core owns editorial semantics; client UI/auth/storage adapters remain downstream unless evidence justifies a shared boundary. | PS-G2, DD-G1 |
| Q45 | Which belong in the editorial framework versus the eval subsystem? | NARROW | AR-11: Evaluation consumes the provider-independent editorial core; no core dependency on harnesses or model providers. | PS-G2, EV-G1 |
| Q46 | Which should eventually be separate packages or repositories? | DEFER | AR-08/11: No package/repository decomposition is accepted before capability and dependency evidence. | DD-G1 |
| Q47 | Can the editorial core remain useful with no model provider configured? | NARROW | AR-11: It must remain useful without ML; the minimal-control and consumer proofs still need execution. | PS-G2, DD-G1 |

## All 52 section 24 decision-queue items

Actions below reorganize the proposed decision queue; they are not gate verdicts, accepted ADRs, new Beads tasks, or instructions to execute held research. MERGE means combine decision questions, not merge code. CONDITIONAL and HELD preserve explicit prerequisites. No ADR files are created.

| # | Original queue item (verbatim) | Proposed action | Program / gate | Rationale or prerequisite |
|---|---|---|---|---|
| 1 | Canonical editorial-state boundary. | MERGE | frame-domain; paired-synthesis: FD-G2, PS-G2 | Group 1–2 with the minimal vocabulary/core boundary; do not select physical storage. |
| 2 | Artifact versus document versus publication semantics. | MERGE | frame-domain; paired-synthesis: FD-G2, PS-G2 | Keep artifact/state/release distinctions inside the same glossary boundary as 1. |
| 3 | Structured document representation versus canonical source text. | RETAIN | representation: REP-G1 | Source-plus-annotations is the control; no canonical representation selected. |
| 4 | Stable semantic identity and anchor guarantees. | RETAIN | representation; frame-domain: REP-G1, FD-G2 | Bind revision, selector, correspondence, and failure guarantees. |
| 5 | Claim model and claim granularity. | RETAIN | frame-domain: FD-G2 | Justify claim granularity through independently encoded material. |
| 6 | Gap versus finding versus obligation versus violation semantics. | REVISE | frame-domain: FD-G1, FD-G2 | Logical plural distinctions; gaps are derived, not compulsory root objects. |
| 7 | Goal-contract schema, inheritance, and lifecycle. | RETAIN | goal-priors: GP-G1 | Define scope, provenance, approval, applicability, and version-change semantics. |
| 8 | Quality-vector semantics and whether any scalar is allowed. | REVISE | evaluation; frame-domain: EV-G1, FD-G2 | Heterogeneous observations; delete any presupposition of canonical vector arithmetic. |
| 9 | Release-readiness and lifecycle-state model. | SPLIT | goal-priors; security; paired-synthesis: GP-G1, SEC-G1, PS-G1 | Separate evaluated readiness, authorized release, and publication side effects. |
| 10 | Editorial-gap ontology architecture. | MERGE | frame-domain: FD-G1, FD-G2 | Group 10–11; ontology extension must preserve scope and avoid double counting. |
| 11 | Ontology extensibility across editorial verticals. | MERGE | frame-domain: FD-G1, FD-G2 | Extension evidence cannot come solely from the paired examples. |
| 12 | Normative-prior registry. | MERGE | goal-priors: GP-G1 | Group 12–13; a registry without applicability/precedence is insufficient. |
| 13 | Prior applicability, precedence, exception, and conflict rules. | MERGE | goal-priors: GP-G1 | Preserve conflict, waiver, inapplicability, and inheritance semantics. |
| 14 | Style-guide licensing and derived-rule policy. | RETAIN | goal-priors; security: GP-G1, SEC-G1 | Rights are source-specific; redistribution is not authorized. |
| 15 | Evidence/source model. | MERGE | goal-priors; frame-domain: GP-G1, FD-G2 | Group 15–16; provenance/authority/entailment/contradiction remain distinct. |
| 16 | Claim/evidence relation model. | MERGE | goal-priors; frame-domain: GP-G1, FD-G2 | Claim/evidence relation requires scope/time and unresolved uncertainty. |
| 17 | Provenance and actor identity model. | SPLIT | frame-domain; security: FD-G2, SEC-G1 | Descriptive attribution is not authorization to act. |
| 18 | Fine-grained operation model. | MERGE | event-state: ES-G1, ES-G2 | Group 18–19; command, attempt, transaction, and observed outcome differ. |
| 19 | Semantic-event model. | MERGE | event-state: ES-G1, ES-G2 | Use a discriminating workload, not four re-encodings of one fixture. |
| 20 | Snapshot/checkpoint semantics. | MERGE | history; representation: HIST-G1, REP-G1 | Group 20–21; bytes, semantics, projections, and availability are separate guarantees. |
| 21 | Exact versus semantic historical reconstruction guarantees. | MERGE | history; security: HIST-G1, SEC-G1 | Exact replay is bounded by retained authorized inputs and erasure policy. |
| 22 | Concurrency/collaboration requirements. | RETAIN | history: HIST-G1 | Establish actual simultaneous-author requirements first. |
| 23 | CRDT requirement and boundary, if any. | CONDITIONAL | history: HIST-G1 | Only after 22 establishes a requirement; CRDT may remain client-side or unnecessary. |
| 24 | Git interoperability/publication boundary. | RETAIN | history; doc-doctor-integration: HIST-G1, DD-G1 | Git interoperability/publication does not imply canonical Git state. |
| 25 | Dolt versus PostgreSQL/event-store versus other semantic-history backends. | RETAIN | history: HIST-G1 | Actual bounded bake-off after workloads/budgets; no winner selected. |
| 26 | DeltaDB/Delta-like operation-layer applicability. | CONDITIONAL | history: HIST-G1 | Candidate capability/access evidence required; no new dependency or current-access claim. |
| 27 | Object-storage boundary. | CONDITIONAL | history: HIST-G1 | Use only if measured payload/recovery needs warrant it; dataset storage still held. |
| 28 | Analytical-storage/telemetry boundary. | SPLIT | evaluation; history; model-training-data: EV-G1, HIST-G1, DG-G0 | Separate evaluation result retention from held training-data analytical architecture. |
| 29 | Backup, restore, export, and migration guarantees. | RETAIN | history; security: HIST-G1, SEC-G1 | Require restore/migration/corruption evidence and all-copy erasure limits. |
| 30 | Eval-instance contract. | RETAIN | evaluation: EV-G1 | Task, budgets, oracle, allowed tools, and failure accounting must be explicit. |
| 31 | Benchmark-suite manifest and version model. | MERGE | evaluation: EV-G1 | Group 31 with score-affecting version manifest 52. |
| 32 | Grader taxonomy and selection policy. | MERGE | evaluation: EV-G1 | Group 32–33; direct measurements preferred where valid, model judges need calibration. |
| 33 | Model-judge meta-evaluation policy. | MERGE | evaluation: EV-G1 | Meta-evaluate graders independently; agreement is not truth. |
| 34 | Per-instance result/provenance contract. | RETAIN | evaluation: EV-G1 | Keep instance-level raw results and full input closure. |
| 35 | Metric suite and statistical policy. | RETAIN | evaluation: EV-G1 | Units, denominators, abstentions, dependence, uncertainty, and stopping rules. |
| 36 | Historical-transition dataset contract. | SPLIT | evaluation; model-training-data: EV-G1, DG-G0 | Bounded evaluation episodes versus held training-target/corpus contracts. |
| 37 | Synthetic-gap generation and validation policy. | SPLIT | evaluation; model-training-data: EV-G1, DG-G0 | Verify bounded eval interventions; training generators/corpora remain held. |
| 38 | Train/dev/test lineage and temporal split policy. | HELD | model-training-data: DG-G0 | Lineage isolation invariant retained; no dataset split design executed. |
| 39 | Contamination detection and benchmark retirement policy. | SPLIT | evaluation; model-training-data: EV-G1, DG-G0 | Benchmark disclosure/retirement boundary recorded; training contamination research held. |
| 40 | Benchmark refresh/saturation policy. | RETAIN | evaluation: EV-G1 | Refresh claims require leakage/saturation monitoring and versioned retirement policy. |
| 41 | Agent capability decomposition. | RETAIN | evaluation; paired-synthesis: EV-G1, PS-G2 | Capabilities tested separately; no specialist agent implementation released. |
| 42 | Typed specialist-agent operations. | SPLIT | event-state; security: ES-G1, SEC-G1 | Typed tool syntax cannot substitute for state-bound authorization. |
| 43 | Abstention and confidence-calibration policy. | RETAIN | evaluation: EV-G1 | Report selective coverage and calibration; represent abstention as an outcome. |
| 44 | End-to-end lifecycle benchmark contract. | RETAIN | paired-synthesis; evaluation: PS-G2, EV-G1 | End-to-end outcomes need independent reader/developer evidence. |
| 45 | Sensitive-data classification and retention. | MERGE | security: SEC-G1 | Group 45–46 with copy inventory, rights, and replay trade-offs. |
| 46 | Deletion/right-to-erasure semantics. | MERGE | security; history: SEC-G1, HIST-G1 | Erasure is not current-row deletion; retain bounded receipts only as authorized. |
| 47 | Copyright/licensing governance. | RETAIN | security; goal-priors: SEC-G1, GP-G1 | Rights decisions precede storage/publication; no blanket compliance conclusion. |
| 48 | Executable-grader sandbox boundary. | MERGE | security; evaluation: SEC-G1, EV-G1 | Group 48–49 without conflating code execution and untrusted model input. |
| 49 | Hostile-content/prompt-injection boundary. | MERGE | security: SEC-G1 | Real boundary tests needed; string inertness alone is not agent security. |
| 50 | Import/export round-trip guarantees. | MERGE | representation; history: REP-G1, HIST-G1 | Group with 3–4 and 20–21 fidelity/identity guarantees. |
| 51 | Public API/domain boundary. | RETAIN | doc-doctor-integration; paired-synthesis: DD-G1, PS-G2 | Consumer mapping follows core proof; no API/package file creation yet. |
| 52 | Versioning policy for score-affecting components. | MERGE | evaluation; event-state: EV-G1, ES-G1 | Group with 31/34; immutable inputs include source, goal, norms, reducer, tools, environment. |

## Cross-cutting obligations not explicit in the question list

Section 18 operations/abstention is covered by AR-06/10/11; section 22 security/privacy by AR-12/13; sections 26–28 review authority, verdicts, and implementation holds by AR-01/14. The [existing paired-proof matrix](../../programs/paired-synthesis/COVERAGE.md) remains authoritative for **experimental** coverage. This question audit does not upgrade any of its `none`, `trivial`, or declarative entries.

## Existing gate identities used by this audit

All listed gates were open in the verified native snapshot. This compact alias map is a historical audit reference, not a live registry; Beads and the generated registry remain authoritative.

| Program | Gate → native ID |
|---|---|
| frame-domain | FD-G1 → j-editorial-4lk.1; FD-G2 → j-editorial-4lk.2 |
| event-state | ES-G1 → j-editorial-t2j.1; ES-G2 → j-editorial-t2j.2 |
| amnesia | AMN-G1 → j-editorial-47m.1; AMN-G2 → j-editorial-47m.2 |
| prose | PR-G1 → j-editorial-cz0.1; PR-G2 → j-editorial-cz0.2 |
| paired-synthesis | PS-G1 → j-editorial-c8r.1; PS-G2 → j-editorial-c8r.2 |
| goal-priors | GP-G1 → j-editorial-wd2.1 |
| representation | REP-G1 → j-editorial-0te.1 |
| history | HIST-G1 → j-editorial-dta.1 |
| evaluation | EV-G1 → j-editorial-k4f.1 |
| security | SEC-G1 → j-editorial-8dd.1 |
| doc-doctor-integration | DD-G1 → j-editorial-vht.1 |
| model-training-data | DG-G0 → j-editorial-o3k.1 |
