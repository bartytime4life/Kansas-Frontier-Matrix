<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/soil/sources/readme
name: Soil Source Registry README
path: data/registry/soil/sources/README.md
type: data-registry-soil-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <soil-domain-steward>
  - <nrcs-source-steward>
  - <rights-steward>
  - <sensitivity-steward>
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
registry_scope: soil-source-descriptor-records
domain: soil
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; cross-domain-source-registry-parent-confirms-data-registry-sources-domain-pattern; soil-domain-registry-points-to-data-registry-sources-soil-or-accepted-source-registry-lane; exact-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; support-type-separation-required; scale-and-resolution-aware; private-land-and-parcel-joins-reviewed; field-verification-not-implied; rights-aware; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/soil/
  - ../../domains/soil/README.md
  - ../../datasets/README.md
  - ../../crosswalks/README.md
  - ../../rights/README.md
  - ../../sensitivity/README.md
  - ../../layers/README.md
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
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/domains/soil/
  - ../../../../policy/domains/soil/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../docs/sources/catalog/nrcs.md
  - ../../../../docs/sources/catalog/nrcs/README.md
  - ../../../../docs/sources/catalog/nrcs/soil-data-access.md
  - ../../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../../docs/sources/catalog/nrcs/web-soil-survey.md
  - ../../../../connectors/nrcs/README.md
  - ../../../../connectors/nrcs/ssurgo/README.md
  - ../../../../connectors/nrcs/gssurgo/README.md
  - ../../../../connectors/nrcs/gnatsgo/README.md
  - ../../../../connectors/nrcs/sda/README.md
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - soil
  - sources
  - source-descriptor
  - source-role
  - support-type
  - nrcs
  - ssurgo
  - gssurgo
  - gnatsgo
  - statsgo2
  - soil-data-access
  - web-soil-survey
  - soil-map-unit
  - soil-component
  - horizon
  - soil-property
  - soil-moisture
  - gridded-derivatives
  - scale
  - resolution
  - rights
  - sensitivity
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/soil/sources/README.md`."
  - "Soil source registry records are admission and authority-control records. They do not store source payloads, prove soil claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The cross-domain source registry parent confirms `data/registry/sources/<domain>/` as a permitted source-registry pattern. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled."
  - "NRCS and other soil source families must not be collapsed into one source role, cadence, scale, support type, rights posture, or release posture."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Source Registry

Domain-first registry lane for Soil source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-8B4513">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not soil truth" src="https://img.shields.io/badge/boundary-not%20soil%20truth-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Soil source boundary](#soil-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/soil/sources/` is a source-registry lane for Soil admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, parcel truth, field-verification truth, conservation-compliance truth, soil-claim truth, or generated-answer authority.

---

## Scope

This directory documents and may hold Soil source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Soil lane.

Soil source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, endpoint terms, steward obligations, and access posture;
- sensitivity and support posture for map units, components, horizons, soil properties, interpretations, station observations, gridded derivatives, model-derived surfaces, private-land joins, and parcel-adjacent use;
- cadence, source head, retrieval window, source vintage, effective time, valid time, release time, source scale, spatial resolution, attribute support, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required quarantine, validation, unit normalization, support-type checks, projection checks, aggregation, redaction, proof, catalog, release, correction, stale-state, withdrawal, and rollback requirements.

