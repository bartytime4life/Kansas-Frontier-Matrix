---
title: "🧾 KFM — Remote Sensing Per‑Run Validation Bundles (Run ID · Artifacts · Links)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/README.md"

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

intent: "remote-sensing-validation-per-run-index"
audience:
  - "Remote Sensing Engineering"
  - "Data Engineering"
  - "Reliability Engineering"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-reports-per-run-index"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/README.md"
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

# 🧾 **KFM — Remote Sensing Per‑Run Validation Bundles**
`docs/analyses/remote-sensing/validation/reports/per-run/README.md`

**Purpose**  
Define the structure and naming for **per‑run** validation report bundles that map 1:1 to a pipeline execution
and link to governed artifacts (STAC/DCAT/PROV) and run logs/config snapshots.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-blue" />

</div>

---

## 📘 Overview

Per-run bundles are the most audit-friendly report unit:

- ties directly to a single pipeline execution (`run_id`),
- can be referenced from PR checks, release promotion, and incident notes,
- contains a human-readable summary plus machine-readable metrics and refs,
- stays light by linking to governed artifacts instead of embedding large data.

Per-run reports are **documentation-grade**. The authoritative artifacts live under governed data paths.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/          — Reports root
└── 📁 per-run/                                             — Per-run bundles (this directory)
    ├── 📄 README.md                                        — This index
    └── 📁 <run_id>/                                        — One folder per run (recommended)
        ├── 📄 summary.md                                   — Human-readable summary
        ├── 🧾 metrics.json                                 — Small machine-readable summary
        ├── 🧾 links.json                                   — STAC/DCAT/PROV refs + run log/config refs
        ├── 🧾 drift.delta.json                              — Optional: previous-run comparison (small)
        └── 📁 evidence/                                    — Optional: small evidence artifacts (safe only)
            ├── 🧾 tables.csv                               — Optional: small metric tables (no secrets)
            └── 📄 notes.md                                 — Optional: operator notes (no sensitive content)
~~~

> If `<run_id>` contains characters unsuitable for paths, use a stable slug and store the canonical `run_id`
> inside `links.json` and `metrics.json`.

---

## 🧾 Per‑run bundle contract (recommended)

Each per-run bundle SHOULD include:

### 1) `summary.md` (human-facing)

Minimum content:

- `run_id` and pipeline name/version
- execution window (UTC), AOI (generalized if needed)
- pass/fail overview and top failing checks
- brief “what changed” (if drift is detected)
- links to catalogs and provenance (do not paste huge payloads)

### 2) `metrics.json` (machine-facing, small)

Recommended fields:

- `run_id`
- `pipeline_id`
- `pipeline_version`
- `started_utc`, `ended_utc`, `duration_s`
- `datasets_checked` (count)
- `checks_total`, `checks_failed`, `checks_pass_ratio`
- `freshness_p95_seconds` (if applicable)
- `drift_flags_total`
- `care_gate_status` (`allow|redact|deny`)
- `sovereignty_gate` (`clear|restricted|conflict|unknown`)
- `redaction_summary` (counts + reason codes only)

### 3) `links.json` (references only)

Recommended fields:

- `stac_collections` and `stac_items` (repo paths or stable hrefs)
- `dcat_datasets` (repo paths or stable hrefs)
- `prov_bundles` (repo paths or governed provenance locations)
- `run_logs` (e.g., `mcp/runs/<run_id>/validate.log`)
- `config_snapshot` (e.g., `mcp/runs/<run_id>/config.snapshot.json`)
- `code_commit_sha` and/or workflow run identifier
- optional `attestations` (SBOM/SLSA refs where applicable)

---

## 🧭 Naming conventions

Use deterministic naming:

- Folder: `per-run/<run_id>/`
- Files: `summary.md`, `metrics.json`, `links.json`
- Optional:
  - `drift.delta.json` (only if drift is computed)
  - `evidence/` (small, safe artifacts only)

---

## 🛡️ FAIR+CARE and sovereignty posture

Per-run bundles MUST be safe to publish in-repo:

- no restricted coordinates,
- no internal-only endpoints, tokens, or signed URLs,
- no re-identifying join keys for sensitive datasets,
- no imagery samples unless governance explicitly allows.

If a run touches governed or sensitive datasets:

- set `care_gate_status` appropriately (`redact` or `deny`),
- include only aggregated metrics and generalized spatial descriptors,
- reference restricted artifacts by governed paths only.

---

## 🧪 CI/CD alignment

Per-run bundles are ideal for CI and release promotion:

- PR checks can attach/link to `per-run/<run_id>/summary.md`
- Release rollups can aggregate `metrics.json` across runs
- Incident timelines can cite per-run bundles as evidence

Recommended gates:

- STAC/DCAT schema validation results recorded (summary + link to machine report)
- asset integrity checks (checksums and expected asset presence; values safe)
- spatiotemporal sanity checks (generalized AOI)
- drift thresholds vs previous run/release

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial per-run reports index; defined bundle structure, naming, and governance posture. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Reports](../README.md) ·
[📅 Daily Reports](../daily/README.md) ·
[📦 Release Reports](../releases/README.md) ·
[📡 Validation](../../README.md) ·
[📡 Remote Sensing Analyses](../../../README.md) ·
[🏛️ Governance Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

