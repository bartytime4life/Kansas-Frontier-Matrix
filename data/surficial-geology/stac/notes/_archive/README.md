---
title: "🗃️ Surficial Geology — STAC Notes Archive"
path: "data/surficial-geology/stac/notes/_archive/README.md"

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
    - "data/surficial-geology/stac/notes/_archive/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:stac:notes:archive-readme:v0.1.0"
semantic_document_id: "surficial-geology-stac-notes-archive-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:stac:notes:archive-readme:v0.1.0"

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

# 🗃️ **Surficial Geology — STAC Notes Archive**
`data/surficial-geology/stac/notes/_archive/README.md`

**Purpose**  
Hold **superseded** STAC catalog notes for auditability (append-only history), while keeping active STAC guidance in `data/surficial-geology/stac/notes/`.

</div>

---

## 📘 Overview

This directory stores **archived (superseded) STAC notes** for the Surficial Geology dataset-local STAC catalog.

Archive notes here when they are no longer the current guidance due to:

- catalog migrations (IDs, paths, link policies),
- changes to STAC profile/extension usage,
- sharding strategy changes,
- updated governance or publication rules that invalidate older guidance.

Archive notes are:

- **Documentation artifacts** (not machine-validated STAC JSON),
- **Append-only** (do not rewrite history),
- **Audit-oriented** (kept to explain past decisions and transitions).

Use the active notes folder for current guidance:

- `data/surficial-geology/stac/notes/`

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/stac/notes/                 — STAC notes (current + archive)
├── 📄 README.md                                      — Current STAC notes index
├── 📄 YYYY-MM-DD__<short_slug>.md                    — Current note(s)
└── 📁 _archive/                                      — Superseded notes (this directory)
    ├── 📄 README.md                                  — This file
    └── 📄 YYYY-MM-DD__<short_slug>.md                — Archived note(s) (kept as-is)
~~~

Recommended conventions:

- Prefer keeping the original filename when moving a note into `_archive/`.
- If the same filename would collide, add a suffix:
  - `YYYY-MM-DD__<short_slug>__superseded.md`
- When archiving a note, create or update an active note that points to the archived path and explains what replaced it.

---

## 🧭 Context

STAC notes support the catalog layer:

Deterministic ETL → outputs (tiles/vectors/metadata) → STAC (Collections/Items) → graph ingestion → API → frontend → Story Nodes → Focus Mode

This archive exists to preserve the “paper trail” of catalog decisions without requiring consumers to infer history from diffs alone.

Canonical catalog entry points remain:

- `data/surficial-geology/stac/README.md`
- `data/surficial-geology/stac/collections/`
- `data/surficial-geology/stac/items/`

---

## 📦 Data & Metadata

### Archiving rules

When moving a note into `_archive/`:

- Do not edit the content unless you are removing disallowed content (secrets/PII/sensitive precision). If redaction is necessary, document the redaction decision in a new active note.
- Add a short pointer in the active notes folder describing:
  - what replaced the archived guidance,
  - the effective date of the replacement,
  - any migration impacts (IDs, paths, sharding scheme, link policy).

### What not to store here

- Raw data, derived outputs, or STAC JSON.
- Large pasted logs or external text dumps.
- Secrets, tokens, credentials, PII, or restricted sensitive precision.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

Archived notes should not be required for STAC validation or traversal. They are optional documentation and should not be treated as authoritative metadata in place of STAC JSON.

### DCAT

If documentation distributions are published, archived notes should generally remain internal audit artifacts unless explicitly included by the publication policy.

### PROV

Archive notes may be modeled as documentation `prov:Entity` artifacts referenced by:

- catalog migration activities, or
- governance review activities,

but authoritative run lineage remains in:

- `data/surficial-geology/lineage/prov/`
- `data/surficial-geology/lineage/openlineage/`
- `mcp/runs/` (run logs/config snapshots)

---

## 🧪 Validation & CI/CD

Minimum expectations for archived notes:

- no secrets and no PII,
- no disallowed sensitive precision,
- repo-relative paths are accurate if referenced,
- archived notes do not introduce requirements that contradict current governance.

---

## ⚖ FAIR+CARE & Governance

Archived documentation can still create risk if it contains:

- sensitive location discoverability details,
- internal endpoints, credentials, or signed URLs,
- personal contact details.

If any archived note would violate governance, redact by policy and record the decision and scope in an active note (do not silently modify history).

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `_archive/` README defining purpose, layout, and append-only archive rules for STAC notes. |

---

<div align="center">

🗃️ **Surficial Geology — STAC Notes Archive**  
KFM Catalog Layer · Audit Trail · Governance-Aware

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

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

