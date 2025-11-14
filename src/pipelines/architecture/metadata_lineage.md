---
title: "🧬 Kansas Frontier Matrix — Metadata & Lineage Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/metadata_lineage.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipeline-lineage-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧬 **Kansas Frontier Matrix — Metadata & Lineage Architecture**  
`src/pipelines/architecture/metadata_lineage.md`

**Purpose:**  
Define the **metadata, provenance, and lineage system** that governs every KFM pipeline (ETL, AI, geospatial, metadata, Story Nodes, STAC/DCAT publishing).  
This document specifies how **PROV-O**, **CIDOC-CRM**, **STAC**, **DCAT**, and **FAIR+CARE** metadata integrate to deliver **verifiable, reproducible, ethically governed lineage** across the entire Kansas Frontier Matrix.

</div>

---

## 📘 Overview

Metadata and lineage are **first-class citizens** in KFM.  
Every transformation, dataset, Story Node, AI inference, geospatial asset, or document ingestion must be:

- **Traceable** → exact inputs, parameters, tools, seeds  
- **Reconstructable** → deterministic reproduction  
- **Governed** → FAIR+CARE semantics (CARE labels, sovereignty, ethical flags)  
- **Provable** → PROV-O / CIDOC structured lineage  
- **Publishable** → STAC/DCAT compliant  
- **Auditable** → Governance ledger entries  
- **Telemetry-linked** → energy, CO₂e, runtime, validation results  

This architecture ensures KFM data remains **archives-grade**, **scientifically valid**, and **ethically compliant**.

---

## 🗂️ Directory Structure

~~~~~text
src/pipelines/architecture/
├── metadata_lineage.md       # This file
├── validation_standards.md
├── reliable-pipelines.md
├── telemetry_spec.md
├── governance_contracts.md
└── pipeline_patterns.md
~~~~~

---

## 🧩 Metadata & Lineage Pipeline (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Pipeline Start<br/>extract · transform · load"] --> B["Metadata Extractor"]
  B --> C["Lineage Engine<br/>PROV-O · CIDOC CRM"]
  C --> D["STAC/DCAT Builder"]
  D --> E["Integrity Layer<br/>Checksums · Hashes"]
  E --> F["Telemetry Layer<br/>runtime · energy · CO₂e · CARE"]
  F --> G["Governance Ledger<br/>Append-only"]
~~~~~

---

## 🧬 1. Metadata Standards Required

All pipeline outputs must adhere to:

### ✔ STAC 1.0 (Items + Collections)
Required fields for every STAC Item:

| Field | Required |
|-------|---------|
| `id` | ✔ |
| `type` | ✔ |
| `assets` | ✔ |
| `bbox` | ✔ |
| `geometry` | ✔ |
| `properties.datetime` | ✔ |
| `kfm:provenance` | ✔ |
| `kfm:care_label` | ✔ |

### ✔ DCAT 3.0
Required for dataset-level publishing:

- `dct:title`  
- `dct:description`  
- `dct:spatial`  
- `dct:temporal`  
- `dct:provenance`  
- `dct:license`

### ✔ PROV-O (W3C Provenance Ontology)
Used for lineage modeling.

Entities:
- `prov:Entity`  
- `prov:Activity`  
- `prov:Agent`

Relations:
- `prov:wasDerivedFrom`  
- `prov:used`  
- `prov:wasGeneratedBy`

### ✔ CIDOC-CRM (ISO 21127)
Required for cultural, historical, archival datasets.

Examples:
- `E31 Document`  
- `E53 Place`  
- `E5 Event`  
- `E21 Person`  
- `E52 Time-Span`

---

## 🧩 2. Lineage Record Requirements

Every pipeline must emit a **lineage record** describing:

| Field | Description |
|-------|-------------|
| `source_ids` | STAC/DCAT IDs for all input datasets |
| `transformations` | List of pipeline steps, tools, config parameters |
| `software_agents` | Versions of GDAL, spaCy, transformers, Python, etc. |
| `generated_assets` | IDs of STAC Items, Neo4j nodes, GeoParquet files |
| `checksums` | sha256 or blake3 for every artifact |
| `care_label` | public / sensitive / restricted |
| `sensitivity_notes` | if restricted or sensitive |
| `geo_masking` | H3/fuzzing applied? |
| `temporal_alignment` | OWL-Time intervals produced |
| `graph_nodes_created` | Entities/relations added to Neo4j |
| `model_versions` | Relevant ML model versions used |
| `provenance_model` | PROV-O or CIDOC record summary |

