# `graph/` — Knowledge Graph & Linking Layer

This module provides the **graph representation** of the **Kansas Geo Timeline**.  
It unifies **people, places, events, and documents** into a **temporal-spatial knowledge graph** that can be queried, visualized, and linked to STAC + NLP outputs.

---

## Design Goals

- **Unified representation**: Nodes for people, places, groups, documents, treaties, trails, events.
- **Temporal dimension**: Every node and edge has start/end dates (if known).
- **Spatial grounding**: Place nodes carry geometries (GeoJSON, bbox) and can be tied to layers.
- **Traceability**: Edges carry provenance (checksums, source refs).
- **Interoperability**: Expose data as JSON-LD / RDF if needed for external tools.
- **Visualization**: Graph data feeds into timeline UIs and map overlays.

---

## Directory Layout

```

src/kansas_geo_timeline/graph/
├── **init**.py
├── base.py           # Core node/edge models and GraphError
├── builder.py        # Ingest STAC/NLP records into graph form
├── query.py          # Query helpers (by time, type, keyword)
├── export.py         # Serialize to JSON-LD, GraphML, Neo4j CSVs
├── schema.py         # Canonical node/edge schema definitions
└── README.md         # This file

````

---

## Workflow

```mermaid
flowchart TD
  A["NLP Output\n(data/processed/text/*.jsonl)"] --> B["Graph Builder\n(builder.py)"]
  A2["STAC Items\n(stac/items/*.json)"] --> B
  B --> C["Graph Store\n(data/processed/graph/*.json)"]
  C --> D["Graph Queries\n(query.py, export.py)"]
  D --> E["Visualizations\n(web viewer overlays,\nnetwork diagrams)"]
````

---

## Usage

### Python API

```python
from kansas_geo_timeline.graph.builder import GraphBuilder
from kansas_geo_timeline.graph.query import GraphQuery

builder = GraphBuilder()
graph = builder.from_files(
    stac_dir="stac/items/",
    nlp_jsonl="data/processed/text/diaries.jsonl"
)

# Query by entity type
q = GraphQuery(graph)
forts = q.nodes_by_type("Fort")
```

### Command Line (planned)

```bash
python -m kansas_geo_timeline.graph.builder \
    --stac stac/items \
    --nlp data/processed/text/diaries.jsonl \
    --out data/processed/graph/diaries_graph.json
```

---

## Dependencies

* [`networkx`](https://networkx.org/) — in-memory graph structures
* [`pystac`](https://pystac.readthedocs.io/) — parsing STAC items
* [`jsonlines`](https://pypi.org/project/jsonlines/) — NLP JSONL streaming
* [`rdflib`](https://rdflib.readthedocs.io/) — (optional) RDF/JSON-LD exports

All declared in the root `pyproject.toml`.

---

## Notes

* Each **node** must include:

  * `id` (stable, prefixed e.g. `kfm:fort:larned`)
  * `type` (Person, Place, Event, Document, Group, …)
  * `labels` (human-readable names, aliases)
  * `time` (start/end if known)
  * `geometry` (if spatial)
* Each **edge** must include:

  * `source`, `target`
  * `relation` (e.g. *located_in*, *signed*, *traveled*, *mentions*)
  * `provenance` (checksum + source)
* Graph artifacts live under `data/processed/graph/` and are versioned like other processed outputs.

---

✅ **Mission-grade principle**: All higher-level queries, narratives, and visualizations are driven from this graph layer.
It is the **backbone** connecting **raw sources → NLP → STAC → maps/timelines**.

```
