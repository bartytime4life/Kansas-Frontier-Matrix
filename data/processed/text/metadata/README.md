<div align="center">

# 📜 Kansas-Frontier-Matrix — Processed Text Metadata (`data/processed/text/metadata/`)

**Mission:** Maintain **metadata records** describing all processed text datasets —  
their provenance, schema, NLP model lineage, and temporal coverage — ensuring transparent,  
traceable documentation for all textual and linguistic assets in the Kansas Frontier Matrix system.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)
[![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

## 📚 Table of Contents
- [Overview](#overview)
- [Directory Layout](#directory-layout)
- [Metadata Structure](#metadata-structure)
- [STAC Integration](#stac-integration)
- [Validation & Provenance](#validation--provenance)
- [Adding or Editing Metadata](#adding-or-editing-metadata)
- [References](#references)

---

## 🧠 Overview

This folder contains **structured metadata JSON files** for all cleaned and processed text datasets  
within `data/processed/text/`. These metadata records form the **semantic bridge** between  
OCR-corrected text corpora and the knowledge graph entities derived from them.

Each metadata file adheres to the **Master Coder Protocol (MCP)** documentation model and  
the **SpatioTemporal Asset Catalog (STAC 1.0)** standard, enabling dataset discovery,  
linking, and reproducibility across the project.

These records also capture **NLP model lineage** — including the model name, version,  
and tokenization/NER parameters used — ensuring full auditability of language processing steps.

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── text/
        └── metadata/
            ├── ocr_cleaned_diaries_1850_1900.json
            ├── kansas_treaties_cleaned.json
            ├── newspapers_1854_1925_cleaned.json
            ├── nlp_entities_extracted.json
            ├── term_frequencies_ks_press.json
            ├── template.json
            └── README.md
````

Each `.json` file documents one text dataset from the parent directory
(`data/processed/text/`) and links to its input sources in `data/raw/text/`.

---

## 🧩 Metadata Structure

All metadata JSONs comply with the **hybrid MCP-STAC schema** used throughout the Frontier Matrix.

### Example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "newspapers_1854_1925_cleaned",
  "properties": {
    "title": "Kansas Newspapers (1854–1925) – Cleaned OCR Text",
    "datetime": "1925-01-01T00:00:00Z",
    "description": "OCR-corrected and cleaned Kansas newspaper corpus derived from Chronicling America. Includes date, title, and text content in JSONL format.",
    "nlp:model": "en_core_web_trf (spaCy v3.7.2)",
    "nlp:tasks": ["tokenization", "NER", "lemmatization"],
    "processing:software": "Python + spaCy + regex + jsonlines",
    "mcp_provenance": "sha256:f2a7c9...",
    "derived_from": ["data/raw/text/newspapers_1854_1925_ocr.zip"],
    "license": "CC-BY 4.0",
    "keywords": ["Kansas", "newspapers", "OCR", "text mining", "NER"]
  },
  "assets": {
    "data": {
      "href": "../newspapers_1854_1925_cleaned.jsonl",
      "type": "application/jsonl"
    }
  }
}
```

### Required Metadata Fields

| Field                 | Description                          | Example                                       |
| --------------------- | ------------------------------------ | --------------------------------------------- |
| `id`                  | Unique dataset identifier            | `"kansas_treaties_cleaned"`                   |
| `title`               | Descriptive name of dataset          | `"Treaty Transcripts – Kansas Land Cessions"` |
| `datetime`            | Processing or dataset reference date | `"1867-10-21T00:00:00Z"`                      |
| `nlp:model`           | NLP model and version used           | `"en_core_web_sm (spaCy v3.6.0)"`             |
| `nlp:tasks`           | NLP tasks performed                  | `["tokenization", "NER"]`                     |
| `mcp_provenance`      | Checksum or hash reference           | `"sha256:a3f19e..."`                          |
| `derived_from`        | Input dataset(s) or sources          | `["data/raw/text/treaties_ocr.zip"]`          |
| `processing:software` | Libraries or pipelines used          | `"spaCy + regex + textacy"`                   |

Optional fields include:

* `language` (ISO-639 code, e.g., `"en"`)
* `text:count` (number of documents/records)
* `token:count` (word/token total)
* `ner:count` (number of recognized entities)
* `quality:score` (OCR accuracy estimate)

---

## 🌐 STAC Integration

Each metadata record feeds directly into the [project-wide STAC catalog](../../../stac/),
where text datasets appear as **STAC Items** under the “Text” collection.

STAC entries allow:

* Spatial-temporal filtering (based on document dates or regions mentioned)
* Semantic search via tags and NLP-derived entities
* API-based access for downstream tools and visualization in the web app

---

## 🔍 Validation & Provenance

Validation steps include:

1. **JSON Schema Validation:** Confirms that each metadata file conforms to
   `data/processed/metadata/schema/processed_item.schema.json`.
2. **Checksum Verification:** Ensures `mcp_provenance` matches the corresponding `.sha256` file.
3. **Model Lineage Verification:** Confirms NLP model identifiers match registered entries
   in the MCP model registry (under `docs/standards/models.md`).
4. **STAC Compliance:** Validates all mandatory STAC fields and asset references.

Local validation can be run with:

```bash
make validate-text
```

---

## 🧠 Adding or Editing Metadata

1. Copy `template.json` and place it in this directory.
2. Fill in required fields:

   * `id`, `title`, `datetime`, `description`, `nlp:model`, `derived_from`
3. Add a checksum reference from the processed file’s `.sha256`.
4. Validate:

   ```bash
   make validate-text
   ```
5. Commit the JSON and submit a PR including:

   * Associated dataset update
   * Description of NLP tasks performed
   * Source citation and license information

---

## 📖 References

* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **spaCy NLP Framework:** [https://spacy.io/](https://spacy.io/)
* **jsonlines Format:** [https://jsonlines.org/](https://jsonlines.org/)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)
* **Chronicling America OCR Archive:** [https://chroniclingamerica.loc.gov/](https://chroniclingamerica.loc.gov/)
* **ISO 639-3 Language Codes:** [https://iso639-3.sil.org/code_tables/639/data](https://iso639-3.sil.org/code_tables/639/data)

---

<div align="center">

*“Every document deserves its context — these metadata files preserve the language, lineage, and legacy of Kansas texts.”*

</div>
```

