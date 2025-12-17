---
title: "CAMS NRT (Copernicus) — Air Quality Source"
path: "data/air-quality/sources/cams-nrt.md"
version: "v0.1.0"
last_updated: "2025-12-17"
release_stage: "Draft / Proposed"
lifecycle: "Active (Iterating)"
review_cycle: "Quarterly · Data Stewardship"
content_stability: "evolving"

status: "Draft"
doc_kind: "DataSpec"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "air-quality"
  applies_to:
    - "data/air-quality/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; follow standard redaction rules if any downstream joins add sensitive fields)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Review on major Copernicus ADS/API changes, or KFM v12 migration"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256-if-any>"

signature_ref: "././releases/<release-tag>/signature.sig"
attestation_ref: "././releases/<release-tag>/slsa-attestation.json"
sbom_ref: "././releases/<release-tag>/sbom.spdx.json"
manifest_ref: "././releases/<release-tag>/manifest.zip"

telemetry_ref: "././releases/<release-tag>/focus-telemetry.json"
telemetry_schema: "././schemas/telemetry/markdown-protocol-v11.2.6.json"
energy_schema: "././schemas/telemetry/energy-v2.json"
carbon_schema: "././schemas/telemetry/carbon-v2.json"

governance_ref: "governance/ROOT-GOVERNANCE.md"
ethics_ref: "faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "data/air-quality/sources/cams-nrt.md@v0.1.0"
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"

provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "././schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "././schemas/shacl/kfm-markdown-protocol-v11.2.6.shacl.ttl"

story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:data:air-quality:source:cams-nrt:v0.1.0"
semantic_document_id: "kfm-data-air-quality-source-cams-nrt"
event_source_id: "ledger:kfm:data:air-quality:source:cams-nrt:v0.1.0"
doc_integrity_checksum: "sha256:<calculated-in-ci>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "metadata-extraction"
  - "summary"
  - "layout-normalization"
  - "a11y-adaptations"
  - "table-reformatting"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - "metadata-extraction"
    - "summary"
    - "layout-normalization"
    - "a11y-adaptations"
  prohibited:
    - "speculative-additions"
    - "unverified-architectural-claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "secret-scan"
  - "pii-scan"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

fencing_profile: "outer-backticks-inner-tildes-v1"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🌬️ CAMS NRT (Copernicus) — Air Quality Source

**Path:** `data/air-quality/sources/cams-nrt.md`  
**Upstream:** Copernicus Atmosphere Monitoring Service (CAMS) via the Copernicus Atmosphere Data Store (ADS)  
**KFM role:** ETL source → STAC/DCAT/PROV → Graph/API → UI/Focus Mode

<img alt="doc_kind" src="https://img.shields.io/badge/doc_kind-DataSpec-0b5563?style=for-the-badge" />
<img alt="domain" src="https://img.shields.io/badge/domain-air--quality-1f6feb?style=for-the-badge" />
<img alt="status" src="https://img.shields.io/badge/status-Draft-6e7781?style=for-the-badge" />
<img alt="protocol" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-7c3aed?style=for-the-badge" />

</div>

---

> **Purpose (required):** Document the **CAMS Near‑Real‑Time (NRT)** global atmospheric composition forecast dataset as a **KFM air‑quality source**, including:  
> (1) what it is, (2) how to access it safely, (3) the minimum metadata we must preserve, and (4) how to align outputs with **STAC/DCAT/PROV**.

## 📘 Overview

CAMS (Copernicus Atmosphere Monitoring Service) provides **global atmospheric composition forecasts** (reactive trace gases, aerosols, greenhouse gases, and related fields). The “NRT” designation is typically used to indicate **near‑real‑time availability** for the most recent window of forecast products, alongside “archived” products with a delay.

**Why KFM uses this source (intended):**
- Provide a **modeled atmospheric composition / air‑quality baseline** to contextualize Kansas events (dust, smoke transport, seasonal haze, etc.).
- Support **spatiotemporal overlays** in the KFM UI when observational station coverage is sparse.
- Provide a consistent, standards‑friendly dataset for downstream STAC/DCAT cataloging and provenance (PROV‑O).

**Key upstream facts (from provider documentation):**
- CAMS global forecasts are generated **twice daily** and include **>50 chemical species** and **7 aerosol types**.
- The ADS “Global atmospheric composition forecasts” dataset is provided on a **0.4° × 0.4°** global grid.
- The dataset includes commonly used air‑quality fields such as **particulate matter (PM1/PM2.5/PM10)** as well as trace gases (e.g., O₃, NO₂, CO).
- Data is **open and free of charge**, with a **CC‑BY** license for this dataset and a DOI for citation.

### Upstream canonical identifiers

| Item | Value |
|---|---|
| ADS dataset id (used in API requests) | `cams-global-atmospheric-composition-forecasts` |
| Dataset DOI | `10.24381/04a0b097` |
| Dataset license (upstream) | CC‑BY (see ADS dataset page) |

