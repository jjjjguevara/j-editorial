# Phase 3 results

Verdict: **pass-with-constraints for the executed probes**. No physical architecture
or general editorial-quality conclusion follows. Source IDs resolve in
[SOURCE-LEDGER.md](SOURCE-LEDGER.md); observations resolve to
[behavioral-probes.json](results/behavioral-probes.json).

## 1. Method and falsification targets

The unchanged Phase 2 technical and prose fixtures provide 13 and 22 transaction
heads. The experiment attempts to break their declared integrity, then compares
four information-preserving encodings using an executable causal reducer.

The targeting experiment uses exact source fragments from three real About-page
checkpoints and one API-reference checkpoint. Historical label removal and rewriting
are distinguished from deliberately generated move/duplicate/delete/split cases.
The latter are experimental inputs, not alleged historical edits or preference labels.

Native Git and SQLite probes test specific mechanisms. They do not stand in for
Dolt, PostgreSQL, a temporal database, CRDT or DeltaDB deployments. No performance
ranking is inferred from a small serialization-size comparison.

Falsifiers include an invalid reference accepted by the strengthened guard, a
causally impossible fluent, a roundtrip changing data, shuffled storage changing
state, conflict silently resolved by order, an ambiguous anchor guessed as unique,
a failed transaction exposing half its writes, or tampering remaining undetected.

## 2. Eight legacy-validator blind spots

Each original validator accepts all four mutations below. The added semantic guard
rejects each while continuing to accept the original fixtures.

| Mutation | Technical original | Prose original | New guard |
|---|---|---|---|
| Unknown transaction actor | accepts | accepts | rejects both |
| Fluent ends before its initiating transaction | accepts | accepts | rejects both |
| Material effect references a missing checkpoint | accepts | accepts | rejects both |
| Fluent references an undeclared subject | accepts | accepts | rejects both |

This is negative evidence against treating the earlier validator passes as a full
semantic-validity proof. Earlier outputs are preserved unchanged. The new guard
adds identity lookup, causal reachability, checkpoint references and subject
registration; it does not claim general schema validation or authentication.

An existing actor ID is not authenticated identity. These fixtures do not prove
that a caller may impersonate a named owner, nor implement a production permission
system. That remains a security gate. A finding recorded by an allowed observer
still does not become true merely because the event passes integrity checks.

## 3. Representation alternatives

All four alternatives retain the same input information and reconstruct computed
state at every original transaction head: **35 heads × 4 encodings = 140 compared
head states**. Both histories also remain invariant under shuffled storage order.

| Encoding | Technical bytes | Prose bytes | Preserved requirement |
|---|---:|---:|---|
| Event-first | 9,530 | 27,784 | Events and contextual records |
| Fact-first | 10,761 | 30,913 | Effect facts plus transaction envelopes, including zero-effect occurrences |
| Event–fluent with cached head states | 17,083 | 57,164 | Events plus explicitly derived state copies |
| Checkpoint plus semantic journal | 9,544 | 27,798 | Material bindings and complete semantic journal |

These are compact JSON bytes for this implementation, not server storage costs,
write amplification measurements, compression ratios or production latency. The
larger event–fluent encoding deliberately materializes every head: its size is a
consequence of this cache policy, not an inherent defect of fluent semantics.

The fact-first comparison is not weakened by throwing away transactions. A separate
ablation shows that exporting only state-changing effect rows loses one technical
observation and three prose observations, including the synthetic reviewer dialogue.
Exporting only material-changing checkpoints loses ten technical and eighteen prose
transactions. Those losses indict the ablated exports, not every fact-oriented or
checkpoint-oriented architecture.

**Result:** the evidence constrains information preservation more strongly than
physical organization. No winner is selected. A shared reducer creates common-mode
risk: these roundtrips are not four independently implemented semantic engines.

## 4. Causal interpretation

The experimental reducer considers only ancestors of the requested head. At each
literal effect path it finds causally maximal writers. Incomparable conflicting
values remain an explicit conflict set; a causally later explicit adjudication may
override both. A sibling's disposition does not leak into another branch.

