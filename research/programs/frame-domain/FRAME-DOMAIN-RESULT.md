# Editorial Construction Space and domain distinctions — Phase 2 result

Status: **research result / candidate logical model / no production schema**  
Programs: `BR-FRAME`, `BR-DOM`  
Fixture: `fixtures/amnesia-notes-event-fluent.json`  
Dataset research: **not executed**

Source identifiers resolve in [`SOURCE-LEDGER.md`](../../packets/2026-09-04-phase-2-foundations/SOURCE-LEDGER.md).

## 1. Result

The D-02R hypothesis survives the first technical fixture, with one refinement:

> The typed record family should be treated as a vocabulary of irreducible semantic distinctions and roles, not as a requirement that every distinction become a separate stored object.

The Editorial Construction Space remains useful as a completeness test:

| Axis | Question applied to an editorial datum |
|---|---|
| Constructive | What unit, relation, or operation is involved? |
| Referential | What referent, evidence presentation, or stabilized structure is involved? |
| Pragmatic/governance | Which actor, dialogue, authority, norm, or decision is involved? |

The axes are non-exclusive. The Amnesia signature finding occupies all three at once:

- **constructive:** it relates a documentation target to a product symbol and results from a comparison operation;
- **referential:** it concerns pinned source representations and checker evidence;
- **pragmatic/governance:** it challenges a release/parity claim and requires an authorized disposition.

This preserves the central lesson drawn from Bueno's gnoseological space without treating editorial publication as categorical closure.

## 2. Candidate unit: an identity-bearing editorial datum

The smallest useful logical unit is not a scalar score or a vector coordinate. It is an identity-bearing, provenance-bearing datum that can participate in several relations.

A datum may be:

- an occurrence;
- an assertion or finding;
- an obligation;
- a relation between evidence and assertion;
- a decision;
- a time-scoped condition;
- an exact material checkpoint;
- a projection result.

The research fixture represents a finding once and attaches several roles and relations to it. It does not create separate copies named “epistemic finding,” “normative violation,” and “release blocker.” Separate state effects record how the same finding changes the current state.

## 3. Distinctions that survived reduction attempts

### 3.1 Artifact state and semantic state

An artifact checkpoint answers:

> Which exact material representation existed?

A semantic state answers:

> What currently holds, according to which events, rules, evidence, and reducer?

Semantic replay cannot substitute for exact bytes. A new renderer, parser, or normalization rule may produce a different representation even when given “equivalent” semantic content. `HIST-01`, `REP-07`, `REP-08`, and `REP-09` support preserving exact identities and operation provenance.

**Result:** retain the distinction.

### 3.2 Event and fluent

An event answers:

> What occurrence was recorded?

A fluent answers:

> What condition held over an interval?

“Checker executed” is an event. “Obligation remains unsatisfied” is a fluent. Re-emitting an “unsatisfied” pseudo-event for every query would obscure duration and would not explain what initiated or terminated the condition. `EVT-04`, `EVT-05`, and `EVT-10` support this separation.

**Result:** retain the distinction.

### 3.3 Observation and truth

A checker result, human review, or model judgment is an observation with method, actor, version, evidence, and uncertainty. The event that records it establishes that the observation occurred; it does not establish that the observation is correct.

**Result:** retain `Observation`, `Assertion/Finding`, and `Evidence` as distinguishable roles.

### 3.4 Obligation and finding

An obligation states what ought to hold under a goal or norm. A finding states what an evaluator observed. One finding may bear on several obligations, and several conflicting findings may bear on one obligation.

**Result:** retain both.

### 3.5 Proposal, operation, decision, and outcome

A proposed correction can be valid yet rejected for scope. An accepted operation can fail before producing a checkpoint. A completed operation can be followed by verification failure.

**Result:** do not collapse these into one `Edit` or one status flag.

### 3.6 Agent, role, and authority

An actor's identity does not imply authority. A checker may record observations but cannot accept a release. A maintainer may accept or waive but cannot convert unavailable evidence into observed evidence.

**Result:** retain role and authority separately from actor identity.

### 3.7 Release and quality

A release decision is made under a goal, evidence state, policy version, and authority. It is not a permanent statement of truth or a universal quality number.

**Result:** retain release as an authority-bearing decision/projection concern.

## 4. Reductions rejected by the fixture

