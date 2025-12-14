---
title: "🗺️ KFM — Remote Sensing Validation Evidence Map Templates (Reports · Redaction · Determinism)"
path: "docs/analyses/remote-sensing/validation/reports/templates/evidence/maps/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Template Pack"
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

intent: "rs-validation-evidence-map-templates"
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

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:templates:evidence:maps:v11.2.6"
semantic_document_id: "kfm-rs-validation-evidence-maps-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/templates/evidence/maps/README.md"
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
  - "content-alteration"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🗺️ **KFM — Remote Sensing Validation Evidence Map Templates**
`docs/analyses/remote-sensing/validation/reports/templates/evidence/maps/README.md`

**Purpose**  
Define the **governed, deterministic** conventions for “evidence maps” embedded in remote-sensing validation reports (per-run, daily, release), including **redaction posture** and **machine-checkable metadata**.

<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/Evidence-Maps-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Evidence maps are **human-auditable visual artifacts** that support validation outcomes without requiring privileged access to raw inputs.

They are used to:

- communicate *where* evaluation occurred (at a governance-safe granularity),
- visualize aggregated error / residual structure (without leaking sensitive locations),
- summarize drift patterns across runs/releases,
- provide context for QA decisions (pass/warn/fail) with traceable provenance.

This directory defines:

- **map categories** (what types of maps are acceptable),
- **file naming and metadata requirements**,
- **redaction rules** for CARE/sovereignty constraints,
- **determinism rules** so repeated builds produce stable artifacts.

> Evidence maps are not a substitute for provenance. Every map MUST be referenced from an evidence index and associated PROV bundle.

### Map types (recommended)

1. **Coverage / footprint maps**
   - show generalized spatial scope (e.g., Kansas outline; H3 or tile-grid footprint)
2. **Residual / error maps**
   - aggregated MAE/RMSE/bias by tile/H3 cell (no point disclosure)
3. **Classification “difference” maps**
   - class disagreement counts at coarse resolution (avoid per-pixel examples in restricted zones)
4. **Drift maps**
   - release-to-release deltas summarized by region/tile
5. **Mask / quality maps**
   - cloud/invalid fraction by tile/H3 cell, not per-scene coordinate callouts

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/templates/           — Report template pack (governed)
└── 📁 evidence/                                                      — Evidence template family (indexes + media)
    ├── 📁 maps/                                                      — Evidence map conventions (this directory)
    │   └── 📄 README.md                                              — This document
    ├── 📁 plots/                                                     — Evidence plot conventions (time-series, histograms)
    ├── 📁 tables/                                                    — Evidence table conventions (CSV/Parquet summaries)
    └── 📁 indexes/                                                   — Evidence index templates (link map/plot/table refs)
~~~

---

## 🧭 Context

### Where these templates are used

Evidence maps are typically attached under one of:

- per-run: `docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/evidence/maps/`
- daily: `docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/attachments/` (or `evidence/maps/` when used)
- release: `docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/maps/`

The authoritative linkage is the **evidence index** for the bundle (release or run), not the map filename alone.

### Deterministic map generation (expectation)

If a pipeline generates evidence maps automatically, it MUST:

- use stable input enumeration (sorted list of tiles/items),
- pin styles/symbolization parameters (no “auto” scales that depend on data ordering),
- record the exact map recipe in provenance (tool version, params, seed if sampling).

---

## 🧪 Validation & CI/CD

### Required checks (recommended)

CI SHOULD enforce:

- **no EXIF / GPS metadata** in raster images intended for public docs,
- filenames comply with the conventions below,
- presence of a sidecar entry in the evidence index (release/run),
- checksums recorded in the bundle manifest.

### Minimal “map artifact checklist”

For each map file included in a governed report bundle:

- [ ] has a stable `map_id`
- [ ] has a deterministic `checksum_sha256`
- [ ] is referenced in the evidence index
- [ ] declares governance posture (CARE + sovereignty gate outcome)
- [ ] avoids sensitive coordinate disclosure (see governance section)

---

## ⚖ FAIR+CARE & Governance

### Redaction and disclosure rules (non-negotiable)

Evidence maps MUST NOT:

- embed precise coordinates for restricted / sovereignty-controlled data,
- include “pinpoint” markers to sensitive locations,
- show raw per-pixel examples for restricted AOIs if it enables reverse-location inference,
- include signed URLs, secrets, tokens, or private bucket paths.

Evidence maps SHOULD:

- generalize spatial scope to an approved representation:
  - state/region boundary,
  - **tile grid**,
  - **H3 at an approved resolution**,
  - “coarse raster” aggregation (policy-defined),
- use aggregation thresholds:
  - do not display cells with counts below a governance minimum (k-anonymity style),
- display **only** governance-safe layers:
  - residual magnitude, coverage fraction, class disagreement counts, etc.

If governance status is unclear, fail closed:

- omit the map from public bundles, or
- include only region-level summary (no grids), and mark `care_gate_status=deny` / `sovereignty_gate=unknown` in the metadata.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed conventions for evidence maps (determinism, metadata expectations, and FAIR+CARE redaction posture). |

---

<div align="center">

🗺️ **KFM — Remote Sensing Validation Evidence Map Templates**  
Documentation-First · FAIR+CARE Governance · Sustainable Intelligence

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[📡 Validation](../../../../README.md) ·  
[🧾 Reports](../../../README.md) ·  
[🧩 Templates](../../README.md) ·  
[🧾 Evidence Templates](../README.md) ·  
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·  
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

