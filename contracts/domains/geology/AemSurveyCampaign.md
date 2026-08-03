<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-aem-survey-campaign
title: AemSurveyCampaign Contract — Geology / Hydrology (GMD 3 AEM 2026)
type: semantic-contract
version: v0.1
status: draft; PROPOSED; DISABLED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Geophysics steward
  - OWNER_TBD — Spatial/CRS steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Sensitivity reviewer
linked_schema: schemas/contracts/v1/domains/geology/aem_survey_campaign.schema.json
linked_source_descriptor: fixtures/contracts/v1/source/source_descriptor/valid/valid_gmd3_aem_2026.json
fixtures_root: fixtures/domains/geology/aem_survey_campaign/
governance_issue: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1944
[/KFM_META_BLOCK_V2] -->

# `AemSurveyCampaign` Contract — Geology / Hydrology

> **Status**: PROPOSED — disabled, noncanonical candidate. No connector activation,
> schedule, credential, live payload, release, or publication is authorized by this
> contract. No product is asserted to exist until official bytes and source metadata
> are formally observed.

---

## Purpose

`AemSurveyCampaign` is the canonical source-family packet for an airborne
electromagnetic (AEM) survey campaign admitted into the KFM geology domain.
This contract governs the **2026 Southwest Kansas GMD 3 AEM survey** conducted by
the Kansas Geological Survey (KGS), Groundwater Management District No. 3 (GMD 3),
and Aqua Geo Frameworks.

Cross-domain consumers (geology *and* hydrology) **must** reference one campaign
identity rather than creating duplicate source authorities.

---

## Required Stage Separation

The following stages are **distinct** and must **never** be interchanged or
collapsed into each other:

| Stage | Object type | Description |
|-------|------------|-------------|
| 1 | `AemSurveyCampaign` | Survey campaign and planned/actual footprint |
| 2 | `AemFlightLine` | Flight line and acquisition segment |
| 3 | `AemRawObservation` | Raw instrument observation |
| 4 | `AemNavigationRecord` | Navigation/positioning and altitude observation |
| 5 | `AemProcessingRun` | Processing run and software/configuration version |
| 6 | `AemInversionModel` | Inversion model/version |
| 7 | `AemResistivityProduct` | Resistivity section or voxel product |
| 8 | `AemHydrostratigraphicProduct` | Interpreted hydrostratigraphic unit/product |
| 9 | `AemUncertaintyRecord` | Uncertainty/quality-control result |
| 10 | `AemRecommendation` | Recommendation, plan, or management decision |
| 11 | `AemReleaseCarrier` | Released carrier and release decision |

A processed or interpreted product must not rewrite the raw acquisition identity.
A resistivity map or voxel is **not** a groundwater-level observation, water-right
record, legal finding, recommendation, or release authority.

---

## Minimum Contract Fields

### Identity

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Stable campaign identity (`kfm:geology:aem-campaign:<slug>`) |
| `object_type` | yes | Must be `"AemSurveyCampaign"` |
| `product_id` | yes | Must differ from `source_descriptor_ref` (no identity collapse) |
| `source_descriptor_ref` | yes | Reference to the canonical SourceDescriptor (`src:kgs-gmd3-aem-2026`) |

### Spatial Reference

| Field | Required | Description |
|-------|----------|-------------|
| `horizontal_crs` | yes | Horizontal CRS (e.g., `"EPSG:4326"`) |
| `vertical_datum` | yes | Vertical datum — must not be absent or unknown |
| `depth_reference` | yes | Depth reference benchmark (e.g., `"land_surface"`) |
| `depth_positive_direction` | yes | Must be `"down"` or `"up"` — no ambiguity |

### Acquisition State

| Field | Required | Description |
|-------|----------|-------------|
| `campaign_state` | yes | `planned`, `in_flight`, `completed`, or `abandoned` |
| `acquisition_state` | yes | `planned`, `actual`, `partial`, or `unknown` |

### Processing and Inversion

| Field | Required | Description |
|-------|----------|-------------|
| `processing_software_version` | yes | Non-empty processing software version string |
| `inversion_software_version` | yes | Non-empty inversion software version string |
| `raw_source_ref` | yes | Reference to the raw acquisition record (lineage must not break) |

### Product Units

| Field | Required | Description |
|-------|----------|-------------|
| `resistivity_units` | yes | Resistivity units (e.g., `"ohm·m"`) — must not be absent |

### Uncertainty

| Field | Required | Description |
|-------|----------|-------------|
| `uncertainty` | yes | Uncertainty/QC block — must not be omitted |
| `uncertainty.method` | yes | Description of the uncertainty method |

### Governance

| Field | Required | Description |
|-------|----------|-------------|
| `evidence_refs` | yes | At least one EvidenceRef binding — must not be empty |
| `release_state` | yes | `not_released` for all proposed/disabled records |
| `correction` | conditional | If present, must carry `supersedes_ref` (no silent supersession) |

---

## Fail-Closed Rules

The following conditions **must** cause validation to fail:

1. **Missing/unknown vertical datum** — `vertical_datum` absent or empty.
2. **Ambiguous depth convention** — `depth_positive_direction` not `"down"` or `"up"`.
3. **Unversioned processing or inversion** — `processing_software_version` or
   `inversion_software_version` absent or empty.
4. **Missing units** — `resistivity_units` absent or empty.
5. **Product/source identity collapse** — `product_id` equals `source_descriptor_ref`.
6. **Raw/processed lineage break** — `raw_source_ref` absent.
7. **Uncertainty omission** — `uncertainty` block absent.
8. **Silent supersession** — `correction` block present but `supersedes_ref` absent.
9. **Unbound EvidenceRef** — `evidence_refs` empty or absent.
10. **False release/publication state** — proposed/disabled record with `release_state`
    other than `not_released`.

---

## Not Established by This Contract

- No endpoint, connector activation, schedule, credential, or live payload.
- No geology/resource assertion, policy decision, proof, release, deployment, or
  publication state.
- No groundwater-level observation, water-right record, legal finding, or
  recommendation.
- No product existence assertion until official bytes and source metadata are
  formally observed.
