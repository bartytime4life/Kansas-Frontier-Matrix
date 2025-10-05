<div align="center">

# 🕸️ Kansas Frontier Matrix — Knowledge Graph & Semantic Layer  
`src/graph/README.md`

**Neo4j · CIDOC CRM · OWL-Time · Provenance Reasoning**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/graph/`** directory contains the **Knowledge Graph engine** of the **Kansas Frontier Matrix (KFM)** —  
a semantic network that interconnects *people, places, events, documents, and artifacts* across time and space.  

The knowledge graph enables deep, queryable insight into Kansas history by combining **AI/ML-enriched data**,  
**ontological modeling**, and **graph reasoning** built on open cultural heritage standards like **CIDOC CRM**  
and **OWL-Time**.  

This layer transforms raw and enriched data into a **linked data ecosystem**, forming the semantic core of the project.

---

## 🧩 Role in the System

```mermaid
flowchart TD
    A["data/enriched/entities + links"] --> B["graph_loader.py<br/>Neo4j ingestion"]
    B --> C["Neo4j Knowledge Graph<br/>CIDOC CRM + OWL-Time schema"]
    C --> D["API Layer (FastAPI / GraphQL)<br/>/events /places /people endpoints"]
    D --> E["Frontend Map + Timeline<br/>semantic queries + AI summaries"]
````

<!-- END OF MERMAID -->

The Knowledge Graph is both the **backbone of semantic interoperability**
and the **query layer powering the interactive Kansas timeline and map.**

---

## 📂 Directory Layout

```
src/graph/
├── __init__.py
├── graph_schema.py      # CIDOC CRM + OWL-Time schema definitions
├── neo4j_connection.py  # Connection utilities for Neo4j
├── graph_loader.py      # ETL loader for nodes & relationships
├── graph_queries.py     # Standardized Cypher query library
├── reasoner.py          # Rule-based inference engine
├── graph_export.py      # Export graph to JSON-LD, RDF, or TTL
└── README.md            # (this file)
```

Each module can be run standalone or invoked as part of the **`make load`** pipeline.

---

## 🧱 Core Entities and Relationships

The Kansas Frontier Matrix graph uses a minimal, extensible ontology inspired by **CIDOC CRM**
and **W3C OWL-Time** to maintain compatibility with historical, archaeological, and GIS datasets.

### 🔹 Primary Node Types

| Label            | Description                                                      | Example                                       |
| :--------------- | :--------------------------------------------------------------- | :-------------------------------------------- |
| **Person**       | Historical individuals, settlers, tribal leaders, soldiers, etc. | `("John Smith", born 1832)`                   |
| **Place**        | Towns, forts, rivers, counties, natural landmarks                | `("Fort Larned", lat=-99.13, lon=38.19)`      |
| **Event**        | Battles, treaties, disasters, migrations, settlements            | `("Battle of Solomon Fork", date=1857-07-29)` |
| **Document**     | Letters, newspaper articles, maps, diaries                       | `("Kansas Tribune, July 1856")`               |
| **Organization** | Tribal nations, government offices, railroads                    | `("Union Pacific Railroad")`                  |

### 🔸 Relationship Types

| Relation          | Description                                      | Example                                |
| :---------------- | :----------------------------------------------- | :------------------------------------- |
| `OCCURRED_AT`     | Event took place at a Place                      | `(Event)-[:OCCURRED_AT]->(Place)`      |
| `PARTICIPATED_IN` | Person or Organization involved in an Event      | `(Person)-[:PARTICIPATED_IN]->(Event)` |
| `MENTIONS`        | Document references an entity                    | `(Document)-[:MENTIONS]->(Event)`      |
| `LOCATED_IN`      | Place belongs to a region or administrative area | `(Place)-[:LOCATED_IN]->(County)`      |
| `HAS_SOURCE`      | Node derived from a dataset or archive           | `(Entity)-[:HAS_SOURCE]->(Dataset)`    |
| `SIMILAR_TO`      | Semantic similarity between entities (AI/NLP)    | `(Event)-[:SIMILAR_TO]->(Event)`       |

---

## 🧮 Graph Schema Definition

Schema definitions are declared in **`graph_schema.py`**,
combining **Neo4j label constraints**, **indexing**, and **ontology mapping**.

