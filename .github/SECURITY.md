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

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Security Status" src="https://img.shields.io/badge/Security-Monitored-success" />

</div>


---

## 📘 Overview

Security in KFM follows a **transparency → prevention → reproducibility** model, using:

- **OWASP Top 10**  
- **NIST SSDF (SP 800-218)**  
- **SLSA 1.0 Provenance Requirements**  
- **GitHub Advanced Security**  
- **FAIR+CARE Ethics**  

All CI/CD and security outputs converge into:

    ../releases/v10.3.0/focus-telemetry.json

Artifacts referenced via:

- `../releases/v10.3.0/sbom.spdx.json`  
- `../releases/v10.3.0/manifest.zip`  

ensuring one-hop supply chain verifiability.

---

## 🧩 Scope

This policy covers:

- **All monorepo code:** `src/`, `web/`, `data/`, `tools/`, `.github/`  
- **Workflows:** `.github/workflows/**`  
- **Runtime artifacts:** Docker images, static web deployment, API services  
- **Ecosystem components:** Neo4j, FastAPI/GraphQL, React/MapLibre/Cesium, STAC/DCAT cataloging  

---

## 🚨 Reporting a Vulnerability (CVD)

**Do NOT file a public GitHub issue.**  
Private, secure reporting channel:

    security@kansasfrontiermatrix.org

Include when possible:

- Summary + suspected **CWE/CVE**
- Estimated **CVSS v3.1** score
- Affected paths or modules
- Steps to reproduce + PoC
- Log output and environment details  
- Disclosure preference (credit or anonymous)

**SLA:**  
- Acknowledgement: **within 72 hours**  
- Fix plan: **within 10 business days**  

Encrypted communication available on request (PGP preferred).

---

## 🔒 Responsible Disclosure Process

- No public disclosure until a **patch/release** is available  
- Researchers may be credited (with consent)  
- Fixes validated in CI  
- Security notes embedded in CHANGELOG + SBOM  
- Embargo default: **30 days** (severity-dependent)

---

## 🧭 Severity, Triage & Remediation

| Severity | Criteria (Examples) | Triage SLA | Fix SLA |
|----------|---------------------|-----------|---------|
| 🚨 **CRITICAL** | RCE, auth bypass, secrets exposure, supply-chain compromise | 24h | 7 days |
| 🔥 **HIGH** | Privilege escalation, sensitive data exposure | 48h | 14 days |
| ⚠️ **MEDIUM** | XSS/CSRF, moderate leakage | 5 days | 30 days |
| ℹ️ **LOW** | Misconfigs, non-exploitable issues | 10 days | 45 days |

➡️ **CRITICAL CVEs and CRITICAL CodeQL findings block merges immediately.**

---

## ⚙️ Workflow → Security Artifact Mapping

| Workflow | Purpose | Artifact Output |
|----------|----------|------------------|
| `codeql.yml` | Static analysis | `reports/security/codeql/*.sarif` |
| `trivy.yml` | Image/lockfile CVE scan | `reports/security/trivy/*.json` |
| `faircare-validate.yml` | Ethical metadata & consent checks | `reports/fair/faircare_summary.json` |
| `docs-lint.yml` | Markdown/policy compliance | `reports/self-validation/docs/lint_summary.json` |
| `ai-model-audit.yml` | Bias + drift + explainability logs | `reports/audit/ai_model_faircare.json` |
| `telemetry-export.yml` | Aggregated build/security metrics | `../releases/v10.3.0/focus-telemetry.json` |

---

## 🛡️ Secure Development Practices

### 🔐 General Rules  
- **Signed commits and tags** (GPG/SSH)  
- **No plaintext secrets**—use GitHub Encrypted Secrets + OIDC  
- **Dependency locks** maintained and auto-updated (Dependabot)  
- **Two approvals** for security-sensitive PRs  
- **Reproducible, deterministic builds** (SLSA-compliant)

