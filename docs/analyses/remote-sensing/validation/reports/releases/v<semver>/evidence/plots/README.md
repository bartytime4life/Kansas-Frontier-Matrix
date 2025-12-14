---
title: "📈 KFM — Release Validation Evidence Plots (v<semver>) · Deterministic · Governance-Safe"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/plots/README.md"

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

intent: "remote-sensing-validation-release-evidence-plots"
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

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:evidence:plots:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-evidence-plots-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/plots/README.md"
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

# 📈 **KFM — Release Validation Evidence Plots**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/plots/README.md`

**Purpose**  
This folder contains **small, release-grade plots** that support promotion decisions for **v<semver>**.
Plots must be **aggregated**, **deterministic where feasible**, and **governance-safe** for in-repo review.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Evidence Plots" src="https://img.shields.io/badge/Evidence-Plots-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Release plots are curated exhibits that help reviewers quickly verify:

- gate outcomes (pass/warn/fail) and distance-to-threshold,
- distribution shape (bias, tail risk, multimodality),
- drift vs baseline release (aggregate trends),
- support and coverage (counts, strata balance).

Plots here MUST remain **review-friendly** and MUST NOT become a proxy for raw data access.

---

## 🗂️ Directory Layout (expected)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/plots/
├── 📄 README.md                                  — This policy/index
├── 📈 threshold_margins.png                      — Example: distance-to-threshold (release gates)
├── 📈 residual_histogram.png                     — Example: aggregate residual distribution (radiometry)
├── 📈 residual_qq.png                            — Example: distribution alignment (aggregate)
├── 📈 per_class_f1.png                           — Example: classification per-class metrics (aggregate)
├── 📈 confusion_matrix.png                       — Example: confusion matrix (aggregate counts only)
├── 📈 drift_timeseries.png                       — Example: drift vs baseline (aggregate trend)
└── 📈 coverage_summary.png                       — Example: support/coverage counts summary (aggregate)
~~~

Notes:

- Filenames are illustrative. Include only plots actually produced for the release.
- Every plot SHOULD be registered in `../release_evidence_index.json` with a sha256 digest.

---

## ✅ Allowed plot formats

Preferred:

- `PNG` (`.png`) — compact, stable, easy to make deterministic

Allowed with care:

- `SVG` (`.svg`) — only if deterministic (avoid embedded timestamps/metadata)

Avoid:

- interactive HTML plots in this folder,
- animated formats (unless explicitly approved),
- formats that embed environment-dependent metadata.

---

## 🏷️ Naming conventions (recommended)

Use `snake_case` with stable, meaning-forward names.

Recommended patterns:

- `<topic>_<exhibit>.png`
  - `threshold_margins.png`
  - `drift_timeseries.png`
  - `residual_histogram.png`
  - `per_class_f1.png`

Avoid embedding:

- coordinates,
- restricted identifiers,
- internal run infrastructure ids beyond the release semantic label.

---

## 🎯 Determinism requirements (non-negotiable)

Release plots SHOULD be reproducible from the same inputs + config snapshot:

- fixed histogram bins and edges (no silent “auto bins”),
- fixed axis limits when meaningful (avoid autoscaling drift),
- fixed sorting and aggregation rules,
- fixed export size / DPI,
- stable rounding for values shown in labels/legends,
- avoid embedding timestamps, machine paths, or random ids into plot metadata.

If a plot cannot be made deterministic:

- treat it as optional and non-gating,
- record a deterministic reason code in the release rollup (recommended).

---

## 🛡️ Governance and leakage rules (mandatory)

Plots can leak sensitive context through:

- rare-category breakdowns,
- small-area breakdowns,
- inclusion of identifiers or coordinates in labels,
- overly-specific “examples” derived from restricted inputs.

Rules:

- Do NOT include precise coordinates, site identifiers, or restricted ids in any label.
- Do NOT include per-sample examples (chips/thumbnails) in this folder.
- If restricted inputs exist:
  - plot only aggregated distributions and counts,
  - enforce minimum group sizes for subgroup plots (policy-defined),
  - suppress low-support strata and note suppression in captions.
- Never include signed URLs, secrets, internal endpoints, or tokens.

---

## ♿ Accessibility requirements (WCAG-aligned)

Every plot MUST have a caption available via:

- `../release_evidence_index.md` (human index), and/or
- `../release_evidence_index.json` (`caption` fields)

Captions SHOULD include:

- what the plot shows,
- aggregation scope (release-wide; baseline comparison if applicable),
- support basis (counts, sampling posture),
- thresholds and interpretation guidance.

Avoid relying on color alone; include legends and numeric ranges.

---

## 🔗 Registration (release evidence index)

Every plot SHOULD be registered in:

- `../release_evidence_index.json`

Each entry SHOULD include:

- `evidence_id`
- relative path (e.g., `plots/threshold_margins.png`)
- `sha256`
- producing `algorithm_ids`
- a short caption (human-readable; governance-safe)

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- if plots exist:
  - each plot is listed in `../release_evidence_index.json`,
  - sha256 digests match,
  - size limits are respected,
  - leakage scans pass (no coordinates, no secrets, no signed URLs),
  - filenames do not include restricted identifiers.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release evidence plots; defined allowed formats, naming conventions, determinism controls, and governance-safe plotting rules used for release promotion. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Plots" src="https://img.shields.io/badge/Evidence-Plots-blue" />

[⬅ Evidence](../README.md) ·
[🧾 Evidence Index](../release_evidence_index.md) ·
[🧾 Evidence Index JSON](../release_evidence_index.json) ·
[🗺️ Maps](../maps/README.md) ·
[📋 Tables](../tables/README.md) ·
[🏷 Release Report](../../README.md) ·
[🏷 Releases Index](../../../README.md) ·
[🧾 Reports Index](../../../../README.md) ·
[🏃 Per-Run Reports](../../../../per-run/README.md) ·
[📅 Daily Reports](../../../../daily/README.md) ·
[🧩 Methods](../../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

