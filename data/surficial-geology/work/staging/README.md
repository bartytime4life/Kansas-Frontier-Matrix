---
title: "🧰 Surficial Geology — Work — Staging"
path: "data/surficial-geology/work/staging/README.md"

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
    - "data/surficial-geology/work/staging/**"

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

doc_uuid: "urn:kfm:doc:data:surficial-geology:work:staging-readme:v0.1.0"
semantic_document_id: "surficial-geology-work-staging-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:surficial-geology:work:staging-readme:v0.1.0"

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

# 🧰 **Surficial Geology — Work — Staging**
`data/surficial-geology/work/staging/README.md`

**Purpose**  
Provide a governed place for **candidate artifacts awaiting promotion** into authoritative locations (outputs, catalogs, lineage), while preventing accidental dependencies and preserving clear boundaries.

</div>

---

## 📘 Overview

This directory is a **staging area** for Surficial Geology work products that are:

- potentially useful beyond a single scratch session, but
- not yet accepted as deterministic, publishable, or audit-grade artifacts.

Use `work/staging/` for:

- candidate deliverables produced during iteration (pre-release vectors/tiles/metadata) awaiting validation,
- candidate STAC JSON drafts awaiting regeneration/validation/promotion,
- candidate packaging layouts (bundle structure previews) before they are made official,
- review-ready summaries that accompany a promotion PR.

This directory is **non-authoritative**:

- nothing here may be required by ETL, catalogs, lineage, API, UI, or tests,
- files may be replaced or deleted as promotion decisions evolve,
- if an artifact becomes “real,” it must be moved to its governed home and linked to lineage.

Do not use `work/staging/` for:

- raw source-of-record bytes (`data/surficial-geology/raw/**`),
- deterministic distributions (`data/surficial-geology/outputs/**`),
- machine-validated catalogs (`data/surficial-geology/stac/**`),
- audit-grade lineage (`data/surficial-geology/lineage/**`),
- reproducible run evidence (`mcp/runs/**` or `mcp/experiments/**`).

---

## 🗂️ Directory Layout

~~~text
📁 data/surficial-geology/work/                         — Work area (non-authoritative)
└── 📁 staging/                                         — Candidate artifacts awaiting promotion (this directory)
    ├── 📄 README.md                                    — This file
    ├── 📁 candidates/                                  — Candidate artifacts grouped by intent
    │   ├── 📁 outputs/                                 — Candidate outputs (do not treat as publishable)
    │   ├── 📁 stac/                                    — Candidate STAC JSON drafts (do not treat as authoritative)
    │   └── 📁 lineage/                                 — Candidate lineage notes/summaries (not audit-grade)
    ├── 📁 reviews/                                     — Review-ready summaries (small)
    └── 📁 _archive/                                    — Optional: superseded staging sets (keep minimal)
~~~

Notes:

- Keep staging artifacts small and review-oriented.
- Do not accumulate large binaries here; staging is not a second outputs area.
- If a candidate artifact is large, prefer storing only references + checksums and regenerate via pipeline.

---

## 🧭 Context

This folder supports the transition from “working” to “governed”:

Deterministic ETL → outputs → catalogs (STAC/DCAT) → lineage (PROV/OpenLineage) → graph → API → frontend → Story Nodes → Focus Mode

Staging exists to keep clear boundaries:

- **Raw** stays immutable and evidence-grade.
- **Outputs** stay deterministic and versioned.
- **Catalogs** stay machine-validated and consistent.
- **Lineage** stays audit-grade and queryable.

Promotion should always move artifacts to the correct governed home, not keep them in staging.

---

## 📦 Data & Metadata

**Promotion rule (required):** if an artifact is accepted, move it to one of:

- publishable distributions → `data/surficial-geology/outputs/**`
- catalog metadata → `data/surficial-geology/stac/**`
- audit-grade lineage and run notes → `data/surficial-geology/lineage/**`
- reproducible run evidence (configs/logs) → `mcp/runs/<run_id>/`

**Staging file hygiene (required):**

- no secrets, tokens, credentials, or signed URLs,
- no PII (personal emails/phones; do not paste upstream contact blocks),
- no restricted sensitive precision or discoverability guidance,
- avoid absolute workstation paths; prefer repo-relative paths.

**Recommended naming (optional but preferred):**

- `YYYY-MM-DD__<topic>__candidate.<ext>`
- `YYYY-MM-DD__run-<run_id>__<topic>__candidate.<ext>`

**What staging can contain safely:**

- small summaries describing what is expected to be promoted and why,
- checksums/manifests that help reviewers compare candidate vs prior outputs,
- small diffs and validation summaries (not full dataset copies).

---

## 🌐 STAC, DCAT & PROV Alignment

Staging is not intended to be referenced by governed catalog/provenance outputs.

- **STAC**: Collections/Items in `data/surficial-geology/stac/**` must not reference `work/staging/` paths.
- **DCAT**: distributions must not point to staging artifacts.
- **PROV/OpenLineage**: audit-grade records live under `data/surficial-geology/lineage/**` (and run evidence under `mcp/runs/**`), not in staging.

If a staging artifact must be cited by STAC/DCAT/PROV, it must be promoted first.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode must not depend on staging artifacts.

If a candidate introduces an end-user caveat or interpretive constraint, capture it in governed notes after promotion:

- dataset/run caveats → `data/surficial-geology/lineage/notes/`
- catalog caveats → `data/surficial-geology/stac/notes/`

---

## 🧪 Validation & CI/CD

Minimum expectations for commits under `work/staging/`:

- passes secret scanning and PII scanning expectations,
- remains non-essential (no build/test/runtime dependency),
- avoids large binaries and bulk dataset copies,
- does not include mutable “latest” files intended to be overwritten repeatedly.

Promotion should be gated by the same validations required for the target surface (outputs/catalogs/lineage), not by staging content.

---

## ⚖ FAIR+CARE & Governance

Staging can accidentally become a “shadow publish surface” if not controlled.

Rules:

- do not stage restricted or sensitive precision artifacts,
- do not stage artifacts with unclear rights/redistribution terms,
- keep staging content minimal and move governance-significant decisions into lineage notes/manifests when finalized,
- when in doubt, stage summaries and checksums only, then regenerate deterministically during promotion.

See governance and sovereignty policies linked in the footer.

---

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v0.1.0**  | 2025-12-14 | Initial `work/staging/` README defining scope, promotion boundaries, hygiene rules, and governance constraints. |

---

<div align="center">

🧰 **Surficial Geology — Work — Staging**  
KFM Data Layer · Candidate Artifacts · Governance-Aware

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

