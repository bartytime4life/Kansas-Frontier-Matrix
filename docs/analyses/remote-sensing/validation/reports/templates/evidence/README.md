---
title: "🧾 KFM — Evidence Templates for Remote Sensing Validation Reports (Maps · Plots · Tables · Indexes)"
path: "docs/analyses/remote-sensing/validation/reports/templates/evidence/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Templates Guide"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-evidence-templates"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:templates:evidence:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-report-evidence-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/templates/evidence/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧾 **KFM — Evidence Templates for Validation Reports**
`docs/analyses/remote-sensing/validation/reports/templates/evidence/README.md`

**Purpose**  
Canonical templates and rules for producing **evidence artifacts** (maps, plots, tables) and **evidence indexes**
used in remote-sensing validation reports (daily, per-run, and release).

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Templates" src="https://img.shields.io/badge/Evidence-Templates-blue" />
<img alt="Determinism" src="https://img.shields.io/badge/Determinism-Pinned-informational" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

“Evidence” is the **supporting artifact set** for a validation report:

- **Plots** (aggregated distributions, deltas, error curves),
- **Maps** (generalized spatial summaries, safe AOI rollups),
- **Tables** (metric summaries, thresholds, pass/fail reason codes),
- **Indexes** (machine-readable and human-readable registries of evidence items).

Evidence templates exist to enforce:

- determinism (stable bins, stable rounding, stable sort order),
- governance safety (no sensitive leakage),
- accessibility (alt text and readable captions),
- consistency across daily/per-run/release report layouts.

---

## ✅ What evidence templates are for

Evidence templates standardize:

- file naming conventions,
- minimum caption/metadata requirements,
- aggregation and safe visualization posture,
- evidence indexing in:
  - JSON (machine-readable inventory),
  - Markdown (human navigation).

Evidence templates are intentionally **generic** and should not bake in dataset-specific assumptions.

---

## 🗂️ Directory Layout (templates)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/templates/evidence/                 — Evidence template root
├── 📄 README.md                                                                      — This index (you are here)
├── 📁 indexes/                                                                       — Evidence index templates (JSON + MD)
│   ├── 🧾 release_evidence_index.template.json                                       — Template: releases/v<semver>/evidence/release_evidence_index.json
│   └── 📄 release_evidence_index.template.md                                         — Template: releases/v<semver>/evidence/release_evidence_index.md
├── 📁 plots/                                                                         — Plot templates and caption conventions
│   ├── 📄 plots.README.template.md                                                   — Template: evidence/plots/README.md
│   └── 📄 plot_caption.template.md                                                   — Template: per-plot caption blocks (optional)
├── 📁 maps/                                                                          — Map templates and safe-extent rules
│   ├── 📄 maps.README.template.md                                                    — Template: evidence/maps/README.md
│   └── 📄 map_caption.template.md                                                    — Template: per-map caption blocks (optional)
└── 📁 tables/                                                                        — Table templates and stable ordering rules
    ├── 📄 tables.README.template.md                                                  — Template: evidence/tables/README.md
    └── 📄 table_caption.template.md                                                  — Template: per-table caption blocks (optional)
~~~

Notes:

- Keep the template surface area small.
- Add only what you actively use and can govern.

---

## 🧩 Evidence classes (recommended)

### 1) Plots

Intended for deterministic, review-friendly figures:

- error distributions (MAE/RMSE histograms with pinned bins),
- time-series summary plots (p50/p90 bands over time),
- drift deltas (release-to-release aggregate deltas).

Plot rules:

- pin bins and axis ranges where relevant,
- record rounding policy in captions (e.g., “rounded to 3 decimals”),
- never include raw coordinate scatter for restricted inputs.

### 2) Maps

Maps are high-risk for leakage. Only include:

- generalized spatial summaries (region-level, coarse grid, H3 at governed resolution),
- masked/aggregated patterns that meet minimum group-size constraints.

