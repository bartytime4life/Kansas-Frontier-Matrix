---
title: "🛡️ KFM v11.2.2 — Dependency-Confusion Defense Policy (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/dependency-confusion/policy/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Supply-Chain Security · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "Aligned with v10.x → v11.x supply-chain security contract"

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

doc_kind: "Policy"
intent: "dependency-confusion-defense"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Governance · Protection of Critical Infrastructure"
classification: "Security · Supply Chain · Dependency Management"
sensitivity: "Security-Sensitive (Non-personal)"
sensitivity_level: "High"
public_exposure_risk: "Low"
indigenous_rights_flag: true
risk_category: "High"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded by next supply-chain security revision"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/supply-chain/dependency-confusion/policy/README.md@v11.2.1"
  - "docs/security/supply-chain/dependency-confusion/policy/README.md@v11.2.0"
  - "docs/security/supply-chain/dependency-confusion/README.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:security:dependency-confusion:policy:root:v11.2.2"
semantic_document_id: "kfm-depconf-policy-root-v11.2.2"
event_source_id: "ledger:depconf.policy.root.v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧱 Security Requirements (Enforced)"
    - "🧪 Validation & CI/CD Enforcement"
    - "🕰️ Version History"
---

<div align="center">

# 🛡️ **KFM v11.2.2 — Dependency-Confusion Defense Policy**  
`docs/security/supply-chain/dependency-confusion/policy/README.md`

**Purpose:**  
Define the *formal, enforceable security controls* that harden the Kansas Frontier Matrix (KFM)  
supply chain against dependency-confusion attacks across all languages, registries, CI/CD  
environments, and pipeline layers.  
This policy is Diamond⁹ Ω / Crown∞Ω Ultimate certified and enforced continuously by KFM-CI.

</div>

---

## 📘 Overview

Dependency-confusion (a.k.a. namespace shadowing) occurs when malicious public-registry  
packages override internal/private dependencies through unqualified namespace resolution or  
version precedence manipulation.

KFM v11.2.2 enforces a multilayer defense strategy including:

- **Deterministic package pinning** (PyPI, NPM, Cargo, Maven, NuGet, RubyGems, Go)  
- **Registry isolation + strict allow-listing**  
- **Cryptographic signature enforcement & SLSA-Level ≥ 3 attestation**  
- **SBOM-driven build sealing**  
- **Namespace collision scanning & early warning detection**  
- **CI/CD isolation + hermetic sandboxing**  
- **Automatic diff-monitoring for upstream namespace activity**  
- **Fallback-controls activation for mirror failures or drift**  

All protections must remain deterministic, reproducible, provenance-aligned, and FAIR+CARE compliant.

---

## 🗂️ Directory Layout

~~~text
📁 dependency-confusion/
└── 📁 policy/
    ├── 📄 README.md                 # This file — top-level dependency-confusion policy
    ├── 📄 rules.md                  # Enforcement rules
    ├── 📄 registry-isolation.md     # Registry allow-listing & isolation rules
    ├── 📄 signature-requirements.md # Cryptographic signature & provenance rules
    ├── 📄 fallback-controls.md      # Degraded-mode & emergency fallback policies
    ├── 📄 exceptions.md             # Governance-approved exceptions (SER)
    ├── 📄 incidents.md              # Historical incident register
    └── 📂 evidence/                 # Machine evidence vault
        ├── 🛰️ namespace-scan.json
        ├── 🧬 sbom-diff.json
        ├── 🔐 registry-audit.json
        └── 🧾 attestation-verify.json
~~~

---

## 🧱 Security Requirements (Enforced)

### 1. 📦 Deterministic Dependency Pinning
All dependencies MUST be pinned to:

- **Exact version**  
- **Exact registry**  
- **Exact hash/digest** (pip hash-mode, npm integrity, cargo checksum, etc.)

❌ **Unbounded or floating specifiers** (`*`, `>`, `<`, `^`, `~`) are prohibited.

---

### 2. 🔒 Registry Isolation & Allow-Listing
KFM mandates strict registry isolation:

- PyPI → internal mirror only  
- NPM → GitHub scoped `@kfm/*` only  
- Cargo → `source = "kfm-internal"`  
- Maven → `kfm-mirror` only  

All public registries are blocked unless explicitly approved via SER governance.

(Details in: `registry-isolation.md`)

---

### 3. ✍️ Cryptographic Signatures & Provenance
All dependencies MUST include:

- Verified **SLSA-3+ provenance attestation**  
- Verified cryptographic signatures (Cosign/GPG)  
- Matching SBOM digests  

Unsigned or unverifiable artifacts → **blocked + quarantined**.

(Details in: `signature-requirements.md`)

---

### 4. 🛰️ Namespace Collision Scanning
Automated CI/CD jobs MUST:

- Scan upstream registries for namespace collisions  
- Identify shadow/rogue packages  
- Block risky name ranges  
- Auto-file an SBD (Security Block Declaration)  

---

### 5. 🧪 Hermetic CI/CD & Sandboxing
All builds MUST:

- Run with **zero outbound Internet**  
- Resolve dependencies *only* from internal mirrors  
- Use pinned, digested, SLSA-attested artifacts  
- Execute inside isolated sandboxes  

---

### 6. 🧯 Fallback Controls for Degraded Mode
Fallback controls activate automatically when:

- Mirror is unreachable  
- SBOM drift detected  
- Namespace-monitor fails  
- Registry integrity cannot be verified  

Fallback behaviors include:

- Lockfile freeze  
- Local-artifact-cache-only mode  
- Mirror quarantine  
- Namespace blocklist escalation  

(Details in: `fallback-controls.md`)

---

### 7. 📝 Governance & Incident Response
Upon detecting a namespace conflict:

1. CI blocks merge  
2. Security Council notified  
3. SBD filed  
4. Incident logged in `incidents.md`  
5. Package quarantined  
6. Permanent denylist entry created  

Exceptions require SER (Security Exception Request) and appear in `exceptions.md`.

---

## 🧪 Validation & CI/CD Enforcement

This policy is enforced by:

- `security-depscan.yml`  
- `registry-policy-check.yml`  
- `sbom-validate.yml`  
- `slsa-attestation-verify.yml`  
- `namespace-monitor.yml`  
- `security-evidence-lint.yml`  
- `governance-policy-check.yml`  

All failures **block merges** into `main`, `release/*`, and `secure/*`.

---

## 🕰️ Version History

| Version | Date       | Changes                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Full rewrite; added fallback & signature policies; directory layout updated; MDP v11.2.2 alignment |
| v11.1.0 | 2025-10-02 | Added SLSA-3 requirements & namespace-diff monitoring                   |
| v11.0.0 | 2025-08-11 | Initial v11 release                                                     |

---

<div align="center">

🌐 [KFM Project](../../../../../README.md) • 🔐 [Security Standards](../../../../standards/README.md) • 🧭 [Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
