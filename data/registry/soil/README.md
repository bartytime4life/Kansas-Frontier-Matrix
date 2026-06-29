<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/soil/readme
name: Soil Registry README
path: data/registry/soil/README.md
type: data-registry-soil-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <soil-domain-steward>
  - <source-steward>
  - <dataset-steward>
  - <crosswalk-steward>
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
registry_scope: soil-domain-first-registry-parent
domain: soil
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; cross-domain-source-registry-parent-confirms-data-registry-sources-domain-pattern; soil-domain-registry-points-to-data-registry-sources-soil-or-accepted-source-registry-lane; subtype-first-source-registry-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; support-type-separation-required; scale-and-resolution-aware; private-land-and-parcel-joins-reviewed; field-verification-not-implied; rights-aware; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/soil/
  - ../domains/soil/README.md
  - ../datasets/README.md
  - ../crosswalks/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../layers/README.md
  - sources/README.md
  - ../../raw/soil/README.md
  - ../../work/soil/
  - ../../quarantine/soil/
  - ../../processed/soil/
  - ../../catalog/domain/soil/
  - ../../published/layers/soil/
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../contracts/domains/soil/README.md
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/soil/
  - ../../../policy/domains/soil/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
  - ../../../docs/sources/catalog/nrcs.md
  - ../../../docs/sources/catalog/nrcs/README.md
  - ../../../docs/sources/catalog/nrcs/soil-data-access.md
  - ../../../docs/sources/catalog/nrcs/ssurgo.md
  - ../../../docs/sources/catalog/nrcs/web-soil-survey.md
  - ../../../connectors/nrcs/README.md
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - soil
  - domain-first-registry
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
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/soil/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The cross-domain source registry parent confirms `data/registry/sources/<domain>/` as a permitted source-registry pattern, while the Soil domain registry points to `data/registry/sources/soil/` or an accepted source-registry lane."
  - "This parent is treated as a compatibility/routing lane until registry topology is reconciled. It must not become source payload storage, contract/schema/policy authority, soil truth, field verification, proof, catalog, release, or public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Soil Registry

Domain-first registry parent for Soil registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: soil" src="https://img.shields.io/badge/domain-soil-8B4513">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not soil truth" src="https://img.shields.io/badge/boundary-not%20soil%20truth-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Soil registry boundary](#soil-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/soil/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, parcel truth, field-verification truth, conservation-compliance truth, soil-claim truth, or generated-answer authority.

---

## Scope

`data/registry/soil/` is a domain-first routing lane for Soil registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for Soil sources.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Soil registry lane may point to or summarize governance state for:

- source descriptors and source-admission records;
- source-role assignments and source-family posture;
- support type, scale, resolution, source-head, cadence, rights, sensitivity, correction, supersession, stale-state, withdrawal, and freshness state;
- soil map units, components, horizons, soil properties, hydrologic soil groups, station observations, gridded derivatives, model-derived surfaces, and interpretation surfaces;
- NRCS SSURGO, gSSURGO, gNATSGO, STATSGO2, Soil Data Access, Web Soil Survey, station-observation, gridded, remote-sensing, and model-source contexts;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, full soil-survey tables, raster grids, station readings, proof packs, catalog records, release manifests, public map artifacts, field determinations, land-management decisions, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/soil/
```

This is a **domain-first** registry path. Current source-registry evidence also supports a subtype-first source registry pattern:

```text
data/registry/sources/soil/
```

The Soil domain registry README points to `data/registry/sources/soil/` or an accepted source registry lane for source identity, role, rights, cadence, authority limits, and access posture. The child source README preserves the requested domain-first path while marking final topology **NEEDS VERIFICATION**.

Therefore, `data/registry/soil/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Soil domain-first registry parent | `data/registry/soil/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed child registry lane | `data/registry/soil/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical source lane | `data/registry/sources/soil/` | Needs topology reconciliation with this path. |
| Soil domain registry records | `data/registry/domains/soil/` | Domain-state records; do not duplicate here without topology decision. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, field names, MUKEY/component/horizon identifiers, units, vocabularies, and domain lanes. |
| Rights registry records | `data/registry/rights/` | Rights review state and rights-readiness pointers. |
| Sensitivity registry records | `data/registry/sensitivity/` | Sensitivity, geoprivacy, redaction, review, and exposure-control state. |
| Layer registry records | `data/registry/layers/` | Layer identity and release-readiness pointers. |
| Soil source payloads | `data/raw/soil/`, `data/work/soil/`, `data/quarantine/soil/`, `data/processed/soil/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Human-facing source/product pages | `docs/sources/catalog/nrcs/` and accepted source catalog docs | Reader-oriented source documentation; not authoritative descriptor instances. |
| Connector logic | `connectors/nrcs/` and product connector lanes | Fetch/admission helpers only; not source truth, registry truth, pipeline truth, proof, policy, catalog, or release. |
| Soil semantic meaning | `contracts/domains/soil/` | Object-family meaning and invariants. |
| Machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/soil/`, or ADR-selected schema lane | Schema enforcement; exact source/registry schema state remains NEEDS VERIFICATION. |
| Policy and rights | `policy/domains/soil/`, `policy/rights/`, and accepted sensitivity/support policy lanes | Exposure, rights, support type, sensitivity, and admissibility rules. |
| Validation/support receipts | `data/receipts/` and accepted Soil receipt lanes | Process memory for checks, transforms, aggregation, and support validation. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog and graph projections | `data/catalog/domain/soil/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, public-safe summaries, or public UI behavior.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Soil source descriptor and source-admission registry lane. | Not source payload storage, soil truth, parcel truth, field verification, proof, receipt storage, catalog closure, semantic contract authority, schema authority, policy, release authority, or public output. |

---

## Soil registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/soil/...` and `data/registry/sources/soil/`. |
| Registry is not soil truth | Registry state does not prove map units, components, horizons, soil properties, station readings, gridded surfaces, interpretations, suitability, field conditions, or parcel-scale outcomes. |
| Source role is preserved | Registry state must not upgrade primary, corroborating, context, restricted, modeled, aggregate, candidate, synthetic, or review-needed source roles. |
| Support type is preserved | Map-unit, component, horizon, station/depth, grid-cell, model-surface, and interpretation support must not be silently merged. |
| Scale and resolution matter | Survey, generalized, station, gridded, and remote-sensing sources must preserve intended scale, resolution, support, and uncertainty. |
| Soil geometry is not parcel truth | Soil map units, component joins, and gridded surfaces do not prove parcel ownership, field verification, legal access, conservation compliance, crop management, or site-specific suitability by themselves. |
| Derived interpretations are downstream carriers | Suitability ratings, hydrologic soil groups, erosion risk, productivity, and model-derived layers inherit source-role, scale, support, uncertainty, rights, sensitivity, and release posture. |
| Rights and restrictions travel | License, attribution, redistribution, endpoint terms, source restrictions, and steward caveats must remain attached downstream. |
| Registry is not validation | Validation receipts, unit-normalization receipts, support-type receipts, transform receipts, policy receipts, and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to README/routing material and registry-local sidecars that do not duplicate authority from subtype-first lanes:

