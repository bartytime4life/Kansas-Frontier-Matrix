<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/layers/atmosphere/readme
name: Atmosphere Layer Registry README
path: data/registry/layers/atmosphere/README.md
type: data-registry-layer-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <layer-steward>
  - <atmosphere-domain-steward>
  - <map-layer-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: atmosphere-layer-registry-records
domain: atmosphere
path_posture: existing-empty-placeholder-replaced; layer-registry-parent-currently-greenfield-stub; subtype-first-layer-registry-path-confirmed; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; not-emergency-guidance; station-location-and-sensor-context-reviewed; source-role-preserving; knowledge-character-preserving; freshness-aware; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../sources/README.md
  - ../../sources/atmosphere/
  - ../../crosswalks/README.md
  - ../../../raw/atmosphere/
  - ../../../work/atmosphere/
  - ../../../quarantine/atmosphere/
  - ../../../processed/atmosphere/
  - ../../../catalog/domain/atmosphere/
  - ../../../published/layers/atmosphere/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../../docs/domains/atmosphere/POLICY.md
  - ../../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../../contracts/domains/atmosphere/domain_layer_descriptor.md
  - ../../../../contracts/data/layer_descriptor.md
  - ../../../../contracts/data/layer_manifest.md
  - ../../../../contracts/data/layer_catalog_item.md
  - ../../../../policy/domains/atmosphere/
  - ../../../../policy/sensitivity/atmosphere/
  - ../../../../schemas/contracts/v1/domains/atmosphere/domain_layer_descriptor.schema.json
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - layers
  - atmosphere
  - air
  - domain-layer-descriptor
  - layer-descriptor
  - layer-manifest
  - map-layer
  - source-role
  - knowledge-character
  - rights
  - sensitivity
  - freshness
  - air-quality
  - smoke
  - weather
  - climate
  - station
  - sensor
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/layers/atmosphere/README.md`."
  - "The parent `data/registry/layers/README.md` is currently a greenfield stub, so layer-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Atmosphere layer registry records are registry/control records. They do not store layer payloads, render tiles, prove Atmosphere claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "Atmosphere layer registry state must preserve source role and knowledge character: AQI is not concentration; AOD is not PM2.5; model fields are not observations; advisory context is not KFM emergency guidance."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Layer Registry

Subtype-first layer-registry lane for Atmosphere/Air layer registry records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-0aa">
  <img alt="Lane: layers" src="https://img.shields.io/badge/lane-layers-blue">
  <img alt="Boundary: not layer bytes" src="https://img.shields.io/badge/boundary-not%20layer%20bytes-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Atmosphere layer boundary](#atmosphere-layer-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/layers/atmosphere/` is a registry lane for Atmosphere layer identity, meaning, constraints, and release-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, published layer bytes, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, operational guidance, or generated-answer authority.

---

## Scope

This directory documents and may hold Atmosphere layer registry records, layer-family indexes, registry-local manifests, descriptor pointers, release-readiness pointers, and routing notes for map layers that represent Atmosphere/Air-domain material.

Atmosphere layer registry records may describe:

