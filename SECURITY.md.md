<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<REVIEW-REQUIRED-UUID>
title: SECURITY
type: standard
version: v1
status: draft
owners: <REVIEW-REQUIRED>
created: <PRESERVE-IF-EXISTING-OR-SET-ON-COMMIT>
updated: 2026-03-15
policy_label: <REVIEW-REQUIRED>
related: [README.md, CONTRIBUTING.md, .github/CODEOWNERS, .github/README.md, .github/SECURITY.md]
tags: [kfm, security, vulnerability-disclosure, secure-development, governed-delivery]
notes: [Current-session source basis for this revision was the mounted March 2026 PDF corpus only; exact repo placement, owners, reporting channels, supported-release matrix, GitHub advisory configuration, and SLA values still require direct verification before commit.]
[/KFM_META_BLOCK_V2] -->

# SECURITY

Security reporting, disclosure, release protection, and secure-development expectations for the Kansas Frontier Matrix (KFM).

| Field | Value |
| --- | --- |
| **Status** | Draft · review required before commit |
| **Truth posture** | **CONFIRMED** doctrine · **PROPOSED** local realization detail · **UNKNOWN** unverified repo/runtime specifics |
| **Primary focus** | Vulnerability disclosure, trust-membrane protection, governed-release integrity, runtime exposure, evidence/citation failures, rights and sensitivity leakage |
| **Related** | [README.md](README.md) · [CONTRIBUTING.md](CONTRIBUTING.md) · [.github/CODEOWNERS](.github/CODEOWNERS) |

> [!IMPORTANT]
> This policy is intentionally evidence-bounded. The mounted workspace used for this revision exposed PDF corpus evidence only, not a directly inspectable repository tree, workflow directory, release inventory, reporting inbox, or advisory configuration. Replace every `<REVIEW-REQUIRED>` marker before commit, and verify whether the canonical file should live at `./SECURITY.md`, `.github/SECURITY.md`, or one authoritative location with the other delegating.

## Purpose

This file defines how security issues should be reported, triaged, fixed, verified, corrected, and disclosed for KFM.

KFM security is broader than classic software vulnerability handling. Because KFM is a governed spatial evidence system, security also includes failures that weaken governed publication, bypass the trust membrane, misrepresent derived layers as authoritative truth, expose restricted or sensitive material, break evidence resolution, or allow a runtime surface to return stronger certainty than the evidence and policy state support.

## Truth posture for this file

Use the following meanings whenever this policy distinguishes doctrine from local implementation detail:

- **CONFIRMED**: grounded in the mounted KFM doctrinal and security corpus.
- **PROPOSED**: recommended repo or runtime realization consistent with that doctrine, but not directly verified as mounted implementation in this session.
- **UNKNOWN**: not verified strongly enough in the current session to claim as active repo, workflow, deployment, or reporting reality.

This file states doctrine confidently where the corpus supports it and keeps local operational details visible as review-required where the workspace did not verify them.

## What counts as a security issue in KFM

Use this policy for reports involving any of the following:

- unauthorized access, authentication bypass, role escalation, or trust-membrane bypass
- direct or indirect client access to canonical stores, raw artifacts, restricted data, policy-protected surfaces, or model runtimes
- evidence-resolution failure that could make a consequential claim, map surface, dossier, story, export, or Focus-style response appear more trustworthy than it is
- uncited, unresolved, out-of-scope, or policy-bypassing AI/runtime behavior
- release-integrity failures such as missing proof objects, missing rollback posture, missing manifests or receipts, unsigned or mis-scoped artifacts, policy-bundle drift, or documentation drift that weakens safe operation
- secrets exposure, dependency or build compromise, supply-chain risk, or unsafe runtime/deployment configuration
- denial-of-service, resource exhaustion, or failure modes that materially threaten the governed path, correction capability, or reviewability of published state
- rights, sensitivity, location-exposure, or redaction/generalization failures that could expose protected or over-precise information

## What this policy does not cover

This file does **not** cover:

- ordinary feature requests, product ideas, or design discussion
- non-security bug reports with no exploit path, trust impact, or exposure consequence
- routine content or dataset corrections that do not involve confidentiality, integrity, policy bypass, or unsafe publication
- general support requests or usage help
- speculative claims with no reproduction details
- public proof-of-concept releases before coordinated handling
- retaliatory access, counterattack, or any testing that exceeds clearly authorized scope

Use [CONTRIBUTING.md](CONTRIBUTING.md) for normal contribution flow. Route ordinary content or data corrections through the governed correction workflow rather than this policy.

## KFM security principles

The following principles are the working security baseline for this repository:

| Principle | What it means here |
| --- | --- |
| **Governed publication first** | Security begins before public release, not after exposure. Promotion, publication, rollback, and correction are security-relevant state changes. |
| **Trust membrane** | Public and normal client surfaces must not bypass governed interfaces to reach canonical stores, raw artifacts, caches, or model runtimes directly. |
| **Authoritative vs. derived separation** | Search, graph, vector, tile, cache, summary, and AI layers are valuable but secondary. They must not silently become root truth. |
| **Fail closed** | Missing evidence, unresolved rights, unclear sensitivity, broken citations, missing review, or incomplete release state must narrow, deny, hold, quarantine, generalize, or abstain rather than publish optimistically. |
| **Evidence-bearing release** | Promotion is a governed state change, not a file move. Release integrity depends on manifests, receipts, provenance, signatures where required, and correction readiness. |
| **Least privilege** | Security applies across source onboarding, build, publish, runtime, correction, and recovery. Automation, services, and operators should have only the access they need. |
| **Operational evidence** | Logs, traces, metrics, audit joins, correction notices, and release references are part of the security system, not ornamental telemetry. |
| **Documentation as production surface** | Contracts, diagrams, examples, runbooks, and rollback instructions are security-relevant artifacts and must stay aligned with behavior. |
| **Visible incompleteness over false certainty** | Keep **UNKNOWN** visible until direct repo or runtime evidence exists. A calm negative outcome is safer than persuasive overclaiming. |

## Placement and discovery

Before merge, verify final placement and keep a single canonical policy source.

Recommended review questions:

- Should `./SECURITY.md` be the authoritative policy for repository readers?
- Is `.github/SECURITY.md` required for platform discovery, and if so, should it delegate to the canonical file rather than diverge?
- Are [README.md](README.md), [CONTRIBUTING.md](CONTRIBUTING.md), `.github/README.md`, and `.github/CODEOWNERS` aligned with this policy?

Avoid duplicated policies that can drift.

## Supported scope and release posture

Exact supported versions and release identifiers were **not** directly verified in the current session. Until the repo’s release inventory is surfaced, use the following posture:

| Scope | Current posture |
| --- | --- |
| **Exact release/version support matrix** | `NEEDS VERIFICATION BEFORE PUBLISH` |
| **Current governed code, documentation, contracts, and policy surface under active review** | In scope for private security reporting |
| **Promoted or outwardly visible artifacts and surfaces** | In scope |
| **Superseded, stale-visible, generalized, restricted, withdrawn, or corrected surfaces** | Still reportable; remediation may be correction, supersession, withdrawal, generalization, or rollback rather than a code patch |
| **Local-only phase-one runtime posture** | In scope, especially for exposure, policy, evidence, audit-path, and model-boundary failures |
| **Third-party systems not controlled by KFM** | Out of scope unless the issue is caused by KFM-controlled configuration, exposure, packaging, or handling |

## Report a vulnerability

Report security issues **privately first**.

### Private reporting channel

| Field | Value |
| --- | --- |
| **Primary private channel** | `<REVIEW-REQUIRED: monitored security inbox or private advisory path>` |
| **Secondary / fallback channel** | `<REVIEW-REQUIRED: maintainer fallback for confidential reports>` |
| **GitHub private advisory path** | `<REVIEW-REQUIRED>` |
| **Public issue tracker** | **Do not use** for undisclosed security findings |
| **Secure document exchange / PGP** | `<REVIEW-REQUIRED: add only if actually supported>` |
| **Acknowledgement target** | `<REVIEW-REQUIRED>` |
| **Status update cadence** | `<REVIEW-REQUIRED>` |
| **Coordinated disclosure target** | `<REVIEW-REQUIRED>` |

Until these values are verified and published, do **not** post exploit details in issues, discussions, pull requests, public chats, or public documentation.

### What to include in a report

A useful report includes:

- affected route, service, surface, component, artifact, or workflow
- clear impact statement
- reproduction steps
- smallest safe proof of concept
- expected safe behavior versus observed behavior
- whether the issue affects confidentiality, integrity, availability, policy enforcement, evidence linkage, release integrity, correction behavior, or runtime trust
- relevant logs, screenshots, traces, digests, or receipts, with sensitive data minimized or redacted
- any suggested mitigation, containment, or configuration guardrail

### Private report template

```text
Subject: [KFM SECURITY] short title

Affected surface:
Environment/profile:
Impact:
Category:
Reproduction steps:
Minimal proof of concept:
Expected safe behavior:
Observed behavior:
Sensitive data touched (if any):
Suggested mitigation/containment:
Disclosure constraints or timing concerns:
Contact preference:
```

## Good-faith research and disclosure boundaries

KFM prefers clear, bounded reporting lanes over silence and fear.

Good-faith research is welcome when it:

- stays within explicitly authorized scope or a separately published safe-harbor lane
- is privacy-respecting and data-minimizing
- is limited to what is necessary to demonstrate the issue
- is promptly and privately reported
- is documented clearly enough to support verification and remediation
- avoids degrading availability, exposing unrelated data, or expanding access beyond the minimum needed

This document does **not** by itself authorize unrestricted testing. If you accidentally encounter a vulnerability, stop after confirming the issue, avoid unrelated access, preserve only the minimum notes needed to explain it, and report it through the safest private channel available.

## Prohibited or out-of-scope testing

Unless KFM explicitly publishes written authorization, the following are out of scope:

- social engineering, phishing, or impersonation attempts against maintainers, contributors, vendors, or third parties
- physical intrusion or facility-access attempts
- denial-of-service, destructive load testing, or intentionally availability-impacting behavior
- accessing, downloading, retaining, modifying, or sharing unrelated data once exposure is demonstrated
- pivoting into third-party, shared, upstream, or provider systems
- mass scanning or automated exploitation beyond clearly agreed scope
- testing that targets exact locations, culturally sensitive materials, restricted historical material, or protected ecological content without explicit authorization
- retaliatory access, counterattack, or hack back

## Triage, remediation, correction, and disclosure

KFM should handle security as governed operational work rather than ad hoc heroics.

### Triage lens

Prioritize by:

- external reachability
- privilege yield
- exploit maturity
- asset and claim criticality
- policy, evidence, or rights impact
- ease of abuse in the real operating environment
- blast radius across public claims, maps, stories, exports, review surfaces, and runtime trust objects

### Remediation model

Separate these outcomes clearly:

| Outcome | Meaning |
| --- | --- |
| **Remediation** | Remove the weakness |
| **Mitigation** | Reduce exposure while the weakness remains |
| **Acceptance** | Explicitly own and time-bound residual risk |
| **Correction / supersession** | Change published truth state without pretending nothing happened |
| **Withdrawal / restriction / generalization** | Narrow or remove outward visibility when that is the safest governed result |

### Coordinated handling sequence

1. Receive privately.
2. Confirm scope, authorization, and immediate containment needs.
3. Reproduce safely.
4. Contain, mitigate, restrict, or generalize if users are exposed.
5. Fix or otherwise correct the unsafe state.
6. Verify with negative-path and happy-path tests.
7. Update contracts, examples, runbooks, diagrams, release evidence, and correction notices where behavior changed.
8. Promote, withdraw, supersede, or roll back with restore/correction readiness.
9. Coordinate disclosure once users are not needlessly exposed.

No public disclosure should outrun containment, fix verification, or an explicitly defined coordinated-disclosure window.

## Security-affecting change checklist

Use this checklist for any change that can alter trust, exposure, runtime safety, or release integrity.

- [ ] Threat model impact reviewed
- [ ] Trust membrane preserved; no new direct client/store or client/model bypass
- [ ] Least-privilege impact reviewed for users, services, jobs, automation, and secrets
- [ ] Policy and evidence resolution still occur in the request path where required
- [ ] Negative-path tests covered where relevant: deny, abstain, citation-negative, stale-state, correction, rollback, restore
- [ ] Sensitive data, exact locations, and restricted content remain correctly withheld, generalized, or review-gated
- [ ] Release evidence updated where behavior changed: manifests, receipts, proofs, review records, correction notices, or equivalent artifacts
- [ ] Documentation, examples, diagrams, and runbooks updated in the same governed change stream
- [ ] Model runtime remains behind the governed API and is not directly exposed
- [ ] Backup, restore, supersession, withdrawal, and correction implications reviewed

## FAQ

### Can I open a public issue?

Not for undisclosed security findings. Use a private reporting path.

### What if I am not sure whether the issue is security-related?

Report it privately if it could affect confidentiality, integrity, availability, policy enforcement, evidence linkage, release integrity, correction behavior, rights or sensitivity handling, or runtime trust.

### Does this policy cover AI and evidence issues?

Yes. In KFM, trust failures include uncited or unresolved consequential output, policy-bypass retrieval, unsafe model exposure, evidence-resolution failure, or any route that weakens cite-or-abstain behavior.

### What if I accidentally accessed data?

Stop immediately, minimize retention, do not continue exploring unrelated data, preserve only the minimum evidence needed to explain what happened, and report it privately.

### Are deny, abstain, hold, withdrawal, supersession, or generalization valid outcomes?

Yes. KFM is fail closed. Safe negative outcomes are first-class security outcomes.

## Appendix A — Indicative in-scope surfaces

| Surface | Example concern |
| --- | --- |
| Governed API | auth bypass, route-class drift, unpublished-scope reads, missing audit linkage |
| Policy/runtime path | policy bypass, missing deny/abstain behavior, out-of-scope response, post-generation citation failure |
| Evidence resolution | broken `EvidenceRef` → `EvidenceBundle` resolution, stale support, missing drill-through |
| Release and delivery | missing manifests, missing proof objects, unsigned or mis-scoped artifacts, rollback gaps |
| Docs / runbooks / contracts | drift that weakens safe operation or hides security-critical behavior |
| Local/runtime boundary | direct model exposure, direct database exposure, direct artifact-root reachability |
| Derived layers | stale or policy-incorrect search, vector, tile, graph, cache, or summary behavior presented as current truth |
| Corrections | missing correction notices, silent withdrawal, supersession without traceability |

## Appendix B — Needs-verification items before publish

- exact file placement: `./SECURITY.md` vs `.github/SECURITY.md` vs one canonical file with delegation
- dedicated private reporting channel
- owners and escalation path
- supported release/version matrix
- GitHub private advisory configuration
- acknowledgement and disclosure SLAs
- whether additional repo-local runbooks or incident documents should be linked here

[Back to top](#security)
