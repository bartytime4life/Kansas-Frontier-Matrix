---
title: "🛰️ KFM v11.2.3 — STAC Best Practices (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Best-practice guidance for authoring STAC Items, Collections, and Catalogs in the Kansas Frontier Matrix, including geometry, temporal, asset, naming, and governance patterns."
path: "docs/standards/catalogs/stac/stac-best-practices.md"
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

doc_uuid: "urn:kfm:doc:standards-catalogs-stac-best-practices-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-stac-best-practices-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:best-practices:v11.2.3"

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

doc_kind: "Standards Guidance"
intent: "catalogs-stac-best-practices"
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

json_schema_ref: "../../../schemas/json/catalogs-stac-best-practices-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-stac-best-practices-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC best-practices revision"
---

<div align="center">

# 🛰️ Kansas Frontier Matrix — STAC Best Practices  
`docs/standards/catalogs/stac/stac-best-practices.md`

**Purpose:**  
Provide **concrete, enforceable best practices** for authoring STAC Items, Collections, and Catalogs in KFM — covering geometry, temporal fields, assets, naming, links, and governance semantics — consistent with the **KFM STAC profile** and the **STAC-first → DCAT-derived** model.

</div>

---

## 📘 1. Scope & Relationship to Other Docs

This document is **guidance + patterns** and must be read alongside:

- `stac-kfm-profile.md` — normative KFM STAC profile (required fields, constraints).  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived standard.  
- `../stac/README.md` — STAC standards index.  
- `../stac/extensions/README.md` — KFM STAC extensions.

**Key KFM stance:**

- STAC is the **authoritative geospatial metadata layer**.  
- These best practices ensure STAC records are not only valid, but **usable, performant, and governed**.

---

## 🗺️ 2. Geometry & Spatial Extents

### 2.1 Geometry vs BBox

**Rule:**

- `geometry` is the **authoritative footprint**.  
- `bbox` is a **derived envelope** for search, map overviews, and DCAT.

**Best practices:**

- Always provide:
  - `geometry` for Items.  
  - `extent.spatial` for Collections (per STAC spec).  

- Keep `bbox`:
  - As a **tight, minimal bounding box** around `geometry`.  
  - Derived by tooling, not hand-maintained whenever possible.

### 2.2 Precision & Generalization

**For general/public datasets:**

- Use full-resolution geometry where FAIR+CARE and sovereignty rules permit.  

**For sensitive datasets (e.g., archaeology, protected habitats):**

- Use **generalized geometries**:
  - Coarser polygons.  
  - `h3-only` or grid-based representations for public STAC.  
- Keep precise geometries in:
  - Internal-only STAC Items, OR  
  - Separate Assets (e.g., internal vector files) referenced only from non-public environments.

**Governance consistency:**

- Geometry generalization must match:
  - `kfmfc:visibility_rules` (FAIR+CARE extension).  
  - Domain-specific sensitivity (e.g., `kfmarch:sensitivity_class`).

### 2.3 CRS & Coordinates

- STAC geometry/bboxes **must be WGS84 lon/lat** (EPSG:4326).  
- Any other CRS should be documented in:
  - Asset metadata (e.g., GeoTIFF CRS).  
  - Domain extensions (e.g., hydrology vertical datums).

---

## ⏱️ 3. Temporal Fields & Time Semantics

### 3.1 Use of `datetime` vs `start_datetime` / `end_datetime`

**Instantaneous data (e.g., satellite scene, single timestamp):**

- Use `properties.datetime`.  
- Do **not** set start/end unless semantically necessary.

**Interval / aggregated data (e.g., 24h precipitation, daily mean streamflow):**

- Use `properties.start_datetime` and `properties.end_datetime`.  
- Optionally set `datetime` to:
  - The center of the interval, OR  
  - Omit `datetime` if interval semantics are clear and consistent with KFM profile.

### 3.2 Time vs Model Run Time

For forecasts and model outputs (e.g., HRRR, GFS):

- Use:
  - `properties.datetime` or interval for **valid time**.  
  - `kfmclim:run_datetime` (climate extension) for **run time**.  
  - `kfmclim:lead_time_hours` for forecast lead time.

### 3.3 Collections & Temporal Extents

- Collections should use `extent.temporal.interval` to represent:
  - Overall temporal span (e.g., `["2010-01-01T00:00:00Z", null]`).  
- Do not over-specify; let Items capture finer granularity.

---

## 📦 4. Assets, Roles & Media Types

### 4.1 Asset Naming

**Best practice:**

- Use **short, semantic keys** in `assets`:

  - `data` — primary data asset.  
  - `thumbnail` — quick-look image.  
  - `overview` — reduced-resolution derivative.  
  - `metadata` — extended metadata doc (e.g., PDF, JSON).  
  - Domain-specific keys (e.g., `timeseries`, `index`, `quality`) where documented.

### 4.2 Roles

Use `roles` consistently:

- `["data"]` — primary analysis-ready content.  
- `["thumbnail"]` — UI preview.  
- `["overview"]` — lower-res/higher-performance version.  
- `["metadata"]` — additional documentation.  
- Domain-specific roles (`["timeseries"]`, `["index"]`) must be described in domain docs.

### 4.3 Media Types

- Use standard **MIME types**:
  - GeoTIFF: `"image/tiff; application=geotiff"`  
  - Cloud-Optimized GeoTIFF: same with additional profile metadata, not a different MIME.  
  - NetCDF: `"application/x-netcdf"`  
  - Parquet: `"application/x-parquet"`  
  - PNG: `"image/png"`  
  - JPEG: `"image/jpeg"`  

