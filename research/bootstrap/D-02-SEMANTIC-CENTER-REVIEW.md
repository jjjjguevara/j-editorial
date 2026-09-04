# D-02 semantic-center review — from a single root to an editorial construction space

Status: **research synthesis / pivotal-decision hold / not an ontology**  
Research cutoff: **2026-09-04**  
Implementation: **blocked**  
Dataset research: **not executed**

Source identifiers resolve in [`PHASE-2-SOURCE-LEDGER.md`](PHASE-2-SOURCE-LEDGER.md).

## 1. Executive result

The original D-02 choice—`Gap`-centered, `Obligation/Finding`-centered, or event-centered—is too early because it asks one primitive to do two jobs:

1. organize analysis of the editorial field; and
2. serve as the canonical persisted domain primitive.

Those jobs should be separated.

The strongest current research hypothesis is:

```text
Editorial Construction Space
  = a three-axis analytic scaffold

Typed Editorial Record Family
  = plural domain records with shared identity, provenance,
    targeting, version, authority, and state semantics

Editorial Episode
  = a cross-axis analysis/replay envelope, not necessarily
    the sole stored root and not assumed to imply event sourcing
```

Under this hypothesis:

- `Obligation` expresses what ought to hold under a goal or norm;
- `Assertion` or `Finding` expresses what an actor or process claims or observes;
- `Evidence` records what supports, weakens, or contradicts an assertion;
- `Operation` records an attempted editorial transformation or adjudicative act;
- `Outcome` records what happened and what was verified;
- `Gap` is an adverse, unresolved condition derived from an unsatisfied obligation or unresolved adverse finding;
- `Event` carries history but does not monopolize semantics.

This is a favored **research hypothesis**, not an accepted ontology or schema.

## 2. Why the original question fails

A single-root choice produces category errors in ordinary editorial cases:

| Case | Why one root is insufficient |
|---|---|
| A reference page exactly matches its API | Positive evidence is not naturally a gap. |
| A release waives a low-risk style issue | A waiver is a decision under authority, not the disappearance of an observation. |
| Two qualified reviewers disagree | The disagreement must remain representable without declaring either finding canonical. |
| The product changes but the document does not | Staleness can arise from a changed referent, not an edit event in the artifact. |
| An agent proposes a valid edit that is rejected for scope | Operation quality, acceptance, and artifact outcome are distinct. |
| A rule changes after publication | The artifact may acquire a new obligation without its historical release becoming fictitious. |
| A paragraph becomes rhetorically stronger without changing its factual claims | Transformation and improvement cannot be reduced to constraint satisfaction alone. |
| A target is deleted for privacy reasons | Audit identity, payload retention, selector resolution, and erasure status diverge. |

`Gap`, `Finding`, `Obligation`, and `Event` are therefore better treated as distinct types or views until experiments prove a safe reduction.

## 3. Gustavo Bueno's gnoseological space

### 3.1 What transfers

Bueno's Theory of Categorical Closure analyzes positive sciences as heterogeneous bodies rather than as sets of propositions alone. Its gnoseological space has three axes and nine figure families: [GB-01]

| Axis | Figures |
|---|---|
| Syntactic | terms, relations, operations |
| Semantic | referentials, phenomena, essences |
| Pragmatic | autologisms, dialogisms, norms |

The central transferable move is not the vocabulary by itself. It is the refusal to isolate semantics from material operations, referents, operator subjects, dialogue, and norms. Bueno also treats scientific facts as cross-axis constructions rather than free-standing observations. [GB-03, GB-04]

### 3.2 What does not transfer directly

The theory is explicitly a philosophical theory of positive sciences. An editorial workflow is not thereby a science, and an edited document does not acquire a categorical closure simply because it passes a release gate. The following mappings are forbidden unless later research establishes them:

- categorical closure = publication;
- synthetic identity = editorial correctness;
- essence = approved house style;
- operator elimination = removal of human provenance;
- repeatability = universal writing quality;
- scientific truth = benchmark score.

Applications of the general theory to particular scientific fields are expected to test and refine the general frame. J-Editorial can borrow that falsifiable posture: its paired technical and prose slices must challenge the general editorial frame rather than merely instantiate it. [GB-02, GB-05]

## 4. Candidate Editorial Construction Space

The following translation is deliberately operational and defeasible.

### 4.1 Constructive axis

| Candidate figure | Editorial interpretation | Examples |
|---|---|---|
| **Units** | Addressable artifact or contract constituents | artifact state, section, paragraph, claim, example, citation, table, API member, goal clause |
| **Relations** | Typed connections among units and contextual records | supports, contradicts, cites, duplicates, specializes, targets, supersedes, requires, resolves |
| **Operations** | Actions that attempt to transform or adjudicate state | add, delete, rewrite, move, split, merge, cite, qualify, verify, waive, approve, publish, reopen |

This axis prevents the framework from treating text as propositions alone. A test runner, parser, renderer, source synchronizer, reviewer, and agent can all participate in editorial operations, but their authority and outputs differ.

