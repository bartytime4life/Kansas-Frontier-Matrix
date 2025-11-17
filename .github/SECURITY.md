---
title: "🔒 Kansas Frontier Matrix — Security Policy & Operational Safeguards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/SECURITY.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly · Autonomous · Security & FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../releases/v10.4.0/manifest.zip"
telemetry_ref: "../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/security-policy-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Security Policy"
intent: "security-governance"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Security Guild + FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - ".github/SECURITY.md@v10.0.0"
  - ".github/SECURITY.md@v10.3.2"
  - ".github/SECURITY.md@v10.4.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SecurityPolicy"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../schemas/json/security-policy.schema.json"
shape_schema_ref: "../schemas/shacl/security-policy-shape.ttl"
doc_uuid: "urn:kfm:doc:github-security-policy-v10.4.1"
semantic_document_id: "kfm-doc-github-security"
event_source_id: "ledger:.github/SECURITY.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "United States / Kansas"
classification: "Public Document"
role: "security-policy"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next security policy update"
---

<div align="center">

# 🔒 **Kansas Frontier Matrix — Security Policy & Operational Safeguards**  
`.github/SECURITY.md`

**Purpose:**  
Define the **security protocols, reporting mechanisms, supply-chain safeguards, vulnerability procedures, and  
FAIR+CARE-aligned ethical security controls** for all contributors and maintainers of the Kansas Frontier Matrix (KFM).  
This policy ensures that KFM’s code, datasets, governance metadata, documentation, and automation remain secure,  
auditable, and ethically maintained.

</div>

---

## 📘 Overview

Security in KFM is:

- **Zero-trust by default**  
- **FAIR+CARE aligned**  
- **SBOM-governed**  
- **Telemetried**  
- **Auditable & version-pinned**  
- **Supply-chain hardened**  

This document outlines:

1. Vulnerability reporting workflow  
2. Responsible disclosure policy  
3. Security boundaries  
4. Supply-chain controls  
5. CARE-governed security constraints  
6. SLSA/SBOM requirements  
7. Contributor responsibilities  

---

## 🗂️ File Context

