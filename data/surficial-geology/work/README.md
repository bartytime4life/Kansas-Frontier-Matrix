---
title: "🧰 Surficial Geology — Work"
path: "data/surficial-geology/work/README.md"

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
    - "data/surficial-geology/work/**"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

doc_uuid: "urn:kfm:doc:data:surficial-geology:work-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work-readme:v0.1.0"

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

# 🧰 **Surficial Geology — Work**
`data/surficial-geology/work/README.md`

**Purpose**  
Provide a governed workspace for **non-authoritative, in-progress** artifacts used during ingestion, QA/QC, and local experimentation—without contaminating raw inputs, deterministic outputs, or catalog/provenance records.

</div>

---

## 📘 Overview

This directory is a **workspace** for Surficial Geology tasks. It is **not** a publishing surface and **not** a source of truth.

Use `work/` for:

- temporary or exploratory artifacts (small subsets, quick plots, scratch scripts, intermediate notes),
- QA/QC scratch outputs that help confirm correctness before a deterministic pipeline change,
- staging artifacts awaiting promotion into the correct governed location.

Do not use `work/` for:

- **raw source intake** (use `data/surficial-geology/raw/`),
- **deterministic distributions** (use `data/surficial-geology/outputs/`),
- **repeatable processing artifacts** (use `data/processed/` if that exists for the domain),
- **run logs/config snapshots** (use `mcp/runs/` or `mcp/experiments/`),
- **catalog metadata** (use `data/surficial-geology/stac/` and DCAT locations per repo policy),
- **lineage/provenance** (use `data/surficial-geology/lineage/`).

Work artifacts are expected to be **minimal, disposable, and non-breaking**.

---

## 🗂️ Directory Layout

~~~text
📁 work/                                            — Non-authoritative workspace (this directory)
├── 📄 README.md                                     — This file (rules + scope)
├── 📁 scratch/                                      — Small experiments, notes, throwaways
├── 📁 staging/                                      — Candidate artifacts awaiting promotion
├── 📁 qa/                                           — QA/QC scratch results (summaries, check outputs)
└── 📁 tmp/                                          — Short-lived intermediates (prefer to keep empty)
~~~

Notes:

- Folder names above are recommended conventions; keep the structure boring and predictable.
- Avoid committing large binaries or voluminous intermediates here. If something must be retained for auditability, it belongs in lineage (`data/surficial-geology/lineage/`) or run artifacts (`mcp/runs/`), not here.

---

## 🧭 Context

`work/` supports development and review steps around the core pipeline:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

This folder exists to keep the repo organized:

- Raw inputs stay immutable and traceable.
- Outputs stay deterministic and versioned.
- Catalogs and provenance remain machine-validated.
- Workspace artifacts do not become accidental dependencies.

---

## 📦 Data & Metadata

Rules for anything placed in `work/`:

- **Non-authoritative**: nothing in `work/` should be required by the pipeline, API, or UI.
- **Promote or delete**: if an artifact becomes important, move it to the correct governed location and record lineage appropriately.
- **Small and readable**: prefer text, small samples, and short summaries over large datasets.
- **No secrets and no PII**: never place tokens, credentials, personal emails, or other sensitive identifiers here.
- **No “fixing” data here**: if you discover an issue, fix the deterministic transform/config/code and regenerate outputs.

Promotion guidance (where artifacts should go once “real”):

- source bytes and source snapshots → `data/surficial-geology/raw/`
- distribution artifacts (vectors/tiles/metadata) → `data/surficial-geology/outputs/`
- lineage evidence (manifests, PROV, OpenLineage) → `data/surficial-geology/lineage/`
- run records and logs/config snapshots → `mcp/runs/` (or `mcp/experiments/` for research)

---

## 🌐 STAC, DCAT & PROV Alignment

`work/` is not intended to be referenced by catalogs or provenance.

- STAC Items and Collections should reference **versioned outputs** and governed provenance artifacts, not `work/`.
- DCAT distributions should point to publishable artifacts (typically outputs), not `work/`.
- PROV should not treat `work/` as a stable entity store. If an artifact is necessary to explain a run, store it in `mcp/runs/` or `data/surficial-geology/lineage/` and link it from there.

If something in `work/` needs to be cited as evidence, it is in the wrong place—promote it.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on `work/`.

- Narratives should link to STAC ids, output assets, and lineage artifacts.
- Any interpretation or caveat intended for end users should be recorded in governed notes (e.g., `data/surficial-geology/lineage/notes/` or STAC notes), not in `work/`.

---

## 🧪 Validation & CI/CD

Minimum expectations for `work/`:

- passes secret scanning and PII scanning policies,
- does not introduce required dependencies (builds/tests must not rely on `work/` content),
- does not accumulate large binary artifacts that bloat the repo,
- does not contain “latest” pointers or mutable files intended to be overwritten repeatedly.

If CI has size guards or forbidden-pattern checks, `work/` should remain compliant by design.

---

## ⚖ FAIR+CARE & Governance

Workspaces can accidentally leak sensitive operational details.

- Do not store credentials, internal endpoints, or contact PII.
- Do not store restricted location precision or discoverability guidance.
- When sovereignty-related constraints apply, default to generalization and move governance-significant decisions into lineage notes and manifests (not workspace scratch files).

See the governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/` README defining workspace scope, promotion rules, and boundaries vs raw/outputs/catalogs/lineage. |

---

<div align="center">

🧰 **Surficial Geology — Work**  
KFM Data Layer · Non-Authoritative Workspace · Governance-Aware

[📘 Docs Root](../../../docs/README.md) ·
[📂 Standards Index](../../../docs/standards/README.md) ·
[📄 Templates Index](../../../docs/templates/README.md) ·
[⚙ CI/CD Workflows](../../../docs/workflows/README.md) ·
[📈 Telemetry Standard](../../../docs/standards/telemetry_standards.md) ·
[📊 Telemetry Docs](../../../docs/telemetry/README.md) ·
[♿ UI Accessibility Standard](../../../docs/standards/ui_accessibility.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

