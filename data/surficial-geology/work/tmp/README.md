---
title: "🧰 Surficial Geology — Work — Tmp"
path: "data/surficial-geology/work/tmp/README.md"

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
    - "data/surficial-geology/work/tmp/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:tmp-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-tmp-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:tmp-readme:v0.1.0"

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

# 🧰 **Surficial Geology — Work — Tmp**
`data/surficial-geology/work/tmp/README.md`

**Purpose**  
Provide a controlled place for **short-lived, non-authoritative intermediates** used during local work, while keeping `raw/`, `outputs/`, `stac/`, and `lineage/` clean and deterministic.

</div>

---

## 📘 Overview

This directory is a **temporary workspace** for Surficial Geology.

Use `work/tmp/` for:

- transient intermediate files created during local experimentation,
- short-lived conversion artifacts used to confirm a hypothesis,
- scratch outputs that should not be preserved as part of the domain’s governed record.

This directory is **non-authoritative**:

- nothing here may be required by ETL, catalogs, lineage, API, UI, or tests,
- files here should be treated as disposable,
- if anything becomes important to reproduce, validate, publish, or audit, it must be promoted to a governed location.

Expectation: `tmp/` should be **empty or near-empty** in normal operation.

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/                    — Work area (non-authoritative)
└── 📁 tmp/                                        — Short-lived intermediates (this directory)
    └── 📄 README.md                               — This file
~~~

Notes:

- Do not create deep structure here unless a specific workflow requires it.
- Prefer keeping `tmp/` empty in committed history.

---

## 🧭 Context

`work/tmp/` exists to protect governed surfaces:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Hard boundaries:

- Immutable source intake belongs in `data/surficial-geology/raw/**`
- Deterministic deliverables belong in `data/surficial-geology/outputs/**`
- Catalog metadata belongs in `data/surficial-geology/stac/**`
- Audit-grade lineage belongs in `data/surficial-geology/lineage/**`
- Reproducible run evidence belongs in `mcp/runs/**` (or `mcp/experiments/**` for research)

`tmp/` is allowed only for ephemeral local work.

---

## 📦 Data & Metadata

Rules for `tmp/`:

- **Prefer not committing files here.**
- If a workflow produces intermediates, route them to local working directories or run workspaces; do not treat `tmp/` as a second outputs directory.
- **No secrets / no PII** (tokens, credentials, signed URLs, personal emails/phones).
- **No restricted precision** or discoverability guidance for sensitive locations.
- **No “canonical” conversions**: do not create official exports here; official exports must be generated deterministically and stored under `outputs/` (with provenance).

Promotion rule:

If an artifact is needed beyond a short debugging session, move it to the correct governed home:

- publishable distributions → `data/surficial-geology/outputs/**`
- catalog metadata → `data/surficial-geology/stac/**`
- provenance/notes/manifests → `data/surficial-geology/lineage/**`
- run reproducibility evidence → `mcp/runs/<run_id>/`

---

## 🌐 STAC, DCAT & PROV Alignment

This folder must not be referenced by:

- STAC Collections/Items (`data/surficial-geology/stac/**`)
- DCAT dataset/distribution records
- PROV/OpenLineage artifacts (`data/surficial-geology/lineage/**`)

If something in `tmp/` needs to be referenced by STAC/DCAT/PROV, it is in the wrong place—promote it first.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on `work/tmp/`.

If a temporary finding creates a user-facing caveat, record it in governed notes after validation:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`
- catalog caveats → `data/surficial-geology/stac/notes/`

---

## 🧪 Validation & CI/CD

Minimum expectations for the `tmp/` directory:

- remains small (ideally only this README),
- passes secret scanning and PII scanning,
- introduces no repo dependencies (build/test/ETL must not rely on `tmp/` content),
- does not accumulate binaries or repeated intermediates.

If CI enforces size or forbidden-pattern rules, `tmp/` should remain compliant by design.

---

## ⚖ FAIR+CARE & Governance

Temporary does not mean safe by default.

- Do not place restricted-location artifacts here.
- Do not paste provider contact blocks from metadata (PII).
- Do not copy content with unclear rights into this folder.

If a governance-relevant decision occurs during local work, record the decision in a governed location and enforce it in deterministic pipelines and catalogs.

See policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/tmp/` README defining ephemeral scope, non-dependency rules, and promotion boundaries. |

---

<div align="center">

🧰 **Surficial Geology — Work — Tmp**  
KFM Data Layer · Ephemeral Workspace · Governance-Aware

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

