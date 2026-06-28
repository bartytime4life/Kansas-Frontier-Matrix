<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/hydrology/readme
name: Hydrology Registry README
path: data/registry/hydrology/README.md
type: data-registry-hydrology-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <hydrology-domain-steward>
  - <source-steward>
  - <dataset-steward>
  - <crosswalk-steward>
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
registry_scope: hydrology-domain-first-registry-parent
domain: hydrology
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-subtype-first-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; freshness-bound; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/hydrology/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - sources/README.md
  - ../../raw/hydrology/README.md
  - ../../work/hydrology/
  - ../../quarantine/hydrology/
  - ../../processed/hydrology/
  - ../../catalog/domain/hydrology/
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../docs/domains/hydrology/SOURCE_FAMILIES.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../contracts/domains/hydrology/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../policy/sensitivity/hydrology/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - hydrology
  - domain-first-registry
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
  - "This README replaces the greenfield stub at `data/registry/hydrology/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The inspected Hydrology source-registry doctrine names `data/registry/sources/hydrology/` as the registry data home. Therefore this parent is treated as a compatibility/routing lane until registry topology is reconciled."
  - "Hydrology source roles, time kinds, datum/unit metadata, regulatory flood context, modeled derivatives, provisional observations, aggregation scope, freshness, correction, and rollback remain explicit governance blockers."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Registry

Domain-first registry parent for Hydrology registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-1f9eda">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Hydrology registry boundary](#hydrology-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/hydrology/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, emergency alert material, or generated-answer authority.

---

## Scope

`data/registry/hydrology/` is a domain-first routing lane for Hydrology registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for the Hydrology lane.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Hydrology registry lane may point to or summarize governance state for:

- Hydrology source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, sensitivity, cadence, source-head, activation, intake, correction, supersession, stale-state, and freshness state;
- WBD/HUC, NHDPlus/3DHP, NWIS/Water Data, NFHL, 3DEP, state water-office, water-quality, groundwater, flood-evidence, drought, and irrigation-link blockers;
- source time, observed time, valid/effective time, retrieval time, release time, and correction time distinctions;
- datum, unit, parameter, site, geometry/support, approval-status, provisional-status, model-lineage, and aggregation-scope requirements;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, hydrologic claims, proof packs, catalog records, release manifests, public map artifacts, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/hydrology/
```

This is a **domain-first** registry path. Current Hydrology source-registry evidence also supports a **subtype-first** source registry pattern:

```text
data/registry/sources/hydrology/
```

Other registry parents in this sequence use subtype-first lanes such as:

```text
data/registry/domains/
data/registry/datasets/
data/registry/crosswalks/
```

Therefore, `data/registry/hydrology/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Hydrology domain-first registry parent | `data/registry/hydrology/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed Hydrology child registry lane | `data/registry/hydrology/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical Hydrology source lane | `data/registry/sources/hydrology/` | Named by Hydrology source-registry doctrine as registry data home; needs topology reconciliation with this path. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, parameters, units, datums, fields, and vocabularies. |
| Hydrology source payloads | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Hydrology semantic meaning | `contracts/domains/hydrology/` | Object-family meaning and invariants. |
| Hydrology machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/hydrology/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Hydrology policy and sensitivity | `policy/sensitivity/hydrology/`, `policy/domains/hydrology/`, `policy/rights/` | Exposure, rights, source-role, sensitivity, freshness, datum/unit, and admissibility rules. |
| Hydrology validation receipts | `data/receipts/validation/hydrology/` if/when accepted | Process memory for validation checks. |
| Hydrology proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Hydrology catalog projections | `data/catalog/domain/hydrology/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Hydrology release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Hydrology source descriptor and source-admission registry lane. | Not source payload storage, Hydrology truth, proof, receipt storage, catalog closure, semantic contract authority, policy, release authority, emergency alert material, or public output. |

---

## Hydrology registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/hydrology/...` and subtype-first lanes such as `data/registry/sources/hydrology/`. |
| Source role is preserved | Hydrology registry state must not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted source roles. |
| Regulatory is not observed | NFHL and similar regulatory flood context must not be reframed as observed inundation, forecast, or model output. |
| Provisional is not approved | Provisional readings and candidate records require lifecycle disposition before downstream claims. |
| Aggregate is not per-instant truth | Daily values, annual statistics, HUC rollups, drought links, and other rollups must carry aggregation scope. |
| Modeled is not observed | Rating curves, VAAs, catchments, DEM derivatives, hydrographs, reconstructed traces, and modeled surfaces require model/lineage support. |
| Time kinds stay distinct | Source time, observed time, valid/effective time, retrieval time, release time, and correction time remain separate where material. |
| Datum and units travel | Datum, units, parameter identity, site identity, geometry/support metadata, and approval status should remain explicit through lifecycle movement. |
| Registry is not validation | Validation receipts and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to README/routing material and registry-local sidecars that do not duplicate authority from subtype-first lanes:

- parent README and routing notes;
- compatibility notes explaining the domain-first versus subtype-first topology;
- migration notes, redirect notes, rollback notes, or topology decision notes;
- local indexes that point to child registry lanes without becoming authoritative records themselves;
- checksums, manifests, and signatures for registry routing material where applicable;
- pointers to source descriptors, dataset registry records, crosswalk registry records, domain registry records, contracts, schemas, policy refs, lifecycle payloads, validation receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, stale-state notices, and rollback cards.

If a child lane under this parent stores actual registry records, it must state whether it is canonical, compatibility, migration-only, or mirrored, and it must name its conflict/rollback path.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Hydrology source payloads, WBD/NHDPlus packages, water-data extracts, terrain products, regulatory flood packages, water-quality records, groundwater records, drought/irrigation feeds, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, or `data/processed/hydrology/` depending on lifecycle state |
| Emergency alert material, private identifiers, access secrets, sensitive local details, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/hydrology/`, `docs/sources/`, or source catalog docs |
| Canonical source descriptor records if `data/registry/sources/hydrology/` is accepted as canonical | `data/registry/sources/hydrology/` after topology reconciliation |
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

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/hydrology/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/hydrology/       # canonical source descriptors
data/registry/hydrology/README.md      # compatibility pointer / migration note only
```

Do not maintain two divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/hydrology/...` or subtype-first lanes such as `data/registry/sources/hydrology/` are canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source time, observed time, retrieval time, valid/effective time, freshness posture, datum/units, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, or public-safe posture.
- [ ] Confirm regulatory context, observed readings, modeled derivatives, aggregates, provisional material, and candidate evidence are not collapsed.
- [ ] Confirm regulatory flood context is not presented as observed inundation, forecast, or model output.
- [ ] Confirm sensitive local details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or time-bound Hydrology source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/hydrology/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/hydrology/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The Hydrology child `sources/` README marks the domain-first path as confirmed but layout-NEEDS VERIFICATION against `data/registry/sources/hydrology/`. | CONFIRMED by GitHub contents API during this edit |
| Hydrology source-registry doctrine names `data/registry/sources/hydrology/` as the registry data home and says source role is fixed at admission. | CONFIRMED by GitHub contents API in this sequence |
| Hydrology source-registry doctrine warns that regulatory flood layers must not collapse into observed flooding. | CONFIRMED by GitHub contents API in this sequence |
| Hydrology RAW README keeps RAW source capture separate from registry, proof, receipt, policy, release, public, and answer authority. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Hydrology registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Hydrology registry records. | UNKNOWN |
| This README grants public access to Hydrology registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Hydrology registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Hydrology truth
```
