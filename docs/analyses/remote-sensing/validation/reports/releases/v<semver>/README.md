---
title: "🏷️ KFM — Remote Sensing Validation Release Report (v<semver>)"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Release Report"
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

intent: "remote-sensing-validation-release-report"
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

commit_sha: "<release-commit-sha>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-report-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/README.md"
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

# 🏷️ **KFM — Remote Sensing Validation Release Report**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/README.md`

**Purpose**  
This folder is the **release-grade validation bundle** for remote-sensing outputs promoted as **v<semver>**.
It aggregates per-run evidence into a single, governance-safe package suitable for **promotion decisions**, **audit**, and **reproducible rollback**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

A **release report** is the canonical, human-readable + machine-readable record that:

- names the released dataset(s) and their STAC/DCAT identifiers,
- summarizes validation outcomes and thresholds,
- captures drift/diff results vs the previous release (when applicable),
- proves determinism and governance posture (what was redacted, why, and how),
- links to evidence and provenance bundles (PROV/OpenLineage, manifests, digests).

This folder is expected to be **safe for in-repo publication** by default. If any input is restricted, this report MUST remain aggregated and redacted per policy.

---

## 🧭 What “v<semver>” means here

`v<semver>` is the **released dataset version** (SemVer) for the promoted remote-sensing product(s).

Recommended SemVer mapping:

- **MAJOR**: breaking schema/meaning/CRS change; compatibility breaks.
- **MINOR**: backward-compatible additions; new optional fields/assets/bands; new coverage.
- **PATCH**: data corrections/QA fixes without schema/meaning changes.

If multiple datasets are released together, this folder SHOULD include a mapping table (dataset id → released version) and explicitly name any mixed-version composition.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/
├── 📄 README.md                                  — This release report (index + narrative)
├── 🧾 release.summary.json                       — Required: machine-readable rollup (gates, metrics, refs)
├── 📄 release.summary.md                         — Optional: human narrative (executive summary, notes)
├── 📋 metrics_rollup.csv                         — Optional: aggregate metrics table (p50/p90/p99, etc.)
├── 📋 thresholds_eval.csv                        — Optional: threshold checks table (metric, threshold, outcome)
├── 📋 drift_delta_summary.csv                    — Optional: aggregate drift vs prior release (counts + deltas)
├── 📁 provenance/                                — Recommended: provenance pointers (PROV/OpenLineage refs)
│   └── 📄 README.md
├── 📁 manifests/                                 — Recommended: input/config/output manifests + digests
│   └── 📄 README.md
└── 📁 evidence/                                  — Optional: small, governance-safe exhibits (plots/tables/maps)
    └── 📄 README.md
~~~

Notes:

- Keep this folder **small and reviewable**.
- Large or sensitive artifacts SHOULD be stored as governed assets referenced via STAC and PROV (ids + digests), not copied here.

---

## ✅ Required contents (minimum)

### 1) Release identification

The report MUST identify:

- released dataset id(s) (KFM URNs preferred),
- STAC Collection/Item identifiers relevant to the release,
- DCAT dataset/distribution identifiers (if published),
- release commit sha and/or build attestation references (when governed).

### 2) Validation scope

The report MUST include:

- time window (UTC) covered by validation,
- spatial scope (generalized when required),
- sampling mode (full vs sampled) and sampling metadata if sampled.

### 3) Gates and outcomes

The report MUST state:

- pass/warn/fail outcome for each gate (quality, drift, determinism, governance),
- threshold margins (how far from the gate; aggregated),
- deterministic reason codes for any warn/fail.

### 4) Provenance and reproducibility

The report MUST link to:

- PROV-O JSON-LD bundle(s) or references,
- config snapshot (thresholds/masks/sampling/numeric policy),
- input pack manifest (inputs + digests),
- output manifest (outputs + digests).

---

## 🧾 Required machine-readable rollup

### `release.summary.json` (required)

