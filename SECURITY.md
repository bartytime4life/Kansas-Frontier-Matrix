<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8b3e793b-3d2f-4a21-9a4d-3c38f6f26b87
title: SECURITY — Vulnerability Disclosure Policy
type: standard
version: v1
status: draft
owners: Security Working Group (SWG) <security@YOURDOMAIN.example>
created: 2026-02-23
updated: 2026-02-23
policy_label: public
related:
  - docs/governance/ROOT_GOVERNANCE.md
  - docs/governance/REVIEW_GATES.md
  - docs/governance/ETHICS.md
  - docs/governance/SOVEREIGNTY.md
tags: [kfm, security, disclosure, governance]
notes:
  - Replace placeholder contacts, keys, and SLAs before publishing.
  - Mirror this file into .github/SECURITY.md if you want GitHub’s “Security policy” UI to show it.
[/KFM_META_BLOCK_V2] -->

# SECURITY — Vulnerability Disclosure Policy

This document explains how to report security issues in this repository and what to expect from us.

## Quick rules
- **Do not** open public issues or PRs for security vulnerabilities.
- **Do** report privately using the channels below.
- **Do not** include sensitive data (keys, tokens, personal data, exact vulnerable site locations, etc.).
- If in doubt about sensitivity/permissions, **default to private + minimal disclosure**.

---

## Reporting a vulnerability

### Preferred channel
Email: **security@YOURDOMAIN.example**  
Subject: **[SECURITY] <short summary>**

If you have a CVE request, include: **“CVE Request”** in the subject.

### Alternative channels (if configured)
- GitHub Security Advisories: **https://github.com/<org>/<repo>/security/advisories/new**
- Encrypted reporting (PGP): see “Encryption” below.

### What to include
Please include:
- A concise summary of the issue and **impact** (what an attacker can do).
- **Affected component(s)** (e.g., API boundary, pipelines, graph build, UI, Story Nodes, releases).
- **Reproduction steps** or a proof-of-concept (PoC) that is safe and minimal.
- Any relevant logs, stack traces, request/response samples (redacted).
- Your suggested severity (if you have one) and reasoning.
- Your contact info and preferred attribution name (or “anonymous”).

### What *not* to include
Please avoid:
- Secrets: API keys, tokens, passwords, private certificates.
- Private/personal data.
- Exact coordinates or identifying details for sensitive/culturally restricted/vulnerable locations.
- Exploit chains that enable broad compromise unless requested by the SWG.

---

## Scope

### In scope
- **Governed APIs and policy boundary** (authz/authn, rate limiting, abuse controls, audit logging).
- **Data pipelines** (integrity, provenance, promotion gates, quarantining, validation bypasses).
- **Metadata + catalogs** (STAC/DCAT/PROV correctness, tamper resistance, injection risks).
- **Graph build/indexing** (injection, privilege escalation, data poisoning, unauthorized traversal).
- **Map/Story UI** (XSS/CSRF, SSRF, unsafe file upload, token leakage, privacy leaks).
- **Focus Mode AI / automation** (policy bypass, prompt injection leading to restricted data exposure).
- **Supply chain** (dependency compromise, CI secrets exposure, build provenance/SBOM integrity).

### Out of scope (unless explicitly stated otherwise)
- Security of your own fork, local environment, or third-party services you configure independently.
- Denial-of-service tests that degrade availability (unless pre-approved).
- Social engineering, phishing, physical attacks.

---

## Safe harbor for good-faith research

We support good-faith security research that:
- Avoids privacy violations and service disruption.
- Uses **only** the minimum data needed to demonstrate impact.
- Respects data sovereignty and culturally restricted knowledge constraints.
- Gives us a reasonable window to remediate before public disclosure.

We do **not** consider the following to be authorized:
- Accessing or exfiltrating data you don’t own or have explicit permission to access.
- Attempting to identify individuals from data, even if technically possible.
- Attempting lateral movement beyond the smallest necessary proof of impact.

If you’re uncertain whether a test is safe, **ask first** via the reporting channel.

---

## Severity and response targets (editable)

We use a practical severity model aligned with industry norms (Critical/High/Medium/Low).
Targets below are goals, not guarantees.

| Severity | Examples (non-exhaustive) | Acknowledge | Triage | Fix target |
|---|---|---:|---:|---:|
| Critical | RCE, auth bypass, mass data exposure, signing key compromise | 2 business days | 5 business days | 14–30 days |
| High | privilege escalation, significant injection, sensitive data leak | 3 business days | 10 business days | 30–60 days |
| Medium | limited-scope leaks, non-exploitable-by-default issues | 5 business days | 15 business days | 60–90 days |
| Low | hardening, best-practice gaps | 10 business days | 20 business days | as scheduled |

---

## Coordinated disclosure

We prefer coordinated disclosure.
- We’ll confirm receipt, assess impact, and work with you on a disclosure timeline.
- We may request additional details or a safer PoC.
- If we publish a security advisory, we’ll credit you if you want attribution.

**Please do not publish** details before we confirm remediation or agree on an embargo date.

---

## Data governance & sensitive content handling

This project may contain (or derive) sensitive information, including:
- Locations of vulnerable sites
- Culturally restricted knowledge
- Proprietary or licensed datasets
- Personal or community-linked data

If your report involves any of the above:
- Provide a **generalized description** (e.g., “within 10–25 km of X region”) rather than exact coordinates.
- Prefer screenshots with identifying details blurred, or textual descriptions.
- Flag the report as **“SENSITIVE: governance review needed”**.

---

## Security incident: what we may do

Depending on severity, we may:
- Quarantine affected data artifacts and block promotions (Raw → Work/Quarantine → Processed → Published).
- Rotate secrets, revoke tokens, and invalidate caches.
- Publish a security advisory and release notes.
- Add regression tests and policy checks so the class of issue fails closed.

---

## Encryption (optional but recommended)

If you need encrypted comms:
- PGP public key: **(add link here)**
- Fingerprint: **(add fingerprint here)**

---

## Supported versions (fill in)

| Version / branch | Supported | Notes |
|---|---|---|
| main | ✅ / ❌ | |
| latest release (vX.Y.Z) | ✅ / ❌ | |
| previous release (vX.Y.Z-1) | ✅ / ❌ | |

---

## Security best practices for contributors (short)

- Never commit secrets. Use `.env.example` and secret managers in CI.
- Treat the **policy boundary** as a security boundary: clients must not bypass governed APIs.
- Add tests for security invariants (authz, validation, provenance checks, redaction).
- Prefer dependency pinning and add SBOM/signing where supported.
- Log safely: no secrets, no personal data, no precise sensitive locations.

---

## Contact

Security Working Group (SWG): **security@YOURDOMAIN.example**  
Backup contact: **(add backup contact/rotation)**

If you believe the issue is actively exploited, write **“URGENT”** in the subject line.