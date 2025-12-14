---
title: "🏷️ KFM — Remote Sensing Release Validation Reports (Promotion Gates · SemVer Rollups · Audit Bundles)"
path: "docs/analyses/remote-sensing/validation/reports/releases/README.md"

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

intent: "remote-sensing-validation-release-reports-index"
audience:
  - "Remote Sensing Engineering"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Release Managers"
  - "Governance Reviewers"
  - "Science QA Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-reports-releases-index"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
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

# 🏷️ **KFM — Remote Sensing Release Validation Reports**
`docs/analyses/remote-sensing/validation/reports/releases/README.md`

**Purpose**  
Define the structure and naming for **release-level validation rollups** used for promotion gates, SemVer-aligned change summaries, drift thresholds, and audit bundles referencing STAC/DCAT/PROV.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="License CC-BY 4.0" src="https://img.shields.io/badge/License-CC--BY%204.0-blue" />

</div>

---

## 📘 Overview

Release reports provide a stable, audit-friendly summary of validation outcomes for a **named release** (SemVer).

These reports are used to:

- support **promotion decisions** (staging → prod),
- record **what changed** and why it is compatible (SemVer posture),
- document drift thresholds and gate results,
- provide a lightweight audit trail that links to:
  - STAC collections/items,
  - DCAT datasets/distributions,
  - PROV bundles (and optional OpenLineage),
  - SBOM/SLSA attestations and checksums (when applicable).

Release reports are documentation-grade artifacts. They SHOULD reference (not duplicate) governed data artifacts.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/          — Reports root
└── 🏷️ releases/                                            — Release rollups (this directory)
    ├── 📄 README.md                                        — This index
    └── 🏷️ v<semver>/                                       — One folder per release (recommended)
        ├── 📄 qa-rollup.md                                 — Human-readable promotion rollup (required)
        ├── 🧾 metrics.json                                 — Machine-readable summary (recommended)
        ├── 🧾 links.json                                   — STAC/DCAT/PROV + attestations refs (recommended)
        ├── 🧾 drift.delta.json                              — Diff vs previous release (recommended)
        └── 🧾 evidence/                                    — Optional: small evidence artifacts (safe only)
            ├── 📋 tables/                                  — Optional: small metric tables (no secrets)
            ├── 📈 plots/                                   — Optional: deterministic plots (no leakage)
            ├── 🗺️ maps/                                    — Optional: generalized maps (governance-safe only)
            └── 📄 notes.md                                 — Optional: steward notes (no sensitive content)
~~~

Notes:

- Recommended folder naming is `vMAJOR.MINOR.PATCH` to match governed release tags.
- Keep evidence artifacts small and safe; link to larger governed assets via STAC/DCAT/PROV references.

---

## 🧾 Release bundle contract (recommended)

Each release folder SHOULD include:

### 1) `qa-rollup.md` (required)

Minimum content:

- release tag: `vMAJOR.MINOR.PATCH`
- coverage scope (pipelines/datasets included)
- pass/fail overview and gating outcomes
- drift highlights vs previous release (counts and threshold deltas)
- SemVer posture summary (why MAJOR/MINOR/PATCH is correct)
- links to catalogs and provenance (no large payloads embedded)

### 2) `metrics.json` (recommended, small)

Recommended fields:

- `release_version`
- `previous_release_version` (nullable)
- `datasets_checked`
- `pipelines_total`, `pipelines_failed`
- `checks_total`, `checks_failed`, `checks_pass_ratio`
- `freshness_p95_seconds` (if applicable)
- `drift_flags_total`
- `care_gate_status` (`allow|redact|deny`)
- `sovereignty_gate` (`clear|restricted|conflict|unknown`)
- `redaction_summary` (counts + reason codes only)

### 3) `links.json` (recommended, references only)

Recommended fields:

- `stac_collections` / `stac_items` (repo paths)
- `dcat_datasets` (repo paths)
- `prov_bundles` (repo paths or governed provenance locations)
- `run_ids` included in the rollup
- `config_snapshots` (e.g., `mcp/runs/**/config.snapshot.json`)
- `sbom_ref`, `slsa_attestation_ref`, `manifest_ref` (when used)
- `code_commit_sha` and any release pipeline run id

### 4) `drift.delta.json` (recommended)

Keep small and safe:

- counts changed (items/tiles/assets)
- key metric deltas (coverage %, error stats)
- threshold outcomes (pass/fail)
- no raw coordinates or restricted identifiers

---

## 🧭 Naming conventions

Use deterministic naming:

- `releases/v<semver>/qa-rollup.md`
- `releases/v<semver>/metrics.json`
- `releases/v<semver>/links.json`
- `releases/v<semver>/drift.delta.json`

---

## 🛡️ FAIR+CARE and sovereignty posture

Release reports MUST be safe to publish in-repo:

- no restricted coordinates or re-identifying location instructions,
- no internal endpoints, tokens, or signed URLs,
- no embedding of full imagery samples unless governance explicitly allows.

If a release includes governed datasets with sensitivity constraints:

- set `care_gate_status` to `redact` or `deny` as applicable,
- keep spatial reporting generalized (region-level or coarse H3),
- link to restricted artifacts only via governed repo paths.

---

## 🧪 CI/CD alignment and promotion gates

Release bundles SHOULD be produced (or updated) by the release workflow after:

- STAC/DCAT validation passes,
- provenance bundles are complete and linked,
- drift checks vs previous release are evaluated,
- any required attestations are generated and referenced.

When promotion fails, `qa-rollup.md` SHOULD:

- identify which gate failed,
- show expected vs observed metrics (safe),
- link to the run logs and provenance.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial release reports index; defined bundle structure, naming, and governance posture for promotion rollups. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Reports](../README.md) ·
[📅 Daily Reports](../daily/README.md) ·
[🧾 Per‑Run Bundles](../per-run/README.md) ·
[📡 Validation](../../README.md) ·
[🛰️ Remote Sensing Analyses](../../../README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
