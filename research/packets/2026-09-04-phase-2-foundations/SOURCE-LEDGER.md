# Phase 2 foundations — source ledger

> **Superseded ledger (2026-09-04).** Identifiers in this file are scoped to this file and collide with identifiers in other legacy ledgers. New work cites `research/LEDGER.md`, whose legacy identifier map resolves every identifier below. This file is frozen as part of its packet; only this banner was added.

Status: **research evidence / no architecture authority**  
Research cutoff: **2026-09-04**  
Repository baseline: `jjjjguevara/j-editorial@70c8156cb52755ccffe4e9ed3049bd7f01f52297`  
External product refs: `jjjjguevara/amnesia@4d0d1efec4ee4958db504cb56bcf47dfbc19b92a`, `jjjjguevara/amnesia-docs@5d8aa677793cc2b4734106bb21e6118f0cc5a2aa`  
Dataset research: **not executed**

This ledger records the sources used to execute the Phase 2 foundational research. A source establishes only the claim stated in its row. No listed data model, event store, database, serialization, or standard is thereby selected for J-Editorial.

## Source-quality rules

- Primary specifications, official documentation, original papers, and pinned repository evidence are preferred.
- Vendor documentation establishes a vendor's behavior or stated contract, not independent superiority.
- A formalism may supply useful distinctions without becoming a product ontology.
- A storage mechanism may satisfy one role without being suitable as the system of record.
- Private-repository observations are summarized and pinned; full private source is not copied here.
- The experiment's deterministic JSON digest is not described as RFC 8785/JCS compliant.

## State machines, events, facts, and causal order

