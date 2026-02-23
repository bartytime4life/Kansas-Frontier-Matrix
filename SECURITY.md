<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7e2f2d2e-5c28-4ed5-8f8b-0dfb2d3356ae
title: SECURITY.md
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-23
updated: 2026-02-23
policy_label: public
related:
  - ./README.md
  - ./.github/ISSUE_TEMPLATE/bug_report.yml
  - ./.github/ISSUE_TEMPLATE/feature_request.yml
tags: [kfm, security, vulnerability-disclosure]
notes:
  - Replace all "TBD" and placeholder contact info before publishing.
  - Keep this file in the repo root (or .github/) so GitHub can discover it.
[/KFM_META_BLOCK_V2] -->

# Security Policy

This document explains how to report security vulnerabilities in this repository and what you can expect from us during triage and remediation.

- **Do not** report security issues in public GitHub issues.
- **Do** use a private channel (GitHub Security Advisory or email) so we can protect users while we fix the issue.

## Quick navigation

- [Supported versions](#supported-versions)
- [Reporting a vulnerability](#reporting-a-vulnerability)
- [What to include](#what-to-include)
- [Response and remediation process](#response-and-remediation-process)
- [Scope](#scope)
- [Safe harbor](#safe-harbor)
- [Security posture notes for data and maps](#security-posture-notes-for-data-and-maps)

---

## Supported versions

Security fixes are typically applied to the **latest released** version and/or the **default branch**.

| Version / Branch | Supported |
|---|---|
| `main` (default branch) | ✅ |
| Latest release | ✅ |
| Older releases | ⚠️ Best-effort |
| Unreleased forks | ❌ |

> **NOTE:** If you are unsure which version you are running, include commit hash, tag, or container/image digest in your report.

---

## Reporting a vulnerability

### Preferred: GitHub Security Advisories (private)

If this repository has GitHub Security Advisories enabled, use the **“Report a vulnerability”** button on the repo’s *Security* tab. This keeps the report private and supports coordinated disclosure.

### Alternative: Email (private)

Email: **TBD (e.g., `security@your-org.example`)**  
Subject: **`[SECURITY] <short summary>`**

If you can, encrypt sensitive details (proofs, logs, reproduction datasets) using our PGP key:

- PGP key: **TBD**
- Fingerprint: **TBD**

Example (ASCII-armored) usage:

```bash
# Example: encrypt report.txt for the security team key
gpg --encrypt --armor --recipient "TBD_SECURITY_TEAM_KEY_ID" report.txt
```

### If you believe there is active exploitation

If you believe an issue is being actively exploited in the wild:
- Mark your report as **URGENT** in the subject/title.
- Include *only the minimum necessary* details for us to confirm impact.
- Avoid publishing any indicators-of-compromise (IoCs) that would enable copycat attacks.

---

## What to include

Please include as much of the following as you can:

- A clear description of the issue and **why it is a security problem**
- Affected component(s) (e.g., API, pipeline, UI, storage adapter, auth)
- Exact version / commit hash and deployment context
- Steps to reproduce (PoC, minimal repro repo, request/response samples)
- Impact assessment:
  - What an attacker can do
  - Preconditions (auth required? network access? specific role?)
  - Worst-case outcome
- Any known mitigations or workarounds
- If relevant: logs, stack traces, screenshots, or traces (**redact secrets**)

### Please do NOT include

- Secrets (API keys, tokens, passwords), even if “already leaked”
- Exact coordinates or culturally restricted locations if your report involves sensitive sites  
  (see [Security posture notes for data and maps](#security-posture-notes-for-data-and-maps))

---

## Response and remediation process

We aim to follow a coordinated vulnerability disclosure flow:

1. **Acknowledgement**: We confirm receipt.
2. **Triage**: We validate, assess severity, and identify affected versions/components.
3. **Remediation plan**: We determine fix strategy and release vehicle.
4. **Fix & test**: We implement remediation with regression tests and security checks.
5. **Release**: We publish patches and advisories as appropriate.
6. **Disclosure**: We coordinate timing and credit (if requested).

### Target timelines (best-effort)

These are targets, not guarantees (severity and complexity vary):

- Acknowledge within: **TBD (e.g., 2 business days)**
- Initial triage within: **TBD (e.g., 5 business days)**
- Patch for critical issues within: **TBD (e.g., 7–30 days)**

---

## Scope

### In scope

- Vulnerabilities in code in this repository
- CI/CD or build workflows that could enable supply-chain compromise
- Authentication/authorization flaws
- Data exposure issues (private datasets, restricted content, secrets)
- Map/Story UI security issues (XSS, CSRF, injection, unsafe rendering)
- API issues (injection, IDOR, auth bypass, broken access control)
- Storage/indexing misconfigurations caused by this repo’s code/config

### Out of scope

- Social engineering attacks against maintainers/users
- Denial-of-service requiring excessive traffic (unless a clear algorithmic amplification exists)
- Issues in unsupported versions (see [Supported versions](#supported-versions))
- Vulnerabilities solely in third-party services not managed by this repo

---

## Safe harbor

We support good-faith security research that:

- Avoids privacy violations and data destruction
- Uses the minimum amount of data access needed to demonstrate impact
- Does not intentionally degrade service for others
- Does not publicly disclose before we have a reasonable chance to remediate

> **NOTE:** If you are unsure whether a test is safe, stop and contact us first via a private channel.

---

## Security posture notes for data and maps

This project may involve **sensitive locations, vulnerable sites, or culturally restricted knowledge**. Security reporting must preserve the trust membrane:

- Do not include exact coordinates for sensitive/restricted sites in reports.
- If location detail is required for reproduction, share it **only via encrypted channels** and consider sharing:
  - generalized bounding boxes,
  - hashed identifiers,
  - redacted exemplars,
  - or synthetic test data.

If your report involves potential harm to communities or sensitive sites, explicitly flag it as:
- **“Sensitive / governance review needed”**

---

## Credit

If you want public credit, include the name/handle and a preferred link in your report. If you prefer to remain anonymous, we will respect that.

Thank you for helping keep the project and its users safe.