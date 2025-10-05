<div align="center">

# 🗄️ Kansas Frontier Matrix — Data Load & Integration Pipelines  
`src/pipelines/load/README.md`

**Graph Ingestion · STAC Indexing · Provenance Tracking**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/pipelines/load/`** directory contains the **final integration layer** of the **Kansas Frontier Matrix (KFM)**  
ETL system — responsible for loading processed and enriched data into the project’s  
**Knowledge Graph (Neo4j)** and **SpatioTemporal Asset Catalog (STAC)**.  

This layer transforms semantic data and geospatial outputs into a unified, queryable, and versioned structure.  
It serves as the bridge between the data pipelines and the **web application API**, ensuring all assets  
(map layers, events, entities, and relationships) are properly indexed, timestamped, and linked with provenance.

---

## 🏗️ Pipeline Role in the System

```mermaid
flowchart TD
    A["data/processed/<files>"] --> B["Enrichment Outputs<br/>entities · links · summaries"]
    B --> C["Load Layer<br/>Neo4j Graph + STAC Index"]
    C --> D["Neo4j Knowledge Graph<br/>CIDOC CRM · OWL-Time"]
    C --> E["data/stac/catalog.json<br/>collections · items · assets"]
    D --> F["API Layer (FastAPI/GraphQL)"]
    E --> F
    F --> G["Frontend Timeline + Map (React/MapLibre)"]
````

<!-- END OF MERMAID -->

This stage consolidates all processed data into **two master repositories of truth**:

* 🧭 **Knowledge Graph** → links people, places, events, and documents semantically
* 🗺 **STAC Catalog** → indexes geospatial and temporal assets for visualization

---

## 📂 Directory Layout

```
src/pipelines/load/
├── __init__.py
├── stac_writer.py        # Build and update STAC Collections & Items
├── graph_loader.py       # Load entities and relationships into Neo4j
├── checksum_utils.py     # Verify data integrity with SHA-256 hashes
├── provenance_logger.py  # Create detailed provenance records
├── data_register.py      # Update registry of datasets and schema mappings
└── README.md             # (this file)
```

---

## 🧱 Components Overview

| Module                   | Function                                                                                                                                           | Key Tools                            |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| **graph_loader.py**      | Inserts nodes (People, Places, Events, Documents) and relationships (`OCCURRED_AT`, `MENTIONS`, `PARTICIPATED_IN`) into the Neo4j knowledge graph. | `neo4j-driver`, `pandas`, `networkx` |
| **stac_writer.py**       | Generates STAC-compliant JSON for processed layers (COG, GeoJSON, CSV).                                                                            | `pystac`, `jsonschema`               |
| **checksum_utils.py**    | Validates SHA-256 checksums for reproducibility and data lineage.                                                                                  | `hashlib`, `os`, `json`              |
| **provenance_logger.py** | Appends data lineage info to a persistent provenance log.                                                                                          | `logging`, `datetime`                |
| **data_register.py**     | Maintains registry of all data collections and schema mappings.                                                                                    | `pandas`, `yaml`                     |

---

## ⚙️ Graph Loading Workflow

1. **Initialize Neo4j connection**

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
```

2. **Create or update entity nodes**

```python
def create_place(tx, name, lat, lon):
    tx.run("""
        MERGE (p:Place {name: $name})
        SET p.latitude = $lat, p.longitude = $lon
    """, name=name, lat=lat, lon=lon)
```

3. **Link relationships**

```python
def link_event_place(tx, event_id, place_id):
    tx.run("""
        MATCH (e:Event {id: $event_id}), (p:Place {id: $place_id})
        MERGE (e)-[:OCCURRED_AT]->(p)
    """, event_id=event_id, place_id=place_id)
```

4. **Batch ingestion**

All graph insertions use **transaction batching** for efficiency.
Example:

```bash
python src/pipelines/load/graph_loader.py --input data/processed/enriched/entities.json --batch 500
```

---

## 🗺️ STAC Catalog Integration

The **STAC (SpatioTemporal Asset Catalog)** structure enables standardized geospatial metadata indexing.

### Example STAC Item (`data/stac/items/ks_1m_dem_2018_2020.json`)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "ks_1m_dem_2018_2020",
  "properties": {
    "title": "Kansas 1m Digital Elevation Model (2018–2020)",
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "providers": [{"name": "USGS 3DEP", "roles": ["producer", "licensor"]}]
  },
  "assets": {
    "cog": {
      "href": "https://example.com/ks_1m_dem_2018_2020.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data"]
    }
  },
  "geometry": {"type": "Polygon", "coordinates": [[[...]]]},
  "bbox": [-102.05, 36.99, -94.61, 40.00]
}
```

### Auto-generation

The loader automatically:

* Creates new **Items** for each dataset in `data/processed/`
* Updates **Collections** when new datasets are added
* Verifies compliance with `stac-spec` via `jsonschema`
* Adds provenance (source URL, checksum, process timestamp)

Run:

```bash
python src/pipelines/load/stac_writer.py --input data/processed/ --output data/stac/
```

---

## 🔒 Provenance & Checksum Tracking

To ensure reproducibility and scientific integrity:

* Each asset and JSON file includes a `.sha256` checksum file
* The **provenance log** (`logs/pipelines/load.log`) records:

  * Source path and license
  * Generation timestamp
  * STAC item or Neo4j node ID
  * Validation result

Example:

```
[2025-10-05 13:50:44] graph_loader | Loaded 4,392 nodes | 12,871 relationships | OK
[2025-10-05 13:55:21] stac_writer | 33 new STAC Items generated | OK
```

---

## 🔁 Integration Flow

* **Upstream:** Consumes processed and enriched outputs from `transform/` and `enrich/`
* **Downstream:** Feeds the **API layer (FastAPI/GraphQL)** and **frontend map/timeline**
* **Automation:** `make load` runs the full integration workflow, validating graph integrity and STAC metadata

---

## 🧾 Example Workflow

```bash
# Run all load operations (graph + STAC)
make load

# Load enriched entities into Neo4j
python src/pipelines/load/graph_loader.py --input data/processed/enriched/entities.json

# Validate and regenerate STAC catalog
python src/pipelines/load/stac_writer.py --input data/processed/ --output data/stac/

# Verify checksums
python src/pipelines/load/checksum_utils.py --verify data/processed/
```

---

## 📊 Validation & Quality Control

| Validation Type         | Description                                                           | Tool                   |
| :---------------------- | :-------------------------------------------------------------------- | :--------------------- |
| Graph Integrity         | Ensures valid node relationships (no orphaned or duplicate entities). | `Cypher`, `networkx`   |
| STAC Schema             | Confirms all metadata matches STAC 1.0.0 specification.               | `jsonschema`           |
| Checksums               | Validates all `.sha256` signatures before ingestion.                  | `hashlib`              |
| Provenance Completeness | Verifies every record links to at least one source manifest.          | `provenance_logger.py` |

---

## 📚 References

* [Kansas Frontier Matrix — File & Data Architecture](../../../docs/architecture.md)
* [AI System Developer Documentation](../../../docs/ai-system.md)
* [SpatioTemporal Asset Catalog (STAC) Spec 1.0.0](https://stacspec.org/)
* [CIDOC CRM & OWL-Time Ontologies](https://cidoc-crm.org/)
* [Scientific Method & MCP Templates](../../../docs/templates/experiment.md)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Data Provenance · Knowledge Graphs · Open Reproducibility*

</div>
