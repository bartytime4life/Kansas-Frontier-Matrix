<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/layers/agriculture/readme
name: Agriculture Layer Registry README
path: data/registry/layers/agriculture/README.md
type: data-registry-layer-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <layer-steward>
  - <agriculture-domain-steward>
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
registry_scope: agriculture-layer-registry-records
domain: agriculture
path_posture: existing-empty-placeholder-replaced; layer-registry-parent-currently-greenfield-stub; subtype-first-layer-registry-path-confirmed; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; aggregate-or-permissioned-only; field-level-deny-default; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../sources/README.md
  - ../../sources/agriculture/
  - ../../crosswalks/README.md
  - ../../../raw/agriculture/
  - ../../../work/agriculture/
  - ../../../quarantine/agriculture/README.md
  - ../../../processed/agriculture/
  - ../../../catalog/domain/agriculture/
  - ../../../published/layers/agriculture/
  - ../../../receipts/agriculture/README.md
  - ../../../proofs/
  - ../../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../../docs/domains/agriculture/DATA_LIFECYCLE.md
  - ../../../../docs/domains/agriculture/CANONICAL_PATHS.md
  - ../../../../docs/domains/agriculture/CONTINUITY_INVENTORY.md
  - ../../../../docs/domains/agriculture/RELEASE_INDEX.md
  - ../../../../contracts/domains/agriculture/domain_layer_descriptor.md
  - ../../../../contracts/data/layer_descriptor.md
  - ../../../../contracts/data/layer_manifest.md
  - ../../../../contracts/data/layer_catalog_item.md
  - ../../../../policy/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/agriculture/domain_layer_descriptor.schema.json
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - layers
  - agriculture
  - domain-layer-descriptor
  - layer-descriptor
  - layer-manifest
  - map-layer
  - source-role
  - rights
  - sensitivity
  - aggregation
  - field-level-deny-default
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/layers/agriculture/README.md`."
  - "The parent `data/registry/layers/README.md` is currently a greenfield stub, so layer-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Agriculture layer registry records are registry/control records. They do not store layer payloads, render tiles, prove Agriculture claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "Agriculture public posture is aggregate or permissioned only; field-level claims and private-sensitive joins fail closed until governed policy/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture Layer Registry

Subtype-first layer-registry lane for Agriculture layer registry records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Lane: layers" src="https://img.shields.io/badge/lane-layers-blue">
  <img alt="Boundary: not layer bytes" src="https://img.shields.io/badge/boundary-not%20layer%20bytes-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Agriculture layer boundary](#agriculture-layer-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/layers/agriculture/` is a registry lane for Agriculture layer identity, meaning, constraints, and release-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, published layer bytes, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Agriculture layer registry records, layer-family indexes, registry-local manifests, descriptor pointers, release-readiness pointers, and routing notes for map layers that represent Agriculture-domain material.

Agriculture layer registry records may describe:

