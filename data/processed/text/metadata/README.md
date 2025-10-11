<div align="center">

# 📜 Kansas-Frontier-Matrix — Processed Text Metadata

`data/processed/text/metadata/`

**Mission:** Maintain **metadata records** describing all processed text datasets —
their provenance, schema, NLP model lineage, and temporal coverage — ensuring transparent,
traceable documentation for all textual and linguistic assets in the Kansas Frontier Matrix (KFM) system.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)  [![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  [![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

### 🧭 Table of Contents

* [Overview](#overview)
* [Directory Layout](#directory-layout)
* [Metadata Structure](#metadata-structure)
* [STAC Integration](#stac-integration)
* [Validation & Provenance](#validation--provenance)
* [Adding or Editing Metadata](#adding-or-editing-metadata)
* [Versioning & Changelog](#versioning--changelog)
* [References](#references)

---

## 🧠 Overview

This folder contains **structured metadata JSON files** for all cleaned and processed text datasets
within `data/processed/text/`. These metadata records form the **semantic bridge** between
OCR-corrected text corpora and the knowledge-graph entities derived from them.

Each file adheres to both the **Master Coder Protocol (MCP)** documentation model and the
**SpatioTemporal Asset Catalog (STAC 1.0)** standard — enabling discovery, provenance tracking,
and reproducibility across all textual data pipelines.

Metadata also capture **NLP model lineage** — model name, version, and tokenization/NER parameters —
ensuring that every language-processing step is fully auditable.

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
```

Each `.json` file documents one dataset from the parent folder
(`data/processed/text/`) and links to its raw input sources in `data/raw/text/`.

---

## 🧩 Metadata Structure

All metadata files conform to the **hybrid MCP–STAC schema**.

### Example

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "newspapers_1854_1925_cleaned",
  "properties": {
    "title": "Kansas Newspapers (1854–1925) – Cleaned OCR Text",
    "datetime": "1925-01-01T00:00:00Z",
    "description": "OCR-corrected and cleaned Kansas newspaper corpus derived from Chronicling America.",
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

### Required Fields

| Field                 | Description                  | Example                                       |
| :-------------------- | :--------------------------- | :-------------------------------------------- |
| `id`                  | Unique dataset identifier    | `"kansas_treaties_cleaned"`                   |
| `title`               | Descriptive dataset name     | `"Treaty Transcripts – Kansas Land Cessions"` |
| `datetime`            | Processing or reference date | `"1867-10-21T00:00:00Z"`                      |
| `nlp:model`           | NLP model + version          | `"en_core_web_sm (spaCy v3.6.0)"`             |
| `nlp:tasks`           | NLP tasks performed          | `["tokenization","NER"]`                      |
| `mcp_provenance`      | Hash reference to checksum   | `"sha256:a3f19e..."`                          |
| `derived_from`        | Input data sources           | `["data/raw/text/treaties_ocr.zip"]`          |
| `processing:software` | Libraries or pipelines used  | `"spaCy + regex + textacy"`                   |

**Optional fields:**
`language`, `text:count`, `token:count`, `ner:count`, `quality:score`

---

## 🌐 STAC Integration

Each record feeds into the **project-wide STAC catalog** under the *Text* collection.

This allows:

* Spatial–temporal filtering by document date or coverage.
* Semantic search using NLP-derived keywords or entity tags.
* Programmatic retrieval through the KFM API or web map interface.

---

## 🔍 Validation & Provenance

Validation stages include:

1. **Schema Validation** — JSON Schema (`processed_item.schema.json`).
2. **Checksum Verification** — ensures `mcp_provenance` matches `.sha256`.
3. **Model Lineage Validation** — checks `nlp:model` entries against the MCP model registry.
4. **STAC Compliance** — confirms mandatory fields & asset links.

Run local validation:

```bash
make validate-text
```

---

## 🧠 Adding or Editing Metadata

1. Copy `template.json` → rename for your dataset.
2. Populate all required fields (`id`, `title`, `datetime`, `description`, `nlp:model`, `derived_from`).
3. Reference the `.sha256` checksum.
4. Validate:

   ```bash
   make validate-text
   ```
5. Submit a PR containing:

   * New/updated metadata file.
   * Associated dataset and source license info.
   * Notes on NLP model and preprocessing.

---

## 🧮 Versioning & Changelog

| Version  | Date       | Notes                                                                                                      |
| :------- | :--------- | :--------------------------------------------------------------------------------------------------------- |
| **v1.3** | 2025-10-11 | Added explicit **Version & Changelog** section and SemVer policy for docs; standardized metadata template. |
| **v1.2** | 2025-10-10 | Protocol alignment — badges, STAC integration, and MCP compliance matrix.                                  |
| **v1.1** | 2025-10-08 | Expanded metadata examples with NLP lineage and audit fields.                                              |
| **v1.0** | 2025-10-05 | Initial metadata README with STAC schema and directory contract.                                           |

---

## 📖 References

* [STAC Specification 1.0](https://stacspec.org)
* [spaCy NLP Framework](https://spacy.io/)
* [JSON Lines Format](https://jsonlines.org/)
* [Master Coder Protocol (MCP)](../../../../docs/standards/)
* [Chronicling America OCR Archive](https://chroniclingamerica.loc.gov/)
* [ISO 639-3 Language Codes](https://iso639-3.sil.org/code_tables/639/data)

---

<div align="center">

> *“Every document deserves its context — these metadata files preserve the language, lineage, and legacy of Kansas texts.”*

</div>
