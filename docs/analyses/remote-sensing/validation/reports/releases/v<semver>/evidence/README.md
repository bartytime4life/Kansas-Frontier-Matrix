---
title: "📦 KFM — Release Validation Evidence (v<semver>) · Exhibits · Plots · Tables · Maps"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/README.md"

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

intent: "remote-sensing-validation-release-evidence"
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

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<release-commit-sha>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:evidence:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-evidence-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/README.md"
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

# 📦 **KFM — Release Validation Evidence**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/README.md`

**Purpose**  
This folder contains **release-grade, governance-safe evidence exhibits** supporting the validation report for **v<semver>**.
Evidence here is **aggregated**, **deterministic where feasible**, and **safe for in-repo publication**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Evidence Exhibits" src="https://img.shields.io/badge/Evidence-Exhibits-informational" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Release evidence is the **curated exhibit set** that supports promotion decisions for **v<semver>**.

Evidence in this folder SHOULD help reviewers quickly answer:

- Do key metrics pass thresholds (and by what margin)?
- Is support sufficient (coverage, counts, sampling posture)?
- Are failures explainable (known drift, known bias, known geometry issue)?
- How does the release compare to the prior baseline (aggregate drift/diff)?
- Is the evidence consistent with the release report’s gate outcomes?

This folder is intentionally **not** a data dump. Keep exhibits small and reviewable.

---

## 🧭 Relationship to per-run evidence

Release evidence is typically derived from (or summarizes):

- per-run evidence:
  - `docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/`
- per-run summaries and manifests:
  - `docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/`

Release evidence MUST NOT expand scope beyond what the release report and governed manifests authorize.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/
├── 📄 README.md                                — This policy/index
├── 🧾 release_evidence_index.json              — Recommended: registry of evidence files (ids + digests)
├── 📄 release_evidence_index.md                — Optional: human index with links + captions
├── 📁 plots/                                   — Optional: deterministic plots (small)
│   └── 📄 README.md
├── 📁 tables/                                  — Optional: aggregated tables (small)
│   └── 📄 README.md
└── 📁 maps/                                    — Optional: generalized maps (NO sensitive precision)
    └── 📄 README.md
~~~

Notes:

- Only add subfolders you actually use.
- Every evidence artifact SHOULD be registered in `release_evidence_index.json` with a sha256 digest.
- If an exhibit is large or sensitive, store it as a governed asset and reference it via STAC/PROV (id + digest), not by copying bytes here.

---

## ✅ What belongs here

Evidence artifacts SHOULD be:

- **Aggregated**:
  - release-wide metrics rollups (overall + p50/p90/p99),
  - threshold evaluations (metric, threshold, outcome),
  - support counts (items/tiles/time steps; stratified counts only),
  - drift/delta summaries vs baseline release.
- **Governance-safe**:
  - no restricted identifiers,
  - no sensitive coordinates,
  - no “how to locate” information.
- **Deterministic where feasible**:
  - stable binning, stable sorting, stable rounding.

Recommended exhibits by type:

### 📊 Plots (examples)
- threshold margin plot(s) for critical gates
- residual histograms / QQ plots (radiometry)
- per-class metric bars (classification)
- drift trend lines vs baseline (aggregate)

### 📋 Tables (examples)
- `metrics_rollup.csv`
- `thresholds_eval.csv`
- `drift_delta_summary.csv`
- `support_counts.csv` (including sampling posture if sampled)

### 🗺️ Maps (examples)
- region-level or H3-generalized heatmaps of aggregate error/coverage
- strictly generalized; no pinpointing

---

## ⛔ What must NOT be committed here

Do NOT include:

- raw rasters, tiles, or image chips (including before/after panels),
- per-sample tile/item lists when restricted inputs exist,
- precise coordinates or site identifiers,
- signed URLs, access tokens, secrets, internal endpoints,
- bulky logs, payload dumps, or environment-dependent exports.

If the release depends on restricted evidence:

- store it as a governed asset under policy control,
- reference only by stable id + digest in `release_evidence_index.json`,
- ensure the release report gates explain any redaction.

---

## 🧾 Recommended index: `release_evidence_index.json`

This file SHOULD enumerate every evidence artifact in this folder.

Illustrative shape:

~~~json
{
  "index_kind": "release_evidence_index",
  "index_version": "v1",
  "release_version": "v<semver>",
  "release_commit_sha": "<sha>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "artifacts": [
    {
      "evidence_id": "kfm:rs:evidence:threshold-margins:v1",
      "path": "plots/threshold_margins.png",
      "sha256": "<sha256>",
      "algorithm_ids": ["kfm:rs:validate:drift:release-delta:v1"],
      "caption": "Distance-to-threshold for release gates (aggregate)."
    }
  ],
  "refs": {
    "release_summary_json": "../release.summary.json",
    "baseline_release": "v<semver-1>|null",
    "per_run_refs": []
  }
}
~~~

---

## 🎯 Determinism requirements (non-negotiable)

Evidence SHOULD be reproducible:

- stable sorting for tables (explicit key ordering),
- stable rounding rules (documented; consistent across exhibits),
- pinned histogram bins and plot axes,
- pinned map extents and aggregation keys (region/H3 resolution),
- avoid embedding timestamps/paths into file metadata.

If deterministic rendering cannot be achieved for a specific exhibit:

- treat it as optional (non-gating),
- record a deterministic reason code in the release rollup (recommended).

---

## 🛡️ FAIR+CARE and sovereignty posture

Release evidence is public-facing unless explicitly restricted.

Rules:

- if any input is sovereignty-restricted or governance is unclear:
  - fail closed for promotion gates unless an approved override exists,
  - publish only aggregated, generalized evidence,
  - suppress low-support or rare-category breakdowns where re-identification risk exists.
- never include precise spatial details that could be used to locate sensitive sites.

---

## ♿ Accessibility requirements (WCAG-aligned)

Every exhibit SHOULD have an accessible caption available via:

- `release_evidence_index.md`, or
- the `caption` field in `release_evidence_index.json`.

Captions SHOULD include:

- what the exhibit shows,
- the aggregation scope (release-wide, region-level, H3 resolution),
- the support basis (counts / sampling posture),
- how to interpret pass/warn/fail signals.

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- if evidence is present:
  - `release_evidence_index.json` exists,
  - all listed files exist and sha256 digests match,
  - size limits are respected,
  - leakage scans pass (no coordinates, no secrets, no signed URLs),
  - exhibits remain aggregated (no “raw” formats).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release evidence exhibits; defined allowed evidence types, prohibited content, determinism posture, indexing requirements, and governance-safe publication rules. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Exhibits" src="https://img.shields.io/badge/Evidence-Exhibits-informational" />

[⬅ Release Report](../README.md) ·
[🏷 Releases Index](../../README.md) ·
[🧾 Reports Index](../../../README.md) ·
[🏃 Per-Run Reports](../../../per-run/README.md) ·
[📅 Daily Reports](../../../daily/README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