- stable Agriculture layer identity and display-facing layer families;
- Agriculture object families represented by the layer;
- relationships to `DomainLayerDescriptor`, generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` objects;
- source-role, source-family, and cross-lane provenance constraints;
- evidence, proof, validation, catalog, policy, release, correction, and rollback references;
- sensitivity posture, aggregation posture, field-level restrictions, and permissioned-access blockers;
- public-safe summary requirements, allowed geometry precision, field allowlists, and join-safety notes;
- release and rollback pointers for layer versions once release governance has closed.

They do **not** contain map bytes, tiles, full style documents, source payloads, processed objects, catalog truth, proof bundles, release manifests, or public UI output.

---

## Path posture

The requested and existing lane is:

```text
data/registry/layers/agriculture/
```

This is a subtype-first registry path: registry family first (`layers`), then domain (`agriculture`). That pattern is consistent with other subtype-first registry families such as `sources/`, `datasets/`, `domains/`, and `crosswalks/` used elsewhere in this repository sequence.

The parent currently exists only as a greenfield stub:

```text
data/registry/layers/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live layer registry records, schema validation, release integration, or governed API layer resolution already exist.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Agriculture layer registry records | `data/registry/layers/agriculture/` | Layer identity, Agriculture meaning pointers, policy/evidence/release refs, and registry-local state. |
| Layer registry parent | `data/registry/layers/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Agriculture source descriptors | `data/registry/sources/agriculture/` after topology reconciliation | Source identity/admission records; not layer registry records. |
| Agriculture source payloads | `data/raw/agriculture/`, `data/work/agriculture/`, `data/quarantine/agriculture/`, `data/processed/agriculture/` | Actual data belongs in lifecycle lanes, not registry records. |
| Agriculture semantic layer meaning | `contracts/domains/agriculture/domain_layer_descriptor.md` | Domain-specific semantic contract for Agriculture layer constraints. |
| Generic layer contracts | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` | Generic layer descriptor, manifest, and catalog item meaning; do not duplicate here. |
| Agriculture machine shape | `schemas/contracts/v1/domains/agriculture/domain_layer_descriptor.schema.json` and accepted layer-registry schemas | Schema enforcement; registry schema remains NEEDS VERIFICATION. |
| Agriculture policy and sensitivity | `policy/domains/agriculture/`, `policy/sensitivity/agriculture/`, `policy/rights/` | Exposure, aggregation, field-level, rights, and access rules. |
| Agriculture validation receipts | `data/receipts/agriculture/` and accepted validation receipt lanes | Process memory for checks. |
| Agriculture proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Agriculture catalog projections | `data/catalog/domain/agriculture/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Agriculture published layer bytes | `data/published/layers/agriculture/` if/when accepted | Released public-safe layer artifacts and direct sidecars only. |
| Agriculture release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Agriculture layer boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It identifies and constrains a layer family; it does not contain layer bytes. |
| Descriptor is not a manifest | `DomainLayerDescriptor`, `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` remain separate object families. |
| Registry is not published output | Published Agriculture map artifacts belong under a released artifact lane after release governance. |
| Field-level fails closed | Field-level NASS-style claims, farm-operator private data, proprietary yield, pesticide records, and private-sensitive joins require denial, restriction, permissioning, aggregation, or review before exposure. |
| Aggregation is load-bearing | Public Agriculture posture is aggregate or permissioned only; aggregation scope, method, and receipt references must remain visible. |
| Cross-lane joins preserve ownership | Soil, Hydrology, People/Land, Geology, Atmosphere, Habitat, Fauna, Flora, and Hazards claims remain owned by their respective lanes. |
| Source role is preserved | Source roles must not be upgraded by map styling, tiling, cataloging, release review, or generated explanation. |
| Style is not policy | Style fragments and rendering hints cannot substitute for redaction, generalization, evidence, catalog, release, or access-control decisions. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Agriculture layer registry records and registry-local support files:

- layer-family README files and registry-local indexes;
- stable layer IDs, layer family names, and domain object-family refs;
- `DomainLayerDescriptor` refs and generic layer contract refs;
- source registry refs, dataset registry refs, crosswalk refs, and domain registry refs;
- policy refs, sensitivity refs, field allowlist/denylist refs, aggregation refs, and access posture refs;
- validation receipt refs, proof refs, EvidenceBundle refs, catalog refs, review refs, release refs, correction refs, supersession refs, withdrawal refs, and rollback refs;
- release-readiness notes and registry-local manifests that point outward rather than duplicating authority.

Keep records compact and pointer-based. Do not embed tile payloads, source-native dumps, proof packs, policy decisions, catalog records, release manifests, or Agriculture claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Agriculture payloads, NASS/CDL/crop/yield/source-native extracts, field records, remote-sensing scenes, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/agriculture/`, `data/work/agriculture/`, `data/quarantine/agriculture/`, or `data/processed/agriculture/` depending on lifecycle state |
| Published layer bytes, tiles, public-safe GeoParquet, released PMTiles, COGs, vector-tile bundles, tiles.json, or layer artifact sidecars | `data/published/layers/agriculture/` after governed release |
| Source descriptor/admission records | `data/registry/sources/agriculture/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/agriculture/` |
| Generic layer contract meaning | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` |
| JSON Schema | `schemas/contracts/v1/...` |
| Policy rules, sensitivity rules, rights rules, access-control logic, aggregation policy, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, aggregation receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/layers/agriculture/
├── README.md
├── crop_observations/
│   ├── README.md
│   └── index.local.json
├── crop_progress/
│   ├── README.md
│   └── index.local.json
├── drought_stress/
│   ├── README.md
│   └── index.local.json
├── pest_stress/
│   ├── README.md
│   └── index.local.json
├── irrigation_links/
│   ├── README.md
│   └── index.local.json
├── conservation_practices/
│   ├── README.md
│   └── index.local.json
├── soil_crop_suitability/
│   ├── README.md
│   └── index.local.json
├── agricultural_economy/
│   ├── README.md
│   └── index.local.json
├── supply_chain_nodes/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Do not create a new child lane until layer identity, object-family ownership, sensitivity posture, source-role posture, policy refs, evidence refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact layer-registry schema remains **NEEDS VERIFICATION**. An Agriculture layer registry record should be structured enough for audit, release readiness, correction, and rollback.

```json
{
  "id": "kfm-layer:agriculture:<stable-layer-id>",
  "record_type": "layer_registry_record",
  "domain": "agriculture",
  "layer_family": "crop_observations | crop_progress | drought_stress | pest_stress | irrigation_links | conservation_practices | soil_crop_suitability | agricultural_economy | supply_chain_nodes | other",
  "domain_layer_descriptor_refs": [],
  "generic_layer_descriptor_refs": [],
  "layer_manifest_refs": [],
  "layer_catalog_item_refs": [],
  "agriculture_object_family_refs": [],
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "crosswalk_refs": [],
  "policy_refs": [],
  "sensitivity_refs": [],
  "aggregation_receipt_refs": [],
  "validation_receipt_refs": [],
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

- [ ] Confirm the layer record belongs in `data/registry/layers/agriculture/`, not `data/published/layers/agriculture/`, `data/registry/sources/agriculture/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, or `release/`.
- [ ] Confirm the Agriculture object family and layer family are identified.
- [ ] Confirm `DomainLayerDescriptor`, generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` relationships are pointer-based and not duplicated.
- [ ] Confirm source roles, source families, source snapshots, and cross-lane ownership are preserved.
- [ ] Confirm field-level, farm/operator, proprietary, pesticide, person-parcel, and private-sensitive joins fail closed unless permissioning, aggregation, redaction, review, and release gates explicitly permit a derivative.
- [ ] Confirm aggregation scope, method, denominator, geography, time period, and `AggregationReceipt` references where public aggregation is used.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential layer use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, and rollback paths exist for mutable or externally governed layer material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/layers/agriculture/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Agriculture lifecycle docs require RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and say promotion is a governed state transition, not a file move. | CONFIRMED by GitHub contents API during this edit |
| Agriculture lifecycle docs state public posture is aggregate-default and field-level deny-by-default. | CONFIRMED by GitHub contents API during this edit |
| Agriculture source-registry docs point to `data/registry/sources/agriculture/` for per-source records and mark source registry as admission/authority control. | CONFIRMED by GitHub contents API during this edit |
| Agriculture `DomainLayerDescriptor` contract exists and points to `data/registry/layers/` while warning that schema/validator/layer registry behavior remain unverified. | CONFIRMED by GitHub contents API during this edit |
| A Hydrology published-layer README exists as precedent separating published layer artifacts from registry, proof, receipts, release, and source input. | CONFIRMED by GitHub contents API during this edit |
| Concrete Agriculture layer registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/layers/` is resolved. | NEEDS VERIFICATION |
| CI validates Agriculture layer registry records. | UNKNOWN |
| This README grants public access to Agriculture layer registry internals. | DENY |

---

## Maintainer note

Agriculture layer registry records are useful because they make layer identity, Agriculture meaning, source-role constraints, sensitivity posture, aggregation posture, release readiness, correction, and rollback inspectable before a layer can become a governed public surface. They become dangerous when treated as layer bytes, proofs, catalog closure, release decisions, or Agriculture truth. Keep the chain explicit:

```text
layer registry record -> layer descriptor refs -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
layer registry record -> public Agriculture map truth
```
