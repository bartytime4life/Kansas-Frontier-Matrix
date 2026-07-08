<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/security-policy-root
title: SECURITY.md — Security Policy and Vulnerability Disclosure
type: policy-facing-readme
version: v0.2
status: draft
owner: TODO-security-owner-plus-repo-steward-plus-docs-steward-plus-policy-steward-plus-release-steward
created: NEEDS VERIFICATION — file existed before this expansion
updated: 2026-07-08
policy_label: public; security; vulnerability-disclosure; sensitive-reporting; deny-by-default; fail-closed; non-authoritative
owning_root: repo-root
responsibility: public repository security policy and vulnerability disclosure entrypoint; explains how to report security-sensitive defects, what not to disclose publicly, what KFM treats as security-sensitive, how reports route to governance, and what remains needs-verification while deferring enforceable security doctrine to docs/security, admissibility decisions to policy, exposure posture to infra and governed APIs, evidence/proofs/receipts to data roots, and release/rollback/correction decisions to release governance
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - README.md
  - docs/security/README.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/governed-api.md
  - policy/README.md
  - release/README.md
  - tools/validators/README.md
  - tools/watchers/README.md
  - data/receipts/
  - data/proofs/
  - release/
notes:
  - "This file replaces the previous short SECURITY.md placeholder. The old placeholder used security@kfm.local; this update removes that non-operational address and marks reporting channels as NEEDS VERIFICATION until an actual private channel is configured."
  - "Do not publish security-sensitive vulnerability details in public issues, PRs, comments, discussions, screenshots, logs, or generated artifacts."
  - "SECURITY.md is the public disclosure entrypoint. It does not itself decide policy, approve release, authorize testing, or create exceptions to deny-by-default sensitive-data posture."
  - "Executable security controls, GitHub private vulnerability reporting settings, CODEOWNERS, branch protection, CI gates, runtime routes, emitted receipts, signed releases, and incident-response automation remain NEEDS VERIFICATION unless separately checked."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Security policy

