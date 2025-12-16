---
title: "🔐 Kansas Frontier Matrix — Sigstore, Cosign v3 & Verifiable Artifact Governance"
path: "docs/security/supply-chain/sigstore-cosign-v3/README.md"
version: "v11.2.6"
last_updated: "2025-12-15"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security & FAIR+CARE Council Oversight"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Architecture & Policy Guide"
intent: "artifact-signing-and-attestation"

license: "CC-BY 4.0"
jurisdiction: "United States · Kansas"
classification: "Public Document"
sensitivity: "General"
sensitivity_level: "Low"
public_exposure_risk: "Low"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/security-supply-chain-v3.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../../../.github/SECURITY.md"

doc_uuid: "urn:kfm:doc:security-supply-chain-sigstore-cosign-v3-readme-v11.2.6"
semantic_document_id: "kfm-doc-security-supply-chain-sigstore-cosign-v3"
event_source_id: "ledger:docs/security/supply-chain/sigstore-cosign-v3/README.md"
immutability_status: "version-pinned"

ai_training_allowed: false
ai_training_guidance: "Do not use supply-chain logs, telemetry, or verification evidence as model training data."
ai_outputs_require_explainability: true
ai_outputs_require_bias_audit: false

machine_readable: true
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

header_profile: "standard"
footer_profile: "kfm_footer_v1"
diagram_profiles:
  - "mermaid-flowchart-v1"

link_policy: "relative-only"
fencing_profile: "outer-backticks-inner-tildes-v1"

test_profiles:
  - "schema-lint"
  - "link-check"
  - "spell-check"
  - "security-policy-lint"
  - "telemetry-schema-validate"

ci_integration:
  workflows:
    - ".github/workflows/kfm-ci.yml"
    - ".github/workflows/security-audit.yml"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "🗺️ Diagrams"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧠 Story Node & Focus Mode Integration"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🔐 **Kansas Frontier Matrix — Sigstore, Cosign v3 & Verifiable Artifact Governance**
`docs/security/supply-chain/sigstore-cosign-v3/README.md`

**Purpose**  
Define the **canonical, verifiable artifact governance** model for KFM using the **Sigstore ecosystem** and **Cosign v3**.

KFM uses cryptographic verification to ensure that **datasets, catalogs, graph exports, container images, models, and documentation artifacts** are:
**signed**, **attested**, **transparency-logged**, and **policy-verifiable** before promotion to a governed release.

</div>

---

## 📘 Overview

KFM enforces **cryptographically verifiable trust** across governed artifacts using:

- **Cosign v3** for signing and in-toto attestations
- **Keyless identity** (OIDC-bound) rather than long-lived signing keys
- **Transparency logging** (Rekor inclusion) for auditability
- **Policy-enforced verification** inside CI/CD and promotion workflows

**Sigstore is not optional** for governed artifacts in KFM.

### Scope

This policy applies to **governed artifacts**, including (non-exhaustive):

- Release artifacts in `releases/<version>/` (e.g., `sbom.spdx.json`, `manifest.zip`, telemetry bundles)
- STAC catalog files and release metadata catalogs
- Graph database export artifacts used for governed ingestion
- Container images used by API services and pipeline runners
- Model artifacts used in Focus Mode
- Documentation bundles shipped as part of a governed release

---

## 🗂️ Directory Layout

~~~text
docs/security/supply-chain/sigstore-cosign-v3/
└── README.md  # This document (Sigstore/Cosign governance model and policy)
~~~

If supporting materials are added (policies, templates, examples), they MUST be listed here and validated in CI.

---

## 🧭 Context

KFM publishes and processes high-value cultural, environmental, and historical datasets. Supply-chain compromise risks include:

- Artifact substitution (a dataset/model/container replaced post-build)
- Provenance spoofing (fake lineage or metadata injected into a release)
- Dependency compromise (malicious transitive packages or base images)
- Silent drift (changes introduced outside governed promotion paths)

Sigstore-based verification provides three governance properties KFM depends on:

- **Authenticity**: “Who produced this artifact?”
- **Integrity**: “Has it been modified since it was produced?”
- **Auditability**: “Can we prove verification later (including offline)?”

---

## 🧱 Architecture

### Sigstore components (conceptual)

- **Cosign v3**  
  Canonical signing + attestation tool used by KFM for governed artifacts.

- **Fulcio (identity)**  
  Issues short-lived certificates bound to OIDC identities for keyless signing.

- **Rekor (transparency)**  
  Append-only transparency log enabling auditability and tamper detection.

### Artifact signing model

KFM signs and verifies artifacts by **digest**, not by mutable tags or filenames.

**Required invariants:**

- Every governed artifact has a stable cryptographic **digest**
- Signatures and attestations refer to the artifact **digest**
- Verification gates evaluate:
  - Allowed signer identity (OIDC issuer + identity constraints)
  - Required attestations by artifact class
  - Transparency inclusion / bundle evidence where required

### Bundles & offline verification

