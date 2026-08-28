<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/layers/flora/readme
name: Flora Layer Registry README
path: data/registry/layers/flora/README.md
type: data-registry-layer-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <layer-steward>
  - <flora-domain-steward>
  - <map-layer-steward>
  - <policy-steward>
  - <sensitivity-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: flora-layer-registry-records
domain: flora
path_posture: existing-empty-placeholder-replaced; layer-registry-parent-currently-greenfield-stub; subtype-first-layer-registry-path-confirmed; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; rare-plant-deny-default; culturally-sensitive-plant-knowledge-protected; exact-sensitive-geometry-fail-closed; source-role-preserving; redaction-receipt-required-for-public-safe-derivatives; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../datasets/flora/README.md
  - ../../sources/README.md
  - ../../sources/flora/
  - ../../flora/README.md
  - ../../flora/sources/README.md
  - ../../crosswalks/README.md
  - ../../../raw/flora/
  - ../../../work/flora/
  - ../../../quarantine/flora/
  - ../../../processed/flora/
  - ../../../catalog/domain/flora/
  - ../../../catalog/stac/flora/README.md
  - ../../../published/layers/flora/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../../docs/domains/flora/OBJECT_FAMILIES.md
  - ../../../../docs/domains/flora/MAP_UI_CONTRACTS.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../contracts/domains/flora/domain_layer_descriptor.md
  - ../../../../contracts/data/layer_descriptor.md
  - ../../../../contracts/data/layer_manifest.md
  - ../../../../contracts/data/layer_catalog_item.md
  - ../../../../policy/domains/flora/
  - ../../../../policy/sensitivity/flora/
  - ../../../../policy/geoprivacy/
  - ../../../../schemas/contracts/v1/domains/flora/domain_layer_descriptor.schema.json
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - layers
  - flora
  - domain-layer-descriptor
  - layer-descriptor
  - layer-manifest
  - map-layer
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - redaction
  - rare-plants
  - culturally-sensitive-plants
  - occurrence-summary
  - vegetation-community
  - invasive-plants
  - phenology
  - range-polygon
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/layers/flora/README.md`."
  - "The parent `data/registry/layers/README.md` is currently a greenfield stub, so layer-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "Flora layer registry records are registry/control records. They do not store layer payloads, render tiles, prove Flora claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "Exact rare/protected/culturally sensitive plant locations are denied on public surfaces by default; public-safe Flora layer derivatives require review, redaction/generalization, receipts, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Layer Registry

Subtype-first layer-registry lane for Flora layer registry records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Lane: layers" src="https://img.shields.io/badge/lane-layers-blue">
  <img alt="Boundary: not layer bytes" src="https://img.shields.io/badge/boundary-not%20layer%20bytes-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Flora layer boundary](#flora-layer-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/layers/flora/` is a registry lane for Flora layer identity, meaning, constraints, sensitivity posture, and release-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, published layer bytes, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Flora layer registry records, layer-family indexes, registry-local manifests, descriptor pointers, release-readiness pointers, and routing notes for map layers that represent Flora-domain material.

Flora layer registry records may describe:

- stable Flora layer identity and display-facing layer families;
- Flora object families represented by the layer;
- relationships to `DomainLayerDescriptor`, generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` objects;
- source-role, source-family, redaction, sensitivity, geoprivacy, temporal, and cross-lane provenance constraints;
- evidence, proof, validation, redaction, catalog, policy, review, release, correction, and rollback references;
- public-safe summary requirements, allowed geometry precision, withheld-detail posture, trust badges, caveats, field allowlists, and negative states;
- release and rollback pointers for layer versions once release governance has closed.

They do **not** contain map bytes, tiles, full style documents, source payloads, processed objects, catalog truth, proof bundles, release manifests, sensitive plant details, or public UI output.

---

## Path posture

The requested and existing lane is:

```text
data/registry/layers/flora/
```

This is a subtype-first registry path: registry family first (`layers`), then domain (`flora`). That pattern is consistent with other subtype-first registry families such as `sources/`, `datasets/`, `domains/`, and `crosswalks/` used elsewhere in this repository sequence.

The parent currently exists only as a greenfield stub:

```text
data/registry/layers/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live layer registry records, schema validation, release integration, or governed API layer resolution already exist.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Flora layer registry records | `data/registry/layers/flora/` | Layer identity, Flora meaning pointers, sensitivity posture, policy/evidence/release refs, and registry-local state. |
| Layer registry parent | `data/registry/layers/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Flora source descriptors | `data/registry/sources/flora/` and/or reconciled Flora source registry lanes | Source identity/admission records; not layer registry records. |
| Flora dataset registry records | `data/registry/datasets/flora/` | Dataset identity and dataset-state records; not layer identity. |
| Flora source payloads | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` | Actual data belongs in lifecycle lanes, not registry records. |
| Flora semantic layer meaning | `contracts/domains/flora/domain_layer_descriptor.md` | Domain-specific semantic contract for Flora layer constraints. |
| Generic layer contracts | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` | Generic layer descriptor, manifest, and catalog item meaning; do not duplicate here. |
| Flora machine shape | `schemas/contracts/v1/domains/flora/domain_layer_descriptor.schema.json` and accepted layer-registry schemas | Schema enforcement; registry schema remains NEEDS VERIFICATION. |
| Flora policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, redaction, geoprivacy, source-role, rights, and access rules. |
| Flora validation/redaction receipts | accepted validation and redaction receipt lanes | Process memory for checks and public-safe transforms. |
| Flora proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Flora catalog projections | `data/catalog/domain/flora/`, `data/catalog/stac/flora/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Flora published layer bytes | `data/published/layers/flora/` if/when accepted | Released public-safe layer artifacts and direct sidecars only. |
| Flora release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Flora layer boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It identifies and constrains a layer family; it does not contain layer bytes. |
| Descriptor is not a manifest | `DomainLayerDescriptor`, `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` remain separate object families. |
| Registry is not published output | Published Flora map artifacts belong under a released artifact lane after release governance. |
| Exact sensitive plant geography fails closed | Exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default unless policy, steward review, redaction/generalization, receipts, release, correction, and rollback support explicitly permit a public-safe derivative. |
| Public-safe does not mean exact | A generalized, aggregated, fuzzed, withheld, or denied display state may be the correct public answer. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, and restricted roles must not be upgraded by styling, tiling, cataloging, release review, or generated explanation. |
| Layer is not Flora truth | Layers, tiles, styles, and UI surfaces are downstream carriers. EvidenceBundle, policy, review, and release state carry authority. |
| Culturally sensitive plant knowledge is protected | CARE/sovereignty-sensitive and steward-controlled knowledge must remain restricted unless reviewed and released under the appropriate audience and transform. |
| Join-induced sensitivity is inherited | Private-land, parcel, archaeology, habitat, fauna, or other joins may raise the sensitivity tier; the most restrictive applicable posture governs. |
| Style is not policy | Style fragments and rendering hints cannot substitute for redaction, generalization, evidence, catalog, release, or access-control decisions. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Flora layer registry records and registry-local support files:

- layer-family README files and registry-local indexes;
- stable layer IDs, layer family names, and domain object-family refs;
- `DomainLayerDescriptor` refs and generic layer contract refs;
- source registry refs, dataset registry refs, crosswalk refs, and domain registry refs;
- policy refs, sensitivity refs, geoprivacy refs, redaction refs, field allowlist/denylist refs, trust-badge refs, and access posture refs;
- validation receipt refs, RedactionReceipt refs, proof refs, EvidenceBundle refs, catalog refs, review refs, release refs, correction refs, supersession refs, withdrawal refs, and rollback refs;
- release-readiness notes and registry-local manifests that point outward rather than duplicating authority.

