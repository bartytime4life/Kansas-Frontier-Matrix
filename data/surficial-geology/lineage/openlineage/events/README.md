---
title: "🧬 Surficial Geology — OpenLineage Events"
path: "data/surficial-geology/lineage/openlineage/events/README.md"

version: "v0.1.0"
last_updated: "2025-12-14"
release_stage: "Draft / In-Progress"
content_stability: "draft"

status: "Active"
doc_kind: "Index"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"

scope:
  domain: "surficial-geology"
  applies_to:
    - "data/surficial-geology/lineage/openlineage/events/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage:openlineage:events-readme:v0.1.0"
semantic_document_id: "surficial-geology-openlineage-events-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage:openlineage:events-readme:v0.1.0"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-relationship-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧬 **Surficial Geology — OpenLineage Events**
`data/surficial-geology/lineage/openlineage/events/README.md`

**Purpose**  
Store **OpenLineage event payloads** (machine-readable lineage) for Surficial Geology pipeline runs, in a form that is **auditable**, **sanitized**, and **linkable** to KFM provenance (PROV), catalogs (STAC/DCAT), and graph ingestion.

</div>

---

## 📘 Overview

This directory holds **OpenLineage event JSON** captured from Surficial Geology workflows (ETL, export, tiling, validation, publication).

Use these events to:

- Reconstruct **what ran**, **when**, **with what inputs**, and **what outputs were produced**.
- Support downstream lineage stores and UIs (e.g., lineage graphs) without requiring access to ephemeral runtime logs.
- Provide **evidence-grade provenance** that can be mapped into **W3C PROV** activities/entities.

### What belongs here

- OpenLineage events as **verbatim (but sanitized) JSON payloads**, typically one file per event.
- Events for **release-grade** runs (or other runs explicitly designated for retention).

### What does not belong here

- Secrets, tokens, credentials, signed URLs, or internal-only endpoints.
- PII (names/emails) that appear in runtime metadata unless explicitly governed and approved.
- Bulk raw logs (put those under `mcp/runs/` or `mcp/experiments/` per run policy; link from lineage notes/manifests instead).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/lineage/
└── 📁 openlineage/
    └── 📁 events/                                 — OpenLineage event payloads (this folder)
        ├── 📄 README.md                            — This file
        ├── 📁 run_<run_id>/                        — Recommended: one folder per OpenLineage runId
        │   ├── 🧾 <ts>__START__<job>.json           — START event
        │   ├── 🧾 <ts>__COMPLETE__<job>.json        — COMPLETE event
        │   └── 🧾 <ts>__FAIL__<job>.json            — FAIL event (if applicable)
        └── 📁 batch_exports/                        — Optional: bundled exports (NDJSON), if used
            └── 🧾 openlineage_events_<date>.ndjson  — One JSON per line (sanitized)
~~~

**Conventions**

- `<run_id>` SHOULD be the OpenLineage `run.runId` (UUID string) or a stable surrogate derived from the run record.
- `<ts>` SHOULD be UTC in sortable form: `YYYYMMDDThhmmssZ` (derived from `eventTime`).
- `<job>` SHOULD be a filesystem-safe job name token (e.g., `surficial_geology_etl`, `surficial_geology_tiles`).

---

## 🧭 Context

In the KFM pipeline, these artifacts support provenance across the full chain:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

OpenLineage events are **run-level lineage telemetry**. They are not a replacement for KFM’s PROV outputs, but they are:

- A **portable interchange** format for lineage capture
- A strong **evidence source** for generating PROV Activities/Entities
- Useful for **impact analysis** (what depends on what) and **audit trails**

Related Surficial Geology lineage folders:

- `data/surficial-geology/lineage/manifests/` — curated run + artifact manifests (checksums, inventories)
- `data/surficial-geology/lineage/indexes/` — derived indexes for fast traversal/search
- `data/surficial-geology/lineage/notes/` — human-readable explanations, exceptions, governance notes
- `data/surficial-geology/lineage/openlineage/` — OpenLineage overview and integration notes

---

## 📦 Data & Metadata

### Minimum event expectations

Each event file SHOULD be a valid OpenLineage event JSON object containing, at minimum:

