<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/datasets/flora/readme
name: Flora Dataset Registry README
path: data/registry/datasets/flora/README.md
type: data-registry-datasets-domain-readme
version: v0.1.0
status: draft
owners:
  - <registry-steward>
  - <dataset-steward>
  - <flora-domain-steward>
  - <source-steward>
  - <catalog-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: flora-dataset-registry-records
domain: flora
path_posture: existing-empty-placeholder-replaced; parent-datasets-registry-stub-confirmed; exact-dataset-registry-layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; rare-plant-deny-default; source-role-preserving; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../crosswalks/README.md
  - ../../../raw/flora/
  - ../../../work/flora/
  - ../../../quarantine/flora/
  - ../../../processed/flora/
  - ../../../catalog/stac/flora/README.md
  - ../../../catalog/domain/flora/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/sources/catalog/gbif/async-download.md
  - ../../../../docs/sources/catalog/natureserve/sensitive-taxa-list.md
  - ../../../../docs/sources/catalog/kansas/kdwp.md
  - ../../../../contracts/domains/flora/
  - ../../../../schemas/contracts/v1/domains/flora/
  - ../../../../policy/domains/flora/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - datasets
  - flora
  - dataset-identity
  - source-role
  - evidence
  - provenance
  - rights
  - sensitivity
  - rare-plant
  - geoprivacy
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/datasets/flora/README.md`."
  - "Flora dataset registry records describe dataset identity, role, scope, provenance, rights, cadence, sensitivity posture, lifecycle links, and downstream eligibility. They do not store source payloads or publish data."
  - "Flora exact rare, protected, or culturally sensitive plant locations remain denied on public surfaces by default unless transformed, reviewed, receipted, and released through governed gates."
  - "Concrete dataset registry schemas, validators, examples, CI enforcement, and emitted records remain NEEDS VERIFICATION until inspected."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Dataset Registry

Governed registry lane for Flora dataset identity and dataset-state records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: datasets" src="https://img.shields.io/badge/lane-datasets-blue">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Dataset boundary](#dataset-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested record shape](#suggested-record-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/datasets/flora/` is a registry lane for Flora dataset identity and dataset-state records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, policy, release authority, or a public API/UI surface.

---

## Scope

This directory documents and should eventually hold Flora dataset registry records: stable descriptions of dataset identity, dataset family, source authority, source role, rights posture, retrieval/update cadence, lifecycle linkage, sensitivity posture, evidence requirements, catalog expectations, release eligibility, correction posture, and rollback dependencies.

A Flora dataset registry record may describe dataset families such as:

- taxon backbone or taxon list datasets;
- herbarium specimen datasets;
- occurrence datasets;
- rare/protected/sensitive plant datasets;
- vegetation community datasets;
- invasive plant datasets;
- phenology datasets;
- range/distribution polygon datasets;
- restoration planting datasets;
- public-safe generalized Flora derivative datasets.

A registry record is not the dataset itself. It is a governed handle that lets KFM reason about how a dataset may be admitted, refreshed, validated, cataloged, corrected, released, or withdrawn.

---

## Path posture

The requested lane is:

```text
data/registry/datasets/flora/
```

This follows the data-side registry pattern: `data/registry/` stores registry state adjacent to the lifecycle phases, while Flora remains a domain segment inside the responsibility root.

The parent dataset registry path exists but is currently a stub:

```text
data/registry/datasets/README.md
```