Keep records compact and pointer-based. Do not embed tile payloads, source-native dumps, proof packs, policy decisions, catalog records, release manifests, or Flora claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora payloads, herbarium archives, Darwin Core exports, occurrence exports, taxonomy tables, vegetation datasets, invasive records, phenology feeds, restoration records, remote-sensing scenes, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, or `data/processed/flora/` depending on lifecycle state |
| Published layer bytes, tiles, public-safe GeoParquet, released PMTiles, COGs, vector-tile bundles, tiles.json, or layer artifact sidecars | `data/published/layers/flora/` after governed release |
| Exact rare/protected/culturally sensitive plant coordinates, steward-only notes, culturally sensitive plant knowledge, private identifiers, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Source descriptor/admission records | `data/registry/sources/flora/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/flora/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/flora/` |
| Generic layer contract meaning | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` |
| JSON Schema | `schemas/contracts/v1/...` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, redaction policy, or release rules | `policy/` |
| Validation receipts, redaction receipts, transform receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/layers/flora/
├── README.md
├── occurrence_summary/
│   ├── README.md
│   └── index.local.json
├── rare_plant_generalized/
│   ├── README.md
│   └── index.local.json
├── vegetation_communities/
│   ├── README.md
│   └── index.local.json
├── invasive_plants/
│   ├── README.md
│   └── index.local.json
├── phenology/
│   ├── README.md
│   └── index.local.json
├── range_polygons/
│   ├── README.md
│   └── index.local.json
├── habitat_associations/
│   ├── README.md
│   └── index.local.json
├── botanical_survey_effort/
│   ├── README.md
│   └── index.local.json
├── restoration_plantings/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Do not create a new child lane until layer identity, object-family ownership, source role, sensitivity posture, redaction posture, policy refs, evidence refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact layer-registry schema remains **NEEDS VERIFICATION**. A Flora layer registry record should be structured enough for audit, release readiness, correction, and rollback.

```json
{
  "id": "kfm-layer:flora:<stable-layer-id>",
  "record_type": "layer_registry_record",
  "domain": "flora",
  "layer_family": "occurrence_summary | rare_plant_generalized | vegetation_communities | invasive_plants | phenology | range_polygons | habitat_associations | botanical_survey_effort | restoration_plantings | other",
  "domain_layer_descriptor_refs": [],
  "generic_layer_descriptor_refs": [],
  "layer_manifest_refs": [],
  "layer_catalog_item_refs": [],
  "flora_object_family_refs": [],
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "crosswalk_refs": [],
  "policy_refs": [],
  "sensitivity_refs": [],
  "geoprivacy_refs": [],
  "redaction_receipt_refs": [],
  "validation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | generalized-public-safe | permissioned | restricted | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm the layer record belongs in `data/registry/layers/flora/`, not `data/published/layers/flora/`, `data/registry/sources/flora/`, `data/registry/datasets/flora/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, or `release/`.
- [ ] Confirm the Flora object family, layer family, source role, sensitivity posture, and public exposure posture are identified.
- [ ] Confirm `DomainLayerDescriptor`, generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` relationships are pointer-based and not duplicated.
- [ ] Confirm exact rare/protected/culturally sensitive plant locations and culturally sensitive plant knowledge fail closed unless public-safe transform, steward review, RedactionReceipt, release state, correction path, and rollback target are present.
- [ ] Confirm source roles, source families, source snapshots, taxonomy/crosswalk posture, temporal scope, and cross-lane ownership are preserved.
- [ ] Confirm geoprivacy, generalization, aggregation, withholding, suppression, or denial states are visible where required.
- [ ] Confirm private-land, parcel, archaeology, habitat, fauna, or other joins inherit the most restrictive applicable sensitivity posture.
- [ ] Confirm validation receipts, redaction receipts, and policy outcomes exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential layer use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or sensitive layer material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/layers/flora/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Flora `DomainLayerDescriptor` contract exists and states that layer descriptors do not make layers truth, do not authorize rare-plant geometry exposure, and do not replace release, policy, review, or EvidenceBundle resolution. | CONFIRMED by GitHub contents API during this edit |
| Flora sensitivity docs state exact rare/protected/culturally sensitive plant locations are denied on public surfaces by default and require steward review, transformed geometry, and RedactionReceipt for public release. | CONFIRMED by GitHub contents API during this edit |
| Flora lifecycle docs require RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and state promotion is a governed state transition, not a file move. | CONFIRMED by GitHub contents API during this edit |
| Concrete Flora layer registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/layers/` is resolved. | NEEDS VERIFICATION |
| CI validates Flora layer registry records. | UNKNOWN |
| This README grants public access to Flora layer registry internals. | DENY |

---

## Maintainer note

Flora layer registry records are useful because they make layer identity, Flora meaning, source-role constraints, sensitivity posture, redaction posture, release readiness, correction, and rollback inspectable before a layer can become a governed public surface. They become dangerous when treated as layer bytes, proofs, catalog closure, release decisions, or Flora truth. Keep the chain explicit:

```text
layer registry record -> layer descriptor refs -> lifecycle payload -> validation/redaction receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
layer registry record -> public Flora map truth
```
