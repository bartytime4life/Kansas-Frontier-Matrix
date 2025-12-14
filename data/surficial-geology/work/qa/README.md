---
title: "🔍 Surficial Geology — Work — QA"
path: "data/surficial-geology/work/qa/README.md"

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
    - "data/surficial-geology/work/qa/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:qa-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-qa-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:qa-readme:v0.1.0"

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

# 🔍 **Surficial Geology — Work — QA**
`data/surficial-geology/work/qa/README.md`

**Purpose**  
Provide a governed place for **QA/QC workspace artifacts** (checks, summaries, diffs) used to validate Surficial Geology processing before promoting changes into deterministic pipelines, outputs, catalogs, or lineage.

</div>

---

## 📘 Overview

This folder is for **quality assurance work products** created during development and review.

Use `work/qa/` for:

- quick validation outputs (geometry validity checks, schema diffs, counts, bounds checks),
- short summary reports for reviewers (what changed, what passed/failed, what needs attention),
- small samples used for debugging (limited-size extracts, not full datasets),
- plots/tables used to confirm expected results.

Do **not** treat anything in this folder as authoritative.

If a QA artifact becomes important for auditability or provenance, it must be promoted to a governed lineage/run location (see below).

---

## 🗂️ Directory Layout

~~~text
📁 work/qa/                                         — QA/QC workspace (this directory)
├── 📄 README.md                                     — This file (rules + scope)
├── 📁 reports/                                      — Human-readable summaries (small, review-friendly)
├── 📁 checks/                                       — Machine-readable check outputs (small)
├── 📁 diffs/                                        — Schema/attribute/extent diffs (small)
├── 📁 samples/                                      — Tiny representative samples for debugging (strictly limited)
└── 📁 _archive/                                     — Optional: superseded QA notes (keep minimal)
~~~

Notes:

- Keep artifacts small and review-oriented.
- Avoid committing large binaries or full dataset copies here.

---

## 🧭 Context

This folder supports pre-merge and pre-release validation without polluting governed surfaces:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

`work/qa/` exists so QA can happen while keeping:

- `raw/` immutable,
- `outputs/` deterministic and versioned,
- `stac/` machine-validated,
- `lineage/` audit-grade.

---

## 📦 Data & Metadata

### Non-authoritative rule

Nothing in `work/qa/` may be required by:

- ingestion/ETL,
- STAC/DCAT generation,
- provenance generation,
- graph ingestion,
- API runtime,
- frontend/Story Nodes/Focus Mode.

If a pipeline depends on it, it does not belong here.

### Recommended naming

For QA artifacts tied to a specific run or change, prefer sortable names:

- `YYYY-MM-DD__<topic>.md`
- `YYYY-MM-DD__run-<run_id>__<topic>.<ext>`
- `YYYY-MM-DD__pr-<num>__<topic>.<ext>` (if you track PR numbers)

### Promote-or-delete rule

If an artifact is needed long-term, move it to the correct governed location:

- reproducible run logs/config snapshots → `mcp/runs/<run_id>/`
- provenance/audit evidence → `data/surficial-geology/lineage/**`
- publishable metadata → `data/surficial-geology/outputs/metadata/**`
- publishable catalog records → `data/surficial-geology/stac/**`

---

## 🌐 STAC, DCAT & PROV Alignment

`work/qa/` should not be referenced by catalog or provenance artifacts.

- STAC Items/Collections should reference **outputs** and governed provenance, not `work/qa/`.
- DCAT distributions should point to publishable assets and governed documentation, not `work/qa/`.
- PROV/OpenLineage should reference run artifacts and inputs/outputs, not QA scratch products.

If you need to cite QA results in lineage, promote them to `data/surficial-geology/lineage/notes/` (human) or `mcp/runs/` (run evidence) and reference from there.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on `work/qa/`.

If a QA result is important for narrative interpretation (limitations, known issues, caveats), capture it in:

- `data/surficial-geology/lineage/notes/` (domain/run caveats), and/or
- `data/surficial-geology/stac/notes/` (catalog-specific caveats)

---

## 🧪 Validation & CI/CD

Minimum expectations for anything committed here:

- no secrets, tokens, credentials, or signed URLs,
- no PII,
- no sensitive restricted precision beyond policy thresholds,
- small footprint (avoid large binaries and large dataset extracts),
- does not introduce repo dependencies (build/test must not rely on these files).

If a QA artifact represents a formal acceptance gate, it belongs in deterministic validation tooling and run records, not in `work/qa/`.

---

## ⚖ FAIR+CARE & Governance

QA artifacts can accidentally expose sensitive operational details or enable inference.

- Do not store restricted coordinates, discoverability guidance, or sensitive site references.
- Avoid embedding provider contact details or personal emails.
- Record governance-relevant QA decisions in lineage notes/manifests, not in scratch files.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/qa/` README defining QA workspace scope, promotion rules, and boundaries vs outputs/catalogs/lineage. |

---

<div align="center">

🔍 **Surficial Geology — Work — QA**  
KFM Data Layer · QA Workspace · Governance-Aware

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

© 2025 Kansas Frontier Matrix — CC-BY 4.0

</div>