The synthetic disagreement probe preserves `accept` and `reject` concurrently,
then records `deferred` as a later decision. A separate temporal query demonstrates
that late knowledge can alter a present reconstruction of an earlier effective date
without changing the answer available at an earlier knowledge cutoff.

This is an executed reference interpretation, not a production reducer contract.
Aliases such as `findings.notes` and `finding:notes-signature` are interpreted
literally. A later ontology must define correspondence rather than rely on implicit
string similarity. Full predecessor precondition checking, authentication, arbitrary
schema migrations, and recomputation of all historical readiness labels remain open.

## 5. Target identity and fidelity

The actual About-page label removal shifts a preserved biography sentence. Reusing
its old raw-source position misses it; exact quote matching recovers it. The earlier
semantic rewrite removes a formerly present sentence. Quote matching reports
`unresolved`, not a fabricated identity link or a conclusion that the idea was deleted.

On both prose and API fragments, insertion and movement retain a unique quote;
duplication becomes ambiguous; deletion, rewriting and splitting become unresolved.
Bounded context resolves a constructed partial duplicate but correctly remains
ambiguous when the entire surrounding context is duplicated.

**Interpretation:** preserve checkpoint, projection identity, coordinate unit,
quote/context where permitted, structural/symbol hints, and an explicit resolution
outcome. Textual matching alone cannot justify semantic continuity across rewriting.
A future correspondence decision should retain who made it, the evidence and any
split/merge alternatives. This follows the separation of target identity, selectors
and source state in S01, with provenance distinctions from S03.

These probes use literal source fragments and Unicode-codepoint coordinates.
They are **not** W3C TextQuoteSelector conformance tests: the specification's
text normalization and markup processing are not implemented. They also do not
establish built HTML, DOM visibility, accessibility or full Astro/Markdown roundtrip.
Opaque syntax and hostile-looking text survive a JSON roundtrip as inert data;
this does not test an LLM's resistance to prompt injection (S08).

## 6. Native storage probes and negative evidence

Git stores and retrieves the exact fragment-manifest bytes. A single-reference
compare-and-swap rejects a stale expected object ID. Changing the current reference
still leaves the prior object retrievable. **Logical replacement is not erasure.**
These limited observations align with Git's reference mechanism (S02); they do not
establish atomic visibility of a multi-reference publication protocol.

SQLite receives one event row and one effect row inside an uncommitted transaction.
A child process exits abruptly before commit; reopening the database exposes neither
row. The committed control exposes both. A neutral JSON export recreates the two
rows in a fresh database, and modifying a sealed export changes its digest.
This is process-interruption evidence, not power-loss or hardware durability (S04).

With `secure_delete=OFF`, deleting a synthetic sentinel removes it from query
results but leaves its bytes in the database file. `VACUUM` removes that sentinel
from the current file scan. Backups, OS snapshots, storage-media remnants, replicas,
virtual tables and downloaded exports were not tested. S05 documents further
limits; neither this run nor that setting establishes a universal erasure guarantee.

## 7. Operational magnitudes and limits

The runner uses two existing histories, four bounded fragments, eight deliberate
integrity corruptions, four representations, 35 original heads, a tiny synthetic
causal example, and temporary native stores. It invokes no model, hosted database,
paid API or network resource. All 67 checks record actual and expected values.

Local execution used Python 3.13.5, Git 2.47.3 and SQLite 3.46.1. The initial CI
transport used Python 3.12.3, Git 2.55.0 and SQLite 3.45.1. CI reruns must compare
the stable experiment digest, retaining environment differences separately.
No throughput, tail-latency, scaling or total-cost recommendation follows.

## 8. Recommendation

Continue with explicit identity, causal relationships, context-qualified facts,
source bindings and versioned derived views. Retain all four physical organizations
until the same substantive workload is implemented in actual candidate substrates.
Prefer abstention to guessed target continuity. Separate integrity, semantic validity,
measurement validity and publication authority in every later gate.

The paired model remains worth investigating; the previous structural passes were
not strong enough to select its production realization. See the gate for remaining
build, reader, grader, migration, security and persistence obligations.
