<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-soil-moisture-readme
title: tools/validators/domains/soil/moisture README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-soil-contract-steward-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; per-domain-validator; soil; soil-moisture-observation; station-soil-moisture; satellite-grid-soil-moisture; unit-depth-qc; stale-state; support-type-separation; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Soil-specific moisture validator lane for checking SoilMoistureObservation candidates, station readings, satellite/grid observations, support-type separation, source role, source cadence, observation time, valid time, retrieval time, depth, unit, measurement type, QC flags, stale-state caveats, evidence, policy, release, correction, rollback, and public-surface denial posture while deferring Soil meaning, source registry authority, evidence records, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../_common/README.md
  - ../catalog_closure/README.md
  - ../dual_hash/README.md
  - ../horizon_depth/README.md
  - ../lineage/README.md
  - ../../../catalog_closure/README.md
  - ../../../cross-domain-joins/README.md
  - ../../../../../contracts/domains/soil/soil_moisture_observation.md
  - ../../../../../contracts/domains/soil/domain_observation.md
  - ../../../../../contracts/domains/soil/domain_validation_report.md
  - ../../../../../contracts/domains/soil/soil_time_caveat.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../../docs/runbooks/soil/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/ROLLBACK_RUNBOOK.md
  - ../../../../../docs/sources/catalog/nrcs/scan-soil-climate.md
  - ../../../../../docs/sources/catalog/noaa/noaa-uscrn.md
  - ../../../../../data/registry/sources/soil/README.md
  - ../../../../../data/catalog/domain/soil/README.md
  - ../../../../../data/proofs/soil/README.md
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "A SoilMoistureObservation semantic contract is confirmed, but its paired schema was not found in that contract-authoring task. Field realization and machine validation remain PROPOSED / NEEDS VERIFICATION."
  - "Soil moisture support types must not collapse: station readings, satellite/grid observations, survey map units, gridded derivatives, private operational sensors, and interpreted/public products are different support classes."
  - "This validator lane checks moisture observation posture only. It must not define Soil meaning, create SourceDescriptors, create EvidenceBundles, approve release, publish layers, certify agronomic suitability, or provide operational/private sensor disclosure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/soil/moisture

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--moisture-informational)
![boundary](https://img.shields.io/badge/boundary-validator--only-lightgrey)
![support](https://img.shields.io/badge/support--type-separate-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/soil/moisture/` is the proposed Soil-specific validator lane for checking `SoilMoistureObservation` unit, depth, QC, cadence, stale-state, source-role, support-type, evidence, policy, release, correction, rollback, and public-surface posture.

---

## Purpose

`tools/validators/domains/soil/moisture/` exists for Soil moisture observation checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Do Soil moisture candidates preserve source identity, source role, support type, station/grid subject, observation value, unit, depth, measurement type, QC flags, cadence, observed/source/valid/retrieval/release/correction time, stale-state caveats, EvidenceRef/EvidenceBundle support, policy posture, release linkage, correction lineage, rollback targets, and public-surface boundaries before they are used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Soil truth, source truth, station truth, satellite-grid truth, SourceDescriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/soil/moisture/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent `tools/validators/domains/soil/README.md` | **CONFIRMED stub** | Parent file currently says only `# validators :: soil`; this README keeps its own boundary explicit. |
| SoilMoistureObservation contract | **CONFIRMED in repo evidence / draft** | `contracts/domains/soil/soil_moisture_observation.md` defines a source-scoped time-series moisture observation with source, support type, unit, depth, cadence, QC, time scope, evidence, policy, release, and rollback posture. |
| Paired moisture schema | **NOT FOUND in contract evidence / NEEDS VERIFICATION** | The contract states that `schemas/contracts/v1/domains/soil/soil_moisture_observation.schema.json` was not found in that task; field-level machine shape remains proposed. |
| Soil proof lane | **CONFIRMED in repo evidence / draft** | `data/proofs/soil/README.md` says support-type separation is mandatory and that station reading, satellite grid, static survey, gridded derivative, pedon evidence, and interpretation cannot masquerade as one surface. |
| Moisture source families | **CONFIRMED in repo evidence / draft** | Current Soil evidence names station soil-moisture, satellite-grid, Kansas Mesonet, SCAN, USCRN, and SMAP as Soil source/support families. |
| Moisture executable, fixtures, policy bundles, source mappings, and CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not claim that a moisture validator executable, fixture set, source mapping, runtime integration, or CI check exists. |

[Back to top](#top)

---

## Proposed validation focus

Until a Soil schema/source profile confirms exact field names, this README treats the following as proposed validation concepts, not implemented fields:

| Concept | Proposed meaning | Notes |
|---|---|---|
| Observation value | Source-scoped moisture value. | Must carry measurement type and unit. |
| Measurement type | Volumetric, gravimetric, source-specific, modeled estimate, retrieval, or accepted schema-selected equivalent. | Do not infer type from source name alone. |
| Unit | Observation unit or measurement basis. | Unitless values must fail closed unless source contract explicitly permits. |
| Depth | Sensor depth, profile depth, grid retrieval depth band, or source-specific depth context. | Depth and depth unit must be explicit where material. |
| Support type | Station soil moisture, satellite-grid soil moisture, derivative, candidate, private operational sensor, or accepted equivalent. | Support types are not interchangeable. |
| QC flags | Quality-control, missing-value, stale-state, sensor/source/product, revision, or limitation flags. | QC must remain visible through release/public surfaces where material. |
| Cadence and time posture | Observed time, source time, valid time, retrieval time, release time, correction time, and stale-state caveat. | These time kinds must not collapse. |
| Spatial support | Station, grid cell, generalized location, hidden location, aggregate, or denied location marker. | Exact operational/private sensor disclosure must fail closed. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Soil-specific moisture validator entrypoints | `tools/validators/domains/soil/moisture/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Soil validator parent index | `tools/validators/domains/soil/` |
| Soil catalog closure validator | `tools/validators/domains/soil/catalog_closure/` |
| Soil dual-hash validator | `tools/validators/domains/soil/dual_hash/` |
| Soil horizon-depth validator | `tools/validators/domains/soil/horizon_depth/` |
| Soil lineage validator | `tools/validators/domains/soil/lineage/` |
| SoilMoistureObservation meaning | `contracts/domains/soil/soil_moisture_observation.md` or accepted contract home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| Soil source descriptors and source registry | `data/registry/sources/soil/` or accepted source registry home |
| Soil catalog records | `data/catalog/domain/soil/` or accepted catalog home |
| EvidenceBundle and proof support | `data/proofs/soil/`, `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/soil/moisture/`, `tests/domains/soil/`, `fixtures/domains/soil/soil_moisture_observation/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Soil moisture, support-type, unit, depth, QC, cadence, evidence, policy, and release-reference rules.
- **NEEDS VERIFICATION:** exact executable names, field names, schema homes, source mappings, fixture shape, policy bundles, report destinations, receipts, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Soil doctrine, moisture contract, schema home, policy home, source registry, catalog storage, proof storage, receipt storage, lifecycle data store, release record store, published artifact store, public runtime surface, operational sensor disclosure surface, or agronomic recommendation authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/soil/moisture/` include checks that:

- verify every consequential Soil moisture candidate points to an admitted Soil source descriptor or source-registry record;
- verify `support_type`, source role, source native ID, observation subject, observation value, unit, measurement type, depth, depth unit, QC flags, cadence, time posture, EvidenceRef, policy, release, correction, and rollback references where required;
- verify station readings, satellite-grid observations, gridded derivatives, static survey material, private operational sensors, and interpreted products are not collapsed;
- verify Mesonet/SCAN/USCRN-style station readings are not treated as SMAP-style satellite grids, SSURGO survey map units, countywide moisture surfaces, or management advice;
- verify SMAP/satellite-grid observations are not treated as station readings, private sensor feeds, or SSURGO survey truth;
- detect stale, missing, malformed, unitless, depthless, QC-denied, or cadence-ambiguous readings;
- detect when public-bound catalog entries, proof references, release candidates, map layers, Evidence Drawer payloads, Focus Mode answers, exports, or AI context depend on unvalidated moisture observations;
- emit deterministic validation reports without creating receipts, proofs, release manifests, public artifacts, or operational recommendations.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/soil/moisture/` | Correct home |
|---|---|
| SoilMoistureObservation meaning | `contracts/domains/soil/soil_moisture_observation.md` or accepted contract home |
| Soil moisture schema | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or accepted schema home |
| Soil source descriptors and source mappings | `data/registry/sources/soil/` or accepted source registry/source-profile home |
| Soil domain docs | `docs/domains/soil/` |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Pipeline execution logic or sensor parsers | `pipelines/domains/soil/`, `packages/domains/soil/`, or accepted implementation roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, operational sensor disclosure, or agronomic recommendation output | governed application/runtime roots |

[Back to top](#top)

---

## Soil moisture validator posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks source descriptor, source role, support type, source native ID, observation subject, observation value, unit, measurement type, depth context, QC posture, cadence, temporal scope, EvidenceRef, EvidenceBundle/proof reference, validation report, policy posture, release reference, correction path, or rollback target required for its use;
- collapses station soil moisture, satellite-grid soil moisture, static survey, gridded derivative, private operational sensor, pedon/profile, or interpreted product support;
- treats one station reading as countywide truth, survey map-unit truth, flood/drought authority, irrigation recommendation, or management advice;
- treats SMAP or another satellite/grid product as a station reading, private sensor record, SSURGO map unit, or field-verified condition;
- omits or masks units, depth, QC flags, stale-state caveats, source cadence, source revision, or missing-value posture where material;
- exposes private operational sensor data, farm-/owner-specific detail, precise private sensor location, or reverse-engineerable derivatives without rights, sensitivity review, policy, release, correction, and rollback support;
- treats Agriculture crop/yield, Hydrology drought/flood/streamflow, Atmosphere precipitation, Habitat, Geology, or Hazards claims as Soil-owned truth through a moisture artifact;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on unvalidated moisture observations;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale readings, stale source descriptors, or incomplete proof closure;
- treats moisture validation as EvidenceBundle creation, PolicyDecision creation, release approval, publication, operational advice, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_MOISTURE_PASS` | Configured Soil moisture checks passed. |
| `SOIL_MOISTURE_FAIL` | One or more configured Soil moisture checks failed. |
| `SOIL_MOISTURE_SOURCE_DESCRIPTOR_MISSING` | Required source descriptor or source registry pointer is absent. |
| `SOIL_MOISTURE_SUPPORT_TYPE_MISSING` | Required support-type label is absent. |
| `SOIL_MOISTURE_SUPPORT_TYPE_COLLAPSE` | Station, satellite-grid, survey, derivative, private sensor, or interpretation support types are conflated. |
| `SOIL_MOISTURE_VALUE_MISSING` | Observation value is absent where required. |
| `SOIL_MOISTURE_UNIT_MISSING` | Required observation unit is absent. |
| `SOIL_MOISTURE_UNIT_INVALID` | Observation unit is unsupported or inconsistent. |
| `SOIL_MOISTURE_DEPTH_MISSING` | Required depth or depth context is absent. |
| `SOIL_MOISTURE_DEPTH_UNIT_INVALID` | Depth unit is missing, unsupported, or mixed without accepted conversion. |
| `SOIL_MOISTURE_QC_MISSING` | Required quality-control or missing-value posture is absent. |
| `SOIL_MOISTURE_QC_DENIED` | QC flags or source posture deny use for the requested surface. |
| `SOIL_MOISTURE_TIME_SCOPE_MISSING` | Required observed/source/valid/retrieval/release/correction time is absent. |
| `SOIL_MOISTURE_STALE` | Observation is stale for the claimed use without a valid caveat or release posture. |
| `SOIL_MOISTURE_PRIVATE_SENSOR_DENIED` | Private or operational sensor data is unsafe for the requested surface. |
| `SOIL_MOISTURE_CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Soil without preserving boundaries. |
| `SOIL_MOISTURE_PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `SOIL_MOISTURE_LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/soil/moisture/
├── README.md
├── test_soil_moisture.py
└── fixtures/
    ├── valid_station_moisture_observation/
    ├── valid_satellite_grid_moisture_observation/
    ├── missing_source_descriptor/
    ├── support_type_collapse/
    ├── missing_unit/
    ├── invalid_unit/
    ├── missing_depth/
    ├── qc_denied/
    ├── stale_observation/
    ├── private_sensor_denied/
    └── cross_domain_authority_collapse/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/soil/moisture
```

```bash
python tools/validators/domains/soil/moisture/validate_soil_moisture.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_soil_moisture.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Soil contracts, schemas, source descriptors, source-role rules, and policy rather than defining meaning locally.
- [ ] Station, satellite-grid, survey, derivative, private sensor, pedon/profile, and interpretation support types remain distinct.
- [ ] Unit, depth, measurement type, QC, cadence, stale-state, and temporal scope remain visible.
- [ ] Moisture checks do not replace SourceDescriptor, EvidenceBundle, proof, receipt, PolicyDecision, ReleaseManifest, correction, or rollback records.
- [ ] Cross-domain joins preserve Agriculture, Hydrology, Atmosphere, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, private operational sensors, or stale readings.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, operational advice, source authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Soil moisture validator file. |
| Next smallest safe change | Verify actual Soil moisture scripts, accepted field names, unit/depth/QC rules, schemas, source mappings, source descriptors, fixtures, report destinations, receipts, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
