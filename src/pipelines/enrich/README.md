<div align="center">

# 🧠 Kansas Frontier Matrix — AI & Data Enrichment Pipelines  
`src/pipelines/enrich/README.md`

**NLP · Geocoding · Entity Linking · Summarization · Correlation**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/pipelines/enrich/`** module performs **AI/ML-driven semantic enrichment** on processed datasets in the  
Kansas Frontier Matrix (KFM). It bridges the gap between raw, transformed data and the structured, linked  
knowledge graph by extracting, interpreting, and connecting entities across text, maps, and tabular data.  

The enrichment stage applies **Natural Language Processing (NLP)**, **geocoding**, **entity linking**, and **multi-source correlation**  
to produce intelligent metadata and relationships — forming the foundation of the Frontier Matrix knowledge graph.

---

## 🏗️ Role in the System

```mermaid
flowchart TD
    A["data/processed/<*.csv|.geojson|.tif>"] --> B["Enrichment Modules<br/>NLP · Geocoding · Linking · Summarization"]
    B --> C["Semantic Facts<br/>(entities, relationships, summaries)"]
    C --> D["Knowledge Graph (Neo4j)"]
    C --> E["Search Index / STAC Metadata"]
````

<!-- END OF MERMAID -->

This layer transforms **structured and unstructured data** into **knowledge-ready assets**, augmenting them with:

* 🧭 **Geospatial context** — place names → coordinates
* 👥 **Entity recognition** — detect people, organizations, events
* 🕰 **Temporal linking** — normalize dates and event timelines
* 🔗 **Cross-source connections** — match identical entities across datasets
* ✍️ **AI summaries** — generate concise overviews for map popups & entity panels

---

## 📂 Directory Layout

```
src/pipelines/enrich/
├── __init__.py
├── nlp_entities.py        # Named Entity Recognition & Text Tagging
├── summarizer.py          # AI summarization using Transformer models
├── entity_linker.py       # Fuzzy + contextual linking to graph nodes
├── correlate_sources.py   # Multi-source cross-validation of events
├── geocode_utils.py       # Reverse & forward geocoding (GNIS, OSM)
└── README.md              # (this file)
```

Each module can run standalone for testing, or be orchestrated via the global `make enrich` target.

---

## 🧩 Functional Overview

| Component                | Description                                                                                                   | Key Libraries                                         |
| :----------------------- | :------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------- |
| **nlp_entities.py**      | Extracts `PERSON`, `PLACE`, `DATE`, `EVENT` entities from text and attaches metadata.                         | `spaCy`, `regex`, `transformers`                      |
| **summarizer.py**        | Generates human-readable summaries from OCR’d text or document collections.                                   | `HuggingFace Transformers` (`BART`, `T5`)             |
| **entity_linker.py**     | Matches extracted entities to canonical graph nodes via fuzzy string and context scoring.                     | `fuzzywuzzy`, `sentence-transformers`, `neo4j-driver` |
| **correlate_sources.py** | Cross-validates facts from multiple sources (e.g. text + GIS + time series) to detect consensus or anomalies. | `pandas`, `scipy`, `networkx`                         |
| **geocode_utils.py**     | Converts named places to latitude/longitude via GNIS, Nominatim, or ArcGIS API.                               | `geopy`, `requests`                                   |

---

## 🧱 NLP Entity Extraction

### Named Entity Recognition (NER)

```python
import spacy
nlp = spacy.load("en_core_web_trf")

text = "In August 1867, a flood washed through the Arkansas River near Wichita."
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
```

Output:

```
August 1867  DATE
Arkansas River  GPE
Wichita  GPE
```

Entities are stored as structured dictionaries:

```json
{
  "entity": "Arkansas River",
  "type": "Place",
  "confidence": 0.98,
  "context": "flood event near Wichita",
  "source": "fema_floods_1867"
}
```

---

## 🌍 Geocoding & Location Normalization

* **Forward Geocoding**: Resolves place names → coordinates using **USGS GNIS** or **OpenStreetMap Nominatim** APIs.
* **Reverse Geocoding**: Enriches point data with county, watershed, or township metadata.
* **Output**: Adds `lat`, `lon`, and standardized `place_id` fields to entity dictionaries.

