<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7d7a9c1e-8a22-4c26-89c2-2a6c7b0a6a6d
title: SECURITY
type: standard
version: v3
status: draft
owners: KFM Security & Governance Stewards (TBD)
created: 2026-02-26
updated: 2026-03-02
policy_label: public
related:
  - kfm://doc/kfm-gdg-vnext-2026-02-20
  - ./README.md
  - ./.github/README.md
  - ./CONTRIBUTING.md
tags: [kfm, security, governance, policy-as-code]
notes:
  - SECURITY policy aligned to governance-first, default-deny KFM posture.
  - Adds: truth-path security mapping, Promotion Contract gate mapping, security control matrix, and policy-safe error contract.
  - TODOs to resolve before publishing: contacts, encryption key/process, supported-version window, audit retention policy.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Kansas Frontier Matrix (KFM) — Security Policy

![Status](https://img.shields.io/badge/status-draft-yellow)
![Posture](https://img.shields.io/badge/posture-default--deny-important)
![Fail-closed](https://img.shields.io/badge/gates-fail--closed-critical)
![Policy](https://img.shields.io/badge/policy-policy--as--code-blue)
![Evidence](https://img.shields.io/badge/ux-evidence--first-0aa)
![Supply chain](https://img.shields.io/badge/supply%20chain-attest%20or%20block-important)
![Citations](https://img.shields.io/badge/focus-cite--or--abstain-critical)
![Audit](https://img.shields.io/badge/audit-append--only-informational)

> **TL;DR:** In KFM, **security is governance**: policy labels, default‑deny, evidence resolution, and auditability are enforced in **CI** and at **runtime**.  
> If a control is uncertain, KFM **fails closed**.

> [!IMPORTANT]
> This document is **public**. Do not add secrets, internal endpoints, or restricted dataset identifiers here.

---

## Quick navigation

- [Scope and non-goals](#scope-and-non-goals)
- [Open TODOs before publishing](#open-todos-before-publishing)
- [Supported versions](#supported-versions)
- [Reporting a vulnerability](#reporting-a-vulnerability)
- [What counts as a security issue](#what-counts-as-a-security-issue)
- [Security principles](#security-principles)
- [KFM security model](#kfm-security-model)
- [Security across the truth path](#security-across-the-truth-path)
- [Threat-model invariants](#threat-model-invariants)
- [Policy labels, sensitive locations, and privacy](#policy-labels-sensitive-locations-and-privacy)
- [Authentication and authorization](#authentication-and-authorization)
- [Policy-safe errors](#policy-safe-errors)
- [Secrets and credentials](#secrets-and-credentials)
- [Supply chain integrity](#supply-chain-integrity)
- [Audit logs and run receipts](#audit-logs-and-run-receipts)
- [Security gates and required checks](#security-gates-and-required-checks)
- [Incident response](#incident-response)
- [Coordinated disclosure](#coordinated-disclosure)
- [References](#references)

---

## Scope and non-goals

### In scope

This policy covers security controls for:

- **Repo**: contributions, CI/CD gates, dependency integrity, secret hygiene
- **Pipelines**: source intake, processing, cataloging, promotions, exports
- **Runtime**: governed APIs, evidence resolver, policy enforcement, caching behavior
- **UI**: evidence-first UX, policy notices, anti-leak affordances
- **Focus Mode**: cite-or-abstain, prompt-injection resistance, restricted-data protection
- **Operational security**: audit logging, incident response, rollback-first mitigations

### Non-goals

- Physical security, employee device security, and other organizational policies (covered elsewhere)
- Bug bounty terms (unless explicitly added)
- SLA/SLO guarantees (separate doc)

> [!NOTE]
> This document may refer to **recommended** repo paths (e.g., `policy/`, `contracts/`, `tools/`).  
> If your repo uses different paths, update accordingly. Do not assume a path exists unless verified.

[Back to top](#top)

---

## Open TODOs before publishing

This policy **must not** be promoted to `published` until the following are resolved:

- [ ] **Security contact** is real (email and/or GH private reporting enabled)
- [ ] **Encryption** path is published (PGP or secure intake portal)
- [ ] **Supported-version window** is defined (release cadence + backport expectations)
- [ ] **Audit retention** policy exists (duration, access rules, deletion policy)
- [ ] **Incident runbooks** exist (or are linked) for SEV-1/2

[Back to top](#top)

---

## Supported versions

> [!NOTE]
> Release/support policy is **TBD**. Until a formal policy exists, treat:
> - the default branch (often `main`) **and**
> - the latest release tag (if releases exist)
> as the only supported versions for security fixes.

| Version / branch | Supported | Notes |
|---|---:|---|
| Default branch (e.g., `main`) | ✅ | Active development line |
| Latest release tag | ✅ | Fixes SHOULD be backported here when feasible |
| Older tags/releases | ❌ | Upgrade to latest |

> [!PROPOSED]
> Once releases exist, define an explicit window (e.g., **N-1 releases** or **90 days**) and publish it here.

[Back to top](#top)

---

## Reporting a vulnerability

**Please do not open public issues for security reports.**

Preferred reporting paths (in order):

1) **GitHub private vulnerability reporting** *(if enabled for this repo)*  
   Repository **Security** tab → **Report a vulnerability**

2) **Private email to the security contact**
   - **Primary:** `TODO: security-contact@example.org`
   - **Backup:** `TODO: maintainer-contact@example.org`

3) **If neither is available:** open a GitHub issue **without details** and request a private channel.  
   (Do not include exploit payloads, sensitive coordinates, or PII.)

### Encryption (recommended)

> [!PROPOSED]
> Publish one of the following before moving this document to `published`:
> - a PGP public key fingerprint, or
> - an org-standard secure intake process (ticketing portal) that supports attachments safely.

- **PGP key:** `TODO`
- **Key fingerprint:** `TODO`

### What to include

- Clear description of the issue and **potential impact**
- Minimal reproduction steps (or proof-of-concept)
- Affected component(s): API, pipeline, UI, policy bundle, evidence resolver, catalogs, exports, CI gates
- Whether the issue involves **restricted data exposure**, **sensitive locations**, or **PII**
- If available: request IDs, run IDs, dataset_version_id, artifact digests (policy-safe identifiers)

### Data exposure reports (special handling)

If you believe you found any of the following, treat it as a **security incident**:

- `restricted` / `restricted_sensitive_location` data exposure
- PII or reidentifiable records
- “policy bypass” behavior (e.g., access without appropriate policy checks)
- export controls bypass (downloaded content that should be blocked)
- error-message leakage that reveals restricted dataset existence

> [!WARNING]
> Do **not** attach bulk data, precise coordinates, or personal information in the report.
> Prefer:
> - redacted screenshots
> - hashes/IDs (dataset_version_id, run_id, artifact digests)
> - minimal request/response metadata

### What you can expect (targets)

- Acknowledgement: **within 3 business days** *(target; may vary)*
- Triage + severity assignment: **within 10 business days** *(target; may vary)*
- Fix and advisory: coordinated with reporter, depending on impact and release cadence

> [!NOTE]
> KFM may ship a **fail-closed mitigation** (e.g., deny access or suppress exports) before a full fix.

[Back to top](#top)

---

## What counts as a security issue

KFM security issues include (non-exhaustive):

### Access control / policy enforcement
- **Policy bypass:** gaining access to data/evidence without satisfying policy checks
- **Cross-role leakage:** public user receives restricted content due to caching, routing, or index leakage
- **Policy-safe errors violated:** users can infer restricted dataset existence via error differences

### Sensitive location & privacy
- **Sensitive-location leakage:** exposing precise coordinates/geometries that must remain restricted
- **PII leakage:** exposing individual-level records or enabling reidentification
- **Unsafe aggregation:** releasing aggregates below minimum-count thresholds

### Evidence, catalogs, and provenance integrity
- **EvidenceRef tampering:** citations resolve to incorrect evidence (mismatched digest / wrong dataset_version_id)
- **Catalog/link integrity failure:** DCAT/STAC/PROV cross-links wrong or point to non-canonical artifacts
- **Receipt/audit spoofing:** run receipts or audit entries can be deleted/rewritten/spoofed

### Supply chain & secrets
- **Secret leakage:** committing credentials/tokens/keys to the repo or logs
- **Supply chain compromise:** tampered dependencies, unverified build artifacts, missing attestations
- **Dependency confusion / typosquatting** risks in build pipelines

### Focus Mode & retrieval security
- **Prompt-injection leading to policy bypass** (retrieved content causes unauthorized tool use or leakage)
- **Cite-or-abstain failure:** Focus returns claims without resolvable citations for requester’s role
- **Restricted evidence in “reasoning context”** that later leaks into output

[Back to top](#top)

---

## Security principles

KFM’s security posture is defined by these non-negotiable principles:

1. **Default deny**: if policy is uncertain or evaluation fails → deny.
2. **Fail closed**: missing artifacts, missing receipts, missing rights → block promotion and/or block runtime.
3. **Trust membrane**: clients never access storage/DB directly; governed API + policy boundary only.
4. **Cite-or-abstain**: user-facing claims require resolvable, policy-allowed evidence.
5. **Tamper-evident truth**: processed artifacts + catalogs + receipts are immutable by digest.
6. **Least privilege**: services/pipelines have only the access they need; rotate + audit.

[Back to top](#top)

---

## KFM security model

### Trust membrane

```mermaid
flowchart LR
  U[User] --> UI[Map and Story UI]
  UI --> API[Governed API]
  API --> PDP[Policy Decision Point]
  API --> ER[Evidence Resolver]
  PDP --> Store[(Artifact and Catalog Stores)]
  ER --> Store
  API --> Audit[(Audit ledger)]

  Dev[Contributor and Operator] --> CI[CI policy and provenance gates]
  CI --> Store
  CI --> Audit
```

**Key points**
- Policy decisions are enforced at **runtime** (API + evidence resolver) and in **CI** (policy/provenance gates).
- The UI may display policy status, but **does not make policy decisions**.
- “Citations” are **EvidenceRefs** that resolve to inspectable **EvidenceBundles**, not pasted URLs.

### Policy-as-code (concept)

KFM uses a policy bundle (OPA/Rego or equivalent) as shared semantics across:
- CI merge gates
- runtime API enforcement
- evidence resolution enforcement
- export controls

Example (illustrative only):

```rego
package kfm.authz

default allow = false

allow {
  input.user.role == "steward"
}

allow {
  input.user.role == "public"
  input.action == "read"
  input.resource.policy_label == "public"
}

# Obligations example: UI notice for generalized geometry
obligations[o] {
  input.resource.policy_label == "public_generalized"
  o := {"type": "show_notice", "message": "Geometry generalized due to policy."}
}
```

> [!IMPORTANT]
> A policy engine error must fail closed (deny) and produce a policy-safe error message.

[Back to top](#top)

---

## Security across the truth path

KFM’s lifecycle zones are security boundaries. Promotion is **blocked** unless gates are satisfied.

```mermaid
flowchart LR
  Up[Upstream source] --> Raw[RAW zone]
  Raw --> Work[WORK and Quarantine]
  Work --> Proc[PROCESSED]
  Proc --> Cat[CATALOG triplet]
  Cat --> Pub[PUBLISHED surfaces]
  Pub --> UX[Map UI and Focus Mode]
```

### Zone expectations (security view)

| Zone | What lives here | Security posture |
|---|---|---|
| **RAW** | Immutable acquisition copies + license snapshot + checksums | Restricted by default; append-only; never public |
| **WORK / Quarantine** | Transforms, QA, redactions/generalizations | Failures isolated; may be rewritten; **no serving** |
| **PROCESSED** | Publishable artifacts with digests (COG, GeoParquet, PMTiles, etc.) | Immutable by digest; promoted only when gates pass |
| **CATALOG / Triplet** | Cross-linked DCAT + STAC + PROV | Must validate and cross-link; EvidenceRefs resolve |
| **PUBLISHED** | Governed runtime surfaces (API, tiles, stories, Focus answers) | Policy enforced; logging/audit on governed actions |

### Promotion Contract mapping (security relevance)

> [!IMPORTANT]
> Treat these gates as **merge-required** checks (CI) and **promotion-required** checks (release lane).

| Gate | What must be present | Security meaning |
|---:|---|---|
| A | Identity & versioning (dataset_id, dataset_version_id, spec_hash, digests) | Prevents spoofing and “mystery data” |
| B | Licensing & rights metadata | Prevents rights violations + unsafe mirroring |
| C | Sensitivity classification & redaction plan | Prevents sensitive-location/PII leakage |
| D | Catalog triplet validation (DCAT/STAC/PROV + cross-links) | Prevents broken citations and “ghost evidence” |
| E | QA checks & thresholds | Prevents unsafe/low-quality outputs from publication |
| F | Run receipt & audit record | Ensures traceability; blocks unverifiable outputs |
| G | Release manifest | Makes promotion auditable and reversible |

[Back to top](#top)

---

## Threat-model invariants

These invariants must remain true. If any becomes uncertain, fail closed and escalate.

| ID | Invariant | Enforcement hints |
|---:|---|---|
| TM-001 | No direct client-to-storage/DB | Network policy + code review + tests |
| TM-002 | Policy-safe errors | Uniform error model; anti-enumeration |
| TM-003 | Export controls enforced | Policy checks + obligation transforms |
| TM-004 | Prompt-injection defenses | Tool allowlist + evidence-only citations |
| TM-005 | Cite-or-abstain hard gate | Citation verification step blocks output |
| TM-006 | Restricted leakage scanning (when required) | Output scanning + fixtures + redaction tests |
| TM-007 | Least-privileged credentials | Scoped creds, rotation, audit |
| TM-008 | Immutability by digest | Content-addressable artifacts; no mutation |
| TM-009 | Supply-chain provenance | SBOM + provenance attestations (when enabled) |
| TM-010 | Append-only audit ledger | Write-once semantics; access-controlled |
| TM-011 | Audit redaction | Logs do not leak restricted data/PII |

[Back to top](#top)

---

## Policy labels, sensitive locations, and privacy

### Policy labels

Policy labels drive access decisions and redaction/generalization obligations.

Starter labels (extend as needed):
- `public`
- `public_generalized`
- `internal`
- `restricted`
- `restricted_sensitive_location`
- `embargoed`
- `quarantine`

### Default-deny expectations

- If a dataset is `restricted` or `restricted_sensitive_location`, access is **deny by default**.
- If a public representation is permitted, create a **separate** `public_generalized` derivative.
- Error responses must not leak restricted metadata (including “does this exist?” signals).

### Sensitive location protection

For culturally sensitive or at-risk locations:
- Store **precise** geometry only in restricted datasets.
- Publish only generalized derivatives, or metadata-only records.
- Enforce policy at the serving layer (no bypass via static tile hosting or public object URLs).
- Include automated tests (e.g., “no restricted bbox leakage”, “no coordinate fields in public exports”).

> [!WARNING]
> Do **not** randomize coordinates for “privacy” unless you can prove it is reproducible and non-leaky.
> Prefer deterministic, documented generalization methods with versioned rules.

### PII risk and aggregation thresholds

Some sources have reidentification risk (property, health, crime, etc.).
- Do not publish individual-level records publicly.
- Aggregate to safe geographies and enforce minimum-count thresholds.
- Document thresholds as policy obligations.
- Keep raw data restricted even when aggregated outputs are public.

[Back to top](#top)

---

## Authentication and authorization

> [!IMPORTANT]
> **DECISION NEEDED:** choose identity provider and access model.

Recommended baseline:
- OIDC for authentication
- RBAC + policy labels for authorization
- Add ABAC only when required for partner data

### Authorization boundary model

- **PDP (Policy Decision Point):** evaluates allow/deny + obligations
- **PEP (Policy Enforcement Point):** enforces PDP decision (API/evidence resolver/export service)
- **Obligation application:** transforms outputs or UI responses (generalize geometry, suppress export, show notice)

> [!NOTE]
> Cache policy-sensitive responses carefully (vary by auth/role). Tile caches must not leak restricted views.

[Back to top](#top)

---

## Policy-safe errors

A policy-safe error prevents public users from inferring restricted data existence.

**Principles**
- Prefer **uniform** 404/403 behavior for restricted resources (anti-enumeration).
- Error responses MUST include an **audit_ref** (or equivalent) for follow-up.
- Never include restricted dataset IDs, titles, bboxes, or coordinate hints in error messages.

Example error DTO (illustrative):

```yaml
ErrorResponse:
  type: object
  required: [error_code, message, audit_ref]
  properties:
    error_code: { type: string }
    message: { type: string }
    audit_ref: { type: string }
```

[Back to top](#top)

---

## Secrets and credentials

- Never store secrets in the repository.
- Do not print secrets in logs (CI or runtime).
- Use a secrets manager for production credentials.
- Use **scoped** credentials per source integration / pipeline runner.
- Rotate secrets regularly and record rotation events in audit logs (policy-safe).

Recommended controls:
- secret scanning + push protection (if available)
- CI checks that fail if common secret patterns are detected
- least-privilege IAM for object storage, DB, and message queues

[Back to top](#top)

---

## Supply chain integrity

Recommended before broad public release:

- Pin dependencies and verify checksums where possible
- Generate SBOMs (SPDX) for build artifacts
- Generate build provenance attestations (SLSA/in-toto)
- Verify attestations server-side (or in the release lane)
- Pin container images by digest (no `:latest`)

> [!PROPOSED]
> Adopt keyless signing via OIDC-based identity for releases (organization policy permitting).  
> If attestations are required, the release lane should **block** when missing.

> [!IMPORTANT]
> Do **not** fetch remote attestations directly from untrusted origins in the browser.  
> Proxy through a server that verifies signatures and strips secrets.

[Back to top](#top)

---

## Audit logs and run receipts

Audit logs and run receipts may contain sensitive operational details.

Minimum protections:
- Append-only storage
- Redaction for PII and restricted information
- Access restricted to authorized stewards/operators
- Defined retention policy (TBD) and deletion policy (TBD)

### Receipts as security artifacts

Run receipts should be treated as security-critical because they prove:
- which inputs produced which outputs
- which policy decisions and obligations were applied
- which environment and container digest executed the run

> [!IMPORTANT]
> If receipts are missing, incomplete, or unverifiable, treat the associated outputs as **not promotable**.

[Back to top](#top)

---

## Security gates and required checks

Security-related checks should be treated as **merge-required gates** (fail closed).

### CI security gate categories (minimum)

- **Policy tests:** fixtures-driven allow/deny/obligation outcomes
- **Schema/profile validation:** strict validation of DCAT/STAC/PROV and internal schemas
- **Contract tests:** OpenAPI / DTO compatibility checks
- **Integration tests:** evidence resolver resolves sample refs without policy bypass
- **E2E tests:** UI shows policy notices; citations resolve through the evidence resolver
- **Secret scanning:** fail if secrets are detected (or substitute)
- **Dependency review:** fail on risky dependency diffs (or substitute)

### Anti-skip requirement

> [!WARNING]
> A required security gate must not be skippable via `paths:` filters, `if:` conditions, or job fanout.
> Prefer a single always-runs gate-summary job marked as required in rulesets/branch protection.

### Security control matrix (recommended)

| Control | Statement | Enforced in | Evidence artifact |
|---|---|---|---|
| SC-01 | Default deny on policy evaluation error | Runtime + CI | Policy test fixtures |
| SC-02 | EvidenceRefs resolve to EvidenceBundles | Runtime + CI | Resolver integration tests |
| SC-03 | Catalog triplet cross-links are valid | CI | Validator + link-check report |
| SC-04 | Public exports contain no restricted fields | CI + Runtime | Export scan + obligation record |
| SC-05 | Focus Mode citation verification is a hard gate | Runtime + CI | Golden queries + citation coverage |
| SC-06 | Release artifacts are signed/attested (when required) | CI + Release | SBOM + attestation verification logs |

See: `.github/README.md` for the governance-side “required checks registry” (if present).

[Back to top](#top)

---

## Incident response

> [!NOTE]
> This is a minimal policy. Full incident runbooks should live in `docs/runbooks/` (if present).

### Severity (recommended levels)

- **SEV-1:** confirmed restricted/PII/sensitive-location exposure; active exploitation; policy bypass at runtime
- **SEV-2:** high-impact vulnerability with plausible exploitation; supply-chain integrity break
- **SEV-3:** moderate issues; defense-in-depth gaps; misconfigurations with limited impact
- **SEV-4:** low-impact issues; hardening tasks

### Immediate actions for suspected data exposure

1. **Contain:** disable exports / deny affected endpoints / revoke credentials as needed (fail closed).
2. **Preserve evidence:** record request IDs, run IDs, dataset_version_id, digests (avoid copying data).
3. **Assess scope:** identify affected roles, datasets, and time window.
4. **Remediate:** patch + add tests/gates; rebuild projections if needed.
5. **Notify:** coordinate with governance stewards for disclosure obligations.

[Back to top](#top)

---

## Coordinated disclosure

We aim to follow coordinated disclosure:
- Report privately
- Allow maintainers reasonable time to investigate and patch
- Public disclosure should be coordinated once fixes are available

> [!PROPOSED SAFE HARBOR — PENDING LEGAL REVIEW]
> We welcome good-faith security research that avoids:
> - privacy violations or exfiltration of restricted data,
> - social engineering,
> - physical disruption,
> - denial-of-service testing against shared infrastructure,
> - publishing exploit details before a fix is available.

[Back to top](#top)

---

## References

- `kfm://doc/kfm-gdg-vnext-2026-02-20` — KFM Definitive Design & Governance Guide (vNext)
- Repo root `README.md` (trust membrane + Promotion Contract), if present
- `.github/README.md` (required checks registry + CI gate index), if present
- `CONTRIBUTING.md` (security expectations for contributors), if present

[Back to top](#top)

---

<details>
<summary><strong>Appendix A — PR Security Checklist</strong></summary>

- [ ] No secrets committed (including in docs/examples)
- [ ] Policy changes include fixtures + tests (allow/deny/obligations)
- [ ] Catalog changes validate (DCAT/STAC/PROV) and links resolve
- [ ] Runtime changes preserve cite-or-abstain hard gate
- [ ] Any sensitive-location logic includes “no coordinate leakage” tests
- [ ] Any export change is policy-gated and scanned
- [ ] Any auth/cache change is reviewed for cross-role leakage

</details>

<details>
<summary><strong>Appendix B — Minimal Verification Steps (convert Unknown → Confirmed)</strong></summary>

Run these checks and attach outputs to the next revision of this file:

- [ ] Confirm repo paths: capture `git rev-parse HEAD` and `tree -L 3`
- [ ] Extract required checks from `.github/workflows/*` and list which block merges
- [ ] Verify policy pack exists and tests run in CI (default deny enforced)
- [ ] Verify evidence resolver exists and resolves sample EvidenceRefs end-to-end
- [ ] Verify Focus Mode evaluation harness exists (golden queries + citation gate)

</details>
