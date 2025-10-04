<div align="center">

# 📜 Kansas Frontier Matrix — Text Metadata  
`data/processed/metadata/text/`

**Mission:** Curate, document, and standardize all **processed textual datasets** —  
including historical documents, newspaper archives, oral histories, and transcriptions —  
for integration within the Kansas Frontier Matrix knowledge graph and timeline viewer.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory documents all **processed textual resources** in Kansas Frontier Matrix (KFM).  
These include:
- Digitized **letters, diaries, and manuscripts**  
- **Newspaper OCR text** from historical archives  
- **Oral history transcripts and interviews**  
- **Treaties, legislation, and archival documents**  

Each file includes:
- **STAC 1.0 metadata** (`.json`)  
- Provenance information (source URL, license, date processed)  
- NLP entity extraction and summarization details  
- Validation against shared schema definitions (`data/processed/metadata/schema/text.schema.json`)  

Text datasets form the narrative backbone of the Frontier Matrix — connecting people, events, and places across time.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/text/
├── README.md
├── newspaper_articles_1850_1920.json
├── oral_histories_transcripts.json
├── treaties_legislation_1820_1900.json
└── thumbnails/
    ├── newspaper_articles_1850_1920.png
    ├── oral_histories_transcripts.png
    └── treaties_legislation_1820_1900.png
````

> **Note:**
> Each `.json` file is a STAC metadata record for a processed textual dataset in `data/processed/text/`.
> Thumbnails are small preview images (word clouds, document snapshots, etc.) used in the KFM web app and catalog.

---

## 🧾 Text Datasets (Processed Assets)

| Dataset                               | Source                                          | Format      | Temporal Coverage | Output                                                    |
| :------------------------------------ | :---------------------------------------------- | :---------- | :---------------- | :-------------------------------------------------------- |
| **Historical Newspapers (1850–1920)** | Library of Congress – Chronicling America       | TXT → JSONL | 1850–1920         | `data/processed/text/newspaper_articles_1850_1920.jsonl`  |
| **Oral Histories & Interviews**       | Kansas Historical Society / University Archives | TXT → JSON  | 1900–2025         | `data/processed/text/oral_histories_transcripts.json`     |
| **Treaties & Legislative Documents**  | Yale Avalon Project / Gov Archives              | TXT → JSON  | 1820–1900         | `data/processed/text/treaties_legislation_1820_1900.json` |

All text datasets are stored in open formats (**TXT**, **JSON**, or **JSONL**)
and indexed under `data/stac/text/` for discovery and search integration.

---

## 💾 Example STAC Metadata

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "newspaper_articles_1850_1920",
  "properties": {
    "title": "Kansas Historical Newspaper OCR Collection (1850–1920)",
    "datetime": "1920-01-01T00:00:00Z",
    "description": "Digitized OCR text of Kansas newspapers from Chronicling America (1850–1920).",
    "themes": ["text", "newspapers", "history"],
    "license": "Public Domain (Library of Congress)",
    "providers": [
      {"name": "Library of Congress", "roles": ["producer"]},
      {"name": "Kansas Frontier Matrix", "roles": ["processor"]}
    ]
  },
  "assets": {
    "data": {
      "href": "../text/newspaper_articles_1850_1920.jsonl",
      "type": "application/jsonl",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/newspaper_articles_1850_1920.png"
    }
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00]
}
```

---

## 🧩 Semantic & Ontological Alignment

| Entity                              | Ontology Mapping                         | Example                               |
| :---------------------------------- | :--------------------------------------- | :------------------------------------ |
| Newspaper Article                   | `E31_Document` + `E33_Linguistic_Object` | “Leavenworth Times, July 4, 1876”     |
| Oral History Transcript             | `E7_Activity` + `E33_Linguistic_Object`  | “Interview with a Dust Bowl Survivor” |
| Treaty or Law Text                  | `E5_Event` + `E31_Document`              | “1854 Kansa Land Cession Treaty”      |
| Named Entity (Person, Place, Event) | `E21_Person`, `E53_Place`, `E5_Event`    | Extracted entities from NLP pipeline  |

This alignment allows semantic linking of text mentions to entities in the knowledge graph
(e.g., connecting a treaty mention to its corresponding geographic boundary or participant list).

---

## ⚙️ ETL & Processing Workflow

**Pipeline:**
`make text` → runs `src/pipelines/text/text_pipeline.py`

**Dependencies:**
`spaCy`, `transformers`, `nltk`, `pandas`, `jsonlines`, `langdetect`

**Steps:**

1. Fetch source text files (newspapers, oral histories, treaties)
2. Clean and normalize OCR text (remove artifacts, fix encoding)
3. Apply NLP models for entity extraction (people, places, events)
4. Generate document summaries and keywords
5. Save structured JSONL outputs with extracted metadata
6. Compute `.sha256` checksums for provenance
7. Generate STAC metadata and thumbnails

---

## 🧮 Provenance & Validation

* **Checksums:** `.sha256` sidecars for each processed text dataset
* **Licensing:** Public domain (LoC, Yale Avalon, KHS) or CC-BY 4.0 for derived corpora
* **Validation:** JSON Schema + STAC validator in CI/CD
* **Cross-links:** Provenance entries in `data/sources/text/*.json`

---

## 🔗 Integration Points

| Component                                         | Role                                                   |
| :------------------------------------------------ | :----------------------------------------------------- |
| `data/stac/text/`                                 | STAC Items & Collections for text datasets             |
| `web/config/layers.json`                          | Web UI integration for narrative layers & keyword maps |
| `src/graph/text_nodes.py`                         | Graph ingestion and NLP entity linking                 |
| `docs/architecture.md`                            | Documentation of AI/NLP integration                    |
| `data/processed/metadata/schema/text.schema.json` | Schema validation for text metadata                    |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                 |
| :---------------------- | :--------------------------------------------- |
| **Documentation-first** | README + STAC metadata per dataset             |
| **Reproducibility**     | Deterministic text pipeline + logs             |
| **Open Standards**      | JSON, JSONL, TXT formats with STAC compliance  |
| **Provenance**          | URLs, checksums, and licenses included         |
| **Auditability**        | Entity extraction logs and CI validation tests |

---

## 📅 Version History

| Version | Date       | Summary                                                                                  |
| :------ | :--------- | :--------------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial text metadata release — includes newspapers, oral histories, and treaty datasets |

---

## 📎 References

* [Library of Congress — Chronicling America](https://chroniclingamerica.loc.gov/)
* [Kansas Historical Society — Oral Histories](https://www.kshs.org/)
* [Yale Avalon Project — Treaties & Documents](https://avalon.law.yale.edu/)
* [spaCy NLP Toolkit](https://spacy.io/)
* [Master Coder Protocol Documentation](../../../docs/templates/)

---

<div align="center">

**Kansas Frontier Matrix** — *“Voices of the Frontier: From Newspapers to Narratives.”*
📍 [`data/processed/metadata/text/`](.) · Integrated within the **STAC Data Catalog Layer**

</div>
