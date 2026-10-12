<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-publish-layers-readme
title: Hydrology Publish Layers Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <release-steward>
  - <catalog-steward>
  - <map-layer-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/publish_layers/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/hydrology/README.md
  - pipelines/domains/hydrology/publish/README.md
  - pipelines/domains/hydrology/catalog/README.md
  - pipelines/domains/hydrology/catalog_close/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - pipeline_specs/hydrology/publish_layers.yaml
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
  - publish-layers
  - map-layers
  - public-safe
  - vector-tiles
  - pmtiles
  - geojson
  - release-manifest
  - rollback-card
  - correction
  - evidence-bundle
  - nfhl
  - source-role
  - governed-api
  - governance
notes:
  - "This README fills the blank pipelines/domains/hydrology/publish_layers path as a nested executable public-safe layer assembly sublane."
  - "Publish Layers logic is executable map-layer artifact assembly support only; it does not own release decisions, release manifests, policy, EvidenceBundle truth, catalog truth, lifecycle data, source descriptors, schemas, or public API authority."
  - "Layer publication remains a governed state transition under release responsibility roots; this sublane may only materialize layer artifacts from approved ReleaseManifest inputs."
  - "Hydrology layer artifacts must preserve source-role, time/freshness, evidence, sensitivity/public-safe transform, symbology caveats, correction, and rollback state."
  - "NFHL remains regulatory context only and must never publish as observed flooding, current condition, or KFM-issued guidance."
  - "Concrete executable behavior, tile formats, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Publish Layers Pipeline

