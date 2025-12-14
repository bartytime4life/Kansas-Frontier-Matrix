---
title: "🧷 KFM — Sampling Templates (Frame Manifest · Selection · Stratification)"
path: "docs/analyses/remote-sensing/validation/methods/sampling/templates/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Templates"
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

intent: "remote-sensing-validation-sampling-templates"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:sampling:templates:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-sampling-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/sampling/templates/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

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
---

<div align="center">

# 🧷 **KFM — Sampling Templates**
`docs/analyses/remote-sensing/validation/methods/sampling/templates/README.md`

**Purpose**  
Standardize the **sampling output manifests**, **selection rules**, and **stratification templates** used across KFM remote-sensing validation.
These templates enable consistent sampling frame construction, reproducible sampling selection, and governance-compliant reporting.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Sampling" src="https://img.shields.io/badge/Validation-Sampling-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory is reserved for **templates** used in sampling-based validation:

- **Sampling frame manifests** to define eligible candidates,
- **Sampling selection templates** for reproducible NRT/randomized stratified sampling,
- **Stratification templates** for domain-driven selection (e.g., based on land cover, cloud fraction, temporal buckets),
- **Governance-compliant reporting** to ensure all sampling maintains auditability and determinism.

These templates help prevent drift and support:

- per-run provenance,
- consistent daily rollups,
- reliable release rollups for governance and auditing.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/sampling/
└── 📁 templates/                                             — Templates for sampling (this directory)
    ├── 📄 README.md                                          — This index (you are here)
    ├── 🧾 sample_frame_manifest.template.json                 — Recommended: manifest for sampled items/tiles
    ├── 🧾 sample_selection.template.json                      — Recommended: template for selected sample records
    ├── 🧾 stratification.template.json                        — Recommended: stratified sampling policies
    ├── 🧾 example_sampling.pass.json                         — Optional: “golden” pass example (small)
    ├── 🧾 example_sampling.fail.json                         — Optional: “golden” fail example (small)
    └── 🧾 example_sampling.warn.json                         — Optional: “golden” warn example (small)
~~~

> Filenames above are recommended conventions. Add only what is used by CI validators and report writers, and keep examples small.

---

## 🧾 Template inventory (recommended)

### 1) Sample frame manifest template

This template defines the **list of eligible candidates** from which samples are drawn. It should include:

- ordered unit ids (STAC Item ids, tile ids, etc.),
- sample eligibility criteria (based on masks, coverage, governance constraints),
- sample frame hash (deterministic enumeration).

Skeleton (illustrative only):

~~~json
{
  "frame_version": "v1",
  "sample_size": 500,
  "sampling_scope": {
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "time_window": {
      "start": "2025-01-01T00:00:00Z",
      "end": "2025-01-02T00:00:00Z"
    }
  },
  "eligibility_criteria": {
    "cloud_mask": "excluded",
    "nodata_mask": "excluded",
    "sovereignty_gate": "allowed"
  },
  "candidate_ids": [
    "urn:kfm:dataset:<dataset_id>:tile:<tile_id>",
    "urn:kfm:dataset:<dataset_id>:tile:<tile_id>"
  ],
  "frame_hash_sha256": "<sha256>"
}
~~~

### 2) Sample selection template

This template defines how **samples are selected** from the frame. Include:

- sample mode (random, stratified, systematic, etc.),
- the seed used (for reproducibility),
- the selected units/tiles/items and their metadata.

Skeleton (illustrative only):

~~~json
{
  "selection_version": "v1",
  "sampling_mode": "random",
  "seed": 1337,
  "sampled_count": 50,
  "selected_ids": [
    "urn:kfm:dataset:<dataset_id>:tile:<tile_id>",
    "urn:kfm:dataset:<dataset_id>:tile:<tile_id>"
  ],
  "sample_frame_hash_sha256": "<sha256>"
}
~~~

### 3) Stratification template

Stratified sampling templates should specify the **strata** used for sampling and how to select from them:

- define stratification categories (e.g., land cover types, temporal groupings),
- specify the minimum number of samples per strata.

Skeleton (illustrative only):

~~~json
{
  "stratification_version": "v1",
  "strata": [
    {
      "key": "land_cover=forest",
      "min_samples": 100,
      "selection_method": "random"
    },
    {
      "key": "land_cover=grassland",
      "min_samples": 50,
      "selection_method": "random"
    }
  ],
  "sample_size": 500,
  "frame_hash_sha256": "<sha256>"
}
~~~

### 4) Reason codes template (optional)

Reason codes map failures or anomalies to human-readable terms, helping operators and auditors understand why a sample was flagged as problematic.

Skeleton (illustrative only):

~~~json
{
  "reason_codes": [
    {"code": "SAMPLE_MISSING", "severity": "fail", "hint": "Sample could not be retrieved due to missing data."},
    {"code": "INSUFFICIENT_SUPPORT", "severity": "warn", "hint": "Insufficient sample support for valid metric computation."},
    {"code": "CLOUD_MASK_FAILURE", "severity": "fail", "hint": "Cloud mask not correctly applied, sample invalid."},
    {"code": "SOVEREIGNTY_GATE_BLOCKED", "severity": "fail", "hint": "Sample blocked due to sovereignty gate."}
  ]
}
~~~

---

## 🎯 Determinism requirements for templates

Templates MUST support deterministic sampling:

- **stable enumeration**:
  - candidates sorted lexicographically (e.g., by ID or tile coordinates),
  - sampling lists and frame order should be identical for identical runs.
- **fixed seed** for random or stratified sampling:
  - store the seed value in the output and use it to derive the sample.
- **stable aggregation**:
  - when grouping, aggregate results deterministically by `stratum` or `spatial_scope`.
- **consistent reason codes**:
  - use the same reason code for the same failure across different runs or reports.

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates and sample selections MUST remain safe for publication in repos:

- **no raw coordinates** in public artifacts unless explicitly allowed,
- **no site-specific identifiers** unless generalized (region-level summaries),
- **no signed URLs**, tokens, or internal endpoints in reports or artifacts.

Governance posture:

- If governance requires redaction (e.g., sovereignty or sensitivity flags), set `care_gate_status = redact|deny` and include redaction summary.
- **Redacted sample details** should only include aggregated information (e.g., counts) unless approved for deep review.

---

## 🧪 CI/CD expectations (recommended)

Templates enable CI validation checks such as:

- **Reproducibility**: sample manifest and selected hash must match the expected value from the same frame and config.
- **Governance leakage check**: Ensure no restricted fields (e.g., coordinates, secret tokens) are included in the output templates.
- **Provenance consistency**: Ensure the sample frame and selected samples are properly linked in provenance and STAC artifacts.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed sampling templates index; defined sample frame manifest, selection, stratification, and reason-code templates for remote-sensing validation. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Sampling" src="https://img.shields.io/badge/Validation-Sampling-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Sampling](../README.md) ·
[🧮 Algorithms](../algorithms/README.md) ·
[📐 Metrics](../metrics/README.md) ·
[🧾 Provenance](../provenance/README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

