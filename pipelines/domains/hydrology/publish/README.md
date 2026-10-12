<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-publish-readme
title: Hydrology Publish Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <release-steward>
  - <catalog-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/publish/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - pipeline_specs/hydrology/publish.yaml
  - contracts/domains/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/published/layers/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
  - release/promotion_decisions/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - publish
  - release-controlled
  - public-safe
  - release-manifest
  - rollback-card
  - correction
  - evidence-bundle
  - source-role
  - nfhl
  - catalog-close
  - governed-api
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/publish path as a nested executable publication-artifact assembly sublane."
  - "Publish logic here is executable artifact assembly support only; it does not own release decisions, release manifests, policy, EvidenceBundle truth, catalog truth, lifecycle data, source descriptors, schemas, or public API authority."
  - "Publication remains a governed state transition under release responsibility roots; this sublane may only materialize artifacts from approved ReleaseManifest inputs."
  - "Hydrology public artifacts must preserve source-role, time/freshness, evidence, sensitivity/public-safe transform, correction, and rollback state."
  - "NFHL remains regulatory context only and must never publish as observed flooding or current guidance."
  - "Concrete executable behavior, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Publish Pipeline

> Executable Hydrology sublane for assembling release-approved, public-safe Hydrology artifacts from closed catalog/triplet candidates and approved ReleaseManifest inputs — without making release decisions, bypassing policy, rewriting evidence, or turning published artifacts into canonical truth.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20publish%20assembly-2e7d32)
![authority](https://img.shields.io/badge/authority-artifact%20assembly%20only-0a7ea4)
![release](https://img.shields.io/badge/release%20decision-not%20owned%20here-d62728)
![anti-collapse](https://img.shields.io/badge/published%20artifact%20%E2%89%A0%20canonical%20truth-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/publish/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Publication artifact assembly  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** release-controlled artifact assembly only; no direct release approval, no direct public API authority, and no writes outside approved release/published artifact homes

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Publish anti-collapse rules](#3-publish-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Publish scope](#6-publish-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal publish receipt](#11-minimal-publish-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Correction and rollback](#13-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/publish/` is the executable sublane for assembling Hydrology artifacts after release workflow approval.

It supports artifact assembly for:

- public-safe Hydrology layer packages;
- public-safe catalog exports;
- public-safe triplet or graph projection exports;
- release-approved metadata bundles for watersheds, HUCs, reaches, gauges, wells, waterbodies, observation datasets, hydrographs, and regulatory-context products;
- public-safe hydrology tiles, static files, or generated manifests where the release workflow explicitly permits them;
- Evidence Drawer and Focus Mode payload packages that carry EvidenceBundle refs rather than embedding unsupported claims;
- correction notices, tombstone markers, supersession markers, and rollback-target materialization;
- audit receipts proving the output was assembled from a specific ReleaseManifest and approved candidate set.

This directory implements or will implement the **how** of release-controlled artifact assembly. It does not decide release, define public policy, approve sensitivity transforms, define source identity, store canonical records, fetch source data, issue current advisories, decide regulatory meaning, or certify engineering use.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how** of artifact assembly. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and pipeline READMEs. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `publish/`? | This is a narrow executable lane for materializing already-approved public-safe artifacts. | PROPOSED / NEEDS VERIFICATION |
| Does this own release decisions? | No. Release decisions, ReleaseManifests, and rollback cards remain under release responsibility roots. | CONFIRMED governance posture |
| Does this replace `catalog_close/`? | No. `catalog_close/` verifies release-preflight closure; this lane materializes artifacts only after release approval. | PROPOSED |
| Can it read RAW/WORK/QUARANTINE? | No for normal publishing. It reads approved release inputs, catalog/triplet candidates, and processed/public-safe refs only. | CONFIRMED doctrine posture |
| Can it write public API code? | No. It may write approved artifacts; governed APIs and UI code live in app/package roots. | CONFIRMED root separation |

> [!IMPORTANT]
> A publish pipeline is not a release authority. It is only an artifact assembler that consumes an approved release package and produces auditable, rollbackable, public-safe Hydrology artifacts.

[⬆ Back to top](#top)

---

## 3. Publish anti-collapse rules

Publishing must not collapse release state, evidence state, or truth class.

Disallowed collapses:

```text
publish job -> release approval
published artifact -> canonical truth
published artifact -> EvidenceBundle
ReleaseManifest -> source descriptor
catalog candidate -> public artifact without release
triplet delta -> canonical review state
NFHL regulatory context -> observed flooding
observed gauge reading -> current advisory
time-series artifact -> current operational decision
generated label -> evidence
missing rollback target -> published artifact
```

Required distinctions:

- ReleaseManifest, RollbackCard, EvidenceBundle, SourceDescriptor, catalog item, graph delta, and published artifact remain distinct;
- source role and knowledge character remain explicit in artifact metadata;
- observation time, valid time, retrieval time, processing time, catalog time, release time, and correction time remain distinct;
- public-safe transform state is preserved;
- correction path and rollback target are included in publish receipts;
- generated summaries remain downstream display aids, never evidence.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology publication artifact assembly.

Appropriate contents include:

- fixture-only publish dry-run entrypoints;
- ReleaseManifest input readers;
- public-safe artifact builders for Hydrology layers, catalog exports, and graph projection exports;
- metadata stampers that preserve EvidenceBundle, policy, source-role, time/freshness, and rollback refs;
- published artifact digest and integrity manifest builders;
- supersession, tombstone, correction, and rollback materialization helpers;
- no-raw-read and no-direct-release validators;
- no-NFHL-as-observed validators for public artifact metadata;
- publish receipt emitters, if not shared;
- thin adapters that read approved release inputs, not source systems or unapproved lifecycle stores.

A good placement test:

> If the code takes an approved Hydrology ReleaseManifest and materializes public-safe artifacts with receipts and rollback targets, it may belong here. If it decides release, performs catalog closure, fetches data, defines schemas, edits public API code, or reads unapproved RAW/WORK/QUARANTINE inputs, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Release decisions, ReleaseManifests, approvals, rollback cards | `release/...` responsibility roots |
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture and doctrine | `docs/domains/hydrology/...` |
| Object meaning contracts | `contracts/domains/hydrology/` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Ingest, normalize, validate, catalog, or catalog-close logic | Owning `pipelines/domains/hydrology/*` lane |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/publish/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/publish/` or accepted test home |
| Raw, work, quarantine, processed, catalog, or triplet stores | `data/...` lifecycle homes |
| Public API or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Current advisories, operational decisions, regulatory determinations, or engineering certification | Outside this publish artifact assembly lane |

[⬆ Back to top](#top)

---

## 6. Publish scope

| Scope area | Publish responsibility | Failure behavior |
|---|---|---|
| Release input | Confirm approved ReleaseManifest and rollback refs. | Deny artifact assembly. |
| Public-safe artifacts | Materialize only approved layers, exports, and metadata. | Deny or quarantine on missing transform refs. |
| Evidence refs | Preserve EvidenceBundle refs and citation state. | Deny if claim-bearing artifact lacks support. |
| Source-role metadata | Preserve observed, modeled, regulatory, aggregate, derived, generated context. | Deny if collapsed. |
| NFHL context | Preserve regulatory-context caveat. | Deny if treated as observed flooding. |
| Time/freshness | Preserve observation, valid, retrieval, processing, release, correction times. | Deny or restrict if missing. |
| Integrity | Emit hashes, file manifests, and publish receipts. | Deny if digest mismatch. |
| Correction/rollback | Materialize correction and rollback hooks. | Deny if missing. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology publish run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved release inputs only: ReleaseManifest, rollback refs, catalog/triplet candidate refs, processed refs, public-safe transform refs, policy outcomes, and EvidenceBundle refs.
2. **Validate** release approval, public-safe state, source-role metadata, time/freshness metadata, artifact target paths, integrity plan, correction path, and rollback target.
3. **Materialize** approved public-safe artifacts into accepted published artifact homes only.
4. **Emit receipts** with input refs, release refs, artifact hashes, output refs, correction refs, and rollback refs.
5. **Never mutate** canonical stores, source descriptors, policy, schemas, EvidenceBundles, or release decisions.
6. **Never publish without approved release input.**

Publishing is a governed state transition controlled by release authority. This pipeline only performs the release-approved artifact assembly step.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology publish run must check or explicitly fail closed on:

1. **ReleaseManifest gate** — approved ReleaseManifest exists and names Hydrology publish targets.
2. **Rollback gate** — RollbackCard or accepted rollback target exists before artifact write.
3. **Release-candidate gate** — inputs are release-candidate or release-approved refs, not raw/work/quarantine records.
4. **Evidence gate** — claim-bearing artifacts resolve EvidenceBundle support.
5. **Policy gate** — finite policy outcome authorizes publication scope and public-safe transforms.
6. **Sensitivity/public-safe gate** — redaction, generalization, restriction, denial, delay, or allow state is explicit.
7. **Source-role gate** — observed, modeled, regulatory, official-source, aggregate, derived, and generated classes remain distinct.
8. **NFHL gate** — NFHL remains regulatory context and never publishes as observed flooding or current guidance.
9. **Time/freshness gate** — observation, valid, retrieval, processing, release, and correction times are explicit.
10. **Artifact integrity gate** — output paths, hashes, manifests, and size/format checks pass.
11. **Correction path gate** — correction notice path or correction mechanism is recorded.
12. **No-canonical-mutation gate** — publish job does not alter source, processed, catalog, graph, policy, schema, or release authority records.
13. **Governed API boundary gate** — public clients consume governed APIs/released artifacts, not internal stores or model outputs.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/publish/
├── README.md                         # this file
├── PUBLISH_CONTRACT.md               # PROPOSED: hydrology publish artifact assembly contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── read_release_manifest.py          # PROPOSED
├── validate_release_inputs.py        # PROPOSED
├── validate_public_safe_state.py     # PROPOSED
├── validate_source_role_metadata.py  # PROPOSED
├── build_layer_artifacts.py          # PROPOSED
├── build_catalog_export.py           # PROPOSED
├── build_graph_export.py             # PROPOSED
├── build_integrity_manifest.py       # PROPOSED
├── build_publish_receipt.py          # PROPOSED
├── materialize_correction_hooks.py   # PROPOSED
└── adapters/                         # PROPOSED thin release-input adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/publish.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release-controlled homes such as `data/published/layers/hydrology/`, published catalog/graph artifact homes if approved, `data/receipts/pipeline/hydrology/publish/`, and `release/` records controlled by release authority.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/publish/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Release manifest input | `release/manifests/hydrology/` | Required before real publish run. |
| Release candidate input | `release/candidates/hydrology/` | Reviewable input only. |
| Catalog input | `data/catalog/domain/hydrology/` | Projection input after closure. |
| Triplet input | `data/triplets/hydrology/` | Graph projection input after closure. |
| Evidence input | `data/proofs/evidence_bundle/` | Required for claim-bearing artifacts. |
| Published artifact | `data/published/layers/hydrology/` or approved published home | Release-controlled output only. |
| Publish receipt | `data/receipts/pipeline/hydrology/publish/<run_id>.yml` or accepted receipt home | Records manifest, inputs, hashes, outputs, rollback. |
| Correction / rollback refs | `release/...` accepted homes | Owned by release authority. |

[⬆ Back to top](#top)

---

## 11. Minimal publish receipt

The final schema is not defined here. This example shows the minimum information a Hydrology publish receipt should preserve.

```yaml
schema_version: kfm.hydrology_publish_receipt.v1
receipt_id: hydrology_publish_<release_id>_<run_id>_<hash>
pipeline_id: domains.hydrology.publish
run_id: run_YYYYMMDDThhmmssZ
status: PUBLISH_RECEIPT
release:
  release_id: <release_id>
  release_manifest_ref: release/manifests/hydrology/<release_id>.yml
  rollback_card_ref: release/manifests/hydrology/<release_id>.rollback.yml
  correction_path_ref: release/corrections/hydrology/<release_id>/
input_refs:
  catalog_refs: []
  triplet_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  public_safe_transform_refs: []
anti_collapse:
  publish_job_is_release_approval: false
  published_artifact_is_canonical_truth: false
  published_artifact_is_evidence_bundle: false
  nfhl_is_observed_flooding: false
outputs:
  artifacts:
    - artifact_ref: data/published/layers/hydrology/<release_id>/<artifact>.json
      artifact_hash: sha256:<hash>
      artifact_kind: <layer|catalog_export|graph_export|metadata|correction|tombstone>
  integrity_manifest_ref: data/published/layers/hydrology/<release_id>/manifest.yml
outcome:
  decision: MATERIALIZED
  release_handoff: complete
rollback:
  rollback_required: true
  rollback_verified: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until release-input schema, public-safe transforms, evidence, policy, rollback, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/publish/
├── test_no_network_dry_run.py              # PROPOSED
├── test_release_manifest_required.py       # PROPOSED
├── test_rollback_card_required.py          # PROPOSED
├── test_no_raw_work_quarantine_inputs.py   # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_public_safe_transform_required.py  # PROPOSED
├── test_nfhl_not_observed_flooding.py      # PROPOSED
├── test_publish_not_release_approval.py    # PROPOSED
├── test_artifact_not_canonical_truth.py    # PROPOSED
├── test_no_canonical_mutation.py           # PROPOSED
├── test_integrity_hashes.py                # PROPOSED
├── test_correction_path_required.py        # PROPOSED
└── test_governed_api_boundary.py           # PROPOSED
```

A dry run should prove fixtures load without network access, release manifests and rollback cards are required, raw/work/quarantine inputs are denied, public-safe transform refs are required, NFHL remains regulatory context, published artifacts are not canonical truth, receipts are deterministic, and the job does not mutate source, processed, catalog, graph, schema, policy, EvidenceBundle, or release authority records.

[⬆ Back to top](#top)

---

## 13. Correction and rollback

Hydrology publish must make correction and rollback visible.

Required chain:

```text
approved Hydrology ReleaseManifest
  -> publish validation
  -> artifact materialization
  -> integrity manifest
  -> publish receipt
  -> correction hook
  -> rollback-verification hook
  -> governed API / public artifact availability
```

Correction and rollback posture:

- published artifacts are superseded or withdrawn by governed release/correction workflow, not hidden overwrite;
- publish receipts preserve release refs, input refs, artifact hashes, evidence refs, source-role refs, policy outcomes, correction refs, and rollback refs;
- public artifacts are invalidated if ReleaseManifest, EvidenceBundle, policy, source-role, public-safe transform, catalog, graph, correction, or rollback refs drift;
- rollback is owned by `release/`, but this pipeline must materialize and verify rollback targets before publication.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/publish/README.md` file;
- identifies this directory as a nested executable Hydrology publication-artifact assembly sublane;
- prevents release-decision, source, schema, contract, policy, fixture, test, data, proof, catalog, graph, app, and UI authority from being placed here;
- preserves ReleaseManifest, RollbackCard, EvidenceBundle, source-role, time/freshness, policy, public-safe transform, artifact integrity, correction, and rollback boundaries;
- blocks publish-as-release-approval, artifact-as-canonical-truth, artifact-as-evidence, NFHL-as-observed, no-rollback publication, and direct internal-store exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has release-input fixtures, schema-backed publish receipts, contract conformance, release-manifest/rollback/evidence/public-safe/source-role/no-canonical-mutation tests, deterministic integrity manifests, CI coverage, steward-review handoff, and correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-PUBLISH-001` | Should Hydrology publish remain domain-specific, or should shared artifact assembly live in `pipelines/catalog/` or a release pipeline with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-PUBLISH-002` | Which release schema owns publish receipts, integrity manifests, correction hooks, and rollback verification? | NEEDS VERIFICATION |
| `HYDRO-PUBLISH-003` | Which artifact kinds are first-wave: vector tiles, GeoJSON, PMTiles, STAC/DCAT exports, graph exports, static summaries, or all by adapter? | NEEDS VERIFICATION |
| `HYDRO-PUBLISH-004` | Which CI job owns Hydrology publish invariant tests? | UNKNOWN |
| `HYDRO-PUBLISH-005` | Which public-safe precision, time/freshness, and caveat levels are allowed by Hydrology publication posture? | NEEDS VERIFICATION |
| `HYDRO-PUBLISH-006` | How should governed API cache invalidation be linked to publish receipts without letting the pipeline own API behavior? | NEEDS VERIFICATION / ADR |
| `HYDRO-PUBLISH-007` | Which rollback verification format is required before artifact availability? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, release-decision logic, direct public API code, direct UI code, current advisory language, unreviewed generated summaries, or writes to published artifact homes until ReleaseManifest, EvidenceBundle, public-safe transform, integrity, correction, and rollback gates are proven.
