<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/hydrology/sources/readme
name: Hydrology Source Registry README
path: data/registry/hydrology/sources/README.md
type: data-registry-hydrology-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <hydrology-domain-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: hydrology-source-descriptor-records
domain: hydrology
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-hydrology; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; freshness-bound; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/hydrology/
  - ../../datasets/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/hydrology/README.md
  - ../../../raw/hydrology/fema_nfhl/README.md
  - ../../../raw/hydrology/usgs_3dep/README.md
  - ../../../raw/hydrology/usgs_nhdplus_hr/README.md
  - ../../../raw/hydrology/usgs_water_data/README.md
  - ../../../raw/hydrology/usgs_wbd/README.md
  - ../../../work/hydrology/
  - ../../../quarantine/hydrology/
  - ../../../processed/hydrology/
  - ../../../catalog/domain/hydrology/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hydrology/SOURCE_FAMILIES.md
  - ../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../policy/sensitivity/hydrology/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - hydrology
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - freshness
  - water-data
  - streamgage
  - flood-context
  - watershed-boundary
  - huc
  - nhdplus
  - terrain
  - groundwater
  - water-quality
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/hydrology/sources/README.md`."
  - "Hydrology source registry records are admission and authority-control records. They do not store source payloads, prove hydrologic claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The inspected Hydrology source-registry doctrine names `data/registry/sources/hydrology/` as the registry data home. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled."
  - "Hydrology source roles, time kinds, datum/unit metadata, regulatory flood context, modeled derivatives, provisional observations, aggregation scope, freshness, correction, and rollback must remain explicit."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Source Registry

Domain-first registry lane for Hydrology source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Hydrology source boundary](#hydrology-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/hydrology/sources/` is a source-registry lane for Hydrology admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, emergency alert material, or generated-answer authority.

---

## Scope

This directory documents and may hold Hydrology source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Hydrology lane.

Hydrology source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, and terms posture;
- sensitivity, freshness, datum/unit, geometry/support, and release-boundary posture;
- cadence, source head, retrieval window, observed/source time, valid/effective time, retrieval time, source vintage, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required redaction, quarantine, validation, proof, catalog, release, correction, stale-state, and rollback requirements.

They do **not** record hydrologic truth. A source descriptor can authorize or deny admission conditions, but every hydrologic claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/hydrology/sources/
```

This is a domain-first registry path. Current Hydrology source-registry doctrine names the subtype-first pattern as the registry data home:

```text
data/registry/sources/hydrology/
```

Because both patterns are visible in repo evidence, this README preserves the requested path while marking final topology as **NEEDS VERIFICATION**. Until registry layout is reconciled by accepted directory or ADR guidance, do not silently duplicate source descriptor instances across both lanes. Prefer one canonical descriptor record with compatibility pointers, migration notes, and rollback history.

The domain-first parent exists but is currently a stub:

```text
data/registry/hydrology/README.md
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Hydrology source descriptor/admission records | `data/registry/hydrology/sources/` and/or `data/registry/sources/hydrology/` after topology reconciliation | Source identity, role, rights, terms, cadence, freshness, activation, supersession, and authority limits. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Human-facing Hydrology source orientation | `docs/domains/hydrology/SOURCE_REGISTRY.md`, `SOURCE_FAMILIES.md`, `SOURCE_ROLE_MATRIX.md`, `DATA_LIFECYCLE.md` | Explains source families, source-role discipline, admission posture, lifecycle movement, and boundaries; not machine descriptor storage. |
| Hydrology source payloads | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/` | Actual data belongs in lifecycle lanes, not registry records. |
| Hydrology domain/dataset/crosswalk registry records | `data/registry/domains/`, `data/registry/datasets/`, `data/registry/crosswalks/` | Adjacent registry state; not source descriptor authority. |
| Hydrology semantic meaning | `contracts/domains/hydrology/` | Object-family meaning and invariants. |
| Hydrology machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/hydrology/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Hydrology policy and sensitivity | `policy/sensitivity/hydrology/`, `policy/domains/hydrology/`, `policy/rights/` | Exposure, rights, source-role, sensitivity, freshness, datum/unit, and admissibility rules. |
| Hydrology validation receipts | `data/receipts/validation/hydrology/` if/when accepted | Process memory for validation checks. |
| Hydrology proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Hydrology catalog projections | `data/catalog/domain/hydrology/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Hydrology release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Hydrology source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Source role is fixed at admission | The canonical role must not be upgraded by processing, aggregation, cataloging, release review, map rendering, or generated explanation. |
| Descriptor is not hydrologic truth | WBD, NHDPlus/3DHP, NWIS/Water Data, NFHL, terrain, state water-office, water-quality, groundwater, flood-evidence, drought, and irrigation-link sources still require evidence and review before claims. |
| Regulatory is not observed | NFHL or other regulatory flood context must not be reframed as observed inundation, forecast, or model output. |
| Provisional is not approved | Provisional readings and candidate records require lifecycle disposition before downstream claims. |
| Aggregate is not per-instant truth | Daily values, annual statistics, HUC rollups, drought links, and other rollups must carry aggregation scope. |
| Modeled is not observed | Rating curves, VAAs, catchments, DEM derivatives, hydrographs, reconstructed traces, and modeled surfaces require model/lineage support. |
| Time kinds stay distinct | Source time, observed time, valid/effective time, retrieval time, release time, and correction time remain separate where material. |
| Datum and units travel | Datum, units, parameter identity, site identity, geometry/support metadata, and approval status should remain explicit through lifecycle movement. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Hydrology source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, sensitivity, cadence, steward, endpoint, access, attribution, redistribution, freshness, and authority-scope metadata;
- source time, observed time, retrieval time, valid/effective time where applicable, product vintage, endpoint identity, geometry/support metadata, datum/unit metadata, approval status, and source-head metadata summaries;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed large payloads, sensitive local details, proof packs, policy decisions, catalog records, release manifests, source-native dumps, or hydrologic claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Hydrology source payloads, WBD/NHDPlus packages, water-data extracts, terrain products, regulatory flood packages, water-quality records, groundwater records, drought/irrigation feeds, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, or `data/processed/hydrology/` depending on lifecycle state |
| Emergency alert material, private identifiers, access secrets, sensitive local details, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/hydrology/`, `docs/sources/`, or source catalog docs |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/hydrology/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/hydrology/` |
| Policy rules, sensitivity rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Hydrology layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/hydrology/sources/
├── README.md
├── usgs_wbd/
│   ├── README.md
│   └── index.local.json
├── usgs_nhdplus_hr/
│   ├── README.md
│   └── index.local.json
├── usgs_water_data/
│   ├── README.md
│   └── index.local.json
├── fema_nfhl/
│   ├── README.md
│   └── index.local.json
├── usgs_3dep/
│   ├── README.md
│   └── index.local.json
├── water_quality/
│   ├── README.md
│   └── index.local.json
├── groundwater/
│   ├── README.md
│   └── index.local.json
├── drought_irrigation/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/hydrology/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain two divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Hydrology source registry record should be structured enough for audit, admission, validation, correction, stale-state handling, and rollback.

