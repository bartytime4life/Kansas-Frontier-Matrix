---
title: "📡 KFM — Remote Sensing Validation Reports (Artifacts · Summaries · Governance)"
path: "docs/analyses/remote-sensing/validation/reports/README.md"

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

intent: "remote-sensing-validation-reports-index"
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

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-reports-index"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/README.md"
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

# 📡 **KFM — Remote Sensing Validation Reports**
`docs/analyses/remote-sensing/validation/reports/README.md`

**Purpose**  
Governed index of **validation report artifacts** produced by remote-sensing pipelines:
metrics, summaries, diffs, and evidence bundles used for QA gates, release promotion, and auditability.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-blue" />

</div>

---

## 📘 Overview

This directory is the canonical home (in `docs/`) for **human-readable validation reports** and **report manifests** that:

- summarize quality checks (coverage, integrity, spatial/temporal sanity),
- record drift and deltas between releases,
- capture pass/fail outcomes for CI gates,
- link to governed artifacts (STAC/DCAT/PROV) rather than embedding large data.

Reports here are documentation-grade outputs. The authoritative machine artifacts live under governed data paths (e.g., `data/processed/**`, `data/stac/**`, `data/dcat/**`, PROV bundles).

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/                     — Validation docs root
└── 📁 reports/                                                 — Human-facing reports (this directory)
    ├── 📄 README.md                                            — This index
    ├── 📁 daily/                                               — Daily validation summaries (optional)
    ├── 📁 per-run/                                             — Per-run validation bundles (recommended)
    ├── 📁 releases/                                            — Release-level QA rollups (recommended)
    └── 📁 templates/                                           — Report templates + checklists (optional)
~~~

> Subfolders are recommended for organization. If they do not exist yet, add them as needed under governance review.

---

## 🧾 What belongs here

Put **docs-friendly** artifacts here:

- Markdown summaries for humans (`.md`)
- Small JSON summaries (counts/thresholds/outcomes) (`.json`)
- CSV/TSV metric tables when small and stable (`.csv`)
- Links to governed assets (STAC Items, DCAT datasets, PROV bundles)
- “Why it failed” notes for CI gates (no secrets)

Typical report content:

- completeness and missingness statistics
- band/asset integrity checks (expected assets present, sizes, checksums)
- spatial coverage checks (bbox sanity, CRS sanity, footprint shape rules)
- temporal coverage checks (expected windows met)
- cloud/mask coverage statistics (if applicable)
- resampling/tiling checks (tile count, edge overlap sanity)
- drift comparison vs last release (counts and key metric deltas)

---

## 🚫 What does not belong here

Do not commit:

- large rasters, tiles, or full imagery assets
- raw restricted coordinates, site-access instructions, or re-identifying join keys
- secrets, tokens, signed URLs, internal endpoints
- full “machine provenance payloads” when they already exist in `data/processed/prov/**` (link instead)

If a report needs to reference large artifacts:

- link to STAC assets or stable repo paths
- include checksums/digests and ids, not the bytes

---

## 🧭 Naming conventions (recommended)

Use deterministic, sortable naming:

- per run:
  - `per-run/<run_id>/summary.md`
  - `per-run/<run_id>/metrics.json`
  - `per-run/<run_id>/links.json` (STAC/DCAT/PROV refs)
- per date:
  - `daily/YYYY/MM/DD/summary.md`
- per release:
  - `releases/v<semver>/qa-rollup.md`

Where:

- `<run_id>` SHOULD be a stable run identifier (e.g., `urn:kfm:run:...` slug, or a CI run id)
- release folder uses the governed release tag (e.g., `v11.2.6`)

---

## 🔗 Required link-outs (minimum)

Each report bundle SHOULD include references to:

- the STAC Collection/Item(s) validated (`data/stac/**` refs)
- the DCAT dataset/distribution(s) validated (`data/dcat/**` refs)
- the PROV bundle for the run (`data/processed/prov/**` or governed provenance path)
- the run config snapshot (recommended: `mcp/runs/**/config.snapshot.json`)

This keeps reports lightweight while preserving auditability.

---

## 🛡️ FAIR+CARE and sovereignty posture

Remote-sensing validation can inadvertently expose sensitive locations when AOIs are small or tied to cultural/archaeological contexts.

Rules:

- obey dataset governance labels: when labels require masking or aggregation, reports MUST comply
- prefer region-level or coarse H3 summaries when reporting spatial coverage
- if a report would violate sovereignty policy:
  - omit sensitive fields and record `care_gate_status: "redact"` or `care_gate_status: "deny"` in the report summary
  - link to restricted artifacts only via governed access paths (no public URLs)

---

## 🧪 Validation and CI/CD alignment

Reports in this directory are expected to support (or mirror) machine gates, such as:

- schema validation (STAC/DCAT)
- asset integrity (checksums, expected bands/assets)
- spatiotemporal sanity checks
- drift thresholds vs previous release
- policy gates (rights/sensitivity labels consistent and enforced)

When a CI gate fails, the report SHOULD:

- identify the failing check
- show the expected vs observed metric
- link to the relevant provenance run id and artifacts

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed index for remote sensing validation reports; established directory structure, naming, and governance posture. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Validation](../README.md) ·
[📡 Remote Sensing Analyses](../../README.md) ·
[🏛️ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
