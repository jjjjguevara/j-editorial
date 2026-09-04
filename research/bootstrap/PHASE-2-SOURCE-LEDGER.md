# Bootstrap phase-2 source ledger

Status: **research evidence / no architectural authority**  
Research cutoff: **2026-09-04**  
Scope: D-02 semantic-center research, D-03 implications, D-04 comparator evidence, and the Amnesia technical-slice audit  
Dataset research: **not executed**

This ledger extends, rather than replaces, [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md). Primary and official sources are preferred. A source establishes only the claim listed; it does not make its model a J-Editorial dependency.

## 1. Gustavo Bueno and the gnoseological space

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `GB-01` | [Gustavo Bueno, *Teoría del cierre categorial*](https://www.fgbueno.es/gbm/gb1996ks.htm), Fundación Gustavo Bueno | 1996 overview | Defines the three axes and nine figure families; describes sciences as heterogeneous bodies not reducible to written propositions. | Condensed exposition of a multi-volume philosophical theory; scoped to positive sciences. |
| `GB-02` | [Gustavo Bueno, *¿Qué es la ciencia?*](https://fgbueno.es/gbm/gb1995qc.htm) | 1995 | Establishes the theory's object and constructivist account of science. | Does not provide an editorial ontology. |
| `GB-03` | [Gustavo Bueno, “Cierre categorial”](https://www.fgbueno.es/med/tes/t024.htm) | 2010 | Clarifies closure under operations and the plurality of scientific categories. | Introductory audiovisual transcription; not a transfer rule for publication workflows. |
| `GB-04` | [Gustavo Bueno, “Idea de Hecho (b)”](https://www.fgbueno.es/med/tes/t042.htm) | 2010 | Treats scientific facts as participating across syntactic, semantic, and pragmatic figures and emphasizes operation, referent, perspective, structure, and norm. | Concerns scientific facts; editorial “facts” require independent analysis. |
| `GB-05` | [Evaristo Álvarez Muñoz, “El cierre categorial e historia interna de la ciencia…”](https://www.fgbueno.es/bas/bas242a.htm) | *El Basilisco* 42, 2011 | Shows the expected feedback between general gnoseology and special field reconstruction. | A special study in geoscience, not writing studies. |

## 2. Provenance, annotation, constraints, policy, and text

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `STD-01` | [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) and [PROV-O](https://www.w3.org/TR/prov-o/) | W3C Recommendations, 2013 | Entity, Activity, Agent, generation, usage, derivation, revision, attribution, association, delegation, and provenance bundles. | Domain-neutral provenance; no editorial obligations or release model. |
| `STD-02` | [W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/) | W3C Recommendation, 2017 | Annotation Body/Target/Motivation, resource state, SpecificResource, selectors, and segment targeting. | Does not define version history, adjudication, or normative force. |
| `STD-03` | [W3C Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/) | W3C Recommendation, 2017 | Separates data/shape graphs from validation reports; result records identify focus node, severity, source component, shape, path, and value. | Best for machine-executable graph constraints; not a theory of prose adequacy. |
| `STD-04` | [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/) | W3C Recommendation, 2018 | Distinguishes Policy, Party, Asset, Action, Permission, Prohibition, Duty, and Constraint. | Designed for content/service usage policy, not general editorial quality. |
| `STD-05` | [TEI P5, “Non-hierarchical Structures”](https://tei-c.org/release/doc/tei-p5-doc/en/html/NH.html) | P5 4.12.0, 2026-07-28 | Documents conflicts among physical, rhetorical, linguistic, and analytic hierarchies and stand-off markup trade-offs. | TEI/XML-specific implementation context. |
| `STD-06` | [TEI P5, “Certainty, Precision, and Responsibility”](https://tei-c.org/release/doc/tei-p5-doc/en/html/CE.html) | P5 4.12.0, 2026-07-28 | Structured uncertainty, precision, attribution, and responsibility precedent. | Encoding vocabulary, not an editorial lifecycle. |

## 3. Bibliographic, archival, event, assertion, and discourse models

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `STD-07` | [IFLA Library Reference Model](https://repository.ifla.org/handle/20.500.14598/40) | IFLA LRM, approved 2017; repository version updated 2025 | High-level distinction among bibliographic entities and linked-data-oriented conceptual modelling. | Bibliographic discovery model; does not model fine-grained editing. |
| `STD-08` | [LRMoo](https://cidoc-crm.org/lrmoo) | official 1.0 approved 2024; 1.1.1 published 2025 | Aligns IFLA LRM semantics with CIDOC CRM's object/event orientation. | Broad cultural-heritage ontology; too heavy to assume as product core. |
| `STD-09` | [CIDOC CRM last official release](https://cidoc-crm.org/get-last-official-release) | official 7.1.3, 2024-02 | Event-centric integration precedent for heterogeneous facts, actors, objects, and temporal entities. | Cultural-heritage scope and implementation complexity. Later working versions are not the last official release. |
| `STD-10` | [ICA Records in Contexts — Conceptual Model](https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-conceptual-model/) | RiC-CM 1.0, 2023 | Connects record resources, agents, and activities and replaces a single hierarchical descriptive assumption with contextual relations. | Archival description, not prospective editorial evaluation. |
| `STD-11` | [ICA Records in Contexts — Ontology](https://www.ica.org/ica-network/expert-groups/egad/records-in-contexts-ontology/) | RiC-O 1.1, 2025-05 | Formalizes RiC-CM; strengthens record resource, instantiation, and agent distinctions. | RDF/OWL implementation is evidence, not a required J-Editorial stack. |
| `STD-12` | [Nanopublication Guidelines](https://nanopub.net/guidelines/working_draft/) | community working draft, inspected 2026-09-04 | Separates assertion, assertion provenance, and publication information; accommodates claims, hypotheses, negative results, and opinions. | Working draft and assertion-centric model; not an edit/history system. |
| `STD-13` | [Werner Kunz and Horst Rittel, *Issues as Elements of Information Systems*](https://escholarship.org/uc/item/1sc9p189) | Working Paper 131, 1970 | IBIS precedent for issue, position, argument, and decision discourse around ill-structured problems. | Design/planning discourse model; not artifact representation. |
| `STD-14` | [Modgil and Prakken, “On logical specifications of the Argument Interchange Format”](https://doi.org/10.1093/logcom/exs033) | *Journal of Logic and Computation* 23(5), 2013 | AIF as an interlingua for information nodes and inference/conflict/preference scheme applications. | Argumentation semantics, not editorial lifecycle or source fidelity. |
| `STD-15` | [RO-Crate Metadata Specification 1.3](https://www.researchobject.org/ro-crate/specification/1.3/) | Recommendation, 2026-06-22 | Packages data and contextual entities with stable identifiers, profiles, provenance, actions, instruments, inputs, results, and status. | Research-object packaging and interchange; not an ontology of editorial judgment. |

## 4. Delta and history comparator

| ID | Source | Version/date | Use | Limitation |
|---|---|---|---|---|
| `HIST-08` | [Zed, “Software Is Made Between Commits”](https://zed.dev/blog/introducing-deltadb) | 2026-06-11 | Vendor description of DeltaDB operation-level deltas, stable identities, conversation linkage, CRDT worktrees, and between-commit branch points. | Vendor claim; no independently accessible stable storage/API contract was established in this run. |
| `HIST-09` | [Zed, “Introducing Delta”](https://zed.dev/blog/introducing-delta) | 2026-08-12 | Establishes Delta as the first DeltaDB client, private-beta status, Git coexistence, real-time replication, and code/conversation review model. | Product announcement and private beta; client access does not prove backend suitability. |
| `HIST-10` | [DeltaDB Early Access](https://zed.dev/deltadb) | inspected 2026-09-04 | Current public capability claims: rewind to operations, stable edit identity, conversation trace, arbitrary branch points. | Marketing/early-access page; no benchmark or durability evidence. |

## 5. Amnesia repository evidence

Private repository evidence is pinned for reproducibility within authorized environments. It cannot be independently inspected by unauthenticated reviewers.

| ID | Source | Ref | Supported observation |
|---|---|---|---|
| `AMN-01` | `jjjjguevara/amnesia-docs` README and tree | `5d8aa677793cc2b4734106bb21e6118f0cc5a2aa` | Astro/Starlight documentation source, API section location, and repository structure. |
| `AMN-02` | `amnesia-docs/src/content.config.ts` | same | Typed readiness/parity metadata; comments explicitly state that parity enforcement is not implemented. |
| `AMN-03` | `amnesia-docs/src/content/docs/api/overview.md` and `reference/index.md` | same | Documented API root and per-surface readiness distinctions. |
| `AMN-04` | `amnesia-docs/src/content/docs/api/reference/capabilities.md` | same | Six capabilities, hierarchy, non-sandbox framing, documented `expandCapabilities` signature, shipped/full claim. |
| `AMN-05` | `amnesia-docs/src/content/docs/api/reference/commands-notes.md` | same | Documented notes signatures, async claim, capabilities, events, and shipped/full claim. |
| `AMN-06` | `amnesia-docs/src/content/docs/api/reference/access.md` | same | Global/plugin handles, root shape, `connect()` contract, and explicit voluntary-scoping limitation. |
| `AMN-07` | `jjjjguevara/amnesia/apps/amnesia/src/api/security/capabilities.ts` | `4d0d1efec4ee4958db504cb56bcf47dfbc19b92a` | Actual hierarchy and `expandCapabilities` return type `Set<Capability>`. |
| `AMN-08` | `amnesia/apps/amnesia/src/api/types.ts` | same | Public `AmnesiaAPI`, command interfaces, events, capabilities, and notes signatures. |
| `AMN-09` | `amnesia/apps/amnesia/src/api/facades/notes.ts` and `api/api.ts` | same | Runtime notes facade, capability checks, event emission, synchronous reads, async writes/export, and root assembly. |

## 6. Evidence rules

- A standard supplies a tested distinction or pattern; it is not an implementation selection.
- Bueno's framework is used as an analytic comparator, not as authority to classify editorial work as positive science.
- A private-repository observation must include repository, path, and immutable ref.
- Documentation metadata is an assertion until supporting evidence is bound.
- Runtime code is not automatically the public product contract; source precedence must be explicit.
- A vendor beta claim cannot satisfy a durability, security, performance, or licensing requirement without independent evidence.
- No source in this ledger authorizes model-training corpus acquisition, transformation, labeling, splitting, or training.
