<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/glossary
title: Soil terminology and evidence distinctions
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil terminology and evidence distinctions; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/IDENTITY_MODEL.md
  - docs/domains/soil/DATA_LIFECYCLE.md
  - tools/validators/domains/soil/support_type/README.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# GLOSSARY

Use these definitions to read Soil documentation without collapsing distinct
kinds of evidence. Machine tokens are profile-specific; this glossary does not
create a global enum or an alias map.

## Soil objects and support

| Term | Meaning in this lane | Do not infer |
|---|---|---|
| Map unit | Survey mapping unit with source-native identity and spatial support | A uniform material or property at every point |
| MUKEY | Source-native map-unit key preserved with source/version lineage | A globally timeless geometry identity |
| Component | Constituent soil component associated with a map unit | Exact mapped position of every component |
| COKEY | Source-native component key | A parcel or ownership identifier |
| Horizon | Depth-bounded profile interval with units and method | A continuous geological stratum across the map |
| CHKEY | Source-native horizon key | Independent proof of a measured property |
| Pedon/profile | Local vertical soil evidence or its source-bound view | Regional subsurface continuity |
| Hydrologic soil group | Soil interpretation relevant to runoff context | Streamflow, groundwater level or flood prediction |
| Station observation | Sensor/site observation with time, depth, unit and QC | Conditions across every nearby field |
| Satellite/model grid | Gridded remote-sensing or model-assimilation support | A station measurement or a pixel-level field observation |
| Interpretation | Method- and purpose-bound derived assessment | A direct measurement or universal suitability |
| Support type | The spatial/observational basis of a record | Source authority, rights or release approval |
| Source role | Whether evidence is observed, modeled, administrative or otherwise qualified in its contract | An interchangeable synonym for support type |

## Time, quality and identity

**Vintage** identifies the source survey/product edition. **Observation time**
identifies when the represented observation applies. **Retrieval time** records
when bytes were obtained. A fresh retrieval can contain an old observation.

**Depth support** records the interval and unit to which a value applies.
Surface moisture and root-zone moisture are different supports. **QC** records
quality flags or checks; **uncertainty** records limitations or variability.
Neither may be silently replaced with a single confidence score.

A **content hash** binds selected bytes; a **specification hash** binds the
profile's declared semantics or configuration. Their exact inputs depend on the
owning profile. A digest match establishes identity at that scope, not scientific
truth. See the [identity model](IDENTITY_MODEL.md).

## Lifecycle and finite outcomes

| Term | Scope |
|---|---|
| RAW | Source capture under the applicable custody and admission process |
| WORK / QUARANTINE | Candidate or held material; not public consumption authority |
| PROCESSED | Transformed material retaining method and evidence lineage |
| CATALOG / TRIPLET | Governed discovery/relationship projections; not replacement evidence |
| PUBLISHED | A separately governed public carrier, not any reachable file |
| `PASS` | The particular validator's checks pass; inspect its contract |
| `HOLD` | Required support or a gate is unresolved |
| `DENY` | A forbidden or failed condition is explicitly rejected |
| `ABSTAIN` | The profile cannot support the requested determination |
| `READY_FOR_REVIEW` | All catalog-assessment declarations are satisfied; review is still pending |
| `PROMOTION_CANDIDATE` | Material change deserves review; promotion has not occurred |
| `NON_EVENT` | No substantive change under that exact materiality profile |

## Vocabulary conflicts

The public-safe smoke fixture uses `static_survey`, `station_observation`,
`satellite_grid` and `modeled_derivative`. Richer support-profile terms also
exist, including `authoritative_static_soil` and `station_soil_moisture`.
Use the exact token from the bound schema. Consult
[support-type validation](../../../tools/validators/domains/soil/support_type/README.md)
before translating between profiles; similar wording is not an accepted mapping.

## Maintenance

Add a term only with an owning contract, code profile or clearly labeled proposal.
Record incompatible meanings instead of smoothing them away. Refer scientific
interpretation disputes to the relevant steward role and keep the unresolved
claim out of authoritative public output.
