---
title: "🏷️ KFM — Classification Validation Algorithms (Confusion · F1/IoU · Drift · Governance)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/classification/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Reference"
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

intent: "remote-sensing-validation-algorithms-classification"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:classification:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-algorithms-classification"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/classification/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🏷️ **KFM — Classification Validation Algorithms**
`docs/analyses/remote-sensing/validation/methods/algorithms/classification/README.md`

**Purpose**  
Define the governed metric set and deterministic computation rules for validating **categorical** remote-sensing outputs
(masks, land cover, water, burn, clouds) in KFM, including FAIR+CARE safe reporting requirements.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/Validation-Classification-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Classification validation algorithms apply to:

- binary masks (cloud, water, snow),
- multi-class maps (land cover classes),
- change maps (burn/no-burn),
- thresholded indices (e.g., NDWI water mask).

These algorithms produce:

- confusion-matrix-derived metrics,
- per-class and aggregate summaries,
- drift flags vs prior run or release,
- governance-safe output for per-run, daily, and release reports.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/     — Algorithm docs
└── 📁 classification/                                            — Classification validation (this directory)
    ├── 📄 README.md                                              — This doc
    └── 📁 templates/                                             — Optional: metric output templates/schemas
~~~

---

## 🧾 Inputs (conceptual)

Classification validation requires two aligned rasters (or raster + labeled reference):

- `y_pred`: predicted class per pixel
- `y_true`: reference class per pixel (labels, QA mask, or trusted baseline)

Required metadata:

- class map:
  - `class_id` → `class_name`
- nodata policy:
  - how to treat nodata in pred/true
- spatial and temporal scope (generalized if needed)
- sampling policy (full coverage or deterministic sample)
- governance posture:
  - CARE gate status and sovereignty gate status

---

## ✅ Core metrics (required)

### 1) Confusion matrix (required)

For classes `C = {c1..ck}`, build `M[k×k]` where:

- `M[i,j] = count(y_true = ci AND y_pred = cj)`

Determinism:

- class ordering must be stable and explicit (sorted by `class_id`).
- nodata class MUST be excluded from scoring unless explicitly configured.

### 2) Per-class precision, recall, F1 (required)

For class `c`:

- `TP = M[c,c]`
- `FP = sum_j M[j,c] - TP`
- `FN = sum_j M[c,j] - TP`

Metrics:

- `precision_c = TP / (TP + FP)` (define 0/0 behavior → 0 unless configured)
- `recall_c = TP / (TP + FN)` (define 0/0 behavior → 0 unless configured)
- `f1_c = 2 * precision_c * recall_c / (precision_c + recall_c)` (define 0/0 behavior → 0)

### 3) IoU / Jaccard (required for masks and recommended for multi-class)

For class `c`:

- `iou_c = TP / (TP + FP + FN)` (define 0/0 behavior → 0)

For binary masks, report:

- `iou_positive` and `iou_negative` (optional), but always include positive class IoU.

### 4) Overall accuracy (required)

- `accuracy = sum_c M[c,c] / sum_{i,j} M[i,j]`

### 5) Macro and weighted averages (required)

- `macro_f1 = mean_c f1_c`
- `weighted_f1 = sum_c (support_c / total) * f1_c`
- similarly for precision/recall if used in gating

Where:

- `support_c = sum_j M[c,j]`

---

## 📏 Thresholds and gate outcomes (recommended)

For each dataset/product, define policy thresholds (examples only):

- `macro_f1_min`
- `iou_positive_min`
- `accuracy_min`
- `class_specific_min` (e.g., water IoU ≥ X)

Gate outcome:

- `pass`: all required thresholds satisfied
- `warn`: non-critical thresholds breached or low sample support
- `fail`: critical threshold breached

All threshold evaluation MUST be deterministic and recorded.

---

## 🧪 Sampling and determinism

### Full coverage (preferred)

When feasible, compute metrics over all eligible pixels (bounded AOI, bounded time).

### Deterministic sampling (when needed)

If sampling is required:

- use a fixed seed (`seed`) and record it,
- define sample frame deterministically (tile list sorted; pixel indexing deterministic),
- optionally stratify by:
  - class prevalence,
  - ecoregion/zone,
  - acquisition conditions (season bucket),
- record sample sizes per stratum.

Sampling artifacts (if any) should be stored as governed assets and linked.

---

## 🧩 Special cases (policy-driven)

### Binary masks

- Treat “positive” as the feature of interest.
- Report:
  - IoU (positive),
  - precision/recall/F1 (positive),
  - false positive rate and false negative rate (optional).

### Rare classes

Rare classes can cause unstable metrics.

Rules:

- always report `support_c`,
- if `support_c < min_support`:
  - set `reason_code` such as `LOW_SUPPORT_CLASS`,
  - treat thresholding as `warn` unless policy says otherwise.

### Class remapping

If `y_true` and `y_pred` use different class schemes:

- remapping MUST be explicit and versioned,
- store mapping table as a governed artifact,
- record mapping hash in outputs.

---

## 🛡️ FAIR+CARE and sovereignty posture

Classification outputs can leak sensitive information via:

- tiny AOIs,
- example tiles/images,
- per-site performance stats.

Rules:

- in repo-facing reports, do not include raw coordinates or exemplar tiles unless explicitly allowed.
- prefer aggregated reporting:
  - region-level or coarse H3 summaries,
  - class-level metrics only when not sensitive.
- if `care_gate_status != allow`, redact:
  - high-resolution spatial breakdowns,
  - any “best/worst location” lists.

If governance is unclear:

- fail closed (`care_gate_status = deny`), require review.

---

## 📦 Standard output shape (recommended)

Use the algorithm output envelope defined in the parent algorithms index, with classification-specific `results.metrics`.

Example (truncated):

~~~json
{
  "algorithm_id": "kfm:rs:validate:classification:confusion:v1",
  "run_id": "urn:kfm:run:...",
  "dataset_id": "urn:kfm:dataset:...",
  "results": {
    "metrics": {
      "accuracy": 0.93,
      "macro_f1": 0.88,
      "weighted_f1": 0.92,
      "per_class": [
        {"class_id": 0, "name": "background", "support": 123, "precision": 0.9, "recall": 0.8, "f1": 0.85, "iou": 0.74},
        {"class_id": 1, "name": "water",      "support": 456, "precision": 0.95, "recall": 0.96, "f1": 0.955, "iou": 0.91}
      ]
    },
    "thresholds": {
      "macro_f1_min": 0.85,
      "iou_positive_min": 0.9
    },
    "outcome": "pass",
    "reason_codes": []
  }
}
~~~

---

## 🧪 Validation & CI/CD alignment

Classification validation feeds:

- per-run bundles: `docs/analyses/remote-sensing/validation/reports/per-run/`
- daily rollups: `docs/analyses/remote-sensing/validation/reports/daily/`
- release rollups: `docs/analyses/remote-sensing/validation/reports/releases/`

Recommended CI checks:

- metrics JSON schema validation (if/when schema is defined)
- threshold gate enforcement
- leakage checks for restricted fields

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed classification validation algorithms reference; defined confusion-matrix metrics, determinism rules, sampling posture, thresholds, and FAIR+CARE reporting constraints. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Validation-Classification-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Algorithms](../README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