```python
SCHEMA = {
    "labels": ["Person", "Place", "Event", "Document", "Organization"],
    "relationships": [
        "OCCURRED_AT", "PARTICIPATED_IN", "MENTIONS",
        "LOCATED_IN", "HAS_SOURCE", "SIMILAR_TO"
    ],
    "indexes": [
        ("Person", "id"), ("Place", "name"), ("Event", "id"), ("Document", "id")
    ]
}
```

CIDOC CRM classes and OWL-Time properties are mirrored for interoperability:

```python
CIDOC_MAP = {
    "E21_Person": "Person",
    "E53_Place": "Place",
    "E5_Event": "Event",
    "E31_Document": "Document",
    "E39_Actor": "Organization"
}
OWL_TIME_MAP = {
    "hasBeginning": "start_date",
    "hasEnd": "end_date",
    "intervalDuring": "temporal_overlap"
}
```

---

## 🔌 Connecting to Neo4j

Neo4j is the primary graph engine. Connection details are stored in `.env` or a config file.

```python
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    uri="bolt://localhost:7687",
    auth=("neo4j", "password")
)
```

Query example:

```python
with driver.session() as session:
    result = session.run("""
        MATCH (e:Event)-[:OCCURRED_AT]->(p:Place)
        RETURN e.title AS event, p.name AS place
        ORDER BY e.start_date LIMIT 10
    """)
    for record in result:
        print(record["event"], "→", record["place"])
```

---

## 🧠 Rule-Based Reasoning Engine

The **`reasoner.py`** module performs lightweight inferencing over the graph:
it can derive new facts based on known relationships, temporal overlap, or geographic proximity.

Example rule (in Python pseudocode):

```python
# If an Event occurred within a Place that is in a County,
# infer the event also OCCURRED_IN that County.
def infer_county_events(tx):
    tx.run("""
        MATCH (e:Event)-[:OCCURRED_AT]->(p:Place)-[:LOCATED_IN]->(c:County)
        MERGE (e)-[:OCCURRED_IN]->(c)
    """)
```

Rules like these extend implicit connections to support **timeline queries** and **regional aggregations**.

---

## 🧾 Export and Interoperability

The **graph_export.py** module allows exporting the Neo4j graph to multiple open formats:

| Format           | Description                                               | Use Case                                   |
| :--------------- | :-------------------------------------------------------- | :----------------------------------------- |
| **JSON-LD**      | JSON Linked Data compatible with schema.org and CIDOC CRM | For semantic web interoperability          |
| **RDF/XML**      | RDF triples for SPARQL endpoints or external ingestion    | For integration with heritage repositories |
| **TTL (Turtle)** | Compact human-readable RDF syntax                         | For ontology debugging and validation      |

Run:

```bash
python src/graph/graph_export.py --format jsonld --output data/export/graph.jsonld
```

---

## 🧩 Integration Flow

* **Upstream:** Consumes enriched data (`data/processed/enriched/entities.json`, `links.json`)
* **Downstream:** Powers the FastAPI/GraphQL endpoints used by the **web map & timeline UI**
* **Automation:** Triggered via `make load` or `make graph`

---

## 🧰 Example Workflow

```bash
# Initialize graph schema and indexes
python src/graph/graph_schema.py --init

# Load enriched entities and relationships
python src/graph/graph_loader.py --input data/processed/enriched/entities.json

# Run inference engine to expand relationships
python src/graph/reasoner.py

# Export graph for sharing
python src/graph/graph_export.py --format ttl
```

Example log (`logs/pipelines/graph.log`):

```
[2025-10-05 15:42:09] graph_loader | 12,345 nodes | 47,201 relationships | OK
[2025-10-05 15:44:21] reasoner | 682 inferred relationships | OK
[2025-10-05 15:46:11] export | graph.ttl (4.2MB) written successfully
```

---

## 📚 References

* [Kansas Frontier Matrix – AI System Developer Documentation](../../docs/ai-system.md)
* [File & Data Architecture Guide](../../docs/architecture.md)
* [CIDOC CRM Specification](https://cidoc-crm.org/)
* [W3C OWL-Time Ontology](https://www.w3.org/TR/owl-time/)
* [STAC Metadata Reference](https://stacspec.org/)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Linked Knowledge · Semantic History · Open Reproducibility*

</div>

