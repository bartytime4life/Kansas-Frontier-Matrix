<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: Data Dictionary — <DATASET_NAME>
type: standard
version: v1
status: draft
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - <relative path: data/registry/<dataset_id>.yaml>
  - <relative path: data/specs/<dataset_id>.md>
  - <relative path: data/catalog/dcat/<dataset_id>.json>
  - <relative path: data/catalog/stac/collections/<collection_id>.json>
  - <relative path: data/catalog/prov/<prov_bundle_id>.json>
tags: [kfm, data, data-dictionary, template]
notes:
  - Copy this template to: docs/data/dictionaries/<dataset_id>.md (recommended) OR co-locate with the dataset spec.
  - This is a human-readable companion to machine-readable schemas/contracts. It must not contradict them.
[/KFM_META_BLOCK_V2] -->

# Data Dictionary — <DATASET_NAME>

**One-line purpose:** <What this dataset is and why it exists.>

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Policy](https://img.shields.io/badge/policy_label-<public|restricted>-blue)
![Dataset](https://img.shields.io/badge/dataset_id-<dataset_id>-informational)
![Version](https://img.shields.io/badge/dataset_version_id-<dataset_version_id>-informational)

---

## Quick nav

- [What this document is](#what-this-document-is)
- [Dataset identity](#dataset-identity)
- [Rights and sensitivity](#rights-and-sensitivity)
- [Spatial reference](#spatial-reference)
- [Temporal reference](#temporal-reference)
- [Schema overview](#schema-overview)
- [Field-level dictionary](#field-level-dictionary)
- [Derived fields and transformations](#derived-fields-and-transformations)
- [Quality checks and thresholds](#quality-checks-and-thresholds)
- [Access patterns and API mapping](#access-patterns-and-api-mapping)
- [Known issues](#known-issues)
- [Change log](#change-log)
- [Definition of done](#definition-of-done)

---

## What this document is

This **Data Dictionary** defines the **meaning, types, and constraints** of fields in **<DATASET_NAME>**.

It is intended to:
- eliminate ambiguity in field semantics (what does each field *mean*?)
- make QA rules explicit (what is *valid*?)
- support governed publication (what needs redaction/generalization?)
- support API/UI usage (how should this be displayed and filtered?)

> NOTE  
> This is **not** a substitute for machine-readable schemas (JSON Schema, STAC, etc.).  
> If this doc conflicts with a schema/contract, the schema/contract wins; fix this doc to match.

---

## Dataset identity

### Canonical IDs

| Item | Value |
|---|---|
| dataset_id | `<dataset_id>` |
| dataset_version_id | `<dataset_version_id>` |
| spec_hash | `<spec_hash>` |
| publication_state | `<RAW|WORK|QUARANTINE|PROCESSED|CATALOG|PUBLISHED>` |
| steward | `<name/team>` |
| maintainer | `<name/team>` |

### Artifact link map

> Fill these in with **relative repo links** when available.

| Artifact | Purpose | Link |
|---|---|---|
| Registry entry | Source metadata, cadence, license snapshot pointer | `<data/registry/<dataset_id>.yaml>` |
| Dataset spec | Contract, QA gates, transforms, acceptance criteria | `<data/specs/<dataset_id>.md>` |
| Run receipt | Reproducibility + audit trail for this version | `<data/receipts/<dataset_version_id>.json>` |
| Processed artifacts | Publishable data (e.g., GeoParquet/COG/PMTiles) | `<data/processed/<dataset_id>/<dataset_version_id>/...>` |
| DCAT record | Dataset-level metadata | `<data/catalog/dcat/<dataset_id>.json>` |
| STAC collection/items | Asset-level metadata | `<data/catalog/stac/...>` |
| PROV bundle | Lineage graph | `<data/catalog/prov/...>` |

---

## Rights and sensitivity

### Rights

| Field | Value |
|---|---|
| license | `<SPDX id or “custom”>` |
| attribution | `<required attribution text>` |
| upstream terms snapshot | `<path or EvidenceRef>` |
| restrictions | `<none OR describe restrictions>` |

### Sensitivity

| Field | Value |
|---|---|
| policy_label | `<public|restricted|...>` |
| sensitivity summary | `<why it is sensitive or why it is not>` |
| redaction obligations | `<e.g., generalize geometry to county; remove exact addresses; bin timestamps>` |
| access pathway | `<public API only / restricted API only / steward-reviewed>` |

> WARNING — sensitive locations / vulnerable entities  
> If this dataset contains **vulnerable sites** (archaeology, endangered species, private addresses, critical infrastructure), do **not** publish precise coordinates or identifying attributes without an explicit policy decision and a tested redaction plan.

---

## Spatial reference

| Item | Value |
|---|---|
| geometry type | `<Point|LineString|Polygon|Multi*>` |
| coordinate reference system (CRS) | `<EPSG:####>` |
| axis order | `<lon,lat OR x,y>` |
| spatial resolution | `<e.g., 10m raster; 1:24k vector; N/A>` |
| spatial extent | `<bbox or description>` |
| topology expectations | `<e.g., polygons non-self-intersecting; lines snapped; N/A>` |
| positional accuracy | `<e.g., ±10m; unknown>` |

---

## Temporal reference

| Item | Value |
|---|---|
| event time meaning | `<what time in the real world this represents>` |
| valid time meaning | `<when the record is considered true>` |
| transaction time meaning | `<when KFM ingested/recorded it>` |
| time zone | `<UTC|America/Chicago|source-defined>` |
| temporal extent | `<start → end>` |
| cadence | `<daily|monthly|annual|irregular>` |

---

## Schema overview

### Granularity and “what a row means”

- **Entity represented:** `<e.g., storm event; parcel; grid cell; sensor reading; county-year aggregate>`
- **One record equals:** `<precise definition>`
- **Primary key(s):** `<field(s)>`
- **Natural key(s):** `<optional>`
- **Expected row count (per version):** `<approx>` (optional)

### Tables / layers / collections

> If this dataset has multiple layers/tables, list each one separately.

| Name | Type | Description | Primary key |
|---|---|---|---|
| `<layer_or_table_name>` | `<vector|raster|table>` | `<what it contains>` | `<pk>` |

<details>
<summary><strong>Raster-specific notes (optional)</strong></summary>

| Item | Value |
|---|---|
| pixel size | `<x by y units>` |
| nodata value | `<value>` |
| band count | `<n>` |
| band definitions | `<list bands + meanings>` |
| scaling/offset | `<if applicable>` |

</details>

<details>
<summary><strong>Point cloud / LiDAR-specific notes (optional)</strong></summary>

| Item | Value |
|---|---|
| coordinate system | `<EPSG:####>` |
| classification codes | `<standard used>` |
| point density | `<pts/m²>` |
| vertical datum | `<datum>` |

</details>

---

## Field-level dictionary

> Conventions:
> - **Type** should be explicit (e.g., `string`, `int32`, `float64`, `bool`, `date`, `datetime`, `geometry`, `json`).
> - **Nullable** must be explicit.
> - **Domain** should be an enum, a range, a vocabulary, or “free text”.
> - **Policy** should state whether the field is sensitive, identifying, or needs transformation/redaction.

### Fields

| Field | Display name | Type | Nullable | Units | Domain / constraints | Description | Example | Source / derivation | QA checks | Policy |
|---|---|---:|:---:|---|---|---|---|---|---|---|
| `<field_name>` | `<label>` | `<type>` | `<Y/N>` | `<units>` | `<enum/range/regex>` | `<meaning>` | `<value>` | `<upstream field OR transform>` | `<checks>` | `<public/restricted/redact>` |
| `<field_name>` |  |  |  |  |  |  |  |  |  |  |
| `<field_name>` |  |  |  |  |  |  |  |  |  |  |

### Geometry field

| Item | Value |
|---|---|
| geometry field name | `<geom>` |
| geometry meaning | `<what the geometry represents>` |
| precision | `<decimal places or tolerance>` |
| validity rules | `<non-empty; no self-intersection; etc.>` |
| generalization rules | `<if required by policy>` |

### Enumerations / domain tables

> If you have enums, codes, or controlled vocabularies, document them here (and link to the canonical vocab file if it exists).

| Field | Code | Label | Definition | Notes |
|---|---|---|---|---|
| `<field_name>` | `<code>` | `<label>` | `<definition>` | `<source>` |

---

## Derived fields and transformations

List any fields not directly present upstream, including normalization steps, joins, and computed metrics.

| Output field | Depends on | Transformation | Rationale | Deterministic? | Notes |
|---|---|---|---|:---:|---|
| `<derived_field>` | `<a,b,c>` | `<formula/algorithm>` | `<why it exists>` | `<Y/N>` | `<edge cases>` |

> TIP  
> If a transformation affects policy (e.g., geometry generalization, suppression, bucketing), it should also appear in the **redaction obligations** section and be covered by tests.

---

## Quality checks and thresholds

Define the dataset-specific QA rules and the **minimum acceptable thresholds** for promotion.

| Check ID | What it checks | Method | Threshold | Severity | Where enforced | Notes |
|---|---|---|---|---|---|---|
| `QA-001` | `<e.g., schema validates>` | `<validator>` | `<pass/fail>` | `<blocker>` | `<CI / pipeline>` |  |
| `QA-002` | `<e.g., geometry validity>` | `<st_isvalid>` | `<>= 0.999 valid>` | `<blocker>` |  |  |
| `QA-003` | `<e.g., missingness>` | `<null rate>` | `<<= 2% for required fields>` | `<warn/block>` |  |  |

### QA report pointers

- Latest QA report: `<path>`
- QA summary: `<brief statement of current known limitations>`

---

## Access patterns and API mapping

> This section is for consumers (UI, analysis, downstream APIs). Keep it stable.

### Primary access surfaces

| Surface | Purpose | Link / endpoint |
|---|---|---|
| Governed datasets endpoint | discover dataset versions | `<GET /api/v1/datasets/...>` |
| STAC | geospatial asset discovery | `<GET /api/v1/stac/...>` |
| Tiles | map rendering | `<GET /api/v1/tiles/...>` |
| Evidence | audit/citations for claims | `<GET /api/v1/evidence/...>` |

### Field mapping notes

- API field name differences (if any): `<notes>`
- Units conversions applied in API/UI (if any): `<notes>`
- Default filters / exclusions applied by policy: `<notes>`

---

## Known issues

| Issue | Impact | Mitigation | Status | Owner |
|---|---|---|---|---|
| `<issue>` | `<impact>` | `<mitigation>` | `<open|closed>` | `<name/team>` |

---

## Change log

> Add an entry for every semantic change. If field meaning changes, create a new dataset version.

| Date | dataset_version_id | Change | Breaking? | PR / link | Notes |
|---|---|---|:---:|---|---|
| YYYY-MM-DD | `<dataset_version_id>` | `<summary>` | `<Y/N>` | `<link>` |  |

---

## Definition of done

Before publishing (or claiming) anything based on this dataset:

- [ ] `dataset_id` and `dataset_version_id` filled in and match registry/spec
- [ ] Rights metadata complete (license, attribution, terms snapshot pointer)
- [ ] `policy_label` assigned and redaction obligations documented
- [ ] Spatial reference (CRS/geometry meaning) documented
- [ ] Temporal reference (event/valid/transaction meanings) documented
- [ ] Field table complete for all user-facing fields
- [ ] Derived fields documented (no silent transforms)
- [ ] QA checks + thresholds listed and linked to a QA report
- [ ] Links to DCAT/STAC/PROV and run receipt provided (or explicitly “not yet available”)
- [ ] Reviewed by a steward/maintainer appropriate to the policy label

---

<p align="right"><a href="#data-dictionary--dataset_name">Back to top ↑</a></p>
