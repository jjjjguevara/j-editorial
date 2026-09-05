# Bootstrap Phase 2 foundations

Status: **paired technical-reference/general-prose research executed / human review pending**  
Branch: `research/bootstrap-phase-2-foundations`  
Base: `70c8156cb52755ccffe4e9ed3049bd7f01f52297`  
Research cutoff: **2026-09-04**  
Implementation gate: **closed**  
Persistence/ADR gate: **closed**  
Dataset research: **not executed**

## Purpose

This directory executes the first research stage released by the merged bootstrap adversarial review. It tests the accepted Editorial Construction Space and causal event–fluent shape against two materially different artifacts:

1. an Amnesia API-reference contradiction; and
2. the accepted public portfolio About page as a general-prose companion.

It derives representation/history requirements, establishes a security/authority baseline, and performs a paired-domain representation co-gate. It does not bootstrap production code.

## Accepted inputs

- `D-01`: paired technical-reference and general-prose proof.
- `D-01P`: Option A — `jjjjguevara/sci-jjjjguevara/src/pages/about.astro` at the pinned accepted revision is the prose target; supporting portfolio records are evidence/norms only.
- `D-02R`: Editorial Construction Space plus typed plural records as a falsifiable research hypothesis.
- `D-03`: causal event–fluent multidimensional state with exact checkpoints and versioned projections is adequate for research.
- `D-04`: meaningful semantic operations plus checkpoints.
- `AMN-01`: pinned Amnesia product evidence may be used read/build/test-only in an isolated environment.
- Model-training dataset research remains held.

## Work executed

1. recorded the D-03 and D-01P acceptance boundaries;
2. refined the domain vocabulary through reduction tests;
3. bound current Amnesia Docs and Amnesia product refs;
4. retained static positive and adverse technical evidence separately;
5. constructed and validated a 13-transaction Amnesia causal event–fluent fixture;
6. derived representation, history, time, replay, target, evolution, erasure, and backend-exit requirements;
7. compared candidate substrate roles without selecting one;
8. established the minimum security and authority boundary for later agent/eval work;
9. audited the portfolio as a prose source system and bounded the target to `/about`;
10. reconstructed two real About-page transitions under immutable commits/blobs;
11. constructed and validated a 22-transaction prose fixture with qualified evidence, three defensible remedies, unresolved synthetic review disagreement, privacy rejection/redaction, and counterfactual staleness;
12. bound both independent results into a seven-obligation paired-domain manifest and validated it as `pass-with-constraints`.

## Result

### Technical fixture

```text
status:                    pass
E-01 through E-10:         passed
transactions:              13
source bindings:           5
fluents:                   3
projections:               4
input_file_sha256:         cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82
canonical_research_sha256: 4035f6f544c08e6c8878b0e0bbc0a2a696a48501feab0f1ea554ae74c4450e8c
```

### General-prose fixture

```text
status:                    pass
P-01 through P-12:         passed
transactions:              22
source bindings:           9
actors:                    5
findings:                  5
fluents:                   6
projections:               5
input_file_sha256:         9c24cf03065f69aacaed4375c9830feeec0a78c8277e3a07c0b8f299147b4eb2
canonical_research_sha256: 74e0e3282596fd7ade8607c9a0ef40b82e096ad98840e157407e0c6b972f012e
```

### Paired-domain co-gate

```text
status:                    pass-with-constraints
C-01 through C-07:         passed
manifest_file_sha256:      087bdcfa2959a678deb0fd4953596f6250e6e6be7f38b16b8a71e91a66f80ce5
canonical_research_sha256: 46a0eb9f6f6e955df749677673a85f680dc710af5041ddbf921bce2762c38cd7
```

The favored logical hypothesis remains:

```text
typed identity-bearing editorial data
+ exact material checkpoints
+ causal event transactions
+ time-scoped facts / fluents
+ observations and evidence with provenance and uncertainty
+ explicit obligations, proposals, authority, decisions, and outcomes
+ versioned derived projections
```

The paired result supports this shape for further research. It does not establish prose-grader reliability, empirical reader performance, a production schema, or a persistence architecture.

## Artifact map

