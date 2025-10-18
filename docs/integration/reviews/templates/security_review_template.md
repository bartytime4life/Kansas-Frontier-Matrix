<div align="center">

# 🔐 Kansas Frontier Matrix — **Security & Compliance Review Template**  
`docs/integration/reviews/templates/security_review_template.md`

**Purpose:** Standardize the **security, compliance, and vulnerability review process**  
for all **code, data pipelines, dependencies, and infrastructure components** in the  
**Kansas Frontier Matrix (KFM)** — ensuring all integrations meet **MCP-DL v6.3**,  
**Zero-Trust**, and **Policy-as-Code (OPA/Conftest)** security frameworks before deployment.

[![Security · Trivy](https://img.shields.io/badge/Security-Trivy-blue)](../../../../../.github/workflows/trivy.yml)
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../../.github/workflows/codeql.yml)
[![Policy-as-Code](https://img.shields.io/badge/policy-OPA%2FConftest-purple)](../../../../../.github/workflows/policy-check.yml)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../../LICENSE)

</div>

```yaml
---
title: "Security & Compliance Review Template"
document_type: "Review Template · Security"
version: "v1.0.0"
last_updated: "2025-10-18"
created: "2025-10-04"
owners: ["@kfm-security","@kfm-devops","@kfm-architecture","@kfm-review-board"]
status: "Stable"
maturity: "Production"
scope: "Docs/Integration/Reviews/Templates"
license: "CC-BY 4.0"
tags: ["review","security","compliance","policy-as-code","trivy","codeql","governance"]
audit_framework: "MCP-DL v6.3"
---
````

---

## 🧭 Overview

This template governs the **security and compliance review** of all KFM components —
including **source code, containers, pipelines, datasets, and external dependencies.**

Security reviews ensure each contribution maintains the **integrity, provenance, and confidentiality**
of the project’s data and infrastructure, following the principles of **defense-in-depth** and
**continuous security validation.**

> Once completed, save this review as
> `docs/integration/reviews/logs/YYYY-MM-DD_<component>_securityreview.md`
> and update the central `audit-index.json`.

---

## 🧱 Component Information

| Field              | Description                                | Example                             |
| :----------------- | :----------------------------------------- | :---------------------------------- |
| **Component Name** | Repository or artifact name                | `terrain_pipeline.py`               |
| **Type**           | Code / Model / Container / Dataset / Infra | `Container (Docker)`                |
| **Reviewer(s)**    | Assigned security reviewers                | `@kfm-security`, `@kfm-devops`      |
| **Date**           | ISO 8601                                   | `2025-10-18`                        |
| **CI Build ID**    | Optional                                   | `#1684`                             |
| **Location**       | Path or registry                           | `ghcr.io/bartytime4life/kfm:latest` |

---

## 🛡️ Security Validation Checklist

| Check                           | Description                                                 | Status |
| :------------------------------ | :---------------------------------------------------------- | :----- |
| [ ] **CodeQL Scan**             | Completed successfully; no CRITICAL/HIGH issues unresolved. |        |
| [ ] **Trivy SCA/SBOM**          | No CRITICAL vulnerabilities in base image/dependencies.     |        |
| [ ] **Dependency Pinning**      | All dependencies version-pinned; no floating versions.      |        |
| [ ] **OPA Policy Check**        | `make policy-check` passes; no failed assertions.           |        |
| [ ] **GitHub Actions Security** | All actions pinned by tag/SHA; no unverified sources.       |        |
| [ ] **Container Hardening**     | Non-root user, minimal base image, updated packages.        |        |
| [ ] **Secrets Audit**           | No credentials/API keys present in code or history.         |        |
| [ ] **Access Policy**           | `access_policy:` YAML block defined and appropriate.        |        |
| [ ] **License Compatibility**   | Dependencies meet CC-BY/MIT compatibility standards.        |        |
| [ ] **Network & Ports**         | Services restrict open ports to documented ones only.       |        |

---

## 🧩 Infrastructure & CI/CD Security

| Check                                  | Description                                                     | Status |
| :------------------------------------- | :-------------------------------------------------------------- | :----- |
| [ ] **CI/CD Workflow Isolation**       | Separate tokens and least-privilege scopes.                     |        |
| [ ] **Artifact Integrity**             | Checksum `.sha256` verified for all built artifacts.            |        |
| [ ] **Build Reproducibility**          | Deterministic container builds (same hash).                     |        |
| [ ] **Supply Chain Provenance (SLSA)** | Build provenance metadata (SLSA level ≥2).                      |        |
| [ ] **Signing & Verification**         | GPG or cosign signatures for release artifacts.                 |        |
| [ ] **Retention Policy**               | Artifacts expire or are archived per `preservation_policy`.     |        |
| [ ] **Audit Logs**                     | GitHub + CI logs preserved in `docs/integration/reviews/logs/`. |        |

---

## 🔒 Data & Privacy Controls

| Check                                   | Description                                               | Status |
| :-------------------------------------- | :-------------------------------------------------------- | :----- |
| [ ] **Data Sensitivity Classification** | `classification.sensitivity:` assigned (low/medium/high). |        |
| [ ] **PII Handling**                    | No personally identifiable data; anonymization verified.  |        |
| [ ] **Encryption at Rest**              | Sensitive files encrypted or stored in protected vaults.  |        |
| [ ] **Encryption in Transit**           | HTTPS enforced; no unencrypted endpoints.                 |        |
| [ ] **Public Access Review**            | Open datasets reviewed for exposure risks.                |        |
| [ ] **Dataset License Enforcement**     | Proper redistribution rights confirmed.                   |        |
| [ ] **Data Integrity**                  | Hash checks; tampering detection mechanisms active.       |        |

---

## ⚖️ Compliance & Governance

| Check                         | Description                                            | Status |
| :---------------------------- | :----------------------------------------------------- | :----- |
| [ ] **MCP-DL Compliance**     | Documented under correct MCP-DL v6.3 classification.   |        |
| [ ] **Ethical Access Policy** | Cultural/tribal datasets follow restricted-access SOP. |        |
| [ ] **Regulatory Alignment**  | Meets FAIR data and NASA open-science principles.      |        |
| [ ] **Preservation Policy**   | Aligns with repo preservation settings (Zenodo/OSF).   |        |
| [ ] **License Attribution**   | SPDX license headers correct in all files.             |        |
| [ ] **Review Evidence**       | CI artifacts + logs attached to PR.                    |        |

---

## 🧮 Tools & Commands Used

```bash
# Run automated scans before submission
make codeql-scan
make trivy-scan
make policy-check
make sbom

# Generate SBOM
trivy sbom --format spdx-json --output sbom.json .

# Verify artifacts
sha256sum -c data/checksums/*.sha256
```

> All validation logs should be archived in `data/work/logs/security/` or attached as CI artifacts.

---

## 🧾 Reviewer Summary

| Field                | Notes                                                    |
| :------------------- | :------------------------------------------------------- |
| **Findings**         |                                                          |
| **Actions Required** |                                                          |
| **Follow-up Tasks**  |                                                          |
| **Decision**         | ☐ Approved  ☐ Conditional Approval  ☐ Revisions Required |

---

## 🗃 YAML Review Record (Append to Audit Log)

```yaml
component: kfm_terrain_pipeline
review_type: security
reviewers: ["@kfm-security","@kfm-devops"]
status: approved
validation:
  codeql: pass
  trivy: pass
  opa: pass
  secrets: none_found
  license: verified
notes: "Pipeline container validated; no critical CVEs; all actions pinned by SHA."
timestamp: 2025-10-18T16:00:00Z
```

---

## 🔗 References

* [`docs/integration/reviews/checklist.md`](../checklist.md) — Review Board Checklist
* [`docs/standards/markdown_rules.md`](../../../standards/markdown_rules.md) — Documentation standards
* [`docs/architecture/data-architecture.md`](../../../architecture/data-architecture.md) — Infrastructure overview
* [`docs/standards/metadata.md`](../../../standards/metadata.md) — Provenance & metadata schemas
* [`docs/integration/reviews/logs/`](../logs/) — Audit trail for all reviews

---

<div align="center">

### 🔐 “Security is not a gate — it’s the guardrail that keeps knowledge safe.”

**Kansas Frontier Matrix Security & Compliance Council · MCP-DL v6.3**

</div>
