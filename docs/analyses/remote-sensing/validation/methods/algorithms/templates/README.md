---
title: "🧩 KFM — Validation Algorithm Templates (Common Envelopes · Thresholds · Reason Codes)"
path: "docs/analyses/remote-sensing/validation/methods/algorithms/templates/README.md"

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

intent: "remote-sensing-validation-algorithm-templates-common"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:algorithms:templates:index:v11.2.6"
semantic_document_id: "kfm-rs-validation-algorithm-templates-common"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/algorithms/templates/README.md"
immutability_status: "version-pinned"

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

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🧩 **KFM — Validation Algorithm Templates (Common)**
`docs/analyses/remote-sensing/validation/methods/algorithms/templates/README.md`

**Purpose**  
Provide **common, governed templates** shared across remote-sensing validation algorithm families (radiometry, classification, geometry, drift).  
These templates standardize **output envelopes**, **threshold configs**, and **reason code mappings** so rollups remain deterministic and audit-ready.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Templates-Common%20Pack-blue" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory is the **shared template pack** for KFM remote-sensing validation algorithms.

Use these templates to ensure:

- consistent machine-readable outputs across algorithm families,
- deterministic gate evaluation and reason-code classification,
- stable rollups for:
  - per-run bundles,
  - daily rollups,
  - release promotion reports,
- governance-safe reporting posture (FAIR+CARE, sovereignty policies).

This folder is intentionally small. Family-specific templates should live in:

- `radiometry/templates/`
- `classification/templates/`
- `geometry/templates/`
- `drift/templates/`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/algorithms/
└── 📁 templates/                                         — Common templates (this directory)
    ├── 📄 README.md                                      — This index
    ├── 🧾 algorithm_output_envelope.template.json         — Recommended: common output envelope (algorithm → scope → governance → results)
    ├── 🧾 common_thresholds.template.json                 — Recommended: shared threshold policy skeleton (gate mode, severity rules)
    ├── 🧾 reason_codes.template.json                      — Recommended: normalized reason codes + severity mapping
    ├── 🧾 governance_block.template.json                  — Recommended: CARE/sovereignty fields and redaction summary block
    ├── 🧾 refs_block.template.json                        — Recommended: STAC/DCAT/PROV reference arrays
    ├── 🧾 checksums_block.template.json                   — Optional: checksums/digests block (input pack hash, output hash)
    ├── 🧾 example_envelope.minimal.json                   — Optional: “golden” minimal payload (small)
    ├── 🧾 example_envelope.pass.json                      — Optional: “golden” pass payload (small)
    └── 🧾 example_envelope.fail.json                      — Optional: “golden” fail payload (small)
~~~

> Filenames above are recommended conventions. Add only what is used by CI validators and report writers.

---

## 🧾 What belongs here vs in family templates

### Keep here (common across all validation)

- the standard output envelope shape (top-level keys and required blocks),
- common governance block (CARE/sovereignty posture),
- common reference block (STAC/DCAT/PROV pointers),
- common reason codes and severity mapping (when truly shared),
- common threshold policy scaffolding and deterministic gate behavior.

### Keep in family folders (radiometry/classification/geometry/drift)

- metric-specific templates (band metrics, confusion matrices, geometry counts),
- family-specific thresholds (macro F1 vs RMSE vs overlap rates),
- family-specific reason codes (e.g., `MASK_POLICY_INCONSISTENT` vs `TILE_GAP_EXCESS`),
- family-specific example payloads.

---

## 🧱 Standard output envelope (recommended)

All algorithm outputs SHOULD follow a common envelope so rollups can be generic.

Skeleton (illustrative only):

~~~json
{
  "algorithm_id": "kfm:rs:validate:<family>:<name>:v1",
  "run_id": "urn:kfm:run:<...>",
  "dataset_id": "urn:kfm:dataset:<...>",
  "scope": {
    "time_start_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "time_end_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "sampling": "full|tiles|stratified|random",
    "seed": 1337,
    "sample_frame_hash": "<sha256>"
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {
      "events_total": 0,
      "reasons": []
    }
  },
  "results": {
    "metrics": {},
    "thresholds": {},
    "outcome": "pass|warn|fail",
    "reason_codes": []
  },
  "refs": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": []
  },
  "checksums": {
    "input_pack_sha256": "<sha256>",
    "output_sha256": "<sha256>"
  },
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
~~~

Envelope rules:

- keep `metrics` and `thresholds` **small** and **stable**,
- store heavy artifacts (tables, plots, full diffs) elsewhere and link via `refs`,
- keep `reason_codes` deterministic (see below).

---

## 🚦 Common gate behavior (deterministic)

A common thresholds template SHOULD define:

- `gate_mode`: `fail_closed` (default) or `warn_open` (rare; requires governance approval)
- severity of missing values or missing baselines
- deterministic tie-breaking rules when multiple reasons apply

Recommended deterministic behavior:

- `reason_codes` MUST be sorted lexicographically.
- `outcome` MUST be derived deterministically from:
  - gate mode,
  - threshold evaluation results,
  - reason-code severity mapping.

---

## 🧾 Normalized reason codes (common set)

This folder SHOULD only contain reason codes that are broadly shared across families.

Suggested common codes:

- `BASELINE_NOT_FOUND`
- `PROVENANCE_INCOMPLETE`
- `GOVERNANCE_STATUS_UNKNOWN`
- `CARE_REDACTION_APPLIED`
- `SOVEREIGNTY_GATE_RESTRICTED`
- `LOW_SUPPORT`
- `THRESHOLD_BREACH_CRITICAL`
- `THRESHOLD_BREACH_NONCRITICAL`

Family-specific codes belong in family template folders.

---

## 🎯 Determinism requirements for templates

Templates MUST support deterministic computation and reporting:

- stable enumeration:
  - item ids and asset keys sorted before aggregation,
- stable numeric behavior:
  - quantile method pinned (when used),
  - histogram bins pinned (when used),
- stable baseline selection when required:
  - baseline resolution rules explicit and deterministic,
- stable output ordering:
  - `reason_codes` sorted,
  - per-band/per-class lists sorted by stable keys (band name, class_id),
- stable sampling:
  - include `seed` and `sample_frame_hash` when sampling is used.

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates and example payloads MUST be safe to publish in-repo:

- no raw coordinates or “how to locate” guidance,
- no internal endpoints, tokens, or signed URLs,
- avoid tile-level offender lists unless governance explicitly allows.

If a product is governance-restricted:

- emit only generalized `spatial_scope`,
- set `care_gate_status = redact|deny` and record a redaction summary,
- require steward review for deeper diagnostics outside public artifacts.

---

## 🧪 CI/CD usage (recommended)

Templates support CI by enabling:

- schema validation (if/when JSON Schemas exist under governed `schemas/`),
- golden payload regression tests:
  - ensure output envelope does not drift unintentionally,
- deterministic gate checks:
  - same inputs/config → same `reason_codes` ordering and `outcome`.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed common template pack for remote-sensing validation algorithms; standardized output envelope, common threshold scaffolding, common governance/refs blocks, and deterministic reason-code behavior. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Templates-Common%20Pack-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Algorithms Index](../README.md) ·
[🌈 Radiometry Templates](../radiometry/templates/README.md) ·
[🏷️ Classification Templates](../classification/templates/README.md) ·
[📐 Geometry Templates](../geometry/templates/README.md) ·
[📉 Drift Templates](../drift/templates/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

