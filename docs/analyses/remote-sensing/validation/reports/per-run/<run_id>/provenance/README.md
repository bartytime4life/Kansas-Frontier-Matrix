---
title: "🧬 KFM — Per-Run Validation Provenance (PROV-O · OpenLineage · Ref Bundles)"
path: "docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/provenance/README.md"

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

intent: "remote-sensing-validation-per-run-provenance"
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

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:per-run:<run_id>:provenance:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-per-run-provenance-<run_id>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/provenance/README.md"
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

# 🧬 **KFM — Per‑Run Validation Provenance**
`docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/provenance/README.md`

**Purpose**  
Define how a single validation run (`<run_id>`) references provenance artifacts:
**PROV‑O JSON‑LD**, **OpenLineage events**, and related digests/identifiers—kept **small, deterministic, and governance-safe**.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />
<img alt="Reports Per-Run" src="https://img.shields.io/badge/Reports-Per--Run-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder holds **provenance references** for a single validation run (`<run_id>`).

The intent is to keep the run bundle:

- **auditable** (stable ids + hashes + pointers),
- **deterministic** (reproducible link structure),
- **governance-safe** (no sensitive or restricted detail),
- **small** (no large provenance dumps committed into docs).

Normative provenance posture lives in:

- `docs/analyses/remote-sensing/validation/methods/provenance/README.md`

---

## 🆔 What is `<run_id>`?

`<run_id>` MUST identify one validation execution.

Recommended forms:

- `urn:kfm:run:<...>` (preferred for governed runs)
- `urn:uuid:<...>` (acceptable if policy permits)

`<run_id>` SHOULD be reproducible from run context (e.g., `frame_hash + config_hash`) and MUST NOT be derived from wall-clock time alone.

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/per-run/<run_id>/provenance/
├── 📄 README.md                                              — This policy/index
├── 🧾 prov_bundle.ref.json                                   — Recommended: pointer to PROV-O JSON-LD bundle (id + digest)
├── 🧾 openlineage.ref.json                                   — Optional: pointer to OpenLineage event set (run id + digest)
├── 🧾 provenance_index.json                                  — Optional: small registry of provenance pointers for the run
└── 🧾 attestations.ref.json                                  — Optional: pointers to attestations (SBOM/SLSA) when required by policy
~~~

> These files are pointers, not payloads. If a provenance artifact is large, store it as a governed asset and reference it here.

---

## ✅ What belongs here

Keep provenance content in this folder to **references and checksums**:

- stable ids:
  - `run_id`
  - `algorithm_id`(s)
  - related STAC item ids for run outputs (when used)
- digests:
  - `sha256` for referenced provenance bundles and manifests
- pointers:
  - repo paths to small local artifacts
  - governed asset identifiers (STAC asset keys / URNs)
- high-level governance posture:
  - `care_gate_status`
  - `sovereignty_gate`
  - redaction summary counts and reason codes only

---

## ⛔ What must NOT be stored here

Do NOT commit any of the following in this folder:

- large PROV-O JSON-LD payloads (unless explicitly tiny and approved),
- raw coordinate lists, site identifiers, or “how to locate” details,
- signed URLs, tokens, credentials, internal endpoints, secrets,
- per-sample lists from restricted collections,
- bulky run logs or payload dumps.

If deeper detail is required:

- store it as a governed artifact and link via STAC assets and PROV entity ids,
- keep only digests and stable references here.

---

## 🧾 Recommended pointer shapes (illustrative)

### `prov_bundle.ref.json`

~~~json
{
  "ref_kind": "prov_bundle",
  "ref_version": "v1",
  "run_id": "urn:kfm:run:<run_id>",
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

### `openlineage.ref.json`

~~~json
{
  "ref_kind": "openlineage",
  "ref_version": "v1",
  "run_id": "urn:kfm:run:<run_id>",
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

- the run’s `run.summary.json` links to this folder (refs),
- the run’s STAC Item (when used) includes assets for:
  - run summary,
  - provenance bundle,
  - config snapshot and input pack manifest,
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
  - the `run_id` in `run.summary.json` MUST match the `run_id` in these provenance refs,
  - digest fields in manifests SHOULD match digest fields referenced here.

If provenance is required by contract and missing:

- record a deterministic reason code (e.g., `PROVENANCE_INCOMPLETE`) in `run.summary.json`,
- treat as `fail` or `warn` per governed gate mode.

---

## 🛡️ FAIR+CARE and sovereignty posture

This folder is public-facing by default. Therefore:

- never include raw coordinates or restricted identifiers,
- keep spatial scope generalized (region/coarse grid) if included at all,
- when redaction is applied:
  - record only counts and reason codes,
  - link to governed artifacts rather than embedding details.

---

## 🧪 CI/CD expectations (recommended)

CI may validate:

- required pointer files exist for governed runs (policy-dependent),
- required fields present (`run_id`, `sha256`, `storage_ref`, governance posture),
- cross-link consistency:
  - `run_id` matches run summary and manifests,
  - STAC item id / asset keys are present in refs (when STAC is used),
- leakage scans:
  - no coordinates,
  - no secrets,
  - no signed URLs.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed provenance pointer policy for per-run validation bundles; defined allowed reference files, determinism rules, STAC linkage patterns, and governance-safe publication posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />

[⬅ Run Bundle](../README.md) ·
[🧾 Manifests](../manifests/README.md) ·
[📎 Attachments](../attachments/README.md) ·
[🧾 Per-Run Reports](../../README.md) ·
[📅 Daily Reports](../../daily/README.md) ·
[🧩 Methods](../../../methods/README.md) ·
[🧾 Provenance Methods](../../../methods/provenance/README.md) ·
[🏛️ Governance Charter](../../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

