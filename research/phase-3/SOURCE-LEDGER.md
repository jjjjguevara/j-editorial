# Phase 3 primary-source ledger

Accessed: **2026-09-04**. Sources establish only the contribution shown below.
Recommendations and experiment outcomes are separate. No benchmark dataset, corpus,
training recipe or proprietary style-guide text was collected. Linked papers were
used through their official abstracts/metadata; no claim of full-paper analysis is made.

| ID | Primary source | Inspected scope and contribution | Boundary |
|---|---|---|---|
| S01 | W3C, [Web Annotation Data Model](https://www.w3.org/TR/annotation-model/), Recommendation 2017 | Specific resources, quote/position selectors, source state, position fragility and normalization requirements | Our raw-source probe borrows distinctions; it does not implement conformance or identity through arbitrary rewriting |
| S02 | Git, [git-update-ref](https://git-scm.com/docs/git-update-ref) | Expected-old-object update and reference transactions | Single-ref CAS is not a multi-store commit or a physical erasure mechanism |
| S03 | W3C, [PROV-DM](https://www.w3.org/TR/prov-dm/), Recommendation 2013 | Entities, activities, agents, derivation and attribution | Provenance does not establish truth, editorial policy or permission |
| S04 | SQLite, [Atomic Commit](https://www.sqlite.org/atomiccommit.html) | Journal-mediated all-or-none changes and failure assumptions | Our process-exit test is narrower than OS crash, power loss or hardware durability |
| S05 | SQLite, [PRAGMA secure_delete](https://www.sqlite.org/pragma.html#pragma_secure_delete) | Deleted bytes, zeroing/VACUUM behavior, freelist and virtual-table limitations | Current-file sentinel removal is not proof of erasure across snapshots, replicas or backups |
| S06 | Howcroft et al., [Twenty Years of Confusion in Human Evaluation](https://aclanthology.org/2020.inlg-1.23/), INLG 2020, DOI 10.18653/v1/2020.inlg-1.23 | Official abstract describes inconsistent criteria and reporting, motivating explicit constructs and evaluation sheets | No paper corpus inspected; no claimed empirical validation of our rubric |
| S07 | Belz and Thomson, [2024 ReproNLP Shared Task](https://aclanthology.org/2024.humeval-1.9/), HumEval 2024 | Official abstract/metadata used as a reproducibility-method reference | Does not determine J-Editorial sample size, agreement target or reader population |
| S08 | OWASP, [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Source content as an untrusted surface, least privilege and control separation | JSON roundtrip of hostile text is not a deployed agent security test |
| S09 | Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), 2026-01-09 | Task/trial/grader distinctions, actual environment outcomes, multiple grader methods and calibration | Industrial guidance, not independent evidence that any candidate grader works here |
| S10 | Beads, [Sync Concepts at v1.2.2](https://github.com/gastownhall/beads/blob/v1.2.2/docs/SYNC_CONCEPTS.md) | Fresh-clone `bd bootstrap`, native Dolt authority and separation from passive JSONL exports | Tracker use does not select Dolt as product persistence |

## Repository evidence

The inherited technical and prose fixture source maps retain exact repository,
commit and blob identities. Phase 3 reuses their unchanged bytes and digests.

| Source | Immutable revision | Artifact identity and use |
|---|---|---|
| Portfolio About before prose audit | `f66fa3d1b6c7b03ece46eb2f20d9089a51f02e2a` | `src/pages/about.astro`, blob `e11905e3db4591301c9bb17bed5a50490ba5bffb` |
| Portfolio About after prose audit | `900483708d74e83c5f4acd3b308127f7fa430117` | Same path, blob `5d3d5007a6d2af82d8526e5862e87ec9dd239b26` |
| Accepted Portfolio About | `1c93b60e75ce60203295a988b8125d44e6acb6bc` | Same path, blob `d56c560fc63569b471cc4e81a65daf52568fe754`; introduced by `ddf0bcee6dc95d1deac016d8e47ee286d5c04055` |
| Amnesia Docs notes reference | `5d8aa677793cc2b4734106bb21e6118f0cc5a2aa` | `src/content/docs/api/reference/commands-notes.md`, blob `1cda5daf0f96cde966d18b4e9da640d1a27ca084` |
| Phase 2 accepted merge | `0d24e78713ed7a2c04810ce9961e5c28ab3da096` | Governing inputs; former research head `5145236b652476ca8e07cfb6f78b17b5d1eeec03` |

The four full source files were locally reconstructed from connector-returned UTF-8
content and matched to their Git blob hashes before bounded extraction. The committed
fragment manifest records source SHA-256, source byte size, codepoint ranges and
fragment SHA-256. A fragment digest alone cannot independently verify its membership
in a whole source file; rechecking that requires authorized source retrieval.

## Execution provenance

Initial read-only CI run: `33913135453`, commit
`3331a846dd35cc367cad347e7f724c0ca187a24e`. Artifact `9952114521`, ZIP SHA-256:

```text
b1223321c1d7cde7f045daf63d32082c06c70011461cd46dd462a5069f7672e4
```

This artifact made the public research checkout available locally and reproduced
all three original Phase 2 results byte-for-byte. Follow-on execution records retain
separate environment versions and the stable experiment digest.

Pinned execution dependencies are checkout
`11d5960a326750d5838078e36cf38b85af677262`, upload-artifact
`ea165f8d65b6e75b540449e92b4886f43607fa02`, Beads 1.2.2 Linux amd64
SHA-256 `8140098a51d3b81d5548d1c5e6db1a2d9930e5d141efe2a4bff7d079c4d321e8`, and Dolt
2.3.2 Linux amd64 SHA-256 `7a2949fa2b2b3799ee1e57e6d64519a8d65d675fd832f6469d4e07e5a1c72b14`.
The native tracker tools are a separate probe, not a dependency of the 67-check runner.
