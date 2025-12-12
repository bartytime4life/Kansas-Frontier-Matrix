---
title: "🔏 Kansas Frontier Matrix — Dataset Signing, Attestation & Policy Enforcement"
path: "docs/standards/data-integrity/dataset-signing-attestation.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Security & Reliability Board"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "dataset-signing-attestation"
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

scope:
  domain: "data-integrity"
  applies_to:
    - "data/**"
    - "releases/**"
    - "mcp/**"
    - "tools/**"
    - ".github/**"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "Security & Reliability Board"

commit_sha: "<latest-commit-hash>"
doc_uuid: "urn:kfm:doc:standards:data-integrity:dataset-signing-attestation:v11.2.6"
semantic_document_id: "kfm-standard-data-integrity-dataset-signing-attestation-v11.2.6"
event_source_id: "ledger:kfm:doc:standards:data-integrity:dataset-signing-attestation:v11.2.6"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

provenance_chain:
  - "docs/standards/data-integrity/dataset-signing-attestation.md@v11.2.6"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

# 🔏 Dataset Signing, Attestation & Policy Enforcement

This standard defines **how Kansas Frontier Matrix (KFM)** cryptographically signs datasets, issues provenance attestations, enforces policy gates, and records verifiable governance evidence across the full pipeline.

It applies to **raw, processed, derived, and published artifacts**, including (but not limited to) Parquet tables, Cloud‑Optimized GeoTIFFs (COGs), NetCDF, Zarr, STAC Items, and release bundles.

---

## 📘 Overview

### Objectives (normative)

KFM data integrity controls exist to:

- ensure **immutability and tamper evidence** for scientific datasets
- bind artifacts to **reproducible provenance** (PROV‑O and supply-chain attestations)
- enforce **policy-as-code** at merge, release, and publication time
- provide **auditable governance evidence** for FAIR+CARE oversight
- support **long-term verification** independent of vendors or infrastructure

### Core guarantees (normative)

1. **Checksums are mandatory**  
   Every publishable artifact MUST have a recorded cryptographic checksum (SHA‑256).

2. **Signing is mandatory for publication**  
   Published datasets and release manifests MUST be signed.

3. **Attestation is mandatory for governed releases**  
   Release bundles MUST include a build/provenance attestation that can be verified offline.

4. **Policy gates are mandatory**  
   A dataset MUST NOT publish if it fails governance, licensing, sensitivity, provenance, schema, or security checks.

### Definitions

- **Artifact**: a concrete file or object to be published (COG, Parquet, JSON, etc.).
- **Manifest**: the canonical list of artifacts with checksums + metadata used for verification.
- **Signature**: cryptographic proof that a manifest/artifact is authentic.
- **Attestation**: structured statement about *how* an artifact was produced (build steps, inputs, environment).
- **Policy gate**: a deterministic check that must pass before merge/release/publish.

---

## 🗂 Directory Layout

~~~text
docs/
└── 📁 standards/
    ├── 📁 data-integrity/
    │   └── 📄 dataset-signing-attestation.md           🔏 This standard
    ├── 📁 governance/
    │   └── 📄 ROOT-GOVERNANCE.md
    ├── 📁 faircare/
    │   └── 📄 FAIRCARE-GUIDE.md
    └── 📁 sovereignty/
        └── 📄 INDIGENOUS-DATA-PROTECTION.md

data/
├── 📁 sources/                                         📜 Source manifests + rights
├── 📁 raw/                                             🧊 Immutable ingests
├── 📁 processed/                                       🧪 Derived artifacts (deterministic)
└── 📁 stac/                                            🛰️ Published catalogs + assets

mcp/
└── 📁 runs/
    └── 📁 <run_id>/                                    🧾 Run logs + config snapshot + validation reports

tools/
└── 📁 integrity/
    ├── 📄 manifest.py                                  🧾 Build/validate artifact manifests
    ├── 📄 sign.py                                      ✍️ Sign manifests/artifacts
    ├── 📄 verify.py                                    ✅ Verify signatures + checksums
    └── 📁 policy/                                      🧷 Policy-as-code (OPA/Conftest rules)

