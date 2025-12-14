---
title: "🧾 KFM — Daily Validation Manifests (Input Pack · Config Snapshot · Output Manifest)"
path: "docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/manifests/README.md"

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

intent: "remote-sensing-validation-daily-report-manifests"
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
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:daily:manifests:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-daily-manifests"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/manifests/README.md"
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

# 🧾 **KFM — Daily Validation Manifests**
`docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/manifests/README.md`

**Purpose**  
Define what “manifests” are for a single day’s remote-sensing validation bundle and how they must be written:
**deterministic**, **auditable**, and **governance-safe** (no sensitive leakage).

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Manifests" src="https://img.shields.io/badge/Bundle-Manifests-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Manifests are the **small, immutable “what exactly happened” records** for a validation run/day.

They exist so we can always answer:

- What exact inputs were evaluated (and their digests)?
- What exact configuration produced the outputs (thresholds, masks, sampling, numeric policy)?
- What outputs were produced (and their digests)?
- Can we replay the run and get identical results?

This folder MUST remain safe for publication:

- do not embed data payloads,
- do not embed coordinates or sensitive identifiers,
- do not include signed URLs, secrets, or internal endpoints.

Use **references and digests** instead.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/manifests/
├── 📄 README.md                                               — This file (manifest policy/index)
├── 🧾 input_pack_manifest.json                                 — Required (recommended): immutable inputs evaluated
├── 🧾 config_snapshot.json                                     — Required (recommended): pinned config/thresholds/masks
├── 🧾 output_manifest.json                                     — Required (recommended): outputs produced (refs + digests)
├── 🧾 sampling_manifest.json                                   — Optional: frame/selection details (if sampling used)
└── 🧾 checksums.json                                           — Optional: convenience rollup of digest fields
~~~

Notes:

- Keep these manifests small. If the candidate set or selected set is large:
  - store the full list as a governed artifact elsewhere and reference it by id/path + digest here.

---

## ✅ Required properties (manifest-wide)

Every manifest file SHOULD include:

- `manifest_kind`: one of `input_pack|config_snapshot|output|sampling|checksums`
- `manifest_version`: e.g., `"v1"`
- `created_utc`: ISO8601 UTC timestamp
- `run_id`: stable identifier for the validation run/bundle
- `day_utc`: `YYYY-MM-DD`
- `algorithm_ids`: list (when applicable) or a single `algorithm_id`
- `governance` posture:
  - `care_gate_status`: `allow|redact|deny`
  - `sovereignty_gate`: `clear|restricted|conflict|unknown`
  - `redaction_summary`: counts + reason codes only

---

## 🎯 Determinism rules (non-negotiable)

Manifests MUST support deterministic replay:

- Stable ordering:
  - lists MUST be sorted deterministically (lexicographic by `id` unless otherwise specified).
- Stable hashing:
  - digests MUST be computed over immutable inputs/bytes or stable canonical representations.
- Pinned configuration:
  - all thresholds/masks/sampling/numeric policy must be included or referenced by digest.
- No clock-entropy in identifiers:
  - do not generate `run_id` from wall-clock alone.
  - `run_id` should be derived from frame/config hashes (see sampling/provenance docs).

If a list is empty due to gating, record that explicitly, do not omit keys.

---

## 🧾 input_pack_manifest.json (recommended)

This manifest captures **what was evaluated**.

Include:

- scope:
  - UTC window,
  - generalized spatial scope (region/coarse grid where required),
  - sampling unit (item/tile/time-step), if relevant
- inputs:
  - stable ids (STAC Item ids, dataset URNs, artifact URNs),
  - immutable URIs/paths when allowed,
  - digests (preferred sha256),
  - role: `primary|reference|baseline|auxiliary`

Skeleton (illustrative):

~~~json
{
  "manifest_kind": "input_pack",
  "manifest_version": "v1",
  "created_utc": "2025-12-14T00:00:00Z",
  "day_utc": "YYYY-MM-DD",
  "run_id": "urn:kfm:run:<...>",
  "scope": {
    "time_start_utc": "YYYY-MM-DDT00:00:00Z",
    "time_end_utc": "YYYY-MM-(DD+1)T00:00:00Z",
    "spatial_scope": "kansas|region:<...>|h3:r<...>",
    "unit": "item|tile|time_step|item_tile"
  },
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "inputs": [
    {
      "id": "urn:kfm:stac:item:<...>",
      "uri": "data/stac/<...>.json",
      "sha256": "<sha256>",
      "role": "primary"
    }
  ],
  "frame_hash_sha256": "<sha256>",
  "input_pack_sha256": "<sha256>"
}
~~~

