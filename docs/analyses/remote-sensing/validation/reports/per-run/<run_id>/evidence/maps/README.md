---
title: "🗺️ KFM — Per-Run Validation Evidence Maps (Generalized · Deterministic · Governance-Safe)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/maps/README.md"

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

intent: "remote-sensing-validation-per-run-evidence-maps"
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

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:evidence:maps:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-evidence-maps-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/maps/README.md"
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

# 🗺️ **KFM — Per‑Run Validation Evidence Maps**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/maps/README.md`

**Purpose**  
This folder stores **generalized, governance-safe map exhibits** for a single validation run (`<run_id>`).
Maps must support review and release promotion while avoiding sensitive leakage and remaining reproducible under governed constraints.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Maps" src="https://img.shields.io/badge/Evidence-Maps-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Map exhibits are optional but useful to communicate validation outcomes:

- where error/uncertainty concentrates at a **generalized** spatial scale,
- whether coverage/support is spatially balanced,
- whether drift is geographically systematic (aggregated) vs uniform.

Maps in this folder MUST be:

- **generalized** (region/coarse grid; no pinpoint locations),
- **aggregated** (counts/metrics; not raw imagery chips),
- **deterministic** (pinned bins/extents/labels),
- **governance-safe** (FAIR+CARE and sovereignty screening mandatory).

---

## 🗂️ Directory Layout (expected)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/maps/
├── 📄 README.md                              — This policy/index
├── 🗺️ region_error_heatmap.png               — Example: region-level aggregate error map
├── 🗺️ h3_r<r>_error_heatmap.png              — Example: H3-generalized aggregate error map
├── 🗺️ region_coverage_counts.png             — Example: support/coverage counts map
├── 🗺️ region_outcome_passfail.png            — Example: pass/warn/fail by generalized region (if policy allows)
└── 🗺️ drift_delta_region_summary.png         — Example: release-to-release aggregate drift by region
~~~

Notes:

- Filenames are illustrative. Only include maps you actually produce.
- Any map included here SHOULD be registered in `../evidence_index.json` with a sha256 digest.

---

## ✅ Allowed map formats

Preferred:

- `PNG` (`.png`) — default for compact, deterministic map exhibits
- `SVG` (`.svg`) — acceptable if deterministic and metadata-stable

Avoid in this folder:

- `GeoTIFF`, `COG`, `NetCDF`, or any “data payload” rasters
- interactive map bundles (HTML/JS) unless explicitly approved and governance-safe

If a map needs to exist as a geospatial artifact:

- store it as a governed dataset asset and reference it via STAC/PROV,
- keep only small, safe exhibits in this directory.

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

Maps SHOULD be reproducible from the same inputs and config:

- fixed spatial scope and projection (documented in the config snapshot),
- fixed binning rules (no silent “auto bins”):
  - metric bins explicitly defined,
  - colorbar breakpoints explicitly defined,
- fixed aggregation keys (e.g., `region_id` or `h3_index` at a governed resolution),
- fixed extents and labels (avoid dynamic labeling),
- avoid export-time metadata embedding (timestamps, machine paths) where possible.

If deterministic rendering cannot be achieved:

- treat the map as optional,
- record a deterministic reason code (e.g., `NONDETERMINISTIC_RENDERING`) in the run summary if it affects gating.

---

## 🛡️ Governance and leakage rules (mandatory)

Maps can leak sensitive locations if they are too precise or show rare features.

Rules:

- **No precise coordinates** or pinpoint markers.
- Use only **generalized** spatial scopes:
  - region-level bins (county/eco-region/approved region partitions), or
  - H3 generalization at a governed resolution (e.g., `h3:r8` or coarser), when allowed.
- Enforce **minimum group sizes** before plotting subgroup results (policy-defined).
- Never include “before/after” chips or thumbnails derived from restricted inputs.
- If any input is sovereignty-restricted or governance is unclear:
  - produce only aggregated counts/metrics at coarse scopes,
  - suppress low-support bins,
  - fail closed in run gating per policy.

---

## ♿ Accessibility requirements (WCAG-aligned)

Every map exhibit SHOULD have a text description available via one of:

- `../evidence_index.md` caption text, or
- a short caption embedded in `../evidence_index.json` for the artifact.

Recommended minimum caption content:

- what metric is mapped,
- the generalized spatial scope (region type or H3 resolution),
- the aggregation summary (mean/median/p90),
- the support count basis (N bins / N samples).

Avoid relying on color alone; include legends and numeric ranges.

---

## 🔗 Registration in the evidence index

Every map SHOULD be referenced from:

- `../evidence_index.json`

Each entry SHOULD include:

- `evidence_id`
- relative path (e.g., `maps/region_error_heatmap.png`)
- `sha256`
- producing `algorithm_ids`
- generalized scope descriptor (region type or H3 resolution)
- a short caption (human-readable)

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- maps are optional, but if present:
  - every map is listed in `../evidence_index.json`,
  - sha256 digests match,
  - size limits are respected,
  - leakage scans pass (no coords, no secrets, no signed URLs),
  - filenames do not contain restricted identifiers.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for per-run evidence maps; defined allowed formats, naming conventions, determinism controls, and governance-safe spatial generalization rules. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Maps" src="https://img.shields.io/badge/Evidence-Maps-blue" />

[⬅ Evidence](../README.md) ·
[🧾 Evidence Index](../evidence_index.json) ·
[📊 Plots](../plots/README.md) ·
[📋 Tables](../tables/README.md) ·
[🏃 Run Bundle](../../README.md) ·
[🧾 Manifests](../../manifests/README.md) ·
[🧬 Provenance](../../provenance/README.md) ·
[📎 Attachments](../../attachments/README.md) ·
[🧾 Per-Run Reports](../../../README.md) ·
[🧾 Reports Index](../../../../README.md) ·
[🧩 Methods](../../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

