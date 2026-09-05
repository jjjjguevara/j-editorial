# Bootstrap decision addendum — 2026-09-04

Status: **partial owner decisions / research-only authority / implementation blocked**  
Controlling gate: **`ADVERSARIAL-REVIEW-REQUIRED`**  
Dataset-research execution: **held**  
Applies to: `BOOTSTRAP.md`, PR #1, and the phase-1 bootstrap packet

This addendum records the owner's response to D-01 through D-04 and the research consequences that can be applied without making the unresolved choices implicitly. It is not an ADR, schema, storage decision, implementation authorization, or release of the bootstrap gate.

## 1. Decision status

| Decision | Owner direction | Status | Binding consequence |
|---|---|---|---|
| `D-01` — first end-to-end proof | Choose **C**, a paired technical-reference and general-prose proof. Use `jjjjguevara/amnesia-docs` as the first technical-reference use case. | **Accepted direction; one fixture identity remains open** | The first proof must exercise the same editorial semantics across two unlike artifact classes. The technical half is Amnesia API documentation. The prose half requires an explicit artifact and goal contract before fixture work begins. |
| `D-02` — semantic center | The original choice is premature. Research Gustavo Bueno's *Teoría del Espacio Gnoseológico* and additional approaches before choosing. | **Research further** | No single ontology root—`Gap`, `Finding`, `Obligation`, or `Event`—may be selected. Phase 2 must separate the analytic frame from the canonical record grammar and compare credible alternatives. |
| `D-03` — representation authority | Likely closer to option C and possibly three-layered, but dependent on D-02. | **Deferred; C-leaning hypothesis only** | Source, semantic, and derived-projection authority must be distinguished in research. This does not authorize three databases, services, stores, or persistence layers. |
| `D-04` — minimum history guarantee | Choose **B for now**, given current access to the Delta client rather than a separately usable DeltaDB interface. | **Provisionally accepted** | The first proof must retain meaningful proposed, accepted, rejected, and failed editorial operations plus checkpoints, without requiring every keystroke. The guarantee is backend-neutral and must be revisited if finer-grained history becomes testable. |

## 2. D-01 interpretation

Option C is not satisfied by running two versions of the same technical-document fixture. The paired proof must expose both:

1. **technical-reference semantics**, where many claims can be checked against executable product evidence; and
2. **general-prose semantics**, where audience, framing, rhetoric, evidence sufficiency, ambiguity, and adjudication cannot be reduced to API parity.

The Amnesia half is further scoped in [`AMNESIA-DOCS-SLICE-AUDIT.md`](../programs/amnesia/AMNESIA-DOCS-SLICE-AUDIT.md). The identity of the prose artifact remains a pivotal owner decision because it determines its purpose, rights, audience, evidence sources, and acceptable editorial outcomes.

## 3. D-02 research result

The initial D-02 alternatives conflate two different decisions:

- an **analytic coordinate system** for asking whether the model has omitted operations, referents, actors, dialogue, or norms; and
- a **canonical record grammar** for persisted editorial facts and assertions.

Bueno's gnoseological space is useful as the first kind of construct. It does not itself provide an editorial data model, and categorical closure must not be equated with publication or release readiness. Comparative work against PROV, Web Annotation, SHACL, ODRL, TEI, IFLA LRM/LRMoo, CIDOC CRM, ICA Records in Contexts, nanopublications, IBIS/AIF, and RO-Crate supports a provisional plural typed grammar rather than a universal `Gap` root.

The complete reasoning, counterexamples, and revised decision are in [`D-02-SEMANTIC-CENTER-REVIEW.md`](../programs/frame-domain/D-02-SEMANTIC-CENTER-REVIEW.md).

## 4. D-03 research boundary

A defensible working distinction is among three **authority concerns**:

1. **artifact/source-state authority** — what representation existed at a pinned state;
2. **editorial-semantic authority** — goals, norms, assertions, findings, evidence, actors, operations, and decisions;
3. **derived-projection authority** — renderings, indexes, scores, evaluations, readiness summaries, and reports.

This is a research hypothesis close to option C, not an accepted architecture. Mappings can be stale, partial, conflicting, or ambiguous and must retain provenance. D-03 remains blocked by the revised D-02 decision and representation experiments.

## 5. D-04 interpretation

The provisionally accepted first-slice guarantee is:

```text
meaningful editorial operation
  + actor and authority
  + target and pre-state
  + goal/norm/evidence context
  + proposal/acceptance/rejection/failure state
  + verification and outcome
  + resulting checkpoint when materialized
```

It explicitly does **not** require continuous capture of cursor movement or every text delta. It also does not select Git, Dolt, PostgreSQL, DeltaDB, a CRDT, or event sourcing.

Zed's current public Delta/DeltaDB materials are relevant comparator evidence because they claim operation identity, between-commit history, conversation linkage, and arbitrary branch points. Access through the Delta client does not yet establish a stable, independently testable storage API for J-Editorial. DeltaDB therefore remains a comparator and possible future experiment, not the reason for the domain guarantee.

## 6. Documents deliberately not rewritten yet

`BOOTSTRAP.md`, `ROADMAP.md`, `RESEARCH.md`, and the held model-training-data charter should be revised as one consistent controlling-document change only after:

- the revised D-02 research hypothesis is accepted or narrowed;
- the D-01 prose companion is identified;
- the Amnesia oracle boundary is authorized; and
- D-03 is narrowed enough to state representation research requirements without implying architecture.

Partial owner decisions are recorded here so they cannot be lost, while unresolved decisions remain visible rather than being silently filled in.

## 7. Current halt questions

The exact remaining owner questions and answer format are maintained in [`OWNER-DECISIONS.md`](OWNER-DECISIONS.md).

No answer by itself authorizes implementation, dataset research, an ADR, a persistence selection, or a merge.
