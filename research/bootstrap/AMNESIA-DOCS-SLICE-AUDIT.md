# Amnesia Docs technical-slice audit

Status: **candidate technical half of D-01C / research fixture only**  
Documentation repository: `jjjjguevara/amnesia-docs`  
Documentation ref inspected: `5d8aa677793cc2b4734106bb21e6118f0cc5a2aa`  
Product repository: `jjjjguevara/amnesia`  
Product ref inspected: `4d0d1efec4ee4958db504cb56bcf47dfbc19b92a`  
Research cutoff: **2026-09-04**  
Dataset research: **not executed**

Source identifiers resolve in [`PHASE-2-SOURCE-LEDGER.md`](PHASE-2-SOURCE-LEDGER.md).

## 1. Result

`amnesia-docs` is a strong technical-reference proof, but it is not the OpenAPI scenario assumed in phase 1. It documents a typed Obsidian-plugin API whose authority is distributed across TypeScript interfaces, exported symbols, runtime assembly, capability facades, tests, and Markdown pages. [AMN-01 through AMN-09]

That distribution is valuable for J-Editorial because it creates a real cross-representation editorial problem:

```text
published documentation claims
        ↕
front-matter readiness/parity claims
        ↕
public TypeScript contract
        ↕
runtime wiring and capability checks
        ↕
behavioral tests and observed execution
        ↕
human judgment about explanation and safe framing
```

No one layer is automatically sufficient ground truth.

## 2. Why this is a better stress case than synthetic OpenAPI

The API root exposes version, state, commands, events, hooks, UI extension points, and `connect()`. Individual surfaces have different readiness labels. The capability mechanism is intentionally described as accident prevention and voluntary scoping rather than a security sandbox. [AMN-03, AMN-04, AMN-06]

This yields obligations that are:

- deterministic: member existence, method name, parameter shape, return type, optionality, event payload, capability hierarchy;
- behavioral: facade wiring, emitted event, error behavior, async boundary, runtime availability;
- documentary: readiness, parity, experimental/stable distinction, source version, deprecation;
- interpretive: whether limitations and security posture are explained honestly enough for a developer to act safely.

The slice therefore tests the boundary between executable evidence and editorial judgment without requiring an invented benchmark corpus.

## 3. Initial bounded surface

The recommended first technical sub-slice is:

```text
API root and access
+ capability vocabulary and hierarchy
+ commands.notes
```

This is bounded enough for a first experiment and already crosses public types, runtime facades, permissions, event emission, documentation, examples, and readiness metadata. It must remain possible to replace the sub-slice if authoritative source access or build reproducibility fails.

## 4. Authority chain to test

The fixture must pin every source rather than following moving branch names.

| Evidence class | Candidate authority | Limitation |
|---|---|---|
| Documentation state | Pinned `amnesia-docs` source files and built output | A page can claim parity without enforcement. Built output can differ from source through config/plugins. |
| Public type contract | Pinned exports and `AmnesiaAPI`/command interfaces in `amnesia` | Types do not prove runtime wiring or behavior. Internal types may not equal supported public exports. |
| Runtime composition | `createAPI`, facades, global/plugin exposure | Wiring does not prove behavior across environments. |
| Capability behavior | hierarchy, expansion, `requireCapability`, scoped facades | The mechanism is not a sandbox and can be bypassed through the admin/global path. |
| Behavioral evidence | focused tests and reproducible execution | Tests can be incomplete, stale, skipped, or test a different build. |
| Release/readiness evidence | labels, release records, accepted decisions | Labels are policy claims, not self-validating facts. |
| Human evaluation | task completion, clarity, risk communication | Reviewer judgment can disagree and requires audience/authority records. |

Conflicts must be preserved as findings. The framework must not silently declare code, tests, or prose universally superior. Source precedence belongs in the goal contract and may differ by obligation.

## 5. Concrete parity findings

The audit found real mismatches suitable for the evaluation fixture. These are observations at the pinned refs, not patches authorized for either repository.

### AMN-F01 — `commands.notes` signatures and synchrony disagree

The documentation marks `commands.notes` as `readiness: shipped` and `parity: full`, says all methods are asynchronous, and documents signatures such as `create(note)`, `delete(id)`, `getNotes()`, and `getNote(id)`. [AMN-05]

The pinned public interface and facade instead expose forms including:

- `create(bookId, location, content, options?)`;
- `update(noteId, updates)`;
- `delete(bookId, noteId)`;
- `getNotes(bookId)`;
- `getNote(bookId, noteId)`;
- `getNoteForHighlight(bookId, highlightId)`;
- `exportNotes(bookId, format)`.

Several reads are synchronous in the interface/facade rather than Promise-returning. [AMN-08, AMN-09]

This single case can test:

- deterministic signature comparison;
- the difference between method existence and full parity;
- false or stale readiness metadata;
- finding severity and grouping;
- source-version conflicts;
- a corrective operation and post-edit verification;
- human review of whether examples remain understandable.

### AMN-F02 — `expandCapabilities` return type disagrees

The capabilities page documents:

```ts
expandCapabilities(capabilities: Capability[]): Capability[]
```

The pinned implementation returns `Set<Capability>`. The six-token vocabulary and hierarchy otherwise substantially align. [AMN-04, AMN-07]

