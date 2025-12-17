---
title: "Air Quality — Source: AirNow"
path: "data/air-quality/sources/airnow.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Source"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:air-quality:sources:airnow:v1.0.0"
semantic_document_id: "kfm-air-quality-source-airnow-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:sources:airnow:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Air Quality — Source: AirNow

## 📘 Overview

### Purpose
- Document AirNow as a governed source for air-quality observations/forecasts used by the KFM air-quality domain.
- Define ingestion constraints (cadence, validation, provenance capture) and safe handling (no secrets in repo).

### Scope
| In Scope | Out of Scope |
|---|---|
| AirNow near-real-time AQI observations | EPA AQS regulatory/certified datasets |
| AirNow forecasts (where available) | Non-AirNow sensor networks unless explicitly added |
| Kansas-focused pulls and/or national pulls | User-submitted sensor readings (not confirmed in repo) |

### Audience
- Primary: Data engineers and pipeline maintainers
- Secondary: Catalog/metadata maintainers, QA/validation, UI consumers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: AQI, reporting area, observation, forecast, provenance activity

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Air-quality governance | `data/air-quality/governance/api-lifecycle-tracking.md` | TBD | Lifecycle monitoring and response |
| AirNow source doc (this doc) | `data/air-quality/sources/airnow.md` | TBD | Source constraints + mapping |
| Pipelines | `src/pipelines/` | TBD | ETL + normalization (not confirmed in repo) |
| Catalog outputs | `data/stac/` | TBD | STAC/DCAT/PROV products |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Access method described without secrets
- [ ] Data fields documented (at least core observation fields)
- [ ] Validation rules and quality checks defined
- [ ] STAC/DCAT/PROV mapping guidance provided
- [ ] Update cadence and operational expectations stated

## 🗂️ Directory Layout