### 4.2 Referential axis

| Candidate figure | Editorial interpretation | Examples |
|---|---|---|
| **Referents / evidence objects** | Things against which claims or obligations can be tested | source code, running API, law, dataset, event, source document, audience task, product behavior |
| **Presentations / phenomena** | Situated observations or representations of referents | source snapshot, rendering, test output, user report, reviewer view, model output, screenshot |
| **Stabilized structures** | Repeatedly supported, versioned models or constraints | API contract, terminology model, invariant, accepted mapping, domain rule, validated pattern |

“Stabilized structure” replaces a direct import of *essence*. It must remain versioned, defeasible, and scoped. The distinction between a referent and one presentation of it is essential: a page render, parsed AST, and source bytes may disagree without any one being the whole artifact.

### 4.3 Pragmatic and governance axis

| Candidate figure | Editorial interpretation | Examples |
|---|---|---|
| **Actor continuity** | Identity, rationale, commitments, memory, and authority of a participant | author, reviewer, editor, agent, tool, organization, delegated role |
| **Dialogue and adjudication** | Structured disagreement, response, negotiation, and decision | review thread, objection, rebuttal, dissent, arbitration, accepted exception |
| **Norms** | Conditions governing what ought to be done or accepted | goal contract, style rule, release policy, permission, legal constraint, prior bundle |

This axis prevents “human approved” from becoming an unexplained truth flag. Acceptance must identify who had authority, under which norm, with what evidence, and whether dissent or uncertainty survived.

## 5. Editorial Episode as a unit of analysis

An **Editorial Episode** is a bounded envelope joining the three axes:

```text
actors operating under norms
  perform or assess operations on artifact units
  with respect to referents and evidence presentations
  producing assertions/findings, decisions, outcomes,
  and possibly a new materialized artifact state
```

Candidate episode contents:

- episode identity and time bounds;
- purpose/goal-contract version;
- participating agents and authority;
- pre-state and targeted units;
- applicable norms and obligations;
- evidence/referents and observation method;
- proposed/performed operations;
- assertions, findings, objections, and confidence;
- acceptance, rejection, waiver, or abstention decision;
- verification results;
- post-state/checkpoint and opened/closed/reopened gaps;
- links to predecessor, branch, merge, supersession, and erasure events.

The episode is useful for evaluation, replay, and causal inquiry. It should initially be a query and interchange envelope. Declaring it the only stored root would prematurely assume event sourcing and projection semantics.

## 6. Comparative models

No reviewed model covers the whole editorial problem. Each supplies a burden of proof.

| Model | What it contributes | What it does not settle for J-Editorial |
|---|---|---|
| **W3C PROV-DM / PROV-O** [STD-01] | Domain-neutral Entity–Activity–Agent provenance, usage, generation, derivation, revision, attribution, and responsibility. | Editorial obligations, target anchoring, disagreement, and release semantics. |
| **W3C Web Annotation** [STD-02] | Body–Target–Motivation, resource states, selectors, and multiple ways to identify a segment. | Artifact history, normative force, operation outcomes, and adjudication. |
| **W3C SHACL** [STD-03] | Separates constraints/shapes from immutable input graphs and typed validation results with focus node, path, severity, source shape, and source component. | Subjective adequacy, rhetoric, open-textured norms, and human authority. |
| **W3C ODRL** [STD-04] | Explicit policy, party, asset, action, permission, prohibition, duty, and constraint distinctions. | General editorial quality or evidence evaluation. |
| **TEI P5** [STD-05, STD-06] | Shows that textual, physical, rhetorical, and analytic hierarchies overlap; supports stand-off layers, certainty, precision, source, and responsibility. | A format-neutral editorial lifecycle or history model. |
| **IFLA LRM / LRMoo** [STD-07, STD-08] | Distinguishes intellectual work, expression, manifestation, and item/instantiation concerns and aligns bibliographic semantics with event-oriented cultural heritage models. | Fine-grained editorial operations, findings, and release gates. |
| **CIDOC CRM** [STD-09] | Event-centric integration of heterogeneous cultural-heritage facts and temporal entities. | A lightweight product model and editorial norm/evaluation semantics. |
| **ICA Records in Contexts** [STD-10, STD-11] | Connects record resources, instantiations, agents, and activities in a contextual graph rather than a single archival hierarchy. | Prospective editorial intent, quality, and agent evaluation. |
| **Nanopublications** [STD-12] | Separates an assertion, provenance of the assertion, and publication information; supports claims, hypotheses, negative results, and opinions. | Artifact transformations and multi-party review workflows. |
| **IBIS / AIF** [STD-13, STD-14] | Represents issues, positions, arguments, conflict, preference, inference, and dialogue histories. | Source fidelity, artifact state, and release outcomes. |
| **RO-Crate 1.3** [STD-15] | Packages data and contextual entities with identifiers, profiles, actions, instruments, inputs, results, and provenance. | An editorial semantic center or stable target identity. |

