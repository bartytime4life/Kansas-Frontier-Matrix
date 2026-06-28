<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/domains/soil/readme
name: Soil Domain Registry README
path: data/registry/domains/soil/README.md
type: data-registry-domains-domain-readme
version: v0.1.0
status: draft
owners:
  - <registry-steward>
  - <soil-domain-steward>
  - <source-steward>
  - <data-steward>
  - <contract-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: soil-domain-registry-records
domain: soil
path_posture: existing-empty-placeholder-replaced; parent-domains-registry-stub-confirmed; soil-domain-registry-path-confirmed-by-soil-canonical-paths; exact-domain-registry-layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; support-type-separation-required; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../datasets/README.md
  - ../../crosswalks/README.md
  - ../../../raw/soil/README.md
  - ../../../work/soil/
  - ../../../quarantine/soil/
  - ../../../processed/soil/
  - ../../../catalog/domain/soil/
  - ../../../published/layers/soil/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../contracts/domains/soil/README.md
  - ../../../../schemas/contracts/v1/domains/soil/
  - ../../../../policy/domains/soil/
  - ../../../../docs/sources/catalog/nrcs/soil-data-access.md
  - ../../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../../docs/sources/catalog/nrcs/gssurgo.md
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - domains
  - soil
  - domain-registry
  - source-role
  - support-type
  - ssurgo
  - gssurgo
  - gnatsgo
  - soil-data-access
  - mesonet
  - scan
  - uscrn
  - smap
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the empty placeholder at `data/registry/domains/soil/README.md`."
  - "Soil domain registry records describe domain-lane state, object-family coverage, source-family posture, lifecycle links, support-type boundaries, and governance readiness. They do not store source payloads or publish data."
  - "Soil canonical-path doctrine lists `data/registry/domains/soil/` as a Soil data-side registry lane, while path maturity and exact layout remain NEEDS VERIFICATION until implementation evidence is inspected."
  - "Concrete domain registry schemas, validators, emitted records, CI enforcement, release integration, and governed API behavior remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Domain Registry

Governed registry lane for Soil domain-state records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: domains" src="https://img.shields.io/badge/lane-domains-blue">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-8B4513">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Domain registry boundary](#domain-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested record shape](#suggested-record-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/domains/soil/` is a registry lane for Soil domain-state records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, source registry authority, semantic contract authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

This directory documents and should eventually hold Soil domain registry records: stable, inspectable records that describe the Soil lane's domain state, object-family coverage, source-family posture, support-type boundaries, lifecycle references, evidence requirements, policy posture, catalog expectations, public-readiness blockers, correction state, and rollback dependencies.

A Soil domain registry record may track governance state for:

- `SoilMapUnit`, `SoilComponent`, `Horizon`, `SoilProperty`, and component-horizon joins;
- hydrologic soil groups, pedon/profile views, soil-time caveats, and map-unit interpretations;
- soil-moisture observations, station/depth/unit/QC support, and sensor-source posture;
- gridded derivatives, satellite grids, and support/resolution metadata;
- erosion risk, suitability ratings, and interpretation surfaces;
- source families such as NRCS SSURGO, USDA NRCS Soil Data Access, gSSURGO, gNATSGO, Kansas Mesonet, NRCS SCAN, NOAA USCRN, NASA SMAP, and ISRIC SoilGrids;
- public-safe Soil layer readiness, catalog closure, correction posture, stale-state handling, and rollback readiness.

A domain registry record is not a soil observation, map unit, component, horizon, station reading, gridded surface, suitability claim, public layer, proof, catalog record, or release decision. It is a governed handle that helps reviewers understand what the Soil lane says it owns, what it can safely use, and what still blocks promotion.

---

## Path posture

The requested lane is:

```text
data/registry/domains/soil/
```

Soil canonical-path doctrine lists this path as a Soil data-side registry lane. Directory Rules also require domains to appear as segments inside responsibility roots, not as root-level folders.

