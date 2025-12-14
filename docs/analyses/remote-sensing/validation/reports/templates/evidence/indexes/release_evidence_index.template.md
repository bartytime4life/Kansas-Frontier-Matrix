---
title: "🧾 KFM — Release Evidence Index Template (Markdown) · Remote Sensing Validation"
path: "docs/analyses/remote-sensing/validation/reports/templates/evidence/indexes/release_evidence_index.template.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Template"
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

intent: "template-release-evidence-index-markdown"
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

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:templates:evidence:indexes:release-evidence-index-md:v11.2.6"
semantic_document_id: "kfm-template-release-evidence-index-md"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/templates/evidence/indexes/release_evidence_index.template.md"
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

# 🧾 **Release Evidence Index**
`releases/v<semver>/evidence/release_evidence_index.md` *(generated from template)*

**Purpose**  
Human-readable evidence registry for a release validation bundle. This index MUST mirror the machine-readable JSON index:
`releases/v<semver>/evidence/release_evidence_index.json`.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Index" src="https://img.shields.io/badge/Evidence-Index-blue" />
<img alt="Release v semver" src="https://img.shields.io/badge/Release-v%3Csemver%3E-informational" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This document enumerates the **review evidence** for release `v<semver>`:

- 🗺️ **Maps** (governance-safe, generalized spatial summaries)
- 📈 **Plots** (deterministic, comparable figures)
- 📋 **Tables** (aggregate metrics, thresholds, reason codes)

This index MUST:

- match the JSON inventory for ids, filenames, and ordering,
- provide short, review-friendly captions,
- avoid leakage (no precise coordinates, no signed URLs, no restricted identifiers).

---

## ✅ How to use this template

1. Copy this file to:
   - `docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/release_evidence_index.md`
2. Replace all placeholders:
   - `v<semver>`, `<sha256>`, `<created_utc>`, `<run_id>`, `<dataset_id>`, `<algorithm_id>`
3. Ensure the Markdown entries match:
   - `release_evidence_index.json` (same evidence ids, same order, same filenames, same digests)

---

## 🛡️ Governance posture (required)

**CARE gate status:** `allow|redact|deny`  
**Sovereignty gate:** `clear|restricted|conflict|unknown`  
**Redaction summary:** `<brief, non-sensitive summary>`

Notes:

- If `redact` or `deny`, maps may be omitted or replaced with aggregated tables only.
- Do not publish precise coordinates or “how to locate” details.

---

## 🗂️ Evidence inventory (stable order)

Ordering rule:

1) `Maps` (sorted by `evidence_id`)  
2) `Plots` (sorted by `evidence_id`)  
3) `Tables` (sorted by `evidence_id`)

Each entry MUST include:

- evidence id,
- relative path,
- sha256 digest,
- short caption,
- optional references (STAC/DCAT/PROV ids only; no signed URLs)

---

## 🗺️ Maps

> Use maps only when governance permits. Prefer generalized grids (region / coarse H3) with minimum group-size thresholds.

### Entries

- **ev:map:<slug>:001** — `maps/<filename>.png` · `sha256:<sha256>`  
  - Caption: `<short caption (what it shows, units, generalization method)>`  
  - Generalization: `<e.g., H3 r8, min_count=25, region-level>`  
  - Refs: `stac:<item_id>` · `prov:<bundle_id>` · `run:<run_id>`

- **ev:map:<slug>:002** — `maps/<filename>.png` · `sha256:<sha256>`  
  - Caption: `<short caption>`  
  - Generalization: `<method>`  
  - Refs: `stac:<item_id>` · `prov:<bundle_id>` · `run:<run_id>`

---

## 📈 Plots

> Plots MUST be deterministic (pinned bins and/or pinned axis bounds when comparisons matter). State rounding policy in captions.

### Entries

- **ev:plot:<slug>:001** — `plots/<filename>.png` · `sha256:<sha256>`  
  - Caption: `<short caption (metric, unit, rounding, sampling mode/seed if used)>`  
  - Determinism: `<bins/axes pinned; seed recorded if sampled>`  
  - Refs: `dataset:<dataset_id>` · `algorithm:<algorithm_id>` · `run:<run_id>`

- **ev:plot:<slug>:002** — `plots/<filename>.png` · `sha256:<sha256>`  
  - Caption: `<short caption>`  
  - Determinism: `<notes>`  
  - Refs: `dataset:<dataset_id>` · `algorithm:<algorithm_id>` · `run:<run_id>`

---

## 📋 Tables

> Tables MUST be stable-sorted and aggregated. Avoid per-sample listings when restricted inputs exist.

### Entries

- **ev:table:<slug>:001** — `tables/<filename>.csv` · `sha256:<sha256>`  
  - Caption: `<short caption (what metrics/thresholds; sort keys; rounding)>`  
  - Sorting: `<e.g., algorithm_id, dataset_id, region_id>`  
  - Refs: `dataset:<dataset_id>` · `algorithm:<algorithm_id>` · `run:<run_id>`

- **ev:table:<slug>:002** — `tables/<filename>.csv` · `sha256:<sha256>`  
  - Caption: `<short caption>`  
  - Sorting: `<keys>`  
  - Refs: `dataset:<dataset_id>` · `algorithm:<algorithm_id>` · `run:<run_id>`

---

## 🔁 Consistency checks (required)

Before promotion, confirm:

- [ ] Every entry here exists on disk under `evidence/`
- [ ] Every entry here appears in `release_evidence_index.json`
- [ ] Every sha256 here matches the JSON index and the actual file bytes
- [ ] Ordering matches the JSON index (stable by `evidence_id`)
- [ ] Governance posture matches the release report summary

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed Markdown template for release evidence indexes; standardized entry blocks, determinism notes, governance posture block, and JSON parity requirements. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />

[⬅ Templates Index](../../README.md) ·
[🧾 Evidence Templates](../README.md) ·
[🧾 Evidence Index Templates](./README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

