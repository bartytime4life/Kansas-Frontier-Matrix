---
title: "📦 KFM v11.2.3 — STAC → DCAT Derivation Model (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Authoritative pattern for treating STAC as the source of truth and emitting DCAT automatically from STAC for the Kansas Frontier Matrix."
path: "docs/standards/catalogs/stac-dcat-derivation.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → DCAT 3.0 crosswalk compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-stac-dcat-derivation-v11.2.3"
semantic_document_id: "kfm-standards-stac-dcat-derivation-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac-dcat-derivation:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Standard"
intent: "metadata-stac-to-dcat-derivation"
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

json_schema_ref: "../../schemas/json/stac-dcat-derivation-v1.json"
shape_schema_ref: "../../schemas/shacl/stac-dcat-derivation-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC/DCAT standards update"
---

<div align="center">

# 📦 KFM v11.2.3 — STAC → DCAT Derivation Model  
`docs/standards/catalogs/stac-dcat-derivation.md`

**Purpose:**  
Define the **authoritative KFM pattern** in which **STAC Items and Collections are the source of truth**, and **DCAT is always derived automatically from STAC** for catalogs, portals, and federation.

</div>

---

## 📘 1. Purpose

This standard specifies KFM’s catalog architecture:

- **STAC (SpatioTemporal Asset Catalog) Items and Collections are authoritative.**  
- **DCAT (Data Catalog Vocabulary) representations are emitted automatically from STAC.**

Goals:

- Preserve **spatial accuracy** and **temporal consistency**.  
- Avoid drift between **asset-level metadata** and higher-level catalogs.  
- Ensure catalogs remain **FAIR+CARE-compliant**, provenance-aware, and machine-safe.

---

## 🗂️ 2. Directory Layout (Recommended · v11.2.3)

~~~text
docs/standards/catalogs/
├── 📄 stac-dcat-derivation.md          # This document (STAC → DCAT model)
│
├── 🧩 stac/                            # STAC profiles, patterns, examples
│   └── 📄 stac-kfm-profile.md
│
├── 🧩 dcat/                            # DCAT profiles, patterns, examples
│   └── 📄 dcat-kfm-profile.md
│
└── 🧪 crosswalks/                      # Implementation-oriented crosswalk docs
    └── 📄 stac-dcat-crosswalk.md
~~~

Implementation code & CI hooks should live under:

- `pipelines/catalogs/stac-dcat/` — ETL & crosswalk code.  
- `schemas/catalogs/` — JSON/SHACL schemas validating derived DCAT against this model.

---

## 🌍 3. Why STAC Is the Source of Truth

STAC is a **GeoJSON-native, geospatially explicit** model. A STAC Item/Collection carries:

- `geometry` — exact spatial footprint  
- `bbox` — derived spatial envelope  
- `properties.datetime` or `properties.start_datetime` / `properties.end_datetime`  
- `assets` — per-asset `href`, `type`, `roles`, checksums, titles  
- `properties` — domain-specific metadata (e.g., NAIP, HRRR, archaeology)

These fields drive:

- Map rendering & tiling  
- Ingestion pipelines (ETL, cloud-native access)  
- Provenance & lineage (via PROV-O / KFM registries)  
- Temporal indexing & query  
- Validation via `stac-validator` and related tools  

Because STAC is **spatially explicit, time-aware, and asset-centric**, KFM treats it as **canonical** and **directly maintained** by data engineers and domain stewards.

---

## 📚 4. Why DCAT Should Be Derived

DCAT is optimized for:

- **Discovery & search**  
- **Catalog portals & federation** (e.g., CKAN, GeoNetwork, national portals)  
- Semantic web ecosystems (RDF, JSON-LD, Turtle)

DCAT is **not designed** to be the authoritative geospatial metadata layer for:

- Complex asset lists (multiple formats, pyramids, overviews)  
- Detailed geospatial footprints beyond bounding boxes  
- STAC-specific collection → item → asset structure

Therefore:

- **DCAT must be treated as an artifact** generated from STAC.  
- Editing DCAT directly risks divergence between the catalog and spatially authoritative STAC.

**KFM rule:**  
> STAC is edited → STAC is validated → DCAT is regenerated → portals & catalogs update.

No production DCAT should exist without an upstream STAC representation.

---

## 🧱 5. Recommended Architecture (STAC-First Pipeline)

