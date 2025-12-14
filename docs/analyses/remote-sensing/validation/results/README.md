---
title: "📦 KFM — Remote Sensing Validation Results (Machine Outputs · Deterministic Bundles · Governance-Safe)"
path: "docs/analyses/remote-sensing/validation/results/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Contract"
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

intent: "remote-sensing-validation-results-index"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Release Managers"
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

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:results:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-results"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/results/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 📦 **KFM — Remote Sensing Validation Results**
`docs/analyses/remote-sensing/validation/results/README.md`

**Purpose**  
Define the **machine-output** contract and folder structure for remote-sensing validation results:
deterministic result bundles, governance-safe summaries, and references to STAC/DCAT/PROV.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="Results Machine Outputs" src="https://img.shields.io/badge/Validation-Results-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory is for **results artifacts**: compact, deterministic, machine-readable outputs that summarize validation runs.

Results are used to:

- power CI gates (pass/warn/fail),
- support rollups (daily, release),
- provide audit-friendly summaries linked to STAC/DCAT/PROV,
- enable reproducible re-checks without shipping raw data into docs.

Results here SHOULD remain **small** and **stable**. Detailed artifacts (large rasters, large tables, private evidence) MUST live in governed data locations and be referenced (not embedded).

---

## 🧭 What belongs where

### ✅ Belongs in `results/`

- per-run summary JSON (metrics + thresholds + outcomes),
- rollup summary JSON (daily/release),
- references to:
  - STAC item ids / repo paths,
  - DCAT dataset/distribution ids / repo paths,
  - PROV bundle ids / repo paths,
- checksums/manifests for the result bundle itself,
- redaction summary counters and reason codes (no sensitive detail).

### ❌ Does not belong in `results/`

- raw pixels, raw scenes, or per-pixel dumps,
- precise coordinate listings when governance constraints apply,
- signed URLs, secrets, tokens, internal endpoints,
- large unaggregated tables (publish summaries only).

### Related folders

- 📄 Human-readable reports live in:
  - `docs/analyses/remote-sensing/validation/reports/`
- 🧩 Method definitions live in:
  - `docs/analyses/remote-sensing/validation/methods/`
- 📦 Governed data outputs live under:
  - `data/` (and are referenced via STAC/DCAT/PROV)

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/                    — Validation root
└── 📦 results/                                                — Machine-readable results (this directory)
    ├── 📄 README.md                                           — This index + contract
    ├── 🧾 schemas/                                            — Optional: JSON schemas for results payloads (recommended)
    ├── 🧾 per-run/                                            — One bundle per validation run (recommended)
    │   └── 🧾 <run_id>/                                       — Run-scoped results
    │       ├── 🧾 results.json                                — Required: primary summary (small)
    │       ├── 🧾 gates.json                                  — Optional: gate outcomes and threshold evals
    │       ├── 🧾 refs.json                                   — Optional: STAC/DCAT/PROV references
    │       └── 🧾 manifest.json                               — Optional: checksum manifest for this bundle
    ├── 📅 daily/                                              — Daily rollups (recommended)
    │   └── 📅 YYYY/MM/DD/                                     — Date partition
    │       ├── 🧾 results.rollup.json                          — Required: daily summary (small)
    │       └── 🧾 manifest.json                               — Optional
    └── 🏷️ releases/                                           — Release rollups (recommended)
        └── 🏷️ v<semver>/                                      — Release partition
            ├── 🧾 results.rollup.json                          — Required: release summary (small)
            ├── 🧾 drift.delta.json                             — Optional: diff vs previous release (small)
            └── 🧾 manifest.json                                — Optional
~~~

Notes:

- Keep filenames deterministic and consistent across pipelines.
- If your run orchestrator produces different names, add a mapping note here and keep the output stable.

---

## 🧾 Results contract (governed)

### Required: `results.json` (per-run)

Per-run results MUST:

- identify the run (`run_id`) and time window,
- declare the algorithm set evaluated (by `algorithm_id`),
- record outcome (`pass|warn|fail`) and reason codes,
- include governance posture (CARE + sovereignty gate results),
- link to provenance and catalogs (STAC/DCAT/PROV references),
- include checksums for the result payload (and optionally the input pack digest).

Recommended maximum size: **≤ 1–2 MB**.

### Recommended: minimal payload shape

~~~json
{
  "result_kind": "kfm:rs:validation:results:per-run:v1",
  "run_id": "urn:kfm:run:<run_id>",
  "created_utc": "2025-12-14T00:00:00Z",
  "scope": {
    "time_start_utc": "2025-12-13T00:00:00Z",
    "time_end_utc": "2025-12-14T00:00:00Z",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "sampling": "full|tiles|stratified|random",
    "sampling_seed": 1337
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {
      "events_total": 0,
      "reason_codes": []
    }
  },
  "summary": {
    "datasets_checked": 0,
    "algorithms_checked": 0,
    "checks_total": 0,
    "checks_failed": 0,
    "outcome": "pass|warn|fail",
    "reason_codes": []
  },
  "metrics": [
    {
      "dataset_id": "urn:kfm:dataset:<...>",
      "algorithm_id": "kfm:rs:validate:<family>:<name>:v1",
      "metric_name": "rmse",
      "metric_value": 0.0,
      "metric_unit": "<unit>",
      "threshold": {
        "comparison": "<=|>=|<|>",
        "value": 0.0,
        "outcome": "pass|warn|fail"
      }
    }
  ],
  "refs": {
    "stac_items": [],
    "dcat_datasets": [],
    "prov_bundles": [],
    "config_snapshots": []
  },
  "checksums": {
    "results_sha256": "<sha256>",
    "input_pack_sha256": "<sha256>"
  }
}
~~~

### Rollups: `results.rollup.json` (daily/release)

Rollups MUST:

- enumerate what was included (run ids, datasets, algorithm families),
- report aggregate outcomes (counts + reason codes),
- link to the underlying per-run results,
- remain governance-safe (aggregate only).

---

## 🎯 Determinism requirements (non-negotiable)

Results MUST be reproducible:

- stable input enumeration (sorted datasets/tiles/items),
- fixed random seeds when sampling is used (recorded in output),
- stable sorting of arrays and tables before serialization,
- pinned thresholds and configs (reference a config snapshot),
- deterministic reason-code selection (no ambiguous ties).

### Sorting rules (recommended)

Sort lists by:

1. `dataset_id`
2. `algorithm_id`
3. `metric_name`
4. `scope_id` (if present)

And use deterministic tiebreakers if needed.

---

## 🛡️ FAIR+CARE and sovereignty posture

Results MUST obey governance constraints:

- publish **only** aggregated scopes when redaction is required,
- never include precise coordinates or “how to locate” details,
- never include signed URLs or secrets,
- if governance status is unclear:
  - fail closed (warn/fail per policy),
  - mark `sovereignty_gate="unknown"` or `care_gate_status="deny"` and require review.

---

## 🧪 CI/CD alignment

Recommended CI checks for `results/`:

- schema validation (if result schemas exist under `results/schemas/`),
- leakage checks (no coordinates, no tokens, no signed URLs),
- determinism lint:
  - stable ordering,
  - required fields present,
  - checksums recorded,
- rollup consistency:
  - daily/release rollups reference valid per-run results.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed index and contract for remote-sensing validation results; defined bundle layout, required fields, determinism rules, and governance-safe publication posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Validation Results" src="https://img.shields.io/badge/Validation-Results-blue" />

[📡 Validation](../README.md) ·
[🧾 Reports](../reports/README.md) ·
[🧩 Methods](../methods/README.md) ·
[🏷️ Release Reports](../reports/releases/README.md) ·
[📅 Daily Reports](../reports/daily/README.md) ·
[🏛️ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
