---
title: "🗺️ KFM — Release Validation Evidence Maps (v<semver>) · Generalized · Deterministic · Governance-Safe"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/maps/README.md"

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

intent: "remote-sensing-validation-release-evidence-maps"
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

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:evidence:maps:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-evidence-maps-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/maps/README.md"
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

# 🗺️ **KFM — Release Validation Evidence Maps**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/maps/README.md`

**Purpose**  
This folder contains **generalized, governance-safe map exhibits** that support the release validation bundle for **v<semver>**.
Maps here are **aggregated** (not raw), **deterministic where feasible**, and appropriate for **in-repo review**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Evidence Maps" src="https://img.shields.io/badge/Evidence-Maps-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Release map exhibits are optional, but often helpful for reviewers to assess:

- whether error/uncertainty concentrates geographically at a **safe, generalized** scale,
- whether sampling/support coverage is spatially balanced,
- whether drift vs baseline is geographically systematic (aggregate only),
- whether outcomes align with release gates and threshold margins.

Maps in this folder MUST NOT reveal sensitive locations or restricted context. Always treat maps as a potential leakage surface.

---

## 🗂️ Directory Layout (expected)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/maps/
├── 📄 README.md                                  — This policy/index
├── 🗺️ region_error_heatmap.png                   — Example: region-level aggregate error
├── 🗺️ h3_r<r>_error_heatmap.png                  — Example: H3-generalized aggregate error (governed resolution)
├── 🗺️ region_coverage_counts.png                 — Example: support/coverage counts (aggregate)
├── 🗺️ drift_delta_region_summary.png             — Example: drift vs baseline by region (aggregate)
└── 🗺️ outcome_region_passwarnfail.png            — Example: gate outcome by region (only if policy permits)
~~~

Notes:

- Filenames are illustrative. Include only what the release produces.
- Every map SHOULD be registered in `../release_evidence_index.json` with a sha256 digest.

---

## ✅ Allowed formats

Preferred:

- `PNG` (`.png`) — compact, reviewable, typically easiest to make deterministic
- `SVG` (`.svg`) — allowed if deterministic and metadata-stable

Avoid in this folder:

- raw geospatial rasters (`.tif`, `.cog`, `.nc`) and large payloads,
- interactive HTML maps,
- anything requiring external assets to render.

If a map must exist as a geospatial artifact:

- store it as a governed dataset asset (STAC/DCAT + PROV),
- reference it by stable id and digest in the release report and evidence index.

---

## 🏷️ Naming conventions (recommended)

Use `snake_case` and include only generalized scope tokens.

Recommended patterns:

- `region_<metric>_<summary>.png`
- `h3_r<r>_<metric>_<summary>.png`
- `drift_delta_region_<summary>.png`

Avoid embedding:

- coordinates,
- site identifiers,
- restricted dataset ids,
- exact tile identifiers.

---

## 🎯 Determinism requirements (non-negotiable)

Map exhibits SHOULD be reproducible from the same inputs and config snapshot:

- fixed spatial scope and projection (documented in release config),
- fixed aggregation keys (region id, or H3 at a governed resolution),
- fixed binning rules (no silent “auto bins”):
  - explicit numeric bins,
  - explicit legend breakpoints,
- fixed extents and labels (avoid dynamic labeling),
- avoid export-time metadata embedding (timestamps, local paths) where feasible.

If deterministic rendering is not achievable:

- treat the map as optional and non-gating,
- record a deterministic reason code in the release rollup (recommended).

---

## 🛡️ Governance and leakage rules (mandatory)

Maps can leak sensitive locations if they are too precise or show rare patterns.

Rules:

- **No precise coordinates** or pinpoint markers.
- Use **generalized** spatial scopes only:
  - region-level bins (county/eco-region/approved partitions), or
  - H3 generalization at a governed resolution (often coarse).
- Enforce **minimum group sizes** for any subgroup visualization (policy-defined).
- Do not publish “before/after” chips, thumbnails, or raw imagery excerpts.
- If any input is sovereignty-restricted or governance is unclear:
  - publish only high-level aggregates,
  - suppress low-support bins,
  - fail closed on release gates unless an approved override exists.

---

## ♿ Accessibility requirements (WCAG-aligned)

Every map SHOULD have an accessible caption available via:

- `../release_evidence_index.md` (human index), and/or
- `../release_evidence_index.json` (`caption` fields)

Captions SHOULD include:

- the metric mapped,
- the aggregation scope (region type or H3 resolution),
- the value summary (mean/median/p90),
- the support basis (counts and sampling posture).

Avoid relying on color alone; include legends and numeric ranges.

---

## 🔗 Registration (release evidence index)

Every map exhibit SHOULD be registered in:

- `../release_evidence_index.json`

Each entry SHOULD include:

- `evidence_id`
- relative path (e.g., `maps/region_error_heatmap.png`)
- `sha256`
- producing `algorithm_ids`
- generalized scope descriptor (region type or H3 resolution)
- a short, governance-safe caption

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- if maps exist:
  - each map is listed in `../release_evidence_index.json`,
  - sha256 digests match,
  - size limits are respected,
  - leakage scans pass (no coordinates, no secrets, no signed URLs),
  - filenames do not include restricted identifiers.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release evidence maps; defined allowed formats, naming conventions, determinism controls, and governance-safe generalization rules for maps used in release promotion. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Maps" src="https://img.shields.io/badge/Evidence-Maps-blue" />

[⬅ Evidence](../README.md) ·
[🧾 Evidence Index](../release_evidence_index.md) ·
[🧾 Evidence Index JSON](../release_evidence_index.json) ·
[🏷 Release Report](../../README.md) ·
[🏷 Releases Index](../../../README.md) ·
[🧾 Reports Index](../../../../README.md) ·
[🏃 Per-Run Reports](../../../../per-run/README.md) ·
[📅 Daily Reports](../../../../daily/README.md) ·
[🧩 Methods](../../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