The parent domain registry path exists but is currently a stub:

```text
data/registry/domains/README.md
```

Because the parent is not yet expanded, this README documents the Soil domain sublane only. It does not assert final registry taxonomy for every domain or registry subtype.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Soil domain registry records | `data/registry/domains/soil/` | Domain-state records, object-family coverage, source-family posture, support-type boundaries, lifecycle refs, blockers, and readiness state. |
| Soil source payloads | `data/raw/soil/`, `data/work/soil/`, `data/quarantine/soil/`, `data/processed/soil/` | Actual data belongs in lifecycle lanes, not registry records. |
| Soil source registry records | `data/registry/sources/soil/` or accepted source registry lane | Source identity, role, rights, cadence, authority limits, and access posture. |
| Soil dataset registry records | `data/registry/datasets/soil/` if/when accepted | Dataset identity and dataset-state records. |
| Soil crosswalk registry records | `data/registry/crosswalks/` or accepted crosswalk lane | Mapping state across source IDs, authority IDs, fields, and vocabularies. |
| Soil semantic meaning | `contracts/domains/soil/` | Object-family meaning and invariants. |
| Soil machine shape | `schemas/contracts/v1/domains/soil/` or ADR-selected schema lane | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Soil policy and rights | `policy/domains/soil/` and cross-cutting policy roots | Exposure, rights, support type, sensitivity, and admissibility rules. |
| Soil validation receipts | `data/receipts/validation/soil/` if/when accepted | Process memory for validation checks. |
| Soil proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Soil catalog projections | `data/catalog/domain/soil/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Soil release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Domain registry boundary

| Rule | Handling |
|---|---|
| Registry record is domain-state metadata | It describes the Soil lane's governed state; it does not contain soil payloads. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted roles must not be upgraded by registry state. |
| Support type is preserved | Static survey, gridded derivative, station reading, satellite grid, pedon/profile evidence, and interpretation/suitability surfaces must not be silently fused. |
| Soil keys remain auditable | MUKEY, COKEY, CHKEY, horizon depths, component-horizon joins, station IDs, depth/unit/QC, product vintage, resolution, and derivation lineage should remain traceable where applicable. |
| Registry is not contract | Object meaning remains in `contracts/`. |
| Registry is not schema | Machine shape remains in `schemas/`. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | Catalog/discovery records remain under `data/catalog/`. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Soil domain registry records and registry-local support files:

- Soil domain-state records;
- object-family coverage indexes;
- source-family posture indexes;
- support-type separation records;
- domain readiness and blocker summaries;
- local manifests, checksums, signatures, and index sidecars for domain registry state;
- links to source descriptors, dataset registry records, crosswalk registry records, contracts, schemas, policy refs, lifecycle payloads, validation receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, and rollback cards;
- public-safe summaries that omit sensitive, private, restricted, or operationally risky details.

Registry records should point outward by stable ID, path, URI, digest, or EvidenceRef rather than copying source payloads, contracts, schemas, proofs, catalog records, policy decisions, receipts, release manifests, or public artifacts into the registry lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Soil source payloads, SDA query dumps, SSURGO/gSSURGO/gNATSGO extracts, station data, SMAP granules, SoilGrids tiles, shapefiles, rasters, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/soil/`, `data/work/soil/`, `data/quarantine/soil/`, or `data/processed/soil/` depending on lifecycle state |
| Farm-/owner-specific restricted detail, private identifiers, credentials, tokens, exact operational sensor exposure, or restricted notes | restricted lifecycle lane, quarantine, or governed secret/restricted storage as applicable |
| Source descriptors and source activation decisions | `data/registry/sources/soil/` or accepted source registry/source-catalog lanes |
| Dataset identity records | `data/registry/datasets/soil/` if/when accepted, or the accepted dataset registry lane |
| Crosswalk mapping records | `data/registry/crosswalks/` or accepted crosswalk registry lane |
| Semantic object contracts | `contracts/domains/soil/` |
| JSON Schema | `schemas/contracts/v1/domains/soil/` or ADR-selected schema lane |
| Policy rules, support-type admissibility rules, rights rules, sensitivity rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Soil layers, PMTiles, reports, dashboards, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/domains/soil/
├── README.md
├── object_families/
│   ├── README.md
│   └── index.local.json
├── source_families/
│   ├── README.md
│   └── index.local.json
├── support_types/
│   ├── README.md
│   └── index.local.json
├── readiness/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

