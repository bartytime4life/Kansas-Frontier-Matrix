# Security Policy

The **Kansas-Frontier-Matrix** project takes security seriously.  
This page explains **how to report vulnerabilities** and **what to expect** from maintainers.

---

## Supported Versions

Security fixes are provided for the **`main`** branch.  
Older tags, forks, or experimental branches may not receive patches.

---

## How to Report a Vulnerability

> **Please do not open a public GitHub issue for security reports.**

1) **Contact (private):**
   - 📧 Email: `security@kansasfrontier.org` (preferred)
   - 🔐 GitHub Security Advisories: [Create a private advisory](../../security/advisories/new)

2) **Include details where possible:**
   - Affected paths (files/workflows/containers) and commit SHA(s)
   - Reproduction steps / PoC (minimal & safe)
   - Impact (e.g., RCE, data integrity, supply-chain, token exposure)
   - Environment (OS, Python/Node versions, CLI flags)
   - Suggested mitigations, if any

3) **Timelines (targets):**
   - **Acknowledgment:** within **72 hours**
   - **Initial assessment/mitigation:** within **7 days** (severity-dependent)
   - **Fix & advisory:** prioritized by severity (see below)

If your report involves **exposed secrets**, please state that clearly; we will **rotate tokens** and invalidate compromised artifacts swiftly.

---

## Scope

In scope:
- Repository code and tools: `src/`, `scripts/`, `web/`
- GitHub Actions workflows: `.github/workflows/**`
- Container files: `docker/**`, `Dockerfile`, `docker-compose.yml`
- Data pipelines & CLIs (fetch/ETL, STAC validation, rendering)
- Docs build chain if it can influence the site or CI

Out of scope:
- Dataset content/accuracy (e.g., historical mislabels, OCR mistakes)
- Vulnerabilities in **upstream dependencies** (report upstream as well—though we will triage & patch our pins)

---

## Responsible Testing (“Safe Harbor”)

We welcome **good-faith research** that:
- Avoids privacy violations, data exfiltration, or service disruption
- Respects rate limits and does **not** perform DoS/traffic floods
- Keeps PoCs local/offline where possible (the web app is static)
- Does **not** exploit third-party services without their permission

If you follow these rules, we will not pursue action under applicable laws or terms of service.

---

## Triage & Severity

We use CVSS v3.1 as guidance:

| Severity | Examples in this repo | Target response |
|---|---|---|
| **Critical** | RCE in scripts/CLI; supply-chain takeover (actions, containers) | Hotfix/mitigation ASAP; publish advisory |
| **High** | Token/secret leak paths; path traversal leading to overwrite | Patch within 7 days |
| **Medium** | Script injection in docs pipelines; weak defaults | Patch in next planned release |
| **Low** | Non-exploitable hardening gaps | Backlog with clear tracking |

You will receive updates at each stage (ack → triage → fix → disclosure).

---

## Our Current Security Practices

**CI & Scanning**
- **CodeQL** for Python & JS/TS ([workflow](./workflows/codeql.yml))  
- **Pre-commit** hygiene & **secret scanning** (gitleaks on push, plus `detect-aws-credentials`) — see [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml)

**Least-Privilege CI**
- Workflows run with reduced `permissions` and **concurrency** to limit blast radius
- Hardened runners (egress auditing) where applicable

**Supply-Chain Hygiene**
- Pinned base images in `docker/`
- `.dockerignore` and `.gitignore` tuned to keep large/untrusted artifacts out of builds
- JSON Schema validation for `web/config` (legend/categories/sources) in CI & hooks

**Reproducibility**
- Makefile targets for deterministic builds (`make prebuild`, `make stac-validate`)
- Checksums (`*.sha256`) and metadata sidecars for major artifacts

> If an SBOM workflow is present in this repo, we will include it in advisories for rapid dependency triage.

---

## What Maintainers Do on a Valid Report

1. **Acknowledge** and assign a CVE/CVSS assessment (if applicable)  
2. **Mitigate** quickly (revoke tokens, quarantine artifacts, disable risky job paths)  
3. **Fix** with tests + hardening (and backport if needed)  
4. **Disclose** via GitHub Security Advisory and RELEASE notes; credit researcher unless anonymity requested

---

## Disclosure

- Keep details **private** until a fix is released.  
- We coordinate on a responsible timeline; public advisory & release notes will follow.  
- Researchers are credited in the advisory/release unless anonymity is requested.

---

## Contact & Questions

- Sensitive reports: `security@kansasfrontier.org` or [private advisory](../../security/advisories)  
- General questions: [Discussions](../../discussions) or [Issues](../../issues)

Thank you for helping keep **Kansas-Frontier-Matrix** and its users safe.
