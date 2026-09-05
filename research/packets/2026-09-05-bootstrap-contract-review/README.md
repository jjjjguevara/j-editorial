# Bootstrap contract adversarial review — 2026-09-05

**Verdict: RETURN-WITH-FINDINGS.** The static review is executed; the proposed amendments are ready for external revision, not accepted. `ADVERSARIAL-REVIEW-REQUIRED`, every empirical program gate, and the architecture, implementation, provider-disclosure, and model-training-data holds remain unchanged.

## Authority, target, and method

Authorization is `BOOTSTRAP-REVIEW-2` in the [decision log](../../decisions/DECISION-LOG.md): the current owner request authorizes a review and a PR, not merge or scientific gate closure. The target is `BOOTSTRAP.md` at main commit `360d6ed15fbee7d38dc659f8324763bf637b3924`, blob `26c35a75d9d9fb81402a2705d5a0cf09099c310e`. The review also inspects the research charter, roadmap, program charters/results, paired coverage, decision log, and merged PR #3 reconciliation.

Method: expert static adversarial review, logical counterexamples, primary-source rechecks, and reproduction of already committed tools. This session did not author new experimental fixtures or validators, recruit participants, invoke a model provider, benchmark a database, inspect new private product source, construct corpora, or run held dataset research. The counterexamples below are reasoning tests, not claims that an unbuilt product has been exploited.

Independence: this is a separate review session from the earlier fixture-authoring sessions, not an independently authenticated human review. The reviewer also authored the proposed remedies; those remedies have no independent validator/red-team acceptance yet. Existing fixture reproduction is explicitly not the pre-registered independent research required by `RESEARCH.md` sections 23–27.

Navigation: [question and ADR coverage](COVERAGE.md), [source rechecks](SOURCE-RECHECKS.md), [validation and evidence](VALIDATION.md). The matrices are audit traceability, not a competing task tracker.

## Findings and proposed dispositions

All fourteen findings remain **RETURN-WITH-FINDINGS** pending external review of the remedy and, where specified, the existing program gate. “Proposed correction” means wording in this PR, not a validated implementation. Severity describes the risk of acting on the contract, not a discovered deployed vulnerability.

### AR-01 — Research acceptance, provenance, and release authority are conflated (high)

**Attack.** The scope block calls D-03 accepted while its provenance paragraph says the owner's acceptance is missing. A reader can either demand an already-given decision again or treat acceptance of a research shape as proof of architecture. The merged PR #3 receipt has already recovered the omitted excerpts, with a retrieval qualification.

**Proposed correction.** Reconcile the scope paragraph to that receipt, preserve D-04's **for now**, and rename section 3 to a hypothesis under falsification. Sections 0.5 and 27.1 separate a review request, proposed wording, merge, and an explicit scoped release receipt. No new owner preference is inferred.

**Residual.** Recovered excerpts are not independently archived transcript bytes. No empirical gate is passed by provenance repair; `ES-G2` and owner release remain open. Reject any interpretation that this PR selects storage or releases implementation.

### AR-02 — The glossary reinstates ontology commitments the scope rejects (high)

**Attack.** Section 3 derives gaps from findings/obligations, but section 5 calls a gap first-class and still asks whether obligations differ. A satisfied obligation exists without an adverse finding. One unsupported claim can be classified under several gap types; counting each label as a new defect inflates both liabilities and improvements. Section 8.4 also retains a mandatory vector underneath a scalar despite the heterogeneous-observation direction.

**Proposed correction.** Align gap, obligation, and checkpoint definitions; allow persistent view identities without mandating stores. Preserve heterogeneous observations and require explicit scale/weighting justification rather than assume vector arithmetic.

**Residual.** A minimal source-plus-annotations model remains a serious alternative. Independently encoded material must establish which distinctions and durable IDs earn their cost (`FD-G1`, `FD-G2`, `PS-G2`); paired examples do not establish a universal ontology.

### AR-03 — Readiness can pass without an evaluated release contract (high)