| Artifact | Role |
|---|---|
| [`D-03-ACCEPTANCE.md`](../../decisions/D-03-ACCEPTANCE.md) | Binding scope of the causal event–fluent research direction |
| [`D-01P-ACCEPTANCE.md`](../../decisions/D-01P-ACCEPTANCE.md) | Binding owner acceptance of the portfolio About-page scope |
| [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md) | Primary/official sources, pinned Amnesia evidence, and limitations |
| [`FRAME-DOMAIN-RESULT.md`](../../programs/frame-domain/FRAME-DOMAIN-RESULT.md) | Cross-axis datum, surviving distinctions, rejected reductions, and candidate vocabulary |
| [`AMNESIA-ORACLE-EXPERIMENT.md`](../../programs/amnesia/AMNESIA-ORACLE-EXPERIMENT.md) | Pinned static product/docs evidence, history observations, execution limits, and technical sub-gate |
| [`EVENT-FLUENT-EXPERIMENT.md`](../../programs/event-state/EVENT-FLUENT-EXPERIMENT.md) | Technical fixture method, trace, E-01–E-10 results, comparison, and falsification conditions |
| [`PORTFOLIO-PROSE-CANDIDATE-AUDIT.md`](../../programs/prose/PORTFOLIO-PROSE-CANDIDATE-AUDIT.md) | Pre-decision portfolio scope/evidence audit |
| [`PORTFOLIO-PROSE-EXPERIMENT.md`](../../programs/prose/PORTFOLIO-PROSE-EXPERIMENT.md) | Executed prose fixture, P-01–P-12 results, and limitations |
| [`PAIRED-DOMAIN-RESULT.md`](../../programs/paired-synthesis/PAIRED-DOMAIN-RESULT.md) | C-01–C-07 cross-domain result and required refinements |
| [`REPRESENTATION-HISTORY-RESULT.md`](../../programs/representation/REPRESENTATION-HISTORY-RESULT.md) | Logical requirements, replay/time/target contracts, backend-exit contract, and bake-off workload |
| [`SECURITY-AUTHORITY-BASELINE.md`](../../programs/security/SECURITY-AUTHORITY-BASELINE.md) | Trust zones, authority matrix, agent boundary, retention, erasure, and threat cases |
| [`REPRODUCE.md`](REPRODUCE.md) | Technical, prose, and paired validator reproduction instructions |
| [`STAGE-GATE.md`](STAGE-GATE.md) | Phase results, released research, remaining holds, and review boundary |
| [`fixtures/amnesia-notes-event-fluent.json`](../../programs/event-state/fixtures/amnesia-notes-event-fluent.json) | Technical research-only trace; not a corpus |
| [`fixtures/portfolio-about-event-fluent.json`](../../programs/prose/fixtures/portfolio-about-event-fluent.json) | General-prose research-only trace; not a corpus |
| [`fixtures/paired-domain-proof.json`](../../programs/paired-synthesis/fixtures/paired-domain-proof.json) | Immutable cross-result binding and co-gate claims |
| [`tools/validate_event_fluent_fixture.py`](../../programs/event-state/tools/validate_event_fluent_fixture.py) | Technical standard-library fixture validator |
| [`tools/validate_portfolio_prose_fixture.py`](../../programs/prose/tools/validate_portfolio_prose_fixture.py) | General-prose standard-library fixture validator |
| [`tools/validate_paired_domain.py`](../../programs/paired-synthesis/tools/validate_paired_domain.py) | Cross-result binding and non-overstatement validator |
| [`results/amnesia-notes-event-fluent-validation.json`](../../programs/event-state/results/amnesia-notes-event-fluent-validation.json) | Committed deterministic technical result |
| [`results/portfolio-about-event-fluent-validation.json`](../../programs/prose/results/portfolio-about-event-fluent-validation.json) | Committed deterministic prose result |
| [`results/paired-domain-validation.json`](../../programs/paired-synthesis/results/paired-domain-validation.json) | Committed paired-domain result |

## Deliberate non-actions

This phase did not:

- modify Amnesia, Amnesia Docs, Doc Doctor, or the portfolio source;
- invoke a workflow that could deploy;
- reproduce a private repository build without an isolated authenticated checkout;
- assert that the live `/about` route equals the pinned source;
- independently verify private professional or academic records;
- establish human/model prose-grader reliability or empirical reader-task success;
- select a backend, event store, database, CRDT, canonical serialization, or implementation language;
- accept an ADR;
- create production schemas, APIs, packages, services, or agents;
- alter `.beads` directly;
- execute dataset/corpus research, labeling, preference extraction, training, or benchmarking.

## Tracking limitation

The repository's native Beads store is Dolt-backed. This execution environment does not provide a compatible `bd`/`dolt` checkout, so tracker state was not fabricated or manually edited. The existing Beads fan-out contract remains required in a compatible checkout.

## Next stage

The paired foundation now supports research on:

- isolated Amnesia and portfolio build/source parity;
- target-resolution experiments across real document edits;
- the representation/history substrate bake-off;
- empirical reader-task and annotation protocol design;
- deterministic, human, and model grader calibration/meta-evaluation;
- a later D-03R/representation ADR packet based on both proof slices.

All production implementation, persistence, dataset, training, and bootstrap-exit gates remain closed pending the corresponding research and human review.