.github/
└── 📁 workflows/
    └── 📄 kfm-ci.yml                                   🔁 CI gates (lint, scan, validate, attest)

releases/
└── 📁 v11.2.6/
    ├── 📄 manifest.zip                                 📦 Release manifest bundle (checksums + inventory)
    ├── 📄 signature.sig                                🔏 Release signature (for manifest bundle)
    ├── 📄 slsa-attestation.json                         🧾 Build/provenance attestation
    └── 📄 sbom.spdx.json                                🧱 SBOM for release toolchain (where applicable)
~~~

---

## 🧭 Context

### Threat model (practical)

This standard exists to reduce or detect:

- accidental corruption (partial uploads, storage bitrot, truncation)
- malicious tampering (artifact replacement, manifest rewriting)
- policy drift (datasets published without required governance metadata)
- provenance ambiguity (no verifiable link between source inputs and derived outputs)

### Trust boundaries

- The **frontend/UI** MUST NOT trust unsigned artifacts.
- The **API** SHOULD refuse to serve artifacts that fail verification or policy gates.
- **Story Nodes / Focus Mode** MUST reference cataloged STAC Items with resolvable integrity evidence.

### Non-goals

- This standard does not define encryption-at-rest or secrets management.
- This standard does not supersede domain governance rules; it enforces them.

---

## 🧱 Architecture

### Architectural placement (KFM pipeline)

~~~text
Deterministic ETL
   ↓
Artifact Build (Parquet / COG / NetCDF / Zarr / JSON)
   ↓
Checksum + Manifest Materialization (SHA-256 inventory)
   ↓
Signing (dataset/release signature)
   ↓
Provenance Attestation (build/run statement)
   ↓
Policy Evaluation (policy-as-code gates)
   ↓
STAC / DCAT / PROV Catalog Emission
   ↓
Graph Ingest (Neo4j) + API Publication
   ↓
UI · Story Nodes · Focus Mode
~~~

### Canonical integrity objects

KFM uses three canonical objects to make verification portable:

1. **Artifact checksums**  
   SHA‑256 per artifact (required).

2. **Manifest bundle**  
   A single release-scoped bundle containing:
   - artifact inventory
   - checksums
   - minimal metadata to locate artifacts and validate structure

3. **Signature + attestation**  
   A signature proving authenticity, and an attestation proving build provenance.

### Key requirements (normative)

- **Algorithm**: SHA‑256 MUST be used for checksums.
- **Determinism**: A rerun with the same inputs/config/toolchain MUST produce identical manifests and checksums (except when upstream inputs change).
- **Idempotency**: Manifest creation MUST be idempotent; duplicates are forbidden.
- **Separation of concerns**: Raw ingests remain immutable; integrity metadata is additive.

### Signing model (implementation-neutral)

This standard is compatible with:

- key-based signing (maintained keys with rotation policy)
- keyless signing (identity-bound ephemeral signing with verifiable transparency logs)

Regardless of mechanism, KFM MUST be able to:

- verify signatures offline from stored evidence in `releases/**`
- map signatures to a governed identity (board/service role) via attestation metadata

### Attestation model (implementation-neutral)

Attestation MUST capture:

- inputs (source IDs + checksums)
- processing config snapshot ID + checksum
- toolchain versions
- execution environment identifier (CI runner, container digest, etc.)
- output manifest checksum

---

## 📦 Data & Metadata

### Manifest schema (minimum)

A release manifest MUST include (at minimum):

- `release_version`
- `created_at`
- `artifacts[]`:
  - `path`
  - `media_type`
  - `sha256`
  - `bytes`
  - `logical_id` (stable dataset/asset ID)
  - `provenance_ref` (PROV entity/activity reference or pointer)

### Checksums in catalogs (normative)

- STAC assets MUST include checksum metadata (either directly in `assets.*.extra_fields` or via a referenced sidecar).
- DCAT distributions SHOULD reference checksums where possible.
- PROV Entities MUST be able to link to checksum-bearing artifacts.

### Required policy metadata

Any publishable dataset MUST surface policy-critical metadata:

- `license`
- `classification`
- `sensitivity` + `sensitivity_level`
- `fair_category` + `care_label`
- `indigenous_rights_flag` (where applicable)
- `governance_ref` + `ethics_ref` + `sovereignty_policy`
- `provenance_chain` (document-level) and run lineage (dataset-level)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For governed publishing:

- Every STAC Item MUST be able to resolve:
  - the artifact(s)
  - the checksum(s)
  - the provenance reference(s)

Recommended minimum STAC integrity fields per asset:

- checksum reference (sha256 string or pointer)
- role: `data` / `metadata` / `provenance` / `manifest`
- signing reference (pointer to `releases/**` evidence for governed releases)

### DCAT

DCAT records SHOULD include:

- dataset license and publisher
- distribution checksums where feasible
- distribution links to manifest/provenance artifacts

### PROV-O

PROV MUST encode:

- `prov:Entity` for:
  - raw input artifacts
  - derived artifacts
  - manifest bundle
  - signature object
  - attestation object
- `prov:Activity` for:
  - manifest build
  - signing
  - attestation emission
  - policy evaluation
  - publish
- `prov:Agent` for:
  - signing authority (board/service identity)
  - pipeline runner identity
  - governance body references (where required)

---

## 🗺 Diagrams

~~~mermaid
flowchart TD
  A["Build artifacts<br/>(COG/Parquet/NetCDF/Zarr/STAC JSON)"] --> B["Compute SHA-256 checksums"]
  B --> C["Assemble release manifest bundle"]
  C --> D["Sign manifest bundle"]
  C --> E["Emit build/provenance attestation"]
  D --> F["Policy evaluation gates"]
  E --> F
  F -->|pass| G["Publish catalogs + artifacts"]
  F -->|fail| H["Block release/publish + record failure report"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Story Node evidence rule (normative)

Story Nodes MUST reference:

- STAC Items that resolve to artifacts whose checksums are present in a signed manifest (for governed releases), and
- provenance references sufficient to trace derived artifacts back to sources and processing activities.

### Focus Mode guardrails (normative)

Focus Mode MAY:

- summarize integrity evidence
- surface verification status
- trace provenance

Focus Mode MUST NOT:

- invent verification outcomes
- claim an artifact is “trusted” without successful verification
- bypass sovereignty or sensitivity policies

---

## 🧪 Validation & CI/CD

### Required gates (normative)

Before publish:

- `schema-lint` for dataset schemas and manifests
- `stac-validate` for STAC Items/Collections
- `prov-validate` for PROV graphs (no dangling refs)
- `secret-scan` and `pii-scan` for repo outputs
- `policy-check` (OPA/Conftest or equivalent) enforcing:
  - license presence and compatibility
  - classification/sensitivity requirements
  - sovereignty constraints
  - provenance completeness requirements
- `integrity-verify` verifying:
  - manifest checksums match artifacts
  - signatures verify against stored evidence

### Failure handling (normative)

- A policy failure MUST block publish (and SHOULD block merge for governed datasets).
- Failed runs MUST record:
  - config snapshot
  - failed gate(s)
  - artifact inventory present at time of failure
  - remediation guidance (non-sensitive)

---

## ⚖ FAIR+CARE & Governance

### Governance requirements (normative)

- Signing authority is delegated by governance and MUST be auditable.
- Any exception to signing/attestation requirements MUST be explicitly recorded with rationale and scope.

### Sovereignty and harm minimization

- Integrity evidence MUST NOT leak sensitive locations or restricted overlays.
- Where sovereignty constraints apply, manifests and catalogs MUST support:
  - redaction/masking policies
  - controlled distributions
  - access-gated publication while preserving internal verification

Binding references:

- Governance: `governance_ref`
- Ethics: `ethics_ref`
- Sovereignty: `sovereignty_policy`

---

## 🕰 Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-12 | KFM‑MDP alignment: approved H2 headings and ordering, tilde‑fenced diagrams/blocks, required front‑matter governance + AI limits, and a portable manifest/sign/attest/policy architecture for governed releases. |

---

<div align="center">

[📘 Docs Root](../../README.md) ·
[📑 Standards Index](../README.md) ·
[⚖️ Governance Charter](../governance/ROOT-GOVERNANCE.md) ·
[🧬 FAIR+CARE Guide](../faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix · CC‑BY 4.0

</div>
