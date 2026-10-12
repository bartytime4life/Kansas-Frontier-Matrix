<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/proofs/hydrology/readme
title: Hydrology Proofs README
type: data-lifecycle-readme
version: v0.1
status: draft
owners: <PLACEHOLDER — Data steward · Hydrology lane steward · Proof/release steward · Safety/policy reviewer>
created: 2026-06-25
updated: 2026-06-25
policy_label: internal-planning
intended_path: data/proofs/hydrology/README.md
owning_root: data/
lifecycle_area: proofs
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/domains/hydrology/README.md
  - docs/domains/hazards/README.md
  - docs/domains/soil/README.md
  - docs/domains/agriculture/README.md
  - docs/domains/settlements-infrastructure/README.md
  - data/receipts/hydrology/README.md
  - data/catalog/README.md
  - data/published/hydrology/README.md
  - release/manifests/hydrology/README.md
  - schemas/contracts/v1/domains/hydrology/
  - policy/domains/hydrology/
  - policy/release/hydrology/
tags: [kfm, data, proofs, hydrology, evidence, validation, policy, release, rollback, huc12, wbd, nhdplus, usgs-water-data, nfhl, source-role]
notes:
  - "This README governs the hydrology proof lane only; it is not itself a proof object, release decision, emergency alert, flood warning, or publication manifest."
  - "Hydrology proofs must preserve source-role separation: observed water conditions, watershed units, regulatory flood context, terrain-derived context, models, and public map artifacts are different truth classes."
  - "Implementation depth remains UNKNOWN until verified against the mounted repository, schemas, validators, fixtures, CI, emitted receipts, emitted proofs, and release manifests."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Proofs

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success?style=flat-square)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-orange?style=flat-square)
![area](https://img.shields.io/badge/data%20area-proofs-blue?style=flat-square)
![domain](https://img.shields.io/badge/domain-hydrology-1f6feb?style=flat-square)
![safety](https://img.shields.io/badge/not%20for-flood%20warning-critical?style=flat-square)
![publication](https://img.shields.io/badge/publication-not%20by%20file%20move-critical?style=flat-square)

> **One-line purpose.** `data/proofs/hydrology/` stores machine-checkable proof objects that support hydrology-domain evidence closure, source-role separation, validation, policy decisions, catalog closure, release review, correction, and rollback — without turning KFM into a live flood-warning, emergency-response, or regulatory-determination authority.

---

## Mini table of contents

- [1. Scope](#1-scope)
- [2. Directory contract](#2-directory-contract)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Hydrology proof responsibilities](#5-hydrology-proof-responsibilities)
- [6. Expected object families](#6-expected-object-families)
- [7. Naming and identity](#7-naming-and-identity)
- [8. Minimum proof closure checklist](#8-minimum-proof-closure-checklist)
- [9. Hydrology thin-slice proof pattern](#9-hydrology-thin-slice-proof-pattern)
- [10. Safety, policy, and source-role posture](#10-safety-policy-and-source-role-posture)
- [11. Validation expectations](#11-validation-expectations)
- [12. Promotion, publication, and rollback](#12-promotion-publication-and-rollback)
- [13. Maintenance checklist](#13-maintenance-checklist)
- [14. Open verification backlog](#14-open-verification-backlog)

---

## 1. Scope

This directory is the hydrology-domain lane under the KFM proof lifecycle area.

It exists to hold proof artifacts for claims and derived outputs involving watersheds, HUC12/WBD context, flowlines, NHD/NHDPlus identity, stream permanence, gauge and site observations, hydrographs, observed water conditions, groundwater/surface-water context, regulatory floodplain context, terrain-derived hydrology, wetland/riparian context, drought/flood hydrologic indicators, and public-safe hydrology layer candidates.

The proof lane supports review and publication decisions. It does **not** publish anything by itself.

### Safety boundary

KFM hydrology outputs are evidence-backed context for mapping, history, review, planning, resilience, and explanation. They are **not** flood warnings, emergency alerts, evacuation instructions, rescue guidance, navigation guidance, dam-safety directives, engineering determinations, or authoritative regulatory decisions.

Any proof artifact that touches flood, drought, warning, advisory, or operational hydrologic material must record source authority, source role, issue time where relevant, valid time, retrieval time, release time, stale-state behavior, and official-source referral behavior.

### Truth posture

| Statement | Status |
|---|---:|
| `data/proofs/hydrology/` is the intended home for hydrology proof artifacts. | **PROPOSED** until verified against the mounted repo and Directory Rules version in force. |
| Hydrology proofs must remain downstream of source descriptors, evidence records, validation, policy, review state, and release state. | **CONFIRMED doctrine / PROPOSED lane application**. |
| Hydrology public surfaces must keep observed conditions, hydrologic units, regulatory flood context, models, and map artifacts distinct. | **CONFIRMED doctrine / PROPOSED implementation control**. |
| Existing hydrology proof schemas, validators, CI jobs, fixtures, and emitted proof packs are present. | **UNKNOWN** until inspected in a mounted checkout. |

---

## 2. Directory contract

`data/proofs/hydrology/` is a responsibility-rooted lane, not a topic bucket.

It answers to:

- the `data/` lifecycle root;
- the `proofs/` lifecycle area;
- the hydrology domain lane;
- evidence, validation, policy, release, correction, and rollback governance;
- the KFM rule that promotion is a governed state transition, not a file move;
- the hydrology safety rule that KFM does not act as a live flood-warning or emergency-response authority.

### Contract summary

| Field | Value |
|---|---|
| Root owner | `data/` lifecycle stewardship |
| Area owner | Proof / release support stewardship |
| Domain lane | Hydrology |
| Public exposure | None by direct file path |
| Normal public path | Governed API → released artifact / catalog / EvidenceBundle projection / policy-filtered hydrology view |
| Adjacent lifecycle roots | `data/receipts/`, `data/catalog/`, `data/published/`, `release/` |
| Required public label | Context and evidence support only; not emergency alerting, flood warning, engineering determination, or regulatory authority unless the released source supports that limited context |
| Forbidden shortcut | Direct UI, API, model, or map access to this folder as public truth |

---

## 3. What belongs here

Store proof objects that can be independently inspected, validated, hashed, compared, cited by a release decision, and used for correction or rollback review.

Examples include:

| Proof artifact | Purpose | Status |
|---|---|---:|
| `proofpack.<hydrology_object_id>.<run_id>.json` | Bundled proof closure for one hydrology object, candidate layer, analytical summary, or release candidate. | **PROPOSED** |
| `validation-proof.<run_id>.json` | Shows schema, geometry, CRS, topology, temporal, freshness, source-reference, and source-role validation outcomes. | **PROPOSED** |
| `policy-proof.<run_id>.json` | Records rights, sensitivity, source-role, release-state, access, and public-safety boundary checks. | **PROPOSED** |
| `identity-permanence-proof.<object_id>.json` | Confirms hydrologic identity, flowline/crosswalk permanence, and deterministic object continuity rules. | **PROPOSED** |
| `huc12-context-proof.<huc12_id>.<run_id>.json` | Confirms watershed identity, source version, geometry fingerprint, and temporal support. | **PROPOSED** |
| `gauge-observation-proof.<site_id>.<run_id>.json` | Confirms site identity, observation time, retrieval time, units, datum, source role, and EvidenceBundle support. | **PROPOSED** |
| `nfhl-source-role-proof.<artifact_id>.json` | Confirms NFHL/regulatory flood context is not mislabeled as an observed flood event or live warning. | **PROPOSED** |
| `terrain-derivation-proof.<artifact_id>.json` | Confirms terrain-derived stream, basin, wetness, slope, or flow-accumulation products carry method, DEM source, resolution, and uncertainty support. | **PROPOSED** |
| `temporal-support-proof.<object_id>.json` | Confirms source, observed, valid, retrieval, release, stale, and correction times are distinct where material. | **PROPOSED** |
| `evidence-closure-proof.<evidence_bundle_id>.json` | Confirms every material hydrology claim has resolvable evidence support. | **PROPOSED** |
| `catalog-closure-proof.<catalog_record_id>.json` | Confirms catalog, provenance, citation, digest, source-role, and release-candidate closure before release review. | **PROPOSED** |
| `public-safe-geometry-proof.<artifact_id>.json` | Documents generalization, suppression, precision degradation, or withheld infrastructure/sensitive geometry. | **PROPOSED** |
| `public-safety-boundary-proof.<artifact_id>.json` | Confirms the artifact cannot be represented as a live alert, official warning, rescue instruction, or emergency directive. | **PROPOSED** |
| `rollback-proof.<release_candidate_id>.json` | Confirms a rollback target exists and is sufficient before release. | **PROPOSED** |

Proof objects should be small, structured, deterministic where practical, and reproducible from the referenced inputs.

---

## 4. What does not belong here

Do **not** store these in `data/proofs/hydrology/`:

| Do not store | Correct home | Reason |
|---|---|---|
| Raw USGS, NHD, WBD, NFHL, NOAA/NWS, state, local, sensor, gauge, raster, or source API payloads | `data/raw/hydrology/` or `data/raw/<source-family>/` | Raw material must remain in the RAW lifecycle area. |
| Live warning feeds, alert streams, emergency dashboards, or operational water-condition dashboards | Connector/runtime/source-specific areas, with no public path unless separately governed | Proofs may snapshot and prove context; they are not live alert feeds. |
| Work-in-progress transforms or failed normalization outputs | `data/work/hydrology/` or `data/quarantine/hydrology/` | Proofs cite work; they are not the work surface. |
| Validated processed hydrology records | `data/processed/hydrology/` | Processed objects are source-derived records, not proof records. |
| STAC, DCAT, PROV, or other catalog records | `data/catalog/` | Catalog records have their own lifecycle responsibility. |
| Runtime receipts | `data/receipts/hydrology/` | Receipts record runs/actions; proofs support closure and decisions. |
| Release manifests, promotion decisions, rollback cards, correction notices | `release/` | Release authority belongs to the release responsibility root. |
| Public PMTiles, GeoParquet, GeoJSON, COG, CSV, report, or API payload exports | `data/published/hydrology/` | Published artifacts are the released delivery surface. |
| Policy rules | `policy/` | Policy authority does not live inside proof data. |
| Schemas | `schemas/contracts/v1/domains/hydrology/` or another ADR-approved schema home | Schema authority belongs under the schema root. |
| Tests or fixtures | `tests/` and `fixtures/` | Test evidence belongs in test/fixture roots, not lifecycle data. |
| Model code, notebooks, or validators | `packages/`, `pipelines/`, `tools/validators/`, or `scripts/` as appropriate | Executable logic must not be hidden inside proof data. |

---

## 5. Hydrology proof responsibilities

Hydrology proofs should answer these questions before a hydrology artifact can support a public or semi-public claim:

1. **Source support:** Which source descriptors support this hydrology object or derived artifact?
2. **Source role:** Is the object an observation, watershed unit, flowline identity, regulatory context, terrain-derived result, model output, or public map artifact?
3. **Evidence closure:** Which EvidenceBundle supports each material claim?
4. **Spatial support:** What geometry, CRS, topology, scale, resolution, snapping, conflation, and generalization rules apply?
5. **Temporal support:** What source, observed, valid, retrieval, release, stale, and correction times matter?
6. **Policy support:** Are rights, terms, sensitivity, official-source referral, public-safety disclaimers, and steward review requirements satisfied?
7. **Validation support:** Which validators passed, failed, abstained, denied, or require review?
8. **Release support:** Which release candidate or manifest cites this proof?
9. **Correction support:** What stale-state, correction, supersession, and rollback path exists?

A proof object should be rejected if it cannot identify the source, evidence, policy, validation, and release context it is meant to support.

---

## 6. Expected object families

Hydrology proof objects may support, but do not replace, these hydrology-domain object families:

| Hydrology object family | Proof concern |
|---|---|
| `WatershedUnit` / `HUC12` | Unit identity, boundary source, source version, geometry fingerprint, valid/source/retrieval time. |
| `Flowline` / `Reach` | Stable identifier, crosswalk, conflation method, topology, permanence, source version. |
| `HydroSite` / `GaugeSite` | Site identity, station metadata, datum/unit handling, relocation or decommissioning status. |
| `WaterObservation` | Observed time, parameter, unit, method, quality flag, retrieval time, evidence support. |
| `Hydrograph` | Time-series window, aggregation method, missing data, unit conversion, source role, uncertainty. |
| `NFHLZone` / `RegulatoryFloodContext` | Regulatory source role, effective date, flood-zone semantics, not observed/current flood status. |
| `FloodEventObservation` | Event source, observed/valid time, event boundary uncertainty, relation to official reports. |
| `DroughtHydrologyIndicator` | Indicator method, aggregation window, source role, uncertainty, stale-state behavior. |
| `TerrainDerivedHydrology` | DEM source, resolution, flow-routing method, sinks/breaches, uncertainty, derivative warning. |
| `WetlandRiparianContext` | Source vocabulary, relation to habitat/soil lanes, geometry generalization, sensitivity review. |
| `HydrologyLayerManifest` | Layer identity, source roles, evidence links, public-safe geometry, release and rollback references. |
| `EvidenceDrawerPayload` | EvidenceBundle projection, citation status, policy state, stale/correction state, finite outcome. |

When a proof references hazards, soils, agriculture, habitat, settlements, or infrastructure evidence, it must preserve the owning lane and should not collapse those claims into hydrology authority.

---

## 7. Naming and identity

Use names that are deterministic enough to diff and inspect.

Recommended pattern:

```text
<proof_family>.<domain>.<stable_object_or_candidate_id>.<run_id>.json
```

Examples:

```text
proofpack.hydrology.huc12_102600060305_demo.run_20260625T000000Z.json
validation-proof.hydrology.gauge_usgs_06892350_demo.run_20260625T000000Z.json
identity-permanence-proof.hydrology.flowline_demo_comid_123456.run_20260625T000000Z.json
nfhl-source-role-proof.hydrology.nfhl_zone_demo.run_20260625T000000Z.json
terrain-derivation-proof.hydrology.flow_accumulation_demo.run_20260625T000000Z.json
catalog-closure-proof.hydrology.layer_candidate_huc12_public_demo.run_20260625T000000Z.json
public-safety-boundary-proof.hydrology.flood_context_demo.run_20260625T000000Z.json
```

### Identity guidance

A proof record should carry, at minimum:

- `proof_id`
- `proof_family`
- `domain`
- `object_id` or `release_candidate_id`
- `run_id`
- `source_descriptor_ids`
- `source_role`
- `evidence_bundle_ids`
- `validation_report_ids`
- `policy_decision_ids`
- `catalog_record_ids`
- `release_candidate_id`
- `content_hash`
- `input_hashes`
- `schema_version`
- `generated_at`
- `valid_time` where material
- `retrieval_time` where material
- `release_time` where material
- `correction_or_supersession_ref` when present
- `rollback_ref` when present

### Deterministic identity inputs

Hydrology proof identity should consider:

- source ID and authority role;
- source role: observation, regulatory context, hydrographic unit, terrain derivative, model, or release artifact;
- hydrologic identifier: HUC, reach/COMID, site number, flood zone ID, layer ID, or candidate release ID;
- geometry fingerprint and CRS when geometry matters;
- source version and schema version;
- observed, valid, source, retrieval, release, and correction time where material;
- canonicalized payload hash;
- transform, validator, and policy version where output is derived or public-safe.

---

## 8. Minimum proof closure checklist

Before a hydrology proof can be cited by release review, it should satisfy this checklist:

- [ ] The proof declares its object family, source role, and domain lane.
- [ ] Every material claim resolves to at least one EvidenceBundle or declares `ABSTAIN`.
- [ ] Source descriptors identify source role, rights, retrieval method, citation, and sensitivity posture.
- [ ] Hydrology source roles are not collapsed.
- [ ] NFHL/regulatory flood context is never labeled as observed flood, current flood status, or emergency warning.
- [ ] Observed water data records distinguish observed time from retrieval time and release time.
- [ ] Watershed/flowline identity records include source version and deterministic identity inputs.
- [ ] Geometry, CRS, precision, scale, topology, and generalization are recorded where relevant.
- [ ] Validation outcomes are finite: `ANSWER`, `ALLOW`, `HOLD`, `ABSTAIN`, `DENY`, or `ERROR`, depending on the relevant contract.
- [ ] Policy decisions include rights, sensitivity, access, stale-state, official-source referral, and public-safety checks.
- [ ] Catalog/provenance/citation closure exists or the proof is held from release.
- [ ] The proof records content hashes and input hashes.
- [ ] A release candidate cites the proof, or the proof is clearly marked as pre-release support.
- [ ] A correction path and rollback target exist before public release.

---

## 9. Hydrology thin-slice proof pattern

A safe first slice should be fixture-first and no-network by default.

Recommended first slice:

```text
one HUC12 fixture
+ one normalized hydrology observation fixture
+ one regulatory flood-context fixture
+ one terrain or flowline identity fixture
+ one EvidenceBundle
+ one validation proof
+ one policy proof
+ one catalog-closure proof
+ one layer manifest candidate
+ one Evidence Drawer payload fixture
+ one release dry-run
+ one rollback proof
```

### Example folder sketch

```text
data/proofs/hydrology/
├── README.md
├── huc12_demo/
│   ├── proofpack.hydrology.huc12_102600060305_demo.run_20260625T000000Z.json
│   ├── validation-proof.hydrology.huc12_102600060305_demo.run_20260625T000000Z.json
│   └── catalog-closure-proof.hydrology.layer_candidate_huc12_public_demo.run_20260625T000000Z.json
├── gauge_demo/
│   ├── proofpack.hydrology.gauge_usgs_06892350_demo.run_20260625T000000Z.json
│   └── temporal-support-proof.hydrology.gauge_usgs_06892350_demo.run_20260625T000000Z.json
├── nfhl_demo/
│   ├── nfhl-source-role-proof.hydrology.nfhl_zone_demo.run_20260625T000000Z.json
│   └── public-safety-boundary-proof.hydrology.flood_context_demo.run_20260625T000000Z.json
└── release_candidate_demo/
    ├── evidence-closure-proof.hydrology.layer_candidate_huc12_public_demo.run_20260625T000000Z.json
    └── rollback-proof.hydrology.layer_candidate_huc12_public_demo.run_20260625T000000Z.json
```

This sketch is illustrative. Verify exact schema names, fixture IDs, and run-ID conventions before committing emitted proof objects.

---

## 10. Safety, policy, and source-role posture

Hydrology proof review should deny or hold artifacts when any of these conditions apply:

| Condition | Expected outcome | Reason |
|---|---:|---|
| NFHL/regulatory flood context is described as observed flood or current flood status. | `DENY` | Regulatory context and observed events are different source roles. |
| KFM output is framed as a flood warning, emergency alert, evacuation instruction, or rescue guidance. | `DENY` | KFM is not a life-safety authority. |
| Source rights, terms, or redistribution status are unclear. | `HOLD` / `DENY` | Publication requires rights support. |
| Source role is missing or ambiguous. | `HOLD` / `ABSTAIN` | Hydrology depends on source-role separation. |
| Observation time, retrieval time, or release time is missing where material. | `HOLD` / `ABSTAIN` | Time-aware support is required. |
| Gauge/site identity cannot be resolved or conflicts with source metadata. | `HOLD` / `DENY` | Identity stability is required for trust. |
| Geometry is overprecise for sensitive infrastructure, private-property, or security-relevant context. | `HOLD` / `DENY` until generalized or withheld | Public-safe geometry must be proven. |
| EvidenceBundle cannot be resolved. | `ABSTAIN` / `DENY` | Cite-or-abstain is the default truth posture. |
| Release candidate has no rollback target. | `HOLD` / `DENY` | Public release must be reversible. |

### Source-role anti-collapse rules

Hydrology proofs must keep these distinctions visible:

- `WatershedUnit` is not a water observation.
- `Flowline` is not proof of current water presence.
- `NFHLZone` is not an observed flood event or live flood warning.
- `TerrainDerivedHydrology` is a derivative method output, not direct observation.
- `Hydrograph` is an observation-derived visualization or series, not the source itself.
- `ModelOutput` is interpretation and must carry method, uncertainty, and limits.
- `PublishedLayer` is a released carrier, not sovereign truth.
- `FocusModeAnswer` is interpretive and must remain downstream of released evidence and policy.

---

## 11. Validation expectations

Hydrology proof validation should include, where relevant:

| Validator class | Checks |
|---|---|
| Schema validation | Required fields, enum values, version pins, canonical JSON behavior. |
| Evidence validation | EvidenceRef resolution, EvidenceBundle completeness, citation closure. |
| Source-role validation | Observation/regulatory/model/terrain-derived/release-artifact separation. |
| Identity validation | HUC/site/flowline IDs, source version, crosswalk stability, duplicate handling. |
| Temporal validation | Observed, valid, source, retrieval, release, stale, correction, and expiry times. |
| Spatial validation | Geometry validity, CRS, topology, scale, snapping/conflation, generalization. |
| Policy validation | Rights, sensitivity, access, public-safety boundary, official-source referral. |
| Catalog closure validation | STAC/DCAT/PROV/digest/citation support where release-relevant. |
| Release validation | ReleaseManifest linkage, proof-pack linkage, rollback target, correction path. |

Validator reports may be referenced by proof objects, but validator execution receipts belong under `data/receipts/` unless a specific report is itself a proof object.

---

## 12. Promotion, publication, and rollback

A proof object in this directory does not promote or publish a hydrology artifact.

Publication requires at least:

1. source descriptors and rights posture;
2. processed hydrology objects or released candidates;
3. EvidenceBundle support;
4. validation reports and proof closure;
5. policy decisions;
6. catalog closure;
7. release manifest and promotion decision;
8. public-safe artifact generation;
9. correction notice path;
10. rollback card or rollback proof.

### Release handoff

Hydrology release candidates should cite proof objects by stable ID and digest. The release root owns the final promotion decision; `data/proofs/hydrology/` only supplies trust evidence.

### Rollback expectations

Every public hydrology artifact supported by this directory should have enough proof metadata to answer:

- Which proof objects supported the release?
- Which source versions and inputs were used?
- Which map/API/report artifacts were published?
- Which caches or indexes must be invalidated?
- Which previous release or safe empty state can be restored?
- Which correction notice should be shown to users?

---

## 13. Maintenance checklist

Use this checklist when adding or reviewing hydrology proof files:

- [ ] File is in the hydrology proof lane because it is a proof object, not because it is merely hydrology-related.
- [ ] File is structured, deterministic, and hashable.
- [ ] File names include proof family, domain, stable object/candidate ID, and run ID.
- [ ] Source roles are explicit and not collapsed.
- [ ] NFHL/regulatory context is not treated as observed flood or live warning.
- [ ] Time fields are separated where material.
- [ ] EvidenceBundle references are resolvable or the proof abstains.
- [ ] Policy decisions and validation reports are referenced by ID/digest.
- [ ] Sensitive geometry and infrastructure/private-property implications are reviewed.
- [ ] Public-safety boundary and official-source referral are present where needed.
- [ ] Release candidate, catalog record, and rollback references are present when release-relevant.
- [ ] No raw payloads, work files, receipts, policies, schemas, tests, notebooks, or published artifacts were placed here.

---

## 14. Open verification backlog

| Item | Status | Verification step |
|---|---:|---|
| Confirm this exact directory exists in the mounted repo. | **NEEDS VERIFICATION** | Inspect `data/proofs/hydrology/` in a checkout. |
| Confirm parent `data/proofs/README.md` contract. | **NEEDS VERIFICATION** | Compare this README with parent proof-lane README. |
| Confirm current Directory Rules version and any ADRs affecting `data/proofs/`. | **NEEDS VERIFICATION** | Inspect `docs/doctrine/directory-rules.md` and accepted ADRs. |
| Confirm hydrology schema home and object-family names. | **NEEDS VERIFICATION** | Inspect `schemas/contracts/v1/domains/hydrology/` and `contracts/`. |
| Confirm hydrology validators and fixture conventions. | **NEEDS VERIFICATION** | Inspect `tools/validators/`, `tests/`, and `fixtures/`. |
| Confirm emitted hydrology receipts/proofs/release manifests exist. | **UNKNOWN** | Inspect generated data and CI outputs. |
| Confirm source rights and redistribution posture for hydrology sources. | **NEEDS VERIFICATION** | Review source descriptors and rights registry. |
| Confirm public-safety wording with hazards/safety reviewers. | **NEEDS VERIFICATION** | Review with hazards, hydrology, and policy stewards. |
| Confirm rollback and correction path for hydrology releases. | **NEEDS VERIFICATION** | Inspect `release/`, `data/rollback/`, and correction-notice docs. |

---

## Maintainer note

This README should evolve only when proof-lane responsibilities change. Do not use it to define schemas, rewrite policy, publish hydrology layers, or bless source claims. Those belong in their own responsibility roots.

[Back to top](#top)
