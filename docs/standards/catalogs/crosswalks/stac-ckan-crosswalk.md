---
title: "🔁 KFM v11.2.6 — STAC → CKAN Crosswalk (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Guided crosswalk for deriving CKAN/portal metadata from authoritative STAC (and optionally DCAT) records in the Kansas Frontier Matrix."
path: "docs/standards/catalogs/crosswalks/stac-ckan-crosswalk.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → CKAN 2.x mapping compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-crosswalks-stac-ckan-v11.2.6"
semantic_document_id: "kfm-standards-catalogs-crosswalks-stac-ckan-v11.2.6"
event_source_id: "ledger:kfm:standards:catalogs:crosswalks:stac-ckan:v11.2.6"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/catalog-metadata-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

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

json_schema_ref: "../../../../schemas/json/catalogs-stac-ckan-crosswalk-v1.json"
shape_schema_ref: "../../../../schemas/shacl/catalogs-stac-ckan-crosswalk-v1.shape.ttl"

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

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 standards/
        └── 📁 catalogs/
            └── 📁 crosswalks/                         🔀 Catalog crosswalk standards subtree
                ├── 📄 README.md                       📚 Crosswalks standards index
                ├── 📄 stac-dcat-crosswalk.md          📦 STAC → DCAT field-level mapping (canonical)
                ├── 📄 stac-ckan-crosswalk.md          🔁 This file — STAC → CKAN / portal crosswalk
                └── 📁 profiles/                       🧩 Domain-specific crosswalk profiles
                    ├── 📄 stac-dcat-hydro-profile.md  💧 Hydrology-focused crosswalk profile
                    └── 📄 stac-dcat-archaeo-profile.md 🏺 Archaeology / heritage crosswalk profile
~~~

**Directory contract**

- This spec sits under the **catalog crosswalks subtree** and depends on:
  - `docs/standards/catalogs/README.md` (catalog standards index)  
  - `docs/standards/catalogs/stac-dcat-derivation.md` (STAC → DCAT derivation model)  
  - `docs/standards/catalogs/crosswalks/README.md` (this subtree’s index)  
- Implementations live in code and CI pipelines (e.g., `src/pipelines/catalogs/stac-ckan/`), but **must reference this document by path and version**.

---

## 📘 Scope & KFM Position

This crosswalk describes how to derive **CKAN dataset/resource metadata** from:

- **Authoritative STAC Items & Collections** (primary source), and  
- Optionally, **derived DCAT** artifacts (secondary view) when a portal already consumes DCAT.

It must be read alongside:

- `../README.md` — catalog standards index.  
- `../crosswalks/README.md` — crosswalk standards index.  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived model.  
- `../stac/stac-kfm-profile.md` — KFM STAC profile (authoritative).  
- `../dcat/dcat-kfm-profile.md` — KFM DCAT profile.  
- `./stac-dcat-crosswalk.md` — STAC → DCAT crosswalk (primary).

**KFM position:**

- **STAC is authoritative**, DCAT is derived.  
- CKAN/portal metadata is **also derived** (from STAC directly or via DCAT).  
- CKAN is **never** the authoritative catalog layer in KFM.

---

## 🧱 CKAN Concepts & Targets

This crosswalk covers CKAN core structures:

- **Dataset-level** (`package`) metadata  
- **Resource-level** (`resource`) metadata  

Primary CKAN fields:

- Dataset (`package`):

  - `name` (machine-safe ID)  
  - `title`  
  - `notes`  
  - `tags`  
  - `groups` (optional)  
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

## 📦 STAC / DCAT → CKAN Dataset Mapping

### Identification & Names

**Goal:** produce a stable CKAN `name` and descriptive `title` from STAC/DCAT.

| CKAN Field | Source & Rule                                                                 |
|-----------|-------------------------------------------------------------------------------|
| `name`    | Derived from STAC `id` or DCAT `dct:identifier`, lowercased, hyphenated, ASCII-safe. |
| `title`   | STAC `properties.title` or Collection `title` → DCAT `dct:title` → CKAN `title`.     |

**Best practice:**

- For dataset-level CKAN packages, prefer **Collection-level identifiers** (e.g., `naip_ks_2023`, `hrrr_precip_ks_3km`) rather than individual Item IDs.

