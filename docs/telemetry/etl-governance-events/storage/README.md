---
title: "🗄️ Kansas Frontier Matrix — ETL Governance Events Telemetry Storage Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/etl-governance-events/storage/README.md"

version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../releases/v11.2.6/etl-governance-events-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/etl-governance-events-v11.2.6.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

scope:
  domain: "telemetry-etl-governance-events-storage"
  applies_to:
    - "docs/telemetry/etl-governance-events/storage/**"
    - "data/logs/etl-governance-events/**"
    - "data/archive/etl-governance-events/**"
    - "releases/*/etl-governance-events-telemetry.json"
    - ".github/workflows/telemetry-export.yml"
  non_goals:
    - "Defining the event schema (see ../specs/README.md)"
    - "Providing example payloads (see ../examples/README.md)"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Operational telemetry; low-risk when aggregated"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by ETL Governance Events Telemetry Storage Standard v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/etl-governance-events/storage/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:etl-governance-events:storage:v11.2.6"
semantic_document_id: "kfm-telemetry-etl-governance-events-storage-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:etl-governance-events:storage:v11.2.6"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/telemetry-export.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
---

<div align="center">

# 🗄️ **Kansas Frontier Matrix — ETL Governance Events Telemetry Storage Standard**
`docs/telemetry/etl-governance-events/storage/README.md`

**Purpose**  
Define **where** ETL governance events are written, **how** they are partitioned and named, **when** they are compressed/archived, and **what integrity + governance evidence** must accompany them.  
This makes ETL governance telemetry **deterministic**, **auditable**, **FAIR+CARE-aligned**, and safe to feed into **release telemetry**, **catalogs**, **Neo4j**, and **Focus Mode**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-ETL_Governance_Storage-informational" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This standard defines **storage tiers** for ETL governance events:

- **Hot logs (JSONL)** for near-term debugging and reconciliation.  
- **Warm logs (compressed JSONL)** for retention and cheap replay.  
- **Cold archives (Parquet)** for analytics and long-term trend queries.  
- **Release summaries (JSON)** for governed rollups and dashboards.

This standard is **normative** for:

- Directory structure and file naming.  
- Sidecar metadata and checksums.  
- Compression, rotation, and retention behavior.  
- CI validation expectations for storage correctness.

This standard is **not** the event schema. The canonical schema and semantics live at:

- `docs/telemetry/etl-governance-events/specs/README.md`

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 etl-governance-events/
        ├── 📁 specs/
        │   └── 📄 README.md                         # Normative event schema & semantics
        ├── 📁 examples/
        │   └── 📄 README.md                         # Example payload catalog (non-normative)
        └── 📁 storage/
            └── 📄 README.md                         # ← This storage standard

📁 data/
├── 📁 logs/
│   └── 📁 etl-governance-events/
│       ├── 📁 YYYY/
│       │   └── 📁 MM/
│       │       ├── 📄 etl-governance-events-YYYY-MM-DD.jsonl        # Hot log (NDJSON)
│       │       ├── 🧾 etl-governance-events-YYYY-MM-DD.meta.json    # Sidecar metadata
│       │       └── 📄 etl-governance-events-YYYY-MM-DD.jsonl.gz     # Warm log (compressed)
│       └── 📁 index/
│           ├── 🧾 etl-governance-events-file-index.json             # File inventory (optional)
│           └── 🧾 etl-governance-events-checksums.json              # Rolling checksums (optional)
│
└── 📁 archive/
    └── 📁 etl-governance-events/
        ├── 📦 etl-governance-events-YYYY-QN.parquet                 # Cold archive (preferred)
        └── 📦 etl-governance-events-YYYY-QN.jsonl.gz                # Cold archive (fallback)

📁 releases/
└── 📁 vX.Y.Z/
    ├── 🧾 etl-governance-events-telemetry.json                      # Release rollup (summary)
    ├── 🧾 sbom.spdx.json                                            # Tooling SBOM
    └── 📦 manifest.zip                                              # Checksums + provenance pointers
~~~

---

## 🧭 Context

ETL governance events are storage-backed “truth” for:

- **Reliability**: retries, replays, failure causes, and resolution status.  
- **Governance**: pass/fail/quarantine/override decisions and reasons.  
- **Sustainability**: energy and carbon cost per run and per pipeline.  
- **Lineage**: the minimal anchors required to reconstruct PROV and OpenLineage views.

Storage must support three read modes:

1. **Operator debugging** (hot JSONL; short window; fastest append).  
2. **Audit replay** (warm JSONL.gz; longer retention; deterministic replay).  
3. **Analytics** (cold Parquet; efficient query; schema stability).

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["ETL pipeline emits events"] --> B["Append to hot JSONL (daily partition)"]
  B --> C["Write sidecar meta.json (counts, checksums)"]
  C --> D["Compress to JSONL.GZ (warm retention)"]
  D --> E["Aggregate to quarterly Parquet (cold archive)"]
  E --> F["Build release rollup JSON (governed summary)"]
  F --> G["Catalog + graph + dashboards consume summaries"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Storage guarantees that a Story Node can safely reference ETL history without scraping raw pipeline logs.

- Story Nodes MAY reference:
  - A daily file: `data/logs/etl-governance-events/YYYY/MM/etl-governance-events-YYYY-MM-DD.jsonl.gz`
  - A quarterly archive: `data/archive/etl-governance-events/etl-governance-events-YYYY-QN.parquet`
  - A release rollup: `releases/vX.Y.Z/etl-governance-events-telemetry.json`

- Focus Mode MAY:
  - Summarize trends by `pipeline_id` and time window.
  - Highlight governance outcomes (“quarantined” counts, override patterns).
  - Join with other telemetry ledgers (docs-lint, faircare-validate, ai-train).

- Focus Mode MUST NOT:
  - Surface sensitive details beyond what event payloads allow (no raw PII, no precise sensitive coordinates).
  - “Invent” missing periods if logs are absent.

---

## 🧪 Validation & CI/CD

Storage validation is enforced via `telemetry-export.yml` and schema validation jobs:

- Hot logs (`*.jsonl`) MUST be valid NDJSON: one JSON object per line.  
- Warm logs (`*.jsonl.gz`) MUST decompress into byte-for-byte identical lines as the hot file content for the same date.  
- Sidecar (`*.meta.json`) MUST be consistent with the corresponding hot log:
  - `events_count` matches line count.
  - `sha256_uncompressed` matches the hot file.
  - `sha256_gzip` matches the compressed file.
- Quarterly archives MUST be derived only from validated daily logs.

Minimum CI checks (normative):

- Validate each event line against `schemas/telemetry/etl-governance-events/etl-governance-event-v11.2.6.json`.
- Validate rollup JSON against `schemas/telemetry/etl-governance-events-v11.2.6.json`.
- Validate that filenames match the required patterns.

---

## 📦 Data & Metadata

### 1. File naming (normative)

Daily partition (hot):

- `data/logs/etl-governance-events/YYYY/MM/etl-governance-events-YYYY-MM-DD.jsonl`

Daily compressed (warm):

- `data/logs/etl-governance-events/YYYY/MM/etl-governance-events-YYYY-MM-DD.jsonl.gz`

Daily sidecar (required):

- `data/logs/etl-governance-events/YYYY/MM/etl-governance-events-YYYY-MM-DD.meta.json`

Quarterly archive (preferred):

- `data/archive/etl-governance-events/etl-governance-events-YYYY-QN.parquet`

Quarterly archive (fallback):

- `data/archive/etl-governance-events/etl-governance-events-YYYY-QN.jsonl.gz`

Release rollup:

- `releases/vX.Y.Z/etl-governance-events-telemetry.json`

### 2. Sidecar schema (required fields)

The sidecar file (`*.meta.json`) MUST include:

- `date` (YYYY-MM-DD, UTC)  
- `events_count` (integer)  
- `sha256_uncompressed` (hex)  
- `sha256_gzip` (hex, if gzip exists)  
- `schema_version` (e.g., `etl-governance-event-v11.2.6`)  
- `generated_at` (UTC ISO-8601)  
- `producer` (pipeline or system name, e.g., `kfm-telemetry-aggregator`)  

Recommended fields:

- `pipelines_seen[]` (unique pipeline IDs in the file)  
- `governance_decision_counts{}` (counts by decision)  
- `energy_wh_total`, `carbon_gco2e_total` (daily sums)

### 3. Retention policy (default, configurable)

Default retention rules for this domain (can be tightened by governance):

- Hot JSONL: retain 30 days (operational debugging).  
- Warm JSONL.GZ: retain 365 days (audit replay).  
- Quarterly Parquet: retain 5 years (trend analysis).  
- Release rollups: retain for the lifetime of the release artifacts.

Any purge MUST be logged as an ETL governance event (e.g., `event_type: retention_purge`) and reflected in manifests.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. STAC

Recommended pattern:

- Collection: `kfm-telemetry-etl-governance`  
- Items:
  - Quarterly archive items (`etl-governance-events-YYYY-QN`) with assets:
    - `archive-parquet` or `archive-jsonl-gz`
    - `rollup-json` (optional pointer to a release rollup)

Non-spatial: `geometry` may be `null`.

### 2. DCAT

Recommended pattern:

- Dataset: “KFM ETL Governance Events Telemetry”  
- Distributions:
  - Daily JSONL.GZ files (optional for public catalogs; often internal-only)
  - Quarterly Parquet archives (preferred for sharing)
  - Release rollup JSON (public-friendly summary)

Checksums MUST be recorded in `manifest.zip` and referenced in DCAT distributions.

### 3. PROV-O

Storage creates stable, derivable identifiers for provenance:

- Daily log entity: `urn:kfm:entity:etl-governance-log:YYYY-MM-DD`
- Quarterly archive entity: `urn:kfm:entity:etl-governance-archive:YYYY-QN`
- Aggregation activity: `urn:kfm:activity:etl-governance-aggregate:<run_id>`

Relations:

- Aggregation `prov:used` daily logs  
- Archive `prov:wasGeneratedBy` aggregation activity  
- Release rollup `prov:wasDerivedFrom` archive and/or daily logs

---

## 🧱 Architecture

Storage responsibilities are split:

- **Emitters** (pipelines) append events to daily hot logs through a single library/CLI.
- **Rotators** compress hot logs and write sidecars.
- **Aggregators** build quarterly archives and release rollups.
- **Validators** enforce schema and storage invariants in CI.

Normative boundary rule:

- Pipeline code MUST NOT write directly into `releases/`.
  - Pipelines write logs to `data/logs/etl-governance-events/`.
  - CI / release tooling writes rollups to `releases/vX.Y.Z/`.

---

## ⚖ FAIR+CARE & Governance

Storage MUST be safe by construction:

- No raw PII in event payloads.
- No precise coordinates for sensitive or sovereign sites; reference governed dataset IDs and redacted geometry IDs only.
- Any override to normal retention MUST be:
  - documented,
  - logged as a governance event,
  - approved through governance processes referenced in `governance_ref`.

This storage standard is governance evidence itself:
- it specifies deterministic behaviors,
- it enables audit trails,
- and it defines how telemetry is made reusable without leaking sensitive content.

---

## 🕰️ Version History

| Version   | Date       | Author            | Summary                                                                 |
|----------:|-----------:|-------------------|-------------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `@kfm-telemetry`  | Built storage standard from scratch: tiers, naming, sidecars, retention, CI checks, and STAC/DCAT/PROV mapping. |
| v11.2.4   | 2025-12-06 | `@kfm-telemetry`  | Prior baseline storage guidance (superseded by v11.2.6 rewrite).        |

---

<div align="center">

🗄️ **KFM — ETL Governance Events Storage Standard (v11.2.6)**  
Deterministic Storage · Audit Replay · Sustainable Telemetry  

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Telemetry-ETL_Governance_Storage-informational" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ ETL Governance Telemetry Index](../README.md) ·
[📘 Specs](../specs/README.md) ·
[🧾 Examples](../examples/README.md) ·
[⚙ Telemetry Export Workflow](../../../workflows/telemetry-export.yml.md) ·
[📚 Glossary](../../../glossary.md) ·
[📘 Markdown Protocol](../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω  

</div>