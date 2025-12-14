---
title: "🔗 Surficial Geology — Lineage Notes"
path: "data/surficial-geology/lineage/notes/README.md"

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
    - "data/surficial-geology/lineage/notes/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:lineage-notes-readme:v0.1.0"
semantic_document_id: "surficial-geology-lineage-notes-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:lineage-notes-readme:v0.1.0"

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

# 🔗 **Surficial Geology — Lineage Notes**
`data/surficial-geology/lineage/notes/README.md`

**Purpose**  
Capture **human-readable** lineage context for Surficial Geology outputs—decisions, caveats, and review notes—without replacing the machine-readable manifests and PROV traces.

</div>

---

## 📘 Overview

This folder exists for **narrative provenance**: the “why” behind pipeline outputs and catalog metadata.

Use `lineage/notes/` when you need to document things that are hard to express in strict schemas, such as:

- Interpretation choices (e.g., classification harmonization, field mapping rationale)
- Known limitations (coverage gaps, geometry artifacts, attribute caveats)
- QA/QC outcomes that matter to downstream users
- Governance and stewardship decisions (generalization/redaction rationale)
- Reconciliation notes when source updates change outputs across versions

### Relationship to other lineage folders

This directory complements (but does not replace):

- `../manifests/` — authoritative, machine-readable source + transform manifests
- `../indexes/` — searchable/compiled indexes over manifests/runs (where applicable)
- `../../outputs/` — the generated artifacts that must be reproducible and checksum-tracked

If a note describes a change that affects reproducibility or interpretation, the corresponding **manifest(s), STAC/DCAT record(s), and/or PROV summary** must be updated to match.

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/lineage/notes/          — Human-readable lineage notes (this directory)
├── 📄 README.md                                 — This file
├── 📄 YYYY-MM-DD__<short_slug>.md               — Single-topic note (recommended pattern)
├── 📄 YYYY-MM-DD__run-<run_id>__summary.md      — Optional: per-run narrative summary
└── 📁 _archive/                                 — Optional: superseded notes kept for auditability
~~~

Recommended conventions:

- Keep note filenames **boring and sortable**: `YYYY-MM-DD__<short_slug>.md`
- Prefer one topic per note; add new notes rather than editing history heavily.
- If a note is superseded, keep it and add a newer note that points back to it (don’t erase audit trails).

---

## 🧭 Context

These notes sit alongside the provenance chain that powers the KFM pipeline:

Deterministic ETL → catalogs (STAC/DCAT/PROV) → graph (Neo4j) → API → frontend → Story Nodes → Focus Mode

`lineage/notes/` is primarily for:

- Curators and maintainers validating transformations
- Reviewers performing governance checks
- Future contributors trying to reproduce or extend the work
- Focus Mode narrative builders who need defensible caveats and framing

---

## 📦 Data & Metadata

### What each note should include

Each note SHOULD include, in plain language:

- **Scope**: what dataset/version/output(s) the note pertains to
- **Trigger**: why the note exists (e.g., anomaly found, source update, schema change)
- **Decision / outcome**: what was changed (or not changed) and why
- **Evidence pointers** (paths, not inline dumps):
  - run log folder in `mcp/runs/...` (preferred)
  - relevant manifest(s) in `../manifests/...`
  - output artifacts in `../../outputs/...`
  - STAC/DCAT records under `data/stac/...` or catalog mapping docs (if applicable)

### What not to put in notes

- Raw source payloads (store under `data/raw/` with a proper source manifest)
- Secrets, tokens, credentials, internal URLs requiring auth
- Personal data (PII) or doxxing risk content
- Sensitive site specifics or “how to locate” guidance (see governance section)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

When a note materially changes interpretation, add it as a **documentation asset** in the relevant STAC Collection/Item (e.g., role `documentation`) and point to the note by path.

### DCAT

If notes are part of a public “distribution package,” they may be represented as a documentation distribution. Otherwise, keep them as internal audit artifacts referenced by provenance.

### PROV

Notes can be treated as provenance-supporting `prov:Entity` records (documentation artifacts) and referenced from the producing `prov:Activity` summary (e.g., the run that generated or revised outputs).

---

## 🧪 Validation & CI/CD

Minimum expectations before committing or updating notes:

- **No sensitive precision**: avoid exact coordinates or actionable location instructions.
- **Path accuracy**: referenced files/folders must exist (manifests, outputs, runs).
- **Reproducibility respect**: if a note describes a change, ensure:
  - manifests reflect it
  - checksums are updated where applicable
  - the run record exists or is linked
- **Governance scans**: notes must pass secret/PII scanning policies.

---

## ⚖ FAIR+CARE & Governance

Even descriptive notes can cause harm if they increase the discoverability of sensitive places.

Rules of thumb:

- Prefer **generalization** over precision (county-level, watershed-level, or “within Kansas”).
- If a discussion involves sovereignty or sensitive sites, document **process and safeguards**, not discoverability.
- Record redaction/generalization decisions explicitly in the note when applicable.

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `lineage/notes/` README defining scope, naming conventions, and how narrative lineage complements manifests and PROV. |

---

<div align="center">

🔗 **Surficial Geology — Lineage Notes**  
KFM Data Layer · Provenance-First · Human-Readable Audit Trail

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

