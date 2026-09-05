# Amnesia technical-reference proof — Charter

Slug: `amnesia`  
Alias: `BR-AMN`  
Beads epic: `j-editorial-47m`  
Lifecycle: **ACTIVE**  
Controlling contract: `BOOTSTRAP.md`; method: `RESEARCH.md`  
Decisions relied on: `AMN-01` (verbatim), `D-01` (paraphrased); see [`DECISION-LOG.md`](../../decisions/DECISION-LOG.md); authorization boundary in [`AMNESIA-ORACLE-AUTHORIZATION.md`](../../decisions/AMNESIA-ORACLE-AUTHORIZATION.md)

## 1. Authority and status

Research-only use of `jjjjguevara/amnesia-docs` and `jjjjguevara/amnesia` at immutable refs. No mutation, pull request, release, deployment, or external-provider disclosure. The program is ACTIVE on static evidence; the executable oracle has never run.

## 2. Mission

Evaluate documentation claims against pinned product types, runtime composition, focused tests, and human developer tasks, and supply the technical half of the paired proof.

## 3. Why the program is separate

It is the only slice with a largely deterministic referent, so it anchors what "executable evidence" means for the framework.

## 4. Decisions or specification questions it informs

The first end-to-end proof; obligation-specific grader allocation; evidence and referent modelling (`BOOTSTRAP.md` ADR queue items 15 and 16).

## 5. In scope / out of scope

In scope: API root and access, capability vocabulary and hierarchy, `commands.notes`; pinned refs `amnesia-docs@5d8aa677793cc2b4734106bb21e6118f0cc5a2aa` and `amnesia@4d0d1efec4ee4958db504cb56bcf47dfbc19b92a`.  
Out of scope: fixing the documentation, changing the product, any corpus use.

## 6. Dependencies on other programs

Upstream: `AMN-01`. Downstream: `paired-synthesis`, `evaluation`, `goal-priors`.

## 7. Hypotheses under attack

- H1. Documentation claims can be evaluated reproducibly against the pinned product. Status: one contradiction established by reading; nothing executed.
- H2. Source precedence is obligation-specific rather than universal. Status: argued in [`AMNESIA-ORACLE-EXPERIMENT.md`](AMNESIA-ORACLE-EXPERIMENT.md) section 7.
- H3. A product change can make unchanged documentation stale. Status: modelled as a counterfactual; the real product API directory is unchanged across the 47 commits after the pin, so the case has not occurred.

## 8. Required current / SOTA reconnaissance

Re-inspect both repositories at execution; the docs repository has not moved past the pin, the product repository has.

## 9. Required primary-source classes

Class 5.4 (pinned source and history), 5.5 (executed type checks and tests once `AMN-G1` runs), 5.6 (developer-task review).

## 10. Comparison set

Docs-as-code parity checkers and API-description linters were surveyed in Phase 1; none is selected.

## 11. Experiments or bake-offs

`AMN-G1`: isolated checkout of both pinned refs on the owner's machine, dependency install from lockfiles, type check, focused notes and capability tests, docs build with deployment disabled; raw output committed beside its digest. This is the first experiment in the program that can return a negative result.

## 12. Representative workloads or fixtures

The event-state fixture uses this slice; the notes fragment in [`representation/fixtures/target-fragments.json`](../representation/fixtures/target-fragments.json).

## 13. Scale and budget analysis

Not yet specified; expected to be small.

## 14. Security, privacy, licensing, governance

Private source stays in the owner's environment; only bounded observations enter the repository. No workflow with deployment permission may be invoked to obtain evidence.

## 15. Interoperability and migration

Not applicable at this stage.

## 16. Deliverables

Oracle contract; executed check outputs; adjudication packet; positive and adverse findings kept separate.

## 17. Falsification criteria

The slice is returned for narrowing if pinned product evidence cannot be built or tested, if source precedence cannot be stated per obligation, or if the static contradiction is not reproduced by an executed type check.

## 18. Gate criteria

- `AMN-G1` `j-editorial-47m.1`: isolated build, type-check, and focused tests at pinned refs with committed raw output.
- `AMN-G2` `j-editorial-47m.2`: developer-task evidence.

## 19. Downstream ADR or specification candidates

Evidence/source model; claim-evidence relation model.

## 20. Residual risk and revisit policy

The documented contradiction is live in the owner's public documentation; fixing it is outside this program. Revisit the pin if the docs repository changes.

## 21. Independence declaration

Audit, experiment, and fixture share one author lineage. The 2026-09-04 review independently re-read the pinned files in local clones and confirmed the contradiction; no executed check has run.