- stable Atmosphere layer identity and display-facing layer families;
- Atmosphere object families represented by the layer;
- relationships to `DomainLayerDescriptor`, generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` objects;
- source-role, knowledge-character, source-family, temporal, and cross-lane provenance constraints;
- evidence, proof, validation, catalog, policy, release, correction, and rollback references;
- sensitivity posture for station/sensor context, advisory context, low-cost sensors, smoke/AOD products, climate products, and joined exposure contexts;
- public-safe summary requirements, allowed geometry precision, freshness indicators, caveat requirements, field allowlists, and display constraints;
- release and rollback pointers for layer versions once release governance has closed.

They do **not** contain map bytes, tiles, full style documents, source payloads, processed objects, catalog truth, proof bundles, release manifests, current operational guidance, or public UI output.

---

## Path posture

The requested and existing lane is:

```text
data/registry/layers/atmosphere/
```

This is a subtype-first registry path: registry family first (`layers`), then domain (`atmosphere`). That pattern is consistent with other subtype-first registry families such as `sources/`, `datasets/`, `domains/`, and `crosswalks/` used elsewhere in this repository sequence.

The parent currently exists only as a greenfield stub:

```text
data/registry/layers/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live layer registry records, schema validation, release integration, or governed API layer resolution already exist.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Atmosphere layer registry records | `data/registry/layers/atmosphere/` | Layer identity, Atmosphere meaning pointers, policy/evidence/release refs, caveats, and registry-local state. |
| Layer registry parent | `data/registry/layers/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Atmosphere source descriptors | `data/registry/sources/atmosphere/` after topology reconciliation | Source identity/admission records; not layer registry records. |
| Atmosphere source payloads | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/quarantine/atmosphere/`, `data/processed/atmosphere/` | Actual data belongs in lifecycle lanes, not registry records. |
| Atmosphere semantic layer meaning | `contracts/domains/atmosphere/domain_layer_descriptor.md` | Domain-specific semantic contract for Atmosphere layer constraints. |
| Generic layer contracts | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` | Generic layer descriptor, manifest, and catalog item meaning; do not duplicate here. |
| Atmosphere machine shape | `schemas/contracts/v1/domains/atmosphere/domain_layer_descriptor.schema.json` and accepted layer-registry schemas | Schema enforcement; registry schema remains NEEDS VERIFICATION. |
| Atmosphere policy and sensitivity | `policy/domains/atmosphere/`, `policy/sensitivity/atmosphere/`, `policy/rights/` | Exposure, station/sensor handling, caveats, source-role, freshness, rights, and access rules. |
| Atmosphere validation receipts | accepted validation receipt lanes | Process memory for checks. |
| Atmosphere proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Atmosphere catalog projections | `data/catalog/domain/atmosphere/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Atmosphere published layer bytes | `data/published/layers/atmosphere/` if/when accepted | Released public-safe layer artifacts and direct sidecars only. |
| Atmosphere release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Atmosphere layer boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It identifies and constrains a layer family; it does not contain layer bytes. |
| Descriptor is not a manifest | `DomainLayerDescriptor`, `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` remain separate object families. |
| Registry is not published output | Published Atmosphere map artifacts belong under a released artifact lane after release governance. |
| Knowledge character is preserved | AQI, concentration, AOD, smoke context, observations, forecasts, climate normals, climate anomalies, and advisories are distinct claim characters. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, and restricted roles must not be upgraded by styling, tiling, cataloging, release review, or generated explanation. |
| Advisory context is not KFM guidance | Atmosphere may carry evidence-labeled advisory context and official-source pointers, but KFM does not replace official advisories or emergency alerting. |
| Model fields are not observations | Forecast, HRRR, CAMS, smoke-model, climate-anomaly, and derived layers require model identity, run receipts, uncertainty/caveat notes, and source-role preservation. |
| Sensor context needs caveats | Low-cost sensors, station siting, calibration, correction, and network identity must remain visible where they affect meaning. |
| AOD and smoke context are not PM2.5 by default | Any conversion, fusion, or interpretation requires transform receipts, evidence refs, uncertainty/caveat notes, and policy review. |
| Style is not policy | Style fragments and rendering hints cannot substitute for redaction, generalization, evidence, catalog, release, or access-control decisions. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Atmosphere layer registry records and registry-local support files:

- layer-family README files and registry-local indexes;
- stable layer IDs, layer family names, and domain object-family refs;
- `DomainLayerDescriptor` refs and generic layer contract refs;
- source registry refs, dataset registry refs, crosswalk refs, and domain registry refs;
- policy refs, sensitivity refs, caveat refs, field allowlist/denylist refs, freshness refs, and access posture refs;
- validation receipt refs, proof refs, EvidenceBundle refs, catalog refs, review refs, release refs, correction refs, supersession refs, withdrawal refs, and rollback refs;
- release-readiness notes and registry-local manifests that point outward rather than duplicating authority.

Keep records compact and pointer-based. Do not embed tile payloads, source-native dumps, proof packs, policy decisions, catalog records, release manifests, or Atmosphere claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Atmosphere payloads, AQS/AirNow/NWS/Mesonet/HRRR/HMS/CAMS/GOES/VIIRS/OpenAQ/source-native extracts, station feeds, model outputs, remote-sensing scenes, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/atmosphere/`, `data/work/atmosphere/`, `data/quarantine/atmosphere/`, or `data/processed/atmosphere/` depending on lifecycle state |
| Published layer bytes, tiles, public-safe GeoParquet, released PMTiles, COGs, vector-tile bundles, tiles.json, or layer artifact sidecars | `data/published/layers/atmosphere/` after governed release |
| Source descriptor/admission records | `data/registry/sources/atmosphere/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/atmosphere/` |
| Generic layer contract meaning | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` |
| JSON Schema | `schemas/contracts/v1/...` |
| Policy rules, sensitivity rules, rights rules, access-control logic, caveat policy, or release rules | `policy/` |
| Validation receipts, transform receipts, model receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/layers/atmosphere/
├── README.md
├── air_quality_observations/
│   ├── README.md
│   └── index.local.json
├── pm25_observations/
│   ├── README.md
│   └── index.local.json
├── ozone_observations/
│   ├── README.md
│   └── index.local.json
├── smoke_context/
│   ├── README.md
│   └── index.local.json
├── aod_rasters/
│   ├── README.md
│   └── index.local.json
├── weather_observations/
│   ├── README.md
│   └── index.local.json
├── wind_fields/
│   ├── README.md
│   └── index.local.json
├── precipitation_observations/
│   ├── README.md
│   └── index.local.json
├── temperature_observations/
│   ├── README.md
│   └── index.local.json
├── climate_normals/
│   ├── README.md
│   └── index.local.json
├── climate_anomalies/
│   ├── README.md
│   └── index.local.json
├── forecast_context/
│   ├── README.md
│   └── index.local.json
├── advisory_context/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Do not create a new child lane until layer identity, object-family ownership, source role, knowledge character, sensitivity posture, caveat posture, policy refs, evidence refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact layer-registry schema remains **NEEDS VERIFICATION**. An Atmosphere layer registry record should be structured enough for audit, release readiness, correction, and rollback.

