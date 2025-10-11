<div align="center">

# 🔐 Kansas-Frontier-Matrix — Processed Text Checksums

`data/processed/text/checksums/`

**Mission:** Store **checksum files (`.sha256`)** verifying the integrity of all processed text datasets —
OCR-corrected transcripts, NLP-extracted entities, and tokenized corpora — ensuring data fidelity
and provenance across KFM’s linguistic archive.

[![Build & Deploy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/site.yml?label=Build%20%26%20Deploy)](../../../../.github/workflows/site.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../../../.github/workflows/stac-validate.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Trivy](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)  [![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  [![License: Code](https://img.shields.io/badge/License-MIT-yellow)](../../../../LICENSE)

</div>

---

### 🧭 Table of Contents

* [Overview](#overview)
* [Purpose](#purpose)
* [Directory Layout](#directory-layout)
* [Checksum Standards](#checksum-standards)
* [Verification Workflow](#verification-workflow)
* [Integration with MCP & STAC](#integration-with-mcp--stac)
* [Adding or Updating Checksums](#adding-or-updating-checksums)
* [Versioning & Changelog](#versioning--changelog)
* [References](#references)

---

## 🧠 Overview

This folder holds **SHA-256 checksum files** used to verify the integrity of text-based datasets in `data/processed/text/`.
Checksums serve as **immutable fingerprints** that link each file to its metadata (`mcp_provenance`) and to STAC items,
enabling end-to-end reproducibility across the MCP provenance chain.

---

## 🎯 Purpose

* **Integrity** — Detect any post-processing alterations to JSONL/CSV/JSON corpora.
* **Reproducibility** — Confirm dataset stability across rebuilds and environments.
* **Automation** — Power CI validation in GitHub Actions.
* **Linkage** — Bind asset files ↔ metadata ↔ STAC using the same hash.

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
```

Each `.sha256` file contains:

```
<hash>  <relative_path_to_dataset>
```

Example:

```
c41b983e774eac1183b1b6dbbfb64a2b99c546785a9b6eb57df9c9a799764a9a  newspapers_1854_1925_cleaned.jsonl
```

**Naming Convention**
`<dataset_filename>.<ext>.sha256` (same basename as the data file, plus `.sha256`).

---

## 🧩 Checksum Standards

| Standard    | Algorithm                 | Output            | Purpose                          |
| :---------- | :------------------------ | :---------------- | :------------------------------- |
| **SHA-256** | 256-bit secure hash       | 64-char hex       | Strong integrity verification    |
| **Format**  | GNU coreutils `sha256sum` | one hash per line | Human + machine friendly         |
| **Mode**    | Binary (`--binary`)       | cross-OS stable   | Avoid CRLF drift & locale issues |

> Compatible with `sha256sum` (Linux), `shasum -a 256` (macOS), and BusyBox variants.

---

## 🔍 Verification Workflow

```bash
# Verify a single corpus
sha256sum -c data/processed/text/checksums/newspapers_1854_1925_cleaned.jsonl.sha256

# Verify all processed text corpora
find data/processed/text/checksums -name "*.sha256" -exec sha256sum -c {} \;
```

Expected success:

```
newspapers_1854_1925_cleaned.jsonl: OK
ocr_cleaned_diaries_1850_1900.jsonl: OK
```

Failure example:

```
nlp_entities_extracted.json: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

**Quick Verify (local)**

```bash
sha256sum -c checksums/*.sha256
```

**CI Targets**

* `make validate-text` → runs checksum verification in CI
* `pre-commit` → optional hook to block commits when hashes are stale

---

## 🌐 Integration with MCP & STAC

1. **MCP Provenance** — Each metadata JSON in `../metadata/` includes
   `"mcp_provenance": "sha256:<hash>"`, referencing its dataset’s checksum.

2. **STAC Items** — STAC entries under `data/stac/` reference the same files;
   the file on disk must match the checksum verified here to pass validation.

This **shared hash** is the canonical link across data, metadata, and catalogs.

---

## ⚙️ Adding or Updating Checksums

1. Generate a checksum for each new/updated file:

   ```bash
   sha256sum <file> > data/processed/text/checksums/<file>.sha256
   ```
2. Verify locally:

   ```bash
   sha256sum -c data/processed/text/checksums/<file>.sha256
   ```
3. Commit **both** the data file and its `.sha256`.
4. Update references:

   * `../metadata/<name>.json` → `mcp_provenance` value
   * STAC item for the dataset (asset points to the same file)
5. Push; CI will run `make validate-text` and fail if mismatched.

---

## 🧮 Versioning & Changelog

| Version  | Date       | Notes                                                                                                   |
| :------- | :--------- | :------------------------------------------------------------------------------------------------------ |
| **v1.3** | 2025-10-11 | Standardized to KFM grid; added Naming Convention, Quick Verify, and CI Targets; clarified binary mode. |
| **v1.2** | 2025-10-10 | Expanded verification examples; linked MCP `mcp_provenance` and STAC flow.                              |
| **v1.1** | 2025-10-08 | Initial checksum README with layout and workflow.                                                       |
| **v1.0** | 2025-10-05 | Bootstrapped checksums directory and examples.                                                          |

---

## 📖 References

* GNU Coreutils — [sha2 utilities](https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html)
* STAC 1.0 — [stacspec.org](https://stacspec.org) · JSON Lines — [jsonlines.org](https://jsonlines.org/)
* spaCy — [spacy.io](https://spacy.io/) · MCP — [`docs/standards/`](../../../../docs/standards/)
* Chronicling America — [chroniclingamerica.loc.gov](https://chroniclingamerica.loc.gov/)

---

<div align="center">

> *“Every line verified, every word preserved — checksums guard the integrity of Kansas’s written frontier.”*

</div>
