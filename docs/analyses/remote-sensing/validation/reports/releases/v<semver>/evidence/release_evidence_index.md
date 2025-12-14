---
title: "📦 KFM — Release Evidence Index (v<semver>)"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/release_evidence_index.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index"
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

intent: "remote-sensing-validation-release-evidence-index"
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

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:evidence:index-md:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-evidence-index-md-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/release_evidence_index.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
---

# 📦 Release Evidence Index (v<semver>)

This file is the **human-readable index** of evidence exhibits stored in this folder for the release report **v<semver>**.

Authoritative machine index:

- `release_evidence_index.json` (same folder)

Rules:

- Every exhibit listed here SHOULD also be listed in `release_evidence_index.json`.
- Evidence MUST remain **aggregated** and **governance-safe** (no coordinates, no restricted identifiers, no signed URLs).

---

## ✅ How to use this index

Use this file during review to quickly find:

- threshold and gate exhibits,
- drift/delta summaries vs baseline,
- coverage/support exhibits,
- any release-level plots/tables/maps used to justify promotion.

If an exhibit is sensitive or large, it MUST NOT be copied into this folder; instead reference it by stable id + digest in `release_evidence_index.json`.

---

## 🧾 Release evidence inventory

> Replace placeholders and add/remove rows as exhibits are produced.

| Evidence ID | Type | File | Caption | Produced by (algorithm_id) | sha256 |
|---|---|---|---|---|---|
| `kfm:rs:evidence:threshold-margins:v1` | plot | `plots/threshold_margins.png` | Distance-to-threshold for release gates (aggregate). | `kfm:rs:validate:release:gates:v1` | `<sha256>` |
| `kfm:rs:evidence:metrics-rollup:v1` | table | `tables/metrics_rollup.csv` | Release-wide metric rollup (overall + p50/p90/p99). | `kfm:rs:validate:metrics:rollup:v1` | `<sha256>` |
| `kfm:rs:evidence:thresholds-eval:v1` | table | `tables/thresholds_eval.csv` | Gate evaluation table (metric, threshold, outcome). | `kfm:rs:validate:gates:thresholds:v1` | `<sha256>` |
| `kfm:rs:evidence:drift-delta-summary:v1` | table | `tables/drift_delta_summary.csv` | Aggregate drift vs baseline release (counts + deltas). | `kfm:rs:validate:drift:release-delta:v1` | `<sha256>` |
| `kfm:rs:evidence:region-error-heatmap:v1` | map | `maps/region_error_heatmap.png` | Generalized region-level error summary map (no pinpoint). | `kfm:rs:validate:geometry:regional:v1` | `<sha256>` |

---

## 🎯 Required invariants (governed)

- **Deterministic:** Sorting, binning, rounding, and aggregation must be pinned by the release config snapshot.
- **No leakage:** Evidence MUST NOT include:
  - coordinates,
  - site identifiers,
  - per-sample tile/item lists when restricted inputs exist,
  - signed URLs or secrets.
- **Digest integrity:** The `sha256` listed here SHOULD match:
  - the file bytes on disk, and
  - the digest recorded in `release_evidence_index.json`.

---

## ♿ Accessibility requirements

Every evidence artifact MUST have a caption that is:

- specific (what metric / what scope / what aggregation),
- interpretable without color-only cues (include range or threshold),
- governance-safe (no sensitive detail).

Captions SHOULD be duplicated in:

- `release_evidence_index.json` (`caption` fields), and
- this table.

---

## ➕ Adding a new exhibit (checklist)

1. Add the evidence file under one of:
   - `plots/`
   - `tables/`
   - `maps/`
2. Compute `sha256` (preferred).
3. Register it in `release_evidence_index.json`.
4. Add a row to the table above.
5. Confirm the exhibit is aggregated and governance-safe.

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governed template for a human-readable release evidence index aligned to the machine index (`release_evidence_index.json`). |

---

Back to evidence README · [`README.md`](README.md) · Release report · [`../README.md`](../README.md) · Releases index · [`../../README.md`](../../README.md) · Reports index · [`../../../README.md`](../../../README.md) · Governance · [`../../../../../../../standards/governance/ROOT-GOVERNANCE.md`](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

