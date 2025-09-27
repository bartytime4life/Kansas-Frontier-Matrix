# `nlp/` — Natural Language Processing Layer

This module provides **text ingestion, parsing, and semantic enrichment** for the
**Kansas Geo Timeline** project.  
It transforms raw textual sources (newspapers, diaries, treaties, archaeology notes,
land deeds, oral histories, etc.) into **structured, time-aware metadata** that can be
linked to the geospatial and temporal layers.

---

## Design Goals

- **Normalize & Annotate** historical texts for alignment with spatial data.
- **Time Extraction**: detect explicit and implicit dates, ranges, and eras.
- **Entity Linking**: people, places, groups, and events → STAC/graph identifiers.
- **Vocabulary Expansion**: maintain a glossary of Kansas-frontier terms and variants.
- **Search & Discovery**: provide keyword, semantic, and timeline-aware search over
  ingested corpora.

---

## Directory Layout

```

src/kansas_geo_timeline/nlp/
├── **init**.py
├── base.py             # Abstract base for NLP pipelines (ETL style)
├── tokenizer.py        # Tokenization / sentence splitting
├── date_extractor.py   # Regex + ML for time expressions
├── entity_extractor.py # Named entities, place/people/org/event recognition
├── glossary.py         # Frontier-specific vocabulary expansion
├── linker.py           # Cross-link to STAC IDs, maps, and collections
├── pipeline.py         # Orchestration of all NLP steps
└── README.md           # This file

````

---

## Workflow

```mermaid
flowchart TD
  A["Raw Text Sources\n(data/raw/texts/*.txt, *.jsonl)"] --> B["NLP Pipeline\n(tokenize, dates, entities)"]
  B --> C["Structured Output\n(data/processed/text/*.jsonl)"]
  C --> D["STAC Items / Linked Data\n(stac/items/*.json)"]
  D --> E["Web Viewer Search + Timeline\n(web/config, UI overlays)"]
````

---

## Usage

### CLI (planned)

```bash
# Run full NLP pipeline on new diaries
python -m kansas_geo_timeline.nlp.pipeline \
    --input data/raw/texts/diaries_1860s.jsonl \
    --output data/processed/text/diaries_1860s.jsonl \
    --stac-dir stac/items/text
```

### Python API

```python
from kansas_geo_timeline.nlp.pipeline import NLPPipeline

nlp = NLPPipeline()
records, stac_items = nlp.run("data/raw/texts/letters_1850s.jsonl")
```

---

## Dependencies

* [`regex`](https://pypi.org/project/regex/) for date/era extraction
* [`spacy`](https://spacy.io/) for tokenization and NER
* [`dateparser`](https://dateparser.readthedocs.io/) for fuzzy historical dates
* [`pystac`](https://pystac.readthedocs.io/) for STAC item wiring
* [`jsonlines`](https://pypi.org/project/jsonlines/) for streaming I/O

All are declared in the root `pyproject.toml`.

---

## Notes

* Every processed text block should include:

  * **Original text** (normalized to UTF-8)
  * **Tokens / sentences**
  * **Extracted dates** (with confidence + normalized ISO ranges)
  * **Entities** (linked to KFM vocab or STAC IDs where possible)
  * **Provenance** (checksum + source reference)
* STAC items are created in `stac/items/text/` for easy browsing & linking.
* The module is designed to be **extensible**: new extractors can be added under `nlp/`
  and registered in `pipeline.py`.

---

✅ **Mission-grade principle**: All text entering this system must pass through this NLP layer
so that narrative + document data are aligned with geospatial/temporal records.

```
