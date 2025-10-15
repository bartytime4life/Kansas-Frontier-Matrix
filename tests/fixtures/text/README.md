<div align="center">

# 📝 Kansas Frontier Matrix — **Text Fixtures**  
`tests/fixtures/text/`

**OCR · Historical Snippets · NLP Training Samples**

[![Tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/tests.yml/badge.svg)](../../../.github/workflows/tests.yml)
[![Docs · MCP-DL v6.2](https://img.shields.io/badge/Docs-MCP--DL%20v6.2-blue)](../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../LICENSE)

</div>

---

```yaml
---
title: "KFM • Text Fixtures (tests/fixtures/text/)"
version: "v1.0.0"
last_updated: "2025-10-14"
owners: ["@kfm-ai", "@kfm-nlp"]
tags: ["text","ocr","fixtures","nlp","language","mcp"]
license: "MIT"
semantic_alignment:
  - FAIR Principles (Findable, Accessible, Interoperable, Reusable)
  - MCP-DL v6.2 Provenance Documentation
  - WCAG 2.1 AA (Accessible Text Content)
---
````

---

## 🧭 Overview

The `tests/fixtures/text/` directory provides **textual test samples** for verifying KFM’s **AI, NLP, and OCR pipelines**.
These fixtures simulate **historic Kansas documents** — diaries, treaties, and field reports — in a small,
deterministic form, used to test the system’s ability to extract named entities, dates, and geographic references.

Each file is short, UTF-8 encoded, and designed for reproducible parsing, tokenization, and semantic linking tests.

> **Purpose:** Enable robust NLP model validation and OCR parsing under Master Coder Protocol (MCP-DL v6.2) standards of traceable, reproducible AI development.

---

## 🧱 Directory Structure

```text
tests/fixtures/text/
├── sample_diary.txt        # OCR-style diary entry snippet (1890s)
├── treaty_excerpt.txt      # Partial Kansas treaty transcription
├── letter_fragment.txt     # Civil War–era correspondence snippet
├── report_excerpt.txt      # Geological survey text fragment
└── README.md               # This documentation file
```

---

## 🧩 Fixture Overview

| File                  | Type                    | Origin / Theme                 | Used In                                           | Purpose                                         |
| :-------------------- | :---------------------- | :----------------------------- | :------------------------------------------------ | :---------------------------------------------- |
| `sample_diary.txt`    | OCR transcription       | 1890s farm diary               | `ai_entity_extraction.ipynb`, `nlp/tests/`        | Named Entity Recognition (dates, locations)     |
| `treaty_excerpt.txt`  | Historical treaty text  | 1850s U.S.–Tribal treaty       | `ai_relation_extraction`, `stac/metadata linking` | Relationship extraction and citation validation |
| `letter_fragment.txt` | Civil War letter        | Union soldier’s correspondence | `ocr_parser`, `ai_pipeline`                       | OCR validation and language normalization       |
| `report_excerpt.txt`  | Geological field report | 1930s survey                   | `document_summarizer`, `text_cleaner`             | AI summarization, sentence segmentation         |

---

## 🧠 Example Fixture Content — `sample_diary.txt`

```text
March 12, 1894 – The Arkansas River overflowed near Larned.  
Father said the fields by the creek turned to silt overnight.  
We repaired the fence before noon and rode east toward Ellsworth for seed.
```

**Notes:**

* Short, realistic syntax.
* Contains **dates**, **locations**, and **event context** for NER testing.
* No proprietary data — entirely synthetic but historically grounded.

---

## 🧪 Usage in Tests

### 🐍 Python

```python
from pathlib import Path

def test_text_load(fixtures_dir):
    diary = (fixtures_dir / "text/sample_diary.txt").read_text(encoding="utf-8")
    assert "Arkansas River" in diary
    assert "Larned" in diary
```

### 🤖 NLP Integration

```python
from tools.ai_utils import extract_entities

text = open("tests/fixtures/text/treaty_excerpt.txt").read()
entities = extract_entities(text)
assert any(e['type'] == "Place" for e in entities)
```

### 🧬 OCR Simulation

Used by OCR post-processing functions to validate:

* Whitespace normalization
* OCR confidence scoring
* Misread correction (e.g., “Lamed” → “Larned”)

---

## 🧮 Design & Provenance

| Attribute         | Specification                                                     |
| :---------------- | :---------------------------------------------------------------- |
| **Encoding**      | UTF-8                                                             |
| **Line Endings**  | Unix (`\n`)                                                       |
| **Character Set** | ASCII + diacritics allowed                                        |
| **File Size**     | < 5 KB each                                                       |
| **Randomness**    | None — deterministic strings                                      |
| **Provenance**    | Generated or derived from public-domain archives / synthetic data |
| **Metadata**      | Optional `.meta.json` with author, date, license                  |

**Example Metadata (`treaty_excerpt.meta.json`):**

```json
{
  "id": "treaty_excerpt",
  "source": "Public domain transcription based on 1850s Kansas treaty records",
  "license": "Public Domain",
  "checksum": "sha256:27bca6a5..."
}
```

---

## ♿ Accessibility & Compliance

* All text is **plain UTF-8** (no proprietary fonts).
* Texts use **semantic punctuation** and complete sentences for screen reader clarity.
* Fixtures meet **WCAG 2.1 AA** readability guidelines (language simplicity, contrast in rendered docs).
* Each text fixture includes descriptive metadata in the repository documentation for discoverability.

---

## 🔄 Regeneration Process

| Step | Tool                                         | Purpose                                         |
| :--- | :------------------------------------------- | :---------------------------------------------- |
| 1️⃣  | `tools/notebooks/ai_entity_extraction.ipynb` | Generate or clean new text samples              |
| 2️⃣  | `text_cleaner.py`                            | Normalize OCR whitespace, correct encoding      |
| 3️⃣  | `sha256sum`                                  | Generate checksums for provenance               |
| 4️⃣  | `pytest`                                     | Validate encoding and readability before commit |

All new fixtures must be committed with a provenance entry and reviewed during pull requests.

---

## 🧠 MCP Compliance Checklist

| MCP Principle       | Implementation                                 |
| :------------------ | :--------------------------------------------- |
| Documentation-first | Each file documented here or via `.meta.json`  |
| Reproducibility     | Deterministic plain-text fixtures, checksummed |
| Provenance          | Metadata and public-domain sourcing            |
| Accessibility       | WCAG-compliant formatting and structure        |
| Open Standards      | UTF-8 plain text, JSON metadata                |
| Auditability        | CI validation of encoding + checksum integrity |

---

<div align="center">

🪶 *Simple words, strong validation.*
Text fixtures give Kansas Frontier Matrix its linguistic and historical grounding — one sentence at a time.

</div>
```