```python
from geopy.geocoders import Nominatim
geo = Nominatim(user_agent="kansas_frontier_matrix")
loc = geo.geocode("Fort Larned, Kansas")
print(loc.latitude, loc.longitude)
```

---

## 🧠 AI Summarization

Large Language Models (LLMs) generate concise, human-readable summaries from multi-page documents, diaries, or archival OCR text.

Example:

```python
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = open("data/processed/documents/diary_1867.txt").read()
print(summarizer(text, max_length=120, min_length=40, do_sample=False)[0]["summary_text"])
```

Example output:

> “In August 1867, settlers along the Arkansas River experienced catastrophic flooding. Many homes were lost, leading to federal disaster aid requests from Sedgwick County.”

These summaries are saved as `.summary.txt` and referenced in the STAC metadata for each document.

---

## 🔗 Entity Linking & Cross-Referencing

Entity linking aligns discovered entities to canonical graph nodes.
For instance, “Ft. Larned” → “Fort Larned (Place: Neo4j ID 112)” using a combination of fuzzy string match and contextual metadata.

```python
from fuzzywuzzy import process
matches = process.extractOne("Ft. Larned", ["Fort Larned", "Fort Scott", "Fort Riley"])
print(matches)
```

Output:

```
('Fort Larned', 96)
```

Each link includes:

* `match_score` (0–100)
* `context_overlap` (textual + temporal)
* `source_count` (how many datasets agree)

Low-confidence matches are flagged for human review through the admin interface.

---

## 🧮 Multi-Source Correlation

The **correlate_sources.py** module compares attributes across datasets to find convergent patterns:

* Confirmed event dates (e.g., flood date in text + NOAA rainfall + FEMA record)
* Spatial consistency (text mentions + geospatial layers)
* Statistical correlations (e.g., drought reports vs. water table levels)

It outputs a **correlation matrix** and confidence scores for each linked entity pair.

```python
import pandas as pd
corr = pd.read_csv("data/processed/correlation/flood_1867.csv")
corr.head()
```

---

## ⚙️ Example Workflow

```bash
# Run all enrichment tasks
make enrich

# Or run individually:
python src/pipelines/enrich/nlp_entities.py --input data/processed/texts/
python src/pipelines/enrich/geocode_utils.py --input data/processed/places.csv
python src/pipelines/enrich/entity_linker.py --input data/processed/entities.json
```

Each run appends to `logs/pipelines/enrich.log`:

```
[2025-10-05 14:20:05] nlp_entities | 132 documents processed | 5,412 entities extracted
[2025-10-05 14:22:14] geocode_utils | 5,391 place names resolved via GNIS
[2025-10-05 14:25:01] entity_linker | 1,044 new graph links | avg score=92%
```

---

## 🧾 Output Artifacts

| Artifact                 | Description                                     | Destination                            |
| :----------------------- | :---------------------------------------------- | :------------------------------------- |
| `*.entities.json`        | Extracted named entities with type + confidence | `data/processed/enriched/entities/`    |
| `*.summary.txt`          | AI-generated text summaries                     | `data/processed/enriched/summaries/`   |
| `*.links.json`           | Entity linking results (matches + scores)       | `data/processed/enriched/links/`       |
| `correlation_matrix.csv` | Multi-source validation scores                  | `data/processed/enriched/correlation/` |

---

## 🧩 Integration Flow

* **Upstream:** Consumes cleaned data from `transform/`
* **Downstream:** Sends enriched outputs to `load/` for graph insertion and STAC indexing
* **Automation:** `make enrich` executes all modules; logs, checkpoints, and SHA-256 hashes are created automatically.

---

## 📚 References

* [Kansas Frontier Matrix – AI System Developer Docs](../../../docs/ai-system.md)
* [Scientific Method & MCP Templates](../../../docs/templates/experiment.md)
* [CIDOC CRM & OWL-Time Ontologies](https://cidoc-crm.org/)
* [NASA-Grade Scientific Modeling Guide](../../../docs/standards/README.md)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Historical AI · Spatial Intelligence · Open Reproducibility*

</div>

