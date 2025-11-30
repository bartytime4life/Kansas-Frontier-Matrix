---
title: "🧹 KFM v11.2.2 — Pre-Commit Validation Rules for Dependency-Confusion Defense (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/pre-commit-rules.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security Council · FAIR+CARE"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/security-v3.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Security · Pre-Commit-Rules"
intent: "developer-local-enforcement · dependency-confusion-prevention"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Infrastructure Protection"
classification: "Security · Developer Enforcement"
sensitivity: "Security-Sensitive (non-personal)"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "Medium"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded when v11.3 pre-commit rules are released"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "FAIR+CARE"
  - "PROV-O"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/checks/pre-commit-rules.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/checks/pre-commit-rules.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/checks/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:security:depconf:checks:precommit:v11.2.2"
semantic_document_id: "kfm-depconf-precommit-rules-v11.2.2"
event_source_id: "ledger:depconf.checks.precommit.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "timeline-generation"
  - "diagram-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "unverified-architectural-claims"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🛠️ Required Tools (KFM-DTK)"
    - "🧹 Mandatory Pre-Commit Rule Set"
    - "🔧 Installing Pre-Commit Hook"
    - "🕰️ Version History"
---

<div align="center">

# 🧹 **Pre-Commit Validation Rules for Dependency-Confusion Defense**  
`docs/security/supply-chain/dependency-confusion/checks/pre-commit-rules.md`

**Purpose:**  
Define the mandatory developer-side enforcement layer that prevents dependency-confusion risks  
*before* code reaches CI/CD pipelines.  
These checks ensure pinning discipline, registry isolation, provenance integrity, and SBOM  
alignment at the earliest point of change.

</div>

---

## 📘 Overview

Pre-commit validation is the **local enforcement tier** of KFM’s supply-chain defense.  
It mirrors CI behavior using local-only checks that block commits when:

- Dependencies are unpinned  
- Registries are misconfigured  
- Namespace conflicts exist publicly  
- Signatures or provenance are invalid  
- SBOM and lockfile diverge  
- Fallback logic must activate  
- Governance exceptions are missing or expired  

Local enforcement reduces CI failures and maintains deterministic, secure development.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 checks/
    ├── 📄 README.md                     # Automated checks index
    ├── 📄 ci-validation-rules.md        # CI validation rules
    ├── 📄 provenance-hooks.md           # SLSA + attestation workflow hooks
    ├── 📄 registry-anomaly-detection.md # Registry anomaly detection rules
    ├── 📄 pre-commit-rules.md           # This file — developer-side enforcement
    └── 📄 local-scan-guidance.md        # Manual/local scan instructions
~~~

---

## 🛠️ Required Tools (KFM-DTK)

Install the developer toolkit:

```bash
pip install kfm-dtk
```

Provides:

- `kfm-ns-scan` — namespace collision detection  
- `kfm-reg-audit` — registry isolation validation  
- `kfm-lock-verify` — pinning & lockfile integrity  
- `kfm-sbom-diff` — SBOM drift detection  
- `kfm-provenance-verify` — signature & provenance validation  
- `kfm-fallback-test` — fallback simulation & hermetic testing  

---

## 🧹 Mandatory Pre-Commit Rule Set

### 1️⃣ 🧩 Exact Pinning & Lockfile Integrity  
```bash
kfm-lock-verify
```
Ensures:

- Exact versions  
- Exact registries  
- Cryptographic digests  
- Lockfile ↔ SBOM parity  
- No floating deps  
- No registry drift  

Fail → commit blocked.

---

### 2️⃣ 🔒 Registry Isolation Enforcement  
```bash
kfm-reg-audit --strict
```

Detects:

- Public registry usage  
- Fallback to untrusted endpoints  
- TLS or mirror mismatches  

Fail → commit blocked.

---

### 3️⃣ 🛰️ Namespace Collision Pre-Scan  
```bash
kfm-ns-scan .
```

Flags:

- Public first-publish attackers  
- Typosquats  
- Homoglyph patterns  
- Namespace lookalikes  

Fail → SBD required + commit blocked.

---

### 4️⃣ ✍️ Signature & Provenance Verification  
```bash
kfm-provenance-verify --local
```

Validates:

- Cosign artifact signatures  
- GPG commit/tag signatures  
- SLSA provenance bundles  
- Provenance ↔ SBOM ↔ digest consistency  

Fail → commit rejected.

---

### 5️⃣ 🧬 SBOM Drift Detection  
```bash
kfm-sbom-diff --local
```

Detects:

- Shadow deps  
- Hash drift  
- Lockfile/graph mismatch  
- External version injection  

Fail → commit blocked.

---

### 6️⃣ 🧱 Hermetic Sandbox Validation  
```bash
kfm-fallback-test --validate
```

Ensures:

- Zero outbound registry access  
- No auto-installers or update services  
- No dependency-resolver fallback  
- Fully deterministic environment  

Fail → commit denied.

---

### 7️⃣ 🧭 Governance Constraint Validation  
Automatically checks:

- SER validity (active & unexpired)  
- Correctness of YAML headers in policy files  
- Schema compliance for registry/incident/exception docs  

Fail → commit blocked.

---

## 🔧 Installing Pre-Commit Hook

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: kfm-precommit
        name: KFM Dependency-Confusion Precommit
        entry: tools/kfm-dtk/hooks/kfm-precommit.sh
        language: system
        pass_filenames: false
```

Then activate:

```bash
pre-commit install
```

---

## 🕰️ Version History

| Version  | Date       | Notes                                                     |
|----------|------------|-----------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Extended metadata; layout moved; rules aligned with v11.2.2 |
| v11.2.1  | 2025-10-17 | Added hermetic sandbox + fallback validation               |
| v11.2.0  | 2025-09-05 | Initial developer pre-commit ruleset                       |

---

<div align="center">

🧪 [Automated Checks](./README.md) • 🧬 [Provenance Hooks](./provenance-hooks.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
