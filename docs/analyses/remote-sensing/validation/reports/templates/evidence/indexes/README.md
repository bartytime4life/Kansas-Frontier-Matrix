---
title: "🧾 KFM — Evidence Index Templates (JSON + Markdown) for Remote Sensing Validation Reports"
path: "docs/analyses/remote-sensing/validation/reports/templates/evidence/indexes/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Templates Guide"
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

intent: "remote-sensing-validation-evidence-index-templates"
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

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:templates:evidence:indexes:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-evidence-index-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/templates/evidence/indexes/README.md"
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

# 🧾 **KFM — Evidence Index Templates**
`docs/analyses/remote-sensing/validation/reports/templates/evidence/indexes/README.md`

**Purpose**  
Provide governed templates for **evidence indexes** (JSON + Markdown) used by remote-sensing validation reports.
Indexes are the canonical registry for evidence artifacts (maps/plots/tables) and MUST be deterministic and governance-safe.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Templates Evidence Indexes" src="https://img.shields.io/badge/Templates-Evidence%20Indexes-blue" />
<img alt="Determinism Pinned" src="https://img.shields.io/badge/Determinism-Pinned-informational" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

Evidence indexes are the authoritative bridge between:

- **human review** (navigable Markdown index), and
- **machine enforcement** (JSON inventory with checksums and stable identifiers).

These templates are used to generate (or manually author) indexes that:

- list evidence artifacts (maps, plots, tables),
- bind each artifact to a sha256 digest,
- document determinism posture (bins/rounding/seed),
- record governance posture (CARE/sovereignty gate outcomes),
- support reproducible release review.

### Template rules (mandatory)

- The JSON index MUST be deterministic:
  - stable sort order,
  - stable identifiers,
  - digests for every referenced artifact.
- The Markdown index MUST mirror the JSON index:
  - same evidence ids and filenames,
  - same ordering,
  - human-readable captions and navigation.
- Indexes MUST NOT leak restricted content:
  - no precise coordinates unless permitted by labels,
  - no signed URLs,
  - no secrets or internal endpoints.

### Where these templates are used

- Release evidence inventory:
  - `docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/release_evidence_index.json`
  - `docs/analyses/remote-sensing/validation/reports/releases/v<semver>/evidence/release_evidence_index.md`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/templates/evidence/indexes/   — Evidence index templates (JSON + Markdown)
├── 📄 README.md                                                                — This document
├── 🧾 release_evidence_index.template.json                                     — Template: machine-readable evidence inventory (release scope)
└── 📄 release_evidence_index.template.md                                       — Template: human-readable evidence inventory (release scope)
~~~

### Minimal template expectations

#### JSON index (required fields)

The JSON template SHOULD include:

- `index_kind`, `index_version`
- `release_version` (`v<semver>`) or `run_id` (if adapted for per-run)
- `created_utc`
- `governance` summary (gate outcomes, redaction counts)
- `evidence[]` entries with:
  - `evidence_id`
  - `kind` (`map|plot|table`)
  - `path` (relative, in-repo)
  - `sha256`
  - `caption` (short)
  - `refs` (optional STAC/DCAT/PROV pointers)

Illustrative shape:

~~~json
{
  "index_kind": "release_evidence_index",
  "index_version": "v1",
  "release_version": "v<semver>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_events_total": 0
  },
  "evidence": [
    {
      "evidence_id": "ev:<kind>:<slug>:<n>",
      "kind": "plot",
      "path": "evidence/plots/<file>",
      "sha256": "<sha256>",
      "caption": "Short, review-friendly caption."
    }
  ]
}
~~~

#### Markdown index (required conventions)

The Markdown template SHOULD:

- present evidence grouped by `Maps`, `Plots`, `Tables` (as H3/H4 under this H2),
- list evidence in the same stable order as JSON,
- provide short captions and the sha256 digest (or a link to a manifest that contains it),
- avoid embedding sensitive imagery inline when governance labels require redaction.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed index for evidence index templates; standardized JSON+MD expectations, determinism posture, and governance-safe publication rules. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Evidence Index Templates" src="https://img.shields.io/badge/Evidence-Index%20Templates-blue" />

[⬅ Evidence Templates](../README.md) ·
[🧾 Report Templates](../../README.md) ·
[📦 Reports Index](../../../README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

