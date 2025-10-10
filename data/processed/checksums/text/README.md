<div align="center">

# 📜 Kansas Frontier Matrix — Text Checksums  
`data/processed/checksums/text/`

**Mission:** Preserve the **integrity, provenance, and reproducibility** of all processed **textual datasets** —  
including historical newspapers, oral histories, treaties, and transcripts — through verified SHA-256 checksums  
that uphold the principles of open, auditable scholarship under the Master Coder Protocol (MCP).

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../../../docs/)
[![License: Data](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)

</div>

---

## 📚 Overview

This directory contains **SHA-256 checksum files (`.sha256`)** for all processed **text datasets**  
in the Kansas Frontier Matrix (KFM).  

Each checksum acts as a **cryptographic signature** that ensures:
- 📜 **Integrity** — text files remain unmodified from their validated state.  
- 🔁 **Reproducibility** — AI/NLP and OCR workflows yield consistent outputs.  
- 🔗 **Provenance** — datasets remain traceable across source → metadata → STAC → publication.  
- ⚙️ **Auditability** — every checksum is continuously validated in CI/CD workflows.

Checksums are automatically generated during the **text ETL pipeline** (`make text`) and revalidated  
via GitHub Actions to ensure project-wide reproducibility and authenticity.

---

## 🗂️ Directory Layout

```bash
data/processed/checksums/text/
├── README.md
├── newspaper_articles_1850_1920.jsonl.sha256
├── oral_histories_transcripts.json.sha256
└── treaties_legislation_1820_1900.json.sha256

Each .sha256 corresponds 1:1 to its dataset in data/processed/text/.
CI workflows (stac-validate.yml) re-hash all text files during builds to verify their immutability.

⸻

🎯 Purpose

Objective	Description
Integrity Verification	Detects file corruption or unauthorized edits post-processing.
Reproducibility	Confirms deterministic AI/NLP and OCR pipeline outputs.
Provenance Tracking	Connects processed datasets with STAC metadata and source lineage.
CI Enforcement	Automated validation ensures MCP reproducibility and audit compliance.


⸻

🧮 Example .sha256 File

# File: newspaper_articles_1850_1920.jsonl.sha256
acbbfca1d5e56b2ef14898ce22d0837ffb7341a912d1b5206de91f08a64cc8b1  newspaper_articles_1850_1920.jsonl

This checksum authenticates the text dataset
data/processed/text/newspaper_articles_1850_1920.jsonl, ensuring it matches the last verified build artifact.

⸻

⚙️ Checksum Generation Workflow

Checksums are produced automatically after text ETL completion.

Makefile target

make text-checksums

Equivalent Python utility

python src/utils/generate_checksums.py data/processed/text/ --algo sha256

Steps
	1.	Locate processed text datasets (.txt, .json, .jsonl, .csv).
	2.	Compute SHA-256 hash using Python’s hashlib or GNU sha256sum --binary.
	3.	Write <filename>.sha256 files into this directory.
	4.	Validate these hashes automatically in CI/CD workflows.

💡 Use sha256sum --binary for platform-independent hash generation.

⸻

🔎 CI/CD Validation

Checksum validation runs automatically in GitHub Actions workflows for every build or PR.

Example validation command

sha256sum -c data/processed/checksums/text/*.sha256

If any mismatch is detected, the pipeline fails, blocking merges or deployments
until the affected dataset is reprocessed and revalidated.
All validation logs are archived to maintain a permanent MCP audit trail.

⸻

🧩 Integration with Metadata & STAC

Linked Component	Purpose
data/processed/metadata/text/	STAC Items reference .sha256 for dataset integrity.
src/pipelines/text/text_pipeline.py	Automates hash generation and verification within ETL.
.github/workflows/stac-validate.yml	CI workflow verifying checksum and STAC metadata compliance.
data/stac/text/	STAC catalog embeds SHA-256 digests in assets.checksum:sha256.


⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation
Documentation-first	Each dataset has corresponding .sha256 and metadata record.
Reproducibility	Hashes confirm deterministic NLP/OCR results and unchanged artifacts.
Open Standards	SHA-256 (FIPS 180-4) ensures robust cross-platform consistency.
Provenance	Hashes link datasets across metadata, STAC, and source archives.
Auditability	CI/CD workflows enforce continuous verification and changelog transparency.


⸻

🧮 Maintenance & Best Practices
	•	🔄 Checksum Refresh: Regenerate checksums after reprocessing or NLP pipeline updates.
	•	🧾 Naming Consistency: Ensure checksum filenames match exactly with their dataset names.
	•	📜 Version Tracking: Update mcp_provenance fields in STAC/metadata after regenerating hashes.
	•	🧪 Bulk Validation: Maintain a _manifest_all.sha256 for large-scale text audits.
	•	⚙️ Automation: Add pre-commit hooks to prevent stale or missing checksums in commits.

⸻

📅 Version History

Version	Date	Summary
1.0.1	2025-10-10	Upgraded README with CI/CD integration, MCP best practices, and workflow steps.
1.0.0	2025-10-04	Initial text checksum documentation and validation manifests.


⸻

📖 References
	•	GNU Coreutils — SHA utilities: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html
	•	STAC 1.0 Specification: https://stacspec.org
	•	JSON Schema: https://json-schema.org
	•	MCP Standards (KFM): ../../../../docs/standards/
	•	Open Data Provenance: https://www.nature.com/articles/s41597-019-0193-2

⸻


<div align="center">


Kansas Frontier Matrix — “Every Word Verified: Integrity in the Historical Record.”
📍 data/processed/checksums/text/ · Linked to the Text STAC Collection

</div>
```