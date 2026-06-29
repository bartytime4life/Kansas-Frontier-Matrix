<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/layers/habitat/readme
name: Habitat Layer Registry README
path: data/registry/layers/habitat/README.md
type: data-registry-layer-domain-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <layer-steward>
  - <habitat-domain-steward>
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
registry_scope: habitat-layer-registry-records
domain: habitat
path_posture: existing-empty-placeholder-replaced; layer-registry-parent-currently-greenfield-stub; subtype-first-layer-registry-path-confirmed; habitat-domain-layer-descriptor-not-verified; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; sensitive-joins-fail-closed; occurrence-context-not-habitat-truth; most-restrictive-joined-tier-governs; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../domains/README.md
  - ../../datasets/README.md
  - ../../sources/README.md
  - ../../sources/habitat/
  - ../../habitat/README.md
  - ../../habitat/sources/README.md
  - ../../crosswalks/README.md
  - ../../../raw/habitat/
  - ../../../work/habitat/
  - ../../../quarantine/habitat/
  - ../../../processed/habitat/
  - ../../../catalog/domain/habitat/
  - ../../../published/layers/habitat/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/HABITAT_SOURCE_LEDGER.md
  - ../../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../../docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/habitat/HABITAT_DOMAIN_MODEL.md
  - ../../../../docs/domains/habitat/FILE_SYSTEM_PLAN.md
  - ../../../../docs/domains/habitat/ARCHITECTURE.md
  - ../../../../contracts/domains/habitat/
  - ../../../../contracts/data/layer_descriptor.md
  - ../../../../contracts/data/layer_manifest.md
  - ../../../../contracts/data/layer_catalog_item.md
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../policy/geoprivacy/
  - ../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - layers
  - habitat
  - domain-layer-descriptor
  - layer-descriptor
  - layer-manifest
  - map-layer
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - occurrence-context
  - sensitive-joins
  - land-cover
  - wetlands
  - ecological-systems
  - critical-habitat
  - stewardship
  - suitability
  - connectivity
  - corridors
  - restoration
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/layers/habitat/README.md`."
  - "The parent `data/registry/layers/README.md` is currently a greenfield stub, so layer-registry topology and canonical record shape remain NEEDS VERIFICATION."
  - "A Habitat-specific `domain_layer_descriptor.md` was not verified during this edit; use generic layer contracts and Habitat object contracts as pointers until a Habitat domain-layer descriptor is created or discovered."
  - "Habitat layer registry records are registry/control records. They do not store layer payloads, render tiles, prove Habitat claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "Sensitive joins, occurrence-context inputs, controlled ecological records, rights-unclear feeds, and source-role conflicts fail closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Layer Registry

Subtype-first layer-registry lane for Habitat layer registry records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: layers" src="https://img.shields.io/badge/lane-layers-blue">
  <img alt="Boundary: not layer bytes" src="https://img.shields.io/badge/boundary-not%20layer%20bytes-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Habitat layer boundary](#habitat-layer-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/layers/habitat/` is a registry lane for Habitat layer identity, meaning, constraints, sensitivity posture, and release-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, published layer bytes, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and may hold Habitat layer registry records, layer-family indexes, registry-local manifests, descriptor pointers, release-readiness pointers, and routing notes for map layers that represent Habitat-domain material.

Habitat layer registry records may describe:

- stable Habitat layer identity and display-facing layer families;
- Habitat object families represented by the layer;
- relationships to generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` objects, plus any future Habitat `DomainLayerDescriptor` once verified;
- source-role, source-family, sensitivity, geoprivacy, temporal, uncertainty, and cross-lane provenance constraints;
- evidence, proof, validation, catalog, policy, review, release, correction, and rollback references;
- public-safe summary requirements, allowed geometry precision, generalized/suppressed detail posture, trust badges, caveats, field allowlists, and negative states;
- release and rollback pointers for layer versions once release governance has closed.

They do **not** contain map bytes, tiles, full style documents, source payloads, processed objects, catalog truth, proof bundles, release manifests, sensitive joined detail, or public UI output.

---

## Path posture

The requested and existing lane is:

```text
data/registry/layers/habitat/
```

This is a subtype-first registry path: registry family first (`layers`), then domain (`habitat`). That pattern is consistent with other subtype-first registry families such as `sources/`, `datasets/`, `domains/`, and `crosswalks` used elsewhere in this repository sequence.

The parent currently exists only as a greenfield stub:

```text
data/registry/layers/README.md
```

Therefore, this README treats the target path as **CONFIRMED path presence / NEEDS VERIFICATION canonical shape**. Do not treat this README as proof that live layer registry records, schema validation, release integration, or governed API layer resolution already exist.

A Habitat-specific `contracts/domains/habitat/domain_layer_descriptor.md` was not verified during this edit. Until such a contract is created or discovered, this README treats Habitat layer registry records as pointer-based records that must reference generic layer contracts, Habitat object contracts, source descriptors, policy, evidence, release, and rollback state without inventing a live semantic contract.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Habitat layer registry records | `data/registry/layers/habitat/` | Layer identity, Habitat meaning pointers, sensitivity posture, policy/evidence/release refs, and registry-local state. |
| Layer registry parent | `data/registry/layers/README.md` | Parent is currently a greenfield stub; canonical parent contract remains NEEDS VERIFICATION. |
| Habitat source descriptors | `data/registry/sources/habitat/` and/or reconciled Habitat source registry lanes | Source identity/admission records; not layer registry records. |
| Habitat source payloads | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/` | Actual data belongs in lifecycle lanes, not registry records. |
| Habitat semantic object meaning | `contracts/domains/habitat/` | Habitat object-family meaning; a Habitat domain-layer descriptor remains NEEDS VERIFICATION. |
| Generic layer contracts | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` | Generic layer descriptor, manifest, and catalog item meaning; do not duplicate here. |
| Habitat machine shape | `schemas/contracts/v1/domains/habitat/` and accepted layer-registry schemas | Schema enforcement; registry schema remains NEEDS VERIFICATION. |
| Habitat policy and sensitivity | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, sensitive joins, occurrence context, rights, and access rules. |
| Habitat validation/redaction receipts | accepted validation and redaction receipt lanes | Process memory for checks and public-safe transforms. |
| Habitat proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Habitat catalog projections | `data/catalog/domain/habitat/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Habitat published layer bytes | `data/published/layers/habitat/` if/when accepted | Released public-safe layer artifacts and direct sidecars only. |
| Habitat release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Habitat layer boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It identifies and constrains a layer family; it does not contain layer bytes. |
| Descriptor is not a manifest | `LayerDescriptor`, `LayerManifest`, `LayerCatalogItem`, and any future Habitat `DomainLayerDescriptor` remain separate object families. |
| Registry is not published output | Published Habitat map artifacts belong under a released artifact lane after release governance. |
| Habitat does not own occurrence truth | Flora/Fauna occurrence records and occurrence aggregators are join context unless the owning lane releases a public-safe derivative. |
| Sensitive joins fail closed | Joins to sensitive Flora, Fauna, heritage, stewardship, restricted ecological records, private parcels, or protected context inherit the most restrictive applicable posture. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, occurrence-context, and restricted roles must not be upgraded by styling, tiling, cataloging, release review, or generated explanation. |
| Regulatory and modeled layers stay scoped | Critical-habitat designations, wetland inventories, suitability layers, connectivity, corridors, stewardship zones, restoration priorities, and modeled products must preserve source role and authority limits. |
| Public-safe does not mean exact | A generalized, aggregated, fuzzed, withheld, or denied display state may be the correct public answer. |
| Style is not policy | Style fragments and rendering hints cannot substitute for redaction, generalization, evidence, catalog, release, or access-control decisions. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Habitat layer registry records and registry-local support files:

- layer-family README files and registry-local indexes;
- stable layer IDs, layer family names, and domain object-family refs;
- generic layer contract refs and, when verified, Habitat domain-layer descriptor refs;
- source registry refs, dataset registry refs, crosswalk refs, and domain registry refs;
- policy refs, sensitivity refs, geoprivacy refs, redaction refs, field allowlist/denylist refs, trust-badge refs, uncertainty refs, and access posture refs;
- validation receipt refs, redaction/generalization receipt refs, proof refs, EvidenceBundle refs, catalog refs, review refs, release refs, correction refs, supersession refs, withdrawal refs, and rollback refs;
- release-readiness notes and registry-local manifests that point outward rather than duplicating authority.

Keep records compact and pointer-based. Do not embed tile payloads, source-native dumps, proof packs, policy decisions, catalog records, release manifests, or Habitat claim content in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Habitat payloads, NLCD/NWI/GAP/LANDFIRE/USFWS/NatureServe/KDWP/PAD-US/occurrence-context extracts, field-survey products, remote-sensing scenes, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, or `data/processed/habitat/` depending on lifecycle state |
| Published layer bytes, tiles, public-safe GeoParquet, released PMTiles, COGs, vector-tile bundles, tiles.json, or layer artifact sidecars | `data/published/layers/habitat/` after governed release |
| Sensitive joined detail, steward-only notes, controlled ecological records, protected occurrence-derived locations, private identifiers, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Source descriptor/admission records | `data/registry/sources/habitat/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/habitat/` |
| Generic layer contract meaning | `contracts/data/layer_descriptor.md`, `contracts/data/layer_manifest.md`, `contracts/data/layer_catalog_item.md` |
| JSON Schema | `schemas/contracts/v1/...` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, redaction policy, or release rules | `policy/` |
| Validation receipts, redaction receipts, transform receipts, model receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/layers/habitat/
├── README.md
├── habitat_patches/
│   ├── README.md
│   └── index.local.json
├── land_cover_observations/
│   ├── README.md
│   └── index.local.json
├── wetlands_context/
│   ├── README.md
│   └── index.local.json
├── ecological_systems/
│   ├── README.md
│   └── index.local.json
├── critical_habitat/
│   ├── README.md
│   └── index.local.json
├── suitability_surfaces/
│   ├── README.md
│   └── index.local.json
├── connectivity_edges/
│   ├── README.md
│   └── index.local.json
├── corridors/
│   ├── README.md
│   └── index.local.json
├── restoration_opportunities/
│   ├── README.md
│   └── index.local.json
├── stewardship_zones/
│   ├── README.md
│   └── index.local.json
├── uncertainty_surfaces/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Do not create a new child lane until layer identity, object-family ownership, source role, sensitivity posture, redaction posture, policy refs, evidence refs, release refs, and rollback path are known.

