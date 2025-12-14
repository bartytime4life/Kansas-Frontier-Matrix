---
title: "🧩 KFM — Validation Provenance Templates (PROV-O · OpenLineage · Manifests · Linkage Blocks)"
path: "docs/analyses/remote-sensing/validation/methods/provenance/templates/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Templates"
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

intent: "remote-sensing-validation-provenance-templates"
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

governance_ref: "../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:provenance:templates:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-provenance-templates"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/provenance/templates/README.md"
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

# 🧩 **KFM — Validation Provenance Templates**
`docs/analyses/remote-sensing/validation/methods/provenance/templates/README.md`

**Purpose**  
Provide governed templates for provenance artifacts emitted by remote-sensing validation:
**PROV‑O JSON‑LD**, **OpenLineage events**, and deterministic **input/output manifests** with checksums—plus linkage blocks for **STAC/DCAT** references.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This folder contains **templates** used to standardize provenance emission for validation runs:

- deterministic run identifiers,
- immutable input/output manifests (URIs + digests),
- reproducible config snapshots (pinned thresholds, mask policies, seeds),
- PROV‑O bundles aligned to `KFM-PROV v11`,
- OpenLineage events for ops-level job/run tracking,
- safe linkage blocks for STAC/DCAT references.

These templates exist to prevent drift and to support:

- per-run provenance bundles,
- daily and release rollups,
- CI policy gates (fail-closed when required).

Normative provenance posture is defined in:

- `../README.md`

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/provenance/
└── 📁 templates/                                              — Templates and examples (this directory)
    ├── 📄 README.md                                           — This index
    ├── 🧾 prov_bundle.template.jsonld                          — Recommended: minimal PROV-O JSON-LD bundle
    ├── 🧾 openlineage_events.template.json                     — Recommended: start/complete/fail event skeletons
    ├── 🧾 input_pack_manifest.template.json                    — Recommended: immutable input URIs + checksums
    ├── 🧾 output_manifest.template.json                        — Recommended: output URIs + checksums
    ├── 🧾 config_snapshot.template.json                        — Recommended: pinned params/thresholds/masks/seeds
    ├── 🧾 linkage_block.template.json                          — Optional: STAC/DCAT/PROV reference block
    ├── 🧾 governance_block.template.json                       — Optional: CARE/sovereignty posture + redaction summary
    ├── 🧾 checksums_block.template.json                        — Optional: standard checksum/digest fields
    ├── 🧾 example_prov.minimal.jsonld                          — Optional: tiny golden PROV bundle (small)
    ├── 🧾 example_openlineage.minimal.json                     — Optional: tiny golden OpenLineage event set (small)
    └── 🧾 example_manifests.minimal.json                       — Optional: tiny golden input/output manifests (small)
~~~

> Filenames above are recommended conventions. Add only what is used by CI validators and report writers, and keep examples small.

---

## 🧾 Template inventory (recommended)

### 1) `prov_bundle.template.jsonld` (PROV‑O)

The PROV template SHOULD include, at minimum:

- `prov:Entity`:
  - input pack (manifest)
  - config snapshot
  - metrics summary output
- `prov:Activity`:
  - validation activity (algorithm run)
- `prov:Agent`:
  - pipeline runner / CI validator
- relations:
  - `prov:used`
  - `prov:wasGeneratedBy`
  - `prov:wasAssociatedWith`
  - `prov:wasDerivedFrom` (when applicable)

Recommended KFM extensions (illustrative field names; keep stable):

- `kfm:run_id`
- `kfm:algorithm_id`
- `kfm:care_gate_status`
- `kfm:sovereignty_gate`
- `kfm:input_pack_sha256`
- `kfm:config_snapshot_sha256`

### 2) `openlineage_events.template.json` (OpenLineage)

The OpenLineage template SHOULD define:

- `job`:
  - stable name and namespace
- `run`:
  - stable `runId` (mapped to KFM `run_id` or cross-linked)
- `inputs` and `outputs`:
  - dataset references (URIs) and checksums when available
- lifecycle:
  - start event
  - complete event
  - fail event

