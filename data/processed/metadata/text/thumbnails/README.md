<div align="center">

# 🖼️ Kansas Frontier Matrix — Text Thumbnails  
`data/processed/metadata/text/thumbnails/`

**Mission:** Store and document **thumbnail preview images** generated from processed textual datasets —  
including newspapers, oral histories, and treaty documents — for use in the Kansas Frontier Matrix web app,  
STAC catalog, and documentation previews.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **thumbnail images (PNG format)** representing Kansas Frontier Matrix’s  
processed text datasets. Each thumbnail acts as a **compact visual summary** —  
showing linguistic and thematic structure through:  
- Word clouds  
- Keyword frequency or co-occurrence plots  
- Document density maps or topic clusters  

Thumbnails appear across:
- The **KFM Web App** (MapLibre / React)  
- The **STAC Catalog** (`data/stac/text/`)  
- The **Documentation Site** (for dataset preview cards)  

All thumbnails are **auto-generated** during the text ETL pipeline (`make text`)  
and rebuilt whenever datasets change.

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Processed Text Corpora\n(data/processed/text/*.json|*.jsonl)"] --> B["Thumbnail Generator\n(src/pipelines/text/text_pipeline.py)"]
  B --> C["Thumbnails (.png)\n(data/processed/metadata/text/thumbnails/)"]
  C --> D["Metadata Linking\n(data/processed/metadata/text/*.json)"]
  D --> E["Catalog + Web UI\n(data/stac/text/ · web/config/layers.json)"]
  %% END OF MERMAID
````

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/text/thumbnails/
├── README.md
├── newspaper_articles_1850_1920.png
├── oral_histories_transcripts.png
└── treaties_legislation_1820_1900.png
```

> **Note:**
> Each `.png` thumbnail corresponds to a STAC metadata file in
> `data/processed/metadata/text/` and a dataset under `data/processed/text/`.
> These are linked through the `"thumbnail"` field in the STAC JSON assets.

---

## 📜 Thumbnail Index

| Dataset                                | Thumbnail File                       | Source Data                                               | Description                                                                   |
| :------------------------------------- | :----------------------------------- | :-------------------------------------------------------- | :---------------------------------------------------------------------------- |
| **Historical Newspapers (1850–1920)**  | `newspaper_articles_1850_1920.png`   | `data/processed/text/newspaper_articles_1850_1920.jsonl`  | Word cloud of OCR text from Kansas newspapers, showing frequent terms by era. |
| **Oral Histories & Interviews**        | `oral_histories_transcripts.png`     | `data/processed/text/oral_histories_transcripts.json`     | Visualization showing keyword frequency across oral history transcripts.      |
| **Treaties & Legislation (1820–1900)** | `treaties_legislation_1820_1900.png` | `data/processed/text/treaties_legislation_1820_1900.json` | Entity and topic cloud summarizing treaties and legal acts.                   |

---

## ⚙️ Thumbnail Generation Workflow

**Makefile Target**

```bash
make text-thumbnails
```

**Python Command**

```bash
python src/pipelines/text/text_pipeline.py --generate-thumbnails
```

**Workflow Steps**

1. Load text datasets (`.txt`, `.json`, `.jsonl`).
2. Extract or tokenize words using NLP tools (`spaCy`, `nltk`).
3. Compute frequency distributions or keyword clusters.
4. Render a word cloud or visualization using `matplotlib`, `wordcloud`, or `plotly`.
5. Export `.png` previews (max 1024×768 px).
6. Save under this directory and register in the STAC JSON `"thumbnail"` asset.

> ♻️ **Regeneration:** All thumbnails rebuild automatically on ETL re-run or metadata update.

---

## 🧮 Specifications & Provenance

| Property         | Specification                                                |
| :--------------- | :----------------------------------------------------------- |
| **File Type**    | PNG (lossless)                                               |
| **Resolution**   | ≤ 1024×768 px                                                |
| **Color Scheme** | KFM Monochrome palette (navy → gray → gold)                  |
| **Generated By** | Python (`matplotlib`, `wordcloud`, `seaborn`, `plotly`)      |
| **Attribution**  | Derived from open-source or public-domain text archives      |
| **Regeneration** | Auto-regenerated during text ETL or `make validate-metadata` |

---

## 🤖 AI & NLP Visualization Integration

The **AI subsystem** enhances thumbnails with automated content analysis:

* **Entity-Aware Clouds:** NLP models weight terms by entity frequency (people, places, events).
* **Sentiment Spectrum:** Color gradients visualize sentiment trends (for diaries/interviews).
* **Topic Inference:** Optional topic modeling (`BERTopic`, `LDA`) overlays dominant clusters.
* **Confidence Scoring:** Metadata stores mean confidence (`nlp:confidence_mean`) for generated thumbnails.

> 🔍 AI-derived thumbnails are logged under `data/processed/text/ai_metadata/`
> and reviewed before publishing to ensure semantic accuracy.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                        |
| :------------------------------------ | :------------------------------------------------------------- |
| `data/processed/metadata/text/*.json` | Each STAC item references its thumbnail                        |
| `src/pipelines/text/text_pipeline.py` | Generates and attaches thumbnails automatically                |
| `data/stac/text/`                     | Catalog items embed thumbnails for visual preview              |
| `web/config/layers.json`              | Displays thumbnails in story map timelines and data browser UI |

---

## ✅ MCP Compliance Summary

| MCP Principle           | Implementation                                                  |
| :---------------------- | :-------------------------------------------------------------- |
| **Documentation-first** | README + per-dataset STAC JSON + linked thumbnail               |
| **Reproducibility**     | Deterministic thumbnail generation with controlled random seeds |
| **Open Standards**      | PNG + STAC-compliant asset linking                              |
| **Provenance**          | Derived from versioned, validated text datasets                 |
| **Auditability**        | CI rebuild and validation on every ETL run                      |

---

## 🧾 Version History

| Version   | Date       | Summary                                                                                         |
| :-------- | :--------- | :---------------------------------------------------------------------------------------------- |
| **1.1.0** | 2025-10-11 | Added front-matter, Mermaid diagram, AI-assisted generation section, and MCP compliance summary |
| 1.0.0     | 2025-10-04 | Initial text thumbnail release (newspaper, oral history, and treaty datasets)                   |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Words that Shaped the Frontier.”*
📍 [`data/processed/metadata/text/thumbnails/`](.) · Linked to the **Text STAC Collection**

</div>
```