- Avoid ad-hoc or incorrect media types; they break consumers and catalogers.

### 4.4 Checksums & Size

- Include `checksum:sha256` for assets where feasible.  
- Prefer full SHA-256 over weaker hash algorithms.  
- File size fields (if used) should be in **bytes** and match downstream checks where possible.

---

## 🧾 5. IDs, Naming & Collections vs Items

### 5.1 ID Conventions

**Item IDs:**

- Must be **stable**, safe for use in URLs and filenames.  
- Recommended pattern:

  - `<dataset-short-name>_<YYYY><MM><DD>[_<HHMM>][_<tile-or-region-id>]`  

  Examples:

  - `naip_2023_tile_001`  
  - `hrrr_precip_20250601_0000_f006`  
  - `arch_landscape_flint_hills_v1`

**Collection IDs:**

- Describe the **dataset family**, not individual scenes:

  - `naip_ks_2023`  
  - `hrrr_precip_ks_3km`  
  - `arch_cultural_regions_ks_v1`

### 5.2 Collections vs Items

**Use Collections to:**

- Group Items from a single dataset family.  
- Describe:
  - High-level spatial/temporal extents  
  - Common licensing, providers, and governance metadata  

**Use Items to:**

- Represent **individual observations or slices**:
  - A single scene/tile/time slice.  
  - A single gauge/time-day combination, if using gauge-based STAC.  
  - A single landscape-aggregate or region representation.

**Do NOT:**

- Put large time series into a single Item; prefer:
  - One Item per day/tile, or  
  - One Item per region/time-slice, with Assets holding time series.

---

## 🔗 6. Links, Providers & Lineage

### 6.1 Links

Use `links` to:

- Express hierarchy:
  - `self`, `parent`, `collection`, `root`.

- Connect to related resources:
  - `about`, `via`, `derived_from`, `latest-version`.  

Where possible, tie links to:

- KFM dataset registry records.  
- External authoritative sources (e.g., NOAA, USGS, KSHS) with stable URIs.

### 6.2 Providers

Populate `providers` thoughtfully:

- Include:
  - `name`, `roles` (`["producer"]`, `["licensor"]`, `["processor"]`, `["host"]`).  
  - `url` where appropriate.

Use provider roles to:

- Distinguish **source agencies** from **KFM processing/hosting roles**.

---

## 🛡️ 7. FAIR+CARE, Sovereignty & STAC

STAC must **embed governance metadata** via KFM extensions:

- Use `kfm-faircare` (`stac-ext-faircare.md`) for:

  - `kfmfc:sensitivity`  
  - `kfmfc:care_label`  
  - `kfmfc:sovereignty_flag`  
  - `kfmfc:visibility_rules`  

- Use domain extensions (`kfm-archaeology`, `kfm-hydrology`, `kfm-climate`) to refine:

  - Domain-specific sensitivity (e.g., `kfmarch:sensitivity_class`).  
  - Governance notes (e.g., hydrology rights-sensitive data).

**Best-practice rules:**

- **Do not** embed personally identifying or site-level restricted information in public STAC.  
- Where necessary, maintain:
  - An **internal STAC** with full details.  
  - A **public derivative STAC** with generalized geometry and redacted fields.

- Keep provenance:
  - STAC → derived STAC (public) should be connected via PROV-O logs.

---

## 🧪 8. Validation & CI Patterns

KFM CI must enforce both:

1. **Schema-level correctness**
   - Using `stac-validator` + KFM extension schemas.  

2. **Best-practice linting**
   - Using `stac-check` or KFM-specific linters to check:
     - ID formats.  
     - Temporal field consistency.  
     - Geometry/bbox semantics.  
     - Asset MIME types and roles.  
     - Required KFM fields (`kfm-core`, FAIR+CARE, etc.).

Indicative CI workflows:

- `catalog-stac-validate.yml`  
- `catalog-stac-lint.yml`  
- `catalog-stac-extensions-validate.yml`

These should run:

- On pull requests touching STAC.  
- On scheduled basis for full-catalog health checks.

Telemetry from these jobs should populate:

- `catalog-metadata-telemetry.json` with:
  - Counts of STAC validation errors/warnings.  
  - Frequency of specific failure modes.

---

## ✅ 9. Quick Checklist for Authors

Before merging new or updated STAC content:

1. **Geometry & bbox**
   - Geometry = accurate, CRS = EPSG:4326.  
   - Bbox = derived, not random.  
   - Generalized where governance requires.

2. **Temporal fields**
   - `datetime` for instants; `start/end` for intervals.  
   - Forecasts: run time vs valid time captured via climate extension.

3. **Assets**
   - Clear, semantic asset keys.  
   - Roles, MIME types, and checksums set correctly.

4. **IDs & naming**
   - Stable, meaningful IDs for Items and Collections.  
   - Patterns consistent with KFM domain conventions.

5. **Governance**
   - FAIR+CARE & sovereignty fields set if applicable.  
   - No sensitive internal-only fields in public STAC.

6. **Validation**
   - `stac-validator` passes with KFM profiles and extensions.  
   - CI passes all STAC-related workflows.

---

## 🕰️ 10. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial KFM STAC best-practices guide; codified geometry, temporal, asset, naming, link, and governance patterns consistent with KFM STAC profile and STAC-first → DCAT-derived model. |