```json
{
  "id": "kfm-layer:atmosphere:<stable-layer-id>",
  "record_type": "layer_registry_record",
  "domain": "atmosphere",
  "layer_family": "air_quality_observations | pm25_observations | ozone_observations | smoke_context | aod_rasters | weather_observations | wind_fields | precipitation_observations | temperature_observations | climate_normals | climate_anomalies | forecast_context | advisory_context | other",
  "domain_layer_descriptor_refs": [],
  "generic_layer_descriptor_refs": [],
  "layer_manifest_refs": [],
  "layer_catalog_item_refs": [],
  "atmosphere_object_family_refs": [],
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "crosswalk_refs": [],
  "policy_refs": [],
  "sensitivity_refs": [],
  "freshness_refs": [],
  "caveat_refs": [],
  "validation_receipt_refs": [],
  "transform_receipt_refs": [],
  "model_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | permissioned | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm the layer record belongs in `data/registry/layers/atmosphere/`, not `data/published/layers/atmosphere/`, `data/registry/sources/atmosphere/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, or `release/`.
- [ ] Confirm the Atmosphere object family, layer family, source role, and knowledge character are identified.
- [ ] Confirm `DomainLayerDescriptor`, generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` relationships are pointer-based and not duplicated.
- [ ] Confirm AQI, concentration, AOD, PM2.5, smoke context, observations, forecasts, advisories, climate normals, climate anomalies, modeled products, and aggregates are not collapsed.
- [ ] Confirm source roles, source families, source snapshots, station/network identity, sensor context, model run context, and cross-lane ownership are preserved.
- [ ] Confirm freshness, valid time, observed time, retrieval time, issue/expiry time, correction time, and release time are preserved where material.
- [ ] Confirm station/sensor, low-cost sensor, smoke/AOD, advisory, climate, model, and sensitive-join caveats are present where required.
- [ ] Confirm validation receipts, transform receipts, model receipts, and policy outcomes exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential layer use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or time-bound layer material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/layers/atmosphere/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Atmosphere lifecycle docs require RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and say promotion is a governed state transition, not a file move. | CONFIRMED by GitHub contents API during this edit |
| Atmosphere lifecycle docs state Atmosphere/Air carries evidence-labeled observations, official contexts, and derived products, not emergency instructions. | CONFIRMED by GitHub contents API during this edit |
| Atmosphere source-registry docs point to `data/registry/sources/atmosphere/` for machine-readable source registry support and define source admission as a trust-membrane gate. | CONFIRMED by GitHub contents API during this edit |
| Atmosphere `DomainLayerDescriptor` contract exists and points to `data/registry/layers/` while warning that layer registry behavior remains unverified. | CONFIRMED by GitHub contents API during this edit |
| Concrete Atmosphere layer registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/layers/` is resolved. | NEEDS VERIFICATION |
| CI validates Atmosphere layer registry records. | UNKNOWN |
| This README grants public access to Atmosphere layer registry internals. | DENY |

---

## Maintainer note

Atmosphere layer registry records are useful because they make layer identity, Atmosphere meaning, source-role constraints, knowledge-character constraints, sensitivity posture, caveat posture, release readiness, correction, and rollback inspectable before a layer can become a governed public surface. They become dangerous when treated as layer bytes, proofs, catalog closure, release decisions, emergency guidance, or Atmosphere truth. Keep the chain explicit:

```text
layer registry record -> layer descriptor refs -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
layer registry record -> public Atmosphere map truth
```
