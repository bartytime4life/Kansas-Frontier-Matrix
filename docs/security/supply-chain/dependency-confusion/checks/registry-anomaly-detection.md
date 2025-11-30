---
title: "🛰️ KFM v11.2.2 — Registry Anomaly Detection Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/checks/registry-anomaly-detection.md"
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

doc_kind: "Security · Registry-Anomaly-Detection"
intent: "registry-anomaly-detection · upstream-threat-detection · provenance-integrity"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Governance · Critical Infrastructure"
classification: "Security · Automated Detection"
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
sunset_policy: "Superseded upon next anomaly-detection revision"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:Feature"

metadata_profiles:
  - "DCAT 3.0"
  - "STAC 1.0.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/checks/registry-anomaly-detection.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/checks/registry-anomaly-detection.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/checks/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:security:depconf:checks:registry-anomaly-detection:v11.2.2"
semantic_document_id: "kfm-depconf-registry-anomaly-v11.2.2"
event_source_id: "ledger:depconf.checks.registryanomaly.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "timeline-generation"

ai_transform_prohibited:
  - "content-alteration"
  - "narrative-fabrication"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🛰️ Detection Categories"
    - "🗃️ Evidence Outputs"
    - "🧪 CI Enforcement"
    - "🕰️ Version History"
---

<div align="center">

# 🛰️ **Registry Anomaly Detection Rules**  
`docs/security/supply-chain/dependency-confusion/checks/registry-anomaly-detection.md`

**Purpose:**  
Define automated behavioral, statistical, and cryptographic anomaly-detection logic used by  
KFM-CI to detect registry poisoning, namespace hijacking, dependency-confusion threats,  
and upstream supply-chain compromise indicators.

</div>

---

## 📘 Overview

Registry anomaly detection is a **behavioral and metadata-driven threat detection layer** extending  
KFM’s strict registry-isolation model.  
It detects subtle, emergent, or adversarial upstream behavior, including:

- Namespace hijacks  
- First-publish attacks  
- Registry poisoning  
- Digest drift  
- Publisher compromise  
- Typosquatting variants  
- Suspicious publish-time patterns  
- Metadata irregularities  
- TLS & certificate anomalies  

Every anomaly generates:

- Immutable machine evidence  
- A CI hard-fail  
- Namespace or registry quarantine  
- A governance-required incident review  

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 checks/
    ├── 📄 README.md                     # Automated checks overview
    ├── 📄 ci-validation-rules.md        # CI validation rules
    ├── 📄 provenance-hooks.md           # Attestation/provenance hooks
    ├── 📄 registry-anomaly-detection.md # This file — anomaly detection rules
    ├── 📄 pre-commit-rules.md           # Developer-machine enforcement
    └── 📄 local-scan-guidance.md        # Manual/local scan procedures
~~~

---

## 🛰️ Detection Categories

### 1️⃣ 🧿 Namespace Activity Anomalies  
Detects:

- New external packages matching internal KFM names  
- Rapid namespace creation  
- Typosquatting shapes (hyphens, underscores, confusables)  
- High-risk substring permutations  
- Shadow-version releases timed near KFM internal releases  

Actions:

- Namespace quarantine  
- SBD (Security Block Declaration)  
- Evidence → `namespace-scan.json`  
- Incident stub creation  

---

### 2️⃣ ⏱️ Publish-Time Anomalies  
Detects:

- Rapid version spikes  
- Suspicious major-version jumps  
- Duplicate version numbers  
- Publish bursts consistent with malware campaigns  
- Odd-hour coordinated pushes  

Actions:

- Version quarantine  
- SBOM revalidation  
- Provenance reevaluation  

---

### 3️⃣ 🔐 TLS & Certificate Anomalies  
Validates registry-connection safety:

- TLS pinning enforcement  
- Certificate chain correctness  
- Expected SAN entries  
- No stale/intermediate cert abuse  
- No clock-skew anomalies  

Actions:

- Connection block  
- Registry quarantine  
- Evidence → `registry-audit.json`  

---

### 4️⃣ 🧬 Metadata & Digest Drift  
Compares upstream metadata against:

- KFM internal mirrors  
- Sealed SBOM digests  
- Known-good artifact history  
- SLSA provenance metadata  

Drift may indicate:

- Registry poisoning  
- MITM attacks  
- Malicious overwrite  
- Compromised publisher account  

Actions:

- SBOM drift freeze  
- Mirror quarantine  
- Evidence → `sbom-diff.json`  

---

### 5️⃣ 🧩 Resolution Behavior Anomalies  
Detects:

- Resolver attempting public registries  
- Protocol drift (HTTP→HTTPS mismatch)  
- Overridden source maps  
- Unpinned/fallback resolution attempts  
- Unexpected dependency graph changes  

Actions:

- Resolution halt  
- Governance review required  

---

### 6️⃣ 🕵️ Publisher Identity Anomalies  
Detects:

- Suspicious new publisher accounts  
- Maintainer handoff anomalies  
- Key-rotation irregularities  
- Email/identity mismatch patterns  
- Contributor behavior anomalies  

May indicate upstream credential compromise.

---

### 7️⃣ 🔡 Typosquatting Indicators  
Detects:

- Levenshtein-distance near-matches  
- Unicode homoglyph tricks  
- Visual-similar namespace variants  
- Prefix/suffix injection patterns  
- Lookalike vendor prefixes  

Examples:  
`@kfm/core` → `@kfm-cor`, `@kfm0/core`, `@kfn/core`

---

### 8️⃣ 🚨 Sudden First-Publish Events  
Flags:

- New public publishes that match internal module names  
- Variants of KFM namespaces  
- Names seen only internally appearing externally  

This is the most well-known dependency-confusion attack vector.

---

## 🗃️ Evidence Outputs

All anomalies generate evidence stored under:

```
docs/security/supply-chain/dependency-confusion/policy/evidence/
```

Including:

- 🛰️ `namespace-scan.json`  
- 🔐 `registry-audit.json`  
- 🧬 `sbom-diff.json`  
- 🧾 `attestation-verify.json`  

Evidence must be:

- Timestamped  
- Immutable  
- Schema-validated  
- FAIR+CARE compliant  
- Linked via PROV-O (`prov:Entity`, `prov:Activity`, `prov:Agent`)  

---

## 🧪 CI Enforcement

Registry anomaly detection participates in:

- `namespace-monitor.yml`  
- `registry-policy-check.yml`  
- `dependency-integrity.yml`  
- `sbom-validate.yml`  
- `slsa-attestation-verify.yml`  

Any anomaly triggers:

- CI hard-fail  
- Namespace or registry quarantine  
- Incident stub  
- Council review  

---

## 🕰️ Version History

| Version  | Date       | Notes                                                          |
|----------|------------|----------------------------------------------------------------|
| v11.2.2  | 2025-11-30 | Extended metadata; layout moved; complete anomaly framework     |
| v11.2.1  | 2025-10-16 | Added publisher-identity drift detection                        |
| v11.2.0  | 2025-09-01 | Initial anomaly-detection ruleset                               |

---

<div align="center">

🧪 [Automated Checks](./README.md) • 🔒 [Registry Isolation](../policy/registry-isolation.md) • 🧭 [Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
