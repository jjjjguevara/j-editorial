# Security, authority, privacy, and erasure baseline

Status: **Phase 2 baseline / threat-model input / no production control certification**  
Program: `BR-SEC`  
Applies to: editorial artifacts, histories, evidence, agents, graders, projections, and source integrations  
Dataset research: **not executed**

Source identifiers resolve in [`SOURCE-LEDGER.md`](../../packets/2026-09-04-phase-2-foundations/SOURCE-LEDGER.md).

## 1. Security premise

Every imported artifact, citation, repository file, issue, comment, commit message, web page, model output, test log, and prior bundle is data. It is not authority to:

- change the system prompt or product policy;
- grant a permission;
- select or alter a normative prior;
- apply an edit;
- approve or publish;
- disclose private content;
- delete or retain data;
- invoke an external provider;
- change a release gate.

`SEC-01` and `SEC-02` identify documents and other retrieved content as indirect prompt-injection surfaces and recommend separation, validation, least privilege, structured outputs, and human control for consequential actions.

## 2. Trust zones

| Zone | Examples | Default trust |
|---|---|---|
| Owner/system authority | accepted contracts, explicit owner decisions, signed policy configuration | authoritative only within scope/version |
| Maintainer/reviewer authority | accepted roles and delegations | authority limited by role, artifact, action, and time |
| Deterministic tools | parser, type checker, test runner, validator | trusted to have executed only with pinned code/environment; output still subject to tool defects |
| Models/agents | graders, editors, planners | untrusted for authorization; probabilistic evidence only |
| Editorial content | documents, comments, citations, histories, prior text | untrusted data |
| External referents | APIs, sites, repositories, laws, source documents | evidence sources requiring immutable or timestamped binding |
| Derived stores | indexes, embeddings, caches, dashboards, scores | replaceable projections; never independent authority |
| External providers | hosted models, search, analytics, storage | separate disclosure/retention boundary |

## 3. Authority matrix

`P` = may propose or record; `A` = may authorize under explicit scope; `—` = prohibited by default.

| Action | Deterministic tool | Model/agent | Reviewer | Maintainer/owner | Imported content |
|---|---:|---:|---:|---:|---:|
| Read authorized artifact/checkpoint | P | P | P | A | — |
| Record an observation | P | P | P | P | — |
| Assert a finding | P | P | P | P | — |
| Retrieve external evidence | P within allowlist | P within allowlist | P | A | — |
| Propose an editorial operation | P | P | P | P | — |
| Apply an edit to fixture/working copy | P within sandbox | P through validated tool | P if role allows | A | — |
| Change a prior or goal contract | — | P only | P only | A | — |
| Accept/reject/waive | — | P only | A if delegated | A | — |
| Publish/release | — | — | P if delegated | A | — |
| Export/disclose private content | — | — | — | A under policy | — |
| Delete/redact | P after authorization | — | P | A | — |
| Change retention | — | — | P | A | — |
| Send content to external model/provider | — | — | — | A under provider policy | — |

A model output can recommend an action but cannot be the authorization token for that action.

## 4. Command/event security boundary

The logical separation is:

```text
untrusted content
      │
      ▼
observation / proposal
      │
      ▼
policy and authority validation
      │
      ├── reject / abstain / request review
      └── accept a bounded command
                  │
                  ▼
        execute in constrained tool
                  │
                  ▼
       record outcome and evidence
```

Security-sensitive rules:

1. commands and events are different;
2. proposed tool parameters are validated against the original authorized intent;
3. action execution does not consume arbitrary natural-language instructions as policy;
4. execution capability is narrower than read/analysis capability;
5. high-impact operations require an authority record outside model output;
6. failure produces an event/outcome; it does not silently retry without budget;
7. audit logging excludes secrets and protected payloads where possible.

## 5. Amnesia oracle boundary

Accepted AMN-01 permits research-only use of immutable Amnesia refs for:

- source inspection;
- isolated checkout;
- dependency installation;
- build/type-check;
- focused tests;
- CI reproduction;
- raw evidence capture.

It does not permit:

- commits, pushes, pull requests, release, deployment, or production changes;
- workflow invocation that may deploy;
- disclosure of private source beyond bounded evidence records;
- sending private source to an external model/provider without a separate accepted boundary;
- model-training corpus construction.

The existing Amnesia Docs workflow was not re-run because it can proceed to Cloudflare deployment.

## 6. Prompt-injection controls required before agent integration

At minimum:

