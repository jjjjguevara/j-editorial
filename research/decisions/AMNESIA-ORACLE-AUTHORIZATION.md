# AMN-01 — Amnesia product-oracle authorization

Status: **accepted / research-only / immutable-ref requirement**  
Owner decision: **AMN-01 option A**  
Date: **2026-09-04**  
Repositories: `jjjjguevara/amnesia-docs`, `jjjjguevara/amnesia`  
Implementation and mutation authority: **not granted**  
Dataset research: **held**

This record supersedes the unresolved authorization question in Section 9 of [`AMNESIA-DOCS-SLICE-AUDIT.md`](../programs/amnesia/AMNESIA-DOCS-SLICE-AUDIT.md).

## 1. Authorized purpose

The private Amnesia product repository may serve as the executable product-evidence oracle for the Amnesia Docs technical proof. The documentation repository and its development history may serve as a bounded evaluation and architecture fixture containing real faulty references, corrections, readiness changes, and editorial improvements.

## 2. Authorized research operations

Against authorized environments and immutable refs, bootstrap research may:

- read repository source, tests, configuration, decisions, and history;
- check out or materialize repository states;
- install declared dependencies in an isolated environment;
- build and type-check;
- run focused unit, integration, contract, and documentation-example tests;
- invoke existing CI or reproduce its relevant commands;
- compare documentation claims against public types, exports, runtime composition, capability checks, events, and observed behavior;
- compare documentation states across commits;
- capture raw command output, test reports, diffs, hashes, and environment metadata;
- create local or J-Editorial-only fixtures and reports referring to pinned evidence;
- use failures, corrections, and improvements to test D-03 state transitions and D-04B history reconstruction.

## 3. Prohibited operations

This authorization does not permit bootstrap research to:

- edit, commit, push, open a pull request, merge, tag, release, or deploy in either Amnesia repository;
- change issues, project state, branch protection, secrets, workflows, or production services;
- expose private source or secrets outside authorized evidence records;
- infer that a commit, merge, or published page is correct solely because it exists;
- treat accepted edits as preference labels or ideal model outputs;
- construct, label, split, publish, or train on a model-training corpus;
- send private source or repository contents to an external model/provider without a separately accepted security boundary.

## 4. Pinning and reproducibility

Every formal result must record:

- repository and immutable commit SHA;
- paths and symbols evaluated;
- dependency lockfiles and relevant tool versions;
- command, environment, and configuration;
- raw output or content-addressed locator;
- evaluator/reducer version;
- event, observation, and recording times where they differ;
- known skipped tests, inaccessible services, and nondeterministic components.

Moving branch names may be used for reconnaissance only. Any finding promoted into the bootstrap packet must be rebound to immutable refs.

## 5. Oracle precedence is obligation-specific

No source is universally authoritative:

| Obligation | Candidate primary evidence | Required qualification |
|---|---|---|
| Public symbol/signature | exported public TypeScript contract | verify the export boundary and pinned build |
| Runtime availability | composition/wiring plus focused execution | types alone do not prove reachability |
| Behavior | focused tests and observed execution | tests may be incomplete or stale |
| Release/readiness | accepted release policy and evidence bundle | metadata is an assertion, not proof |
| Security framing | actual capability/bypass behavior plus expert review | capability intent is not a sandbox |
| Audience usability | structured developer task and human review | executable parity does not prove clarity |

Conflicts remain findings. Source precedence must be stated in the goal contract rather than silently imposed by the harness.

## 6. Seed evidence

The current technical audit pins:

- documentation: `5d8aa677793cc2b4734106bb21e6118f0cc5a2aa`;
- product: `4d0d1efec4ee4958db504cb56bcf47dfbc19b92a`.

These are seed refs, not permanent baselines. New experiments may select later or earlier states when the selection rationale is explicit.

The documentation history already includes a first-release API publication followed by later wording and surface changes. That history is useful precisely because published claims, metadata, product state, and later corrections can diverge.

## 7. D-03 use

The Amnesia fixture must test at least this transition family:

```text
oracle refs bound
  -> check executed
  -> positive/adverse/uncertain findings recorded
  -> correction proposed
  -> accepted/rejected/waived
  -> artifact checkpoint materialized
  -> verification observed
  -> release/readiness projection updated
```

A single transaction must be able to change several state dimensions while leaving others untouched. A product change must also be able to make unchanged documentation stale.

## 8. Revocation and scope change

The owner may narrow or revoke this authorization. Any broader mutation, deployment, provider disclosure, or dataset use requires a separate explicit decision.