**Attack.** `all(required_conditions_pass)` is vacuously true for an empty list, while a detector that did not run may report no blockers. An approval for revision A also cannot authorize publication of revision B. A waiver or stale source must not silently convert an unverified claim into correctness.

**Proposed correction.** Section 8.3 requires an approved applicability inventory, admissible evidence, explicit unknown/conflict dispositions, waiver authority and expiry, and revision-bound approval/publication. An empty inventory needs explicit justification rather than automatic acceptance.

**Residual.** Release-policy semantics, invalid/expired-waiver cases, and changed-input cases require independent proof (`GP-G1`, `PS-G1`, `SEC-G1`). This review supplies no executable release policy.

### AR-04 — Goal or prior changes can launder an apparent improvement (high)

**Attack.** An evaluator can improve coverage by dropping an inconvenient obligation, changing audience, or choosing the more permissive rule. An edit then appears successful without improving the artifact. A syntactically present citation can also be inapplicable to the actual claim.

**Proposed correction.** Section 7.1 binds obligations to source, scope, applicability, version, and authority. Changed goals/norms produce a separately identified evaluation; fixed-goal comparisons measure editorial change. Unknown applicability differs from inapplicability, and conflicts remain visible.

**Residual.** `GP-G1` must establish precedence, inheritance, defeasibility, and domain exceptions. No guide redistribution right is granted. A narrow publication-specific prior set is preferable to unsupported universal rules.

### AR-05 — Text/hash equivalence is not identity or safe retargeting (high)

**Attack.** Two identical paragraphs have the same digest but may have different obligations and authorship. Moving, splitting, copying, normalizing Unicode, or rewriting them can make a selector ambiguous. A successful JSON round-trip does not establish AST/DOM, source-byte, or unsupported-syntax fidelity.

**Proposed correction.** Section 6.4 binds targets to revisions and coordinate systems, distinguishes resolution outcomes, and requires correspondence evidence. Preserve exact bytes separately from normalized/hash inputs. Specify an encoding profile without selecting JSON or RFC 8785. Checkpoints state exact, semantic, and projection guarantees separately. Relevant priors: `SRC-013`, `SRC-014`, `SRC-089`.

**Residual.** `REP-G1`, `FD-G2`, and `HIST-G1` need real-source split/copy/rewrite/round-trip evidence against a minimal annotation control. Literal matching stays bounded evidence, not general stable identity.

### AR-06 — Accepted commands, successful operations, and replay effects differ (high)

**Attack.** An accepted edit can fail before commit, partially apply, or be retried. A replay that sends a publication action again is not harmless state reconstruction. Two concurrent commands approved against the same old state may invalidate one another. Reverting text does not restore a now-expired approval.

**Proposed correction.** Section 12.6 separates proposed, authorized, executed, committed, and verified outcomes; makes replay side-effect-free; and calls for pre-state binding, retry/duplicate semantics, partial-failure audit, and re-evaluation after merge/revert. Git's expected-old-ref mechanism (`SRC-114`) illustrates a bounded control, not a multi-store transaction proof.

**Residual.** `ES-G1`, `ES-G2`, `HIST-G1`, and `PS-G1` require discriminating executions and failed-operation/abstention cases. A checkpoint+journal implementation remains admissible; causal language alone does not require event sourcing.

### AR-07 — Provenance is not truth; hashes are not replay closure (high)

**Attack.** Several sources may all copy one erroneous origin. A source can change while the document remains identical. A hash identifies absent evidence without making it retrievable; changing goal, norm, reducer, evidence, or source validity can change the result of nominally “the same” snapshot.

**Proposed correction.** Section 11.4 distinguishes provenance, authority, applicability, support/contradiction, freshness, and independence, and requires a versioned evaluation-input manifest. Section 12.6 scopes replay to available authorized inputs. Missing bytes and nondeterministic external dependencies limit the claim. `SRC-014` supports provenance relations, not truth.

