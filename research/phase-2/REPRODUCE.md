# Reproduction instructions

Status: **research fixture only**  
Dependencies: Python 3.11+ standard library  
Network: not required  
Private repository access: not required to validate the embedded fixture; required to re-verify source bindings

## Validate the committed fixture

From the repository root:

```bash
python3 research/phase-2/tools/validate_event_fluent_fixture.py \
  research/phase-2/fixtures/amnesia-notes-event-fluent.json \
  --output research/phase-2/results/amnesia-notes-event-fluent-validation.json
```

Expected:

```text
status = pass
E-01 through E-10 = passed
transaction_count = 13
source_binding_count = 5
fluent_count = 3
projection_count = 4
```

The generated file should report:

```text
input_file_sha256 =
  cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82

canonical_research_sha256 =
  4035f6f544c08e6c8878b0e0bbc0a2a696a48501feab0f1ea554ae74c4450e8c
```

The “canonical research” digest is produced by Python `json.dumps` with sorted keys and compact separators. It is a deterministic experiment digest, **not** an RFC 8785/JCS conformance claim.

## Re-verify private source bindings

Under `research/bootstrap/AMNESIA-ORACLE-AUTHORIZATION.md`, an authorized isolated environment may verify:

```text
jjjjguevara/amnesia-docs@5d8aa677793cc2b4734106bb21e6118f0cc5a2aa
jjjjguevara/amnesia@4d0d1efec4ee4958db504cb56bcf47dfbc19b92a
```

Required checks:

1. verify the listed Git blob identities;
2. inspect the exact public type/export boundary;
3. execute the smallest relevant type check;
4. run focused notes and capability tests;
5. build Amnesia Docs with deployment disabled;
6. execute the build-only regression checks;
7. store commands, dependency/tool versions, environment, raw outputs, and digests;
8. bind any promoted finding to immutable refs.

Do not invoke a workflow that can deploy merely to obtain build evidence.

## Scope

Passing this validator establishes internal fixture consistency only. It does not validate a production schema, storage engine, Amnesia runtime, documentation release, or model-training dataset.