> Executable Hydrology sublane for assembling release-approved, public-safe map-layer artifacts from closed Hydrology catalog/triplet candidates and approved ReleaseManifest inputs — without making release decisions, bypassing policy, exposing internal stores, or turning layer artifacts into canonical truth.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20publish%20layers-2e7d32)
![authority](https://img.shields.io/badge/authority-layer%20assembly%20only-0a7ea4)
![release](https://img.shields.io/badge/release%20decision-not%20owned%20here-d62728)
![anti-collapse](https://img.shields.io/badge/layer%20%E2%89%A0%20canonical%20truth-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/publish_layers/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Sublane:** Public-safe layer artifact assembly  
**Placement posture:** nested executable sublane under `pipelines/domains/hydrology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Publication posture:** release-controlled layer assembly only; no direct release approval, no direct public API authority, and no writes outside approved published-layer homes

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Layer anti-collapse rules](#3-layer-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Layer scope](#6-layer-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal layer publish receipt](#11-minimal-layer-publish-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Correction and rollback](#13-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/publish_layers/` is the executable sublane for materializing release-approved Hydrology map-layer artifacts.

It supports layer assembly for:

- public-safe vector layer packages;
- public-safe raster or tile-index metadata packages where approved;
- PMTiles, vector tile, GeoJSON, FlatGeobuf, COG, or static layer manifests where release workflow explicitly permits the format;
- layer metadata for watersheds, HUCs, reaches, gauges, wells, waterbodies, observation datasets, hydrographs, terrain-support context, and regulatory-context products;
- style-agnostic layer metadata that preserves source-role and caveat state;
- Evidence Drawer and Focus Mode layer payload packages that carry EvidenceBundle refs rather than embedding unsupported claims;
- correction notices, tombstone markers, supersession markers, and rollback-target materialization for published layers;
- layer integrity manifests and receipts proving every output was assembled from a specific ReleaseManifest and approved candidate set.

This directory implements or will implement the **how** of release-controlled Hydrology layer assembly. It does not decide release, define public policy, approve sensitivity transforms, define source identity, store canonical records, fetch source data, issue current guidance, decide regulatory meaning, or certify engineering use.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how** of layer artifact assembly. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is the domain lane used by Hydrology docs and pipeline READMEs. | CONFIRMED documentation pattern; behavior NEEDS VERIFICATION |
| Why `publish_layers/`? | This is a narrow executable lane for materializing already-approved public-safe Hydrology layer artifacts. | PROPOSED / NEEDS VERIFICATION |
| Does this own release decisions? | No. Release decisions, ReleaseManifests, and rollback cards remain under release responsibility roots. | CONFIRMED governance posture |
| Does this replace `publish/`? | No. `publish/` is the broader artifact assembly lane; this lane is layer-specific. | PROPOSED |
| Can it read RAW/WORK/QUARANTINE? | No for normal layer publication. It reads approved release inputs, catalog/triplet candidates, processed/public-safe refs, and closure receipts only. | CONFIRMED doctrine posture |
| Can it write public API or UI code? | No. It may write approved layer artifacts; governed APIs and UI code live in app/package roots. | CONFIRMED root separation |

> [!IMPORTANT]
> A layer-publish pipeline is not a release authority. It is only an artifact assembler that consumes an approved release package and produces auditable, rollbackable, public-safe Hydrology layer artifacts.

[⬆ Back to top](#top)

---

## 3. Layer anti-collapse rules

Layer publishing must not collapse release state, evidence state, or truth class.

Disallowed collapses:

```text
layer publish job -> release approval
published layer -> canonical truth
published layer -> EvidenceBundle
ReleaseManifest -> source descriptor
catalog candidate -> layer without release
triplet delta -> canonical review state
NFHL regulatory context -> observed flooding
observed gauge reading -> current guidance
time-series layer -> operational decision
style label -> evidence
generalized layer -> precise internal geometry
missing rollback target -> published layer
```

Required distinctions:

- ReleaseManifest, RollbackCard, EvidenceBundle, SourceDescriptor, catalog item, graph delta, style layer, tile layer, and published artifact remain distinct;
- source role and knowledge character remain explicit in layer metadata;
- precision, generalization, redaction, delay, and restriction transforms are recorded;
- observation time, valid time, retrieval time, processing time, catalog time, release time, tile-build time, and correction time remain distinct;
- layer styles and labels are display aids, never evidence;
- correction path and rollback target are included in layer publish receipts.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology map-layer artifact assembly.

Appropriate contents include:

- fixture-only layer publish dry-run entrypoints;
- ReleaseManifest and layer-target readers;
- public-safe layer builders for approved Hydrology formats;
- vector-tile, PMTiles, GeoJSON, FlatGeobuf, COG manifest, or layer-index builders where explicitly approved;
- metadata stampers that preserve EvidenceBundle, policy, source-role, time/freshness, precision, caveat, and rollback refs;
- layer digest and integrity manifest builders;
- supersession, tombstone, correction, and rollback materialization helpers for layer artifacts;
- no-raw-read and no-direct-release validators;
- no-NFHL-as-observed validators for layer metadata;
- no-style-as-evidence validators;
- layer publish receipt emitters, if not shared;
- thin adapters that read approved release inputs, not source systems or unapproved lifecycle stores.

A good placement test:

> If the code takes an approved Hydrology ReleaseManifest and materializes public-safe map-layer artifacts with receipts and rollback targets, it may belong here. If it decides release, performs catalog closure, fetches data, defines schemas, edits public API/UI code, or reads unapproved RAW/WORK/QUARANTINE inputs, it belongs somewhere else.

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
| Generic publish assembly | `pipelines/domains/hydrology/publish/` or shared release pipeline |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/publish_layers/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/publish_layers/` or accepted test home |
| Raw, work, quarantine, processed, catalog, or triplet stores | `data/...` lifecycle homes |
| Public API or UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Current guidance, operational decisions, regulatory determinations, or engineering certification | Outside this layer artifact assembly lane |

[⬆ Back to top](#top)

---

## 6. Layer scope

| Scope area | Layer responsibility | Failure behavior |
|---|---|---|
| Release input | Confirm approved ReleaseManifest and rollback refs. | Deny layer assembly. |
| Layer targets | Materialize only approved layer ids, formats, zoom/resolution classes, and output paths. | Deny or quarantine if target is unapproved. |
| Public-safe transform | Preserve redaction, generalization, restriction, delay, or allow state. | Deny if missing. |
| Evidence refs | Preserve EvidenceBundle refs and citation state. | Deny if claim-bearing layer lacks support. |
| Source-role metadata | Preserve observed, modeled, regulatory, aggregate, derived, and generated context. | Deny if collapsed. |
| NFHL context | Preserve regulatory-context caveat. | Deny if treated as observed flooding or current condition. |
| Styling metadata | Attach approved style refs and caveats. | Deny if style claims evidence. |
| Integrity | Emit hashes, layer manifests, tile manifests, and publish receipts. | Deny if digest mismatch. |
| Correction/rollback | Materialize correction and rollback hooks. | Deny if missing. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Hydrology layer-publish run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved release inputs only: ReleaseManifest, rollback refs, catalog/triplet candidate refs, processed refs, public-safe transform refs, policy outcomes, EvidenceBundle refs, and layer target specs.
2. **Validate** release approval, public-safe state, source-role metadata, time/freshness metadata, layer target paths, tile/index integrity plan, correction path, and rollback target.
3. **Materialize** approved public-safe layer artifacts into accepted published layer homes only.
4. **Emit receipts** with input refs, release refs, layer ids, tile/index hashes, output refs, correction refs, and rollback refs.
5. **Never mutate** canonical stores, source descriptors, policy, schemas, EvidenceBundles, catalog truth, graph truth, or release decisions.
6. **Never publish layers without approved release input.**

Layer publication is a governed state transition controlled by release authority. This pipeline only performs the release-approved layer assembly step.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Hydrology layer-publish run must check or explicitly fail closed on:

1. **ReleaseManifest gate** — approved ReleaseManifest exists and names Hydrology layer targets.
2. **Rollback gate** — RollbackCard or accepted rollback target exists before layer write.
3. **Release-candidate gate** — inputs are release-candidate or release-approved refs, not raw/work/quarantine records.
4. **Layer-target gate** — layer id, format, tiling/resolution class, output path, and visibility posture are approved.
5. **Evidence gate** — claim-bearing layers resolve EvidenceBundle support.
6. **Policy gate** — finite policy outcome authorizes publication scope and public-safe transforms.
7. **Public-safe gate** — redaction, generalization, restriction, denial, delay, or allow state is explicit.
8. **Source-role gate** — observed, modeled, regulatory, official-source, aggregate, derived, and generated classes remain distinct.
9. **NFHL gate** — NFHL remains regulatory context and never publishes as observed flooding or current guidance.
10. **Time/freshness gate** — observation, valid, retrieval, processing, tile-build, release, and correction times are explicit.
11. **Style/caveat gate** — style labels, legends, tooltips, and layer names do not overclaim evidence or authority.
12. **Artifact integrity gate** — output paths, hashes, manifests, tile counts, and format checks pass.
13. **Correction path gate** — correction notice path or correction mechanism is recorded.
14. **No-canonical-mutation gate** — layer publish job does not alter source, processed, catalog, graph, policy, schema, EvidenceBundle, or release authority records.
15. **Governed API boundary gate** — public clients consume governed APIs/released artifacts, not internal stores or model outputs.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/publish_layers/
├── README.md                         # this file
├── LAYER_PUBLISH_CONTRACT.md         # PROPOSED: hydrology layer artifact contract
├── run_dry_fixture.py                # PROPOSED synthetic/redacted fixture only
├── read_release_manifest.py          # PROPOSED
├── validate_layer_targets.py         # PROPOSED
├── validate_public_safe_state.py     # PROPOSED
├── validate_source_role_metadata.py  # PROPOSED
├── validate_style_caveats.py         # PROPOSED
├── build_vector_tiles.py             # PROPOSED if approved
├── build_pmtiles.py                  # PROPOSED if approved
├── build_geojson_layer.py            # PROPOSED if approved
├── build_layer_manifest.py           # PROPOSED
├── build_layer_publish_receipt.py    # PROPOSED
├── materialize_correction_hooks.py   # PROPOSED
└── adapters/                         # PROPOSED thin release-input adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/publish_layers.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release-controlled homes such as `data/published/layers/hydrology/`, layer metadata/index homes if approved, `data/receipts/pipeline/hydrology/publish_layers/`, and `release/` records controlled by release authority.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/hydrology/publish_layers/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Release manifest input | `release/manifests/hydrology/` | Required before real layer publish run. |
| Release candidate input | `release/candidates/hydrology/` | Reviewable input only. |
| Catalog input | `data/catalog/domain/hydrology/` | Projection input after closure. |
| Triplet input | `data/triplets/hydrology/` | Graph projection input after closure. |
| Evidence input | `data/proofs/evidence_bundle/` | Required for claim-bearing layers. |
| Published layer artifact | `data/published/layers/hydrology/` or approved published layer home | Release-controlled output only. |
| Layer publish receipt | `data/receipts/pipeline/hydrology/publish_layers/<run_id>.yml` or accepted receipt home | Records manifest, inputs, layer ids, hashes, outputs, rollback. |
| Correction / rollback refs | `release/...` accepted homes | Owned by release authority. |

[⬆ Back to top](#top)

---

## 11. Minimal layer publish receipt

The final schema is not defined here. This example shows the minimum information a Hydrology layer publish receipt should preserve.

```yaml
schema_version: kfm.hydrology_layer_publish_receipt.v1
receipt_id: hydrology_publish_layers_<release_id>_<run_id>_<hash>
pipeline_id: domains.hydrology.publish_layers
run_id: run_YYYYMMDDThhmmssZ
status: LAYER_PUBLISH_RECEIPT
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
layer_targets:
  - layer_id: <layer_id>
    artifact_kind: <vector_tile|pmtiles|geojson|flatgeobuf|cog_index|metadata>
    visibility: <public|restricted_public|withheld>
anti_collapse:
  layer_publish_job_is_release_approval: false
  published_layer_is_canonical_truth: false
  published_layer_is_evidence_bundle: false
  nfhl_is_observed_flooding: false
  style_label_is_evidence: false
outputs:
  artifacts:
    - artifact_ref: data/published/layers/hydrology/<release_id>/<layer_id>/<artifact>
      artifact_hash: sha256:<hash>
      artifact_kind: <vector_tile|pmtiles|geojson|flatgeobuf|cog_index|metadata|tombstone>
  layer_manifest_ref: data/published/layers/hydrology/<release_id>/layer-manifest.yml
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

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until release-input schema, public-safe transforms, layer-target spec, evidence, policy, rollback, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/publish_layers/
├── test_no_network_dry_run.py              # PROPOSED
├── test_release_manifest_required.py       # PROPOSED
├── test_rollback_card_required.py          # PROPOSED
├── test_no_raw_work_quarantine_inputs.py   # PROPOSED
├── test_layer_targets_approved.py          # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_public_safe_transform_required.py  # PROPOSED
├── test_nfhl_not_observed_flooding.py      # PROPOSED
├── test_style_label_not_evidence.py        # PROPOSED
├── test_layer_not_canonical_truth.py       # PROPOSED
├── test_no_canonical_mutation.py           # PROPOSED
├── test_integrity_hashes.py                # PROPOSED
├── test_correction_path_required.py        # PROPOSED
└── test_governed_api_boundary.py           # PROPOSED
```

A dry run should prove fixtures load without network access, release manifests and rollback cards are required, raw/work/quarantine inputs are denied, layer targets are explicit, public-safe transform refs are required, NFHL remains regulatory context, styles do not overclaim evidence, layer artifacts are not canonical truth, receipts are deterministic, and the job does not mutate source, processed, catalog, graph, schema, policy, EvidenceBundle, or release authority records.

[⬆ Back to top](#top)

---

## 13. Correction and rollback

Hydrology layer publication must make correction and rollback visible.

Required chain:

```text
approved Hydrology ReleaseManifest
  -> layer target validation
  -> layer artifact materialization
  -> layer integrity manifest
  -> layer publish receipt
  -> correction hook
  -> rollback-verification hook
  -> governed API / released layer availability
```

Correction and rollback posture:

- published layer artifacts are superseded or withdrawn by governed release/correction workflow, not hidden overwrite;
- layer publish receipts preserve release refs, layer refs, input refs, artifact hashes, evidence refs, source-role refs, policy outcomes, correction refs, and rollback refs;
- public layer artifacts are invalidated if ReleaseManifest, EvidenceBundle, policy, source-role, public-safe transform, catalog, graph, style, correction, or rollback refs drift;
- rollback is owned by `release/`, but this pipeline must materialize and verify rollback targets before layer availability.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/hydrology/publish_layers/README.md` file;
- identifies this directory as a nested executable Hydrology public-safe layer artifact assembly sublane;
- prevents release-decision, source, schema, contract, policy, fixture, test, data, proof, catalog, graph, app, UI, and style-authority from being placed here;
- preserves ReleaseManifest, RollbackCard, EvidenceBundle, source-role, time/freshness, policy, public-safe transform, layer target, style caveat, artifact integrity, correction, and rollback boundaries;
- blocks publish-as-release-approval, layer-as-canonical-truth, layer-as-evidence, style-as-evidence, NFHL-as-observed, no-rollback publication, and direct internal-store exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has release-input fixtures, schema-backed layer publish receipts, contract conformance, release-manifest/rollback/evidence/public-safe/source-role/style/no-canonical-mutation tests, deterministic integrity manifests, CI coverage, steward-review handoff, and correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HYDRO-PUBLISH-LAYERS-001` | Should layer publication remain Hydrology-specific, or should shared layer assembly live in a release pipeline with Hydrology adapters? | NEEDS VERIFICATION / ADR |
| `HYDRO-PUBLISH-LAYERS-002` | Which release schema owns layer publish receipts, layer manifests, correction hooks, and rollback verification? | NEEDS VERIFICATION |
| `HYDRO-PUBLISH-LAYERS-003` | Which artifact formats are first-wave: PMTiles, vector tiles, GeoJSON, FlatGeobuf, COG indexes, layer manifests, or all by adapter? | NEEDS VERIFICATION |
| `HYDRO-PUBLISH-LAYERS-004` | Which CI job owns Hydrology layer-publish invariant tests? | UNKNOWN |
| `HYDRO-PUBLISH-LAYERS-005` | Which precision, zoom, time/freshness, and caveat levels are allowed by Hydrology publication posture? | NEEDS VERIFICATION |
| `HYDRO-PUBLISH-LAYERS-006` | How should governed API cache invalidation be linked to layer publish receipts without letting the pipeline own API behavior? | NEEDS VERIFICATION / ADR |
| `HYDRO-PUBLISH-LAYERS-007` | Which rollback verification format is required before layer availability? | NEEDS VERIFICATION |
| `HYDRO-PUBLISH-LAYERS-008` | Where should shared style contracts live so layer builders do not become style authority? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, release-decision logic, direct public API code, direct UI code, style-authority decisions, unreviewed generated labels, or writes to published layer homes until ReleaseManifest, EvidenceBundle, public-safe transform, layer target, integrity, correction, and rollback gates are proven.