**Residual.** `GP-G1`, `ES-G1`, and `AMN-G1` remain open. Raw oracle outputs and their permissible retention cannot be replaced by agent source-reading or unsupported digest claims.

### AR-08 — Representation/storage comparisons lack a decision-relevant control (high)

**Attack.** Four encodings that rearrange the same hand-authored dictionary can all reproduce the same result without comparing physical backends, operational cost, concurrency, or recovery. Branching and CRDT requirements may be imported from interesting tools rather than the first use case.

**Proposed correction.** Section 13.9 requires a minimal checkpoint-plus-annotation control, discriminating workloads, predeclared budgets, complexity/cost accounting, and migration/recovery tests before a substrate decision. Collaboration remains conditional. No performance threshold or vendor preference is invented here.

**Residual.** `ES-G1`, `REP-G1`, and `HIST-G1` must supply actual evidence. Failure to beat the simple control should narrow or reject the richer design. Dataset storage choices remain held, not piggybacked onto persistence research.

### AR-09 — Seeded perturbations are not exhaustive ground truth (high)

**Attack.** Deleting one citation from a supposedly verified document proves which edit was made, not that the resulting document contains exactly one defect. The edit can create collateral problems; a model can detect a valid pre-existing issue or propose a different valid repair and be penalized under exact-match scoring.

**Proposed correction.** Replace section 14.6's exact-ground-truth claim with verified intervention/effect separation, independent adjudication, unchanged controls, valid alternatives, and generator-shortcut checks. Unadjudicated findings remain unknown rather than false.

**Residual.** `EV-G1` must validate task/grader admissibility. Training-target eligibility and corpus-generation research remain `DEFER` under `DG-G0`; this amendment authorizes neither.

### AR-10 — Candidate metric formulas admit selective reporting and false precision (high)

**Attack.** Abstaining on difficult instances improves conditional accuracy; omitting failed attempts improves closure. A recall denominator of “all true gaps” is unavailable without bounded adjudication. Hundreds of adjacent snapshots are not hundreds of independent documents. Weighted overlapping gaps can reward arbitrary taxonomic granularity.

**Proposed correction.** Section 15.11 requires units, matching, denominators/zero cases, adjudication coverage, abstention, infrastructure/retry accounting, clustered sampling, uncertainty, and predeclared decision-relevant differences. No universal sample size or interval method is asserted. `SRC-117` and `SRC-119` motivate explicit constructs and outcome-oriented evaluation, not validated metrics here.

**Residual.** `EV-G1` must establish grader reliability, rare severe error coverage, and a statistical protocol; conditional scores alone cannot support a benchmark claim.

### AR-11 — Expressibility is not editorial usefulness or cross-domain validity (high)

**Attack.** A fixture can express a disagreement or alternate edit because its author wrote two records. That does not show independent readers recognize the distinction or that an editing intervention helps. A system that rewrites acceptable text can score well against its own preferred patch while creating extra review work.

**Proposed correction.** Section 15.11 adds no-edit/simple-checklist controls and independent reader/developer outcomes. Section 27.1 preserves the paired proof's bounded scope and Doc Doctor's downstream boundary. The core must still work without a model provider.

**Residual.** `AMN-G1/2`, `PR-G1/2`, `PS-G1/2`, `FD-G1`, and downstream `DD-G1` remain open. The existing paired coverage lists missing waivers, failed operations, explicit abstention, reverts, harmful fixes, and unnecessary edits; no new experiment in this session repairs them. A failed usefulness comparison can justify reducing the product scope.

### AR-12 — Preserving hostile source is not safely executing or disclosing it (high)

**Attack.** Exact preservation of executable markup conflicts with rendering it unsandboxed. A model can emit a well-formed command that is unauthorized, or approve a benign preview whose payload changes before execution. Raw logs and checkpoints can disclose data to providers or public CI artifacts.

**Proposed correction.** Section 22.7 requires authorization outside the model, per-operation/current-resource approval, an exact approved payload binding, inert storage versus safe rendering, sandbox boundaries, and authorized/redacted evidence retention. `SRC-092` is guidance, not evidence these controls work.

