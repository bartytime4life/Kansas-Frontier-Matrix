---
title: "🛡️ KFM v11 — Security Vulnerability Registry & Advisories (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Central registry and governance hub for KFM security advisories, CVEs, and vulnerability documentation."
path: "docs/security/vulns/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Reference"
review_cycle: "Quarterly · Security & Supply-Chain Council"
content_stability: "stable"
backward_compatibility: "Advisory-only (no runtime behavior)"

status: "Active / Enforced"
doc_kind: "Security Registry"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/security-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/security-v3.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

scope:
  domain: "security"
  applies_to:
    - "vulnerability-registry"
    - "supply-chain"
    - "dependencies"
    - "cryptography"
    - "services"

semantic_intent:
  - "security"
  - "governance"
  - "risk-register"
category: "Documentation · Security · Vulnerabilities"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General (non-sensitive; security controls apply)"
sensitivity_level: "Low"
public_exposure_risk: "Medium"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "KFM Security & Supply-Chain Council"
ttl_policy: "Indefinite (until all referenced vulnerabilities are retired)"
sunset_policy: "Supersede when v11 security registry is replaced"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Collection"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/security/README.md"
  - "security:registry:vulns@v10.x"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-security-vuln-registry-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-security-vuln-registry-v11.2.3-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:security:vulns:registry:v11.2.3"
semantic_document_id: "kfm-security-vuln-registry-v11.2.3"
event_source_id: "ledger:kfm:doc:security:vulns:registry:v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
---

<div align="center">

# 🛡️ KFM v11 — Security Vulnerability Registry & Advisories  

`docs/security/vulns/README.md`

**Purpose:**  
Serve as the **governed hub** for all **KFM security advisories, CVEs, and vulnerability write-ups**, linking them to SBOMs, CI/CD enforcement, and supply-chain governance.

</div>

---

## 📘 1. Overview

The `docs/security/vulns/` tree is the **canonical registry** for:

- KFM-aligned write-ups of **external CVEs** (e.g., node-forge, OpenSSL, npm libraries).  
- **Internal vulnerabilities** discovered in KFM services or infrastructure.  
- **Advisories** that tie vulnerabilities to:
  - SBOM entries  
  - CI/CD enforcement rules  
  - Governance and risk registers  

This directory does **not** redefine upstream CVE content; instead, it:

- Normalizes advisory structure under **KFM-MDP v11.2.2**.  
- Adds provenance, governance, and integration details for the KFM stack.  
- Provides a machine-readable index for Focus Mode, dashboards, and automation.

---

## 🗂️ 2. Directory Layout

~~~text
docs/security/vulns/
├── 📄 README.md                           # This file: registry overview & governance
│
├── 📂 node-forge/                         # Package-family directory (npm cryptography)
│   ├── 📄 CVE-2025-12816.md               # KFM advisory for node-forge ASN.1 flaw
│   └── 📄 INDEX.md                        # (Optional) Package-specific index
│
├── 📂 openssl/                            # Example: OpenSSL-related CVEs
│   └── 📄 INDEX.md                        # Placeholder / future advisories
│
├── 📂 kfm-services/                       # Internal KFM service vulnerabilities
│   └── 📄 INDEX.md                        # Internal vuln registry index
│
└── 📂 archive/                            # Retired or fully-remediated advisories
    └── 📄 INDEX.md                        # Archive index and retirement policy
~~~

**Rules:**

- One advisory per file, named as:  
  - `CVE-YYYY-NNNNN.md` for public CVEs, or  
  - `KFM-SEC-YYYY-NNN.md` for internal-only issues.  
- Package or system families get their own subdirectory (e.g., `node-forge/`, `openssl/`, `kfm-services/`).  
- Archived/retired advisories MUST be moved to `archive/` and flagged accordingly in front matter.

---

## 📑 3. Advisory Document Contract

Each advisory (e.g., `node-forge/CVE-2025-12816.md`) MUST:

- Follow **KFM-MDP v11.2.2** front matter shape with at minimum:
  - `title`, `description`, `path`, `version`, `last_updated`  
  - `status`, `severity`, `cvss_score`, `cve_id` (if public)  
  - `component`, `scope`, `semantic_intent`  
  - SBOM and telemetry references  
