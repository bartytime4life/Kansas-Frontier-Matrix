---
title: "🛰️ KFM v11.2.3 — STAC KFM Profile (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Normative STAC profile for the Kansas Frontier Matrix, defining required fields, extensions, and validation rules for STAC Items, Collections, and Catalogs."
path: "docs/standards/catalogs/stac/stac-kfm-profile.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x profile-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-stac-kfm-profile-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-stac-kfm-profile-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:kfm-profile:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Standard"
intent: "catalogs-stac-kfm-profile"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/catalogs-stac-kfm-profile-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-stac-kfm-profile-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major KFM STAC profile revision"
---

<div align="center">

# 🛰️ Kansas Frontier Matrix — STAC KFM Profile  
`docs/standards/catalogs/stac/stac-kfm-profile.md`

**Purpose:**  
Define the **normative STAC profile** for the Kansas Frontier Matrix (KFM):  
which STAC fields are **required**, which KFM extensions must be used, and how Items, Collections, and Catalogs must be structured to support the **STAC-first → DCAT-derived** model and FAIR+CARE + sovereignty governance.

</div>

---

## 📘 1. Scope & Compatibility

This profile applies to:

- **STAC Items** (individual observations/slices).  
- **STAC Collections** (dataset families).  
- **STAC Catalogs** (navigational groupings).

It is:

- Compatible with **STAC 1.0.x** (target STAC ≥ 1.0.0).  
- Designed to work with:
  - KFM STAC extensions (core, FAIR+CARE, climate, hydrology, archaeology, etc.).  
  - KFM STAC best-practices (`stac-best-practices.md`).  
  - STAC-first → DCAT-derived model (`../stac-dcat-derivation.md`).

**KFM position:**

- STAC is the **authoritative geospatial metadata layer**.  
- This profile is **normative**: STAC that fails this profile is **not production-grade** in KFM.

---

## 🧱 2. STAC Versions & Core Requirements

### 2.1 STAC Version

- All KFM STAC records MUST declare:

  - `stac_version = "1.0.0"` or compatible `1.0.x`.  

- KFM tooling and CI must:
  - Fail STAC using pre-1.0 versions.  
  - Emit warnings for unknown post-1.0 versions until the profile is updated.

### 2.2 Core STAC Fields (Items)

KFM Items MUST include:

| Field                   | Requirement    |
|-------------------------|----------------|
| `type`                  | MUST be `"Feature"`. |
| `id`                    | REQUIRED; stable, unique within dataset. |
| `stac_version`          | REQUIRED; `1.0.x`. |
| `geometry`              | REQUIRED; valid GeoJSON geometry (EPSG:4326). |
| `bbox`                  | REQUIRED; derived from geometry. |
| `properties`            | REQUIRED; JSON object. |
| `properties.datetime` OR (`start_datetime` & `end_datetime`) | REQUIRED per time semantics (see §4). |
| `assets`                | REQUIRED; at least one asset. |
| `links`                 | REQUIRED; MUST include `self` & `collection` where applicable. |

### 2.3 Core STAC Fields (Collections)

Collections MUST include:

| Field                     | Requirement |
|---------------------------|------------|
| `type`                    | MUST be `"Collection"`. |
| `id`                      | REQUIRED; stable collection ID. |
| `stac_version`            | REQUIRED; `1.0.x`. |
| `description`             | REQUIRED. |
| `extent.spatial`          | REQUIRED; includes `bbox` arrays. |
| `extent.temporal`         | REQUIRED; includes temporal intervals. |
| `license`                 | REQUIRED; SPDX-compatible. |
| `links`                   | REQUIRED; `self`, `root`, etc. |

Catalogs MUST follow standard STAC Catalog requirements and provide navigational structure only.

---

## 🧩 3. Required KFM Extensions

KFM STAC records MUST use the following extensions where applicable:

1. **KFM Core extension** (`stac-ext-kfm-core.md`) — `kfm` prefix  
2. **FAIR+CARE & sovereignty extension** (`stac-ext-faircare.md`) — `kfmfc` prefix  
3. **Domain extensions** as appropriate:
   - `stac-ext-climate.md` — `kfmclim`  
   - `stac-ext-hydrology.md` — `kfmhydro`  
   - `stac-ext-archaeology.md` — `kfmarch`  
   - Future domain extensions (e.g., landcover, geology)  

### 3.1 KFM Core Fields (Required)

All production KFM Items and Collections MUST include:

| Field               | Applies To   | Requirement                                    |
|---------------------|-------------|-----------------------------------------------|
| `kfm:dataset_id`    | Item, Coll. | REQUIRED; stable dataset identifier (URI/CURIE). |
| `kfm:domain`        | Item, Coll. | REQUIRED; domain classification.              |
| `kfm:release_stage` | Item, Coll. | REQUIRED; `experimental`, `beta`, `stable`, `retired`. |

Optional but strongly recommended:

- `kfm:subdomain`  
- `kfm:region_slug`  
- `kfm:lifecycle`  
- `kfm:review_cycle`

### 3.2 FAIR+CARE Fields (Required when extension present)

Whenever `kfm-faircare` is applied (which is strongly encouraged for all but the most trivial datasets):

| Field                     | Requirement                        |
|---------------------------|-------------------------------------|
| `kfmfc:sensitivity`       | REQUIRED.                          |
| `kfmfc:care_label`        | REQUIRED.                          |
| `kfmfc:sovereignty_flag`  | REQUIRED (true/false).             |
| `kfmfc:visibility_rules`  | RECOMMENDED, especially for spatial data. |

---

## 🗺️ 4. Temporal Semantics (Profile Rules)