Because the parent is not yet expanded, this README documents the Flora dataset sublane only. It does not assert final registry taxonomy for every domain or dataset family.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Flora dataset registry records | `data/registry/datasets/flora/` | Dataset identity, lifecycle pointers, rights/sensitivity posture, cadence, and eligibility state. |
| Flora source payloads | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` | Actual data belongs in lifecycle lanes, not registry records. |
| Flora source descriptors | `data/registry/sources/flora/` or accepted source registry lane | Source identity, role, rights, terms, cadence, and authority limits. |
| Flora crosswalk registry records | `data/registry/crosswalks/` | Mapping state; not dataset identity. |
| Flora semantic meaning | `contracts/domains/flora/` | Object-family meaning and invariants. |
| Flora machine shape | `schemas/contracts/v1/domains/flora/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Flora policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/flora/`, `policy/geoprivacy/` | Exposure, rights, sensitivity, and admissibility rules. |
| Flora validation receipts | `data/receipts/validation/flora/` | Process memory for validation checks. |
| Flora proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Flora catalog projections | `data/catalog/stac/flora/`, `data/catalog/dcat/flora/`, `data/catalog/prov/flora/`, `data/catalog/domain/flora/` | Catalog/discovery carriers after catalog closure. |
| Flora release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Dataset boundary

| Rule | Handling |
|---|---|
| Registry record is a handle | It identifies and governs a dataset; it does not contain the dataset payload. |
| Source role is preserved | A dataset's observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted role must not be upgraded by processing or publication. |
| Rights and sensitivity fail closed | Unclear license, redistribution, steward obligation, rare-plant risk, cultural sensitivity, private-land exposure, or precise-location risk blocks public promotion. |
| Exact sensitive Flora geometry is denied by default | Exact rare, protected, or culturally sensitive plant locations require steward review, transform, receipt, and release decision before any public-safe derivative exists. |
| Registry is not catalog | STAC/DCAT/PROV records live under `data/catalog/`. A dataset registry record may point to catalog records; it does not replace them. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Registry changes are auditable | Dataset identity, source version, lifecycle refs, correction state, supersession, withdrawal, and rollback dependencies should remain traceable. |

---

## Accepted material

Accepted content is limited to Flora dataset registry records and registry-local support files:

- dataset identity records;
- dataset-family README files;
- local dataset indexes that point to records without becoming public catalog records;
- dataset version, cadence, source-role, source descriptor, rights, sensitivity, steward, retrieval, and lifecycle pointer metadata;
- public-safe eligibility flags and blocker states;
- correction, supersession, withdrawal, stale-state, embargo, and rollback references;
- references to validation receipts, proof packs, catalog records, release candidates, release manifests, and rollback cards;
- checksums, manifests, signatures, and index sidecars for registry integrity where applicable.

Dataset registry records should point outward by stable ID, path, URI, digest, or EvidenceRef rather than copying source payloads, proof material, catalog records, policy decisions, or release manifests into the registry lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora source payloads, Darwin Core archives, specimen dumps, occurrence exports, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, or `data/processed/flora/` depending on lifecycle state |
| Exact rare/protected/culturally sensitive plant coordinates or steward-only notes | restricted lifecycle lane or quarantine with deny-by-default policy controls |
| Source descriptor contract or source terms documentation | source registry/source catalog lanes and `contracts/`/`docs/sources/` as appropriate |
| Crosswalk mapping state | `data/registry/crosswalks/` |
| Semantic object contracts | `contracts/domains/flora/` |
| JSON Schema | `schemas/contracts/v1/domains/flora/` or accepted schema lane |
| Policy rules, geoprivacy rules, sensitivity rules, or access-control logic | `policy/` |
| Validation receipts, run receipts, redaction receipts, or review process memory | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records | `data/catalog/` |
| Public-safe released artifacts, map layers, tiles, reports, dashboards, or API payloads | `data/published/`, governed app/API roots, and `release/` after promotion |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/datasets/flora/
├── README.md
├── taxon_backbones/
│   ├── README.md
│   └── index.local.json
├── specimens/
│   ├── README.md
│   └── index.local.json
├── occurrences/
│   ├── README.md
│   └── index.local.json
├── rare_plants/
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
├── restoration/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

`index.local.json` files are registry-local lookup aids. They are not proof indexes, source payloads, catalog records, release manifests, search indexes, vector indexes, map sources, or public API payloads.

---

## Suggested record shape

The exact schema remains **NEEDS VERIFICATION**. A Flora dataset registry record should be structured enough for audit, refresh, validation, catalog closure, correction, rollback, and release review.

```json
{
  "id": "kfm-dataset:flora:<stable-id>",
  "record_type": "dataset_registry_record",
  "domain": "flora",
  "dataset_family": "taxon_backbone | specimen | occurrence | rare_plant | vegetation_community | invasive_plant | phenology | range_polygon | restoration | derivative",
  "title": "Human-readable dataset title",
  "status": "candidate | active | restricted | quarantined | deprecated | superseded | withdrawn",
  "source_descriptor_refs": [],
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "rights_posture": "open | attribution-required | restricted | stewarded | unknown | denied",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "cadence": "one-time | periodic | event-driven | unknown",
  "retrieval_refs": [],
  "lifecycle_refs": {
    "raw": [],
    "work": [],
    "quarantine": [],
    "processed": [],
    "catalog": [],
    "published": []
  },
  "evidence_refs": [],
  "proof_refs": [],
  "validation_receipt_refs": [],
  "redaction_receipt_refs": [],
  "policy_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm the object is a dataset registry record, not a source payload, source descriptor, crosswalk, proof, receipt, catalog record, release decision, policy, schema, or validator.
- [ ] Confirm source descriptor refs, source role, rights posture, cadence, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, cataloging, or public presentation.
- [ ] Confirm exact rare/protected/culturally sensitive plant locations are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm rights, sensitivity, geoprivacy, cultural, private-land, rare-species, and precise-location risks fail closed when unresolved.
- [ ] Confirm validation receipts exist before catalog/release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed datasets.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/datasets/flora/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/datasets/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Flora lifecycle docs define RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and treat receipts, proofs, registry, and rollback as adjacent lanes. | CONFIRMED by GitHub contents API during this edit |
| Flora sensitivity docs deny exact rare/protected/culturally sensitive plant locations on public surfaces by default and require review/transform/RedactionReceipt for public movement. | CONFIRMED by GitHub contents API during this edit |
| Flora STAC catalog README exists as a catalog-stage sibling that is not source truth, policy, proof, or release authority. | CONFIRMED by GitHub contents API during this edit |
| Concrete Flora dataset registry payloads exist under this lane. | UNKNOWN |
| A canonical Flora dataset registry schema is enforced. | NEEDS VERIFICATION |
| CI validates Flora dataset registry records. | UNKNOWN |
| This README grants public access to Flora dataset registry internals. | DENY |

---

## Maintainer note

A Flora dataset registry record is an indexable governance handle, not a shortcut around the trust membrane. Keep the safe chain explicit:

```text
source descriptor + dataset registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
dataset registry record -> public Flora truth
```