### 🐳 Containers  
- Use minimal, non-root base images  
- Mandatory Trivy scan (CRITICAL ⇒ block)  
- Digest-pinned images (no `latest` tags)

### 🔑 Secrets  
- Rotation ≤ 90 days  
- Scoped credentials only  
- Secret access audited via GitHub logs  

---

## 🧮 Security Architecture (CI-First) — Indented Mermaid

    flowchart TD
      A["Developer Commit / PR"] --> B["Pre-Commit Hooks"]
      B --> C["CI: Validate (STAC · FAIR+CARE · Docs)"]
      C --> D["CI: Security (CodeQL · Trivy)"]
      D --> E["CI: Build & Deploy"]
      E --> F["Telemetry Export & SBOM Attestation"]
      D --> G["Security Reports (SARIF / CVE)"]
      C --> H["Governance Ledgers (FAIR+CARE Council)"]

Immutable governance ledgers:

- `../docs/reports/audit/github_workflows_ledger.json`  
- `../docs/reports/audit/governance_ledger.json`  
- `../docs/reports/audit/release-manifest-log.json`  

---

## 🔗 Supply Chain Provenance & SBOMs

| File | Purpose |
|------|---------|
| `../releases/v10.3.0/sbom.spdx.json` | Full SPDX inventory + dependency graph |
| `../releases/v10.3.0/manifest.zip` | Release manifest + checksums |
| `../releases/v10.3.0/focus-telemetry.json` | Telemetry, security, sustainability |
| `../docs/reports/audit/release-manifest-log.json` | Immutable release chain ledger |
| *(Optional)* `../releases/v10.3.0/bom.cdx.json` | CycloneDX SBOM |

SBOM exports ensure:

- One-hop verification  
- Decentralized reproducibility  
- Full dependency transparency  

---

## ⚖️ FAIR+CARE Security Governance

| Principle | Implementation |
|----------|----------------|
| **Findable** | Issues tracked with IDs + ledger references |
| **Accessible** | Public post-patch summaries; open schemas |
| **Interoperable** | SPDX/CycloneDX/JSON-LD linkages |
| **Reusable** | SLSA attestations + reproducible builds |
| **CARE** | Avoid harm; enforce consent + cultural sensitivity |

---

## 🔁 Branch Protection & Access Controls

| Control | Policy |
|---------|--------|
| Reviews | ≥ 2 reviewer approvals |
| Status Checks | All workflows green |
| Signing | Required for commits/tags |
| Force Push | Disabled on `main` |
| Access | Least-privilege; scoped tokens |
| Audit Trail | Full ledger + CI run IDs |

---

## 📮 Security Contacts

| Topic | Contact | SLA |
|--------|---------|-----|
| Vulnerabilities | `security@kansasfrontiermatrix.org` | 72 hours |
| Ethics/Governance | `governance@kansasfrontiermatrix.org` | 5 business days |
| Data Breach | FAIR+CARE Council | 48 hours triage |
| General Support | GitHub Discussions | Ongoing |

---

## 🕰️ Version History

| Version | Date       | Author           | Summary |
|----------|------------|------------------|---------|
| v10.3.1 | 2025-11-13 | DevSecOps & FAIR+CARE Council | Updated to v10.3 telemetry, governance references, indented diagram compliance. |
| v10.2.2 | 2025-11-12 | DevSecOps        | Severity matrix, CVSS guidance, OIDC rotation policy, ledger references. |
| v10.0.0 | 2025-11-09 | A. Barta         | Added AI audit workflow, sustainability telemetry, CycloneDX note, SLSA provenance chain. |
| v9.7.0  | 2025-11-05 | A. Barta         | Unified security policy with FAIR+CARE automation. |
| v9.5.0  | 2025-10-20 | KFM Core Team    | Added Trivy scanning + SBOM attestation. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to CI/CD Overview](README.md) · [Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>