KFM supports offline verification by retaining verifiable evidence alongside release artifacts.

Offline verification must be possible for:
- release bundles stored in `releases/<version>/`
- archived artifacts referenced from Story Nodes and governance audits

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Build / ETL / Export"] --> B["Generate SBOM (SPDX)"]
  B --> C["Generate Provenance (SLSA-style)"]
  C --> D["Cosign v3: Sign + Attest (keyless identity)"]
  D --> E["Transparency Log Evidence (Rekor inclusion / bundle)"]
  E --> F["Verify (policy + attestation requirements)"]
  F --> G["Promote to Governed Release"]
  G --> H["Catalog + Graph Ingestion (STAC / DCAT / PROV)"]
  H --> I["Publish + Telemetry Export"]
  F --> J["On failure: Block Promotion + Emit Governance Telemetry"]
~~~

---

## 🧪 Validation & CI/CD

### Canonical promotion gate

KFM promotion is evaluated as:

~~~text
Build → Attest → Sign → Log → Verify → Promote
~~~

### Enforcement expectations

CI/CD MUST:

- Generate and retain SBOMs for release artifacts
- Generate and retain SLSA-style provenance attestations for release artifacts
- Verify signatures and attestations before:
  - merge into protected branches (when applicable)
  - publishing a governed release
  - ingesting release artifacts into governed catalogs/graphs

### Failure behavior

- Verification failures MUST **fail closed** for governed promotion paths.
- CI SHOULD still emit governance telemetry for failures (sanitized, non-sensitive).

### Security scanning (adjacent controls)

Supply-chain verification is complementary to (not a replacement for):

- dependency vulnerability scanning
- container scanning
- static analysis / policy checks

---

## 📦 Data & Metadata

### Required attestation classes (by artifact type)

| Artifact Class | Required Attestations (minimum) | Notes |
|---|---|---|
| Release bundle artifacts | Provenance, SBOM | Release integrity depends on these |
| Datasets & derived products | Provenance, Dataset metadata | Metadata must include governance labels when applicable |
| Containers | Provenance, SBOM | Must be verifiable by digest |
| Models | Provenance, SBOM, Model card/eval context | Enforce Focus Mode governance expectations |
| Telemetry bundles | Provenance (as applicable) | Telemetry must not include secrets/PII |

### Attestation payload expectations

Attestations MUST be:

- machine-readable
- linked to the subject artifact digest
- free of secrets and sensitive raw values (especially sensitive coordinates)

Example (shape only; fields vary by attestation type and schema):

~~~json
{
  "subject": [{"name": "artifact", "digest": {"sha256": "<digest>"}}],
  "predicateType": "<attestation-type-uri>",
  "predicate": {
    "build": {"commit_sha": "<sha>", "run_id": "<run-id>", "workflow": "<workflow-id>"},
    "governance": {"release": "v11.2.6", "policy": "sigstore-cosign-v3"},
    "artifacts": {"sbom_ref": "../../../../releases/v11.2.6/sbom.spdx.json"}
  }
}
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

KFM links verifiable supply-chain evidence into catalogs and provenance:

- **STAC**: dataset distributions and metadata may reference signature/attestation artifacts as additional assets
- **DCAT**: distributions may include checksums and verifiable evidence references
- **PROV**: signing and attestation events are modeled as activities generating verification evidence entities

### Governance-critical artifacts

Where applicable, KFM treats the following as governance-critical and eligible for signing/verification:

- STAC catalogs and related metadata exports
- Graph export artifacts used for governed ingest
- Release manifests and SBOMs
- Telemetry bundles used for audit and sustainability reporting

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode rely on trustworthy inputs:

- Story Nodes SHOULD cite governed artifacts that are verifiably signed and attested
- Focus Mode services SHOULD load only governed model artifacts that pass verification
- Any “explainability” or “audit context” surfaced to users MUST reference recorded, verifiable evidence (not reconstructed assumptions)

If a referenced artifact cannot be verified, the UI SHOULD degrade gracefully and surface a governance notice rather than silently proceeding.

---

## ⚖ FAIR+CARE & Governance

Supply-chain verification is part of governance evidence.

### Sovereignty and sensitive content constraints

- Do not sign and publish unredacted artifacts that violate sovereignty policy.
- Signatures/attestations MUST NOT embed restricted raw data (e.g., sensitive coordinates).
- Governance labels (CARE, sensitivity, access conditions) MUST be represented in metadata and, where used, in dataset metadata attestations.

### Exception handling

Any exception to signing/attestation requirements for governed artifacts MUST be:
- documented
- reviewed under security/governance oversight
- traceable in release governance records

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-15 | v11.2.6 alignment; clarified directory layout, CI promotion gate, attestation classes, and catalog/provenance wiring; corrected relative references to releases/schemas/standards. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
**Sigstore & Cosign v3 — Supply Chain Governance (v11.2.6)**

[Security Policy](../../../../.github/SECURITY.md) ·
[Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md) ·
[FAIR+CARE Guide](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[Sovereignty Policy](../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>