| Reduction | Failure |
|---|---|
| Everything is a `Gap` | Cannot represent positive evidence, neutral observations, accepted waivers, or alternative valid resolutions without distortion. |
| Everything is an `Event` | Continuing conditions, applicability intervals, and current obligation state become awkward pseudo-events or expensive projections with hidden semantics. |
| Everything is a `Fact` | Causal intent, command rejection, atomic operation boundaries, and branch adjudication become indirect or disappear. |
| Everything is an `ArtifactState` | Review dialogue, rejected proposals, failed operations, authority, and external referent changes vanish. |
| Everything is one numeric vector | Dimensions have different types, authorities, temporal behavior, and admissible operations; there is no justified addition, magnitude, or distance. |
| One total timeline is the process | Independent reviews and alternative remedies become falsely ordered; causal conflict and merge are lost. |
| One source is universal ground truth | Types, runtime behavior, tests, docs, release policy, and human task success answer different obligations and may conflict. |

## 5. Candidate typed vocabulary

The minimum vocabulary retained for further experiments is:

| Family | Required distinction |
|---|---|
| `Artifact`, `ArtifactState`, `Representation`, `Checkpoint` | Editorial object, exact state, rendered/parsed representation, immutable material binding |
| `Purpose`, `GoalContract` | Intended audience, use, scope, non-goals, and acceptance target |
| `Norm`, `Obligation`, `Constraint`, `Waiver` | What must, should, may, or must not hold; applicability and exceptions |
| `Observation`, `Assertion`, `Finding` | What an actor/tool observed or claimed; polarity, confidence, method |
| `Evidence`, `Referent` | What supports, weakens, or contradicts an assertion and what external thing is being described |
| `Target`, `Selector`, `Resolution` | What unit or referent is addressed and whether the address resolves at a state |
| `Command`, `Proposal`, `EditorialOperation` | Requested, proposed, and performed transformations or adjudicative acts |
| `Agent`, `Role`, `Authority` | Who or what acted, in which capacity, and with which permissions |
| `Decision`, `Outcome`, `Verification` | Accepted/rejected/waived/abstained disposition, actual result, and subsequent check |
| `EventTransaction` | Atomic causal record grouping one or more occurrences and state effects |
| `Fluent` | Time-scoped condition initiated, terminated, asserted, or derived from history |
| `Release` | Accepted material state under a particular goal, policy, evidence state, and authority |
| `Projection` | Versioned derived view such as gaps, readiness, scores, reports, or indexes |
| `EditorialEpisode` | Causally and normatively coherent envelope spanning related transactions |

These are logical distinctions. They do not imply separate files, classes, tables, services, graph nodes, or stores.

## 6. Canonicality by claim type

The research supports claim-specific canonicality rather than one universal authority:

| Claim | Candidate authoritative record |
|---|---|
| Exact source bytes existed | Content-addressed checkpoint plus repository/object locator |
| An actor/tool performed or recorded an act | Immutable event transaction with actor, authority, time, and provenance |
| A condition held under a model | Fluent/fact record or deterministic derivation with reducer/model version |
| A source supports an assertion | Evidence relation with source state and observation method |
| A proposal was accepted or waived | Authority-bearing decision event |
| A gap/readiness/score was reported | Versioned projection output and inputs |
| The external world or product behaved a certain way | Pinned evidence and observation; never the event record alone |

## 7. Gap remains a projection

The working definition remains:

```text
Gap :=
  an unresolved adverse finding
  OR an applicable obligation not currently satisfied
  under a specific goal, norm, evidence, and state interpretation
```

A gap can reopen when:

- the artifact changes;
- the referent changes;
- a new observation arrives;
- a rule or goal changes;
- a waiver expires or is revoked;
- a target resolves differently;
- a reducer/projection version changes.

The underlying finding, evidence, obligation, and history should remain independently queryable.

## 8. Cross-slice falsification requirement

The technical fixture establishes only that the vocabulary can represent deterministic parity, branching remedies, late external change, and erasure. The general-prose companion must still test:

- rhetorical and structural problems with no unique answer;
- factual claims requiring qualified evidence;
- audience-fit judgments;
- multiple acceptable rewrites;
- reviewer disagreement that remains unresolved;
- style/norm conflicts and justified exceptions.

Until that co-gate passes, the vocabulary is not validated as a general editorial model.

## 9. Conclusion

`BR-FRAME` and the first `BR-DOM` reduction pass support continuing with the Editorial Construction Space and typed plural vocabulary. They reject both a universal scalar/vector representation and a universal event type. The next domain work should be driven by representation/history experiments and the prose counterexample, not by adding vocabulary speculatively.
