---
title: "🧾 Surficial Geology — OpenLineage Run Events"
path: "data/surficial-geology/lineage/openlineage/events/run_<run_id>/README.md"

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
    - "data/surficial-geology/lineage/openlineage/events/run_<run_id>/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage:openlineage:events:run-<run_id>:readme:v0.1.0"
semantic_document_id: "surficial-geology-lineage-openlineage-events-run-<run_id>-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage:openlineage:events:run-<run_id>:readme:v0.1.0"

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

# 🧾 **Surficial Geology — OpenLineage Run Events**
`data/surficial-geology/lineage/openlineage/events/run_<run_id>/README.md`

**Purpose**  
Describe what belongs in a single-run OpenLineage event folder, how event files are named and validated, and how per-run lineage is preserved for reproducibility, auditing, and downstream indexing.

</div>

---

## 📘 Overview

This directory contains the **OpenLineage event stream for one pipeline run** (`<run_id>`) associated with Surficial Geology processing and/or export tasks.

Treat everything under `run_<run_id>/` as:

- **Derived** (generated automatically by an instrumented pipeline run)
- **Append-only** (events may be added during a run; do not rewrite prior events)
- **Run-scoped** (all events in this folder must share the same `run.runId` / run identifier)

### What belongs here

- OpenLineage events (JSON) emitted by the run:
  - job/run lifecycle (start/complete/fail)
  - input/output dataset declarations
  - governed facets that support lineage and reproducibility
- A local manifest or roll-up (optional but recommended) that inventories event files and checksums.

### What does not belong here

- Secrets (tokens, connection strings), personal emails, or host-specific credentials.
- Hand-edited “fixes” to lineage. If an event is wrong, fix instrumentation/config and re-run.
- Freeform narrative notes (put those in `data/surficial-geology/lineage/notes/`).

---

## 🗂️ Directory Layout

~~~text
📁 run_<run_id>/                               — OpenLineage events for one pipeline run
├── 📄 README.md                               — This file (conventions + validation rules)
├── 🧾 manifest.json                           — (Recommended) inventory of event files + checksums + run pointer
├── 🧾 events.ndjson                           — (Optional) newline-delimited roll-up of all events in time order
├── 🧾 event_0001.json                         — Event #1 (chronological; zero-padded for stable sorting)
├── 🧾 event_0002.json                         — Event #2
└── 🧾 event_000N.json                         — Event #N (final observed event for the run)
~~~

Notes:

- File names shown above are **recommended conventions**. If your emitter produces different names,
  keep them deterministic and document the pattern in `manifest.json`.
- If both per-event JSON and `events.ndjson` are present, they must represent the **same event set**
  for the run (no drift).

---

## 🧭 Context

In the KFM pipeline, OpenLineage provides **event-level operational lineage**, complementary to:

- PROV summaries and run records (human/audit-friendly lineage)
- index and manifest layers (query-friendly lineage)
- STAC/DCAT catalog entries (dataset discovery)

Conceptually:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

This folder is the **raw event capture** for the run; higher-level lineage products should be generated
from these events (not edited in place).

---

## 📦 Data & Metadata

### Run identifier contract

- `<run_id>` in the folder name MUST match the run identifier used in emitted events.
- Recommended invariant:
  - folder name token == `run.runId` (or a stable string derived from it)
- If the pipeline system uses UUIDs, store the UUID as-is and avoid lossy truncation.

### Event file conventions

Recommended rules for per-event files:

- **Chronological ordering**: the numeric sequence must be non-decreasing with `eventTime`.
- **Stable formatting**: use consistent JSON formatting to reduce non-semantic diffs.
- **One event per file**: each `event_*.json` is a single OpenLineage event object.

Minimum expectations for each event:

- `eventTime` present and parseable (UTC/RFC3339 preferred)
- `run` object present (with `runId` or equivalent)
- `job` object present (stable `namespace` + `name`)
- `producer` present (identifies the emitter; do not embed tokens in this field)
- `inputs` / `outputs` (when applicable) reference **stable dataset identifiers**
  (prefer KFM dataset ids / URNs / STAC ids over ephemeral temp paths)

### `manifest.json` (recommended)

A lightweight roll-up for this run’s event folder.

Typical contents:

- `run_id` (must match `<run_id>`)
- list of event files (relative paths) + sizes + sha256 checksums
- count of events + min/max `eventTime`
- pointer to the canonical run record location (e.g., `mcp/runs/...`) when available
- optional notes about emitter/version (tool + version that generated these events)

---

## 🧪 Validation & CI/CD

Minimum expectations for committed per-run OpenLineage events:

- **JSON validity**: all `event_*.json` parse as JSON objects; `events.ndjson` (if present) parses line-by-line.
- **Run consistency**: every event’s run identifier matches `<run_id>`.
- **Schema sanity**: events are structurally consistent with the OpenLineage event schema used by the repo/tooling.
- **Determinism**: re-exporting the same run should not reorder events or introduce spurious diffs.
- **Checksums**: if `manifest.json` is present, checksums must match file contents.
- **Governance scans**: no secrets, no PII, and no sensitive precision leakage through facets.

---

## ⚖ FAIR+CARE & Governance

OpenLineage events can unintentionally leak sensitive operational details.

When emitting or storing events here:

- Do not include credentials in dataset URIs, facets, or environment payloads.
- Avoid embedding high-precision restricted locations or protected-site hints in facets.
- Prefer stable, governed identifiers (dataset ids, STAC ids, URNs) over raw local filesystem paths.
- If sovereignty/sensitivity flags apply, record the decision in lineage notes/manifests and ensure
  downstream indexing respects masking/generalization rules.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial per-run OpenLineage events README defining run-scoped conventions, recommended file patterns, and validation/governance expectations. |

---

<div align="center">

🪨 **Surficial Geology — Lineage**  
KFM Data Layer · Deterministic Pipelines · Open Provenance

[📘 Docs Root](../../../../../../docs/README.md) ·
[📂 Standards Index](../../../../../../docs/standards/README.md) ·
[📄 Templates Index](../../../../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0

</div>