When both PROV and OpenLineage are used:

- include `kfm:run_id` in OpenLineage `run.facets` (or equivalent),
- include `kfm:openlineage_run_id` in PROV `Activity` (or equivalent).

### 3) `input_pack_manifest.template.json`

The input pack manifest is the **immutable “what was evaluated”** record.

It SHOULD include:

- enumeration rules (stable ordering),
- list of inputs:
  - STAC Item IDs (or URNs)
  - asset identifiers (by key) and immutable hrefs/URIs
  - digests (preferred: sha256)
- scope summary:
  - time window
  - generalized spatial scope (region/coarse grid where required)
- baseline references (if used)

### 4) `output_manifest.template.json`

The output manifest is the **immutable “what was produced”** record.

It SHOULD include:

- metrics summary URI + sha256
- provenance bundle URI + sha256
- optional detailed report artifact URI + sha256
- any rollup contribution record URI + sha256

### 5) `config_snapshot.template.json`

The config snapshot is the **determinism anchor**.

It SHOULD include:

- algorithm id and version
- parameter set (pinned)
- thresholds (pinned)
- mask policy reference (hash/ref)
- sampling policy (including seed and sample-frame hash if sampling)
- numeric policy:
  - dtype expectations
  - NaN handling rules
  - quantile method (if used)
  - histogram bins reference (if used)

---

## 🧷 Deterministic identifiers (required)

Templates MUST support deterministic identifiers.

### `run_id` (recommended)

A stable `run_id` SHOULD be derived from immutable inputs and pinned config:

- `scope_hash = sha256(sorted(input_ids + input_digests) + config_snapshot_sha256 + mask_policy_hash)`
- `run_id = urn:kfm:run:rs-validation:<algorithm_family>:<yyyy-mm-ddThh:mm:ssZ>:<scope_hash_prefix>`

Rules:

- enumeration and sorting MUST be stable before hashing,
- the hashing method MUST be fixed (sha256),
- do not include non-deterministic fields (hostnames, random UUIDs) in the scope hash.

### Entity IDs (recommended)

- inputs: use canonical STAC IDs / URNs whenever possible
- derived outputs: use `urn:kfm:artifact:validation:<family>:<run_id>:<name>`
- activities: use `urn:kfm:activity:validation:<algorithm_id>:<run_id>`

---

## 🚦 Fail-closed posture (policy default)

Templates SHOULD assume `fail_closed` for governed validation unless explicitly overridden in policy.

Fail-closed triggers (non-exhaustive):

- missing input digests (where required by contract),
- missing config snapshot / thresholds,
- missing governance posture (CARE/sovereignty),
- missing PROV/OpenLineage artifacts when mandated by pipeline contract.

---

## 🛡️ FAIR+CARE and sovereignty posture

Templates and examples in this folder MUST remain safe for in-repo publication:

- no raw coordinates,
- no restricted identifiers that expose sensitive collections,
- no signed URLs, tokens, or internal endpoints.

If redaction is required:

- record only generalized spatial scope,
- set `care_gate_status = redact|deny`,
- include `redaction_summary` counts and reason codes,
- reference restricted traces through governed channels (do not embed them here).

---

## 🧪 CI/CD usage (recommended)

These templates support CI validation by enabling checks such as:

- required fields present (run_id, algorithm_id, timestamps, governance posture),
- checksums present for required inputs/outputs,
- no forbidden fields (coordinates, secrets, signed URLs),
- stable ordering rules applied (lexicographic ordering for arrays before hashing),
- cross-link integrity:
  - PROV references match manifest digests,
  - OpenLineage runId cross-links match KFM run_id (when both are used).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed provenance template pack for remote-sensing validation; defined PROV-O/OpenLineage templates, deterministic run/entity identifiers, manifest and config snapshot templates, and governance-safe publication posture. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="KFM-PROV v11" src="https://img.shields.io/badge/KFM--PROV-v11-blue" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[⬅ Provenance](../README.md) ·
[⬅ Methods](../../README.md) ·
[🧾 Reports](../../../reports/README.md) ·
[🏛️ Governance Charter](../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

