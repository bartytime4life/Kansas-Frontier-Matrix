# Security Policy

The **Kansas-Frontier-Matrix** project takes security seriously.  
This document explains how to report vulnerabilities and what you can expect from maintainers.

---

## Supported Versions

We currently support security fixes only for the **`main` branch**.  
Older tags, forks, or experimental branches may not receive patches.

---

## Reporting a Vulnerability

If you discover a security issue:

1. **Do not open a public GitHub issue.**  
   Instead, please email the maintainers:

   - 📧 `security@kansasfrontier.org` (preferred)
   - or use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories)

2. Include as much detail as possible:
   - Steps to reproduce the vulnerability
   - Affected files, scripts, or workflows
   - Potential impact (data integrity, pipeline execution, secrets leakage, etc.)
   - Any suggested mitigations or patches

3. You will receive an acknowledgment within **72 hours**.  
   We aim to provide an initial fix or mitigation within **7 days**, depending on severity.

---

## Scope

This policy covers:
- Repository code (`src/`, `scripts/`, `web/`)
- GitHub Actions workflows (`.github/workflows/`)
- Container builds (`Dockerfile`, `docker/`)
- Data ingestion pipelines (ETL, STAC validation)
- AI/ML integrations where exploitable inputs could be weaponized

It does **not** cover:
- Historical data accuracy (mis-tagged maps, OCR errors, etc.)
- Third-party upstream packages (though we track them via Dependabot & SBOMs)

---

## Security Practices in This Repo

- **CodeQL scanning** (`.github/workflows/codeql.yml`) for Python and JavaScript/TypeScript  
- **SBOM generation** (`.github/workflows/sbom.yml`) using Syft (CycloneDX + SPDX)  
- **Dependabot alerts** for dependencies in Python, Node, and GitHub Actions  
- **Container hardening**: Docker images are minimal, reproducible, and pinned to trusted bases  
- **Principle of Least Privilege**: GitHub Actions run with reduced permissions where possible  
- **Reproducibility Logs**: All ETL runs are logged to ensure traceability and rollback if needed  

---

## Disclosure Policy

- Please keep vulnerability details private until a fix is released.  
- Coordinated disclosure with a **public advisory** will be made once the patch is available.  
- Contributors are credited in release notes unless anonymity is requested.

---

## Questions?

For non-sensitive security questions, open a [GitHub Discussion](../../discussions) or [Issue](../../issues).  
For all sensitive issues, use the **private channels** above.