### NRT vs archived (operational note)

Provider guidance distinguishes:
- **Real‑Time (NRT) access** for the *latest ~3 days* of CAMS global atmospheric composition forecasts.
- **Archived analysis/forecast** access for historical backfill, typically published with a delay (e.g., ~5 days).

KFM can use **NRT** for “current context” layers and **archived** for reproducible historical slices.

## 🗂️ Directory Layout

~~~text
data/
└── 🌬️ air-quality/ — Air-quality domain datasets & runbooks
    ├── 📁 ingestion/ — ETL configs, runbooks, schedules (domain-level)
    │   └── 📄 README.md — How air-quality ingestions run in KFM (entry point)
    └── 📁 sources/ — Source registry (human docs + source contracts)
        ├── 📄 README.md — Source index + naming rules (entry point)
        └── 📄 cams-nrt.md — CAMS NRT (Copernicus ADS) source spec (this file)
~~~

**Naming contract (recommended):**
- Source slug: `cams-nrt`
- Use the slug consistently in:
  - STAC Collection id (e.g., `air-quality-cams-nrt`) *(exact id not confirmed in repo; pick a stable id and keep it forever)*  
  - PROV activity ids (e.g., `prov:Activity/kfm:ingest:cams-nrt:<run-id>`)  
  - Any downstream graph nodes / API routes

## 🧭 Context

### Pipeline placement

This source belongs to the **ETL stage** of the KFM pipeline, and must emit:
1. **STAC** (Items/Collections) describing the derived KFM assets,
2. **DCAT** views (dataset/distribution metadata) for catalog interoperability,
3. **PROV‑O** lineage for reproducibility and auditability.

KFM’s pipeline then indexes these into the **Neo4j knowledge graph**, exposes them through **APIs**, and finally renders them in **React/MapLibre** experiences (including Focus Mode).

### Access requirements (upstream)

To use ADS programmatically:
- You need an ADS account and a **personal access token**.
- You must accept dataset **Terms & Conditions** once before API calls will succeed.
- The ADS UI can generate an API request snippet (“Show API request code”) that is safest to copy into KFM scripts/configs.

> **Security note:** Never commit tokens/keys into the KFM repo. Use local `~/.cdsapirc` for dev and GitHub Actions secrets (or equivalent) for CI.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  ADS["Copernicus ADS (CAMS)"] -->|retrieve (cdsapi)| RAW["Raw pull (zip/grib/netcdf)"]
  RAW --> XFORM["Transform: subset + convert + QA"]
  XFORM --> STAC["STAC Items/Collections"]
  XFORM --> DCAT["DCAT Dataset/Distributions"]
  XFORM --> PROV["PROV lineage"]
  STAC --> GRAPH["Neo4j graph"]
  DCAT --> GRAPH
  PROV --> GRAPH
  GRAPH --> API["KFM APIs"]
  API --> UI["React/MapLibre UI + Focus Mode"]
~~~

## 📦 Data & Metadata

### Typical content & dimensions

The provider tutorial demonstrates that downloaded NetCDF assets can include dimensions such as:
- `forecast_reference_time` (model initialization time)
- `forecast_period` (lead time)
- `latitude`, `longitude`
and may provide a computed `valid_time` coordinate.

This shape matters for how we mint STAC Items (see alignment section).

### KFM‑relevant variables (examples)

The ADS parameter catalog includes (non‑exhaustive):
- **Particulate matter:** PM1, PM2.5, PM10
- **Trace gases:** O₃ (ozone), NO₂ (nitrogen dioxide), CO (carbon monoxide), SO₂ (sulphur dioxide) *(availability depends on level/type selection)*
- **Aerosol diagnostics:** aerosol optical depth (AOD) and related fields

> **Implementation note:** API “variable” identifiers (machine strings) should be sourced from the ADS download form or generated API request code to avoid typos.

### Formats & units

Supported formats commonly include:
- `netcdf_zip` (NetCDF inside a zip)
- GRIB variants (depending on selected options)

Units can vary by variable and level; do not assume “µg/m³” without verifying the variable attributes in the downloaded file.

### References (upstream)

- ADS dataset page (download + citation metadata): `https://ads.atmosphere.copernicus.eu/datasets/cams-global-atmospheric-composition-forecasts`
- ADS API access overview: `https://ads.atmosphere.copernicus.eu/how-to-api`
- ECMWF CAMS global data access note (NRT vs archived): `https://confluence.ecmwf.int/display/CKB/Global+CAMS+data`

## 🌐 STAC, DCAT & PROV Alignment

### STAC strategy (recommended patterns)

Because CAMS files typically contain **many lead times** per initialization, there are two common STAC modeling approaches:

**Option A — One Item per forecast initialization (`forecast_reference_time`)**
- `Item.datetime` = forecast initialization time
- Assets:
  - one NetCDF/GRIB file containing all lead times for selected variables
- Pros: fewer Items, simpler sync
- Cons: searching by “valid time” is harder unless you also index derived slices

