---
title: "🛰️ KFM v11.2.3 — STAC Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index for STAC-based geospatial metadata standards in the Kansas Frontier Matrix, including KFM STAC profiles, best practices, and validation rules."
path: "docs/standards/catalogs/stac/README.md"
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

doc_uuid: "urn:kfm:doc:standards-catalogs-stac-index-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-stac-index-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:index:v11.2.3"

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

doc_kind: "Standards Index"
intent: "catalogs-stac-standards-index"
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

json_schema_ref: "../../../schemas/json/catalogs-stac-index-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-stac-index-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC standards overhaul"
---

<div align="center">

# 🛰️ Kansas Frontier Matrix — STAC Standards Index  
`docs/standards/catalogs/stac/README.md`

**Purpose:**  
Serve as the **governed index** for all **STAC (SpatioTemporal Asset Catalog)** standards in KFM — including the KFM STAC profile, best-practice guidance, validation rules, and their role as the **authoritative geospatial metadata layer** for STAC → DCAT derivation.

</div>

---

## 📘 1. Scope

This index covers all **STAC-focused** standards that KFM uses for:

- Dataset **Items**, **Collections**, and **Catalogs**.  
- KFM-specific **STAC profiles** and required fields.  
- Best-practice patterns for geometry, time, assets, and naming.  
- Validation and governance expectations for STAC metadata.  

It sits under the broader catalog standard index:

- `docs/standards/catalogs/README.md` — catalog standards root  
- `docs/standards/catalogs/stac-dcat-derivation.md` — STAC-first → DCAT-derived model  

**KFM position:**  
> STAC is the authoritative geospatial metadata layer.  
> DCAT and other catalog formats are derived artifacts.

---

## 🗂️ 2. Directory Layout (v11.2.3)

~~~text
docs/standards/catalogs/stac/
├── 📄 README.md                         # This file — STAC standards index
│
├── 🧩 stac-kfm-profile.md               # KFM STAC profile (fields, extensions, constraints)
├── 🧩 stac-best-practices.md            # Naming, tiling, temporal, asset, and link best practices
│
└── 🧩 extensions/                       # (Optional) KFM-specific STAC extension docs
    ├── 📄 stac-ext-kfm-core.md          # Core KFM metadata extension (if applicable)
    └── 📄 stac-ext-domain-*.md          # Domain-specific extensions (climate, archaeology, etc.)
~~~

**Directory contract:**

- All STAC standards documents here must:
  - Follow **KFM-MDP v11.2.3** metadata.  
  - Be **machine-extractable** (clear headings, tables, and crosswalks).  
  - Align with KFM’s **STAC-first** catalog model.  

Implementation code (crosswalks, validators, generators) lives outside this tree (e.g., `pipelines/catalogs/stac-*`).

---

## 📦 3. KFM STAC Profile (Authoritative Layer)

The KFM STAC profile document:

- `docs/standards/catalogs/stac/stac-kfm-profile.md`

is expected to define:

### 3.1 Required STAC Fields

For **Items** and **Collections**, including at minimum:

- Core STAC fields:
  - `id`, `type`, `stac_version`  
  - `geometry`, `bbox`  
  - `properties.datetime` or `properties.start_datetime` / `properties.end_datetime`  
  - `links`, `assets`  

- KFM-specific requirements:
  - Mandatory checksum fields (e.g., `checksum:sha256`) on relevant assets.  
  - KFM domain properties (e.g., `kfm:domain`, `kfm:subdomain`, `kfm:region_slug`).  
  - FAIR+CARE-related properties (e.g., sensitivity tags, sovereignty notes).

### 3.2 Collections & Catalogs

Profile rules for:

- Collection metadata (title, description, spatial/temporal extents).  
- When to use multiple Collections vs one Collection with many Items.  
- Catalogs as navigational structures vs domain groupings.

### 3.3 Alignment with STAC 1.0.x

- KFM must explicitly track STAC version compatibility (e.g., `1.0.0` profile).  
- Deprecation behavior for older STAC versions, if present, should be documented.

---

## 🧠 4. STAC Best Practices (Geometry, Time, Assets, Naming)

The best-practices document:

- `docs/standards/catalogs/stac/stac-best-practices.md`

is expected to encode:

### 4.1 Geometry & Spatial Extents