![status](https://img.shields.io/badge/status-draft-orange)
![posture](https://img.shields.io/badge/posture-deny--by--default-critical)
![public-path](https://img.shields.io/badge/public_path-governed--API--only-blue)
![disclosure](https://img.shields.io/badge/disclosure-private--first-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** This file is the public entrypoint for reporting security-sensitive defects in Kansas Frontier Matrix (KFM) without exposing sensitive locations, private data, credentials, unreleased artifacts, or exploit details in public channels.

---

## Security posture

KFM is a governed, evidence-first, map-first, time-aware spatial knowledge system. Its security posture follows the same trust rules as the rest of the repository:

- **deny by default** where rights, sensitivity, identity, source role, evidence, or release state is unclear;
- **least privilege** for public/API/runtime surfaces;
- **cite-or-abstain** for evidence-backed claims;
- **fail closed** for missing validation, missing policy decisions, missing release support, or unresolved sensitive content;
- **watcher-as-non-publisher** for watchers, CI, and intake jobs;
- **promotion as governed state transition**, not a file move;
- **public clients use governed APIs and released public-safe artifacts only**, never RAW / WORK / QUARANTINE / candidate / internal stores / direct model runtime output.

This policy is intentionally conservative because KFM may handle or reference sensitive ecology, archaeology, infrastructure, living-person, DNA/genomic, private-land, cultural, source-rights, and exact-location material.

[Back to top](#top)

---

## Reporting a vulnerability

> [!IMPORTANT]
> **Do not file public GitHub issues, PR comments, Discussions, screenshots, or logs for security-sensitive defects.** Public disclosure can expose exact sensitive locations, credentials, private records, exploit paths, unreleased artifacts, or reconstruction hints.

### Preferred private channel

The preferred channel is **GitHub private vulnerability reporting** if it is enabled for this repository.

If private vulnerability reporting is not enabled, use a private channel to the repo steward or security owner. The exact security contact is currently **NEEDS VERIFICATION**; do not use placeholder addresses such as `security@kfm.local` as if they were operational.

A future update should configure and document at least one verified private contact path, such as:

- GitHub private vulnerability reporting;
- a verified project security email;
- a private maintainer contact path listed in `CODEOWNERS` or a security contact register.

[Back to top](#top)

---

## What to include in a report

When reporting privately, include only the minimum necessary detail to reproduce and triage the issue.

| Include | Guidance |
|---|---|
| A short summary | What class of problem you found. |
| Affected path or surface | File path, route, workflow, artifact, validator, watcher, policy, or UI surface if known. |
| Impact | What could be exposed, bypassed, corrupted, or overclaimed. |
| Reproduction steps | Minimal steps that avoid touching real sensitive data where possible. |
| Evidence | Redacted screenshots, logs, or snippets if needed. Prefer synthetic examples. |
| Sensitivity notes | Say if the issue involves rare species, archaeology, infrastructure, living-person data, DNA/genomics, private land, cultural material, credentials, tokens, or exact locations. |
| Suggested fix | Optional; keep it bounded and reversible. |

Do **not** include raw secrets, private keys, access tokens, exact sensitive locations, living-person records, DNA/genomic material, source-restricted data, exploit payloads against live systems, or unredacted production logs unless a maintainer explicitly requests a secure transfer path.

[Back to top](#top)

---

## Security-sensitive issues in KFM

Report privately if you find any issue that could cause or enable:

| Category | Examples |
|---|---|
| Sensitive location exposure | Exact rare-species locations, exact precontact archaeology coordinates, culturally sensitive places, burial/sacred sites, protected habitat reconstruction, private stewardship locations. |
| Living-person or DNA exposure | Living-person genealogy, person-parcel joins, consent bypasses, DNA/genomic details, private family linkage, identity reconstruction. |
| Infrastructure exposure | Critical-asset internals, restricted transport/facility topology, vulnerability detail, sensitive operational status, interior/secure facility detail. |
| Lifecycle bypass | RAW / WORK / QUARANTINE / candidate / internal/canonical store data reaching public API, UI, map, tile, export, graph, Focus Mode, embedding, or AI surfaces. |
| Policy bypass | Allowing public release without rights, sensitivity, source-role, evidence, review, release, correction, or rollback support. |
| Source-role collapse | Candidate, modeled, aggregate, administrative, synthetic, contextual, or AI-generated material being presented as observed, authoritative, verified, regulatory, or released truth. |
| AI/runtime bypass | Model output reaching public surfaces without evidence, citation, policy, release, or receipt controls. |
| Watcher or CI publication | Watchers, intake jobs, automation, or CI writing directly to catalog, triplet, published, release, or public runtime surfaces. |
| Credential or secret exposure | Tokens, API keys, signing keys, private endpoint URLs, credentials in logs, fixture leaks, or secret-bearing generated artifacts. |
| Integrity and release failures | Unsigned or unverifiable releases, missing rollback targets, missing correction paths, digest/spec-hash drift, branch-protection bypass, unreviewed release mutation. |
| Supply-chain risk | Dependency compromise, unpinned toolchain, unexpected network access in no-network jobs, artifact tampering, compromised CI workflow, malicious generated files. |

[Back to top](#top)

---

## What KFM should never publish by default

The following content is denied from public surfaces unless a governed, reviewed, rights-cleared, sensitivity-cleared, released, public-safe derivative explicitly allows a narrower representation:

- DNA segments, genotype records, genomic relationships, or DNA-derived identity assertions;
- living-person genealogy, private person records, or person-parcel joins without appropriate consent and policy support;
- exact rare-species or rare-plant locations;
- exact precontact archaeological, burial, sacred, or culturally sensitive coordinates;
- critical infrastructure interior, vulnerability, or operationally sensitive detail;
- sensitive transport/facility topology that could expose restricted or vulnerable infrastructure;
- private-land stewardship details or source-restricted field notes;
- raw credentials, tokens, private keys, signing material, or secret-bearing configuration;
- RAW / WORK / QUARANTINE / candidate / internal/canonical store records on public surfaces;
- unreleased, unsigned, unverifiable, unreviewed, or rollback-less artifacts;
- generated AI claims that lack resolved evidence, citation, policy, release, and receipt support.

[Back to top](#top)

---

## Scope

### In scope for private reporting

- repository files and documentation that could create an unsafe security posture;
- policy, validator, watcher, release, receipt, evidence, source-registry, or lifecycle bypasses;
- public API/UI/map/tile/export/graph/search/Focus Mode/AI surfaces that may leak unreleased or sensitive material;
- CI, workflow, package, dependency, signing, artifact, or release-integrity weaknesses;
- incorrect documentation that would instruct maintainers to publish, expose, or bypass governance controls;
- fixtures or examples that accidentally contain real sensitive data.

### Out of scope without prior written authorization

- active scanning, load testing, fuzzing, exploitation, or social engineering against live systems;
- attempts to access, modify, delete, scrape, exfiltrate, or deanonymize real data;
- testing that reveals or triangulates exact sensitive locations;
- denial-of-service testing;
- physical security testing;
- attacks against third-party services, source providers, or platforms not controlled by this repository;
- public proof-of-concept disclosure before maintainers have had a chance to assess and remediate.

If a test would touch real sensitive data or a live public surface, stop and ask for an authorized test plan through a private channel.

[Back to top](#top)

---

## Handling and triage posture

Security reports should be handled as governed work items, not casual bug reports.

| Stage | Expected posture |
|---|---|
| Intake | Keep the report private. Assign a security owner. Record minimal metadata without spreading sensitive details. |
| Classification | Label impact, affected surfaces, sensitivity category, lifecycle state, source role, rights posture, and public exposure risk. |
| Containment | Disable or restrict affected public surfaces, watchers, workflows, releases, or access paths if needed. Prefer fail-closed behavior. |
| Remediation | Make the smallest reversible fix that restores trust boundaries. Add tests/fixtures/policy updates where behavior changes. |
| Validation | Verify the fix against schemas, policy, source roles, sensitivity, release/correction/rollback, and public-surface boundaries. |
| Release/correction | Publish only through governed release or correction processes. Include rollback target where material. |
| Post-incident | Record what changed, what was exposed, what was not exposed, how evidence was handled, and what must be monitored. |

[Back to top](#top)

---

## Safe harbor posture

Good-faith security research is welcome when it:

- avoids privacy violations and sensitive-location exposure;
- avoids service disruption and data destruction;
- does not access, modify, or exfiltrate non-public data;
- uses synthetic or minimized examples whenever possible;
- reports privately and gives maintainers time to respond;
- follows any written scope and test limits provided by maintainers.

This repository does not currently publish a formal legal safe-harbor program. Treat safe harbor as **NEEDS VERIFICATION** until the project publishes a signed/approved policy.

[Back to top](#top)

---

## Maintainer checklist

When a security report is received, maintainers should verify:

- [ ] private reporting channel was used and public details were minimized;
- [ ] security owner and repo steward are assigned;
- [ ] affected files, routes, workflows, artifacts, validators, watchers, policies, releases, or public surfaces are identified;
- [ ] sensitive data class is recorded without leaking restricted details;
- [ ] source-role, lifecycle, rights, sensitivity, evidence, policy, review, release, correction, and rollback impacts are assessed;
- [ ] containment plan fails closed and avoids silent public fallback;
- [ ] remediation includes tests, fixtures, policy, docs, and runbook updates where behavior changed;
- [ ] any affected release has a correction or rollback path;
- [ ] public communication does not disclose exploit details, exact sensitive locations, credentials, or private records.

[Back to top](#top)

---

## Open verification items

These are checkable but not confirmed by this SECURITY.md update:

- [ ] Enable and verify GitHub private vulnerability reporting for the repository.
- [ ] Replace the contact placeholder with a verified private security contact.
- [ ] Confirm CODEOWNERS security ownership for `SECURITY.md`, `docs/security/`, `policy/`, `infra/`, `.github/workflows/`, `release/`, `tools/validators/`, and `tools/watchers/`.
- [ ] Verify branch protection and security-relevant CI gates.
- [ ] Verify secret scanning, dependency scanning, CodeQL/static analysis, and no-network default behavior where applicable.
- [ ] Verify incident-response runbooks under `docs/runbooks/` or another accepted home.
- [ ] Verify release signing, rollback, correction, and receipt behavior.
- [ ] Verify that public API/UI/map/AI routes cannot read RAW / WORK / QUARANTINE / candidate / internal stores directly.

[Back to top](#top)

---

## Related docs

- [`README.md`](README.md) — root project posture and current repo-evidence boundary.
- [`docs/security/README.md`](docs/security/README.md) — human-facing security doctrine, threat model, and incident-response lane.
- [`docs/doctrine/trust-membrane.md`](docs/doctrine/trust-membrane.md) — public/private boundary doctrine.
- [`docs/doctrine/lifecycle-law.md`](docs/doctrine/lifecycle-law.md) — RAW to PUBLISHED lifecycle invariant.
- [`docs/doctrine/truth-posture.md`](docs/doctrine/truth-posture.md) — cite-or-abstain posture.
- [`docs/doctrine/directory-rules.md`](docs/doctrine/directory-rules.md) — placement and authority-boundary rules.
- [`docs/architecture/governed-api.md`](docs/architecture/governed-api.md) — governed public API boundary.
- [`policy/README.md`](policy/README.md) — policy authority entrypoint.
- [`release/README.md`](release/README.md) — release, rollback, and correction entrypoint.
- [`tools/validators/README.md`](tools/validators/README.md) — validator-root posture.
- [`tools/watchers/README.md`](tools/watchers/README.md) — watcher-root non-publisher posture.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced short placeholder with governed security policy and vulnerability disclosure entrypoint. Removed non-operational placeholder email and marked private reporting channel as NEEDS VERIFICATION. | **CONFIRMED README / controls NEEDS VERIFICATION** |
