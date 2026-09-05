# Causal event–fluent experiment — Amnesia notes trace

Status: **executed / pass for bounded research obligations**  
Program: `BR-EVENT-STATE`  
Fixture: [`fixtures/amnesia-notes-event-fluent.json`](fixtures/amnesia-notes-event-fluent.json)  
Validator: [`tools/validate_event_fluent_fixture.py`](tools/validate_event_fluent_fixture.py)  
Result: [`results/amnesia-notes-event-fluent-validation.json`](results/amnesia-notes-event-fluent-validation.json)  
Dataset research: **not executed**

Source identifiers resolve in [`SOURCE-LEDGER.md`](../../packets/2026-09-04-phase-2-foundations/SOURCE-LEDGER.md).

## 1. Question

Can one causal, identity-bearing editorial transaction affect several dimensions simultaneously while preserving:

- exact material checkpoints;
- continuing facts/fluents;
- observation versus truth;
- actor and authority;
- branch/concurrency semantics;
- multiple time dimensions;
- projection/reducer versions;
- erasure limitations?

## 2. Method

The fixture binds two real immutable repository states:

```text
amnesia-docs@5d8aa677793cc2b4734106bb21e6118f0cc5a2aa
amnesia@4d0d1efec4ee4958db504cb56bcf47dfbc19b92a
```

It uses the known `commands.notes.getNotes` contract mismatch as the seed observation. It then adds two explicitly marked research-only elements:

1. a synthetic corrected documentation checkpoint;
2. a counterfactual later product change used to test delayed observation and unchanged-document staleness.

No Amnesia repository was modified.

The validator is standard-library-only. It validates this research fixture, not a production schema. Its deterministic JSON digest is explicitly not claimed to implement RFC 8785.

## 3. Trace

```text
bind docs/product checkpoints + activate goal
                  │
                  ▼
        static contract check recorded
                  │
                  ▼
  one finding transaction changes five dimensions
      ├─ epistemic: adverse finding supported
      ├─ normative: obligations unsatisfied
      ├─ operational: remediation opened
      ├─ authority: disposition required
      └─ release: parity claim unsupported
         material state remains unchanged
                  │
                  ▼
      three sibling remedy proposals
      ├─ correct documentation
      ├─ change product
      └─ downgrade parity claim
                  │
                  ▼
   accept / reject / supersede under authority
                  │
                  ▼
 materialize synthetic docs checkpoint + verify
                  │
                  ▼
 multi-parent branch adjudication with residual risks
                  │
                  ▼
counterfactual product change learned later
      unchanged docs become stale again
                  │
                  ▼
 redaction retains identity/digest but degrades replay
```

## 4. Executed validation

Command:

```bash
python3 research/programs/event-state/tools/validate_event_fluent_fixture.py \
  research/programs/event-state/fixtures/amnesia-notes-event-fluent.json \
  --output research/programs/event-state/results/amnesia-notes-event-fluent-validation.json
```

Result:

```text
status: pass
transactions: 13
source bindings: 5
fluents: 3
projections: 4
fixture file sha256:
  cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82
deterministic research digest:
  4035f6f544c08e6c8878b0e0bbc0a2a696a48501feab0f1ea554ae74c4450e8c
```

The second digest is generated with sorted-key compact JSON for this experiment. It is not a production canonicalization commitment.

## 5. Results by D-03 obligation

| Test | Result | Evidence |
|---|---|---|
| `E-01` multidimensional atomic transition | **Pass** | `tx:record-finding` changes epistemic, normative, operational, authority, and release state in one transaction. |
| `E-02` unaffected dimensions | **Pass** | The finding transaction does not change material state; `tx:apply-docs` changes the docs checkpoint separately. |
| `E-03` event versus fluent | **Pass** | Three time-scoped fluents are initiated/terminated by identified transactions rather than conflated with the events. |
| `E-04` simultaneous roles | **Pass** | One finding participates in all three Editorial Construction Space axes and six semantic roles without identity duplication. |
| `E-05` branch and causal concurrency | **Pass** | Three sibling proposals share one causal parent; later adjudication has three parents. |
| `E-06` late knowledge | **Pass** | The counterfactual product change is effective on 2026-08-10, observed on 2026-08-12, and recorded seconds later; the docs checkpoint is unchanged. |
| `E-07` replay/projection versioning | **Pass** | Two reducer/projection versions produce different readiness outputs for the same `tx:verify` state head. |
| `E-08` external/nondeterministic evidence | **Pass** | The observation stores tool version, environment, raw-output digest, uncertainty, and abstentions. |
| `E-09` erasure | **Pass** | The redaction case retains permissible identity/digest and declares exact replay impossible and semantic replay partial. |
| `E-10` checkpoint fidelity | **Pass** | Every material source binds an immutable identity; the model forbids semantic replay from claiming byte reconstruction. |

## 6. What the pass establishes

The pass establishes that the candidate logical distinctions are internally coherent for this bounded technical fixture:

- an event transaction can be one causal act with several typed effects;
- one finding can carry several dimensions and relations;
- events and continuing conditions can coexist;
- exact material states and semantic states can coexist without treating them as separate incompatible “truth layers”;
- branch and merge semantics need causal parentage, not only a total sequence;
- projection version changes need not rewrite historical transactions;
- erasure can be represented honestly as loss of replay capability.

## 7. What the pass does not establish

The pass does not prove:

- that the event–fluent hybrid is the only or final architecture;
- that event sourcing should be used;
- that the fixture schema is production-ready;
- that the reducer semantics are complete;
- that the candidate can scale;
- that writes are durable or transactional in a selected backend;
- that target identities survive arbitrary real edits;
- that actual Amnesia builds/tests pass;
- that a human developer can complete the documented task;
- that the model generalizes to prose;
- that erased material can be reconstructed;
- that deterministic JSON serialization is cryptographically canonical;
- that any model-training data is valid.

## 8. Candidate-model comparison

| Model | E-01 | E-03 | E-05 | E-06 | E-07 | E-09 | E-10 | Result |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Pure event-first | strong | weak without a derived fluent model | medium with stream conventions | medium | difficult under reducer evolution | weak | weak unless checkpoints added | insufficient alone |
| Temporal fact/datom-first | strong | strong | medium unless causal transactions are explicit | strong | strong | medium | weak unless material checkpoints added | insufficient alone |
| Event–fluent hybrid | strong | strong | strong with causal DAG | strong | strong with retained projections | explicit but complex | strong with checkpoints | favored logical hypothesis |
| Checkpoint + semantic journal | medium | medium | medium | medium | medium | comparatively simple | strong | viable simpler fallback; may fail full reconstruction |

The comparison supports continuing with the event–fluent hybrid as the favored logical research hypothesis. It does not select a physical event store.

## 9. Falsification conditions for the next experiments

The candidate must be narrowed or rejected if:

- prose judgments require identities or relationships the model cannot express without ad hoc exceptions;
- real target movement causes systematic identity duplication;
- causal DAG reconstruction is ambiguous or prohibitively expensive;
- reducer evolution cannot preserve old and new interpretations;
- erasure requirements make the promised audit semantics misleading;
- exact checkpoint references cannot be exported without backend lock-in;
- the same outcome can only be obtained by smuggling projection values into canonical facts;
- a simpler checkpoint+journal model preserves every required query and audit property.

## 10. Conclusion

The D-03 logical shape passes the first executable architecture fixture. The next valid step is a representation/history workload and isolated Amnesia runtime reproduction—not production event-store implementation.