### Description (`notes`)

| CKAN Field | Source & Rule                                                  |
|-----------|----------------------------------------------------------------|
| `notes`   | STAC description (Item/Collection) → DCAT `dct:description`.   |

Use a **concise, human-readable** description. For complex datasets, DCAT may embed more detailed prose; CKAN `notes` should be an abridged version.

### Tags (`tags`)

| CKAN Field | Source & Rule                              |
|-----------|--------------------------------------------|
| `tags`    | STAC `keywords` + domain/extension hints → DCAT `dcat:keyword` → CKAN tags. |

**Rules:**

- Normalize to lowercase, hyphenated tags.  
- Use governance-approved vocabularies where they exist (e.g., hydrology, climate).

Example:

- STAC `keywords`: `["precipitation", "HRRR", "Kansas"]` → CKAN tags: `["precipitation", "hrrr", "kansas"]`.

### License (`license_id`)

| CKAN Field   | Source & Rule                             |
|-------------|-------------------------------------------|
| `license_id`| STAC `license` or DCAT `dct:license`, mapped to CKAN license ID. |

**Mapping must be explicit** (e.g., `CC-BY-4.0` → `cc-by`).

If license is not recognized, `license_id` may be left blank but **must not misrepresent** licensing terms.

### Extras (`extras`)

Use `extras` to carry structured KFM metadata, for example:

- `kfm_dataset_id` ← `kfm:dataset_id`  
- `kfm_domain` ← `kfm:domain`  
- `kfm_release_stage` ← `kfm:release_stage`  
- `spatial_bbox` ← bounding box string from STAC/DCAT  
- `temporal_start` / `temporal_end` ← from temporal extents  

Extras enable:

- Filtering and advanced search in CKAN.  
- Downstream inference of STAC/DCAT lineage.

---

## 📡 STAC / DCAT → CKAN Resource Mapping

Each STAC Asset that should be exposed in a portal is mapped to a CKAN `resource`.

### URL & Format

| CKAN Field | Source & Rule                                                        |
|-----------|----------------------------------------------------------------------|
| `url`     | STAC Asset `href` → or DCAT `dcat:downloadURL` / `dcat:accessURL`.   |
| `format`  | STAC Asset `type` (MIME) simplified to CKAN `format` label when needed. |

Rules:

- `format` may be a short label (e.g., `GeoTIFF`, `NetCDF`, `Parquet`) or the MIME type, depending on portal conventions.  
- **Never** map to ambiguous/incorrect formats.

### Name & Description

| CKAN Field    | Source & Rule                                         |
|--------------|-------------------------------------------------------|
| `name`       | Derived from Asset key or Asset `title` (if present). |
| `description`| Asset description when available, else dataset snippet.|

### Hash / Checksums

| CKAN Field | Source & Rule                          |
|-----------|----------------------------------------|
| `hash`    | STAC Asset `checksum:sha256` (preferred). |

If checksums exist, CKAN `hash` should use the raw hex string. Additional checksum details MAY be encoded as resource-level `extras` if the portal supports it.

### Resource Selection

Not all STAC assets are suitable as CKAN resources:

- **Include**:
  - Main data assets (`data`, `timeseries`, major `overview`s).  
- **Exclude or internal-only**:
  - Debug/QA or intermediate assets.  
  - Highly internal or sensitive assets not intended for external consumption.

Selection logic MUST be:

- Encapsulated in crosswalk code.  
- Governed by FAIR+CARE and sovereignty rules (see next section).

---

## 🛡️ FAIR+CARE & Sovereignty Constraints

Federating to CKAN/portals is subject to the **same constraints** as DCAT federation.

### Dataset Eligibility

Only derive CKAN packages for datasets where:

- Sensitivity and care labels allow external viewing (e.g., general environmental datasets).  
- CARE metadata does **not** indicate additional restrictions that are incompatible with the target portal.  
- Any sovereignty or heritage flags are respected per KFM policies and agreements.

Internal-only datasets:

- MUST NOT produce CKAN datasets in public portals.  
- MAY appear in **internal CKAN instances** under stricter access controls.

### Spatial & Attribute Redaction

For sensitive domains (e.g., heritage/archaeology):

