<div align="center">

# 🔒 Kansas-Frontier-Matrix — Security Policy (`.github/SECURITY.md`)

**Mission:** Protect the integrity of Kansas-Frontier-Matrix by  
providing a clear process for reporting vulnerabilities,  
coordinating fixes, and practicing **MCP-grade security hygiene**.

[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](./workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](./workflows/trivy.yml)  
[![Secret Scanning](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/secret-scanning.yml/badge.svg)](./workflows/secret-scanning.yml)

</div>

---

## 🔄 Vulnerability Report Lifecycle

```mermaid
flowchart TD
  A["Researcher finds issue"] --> B["🔐 Private report\n(security@kansasfrontier.org or GitHub advisory)"]
  B --> C["⏱️ Acknowledgment\nwithin 72h"]
  C --> D["🧮 CVSS triage\n(severity + scope)"]
  D --> E["🛠️ Mitigation\n(token revoke, artifact quarantine)"]
  E --> F["🔧 Patch & tests\n(backport if needed)"]
  F --> G["📢 Advisory & release notes\ncredit researcher unless anonymous"]

<!-- END OF MERMAID -->



⸻

📌 Supported Versions
	•	Security fixes are provided for the main branch.
	•	Older tags, forks, or experimental branches may not receive patches.

⸻

📨 How to Report

➡️ Do NOT open a public issue for vulnerabilities.
	•	Preferred channels:
	•	📧 security@kansasfrontier.org
	•	🔐 Private GitHub advisory
	•	Include details:
	•	Affected files/paths + commit SHA(s)
	•	Repro steps / PoC (minimal & safe)
	•	Impact (e.g., RCE, token leak, supply-chain)
	•	Environment info (OS, Python/Node versions)
	•	Suggested mitigations (optional)
	•	Response targets:
	•	Acknowledgment → 72h
	•	Initial assessment/mitigation → 7 days (severity-dependent)
	•	Full fix/advisory → prioritized by severity

If your report involves exposed secrets, state clearly; we will rotate tokens immediately.

⸻

🎯 Scope

In scope
	•	Repo code (src/, scripts/, web/)
	•	GitHub Actions workflows (.github/workflows/**)
	•	Container files (docker/**, Dockerfile, docker-compose.yml)
	•	Data pipelines, STAC validation, rendering CLIs
	•	Docs build chain if it can influence site/CI

Out of scope
	•	Dataset content/accuracy (historical mislabels, OCR noise)
	•	Vulnerabilities in upstream deps (report upstream, we patch locally if needed)

⸻

🤝 Safe Harbor (Responsible Testing)

We welcome good-faith research that:
	•	Avoids privacy violations, exfiltration, or disruption
	•	Respects rate limits; no DoS/flooding
	•	Keeps PoCs local/offline (the site is static)
	•	Does not target third-party services without consent

If you follow these rules, we will not pursue action under law or ToS.

⸻

🧮 Severity (CVSS v3.1 guidance)

Severity	Examples in repo	Target response
Critical	RCE in CLI/scripts; supply-chain takeover	Hotfix ASAP + advisory
High	Token leak; path traversal → overwrite	Patch ≤ 7 days
Medium	Script injection in docs/build; weak defaults	Patch in next release
Low	Non-exploitable hardening gap	Backlog + tracking


⸻

🛡️ Current Security Practices
	•	CI & Scanning
	•	CodeQL for Python + JS/TS → codeql.yml
	•	Trivy FS/config/image scans → trivy.yml
	•	Secret scanning (gitleaks + detect-aws-credentials) → secret-scanning.yml
	•	Least privilege CI
	•	Minimal permissions: in workflows
	•	Concurrency guards → avoid duplicate runs
	•	Supply-chain hygiene
	•	Pinned base images (docker/)
	•	.dockerignore/.gitignore exclude unsafe artifacts
	•	JSON Schema validation for configs (legends, sources, categories)
	•	Dependabot security lane (daily) for actions/npm/pip/docker
	•	Reproducibility
	•	Deterministic Make targets (make prebuild, make stac-validate)
	•	SHA-256 checksums + metadata sidecars for artifacts
	•	Optional SBOM workflow → included in advisories

⸻

🔧 Maintainer Response Flow
	1.	Acknowledge → CVSS assessment (CVE if applicable)
	2.	Mitigate → revoke tokens, quarantine artifacts, disable risky jobs
	3.	Fix → patch + add tests, hardening, backport if needed
	4.	Disclose → GitHub advisory + release notes; credit researcher (unless anonymous)

⸻

📢 Coordinated Disclosure
	•	Keep details private until fix is released.
	•	Advisory + release notes published after patch.
	•	Researchers credited unless anonymity requested.

⸻

📬 Contact
	•	Sensitive reports → security@kansasfrontier.org or private advisory
	•	General security questions → Discussions or Issues

🙏 Thank you for helping keep Kansas-Frontier-Matrix safe for everyone.