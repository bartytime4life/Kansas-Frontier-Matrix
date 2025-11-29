---
title: "🧾 NASA SMAP — DCAT, JSON-LD, PROV-O Metadata Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/data/satellites/smap/metadata/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Earth Systems Working Group"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

dcat_profile: "KFM-DCAT v11"
stac_profile: "KFM-STAC v11"
jsonld_profile: "KFM-JSONLD v11"
provenance_profile: "KFM-PROV-O v11.2"
ontology_protocol_version: "KFM-OP v11"
markdown_protocol_version: "KFM-MDP v11.2.2"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-metadata-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
classification: "Public Dataset Metadata"
fair_category: "F1-A1-I2-R3"
care_label: "CARE-A / CARE-B depending on geographies"
indigenous_rights_flag: true
sensitivity_level: "Low (metadata only)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  dct: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/metadata-smap-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/metadata-smap-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:metadata-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-metadata"
event_source_id: "ledger:docs/data/satellites/smap/metadata/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next SMAP metadata schema revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧾 **NASA SMAP — Metadata Layer (DCAT · JSON-LD · PROV-O)**  
`docs/data/satellites/smap/metadata/README.md`

**Purpose**  
Define all **high-level dataset metadata** for NASA SMAP inside the Kansas Frontier Matrix:  
DCAT catalogs, JSON-LD semantic graphs, PROV-O lineage chains, and KFM governance metadata.  
This metadata backs *all* SMAP STAC Collections and Items (soil-moisture, freeze-thaw, VWC, QA/RFI, ancillary).

</div>

---

## 📘 1. Overview

The `metadata/` directory provides dataset-level metadata for SMAP:

- 🧾 **DCAT v3 Datasets**
- 🌐 **JSON-LD knowledge-graph descriptors**
- 🧬 **PROV-O lineage entities & derivations**
- 🛡 **CARE + sovereignty declarations**
- 📜 **Citation & DOI records**
- 🗃 **Dataset-level description modules** (names, themes, keywords)
- 🤝 **Provider/creator attribution** (NASA, KFM pipelines)

This metadata ensures:

- **Interoperability** across STAC, DCAT, GraphQL, Story Node v3, Focus Mode v3  
- **Searchability** via KFM’s knowledge graph  
- **FAIR+CARE compliance** at the dataset level  
- **Reproducible lineage** for hydrology & climate ETL models  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/metadata/
├── 📄 README.md                          # This file
│
├── 🗂️ dcat-dataset.jsonld                # DCAT v3 dataset listing for all SMAP product lines
├── 🌐 jsonld-context.json                # JSON-LD @context for SMAP data in KFM graph
├── 🔗 provenance.jsonld                  # PROV-O lineage for all SMAP transformations
├── 🧭 governance.json                    # CARE labels, sovereignty notes, masking rules
├── 🧭 sensitivity-map.json               # Optional H3-level masking definitions & policy markers
├── 📚 citations.json                     # DOI references, NASA documentation, mission references
├── 🏷 keywords.json                      # Thematic categories used by DCAT, Story Nodes, Focus Mode
└── 📅 temporal-coverage.json             # Start/End dates for SMAP products (OWL-Time)
~~~

---

## 🧩 3. Metadata Specification (KFM-DCAT v11)

### Required DCAT Fields

Each SMAP dataset MUST define:

- `dct:title`  
- `dct:description`  
- `dct:identifier`  
- `dct:temporal` (OWL-Time interval)  
- `dct:spatial` (GeoJSON bbox)  
- `dct:publisher` (NASA + KFM)  
- `dct:license`  
- `dcat:keyword[]`  
- `dcat:distribution[]` referencing STAC assets  

### Required JSON-LD Context

- Alignment with:
  - `schema.org/Dataset`
  - `geo:FeatureCollection`
  - `prov:Entity`
  - `time:TemporalEntity`
  - KFM-OP v11 ontology terms  

### Required PROV-O Blocks

Each dataset must declare:

- `prov:wasDerivedFrom` → NASA L2/L3 product  
- `prov:generatedAtTime`  
- `prov:wasAttributedTo` → KFM ingestion pipeline  
- `prov:used` → QA masks, grid definitions, orbit metadata  

---

## 🛡️ 4. Governance & Sovereignty

Metadata **must include**:

- CARE label (`CARE-A` or `CARE-B`)  
- Sovereignty note (tribal land intersections)  
- H3 masking level (if generalization is applied)  
- `"kfm:mask_applied": true` where applicable  
- Provenance of masking decisions (review committee, rule version)

This ensures surface conditions & derivative interpretations never misrepresent  
sensitive Indigenous geographies.

Governance validation includes:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- Sovereignty rule engine  

---

## 🧪 5. Validation & QA

All metadata is validated using:

- **JSON Schema**  
- **SHACL** (shape constraints)  
- **Ontology conformance** (CIDOC, PROV-O, GeoSPARQL, OWL-Time)  
- **KFM-DCAT v11 compliance**  
- **Check against STAC Collections** for:
  - temporal range consistency  
  - provider alignment  
  - theme/keyword coherence  
- **CARE/H3 auditing**

QA logs appear under:

`docs/data/satellites/smap/qa/`

---

## 🔁 6. Integration + Lineage

Metadata feeds:

- STAC → DCAT crosswalk  
- Story Node v3 → Dataset relations  
- Focus Mode v3 → Environmental context reasoning  
- Multi-mission fusion (HydroGNSS, Mesonet, NOAA, ERA5)

Lineage flows:

```
NASA L2/L3 SMAP Product
 → Metadata extraction
 → DCAT/JSON-LD assembly
 → PROV-O derivation mapping
 → Sovereignty/CARE annotation
 → Registration in KFM catalogs
 → OpenLineage + Telemetry export
```

---

## 🔮 7. Uses Inside KFM

### Story Node v3  
- Entity-to-dataset linking  
- Environmental subgraph embedding  
- Temporal coherence  

### Focus Mode v3  
- Provenance verification  
- Environmental context summaries  
- Dataset relevance reasoning  

### Hydrology/Climate  
- Dataset indexing for ingestion chains  
- Provenance-backed fusion workflows  

### Archaeology  
- Sensitivity-aware environmental overlays  
- Vegetation/wetness change narratives  

### Data API  
- Dataset browsing  
- Thematic search (soil moisture, vegetation, drought, etc.)

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                     |
|--------:|------------|---------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete metadata README; emoji layout; DCAT/JSON-LD/PROV-O alignment; governance/H3 rules. |
| v10.3.2 | 2025-11-14 | Pre-v11 partial metadata outline.                                                           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂️ Satellite Catalog](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

