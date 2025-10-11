<div align="center">

# 📜 Kansas-Frontier-Matrix — Processed Text Data

`data/processed/text/`

**Mission:** Contain, document, and validate all **cleaned, parsed, and structured text corpora** —
OCR-corrected archives, NLP-derived entities, and historical transcripts — forming the **linguistic foundation**
for the KFM knowledge graph and AI/ML enrichment pipelines.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/pre-commit.yml?label=Pre-Commit)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)  [![License: Data](https://img.shields.io/badge/License-CC-BY%204.0-green)](../../../LICENSE)  [![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

### 🧭 Table of Contents

* [Overview](#overview)
* [Directory Layout](#directory-layout)
* [Core Text Datasets](#core-text-datasets)
* [Schema & Format](#schema--format)
* [STAC Metadata](#stac-metadata)
* [Processing Workflow](#processing-workflow)
* [Reproducibility & Validation](#reproducibility--validation)
* [Contributing New Text Data](#contributing-new-text-data)
* [Versioning & Changelog](#versioning--changelog)
* [References](#references)

---

## 🧾 Overview

`data/processed/text/` hosts **ETL-ready textual assets** from Kansas’s documentary heritage —
letters, treaties, newspapers, and diaries — all **cleaned**, **tokenized**, and **semantically structured**.

These bridge **raw OCR inputs** (`data/raw/text/`) with **AI-ready derivatives** (`data/derivatives/text/`), enabling:

* 📍 Entity extraction (people, places, tribes, events)
* 🧭 Temporal / spatial linking to maps & timelines
* 🤖 AI summarization and classification
* 🕸️ Knowledge-graph integration (Neo4j · CIDOC CRM · OWL-Time)

All files undergo **UTF-8**, **schema**, and **checksum** validation in CI.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── text/
        ├── ocr_cleaned_diaries_1850_1900.jsonl
        ├── kansas_treaties_cleaned.jsonl
        ├── newspapers_1854_1925_cleaned.jsonl
        ├── nlp_entities_extracted.json
        ├── term_frequencies_ks_press.csv
        ├── metadata/
        │   ├── ocr_cleaned_diaries_1850_1900.json
        │   ├── newspapers_1854_1925_cleaned.json
        │   └── nlp_entities_extracted.json
        ├── checksums/
        │   ├── ocr_cleaned_diaries_1850_1900.jsonl.sha256
        │   ├── newspapers_1854_1925_cleaned.jsonl.sha256
        │   └── nlp_entities_extracted.json.sha256
        └── README.md
```

---

## ✍️ Core Text Datasets

| Dataset                             | File                                  | Description                                             | Source                    | Format |
| :---------------------------------- | :------------------------------------ | :------------------------------------------------------ | :------------------------ | :----- |
| **Cleaned Diaries (1850–1900)**     | `ocr_cleaned_diaries_1850_1900.jsonl` | OCR-corrected settler diary entries                     | Kansas Historical Society | JSONL  |
| **Treaty Transcripts**              | `kansas_treaties_cleaned.jsonl`       | Normalized treaty texts with parsed tribe/date entities | Yale Avalon / Kappler     | JSONL  |
| **Historic Newspapers (1854–1925)** | `newspapers_1854_1925_cleaned.jsonl`  | Cleaned Kansas articles from *Chronicling America*      | LOC / KHS                 | JSONL  |
| **NLP Entities Extracted**          | `nlp_entities_extracted.json`         | spaCy-derived entities (Person, Place, Event, Date)     | Derived                   | JSON   |
| **Term Frequencies (Press)**        | `term_frequencies_ks_press.csv`       | Word frequency & co-occurrence by decade                | Derived                   | CSV    |

Each JSONL record includes `id`, `title`, `date`, `source`, `text`, `tokens`, `entities`.

---

## 🧩 Schema & Format

```json
{
  "id": "ks_news_1890_0132",
  "title": "Severe Drought in Western Kansas",
  "date": "1890-07-14",
  "source": "Topeka State Journal",
  "text": "The drought this season has affected the wheat crops severely...",
  "tokens": ["drought","season","affected","wheat","crops"],
  "entities": [
    {"type":"EVENT","text":"drought"},
    {"type":"PLACE","text":"Western Kansas"},
    {"type":"DATE","text":"1890"}
  ]
}
```

```csv
term,decade,frequency,relative_freq
drought,1890,230,0.0018
railroad,1890,514,0.0040
```

---

## 🌐 STAC Metadata

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "newspapers_1854_1925_cleaned",
  "properties": {
    "title": "Kansas Newspapers (1854–1925) – Cleaned OCR Text",
    "datetime": "1925-01-01T00:00:00Z",
    "description": "OCR-cleaned historical newspaper corpus from Chronicling America (Kansas subset).",
    "processing:software": "Python + spaCy + regex + jsonlines",
    "mcp_provenance": "sha256:a9b2de…",
    "derived_from": ["data/raw/text/newspapers_1854_1925_ocr.zip"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": {
      "href": "./newspapers_1854_1925_cleaned.jsonl",
      "type": "application/x-jsonlines"
    }
  }
}
```

---

## ⚙️ Processing Workflow

```bash
# 1️⃣ OCR cleaning
python tools/text/ocr_clean.py \
  --input data/raw/text/newspapers_1854_1925_ocr.zip \
  --output data/processed/text/newspapers_1854_1925_cleaned.jsonl

# 2️⃣ Tokenization & entity extraction
python tools/text/nlp_extract.py \
  --input data/processed/text/newspapers_1854_1925_cleaned.jsonl \
  --output data/processed/text/nlp_entities_extracted.json

# 3️⃣ Term frequency analysis
python tools/text/term_stats.py \
  --input data/processed/text/newspapers_1854_1925_cleaned.jsonl \
  --output data/processed/text/term_frequencies_ks_press.csv
```

> All stages run inside the **containerized NLP stack** (spaCy · pandas · regex · jsonlines).

---

## 🔁 Reproducibility & Validation

| Check                 | Method                        | CI Target            |
| :-------------------- | :---------------------------- | :------------------- |
| **Integrity**         | `.sha256` hash per file       | `make validate-text` |
| **Schema Compliance** | STAC v1.0 + JSON Schema       | `make stac-validate` |
| **Encoding**          | UTF-8 enforced via pre-commit | `pre-commit`         |
| **NER Quality**       | Sample precision/recall logs  | `make text-qa`       |

```bash
sha256sum -c checksums/*.sha256  
python -m json.tool metadata/*.json > /dev/null
```

---

## 🧠 Contributing New Text Data

1. Add cleaned `.jsonl` or `.csv`.
2. Create `metadata/<name>.json` with source, license, and processing notes.
3. Generate `.sha256` under `checksums/`.
4. Update STAC Item linking the asset.
5. Validate locally: `make validate-text && make stac-validate`.
6. Open PR including metadata, checksums, and repro commands.

*All submissions are CI-validated before merge.*

---

## 🧮 Versioning & Changelog

| Version  | Date       | Notes                                                                                                            |
| :------- | :--------- | :--------------------------------------------------------------------------------------------------------------- |
| **v2.3** | 2025-10-11 | Standardized formatting to match KFM processed-data grid and badge layout; refined divider rhythm and alignment. |
| **v2.2** | 2025-10-11 | Added lineage diagram, naming conventions, and quick verification commands; clarified STAC media type.           |
| **v2.1** | 2025-10-11 | Introduced per-document version block, reproducibility matrix, and container details.                            |
| **v2.0** | 2025-09-01 | Initial processed text data documentation with CI validation and STAC linkage.                                   |

---

## 📖 References

* [Chronicling America](https://chroniclingamerica.loc.gov/)
* [Kansas Historical Society](https://www.kshs.org/)
* [spaCy](https://spacy.io/) · [JSON Lines](https://jsonlines.org/) · [GDAL / OGR](https://gdal.org/)
* [STAC 1.0 Spec](https://stacspec.org) · [MCP Standards](../../../docs/standards/)

---

<div align="center">

> *“Every letter, law, and line of ink — these processed texts give Kansas’s past a searchable, structured voice.”*

</div>
