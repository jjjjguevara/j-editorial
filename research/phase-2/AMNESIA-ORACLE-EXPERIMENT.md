# Amnesia oracle experiment — Phase 2 technical foundation

Status: **static evidence executed / runtime execution blocked by environment / no source mutation**  
Program: `BR-AMN`  
Authorization: `research/bootstrap/AMNESIA-ORACLE-AUTHORIZATION.md`  
Dataset research: **not executed**

Source identifiers resolve in [`SOURCE-LEDGER.md`](SOURCE-LEDGER.md).

## 1. Bound oracle

The experiment binds:

```text
Documentation:
  jjjjguevara/amnesia-docs
  commit 5d8aa677793cc2b4734106bb21e6118f0cc5a2aa

Product:
  jjjjguevara/amnesia
  commit 4d0d1efec4ee4958db504cb56bcf47dfbc19b92a
```

Moving branches were used only to confirm that these remain the current heads at the research cutoff. Every promoted observation below uses immutable commits and blob identities.

## 2. Bounded surface

```text
API root/access
+ capability vocabulary and hierarchy
+ commands.notes
```

This surface crosses:

- documentation source and metadata;
- public TypeScript interfaces;
- root runtime composition;
- a capability hierarchy;
- facade methods and event emissions;
- release/readiness assertions;
- user-facing examples and explanations.

## 3. Static findings

### AMN-P2-F01 — `commands.notes` signature and synchrony contradiction

The documentation at `AMN-01` declares:

- `readiness: shipped`;
- `parity: full`;
- all methods asynchronous;
- simplified forms such as `create(note)`, `getNotes()`, and `getNote(id)`.

The pinned public interface and facade at `AMN-04` and `AMN-05` instead include:

```text
create(bookId, location, content, options?) -> Promise<Note>
update(noteId, updates)                     -> Promise<Note>
delete(bookId, noteId)                      -> Promise<void>
getNotes(bookId)                            -> Note[]
getNote(bookId, noteId)                     -> Note | undefined
getNoteForHighlight(bookId, highlightId)    -> Note | undefined
searchNotes(query, bookId?)                 -> Note[]
exportNotes(bookId, format)                 -> Promise<string>
```

The static contradiction is high-confidence for the pinned source state. It does not, by itself, prove which product surface the maintainer intends to support in a later release.

Disposition in the research fixture:

```text
obligation:notes-signature-parity = unsatisfied
obligation:honest-readiness       = unsatisfied
release projection                = blocked
```

### AMN-P2-F02 — `expandCapabilities` return-type contradiction

The documentation at `AMN-02` declares:

```text
expandCapabilities(capabilities: Capability[]): Capability[]
```

The product implementation at `AMN-06` returns:

```text
Set<Capability>
```

The hierarchy itself substantially agrees. This demonstrates why page-level pass/fail is too coarse: one part of the page can be supported while a callable signature is contradicted.

### AMN-P2-F03 — typed metadata is not verification

`AMN-03` types the `readiness` and optional `parity` front-matter fields, but its comments explicitly state that parity enforcement is not implemented.

Therefore:

```text
parity: full
```

is an editorial assertion requiring evidence. It is not an executable proof.

### AMN-P2-F04 — publication claim and product evidence are temporally separable

The product notes-facade path traces to commit `01e28c77897332f232431cbb876f4d78405f4e33` on 2026-02-25. The documentation page entered history in commit `af99eaed8dafee509abe6905aed85c8406219cbd` on 2026-06-28.

At the inspected refs, the later documentation still contradicts the earlier product surface. This is useful evidence that:

- chronology does not establish parity;
- a commit message claiming a set is “proven” is not the same as bound proof;
- an accepted or published state can retain a latent contradiction;
- exact source, observation, and decision times must remain distinct.

This finding does not assign blame or infer the original review process.

## 4. Positive findings retained

The fixture also records support rather than only defects:

- the six-member capability vocabulary is represented in both docs and product;
- `write-annotations` implies `read-document` and `read-state` in both;
- notes writes use capability checks in the facade;
- notes mutation methods emit typed note events;
- root composition includes the notes facade;
- the documentation explicitly warns that capability scoping is not a security sandbox.

Positive evidence is retained independently from the adverse findings. It is not converted into an offsetting page score.

## 5. Runtime evidence attempt

The accepted AMN-01 boundary permits isolated checkout, dependency installation, build, type-check, focused tests, and CI reproduction. This execution environment could not complete that path:

- it had no authenticated local checkout of the private repositories;
- outbound DNS was unavailable in the container;
- the available connector can inspect repository source but does not mount a full private checkout;
- the existing `Docs Deploy` workflow can continue to Cloudflare deployment when secrets are present, so it was not re-run under research-only authority.

GitHub reports the current docs commit's `Docs Deploy` run `33239050109` as failed, with build job `99065086589` failed and later deploy/verification jobs skipped. Step summaries were empty and the decoded log was unavailable. The failure cause was therefore not established.

### Required next runtime command family

In an isolated authenticated checkout, with deployment disabled:

```bash
# amnesia-docs
npm ci
bash scripts/check-no-generated-output.sh
npm run build
# execute only the non-deploy regression checks from docs-deploy.yml

# amnesia
# install from the repository's pinned lockfiles and declared toolchain
# run the smallest public-API typecheck and focused notes/capability tests
```

The exact commands must be derived from each pinned repository's current package/task definitions in that environment. No workflow with deployment permission should be invoked merely to obtain build evidence.

## 6. Synthetic correction used only for model testing

The event–fluent fixture embeds a bounded corrected documentation fragment. It:

- changes the notes signatures to match the pinned interface;
- changes `parity` from `full` to `partial`;
- states that runtime and human-task evidence remain pending;
- is content-addressed by SHA-256;
- is never written to `amnesia-docs`.

The correction permits testing proposal, acceptance, materialization, verification, branch adjudication, and reopened staleness without crossing the source-mutation boundary.

## 7. Source-precedence rule

Precedence is obligation-specific:

| Obligation | Primary evidence | Why not universal |
|---|---|---|
| Public callable signature | exported public types, verified against build/export boundary | Types can be stale or internal rather than actually exported. |
| Runtime availability | root composition plus focused execution | Wiring alone can still fail at runtime. |
| Capability behavior | implementation and focused tests | Security framing also requires architectural review. |
| Event payload behavior | types plus emitted runtime behavior | Type declarations do not prove emission. |
| Release/readiness | policy plus bound supporting evidence and authority | Metadata cannot validate itself. |
| Developer usability | structured task and human review | Executable parity does not establish clarity. |

Conflicts are findings. The harness must not silently privilege code, docs, tests, or reviewer preference for every obligation.

## 8. Evidence state at this gate

| Obligation | Status |
|---|---|
| Docs/product refs pinned | **satisfied** |
| Static notes-signature comparison | **satisfied; contradiction found** |
| Static capability comparison | **satisfied; one contradiction and one positive match found** |
| Metadata-enforcement inspection | **satisfied; assertion is not enforced** |
| Docs history boundary | **satisfied** |
| Product history boundary | **partially satisfied** |
| Docs build reproduction | **not executed** |
| Product type-check/build | **not executed** |
| Focused runtime tests | **not executed** |
| Built-site/source equivalence | **not executed** |
| Human developer task | **not executed** |
| Source mutation | **prohibited and not performed** |

## 9. Gate result

`BR-AMN` passes its **static-foundation sub-gate** and supplies a valid seed for the event–fluent and representation/history experiments.

It does not pass the runtime or audience-usefulness gates. Any later claim of full API parity must remain blocked until isolated build/test and human-task evidence are captured.
