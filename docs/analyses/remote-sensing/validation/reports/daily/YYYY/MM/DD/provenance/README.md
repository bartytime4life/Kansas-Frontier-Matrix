---
title: "🧬 KFM — Daily Validation Provenance (PROV-O · OpenLineage · Ref Bundles)"
path: "docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/provenance/README.md"

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

intent: "remote-sensing-validation-daily-report-provenance"
audience:
  - "Remote Sensing Engineering"
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

governance_ref: "../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:daily:provenance:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-daily-provenance"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/provenance/README.md"
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

# 🧬 **KFM — Daily Validation Provenance**
`docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/provenance/README.md`

**Purpose**  
Define how a single day’s validation bundle references provenance artifacts:
**PROV‑O JSON‑LD**, **OpenLineage events**, and related digests/identifiers—kept **small, deterministic, and governance-safe**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder holds **provenance references** for a single day’s validation report bundle.

The intent is to keep the in-repo day bundle:

- **auditable** (stable ids + hashes + pointers),
- **deterministic** (reproducible link structure),
- **governance-safe** (no sensitive or restricted detail),
- **small** (no large provenance dumps).

Normative provenance posture lives in:

- `docs/analyses/remote-sensing/validation/methods/provenance/README.md`

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/provenance/
├── 📄 README.md                                              — This policy/index
├── 🧾 prov_bundle.ref.json                                   — Recommended: pointer to PROV-O JSON-LD bundle (asset id + digest)
├── 🧾 openlineage.ref.json                                   — Optional: pointer to OpenLineage event set (run id + digest)
├── 🧾 provenance_index.json                                  — Optional: small registry of provenance pointers for the day
└── 🧾 attestations.ref.json                                  — Optional: pointers to attestations (SLSA/SBOM refs) when required by policy
~~~

> These files are pointers, not payloads. If a provenance artifact is large, store it as a governed asset and reference it here.

---

## ✅ What belongs here

Keep provenance content in this folder to **references and checksums**:

- stable ids:
  - `run_id`
  - `algorithm_id`(s)
  - STAC item ids for validation outputs
- digests:
  - `sha256` for provenance bundles or manifests
- pointers:
  - repo paths to small local artifacts
  - governed asset identifiers (STAC asset keys / URNs)
- high-level governance posture:
  - `care_gate_status`
  - `sovereignty_gate`
  - redaction summary counts and reason codes

Recommended fields for `prov_bundle.ref.json`:

- `run_id`
- `prov_bundle_id` (URN or STAC asset reference)
- `sha256`
- `storage_ref` (repo path or governed storage path)
- `created_utc`

---

## ⛔ What must NOT be stored here

Do NOT commit any of the following in this folder:

- large PROV-O JSON-LD bundles (unless explicitly tiny and approved),
- raw coordinate lists, site identifiers, or “how to locate” details,
- signed URLs, tokens, credentials, internal endpoints, or secrets,
- per-sample lists from restricted collections,
- bulky run logs or payload dumps.

If deeper detail is required:

- store it as a governed artifact and link via STAC assets and PROV entity ids,
- keep only digests and stable references here.

---

## 🧾 Recommended pointer shapes (illustrative)

### `prov_bundle.ref.json` (example)

~~~json
{
  "ref_kind": "prov_bundle",
  "ref_version": "v1",
  "day_utc": "YYYY-MM-DD",
  "run_id": "urn:kfm:run:<...>",
  "prov_bundle_id": "urn:kfm:artifact:prov:<...>",
  "sha256": "<sha256>",
  "storage_ref": {
    "type": "stac_asset",
    "stac_item_id": "urn:kfm:stac:item:<...>",
    "asset_key": "prov_jsonld"
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
~~~

### `openlineage.ref.json` (example)

~~~json
{
  "ref_kind": "openlineage",
  "ref_version": "v1",
  "day_utc": "YYYY-MM-DD",
  "run_id": "urn:kfm:run:<...>",
  "openlineage_run_id": "urn:uuid:<...>",
  "sha256": "<sha256>",
  "storage_ref": {
    "type": "artifact_ref",
    "path": "data/processed/<...>/openlineage_events.json"
  },
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ"
}
~~~

---

## 🔗 Linkage rules (STAC/DCAT/PROV)

Preferred linkage pattern:

- **STAC Item** for the day or per-run validation output includes assets:
  - `metrics_summary_json`
  - `prov_jsonld` (PROV bundle)
  - optional `openlineage_events`
  - optional `config_snapshot` and `input_pack_manifest`
- this folder references those assets by:
  - STAC item id + asset key, plus digest.

DCAT linkage (when published) SHOULD reference PROV bundle via `dct:provenance` and distribution refs.

---

## 🎯 Determinism requirements (non-negotiable)

Provenance pointers MUST be reproducible:

- use stable `run_id` schemes (derived from frame/config hashes, not wall-clock alone),
- sort arrays and ids lexicographically before hashing,
- record digests for referenced artifacts (sha256 preferred),
- keep cross-links consistent:
  - the `run_id` in summary/manifests must match the `run_id` in provenance refs.

If provenance is required by contract and missing:

- record the failure as a reason code in the day summary (`PROVENANCE_INCOMPLETE`),
- treat as `fail` or `warn` per the governed gate mode.

---

## 🛡️ FAIR+CARE and sovereignty posture

This folder is public-facing by default. Therefore:

- never include raw coordinates or restricted identifiers,
- keep spatial scope generalized (region/coarse grid) when included at all,
- when redaction is applied:
  - record only counts and reason codes,
  - link to governed artifacts rather than embedding details.

---

## 🧪 CI/CD expectations (recommended)

CI may validate:

- required pointer files exist for governed runs (policy-dependent),
- required fields present (`run_id`, `sha256`, `storage_ref`, governance posture),
- cross-link consistency:
  - `run_id` matches day summary and manifests,
  - STAC item id / asset keys are present in refs,
- leakage scans:
  - no coordinates, secrets, or signed URLs.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed provenance pointer policy for daily validation bundles; defined allowed reference files, determinism rules, STAC linkage patterns, and governance-safe publication posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />

[⬅ Day Bundle](../README.md) ·
[🧾 Manifests](../manifests/README.md) ·
[📎 Attachments](../attachments/README.md) ·
[🧩 Methods](../../../../../../methods/README.md) ·
[🧾 Provenance Methods](../../../../../../methods/provenance/README.md) ·
[🏛️ Governance Charter](../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