---

## 🧾 config_snapshot.json (recommended)

This manifest captures **exact configuration** used for validation:

- algorithm ids and versions
- metric definitions and threshold versions
- mask policy references and digests
- sampling policy (mode/unit/seed/systematic rule) when used
- numeric policy:
  - dtype expectations,
  - NaN behavior,
  - rounding rules,
  - quantile method/bins if relevant

Skeleton (illustrative):

~~~json
{
  "manifest_kind": "config_snapshot",
  "manifest_version": "v1",
  "created_utc": "2025-12-14T00:00:00Z",
  "day_utc": "YYYY-MM-DD",
  "run_id": "urn:kfm:run:<...>",
  "algorithms": [
    {"algorithm_id": "kfm:rs:validate:<family>:<name>:v1", "impl_ref": "src/<...>", "impl_sha": "<sha256>"}
  ],
  "thresholds_ref": {"path": "docs/<...>", "sha256": "<sha256>"},
  "mask_policy_ref": {"path": "docs/<...>", "sha256": "<sha256>"},
  "sampling": {
    "mode": "full|fixed_set|random|stratified|systematic",
    "unit": "item|tile|time_step|item_tile",
    "seed": 1337,
    "systematic_rule_id": null
  },
  "numeric_policy": {
    "dtype": "float32",
    "nan_policy": "propagate|omit|zero",
    "rounding": {"decimals": 6}
  },
  "config_snapshot_sha256": "<sha256>"
}
~~~

---

## 🧾 output_manifest.json (recommended)

This manifest captures **what was produced**:

- pointers to summary outputs,
- pointers to provenance bundles,
- optional pointers to detailed reports (stored elsewhere),
- digests for each output asset/ref.

Skeleton (illustrative):

~~~json
{
  "manifest_kind": "output",
  "manifest_version": "v1",
  "created_utc": "2025-12-14T00:00:00Z",
  "day_utc": "YYYY-MM-DD",
  "run_id": "urn:kfm:run:<...>",
  "outputs": [
    {
      "id": "urn:kfm:artifact:validation:metrics:<...>",
      "uri": "docs/analyses/remote-sensing/validation/reports/daily/YYYY/MM/DD/YYYY-MM-DD.summary.json",
      "sha256": "<sha256>",
      "kind": "metrics_summary"
    },
    {
      "id": "urn:kfm:artifact:validation:prov:<...>",
      "uri": "../provenance/prov_bundle.ref.json",
      "sha256": "<sha256>",
      "kind": "prov_ref"
    }
  ],
  "output_sha256": "<sha256>"
}
~~~

---

## 🧾 sampling_manifest.json (optional, when sampling is used)

If sampling is used, record:

- candidate_count + selected_count
- `frame_hash_sha256`
- selection seed or systematic rule
- strata summary (counts only; no per-sample lists when restricted)
- reference to a governed “selected list” artifact when needed

This manifest should remain small; use references for large selections.

---

## 🛡️ Governance and safe publication rules

Do NOT include:

- signed URLs, access tokens, credentials,
- internal endpoints,
- raw coordinates or per-sample lists that enable location inference,
- restricted identifiers (unless generalized and explicitly approved).

Prefer:

- STAC ids + asset keys,
- repo paths,
- content digests (`sha256:<...>`),
- PROV/OpenLineage references.

---

## 🧪 CI/CD expectations (recommended)

CI may check:

- required manifest files exist for governed runs,
- required keys exist (`run_id`, `created_utc`, `governance`, digest fields),
- stable ordering rules applied,
- hashes are present and non-empty,
- manifests do not contain forbidden fields (coords, secrets, signed URLs).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed manifests policy for daily validation bundles; defined required/optional manifests, determinism posture, safe publication rules, and recommended skeleton fields. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Bundle Manifests" src="https://img.shields.io/badge/Bundle-Manifests-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Day Bundle](../README.md) ·
[📎 Attachments](../attachments/README.md) ·
[🧾 Daily Reports](../../../../README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

