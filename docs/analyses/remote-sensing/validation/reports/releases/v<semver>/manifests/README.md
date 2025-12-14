---
title: "🧾 KFM — Release Validation Manifests (v<semver>) · Inputs · Config · Outputs · Digests"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/manifests/README.md"

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

intent: "remote-sensing-validation-release-manifests"
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

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:manifests:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-manifests-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/manifests/README.md"
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

# 🧾 **KFM — Release Validation Manifests**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/manifests/README.md`

**Purpose**  
This folder contains the **deterministic manifest set** that makes the release validation report for **v<semver>** auditable and replayable:
what inputs were validated, what configs were pinned, what outputs were produced, and the digests that bind them together.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Manifests Digests" src="https://img.shields.io/badge/Manifests-Digests-informational" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Manifests are the **release-grade contract** for reproducibility. They are used to:

- prove exactly which input assets (and which versions) were validated,
- pin the validation configuration (thresholds, sampling, redaction posture),
- record deterministic outputs (summaries, evidence exhibits, references),
- support safe rollback and audit without relying on ephemeral infrastructure.

Manifests in this folder MUST remain:

- **deterministic** (stable ordering, stable serialization, stable digests),
- **governance-safe** (no signed URLs, secrets, or sensitive coordinates),
- **reviewable** (small, readable, diff-friendly).

---

## 🗂️ Directory Layout (recommended)

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/manifests/
├── 📄 README.md                                 — This policy/index
├── 🧾 input_pack.manifest.json                  — Required: declared inputs (refs + digests + labels)
├── 🧾 config_snapshot.json                      — Required: pinned validation config (thresholds, sampling, redaction)
├── 🧾 output_manifest.json                      — Required: declared outputs (refs + digests)
├── 🧾 environment.manifest.json                 — Optional: toolchain/container/runtime fingerprints (no secrets)
├── 🧾 evidence.manifest.json                    — Optional: evidence file inventory (may duplicate evidence index)
└── 🧾 manifests.sha256                          — Recommended: sha256 sums for all manifest files in this folder
~~~

Notes:

- Keep filenames stable across releases.
- Large payload artifacts SHOULD be referenced by stable id + digest, not copied into repo.

---

## ✅ Required manifests (minimum)

### 1) `input_pack.manifest.json` (required)

Declares the **input universe** that the release report is allowed to talk about.

Minimum recommended fields:

- release identifiers:
  - `release_version`, `release_commit_sha`
- dataset references:
  - KFM dataset ids,
  - STAC Collection/Item ids where applicable,
  - DCAT dataset/distribution ids where applicable
- input artifacts:
  - stable references (repo paths and/or governed URIs),
  - `sha256` digests,
  - governance labels (classification, CARE/sovereignty gates)

Rules:

- References MUST be stable (no signed URLs).
- Governance labels MUST be included when known; if unknown, fail closed upstream.

### 2) `config_snapshot.json` (required)

Pins the **validation behavior** so reruns produce the same results.

Must include (as applicable):

- threshold set id / threshold values and rounding policy
- sampling posture:
  - mode (`full|fixed_set|random|stratified|systematic`)
  - seed (if applicable)
  - sample frame description
- determinism controls:
  - stable sort keys,
  - numeric dtype/precision policy,
  - bin edges for histograms,
  - map aggregation scope (region/H3 resolution)
- governance posture:
  - CARE/sovereignty gate outcomes,
  - redaction rules and suppression thresholds (minimum group sizes)

### 3) `output_manifest.json` (required)

Declares what the release validation produced.

Minimum recommended fields:

- `release.summary.json` reference and digest
- references to:
  - evidence index files (`evidence/release_evidence_index.json` and `.md`),
  - provenance pointers (`provenance/` bundle references),
  - optional tables/plots/maps in repo (by relative path + digest)
- any external governed outputs referenced via STAC (id + digest)

---

## ➕ Optional manifests (recommended when available)

### `environment.manifest.json` (optional)

Used to fingerprint the runtime environment without leaking secrets.

Recommended fields:

- container image digests (not tags)
- toolchain versions (python/node, key libs)
- OS/arch
- build/run identifiers (non-secret)
- telemetry pointers (if produced elsewhere)

### `evidence.manifest.json` (optional)

A consolidated evidence inventory that can mirror:

- `../evidence/release_evidence_index.json`

Keep it small. Prefer referencing the evidence index as the authoritative list.

---

## 🎯 Determinism requirements (non-negotiable)

All manifest files MUST be reproducible:

- stable ordering for arrays and keys (define and follow a canonical order),
- stable numeric formatting (avoid float noise; apply explicit rounding policy),
- stable timestamps:
  - include `created_utc` only if required,
  - do not include machine-local timestamps, hostnames, temp paths, or random ids,
- stable serialization:
  - use UTF-8,
  - no trailing whitespace variance,
  - no environment-specific fields.

Digest rules:

- prefer `sha256` for all digests,
- digests MUST refer to the exact bytes of the referenced artifact.

---

## 🛡️ Governance and leakage rules (mandatory)

Manifests MUST NOT contain:

- signed URLs or access tokens,
- secrets, credentials, internal endpoints,
- precise coordinates or restricted location descriptors,
- restricted dataset identifiers that are not allowed for the repo’s visibility.

If any input is sovereignty-restricted or governance is unclear:

- manifests MUST record gate outcomes and redaction posture,
- downstream publication should remain aggregated and generalized.

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- required manifests exist:
  - `input_pack.manifest.json`
  - `config_snapshot.json`
  - `output_manifest.json`
- schemas (if/when defined) validate,
- digests are present and syntactically valid,
- referenced repo files exist and match their recorded `sha256`,
- no forbidden content patterns:
  - coordinates,
  - secrets,
  - signed URLs.

Promotion should be blocked if:

- required manifests are missing,
- digests do not match,
- governance posture is missing or inconsistent.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release validation manifests; defined required manifests, determinism posture, governance-safe content rules, and CI expectations for promotion. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Manifests Digests" src="https://img.shields.io/badge/Manifests-Digests-informational" />

[⬅ Release Report](../README.md) ·
[📦 Evidence](../evidence/README.md) ·
[🧬 Provenance](../provenance/README.md) ·
[🏷 Releases Index](../../README.md) ·
[🧾 Reports Index](../../../README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