**Instantaneous Items:**

- Use `properties.datetime` (ISO 8601).  
- DO NOT set `start_datetime`/`end_datetime` unless required by a domain extension.

**Interval Items (aggregations):**

- Use `properties.start_datetime` and `properties.end_datetime`.  
- May omit `datetime` OR set it to a convention (e.g., midpoint), documented in domain profile.

**Forecast vs Analysis:**

- Forecast-specific times MUST use domain fields:
  - `kfmclim:run_datetime`  
  - `kfmclim:lead_time_hours`  

These rules ensure that:

- Temporal extents in STAC are **unambiguous**.  
- STAC → DCAT derivation can accurately populate `dct:temporal`.

---

## 🌍 5. Geometry & Spatial Profile Rules

- `geometry` MUST be valid GeoJSON (EPSG:4326).  
- `bbox` MUST be derivable from `geometry`; automated derivation is recommended.

### 5.1 Sensitive Datasets

For datasets governed by FAIR+CARE with spatial sensitivity:

- Geometry may be:
  - **Generalized** (simplified polygons).  
  - **Aggregate** (H3 or grid cells).  
- Public STAC MUST NOT expose:
  - Exact site coordinates (e.g., archaeological sites).  
  - Non-generalized sensitive boundaries.

Extension fields that enforce this (e.g., `kfmfc:visibility_rules`, `kfmarch:sensitivity_class`) MUST be set appropriately.

---

## 📦 6. Asset Profile & Roles

### 6.1 Asset Requirements

Every Item MUST have at least one `assets` entry with:

- `href` — REQUIRED.  
- `type` — REQUIRED; valid MIME type.  
- `roles` — REQUIRED; at least one role (e.g., `data`, `thumbnail`, `overview`).  

For critical data assets, KFM strongly RECOMMENDS:

- `checksum:sha256`  
- Well-defined `roles` consistent with domain guidance.

### 6.2 Accepted Roles

KFM standard roles include:

- `["data"]` — primary analysis-ready or raw data.  
- `["thumbnail"]` — preview image.  
- `["overview"]` — lower-resolution or pyramid layer.  
- `["metadata"]` — additional docs or sidecar metadata.  
- Domain-specific roles documented in extensions (e.g., `["timeseries"]`, `["index"]`).

Roles used MUST be documented in:

- `stac-best-practices.md`  
- Domain-specific extension docs

---

## 🧬 7. Providers, Licensing & Lineage

### 7.1 Providers

KFM STAC Collections MUST include a `providers` array:

Each provider entry SHOULD include:

- `name` — REQUIRED.  
- `roles` — REQUIRED; from STAC provider roles (producer, licensor, processor, host).  
- `url` — RECOMMENDED.

Items MAY override or add `providers` when they differ from the Collection.

### 7.2 License

- Collections MUST have a `license` field (SPDX-compatible or `proprietary`).  
- Items MAY override the Collection license, but this should be rare and clearly justified.

### 7.3 Lineage & PROV-O

- Where possible, STAC `links` SHOULD include:
  - `via` — upstream source datasets.  
  - `derived_from` — transformation inputs.  

- PROV-O lineage is maintained outside STAC:
  - STAC Items/Collections link to PROV-O logs via `links` or extension fields.  
  - These logs are required for full provenance but not encoded directly in core STAC.

---

## 🧪 8. Validation & CI: Normative Requirements

To conform to the KFM STAC profile:

1. **Schema validation:**
   - `stac-validator` MUST be run with:
     - Core STAC schemas.  
     - KFM extension schemas (`kfm-core`, `kfm-faircare`, domain extensions).

2. **Profile enforcement:**
   - KFM CI MUST run:
     - `catalog-stac-validate.yml` — structural validation.  
     - `catalog-stac-lint.yml` — profile & best-practice checks.  
     - `catalog-stac-extensions-validate.yml` — extension-specific rules.

3. **Failure handling:**
   - Any failure in these CI steps MUST block:
     - Catalog publication.  
     - Downstream DCAT derivation.  
     - Public portal updates, unless explicitly overriden via documented governance decisions.

Telemetry from these workflows MUST be recorded in:

- `catalog-metadata-telemetry.json` with:
  - Validation failures.  
  - Extension use and error frequencies.

---

## ✅ 9. Authoring Checklist (Profile Compliance)

Before merging or publishing STAC:

1. **Core STAC:**
   - Version is 1.0.x.  
   - Items & Collections meet core field requirements.

2. **KFM extensions:**
   - `kfm-core` fields present (`dataset_id`, `domain`, `release_stage`).  
   - FAIR+CARE fields present if applicable (`kfmfc:*`).  
   - Domain-specific fields (climate, hydrology, archaeology, etc.) present and valid.

3. **Geometry & temporality:**
   - Geometry is valid, bbox derived, CRS is EPSG:4326.  
   - Temporal fields represent instants or intervals correctly.

4. **Assets & providers:**
   - Assets have `href`, `type`, `roles`.  
   - Checksums present for key assets.  
   - Providers defined at Collection level.

5. **Governance & sensitivity:**
   - Sensitive datasets use generalized geometries, H3 grids, or derivatives as appropriate.  
   - FAIR+CARE & sovereignty flags are correctly set.  
   - No internal-only fields leak into public STAC.

6. **Validation:**
   - `stac-validator` passes with KFM schemas.  
   - All STAC CI workflows succeed.

---

## 🕰️ 10. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial KFM STAC profile; defined core requirements, extension usage, temporal/geometry rules, and CI validation expectations aligned with STAC-first catalog model and KFM-MDP v11.2.3. |