The comparison favors **typed pluralism**: reuse distinctions and patterns, but do not import any whole ontology as the J-Editorial core.

## 7. Candidate typed record family

The minimum family to test is:

| Record family | Core question |
|---|---|
| `Artifact` / `ArtifactState` / `Representation` | What editorial object and materialized state are under consideration? |
| `Purpose` / `GoalContract` | What is the artifact supposed to accomplish, for whom, and under which scope? |
| `Norm` / `Obligation` / `Constraint` | What ought, may, or must not hold, and under which applicability conditions? |
| `Assertion` / `Finding` | What is claimed or observed, by whom or what, with what polarity and confidence? |
| `Evidence` / `Referent` / `Observation` | What supports or challenges the assertion, and how was it observed? |
| `Target` / `Selector` / `Resolution` | What artifact region, contract clause, claim, or external referent is addressed, and did the target resolve? |
| `EditorialOperation` / `Activity` | What transformation or adjudicative act was proposed or performed? |
| `Agent` / `Role` / `Authority` | Who or what acted, and what were they permitted or competent to decide? |
| `Decision` / `Outcome` / `Verification` | What was accepted, rejected, waived, failed, or verified? |
| `Release` / `Checkpoint` | What state was accepted under which goal, norms, evidence, and unresolved conditions? |
| `EditorialEpisode` | Which records belong to one causally and normatively coherent unit of work? |

Common semantics should include stable identity, type/version, provenance, temporal bounds, scope, target resolution, confidence/uncertainty, authority, and supersession. Common fields do not require one universal base table or class.

## 8. Status of `Gap`

A candidate derived definition is:

```text
Gap := an unresolved adverse finding
       OR an obligation not currently satisfied
       under a specific goal/norm/evidence state
```

Consequences:

- a positive finding is not a gap;
- a waived issue remains observable but may cease to be release-blocking;
- a resolved gap can reopen when evidence, source, goal, or norm versions change;
- one finding may affect several obligations;
- one obligation may have several conflicting findings;
- “no finding” is not evidence of satisfaction;
- unknown/not-evaluated is distinct from pass.

`GapField` can remain a useful projection and prioritization view. It should not be the only canonical record family unless experiments prove that the distinctions above can be preserved without distortion.

## 9. Implications for D-03

The three gnoseological axes are not storage layers. However, this research strengthens a three-concern authority hypothesis:

```text
A. exact artifact/source-state authority
B. editorial-semantic record authority
C. derived projection/evaluation authority
```

Mappings among A, B, and C require versions, provenance, reconciliation status, and explicit ambiguity. This remains close to original option C, but representation research must determine whether the concerns share one store, several stores, or only logical boundaries.

## 10. Paired-proof falsification tests

The D-01C proof should reject this hypothesis if it cannot represent all of the following without type erasure or special pleading:

1. a deterministic API signature mismatch;
2. a correct API claim with positive executable evidence;
3. a prose claim needing qualified citation rather than binary validation;
4. a rhetorically weak but factually correct paragraph;
5. two acceptable prose rewrites with different trade-offs;
6. conflicting expert findings preserved without forced consensus;
7. an accepted waiver with residual risk;
8. an operation that fails before producing a new state;
9. a referent change that makes an unchanged artifact stale;
10. a rule change that opens a new obligation after release;
11. a target that moves or becomes ambiguous across revisions;
12. a redacted payload whose permissible audit identity survives;
13. a branch that accepts a different resolution under a different goal;
14. a derived score that changes while primary findings remain unchanged.

## 11. Revised pivotal decision

### D-02R — Which hypothesis should govern phase-2 domain research?

#### A — Editorial Construction Space + typed plural record family

Use the three-axis space as a falsifiable completeness scaffold; test the plural record family and Editorial Episode envelope across both proof slices. No class hierarchy, database schema, serialization, or event-sourcing architecture is accepted.

**Advantages:** preserves distinctions exposed by the research; creates concrete falsification tests; avoids selecting `Gap` or `Event` as a universal root.

**Risk:** a larger conceptual vocabulary can become overengineered unless the paired fixtures prove each distinction earns its cost.

#### B — Continue comparative research without a favored hypothesis

Keep all root and plural models equally open until a larger literature review is complete.

**Advantages:** minimizes premature commitment.

**Risk:** representation and eval research cannot define stable experimental objects, so bootstrap can expand indefinitely without a falsifiable candidate.

#### C — Owner-specified alternative frame

Replace or narrow the candidate using an explicitly stated alternative and its required proof obligations.

**Research recommendation:** **A**, strictly as a phase-2 research hypothesis.

## 12. Non-conclusions

This review does not:

- establish an ontology;
- require RDF, OWL, SHACL, XML, JSON-LD, or a graph database;
- declare J-Editorial a science;
- equate categorical closure with publication;
- choose event sourcing;
- select a canonical source representation;
- authorize schemas, APIs, adapters, graders, or implementation;
- activate model-training dataset research.
