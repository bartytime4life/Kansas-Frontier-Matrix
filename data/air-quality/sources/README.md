---
title: "🌫️ Air Quality — Source Registry"
path: "data/air-quality/sources/README.md"
version: "v0.1.0"
last_updated: "2025-12-16"
status: "Draft"
doc_kind: "Data"
header_profile: "data-spec"
footer_profile: "standard"

tags:
  - data
  - air-quality
  - sources
  - metadata
  - provenance
  - etl
  - stac
  - dcat
  - prov

guardianship: "KFM Data Council"
domain: "air-quality"
audience:
  - contributors
  - data-engineering
  - research
  - governance-review

severity: "info"
estimated_read_time: "8–12 min"

related_docs:
  - "data/air-quality/ingestion/README.md"
  - "data/README.md"
  - "docs/patterns/provenance/README.md"
  - "docs/patterns/stac/README.md"

canonical_schema: "schemas/<source-metadata-schema>.json"
provenance_required: true
change_log_required: true

ai_generated: true
ai_generated_by: "GPT-5.2 Pro"
ai_generated_on: "2025-12-16"

license: "CC-BY 4.0"
classification: "public"
sensitivity: "low"

fair_category: "environmental-observations"
care_label: "general"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

kfm_version: "v11"
markdown_protocol_version: "KFM-MDP v11.2.6"
pipeline_contract_version: "KFM-PDC v11"
mcp_version: "MCP 2.0"

commit_sha: "<fill-at-merge>"
provenance_chain: []
semantic_document_id: "kfm-data-air-quality-sources-readme"
doc_uuid: "urn:kfm:doc:data:air-quality:sources:readme:v0.1.0"
event_source_id: "ledger:kfm:data:air-quality:sources:readme:v0.1.0"

ai_transform_permissions:
  - summarization
  - extraction
  - classification
  - qa
  - transformation

ai_transform_prohibited:
  - "unbounded-generation-without-citations"
  - "training-on-sensitive-cultural-data"
  - "location-doxxing"
---

# Air Quality — Source Registry

<p align="center">
  <strong>Purpose:</strong> Provide a single, auditable registry of upstream air-quality data sources (datasets, APIs, feeds, and archives) used by KFM’s air-quality ingestion pipelines—capturing licensing, access method, spatial/temporal coverage, and provenance hooks required for STAC/DCAT/PROV.
</p>

## 📘 Overview

This directory is the **authoritative “source-of-sources”** for the *air-quality* domain. It is intentionally **metadata-first**:

- **What belongs here:** machine-readable source descriptors (JSON/YAML as governed), human-readable source notes, and any minimal artifacts required to support provenance (e.g., citation strings, license notes).
- **What does not belong here:** raw downloads, intermediate processing outputs, or final processed datasets. Those belong in the data lifecycle staging areas (e.g., `data/raw/`, `data/work/`, `data/processed/`) and should be tracked with checksums and/or DVC pointers where applicable.

Quick links:

- Air quality ingestion SOP: `../ingestion/README.md`
- Data tree conventions: `../../README.md`
- Provenance pattern: `../../../docs/patterns/provenance/README.md`
- STAC pattern: `../../../docs/patterns/stac/README.md`

## 🗂️ Directory Layout

This folder should remain small and reviewable. Prefer **one file per upstream source**.

~~~text
data/
  air-quality/
    sources/
      README.md

      # Optional: a generated or maintained index that the ingestion pipeline reads first.
      sources.index.json

      # One source record per upstream provider/dataset/feed.
      <source-id>.source.json

      # Optional companion notes when a source needs human explanation (caveats, QA history).
      <source-id>.notes.md

      # Optional license clarification when upstream terms are complex or nonstandard.
      <source-id>.license.md
~~~

Relationship to the broader data lifecycle (context only):

~~~text
data/
  raw/          # raw ingests and/or DVC pointers (by domain)
  work/         # intermediate transforms and staging artifacts
  processed/    # canonical processed outputs used by APIs/UI
  stac/         # STAC Collections/Items for spatiotemporal assets
  reports/      # QA/QC outputs, summaries, profiling reports
  checksums/    # integrity hashes for artifacts that must be verifiable
  updates/      # incremental update payloads
~~~

## 🧭 Context

KFM treats “adding a dataset” as **adding a governed source record + a reproducible ingestion path**.

In practice, the flow for air-quality is:

1. **Define/Update source metadata** (this folder)
2. **Ingest** (domain ingestion SOP + scripts/config)
3. **Stage and validate** (work + QA checks + checksums)
4. **Publish** (processed outputs + STAC/DCAT + provenance)

### Why a dedicated source registry?

A source registry makes it possible to:

- enforce that every dataset shown in the UI/API has a **traceable origin**,
- generate catalogs (DCAT/STAC) consistently from a single metadata spine,
- run repeatable ingestion jobs that don’t embed undocumented URLs or access parameters in code.

### Source IDs

Use **stable, slug-like IDs**. The source ID becomes the filename stem and should not change unless the upstream source is fundamentally replaced.

Recommended pattern:

- `airq-<provider>-<dataset>-<scope>`
- Examples (illustrative only): `airq-epa-aqs-ambient`, `airq-local-sensors-pm25`

If a source is replaced, create a **new source ID** and link them via `replaces` / `supersedes` metadata rather than rewriting history.

## 📦 Data & Metadata

### Minimum required fields for each source record

The KFM workflow expects each source to include the basics needed to identify, access, license, and place the data in space/time. At minimum, capture:

- **Identity:** name, description, publisher/provider
- **Access:** landing page URL(s), API endpoint(s), auth requirements (if any), rate limits (if any)
- **License & attribution:** license name, license URL or text, attribution statement
- **Coverage:** spatial extent + temporal extent
- **Resolution & format:** spatial resolution (if applicable), temporal frequency, file formats/encodings
- **Domain semantics:** pollutants/variables measured, units, measurement method notes (if relevant)
- **Operational notes:** known limitations, QA caveats, update cadence, expected ingestion strategy

If an official JSON schema exists in `schemas/`, the schema is the source of truth. This README describes intent and review expectations.

### Example source record (template)

~~~json
{
  "id": "airq-<provider>-<dataset>-<scope>",
  "title": "<human title>",
  "description": "<what it is and why KFM uses it>",
  "publisher": {
    "name": "<org name>",
    "homepage": "<https://...>"
  },
  "access": {
    "landing_page": "<https://...>",
    "api_endpoint": "<https://...>",
    "access_type": "download|api|archive",
    "auth": "none|api_key|oauth|other",
    "rate_limits": {
      "notes": "<optional>"
    }
  },
  "license": {
    "name": "<license short name>",
    "url": "<https://...>",
    "attribution": "<required attribution text if any>"
  },
  "coverage": {
    "spatial_extent": {
      "type": "bbox",
      "bbox": [-102.051, 36.993, -94.588, 40.003],
      "crs": "EPSG:4326"
    },
    "temporal_extent": {
      "start": "<YYYY-MM-DD or ISO8601>",
      "end": "<YYYY-MM-DD or null>",
      "accrual_periodicity": "hourly|daily|monthly|annual|irregular|continuous"
    }
  },
  "data_characteristics": {
    "variables": [
      {
        "name": "<pollutant or metric>",
        "unit": "<unit>",
        "method": "<optional>"
      }
    ],
    "formats": ["csv", "json", "netcdf", "geotiff", "other"],
    "resolution": {
      "spatial": "<optional>",
      "temporal": "<optional>"
    }
  },
  "provenance": {
    "retrieval_strategy": "<brief: how we fetch it>",
    "expected_lineage": "<brief: how it becomes processed>",
    "citations": [
      "<citation string or bibliographic reference>"
    ]
  },
  "governance": {
    "classification": "public",
    "sensitivity": "low",
    "fair_category": "environmental-observations",
    "care_label": "general",
    "notes": "<any restrictions or special handling>"
  },
  "lifecycle": {
    "status": "active|deprecated|paused",
    "replaces": [],
    "superseded_by": []
  }
}
~~~

### Notes on licenses and terms

- **Do not assume “open data”** even if access is public. Record the license explicitly.
- If the upstream data has restrictions (e.g., redistribution limits, noncommercial terms), capture them clearly and flag for governance review before publishing processed outputs.

### Location sensitivity (precision control)

Air-quality data can include sensor coordinates. When sources include locations that might be sensitive (e.g., private property sensors, sensitive sites), document any required **precision reduction** or **masking rules** here so downstream steps can enforce them consistently.

## 🧪 Validation & CI/CD

Source records should be validated in CI the same way code is validated:

1. **Schema validation** (JSON schema or repo-approved validator)
2. **Linting** (format and required fields)
3. **Governance gates** (license presence, sensitivity labeling, CARE checks)
4. **Provenance checks** (presence of sufficient provenance hooks to generate DCAT/STAC/PROV)

Local expectations (adjust to repo tooling):

- Validate changed source records against the canonical schema in `schemas/`.
- Run the relevant “data + docs” checks used in CI prior to PR.
- If the change impacts ingestion behavior, run the ingestion pipeline in a minimal test mode and attach logs under the governed run-log location (e.g., `mcp/runs/`).

## 🌐 STAC, DCAT & PROV Alignment

KFM’s catalog strategy is intentionally multi-layered:

- **Human-readable:** README/docs describing sources and intent.
- **Machine-readable:** DCAT/STAC catalogs generated from authoritative metadata.
- **Lineage:** PROV records connecting raw → transforms → processed → published artifacts.

Recommended mapping:

- This source record → **DCAT Dataset** (and **DCAT DataService** when the source is primarily an API)
- Ingestion execution (job run) → **PROV Activity**
- Retrieved raw file(s) → **PROV Entity** (and checksum artifact if required)
- Processed air-quality product (GeoJSON/COG/tiles/etc.) → **STAC Item**
- Product grouping (e.g., “Air Quality — Annual PM2.5”) → **STAC Collection**

### API-first sources (DCAT DataService)

For real-time or endpoint-driven sources, represent the endpoint as a **DataService** and connect it to the dataset it serves. This helps downstream catalogs and UIs distinguish “downloadable files” from “queryable services.”

## ⚖ FAIR+CARE & Governance

This directory must remain aligned with:

- FAIR: source metadata should be findable and reusable with explicit licensing and identifiers.
- CARE: Indigenous data protection, cultural sensitivity, and sovereignty constraints must be honored.
- KFM governance: changes that affect publication scope, access rights, or sensitive locations require governance review.

If a source touches Indigenous lands, cultural heritage, or sensitive locations, include explicit notes in the source record and link to any required handling rules.

## 🕰️ Version History

| Date       | Version | Change summary                                      | Author |
|------------|---------|------------------------------------------------------|--------|
| 2025-12-16 | v0.1.0  | Initial README establishing air-quality source registry conventions | GPT-5.2 Pro |

---

[⬅ Root README](../../../README.md) ·
[🧱 Data Architecture](../../ARCHITECTURE.md) ·
[📂 Data Index](../../README.md) ·
[🌫️ Air Quality Domain](../README.md) ·
[🔌 Ingestion SOP](../ingestion/README.md) ·
[🏛️ Governance Charter](../../../docs/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/sovereignty/INDIGENOUS-DATA-PROTECTION.md)
