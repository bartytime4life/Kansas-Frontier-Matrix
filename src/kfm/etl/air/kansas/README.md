---
title: "🌬️ KFM — Kansas Air ETL (OpenAQ v3 · AQS · PurpleAir)"
path: "src/kfm/etl/air/kansas/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE & Reliability Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "README"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-air-etl-kansas-readme"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
openlineage_profile: "OpenLineage v2.5 · Data & ETL pipeline events"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:etl:air:kansas:readme:v11.2.6"
semantic_document_id: "kfm-etl-air-kansas"
event_source_id: "ledger:src/kfm/etl/air/kansas/README.md"
immutability_status: "branch-live"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

classification: "Public Document"
sensitivity: "Mixed (station-level; provider-dependent)"
sensitivity_level: "Low to Medium"
public_exposure_risk: "Dataset-level"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
indigenous_rights_flag: "Dataset-level"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🌬️ **KFM — Kansas Air ETL**
`src/kfm/etl/air/kansas/README.md`

**Purpose**  
Define the Kansas air-quality ETL scope and invariants for **OpenAQ v3**, **EPA AQS**, and **PurpleAir**: deterministic micro-batches, station identity resolution, validation flags, late/changed-data detection, and evidence emission (STAC + PROV-O + OpenLineage).

[✅ Validation & Evidence Checklist](VALIDATION_CHECKLIST.md) ·
[📦 Data Plane](../../../../../data/README.md) ·
[🗄️ Data Architecture](../../../../../data/ARCHITECTURE.md) ·
[🧾 Data Catalog Docs](../../../../../docs/data/)

<br/>

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" alt="KFM-MDP v11.2.6" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" alt="MCP-DL v6.3" />
<img src="https://img.shields.io/badge/Lineage-PROV%E2%80%91O_%7C_OpenLineage-success" alt="PROV-O | OpenLineage" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" alt="Active / Canonical" />

</div>

---

## 📘 Overview

This folder is the **Kansas-specific entry point** for the KFM air-quality ETL.

This ETL is designed to:

- Ingest observations as **micro-batches** using a half-open time window: `[T_start, T_end)`.
- Resolve station identity deterministically across providers and normalize to KFM conventions.
- Detect late-arriving and retroactively edited observations using:
  - deterministic natural keys,
  - `update_count`,
  - and lag metrics such as `time_lag_seconds`.
- Emit evidence artifacts so downstream systems never have to “trust the pipeline” blindly:
  - STAC properties and sidecars,
  - PROV-O JSON-LD run records,
  - OpenLineage run events,
  - validation summaries and delta ledgers (when enabled).

The canonical operational contract for “what must happen on every run” lives in:
- `VALIDATION_CHECKLIST.md`

---

## 🗂️ Directory Layout

~~~text
📁 src/kfm/etl/air/kansas/
├── 📄 README.md                      # This file (scope, invariants, interfaces)
└── 📄 VALIDATION_CHECKLIST.md        # Canonical checklist for validation + evidence emission
~~~

Notes:

- Implementation files, configs, and provider connectors may be colocated here or in adjacent modules under `src/kfm/etl/air/` depending on the current repo organization.
- Any future additions MUST remain deterministic, auditable, and governance-compliant.

---

## 🧭 Context

### Role in the KFM pipeline

Kansas Air ETL sits in the pipeline as:

> ETL → catalogs (STAC/DCAT/PROV) → graph → API → frontend → Story Nodes → Focus Mode

Key boundary rule:
- The frontend does **not** read `data/**` directly; it consumes APIs and governed catalog outputs.

### Expected data-plane destinations

This ETL typically writes governed artifacts into the data plane:

- `data/air-quality/**` for domain products and evidence
- `data/stac/**` for STAC catalogs (if emitting STAC)
- `docs/data/**` for DCAT and contract documentation (when publishing)

Exact paths are defined by pipeline configuration and data contracts, and must remain stable once published.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Provider APIs\n(OpenAQ v3 / AQS / PurpleAir)"] --> B["Micro-batch window\n[T_start, T_end)"]
  B --> C["Normalize\n(units, parameters, station identity)"]
  C --> D["Validate\n(flag_* + profile_version)"]
  D --> E["Upsert + Retroactivity\n(nk + update_count + time lag)"]
  E --> F["Batch gates\n(quorum + drift + quarantine)"]
  F --> G["Commit outputs\n(processed artifacts)"]
  G --> H["Evidence emission\n(STAC + PROV + OpenLineage)"]
  H --> I["Downstream\n(graph + API + UI + narratives)"]
~~~

---