- Derived CKAN metadata should reference only **generalized** STAC/DCAT products.  
- No site codes or fine-grained identifying attributes should be added to CKAN `extras` or resource descriptions.  
- Spatial fields should align with **already generalized** geometries and extents.

When in doubt:

- Prefer **higher-level datasets** (e.g., “Cultural Landscape Regions”) rather than granular layers.

---

## 🧬 Provenance & Lineage

The STAC → CKAN mapping must preserve provenance:

- **STAC source** (Item/Collection) →  
- **DCAT (optional)** →  
- **CKAN dataset/resources**.

Recommended patterns:

- Store `kfm_dataset_id` in CKAN `extras`.  
- Optionally store STAC/DCAT source URLs in `extras`, such as:
  - `stac_collection_url`  
  - `stac_item_url_example`  
  - `dcat_dataset_url`  

PROV-O-level documentation (outside CKAN) SHOULD:

- Record when CKAN exports were generated.  
- From which STAC/DCAT versions.  
- For which portal or partner.

This provenance MUST be compatible with `KFM-PROV v11` and referenced in release telemetry where appropriate.

---

## 🧪 CI & Validation

Before CKAN exports are accepted:

1. **STAC validation**  
   - All source STAC records MUST validate against:
     - STAC 1.0.x schemas.  
     - KFM-STAC v11 profile and mission-tag / event-tag rules.

2. **Crosswalk tests**  
   - Use fixtures with known STAC → CKAN expectations.  
   - Generate CKAN payloads and assert:
     - `name`, `title`, `notes`, `tags`, `extras` are correctly populated.  
     - Required fields for the target CKAN instance are present.  
     - Forbidden fields (sensitive attributes) are absent.

3. **Governance checks**  
   - Confirm restricted datasets are not exported to public CKAN.  
   - Confirm no internal-only IDs, raw coordinates, or sensitive notes are included.

4. **Telemetry logging**  
   - Record counts of exported packages/resources and validation failures in:
     - `catalog-metadata-telemetry.json` (per-version) using `catalog-metadata-v1.json` schema.

CI jobs (indicative) MAY include:

- `catalog-crosswalk-stac-ckan-validate.yml`  
- integrated into `.github/workflows/kfm-ci.yml` for the `dev → staging → production` promotion pipeline.

---

## ✅ Implementation Checklist

When implementing or updating STAC → CKAN exports:

1. **Clarify scope**  
   - Which datasets and which CKAN instance(s)?  
   - Public vs internal portal?

2. **Implement crosswalk logic**  
   - Map STAC/DCAT fields to CKAN dataset/resource fields per this spec.  
   - Handle FAIR+CARE & sovereignty-based filtering of datasets and fields.

3. **Wire CI & tests**  
   - Add regression tests for representative datasets (imagery, climate, hydrology, heritage).  
   - Ensure CI fails on crosswalk regressions or governance violations.

4. **Monitor & refine**  
   - Monitor portal usage and feedback.  
   - Refine tags, descriptions, and extras for findability and clarity (without breaking STAC/DCAT consistency).

5. **Governance review**  
   - Review exports periodically with FAIR+CARE, sovereignty, and domain working groups.  
   - Treat changes to crosswalk semantics as governed events (version bump + audit entry).

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Metadata & Catalogs WG · FAIR+CARE Council | Aligned STAC → CKAN crosswalk with KFM‑MDP v11.2.6; updated paths, profiles, and governance/CI expectations for v11.2.6 catalog stack. |
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial STAC → CKAN crosswalk spec; defined mapping for CKAN datasets/resources, FAIR+CARE constraints, provenance, and CI validation patterns under the STAC-first → DCAT-derived model. |

---

<sub>© 2025 Kansas Frontier Matrix · MIT / CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

🔁 **KFM v11.2.6 — STAC → CKAN Crosswalk**  
STAC‑First Catalogs · DCAT‑Derived Discovery · Portal‑Safe Crosswalks  

[📚 Catalog Crosswalks Index](README.md) · [📚 Catalog Standards Index](../README.md) · [📦 STAC → DCAT Derivation](../stac-dcat-derivation.md) · [⚖ Governance Charter](../../governance/ROOT-GOVERNANCE.md)

</div>