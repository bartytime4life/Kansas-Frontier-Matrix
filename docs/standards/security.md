<div align="center">

# 🔒 Kansas Frontier Matrix — Security & Data Protection Standards

`docs/standards/security.md`

**Purpose:** Establish unified **security, access control, and vulnerability management policies**
for the **Kansas Frontier Matrix (KFM)** repository — ensuring code, data, and infrastructure
are safeguarded while maintaining **open science transparency** and **MCP compliance**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)
[![Security Scans](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

</div>

---

## 📚 Overview

The **KFM Security Standards** ensure that all software, datasets, and automation workflows are:

* 🔐 **Secure by design** — protected from unauthorized access or tampering
* 🧠 **Reproducible with integrity** — checksums & attestations deliver identical, verifiable rebuilds
* 🌍 **Open yet governed** — transparency without compromising provenance & policy
* 🧾 **Auditable** — every change, validation, and scan is logged & reviewable

Security is implemented through layered controls across:

* Repository governance & branch protection
* CI/CD & supply-chain security (SBOM, SLSA, attestation)
* Dependency & container vulnerability management
* Data classification, integrity, and encryption
* Access, identity, and secret management
* Logging, incident response, and disaster recovery

---

## 🧭 Threat Model (concise)

| Vector                | Examples                                                 | Controls                                                                     |
| :-------------------- | :------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **Supply chain**      | Malicious deps, poisoned actions, base image drift       | SBOM + pin SHAs; Trivy/CodeQL; digest-pinned images; SLSA provenance         |
| **CI abuse**          | Token exfil, PR from forks abusing `pull_request_target` | Least-privilege tokens; read-only defaults; no `pull_request_target` secrets |
| **Secrets leakage**   | Keys in code/logs                                        | Pre-commit secret scans; GHA secret masking; Gitleaks                        |
| **Data tampering**    | Silent edits to STAC or raw assets                       | SHA-256 checks; STAC CI validators; signed releases                          |
| **Credential misuse** | Over-scoped PATs; shared accounts                        | Fine-grained tokens; role-based access; 2FA required                         |
| **Container risks**   | Root users, CAP_* perms, CVEs                            | Non-root; drop caps; read-only FS; Trivy; sbom & policy                      |

---

## 🧩 Security Governance Framework

| Layer                   | Responsibility                     | Control Mechanism                           |
| :---------------------- | :--------------------------------- | :------------------------------------------ |
| **Codebase Security**   | Keep unsafe code out of `main`.    | CodeQL, Bandit, ESLint, pre-commit          |
| **Dependency Security** | Identify & fix CVEs fast.          | Trivy, Dependabot, `pip-audit`, `npm audit` |
| **Supply-Chain**        | Trace & verify what we build.      | SBOM (CycloneDX/SPDX), SLSA attestations    |
| **Data Integrity**      | Guarantee artifacts are unchanged. | `.sha256` checks; STAC link validation      |
| **Workflow Security**   | Minimal privs, pinned actions.     | GHA permissions, SHA-pinned actions         |
| **Access Control**      | Enforce least privilege.           | Org roles, CODEOWNERS, branch protection    |
| **Auditability**        | Preserve logs & reports.           | `data/work/logs/security/` (retained)       |

---

## ⚙️ Secure Development Practices

| Practice               | Description                              | Enforcement                           |
| :--------------------- | :--------------------------------------- | :------------------------------------ |
| **Pre-commit hooks**   | Lint, format, secrets & unsafe patterns. | `.pre-commit-config.yaml`             |
| **Code review**        | ≥1 reviewer; CODEOWNERS auto-assign.     | Branch protection + `CODEOWNERS`      |
| **Verified commits**   | GPG/SSH-signed commits.                  | Branch rule: “Require signed commits” |
| **Version pinning**    | Pin deps & actions by digest/SHA.        | PR checks; renovate/dependabot        |
| **No secrets in code** | Secrets only in GHA vault or env.        | Pre-commit & Gitleaks                 |
| **Secure defaults**    | No world-writable files; minimal perms.  | CI file-mode checks                   |

**Sample `CODEOWNERS`:**

```
# Auto-review for protected areas
/docs/standards/ @kfm-security @kfm-docs
/src/**           @kfm-security @kfm-core
/.github/**       @kfm-security
```

---

## 🔗 Supply-Chain Security (SBOM, SLSA, Attestation)

* **SBOM** generated for Python & Node builds (CycloneDX or SPDX) and attached to releases.
* All GitHub Actions **pinned to commit SHAs** (not tags).
* **actions permissions** default to read-only; jobs elevate minimally when required.
* **SLSA-style provenance**: build attestation artifact (who/what/when) stored under `data/work/logs/security/attestations/`.
* **Container images** built from **digest-pinned** base images (no `:latest`); signed releases (optional, cosign).

**Make targets (example):**

```bash
make sbom            # Generate SBOM (CycloneDX JSON) for src/ and web/
make attest          # Emit build provenance JSON
make verify-actions  # Lint workflows for unpinned actions
```

---

## 📦 Dependency & Vulnerability Management

| Tool                          | Function                         | Schedule        |
| :---------------------------- | :------------------------------- | :-------------- |
| **Trivy**                     | CVE scan: deps, containers, IaC. | Weekly + PR     |
| **Dependabot/Renovate**       | Safe version bumps.              | Daily           |
| **CodeQL**                    | Static analysis (SAST).          | PR + weekly     |
| **Bandit**                    | Python security linter.          | Pre-commit + PR |
| **`pip-audit` / `npm audit`** | Deps CVEs.                       | PR              |
| **Gitleaks** (optional)       | Secret detection.                | Pre-commit + PR |

**Example commands**

```bash
trivy fs .
bandit -r src/
pip-audit
npm audit --audit-level=moderate
```

Results stored in:

```
data/work/logs/security/
├── trivy_report.json
├── codeql_alerts.json
├── bandit_summary.log
└── sbom/
```

---

## 🧱 Container Hardening

* **Base image**: minimal (distroless/alpine), **digest-pinned**.
* **User**: non-root (`USER 10001:10001`).
* **FS**: read-only; writable tmp via `emptyDir`/volume.
* **Capabilities**: `--cap-drop=ALL`; seccomp & AppArmor profiles when applicable.
* **Networking**: minimal egress (CI) & no inbound unless needed.
* **Health**: explicit `HEALTHCHECK` for long-running images.

**Dockerfile snippet**

```dockerfile
FROM python:3.12-slim@sha256:<digest>
RUN useradd -u 10001 -m kfm
USER 10001:10001
WORKDIR /app
COPY --chown=10001:10001 requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=10001:10001 . .
# Read-only root FS assumed by runtime; write to /tmp if needed
CMD ["python","-m","src.cli"]
```

---

## 🔐 Data Security: Classification, Integrity, Encryption

### Data Classification

| Tier           | Description           | Examples                                      | Rules                                                     |
| :------------- | :-------------------- | :-------------------------------------------- | :-------------------------------------------------------- |
| **Public**     | Open, redistributable | Public datasets, docs, code                   | Default; STAC indexed                                     |
| **Restricted** | License or embargo    | Time-limited map scans                        | Access via maintainers; encryption optional               |
| **Sensitive**  | PII or legal          | None expected; if present, remove or minimize | Prohibited from repo; if unavoidable, encrypt & segregate |

> KFM aims to avoid PII. Any detected PII triggers redaction and incident workflow.

### Integrity & Provenance

* **SHA-256 checks** for all artifacts; stored in `data/checksums/**`.
* **STAC Items/Collections** must link to checksums & lineage.
* Validation logs kept with **commit hashes**.

### Encryption (when used)

* **At rest:** AES-256; keys in GitHub Secrets or cloud KMS.
* **In transit:** TLS everywhere (artifact downloads, API calls).
* **Key rotation:** at least every 6 months; on incident — immediate.

---

## 🧠 Access Control & Governance

| Role                 | Access         | Description                                 |
| :------------------- | :------------- | :------------------------------------------ |
| **Core Maintainers** | Admin          | Approve PRs, releases, CI secrets, policies |
| **Contributors**     | Write (scoped) | PRs & tests; no prod secrets                |
| **Automations**      | Minimal tokens | Job-scoped GITHUB_TOKEN permissions         |
| **Public**           | Read           | Code & published data only                  |

**Policies**

* Protected branches: `main`, `release/*` require **passing checks + code review**.
* Required status checks: **CodeQL**, **Trivy**, **checksums**, **STAC validate**, **pre-commit**.
* **2FA required** for all members; **fine-grained PATs** only; no classic tokens.

---

## 🔒 Secrets & Credential Management

| Secret Type     | Storage                 | Policy                           |
| :-------------- | :---------------------- | :------------------------------- |
| API Keys        | GitHub Actions Secrets  | Least privilege; masked; rotated |
| Encryption Keys | GitHub Secrets / KMS    | Rotate every 6 months            |
| PATs            | Organization-level only | Fine-grained, short-lived        |
| Dataset Tokens  | `.env` (ignored)        | Loaded only by `make fetch-raw`  |

**Rules**

* No secrets in code, STAC, or commit messages.
* GHA logs auto-mask secrets.
* Access events reviewed quarterly.

---

## 🧱 CI/CD Workflow Security

**Global defaults (recommended in every workflow):**

```yaml
permissions:
  contents: read
  pull-requests: read
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
jobs:
  build:
    permissions:
      contents: read
      id-token: write   # only if OIDC attestation/signing is used
    steps:
      - uses: actions/checkout@<SHA>
        with: {fetch-depth: 1}
      # ... pinned actions only
```

| Workflow                | Security Measures                                 | Description                 |
| :---------------------- | :------------------------------------------------ | :-------------------------- |
| **`fetch.yml`**         | Verify manifest signatures & checksums            | Blocks tampered sources     |
| **`stac-validate.yml`** | Read-only FS; containerized validator; no secrets | Prevents metadata tampering |
| **`checksums.yml`**     | Recompute & compare SHA-256                       | Detects corruption          |
| **`codeql.yml`**        | SAST on PR                                        | Identifies unsafe code      |
| **`trivy.yml`**         | CVE scan for fs/images                            | Weekly baseline & PR gate   |
| **`sbom.yml`**          | Generate SBOM & attach to release                 | Supply-chain traceability   |
| **`attest.yml`**        | Build attestations (SLSA-style)                   | Repro provenance            |

> Never expose secrets to `pull_request` jobs from forks. Prefer `pull_request` over `pull_request_target` unless you fully sandbox.

---

## 🧪 Security Validation & CI Enforcement

| Validation          | Tool/Workflow                         | Gate               |
| :------------------ | :------------------------------------ | :----------------- |
| **Static analysis** | CodeQL, Bandit                        | PR required status |
| **Dependencies**    | Trivy, `pip-audit`, `npm audit`       | PR + weekly        |
| **Secrets**         | Gitleaks (optional)                   | PR                 |
| **Checksums**       | `make checksums`                      | Dataset updates    |
| **STAC**            | `.github/workflows/stac-validate.yml` | PR                 |
| **SBOM**            | `sbom.yml`                            | Release            |

Quarterly manual audit:

* Review `data/work/logs/security/`
* Check branch protections & secret access logs
* Rotate keys as scheduled

---

## 🚨 Incident Response & Recovery

| Step                | Action                                              | Owner                       |
| :------------------ | :-------------------------------------------------- | :-------------------------- |
| **1️⃣ Detect**      | CI alert or report                                  | Security lead / Maintainers |
| **2️⃣ Contain**     | Freeze branch/dataset; revoke secrets               | Core Team                   |
| **3️⃣ Investigate** | Triage CVSS severity; review logs/commits           | Sec + Governance            |
| **4️⃣ Remediate**   | Patch, rotate keys, rebuild & re-hash               | Maintainers                 |
| **5️⃣ Document**    | File report in `data/work/logs/security/incidents/` | Governance                  |
| **6️⃣ Learn**       | Update SOPs, playbooks, and tests                   | Docs Lead                   |

**RTO/RPO targets (guideline):**

* RTO ≤ 24h for public site; RPO ≤ 1h for metadata changes.

---

## 🧰 Copy-Paste: Security Policy Files

**`SECURITY.md` (vuln disclosure) — create at repo root**

```markdown
# Security Policy

## Supported Versions
Security fixes are applied to `main` and the latest release line.

## Reporting a Vulnerability
Email security@kfm.org with details and proof-of-concept.
Please allow 72 hours for acknowledgement. Do not open public issues for
untriaged vulnerabilities.

## Disclosure
We follow coordinated disclosure. Credits are provided upon request.
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                              |
| :---------------------- | :---------------------------------------------------------- |
| **Documentation-first** | Security policy and CI hardening codified before execution. |
| **Reproducibility**     | Deterministic builds, checksums, SBOM, and attestations.    |
| **Open Standards**      | STAC, SPDX/CycloneDX, CodeQL/Trivy, SHA-256.                |
| **Provenance**          | Commit-linked logs; SLSA-style build attestations.          |
| **Auditability**        | Security logs retained under `data/work/logs/security/`.    |

---

## 📎 Related Documentation

| File                           | Description                                   |
| :----------------------------- | :-------------------------------------------- |
| `docs/standards/testing.md`    | Automated & manual testing standards          |
| `docs/standards/coding.md`     | Secure coding & linting practices             |
| `docs/templates/sop.md`        | SOP template for security & incident response |
| `.github/workflows/trivy.yml`  | CVE scanning workflow                         |
| `.github/workflows/codeql.yml` | Static analysis workflow                      |
| `docs/standards/metadata.md`   | STAC + checksum provenance policies           |

---

## 📅 Version History

| Version | Date       | Author                         | Summary                                                                                      |
| :------ | :--------- | :----------------------------- | :------------------------------------------------------------------------------------------- |
| v1.1    | 2025-10-05 | KFM Security & Governance Team | Added SBOM/SLSA, container hardening, CI permission lockdown, incident playbook, CODEOWNERS. |
| v1.0    | 2025-10-04 | KFM Security & Governance Team | Initial security & vulnerability management standards.                                       |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every System Secure. Every Check Proven.”*
📍 [`docs/standards/security.md`](.) · Official security and access control standards under MCP governance.

</div>