This file is the authoritative rollup used by CI/promotion gates.

Recommended minimal shape:

~~~json
{
  "release_version": "v<semver>",
  "released_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "release_commit_sha": "<sha>",
  "datasets": [
    {
      "dataset_id": "urn:kfm:dataset:<...>",
      "stac_collection_id": "kfm-<...>",
      "dcat_dataset_id": "urn:kfm:dcat:<...>",
      "version": "<semver>"
    }
  ],
  "baseline": {
    "previous_release_version": "v<semver-1>|null",
    "baseline_ref": "urn:kfm:...|repo:path|stac:item"
  },
  "scope": {
    "time_start_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "time_end_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "sampling": "full|fixed_set|random|stratified|systematic",
    "seed": 1337
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "gates": [
    {"gate": "quality", "outcome": "pass|warn|fail", "reason_codes": []},
    {"gate": "drift", "outcome": "pass|warn|fail", "reason_codes": []},
    {"gate": "determinism", "outcome": "pass|warn|fail", "reason_codes": []},
    {"gate": "governance", "outcome": "pass|warn|fail", "reason_codes": []}
  ],
  "refs": {
    "manifests": {"path": "manifests/", "sha256": "<sha256>"},
    "provenance": {"path": "provenance/", "sha256": "<sha256>"},
    "evidence": {"path": "evidence/", "sha256": "<sha256>"},
    "per_run_refs": []
  },
  "checksums": {
    "summary_sha256": "<sha256>",
    "input_pack_sha256": "<sha256>",
    "config_snapshot_sha256": "<sha256>",
    "output_manifest_sha256": "<sha256>"
  }
}
~~~

---

## 🎯 Determinism requirements (non-negotiable)

Release reports MUST be reproducible:

- stable sort order for all lists (datasets, gates, per-run refs),
- pinned threshold sets and configs (referenced by digest),
- explicit sampling metadata when sampling is used,
- no signed URLs or environment-specific paths in the rollup,
- digests included for all referenced manifests and core artifacts.

If determinism cannot be proven for a release bundle, the default posture is **fail closed** (promotion blocked) unless governance override is recorded with signed justification.

---

## 🛡️ FAIR+CARE and sovereignty posture

Release reports are public-facing unless explicitly restricted.

Rules:

- do not include precise coordinates, site identifiers, or per-sample tile lists when restricted inputs exist,
- use generalized spatial scopes (region/coarse grid/H3 at governed resolution),
- report redaction as counts + reason codes only,
- if governance status is unclear, gates MUST fail closed per policy.

---

## 🧪 CI/CD and promotion expectations

Promotion workflows SHOULD validate:

- `release.summary.json` exists and passes schema checks,
- manifests and provenance refs exist and have digests,
- gate outcomes satisfy policy for the target environment (staging/prod),
- leakage checks pass (no coords/secrets/signed URLs),
- STAC/DCAT references resolve (where required by the release pathway),
- provenance chains include the release commit and run ids.

---

## ➕ Creating a new release report (checklist)

1. Create a folder: `releases/v<semver>/`
2. Write `release.summary.json` (required).
3. Add optional tables (`metrics_rollup.csv`, `thresholds_eval.csv`, `drift_delta_summary.csv`) if used.
4. Add `provenance/` pointers (PROV/OpenLineage refs + digests).
5. Add `manifests/` (input pack, config snapshot, output manifest + digests).
6. Add `evidence/` exhibits only if governance-safe and small.
7. Update `docs/analyses/remote-sensing/validation/reports/releases/README.md` to index the new release.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed template for remote-sensing validation release reports; defined required rollup, determinism posture, governance-safe publication rules, and CI expectations. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />

[⬅ Releases Index](../README.md) ·
[🧾 Reports Index](../../README.md) ·
[📅 Daily Reports](../../daily/README.md) ·
[🏃 Per-Run Reports](../../per-run/README.md) ·
[🧩 Methods](../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