They do **not** prove that a soil map unit, component, horizon, soil property, hydrologic soil group, station observation, gridded derivative, suitability rating, erosion risk, conservation practice, parcel-scale interpretation, or field condition is true, current, complete, public-safe, or release-approved. A source descriptor can authorize or deny admission conditions, but every consequential soil claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/soil/sources/
```

This is a domain-first registry path. Current cross-domain source-registry evidence also supports a subtype-first source registry pattern:

```text
data/registry/sources/<domain>/
```

The Soil domain registry README points to `data/registry/sources/soil/` or an accepted source registry lane for source identity, role, rights, cadence, authority limits, and access posture. NRCS catalog documentation also states that human-facing product pages do not replace authoritative `SourceDescriptor` records in `data/registry/sources/`.

Therefore, this requested path is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. If `data/registry/sources/soil/` is later accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain divergent descriptor sets.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Soil source descriptor/admission records | `data/registry/soil/sources/` and/or reconciled `data/registry/sources/soil/` | Source identity, role, rights, terms, cadence, activation, authority limits, support type, scale, and caveats. |
| Domain-first registry parent | `data/registry/soil/` | Parent currently exists as a stub; topology remains NEEDS VERIFICATION. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Soil domain registry records | `data/registry/domains/soil/` | Domain-state records; not source descriptor instances. |
| Soil source payloads | `data/raw/soil/`, `data/work/soil/`, `data/quarantine/soil/`, `data/processed/soil/` | Actual data belongs in lifecycle lanes, not registry records. |
| Human-facing source/product pages | `docs/sources/catalog/nrcs/` and accepted source catalog docs | Reader-oriented source documentation; not authoritative descriptor instances. |
| Connector logic | `connectors/nrcs/` and product connector lanes | Fetch/admission helpers only; not source truth, registry truth, pipeline truth, proof, policy, catalog, or release. |
| Soil semantic meaning | `contracts/domains/soil/` | Object-family meaning and invariants. |
| Machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/soil/`, or ADR-selected schema lane | Schema enforcement; exact source descriptor schema state remains NEEDS VERIFICATION. |
| Policy and rights | `policy/domains/soil/`, `policy/rights/`, and accepted sensitivity/support policy lanes | Exposure, rights, support type, sensitivity, and admissibility rules. |
| Validation/support receipts | `data/receipts/` and accepted Soil receipt lanes | Process memory for checks, transforms, aggregation, and support validation. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog and graph projections | `data/catalog/domain/soil/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Soil source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Source role is fixed at admission | Primary, corroborating, context, restricted, modeled, aggregate, candidate, or other accepted source roles must not be upgraded by processing, normalization, joining, cataloging, rendering, or generated explanation. |
| Soil support type is preserved | Map-unit support, component support, horizon support, station/depth support, gridded support, satellite/model support, and interpretation support must not be silently collapsed. |
| Scale and resolution matter | SSURGO-like survey material, generalized products, station observations, gridded products, and remote-sensing products must preserve intended scale, resolution, support, and uncertainty. |
| Soil map geometry is not parcel truth | Soil map units, component joins, and gridded surfaces do not prove parcel ownership, field verification, legal access, conservation compliance, crop management, or site-specific suitability by themselves. |
| Station observations are not area truth | Soil-moisture or climate station readings require station/depth/unit/QC support and must not be generalized into area truth without governed processing. |
| Derived interpretations are downstream carriers | Suitability ratings, hydrologic soil groups, erosion risk, productivity, or model-derived surfaces inherit source-role, scale, support, uncertainty, rights, sensitivity, and release posture. |
| NRCS material is multi-product | SSURGO, gSSURGO, gNATSGO, STATSGO2, SDA, Web Soil Survey, SCAN, and other NRCS products require product-specific role, cadence, scale, rights, and release posture. |
| Rights and restrictions travel | License, attribution, redistribution, endpoint terms, source restrictions, and steward caveats must remain attached downstream. |
| Registry is not validation | Validation receipts, unit-normalization receipts, support-type receipts, transform receipts, policy receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Soil source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, license, attribution, redistribution, cadence, access, endpoint, terms, steward, authority-scope, and caveat metadata;
- source vintage, survey area, geography, spatial precision, temporal precision, scale, resolution, support type, attribute-support notes, retrieval refs, and stale-state notes;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation/unit/support/aggregation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed source payloads, full soil survey tables, raster grids, station readings, proof packs, policy decisions, catalog records, release manifests, or Soil claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw soil-survey payloads, SSURGO/gSSURGO/gNATSGO/STATSGO2 tables, SDA query outputs, Web Soil Survey exports, SCAN/station observations, SoilGrids or SMAP grids, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/soil/`, `data/work/soil/`, `data/quarantine/soil/`, or `data/processed/soil/` depending on lifecycle state |
| Source fetchers, endpoint clients, credentials, watchers, or automation | `connectors/`, `pipelines/`, `pipeline_specs/`, `configs/`, `infra/`, or accepted implementation roots |
| NRCS connector code or request helpers | `connectors/nrcs/` and product connector lanes |
| Dataset identity records | `data/registry/datasets/` |
| Domain-state records | `data/registry/domains/soil/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Rights registry records | `data/registry/rights/` after accepted rights-registry topology |
| Sensitivity registry records | `data/registry/sensitivity/` after accepted sensitivity-registry topology |
| Layer registry records | `data/registry/layers/` after accepted layer-registry topology |
| Semantic object contracts | `contracts/domains/soil/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/soil/` |
| Policy rules, support-type rules, sensitivity rules, rights rules, access-control logic, stale-state rules, or release rules | `policy/` |
| Validation receipts, unit-normalization receipts, transform receipts, aggregation receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Parcel ownership, field verification, conservation-compliance, water-rights, legal access, agronomic prescription, or land-management decisions | outside this registry lane; require appropriate official or reviewed systems |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/soil/sources/
├── README.md
├── nrcs_ssurgo/
│   ├── README.md
│   └── index.local.json
├── nrcs_gssurgo/
│   ├── README.md
│   └── index.local.json
├── nrcs_gnatsgo/
│   ├── README.md
│   └── index.local.json
├── nrcs_soil_data_access/
│   ├── README.md
│   └── index.local.json
├── nrcs_web_soil_survey/
│   ├── README.md
│   └── index.local.json
├── station_observations/
│   ├── README.md
│   └── index.local.json
├── gridded_remote_sensing/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/soil/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Soil source registry record should be structured enough for audit, admission, validation, stale-state handling, correction, and rollback.

```json
{
  "id": "kfm-source:soil:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "soil",
  "source_family": "nrcs_ssurgo | nrcs_gssurgo | nrcs_gnatsgo | nrcs_soil_data_access | nrcs_web_soil_survey | station_observations | gridded_remote_sensing | other",
  "source_name": "Human-readable source name",
  "source_role": "primary | corroborating | context | restricted | modeled | aggregate | candidate | synthetic | needs-review",
  "authority_scope": "What this source may and may not support",
  "support_type": "map_unit | component | horizon | station_depth | grid_cell | model_surface | interpretation | other",
  "rights_posture": "open | attribution-required | restricted | unknown | denied | needs-review",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "cadence": "one-time | periodic | event-driven | user-supplied | unknown",
  "source_time_kind_refs": [],
  "stale_state_refs": [],
  "source_head_refs": [],
  "retrieval_refs": [],
  "activation_refs": [],
  "intake_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "unit_receipt_refs": [],
  "support_receipt_refs": [],
  "aggregation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | permissioned | restricted | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm whether `data/registry/soil/sources/` or `data/registry/sources/soil/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, rights record, sensitivity record, layer record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, test, connector, or pipeline.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source vintage, source scale, support type, resolution, retrieval time, valid/effective time, and authority limits are preserved.
- [ ] Confirm source role and support type are not upgraded by normalization, joins, aggregation, interpolation, modeling, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm map-unit, component, horizon, station/depth, grid, model, and interpretation contexts are not collapsed.
- [ ] Confirm station observations, gridded products, and remote-sensing derivatives carry support, resolution, QC, and uncertainty limits before catalog or release eligibility is asserted.
- [ ] Confirm parcel, private-land, conservation, compliance, water-rights, field-verification, and management-decision contexts are not asserted from soil source descriptors.
- [ ] Confirm validation, unit-normalization, support-type, aggregation, transform, and policy receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, rights-change, support-change, and rollback paths exist for mutable, time-bound, rights-bound, support-bound, or externally governed source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public soil truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/soil/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/soil/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Cross-domain `data/registry/sources/README.md` says source registry records are admission and authority-control records and that per-domain subfolders such as `data/registry/sources/<domain>/` are permitted. | CONFIRMED by GitHub contents API during this edit |
| Soil domain registry README says Soil source registry records belong in `data/registry/sources/soil/` or an accepted source registry lane and names Soil source families including SSURGO, SDA, gSSURGO, gNATSGO, Mesonet, SCAN, USCRN, SMAP, and SoilGrids. | CONFIRMED by GitHub contents API during this edit |
| NRCS Soil Data Access documentation says product pages do not replace authoritative SourceDescriptor records in `data/registry/sources/`. | CONFIRMED by GitHub contents API during this edit |
| NRCS connector README says NRCS products are multi-product and role-specific and must not be collapsed under one source role, cadence, scale, or release posture. | CONFIRMED by GitHub contents API during this edit |
| Concrete Soil source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first source registry lanes is resolved. | NEEDS VERIFICATION |
| A canonical Soil source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Soil source registry records. | UNKNOWN |
| This README grants public access to Soil source registry internals. | DENY |

---

## Maintainer note

Soil source registry records are useful because they make source identity, source role, support type, scale, cadence, rights, sensitivity, authority limits, stale-state, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, release decisions, field verification, parcel truth, conservation-compliance truth, or public soil truth. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> rights/sensitivity/support/stale-state gate -> RAW admission -> lifecycle processing -> validation/unit/support/aggregation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Soil truth
```
