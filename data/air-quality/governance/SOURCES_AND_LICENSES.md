---
title: "Air Quality — Sources and Licenses"
path: "data/air-quality/governance/SOURCES_AND_LICENSES.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"

doc_kind: "Governance"
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

doc_uuid: "urn:kfm:doc:data:air-quality:governance:sources-and-licenses:v1.0.0"
semantic_document_id: "kfm-air-quality-sources-and-licenses-v1.0.0"
event_source_id: "ledger:kfm:doc:data:air-quality:governance:sources-and-licenses:v1.0.0"

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

# Air Quality — Sources and Licenses

> **Not legal advice.** This is a governance/workflow artifact that records source links and licensing constraints for the `data/air-quality/` domain. Always defer to the authoritative license/terms text and the repo’s governance policies.

---

## 🧩 Overview

### Purpose

This document is the **source-of-truth register** for:
- **Upstream data sources** used in the `air-quality` domain
- **Licensing / rights / attribution** obligations
- **Redistribution constraints** (including any limitations that affect STAC/DCAT publication or UI exposure)
- **Verification dates** so we can re-check terms periodically

This file is intended to be used as a **gate** before:
- adding a new upstream source to ETL ingestion
- publishing derived outputs, STAC/DCAT catalogs, or map layers

### Scope

| In scope | Out of scope |
|---|---|
| Air-quality upstream datasets and services (federal, state/local, academic, commercial) | Implementation details of ETL transforms |
| Terms-of-use links, license summaries, attribution notes | Legal interpretation beyond summarization |
| KFM-facing constraints (redistribution, commercial use, rate limits, required notices) | ML modeling decisions and performance tuning |
| “Quality disclaimers” relevant to interpretation (e.g., preliminary vs validated data) | Narrative Story Node writing guidelines (see Story Node template) |

### Audience

- Data engineering / ETL maintainers
- Catalog and provenance maintainers (STAC/DCAT/PROV)
- Governance reviewers / data stewards
- UI layer registry maintainers (to prevent restricted data exposure)

### Definitions

- **Source**: An upstream provider (API, repository, download portal) that emits air-quality related data.
- **License / Rights**: The legal terms under which a dataset or service can be used.
- **Attribution**: Required citation, branding, or notices that must travel with data/visualizations.
- **Redistribution**: Whether KFM can publish the raw/derived data and metadata to third parties (e.g., public static hosting).
- **Verification date**: The last date we checked the upstream license/terms text.

(See global glossary if present: `docs/glossary/GLOSSARY.md`)

### Key Artifacts

| Artifact | Path | Role |
|---|---|---|
| Domain governance index | `data/air-quality/governance/README.md` | Entry point + how to use these governance docs |
| Domain data classification | `data/air-quality/governance/DATA_CLASSIFICATION.md` | Defines sensitivity triggers and release gates |
| **This document** | `data/air-quality/governance/SOURCES_AND_LICENSES.md` | Source register + license/attribution constraints |
| Root governance (canonical) | `docs/governance/ROOT_GOVERNANCE.md` | System-wide rules (authority) |
| Ethics + sovereignty (canonical) | `docs/governance/ETHICS.md`, `docs/governance/SOVEREIGNTY.md` | CARE + sovereignty requirements |

### Definition of Done

- [ ] Every upstream source used by `data/air-quality/` is listed in the Source Register below
- [ ] Each listed source includes: **terms URL(s)**, **license/rights summary**, and **last verified date**
- [ ] Sources with redistribution restrictions are clearly flagged and mapped to classification gates
- [ ] STAC/DCAT license fields for this domain can be derived from this register (no missing license metadata)
- [ ] Validation steps are reproducible (CI or local checks), including link/availability checks (where feasible)
- [ ] CARE + sovereignty concerns are documented for any source that could expose sensitive locations/community impacts

---

## 🗂️ Directory Layout

### This document

