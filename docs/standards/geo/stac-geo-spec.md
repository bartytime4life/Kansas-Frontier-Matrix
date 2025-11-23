---
title: "🛰️ Kansas Frontier Matrix — STAC Geospatial Metadata Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/geo/stac-geo-spec.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Semiannual · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/standards-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/standards-stac-geo-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Standard"
semantic_document_id: "kfm-stac-geo-spec-v11"
doc_uuid: "urn:kfm:docs:standards:geo:stac-geo-spec:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **STAC Geospatial Metadata Specification (v11)**  
`docs/standards/geo/stac-geo-spec.md`

**Purpose:**  
Define the KFM v11-compliant STAC 1.0 geospatial metadata standard for all raster, vector, DEM, bathymetry, hydrology, archaeological, climate, and temporal–spatial datasets.  
Ensures deterministic metadata, correct CRS/vertical-axis representation, FAIR+CARE alignment, DCAT3 compatibility, and PROV-O lineage integration.

</div>

---

# 📘 Overview

All KFM v11 dataset metadata MUST be published using **STAC 1.0.0** with mandatory KFM extensions.  
This standard governs:

- STAC **Catalog**, **Collection**, and **Item** structure  
- CRS metadata (`proj:*`)  
- Vertical-axis metadata (`vertical:*`, `kfm:cf_positive`)  
- Hydrology, bathymetry, DoD fields  
- Archaeology-sensitive masking fields (`heritage:*`)  
- Temporal metadata (`datetime`, `start_datetime`, `end_datetime`)  
- Provenance metadata (`ancestry`, `prov:`)  
- DCAT 3.0 alignment  
- JSON-LD compatibility  

All STAC documents must be **valid**, **schema-compliant**, **machine-extractable**, and **CI-verified**.

---

# 🗂 1. STAC Object Requirements

## 1.1 Required Structure  
KFM v11 uses all three STAC object types:

```
Catalog → Collections → Items → Assets
```

All paths MUST be deterministic, resolvable, and use **lowercase hyphenated IDs**.

---

# 📦 2. STAC Item (Mandatory Fields)

