<div align="center">

# 📜 Kansas Frontier Matrix — Text Checksums  
`data/processed/checksums/text/`

**Mission:** Safeguard the **integrity, provenance, and reproducibility**  
of all processed textual datasets — including newspapers, oral histories, and treaties —  
by maintaining SHA-256 checksum verification for each file in Kansas Frontier Matrix.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This folder contains **SHA-256 checksum files (`.sha256`)**  
for all processed **text datasets** within Kansas Frontier Matrix (KFM).  

These checksums act as immutable fingerprints that:
- **Verify file integrity** for textual datasets  
- **Confirm reproducible ETL outputs** during AI/NLP processing  
- **Provide provenance** linking to STAC and metadata layers  
- **Enable auditability** via automated CI validation  

Generated automatically during the text ETL pipeline (`make text`),  
these checksums are validated through GitHub Actions to maintain end-to-end reproducibility.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/text/
├── README.md
├── newspaper_articles_1850_1920.jsonl.sha256
├── oral_histories_transcripts.json.sha256
└── treaties_legislation_1820_1900.json.sha256
````

> **Note:** Each `.sha256` file corresponds to its dataset in
> `data/processed/text/` and is verified automatically in CI via `sha256sum -c`.

---

## 🔐 Purpose of Checksums

| Objective                  | Description                                                                  |
| :------------------------- | :--------------------------------------------------------------------------- |
| **Integrity Verification** | Detects any modification or corruption in text-based datasets.               |
| **Reproducibility**        | Confirms NLP and OCR processing produce deterministic results.               |
| **Provenance Tracking**    | Links dataset outputs to STAC metadata and source manifests.                 |
| **CI Enforcement**         | GitHub Actions re-hash all text outputs to ensure parity with stored values. |

---

## 🧮 Example `.sha256` File

```bash
# File: newspaper_articles_1850_1920.jsonl.sha256
acbbfca1d5e56b2ef14898ce22d0837ffb7341a912d1b5206de91f08a64cc8b1  newspaper_articles_1850_1920.jsonl
```

This checksum authenticates the dataset
`data/processed/text/newspaper_articles_1850_1920.jsonl`.

---

## ⚙️ Checksum Generation Workflow

Checksums are created automatically during or after text dataset processing.

**Makefile target:**

```bash
make text-checksums
```

**Equivalent Python command:**

```bash
python src/utils/generate_checksums.py data/processed/text/ --algo sha256
```

**Workflow Steps:**

1. Locate processed text datasets (`.txt`, `.json`, `.jsonl`).
2. Compute SHA-256 hash for each file using Python’s `hashlib`.
3. Write `<filename>.sha256` into this folder.
4. Validate checksums on each CI build or deployment.

---

## 🧰 CI/CD Validation

Checksum verification occurs automatically in GitHub Actions workflows.

**Example validation command:**

```bash
sha256sum -c data/processed/checksums/text/*.sha256
```

If any hash fails validation, the build fails — ensuring no altered or corrupted
text data reaches publication or deployment stages.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                           |
| :------------------------------------ | :---------------------------------------------------------------- |
| `data/processed/metadata/text/`       | Metadata JSON files reference associated checksums                |
| `src/pipelines/text/text_pipeline.py` | Generates and verifies all text dataset hashes                    |
| `.github/workflows/stac-validate.yml` | CI automation of STAC and checksum integrity checks               |
| `data/stac/text/`                     | STAC catalog includes checksum references for provenance tracking |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                              |
| :---------------------- | :---------------------------------------------------------- |
| **Documentation-first** | Each text dataset includes `.sha256` checksum and metadata  |
| **Reproducibility**     | Hashes confirm deterministic NLP + ETL output consistency   |
| **Open Standards**      | SHA-256 (FIPS 180-4) cryptographic hashing                  |
| **Provenance**          | Checksum links form part of dataset lineage and audit trail |
| **Auditability**        | Automated CI/CD verification of checksum integrity          |

---

## 📅 Version History

| Version | Date       | Summary                                                  |
| :------ | :--------- | :------------------------------------------------------- |
| v1.0    | 2025-10-04 | Initial release of text checksum documentation and files |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Verified: Integrity in the Historical Record.”*
📍 [`data/processed/checksums/text/`](.) · Linked to the **Text STAC Collection**

</div>
