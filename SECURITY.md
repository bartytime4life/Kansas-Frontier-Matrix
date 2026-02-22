# SECURITY — Vulnerability Reporting & Coordinated Disclosure for Kansas Frontier Matrix (KFM)

> **Purpose:** Provide a safe, private, and governed path to report security issues affecting KFM (code, pipelines, policy, evidence, and data controls).  
> **Posture:** default-deny • fail-closed • evidence-first • policy enforced in CI + runtime

**Status:** vNext (process target; align to repo reality)  
**Owners:** Maintainers / Security Stewards (see CODEOWNERS)  
**Scope:** Anything that can affect **confidentiality, integrity, availability, provenance, or policy enforcement**.

[![Status](https://img.shields.io/badge/status-vNext-blue)](#)
[![Reporting](https://img.shields.io/badge/reporting-private--first-critical)](#)
[![Disclosure](https://img.shields.io/badge/disclosure-coordinated-important)](#)
[![Governance](https://img.shields.io/badge/governance-fail--closed-critical)](#)
[![Policy](https://img.shields.io/badge/policy-default--deny-critical)](#)

**Jump links:**  
[Main README](./README.md) • [Contributing](./CONTRIBUTING.md) • [GitHub governance](./.github/README.md) • [Policy](./policy/) • [Contracts](./contracts/)

---

## Quick navigation
- [How to report a vulnerability](#how-to-report-a-vulnerability)
- [What to include in a report](#what-to-include-in-a-report)
- [Scope: what is and is not covered](#scope-what-is-and-is-not-covered)
- [KFM-specific “high priority” vulnerability classes](#kfm-specific-high-priority-vulnerability-classes)
- [Triage, severity, and coordinated disclosure](#triage-severity-and-coordinated-disclosure)
- [Safe harbor for good-faith research](#safe-harbor-for-good-faith-research)
- [Security expectations for contributors](#security-expectations-for-contributors)
- [Maintainer playbook (fail-closed)](#maintainer-playbook-fail-closed)

---

## How to report a vulnerability

**Do not open a public GitHub issue** for security problems.

### Preferred channel: GitHub Security Advisories (private report)
Use GitHub’s **“Report a vulnerability”** / Security Advisory feature for this repository (private by default).

- This keeps discussion private while maintainers reproduce, patch, and prepare a coordinated disclosure.
- Attach minimal reproduction steps and logs **without** secrets.

### Alternate channel: security email (if configured)
If the repo maintainers publish a security email address, use it.

- **Email:** `TBD` (repo maintainer: set this to a real address)
- **PGP:** `TBD` (optional; publish fingerprint + key location if you require encryption)

### If the issue involves imminent harm or sensitive locations
If your report involves:
- **restricted data leakage**
- **culturally sensitive site location exposure**
- **private individual location inference**
- **vulnerable infrastructure targeting**
treat it as **Critical** and report via **private channels only**.

> **Rule:** If a finding includes precise coordinates or re-identification risk, do **not** include the raw coordinates in the initial report. Provide a generalized description first; we will request details privately if needed.

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)

---

## What to include in a report

Please include:

- **Summary:** what is broken and why it matters (confidentiality/integrity/availability/policy).
- **Affected surface:** API endpoint(s), UI route(s), workflow file(s), policy rule(s), dataset/pipeline component(s).
- **Impact:** what an attacker/user can gain or do.
- **Reproduction:** minimal steps (PoC), requests, inputs, and expected vs actual outcomes.
- **Versions/IDs:** relevant git commit, container image digest, dataset_version_id, run_id, or build artifact digest (if known).
- **Evidence:** screenshots, logs, stack traces (redact secrets), and example requests/responses.
- **Constraints:** any timing or coordination constraints (e.g., embargoed data, partner obligations).

Please **do not** include:

- live credentials, tokens, API keys, cookies
- private user data, restricted documents, or raw sensitive coordinates
- exploit code that enables harm at scale (we can coordinate details privately)

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)

---

## Scope: what is and is not covered

### In scope
Security issues in:

- **Governed API** and authn/authz logic (including policy-safe error behavior)
- **Policy engine** rules, evaluation, and alignment between CI + runtime
- **Evidence resolver** and citation verification gates (Cite-or-abstain enforcement)
- **Catalog validators** and promotion gates (DCAT/STAC/PROV, checksums, linkcheck)
- **Exports** and packaging (license/attribution insertion, data suppression, generalization)
- **Workflows / CI / CODEOWNERS** (supply-chain, secret exposure, permission misuse)
- **Containers / images / deployment configs** that can cause privilege escalation or data exposure
- **UI** issues that can leak restricted existence or allow exfiltration (XSS, SSRF via config, etc.)

### Out of scope (typical)
- social engineering attacks on individuals
- physical attacks, denial-of-service testing without permission
- issues requiring stolen credentials
- vulnerabilities in third-party services you do not control (unless misconfiguration in KFM is the root cause)

> **Important:** KFM treats “governance failures” as security failures when they enable leakage, bypass policy, or break provenance and auditability.

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)

---

## KFM-specific “high priority” vulnerability classes

These are especially important in a map-first, governed system:

1. **Policy bypass**
   - Any path where restricted artifacts, metadata, or existence can be inferred without authorization.

2. **Policy-unsafe error behavior**
   - Different errors for “doesn’t exist” vs “exists but restricted” that leak information.

3. **Evidence resolver weaknesses**
   - EvidenceRef resolution that can be tricked into:
     - returning restricted bundles
     - fetching arbitrary URLs
     - skipping checksum/provenance checks
     - accepting untrusted citations as “verified”

4. **Sensitive location leakage**
   - Exposure of precise coordinates or geometry when policy requires generalization/suppression.

5. **Export control failures**
   - Ability to export or download restricted content, or to reconstruct restricted geometry from exports.

6. **Promotion gate bypass**
   - Ability to “publish” a DatasetVersion without required catalogs, checksums, rights metadata, or audit receipts.

7. **Supply-chain / CI compromise**
   - GitHub Actions permission overreach, unpinned third-party actions, secret exposure in fork contexts,
     or workflow injection via `pull_request_target`.

8. **Prompt injection / data exfiltration in Focus Mode**
   - Retrieved content influencing the system to reveal restricted material, bypass policy, or fabricate citations.

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)

---

## Triage, severity, and coordinated disclosure

### Response flow

~~~mermaid
flowchart LR
  R[Reporter submits private report] --> A[Acknowledge receipt]
  A --> T[Triage and reproduce]
  T --> P[Patch + tests + policy fixtures]
  P --> V[Verify gates: CI + runtime parity]
  V --> D[Draft advisory + release notes]
  D --> F[Fix released / deployed]
  F --> C[Coordinated disclosure]
~~~

### Severity guide (starter)

| Severity | Typical impact | KFM examples |
|---|---|---|
| **Critical** | Unauthorized access to restricted data; remote code execution; privilege escalation; irreversible data/provenance harm | policy bypass; evidence resolver returns restricted bundles; workflow secret exfiltration; export bypass |
| **High** | Significant data exposure or auth bypass with constraints; integrity compromise; persistent XSS | policy-unsafe error leaks; injection on governed surfaces; catalog checksum bypass |
| **Medium** | Limited exposure; denial of service of a subsystem; non-persistent XSS; defense-in-depth failures | missing rate limits; mis-scoped permissions; minor disclosure |
| **Low** | Minimal security impact; hard-to-exploit; informational | headers, minor config hardening |

### Coordinated disclosure expectations

- We coordinate fixes and disclosure to reduce harm.
- We may request that public disclosure waits until a patch is released (or mitigations are available).
- If a vulnerability affects governed datasets or sensitive locations, disclosure may be **more restricted** than typical software issues.

> **Fail-closed principle:** When in doubt, KFM mitigations prioritize **blocking** over partial service.

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)

---

## Safe harbor for good-faith research

We support good-faith security research that helps protect users and governed materials.

You are welcome to:
- investigate issues using **your own accounts/data**
- use **minimal traffic** needed to demonstrate the problem
- report privately and work with maintainers on coordinated disclosure

Please do not:
- access or exfiltrate data you are not authorized to access
- test denial-of-service or disruptive behavior
- attempt persistence, lateral movement, or credential harvesting

If you follow this policy, we will treat your report as a good-faith effort and prioritize responsible handling.

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)

---

## Security expectations for contributors

Security is not a separate phase in KFM. It is an enforcement property.

### Required practices (starter)
- **No secrets in git.** Ever.
- **Least privilege** for workflows and runtime permissions.
- **Pin dependencies and actions** where practical (avoid floating tags).
- **Policy-safe errors:** do not introduce “existence leaks.”
- **Cite-or-abstain**: do not weaken citation verification gates.
- **Provenance and digests:** do not ship artifacts without checksums and run receipts.
- **Sensitive location handling:** do not publish precise coordinates unless explicitly permitted by policy.

### Security review triggers (recommended)
Changes touching:
- `.github/**`, `policy/**`, `contracts/**`, `infra/**`
- any authn/authz, evidence resolution, export logic, dataset promotion, or Focus Mode orchestration  
should be treated as **high-risk** and require the right reviewers (CODEOWNERS).

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)

---

## Maintainer playbook (fail-closed)

When a report is received:

1. **Acknowledge privately** and confirm the intake channel.
2. **Reproduce** with minimal scope.
3. **Classify severity** (include “policy leakage” and “sensitive location” impacts).
4. **Mitigate quickly**:
   - block or gate the surface if uncertain
   - add policy-safe error handling
5. **Patch with tests**:
   - add regression tests
   - add policy fixtures + denial tests
   - add citation verification tests (if evidence-related)
6. **Verify CI + runtime parity**:
   - ensure the same policy semantics apply in both places
7. **Record governance artifacts**:
   - link patch to advisory
   - ensure audit/run receipt implications are considered
8. **Coordinate disclosure** and publish release notes/advisory (as appropriate).

> **Reminder:** A vulnerability that undermines policy enforcement or evidence integrity is a platform integrity issue, not just a bug.

[↑ Back to top](#security--vulnerability-reporting--coordinated-disclosure-for-kansas-frontier-matrix-kfm)