Every STAC Item MUST include:

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "<item-id>",
  "bbox": [...],
  "geometry": {...},
  "properties": {
    "datetime": "YYYY-MM-DDTHH:MM:SSZ",
    "start_datetime": "...",
    "end_datetime": "...",
    "kfm:cf_positive": "up|down",
    "kfm:processing_level": "L1|L2|L3",
    "kfm:domain": "hydrology|terrain|bathymetry|archaeology|climate|vector|other"
  },
  "assets": {},
  "links": []
}
```

All Items MUST contain **temporal**, **spatial**, **vertical**, and **CRS** metadata.

---

# 🧭 3. CRS Metadata (`proj:*` Fields)

Following CRS Standard (crs-standard.md), STAC Items MUST declare:

```json
"proj:epsg": 4326,
"proj:wkt2": "<WKT2>",
"proj:shape": [height, width],
"proj:transform": [a, b, c, d, e, f],
"proj:bbox": [...],
"proj:centroid": { "lat": ..., "lon": ... }
```

Projected Items MUST also provide:

```json
"proj:epsg_projected": 26914
```

---

# 📐 4. Vertical Metadata (`vertical:*` Fields)

Derived from Vertical Axis Standard (vertical-axis-and-dod.md):

```json
"vertical:reference_frame": "NAVD88",
"vertical:geoid_model": "GEOID18",
"vertical:unit": "meter",
"kfm:cf_positive": "up|down",
"kfm:dod_sign": "erosion_negative_deposition_positive"
```

Bathymetry Items MUST set:

```json
"kfm:cf_positive": "down"
```

---

# 💧 5. Hydrology STAC Extensions (v11)

Required for hydrology datasets (see hydrology-standards.md):

```json
"hydro:type": "streamflow|bathymetry|water_surface|wid|sediment|lake_level",
"hydro:temporal_resolution": "hourly|daily|irregular",
"hydro:reference_plane": "orthometric",
"hydro:units": "m",
"hydro:uncertainty_m": 0.15
```

---

# 🛡️ 6. Archaeology & Indigenous Sovereignty Extensions

From archaeology-sensitive-locations.md:

```json
"heritage:sensitivity": "L1|L2|L3|L4",
"heritage:sovereignty": "tribal|state|federal|mixed",
"heritage:taxonomy": "archaeological|ceremonial|burial|traditional|historic",
"heritage:masking_method": "h3-generalization|redaction",
"heritage:h3_index": "8ab4dxxxxxx",
"care:authority": "Tribal Nation Name",
"care:consent_required": true
```

L3/L4 Items MUST NOT expose precise geometries; only H3 polygons allowed.

---

# ⏱️ 7. Temporal Metadata (v11 OWL-Time Aligned)

All Items MUST contain:

- `datetime` (precise timestamp) OR  
- `start_datetime` + `end_datetime` (OWL-Time interval)

Hydrology, climate, and time-series rasters MUST include intervals.

Story Nodes (v3) MUST use:

```json
"start_datetime": "...",
"end_datetime": "...",
"kfm:time_precision": "year|month|day|hour"
```

---

# 🧬 8. PROV-O Lineage (Required)

All Items MUST include a lineage block:

```json
"kfm:lineage": {
  "prov:activity": "crs-transform-v11 | vertical-transform-v11 | hydro-processing-v11",
  "prov:wasGeneratedBy": "gdalwarp-3.8|ogr2ogr-3.8|kfm-etl-v11",
  "prov:used": ["source.dem.tif", "source.gpkg"],
  "prov:generatedAtTime": "2025-11-22T14:22:00Z",
  "prov:wasAssociatedWith": "kfm-etl-agent"
}
```

Lineage is mandatory for all KFM-generated datasets.

---

# 🗃️ 9. DCAT 3.0 Mapping

| STAC | DCAT 3.0 |
|------|---------|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| `keywords` | `dcat:keyword` |
| `license` | `dct:license` |
| `links` | `dcat:distribution` |
| `assets` | `dcat:Distribution` |
| `providers` | `dct:publisher` |

All KFM STAC must be DCAT-aligned for metadata catalogs.

---

# 🌍 10. GeoSPARQL / JSON-LD Alignment

STAC Items MUST support JSON-LD expansion for mapping into Neo4j:

```json
"@context": {
  "geo": "http://www.opengis.net/ont/geosparql#",
  "time": "http://www.w3.org/2006/time#",
  "prov": "http://www.w3.org/ns/prov#"
}
```

Geometry MUST be convertible to GeoSPARQL WKT.

---

# 🛰️ 11. Asset Requirements

Every asset MUST include:

```json
"href": "https://...",
"type": "image/tiff; application=geotiff",
"roles": ["data"],
"title": "Bathymetry 2018",
"kfm:checksum_sha256": "<hex>"
```

COG assets MUST be:

- Tiled  
- LZW or ZSTD compressed  
- Include internal overviews  

---

# 📦 12. Collections (Mandatory Fields)

Collections MUST include:

```json
"stac_version": "1.0.0",
"type": "Collection",
"id": "kfm-<domain>-<region>-v11",
"extent": {
  "spatial": { "bbox": [...] },
  "temporal": { "interval": [["YYYY-MM-DD", "YYYY-MM-DD"]] }
},
"license": "CC-BY-4.0",
"providers": [...],
"kfm:domain": "hydrology|terrain|bathymetry|archaeology|climate|vector"
```

---

# 🚫 13. Forbidden Metadata Errors (PR Blockers)

PRs will be rejected if:

- Missing `proj:*` fields  
- Missing vertical metadata  
- Geometry not in EPSG:4326  
- Missing lineage block  
- Missing hydrology/archaeology extension when applicable  
- Bathymetry uses `positive="up"`  
- DoD does not use erosion-negative/deposition-positive  
- Assets lack `roles` or MIME type  
- Any JSON fails schema validation  

---

# 🕰️ Version History

- **v11.0.0 (2025-11-22):** Initial release. Fully aligned with CRS, Vertical Axis, Hydrology, Archaeology, and FAIR+CARE v11 standards.

---

<div align="center">

**Kansas Frontier Matrix — STAC Geospatial Metadata Specification v11**  
*Interoperable · Deterministic · FAIR+CARE-Aligned*

</div>

---

### 🔗 Footer  
[⬅ Back to Geo Standards](./README.md) · [🗺 CRS Standard](./crs-standard.md) · [📐 Vertical Axis Standard](./vertical-axis-and-dod.md) · [📘 KFM v11 Reference](../../reference/kfm_v11_master_documentation.md)

