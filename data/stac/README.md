<div align="center">


📜 Kansas Frontier Matrix — Text Source Manifests

data/sources/text/

Mission: Curate, document, and validate all external text-based datasets—digitized newspapers, OCR archives, oral histories, treaty transcripts—that form the linguistic and narrative backbone of the Kansas Frontier Matrix (KFM).

</div>



⸻

📚 Overview

data/sources/text/ contains JSON manifests that declare provenance, licensing, access endpoints, temporal coverage, and validation metadata for every text source integrated into KFM.
These manifests drive the ETL, enforce reproducibility, and link outputs to STAC and the Knowledge Graph.

They power:
	•	OCR cleanup + normalization (UTF-8, diacritics, Unicode NFC)
	•	NLP enrichment (tokenization, NER, coreference, date normalization)
	•	Treaty & land-cession document tracking
	•	Oral history alignment with people/places/events
	•	STAC-linked provenance for time-aware discovery

⸻

🗂️ Directory Layout

data/sources/text/
├── README.md
├── loc_chronicling_america.json      # Library of Congress historical newspapers
├── kshs_oral_histories.json          # Kansas Historical Society transcripts
└── yale_avalon_treaties.json         # Yale Avalon Project — treaties & legal texts

Note: Every manifest includes dataset identifiers, licensing, provenance, verification timestamps, and expected formats—enabling deterministic ingestion and audit-ready lineage.

⸻

🗞️ Example Manifest (authoritative pattern)

{
  "id": "loc_chronicling_america",
  "title": "Library of Congress — Chronicling America Historical Newspaper Corpus",
  "provider": "Library of Congress (LOC)",
  "description": "Digitized and OCR-processed newspaper archives spanning 1789–1963.",
  "endpoint": "https://chroniclingamerica.loc.gov/",
  "access_method": "HTTP API",
  "license": "Public Domain (US Government)",
  "license_url": "https://www.loc.gov/legal/",
  "data_type": "text",
  "format": "JSONL",
  "spatial_coverage": "Kansas, USA",
  "temporal_coverage": "1854–1963",
  "update_frequency": "Monthly",
  "last_verified": "2025-10-12",
  "stac_collection": "data/stac/collections/text.json",
  "linked_pipeline": "src/pipelines/text_pipeline.py",
  "contact": "digital@loc.gov",
  "checksum_policy": "sha256 for downloaded bundles",
  "notes": "NLP: NER, sentence segmentation, and temporal tagging for timeline construction."
}

🔎 Schema essentials (../schema/source.schema.json)
	•	Required: id, title, provider, endpoint, license, data_type, format, temporal_coverage, last_verified
	•	Recommended: spatial_coverage, update_frequency, stac_collection, linked_pipeline, checksum_policy, license_url, contact

⸻

🧭 System Context (GitHub-safe Mermaid)

flowchart TD
  A["External Text Archives\nLOC · KSHS · Yale Avalon"] --> B["Source Manifests\n`data/sources/text/*.json`"]
  B --> C["ETL Pipeline\n`src/pipelines/text_pipeline.py`"]
  C --> D["Processed Text Corpora\n`data/processed/text/`"]
  D --> E["Derivatives\nTokenized · NER · Linked Entities"]
  D --> F["STAC Collections\n`data/stac/collections/text.json`"]
  F --> G["Knowledge Graph\nPeople ↔ Places ↔ Events ↔ Documents"]
  E --> H["Web UI\nSearch · Timeline · Document Viewer"]
%%END OF MERMAID%%

Mermaid render-lock: The final line must be exactly %%END OF MERMAID%% on its own line (with the percent signs on both sides).

⸻

⚙️ ETL Integration

Pipeline: src/pipelines/text_pipeline.py
Output: data/processed/text/

Workflow
	1.	Validate manifests against schema → make sources-validate
	2.	Ingest via HTTP/API, persist to data/raw/text/ (immutable)
	3.	Normalize encodings/line endings/metadata → UTF-8 + NFC
	4.	Enrich with NLP (tokenize, NER, temporal parsing, entity linking)
	5.	Register STAC Items/Collections and Graph edges (doc→entity)
	6.	Verify checksums, write provenance logs, publish to CI artifacts

