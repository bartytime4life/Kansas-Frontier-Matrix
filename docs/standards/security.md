<div align="center">

# 🔒 Kansas Frontier Matrix — **Security & Data Protection Standards**  
`docs/standards/security.md`

**Master Coder Protocol (MCP-DL v6.3+) · Secure-by-Design · Supply-Chain Integrity · Provenance · Validation**

[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../docs/)
[![Security Scans](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/trivy.yml?label=Trivy)](../../.github/workflows/trivy.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL&logo=github)](../../.github/workflows/codeql.yml)
[![STAC Validate](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/stac-validate.yml?label=STAC%20Validate)](../../.github/workflows/stac-validate.yml)
[![SBOM](https://img.shields.io/badge/Workflow-sbom.yml-informational)](../../.github/workflows/sbom.yml)
[![SLSA-3 (Target)](https://img.shields.io/badge/Security-SLSA--3%20(Target)-orange)](../standards/security.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Security & Data Protection Standards"
version: "v1.3.0"
last_updated: "2025-10-18"
owners: ["@kfm-security","@kfm-architecture","@kfm-docs"]
tags: ["security","supply-chain","slsa","sbom","codeql","trivy","provenance","ci/cd","mcp"]
status: "Stable"
scope: "Monorepo-Wide"
license: "MIT"
semver_policy: "MAJOR.MINOR.PATCH"
ci_required_checks:
  - trivy
  - codeql
  - stac-validate
  - docs-validate
  - checksums
audit_framework: "MCP-DL v6.3"
semantic_alignment:
  - STAC 1.0 (provenance links)
  - SPDX/CycloneDX (SBOM)
  - SLSA (provenance attestations)
  - ISO 27001-inspired controls (lightweight)
---
````

---

## 📚 Overview

The KFM Security Standards guarantee that software, datasets, and automation are:

* 🔐 **Secure by design** — protected from unauthorized access or tampering
* 🧠 **Reproducible with integrity** — checksums & attestations for verifiable rebuilds
* 🌍 **Open yet governed** — transparency without compromising policy & provenance
* 🧾 **Auditable** — changes, validations, and scans are logged & reviewable

Layers of control cover **repository governance**, **CI/CD supply-chain**, **dependencies & images**, **data classification**, **access & secrets**, and **logging/IR**.

---

## 🧭 Threat Model (concise)

| Vector                | Examples                                           | Controls                                                                            |
| :-------------------- | :------------------------------------------------- | :---------------------------------------------------------------------------------- |
| **Supply chain**      | Malicious deps, unpinned actions, base image drift | SBOM + SHA pins; Trivy/CodeQL; digest-pinned images; SLSA attestations              |
| **CI abuse**          | Token exfil, `pull_request_target` misuse          | Least-privilege tokens; read-only defaults; sandbox forks; no secrets in forked PRs |
| **Secrets leakage**   | Keys in code/logs                                  | Pre-commit secret scans; GH masking; Gitleaks (optional)                            |
| **Data tampering**    | Silent STAC/raw edits                              | SHA-256 checks; STAC CI validators; signed releases                                 |
| **Credential misuse** | Over-scoped PATs; shared accounts                  | Fine-grained PATs; role-based access; 2FA required                                  |
| **Container risks**   | Root users, CAP_* perms, CVEs                      | Non-root; drop caps; read-only FS; Trivy; SBOM & policy                             |

---

## 🧩 Security Governance Framework

| Layer                   | Responsibility                 | Control Mechanism                                    |
| :---------------------- | :----------------------------- | :--------------------------------------------------- |
| **Codebase Security**   | Keep unsafe code out of `main` | CodeQL, Bandit, ESLint, pre-commit                   |
| **Dependency Security** | Identify & fix CVEs fast       | Trivy, Dependabot/Renovate, `pip-audit`, `npm audit` |
| **Supply-Chain**        | Trace & verify what we build   | SBOM (SPDX/CycloneDX), SLSA attestations             |
| **Data Integrity**      | Guarantee artifacts unchanged  | `.sha256` sidecars; STAC link validation             |
| **Workflow Security**   | Minimal privs, pinned actions  | GHA permissions, SHA-pinned actions                  |
| **Access Control**      | Enforce least privilege        | Org roles, CODEOWNERS, branch protection             |
| **Auditability**        | Preserve logs & reports        | `data/work/logs/security/` (retained)                |

---

## ⚙️ Secure Development Practices

| Practice               | Description                         | Enforcement                           |
| :--------------------- | :---------------------------------- | :------------------------------------ |
| **Pre-commit hooks**   | Lint, format, secret patterns       | `.pre-commit-config.yaml`             |
| **Code review**        | ≥1 reviewer; CODEOWNERS auto-assign | Branch protection + `CODEOWNERS`      |
| **Verified commits**   | GPG/SSH-signed commits              | Branch rule: “Require signed commits” |
| **Version pinning**    | Pin deps & actions by digest/SHA    | PR checks; Dependabot/Renovate        |
| **No secrets in code** | Secrets only in GHA/KMS             | Pre-commit & optional Gitleaks        |
| **Secure defaults**    | Least privilege perms, file modes   | CI checks & hardening scripts         |

**Sample `CODEOWNERS`**

```
/docs/standards/ @kfm-security @kfm-docs
/src/**           @kfm-security @kfm-core
/.github/**       @kfm-security
```

---

## 🔗 Supply-Chain Security (SBOM · SLSA · Attestation)

* **SBOM**: Generate CycloneDX or SPDX for Python/Node; attach to releases.
* **Actions pinned**: Use commit SHAs; deny unpinned steps in `make verify-actions`.
* **GHA permissions**: Defaults to read-only; selectively elevate per job.
* **SLSA**: Build attestations stored under `data/work/logs/security/attestations/`.
* **Containers**: Digest-pinned base images, signed (optional via **cosign**).

**Make targets**

```bash
make sbom            # Generate SBOMs for src/ and web/
make attest          # Emit SLSA-style provenance JSON
make verify-actions  # Lint workflows for unpinned actions
```

---

## 📦 Dependency & Vulnerability Management

| Tool                          | Function                      | Schedule        |
| :---------------------------- | :---------------------------- | :-------------- |
| **Trivy**                     | CVE scan: deps/containers/IaC | Weekly + PR     |
| **Dependabot/Renovate**       | Safe version bumps            | Daily           |
| **CodeQL**                    | Static analysis (SAST)        | PR + weekly     |
| **Bandit**                    | Python security linter        | Pre-commit + PR |
| **`pip-audit` / `npm audit`** | Dependency CVEs               | PR              |
| **Gitleaks** (optional)       | Secret detection              | Pre-commit + PR |

**Commands**

```bash
trivy fs .
bandit -r src/
pip-audit
npm audit --audit-level=moderate
```

Reports stored in:

```
data/work/logs/security/
├── trivy_report.json
├── codeql_alerts.json
├── bandit_summary.log
└── sbom/
```

---

## 🧱 Container Hardening

* Minimal **digest-pinned** base image (distroless/alpine).
* **Non-root** user (`USER 10001:10001`); read-only FS; writable `/tmp` only.
* **Capabilities**: `--cap-drop=ALL`; seccomp & AppArmor profiles where applicable.
* **Network**: Minimal egress in CI; no inbound unless necessary.
* **HEALTHCHECK** for services.

**Dockerfile**

```dockerfile
FROM python:3.12-slim@sha256:<digest>
RUN useradd -u 10001 -m kfm
USER 10001:10001
WORKDIR /app
COPY --chown=10001:10001 requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=10001:10001 . .
CMD ["python","-m","src.cli"]
```

---

## 🔐 Data Security — Classification · Integrity · Encryption

### Classification

| Tier           | Description           | Examples                    | Rules                                                              |
| :------------- | :-------------------- | :-------------------------- | :----------------------------------------------------------------- |
| **Public**     | Open, redistributable | Public datasets, docs, code | Default; STAC indexed                                              |
| **Restricted** | License/embargo       | Time-limited scans          | Maintainers only; encrypt at rest if required                      |
| **Sensitive**  | PII or legal          | None expected               | Prohibited; if unavoidable, encrypt & segregate; removal preferred |

> KFM avoids PII. Any detected PII triggers redaction and the incident workflow.

### Integrity & Provenance

* **SHA-256** sidecars for all artifacts (`data/checksums/**`).
* **STAC Items/Collections** must link to checksums & lineage.
* Validation logs retain **commit hashes**.

### Encryption

* **At rest**: AES-256 (KMS or GH Secrets).
* **In transit**: TLS for downloads/APIs.
* **Rotation**: Every 6 months; immediate on incident.

---

## 🧠 Access Control & Governance

| Role                 | Access         | Description                                 |
| :------------------- | :------------- | :------------------------------------------ |
| **Core Maintainers** | Admin          | Approve PRs, releases, CI secrets, policies |
| **Contributors**     | Write (scoped) | PRs & tests; no prod secrets                |
| **Automations**      | Minimal tokens | Job-scoped `GITHUB_TOKEN`                   |
| **Public**           | Read           | Code & published data                       |

**Policies**

* Protected branches (`main`, `release/*`): **passing checks + code review** required.
* Required statuses: CodeQL, Trivy, **checksums**, **STAC validate**, pre-commit.
* **2FA required**; fine-grained PATs only; **no classic tokens**.

---

## 🔒 Secrets & Credential Management

| Secret Type     | Storage             | Policy                           |
| :-------------- | :------------------ | :------------------------------- |
| API Keys        | GH Actions Secrets  | Least privilege; masked; rotated |
| Encryption Keys | GH Secrets / KMS    | Rotate ≥ every 6 months          |
| PATs            | Organization-level  | Fine-grained, short-lived        |
| Dataset Tokens  | `.env` (gitignored) | Used only by `make fetch-raw`    |

**Rules**

* No secrets in code, STAC, or commits.
* GH logs auto-mask secrets.
* Access events reviewed quarterly.

---

## 🧱 CI/CD Workflow Security

Global defaults (recommended in every workflow):

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
      id-token: write   # only if OIDC/signing is needed
    steps:
      - uses: actions/checkout@<SHA>
        with: { fetch-depth: 1 }
      # pinned actions only...
```

| Workflow            | Security Measures                     | Description                 |
| :------------------ | :------------------------------------ | :-------------------------- |
| `fetch.yml`         | Verify manifest sigs & checksums      | Blocks tampered sources     |
| `stac-validate.yml` | Read-only FS; containerized validator | Prevents metadata tampering |
| `checksums.yml`     | Recompute & compare SHA-256           | Detects corruption          |
| `codeql.yml`        | SAST on PR                            | Flags unsafe code           |
| `trivy.yml`         | CVE scan for fs/images                | Weekly baseline + PR gate   |
| `sbom.yml`          | Generate SBOM & attach to release     | Supply-chain traceability   |
| `attest.yml`        | Emit SLSA-style attestations          | Repro provenance            |

> Never expose secrets to `pull_request` jobs from forks; prefer sandboxed `pull_request` with read-only permissions.

---

## 🧪 Security Validation & CI Enforcement

| Validation      | Tool/Workflow                   | Gate            |
| :-------------- | :------------------------------ | :-------------- |
| Static analysis | CodeQL, Bandit                  | PR required     |
| Dependencies    | Trivy, `pip-audit`, `npm audit` | PR + weekly     |
| Secrets         | Gitleaks (optional)             | PR              |
| Checksums       | `make checksums`                | Dataset updates |
| STAC            | `stac-validate.yml`             | PR              |
| SBOM            | `sbom.yml`                      | Release         |

Quarterly manual audit:

* Review `data/work/logs/security/`
* Check branch protections & secret access logs
* Rotate keys as scheduled

---

## 🚨 Incident Response & Recovery

| Step                | Action                                                 | Owner                       |
| :------------------ | :----------------------------------------------------- | :-------------------------- |
| **1️⃣ Detect**      | CI alert or external report                            | Security lead / Maintainers |
| **2️⃣ Contain**     | Freeze branch/dataset; revoke secrets                  | Core Team                   |
| **3️⃣ Investigate** | Triage CVSS; review logs/commits                       | Sec + Governance            |
| **4️⃣ Remediate**   | Patch, rotate keys, rebuild & re-hash                  | Maintainers                 |
| **5️⃣ Document**    | File report under `data/work/logs/security/incidents/` | Governance                  |
| **6️⃣ Learn**       | Update SOPs, playbooks, tests                          | Docs Lead                   |

**RTO/RPO guidance**: RTO ≤ 24h for public site; RPO ≤ 1h for metadata.

---

## 🧰 Copy-Paste Security Policy Files

**`SECURITY.md` (vuln disclosure at repo root)**

```markdown
# Security Policy

## Supported Versions
Security fixes are applied to `main` and the latest release line.

## Reporting a Vulnerability
Email security@kfm.org with details and proof-of-concept within a private channel.
Acknowledgement in ≤72 hours. Do **not** open public issues for untriaged vulnerabilities.

## Disclosure
We follow coordinated disclosure. Credits provided upon request.
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                                |
| :---------------------- | :------------------------------------------------------------ |
| **Documentation-first** | Security policy & CI hardening codified before execution      |
| **Reproducibility**     | Deterministic builds, checksums, SBOM, attestations           |
| **Open Standards**      | STAC, SPDX/CycloneDX, CodeQL/Trivy, SHA-256                   |
| **Provenance**          | Commit-linked logs; SLSA-style build attestations             |
| **Auditability**        | Logs retained in `data/work/logs/security/` with CI artifacts |

---

## 📎 Related Documentation

| File                             | Description                            |
| :------------------------------- | :------------------------------------- |
| `docs/standards/testing.md`      | Automated & manual testing standards   |
| `docs/standards/coding.md`       | Secure coding & linting practices      |
| `docs/standards/metadata.md`     | STAC + checksum provenance             |
| `docs/standards/data-formats.md` | Approved data/file formats & CI checks |
| `docs/templates/sop.md`          | SOP template for incident response     |
| `.github/workflows/trivy.yml`    | CVE scanning workflow                  |
| `.github/workflows/codeql.yml`   | Static analysis workflow               |

---

## 📅 Version History

| Version | Date       | Author        | Summary                                                                                                                   |
| :------ | :--------- | :------------ | :------------------------------------------------------------------------------------------------------------------------ |
| v1.3.0  | 2025-10-18 | @kfm-security | Added SBOM/SLSA/attestations, container hardening, CI permission lockdown, incident playbook, CODEOWNERS, workflow matrix |
| v1.1.0  | 2025-10-05 | @kfm-security | Expanded dependency policies, PR gates, and secrets guidance                                                              |
| v1.0.0  | 2025-10-04 | @kfm-security | Initial security & vulnerability management standards                                                                     |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every System Secure. Every Check Proven.”*
📍 `docs/standards/security.md` — Official security and access control standards under MCP governance.

</div>
