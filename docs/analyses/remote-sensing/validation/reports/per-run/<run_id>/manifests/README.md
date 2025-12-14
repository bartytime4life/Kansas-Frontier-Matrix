---
title: "🧾 KFM — Per-Run Validation Manifests (Input Pack · Config Snapshot · Output Manifest)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/manifests/README.md"

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

intent: "remote-sensing-validation-per-run-manifests"
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

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:manifests:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-manifests-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/manifests/README.md"
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

# 🧾 **KFM — Per‑Run Validation Manifests**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/manifests/README.md`

**Purpose**  
This folder defines the **deterministic manifests** for a single validation run (`<run_id>`):
what inputs were evaluated, what configuration was applied, and what outputs were produced—recorded as small, stable, governance-safe JSON documents.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Bundle Manifests" src="https://img.shields.io/badge/Bundle-Manifests-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Manifests are the run’s **immutable “truth record”** that make replay and governance review possible.

They exist so we can always answer, for `<run_id>`:

- exactly which inputs were validated (with digests),
- exactly which thresholds, masks, sampling, and numeric policies were applied (pinned snapshot),
- exactly which outputs (summaries/evidence pointers) were produced (with digests),
- whether the run is reproducible (determinism posture).

This directory MUST remain safe for in-repo publication:

- do not embed large payloads,
- do not embed sensitive coordinates or restricted identifiers,
- do not include signed URLs, secrets, or internal endpoints.

Use **references and hashes** instead.

---

## 🆔 `<run_id>` expectations

`<run_id>` SHOULD be a stable identifier (prefer URNs):

- `urn:kfm:run:<...>` (preferred)
- `urn:uuid:<...>` (acceptable if policy permits)

`<run_id>` SHOULD be reproducible from run context (e.g., `frame_hash + config_hash`) and MUST NOT rely on wall-clock time alone.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/manifests/
├── 📄 README.md                                               — This policy/index
├── 🧾 input_pack_manifest.json                                 — Recommended: immutable inputs evaluated (ids + digests or refs)
├── 🧾 config_snapshot.json                                     — Recommended: pinned thresholds/masks/sampling/numeric policy
├── 🧾 output_manifest.json                                     — Recommended: outputs produced (ids + digests or refs)
├── 🧾 sampling_manifest.json                                   — Optional: frame/selection details (if sampling used)
└── 🧾 checksums.json                                           — Optional: convenience rollup of digest fields
~~~

Notes:

- Keep manifests small. If an enumeration is large (e.g., millions of tiles), store the full list as a governed artifact and reference it here by id/path + digest.
- Prefer consistent file names across runs so tooling can locate them without custom logic.

---

## ✅ Required properties (manifest-wide)

Every manifest file SHOULD include:

- `manifest_kind`: `input_pack|config_snapshot|output|sampling|checksums`
- `manifest_version`: e.g., `"v1"`
- `created_utc`: ISO8601 UTC timestamp
- `run_id`: stable run identifier (must match the run bundle)
- `time_window_utc`: `{start, end}` where applicable
- `algorithm_ids`: list (when applicable)
- `governance` posture:
  - `care_gate_status`: `allow|redact|deny`
  - `sovereignty_gate`: `clear|restricted|conflict|unknown`
  - `redaction_summary`: counts + reason codes only

If a key is not applicable, include it as `null` rather than omitting it.

---

## 🎯 Determinism rules (non-negotiable)

Manifests MUST support deterministic replay:

- Stable ordering:
  - arrays MUST be sorted deterministically (lexicographic by `id` unless a governed alternative is documented).
- Stable hashing:
  - digests MUST be computed over immutable bytes or a canonical representation.
- Pinned configuration:
  - thresholds/masks/sampling/numeric policy MUST be present or referenced by digest.
- No clock-entropy identifiers:
  - do not derive `run_id` from wall-clock alone.

If determinism is not achieved, record a deterministic reason code in the run summary and treat as `warn`/`fail` per policy.

---

## 🧾 input_pack_manifest.json (recommended)

This manifest captures **what was evaluated** (inputs + scope).

Include:

- run scope:
  - time window (UTC),
  - generalized spatial scope when required (region/coarse grid),
  - evaluation unit (`item|tile|time_step|item_tile`)
- input references:
  - STAC Item ids, dataset URNs, artifact URNs,
  - repo paths when applicable,
  - digests (`sha256` preferred),
  - role: `primary|reference|baseline|auxiliary`

Illustrative skeleton:

~~~json
{
  "manifest_kind": "input_pack",
  "manifest_version": "v1",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "run_id": "urn:kfm:run:<run_id>",
  "time_window_utc": {
    "start": "YYYY-MM-DDTHH:MM:SSZ",
    "end": "YYYY-MM-DDTHH:MM:SSZ"
  },
  "scope": {
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

This manifest captures **the exact validation configuration** used:

- algorithm ids and versions
- metric definitions and threshold versions
- mask policy references and digests
- sampling policy (mode/unit/seed/systematic rule id) when used
- numeric policy:
  - dtype expectations,
  - NaN behavior,
  - rounding rules,
  - quantile method/bins if relevant

Illustrative skeleton:

~~~json
{
  "manifest_kind": "config_snapshot",
  "manifest_version": "v1",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "run_id": "urn:kfm:run:<run_id>",
  "algorithms": [
    {
      "algorithm_id": "kfm:rs:validate:<family>:<name>:v1",
      "impl_ref": "src/<...>",
      "impl_sha256": "<sha256>"
    }
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
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "config_snapshot_sha256": "<sha256>"
}
~~~

---

## 🧾 output_manifest.json (recommended)

This manifest captures **what was produced** (summaries + evidence pointers), with digests.

Outputs SHOULD be references to:

- `run.summary.json` and optional `run.summary.md`
- STAC item ids for produced evidence outputs
- provenance refs (PROV/OpenLineage pointers)
- optional governed artifacts stored elsewhere (referenced by id/path + digest)

Illustrative skeleton:

~~~json
{
  "manifest_kind": "output",
  "manifest_version": "v1",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "run_id": "urn:kfm:run:<run_id>",
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "outputs": [
    {
      "id": "urn:kfm:artifact:validation:summary:<...>",
      "uri": "../run.summary.json",
      "sha256": "<sha256>",
      "kind": "run_summary_json"
    },
    {
      "id": "urn:kfm:stac:item:<...>",
      "uri": "data/stac/<...>.json",
      "sha256": "<sha256>",
      "kind": "stac_item"
    }
  ],
  "output_sha256": "<sha256>"
}
~~~

---

## 🧾 sampling_manifest.json (optional, when sampling is used)

If sampling is used, record:

- `candidate_count` and `selected_count`
- `frame_hash_sha256`
- selection seed or systematic rule id
- strata summary (counts only; no per-sample lists when restricted)
- reference to a governed “selected set” artifact when needed

Keep this manifest small. Use a pointer to a governed selection list if the selection set is large.

---

## 🛡️ Governance and safe publication rules

Do NOT include in manifests:

- signed URLs, access tokens, credentials,
- internal endpoints,
- raw coordinates or per-sample lists that enable location inference,
- restricted identifiers (unless explicitly generalized and approved).

Prefer:

- STAC ids + asset keys,
- repo paths,
- content digests (`sha256:<...>`),
- PROV/OpenLineage references.

---

## 🧪 CI/CD expectations (recommended)

CI MAY validate per-run manifests by checking:

- required files exist for governed runs (policy-dependent),
- required keys exist (`run_id`, `created_utc`, `governance`, digest fields),
- stable ordering rules applied (where applicable),
- hashes are present and non-empty,
- no leakage fields (coords, secrets, signed URLs).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed manifests policy for per-run validation bundles; defined recommended manifest set, determinism posture, safe publication rules, and CI expectations. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Bundle Manifests" src="https://img.shields.io/badge/Bundle-Manifests-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Run Bundle](../README.md) ·
[📎 Attachments](../attachments/README.md) ·
[🧬 Provenance](../provenance/README.md) ·
[🧾 Per-Run Reports](../../README.md) ·
[🧾 Reports Index](../../../README.md) ·
[📅 Daily Reports](../../../daily/README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