This case tests partial correctness: a page can be correct about policy semantics while incorrect about a callable signature. A binary page-level pass/fail would erase that distinction.

### AMN-F03 — parity metadata is typed but not enforced

The content collection defines typed `readiness` and optional `parity` fields, but its own comments state that this is a documented convention and that the machine-enforced parity linter remains held behind another ADR. [AMN-02]

Consequently:

- `parity: full` is an assertion by the editorial workflow;
- it is not an executable proof;
- the assertion needs provenance and target obligations;
- a checker may produce contradictory evidence;
- release policy must define whether contradiction blocks publication or merely reopens review.

### AMN-F04 — documentation and product histories are independent

The two repositories have separate commits and timelines. A documentation commit cannot be evaluated against an unpinned `main`, and a product change can make the unchanged docs stale. A valid eval instance must bind both refs and record any source precedence or compatibility assumption.

## 6. Candidate goal contract

A bounded contract could state:

> At the pinned documentation and product revisions, an external Obsidian plugin developer can identify, connect to, and correctly call the supported notes API under the documented capability model, while understanding which controls are voluntary and which surfaces are not stable.

Candidate hard obligations:

1. every documented in-scope root member exists in the public contract and runtime assembly;
2. documented in-scope method names, required parameters, optional parameters, return values, and async behavior match the pinned public contract;
3. runtime facades implement the public interface and enforce the documented capability for gated methods;
4. documented event names and payloads match the event contract and emitted behavior;
5. every `shipped`/`full` claim has defined supporting evidence;
6. experimental, unavailable, or bypassable behavior is not represented as a security guarantee;
7. examples type-check or execute in the declared environment, or their non-executable status is explicit;
8. the documentation identifies the product/API version or pinned evidence state being described;
9. accepted exceptions and unverified claims remain visible;
10. a developer can complete the defined access-and-notes task without relying on undocumented knowledge.

## 7. Grader allocation

| Obligation | Primary grader | Secondary/adjudication |
|---|---|---|
| Symbol and member existence | parser/type checker | human review for intended public boundary |
| Signature and return parity | AST/type comparison | human review for overloads or adapters |
| Runtime wiring | focused integration test | maintainer adjudication |
| Capability hierarchy | deterministic graph/check | security review for claim framing |
| Event contract | type comparison + behavior test | maintainer adjudication |
| Example validity | type-check/build/run | human review for pedagogical quality |
| Readiness/parity support | policy rule over evidence | maintainer/release authority |
| Clarity and task completion | structured human task | disagreement retained; model judge only after meta-eval |
| Security language | deterministic forbidden-claim checks plus expert review | security authority |

Objective graders may establish contradiction or support for specific obligations. They cannot alone decide audience fitness, risk communication, or release acceptance.

## 8. History fixture under D-04B

A useful episode can be constructed from the real parity mismatch without treating either historical state as training truth:

1. import pinned docs and product states;
2. compile the goal contract into addressable obligations;
3. run signature/readiness checks;
4. record adverse and positive findings with exact targets and source refs;
5. propose one or more documentation operations;
6. retain reviewer disagreement or alternative valid edits;
7. accept, reject, or waive each operation under named authority;
8. materialize a candidate checkpoint;
9. rerun deterministic verification and human task review;
10. record resolved, residual, and newly introduced findings.

This is an architecture/evaluation fixture. It is not a training dataset, benchmark corpus, or authorization to alter Amnesia repositories.

## 9. Required oracle authorization

The objective oracle cannot come from `amnesia-docs` alone. Phase 2 needs an explicit boundary for using the private `jjjjguevara/amnesia` repository at pinned commits as authoritative product evidence, including whether a future J-Editorial research harness may read, build, type-check, and test it in CI.

Without that authorization, the technical slice can evaluate internal consistency of the docs but cannot substantiate API parity claims.

## 10. General-prose companion requirement

D-01C remains incomplete until a specific non-reference prose artifact is selected. The companion should contain at least:

- an identifiable audience and purpose;
- factual or interpretive claims with evidence questions;
- rhetorical/structural alternatives with more than one defensible answer;
- revision history or a bounded sequence that can be constructed without private personal data;
- rights to use it as a repository fixture;
- review authority capable of adjudicating without pretending preference is fact.

A Doc Doctor research article is available as a temporary integration fixture, but it is still technical/research prose and would weakly test generality. A real public-facing essay, article, case narrative, or explanatory piece is the stronger paired proof.

## 11. Acceptance criteria for the technical slice

The slice can pass its bootstrap research gate only if it demonstrates that J-Editorial can:

- bind and reproduce cross-repository evidence at immutable refs;
- decompose a goal into obligation-level checks;
- retain positive, adverse, uncertain, and disputed findings;
- distinguish source mismatch from documentation quality judgment;
- target claims through document movement or report ambiguity;
- record semantic operations plus checkpoints under D-04B;
- rerun deterministic checks and preserve raw results;
- retain an honest readiness decision with unresolved conditions;
- export the fixture without making the selected persistence backend mandatory;
- run without activating model-training dataset research.

Failure to obtain pinned product evidence, reproduce the build/tests, or define source precedence must return the slice for narrowing rather than being papered over with a model judge.