~~~text
Authoritative STAC Catalog
(datasets/stac/**.json)
│
├── validate → stac-validator · stac-check
│
└── transform → stac → DCAT JSON-LD crosswalk
     │
     ├── dcat:Dataset (per STAC Item/Collection)
     ├── dcat:Distribution (per STAC Asset)
     └── Optional dcat:DataService records
~~~

**Key rule:**  
- **Do NOT hand-edit DCAT.**  
- All DCAT (JSON-LD, Turtle, RDF/XML) must be **derived artifacts** produced from STAC via governed crosswalks.

---

## 🔁 6. Minimal STAC → DCAT Crosswalk

This table defines the **minimal, stable mapping template**. Domain-specific extensions may add more fields, but **must not conflict** with this base.

### 6.1 STAC → DCAT (Dataset-Level)

| STAC Field / Concept                  | DCAT / RDF Field                  |
|--------------------------------------|-----------------------------------|
| `id`                                 | `dct:identifier`                  |
| `properties.title` (if present)      | `dct:title`                       |
| `properties.description`             | `dct:description`                 |
| `bbox`                               | `dct:spatial` (`dct:Location`)    |
| `datetime` or `start/end_datetime`   | `dct:temporal` (`dct:PeriodOfTime`) |
| `keywords` / `tags`                  | `dcat:keyword`                    |
| `providers`                          | `dct:publisher`, `dct:creator`    |
| `links` (homepage, docs)             | `dcat:landingPage` / `foaf:page`  |
| Collection membership                | `dct:isPartOf` / `dcat:inSeries`  |

### 6.2 STAC Asset → DCAT Distribution

| STAC Asset Field                     | DCAT / RDF Field                  |
|--------------------------------------|-----------------------------------|
| `href`                               | `dcat:downloadURL`                |
| `type`                               | `dct:format`                      |
| `roles`                              | `dcat:role` (or profile-specific) |
| `checksum:*`                         | `spdx:checksum`                   |
| `title`                              | `dct:title`                       |
| `description` (if present)           | `dct:description`                 |

Additional mappings (e.g., `eo:*`, `sar:*`, domain profiles) should be defined in crosswalk profile docs under `docs/standards/catalogs/crosswalks/`.

---

## 🧪 7. Example STAC → DCAT JSON-LD Derivation

### 7.1 Input STAC Item (Simplified)

~~~json
{
  "id": "naip_2023_tile_001",
  "type": "Feature",
  "geometry": { "...": "..." },
  "bbox": [-98.0, 38.1, -97.9, 38.2],
  "properties": {
    "datetime": "2023-07-11T18:22:00Z",
    "title": "NAIP 2023 Tile 001",
    "description": "NAIP 2023 imagery tile over central Kansas."
  },
  "assets": {
    "image": {
      "href": "https://example.com/naip_001.tif",
      "type": "image/tiff; application=geotiff",
      "checksum:sha256": "abc123..."
    }
  }
}
~~~

### 7.2 Output DCAT JSON-LD (Auto-Generated)

~~~json
{
  "@context": "https://www.w3.org/ns/dcat.jsonld",
  "@type": "dcat:Dataset",
  "dct:identifier": "naip_2023_tile_001",
  "dct:title": "NAIP 2023 Tile 001",
  "dct:description": "NAIP 2023 imagery tile over central Kansas.",
  "dct:spatial": {
    "@type": "dct:Location",
    "bbox": [-98.0, 38.1, -97.9, 38.2]
  },
  "dct:temporal": {
    "@type": "dct:PeriodOfTime",
    "dcat:startDate": "2023-07-11T18:22:00Z",
    "dcat:endDate": "2023-07-11T18:22:00Z"
  },
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dcat:downloadURL": "https://example.com/naip_001.tif",
      "dct:format": "image/tiff; application=geotiff",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "sha256",
        "spdx:checksumValue": "abc123..."
      }
    }
  ]
}
~~~

**Note:**  
- This JSON-LD is **derived**, not authored.  
- Any change to STAC should regenerate a **new DCAT dataset** (or updated fields), never the reverse.

---

## 🛠️ 8. Tooling Recommendations (KFM-STAC/DCAT Stack)

KFM recommends the following tools for a **STAC-first, DCAT-derived** pipeline:

- **STAC Validation & Linting**
  - `stac-validator` — schema + best-practice checks  
  - `stac-check` — additional linting and semantic checks  

- **STAC → DCAT Crosswalk**
  - `stac-utils` / `stactools` crosswalks where available  
  - Custom **Python** or **Node.js** crosswalk scripts in `pipelines/catalogs/stac-dcat/`  
  - **`jq` pipelines** for lightweight field mapping and JSON shaping  

- **CI / Automation**
  - GitHub Actions (e.g., `catalog-stac-validate.yml`, `catalog-stac-dcat-derive.yml`)  
  - Make targets (e.g., `make stac-validate`, `make stac-to-dcat`)  

**Output DCAT guidelines:**

- Always publish **JSON-LD first** (primary).  
- Optionally emit **Turtle** and **RDF/XML** as secondary formats.  
- Store derived DCAT alongside or just downstream of STAC, e.g.:

  - `datasets/stac/…` (source)  
  - `datasets/dcat/jsonld/…` (derived)

---

## ✅ 9. CI & Governance Rules

CI must enforce the following:

1. **No orphan DCAT**  
   - Every DCAT dataset MUST have a corresponding STAC Item/Collection.  

2. **No hand-edited DCAT in production**  
   - Derived DCAT files should be treated as build artifacts:
     - Regenerated by pipelines  
     - Overwritten during CI/CD  
     - Excluded from manual editing (or explicitly flagged if temporarily edited during debugging).

3. **Crosswalk validation**  
   - Derived DCAT must:
     - Validate against the KFM DCAT profile schema.  
     - Maintain identifier and temporal/spatial consistency with STAC.  

4. **Provenance alignment**  
   - PROV-O lineage must link:
     - STAC source → crosswalk script/tool → DCAT artifact  
     - DCAT artifacts must reference the originating STAC IDs.

Governance events:

- Changing the STAC profile or DCAT profile must trigger:
  - Crosswalk updates  
  - Schema and SHACL shape updates  
  - This document’s version bump and review

---

## 🧾 10. Summary (KFM Position)

KFM’s **authoritative stance** for catalog metadata:

- **Always author and maintain metadata in STAC.**  
- **Never treat DCAT as the source of truth.**  
- **Always derive DCAT (JSON-LD and others) from validated STAC via governed crosswalks.**  
- **Use explicit STAC → DCAT mappings to preserve semantic and spatial fidelity.**

This model ensures:

- Spatial correctness for maps and analytics  
- Stable, federated catalogs for discovery & portals  
- Consistent, traceable metadata across KFM’s systems and external partners

---

## 🕰️ 11. Version History

| Version  | Date       | Author                                | Summary                                                                 |
|----------|------------|---------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Initial KFM-standard STAC → DCAT derivation model; defined STAC-first catalog architecture, crosswalk, tooling, and CI rules. |


