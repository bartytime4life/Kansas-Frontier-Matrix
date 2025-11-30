---
title: "⚠️ KFM v11.2.2 — Dependency-Confusion Exception Registry (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/exceptions.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Council · FAIR+CARE"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "Aligned with v10.x → v11.x policy contract"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

signature_ref: "../../../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.2/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/release-manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/security-v3.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

doc_kind: "Security · Exceptions"
intent: "supply-chain-exception-governance"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Governance · Ethical Risk Management"
classification: "Security · Supply Chain · Exception Control"
sensitivity: "Security-Sensitive (Non-personal)"
sensitivity_level: "High"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "90 days per exception entry"
sunset_policy: "Superseded automatically when exception expires"

ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "Dataset"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/policy/exceptions.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/exceptions.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:exceptions:v11.2.2"
semantic_document_id: "kfm-depconf-policy-exceptions-v11.2.2"
event_source_id: "ledger:depconf.policy.exceptions.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
  - "metadata-extraction"
  - "diagram-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Exception Format (Required)"
    - "📂 Current Approved Exceptions (v11.2.2)"
    - "🔐 Exception Lifecycle Rules"
    - "🕰️ Version History"
---

<div align="center">

# ⚠️ **Dependency-Confusion Exception Registry**  
`docs/security/supply-chain/dependency-confusion/policy/exceptions.md`

**Purpose:**  
Serve as the **canonical, governance-controlled exception ledger** for any temporary deviations  
from the KFM v11.2.2 dependency-confusion hardening policy.  
All entries here require formal approval, strict expiry, compensating controls,  
and auditability via PROV-O lineage.

</div>

---

## 📘 Overview

KFM v11.2.2 requires that all dependencies be:

- Fully pinned  
- Registry-isolated  
- SLSA-attested  
- SBOM-validated  
- Namespace-clean  
- Mirror-isolated  

Only in rare, controlled situations may an exception occur.

All exceptions — without exception — MUST be:

- **Request-driven** via a formal Security Exception Request (SER)  
- **Reviewed** by the Supply-Chain Security Council  
- **Approved** by majority governance vote  
- **Time-bounded** (≤ 90 days)  
- **Subject to compensating controls**  
- **Logged immutably** in this registry  
- **CI-validated** every run  

---

## 🧭 Exception Format (Required)

Each registered exception MUST follow this YAML schema:

```yaml
id: EX-DC-XXXX
package: "registry/package-name"
justification: >
  Clear technical necessity, referencing reproducibility, reliability,
  or compatibility constraints with full evidence.
risk_assessment:
  severity: low|medium|high
  likelihood: low|medium|high
  compensating_controls:
    - "hash pinning"
    - "SLSA override attestation"
    - "sandbox execution"
    - "SBOM-sealed local copy"
scope:
  allowed_versions:
    - "1.2.3"
    - "1.2.4"
  registries:
    - "https://internal-mirror.example"
expiration: "YYYY-MM-DD"
approved_by:
  - name: "Security Council Member"
    role: "Council"
date_approved: "YYYY-MM-DD"
```

All fields are mandatory.  
Missing fields → **CI hard fail + governance block**.

---

## 📂 Current Approved Exceptions (v11.2.2)

> ⚠️ *This registry intentionally starts empty.*  
> Add entries **only** through governance-approved PRs with SER documentation.

_No active exceptions._

---

## 🔐 Exception Lifecycle Rules

### 1. ⏳ Mandatory Expiration  
Every exception MUST expire in ≤ 90 days. No indefinite exceptions allowed.

### 2. 🔄 Renewal Requirements  
A renewal requires:

- A new SER  
- Updated justification  
- Fresh risk assessment  
- Evidence of attempted remediation  
- Approval vote  

### 3. 🛠️ Automatic Revocation  
Exceptions are *automatically* revoked if:

- A secure alternative becomes available  
- A name collision emerges  
- SBOM drift occurs  
- Public registry publishes a conflicting version  
- Mirror integrity fails  

### 4. 🧪 CI Enforcement  
CI validates:

- Exception ID format  
- Registry allow-list match  
- Namespace-scan compatibility  
- Hash/digest integrity  
- Expiration date  

A single violation → **merge blocked**.

---

## 🕰️ Version History

| Version  | Date       | Notes                                            |
|----------|------------|--------------------------------------------------|
| v11.2.2  | 2025-11-30 | Full extended metadata upgrade; directory aligned with v11.2.2 |
| v11.2.1  | 2025-10-04 | Added strict 90-day expiration enforcement        |
| v11.2.0  | 2025-09-15 | Initial version                                   |

---

<div align="center">

🔐 [Supply-Chain Security](../../README.md) • 🛡️ [Policy Overview](./README.md) • 🧭 [Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