- parent README and routing notes;
- compatibility notes explaining domain-first versus subtype-first topology;
- migration notes, redirect notes, rollback notes, or topology decision notes;
- local indexes that point to child registry lanes without becoming authoritative records themselves;
- checksums, manifests, and signatures for registry routing material where applicable;
- pointers to source descriptors, dataset registry records, crosswalk registry records, domain registry records, rights registry records, sensitivity registry records, layer registry records, contracts, schemas, policy refs, lifecycle payloads, validation/unit/support/aggregation receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, stale-state notices, and rollback cards.

If a child lane under this parent stores actual registry records, it must state whether it is canonical, compatibility, migration-only, or mirrored, and it must name its conflict/rollback path.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw soil-survey payloads, SSURGO/gSSURGO/gNATSGO/STATSGO2 tables, SDA query outputs, Web Soil Survey exports, station observations, grids, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/soil/`, `data/work/soil/`, `data/quarantine/soil/`, or `data/processed/soil/` depending on lifecycle state |
| Source fetchers, endpoint clients, credentials, watchers, or automation | `connectors/`, `pipelines/`, `pipeline_specs/`, `configs/`, `infra/`, or accepted implementation roots |
| NRCS connector code or request helpers | `connectors/nrcs/` and product connector lanes |
| Canonical source descriptor records if a subtype-first lane is accepted as canonical | `data/registry/sources/soil/` after topology reconciliation |
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

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/soil/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/soil/       # possible canonical source descriptors
data/registry/soil/README.md      # compatibility pointer / migration note only
```

Do not maintain divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/soil/...` or `data/registry/sources/soil/` is canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, test, connector, pipeline, or public artifact.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source vintage, source scale, support type, resolution, retrieval time, valid/effective time, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, support type, evidence strength, review state, catalog state, release state, field-verification state, parcel truth, or public-safe posture.
- [ ] Confirm map-unit, component, horizon, station/depth, grid, model, and interpretation contexts are not collapsed.
- [ ] Confirm station observations, gridded products, and remote-sensing derivatives carry support, resolution, QC, and uncertainty limits before catalog or release eligibility is asserted.
- [ ] Confirm parcel, private-land, conservation, compliance, water-rights, field-verification, and management-decision contexts are not asserted from registry parent state.
- [ ] Confirm validation, unit-normalization, support-type, aggregation, transform, and policy receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, rights-change, support-change, and rollback paths exist for mutable, time-bound, rights-bound, support-bound, or externally governed source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public soil truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/soil/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/soil/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The child `sources/` README marks the domain-first path as confirmed but final topology NEEDS VERIFICATION against subtype-first source-registry patterns. | CONFIRMED by GitHub contents API during this edit |
| Cross-domain `data/registry/sources/README.md` says source registry records are admission and authority-control records and that per-domain subfolders such as `data/registry/sources/<domain>/` are permitted. | CONFIRMED by GitHub contents API in this sequence |
| Soil domain registry README says Soil source registry records belong in `data/registry/sources/soil/` or an accepted source registry lane and names Soil source families including SSURGO, SDA, gSSURGO, gNATSGO, Mesonet, SCAN, USCRN, SMAP, and SoilGrids. | CONFIRMED by GitHub contents API in this sequence |
| NRCS Soil Data Access documentation says product pages do not replace authoritative SourceDescriptor records in `data/registry/sources/`. | CONFIRMED by GitHub contents API in this sequence |
| NRCS connector README says NRCS products are multi-product and role-specific and must not be collapsed under one source role, cadence, scale, or release posture. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Soil registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Soil registry records. | UNKNOWN |
| Runtime registry resolution or governed API behavior reads this registry lane. | UNKNOWN |
| This README grants public access to Soil registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Soil registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> rights/sensitivity/support/stale-state gate -> lifecycle payload -> validation/unit/support/aggregation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Soil truth
```
