---
title: "🔁 KFM v11.2.3 — STAC → CKAN Crosswalk (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Guided crosswalk for deriving CKAN/portal metadata from authoritative STAC (and optionally DCAT) records in the Kansas Frontier Matrix."
path: "docs/standards/catalogs/crosswalks/stac-ckan-crosswalk.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → CKAN 2.x mapping compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-crosswalks-stac-ckan-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-crosswalks-stac-ckan-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:crosswalks:stac-ckan:v11.2.3"

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

doc_kind: "Crosswalk Spec"
intent: "catalogs-stac-to-ckan-crosswalk"
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

json_schema_ref: "../../../schemas/json/catalogs-stac-ckan-crosswalk-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-stac-ckan-crosswalk-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC → CKAN crosswalk revision"
---

<div align="center">

# 🔁 Kansas Frontier Matrix — STAC → CKAN Crosswalk  
`docs/standards/catalogs/crosswalks/stac-ckan-crosswalk.md`

**Purpose:**  
Define a **governed, STAC-first mapping** from KFM STAC (and optionally DCAT) into **CKAN/portal metadata** (datasets + resources), ensuring that external portals remain **derivative**, **FAIR+CARE-compliant**, and **sovereignty-respecting**.

</div>

---

## 📘 1. Scope & KFM Position

This crosswalk describes how to derive **CKAN dataset/resource metadata** from:

- **Authoritative STAC Items & Collections** (primary source), and  
- Optionally, **derived DCAT** artifacts (secondary view), when a portal already consumes DCAT.

It must be read alongside:

- `../README.md` — crosswalk standards index.  
- `../stac/README.md` & `../stac/stac-kfm-profile.md` — STAC profile (authoritative).  
- `../dcat/README.md` & `../dcat/dcat-kfm-profile.md` — DCAT profile.  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived model.  
- `./stac-dcat-crosswalk.md` — STAC → DCAT crosswalk (primary).

**KFM position:**

- **STAC is authoritative**, DCAT is derived.  
- CKAN/portal metadata is **also derived** (from STAC directly or via DCAT).  
- CKAN is **never** the authoritative catalog layer in KFM.

---

## 🧱 2. CKAN Concepts & Targets

This crosswalk covers CKAN core structures:

- **Dataset-level** (`package`) metadata  
- **Resource-level** (`resource`) metadata  

Primary CKAN fields:

- Dataset (`package`):

  - `name` (machine-safe ID)  
  - `title`  
  - `notes`  
  - `tags`  
  - `groups` (optionally)  
  - `extras` (key-value metadata)  
  - `license_id`  

- Resource (`resource`):

  - `url`  
  - `format`  
  - `name`  
  - `description`  
  - `hash` (optional)  
  - `mimetype` / `mimetype_inner` (optional)  

This crosswalk aims to map STAC/DCAT into these fields while:

- Preserving **lineage** and **identifiers**.  
- Avoiding any **governance breaches**.  
- Maintaining reproducibility and consistency.

---

## 📦 3. STAC / DCAT → CKAN Dataset Mapping

### 3.1 Identification & Names

**Goal:** produce a stable CKAN `name` and descriptive `title` from STAC/DCAT.

| CKAN Field | Source & Rule                                                                 |
|-----------|-------------------------------------------------------------------------------|
| `name`    | Derived from STAC `id` or DCAT `dct:identifier`, lowercased, hyphenated, ASCII-safe. |
| `title`   | STAC `properties.title` or Collection `title` → DCAT `dct:title` → CKAN `title`. |

**Best practice:**

- For dataset-level CKAN packages, prefer **Collection-level identifiers** (e.g. `naip_ks_2023`, `hrrr_precip_ks_3km`) rather than individual Item IDs.

### 3.2 Description (`notes`)

| CKAN Field | Source & Rule                                                  |
|-----------|----------------------------------------------------------------|
| `notes`   | STAC description (Item/Collection) → DCAT `dct:description`.   |

Use a **concise, human-readable** description. For complex datasets, DCAT may embed more detailed prose; CKAN `notes` should be an abridged version.

### 3.3 Tags (`tags`)

| CKAN Field | Source & Rule                              |
|-----------|--------------------------------------------|
| `tags`    | STAC `keywords` + domain/extension hints → DCAT `dcat:keyword` → CKAN tags. |

**Rules:**

- Normalize to lowercase, hyphenated tags.  
- Limit to governance-approved vocabularies for certain domains when required.

Example:

- STAC `keywords`: `["precipitation", "HRRR", "Kansas"]` → CKAN tags: `["precipitation", "hrrr", "kansas"]`.

### 3.4 License (`license_id`)

| CKAN Field   | Source & Rule                  |
|-------------|--------------------------------|
| `license_id`| STAC `license` or DCAT `dct:license`, mapped to CKAN license ID. |

**Mapping must be explicit** (e.g., `CC-BY-4.0` → `cc-by`).

If license is not recognized, `license_id` may be left blank but **must not misrepresent** licensing terms.

### 3.5 Extras (`extras`)

Use `extras` to carry structured KFM metadata:

Examples:

- `kfm_dataset_id` ← `kfm:dataset_id`  
- `kfm_domain` ← `kfm:domain`  
- `kfm_release_stage` ← `kfm:release_stage`  
- `spatial_bbox` ← bounding box string from STAC/DCAT  
- `temporal_start` / `temporal_end` ← from temporal extents  

Extras enable:

