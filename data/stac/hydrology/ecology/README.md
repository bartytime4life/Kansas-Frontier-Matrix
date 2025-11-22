---
title: "🧬 Kansas Frontier Matrix — Hydrology–Ecology STAC Collection (v11 Super-Edition)"
path: "data/stac/hydrology/ecology/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology–Ecology Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/data-stac-hydro-ecology-index-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "STAC Collection Index"
intent: "stac-hydrology-ecology-index"
semantic_document_id: "kfm-stac-hydrology-ecology-index"
doc_uuid: "urn:kfm:stac:hydrology:ecology:index:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧬 **Hydrology–Ecology STAC Collection (v11 Super-Edition)**  
`data/stac/hydrology/ecology/README.md`

**Purpose:**  
Provide the **complete STAC specification** for all ecological datasets linked to hydrology, including  
mussel beds, fish assemblages, macroinvertebrate surveys, riparian vegetation, habitat polygons,  
downstream biological responses, ecological impact of hydrologic operations, and WID-related  
ecological monitoring.  
Defines metadata, ontology, provenance, asset schemas, and Focus Mode v3 integration.

</div>

---

# 📘 0. Overview

The **Hydrology–Ecology STAC domain** catalogs ecological datasets that are directly influenced by  
hydrology, geomorphology, sedimentation, and reservoir operations across Kansas.

This includes:

- Mussel bed polygons  
- Fish assemblage surveys  
- Macroinvertebrate indices (EPT richness, HBI, tolerant taxa)  
- Riparian vegetation zones  
- Habitat polygons (riffle, pool, backwater)  
- Downstream impact assessments from dams (e.g., Clinton, Tuttle Creek, Perry, Milford)  
- WID 2025 biological monitoring (mussels, fish, DO/turbidity response)  

These datasets require **tight hydrologic coupling**, making STAC critical for:

- Spatiotemporal ecological analysis  
- AI-driven ecological narratives (Story Nodes)  
- Focus Mode context panels  
- Statewide ecological corridor integration  
- Multi-reservoir biological impact comparison  

---

# 🗂️ 1. Directory Layout (Canonical)

```text
data/
└── stac/
    └── hydrology/
        └── ecology/
            ├── collection.json
            └── items/
                ├── mussels-tc-tailwater.json
                ├── mussels-clinton.json
                ├── fish-tc-2025.json
                ├── fish-clinton.json
                ├── macroinv-tc.json
                ├── riparian-zones.json
                ├── habitat-polygons.json
                ├── downstream-biotic-response.json
                └── wid-2025-biological-summary.json
```

This hierarchy is identical to reservoir-level hydrology STAC design patterns.

---

# 🌍 2. Ecology–Hydrology Dataset Themes

## ✔ 2.1 Mussel Ecology
- Species counts, densities, beds  
- Sensitive to DO, turbidity, substrate composition  
- Strongly affected by dam operations + sediment regimes  

## ✔ 2.2 Fish Assemblages
- Riffle/pool/transition zone species  
- Hydrologic cue dependence  
- Thermal + DO sensitivity  
- Habitat connectivity  

## ✔ 2.3 Macroinvertebrates
- EPT richness  
- Biotic indices (HBI, TBI)  
- Organic matter transport  
- Turbidity + scour effects  

## ✔ 2.4 Riparian + Floodplain Vegetation
- Vegetation community classification  
- Inundation frequency  
- Channel migration corridors  

## ✔ 2.5 Habitat Geometry
- Riffle zones  
- Deep pools  
- Side channels  
- Backwaters  
- Mussel bars  

## ✔ 2.6 Downstream Impact Assessments
- Tailwater DO/turbidity impacts  
- Sediment pulses  
- Fish/mussel response during hydrologic events  
- WID 2025 biological safety thresholds  

---

# 📐 3. Required STAC Metadata Fields (Strict Hydrology–Ecology Profile)

### ✔ Core STAC Fields
- `stac_version`  
- `type = "Feature"`  
- `id`  
- `collection`  
- `geometry`  
- `bbox`  
- `properties.datetime`  
- `assets`  

### ✔ Ecological `kfm:*` Required Fields
| Field | Meaning |
|-------|---------|
| `kfm:parameter` | e.g., mussels, fish, invertebrates, vegetation |
| `kfm:units` | individuals/m², counts, index score |
| `kfm:method` | quadrat sampling, electrofishing, kick-net, UAV, etc. |
| `kfm:provider` | KDWP, USACE, KDWPT, USGS, tribal biologists |
| `kfm:site` | survey station code |
| `kfm:lineage` | ETL → STAC provenance |
| `kfm:quality` | QA/QC class |
| `kfm:hydro_region` | e.g. `Clinton_Reservoir`, `Tailwater`, `Big_Blue_River` |
| `kfm:project` | e.g. WID-2025, Hydrology-Core, Downstream-Effects |

### ✔ Recommended
- `kfm:habitat_type`  
- `kfm:survey_protocol`  
- `kfm:ecological_group`  
- `kfm:dominant_species`  

