<div align="center">

# 🔒 Kansas-Frontier-Matrix — Security Policy  
### `.github/SECURITY.md`

**Mission:** Protect the integrity of Kansas-Frontier-Matrix by  
providing a clear process for reporting vulnerabilities,  
coordinating fixes, and practicing **MCP-grade security hygiene**.

<!-- Core security CI -->
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../actions/workflows/codeql.yml)
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../actions/workflows/trivy.yml)
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](../../actions/workflows/secret-scanning.yml)

<!-- Dependency hygiene -->
[![Dependabot Updates](https://img.shields.io/badge/Dependabot-enabled-brightgreen?logo=dependabot)](../../network/updates)
[![Dependabot Alerts](https://img.shields.io/badge/Alerts-View%20in%20Security%20tab-orange?logo=github)](../../security/dependabot)

<!-- Ecosystem / posture -->
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/bartytime4life/Kansas-Frontier-Matrix/badge)](https://securityscorecards.dev/viewer/?uri=github.com/bartytime4life/Kansas-Frontier-Matrix)
[![License](https://img.shields.io/github/license/bartytime4life/Kansas-Frontier-Matrix?color=0A7BBB)](../../blob/main/LICENSE)

<!-- Optional / enable then uncomment
[![OSV Scanner](https://img.shields.io/badge/OSV%20Scanner-enabled-0A7BBB?logo=open-source-initiative)](https://osv.dev/)
[![SBOM](https://img.shields.io/badge/SBOM-available-0A7BBB?logo=dependabot)](../../releases)
[![CIS Benchmarks](https://img.shields.io/badge/CIS%20Benchmarks-in%20CI-0A7BBB)](#)
-->

</div>

---

## 🔄 Vulnerability Report Lifecycle

```mermaid
flowchart TD
  A["Researcher finds issue"] --> B["🔐 Private report\nsecurity@kansasfrontier.org or GitHub advisory"]
  B --> C["⏱️ Acknowledgment\nwithin 72h"]
  C --> D["🧮 CVSS triage\nseverity + scope"]
  D --> E["🛠️ Mitigation\ntoken revoke · artifact quarantine"]
  E --> F["🔧 Patch & tests\nbackport if needed"]
  F --> G["📢 Advisory & release notes\ncredit researcher unless anonymous"]
````

<!-- END OF MERMAID -->

---

## 📌 Supported Versions

* ✅ `main` branch — security fixes always applied
* ⏳ Older tags/branches — patches not guaranteed

---

## 📨 How to Report

⚠️ **Do NOT open a public issue for vulnerabilities.**

**Preferred channels**

* 📧 `security@kansasfrontier.org`
* 🔐 Private GitHub security advisory

**Include details**

* Affected files/paths + commit SHA(s)
* Repro steps / PoC (minimal & safe)
* Impact (e.g., RCE, token leak, supply-chain)
* Environment info (OS, Python/Node versions)
* Suggested mitigations (optional)

**Response targets**

* 📨 Acknowledgment → **within 72h**
* 🛠️ Initial triage/mitigation → **≤ 7 days** (severity-dependent)
* 🔧 Full fix/advisory → prioritized by severity

If your report involves **exposed secrets**, say so clearly — we will **rotate tokens immediately**.

---

## 🎯 Scope

**In scope**

* Repository code: `src/`, `scripts/`, `web/`
* GitHub Actions: `.github/workflows/**`
* Container files: `docker/**`, `Dockerfile`, `docker-compose.yml`
* Data pipelines, STAC validation, render CLIs
* Docs build chain (where exploitable in CI/site builds)

**Out of scope**

* Dataset content/accuracy (e.g., historical OCR noise)
* Vulnerabilities in upstream dependencies (report upstream; we patch/pin locally as needed)

---

## 🤝 Safe Harbor (Responsible Testing)

We welcome good-faith research that:

* Avoids privacy violations, data exfiltration, or service disruption
* Respects rate limits (no DoS/flooding)
* Keeps PoCs local/offline (the site is static)
* Does **not** target third-party services without consent

If you follow these rules, we will not pursue action under law or ToS.

---

## 🧮 Severity (CVSS v3.1 Guidance)

|    Severity | Examples in repo                              | Target response        |
| ----------: | --------------------------------------------- | ---------------------- |
| 🔴 Critical | RCE in CLI/scripts; supply-chain takeover     | Hotfix ASAP + advisory |
|     🟠 High | Token leak; path traversal → overwrite        | Patch ≤ 7 days         |
|   🟡 Medium | Script injection in docs/build; weak defaults | Patch in next release  |
|      🟢 Low | Non-exploitable hardening gap                 | Backlog + tracking     |

---

## 🛡️ Current Security Practices

**CI & Scanning**

* CodeQL → Python + JS/TS (`codeql.yml`)
* Trivy → FS/config/image scans (`trivy.yml`)
* Secret scanning → `gitleaks`/credential detectors (`secret-scanning.yml`)

**Least-Privilege CI**

* Minimal workflow permissions
* Concurrency guards to prevent duplicate runs

**Supply-Chain Hygiene**

* Pinned base images (`docker/`)
* `.dockerignore` / `.gitignore` exclude unsafe artifacts
* JSON Schema validation for configs (legends, sources, categories)
* Dependabot (daily) for Actions, npm, pip, Docker

**Reproducibility**

* Deterministic Make targets (`make prebuild`, `make stac-validate`)
* SHA-256 checksums + metadata sidecars for artifacts
* Optional SBOM workflow referenced in advisories (if enabled)

---

## 🔧 Maintainer Response Flow

1. **Acknowledge** → CVSS assessment (CVE if applicable)
2. **Mitigate** → revoke tokens, quarantine artifacts, disable risky jobs
3. **Fix** → patch + tests, hardening, backport if needed
4. **Disclose** → GitHub advisory + release notes; credit researcher (unless anonymous)

---

## 📢 Coordinated Disclosure

* Keep details private until a fix is released
* Publish advisory + release notes after patch
* Researchers credited unless anonymity requested

---

## 🧩 Snippets (for Maintainers)

**Minimal workflow permissions & concurrency**

```yaml
permissions:
  contents: read
  actions: none
  checks: write
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

**Example Dependabot group (npm/web)**

```yaml
- package-ecosystem: npm
  directory: /web
  schedule:
    interval: weekly
  groups:
    minor-and-patch:
      patterns: ["*"]
      update-types: ["minor", "patch"]
```

---

## 📬 Contact

* 📨 Sensitive reports → `security@kansasfrontier.org` or private advisory
* 💬 General questions → Discussions or Issues

🙏 Thank you for helping keep Kansas-Frontier-Matrix safe for everyone.