- `eventType` (`START`, `COMPLETE`, or `FAIL`)
- `eventTime` (ISO 8601 timestamp)
- `run.runId` (UUID)
- `job.namespace` and `job.name`
- `inputs[]` / `outputs[]` (where applicable)

### Sanitization requirements (mandatory)

Before committing any event JSON:

- Remove or redact **secrets** and **credentials** (API keys, bearer tokens, signed URLs).
- Remove or redact **PII** (usernames, emails) unless explicitly approved.
- Replace absolute local paths with:
  - repo-relative paths, or
  - stable dataset identifiers (STAC ids, `urn:kfm:*` identifiers), or
  - a neutral URI scheme (e.g., `kfm://data/...`)
- Avoid embedding sensitive precision locations if governance flags require generalization.

If sanitization changes semantics, record the rationale in `data/surficial-geology/lineage/notes/` and reference it from manifests.

### Naming/namespace guidance

To keep lineage interoperable:

- Prefer stable `job.namespace` (e.g., `urn:kfm:pipeline:surficial-geology`) over machine-specific values.
- Prefer stable dataset identity for `inputs/outputs`:
  - STAC Item/Asset ids when available, or
  - stable `urn:kfm:dataset:*` ids,
  - not ephemeral temp filenames.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

OpenLineage events do not replace STAC, but they can reference STAC assets and identifiers:

- If an event output corresponds to a published asset, the output dataset SHOULD be traceable to a STAC `Item` and `asset` entry.
- When feasible, store the mapping between event datasets and STAC assets in:
  - `data/surficial-geology/lineage/indexes/` (machine-readable), and/or
  - `data/surficial-geology/lineage/notes/` (human-readable)

### DCAT

If Surficial Geology distributions are published via DCAT:

- Use events as evidence for the generation of each `dcat:Distribution`.
- Ensure licensing/rights are sourced from authoritative manifests/catalogs (do not infer from runtime metadata).

### PROV

OpenLineage maps naturally into PROV:

- `job` + `runId` → `prov:Activity`
- `inputs/outputs` → `prov:Entity`
- `producer` / pipeline identity → `prov:Agent`
- `START/COMPLETE/FAIL` → event evidence supporting `prov:startedAtTime`, `prov:endedAtTime`, and failure notes

Where PROV summaries exist, they SHOULD reference the relevant OpenLineage event files (by path and checksum).

---

## 🧠 Story Node & Focus Mode Integration

When a Surficial Geology layer is explored in Focus Mode, OpenLineage events can power a “How this was produced” view:

- upstream inputs (datasets/assets)
- processing steps (jobs)
- outputs (published artifacts)
- timestamps and run identifiers
- links to manifests and provenance summaries

This directory is the **machine-readable evidence** that enables those views without embedding opaque logs into narratives.

---

## 🧪 Validation & CI/CD

Minimum expectations for committed OpenLineage event artifacts:

- **Schema sanity**: events are well-formed JSON and conform to expected OpenLineage structure.
- **Sanitization**: secret-scan and pii-scan MUST pass (no tokens, no credentials, no accidental PII).
- **Consistency**:
  - filenames align with `eventTime`, `eventType`, and `job`
  - folder name aligns with `run.runId` (when using the `run_<run_id>/` layout)
- **Provenance linkage**:
  - manifests/indexes (when present) reference events by stable path and checksum
  - release-grade runs are traceable to published outputs and catalogs

---

## ⚖ FAIR+CARE & Governance

Lineage can leak sensitive information even when data is “public”:

- runtime identities (people, emails)
- internal hostnames or network topology
- private bucket names or signed URLs
- implicit sensitive location clues

Default stance: **sanitize and minimize**. If any sovereignty or sensitivity flags apply, follow the linked policies and record any exceptions in lineage notes and manifests.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial README defining the purpose, structure, sanitization rules, and STAC/DCAT/PROV alignment for Surficial Geology OpenLineage events. |

---

<div align="center">

🧬 **Surficial Geology — OpenLineage Events**  
KFM Lineage Layer · Machine-Readable Provenance · Governance-First

[📘 Docs Root](../../../../../docs/README.md) ·
[📂 Standards Index](../../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

