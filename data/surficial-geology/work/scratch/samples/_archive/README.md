---
title: "🗃️ Surficial Geology — Work — Scratch — Samples Archive"
path: "data/surficial-geology/work/scratch/samples/_archive/README.md"

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
    - "data/surficial-geology/work/scratch/samples/_archive/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:scratch:samples:archive-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-scratch-samples-archive-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:scratch:samples:archive-readme:v0.1.0"

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

# 🗃️ **Surficial Geology — Work — Scratch — Samples Archive**
`data/surficial-geology/work/scratch/samples/_archive/README.md`

**Purpose**  
Store **superseded scratch sample artifacts** (tiny, disposable debugging samples) so the active `samples/` folder stays clean, while ensuring nothing here becomes a pipeline, catalog, or provenance dependency.

</div>

---

## 📘 Overview

This folder archives **small, non-authoritative samples** that were used temporarily during local debugging and exploration.

Archive a sample here when:

- it is no longer actively used,
- it helped resolve a specific investigation and is only worth keeping as a minimal breadcrumb,
- it is small and safe to retain under governance rules.

This folder is **not** a source-of-truth and must not be treated as:

- a raw source intake location (`data/surficial-geology/raw/**`),
- a deterministic output distribution (`data/surficial-geology/outputs/**`),
- a catalog surface (`data/surficial-geology/stac/**`),
- provenance evidence (`data/surficial-geology/lineage/**`),
- or a reproducibility/run record (`mcp/runs/**`).

If a sample is needed for reproducibility or long-term validation, it does not belong here—promote it to the correct governed location.

---

## 🗂 Directory Layout

~~~text
📁 data/surficial-geology/work/scratch/                 — Scratch workspace (non-authoritative)
└── 📁 samples/                                         — Scratch samples (non-authoritative)
    ├── 📄 README.md                                    — Samples rules + boundaries
    └── 📁 _archive/                                    — Superseded samples (this directory)
        ├── 📄 README.md                                — This file
        └── 📄 YYYY-MM-DD__<short_slug>.<ext>           — Archived sample (tiny; keep minimal)
~~~

Notes:

- Prefer preserving the original filename when moving a sample into `_archive/`.
- If there is a collision, add a deterministic suffix (example: `__superseded`).
- Keep the archive minimal; delete true throwaways instead of archiving everything.

---

## 🧭 Context

This archive exists to prevent scratch clutter while keeping strict boundaries between:

- **raw** (immutable intake),
- **outputs** (deterministic deliverables),
- **stac** (machine-validated catalog metadata),
- **lineage** (audit-grade provenance),
- **work/scratch** (non-authoritative iteration artifacts).

Archived samples must never be referenced by production surfaces (ETL, catalog generation, graph ingest, API, UI).

---

## 📦 Data & Metadata

Rules for archived samples:

- **Keep them tiny**: minimal rows/features/pixels and minimal spatial extent.
- **No new “official” conversions**: do not treat archive samples as canonical exports.
- **No dependencies**: nothing in this folder may be required by any deterministic pipeline step or validation gate.
- **No secrets / no PII**: never store tokens, credentials, personal emails, phone numbers, or similar.
- **No restricted precision**: do not store samples that disclose disallowed sensitive locations or discoverability guidance.

Recommended naming:

- `YYYY-MM-DD__<topic>.<ext>`
- `YYYY-MM-DD__run-<run_id>__<topic>.<ext>` (only if helpful; still non-authoritative)

Promotion guidance:

- reproducible run evidence → `mcp/runs/<run_id>/`
- audit-grade curated findings → `data/surficial-geology/lineage/notes/`
- publishable derivatives → `data/surficial-geology/outputs/**`
- long-lived documentation → appropriate `docs/**` or domain READMEs

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`)
- DCAT dataset/distribution records
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`)

If a sample must be referenced by STAC/DCAT/PROV, it is in the wrong place—promote it first.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not rely on archived scratch samples as evidence.

If an archived sample revealed a caveat that matters for interpretation or publication, record that caveat in governed notes:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`
- catalog caveats → `data/surficial-geology/stac/notes/`

---

## 🧪 Validation & CI/CD

Minimum expectations for anything committed here:

- passes secret scanning and PII scanning expectations,
- remains small (no large binaries, no bulk extracts),
- does not introduce repo dependencies (build/test/ETL must not rely on these files),
- does not contain mutable “latest” artifacts intended to be overwritten repeatedly.

If a “sample” becomes part of a formal test fixture strategy, it should move to the repo’s governed test/fixture location (if defined) with explicit governance review.

---

## ⚖ FAIR+CARE & Governance

Archived scratch samples can still create harm if they:

- disclose restricted location precision,
- duplicate restricted content without rights support,
- embed operational or contact details copied from upstream metadata.

When in doubt, do not archive; delete and record only the minimal governed lesson in lineage notes.

See the governance and sovereignty policies linked in the footer.

---

## 🕰 Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `samples/_archive/` README defining purpose, non-dependency rules, and promotion boundaries. |

---

<div align="center">

🗃️ **Surficial Geology — Work — Scratch — Samples Archive**  
KFM Data Layer · Scratch Archive · Governance-Aware

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

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