---

## Suggested registry shape

The exact layer-registry schema remains **NEEDS VERIFICATION**. A Habitat layer registry record should be structured enough for audit, release readiness, correction, and rollback.

```json
{
  "id": "kfm-layer:habitat:<stable-layer-id>",
  "record_type": "layer_registry_record",
  "domain": "habitat",
  "layer_family": "habitat_patches | land_cover_observations | wetlands_context | ecological_systems | critical_habitat | suitability_surfaces | connectivity_edges | corridors | restoration_opportunities | stewardship_zones | uncertainty_surfaces | other",
  "domain_layer_descriptor_refs": [],
  "generic_layer_descriptor_refs": [],
  "layer_manifest_refs": [],
  "layer_catalog_item_refs": [],
  "habitat_object_family_refs": [],
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "crosswalk_refs": [],
  "policy_refs": [],
  "sensitivity_refs": [],
  "geoprivacy_refs": [],
  "redaction_receipt_refs": [],
  "validation_receipt_refs": [],
  "model_receipt_refs": [],
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

- [ ] Confirm the layer record belongs in `data/registry/layers/habitat/`, not `data/published/layers/habitat/`, `data/registry/sources/habitat/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, or `release/`.
- [ ] Confirm the Habitat object family, layer family, source role, sensitivity posture, and public exposure posture are identified.
- [ ] Confirm generic `LayerDescriptor`, `LayerManifest`, and `LayerCatalogItem` relationships are pointer-based and not duplicated.
- [ ] Confirm any Habitat `DomainLayerDescriptor` reference resolves to a verified contract before using it as an authority pointer.
- [ ] Confirm Habitat does not claim ownership of Flora/Fauna occurrence truth unless the owning lane releases a public-safe derivative.
- [ ] Confirm sensitive joins, occurrence-context inputs, protected species context, stewardship context, private parcel joins, or restricted ecological records inherit the most restrictive applicable sensitivity posture.
- [ ] Confirm source roles, source families, source snapshots, class-system versions, model/run context, uncertainty posture, temporal scope, and cross-lane ownership are preserved.
- [ ] Confirm geoprivacy, generalization, aggregation, withholding, suppression, or denial states are visible where required.
- [ ] Confirm validation receipts, redaction/generalization receipts, model receipts, and policy outcomes exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential layer use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or sensitive layer material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/layers/habitat/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| A Habitat-specific `contracts/domains/habitat/domain_layer_descriptor.md` was found during this edit. | UNKNOWN / NOT VERIFIED |
| Habitat source ledger says source admission is deny-by-default until reviewed SourceDescriptor and SourceActivationDecision exist. | CONFIRMED by GitHub contents API during this edit |
| Habitat source ledger says occurrence aggregators are occurrence-context and Habitat does not own occurrence truth. | CONFIRMED by GitHub contents API during this edit |
| Habitat source-registry docs define the source registry as admission and authority control, not a bibliography, truth store, or publication authority. | CONFIRMED by GitHub contents API during this edit |
| Habitat lifecycle docs require RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and say promotion is a governed state transition, not a file move. | CONFIRMED by GitHub contents API during this edit |
| Concrete Habitat layer registry payloads exist under this requested lane. | UNKNOWN |
| The final accepted parent contract for `data/registry/layers/` is resolved. | NEEDS VERIFICATION |
| CI validates Habitat layer registry records. | UNKNOWN |
| This README grants public access to Habitat layer registry internals. | DENY |

---

## Maintainer note

Habitat layer registry records are useful because they make layer identity, Habitat meaning, source-role constraints, sensitivity posture, join posture, release readiness, correction, and rollback inspectable before a layer can become a governed public surface. They become dangerous when treated as layer bytes, proofs, catalog closure, release decisions, or Habitat truth. Keep the chain explicit:

```text
layer registry record -> layer descriptor refs -> lifecycle payload -> validation/redaction/model receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
layer registry record -> public Habitat map truth
```
