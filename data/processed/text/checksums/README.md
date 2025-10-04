<div align="center">

# 🔐 Kansas-Frontier-Matrix — Processed Text Checksums (`data/processed/text/checksums/`)

**Mission:** Store **checksum files (`.sha256`)** verifying the integrity of all processed text datasets —  
OCR-corrected transcripts, NLP-extracted entities, and tokenized corpora — ensuring data fidelity  
and provenance across the Kansas Frontier Matrix’s linguistic archive.

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
- [Purpose](#purpose)
- [Directory Layout](#directory-layout)
- [Checksum Standards](#checksum-standards)
- [Verification Workflow](#verification-workflow)
- [Integration with MCP & STAC](#integration-with-mcp--stac)
- [Adding or Updating Checksums](#adding-or-updating-checksums)
- [References](#references)

---

## 🧠 Overview

This folder holds **SHA-256 checksum files** used to verify the integrity of text-based datasets  
in `data/processed/text/`. These files confirm that OCR-cleaned, NLP-processed, and tokenized corpora  
remain unchanged and trustworthy since their last validation.

Checksums serve as **immutable fingerprints** linking each text file to its metadata (`mcp_provenance`)  
and providing end-to-end verification across the Master Coder Protocol (MCP) provenance chain.

---

## 🎯 Purpose

- **Integrity:** Verify that processed text data (JSONL, CSV, JSON) remains unaltered post-cleaning.  
- **Reproducibility:** Allow researchers to confirm dataset consistency across rebuilds or versions.  
- **Automation:** Enable CI/CD validation for textual corpora in GitHub Actions.  
- **Linkage:** Connect hash values with metadata and STAC records for transparent provenance tracking.  

---

## 🧱 Directory Layout

```bash
data/
└── processed/
    └── text/
        └── checksums/
            ├── ocr_cleaned_diaries_1850_1900.jsonl.sha256
            ├── kansas_treaties_cleaned.jsonl.sha256
            ├── newspapers_1854_1925_cleaned.jsonl.sha256
            ├── nlp_entities_extracted.json.sha256
            ├── term_frequencies_ks_press.csv.sha256
            └── README.md
````

Each `.sha256` file contains a single line:

```
<hash>  <relative_path_to_dataset>
```

Example:

```
c41b983e774eac1183b1b6dbbfb64a2b99c546785a9b6eb57df9c9a799764a9a  newspapers_1854_1925_cleaned.jsonl
```

---

## 🧩 Checksum Standards

| Standard     | Algorithm                 | Output                    | Purpose                     |
| ------------ | ------------------------- | ------------------------- | --------------------------- |
| **SHA-256**  | 256-bit secure hash       | 64-character hex          | Data integrity verification |
| **Format**   | GNU Coreutils `sha256sum` | one hash per line         | Machine- and human-readable |
| **Encoding** | Binary mode (`--binary`)  | avoids OS inconsistencies | Ensures reproducible hashes |

All checksums are compatible with standard Unix utilities (`sha256sum`, `shasum -a 256`).

---

## 🔍 Verification Workflow

To verify individual text datasets:

```bash
# Verify one file
sha256sum -c data/processed/text/checksums/newspapers_1854_1925_cleaned.jsonl.sha256

# Verify all processed text corpora
find data/processed/text/checksums -name "*.sha256" -exec sha256sum -c {} \;
```

If all files are valid:

```
newspapers_1854_1925_cleaned.jsonl: OK
ocr_cleaned_diaries_1850_1900.jsonl: OK
```

A failed verification will print:

```
nlp_entities_extracted.json: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

---

## 🌐 Integration with MCP & STAC

Checksums are embedded in both:

1. **MCP Provenance Fields:**
   Each metadata JSON under `data/processed/text/metadata/` includes
   `"mcp_provenance": "sha256:<hash>"`, referencing its checksum.
2. **STAC Items:**
   STAC entries in `data/stac/items/text_*` use the same hash to ensure data
   in catalogs matches the physical file hashes verified here.

This cross-linking ensures that text corpora, metadata, and provenance graphs all
share the same immutable digital signature.

---

## ⚙️ Adding or Updating Checksums

1. Generate checksum(s) for new or updated text files:

   ```bash
   sha256sum <file> > data/processed/text/checksums/<file>.sha256
   ```
2. Verify:

   ```bash
   sha256sum -c data/processed/text/checksums/<file>.sha256
   ```
3. Commit both:

   * The text dataset
   * The corresponding `.sha256` checksum
4. If the file was reprocessed, update the checksum in:

   * The metadata JSON (`mcp_provenance`)
   * The STAC catalog item for that dataset

---

## 📖 References

* **GNU Coreutils SHA Utilities:** [https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html)
* **STAC Specification 1.0:** [https://stacspec.org](https://stacspec.org)
* **JSON Lines Format:** [https://jsonlines.org/](https://jsonlines.org/)
* **Master Coder Protocol (MCP):** [`docs/standards/`](../../../../docs/standards/)
* **Chronicling America OCR Data:** [https://chroniclingamerica.loc.gov/](https://chroniclingamerica.loc.gov/)
* **spaCy NLP Framework:** [https://spacy.io/](https://spacy.io/)

---

<div align="center">

*“Every line verified, every word preserved — checksums guard the integrity of Kansas’s written frontier.”*

</div>
```

