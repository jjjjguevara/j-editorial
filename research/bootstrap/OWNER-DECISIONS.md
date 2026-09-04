# Owner decisions required to continue bootstrap

Status: **partial owner decisions recorded / revised pivotal hold**  
Decision authority: **repository owner**  
Implementation gate: **remains closed**  
Dataset research: **held**

The 2026-09-04 owner response is preserved in [`BOOTSTRAP-DECISION-ADDENDUM.md`](BOOTSTRAP-DECISION-ADDENDUM.md). Phase-2 research has now narrowed the remaining choices.

## 1. Recorded decisions

| ID | Recorded direction | Status |
|---|---|---|
| `D-01` | **C** — paired technical-reference and general-prose proof; `jjjjguevara/amnesia-docs` is the first technical-reference use case. | Accepted direction; prose artifact unresolved. |
| `D-02` | Research further, including Gustavo Bueno's *Teoría del Espacio Gnoseológico* and other approaches. | Research completed to a new candidate hypothesis; owner choice required below. |
| `D-03` | Dependent on D-02; likely closer to split authority/three concerns. | Deferred. |
| `D-04` | **B for now** — semantic operations plus checkpoints; current access is to the Delta client, not a separately usable DeltaDB interface. | Provisionally accepted, backend-neutral. |

## 2. D-02R — Which hypothesis should govern phase-2 domain research?

The evidence in [`D-02-SEMANTIC-CENTER-REVIEW.md`](D-02-SEMANTIC-CENTER-REVIEW.md) shows that the original options conflated the analytic frame with the stored record grammar.

### A — Editorial Construction Space + typed plural records

Use a three-axis analytic scaffold—constructive, referential, and pragmatic/governance—to test completeness. In parallel, test distinct typed records for artifact state, goal, norm/obligation, assertion/finding, evidence, target, operation, agent/authority, decision/outcome, release, and episode.

`Gap` remains a derived adverse/unresolved view. `EditorialEpisode` is an analysis/replay envelope, not an event-sourcing commitment.

**Research recommendation: A.**

### B — No favored hypothesis yet

Continue comparative research with single-root, plural, and schema-neutral approaches equally open.

**Consequence:** avoids even provisional preference, but blocks stable representation and eval experiments and risks an unbounded bootstrap.

### C — Owner-specified alternative

State the alternative frame and which distinctions it must preserve or reject.

## 3. D-01P — What is the general-prose companion?

### A — Existing public-facing prose artifact

Use a real essay, explanatory article, case narrative, or other general-audience prose artifact from a repository controlled by the owner. Record the exact repository/path, audience, purpose, rights, evidence boundary, and review authority.

**Research recommendation: A.** It supplies the strongest counterweight to the technical API slice.

### B — Doc Doctor research article as a temporary fixture

Use `jjjjguevara/doc-doctor/docs/research/ui-ux/AI Editing Tool UI UX Research.md` initially.

**Consequence:** immediate integration evidence, but it remains technical/research prose and does not fully prove general editorial applicability.

### C — Purpose-built bounded prose fixture

Author a controlled article with deliberate evidence, structure, ambiguity, and alternative-rewrite cases.

**Consequence:** clean experimental controls, but synthetic adoption and history evidence.

## 4. AMN-01 — What product-evidence boundary is authorized?

The `amnesia-docs` slice cannot substantiate API parity from documentation alone. May phase-2 research use `jjjjguevara/amnesia` at pinned commits as authoritative product evidence, including repository read, local checkout, build, type-check, focused tests, and CI execution?

### A — Yes

Authorize those research-only operations against immutable refs. No product or docs mutation follows from this authorization.

**Research recommendation: A.**

### B — Read-only source inspection

Allow pinned source inspection but no build, test, checkout, or CI dependency.

**Consequence:** signature comparisons are possible, but runtime and example obligations remain unverified.

### C — No cross-repository oracle

Evaluate only internal consistency and editorial structure in `amnesia-docs`.

**Consequence:** the first technical proof cannot make objective product-parity claims and must be narrowed or replaced.

### Restricted

State exact repository, paths, refs, execution environments, data, or CI restrictions.

## 5. D-03 after D-02R

D-03 is intentionally not requested yet. After D-02R is answered, representation research must test three authority concerns without assuming three physical layers:

1. artifact/source state;
2. editorial-semantic records;
3. derived projections/evaluations.

A later D-03 packet will compare source-first, structured-first, split authority, and any hybrid produced by the experiments.

## 6. Answer format

```text
D-02R: A | B | C
D-01P: A + repository/path | B | C
AMN-01: A | B | C | Restricted: ...
Narrowing or additional constraint:
```

No answer releases the implementation gate, accepts an ADR, selects persistence, authorizes dataset research, or merges PR #1.
