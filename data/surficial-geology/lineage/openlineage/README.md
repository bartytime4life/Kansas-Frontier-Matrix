---
title: "🔗 Surficial Geology — Lineage (OpenLineage)"
path: "data/surficial-geology/lineage/openlineage/README.md"

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
    - "data/surficial-geology/lineage/openlineage/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage-openlineage-readme:v0.1.0"
semantic_document_id: "surficial-geology-lineage-openlineage-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage-openlineage-readme:v0.1.0"

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

# 🔗 **Surficial Geology — Lineage (OpenLineage)**
`data/surficial-geology/lineage/openlineage/README.md`

**Purpose**  
Store **sanitized OpenLineage RunEvent payloads** for Surficial Geology ETL runs so lineage is replayable, auditable, and convertible into KFM-native PROV artifacts.

</div>

---

## 📘 Overview

This folder holds **OpenLineage event payloads** (typically `RunEvent` JSON) captured during deterministic pipeline runs that produce Surficial Geology outputs.

Treat everything under `openlineage/` as:

- **Derived runtime evidence** (captured from instrumented jobs)
- **Append-only** (don’t rewrite history; emit a new run if something changes)
- **Machine-consumable** (structured JSON designed for downstream conversion/indexing)

### Relationship to other lineage folders

- `data/surficial-geology/lineage/openlineage/`  
  Raw-ish OpenLineage events (sanitized and normalized for repo safety).

- `data/surficial-geology/lineage/manifests/`  
  Curated, run-level manifests (what was built, from what, with checksums/config refs).

- `data/surficial-geology/lineage/indexes/`  
  Searchable indexes (by run id, dataset id, job name, date, etc.).

- `data/surficial-geology/lineage/notes/`  
  Human notes and decisions (especially governance/sensitivity decisions).

If OpenLineage instrumentation is not enabled for a pipeline yet, this directory may contain only this README.

---

## 🗂️ Directory Layout

~~~text
📁 openlineage/                                      — OpenLineage lineage payloads (this directory)
├── 📄 README.md                                     — This file (rules + naming + safety)
└── 📁 events/                                       — Event storage (preferred: one folder per run)
    ├── 📁 run_<run_id>/                             — A single deterministic ETL run
    │   ├── 🧾 <ts>__<namespace>__<job>__START.json   — OpenLineage RunEvent (START)
    │   ├── 🧾 <ts>__<namespace>__<job>__COMPLETE.json— OpenLineage RunEvent (COMPLETE)
    │   └── 🧾 <ts>__<namespace>__<job>__FAIL.json    — OpenLineage RunEvent (FAIL) (if any)
    └── 📁 run_<run_id>/...
~~~

Notes:

- `<run_id>` should match the run identifier used elsewhere for provenance (e.g., in `mcp/runs/` and/or PROV summaries).
- `<ts>` should be UTC and filename-safe (example: `20251214T000102Z`).
- `<namespace>` and `<job>` must be sanitized (no spaces; prefer lowercase with underscores).

---

## 🧭 Context

OpenLineage provides a standard event shape that can represent:

- **Job runs** (start/complete/fail)
- **Inputs and outputs** (“datasets” read/written)
- **Runtime facets** (job/run facets, schema facets, documentation facets, etc.)

Within KFM, OpenLineage events are used as *lineage evidence* that can be:

- Converted into PROV (`prov:Activity`, `prov:Entity`, `prov:Agent`)
- Indexed to support “show me what produced this file/layer/version”
- Audited for governance and safety (e.g., ensuring sensitive precision isn’t leaked)

---

## 📦 Data & Metadata

### File format rules

- One file = one JSON object (an OpenLineage event).
- UTF-8, newline at end of file.
- Do not store credentials, tokens, cookies, or any secrets.

### Naming conventions (recommended)

- Run folder: `run_<run_id>/`
- Event file:
  - `<ts>__<job_namespace>__<job_name>__<event_type>.json`
  - `event_type` ∈ `START | COMPLETE | FAIL`

Examples:

- `20251214T031500Z__kfm_surficial_geology__build_vectors__START.json`
- `20251214T032118Z__kfm_surficial_geology__build_vectors__COMPLETE.json`

### Sanitization requirements

OpenLineage payloads often contain fields that may leak sensitive information if captured raw. Before committing events here:

- Remove/redact connection strings, hostnames, usernames, access tokens, signed URLs.
- Prefer **repo-relative paths** over absolute workstation paths.
- Avoid embedding precise coordinates or protected-site locations in any facet payload.
- Prefer stable dataset identifiers (e.g., URNs) over ephemeral local paths when feasible.

If a run contains sensitive lineage details that cannot be safely generalized, do **not** commit the raw event payload. Instead:

- Commit a minimal, redacted event (or omit), and
- Record the decision and rationale under `data/surficial-geology/lineage/notes/`.

---

## 🌐 STAC, DCAT & PROV Alignment

### PROV (primary lineage target)

OpenLineage events are typically converted/mapped into PROV:

- Run/job → `prov:Activity`
- Inputs/outputs → `prov:Entity`
- Tooling/runner → `prov:Agent` (when captured safely)

OpenLineage should be treated as **supporting evidence** for PROV, not a replacement.

### STAC / DCAT (optional references)

When useful, lineage artifacts may be referenced from catalog records as supporting metadata:

- STAC: attach lineage artifacts as a `metadata` or `provenance` asset role (project conventions apply).
- DCAT: represent lineage artifacts as `dcat:Distribution` entries linked to the dataset record.

Do not invent license/rights here—inherit from authoritative dataset/source manifests and catalog records.

---

## 🧪 Validation & CI/CD

Minimum expectations for committed OpenLineage payloads:

- JSON parses cleanly.
- Filenames are stable, consistent, and deterministic.
- No secrets or obvious PII are present (must pass repo scans).
- No sensitive precision is leaked (especially around protected or sovereignty-flagged locations).

If validation tooling is added later (schema validation, OpenLineage spec conformance checks), it should operate deterministically and produce machine-readable reports.

---

## ⚖ FAIR+CARE & Governance

Lineage can reveal more than intended (paths, inferred relationships, sensitive processing context). For Surficial Geology:

- Default to **least-privilege lineage**: include what is needed to prove reproducibility and integrity.
- If sovereignty or sensitivity flags apply, prefer **generalization** and record decisions explicitly.
- Ensure governance references are kept current (see footer links).

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial OpenLineage README defining expected event storage layout, naming rules, sanitization requirements, and alignment with PROV + governance. |

---

<div align="center">

🔗 **Surficial Geology — Lineage (OpenLineage)**  
KFM Data Lineage · Evidence-First · Provenance-Ready

[📘 Docs Root](../../../../docs/README.md) ·
[📂 Standards Index](../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