**Option B — One Item per valid time (`valid_time`)**
- `Item.datetime` = valid time (init + lead)
- Assets:
  - per-lead-time slices (or references into a chunked store)
- Pros: time-search friendly
- Cons: many Items, more processing

> **KFM guidance:** Choose one option per domain and keep it stable for graph/API compatibility. If switching strategies, version the Collection and link via STAC Versioning + PROV revision relations.

### DCAT view

At minimum, DCAT should preserve:
- Dataset title/description/keywords
- License & attribution requirements
- Distributions for:
  - upstream access (ADS dataset id and landing page)
  - KFM STAC Collection endpoint (static or STAC API)
  - any KFM API endpoints that serve derived products

### PROV lineage (minimum viable)

For each ETL run:
- `prov:Activity`: `kfm:ingest:cams-nrt:<run-id>`
- `prov:used`: the upstream dataset reference (ADS dataset id + retrieval parameters snapshot)
- `prov:generated`: KFM output assets + STAC metadata records
- Record:
  - code version (`commit_sha`)
  - request parameters (stored without secrets)
  - file checksums for artifacts

## 🧠 Story Node & Focus Mode Integration

This source is best used as **contextual evidence**, not as a primary “on‑the‑ground measurement” record.

Suggested Story Node / Focus Mode uses:
- **Environmental context layers:** modeled PM2.5 / PM10 fields during multi‑day dust or smoke episodes.
- **Seasonality narratives:** compare seasonal patterns (e.g., winter inversions vs summer ozone season) using consistent gridded model output.
- **Cross‑source triangulation:** combine CAMS modeled fields with station observations (if present) to identify gaps and uncertainty.

> **Governance requirement:** Focus Mode narratives must not assert causal claims (“X caused Y”) without corroborating evidence. Use CAMS as a supporting layer and retain provenance links to the specific run/time slice.

## 🧱 Architecture

### Minimal ingestion recipe (provider‑aligned, safe)

1. **Install `cdsapi`** (ADS docs specify a minimum version).
2. Create `~/.cdsapirc` (local dev only) or use environment‑based configuration in CI.

Example `.cdsapirc` (do **not** commit):

~~~text
url: https://ads.atmosphere.copernicus.eu/api
key: <YOUR_ADS_PERSONAL_ACCESS_TOKEN>
~~~

3. In the ADS dataset download page, select your fields and click **“Show API request code”**.  
   Use that generated request as the authoritative template.

Provider tutorial example request (AOD sample; replace variable/time/area as needed):

~~~python
import cdsapi

URL = "https://ads.atmosphere.copernicus.eu/api"
KEY = "<PERSONAL_ACCESS_TOKEN>"

client = cdsapi.Client(url=URL, key=KEY)

client.retrieve(
    "cams-global-atmospheric-composition-forecasts",
    {
        "variable": "total_aerosol_optical_depth_550nm",
        "date": "2025-01-25",
        "time": "00:00",
        "leadtime_hour": [str(i) for i in range(0, 121)],
        "type": "forecast",
        "data_format": "netcdf_zip",
        "area": [90, -180, 0, 180],
    },
    "download.zip",
)
~~~

> **KFM adaptation:** For Kansas‑focused products, set `area` to a Kansas bounding box (north, west, south, east). Keep the *original request JSON* (minus secrets) in the run log for reproducibility.

## 🧪 Validation & CI/CD

This markdown file is expected to pass KFM’s documentation checks, including:
- front‑matter schema validation (required fields present)
- heading registry enforcement (approved H2 headings)
- directory layout fence requirements (`~~~text`)
- governance footer link checks

Data artifacts produced from CAMS ingestion should additionally pass:
- STAC validation (core + chosen extensions)
- DCAT export validation
- PROV constraints / SHACL (if enabled in KFM)

## ⚖ FAIR+CARE & Governance

- **License & attribution:** Upstream dataset is CC‑BY and should be attributed according to ADS guidance and DOI citation.
- **Privacy:** This source is gridded environmental model output; it contains **no PII** by design. Risks arise only if joined with other sensitive layers; apply KFM redaction rules at join points.
- **Sovereignty:** Although this is global gridded data, KFM still applies sovereignty review where derived products intersect culturally sensitive contexts.

## 🕰️ Version History

| Version | Date | Change | Notes |
|---|---|---|---|
| v0.1.0 | 2025-12-17 | Initial CAMS NRT source documentation | Draft; validate against CI |

---

<div align="center">

**Standards & Governance**  
[Markdown Protocol (KFM‑MDP v11.2.6)](../../../docs/standards/kfm_markdown_protocol_v11.2.6.md) ·
[STAC Patterns](../../../docs/patterns/stac/README.md) ·
[Provenance Patterns](../../../docs/patterns/provenance/README.md) ·
[FAIR+CARE Guide](../../../faircare/FAIRCARE-GUIDE.md) ·
[Sovereignty Policy](../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[Security](../../../SECURITY.md)

</div>
