---
title: "🧯 KFM v11.2.2 — Dependency-Confusion Fallback Controls (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/fallback-controls.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Council · FAIR+CARE"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

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

doc_kind: "Security · Fallback"
intent: "fallback-controls · supply-chain-continuity · degraded-mode-defense"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Governance · Security Safeguard"
classification: "Security · Supply Chain · Emergency Controls"
sensitivity: "Security-Sensitive (Non-personal)"
sensitivity_level: "High"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded when v11.3 fallback controls defined"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/policy/fallback-controls.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/fallback-controls.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:fallback-controls:v11.2.2"
semantic_document_id: "kfm-depconf-policy-fallback-v11.2.2"
event_source_id: "ledger:depconf.policy.fallback.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "diagram-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "unverified-architectural-claims"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧯 Tier 1 — Automated Fallback Controls (Immediate Activation)"
    - "🧯 Tier 2 — Semi-Manual Fallback Controls (Security-Council Trigger)"
    - "🧯 Tier 3 — Emergency Supply-Chain Lockdown (ESCL)"
    - "🕰️ Version History"
---

<div align="center">

# 🧯 **Dependency-Confusion — Fallback Controls**  
`docs/security/supply-chain/dependency-confusion/policy/fallback-controls.md`

**Purpose:**  
Define deterministic secondary and emergency controls activated when primary  
dependency-confusion defenses fail, degrade, or are temporarily unavailable.  
Ensures supply-chain continuity, safety, and provenance integrity during outages or anomalies.

</div>

---

## 📘 Overview

Fallback controls form the **middle layer** of KFM’s defense:

- **Primary Controls →** `rules.md`  
- **Fallback Controls →** *this file*  
- **Ultimate Safeguard →** ESCL (Emergency Supply-Chain Lockdown)

These controls trigger when:

- Registry/mirror integrity degrades  
- Namespace monitoring becomes unavailable  
- Provenance chains cannot be validated in time  
- SBOM drift cannot be reconciled deterministically  
- Network reliability impacts hermetic resolution  

Fallback actions must be:

- Deterministic  
- FAIR+CARE compliant  
- Logged in evidence vaults  
- Reversible once systems stabilize  

---

## 🗂️ Directory Layout

~~~text
📁 policy/
├── 📄 README.md                 # High-level policy overview
├── 📄 rules.md                  # Mandatory enforcement rules
├── 📄 registry-isolation.md     # Registry allow-listing + resolution isolation
├── 📄 signature-requirements.md # Signature & provenance enforcement
├── 📄 fallback-controls.md      # This file — degraded-mode controls
├── 📄 exceptions.md             # Governance-approved SER exceptions
├── 📄 incidents.md              # Incident logs
└── 📂 evidence/                 # Machine evidence vault
    ├── 🛰️ namespace-scan.json
    ├── 🧬 sbom-diff.json
    ├── 🔐 registry-audit.json
    └── 🧾 attestation-verify.json
~~~

---

## 🧯 Tier 1 — Automated Fallback Controls (Immediate Activation)

Tier 1 activates automatically when CI detects anomalies such as:

- Mirror unreachable or latency > threshold  
- SBOM drift (digest mismatch)  
- Namespace-monitor failure or degraded scanning  
- Missing/late provenance chain  
- Suspicious registry metadata changes  

### 1. 🔐 Hard-Pinned Dependency Freezing  
- Lockfiles become **read-only**  
- Only SBOM-sealed dependencies allowed  
- Update attempts blocked  
- Status logged in evidence bundle

### 2. 🧱 Registry Circuit Breaker (Fail-Closed)  
If internal mirrors fail:

- External registries remain **blocked**  
- Builds switch to **sealed local cache only**  
- Unknown dependencies rejected

### 3. 🧪 SBOM Drift Guard  
If SBOM mismatch detected:

- All resolution halted  
- Build uses last-known-good dependency graph

### 4. 🛰️ Namespace Monitor Fallback  
If scanner degrades:

- Dangerous namespaces enforced from historical denylist  
- Only allow-list packages are resolvable

---

## 🧯 Tier 2 — Semi-Manual Fallback Controls (Security Council Trigger)

Tier 2 requires human oversight.

### 1. 🛑 Emergency Package Hold (EPH)  
Council may:

- Freeze entire ecosystems (pip/npm/etc.)  
- Block specific namespaces  
- Disable registry syncs  

### 2. 📦 Manual Verification Queue  
Dependency modifications are manually reviewed for:

- Hash/digest correctness  
- Provenance chain validation  
- SLSA bundle integrity  
- Threat attribution

### 3. 📘 Governance Override  
Only used when operational continuity requires temporary access.

Allowed **only with**:

- SLSA-attested artifacts  
- Hash-locked SBOM sealing  
- Exception logged in `exceptions.md`

---

## 🧯 Tier 3 — Emergency Supply-Chain Lockdown (ESCL)

Highest fallback tier, activated only when:

- Malicious infiltration is detected  
- Mirror poisoning is confirmed  
- Namespace attacks escalate system-wide  
- Provenance chain becomes untrustworthy  
- Multiple registries experience coordinated issues  

### ESCL Actions

- 🚫 All dependency resolution disabled  
- 🔒 Hermetic mode enforced  
- 🗄️ Only sealed dependencies allowed  
- 🧬 SBOM must match last verified digest set  
- 🛰️ Network egress blocked  
- 📁 Artifacts routed through quarantine filters  
- 🧯 Human sign-off required for all builds  

### ESCL Exit Criteria

- Provenance revalidated system-wide  
- Namespace threats mitigated  
- Mirror integrity verified  
- SBOM equivalence restored  
- CI safety thresholds satisfied

---

## 🕰️ Version History

| Version | Date       | Notes |
|--------:|------------|-------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Full extended metadata; aligned to v11.2.2 security controls |
| v11.2.1 | 2025-10-11 | Added ESCL escalation tier                                 |
| v11.2.0 | 2025-09-20 | Initial fallback-controls design                            |

---

<div align="center">

🛡️ [Policy Overview](./README.md) • 📏 [Enforcement Rules](./rules.md) • 🧭 [Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