⸻

🧪 Validation & CI

Manual validation

python src/utils/validate_sources.py data/sources/text/ \
  --schema data/sources/schema/source.schema.json

Make targets

make text-sources         # fetch + stage
make text-validate        # schema + endpoint checks
make text-stac            # build/validate STAC items
make text-checksums       # sha256 for processed corpora

CI gates (summary)
	•	JSON Schema validation (fail on required-missing/type mismatch)
	•	Endpoint liveness + HTTP 2xx/3xx checks
	•	License presence & attribution checks
	•	Encoding/normalization scan (UTF-8, NFC)
	•	Changelog enforcement on manifest edits

GitHub Actions (snippet)

name: text-sources-validate
on:
  pull_request:
    paths: [ "data/sources/text/**" ]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: python src/utils/validate_sources.py data/sources/text/ \
               --schema data/sources/schema/source.schema.json
      - run: make text-stac


⸻

🧩 Provenance Integration

Component	Purpose
data/raw/text/	Immutable source files (as-fetched)
data/processed/text/	Cleaned corpora ready for NLP/analysis
data/stac/collections/text.json	Discovery + asset metadata (time/space/provenance)
data/checksums/text/	SHA-256 manifests for reproducibility
src/pipelines/text_pipeline.py	Orchestrates ingestion → enrich → publish → validate


⸻

🧠 AI / NLP Enrichment Profile (reference)
	•	Tokenization: sentence + word (Punkt or spaCy default)
	•	NER: person/org/place/treaty/legal refs; custom Gazetteer boost for Kansas entities
	•	Temporal: ISO-8601 normalization, fuzzy date ranges, document date vs. event date disambiguation
	•	Linking: entity IDs resolve to Knowledge Graph nodes; STAC relations mirror doc↔asset ties
	•	Confidence: store per-span confidence; surface uncertainty in UI tooltips

⸻

🧠 MCP Compliance Checklist (pre-merge)
	•	Documentation before data/code (docs-first)
	•	Schema-valid JSON manifests present and passing CI
	•	Repro steps (make targets) verified locally
	•	STAC items/collections updated and validated
	•	Checksums written for processed corpora
	•	CHANGELOG updated; version bumped (semver)
	•	Mermaid ends with %%END OF MERMAID%%

⸻

🧾 Text Source Summary

Manifest File	Provider	Description	Coverage	Format	Verified
loc_chronicling_america.json	LOC	OCR-based historical newspapers	Kansas	JSONL	✅ 2025-10-12
kshs_oral_histories.json	KSHS	Transcribed oral histories and interviews	Kansas	TXT	✅ 2025-10-12
yale_avalon_treaties.json	Yale Avalon	Treaty and historical legal documents	National/Global	HTML/TXT	✅ 2025-10-12


⸻

❓ FAQ (quick hits)
	•	Why JSON manifests? Deterministic, reviewable, CI-enforced ingestion configs.
	•	How do we handle broken endpoints? CI fails with actionable message; fall back to archived mirrors if specified.
	•	Mixed encodings? All inputs normalized to UTF-8/NFC; non-conforming inputs rejected with reason.

⸻

🧾 Changelog

Version	Date	Summary
v1.2	2025-10-13	Added MCP checklist, AI/NLP profile, CI snippet, schema essentials; tightened provenance.
v1.1	2025-10-12	Added system diagram, validation workflow, and LOC/KSHS/Yale manifest examples.
v1.0	2025-10-04	Initial creation of text source manifest documentation.


⸻

🏷️ Version Block

Component: data/sources/text/README.md
SemVer: 1.2.0
Spec Dependencies: MCP v1.0 · STAC 1.0
Last Updated: 2025-10-13
Maintainer: @bartytime4life


⸻


<div align="center">


Kansas Frontier Matrix — “Voices of the past become data for the future.”
📍 data/sources/text/ · Canonical registry of historical & linguistic sources powering KFM’s narrative intelligence.

</div>