- `data/air-quality/governance/SOURCES_AND_LICENSES.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Air-quality domain | `data/air-quality/` | Domain datasets + governance (this folder) |
| Domain governance | `data/air-quality/governance/` | Classification, licenses, handling rules |
| Domain data staging (expected) | `data/air-quality/raw/`, `data/air-quality/work/`, `data/air-quality/processed/` | Raw → work → processed for this domain (per KFM conventions) |
| Catalog outputs (expected) | `data/air-quality/stac/` (or centralized `data/stac/`) | STAC Collections/Items for this domain |
| Global governance | `docs/governance/` | Root governance + ethics + sovereignty |

### Expected file tree

~~~text
🗂️ data/
└── 🌫️ air-quality/
    ├── 🛡️ governance/
    │   ├── 📄 README.md
    │   ├── 📄 DATA_CLASSIFICATION.md
    │   └── 📄 SOURCES_AND_LICENSES.md
    ├── 🧪 raw/
    ├── 🧰 work/
    ├── ✅ processed/
    └── 🗃️ stac/
~~~

> If this repo centralizes catalogs under `data/stac/`, ensure the air-quality catalog is published there and this domain folder links to it.

---

## 🧠 Context

### Background

Air quality data is frequently sourced from a **mix of public-domain regulatory networks** and **partner / commercial or community sensor networks**. Even when the measurements themselves are “open,” **terms-of-service** and **redistribution rights** can differ substantially by provider.

KFM treats licensing and provenance as first-class so that catalogs, graph ingest, APIs, and the UI do not accidentally publish restricted data or omit required notices.

### Assumptions

- Licenses and terms can change over time; this register must be re-verified periodically.
- Derived products (aggregations, tiles, joined datasets) inherit constraints unless upstream terms explicitly allow redistribution without restrictions.
- If a source is ambiguous, assume **more restrictive handling** until reviewed.

### Constraints / invariants

- The canonical KFM pipeline order is preserved (ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode).
- No direct graph access from UI; all exposure is gated through APIs and layer registry.
- Sensitive locations must not be inferred or exposed, especially for low-cost sensors near residences.

### Open questions

| Question | Owner | Status | Notes |
|---|---|---|---|
| Which upstream sources are in-scope for v1 ingestion (regulatory only vs include low-cost sensors)? | Data Steward | open | Decide before publishing public layers |
| Will catalogs be domain-local (`data/air-quality/stac/`) or centralized (`data/stac/`)? | Platform Maintainer | open | Choose one canonical location and link |
| What is the review cadence for re-verifying terms (quarterly/biannual)? | Governance | open | Add as CI/telemetry gate if needed |

### Future extensions

- Add automated checks: link availability, “last verified age” thresholds, and license completeness
- Generate STAC/DCAT `license` and `rights` fields mechanically from this register (single source of truth)
- Add a “restricted source allowlist” for UI layer registry gating

---

## 🧭 Diagrams

### System/dataflow diagram

~~~mermaid
flowchart LR
  S[Upstream Sources] --> L[License + Rights Gate<br/>(this register)]
  L --> E[ETL (deterministic)]
  E --> C[STAC/DCAT/PROV catalogs<br/>(license + attribution carried)]
  C --> G[Graph (Neo4j)]
  G --> A[APIs]
  A --> U[Map/UI Layers]
  U --> N[Story Nodes / Focus Mode]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Maintainer
  participant Gov as Governance
  participant Src as Upstream Source
  participant ETL as ETL Pipeline
  participant Cat as Catalogs (STAC/DCAT/PROV)

  Dev->>Gov: Propose new air-quality source
  Gov->>Dev: Approve terms/constraints or request changes
  Dev->>Src: Verify license/terms + record URLs
  Dev->>ETL: Add ingest config + run deterministic ETL
  ETL->>Cat: Emit catalogs incl. license/attribution
  Cat->>Gov: Validate license completeness + publish gates
~~~

---

## 🧾 Data & Metadata

### Inputs

Primary inputs are external datasets/services listed in the **Source Register** below.

#### Source Register (authoritative for this domain)

**Legend for “KFM release impact”:**
- **Open**: safe to publish derived outputs + catalogs publicly (with required attribution).
- **Conditional**: publish only after verifying provider constraints and applying mitigations.
- **Restricted**: do not publish publicly; keep internal or aggregate/anonymize per classification rules.

| Source ID | Source / Publisher | Data type | Access | License / rights summary (non-authoritative) | Terms / License URL(s) | Attribution / notices | Redistribution notes | KFM release impact | Last verified |
|---|---|---|---|---|---|---|---|---|---|
| epa-aqs | US EPA — Air Quality System (AQS) / AirData | Regulatory monitoring observations (e.g., PM2.5, O₃) | AQS API + bulk downloads | Public domain for EPA-produced monitoring data (unless otherwise specified) | https://www.epa.gov/outdoor-air-quality-data/do-i-need-request-permission-use-air-data-or-epa-data<br/>https://www.epa.gov/developers/epa-standard-open-data-license | Cite EPA/AQS + retrieval date in catalog/docs | Redistribution generally permitted; still track provenance | Open | 2025-12-17 |
| epa-airnow | AirNow (EPA + partner agencies) | Near-real-time AQI reporting and pollutant data | API (key) + web products | License/rights must be verified per feed; AirNow includes multi-agency inputs | https://www.airnow.gov/about-airnow/ | Cite AirNow + include QA disclaimer that data is preliminary | Not for regulatory use; may include third-party inputs | Conditional | 2025-12-17 |
| epa-airnow-daily | US EPA — “Download Daily Data” (AirNow extracts) | Recent-day ozone/PM (for periods not yet in AQS) | Download portal | EPA-hosted distribution; usage constraints include “preliminary” and non-regulatory guidance | https://www.epa.gov/outdoor-air-quality-data/download-daily-data | Cite EPA AirNow Daily Data + “preliminary” status | Replace with AQS once validated data available | Conditional | 2025-12-17 |
| openaq | OpenAQ | Aggregated observations from multiple providers | OpenAQ API | Licenses vary by data provider; use OpenAQ license metadata to determine permissions | https://docs.openaq.org/resources/licenses | Follow provider license fields; cite provider and OpenAQ as appropriate | Commercial/redistribution depends on provider license fields | Conditional | 2025-12-17 |
| purpleair | PurpleAir | Low-cost sensor observations | PurpleAir API | Permissioned/proprietary terms; attribution and distribution constraints apply | https://www2.purpleair.com/pages/data-licensing | Attribution required; review Terms; contact PurpleAir for licensing inquiry if needed | Limited distribution; do not publish raw sensor feeds publicly without explicit permission | Restricted | 2025-12-17 |
| nasa-laads-modis-viirs | NASA LAADS DAAC (MODIS/VIIRS atmosphere products) | Satellite atmosphere products (e.g., aerosols) | LAADS downloads/APIs | Data products generally without restrictions on use/redistribution; citation requested; imagery may have separate restrictions | https://ladsweb.modaps.eosdis.nasa.gov/tools-and-services/data-use-and-citation-policies/ | Provide citation/acknowledgment per NASA guidance | Redistribution generally allowed; preserve provenance + citation | Open | 2025-12-17 |
| copernicus-sentinel-5p | Copernicus / ESA (Sentinel-5P/TROPOMI) | Satellite atmospheric composition (e.g., NO₂, aerosols) | Copernicus Data Space (incl. STAC) | Free, full, open access; required source notice on redistribution | https://dataspace.copernicus.eu/terms-and-conditions | Must include “Copernicus Sentinel data [Year]” notice; note modifications if any | Redistribution allowed with notice; keep provenance and modifications notes | Open | 2025-12-17 |

> Add rows for additional sources before ingesting them. If a provider’s license is ambiguous, treat as **Restricted** until reviewed.

### Outputs

Outputs derived from the above inputs may include:

- Domain-normalized tables (time series, station metadata, aggregates)
- Derived spatial layers (grids/tiles, summaries)
- Domain catalogs:
  - STAC Collections/Items referencing assets and carrying license/citation
  - DCAT dataset views (license, access rights, publisher, keywords)
  - PROV activities/entities recording transforms and upstream usage

### Sensitivity & redaction

- **Regulatory monitors (AQS/AirNow)** are typically public, but always confirm the upstream terms.
- **Low-cost/community sensors** may reveal **private/residential locations**. If publishing:
  - aggregate spatially (e.g., grid/hex) and/or jitter coordinates per governance rules
  - never publish sensor IDs tied to private addresses without explicit permission
  - never use AI to infer sensitive locations from sensor context

### Quality signals

- Distinguish **preliminary** (near-real-time) from **validated** (regulatory/QA complete).
- Persist QA flags and provenance to allow downstream filtering.
- Prefer AQS for validated historical analyses when available.

---

## 🧬 STAC, DCAT & PROV alignment

### STAC

- Ensure every dataset/derivative has STAC metadata that includes:
  - a license field (derived from this register)
  - provider attribution (publisher + roles)
  - asset-level links to upstream sources where appropriate
- If a source is **Restricted/Conditional**, the STAC publication strategy must align with classification gates.

### DCAT

- DCAT views must expose:
  - license and/or rights link(s)
  - access rights statements where restrictions exist
  - contact/publisher fields appropriate for the provider

### PROV-O

- PROV records must capture:
  - which upstream sources were used (`prov:used`)
  - when transforms occurred (`prov:generatedAtTime`)
  - which process/version produced derived outputs (`prov:wasGeneratedBy`)
- Carry forward license/attribution context as attributes or linked documentation references.

### Versioning

- If upstream terms change:
  - update this register and bump version
  - update catalogs and layer release gates accordingly
  - record the change in Version History

---

## 🧯 Extension Points Checklist

- [ ] Adds new upstream source (must add to Source Register)
- [ ] Adds new derived dataset output (must map license + attribution)
- [ ] Adds new public UI layer (must pass classification and license gates)
- [ ] Adds new catalog profile extension (must remain backward compatible or version bump)

---

## 🧵 Story Node & Focus Mode Integration

### Relevance to Story Nodes

Air-quality Story Nodes and Focus Mode panels must:
- cite the upstream dataset(s) used for any quantitative claims
- avoid displaying restricted sensor-level locations
- respect provider attribution/notice requirements (e.g., Copernicus notice; NASA citation requests)

### Optional: Focus Mode framing (structured controls)

~~~yaml
focus_controls:
  air_quality:
    default_view: "validated"   # prefer validated sources by default
    allow_preliminary: true     # allow AirNow-like feeds when explicitly labeled
    allow_low_cost_sensors: false  # default off unless governance-approved
~~~

---

## ✅ Validation & CI/CD

### Validation steps

- [ ] Confirm every Source Register row has:
  - terms/license URL(s)
  - last verified date
  - release impact classification (Open/Conditional/Restricted)
- [ ] Confirm any “Restricted” source is not published via public STAC/DCAT or UI layers
- [ ] Confirm catalog license fields match this register (no missing/unknown licenses)

> CI is expected to validate license completeness for dataset/source catalogs (project convention). Add checks here if/when implemented.

### Reproduction

~~~bash
# TBD: add automated link checker and license completeness check.
# Example intent (adapt to repo tooling):
# make lint-docs
# make check-links PATH=data/air-quality/governance/SOURCES_AND_LICENSES.md
~~~

### Telemetry signals

| Signal | Type | Purpose |
|---|---|---|
| license_last_verified_age_days | metric | Identify stale license checks |
| restricted_source_count | metric | Ensure restricted inputs do not leak into public outputs |
| preliminary_vs_validated_ratio | metric | Track reliance on preliminary feeds |

---

## 🔒 FAIR+CARE & Governance

### Review gates

- **New source added** → governance review required (license + classification + release gating)
- **New public layer derived** → review required (attribution/notice + sensitive location risk)
- **Any restricted/conditional source** → explicit approval path defined in governance docs

### CARE considerations

- Air quality exposure can be socially sensitive. Avoid releasing data in ways that:
  - enable targeting specific households or small communities (especially for low-cost sensors)
  - exaggerate precision beyond the source’s QA status (preliminary vs validated)
  - ignores sovereignty constraints in areas where additional restrictions apply

### AI usage constraints

- AI must not infer or expose sensitive locations from sensor context.
- AI outputs must not be treated as legal determinations of licensing.
- Use AI for summarization and checklist generation only, per front-matter constraints.

---

## 🕰️ Version History

| Version | Date | Change | Author | Notes |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-17 | Initial air-quality source + license register | <name> | Seeded with common regulatory + satellite + aggregator + low-cost sensor sources |

---

## 📎 Footer / References

- Root governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Domain classification: `data/air-quality/governance/DATA_CLASSIFICATION.md`
- Domain governance README: `data/air-quality/governance/README.md`
