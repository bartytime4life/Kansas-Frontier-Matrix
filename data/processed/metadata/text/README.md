<div align="center">

# 📜 Kansas Frontier Matrix — Text Metadata  
`data/processed/metadata/text/`

**Mission:** Curate, document, and standardize all **processed textual datasets** —  
including historical documents, newspaper archives, oral histories, and transcriptions —  
for integration within the Kansas Frontier Matrix knowledge graph and timeline viewer.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](https://pre-commit.com/)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory documents **processed textual resources** in KFM, including:

- Digitized **letters, diaries, and manuscripts**
- **Newspaper OCR** from historical archives
- **Oral history transcripts** and interviews
- **Treaties, legislation, and archival documents**

Each metadata file provides:
- **STAC 1.0 item** (`.json`)
- Provenance (source, license, processing date, checksums)
- **NLP fields** (entities, language, summary, keyword facets)
- Validation against shared schema (`data/processed/metadata/schema/text.schema.json`)

---

## 🧭 System Flow (Mermaid)

```mermaid
flowchart TD
  A["Source Texts\n(LoC · KHS · Avalon · Archives)"] --> B["OCR & Normalization\n(Tesseract · orthography fixes)"]
  B --> C["NLP Enrichment\n(spaCy · transformers · NER/summary)"]
  C --> D["Processed Corpora\n(data/processed/text/*.json|*.jsonl|*.txt)"]
  D --> E["STAC Items & Thumbnails\n(data/processed/metadata/text/*.json|thumbnails/*.png)"]
  E --> F["Catalog & Graph\n(data/stac/text · src/graph/text_nodes.py)"]
  %% END OF MERMAID
````

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
```

> **Note:** Each `.json` is a STAC item describing a dataset in `data/processed/text/`.
> Thumbnails are small previews (word clouds, page snapshots) used in the web app and catalog.

---

## 🧾 Text Datasets (Processed Assets)

| Dataset                               | Source                                          | Format      | Temporal Coverage | Output                                                    |
| :------------------------------------ | :---------------------------------------------- | :---------- | :---------------- | :-------------------------------------------------------- |
| **Historical Newspapers (1850–1920)** | Library of Congress · Chronicling America       | TXT → JSONL | 1850–1920         | `data/processed/text/newspaper_articles_1850_1920.jsonl`  |
| **Oral Histories & Interviews**       | Kansas Historical Society · University Archives | TXT → JSON  | 1900–2025         | `data/processed/text/oral_histories_transcripts.json`     |
| **Treaties & Legislative Documents**  | Yale Avalon Project · Govt. Archives            | TXT → JSON  | 1820–1900         | `data/processed/text/treaties_legislation_1820_1900.json` |

All corpora live in open formats (**TXT**, **JSON**, **JSONL**) and are discoverable in `data/stac/text/`.

---

## 💾 Example STAC Item (enhanced)

```json
{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "newspaper_articles_1850_1920",
  "collection": "kfm_text",
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99], [-94.59, 36.99],
      [-94.59, 40.00], [-102.05, 40.00],
      [-102.05, 36.99]
    ]]
  },
  "properties": {
    "title": "Kansas Historical Newspaper OCR Collection (1850–1920)",
    "description": "Digitized OCR text from Chronicling America with NLP enrichment (entities, keywords, summaries).",
    "datetime": "1920-01-01T00:00:00Z",
    "themes": ["text","newspapers","history"],
    "processing:software": "Tesseract 5; spaCy 3; transformers",
    "kfm:mcp_provenance": "sha256:<PUT_FILE_HASH_HERE>",
    "text:language": ["en"],
    "text:ocr_engine": "tesseract",
    "text:ocr_confidence_mean": 0.91,
    "text:ocr_confidence_min": 0.70,
    "license": "Public Domain (Library of Congress)"
  },
  "assets": {
    "data": {
      "href": "../text/newspaper_articles_1850_1920.jsonl",
      "type": "application/jsonl",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "thumbnails/newspaper_articles_1850_1920.png",
      "type": "image/png",
      "roles": ["thumbnail"]
    },
    "checksum:sha256": {
      "href": "../text/checksums/newspaper_articles_1850_1920.jsonl.sha256",
      "type": "text/plain",
      "roles": ["metadata"]
    }
  },
  "links": [
    {"rel": "collection", "href": "../../../stac/collections/kfm_text.json", "type": "application/json"},
    {"rel": "self", "href": "newspaper_articles_1850_1920.json", "type": "application/json"},
    {"rel": "parent", "href": ".", "type": "text/html"}
  ]
}
```

> **Optional fields you can add:** `iiif:manifest`, `tei:xml`, `text:script`, `text:direction`,
> `nlp:entities_count`, `nlp:model`, `nlp:summary_tokens`, `nlp:keywords[]`.

---

## 🧩 Semantic & Ontological Alignment

| Entity                              | Ontology Mapping                               | Example                               |
| :---------------------------------- | :--------------------------------------------- | :------------------------------------ |
| Newspaper Article                   | CIDOC `E31_Document` + `E33_Linguistic_Object` | “Leavenworth Times, July 4, 1876”     |
| Oral History Transcript             | CIDOC `E7_Activity` + `E33_Linguistic_Object`  | “Interview with a Dust Bowl Survivor” |
| Treaty / Law Text                   | CIDOC `E5_Event` + `E31_Document`              | “1854 Kansa Land Cession Treaty”      |
| Named Entity (Person, Place, Event) | `E21_Person`, `E53_Place`, `E5_Event`          | NLP-extracted nodes                   |

These alignments power semantic links in the **knowledge graph** and time-aware map narratives.

---

## ⚙️ ETL & Processing Workflow

**Makefile**

```bash
make text
```

**Pipeline**

```bash
python src/pipelines/text/text_pipeline.py
```

**Steps**

1. Fetch source texts (LoC, KHS, Avalon, etc.).
2. OCR / text cleaning (encoding fixes, dehyphenation, artifact removal).
3. NLP enrichment (language detect, NER, summarization, keywords).
4. Write **JSON/JSONL** with per-doc metadata & spans.
5. Compute **`.sha256`** checksums for each artifact.
6. Generate **STAC items** + thumbnails.
7. Validate with **JSON Schema** + **STAC** in CI.

**Key dependencies:** `tesseract-ocr`, `spaCy`, `transformers`, `nltk`, `pandas`, `jsonlines`, `langdetect`.

---

## 🧮 Provenance, Quality & Validation

* **Checksums:** `data/processed/text/checksums/`
* **Licensing:** Public domain or **CC-BY 4.0** (derived corpora)
* **Quality fields:** `text:ocr_confidence_mean|min|max`, `nlp:model`, `nlp:entities_count`
* **Validation:** JSON Schema + STAC 1.0 via CI; language code checks (`BCP-47`)
* **Source manifests:** `data/sources/text/*.json`

---

## 🔗 Integration Points

| Component                         | Role                                                        |
| :-------------------------------- | :---------------------------------------------------------- |
| `data/stac/text/`                 | STAC Items & Collections for text datasets                  |
| `web/config/layers.json`          | Narrative layers, search facets, timeline integration       |
| `src/graph/text_nodes.py`         | Graph ingestion & entity linking                            |
| `data/processed/text/`            | Canonical processed corpora                                 |
| `data/processed/metadata/schema/` | Validation schemas (`text.schema.json`, shared STAC schema) |

---

## ✅ QA Checklist (copy into PRs)

* [ ] STAC item validates (CI green)
* [ ] `kfm:mcp_provenance` hash matches sidecar checksum
* [ ] Language and OCR fields populated (where applicable)
* [ ] Thumbnail present & path valid in `assets.thumbnail`
* [ ] NLP fields (model, entities_count) included for enriched corpora
* [ ] Sources/licensing clearly stated and resolvable

---

## 🧠 MCP Compliance Summary

| Principle           | Implementation                                                 |
| :------------------ | :------------------------------------------------------------- |
| Documentation-first | README + per-dataset STAC items + schema                       |
| Reproducibility     | Deterministic pipeline; pinned tools; checksums                |
| Open Standards      | JSON/JSONL/TXT; **STAC 1.0**; optional **IIIF/TEI** references |
| Provenance          | `kfm:mcp_provenance` + source manifests + CI logs              |
| Auditability        | CI validation + OCR/NLP quality metrics                        |

---

## 📅 Version History

|  Version  | Date       | Summary                                                                                                           |
| :-------: | :--------- | :---------------------------------------------------------------------------------------------------------------- |
| **1.2.0** | 2025-10-11 | Fixed badge paths; added Mermaid flow; expanded STAC example (checksum + OCR/NLP fields + geometry); QA checklist |
|   1.0.0   | 2025-10-04 | Initial text metadata release (newspapers, oral histories, treaties)                                              |

---

## 📎 References

* Library of Congress — Chronicling America
* Kansas Historical Society — Oral Histories
* Yale Avalon Project — Treaties & Documents
* spaCy NLP Toolkit · Tesseract OCR
* MCP Standards (`docs/standards/`)

---

<div align="center">

**Kansas Frontier Matrix** — *“Voices of the Frontier: From Newspapers to Narratives.”*
📍 [`data/processed/metadata/text/`](.)

</div>
```