- Include human-readable sections covering:

  1. **Overview / Summary**  
  2. **Attack Scenario**  
  3. **Affected Versions / Components**  
  4. **Fix Status (Upstream)**  
  5. **Required Mitigation Steps (KFM policy)**  
  6. **Technical Details (Root cause & failure mode)**  
  7. **Impacted Use-Cases**  
  8. **KFM Integration & Governance**  
  9. **References**  
  10. **Version History**

- Map cleanly into the security ontology (CVE ↔ package ↔ KFM component).

---

## 🧭 4. Integration with SBOM, CI/CD & Supply-Chain

Advisories in this directory are **not standalone text**; they act as **governance artifacts** tying vulnerabilities to:

- **SBOM entries** (via `sbom_ref` and package identifiers).  
- **CI/CD policies** that:
  - Fail builds on vulnerable versions.  
  - Enforce minimum patched versions (e.g., `node-forge >= 1.3.2`).  
- **Risk registers**, where:
  - Each advisory links to an entry with status `(Open / Mitigated / Accepted / Retired)`.  

Typical flow:

1. Vulnerability identified (upstream CVE, audit, or internal finding).  
2. Advisory created under `docs/security/vulns/` with minimal required sections.  
3. CI/CD, SBOM, and governance references updated to point to the advisory.  
4. Once remediation is complete:
   - Advisory’s Version History and status updated.  
   - Risk register updated with resolution details.  

---

## 🧪 5. Minimal Example: KFM-Aligned CVE Advisory Skeleton

This skeleton shows the **shape** expected in each advisory file (details filled per vulnerability):

~~~markdown
---
title: "🚨 KFM v11 — CVE-YYYY-NNNNN (Package · Short Summary)"
description: "Short description of the vulnerability and its impact on KFM."
path: "docs/security/vulns/<package>/CVE-YYYY-NNNNN.md"
version: "v11.2.3"
last_updated: "2025-12-02"
status: "Active Advisory"
severity: "High"
cvss_score: "X.Y"
cve_id: "CVE-YYYY-NNNNN"
component: "<package> (<subsystem>)"
license: "CC-BY 4.0"
# ... standard KFM-MDP v11.2.2 fields ...
---

# 🚨 CVE-YYYY-NNNNN — <package> Short Vulnerability Name

## ⚠️ Summary
## 🧨 Attack Scenario
## 🔍 Affected Versions
## 🛠️ Fix Status
## ✅ Required Mitigation Steps (KFM)
## 🔬 Technical Details
## 📦 Impacted Use-Cases
## 📚 References
## 🕰️ Version History
~~~

All advisory authors SHOULD start from a shared template in `docs/security/templates/` once that directory is defined.

---

## ⚖️ 6. FAIR+CARE & Ethical Security Considerations

While vulnerability content is generally non-sensitive, this registry MUST:

- Avoid disclosing **sensitive deployment details** (e.g., internal hostnames, credentials, specific IPs).  
- Avoid tying vulnerabilities to specific individuals; focus on systems and processes.  
- Respect any jurisdictional or sovereignty constraints from KFM governance (e.g., where a vulnerability might leak information about protected infrastructure or communities).  

Where vulnerabilities intersect with:

- **User safety**
- **Protected cultural/heritage systems**
- **Indigenous-controlled data or infrastructure**

the advisory MUST reference `sovereignty_policy` explicitly in its narrative and mitigation steps.

---

## 📊 7. Telemetry & Observability Links

Security telemetry associated with vulnerabilities SHOULD capture:

- Detection of vulnerable package versions in builds.  
- Remediation status per environment (dev/stage/prod).  
- Residual exceptions/waivers (e.g., pinned legacy systems).  

This README is the anchor for dashboards that:

- Show open vs mitigated advisories.  
- Map CVEs to KFM components and pipelines.  
- Track time-to-remediation over releases.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                          | Summary                                                   |
|----------|------------|---------------------------------|-----------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Security & Supply-Chain Council | Established KFM v11 vulnerability registry overview and patterns. |

---

<div align="center">

🛡️ **KFM v11 — Security Vulnerability Registry & Advisories**  
Security-First · Supply-Chain Aware · Governance-Enforced  

[📘 Security Index](../README.md) · [🔐 Supply-Chain Security](../supply-chain/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>