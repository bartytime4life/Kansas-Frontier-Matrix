<div align="center">

# 📜 Kansas-Frontier-Matrix — Processed Text Data (`data/processed/text/`)

**Mission:** Contain all **cleaned, parsed, and structured text datasets** — OCR outputs, NLP-extracted entities,  
and historical document transcripts — serving as the linguistic foundation for Kansas Frontier Matrix’s  
knowledge graph and AI/ML enrichment pipelines.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.github/workflows/pre-commit.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Core Text Datasets](#core-text-datasets)
- [Schema & Format](#schema--format)
- [STAC Metadata](#stac-metadata)
- [Processing Workflow](#processing-workflow)
- [Reproducibility & Validation](#reproducibility--validation)
- [Contributing New Text Data](#contributing-new-text-data)
- [References](#references)

---

## 🧾 Overview

This directory stores **processed text datasets** — transcribed, cleaned, and tokenized content  
from Kansas’s historical archives, newspapers, treaties, letters, and reports.  

These text files represent the **intermediate stage** between raw OCR outputs in `data/raw/text/`  
and AI-ready derivatives in `data/derivatives/text/` (e.g., entity networks, summaries, NER datasets).  

They provide the linguistic and semantic backbone for:
- Named Entity Recognition (people, places, events)  
- Temporal and spatial reference extraction  
- AI-driven document summarization  
- Knowledge graph population and linking  

All processed texts are validated for structure, encoding (UTF-8), and schema compliance.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── text/
        ├── ocr_cleaned_diaries_1850_1900.jsonl       # OCR-corrected diary transcripts
        ├── kansas_treaties_cleaned.jsonl             # Treaty transcripts, normalized & parsed
        ├── newspapers_1854_1925_cleaned.jsonl        # OCR-corrected historical newspaper articles
        ├── nlp_entities_extracted.json               # NER-extracted entities (people, places, events)
        ├── term_frequencies_ks_press.csv             # Term frequencies from Kansas press archives
        ├── metadata/
        │   ├── ocr_cleaned_diaries_1850_1900.json
        │   ├── newspapers_1854_1925_cleaned.json
        │   └── nlp_entities_extracted.json
        ├── checksums/
        │   ├── ocr_cleaned_diaries_1850_1900.jsonl.sha256
        │   ├── newspapers_1854_1925_cleaned.jsonl.sha256
        │   └── nlp_entities_extracted.json.sha256
        └── README.md
````

---

## ✍️ Core Text Datasets

| Product                             | File                                  | Description                                                                 | Source                    | Format |
| ----------------------------------- | ------------------------------------- | --------------------------------------------------------------------------- | ------------------------- | ------ |
| **Cleaned Diaries (1850–1900)**     | `ocr_cleaned_diaries_1850_1900.jsonl` | OCR-corrected diary entries from settlers and travelers                     | Kansas Historical Society | JSONL  |
| **Treaty Transcripts**              | `kansas_treaties_cleaned.jsonl`       | Parsed treaties and land cessions text with normalized date and tribe names | Yale Avalon / Kappler     | JSONL  |
| **Historic Newspapers (1854–1925)** | `newspapers_1854_1925_cleaned.jsonl`  | OCR-corrected articles from Chronicling America                             | LOC / KHS                 | JSONL  |
| **NLP Entities Extracted**          | `nlp_entities_extracted.json`         | Named entities (Person, Place, Event, Date) extracted via spaCy             | Derived                   | JSON   |
| **Term Frequencies (Press)**        | `term_frequencies_ks_press.csv`       | Word frequency and co-occurrence stats by decade                            | Derived                   | CSV    |

Each JSONL document contains text metadata (`id`, `title`, `date`, `source`, `text`, `tokens`, `entities`).

---

## 🧩 Schema & Format

### JSONL (Line-Delimited JSON)

Each line represents one document:

```json
{
  "id": "ks_news_1890_0132",
  "title": "Severe Drought in Western Kansas",
  "date": "1890-07-14",
  "source": "Topeka State Journal",
  "text": "The drought this season has affected the wheat crops severely...",
  "tokens": ["drought", "season", "affected", "wheat", "crops"],
  "entities": [
    {"type": "EVENT", "text": "drought"},
    {"type": "PLACE", "text": "Western Kansas"},
    {"type": "DATE", "text": "1890"}
  ]
}
```

### CSV Format

Used for analytical outputs (term frequencies, sentiment summaries, etc.):

```csv
term,decade,frequency,relative_freq
drought,1890,230,0.0018
railroad,1890,514,0.0040
```

---

## 🌐 STAC Metadata

Every processed text corpus is indexed in the **STAC catalog** with complete provenance and
processing metadata. Example:

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
    "data": {
      "href": "./newspapers_1854_1925_cleaned.jsonl",
      "type": "application/jsonl"
    }
  }
}
```

---

## ⚙️ Processing Workflow

Text processing pipelines are implemented under `tools/text/` and executed via `Makefile`.
Key stages include:

```bash
# 1. OCR correction & cleaning
python tools/text/ocr_clean.py --input data/raw/text/newspapers_1854_1925_ocr.zip \
  --output data/processed/text/newspapers_1854_1925_cleaned.jsonl

# 2. Tokenization and entity extraction
python tools/text/nlp_extract.py --input data/processed/text/newspapers_1854_1925_cleaned.jsonl \
  --output data/processed/text/nlp_entities_extracted.json

# 3. Frequency analysis
python tools/text/term_stats.py --input data/processed/text/newspapers_1854_1925_cleaned.jsonl \
  --output data/processed/text/term_frequencies_ks_press.csv
```

All text is lowercased, de-noised, normalized (UTF-8), and filtered for relevance to Kansas.

---

## 🔁 Reproducibility & Validation

* **Checksums:** `.sha256` integrity hashes accompany each processed file.
* **STAC Validation:** Metadata verified against STAC 1.0 schema during CI/CD.
* **Makefile Targets:**

  * `make text` → runs text cleaning and entity extraction
  * `make validate-text` → verifies checksums and schema compliance
* **Containerized NLP:** All NLP and OCR cleaning runs in Dockerized Python (spaCy + jsonlines + regex).
* **Quality Checks:** Random sampling, token distribution review, and NER accuracy metrics logged.

---

## 🧠 Contributing New Text Data

1. Place new cleaned text files (`.jsonl` or `.csv`) here.
2. Add `.sha256` checksum and STAC metadata JSON under `metadata/`.
3. Include `DERIVATION.md` explaining:

   * data source and citation,
   * preprocessing and NLP steps,
   * language model and version used.
4. Validate:

   ```bash
   make validate-text
   ```
5. Submit a Pull Request including:

   * STAC metadata,
   * source citation and license,
   * processing method reference.

All contributions are automatically validated and indexed in the project catalog.

---

## 📖 References

* **Chronicling America:** [https://chroniclingamerica.loc.gov/](https://chroniclingamerica.loc.gov/)
* **Kansas Historical Society Archives:** [https://www.kshs.org/](https://www.kshs.org/)
* **spaCy NLP Framework:** [https://spacy.io/](https://spacy.io/)
* **jsonlines Format Spec:** [https://jsonlines.org/](https://jsonlines.org/)
* **GDAL / OGR for Metadata Links:** [https://gdal.org/](https://gdal.org/)
* **STAC Spec 1.0:** [https://stacspec.org](https://stacspec.org)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../docs/standards/)

---

<div align="center">

*“Every letter, law, and line of ink — these cleaned texts give voice to Kansas’s past in digital form.”*

</div>
```

