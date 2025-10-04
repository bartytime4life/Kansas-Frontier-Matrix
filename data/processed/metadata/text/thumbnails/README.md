<div align="center">

# 🖼️ Kansas Frontier Matrix — Text Thumbnails  
`data/processed/metadata/text/thumbnails/`

**Mission:** Store and document **thumbnail preview images** generated from processed textual datasets —  
including newspapers, oral histories, and treaty documents — for use in the Kansas Frontier Matrix web app,  
STAC catalog, and documentation previews.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **thumbnail images (PNGs)** representing Kansas Frontier Matrix’s  
processed textual datasets, providing compact visual summaries such as:
- Word clouds  
- Document snapshots  
- Keyword frequency plots  
- Text density visualizations  

These previews assist users in visually identifying dataset content from the web interface, STAC catalog,  
and documentation site.

All thumbnails are automatically generated during the **text ETL pipeline (`make text`)**  
and updated whenever a dataset changes.

---

## 🗂️ Directory Layout

```bash
data/processed/metadata/text/thumbnails/
├── README.md
├── newspaper_articles_1850_1920.png
├── oral_histories_transcripts.png
└── treaties_legislation_1820_1900.png
````

> **Note:** Each thumbnail corresponds to a metadata file in
> `data/processed/metadata/text/` and a dataset in `data/processed/text/`.
> The `"thumbnail"` asset field in each STAC JSON links to these files.

---

## 📜 Thumbnail Index

| Dataset                                | Thumbnail File                       | Source Data                                               | Description                                                                                  |
| :------------------------------------- | :----------------------------------- | :-------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **Historical Newspapers (1850–1920)**  | `newspaper_articles_1850_1920.png`   | `data/processed/text/newspaper_articles_1850_1920.jsonl`  | Word cloud generated from OCR text of Kansas newspapers, showing most frequent terms by era. |
| **Oral Histories & Interviews**        | `oral_histories_transcripts.png`     | `data/processed/text/oral_histories_transcripts.json`     | Transcript visualization showing keyword density across oral history collections.            |
| **Treaties & Legislation (1820–1900)** | `treaties_legislation_1820_1900.png` | `data/processed/text/treaties_legislation_1820_1900.json` | Word frequency and entity cloud summarizing major treaties and legislative acts.             |

---

## ⚙️ Thumbnail Generation Workflow

Thumbnails are generated automatically as part of the text ETL process.

**Makefile target:**

```bash
make text-thumbnails
```

**Python command:**

```bash
python src/pipelines/text/text_pipeline.py --generate-thumbnails
```

**Steps:**

1. Load text datasets (JSON, TXT, or JSONL format).
2. Parse and clean textual content.
3. Generate word cloud or frequency plot using `matplotlib`, `wordcloud`, or `seaborn`.
4. Export preview as a 1024×768 PNG.
5. Save to this directory and register file paths in each STAC metadata JSON.

---

## 🧮 Specifications & Provenance

| Property             | Specification                                                  |
| :------------------- | :------------------------------------------------------------- |
| **File Type**        | PNG                                                            |
| **Resolution**       | ≤1024×768 px                                                   |
| **Color Scheme**     | Monochrome blue-gray KFM palette                               |
| **Generation Tools** | Python `wordcloud`, `matplotlib`, `seaborn`                    |
| **Attribution**      | Derived from open-domain text datasets (LoC, KHS, Yale Avalon) |
| **Regeneration**     | Thumbnails are recreated automatically on ETL re-run           |

---

## 🧩 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                         |
| :------------------------------------ | :-------------------------------------------------------------- |
| `data/processed/metadata/text/*.json` | Each STAC item references its thumbnail via `"thumbnail"` asset |
| `src/pipelines/text/text_pipeline.py` | Generates and links thumbnail files automatically               |
| `data/stac/text/`                     | STAC catalog includes thumbnails in item definitions            |
| `web/config/layers.json`              | Used as preview images in document explorer or story map panels |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                        |
| :---------------------- | :-------------------------------------------------------------------- |
| **Documentation-first** | Each dataset includes a README + thumbnail metadata                   |
| **Reproducibility**     | Thumbnails generated deterministically via NLP visualization pipeline |
| **Open Standards**      | PNG format, STAC-compliant asset links                                |
| **Provenance**          | Derived from open-access text corpora                                 |
| **Auditability**        | CI validation and automatic regeneration ensure data consistency      |

---

## 📅 Version History

| Version | Date       | Summary                                                                           |
| :------ | :--------- | :-------------------------------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of text thumbnails — newspaper, oral history, and treaty datasets |

---

<div align="center">

**Kansas Frontier Matrix** — *“Visualizing the Words that Shaped the Frontier.”*
📍 [`data/processed/metadata/text/thumbnails/`](.) · Linked to the **Text STAC Collection**

</div>
