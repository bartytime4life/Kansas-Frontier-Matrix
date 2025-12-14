---
title: "📆 KFM — Remote Sensing Validation Daily Report Bundle (YYYY-MM-DD)"
path: "docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Runbook"
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

intent: "remote-sensing-validation-daily-report-day-bundle"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:daily:day-bundle:YYYY-MM-DD:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-daily-report-YYYY-MM-DD"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/README.md"
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

# 📆 **KFM — Remote Sensing Validation Daily Report Bundle**
`docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/README.md`

**Purpose**  
Define the contents and rules for a **single-day validation bundle** (YYYY‑MM‑DD).
This folder holds day-scoped artifacts (summaries, manifests, provenance refs) used for ops visibility, governance review, and release evidence—without leaking restricted information.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Daily" src="https://img.shields.io/badge/Reports-Daily-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory corresponds to a single day:

- Replace `YYYY/MM/DD` with a calendar date (UTC-based reporting).
- This folder MAY contain the canonical day artifacts when you want:
  - a self-contained bundle (easy to archive, promote, or diff),
  - a stable place to store per-run references produced that day,
  - a governance-safe “evidence pack” for release promotion.

Month-level rollups MAY also exist alongside this structure. If both exist:

- month folder provides **at-a-glance** daily summaries,
- day folder provides the **bundle** (refs/manifests/provenance pointers).

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/
├── 📄 README.md                                              — This file (day-bundle rules)
├── 📄 YYYY-MM-DD.summary.json                                 — Daily summary (machine, small)
├── 📄 YYYY-MM-DD.summary.md                                   — Daily summary (human, optional)
├── 📄 YYYY-MM-DD.refs.json                                    — References only (STAC/DCAT/PROV/OpenLineage), optional
├── 📁 manifests/                                              — Deterministic manifests (small, recommended)
│   ├── 📄 input_pack_manifest.json                             — Immutable inputs evaluated (ids + digests or refs)
│   ├── 📄 config_snapshot.json                                 — Pinned thresholds/masks/sampling (digests or refs)
│   └── 📄 output_manifest.json                                 — Outputs produced (ids + digests or refs)
├── 📁 provenance/                                             — Provenance pointers (small, recommended)
│   ├── 📄 prov_bundle.ref.json                                 — Reference to PROV-O JSON-LD bundle (do not embed large)
│   └── 📄 openlineage.ref.json                                 — Reference to OpenLineage event set (do not embed large)
└── 📁 attachments/                                            — Optional: tiny supporting notes (no large tables)
    └── 📄 notes.md
~~~

Notes:

- Prefer **references and hashes** here rather than copying large run bundles.
- If you must store detailed outputs (large JSON, tables, plots), store them as governed artifacts and reference them via STAC assets + PROV.

---

## ✅ Minimum daily summary requirements

`YYYY-MM-DD.summary.json` SHOULD include:

- `day_utc`: `YYYY-MM-DD`
- `time_window_utc`: `{start, end}` in ISO8601 UTC
- `outcome`: `pass|warn|fail`
- `reason_codes`: stable list (empty for pass)
- `support_counts`: items/tiles/pixels/time steps (as applicable)
- `families`: per-family outcomes for algorithms/metrics executed
- `sampling` block when sampling is used:
  - mode, unit, candidate_count, selected_count,
  - `frame_hash_sha256`,
  - seed or systematic rule id
- governance posture:
  - `care_gate_status`,
  - `sovereignty_gate`,
  - `redaction_summary` counts (if any)
- references:
  - STAC ids (validation/report items) and/or href refs,
  - PROV bundle refs,
  - config snapshot digest/ref,
  - input pack digest/ref

Keep the daily summary small and stable.

---

## 🎯 Determinism rules (enforced posture)

Daily bundles MUST be reproducible:

- stable ordering before hashing or aggregation,
- pinned configuration (thresholds/masks/sampling rules) referenced by digest,
- deterministic reason code selection and ordering,
- deterministic sampling selection when sampling is used (seed + stable frame).

### Recommended hashes

- `frame_hash_sha256`: hash of ordered candidate ids + scope metadata (pinned rules)
- `config_snapshot_sha256`: hash of pinned config snapshot
- `input_pack_sha256`: hash of ordered input refs/digests
- `output_sha256`: hash of ordered outputs refs/digests (or the summary itself)

---

## 🛡️ FAIR+CARE and sovereignty posture

This folder is documentation and references only. Do NOT embed:

- raw coordinates,
- restricted site identifiers,
- “how to locate” details,
- signed URLs, secrets, or internal endpoints.

If restricted inputs were evaluated:

- record only generalized spatial scope,
- set explicit governance outcomes:
  - `care_gate_status = redact|deny` when required,
  - `sovereignty_gate = restricted|conflict|unknown` when applicable,
- include redaction counts and reason codes,
- keep detailed traces in governed storage; reference them via STAC/PROV.

---

## 🧪 CI/CD expectations (recommended)

CI MAY validate this day folder by checking:

- naming conventions (`YYYY-MM-DD.*`),
- presence of `summary.json`,
- required fields present (outcome, reason_codes, support_counts, refs),
- no leakage fields (coords, secrets, signed URLs),
- manifest consistency:
  - frame hash and config snapshot hash exist when sampling is used,
  - provenance refs resolve (when required by contract).

---

## 🧭 How to add a new artifact (safe pattern)

1. Add/extend `YYYY-MM-DD.summary.json` with a new family entry and references.
2. Add a small manifest or ref file under `manifests/` or `provenance/`.
3. If the artifact is large:
   - store it as a governed artifact and reference it via:
     - STAC asset href,
     - PROV `prov:Entity` id,
     - digest fields.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed day-bundle README template for daily remote-sensing validation reports; standardized directory layout, minimum summary requirements, determinism posture, governance-safe publication rules, and CI expectations. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Daily" src="https://img.shields.io/badge/Reports-Daily-blue" />

[⬅ Month Index](../README.md) ·
[⬅ Year Index](../../README.md) ·
[🧾 Daily Reports](../../../README.md) ·
[🧾 Reports Index](../../../../README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

