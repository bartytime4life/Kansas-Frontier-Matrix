---
title: "🧾 KFM — Per-Run Validation Evidence (Governance-Safe Artifacts · Plots · Tables)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/README.md"

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

intent: "remote-sensing-validation-per-run-evidence"
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

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:evidence:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-evidence-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/README.md"
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

# 🧾 **KFM — Per‑Run Validation Evidence**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/README.md`

**Purpose**  
This folder holds **governance-safe evidence artifacts** for a single validation run (`<run_id>`):
plots, small tables, and compact “exhibits” that support review and release promotion—without embedding sensitive data or large payloads.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Per-Run" src="https://img.shields.io/badge/Reports-Per--Run-blue" />
<img alt="Evidence Artifacts" src="https://img.shields.io/badge/Evidence-Artifacts-informational" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Evidence artifacts are optional but recommended “review exhibits” for a single validation run.

Use this folder to store **compact, governance-safe** artifacts that help humans answer:

- *What failed (or passed) and where?*
- *How strong is the support (counts, coverage, sampling)?*
- *Do the error patterns look like known issues (drift, bias, misregistration)?*
- *Are results consistent with prior runs/releases?*

This folder is **not** for raw data outputs. Evidence should be derived, aggregated, and safe.

---

## 🆔 What is `<run_id>`?

`<run_id>` MUST identify one validation execution.

Recommended forms:

- `urn:kfm:run:<...>` (preferred)
- `urn:uuid:<...>` (acceptable if policy permits)

`<run_id>` SHOULD be reproducible from run context (e.g., `frame_hash + config_hash`) and MUST NOT rely on wall-clock time alone.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/
├── 📄 README.md                                              — This policy/index
├── 🧾 evidence_index.json                                    — Recommended: registry of evidence files (ids + digests)
├── 📄 evidence_index.md                                      — Optional: human-oriented index w/ links and captions
├── 📊 plots/                                                 — Optional: PNG/SVG plots (small, deterministic)
│   ├── confusion_matrix.png
│   ├── residual_histogram.png
│   └── drift_timeseries.png
├── 📋 tables/                                                — Optional: CSV/Parquet summaries (small, aggregated)
│   ├── metrics_rollup.csv
│   └── thresholds_eval.csv
└── 🗺️ maps/                                                  — Optional: generalized maps (NO sensitive precision)
    ├── region_error_heatmap.png
    └── h3_r<...>_summary.png
~~~

> Use subfolders only if needed. Keep the evidence set small and reviewable.

---

## ✅ What belongs here

Evidence artifacts SHOULD be:

- **Aggregated** (counts, distributions, summaries; not raw pixels/samples)
- **Governance-safe** (no restricted identifiers; no sensitive coordinates)
- **Deterministic** (same inputs + same config → same bytes, when feasible)
- **Small** (prefer “report exhibits” over “data dumps”)

Recommended evidence types:

- **Plots**
  - confusion matrix heatmap (classification)
  - residual histograms / QQ plots (radiometry)
  - drift trend lines vs baseline release
  - per-class metric bar charts (aggregated)
- **Tables**
  - metrics rollup (mean/median/p90/p99)
  - threshold evaluations (metric, threshold, outcome)
  - support counts (tiles/items/time steps; stratified counts only)
- **Generalized maps**
  - region-level summaries (county/region bins) or H3 generalized heatmaps
  - no “pinpoint” displays; no coordinate callouts

---

## ⛔ What must NOT be committed here

Do NOT store:

- raw rasters, tiles, image chips, or “before/after” panels that can reveal sensitive locations,
- per-sample lists of tiles/items when restricted inputs exist,
- precise coordinates, site identifiers, or any “how to locate” content,
- signed URLs, access tokens, credentials, internal endpoints, secrets,
- bulky logs or payload dumps.

If an artifact is needed but large or sensitive:

- store it as a governed asset elsewhere and reference it via STAC/PROV,
- keep only a digest + stable id pointer in `evidence_index.json`.

---

## 🧾 Recommended index file: `evidence_index.json`

The evidence index SHOULD list every evidence artifact in this folder with:

- stable `evidence_id`
- file path
- sha256 digest
- producing algorithm id(s)
- governance posture summary (allow/redact/deny)
- a short caption (human)

Illustrative shape:

~~~json
{
  "index_kind": "evidence_index",
  "index_version": "v1",
  "run_id": "urn:kfm:run:<run_id>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "artifacts": [
    {
      "evidence_id": "kfm:rs:evidence:confusion-matrix:v1",
      "path": "plots/confusion_matrix.png",
      "sha256": "<sha256>",
      "algorithm_ids": ["kfm:rs:validate:classification:confusion-matrix:v1"],
      "caption": "Confusion matrix (macro summary)."
    }
  ]
}
~~~

---

## 🎯 Determinism requirements (non-negotiable)

Evidence artifacts MUST be reproducible whenever feasible:

- stable sorting before aggregation and plotting,
- pinned bins/thresholds (no “auto bins” without recording parameters),
- pinned rendering settings for plots where possible (fonts, DPI, axis limits),
- strip non-deterministic metadata (timestamps in image metadata) when feasible,
- record digests for every evidence file in `evidence_index.json`.

If deterministic rendering is not achievable for a given artifact:

- record a deterministic reason code (e.g., `NONDETERMINISTIC_RENDERING`) in the run summary,
- keep the artifact optional and do not use it as a merge/promotion gate unless approved.

---

## 🛡️ FAIR+CARE and sovereignty posture

Evidence MUST obey governance labels on inputs:

- when redaction is required:
  - prefer aggregated metrics/tables,
  - use generalized spatial scopes only (region/coarse grid),
  - avoid any artifact that could re-identify restricted locations.
- if governance status is unclear:
  - fail closed in the run outcome (per policy),
  - evidence in this folder MUST remain high-level and non-sensitive.

---

## 🔗 Linkage (STAC/DCAT/PROV)

Preferred linkage pattern:

- The run’s `run.summary.json` references:
  - `evidence_index.json` digest (and optionally `evidence_index.md`)
- The run’s STAC Item (when used) includes assets for:
  - evidence index
  - key evidence artifacts (only those governance-approved)
- PROV bundle references evidence artifacts as derived entities:
  - `prov:Entity` for each evidence file
  - `prov:wasGeneratedBy` the validation activity

This folder SHOULD contain bytes only for **safe artifacts**. Otherwise, store bytes as governed assets and reference them here by id + digest.

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- evidence artifacts are optional, but if present:
  - `evidence_index.json` exists and lists all evidence files,
  - each listed file exists and its sha256 matches,
  - size limits (policy-defined) are respected,
  - leakage scans pass (no coordinates, no secrets, no signed URLs),
  - filenames are sane and stable (no spaces recommended for tooling).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed per-run evidence policy; defined allowed evidence types, prohibited content, determinism posture, and STAC/PROV linkage patterns. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Artifacts" src="https://img.shields.io/badge/Evidence-Artifacts-informational" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Run Bundle](../README.md) ·
[🧾 Manifests](../manifests/README.md) ·
[🧬 Provenance](../provenance/README.md) ·
[📎 Attachments](../attachments/README.md) ·
[🧾 Per-Run Reports](../../README.md) ·
[📅 Daily Reports](../../../daily/README.md) ·
[🏷 Release Reports](../../../releases/README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