- Filtering and advanced search in CKAN.  
- Downstream inference of STAC/DCAT lineage.

---

## 📡 4. STAC / DCAT → CKAN Resource Mapping

Each STAC Asset that should be exposed in a portal is mapped to a CKAN `resource`.

### 4.1 URL & Format

| CKAN Field | Source & Rule                       |
|-----------|-------------------------------------|
| `url`     | STAC Asset `href` → or DCAT `dcat:downloadURL` / `dcat:accessURL`. |
| `format`  | STAC Asset `type` (MIME) simplified to CKAN `format` label when needed. |

Rules:

- `format` may be a short label (e.g., `GeoTIFF`, `NetCDF`, `Parquet`) or the MIME type, depending on partner portal conventions.  
- **Never** map to ambiguous/incorrect formats.

### 4.2 Name & Description

| CKAN Field    | Source & Rule                                |
|--------------|----------------------------------------------|
| `name`       | Derived from Asset key or `title` (if present). |
| `description`| Asset description when available, else fallback to dataset description snippet. |

### 4.3 Hash / Checksums

| CKAN Field | Source & Rule                          |
|-----------|----------------------------------------|
| `hash`    | STAC Asset `checksum:sha256` (preferred). |

If checksums exist, CKAN `hash` should use the raw hex string. Optionally, additional checksum metadata can be stored in `extras` at resource-level if the portal supports it.

### 4.4 Resource Selection

Not all STAC assets are suitable as CKAN resources:

- **Include**:
  - Main data assets (`data`, `timeseries`, important `overview`s).  
- **Exclude or consider internal-only**:
  - Debug, QA, or internal intermediate assets.  
  - Highly internal or sensitive assets that are not intended for external consumption.

The selection logic should be:

- Encapsulated in crosswalk code.  
- Governed by FAIR+CARE and sovereignty rules (see §6).

---

## 🛡️ 5. FAIR+CARE & Sovereignty Constraints

Federating to CKAN/portals is subject to the **same constraints** as DCAT federation.

### 5.1 Dataset Eligibility

Only derive CKAN packages for datasets where:

- `kfmfc:sensitivity` allows external viewing (e.g., `general`, some cases of `restricted-generalized`).  
- `kfmfc:care_label` is compatible with the **intended audience** (public, community-specific, internal).  
- `kfmfc:sovereignty_flag` is handled according to agreements and KFM policy.

Internal-only datasets (`restricted-internal`):

- Must **not** produce CKAN datasets in public portals.  
- May appear in a **separate internal CKAN instance** under stricter access controls.

### 5.2 Spatial & Attribute Redaction

For sensitive domains (e.g., archaeology):

- Derived CKAN metadata should only reference **generalized** STAC/DCAT.  
- No site codes or fine-grained identifying attributes should be added to CKAN `extras` or resource descriptions.

If in doubt:

- Prefer a **higher-level dataset** (e.g., “Cultural Landscape Regions”) rather than granular layers.

---

## 🧬 6. Provenance & Lineage

The STAC → CKAN mapping must preserve provenance:

- **STAC source** (Item/Collection) →  
- **DCAT (optional)** →  
- **CKAN dataset/resources**.

Recommended patterns:

- Store `kfm_dataset_id` in CKAN `extras`.  
- Optionally store STAC/ DCAT source URLs in `extras` such as:

  - `stac_collection_url`  
  - `stac_item_url_example`  
  - `dcat_dataset_url`

PROV-O-level documentation (outside CKAN) should:

- Record when CKAN exports were generated.  
- From which STAC/DCAT versions.  
- For which portal or partner.

---

## 🧪 7. CI & Validation

Before CKAN exports are accepted:

1. **STAC validation**  
   - Ensure all source STAC records are valid per KFM STAC profile and extensions.

2. **Crosswalk tests**  
   - Use fixtures with known STAC → CKAN expectations.  
   - Generate CKAN payloads and assert:

     - `name`, `title`, `notes`, `tags`, `extras` are correctly populated.  
     - All required fields for target CKAN instance are present.

3. **Governance checks**  
   - Confirm restricted datasets are not exported to public CKAN.  
   - Confirm no internal-only IDs or sensitive attributes are included.

4. **Telemetry logging**  
   - Record counts of exported packages/resources and validation failures in `catalog-metadata-telemetry.json`.

CI job (indicative):

- `catalog-crosswalk-stac-ckan-validate.yml`.

---

## ✅ 8. Implementation Checklist

When implementing or updating STAC → CKAN exports:

1. **Clarify scope**  
   - Which datasets and which CKAN instance(s)?  
   - Public vs internal portal?

2. **Implement crosswalk logic**  
   - Map STAC/DCAT fields to CKAN dataset/resource fields per this spec.  
   - Handle FAIR+CARE & sovereignty-based filtering.

3. **Wire CI & tests**  
   - Add regression tests for representative datasets (imagery, climate, hydrology, archaeology).  
   - Ensure CI fails on crosswalk regressions.

4. **Monitor & refine**  
   - Monitor portal usage and feedback.  
   - Refine tags, descriptions, and extras for findability and clarity (without breaking STAC/DCAT consistency).

5. **Governance review**  
   - Review exports periodically with FAIR+CARE, sovereignty, and domain working groups.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial STAC → CKAN crosswalk spec; defined mapping for CKAN datasets/resources, FAIR+CARE constraints, provenance, and CI validation patterns under the STAC-first → DCAT-derived model. |