```json
{
  "id": "kfm-source:hydrology:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "hydrology",
  "source_family": "watershed_boundary | stream_network | water_data | regulatory_flood_context | terrain | state_water_office | water_quality | groundwater | flood_evidence | drought_irrigation | context_layer | other",
  "source_name": "Human-readable source name",
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "authority_scope": "What this source may and may not support",
  "rights_posture": "open | attribution-required | restricted | stewarded | unknown | denied",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "freshness_posture": "static | source-vintage | time-bound | provisional | expires | unknown",
  "cadence": "one-time | periodic | event-driven | unknown",
  "source_head_refs": [],
  "retrieval_refs": [],
  "activation_refs": [],
  "intake_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "stale_state_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm whether `data/registry/hydrology/sources/` or `data/registry/sources/hydrology/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source time, observed time, retrieval time, valid/effective time, freshness posture, datum/units, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm regulatory context, observed readings, modeled derivatives, aggregates, provisional material, and candidate evidence are not collapsed.
- [ ] Confirm regulatory flood context is not presented as observed inundation, forecast, or model output.
- [ ] Confirm sensitive local details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or time-bound Hydrology source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/hydrology/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/hydrology/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Hydrology source-registry doctrine names `data/registry/sources/hydrology/` as the registry data home and says source role is fixed at admission. | CONFIRMED by GitHub contents API during this edit |
| Hydrology source-registry doctrine warns that regulatory flood layers must not collapse into observed flooding. | CONFIRMED by GitHub contents API during this edit |
| Hydrology RAW README keeps RAW source capture separate from registry, proof, receipt, policy, release, public, and answer authority. | CONFIRMED by GitHub contents API during this edit |
| Concrete Hydrology source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between `data/registry/hydrology/sources/` and `data/registry/sources/hydrology/` is resolved. | NEEDS VERIFICATION |
| A canonical Hydrology source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Hydrology source registry records. | UNKNOWN |
| This README grants public access to Hydrology source registry internals. | DENY |

---

## Maintainer note

Hydrology source registry records are useful because they make source identity, source role, rights, sensitivity, freshness, activation, correction, stale-state, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, release decisions, or hydrologic truth. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> RAW admission -> lifecycle processing -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Hydrology truth
```