- Use of `geometry` vs `bbox`:
  - `geometry` as the authoritative footprint.  
  - `bbox` as a derived envelope, used for DCAT and quick search.

- Simplification and generalization:
  - When to generalize geometries for public use.  
  - How to represent sensitive regions while preserving essential spatial meaning.

### 4.2 Temporal Fields

- Required use of `properties.datetime` vs `start_datetime` / `end_datetime`.  
- Handling episodic / multi-temporal datasets:
  - Time series vs snapshots.  
  - Collections spanning broad ranges vs Items for individual periods.

### 4.3 Assets

- Asset naming and roles:
  - `data`, `thumbnail`, `overview`, `metadata`, `index`, etc.  
- Media types and formats:
  - Standardized MIME types for common formats (GeoTIFF, Cloud-Optimized formats, NetCDF, etc.).  
- Checksums & sizes:
  - Recommended inclusion of `checksum:*` and optional size fields for reliability and observability.

### 4.4 Naming & IDs

- Conventions for `id` fields:
  - Stable, versioned identifiers.  
  - Avoiding spaces and locale-specific characters.  

- Helpful patterns:
  - `domain_year_type_suffix` (e.g., `naip_2023_tile_001`).  
  - Align with dataset registry IDs and DCAT `dct:identifier`.

---

## 🔁 5. Relationship to DCAT & Crosswalks

The STAC standards here must be read in conjunction with:

- `docs/standards/catalogs/stac-dcat-derivation.md` — the **STAC-first → DCAT-derived model**.  
- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md` — field-level mapping.

**Key KFM position:**

- STAC is the **only authoritative source** of geospatial catalog metadata.  
- DCAT, CKAN, and other catalog forms are derived artifacts.  
- Changes to STAC profiles or best-practices have direct implications for:
  - Crosswalk code  
  - DCAT shapes  
  - External federation behavior

Any STAC profile changes must trigger:

- Crosswalk review & update.  
- DCAT profile and shape review, if impacted.  
- CI & validation workflow updates.

---

## 🧪 6. Validation & CI Expectations

STAC standards are enforced via CI:

- **STAC Validation**:
  - `stac-validator` for schema conformance.  
  - `stac-check` or equivalent for best-practices and semantic checks.

- **Internal CI Jobs** (names illustrative):
  - `catalog-stac-validate.yml` — run validation on all STAC artifacts.  
  - `catalog-stac-lint.yml` — enforce naming, temporal, and geometry conventions.  

CI MUST:

- Fail if any STAC Item/Collection:
  - Violates the KFM STAC profile.  
  - Uses deprecated fields or wrong STAC version.  
  - Contains inconsistent geometry, bbox, or temporal fields.

- Warn/fail on:
  - Missing checksums and critical metadata.  
  - Missing FAIR+CARE-relevant properties where required.

---

## ⚖️ 7. FAIR+CARE & Sovereignty Considerations in STAC

STAC metadata participates fully in KFM’s FAIR+CARE and sovereignty framework:

- STAC properties should carry:
  - Sensitivity tags (e.g., `kfm:sensitivity`).  
  - Sovereignty flags and notes (e.g., references to Indigenous data protection rules).  

- Geographic generalization & masking:
  - Where precise geometry is not appropriate for public distribution, STAC Items used for public-derived catalogs should:
    - Use generalized geometries.  
    - Or be accompanied by separate “public” Collections/Items derived from precise originals.

Provenance must:

- Link STAC edits and generalizations back to:
  - Source datasets.  
  - Governance decisions.  
  - FAIR+CARE reasoning.

---

## ✅ 8. Implementation Checklist (STAC-Centric)

For any new KFM dataset:

1. **Create STAC Item(s) / Collection(s)** that satisfy `stac-kfm-profile.md`.  
2. **Apply best practices** from `stac-best-practices.md`:
   - Geometry, temporal, asset, naming rules.  
3. **Validate STAC** via `stac-validator` and CI.  
4. **Derive DCAT** via governed crosswalks as defined in:
   - `stac-dcat-derivation.md`  
   - `crosswalks/stac-dcat-crosswalk.md`  
5. **Wire into catalogs** and portals using derived DCAT.  
6. **Monitor telemetry** for validation errors and crosswalk failures.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Created STAC standards index; defined directory structure for KFM STAC profile, best practices, and extensions; aligned with STAC-first → DCAT-derived model and KFM-MDP v11.2.3. |


