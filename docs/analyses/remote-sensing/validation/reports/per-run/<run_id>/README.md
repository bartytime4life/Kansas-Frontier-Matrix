---
title: "🏃 KFM — Remote Sensing Validation Per-Run Report Bundle (<run_id>)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/README.md"

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

intent: "remote-sensing-validation-per-run-report-bundle"
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

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/README.md"
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

# 🏃 **KFM — Remote Sensing Validation Per‑Run Report Bundle**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/README.md`

**Purpose**  
Define the contents and rules for a **single validation run bundle** keyed by `<run_id>`.
This folder stores small, deterministic summaries plus **references** to governed evidence (STAC/PROV/OpenLineage), suitable for ops visibility, governance review, and release promotion.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Per-Run" src="https://img.shields.io/badge/Reports-Per--Run-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory corresponds to a **single validation run** identified by `<run_id>`.

A per-run bundle exists to answer, unambiguously:

- what inputs were validated (and their digests),
- what config/thresholds/sampling rules were applied (pinned snapshot),
- what outputs were produced (and their digests),
- what provenance was emitted (PROV-O / OpenLineage),
- what the run outcome was (`pass|warn|fail`) and why (reason codes).

This folder is **reference-first**:

- keep it small,
- do not commit bulky payloads here,
- store heavy artifacts as governed assets and reference them via STAC and PROV.

---

## 🆔 What is `<run_id>`?

`<run_id>` MUST be a stable identifier for a single validation execution.

Recommended forms:

- `urn:kfm:run:<...>` (preferred for governed runs)
- `urn:uuid:<...>` (acceptable if policy permits)

`<run_id>` SHOULD be reproducible from run context (e.g., `frame_hash + config_hash`) and MUST NOT rely on wall-clock time alone.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/
├── 📄 README.md                                              — This file (bundle rules)
├── 🧾 run.summary.json                                       — Required: run outcome + key metrics (machine, small)
├── 📄 run.summary.md                                         — Optional: human summary (small)
├── 🧾 run.refs.json                                          — Optional: references only (STAC/DCAT/PROV/OpenLineage)
├── 📁 manifests/                                             — Recommended: deterministic manifests (small)
│   ├── 🧾 input_pack_manifest.json                           — Inputs (ids + digests or refs)
│   ├── 🧾 config_snapshot.json                               — Pinned thresholds/masks/sampling/numeric policy
│   └── 🧾 output_manifest.json                               — Outputs (ids + digests or refs)
├── 📁 provenance/                                            — Recommended: provenance pointers (small)
│   ├── 🧾 prov_bundle.ref.json                               — Pointer to PROV-O JSON-LD bundle (asset id + digest)
│   └── 🧾 openlineage.ref.json                               — Pointer to OpenLineage events (run id + digest)
└── 📁 attachments/                                           — Optional: governance-safe notes (small)
    └── 📄 notes.md
~~~

Notes:

- If a manifest or provenance artifact is large, store it elsewhere as a governed asset and reference it here by id/path + digest.
- Keep per-sample lists out of this directory unless explicitly approved and governance-safe.

---

## ✅ Minimum required file: `run.summary.json`

`run.summary.json` MUST be small and stable.

Recommended fields:

- `run_id`, `created_utc`
- `day_utc` (or run window)
- `scope` (generalized spatial scope when required; UTC time window)
- `algorithms` executed
- `outcome`: `pass|warn|fail`
- `reason_codes`: deterministic list
- `results`:
  - aggregate metrics and threshold results only
- `support_counts` (items/tiles/pixels/time steps where applicable)
- `sampling` (only if sampling used):
  - mode/unit/seed (or systematic rule id),
  - `frame_hash_sha256`,
  - candidate vs selected counts
- `governance`:
  - CARE gate status,
  - sovereignty gate status,
  - redaction counts and reason codes only
- `refs`:
  - STAC ids/hrefs for produced evidence items,
  - PROV bundle refs,
  - config snapshot and input pack digests/refs

Illustrative skeleton:

~~~json
{
  "run_id": "urn:kfm:run:<run_id>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "scope": {
    "time_start_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "time_end_utc": "YYYY-MM-DDTHH:MM:SSZ",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "unit": "item|tile|time_step|item_tile"
  },
  "algorithms": [
    "kfm:rs:validate:<family>:<name>:v1"
  ],
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "results": {
    "metrics": {},
    "thresholds": {},
    "outcome": "pass|warn|fail",
    "reason_codes": []
  },
  "support_counts": {},
  "sampling": null,
  "refs": {
    "stac_items": [],
    "prov_bundles": [],
    "openlineage_runs": []
  },
  "checksums": {
    "frame_hash_sha256": "<sha256>",
    "config_snapshot_sha256": "<sha256>",
    "input_pack_sha256": "<sha256>",
    "output_sha256": "<sha256>"
  }
}
~~~

---

## 🎯 Determinism requirements (non-negotiable)

Per-run bundles MUST be reproducible:

- stable ordering before aggregation/hashing,
- pinned configuration and thresholds referenced by digest,
- deterministic sampling when sampling is used:
  - stable frame enumeration,
  - seed or systematic rule recorded,
  - selected set reproducible from frame + seed/rule,
- deterministic reason code selection and ordering.

If determinism cannot be achieved:

- set `outcome = "warn"` or `"fail"` (per policy),
- include a deterministic reason code (e.g., `NONDETERMINISTIC_INPUTS`),
- require governance review before promotion.

---

## 🛡️ FAIR+CARE and sovereignty posture

This folder is in-repo and should be treated as public-facing by default.

Do NOT store:

- raw coordinates,
- restricted identifiers,
- signed URLs, secrets, internal endpoints,
- per-sample lists for restricted collections.

When restricted inputs exist:

- record generalized spatial scope,
- store detailed traces as governed assets and reference them via STAC/PROV,
- include only counts and reason codes for redaction actions.

---

## 🧪 CI/CD expectations (recommended)

A governed CI check for per-run bundles MAY enforce:

- required files exist (`run.summary.json`),
- `run.summary.json` validates against a schema (when provided),
- required keys are present (outcome, reason_codes, refs, governance posture),
- cross-link consistency:
  - `run_id` matches manifests and provenance refs,
  - digests are present and non-empty,
- leakage scans:
  - no coordinates,
  - no secrets,
  - no signed URLs.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed per-run bundle README template; standardized layout, minimum run summary requirements, determinism posture, and governance-safe publication rules. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Per-Run" src="https://img.shields.io/badge/Reports-Per--Run-blue" />

[⬅ Per-Run Reports](../README.md) ·
[🧾 Reports Index](../../README.md) ·
[📅 Daily Reports](../../daily/README.md) ·
[🏷 Release Reports](../../releases/README.md) ·
[🧩 Methods](../../../methods/README.md) ·
[🧮 Algorithms](../../../methods/algorithms/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

