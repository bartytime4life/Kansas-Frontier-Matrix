<div align="center">

# 🧬 Kansas Frontier Matrix — NLP & Text Intelligence  
`src/nlp/README.md`

**Natural Language Processing · Entity Extraction · Semantic Linking**

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: Code](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)

</div>

---

## 🎯 Purpose

The **`src/nlp/`** package contains all **Natural Language Processing (NLP)** components that power  
the text understanding and semantic enrichment capabilities of the **Kansas Frontier Matrix (KFM)**.  

These modules process unstructured text sources — such as newspaper archives, diaries, treaties, and reports —  
to extract entities, summarize documents, identify relationships, and connect findings to the project’s **Knowledge Graph**.  

NLP is the backbone of **semantic data generation**, enabling the system to recognize how **people, places, and events**  
relate across historical documents and time.

---

## 🏗️ Role in the System

```mermaid
flowchart TD
    A["Text Sources<br/>OCR · Archives · Newspapers · Diaries"]
      --> B["NLP Pipeline<br/>spaCy · Transformers · Rules"]
      --> C["Entities & Summaries<br/>People · Places · Events · Dates"]
      --> D["Knowledge Graph<br/>Neo4j (CIDOC CRM)"]
      --> E["Frontend UI<br/>AI Summaries · Q&A · Search"]
````

<!-- END OF MERMAID -->

The NLP pipeline operates after document ingestion (`fetch/`) and transformation (`transform/`),
converting free text into structured knowledge through:

* **Named Entity Recognition (NER)**
* **Relation & Event Extraction**
* **Summarization**
* **Entity Linking**
* **Question Answering / AI Assistant (optional)**

---

## 📂 Directory Layout

```
src/nlp/
├── __init__.py
├── ner_model.py           # Custom spaCy model wrapper for NER and tagging
├── relation_extractor.py  # Event and relationship extraction from parsed docs
├── summarizer.py          # AI/ML summarization (BART / T5)
├── entity_linker.py       # Links text entities to Knowledge Graph nodes
├── qna_engine.py          # Experimental QA engine over the graph
└── README.md              # (this file)
```

---

## 🧠 NLP Pipeline Overview

### 1. Named Entity Recognition (NER)

The pipeline detects and classifies entities from raw text.
Entities are categorized into `PERSON`, `PLACE`, `EVENT`, `ORG`, and `DATE`.

```python
import spacy
nlp = spacy.load("en_core_web_trf")

text = "In August 1867, a flood swept across the Arkansas River near Fort Larned."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
```

Output:

```
August 1867 DATE  
Arkansas River GPE  
Fort Larned FACILITY
```

Entities are then standardized, geocoded (for `PLACE`), and inserted into the graph.

---

### 2. Relation & Event Extraction

Using rule-based and transformer-based parsing, the system detects contextual relationships
(e.g., *Person X → participated in → Event Y at → Place Z*).

Example pattern:

```
"John Smith commanded troops during the Battle of the Blue near Independence, Missouri."
```

Parsed relationships:

```json
{
  "person": "John Smith",
  "role": "commander",
  "event": "Battle of the Blue",
  "place": "Independence, Missouri",
  "date": "1864-10-22"
}
```

---

### 3. Summarization

Long-form texts (like diary entries or reports) are condensed using transformer-based summarizers.

```python
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(open("data/processed/texts/diary_1867.txt").read(), 
                     max_length=150, min_length=50, do_sample=False)
print(summary[0]['summary_text'])
```

Example output:

> “Settlers along the Arkansas River endured a devastating flood in August 1867, destroying homes and crops near Fort Larned.”

Summaries are stored as `.summary.txt` and linked to their source documents for fast map/timeline display.

---

### 4. Entity Linking

Entities discovered in text are matched to canonical graph nodes (People, Places, Events).

Techniques used:

* **Exact & Fuzzy Matching** (`Levenshtein`, `fuzzywuzzy`)
* **Contextual Similarity** (via `sentence-transformers`)
* **Graph-Aware Linking** (match based on temporal + geographic overlap)

```python
from fuzzywuzzy import process
match, score = process.extractOne("Ft. Larned", ["Fort Larned", "Fort Riley", "Fort Scott"])
print(match, score)
```

Output:

```
Fort Larned 96
```

Each link receives a confidence score and provenance (source document, timestamp, method).

---

### 5. Question Answering (Experimental)

The `qna_engine.py` module allows natural language queries over the Kansas Frontier knowledge base.

Example:

```bash
> Who lived near Fort Hays in 1870?
```

The engine:

1. Parses the question
2. Converts it to a graph query (Cypher or SPARQL)
3. Returns relevant entities and map highlights

---

## 🧾 Model Training and Fine-Tuning

The custom spaCy model (`ner_model.py`) is fine-tuned on historical Kansas datasets.

**Training Workflow:**

1. Collect labeled examples (`data/training/ner/`)
2. Use spaCy CLI for training:

   ```bash
   python -m spacy train config.cfg --paths.train ./data/training/ner/train.spacy --paths.dev ./data/training/ner/dev.spacy
   ```
3. Export to `models/ner_kansas/`
4. Version the model via Git LFS and register in `docs/model_card.md`

Entity types extended beyond default spaCy:

* `FORT` – Frontier military sites
* `TRIBAL_ENTITY` – Native Nations
* `RIVER` – Named hydrological features
* `DISASTER` – Droughts, floods, fires, tornadoes

---

## 🔍 Logging & Provenance

Every NLP operation logs metadata under `logs/nlp/`:

```
[2025-10-05 12:44:02] nlp_entities | 120 texts processed | 5,442 entities found
[2025-10-05 12:48:17] summarizer   | 30 summaries generated | avg length=142
[2025-10-05 12:53:01] linker       | 920 links created | avg confidence=91%
```

Each record includes:

* Source file or collection ID
* Model version (e.g. `ner_kansas_v0.3`)
* Confidence metrics
* Time of execution

---

## 🧰 Example CLI Workflows

```bash
# Run NER extraction on a folder of processed text files
python src/nlp/ner_model.py --input data/processed/texts/ --output data/processed/nlp/entities.json

# Summarize all newspaper articles from 1880–1900
python src/nlp/summarizer.py --input data/processed/newspapers/ --out data/processed/nlp/summaries/

# Link new entities to the graph
python src/nlp/entity_linker.py --input data/processed/nlp/entities.json

# Run QA engine (interactive mode)
python src/nlp/qna_engine.py
```

---

## 🧮 Outputs

| Output Type       | Description                                                | Destination                     |
| :---------------- | :--------------------------------------------------------- | :------------------------------ |
| `*.entities.json` | Structured entity lists (`Person`, `Place`, `Event`, etc.) | `data/processed/nlp/entities/`  |
| `*.summary.txt`   | AI-generated text summaries                                | `data/processed/nlp/summaries/` |
| `*.links.json`    | Entity linkage confidence records                          | `data/processed/nlp/links/`     |
| `nlp_metrics.log` | Model performance & confidence tracking                    | `logs/nlp/`                     |

---

## 📚 References

* [Kansas Frontier Matrix – AI System Developer Docs](../../docs/ai-system.md)
* [File & Data Architecture Guide](../../docs/architecture.md)
* [Scientific Modeling & Simulation (NASA-Grade Guide)](../../docs/standards/README.md)
* [CIDOC CRM & OWL-Time Ontologies](https://cidoc-crm.org/)

---

<div align="center">

**Kansas Frontier Matrix © 2025**
*Language · Meaning · Context — Preserving Kansas History Through AI*

</div>

