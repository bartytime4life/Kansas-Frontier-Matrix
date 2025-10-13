<div align="center">


📜 Kansas Frontier Matrix — Text Source Manifests

data/sources/text/

Mission: Curate, document, and validate all external text-based datasets — digitized newspapers, OCR archives, oral histories, and treaty transcripts — that form the linguistic and narrative foundation of the Kansas Frontier Matrix (KFM).

</div>



⸻

🧭 Overview

The data/sources/text/ directory contains JSON manifests describing each text dataset integrated into KFM.
These manifests define provenance, licensing, access endpoints, and temporal coverage — forming a declarative registry for reproducible ingestion and validation.

Text sources empower:
	•	📰 Historical newspaper OCR & cleanup
	•	🗣️ Oral history transcript alignment
	•	📜 Treaty & legal text curation
	•	🧠 NLP enrichment (NER, temporal tagging, entity linking)
	•	🕰️ Knowledge Graph integration & time-aware discovery

⸻

🗂️ Directory Layout

data/sources/text/
├── README.md
├── loc_chronicling_america.json      # Library of Congress – historical newspapers
├── kshs_oral_histories.json          # Kansas Historical Society – oral histories
└── yale_avalon_treaties.json         # Yale Avalon Project – treaties & legal texts

🧩 Each manifest includes licensing, provenance, access details, and verification timestamps — ensuring long-term scholarly reproducibility.

⸻

🗞️ Example Manifest

{
  "id": "loc_chronicling_america",
  "title": "Library of Congress — Chronicling America",
  "provider": "Library of Congress",
  "description": "Digitized, OCR-processed newspaper pages (1789–1963).",
  "endpoint": "https://chroniclingamerica.loc.gov/",
  "access_method": "HTTP API",
  "license": "Public Domain (US Government)",
  "data_type": "text",
  "format": "JSONL",
  "spatial_coverage": "Kansas, USA",
  "temporal_coverage": "1854–1963",
  "update_frequency": "Monthly",
  "last_verified": "2025-10-13",
  "linked_pipeline": "src/pipelines/text_pipeline.py",
  "notes": "Used for OCR cleanup, NER extraction, and timeline construction."
}


⸻

🧮 Schema Essentials

🔖 Field	📘 Description
id	Unique short identifier (snake_case)
title	Full descriptive dataset name
provider	Institutional or organizational source
endpoint	Download/API URL or landing page
license	Explicit reuse rights (SPDX or text)
format	Primary data encoding (TXT, JSONL, HTML, CSV)
temporal_coverage	ISO or natural-language range
last_verified	YYYY-MM-DD provenance timestamp


⸻

🧭 System Context (GitHub-Safe Mermaid)

flowchart TD
  A["External Text Archives\nLOC · KSHS · Yale Avalon"] --> B["Source Manifests\n`data/sources/text/*.json`"]
  B --> C["ETL Pipeline\n`src/pipelines/text_pipeline.py`"]
  C --> D["Processed Text Corpora\n`data/processed/text/`"]
  D --> E["Derivatives\nTokenized · NER · Linked Entities"]
  D --> F["STAC Collections\n`data/stac/collections/text.json`"]
  F --> G["Knowledge Graph\nPeople ↔ Places ↔ Events ↔ Documents"]
  E --> H["Web UI\nSearch · Timeline · Document Viewer"]
%%END OF MERMAID%%

💡 Tip: Always terminate with %%END OF MERMAID%% to guarantee correct GitHub rendering.

⸻

⚙️ ETL Integration

Pipeline: src/pipelines/text_pipeline.py
Output: data/processed/text/

Workflow
	1.	🔍 Validate manifests (make sources-validate)
	2.	⬇️ Ingest via API or HTTP
	3.	🧹 Normalize (UTF-8, metadata, structure)
	4.	🧠 Enrich with NLP (NER, temporal parsing)
	5.	🪢 Link to STAC + Knowledge Graph
	6.	✅ Verify checksums & publish logs

⸻

🧩 Provenance Integration

Path	Purpose
data/raw/text/	Immutable source text files
data/processed/text/	Cleaned & NLP-ready corpora
data/stac/collections/text.json	STAC metadata registry
data/checksums/text/	SHA-256 verification
src/pipelines/text_pipeline.py	ETL orchestration layer


⸻

🧠 MCP Compliance Summary

MCP Principle	Implementation
Documentation-first	JSON manifest precedes ingestion
Reproducibility	Deterministic ETL parameters
Open Standards	JSON Schema · UTF-8 · STAC 1.0
Provenance	Manifest → Processed → STAC → Graph
Auditability	CI-enforced schema + checksum validation


⸻

🧾 Text Source Summary

Manifest	Provider	Description	Coverage	Format	Verified
loc_chronicling_america.json	LOC	OCR newspaper corpus	Kansas	JSONL	✅ 2025-10-13
kshs_oral_histories.json	KSHS	Oral history transcripts	Kansas	TXT	✅ 2025-10-13
yale_avalon_treaties.json	Yale Avalon	Historical treaties & legal texts	US / Global	HTML/TXT	✅ 2025-10-13


⸻

🧪 Validation & CI Commands

python src/utils/validate_sources.py data/sources/text/ \
  --schema data/sources/schema/source.schema.json

make text-sources      # fetch & stage
make text-validate     # schema + endpoint check
make text-stac         # STAC build/validate
make text-checksums    # hash verification

CI Hooks
	•	JSON Schema enforcement
	•	Endpoint availability
	•	License completeness
	•	Encoding normalization
	•	Changelog delta audit

⸻

🧾 Changelog

Version	Date	Highlights
v1.2	2025-10-13	Polished layout, added badges, semantic spacing, and CI hooks.
v1.1	2025-10-12	Added system diagram, validation workflow, and manifest examples.
v1.0	2025-10-04	Initial documentation release.


⸻

🏷️ Version Block

Component: data/sources/text/README.md
SemVer: 1.2.0
Spec Dependencies: MCP v1.0 · STAC 1.0
Last Updated: 2025-10-13
Maintainer: @bartytime4life


⸻


<div align="center">


✴️ “Voices of the past become data for the future.”

Kansas Frontier Matrix · Canonical registry of textual archives & narratives
📍 data/sources/text/

</div>