---

## 🧬 3. Lineage JSON Schema (Required v10.3)

~~~~~json
{
  "id": "string",
  "pipeline_id": "string",
  "dataset_id": "string",
  "source_ids": ["string"],
  "transformations": ["string"],
  "software_agents": {
    "python": "3.x",
    "gdal": "3.12.0",
    "spacy": "3.x",
    "transformer_model": "focus-transformer-v2.4"
  },
  "generated_assets": ["string"],
  "checksums": {
    "input": ["sha256:..."],
    "output": ["sha256:..."]
  },
  "care_label": "public",
  "geo_masking": {
    "h3_level": 7,
    "fuzzing_meters": 350
  },
  "temporal_alignment": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  },
  "graph_nodes_created": 213,
  "model_versions": ["focus-v2.4"],
  "provenance_model": "PROV-O",
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~~

---

## 🧠 4. Metadata Generation Flow

### Step 1 — Extract Metadata
- Pull STAC headers  
- Ingest DCAT descriptors  
- Identify document metadata (KHS, treaty archives, NOAA station metadata)

### Step 2 — Build Lineage Chain
- Map processes to PROV-O activities  
- Represent entities with stable identifiers  
- Append CARE flags and governance notes  

### Step 3 — Validate Metadata
- Schema checks (JSON Schema, Pydantic)  
- STAC/DCAT integrity  
- CARE & sovereignty classification  

### Step 4 — Produce STAC/DCAT Records
- Build STAC Items for each output artifact  
- Maintain version semantics (v10.x Items)  

### Step 5 — Emit Lineage Logs
- Written to `data/reports/audit/`  
- Included in per-release `focus-telemetry.json`  

---

## 🛡 5. FAIR+CARE Integration

Lineage must encode:

| FAIR Principle | Implementation |
|----------------|----------------|
| Findable | Stable STAC/DCAT IDs, searchable lineage logs |
| Accessible | Open metadata formats (JSON-LD, STAC) |
| Interoperable | PROV-O, CIDOC, STAC, DCAT |
| Reusable | Versioned metadata & checksum chains |

| CARE Principle | Enforcement |
|----------------|-------------|
| Collective Benefit | Clear contextualization of data lineage |
| Authority to Control | Native sovereignty & consent metadata |
| Responsibility | Complete attribution & contextual ethics |
| Ethics | Mask sensitive coordinates or attributes |

---

## 🛰️ 6. Lineage in Telemetry

Telemetry logs include:

- `generated_checksums`  
- `care_label`  
- `sensitivity_conflicts`  
- `provenance_depth`  
- `source_ids`  
- `transformer_model version` (if AI involved)

Stored in:

```
../../../../releases/v10.3.0/focus-telemetry.json
```

---

## 🧾 7. Example Lineage Entry (v10.3.1)

~~~~~json
{
  "pipeline_id": "etl_prism_climate_v10.3.1",
  "source_ids": ["prism_daily_ks_1950_2024"],
  "transformations": ["download", "netcdf_to_cog", "temporal_align", "stac_item_build"],
  "software_agents": {
    "python": "3.11.5",
    "gdal": "3.12.0",
    "spacy": "3.7.3"
  },
  "generated_assets": ["prism_2024_stac_item"],
  "checksums": {
    "input": ["sha256:001abc..."],
    "output": ["sha256:884def..."]
  },
  "care_label": "public",
  "geo_masking": null,
  "temporal_alignment": {
    "start": "1950-01-01",
    "end": "2024-12-31"
  },
  "graph_nodes_created": 0,
  "model_versions": [],
  "provenance_model": "PROV-O",
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Lineage v3 model finalized for KFM v10.3; added CARE sovereign metadata & CIDOC expansion. |
| v10.2.2 | 2025-11-12 | Pipeline Architecture Team | Initial lineage architecture with PROV-O/STAC integration. |

---

<div align="center">

**Kansas Frontier Matrix — Metadata & Lineage Architecture**  
Traceable Data × Ethical Provenance × Scientific Reproducibility  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Pipeline Architecture](./README.md)

</div>