<div align="center">

# 📜 Kansas Frontier Matrix — Text Checksums  
`data/checksums/text/`

**Mission:** Ensure the **integrity, provenance, and reproducibility** of all processed textual datasets —  
including historical newspapers, oral histories, and treaties — within the Kansas Frontier Matrix (KFM)  
through SHA-256 checksum tracking and CI/CD verification.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

## 📚 Overview

This directory stores **SHA-256 checksum files (`.sha256`)**  
for all processed **text datasets** in Kansas Frontier Matrix.  

Checksums act as **cryptographic fingerprints**, ensuring:
- **Integrity:** Detects file corruption or unauthorized changes.  
- **Reproducibility:** Confirms deterministic NLP and OCR processing across runs.  
- **Provenance:** Links datasets to their STAC metadata and processing lineage.  
- **Auditability:** Validated continuously through automated CI/CD pipelines.  

Checksums are created automatically by the **text ETL pipeline (`make text`)**  
and verified during every validation cycle in GitHub Actions.

---

## 🗂️ Directory Layout

```bash
data/checksums/text/
├── README.md
├── newspaper_articles_1850_1920.jsonl.sha256
├── oral_histories_transcripts.json.sha256
└── treaties_legislation_1820_1900.json.sha256
````

> **Note:** Each `.sha256` file corresponds to a processed dataset under
> `data/processed/text/` and is validated in CI/CD using `sha256sum -c`.

---

## 🔐 Purpose of Checksums

| Objective                  | Description                                                            |
| :------------------------- | :--------------------------------------------------------------------- |
| **Integrity Verification** | Detects corruption or file modification.                               |
| **Reproducibility**        | Confirms consistent ETL outputs for all NLP and OCR data.              |
| **Provenance**             | Provides traceable linkage between datasets, metadata, and STAC items. |
| **Automation**             | Validation runs automatically in CI/CD via GitHub Actions.             |

---

## 🧮 Example `.sha256` File

```bash
# File: newspaper_articles_1850_1920.jsonl.sha256
acbbfca1d5e56b2ef14898ce22d0837ffb7341a912d1b5206de91f08a64cc8b1  newspaper_articles_1850_1920.jsonl
```

This checksum verifies that the dataset
`data/processed/text/newspaper_articles_1850_1920.jsonl`
remains identical to its validated version.

---

## ⚙️ Checksum Generation Workflow

Checksums are generated automatically as part of the text ETL process.

**Makefile target:**

```bash
make text-checksums
```

**Python command:**

```bash
python src/utils/generate_checksums.py data/processed/text/ --algo sha256
```

**Workflow Steps:**

1. Locate processed textual outputs (`.jsonl`, `.json`, `.txt`).
2. Compute SHA-256 hashes using Python’s `hashlib` library.
3. Write `<filename>.sha256` files to this directory.
4. Validate all checksums via CI/CD workflows.

---

## 🧰 CI/CD Validation

Checksum validation occurs automatically during build and deployment workflows.

**Validation command:**

```bash
sha256sum -c data/checksums/text/*.sha256
```

**If a mismatch is found:**

* CI halts immediately.
* The dataset must be reprocessed and its checksum updated.
* Logs capture the discrepancy for MCP audit tracking.

---

## 🧩 Integration with Metadata & STAC

| Linked Component                      | Purpose                                                                     |
| :------------------------------------ | :-------------------------------------------------------------------------- |
| `data/processed/metadata/text/`       | STAC metadata references these checksum files.                              |
| `src/pipelines/text/text_pipeline.py` | Generates and validates hashes during ETL runs.                             |
| `.github/workflows/stac-validate.yml` | Automates checksum and metadata validation.                                 |
| `data/stac/text/`                     | STAC catalog embeds checksum references for provenance and reproducibility. |

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                         |
| :---------------------- | :--------------------------------------------------------------------- |
| **Documentation-first** | Each text dataset includes a README and `.sha256` verification file.   |
| **Reproducibility**     | Deterministic text ETL and NLP processing confirmed via hash checks.   |
| **Open Standards**      | SHA-256 (FIPS 180-4) cryptographic hashing algorithm.                  |
| **Provenance**          | Checksum records link dataset lineage to STAC metadata.                |
| **Auditability**        | Automated verification ensures traceable data integrity across builds. |

---

## 📅 Version History

| Version | Date       | Summary                                                                                           |
| :------ | :--------- | :------------------------------------------------------------------------------------------------ |
| v1.0    | 2025-10-04 | Initial text checksum documentation — includes newspapers, oral histories, and treaties datasets. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Word Verified: Ensuring the Integrity of Kansas’s Historical Record.”*
📍 [`data/checksums/text/`](.) · Linked to the **Text STAC Collection**

</div>