| ID | Source | Version/date | Used for | Limitation |
|---|---|---:|---|---|
| `EVT-01` | Edward F. Moore, [“Gedanken-Experiments on Sequential Machines”](https://doi.org/10.1515/9781400882618-006) | Original 1956; cited edition 2016 | Separation between state transition and state-derived output that motivates the Moore-style `evolve`/`project` distinction. | Classical finite machines are too restrictive for data-bearing editorial state, branch graphs, human disagreement, and external evidence. |
| `EVT-02` | David Harel, [“Statecharts: A Visual Formalism for Complex Systems”](https://doi.org/10.1016/0167-6423(87)90035-9) | 1987 | Hierarchy, concurrency/orthogonality, and communication as extensions to ordinary state diagrams. | A behavioral formalism, not a history, provenance, or editorial truth model. |
| `EVT-03` | W3C, [State Chart XML (SCXML) 1.0](https://www.w3.org/TR/scxml/) | Recommendation, 2015 | Parallel active regions, macrosteps/microsteps, run-to-completion, legal state configurations, and deterministic event processing. | SCXML prioritizes a fully specified executable machine; editorial judgments and external systems can remain uncertain or nondeterministic. |
| `EVT-04` | Robert Kowalski and Marek Sergot, [“A Logic-Based Calculus of Events”](https://doi.org/10.1007/BF03037383) | *New Generation Computing* 4(1), 1986 | Events as distinct from time-scoped facts/fluents and support for later information about earlier events. | Logic-programming formalism; not a direct product schema or persistence recipe. |
| `EVT-05` | Robert Kowalski, [Event Calculus publications](https://www.doc.ic.ac.uk/~rak/papers/rak.html) | Author-maintained bibliography | Primary-author bibliography and follow-on database-update work. | Bibliography does not replace inspection of each underlying work. |
| `EVT-06` | Leslie Lamport, [“Time, Clocks, and the Ordering of Events in a Distributed System”](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/) | 1978 | Happened-before as a partial causal order distinct from a chosen total serialization. | Distributed-system ordering theory does not decide editorial conflict or authority. |
| `EVT-07` | Glynn Winskel, [*Event Structures*](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-95.html) | Cambridge Technical Report 95, 1986 | Causal dependence, concurrency, and conflict among event occurrences. | Denotational/concurrency semantics are more formal and general than the initial product needs. |
| `EVT-08` | Datomic, [Transaction Data](https://docs.datomic.com/transactions/transaction-data-reference.html) | Current docs inspected 2026-09-04 | Atomic sets of datoms, reified transactions, transaction provenance, and distinction between authoring order and fact semantics. | Datomic is a comparator only; its database and tuple model are not selected. |
| `EVT-09` | Microsoft Azure Architecture Center, [Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) | Updated 2026-03-28 | Intent-rich append-only events, replay, projections, snapshots, concurrency, and explicit complexity/migration warnings. | Cloud architecture guidance; not evidence that event sourcing should be universal or used here. |
| `EVT-10` | XTDB, [Time in XTDB](https://docs.xtdb.com/about/time-in-xtdb.html) | Current docs inspected 2026-09-04 | System time versus valid time, late-arriving knowledge, and retroactive correction. | Vendor-specific implementation; editorial work may require more named times than bitemporality alone. |

## Representation, targeting, and provenance

| ID | Source | Version/date | Used for | Limitation |
|---|---|---:|---|---|
| `REP-01` | W3C, [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) | Recommendation, 2017 | Body/target separation, motivations, SpecificResource, text quote/position selectors, and source-state binding. | Does not define editorial obligations, causal history, release authority, or stable identity through every rewrite. |
| `REP-02` | W3C, [PROV-DM](https://www.w3.org/TR/prov-dm/) and [PROV-O](https://www.w3.org/TR/prov-o/) | Recommendations, 2013 | Entity, Activity, Agent, usage, generation, derivation, revision, attribution, association, and responsibility. | Domain-neutral provenance; no native editorial adjudication or obligation semantics. |
| `REP-03` | ProseMirror, [Guide](https://prosemirror.net/docs/guide/) | Current docs inspected 2026-09-04 | Immutable document states, transactions, steps, mapping, rebasing, and the limits of raw positional addresses. | Editor-state model, not durable cross-system provenance or storage history. |
| `REP-04` | Tree-sitter, [Advanced Parsing](https://tree-sitter.github.io/tree-sitter/using-parsers/3-advanced-parsing.html) | Current docs inspected 2026-09-04 | Incremental tree updates and the distinction between updated syntax ranges and externally persisted node identity. | Parser nodes/ranges are not durable semantic IDs across arbitrary rewrites. |
| `REP-05` | Yjs, [Relative Positions](https://docs.yjs.dev/api/relative-positions) | Current docs inspected 2026-09-04 | Relative positions that remain associated with context through collaborative edits. | Requires Yjs document history; resolution can fail after deletion and does not establish editorial meaning. |
| `REP-06` | Automerge, [Document history and heads](https://automerge.org/docs/reference/documents/heads/) and [stable cursors](https://automerge.org/docs/reference/documents/cursors/) | Current docs inspected 2026-09-04 | Change DAGs, branch heads, mergeable histories, and stable relative cursors. | CRDT convergence does not decide truth, authority, waiver, or acceptable prose. |
| `REP-07` | IETF, [RFC 8785 — JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785.html) | 2020 | Evidence that cryptographic hashing requires a defined invariant representation rather than generic “sorted JSON.” | The Phase 2 validator intentionally does not implement JCS; production canonicalization remains open. |
| `REP-08` | SLSA, [Provenance v1.2](https://slsa.dev/spec/v1.2/provenance) | Approved, current 2026 | Verifiable information about where, when, and how artifacts were produced. | Software supply-chain provenance; editorial provenance requires additional domain semantics. |
| `REP-09` | in-toto Attestation Framework, [Link predicate v0.3](https://github.com/in-toto/attestation/blob/main/spec/predicates/link.md) | Inspected 2026-09-04 | Step name, command, materials, products/subjects, environment, and byproducts as a precedent for reproducible operation evidence. | Software-supply-chain step model; not a complete editorial transaction ontology. |

## Checkpoints, history, and candidate substrates

| ID | Source | Version/date | Used for | Limitation |
|---|---|---:|---|---|
| `HIST-01` | Git, [Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) | Pro Git 2nd ed. | Content-addressed blobs, trees, commits, parents, exact checkpoints, and broad interoperability. | Git commits do not natively express semantic editorial transactions, temporal facts, or efficient domain queries. |
| `HIST-02` | Dolt, [Getting Started — Git for Data](https://docs.dolthub.com/introduction/getting-started/git-for-data) | Current docs inspected 2026-09-04 | Versioned relational tables, commits, branches, merges, and SQL access. | Row identity and meaning depend on schema/primary keys; semantic operations are not automatic. |
| `HIST-03` | Dolt, [System Tables](https://docs.dolthub.com/sql-reference/version-control/dolt-system-tables) | Current docs inspected 2026-09-04 | Queryable logs, diffs, commit history, and row-level historical views. | Database diffs remain lower-level than editorial intent and adjudication. |
| `HIST-04` | PostgreSQL, [Logical Decoding](https://www.postgresql.org/docs/current/logicaldecoding.html) | PostgreSQL 18 docs inspected 2026-09-04 | Persistent row-change streams and a possible projection/outbox substrate. | Old-row detail and identity depend on replica identity/schema; application semantics remain external. |
| `HIST-05` | Zed, [“Software Is Made Between Commits”](https://zed.dev/blog/introducing-deltadb) | 2026-06-11 | Fine-grained deltas, stable edit identity, conversation linkage, and arbitrary history branch points as design prior. | Vendor account; no stable independently testable general-purpose storage/API contract was available. |
| `HIST-06` | Zed, [“Introducing Delta”](https://zed.dev/blog/introducing-delta) | 2026-08-12 | Delta as the first DeltaDB client, private-beta maturity, Git coexistence, and real-time replicated worktrees. | Client access does not establish durability, portability, deployment, licensing, or suitability for J-Editorial. |

## Security, authority, privacy, and erasure

| ID | Source | Version/date | Used for | Limitation |
|---|---|---:|---|---|
| `SEC-01` | OWASP, [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Inspected 2026-09-04 | Documents, comments, issues, web pages, and retrieved content as indirect-injection surfaces; separation, validation, monitoring, least privilege, and human controls. | Practical guidance; no defense eliminates prompt injection. |
| `SEC-02` | OWASP, [AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) | Inspected 2026-09-04 | Least privilege, untrusted external content, structured outputs, separate decision/execution, and prohibition on model-only authorization. | General guidance requiring product-specific threat modelling and tests. |
| `SEC-03` | European Union, [GDPR Article 17](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Regulation (EU) 2016/679 | Erasure as a design constraint that can conflict with immutable history and exact replay. | Applicability and exceptions require legal analysis for a specific deployment; this research does not provide legal advice. |
| `SEC-04` | NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) and [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | AI RMF 1.0 / NIST AI 600-1 | Lifecycle governance, testing/evaluation, provenance, monitoring, incident handling, and human accountability. | Voluntary cross-sector guidance, not a complete control set for this product. |

## Pinned Amnesia evidence

The following sources are private. The repository/path/ref/hash tuple is the reproducibility reference. The fixture copies only bounded observations and a synthetic correction candidate, not the private files.

| ID | Repository/path | Immutable ref or blob | Supported observation |
|---|---|---|---|
| `AMN-01` | `jjjjguevara/amnesia-docs/src/content/docs/api/reference/commands-notes.md` | commit `5d8aa677793cc2b4734106bb21e6118f0cc5a2aa`; blob `1cda5daf0f96cde966d18b4e9da640d1a27ca084` | Page asserts `readiness: shipped`, `parity: full`, simplified notes signatures, and async-only behavior. |
| `AMN-02` | `jjjjguevara/amnesia-docs/src/content/docs/api/reference/capabilities.md` | same commit; blob `e4481fb82b03e558fc4c7d7ef936fdf141c2fe76` | Page documents the capability hierarchy and declares `expandCapabilities(...): Capability[]`. |
| `AMN-03` | `jjjjguevara/amnesia-docs/src/content.config.ts` | same commit; blob `46d2c7b876f47528cdfda7220fd2b3ff8754ba68` | Readiness/parity fields are typed, but comments state parity enforcement is not implemented. |
| `AMN-04` | `jjjjguevara/amnesia/apps/amnesia/src/api/types.ts` | commit `4d0d1efec4ee4958db504cb56bcf47dfbc19b92a`; blob `b225ec17f9ddc9b2476829280b2819f83e9530ef` | Public notes interface requires `bookId` for reads and declares several synchronous returns. |
| `AMN-05` | `jjjjguevara/amnesia/apps/amnesia/src/api/facades/notes.ts` | same commit; blob `1a460e0eb7e4cd01730116cc3d2580c0be7424e5` | Runtime facade implements the product signatures, capability checks, and event emissions. |
| `AMN-06` | `jjjjguevara/amnesia/apps/amnesia/src/api/security/capabilities.ts` | same commit; blob `0182fc05febfd09eb3148edea51509c373a1109f` | `expandCapabilities` returns `Set<Capability>` and applies the documented hierarchy. |
| `AMN-07` | `jjjjguevara/amnesia/apps/amnesia/src/api/api.ts` | same commit; blob `d35376b93cc1b0b08ff9ad3ce59c4d795b40f417` | Root API composition wires notes and capability-scoped instances. |
| `AMN-08` | `jjjjguevara/amnesia-docs` history for `commands-notes.md` | creation commit `af99eaed8dafee509abe6905aed85c8406219cbd`, 2026-06-28 | The page entered history in the first-release API documentation commit, whose message claimed the shipped set was proven and that the site build passed. |
| `AMN-09` | `jjjjguevara/amnesia` history for `notes.ts` | path commit `01e28c77897332f232431cbb876f4d78405f4e33`, 2026-02-25 | The product notes facade predates the documentation page at the inspected history boundary. |
| `AMN-10` | GitHub Actions run `33239050109`, job `99065086589` | `amnesia-docs@5d8aa677793cc2b4734106bb21e6118f0cc5a2aa` | GitHub reports a failed Docs Deploy build job. Step details were empty and the decoded job log was unavailable, so this run establishes failure status but not cause. |

## Evidence exclusions

This phase did not:

- clone or build the private Amnesia repositories in an isolated authenticated checkout;
- rerun the existing docs workflow, because that workflow can proceed to Cloudflare deployment;
- assert why the existing workflow failed;
- modify Amnesia, Amnesia Docs, Doc Doctor, or their histories;
- select an event store, database, CRDT, serialization, or canonical hash format;
- inspect, construct, label, split, transform, or train on a model-training dataset.
