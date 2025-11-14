---
title: "🛡️ Kansas Frontier Matrix — Security Policy & Vulnerability Disclosure (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: ".github/SECURITY.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Annual / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../releases/v10.3.0/manifest.zip"
telemetry_ref: "../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/github-security-v1.json"
governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛡️ **Kansas Frontier Matrix — Security Policy**  
`.github/SECURITY.md`

**Purpose:**  
Define coordinated vulnerability disclosure (CVD), secure development lifecycle, CI-first security controls, and supply-chain provenance so software, datasets, and models remain **safe, auditable, and ethical** under **MCP-DL v6.3**, **FAIR+CARE**, **SLSA 1.0**, and ISO-aligned best practices.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../docs/standards/faircare.md)  
[![Security Status](https://img.shields.io/badge/Security-Monitored-success)]()

</div>

---

## 📘 Overview
Security in KFM follows a **transparency → prevention → reproducibility** model, using:

- **OWASP Top 10**  
- **NIST SSDF (SP 800-218)**  
- **SLSA 1.0 Provenance Requirements**  
- **GitHub Advanced Security**  
- **FAIR+CARE Ethics**  

Security artifacts converge into:

~~~~~text
../releases/v10.3.0/focus-telemetry.json
~~~~~

Referenced assets:

- `../releases/v10.3.0/sbom.spdx.json`  
- `../releases/v10.3.0/manifest.zip`  

ensuring one-hop supply-chain verifiability.

---

## 🧩 Scope
This policy covers:

- Entire monorepo (`src/`, `web/`, `data/`, `tools/`, `.github/`)  
- All workflows (`.github/workflows/**`)  
- Runtime artifacts (Docker, static UI bundles, API servers)  
- Ecosystem components (Neo4j, FastAPI, GraphQL, React/MapLibre/Cesium, STAC/DCAT)

---

## 🚨 Reporting a Vulnerability (CVD)

**Do NOT open a public GitHub issue.**  
Use the private security channel:

~~~~~text
security@kansasfrontiermatrix.org
~~~~~

Include:

- Summary + suspected **CWE/CVE**  
- Estimated **CVSS v3.1** score  
- Affected modules / files  
- Steps to reproduce + PoC  
- Logs / environment details  
- Disclosure preference (credited or anonymous)

**SLA:**  
- Acknowledgement: **≤ 72 hours**  
- Fix plan: **≤ 10 business days**

PGP-encrypted reports available on request.

---

## 🔒 Responsible Disclosure Process

- No public disclosure before a **patch is released**  
- Researchers may be credited (with consent)  
- Fixes validated in CI  
- Security notes logged in CHANGELOG + SBOM  
- Default embargo: **30 days** (severity-dependent)

---

## 🧭 Severity, Triage & Remediation

| Severity | Examples | Triage SLA | Fix SLA |
|---------|----------|------------|---------|
| 🚨 **CRITICAL** | RCE, auth bypass, secrets exposure, supply-chain compromise | 24h | 7 days |
| 🔥 **HIGH** | Priv escalation, sensitive data exposure | 48h | 14 days |
| ⚠️ **MEDIUM** | XSS/CSRF, moderate leakage | 5 days | 30 days |
| ℹ️ **LOW** | Misconfigs, audit noise | 10 days | 45 days |

**Critical CVEs & CodeQL findings block merges instantly.**

---

## ⚙️ Workflow → Security Artifact Mapping

| Workflow | Purpose | Artifact |
|----------|----------|----------|
| `codeql.yml` | Static analysis | `reports/security/codeql/*.sarif` |
| `trivy.yml` | Image/lockfile CVE scan | `reports/security/trivy/*.json` |
| `faircare-validate.yml` | Ethical metadata checks | `reports/fair/faircare_summary.json` |
| `docs-lint.yml` | Documentation compliance | `reports/self-validation/docs/lint_summary.json` |
| `ai-model-audit.yml` | Bias/drift/explainability | `reports/audit/ai_model_faircare.json` |
| `telemetry-export.yml` | Build/security metrics | `../releases/v10.3.0/focus-telemetry.json` |

---

## 🛡️ Secure Development Practices

### 🔐 General
- Signed commits/tags (GPG/SSH)  
- No plaintext secrets (GitHub Encrypted Secrets + OIDC)  
- Dependabot + pinned versions  
- Two approvals for sensitive PRs  
- deterministic SLSA-compliant builds  

### 🐳 Containers
- Minimal, non-root images  
- Mandatory Trivy scan  
- Digest-pinned dependencies  

### 🔑 Secrets
- Rotation ≤ 90 days  
- Scoped tokens  
- Access logs reviewed quarterly  

---

## 🧮 Security Architecture (CI-First)

~~~~~mermaid
flowchart TD
  A["Developer Commit / PR"] --> B["Pre-Commit Hooks"]
  B --> C["CI: Validate (STAC · FAIR+CARE · Docs)"]
  C --> D["CI: Security (CodeQL · Trivy)"]
  D --> E["CI: Build & Deploy"]
  E --> F["Telemetry Export & SBOM Attestation"]
  D --> G["Security Reports (SARIF / CVE)"]
  C --> H["Governance Ledgers (FAIR+CARE Council)"]
~~~~~

Immutable governance ledgers:

- `../docs/reports/audit/github_workflows_ledger.json`  
- `../docs/reports/audit/governance_ledger.json`  
- `../docs/reports/audit/release-manifest-log.json`  

---

## 🔗 Supply Chain Provenance & SBOMs

| File | Purpose |
|------|---------|
| `../releases/v10.3.0/sbom.spdx.json` | SPDX dependency graph |
| `../releases/v10.3.0/manifest.zip` | Release manifest + checksums |
| `../releases/v10.3.0/focus-telemetry.json` | Telemetry + security metrics |
| `../docs/reports/audit/release-manifest-log.json` | Release chain ledger |
| `../releases/v10.3.0/bom.cdx.json` | Optional CycloneDX SBOM |

SBOMs ensure:

- One-hop verification  
- Independent reproducibility  
- Total dependency transparency  

---

## ⚖️ FAIR+CARE Security Governance

| Principle | Implementation |
|----------|----------------|
| **Findable** | Issues + IDs + ledger refs |
| **Accessible** | Post-patch notes; open schemas |
| **Interoperable** | SPDX/CycloneDX/JSON-LD |
| **Reusable** | SLSA provenance + reproducibility |
| **CARE** | Consent, sovereignty, minimal harm |

---

## 🔁 Branch Protection & Access Controls

| Control | Policy |
|--------|--------|
| Reviews | ≥ 2 approvals |
| Status Checks | All workflows green |
| Signing | Required |
| Force Push | Disabled |
| Access | Least-privilege |
| Audit Trail | Full ledger + CI run IDs |

---

## 📮 Security Contacts

| Topic | Contact | SLA |
|--------|---------|---------|
| Vulnerabilities | security@kansasfrontiermatrix.org | 72h |
| Governance/Ethics | governance@kansasfrontiermatrix.org | 5 days |
| Data Breach | FAIR+CARE Council | 48h |
| General | GitHub Discussions | Ongoing |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | FAIR+CARE Council · DevSecOps | Updated to v10.3; new telemetry schema; refined severity & provenance. |
| v10.2.2 | 2025-11-12 | DevSecOps | CVSS guidance; updated rotation policy; new ledger references. |
| v10.0.0 | 2025-11-09 | A. Barta | Added AI audit workflow; SLSA provenance; CycloneDX option. |
| v9.7.0 | 2025-11-05 | A. Barta | Unified FAIR+CARE-aligned security policy. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
Maintained under **Master Coder Protocol v6.3**  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Documentation Index](../docs/README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
```
