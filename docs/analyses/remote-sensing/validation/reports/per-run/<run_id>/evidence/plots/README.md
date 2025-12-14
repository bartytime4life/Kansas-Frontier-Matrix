---
title: "📊 KFM — Per-Run Validation Evidence Plots (Deterministic · Governance-Safe)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/plots/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Policy"
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

intent: "remote-sensing-validation-per-run-evidence-plots"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
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

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:evidence:plots:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-evidence-plots-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/plots/README.md"
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

# 📊 **KFM — Per‑Run Validation Evidence Plots**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/plots/README.md`

**Purpose**  
This folder stores **small, governance-safe plots** for a single validation run (`<run_id>`).
Plots must support review and release promotion while remaining **deterministic** and **non-leaking** under FAIR+CARE and sovereignty policy.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Plots" src="https://img.shields.io/badge/Evidence-Plots-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Plots in this folder are **review exhibits** that explain validation outcomes without requiring access to raw data.

They SHOULD answer:

- What metric(s) failed/passed and how close to thresholds?
- Are errors systematic (bias) vs random (noise)?
- Are errors stable across time and/or releases?
- Is support sufficient (coverage, sample size, strata balance)?

Plots MUST remain:

- **small** (review-friendly),
- **deterministic** (reproducible bytes where feasible),
- **governance-safe** (no sensitive or restricted leakage).

---

## 🗂️ Directory Layout (expected)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/plots/
├── 📄 README.md                             — This policy/index
├── 📊 confusion_matrix.png                  — Example: classification exhibit (aggregate)
├── 📊 per_class_f1.png                       — Example: per-class metric bars (aggregate)
├── 📊 residual_histogram.png                 — Example: radiometry exhibit (aggregate)
├── 📊 residual_qq.png                        — Example: distribution fit exhibit
├── 📊 drift_timeseries.png                   — Example: release-to-release drift summary (aggregate)
├── 📊 threshold_margins.png                  — Example: distance-to-threshold exhibit
└── 📊 coverage_summary.png                   — Example: support/coverage counts (aggregate)
~~~

Notes:

- Filenames are illustrative. Only include plots you actually produce.
- Any plot included here SHOULD be registered in `../evidence_index.json` with a sha256 digest.

---

## ✅ Allowed plot formats

Preferred:

- `PNG` (`.png`) — default for compact, deterministic raster plots
- `SVG` (`.svg`) — acceptable if deterministic and safe (avoid embedded timestamps/metadata)

Avoid:

- animated formats (unless explicitly approved),
- interactive HTML exports (riskier and often non-deterministic),
- formats that embed environment-dependent metadata.

---

## 🏷️ Naming conventions (recommended)

Use `snake_case` and keep names stable across runs.

Recommended patterns:

- `<family>_<exhibit>.png`
  - `classification_confusion_matrix.png`
  - `radiometry_residual_histogram.png`
  - `drift_release_delta_timeseries.png`
- Optional suffixes:
  - `_macro`, `_micro`, `_p90`, `_p99`
  - `_h3r8`, `_region` (only if scope is governance-safe and generalized)

Avoid:

- embedding coordinates,
- embedding restricted ids,
- embedding timestamps beyond the run window label if required.

---

## 🎯 Determinism requirements (non-negotiable)

Plots SHOULD be reproducible:

- stable sorting before aggregation,
- pinned binning rules:
  - histogram bin edges defined and recorded (no silent “auto bins”),
  - fixed axis limits when meaningful,
- pinned rendering:
  - fixed DPI/export size,
  - fixed font settings where feasible,
- strip non-deterministic metadata:
  - avoid embedding export timestamps in image metadata,
  - avoid embedding environment paths.

If deterministic rendering cannot be achieved for a plot:

- treat the plot as optional,
- record a deterministic reason code (e.g., `NONDETERMINISTIC_RENDERING`) in the run summary if it affects gating.

---

## 🛡️ Governance and leakage rules (mandatory)

Do NOT include:

- raw coordinates,
- site-level or restricted identifiers,
- “before/after” panels that reveal sensitive locations,
- tile thumbnails or chips from restricted collections,
- signed URLs, secrets, internal endpoints.

If restricted inputs are present:

- plot only aggregated distributions and counts,
- use generalized spatial scopes (region/coarse grid) when mapping,
- ensure minimum group sizes before plotting subgroup breakdowns (policy-defined).

---

## 🔗 Registration in the evidence index

Every plot SHOULD be referenced from:

- `../evidence_index.json`

Each entry SHOULD include:

- `evidence_id`
- relative plot path (e.g., `plots/residual_histogram.png`)
- `sha256`
- producing `algorithm_ids`
- a short caption

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for per-run evidence plots; defined allowed formats, naming conventions, determinism controls, and governance-safe plotting rules. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Plots" src="https://img.shields.io/badge/Evidence-Plots-blue" />

[⬅ Evidence](../README.md) ·
[🧾 Evidence Index](../evidence_index.json) ·
[🏃 Run Bundle](../../README.md) ·
[🧾 Manifests](../../manifests/README.md) ·
[🧬 Provenance](../../provenance/README.md) ·
[📎 Attachments](../../attachments/README.md) ·
[🧾 Per-Run Reports](../../../README.md) ·
[🧾 Reports Index](../../../../README.md) ·
[🧩 Methods](../../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