`index.local.json` files are registry-local lookup aids. They are not proof indexes, catalog records, release manifests, search indexes, vector indexes, graph projections, map sources, public API payloads, or generated-answer sources.

---

## Suggested record shape

The exact schema remains **NEEDS VERIFICATION**. A Soil domain registry record should be structured enough for audit, validation, correction, rollback, and release review.

```json
{
  "id": "kfm-domain-registry:soil:<stable-id>",
  "record_type": "domain_registry_record",
  "domain": "soil",
  "registry_family": "object_family | source_family | support_type | readiness | blocker | release_support",
  "status": "candidate | active | restricted | blocked | deprecated | superseded | withdrawn | denied",
  "object_family_refs": [],
  "source_family_refs": [],
  "source_descriptor_refs": [],
  "support_types": ["static_survey", "gridded_derivative", "station_reading", "satellite_grid", "pedon_profile", "interpretation"],
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "rights_posture": "open | attribution-required | restricted | stewarded | unknown | denied",
  "sensitivity_posture": "public-safe | restricted | denied | needs-review",
  "lifecycle_refs": {
    "raw": [],
    "work": [],
    "quarantine": [],
    "processed": [],
    "catalog": [],
    "published": []
  },
  "contract_refs": [],
  "schema_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm the object is a Soil domain registry record, not source data, source descriptor, dataset registry record, crosswalk, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm the owning root is `data/` and the registry lane is appropriate under Directory Rules and Soil canonical-path doctrine.
- [ ] Confirm source descriptor refs, source role, rights posture, cadence, source family, support type, stewardship obligations, and authority limits are preserved.
- [ ] Confirm static survey, gridded derivative, station reading, satellite grid, pedon/profile, and interpretation surfaces are not silently fused.
- [ ] Confirm MUKEY/COKEY/CHKEY, horizon depths, station/depth/unit/QC, product vintage, resolution, resampling, derivation lineage, and caveats remain traceable where applicable.
- [ ] Confirm farm-/owner-specific, private, restricted, operational, or sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Soil material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the empty placeholder at `data/registry/domains/soil/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as an empty placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/domains/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Soil canonical paths list `data/registry/domains/soil/` as a Soil domain segment under `data/registry/`. | CONFIRMED by GitHub contents API during this edit |
| Soil continuity/lifecycle docs list Soil object families, source families, lifecycle posture, and domain-segment placement as doctrine-grounded but implementation-bounded. | CONFIRMED by GitHub contents API during this edit |
| `data/raw/soil/README.md` exists and keeps RAW Soil payloads separate from registry, proof, receipt, catalog, policy, and release authority. | CONFIRMED by GitHub contents API during this edit |
| `contracts/domains/soil/README.md` exists and keeps Soil semantic contracts separate from schemas, policy, source registry, lifecycle data, and release decisions. | CONFIRMED by GitHub contents API during this edit |
| Concrete Soil domain registry payloads exist under this lane. | UNKNOWN |
| A canonical Soil domain registry schema is enforced. | NEEDS VERIFICATION |
| CI validates Soil domain registry records. | UNKNOWN |
| This README grants public access to Soil domain registry internals. | DENY |

---

## Maintainer note

Soil domain registry records are useful because they make domain ownership, object families, source families, support types, rights, lifecycle refs, blockers, correction, and rollback inspectable. They become dangerous when treated as payloads, proofs, catalog closure, or release decisions. Keep the chain explicit:

```text
source descriptor + domain registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
domain registry record -> public Soil truth
```