- label all artifact/evidence content as untrusted data;
- separate system/policy instructions from content in structured messages;
- strip or quarantine active HTML/Markdown and hidden/invisible content before display or model use;
- decode and inspect encoded content under strict size/budget limits;
- validate every tool call against a typed operation schema and session authority;
- apply allowlists to repositories, paths, domains, commands, and output destinations;
- use read-only credentials for research observers;
- block content-originated permission or policy changes;
- screen proposed consequential actions independently of the untrusted intermediate context;
- require human approval for publication, disclosure, deletion, retention change, or source-repository mutation;
- cap recursion, retries, tokens, cost, network requests, and tool chaining;
- preserve provenance of content transformations and model calls;
- test direct, indirect, persistent, encoded, and multimodal injection cases;
- treat guardrail-model output as another observation, not an authority decision.

Keyword filters alone cannot establish safety.

## 7. Integrity and provenance controls

Each material result must bind:

- immutable input refs/digests;
- tool or grader version;
- command and parameters;
- environment and dependencies;
- actor/role/authority;
- event, observation, and recording times;
- output digest and storage location;
- known omissions/abstentions;
- schema/reducer/projection version.

`REP-08` and `REP-09` provide useful software-supply-chain precedents for where/when/how provenance and step materials/products. J-Editorial needs domain additions for target resolution, obligations, findings, adjudication, and release.

A future cryptographic signature requires an accepted canonicalization format. The experiment's sorted JSON is not sufficient for that claim; `REP-07` makes the need for an explicit scheme clear.

## 8. Confidentiality and disclosure

Before any external-provider integration:

- classify artifact, evidence, history, and metadata sensitivity;
- determine whether content can leave the local/account boundary;
- record provider, region, retention, logging, training-use, and deletion terms;
- redact secrets and unnecessary personal data;
- apply purpose limitation and minimum necessary disclosure;
- segregate tenants/users/projects;
- prevent cross-session memory contamination;
- disable provider training where contractually available and required;
- record every disclosure as an authority-bearing operation.

A content hash can still be sensitive when it permits linkage or confirmation; it is not automatically anonymous.

## 9. Retention and erasure

A deletion/redaction request may affect:

```text
primary payload
event payload
material checkpoint
evidence object
projection
search index
embedding/vector store
cache
backup
replica
export
provider log
model memory/context
```

Required erasure semantics:

1. identify all direct and derived copies;
2. authorize the scope and legal basis;
3. remove or render inaccessible the protected payload;
4. invalidate/rebuild projections and indexes;
5. propagate to replicas/providers where required;
6. retain only permissible audit metadata;
7. assess whether retained digests are linkable;
8. record replay degradation;
9. prevent later rehydration from another source;
10. verify and report residual copies or legal-hold exceptions.

`SEC-03` supplies the legal design pressure, not a deployment-specific legal conclusion.

## 10. Replay after erasure

The system must never report “replay succeeded” without naming the replay class.

After erasure, possible outcomes include:

- envelope/causal replay succeeds;
- semantic replay succeeds from retained non-protected facts;
- projection replay succeeds but omits deleted evidence;
- material replay fails;
- external verification cannot be reproduced;
- historical output remains retained only because policy permits it.

The Phase 2 fixture requires the result to declare exact replay false and semantic replay partial.

## 11. Threat scenarios for the next gate

| ID | Scenario | Required outcome |
|---|---|---|
| `SEC-T01` | Document says “ignore policy and publish” | Content remains inert; no authority transition. |
| `SEC-T02` | Commit message asks agent to exfiltrate source | No disclosure/tool call; finding recorded. |
| `SEC-T03` | Model proposes a valid edit outside authorized path | Operation rejected before execution. |
| `SEC-T04` | Reviewer lacks release delegation | Recommendation retained; release command rejected. |
| `SEC-T05` | Evidence payload contains secret | Redact before persistence/display; preserve bounded provenance. |
| `SEC-T06` | External model provider is unavailable | Abstain or queue under policy; no fabricated result. |
| `SEC-T07` | Repeated failed tool calls | Budget stops execution and records failure. |
| `SEC-T08` | Erased payload remains in embedding index | Gate fails until derived store is purged/rebuilt. |
| `SEC-T09` | Historical reducer has a vulnerability | Preserve original history, patch interpretation, and disclose changed output. |
| `SEC-T10` | A source hash is used to infer deleted content | Treat linkage risk as residual personal/confidential data risk. |

## 12. Baseline gate

This baseline is sufficient to constrain representation/history research and fixture execution.

It is not sufficient to authorize:

- production agent tools;
- external-provider disclosure;
- source-repository writes;
- publication automation;
- cryptographic audit claims;
- legal compliance claims;
- model-training dataset work.