### This document
- `path`: `data/air-quality/sources/airnow.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Domain docs | `data/air-quality/` | Domain-local governance + sources |
| Sources | `data/air-quality/sources/` | Provider docs |
| Governance | `data/air-quality/governance/` | Lifecycle tracking |
| Raw/work/processed | `data/raw/`, `data/work/`, `data/processed/` | Pipeline staging |
| STAC/DCAT/PROV | `data/stac/` + `docs/data/` | Catalog outputs + mappings |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 air-quality/
    ├── 📁 governance/
    │   └── 📄 api-lifecycle-tracking.md
    └── 📁 sources/
        └── 📄 airnow.md
~~~

## 🧭 Context

### Background
AirNow provides public-facing air quality reporting (AQI) and forecasts aggregated from monitoring agencies.
Key operational notes (confirm against official provider documentation during implementation):
- Data may be **preliminary** and not the same as certified regulatory datasets.
- Update cadence is typically near-hourly in many contexts, but varies by location and product.

### Assumptions
- KFM will ingest:
  - AQI observations for key pollutants (at minimum: ozone and particulate matter categories where available),
  - forecasts where available for target geographies.
- KFM will store secrets (API keys) outside the repo.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No secrets in this repo: use environment variables or secret manager references only.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which AirNow endpoints/products will KFM use (zip-based, lat/long, area queries)? | TBD | TBD |
| What is the Kansas-focused strategy (zip list, bbox, counties)? | TBD | TBD |
| What is the permitted request rate for sustained ingest? | TBD | TBD |

### Future extensions
- Add additional pollutant fields/products if available and supported.
- Add a machine-readable “source registry” entry for AirNow (not confirmed in repo).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[AirNow API / data feeds] --> B[ETL + Normalization]
  B --> C[STAC Items + Collections]
  C --> D[DCAT Dataset Views]
  C --> E[PROV Lineage Bundles]
  C --> F[Neo4j Graph]
  F --> G[APIs]
  G --> H[React/Map UI]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Ingest as ETL Job
  participant AirNow as AirNow API
  participant Catalog as STAC/DCAT/PROV

  Ingest->>AirNow: Request observations/forecasts (API key via secrets)
  AirNow-->>Ingest: Response (JSON/CSV)
  Ingest->>Ingest: Normalize + validate + enrich (geography, timestamps)
  Ingest->>Catalog: Emit STAC + PROV
  Catalog-->>Ingest: Validation OK/Fail
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Observations (AQI) | JSON/CSV | AirNow API | Schema + range + completeness |
| Forecasts (AQI) | JSON/CSV | AirNow API | Schema + date consistency |
| Reference geographies (KS zips/counties) | CSV/GeoJSON | KFM curated or external | Geometry validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw pulls (optional) | JSON/CSV | `data/raw/air-quality/airnow/...` | checksums + retention |
| Normalized observations | Parquet/CSV | `data/processed/air-quality/airnow/observations/...` | schema-validated |
| Normalized forecasts | Parquet/CSV | `data/processed/air-quality/airnow/forecasts/...` | schema-validated |
| STAC items | JSON | `data/stac/air-quality/airnow/...` | STAC validator |
| PROV bundles | JSON-LD/Turtle | `data/stac/air-quality/airnow/...` | PROV profile |

### Core fields (observations) — baseline mapping
(Fields vary by endpoint/product; confirm exact names against provider output.)
| Field | Meaning | Validation |
|---|---|---|
| `DateObserved` | observation date | ISO date parse |
| `HourObserved` | observation hour | 0–23 |
| `LocalTimeZone` | timezone name/abbr | non-empty string |
| `ReportingArea` | reporting area/city name | non-empty string |
| `StateCode` | state abbreviation | `^[A-Z]{2}$` |
| `Latitude` | latitude | -90..90 |
| `Longitude` | longitude | -180..180 |
| `ParameterName` | pollutant identifier | allowlist (TBD) |
| `AQI` | AQI value | integer 0..500 (flag outliers) |
| `CategoryNumber` | AQI category id | integer in known set (TBD) |
| `CategoryName` | AQI category label | non-empty string |

### Sensitivity & redaction
- Default: public.
- If downstream joins could reveal protected locations or sovereignty-sensitive sites:
  - generalize coordinates (e.g., to county centroid) or suppress, per sovereignty policy.

### Quality signals
- Freshness: ingestion time within expected window
- Completeness: required fields present for each record
- Plausibility: AQI range checks; coordinates valid
- Consistency: timestamps monotonic for a reporting area; no duplicated keys beyond expected

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Proposed collections (IDs are placeholders until confirmed):
  - `air-quality-airnow-observations`
  - `air-quality-airnow-forecasts`
- Proposed STAC Item partitioning:
  - by day (and optionally by region subset, e.g., Kansas bbox)
- Assets:
  - `raw` (optional): raw provider response (if retained)
  - `normalized`: normalized table file (parquet/csv)
  - `metadata`: any schema/field mapping snapshot

### DCAT
- Dataset identifiers (proposed):
  - `dcat:Dataset` id: `kfm:dataset:air-quality:airnow`
- License mapping:
  - Use EPA/open-data licensing information if applicable; verify provider-specific constraints.
- Publisher/contact mapping:
  - Publisher: U.S. Environmental Protection Agency (or AirNow program) — verify.

### PROV-O
- `prov:Activity` (ingest run) should include:
  - startedAtTime / endedAtTime
  - tool version (pipeline version)
  - non-secret source identifier (e.g., base URL + endpoint name)
- `prov:used`:
  - a logical “AirNow API endpoint” entity (no API key)
- `prov:generated`:
  - normalized dataset entity + STAC item entity

### Versioning
- If outputs are regenerated for the same time slice:
  - produce a new STAC version and link predecessor/successor.
  - do not overwrite without lineage trace.

## 🧪 Validation & CI/CD

### Local validation steps (repeatable)
~~~bash
# TODO: replace with repo-actual commands (not confirmed in repo)
# 1) Fetch a small sample (dev key stored outside repo)
python -m src.pipelines.air_quality.airnow.pull_sample --region KS --date today

# 2) Validate schema + ranges
python -m src.pipelines.air_quality.validate --input data/work/air-quality/airnow/sample.json

# 3) Build STAC + validate
python -m src.catalog.build_stac --domain air-quality --source airnow
python -m src.catalog.validate_stac data/stac/air-quality/airnow
~~~

### Operational checks
- Scheduled “heartbeat” check:
  - endpoint reachable
  - non-empty response for a known test location (if permitted)
- Rate-limit compliance:
  - enforce client-side throttling/backoff
- Incident runbook:
  - mark pipeline as Degraded and fall back to cached/stale data thresholds (TBD)

## ⚖ FAIR+CARE & Governance

### FAIR
- Findable: source doc and governance doc in `data/air-quality/`
- Accessible: clear access method + credential handling guidance
- Interoperable: STAC/DCAT/PROV outputs
- Reusable: explicit validation rules + versioning behavior

### CARE / sovereignty
- If AirNow data is used alongside sensitive cultural heritage layers:
  - ensure that UI and derived outputs do not increase re-identification risk for protected places.

### Required approvals
- Data pipeline maintainer: TBD
- Governance reviewer: TBD
- Security reviewer (auth/secrets handling): TBD

## 🕰️ Version History
| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial AirNow source doc for air-quality domain | ChatGPT (drafting) |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