**Residual.** `SEC-G1` requires a real threat model and controlled tests. A JSON string remaining inert is not prompt-injection resistance. No provider disclosure, expanded privileges, or private-source publication is authorized by this PR.

### AR-13 — Erasure and unrestricted exact-history promises conflict (high)

**Attack.** Removing a row or current-file sentinel leaves checkpoints, replicas, backups, logs, exports, caches, and potentially training derivatives. Retaining every raw output publicly can itself violate privacy/rights. A hash or tombstone may retain identifying information; it is not an automatic safe harbor.

**Proposed correction.** Section 22.7 requires a copy/derivative inventory, lawful retention/access boundaries, bounded purge evidence, and explicit resulting replay limitations. Sections 5 and 11.4 qualify byte retention. `SRC-116` documents bounded SQLite behavior; it supplies neither cross-copy erasure nor a legal compliance conclusion.

**Residual.** `SEC-G1` and `HIST-G1` remain open. Deletion impacts on training artifacts are held under `DG-G0`. Reject an architecture that promises both unconditional exact replay and irreversible deletion of the same content without specifying exceptions.

### AR-14 — Gate vocabulary, coverage, and exit authority are underspecified (high)

**Attack.** BOOTSTRAP section 26 offers five different recommendation labels from RESEARCH's five verdicts. RESEARCH says use the “lowest” verdict without defining an ordering. Empty obligations or a self-authored validator can then appear to pass. Section 27's persistence ADR wording can be read as requiring a file section 24 forbids creating yet.

**Proposed correction.** Align verdicts; add explicit aggregation/admissibility in RESEARCH 26.1; require approved nonempty scope, coverage, preregistration, independent validation, and a red-team record for empirical PASS. Section 27.1 distinguishes a persistence decision process from acceptance of an implementation ADR. Preserve replaced text verbatim, frozen packet verdicts, and all existing gate states.

**Residual.** The aggregation rule itself needs external revision; it is a disposition policy, not an ordinal scientific scale. This review's own wording cannot validate itself. An owner receipt, not a merge or green CI job, releases a specifically named vertical. No ADR files or implementation packages are created.

## Review outcome and gate decomposition

| Obligation | Disposition | Evidence and remaining boundary |
|---|---|---|
| Inspect/falsify the current contract and trace every required question | RETURN-WITH-FINDINGS | Fourteen reasoned findings; all 47 questions and 52 queue items routed in COVERAGE.md; external review pending |
| Propose internally consistent amendments without selecting architecture | RETURN-WITH-FINDINGS | Direct authored changes; superseded text retained; independent acceptance pending |
| Establish empirical representation, usefulness, safety, or grader validity | DEFER | Not executed by this static review; existing program gates remain open |
| Execute model-training-data research | DEFER | Explicit separate-session hold, not a missing claim silently counted as PASS |
| Reproduce existing tooling and check document integrity | RETURN-WITH-FINDINGS | Executed checks recorded in VALIDATION.md; a tooling success is not research PASS |

This review does not relabel every downstream program DEFER: those programs retain their existing lifecycle and gate records. The table describes what this review did and did not establish. There is no automatic blocker closure.

## Tracker and handoff

Beads remains authoritative. Its read-only CI snapshot was retrieved and compared with live `refs/dolt/data` at `ca183ab6331adf1e51b5d533b6c5628a07b2fa1a`. Local `bd prime` failed because `bd` is not installed; no claim, gate closure, database edit, import, registry rewrite, or Dolt push was performed. The proposed findings route to existing gates rather than inventing a second backlog. Fresh native-registry CI on the PR remains a separate check from the historical snapshot.

External revision should examine the fourteen remedies, the release/waiver contract, metric admissibility, replay/erasure limits, and verdict aggregation against the pinned base. Review approval must not be interpreted as authorizing the deferred experiments, accepting a backend, or merging without the owner's instruction.