Map rules:

- do not publish precise point locations unless explicitly allowed by governance labels,
- prefer region labels and aggregated choropleths,
- include the generalization method in captions (e.g., “H3 r8 aggregation; min_count=25”).

### 3) Tables

Tables should emphasize:

- aggregate metrics and thresholds,
- pass/fail outcomes and reason codes,
- stable ordering (by algorithm family, then algorithm_id, then dataset_id).

Table rules:

- do not list restricted sample IDs,
- avoid long per-sample enumerations in public docs,
- include sorting keys and rounding policy.

### 4) Evidence indexes

Indexes bind the evidence to deterministic identifiers:

- machine-readable inventory (`.json`),
- human-readable navigation (`.md`).

Index rules:

- stable ordering (by evidence_id or filename),
- include sha256 digests for every referenced evidence file,
- include governance posture summary (CARE/sovereignty gate outcomes).

---

## 🧷 Standard placeholders (use consistently)

Use these placeholders exactly (case-sensitive):

- `YYYY`, `MM`, `DD` (daily hierarchy)
- `<run_id>` (per-run directory key)
- `v<semver>` (release directory key)
- `<latest-commit-hash>` (repo commit SHA)
- `<sha256>` (digest placeholder)
- `<dataset_id>` / `<collection_id>` / `<item_id>`
- `<algorithm_id>` / `<params_hash>`
- `<created_utc>` (ISO8601 UTC time, when required)

---

## 🎯 Determinism requirements (non-negotiable)

Evidence artifacts MUST be reproducible:

- stable file naming and stable relative paths,
- stable ordering in tables and indexes,
- pinned bins/thresholds for plots,
- explicit rounding policy for numeric values,
- explicit sampling seed and sampling frame when sampling is used.

Avoid:

- “auto” binning or “auto” axis scaling when it impacts comparability,
- embedding local machine metadata (paths, hostnames),
- non-deterministic ordering in indexes.

---

## 🛡️ FAIR+CARE and sovereignty posture (mandatory)

Evidence is a common leakage vector.

Hard rules:

- no precise coordinates unless explicitly permitted by labels,
- no signed URLs, secrets, internal endpoints,
- no restricted dataset identifiers where policy forbids,
- no “how to locate” guidance.

If governance status is unclear:

- fail closed in publication posture:
  - redact maps,
  - publish only aggregated metrics,
  - record gate results in the evidence index and report summary.

---

## ♿ Accessibility requirements (WCAG-aligned)

Every evidence item SHOULD include:

- a short title,
- a descriptive caption,
- alt text for images (or a text equivalent in Markdown),
- units and scale notes,
- generalization/aggregation notes (for maps).

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- evidence indexes exist for releases,
- index entries have:
  - stable references,
  - sha256 digests,
  - deterministic ordering,
- forbidden patterns are absent:
  - coordinates,
  - signed URLs,
  - secrets.

If evidence is produced by automation, the generator should:

- write digests,
- write a stable evidence index,
- fail closed when governance gates require redaction.

---

## ➕ Adding a new evidence template (governed checklist)

1. Pick the evidence class (plots, maps, tables, index).
2. Define:
   - deterministic naming and sorting rules,
   - minimum caption fields,
   - governance posture and redaction triggers,
   - expected placement in daily/per-run/release report trees.
3. Add the template under the appropriate subfolder.
4. Update this README directory layout only when the template is adopted.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed evidence template index; defined plot/map/table/index classes, determinism posture, governance-safe evidence rules, and accessibility expectations. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Templates" src="https://img.shields.io/badge/Evidence-Templates-blue" />

[⬅ Templates Index](../README.md) ·
[🧾 Reports Index](../../README.md) ·
[📅 Daily Reports](../../daily/README.md) ·
[🏃 Per-Run Reports](../../per-run/README.md) ·
[🏷 Release Reports](../../releases/README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

