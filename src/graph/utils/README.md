---
title: "🧮 Kansas Frontier Matrix — Graph Utilities & Helper Modules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/graph/utils/README.md"
version: "v10.1.0"
last_updated: "2025-11-10"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.1.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.1.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
governance_ref: "../../../docs/standards/governance/DATA-GOVERNANCE.md"
telemetry_ref: "../../../releases/v10.1.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/src-graph-utils-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧮 **Kansas Frontier Matrix — Graph Utilities & Helper Modules**
`src/graph/utils/README.md`

**Purpose:**  
Document the **shared utility functions, helper scripts, and Cypher interaction classes** that power ingestion, analytics, and provenance tasks in the Neo4j knowledge graph.  
Implements standardized methods for session handling, checksum computation, graph validation, and FAIR+CARE-compliant data interactions.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blueviolet)](../../../docs/standards/)
[![FAIR+CARE Certified](https://img.shields.io/badge/FAIR%2BCARE-Diamond%E2%81%B9%20%C3%98%20Certified-gold)](../../../docs/standards/faircare-validation.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)
[![Neo4j Python](https://img.shields.io/badge/Driver-neo4j--python%205.x-lightgrey)]()
[![ISO 19115](https://img.shields.io/badge/ISO-19115%20Compliant-blue)]()

</div>

---

## 📘 Overview

The **Graph Utilities module** provides a robust toolkit for programmatic interaction with Neo4j and related metadata services.  
It serves as a bridge between the ETL, AI, and Governance pipelines by abstracting recurring operations such as:

- Opening and managing Neo4j database sessions.  
- Executing Cypher queries with validation and logging.  
- Computing and verifying checksums for data integrity.  
- Converting between STAC/DCAT metadata and graph nodes.  
- Interfacing with provenance systems (IPFS, Ethereum).  
- Supporting AI explainability and Focus Mode analytics.  

All helper functions follow **MCP reproducibility principles** — every function includes logging, checksum validation, and metadata recording to ensure full auditability.

---

## 🧩 Core Modules

| File | Purpose | Description |
|------|----------|-------------|
| **graph_helpers.py** | Neo4j interaction utilities | Provides session handling, transaction context management, and safe query execution. |
| **checksum_utils.py** | Data integrity utilities | Generates and validates SHA-256 checksums for all ingested and linked entities. |
| **metadata_bridge.py** | STAC/DCAT mapping | Translates dataset metadata into Neo4j nodes compliant with FAIR standards. |
| **geo_utils.py** | Spatial operations | Handles GeoJSON parsing, CRS validation, and spatial indexing (GeoSPARQL-compatible). |
| **logger.py** | Unified logging wrapper | Provides standardized logging with MCP-style format for audit and CI/CD telemetry. |

---

## ⚙️ Common Functions (graph_helpers.py)

| Function | Description |
|-----------|-------------|
| `get_session()` | Establishes a Neo4j session using environment credentials (URI, username, password). |
| `run_query(query: str, params: dict = None)` | Executes a Cypher query and returns results as list of dicts. |
| `load_cypher(file_path: str)` | Loads and executes Cypher scripts (schema creation, constraints). |
| `count_nodes(label: str)` | Returns count of all nodes with a given label (used in validation). |
| `create_index(label: str, field: str)` | Creates an index for a given property if not already existing. |
| `check_constraints()` | Validates all schema constraints and returns a compliance report. |

### Example — Query Execution
```python
from src.graph.utils.graph_helpers import get_session, run_query

with get_session() as session:
    result = run_query("MATCH (n:Event) RETURN count(n) AS total_events;")
    print(result[0]['total_events'])
```

---

## 🔐 Checksum Utilities

### Example — SHA-256 Hash Verification
```python
from src.graph.utils.checksum_utils import compute_checksum, verify_checksum

file_path = "data/processed/events_1850.json"
sha256 = compute_checksum(file_path)
is_valid = verify_checksum(file_path, sha256)
```

| Function | Description |
|-----------|-------------|
| `compute_checksum(path)` | Generates SHA-256 hash of any file or serialized object. |
| `verify_checksum(path, expected_hash)` | Compares computed checksum against stored reference. |
| `update_metadata_registry(entity_id, checksum)` | Logs hash values in `src/graph/metadata.json`. |

---

## 🌐 Metadata Bridge Utilities

The `metadata_bridge.py` module links dataset metadata (from STAC/DCAT catalogs) to Neo4j.

### Example — Convert STAC Item → Graph Node
```python
from src.graph.utils.metadata_bridge import stac_to_graph

node = stac_to_graph("data/stac/item_ks_soil_1967.json")
print(node)
# Output: {'id': 'soil_1967', 'type': 'Dataset', 'license': 'Public Domain'}
```

| Function | Description |
|-----------|-------------|
| `stac_to_graph(path)` | Parses a STAC Item and returns a Neo4j-compatible dict. |
| `dcat_to_graph(path)` | Parses a DCAT dataset and maps fields to graph attributes. |
| `validate_metadata_fields(metadata)` | Ensures all required FAIR+CARE metadata keys are present. |

---

## 🗺 Spatial Utilities

| Function | Description |
|-----------|-------------|
| `parse_geojson(file_path)` | Reads and validates GeoJSON geometries. |
| `validate_crs(geojson)` | Ensures spatial data uses EPSG:4326 unless otherwise defined. |
| `calculate_centroid(geometry)` | Computes centroid for visualization or clustering. |
| `geo_distance(coord1, coord2)` | Calculates geodesic distance (Haversine formula). |

### Example
```python
from src.graph.utils.geo_utils import calculate_centroid
centroid = calculate_centroid({"type": "Polygon", "coordinates": [...]})
```

---

## 🧮 Directory Layout

```plaintext
src/graph/utils/
├── README.md               # Documentation (this file)
├── graph_helpers.py        # Neo4j connection and Cypher utilities
├── checksum_utils.py       # Data integrity tools
├── metadata_bridge.py      # STAC/DCAT to Neo4j mapper
├── geo_utils.py            # Spatial utilities and GeoSPARQL compliance
└── logger.py               # MCP-compliant logging for all graph operations
```

---

## 🧪 Validation & Telemetry

| Metric | Description | Verified By |
|--------|--------------|-------------|
| **Query Latency (mean)** | Average runtime of Cypher operations | @kfm-ops |
| **Checksum Integrity** | Match rate between computed and stored hashes | @kfm-validation |
| **FAIR+CARE Metadata Coverage** | % of entities with complete metadata | @faircare-council |
| **Spatial CRS Compliance** | % of GeoJSONs with EPSG:4326 CRS | @kfm-geo |
| **Script Coverage** | % of functions with test cases in `tests/graph_utils/` | @kfm-ci |

Telemetry report → `../../../reports/audit/graph_utils_metrics.json`

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Graph Utilities & Helper Modules (v10.1.0).
Shared utility modules for Neo4j interaction, checksum validation, and FAIR+CARE metadata bridging in the Kansas Frontier Matrix knowledge graph.
```

---

## 🕰️ Version History

| Version | Date | Summary |
|----------|------|----------|
| **v10.1.0** | 2025-11-10 | Added spatial utilities; integrated STAC/DCAT metadata bridge; improved session handling for Neo4j v5.x. |
| **v10.0.0** | 2025-11-08 | Refactored checksum utilities; standardized logging under MCP telemetry schema. |
| **v9.7.0** | 2025-11-05 | Initial helper functions for graph operations, metadata validation, and constraint verification. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT License**  
*Reliable Utilities × FAIR+CARE Data Integrity × Provenance Consistency*  
[Back to Graph README](../README.md) · [Docs Portal](../../../docs/) · [Governance Ledger](../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

