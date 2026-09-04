# Reproduction instructions

Status: **research fixtures only**  
Dependencies: Python 3.11+ standard library  
Network: not required for committed fixture validation  
Private repository access: required only to re-verify source bindings or build source repositories

Run all commands from the repository root.

## 1. Validate the Amnesia technical fixture

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
input_file_sha256 = cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82
canonical_research_sha256 = 4035f6f544c08e6c8878b0e0bbc0a2a696a48501feab0f1ea554ae74c4450e8c
```

## 2. Validate the portfolio About-page fixture

```bash
python3 research/phase-2/tools/validate_portfolio_prose_fixture.py \
  research/phase-2/fixtures/portfolio-about-event-fluent.json \
  --output research/phase-2/results/portfolio-about-event-fluent-validation.json
```

Expected:

```text
status = pass
P-01 through P-12 = passed
transaction_count = 22
source_binding_count = 9
actor_count = 5
finding_count = 5
fluent_count = 6
projection_count = 5
input_file_sha256 = 9c24cf03065f69aacaed4375c9830feeec0a78c8277e3a07c0b8f299147b4eb2
canonical_research_sha256 = 74e0e3282596fd7ade8607c9a0ef40b82e096ad98840e157407e0c6b972f012e
```

This validator checks fixture scope and internal representation obligations. It does not validate prose quality, biography, live-site parity, or grader reliability.

## 3. Validate the paired-domain manifest

Run both fixture validators first so their result files match the pinned manifests, then run:

```bash
python3 research/phase-2/tools/validate_paired_domain.py \
  research/phase-2/fixtures/paired-domain-proof.json \
  research/phase-2/results/amnesia-notes-event-fluent-validation.json \
  research/phase-2/results/portfolio-about-event-fluent-validation.json \
  --output research/phase-2/results/paired-domain-validation.json
```

Expected:

```text
status = pass-with-constraints
C-01 through C-07 = passed
manifest_file_sha256 = 087bdcfa2959a678deb0fd4953596f6250e6e6be7f38b16b8a71e91a66f80ce5
canonical_research_sha256 = 46a0eb9f6f6e955df749677673a85f680dc710af5041ddbf921bce2762c38cd7
technical_fixture_input_sha256 = cba015d96b8ca0331c48dbfb96a2d29408883167ca4bb4af7b84f3cffdffff82
prose_fixture_input_sha256 = 9c24cf03065f69aacaed4375c9830feeec0a78c8277e3a07c0b8f299147b4eb2
```

The paired validator binds independently validated results and checks the C-01–C-07 non-overstatement contract. It does not re-evaluate the raw domain semantics.

## 4. Canonicalization note

All three `canonical_research_sha256` values use Python `json.dumps` with sorted keys and compact separators. They are deterministic experiment digests, not RFC 8785/JCS conformance claims.

## 5. Re-verify Amnesia private-source bindings

Under `research/bootstrap/AMNESIA-ORACLE-AUTHORIZATION.md`, an authorized isolated environment may verify:

```text
jjjjguevara/amnesia-docs@5d8aa677793cc2b4734106bb21e6118f0cc5a2aa
jjjjguevara/amnesia@4d0d1efec4ee4958db504cb56bcf47dfbc19b92a
```

Required checks:

1. verify listed Git blob identities;
2. inspect the exact public type/export boundary;
3. execute the smallest relevant type check;
4. run focused notes and capability tests;
5. build Amnesia Docs with deployment disabled;
6. execute build-only regression checks;
7. store commands, dependency/tool versions, environment, raw outputs, and digests;
8. bind any promoted finding to immutable refs.

Do not invoke a workflow that can deploy merely to obtain build evidence.

## 6. Re-verify portfolio bindings

Within the D-01P boundary, an authorized environment may verify:

```text
repository: jjjjguevara/sci-jjjjguevara
accepted commit: 1c93b60e75ce60203295a988b8125d44e6acb6bc
accepted path: src/pages/about.astro
accepted blob: d56c560fc63569b471cc4e81a65daf52568fe754
```

It may also verify the two bounded historical About checkpoints and the supporting brief/profile/résumé/validator blobs listed in `D-01P-ACCEPTANCE.md` and `PORTFOLIO-PROSE-CANDIDATE-AUDIT.md`.

A build-equivalence run must:

- disable deployment;
- avoid protected Field Notes and private career-archaeology ingestion;
- avoid copying unpublished personal records;
- record exact source ref, dependency lockfile, runtime, build command, generated route identity, output digest, and any normalization used;
- report source/build/live mismatches as findings rather than silently changing the target.

## 7. Scope

Passing these validators establishes internal fixture and cross-result consistency only. It does not validate:

- a production schema or storage engine;
- Amnesia runtime behavior;
- public live-site parity;
- prose quality or recruiter task success;
- independent biographical truth;
- a human or model grader;
- a benchmark corpus or model-training dataset.