## 🧪 Validation & CI/CD

This module is considered “healthy” only when every micro-batch produces:

- deterministic outputs (or deterministic quarantine outputs),
- a validation summary (counts and rates for each flag),
- evidence artifacts (PROV + OpenLineage, and STAC if publishing),
- and verifiable integrity hashes/checksums where applicable.

Minimum CI expectations for changes that touch Kansas air ETL docs or behavior:

- Markdown structure checks (H1/H2 rules, fences, footer links)
- Front-matter schema checks
- Secret scan and PII scan (docs and configs)
- Provenance and evidence checks (if evidence artifacts are generated in repo)
- Diagram checks (Mermaid parseability)

For the run-time checklist and concrete required fields:
- See `VALIDATION_CHECKLIST.md`

---

## 📦 Data & Metadata

### Provider scope (Kansas)

- **OpenAQ v3**: aggregated measurements from multiple sources, may have provider-level updates.
- **EPA AQS**: regulatory monitoring network; includes QC/qualifier metadata that must be preserved.
- **PurpleAir**: community sensors; coordinate precision and exposure policy may vary and requires care.

### Normalized record invariants (minimum)

At a minimum, normalized observations SHOULD include:

- provider identity: `provider`, `provider_last_updated_at`
- station identity: `station_authority`, `station_authoritative_id`, `identity_confidence`
- measurement: `parameter`, `unit`, `value`
- clocks: `source_observed_at`, `ingest_received_at`, `batch_committed_at`
- determinism keys: `nk` (natural key), `payload_hash`
- retroactivity fields: `update_count`, `retroactive_update`, `time_lag_seconds`
- validation fields: `validation_profile_version`, `flag_*`

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

When publishing Kansas air outputs as STAC assets:

- STAC Items MUST surface late/changed-data status via properties:
  - `kfm:update_count`, `kfm:retroactive_update`, `kfm:time_lag_seconds`, `kfm:ingest_received_at`
- STAC Items SHOULD include evidence sidecars as assets:
  - `prov.jsonld`, `openlineage.json`, and a validation summary artifact

### DCAT

When publishing datasets for interoperability and portals:

- DCAT dataset identifiers must remain stable and map to KFM identifiers.
- DCAT distributions should align with publishable assets and/or STAC links.
- Access constraints must be explicit (provider terms, masking, restricted precision).

### PROV-O and OpenLineage

- PROV-O captures the logical chain:
  - inputs → activity (micro-batch) → outputs
- OpenLineage captures execution-level facts:
  - job/run identity, nominal time window, facets for quality and retroactivity

---

## 🧱 Architecture

### Design invariants (non-negotiable)

1. **Deterministic micro-batches**
   - Same inputs + same config + same code + same environment must produce the same outputs.

2. **Idempotency**
   - Replaying the same window must not duplicate records or silently drift results.

3. **Fail-closed gating**
   - Quarantine is allowed; silent publish of degraded data is not.

4. **Evidence-first**
   - Every “published” artifact must be traceable to:
     - a batch window,
     - a provenance record,
     - and (where used) a STAC/DCAT representation.

### Streaming mode (optional)

Streaming is allowed only if it preserves the same invariants as micro-batching:

- identical clock fields
- deterministic idempotency keys
- equivalent evidence emission (OpenLineage + PROV-O)
- quarantine gates

---

## ⚖ FAIR+CARE & Governance

Kansas air-quality data is generally public, but risk is **provider- and station-dependent**:

- Station locations may require generalization or restricted precision depending on policy and stewardship.
- Never store secrets or tokens in docs, configs, or examples.
- Never publish high-precision station coordinates if governance requires masking/generalization.
- If governance metadata is incomplete (license, access constraints, sensitivity), default to:
  - quarantine and steward escalation,
  - and block public catalog updates.

Authoritative governance references:

- `../../../../../docs/standards/governance/ROOT-GOVERNANCE.md`
- `../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md`
- `../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial Kansas Air ETL README; defines scope, invariants, and interfaces; links canonical validation/evidence checklist; aligns with KFM-MDP v11.2.6 requirements. |

---

<div align="center">

🌬️ **KFM — Kansas Air ETL (v11.2.6)**  
Deterministic Pipelines · Evidence-Led Lineage · FAIR+CARE Governed

[⬅ Back to Repository Root](../../../../../README.md) ·
[📦 Data Plane](../../../../../data/README.md) ·
[🗄️ Data Architecture](../../../../../data/ARCHITECTURE.md) ·
[✅ Validation Checklist](VALIDATION_CHECKLIST.md) ·
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

