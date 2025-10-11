<div align="center">

# 📜 Kansas-Frontier-Matrix — Processed Text Data

`data/processed/text/`

**Mission:** Store and document all **cleaned, parsed, and structured text corpora** — OCR-corrected archives, NLP-derived entities,
and historical transcripts — forming the **linguistic foundation** for the Kansas-Frontier-Matrix (KFM) knowledge graph
and AI/ML enrichment pipelines.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/pre-commit.yml?label=Pre-Commit)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 🧭 Table of Contents

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

`data/processed/text/` contains **ETL-ready textual assets** derived from Kansas’s documentary heritage —
letters, treaties, newspapers, and field diaries — cleaned, tokenized, and semantically structured.

These records bridge the gap between **raw OCR outputs** (`data/raw/text/`)
and **AI-ready derivatives** (`data/derivatives/text/`), enabling:

* 📍 *Entity extraction*: people, places, tribes, events
* 🧭 *Temporal & spatial linking* to maps/timelines
* 🤖 *AI summarization & classification*
* 🕸️ *Knowledge-graph enrichment* (Neo4j · CIDOC CRM · OWL-Time)

All files are validated for **UTF-8 encoding**, **schema conformance**, and **checksum integrity** during CI.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── text/
        ├── ocr_cleaned_diaries_1850_1900.jsonl       # OCR-corrected diary transcripts
        ├── kansas_treaties_cleaned.jsonl             # Treaty transcripts (normalized & parsed)
        ├── newspapers_1854_1925_cleaned.jsonl        # Cleaned historical newspaper articles
        ├── nlp_entities_extracted.json               # Named entities (people, places, events)
        ├── term_frequencies_ks_press.csv             # Decadal word frequency stats
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

| Dataset                               | File                                  | Description                                                            | Source                    | Format |
| :------------------------------------ | :------------------------------------ | :--------------------------------------------------------------------- | :------------------------ | :----- |
| **Cleaned Diaries (1850 – 1900)**     | `ocr_cleaned_diaries_1850_1900.jsonl` | OCR-corrected diary entries from settlers and travelers                | Kansas Historical Society | JSONL  |
| **Treaty Transcripts**                | `kansas_treaties_cleaned.jsonl`       | Normalized treaty & land-cession texts with parsed tribe/date entities | Yale Avalon / Kappler     | JSONL  |
| **Historic Newspapers (1854 – 1925)** | `newspapers_1854_1925_cleaned.jsonl`  | OCR-cleaned Kansas articles from *Chronicling America*                 | LOC / KHS                 | JSONL  |
| **NLP Entities Extracted**            | `nlp_entities_extracted.json`         | spaCy-derived entities (Person, Place, Event, Date)                    | Derived                   | JSON   |
| **Term Frequencies (Press)**          | `term_frequencies_ks_press.csv`       | Word frequency & co-occurrence by decade                               | Derived                   | CSV    |

Each JSONL record holds:
`id`, `title`, `date`, `source`, `text`, `tokens`, `entities`.

---

## 🧩 Schema & Format

### JSONL Example

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

### CSV Example

```csv
term,decade,frequency,relative_freq
drought,1890,230,0.0018
railroad,1890,514,0.0040
```

---

## 🌐 STAC Metadata

Each text corpus is indexed within the **STAC catalog** to ensure full lineage and reuse.

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "newspapers_1854_1925_cleaned",
  "properties": {
    "title": "Kansas Newspapers (1854–1925) – Cleaned OCR Text",
    "datetime": "1925-01-01T00:00:00Z",
    "description": "OCR-corrected and cleaned historical newspaper text corpus derived from Chronicling America (Kansas subset).",
    "processing:software": "Python + spaCy + regex + jsonlines",
    "mcp_provenance": "sha256:a9b2de…",
    "derived_from": ["data/raw/text/newspapers_1854_1925_ocr.zip"],
    "license": "CC-BY 4.0"
  },
  "assets": {
    "data": { "href": "./newspapers_1854_1925_cleaned.jsonl", "type": "application/jsonl" }
  }
}
```

---

## ⚙️ Processing Workflow

```bash
# 1️⃣ OCR correction & cleaning
python tools/text/ocr_clean.py \
  --input data/raw/text/newspapers_1854_1925_ocr.zip \
  --output data/processed/text/newspapers_1854_1925_cleaned.jsonl

# 2️⃣ Tokenization & entity extraction
python tools/text/nlp_extract.py \
  --input data/processed/text/newspapers_1854_1925_cleaned.jsonl \
  --output data/processed/text/nlp_entities_extracted.json

# 3️⃣ Frequency analysis
python tools/text/term_stats.py \
  --input data/processed/text/newspapers_1854_1925_cleaned.jsonl \
  --output data/processed/text/term_frequencies_ks_press.csv
```

**All operations** run inside a containerized environment
(`spaCy · regex · jsonlines · pandas · UTF-8 validation`).

---

## 🔁 Reproducibility & Validation

| Check                 | Method                      | CI Target            |
| :-------------------- | :-------------------------- | :------------------- |
| **Integrity**         | SHA-256 hash per file       | `make validate-text` |
| **Schema Compliance** | STAC v1.0 + JSON Schema     | `make stac-validate` |
| **Encoding**          | UTF-8 enforced              | `pre-commit`         |
| **NER Quality**       | Random sample + metrics log | `make text-qa`       |

---

## 🧠 Contributing New Text Data

1. Add cleaned `.jsonl` or `.csv` to this folder.
2. Generate `.sha256` and metadata JSON under `metadata/`.
3. Include `DERIVATION.md` detailing source, preprocessing, and NLP model version.
4. Validate locally:

   ```bash
   make validate-text
   ```
5. Open a PR including:

   * Updated STAC metadata
   * Provenance / license details
   * Repro commands

**All submissions are auto-checked** via CI before merge.

---

## 🧮 Versioning & Changelog

| Field               | Value                                                                             |
| :------------------ | :-------------------------------------------------------------------------------- |
| **Current Version** | `v2.1.0`                                                                          |
| **Last Updated**    | 2025-10-11                                                                        |
| **Maintainer**      | @kfm-data                                                                         |
| **Change Type**     | ✳ Minor — Added explicit version block, reproducibility matrix, refined badge set |

**Changelog**

```md
## v2.1.0 — 2025-10-11
- Added per-document versioning block & changelog section  
- Updated badges to GitHub Actions shield variants  
- Included reproducibility matrix & container details  
- Optimized table formatting for GitHub rendering
## v2.0.0 — 2025-09-01
- Initial release of processed text data documentation
```

---

## 📖 References

* [Chronicling America](https://chroniclingamerica.loc.gov/)
* [Kansas Historical Society Archives](https://www.kshs.org/)
* [spaCy NLP Framework](https://spacy.io/)
* [JSON Lines Spec](https://jsonlines.org/)
* [GDAL / OGR](https://gdal.org/)
* [STAC 1.0 Spec](https://stacspec.org)
* [Master Coder Protocol (MCP)](../../../docs/standards/)

---

<div align="center">

> *“Every letter, law, and line of ink — these processed texts give Kansas’s past a searchable, structured voice.”*

</div>
