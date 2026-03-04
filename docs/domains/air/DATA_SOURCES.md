<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2a2f4f5c-0a21-4c1e-9fb1-cc19b0c0a5d4
title: Air Domain Data Sources
type: standard
version: v1
status: draft
owners: ["TBD"]
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related: [
  "docs/domains/air/README.md",
  "docs/events/environmental/soil-air-ingestion-overview.md",
  "mcp/sops/climate_downscaling.md",
  "data/registry/sources/",
  "tools/validators/"
]
tags: ["kfm","air","data-sources","stac","dcat","prov"]
notes: ["Evidence-labeled register (CONFIRMED/PROPOSED/UNKNOWN). Update quarterly or when adding a new upstream feed."]
[/KFM_META_BLOCK_V2] -->

# Air Domain Data Sources
One place to track *what we ingest for air*, *why*, and *how it is governed*.

> **IMPORTANT (KFM invariants):**
> - **UI/clients MUST NOT access DB/storage directly**; all reads/writes cross governed APIs + policy boundary.
> - **RAW → WORK → PROCESSED → PUBLISHED**: no promotion without identity+schema+license+sensitivity+provenance+checksums+run receipt.
> - **Observed vs modeled MUST remain distinct and traceable** (fail-closed if provenance is missing).

---

## Impact
- **Status:** draft (active editing)
- **Owners:** TBD
- **Badges:** ![status](https://img.shields.io/badge/status-draft-lightgrey) ![policy](https://img.shields.io/badge/policy-public-brightgreen) ![domain](https://img.shields.io/badge/domain-air-blue)
- **Quick nav:** [Scope](#scope) · [Where it fits](#where-it-fits) · [Data source register](#data-source-register) · [STAC-DCAT mapping](#stac--dcat-mapping) · [Governance requirements](#governance-requirements) · [Checklist](#checklist)

---

## Scope
**In scope (Air domain):**
- Ambient air quality: **PM2.5, O₃, NO₂, PM10** (and related pollutants/metadata).
- Air quality *products*: AQI/NowCast-like near-real-time signals (when explicitly sourced and labeled).
- Atmospheric context layers used to interpret air outcomes (meteorology, smoke/aerosols, satellite column proxies), **only when kept distinct** from ground observations.

**Out of scope (belongs elsewhere):**
- Pure weather/climate baselines as a primary product (see `docs/domains/climate/` if present).
- Health outcomes datasets (see `docs/domains/health/` if present).
- Any scraping or acquisition without explicit license/terms clarity (fail-closed; do not ingest).

---

## Where it fits
- **Path:** `docs/domains/air/DATA_SOURCES.md`
- **Upstream:** `data/registry/` connectors + source manifests; domain pipelines under `src/pipelines/`
- **Core storage surfaces:** `data/raw/`, `data/work/`, `data/processed/`, `data/published/`
- **Catalog surfaces:** `data/catalog/{stac|dcat|prov}/` (or equivalent)
- **Downstream:** governed API → UI layers (Map Explorer / Timeline / Story / Focus Mode)

---

## Air ingestion overview diagram

~~~mermaid
flowchart LR
  S["Upstream sources"] --> R["RAW snapshots\nimmutable blobs"]
  R --> W["WORK normalize\nschema, units, ids"]
  W --> P["PROCESSED\nparquet or raster"]
  P --> C["PUBLISHED catalogs\nSTAC + DCAT + PROV"]
  C --> G["Graph ingest\nNeo4j entities"]
  C --> A["Governed API\npolicy boundary"]
  A --> U["UI + Focus Mode\ncite evidence"]
~~~

---

## Data source register

### Conventions used in this register
- **Claim status** (required): `CONFIRMED` / `PROPOSED` / `UNKNOWN`
- **Class**: `Observed` / `Modeled` / `Satellite`
- **Auth**: `None` / `Key` / `Account`
- **Cadence**: best-known schedule; if unclear, mark `UNKNOWN`

> NOTE: “CONFIRMED” here means **explicitly documented in current KFM materials** as part of the air domain intake pattern (not necessarily deployed in your current runtime environment).

---

### Core sources (documented)

| Source | Class | Role (what it is used for) | Delivery | Auth | Cadence | Canonical KFM Collection ID (recommended) | Claim status |
|---|---|---|---|---|---|---|---|
| **EPA AQS** | Observed | Regulatory-grade historical rows + QA flags (source-of-truth for compliance/trends) | REST API / Data Mart | Key | Nightly (historical), hourly (recent) | `air-quality-aqs-ground` | **CONFIRMED** |
| **AirNow** | Observed | Near-real-time AQI/public health signal; NowCast-like current conditions | Auth REST API | Key | Every ~15 minutes | `air-quality-airnow-realtime` | **CONFIRMED** |
| **OpenAQ (v3 API)** | Observed | Harmonized multi-network bridge; comparative analytics; never regulatory | REST API (JSON) | UNKNOWN | Hourly | `air-quality-openaq-global` | **CONFIRMED** |
| **CAMS NRT** | Modeled | Chemical transport forecasts / gap-filling context; stored as modeled (not mixed) | Cloud object storage (GRIB/NetCDF) | UNKNOWN | Per forecast cycle | `air-quality-cams-forecast` | **CONFIRMED** |
| **NOAA HRRR** | Modeled | Mesoscale meteorology + smoke/aerosols context; plume tracking | Cloud GRIB2 | UNKNOWN | Hourly | `air-quality-hrrr-grid` | **CONFIRMED** |
| **Sentinel‑5P (Level‑2)** | Satellite | Column/atmospheric context + spatial completeness; not directly converted to surface AQI | STAC-native catalogs + NetCDF L2 | UNKNOWN | Per orbit | `air-quality-s5p-l2` | **CONFIRMED** |

---

### Secondary / recommended additions

| Source | Class | Why it’s useful | Primary risks / governance notes | Claim status |
|---|---|---|---|---|
| **PurpleAir** | Observed (low-cost) | Dense spatial coverage; useful when corrected + QC’d; supports anomaly/event detection | Must apply documented correction + QC (humidity effects, A/B channel agreement); do not label as regulatory | **PROPOSED** |
| **KDHE monitoring plans + station metadata** | Observed (metadata) | Helps map Kansas station IDs to AQS identifiers; adds network context | Confirm distribution terms; treat as metadata reference; don’t ingest PII | **PROPOSED** |
| **NOAA NAQFC / CMAQ outputs** | Modeled | Short-horizon PM2.5/O₃ forecasts; supports forecasting layers and fusion | Must remain modeled; document bias correction methods; store grids in cloud-native formats | **PROPOSED** |

---

## KFM data modeling
### Graph model (air observations)
**CONFIRMED:** KFM normalizes OpenAQ-derived readings into a harmonized graph schema:
- `AirObservation` → links to `SensorNode` → links to `SourceNetwork`
- `AirObservation` also links to `ParameterUnit` to enforce consistent units.

This model supports graph queries and cross-domain joins (events, places, timelines) without losing provenance.

### Modeled fields must be separate
**CONFIRMED:** Modeled contributions (e.g., CAMS NRT) are stored as distinct modeled entities (example label: `ModeledAirField`, with `source_id="cams-nrt"`) and linked via `DERIVED_FROM` rather than merged into observations.

---

## STAC + DCAT mapping
### Recommended STAC collection mapping (air domain)
**CONFIRMED:** Use distinct Collections per source class so clients can filter and so policy can enforce “observed vs modeled.”

Examples (recommended IDs):
- `air-quality-aqs-ground` (Point time series)
- `air-quality-airnow-realtime` (Point snapshots)
- `air-quality-openaq-global` (Harmonized points)
- `air-quality-cams-forecast` (Raster)
- `air-quality-hrrr-grid` (Raster)
- `air-quality-s5p-l2` (Swath raster)

### Minimum STAC Item fields (air domain)
Required (fail-closed if missing):
- `datetime`, `geometry`, `assets.data`, `assets.metadata`
- `properties.pollutant`, `properties.units`, `properties.quality_flag`

---

## Governance requirements
### Required metadata per source (promotion gate)
Every source ingestion MUST produce (at minimum):
- **Identity:** stable `dataset_id`, `dataset_version`
- **License / rights:** SPDX ID (or explicit license URL) — **fail-closed if ambiguous**
- **Sensitivity label:** public/restricted (default-deny until classified)
- **Checksums:** sha256 (or better) for every persisted artifact
- **Provenance:** run receipt (who/what/when/why), with inputs + transforms + tool versions
- **Validation outputs:** explicit thresholds (QC rules, schema validation)
- **Auditability:** immutable run record + policy decisions

### Quality rules (domain-specific)
- AQS: treat QA/certification flags as first-class; do not “upgrade” without documented basis.
- AirNow: treat as *near-real-time* signal; do not represent as regulatory-grade.
- PurpleAir (if added): correction + QC required; store correction method + parameters as provenance.

### Access + secrets
- No keys in repo. Use environment variables and secret managers.
- Respect rate limits and use backoff; emit telemetry on retries.

---

## Acceptable inputs
This doc accepts:
- New/updated upstream source definitions (API/storage endpoint, terms, cadence)
- Linkouts to connector manifests in `data/registry/`
- Source-specific QC requirements and promotion gates

---

## Exclusions
Do not add here:
- “Random list of possible datasets” without license/terms, cadence, and governance notes
- Any source requiring scraping or bypassing access controls
- Any instructions to bypass rate limits or authentication

---

## Checklist
### Adding a new air source (Definition of Done)
- [ ] Source has a **registry entry** (connector/manifest) with endpoint + auth + cadence.
- [ ] License/terms confirmed and recorded (SPDX or explicit URL). Fail-closed otherwise.
- [ ] Sensitivity label assigned (public/restricted).
- [ ] RAW snapshot storage is immutable + checksum’d.
- [ ] WORK normalization outputs stable schema + unit harmonization.
- [ ] PROCESSED artifacts created in cloud-native format (GeoParquet, NetCDF-to-zarr, etc as appropriate).
- [ ] STAC Item/Collection emitted and validated.
- [ ] DCAT Dataset emitted and validated.
- [ ] PROV lineage emitted and validated.
- [ ] Run receipt emitted (spec hash + artifact digests + tool versions).
- [ ] Policy gates wired in CI (deny promotion if any required surfaces missing).
- [ ] Map/UI integration only via governed APIs.

---

## Appendix
<details>
<summary>Suggested dataset_id patterns (pseudocode)</summary>

~~~text
kfm:air:aqs:site/<aqs_site_id>:param/<code>
kfm:air:airnow:area/<reporting_area_id>:param/<name>
kfm:air:openaq:location/<location_id>:param/<parameter>
kfm:air:cams:field/<variable>:cycle/<run_time>:lead/<fh>
kfm:air:hrrr:field/<variable>:cycle/<run_time>:lead/<fh>
kfm:air:s5p:product/<gas_or_index>:orbit/<orbit_id>
~~~

</details>

---

Back to top: [Air Domain Data Sources](#air-domain-data-sources)