```text
.github/
│
├── SECURITY.md                 # This security policy & safeguards document
├── ARCHITECTURE.md             # GitHub CI/CD & governance architecture
└── README.md                   # GitHub infrastructure overview
````

---

## 🚨 1. Reporting a Vulnerability

If you discover a security vulnerability:

1. **DO NOT** open a public GitHub issue.

2. Email the private security address:

   **📩 [security@kansasfrontiermatrix.org](mailto:security@kansasfrontiermatrix.org)**

3. Include:

   * Vulnerability description
   * Steps to reproduce
   * Impact assessment (if known)
   * Whether the issue involves sensitive or CARE-labeled data
   * Proof-of-concept (optional but helpful)

4. You will receive a **receipt within 48 hours** and a full triage response within **5 business days**.

All disclosures are handled under **Responsible Disclosure v2.0** and KFM’s **Ethical Security Protocol**.

---

## 🛡️ 2. Scope of Security Coverage

This policy covers:

* All code in `src/**`, `web/**`, `tools/**`, `tests/**`, and `docs/**`
* All workflow automation in `.github/workflows/**`
* All datasets with governance constraints (`data/**`)
* All releases, manifests, SBOMs, and provenance files
* STAC/DCAT catalogs and metadata bundles
* AI/ML components and Focus Mode reasoning

This policy does **not** cover:

* External datasets not hosted or redistributed by KFM
* Community forks
* 3rd-party STAC endpoints outside KFM control

---

## 🔐 3. Severity Classification

KFM uses a **FAIR+CARE-extended CVSS scoring model**:

| Severity     | Score    | Notes                                                                 |
| ------------ | -------- | --------------------------------------------------------------------- |
| **Critical** | 9.0–10.0 | Data corruption, bypass of CARE restrictions, supply-chain compromise |
| **High**     | 7.0–8.9  | PII exposure, provenance tampering, STAC integrity break              |
| **Medium**   | 4.0–6.9  | Limited blast radius or difficult to exploit                          |
| **Low**      | 0.1–3.9  | Minor, informational, or mitigated by design                          |

Security and CARE impact are evaluated together.

---

## 🔑 4. Supply-Chain & SBOM Requirements

KFM enforces strict supply-chain constraints:

* Every release must include a **complete SBOM** (`sbom.spdx.json`)
* All packages must be:

  * Version-pinned
  * Integrity-verified
  * SLSA Level 1+ compliant
* CI checks for:

  * Dependency vulnerabilities (OSV scanner)
  * License conflicts
  * Hash mismatches
  * Manifest/SBOM divergence
* No unreviewed dependencies allowed
* No dynamic imports of unverified packages

---

## 👮 5. Workflow & CI/CD Safeguards

CI/CD workflows **must NOT**:

* Expose secrets in logs
* Run arbitrary scripts from forks
* Disable required validators
* Modify governance metadata automatically without review
* Load remote unverified scripts

Workflows **must**:

* Validate all changes using:

  * Schema validation
  * Markdown rules (KFM-MDP v10.4.3)
  * Governance validation (FAIR+CARE)
  * Telemetry validation
  * SBOM integrity checks

* Use **CODEOWNERS** for protected paths:

  * `.github/**`
  * `tools/**`
  * `data/**`
  * `schemas/**`
  * `docs/standards/**`

---

## 🧬 6. AI / Focus Mode Security Constraints

AI models must:

* Never produce unverified historical claims
* Never fabricate dataset metadata
* Never generate sensitive coordinates
* Always annotate AI-generated content
* Respect governance flags (CARE, sovereignty)

Focus Mode must:

* Include provenance indicators for all surfaced content
* Mark speculative or low-confidence sections
* Avoid hallucinated relationships
* Prevent unauthorized summarization of CARE-protected datasets

---

## 🌐 7. Data & CARE Security

Datasets must be secured according to:

* CARE Principles
* Indigenous Data Sovereignty rules (where applicable)
* Redaction/generalization policies
* License and rights-holder reviews

All sensitive data must be generalized using:

* **H3 r7+** for spatial data
* **Fuzzy temporal bins** for time
* Minimum aggregation thresholds for tabular data

All provenance must follow:

* PROV-O
* CIDOC-CRM mapping
* SBOM linkage

---

## 🧪 8. Security Testing Requirements

Security must be tested through:

* Automated dependency scanning
* Workflow integrity scanning
* STAC/DCAT schema validation
* Provenance forgery tests
* CARE rule violation tests
* Flooding, injection, and misuse resistance tests
* AI prompt-injection hardening tests

Security tests are executed in:

* `tests/security/**`
* `tests/schemas/**`
* `.github/workflows/security_audit.yml`

---

## 🧾 9. Vulnerability Disclosure Process

After receiving a report:

1. Triage team assigns severity.
2. A reproducible test case is validated.
3. Patch or mitigation is developed.
4. Governance sign-off is required for:

   * CARE-related issues
   * Sovereignty-sensitive issues
   * Provenance leaks
5. Patch is:

   * Implemented
   * Tested
   * Reviewed under CODEOWNERS
   * Released under a new version tag

Reporter receives:

* Credit (optional; anonymous reporting is supported)
* Resolution summary
* Timeline & severity score

---

## 🕰 Version History

| Version | Date       | Summary                                                                                                  |
| ------: | ---------- | -------------------------------------------------------------------------------------------------------- |
| v10.4.1 | 2025-11-16 | Upgraded to KFM-MDP v10.4.3; added extended metadata, lined directory block, and tightened CI alignment. |
| v10.4.0 | 2025-11-15 | Full rebuild under KFM-MDP v10.4; aligned with governance, SBOM, telemetry, and CARE security            |
| v10.3.2 | 2025-11-14 | Added supply-chain + SLSA guidance                                                                       |
| v10.3.1 | 2025-11-13 | Initial baseline security policy                                                                         |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License
Validated under MCP-DL v6.3 and KFM-MDP v10.4.3
FAIR+CARE Certified · Public Document · Version-Pinned

</div>