---

# 🧭 4. Asset Standards

## ✔ GeoJSON (Primary)
Used for:
- Mussel bed polygons  
- Fish habitat areas  
- Riparian vegetation zones  
- Habitat classifications  
- Downstream impact buffers  

Required:  
- `FeatureCollection`  
- `geometry`: Polygon/Point/LineString  
- `properties`: survey metadata, counts, metrics  

---

## ✔ CSV / CSVW (Secondary)
Used for:
- Species count tables  
- Index scores (EPT, HBI, TBI)  
- Physiochemical parameters linked to ecology  

Columns:
`timestamp, species, count, metric, site_id, qc_flag, provenance`

---

## ✔ COG / Raster (Optional)
Used for:
- Vegetation grids  
- Thermal refugia rasters  
- Hydrodynamic suitability surfaces  

---

## ✔ MP4 (Optional)
Used for:
- Underwater video surveys  
- Habitat drone mapping  
- WID-related biological monitoring videos  

---

# 🧬 5. Example STAC Item (Mussel Polygon)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "mussels-tc-tailwater",
  "collection": "hydrology-ecology",
  "geometry": { "type": "Polygon", "coordinates": [...] },
  "bbox": [-96.60, 39.27, -96.58, 39.29],
  "properties": {
    "datetime": "2024-07-15T00:00:00Z",
    "kfm:parameter": "mussels",
    "kfm:units": "individuals_per_m2",
    "kfm:provider": "KDWPT",
    "kfm:method": "quadrat",
    "kfm:lineage": "etl/ecology/mussels_tc_2024_v1",
    "kfm:quality": "A",
    "kfm:hydro_region": "Big_Blue_Tailwater",
    "kfm:project": "Downstream-Effects"
  },
  "assets": {
    "geojson": {
      "href": "https://example.org/ecology/mussels_tc_tailwater.geojson",
      "type": "application/geo+json",
      "roles": ["data"]
    }
  }
}
```

---

# 🕸️ 6. CIDOC-CRM / GeoSPARQL / OWL-Time Mapping

### CRM Entities
- `E73 InformationObject` → survey dataset  
- `E53 Place` → habitat polygon  
- `E57 Material` → biological material category  
- `E5 Event` → survey activity  
- `E7 Activity` → WID 2025 monitoring  
- `ObservationSeries` → ecological observations  

### Relations
- `P7_took_place_at`  
- `P70_documents`  
- `P1_is_identified_by`  
- `prov:wasGeneratedBy`  
- `geo:hasGeometry`  
- `time:hasTime`  

---

# 🧩 7. DCAT 3.0 Crosswalk

| STAC Field | DCAT Field |
|------------|------------|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| `extent.spatial` | `dct:spatial` |
| `extent.temporal` | `dct:temporal` |
| `assets[].href` | `dcat:downloadURL` |
| `keywords` | `dcat:keyword` |

---

# 🛠️ 8. ETL → STAC → Graph Ingestion Workflow

```
Raw ecological surveys
    ↓ extract
Spatial normalization, schema cleaning
    ↓ transform
Asset creation (GeoJSON / CSVW / COG)
    ↓ stac-annotate
Item creation (STAC JSON)
    ↓ validate
Neo4j ingestion (CIDOC-CRM + GeoSPARQL)
    ↓
Focus Mode v3 binding
```

Each ETL run MUST be documented in:  
`mcp/experiments/hydrology/ecology/*`

---

# 🎯 9. Focus Mode v3 Integration

Focus Mode uses ecology Items to populate:

- Habitat snapshots  
- Species-richness panels  
- Mussel bed overlays  
- Downstream DO/turbidity-linked ecological responses  
- Seasonal or event-based biological indicators  

Selecting a **reach**, **event**, or **species group** automatically filters Items using:

- `kfm:hydro_region`  
- `kfm:parameter`  
- `datetime` range  

---

# 📖 10. Story Node v3 Integration

Example Story Nodes:

- **“Downstream of the Dam: The Life Beneath the Water”**  
- **“Mussel Corridors of the Big Blue and Kansas Rivers”**  
- **“Ecology in the Wake of WID 2025”**  

Story Nodes reference Items via:

```json
{
  "rel": "uses-dataset",
  "target": "mussels-tc-tailwater"
}
```

---

# 🚀 11. Expansion Roadmap

Future hydrology–ecology STAC Items:

- Annual biological monitoring (2025–2035)  
- Invasive species spread polygons  
- Climate-resilience habitat grids  
- WID multi-year biological response Items  
- Environmental DNA datasets (eDNA)  
- Riparian succession models  
- Multi-reservoir ecological corridors  

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial super-edition creation of Ecology STAC domain index.

---

[⬅ Back to Hydrology STAC Domain](../README.md) • [📂 Data Home](../../../README.md) • [🏠 KFM Master Guide](../../../../../docs/reference/kfm_v11_master_documentation.md)

