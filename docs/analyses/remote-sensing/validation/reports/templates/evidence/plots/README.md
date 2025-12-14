---
title: "📈 KFM — Remote Sensing Validation Evidence Plot Templates (Histograms · Time Series · Drift)"
path: "docs/analyses/remote-sensing/validation/reports/templates/evidence/plots/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Template Pack"
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

intent: "rs-validation-evidence-plot-templates"
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

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:templates:evidence:plots:v11.2.6"
semantic_document_id: "kfm-rs-validation-evidence-plots-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/templates/evidence/plots/README.md"
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
  - "content-alteration"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 📈 **KFM — Remote Sensing Validation Evidence Plot Templates**
`docs/analyses/remote-sensing/validation/reports/templates/evidence/plots/README.md`

**Purpose**  
Define governed conventions for **evidence plots** embedded in remote-sensing validation reports (per-run, daily, release), emphasizing **determinism**, **comparability**, and **governance-safe aggregation**.

<img alt="MCP-DL v6.3" src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="Evidence Plots" src="https://img.shields.io/badge/Evidence-Plots-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Evidence plots are **review-grade visual artifacts** that summarize validation outcomes and support governance decisions without requiring privileged access to raw data.

They are used to:

- compare error distributions across runs/releases,
- track time-series stability and missingness,
- summarize classification performance by class (aggregate),
- visualize drift deltas in a stable, comparable way.

This directory defines:

- plot categories (what types are acceptable),
- deterministic plotting rules (bins/axes/rounding),
- naming conventions,
- governance posture (avoid leakage, avoid disallowed detail).

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/templates/           — Report template pack (governed)
└── 📁 evidence/                                                      — Evidence template family (indexes + media)
    ├── 📁 plots/                                                     — Evidence plot conventions (this directory)
    │   └── 📄 README.md                                              — This document
    ├── 📁 maps/                                                      — Evidence map conventions (high-risk; redaction rules)
    ├── 📁 tables/                                                    — Evidence table conventions (stable ordering, aggregates)
    └── 📁 indexes/                                                   — Evidence index templates (bind evidence to digests)
~~~

---

## 🧩 Plot categories (recommended)

### 1) Error distribution plots (continuous metrics)

Use for continuous-valued products and residual analysis:

- histogram of absolute error (MAE distribution),
- histogram of residuals (bias structure),
- quantile summaries (p50/p90 absolute error vs threshold),
- ECDF plots for stable comparison.

Determinism rules:

- pin bin edges (explicit, not data-dependent),
- pin axis ranges when comparing runs/releases,
- pin rounding policy for summary statistics.

### 2) Time-series summary plots

Use for time-series products or repeated acquisitions:

- p50/p90 metric over time by region/tile cohort,
- missingness fraction over time,
- freshness/lag distribution over time (if available).

Determinism rules:

- fixed aggregation window (daily/weekly) declared in caption,
- stable time zone (UTC),
- explicit handling of missing values.

### 3) Classification performance plots

Use for categorical products:

- per-class precision/recall bars (aggregate),
- confusion-matrix heatmap (aggregate, with stable class ordering).

Determinism rules:

- stable class ordering (explicit list),
- stable normalization (none|row|column) declared.

### 4) Drift and release delta plots

Use to compare release `v<semver>` against previous version:

- delta histogram (new - old),
- percent change plots for key metrics,
- threshold gate summary (pass/warn/fail counts).

Determinism rules:

- stable baseline selection documented,
- stable binning and stable axis ranges.

---

## 🧷 Naming conventions (recommended)

Use deterministic, readable filenames:

- `plot_<kind>_<algorithm_id>_<dataset_id>_<scope>_<YYYYMMDD>.png`
- `plot_drift_<metric>_<baseline>_to_<target>_<scope>.png`

Rules:

- avoid spaces,
- keep names predictable and stable across reruns,
- do not include sensitive identifiers in filenames.

---

## 🧾 Required plot metadata (captions)

Every plot included in a governed bundle MUST have a short caption recorded in:

- the evidence index (JSON + Markdown), and/or
- the plot README for the bundle directory.

Captions MUST include:

- what is plotted and its units,
- aggregation scope (time window, region/cohort definition),
- determinism settings:
  - bins/axes pinned,
  - rounding policy,
  - sampling mode/seed (if sampling is used),
- governance posture:
  - CARE/sovereignty gate result (at least at bundle level).

---

## 🎯 Determinism requirements (non-negotiable)

Plots MUST be reproducible:

- stable input enumeration (sorted tiles/items),
- fixed seeds if any sampling is used,
- pinned bins and/or pinned axes for comparisons,
- explicit rounding rules for reported stats.

Avoid:

- auto-binning when comparing releases,
- auto-scaling that changes visual interpretation run-to-run,
- embedding environment-specific paths or timestamps in the figure.

---

## 🛡️ Governance posture (mandatory)

Plots MUST remain governance-safe:

- avoid per-sample point scatter if it enables location inference,
- do not include coordinate axes labeled with precise lat/lon unless allowed,
- do not include signed URLs, secrets, or internal endpoints in figure text.

If governance requires redaction:

- publish aggregated plots only,
- omit any plot that would leak sensitive detail,
- document redaction in the evidence index (reason codes).

---

## ♿ Accessibility requirements (WCAG-aligned)

For each plot:

- include alt text (via Markdown description),
- use concise titles,
- ensure captions describe key patterns (not just “see plot”),
- avoid encoding meaning solely by color (when possible).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed conventions for evidence plots (determinism, naming, caption requirements, and governance-safe aggregation posture). |

---

<div align="center">

📈 **KFM — Remote Sensing Validation Evidence Plot Templates**  
Deterministic Evidence · Governance-Safe Summaries · Review-Grade Reporting

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="MCP-DL v6.3" src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[📡 Validation](../../../../README.md) ·  
[🧾 Reports](../../../README.md) ·  
[🧩 Templates](../../README.md) ·  
[🧾 Evidence Templates](../README.md) ·  
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

