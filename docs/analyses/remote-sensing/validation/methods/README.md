---
title: "🧩 KFM — Remote Sensing Validation Methods (Metrics · Sampling · Algorithms · Provenance)"
path: "docs/analyses/remote-sensing/validation/methods/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Reference"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-methods"
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

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.6/remote-sensing-validation-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/analyses-remote-sensing-validation-methods-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:methods:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-methods"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/methods/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧩 **KFM — Remote Sensing Validation Methods**
`docs/analyses/remote-sensing/validation/methods/README.md`

**Purpose**  
Define the governed validation methods used to evaluate remote-sensing products in KFM:
**metrics**, **sampling**, **algorithms**, and **provenance** conventions that support deterministic QA and FAIR+CARE-safe reporting.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="MCP-DL v6.3" src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

This directory is the **documentation-first, governed reference** for how KFM validates remote-sensing outputs.

It defines:

- **what** is measured (metric definitions, units, aggregation, thresholds),
- **how** evaluation scope is selected (sampling units, deterministic frames, stratification),
- **how** metrics are computed (algorithm families and required behaviors),
- **how** results remain audit-ready (PROV-O/OpenLineage, STAC/DCAT linkage, manifests, checksums),
- **how** governance is enforced (FAIR+CARE posture, sovereignty gates, redaction rules).

Implementations may live in `src/`, `tools/`, or pipeline runners; this documentation is the normative contract.

---

## 🧭 What “validation” means in KFM

Validation is the governed process that:

- compares products to references where available (or to baselines / prior releases),
- tests internal consistency (geometry, schema, temporal cadence, masks),
- produces machine-checkable outcomes used in CI/CD and release promotion:
  - `pass`, `warn`, or `fail`,
  - deterministic reason codes for non-pass outcomes,
  - provenance bundles that explain “what changed” and “why”.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/methods/            — Remote-sensing validation method docs (this directory)
├── 📄 README.md                                              — This index (you are here)
├── 📁 metrics/                                               — Metric definitions, threshold semantics, templates
├── 📁 sampling/                                              — Deterministic frames, stratification, sample manifests
├── 📁 algorithms/                                            — Algorithm family definitions + output contracts
└── 📁 provenance/                                            — PROV-O/OpenLineage posture + linkage templates
~~~

---

## 🧱 Method pillars (governed)

### 1) Metrics

Metrics are defined as stable, comparable quantities with explicit:

- units,
- directionality (higher/lower/target is better),
- aggregation level(s),
- mask and eligibility posture,
- threshold semantics (warn/fail),
- determinism requirements (ordering, seed behavior, quantiles/bins when used).

See:

- `metrics/README.md`
- `metrics/templates/README.md`

### 2) Sampling

Sampling is allowed when full evaluation is too expensive, but it must be:

- deterministic (stable candidate enumeration + pinned seed / systematic rules),
- auditable (frame hash, selection hash, sample manifest),
- governance-safe (no sensitive leakage via small AOIs or per-sample disclosure),
- comparable across runs and releases.

See:

- `sampling/README.md`
- `sampling/templates/README.md`

### 3) Algorithms

Algorithm families define how metrics are computed for different product types:

- radiometry / continuous fields,
- classification / masks,
- geometry / spatial integrity,
- temporal consistency,
- drift (release-to-release comparison).

Each family must emit outputs in a standard governed shape (metrics + thresholds + reason codes + refs).

See:

- `algorithms/README.md`

### 4) Provenance

Every governed validation run must be traceable to:

- exact input artifacts (immutable URIs + digests),
- exact config/thresholds/masks (config snapshot + digests),
- algorithm version,
- governance posture (CARE and sovereignty gates),
- output artifacts (metrics summary + optional detailed reports).

See:

- `provenance/README.md`
- `provenance/templates/README.md`

---

## 🛰️ Reference data posture (governed)

Validation may use any governed reference source that is:

- licensed appropriately,
- provenance-captured,
- compatible with sovereignty and sensitivity labels.

Examples of reference sources (availability varies by product and governance):

- land-cover references (e.g., NLCD-like products),
- in-situ stations for continuous variables (e.g., weather/flux towers),
- baselines from prior KFM releases,
- cross-sensor overlap windows (for transition alignment).

Rules:

- reference usage must be explicit in provenance (`prov:used`),
- any restricted references must remain gated and redacted in public reports.

---

## 🔬 Quality control workflow (high level)

~~~mermaid
flowchart TD
  A["Enumerate scope (items/tiles/time window)"] --> B["Apply governance eligibility + masks (pinned)"]
  B --> C["Sampling (optional): frame hash + selection manifest"]
  C --> D["Compute metrics (deterministic algorithms)"]
  D --> E["Evaluate thresholds (policy)"]
  E --> F["Emit artifacts: metrics summary + optional details"]
  F --> G["Emit provenance: PROV-O/OpenLineage + manifests + checksums"]
  G --> H["Link to catalogs: STAC/DCAT + rollups (per-run/daily/release)"]
~~~

---

## 🚦 Outcomes, thresholds, and gates

Validation outputs MUST include:

- `outcome`: `pass | warn | fail`
- `reason_codes`: stable, deterministic identifiers for:
  - threshold breaches,
  - missing required inputs (fail-closed),
  - insufficient support,
  - governance denial/redaction actions.

Thresholds:

- must be pinned and versioned,
- must identify metric ids and operators clearly,
- must state severity (`warn` or `fail`).

See:

- `metrics/README.md`
- `metrics/templates/README.md`

---

## 🛡️ FAIR+CARE and sovereignty enforcement

Validation can leak sensitive information through:

- reporting at overly fine spatial partitions,
- revealing rare-class examples,
- embedding coordinates or per-sample identifiers,
- including signed URLs, tokens, or internal endpoints.

Rules:

- reports MUST obey the most restrictive label on inputs,
- restricted collections must be:
  - excluded, redacted, or denied per policy,
  - recorded in `redaction_summary` and provenance,
- public artifacts must use generalized spatial scope (region/coarse grid),
- fail closed when governance posture is unclear.

---

## 🧪 CI/CD integration (expectations)

Validation documentation and outputs are designed to support CI checks including:

- schema validation for metric/provenance payloads (when schemas exist),
- reproducibility checks for sampling manifests,
- threshold gate enforcement (pass/warn/fail),
- leakage scans (no coordinates, no secrets, no signed URLs),
- provenance completeness checks (inputs/config/outputs all linked).

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Upgraded methods index to KFM-MDP v11.2.6; aligned directory structure (metrics/sampling/algorithms/provenance), clarified determinism + governance posture, and standardized outcome/gate vocabulary. |
| v10.2.2 | 2025-11-12 | Prior methods overview and examples; superseded by the governed v11 structure and submodule READMEs. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

[🧮 Algorithms](algorithms/README.md) ·
[📐 Metrics](metrics/README.md) ·
[🎯 Sampling](sampling/README.md) ·
[🧾 Provenance](provenance/README.md) ·
[🧾 Reports](../reports/README.md) ·
[🏛️ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
