<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3ec8fca2-c9fd-4c6a-a15a-3be33781a10e
title: SECURITY.md
type: standard
version: v1
status: draft
owners: KFM stewards; platform maintainers
created: 2026-03-07
updated: 2026-03-07
policy_label: public
related: [docs/governance/, docs/runbooks/, docs/adr/]
tags: [kfm, security, responsible-disclosure]
notes: [Root-level repository security policy; replace TODO placeholders before public use]
[/KFM_META_BLOCK_V2] -->

# Security Policy
Responsible disclosure, supported versions, and security expectations for Kansas Frontier Matrix.

> **Status:** draft  
> **Owners:** KFM stewards; platform maintainers  
> **Path:** `/SECURITY.md`  
> **Quick links:** [Supported versions](#supported-versions) · [Report a vulnerability](#reporting-a-vulnerability) · [Security boundaries and scope](#security-boundaries-and-scope) · [Disclosure process](#disclosure-process) · [Baseline hardening expectations](#baseline-hardening-expectations)

## Purpose
This policy explains how to report security issues, which release lines are supported, and which security boundaries matter most for KFM.

KFM is an evidence-first, policy-governed system. Security for this repository therefore includes not only classic software vulnerabilities, but also any defect that bypasses the governed API boundary, weakens policy enforcement, exposes protected data, downgrades sensitivity labels, breaks provenance or evidence resolution, or allows uncited/unsafe publication.

## Repo fit
- **Repo fit:** Root-level security policy for the Kansas Frontier Matrix code, data, CI/CD, and publication pipeline.
- **Upstream dependencies:** Governance contracts, policy rules, runbooks, ADRs, cloud/IAM configuration, CI workflows, and dataset/source policies.
- **Downstream consumers:** Contributors, reviewers, operators, governance stewards, release managers, and security researchers.

## Accepted inputs
Use this policy to report issues involving:
- authentication, authorization, or privilege escalation
- secrets exposure, token leakage, or insecure credential handling
- CI/CD, supply-chain, provenance, or artifact-signing weaknesses
- direct access to protected storage, operational databases, or raw buckets
- policy bypass, rights/sensitivity downgrade, or publication outside governed gates
- sensitive-location, PII, or culturally sensitive data exposure
- API, worker, search, graph, tile, and evidence-resolution vulnerabilities
- AI/Focus behavior that can disclose protected data, fabricate citations, or bypass abstention and policy rules

## Exclusions
The following usually do **not** belong in this channel unless they have a clear security impact:
- feature requests or UX suggestions
- ordinary data corrections, transcription fixes, or historical interpretation disputes
- broken links, spelling mistakes, or routine documentation cleanup
- public-source content complaints without evidence of a policy or access-control failure
- support requests for local setup, ingestion, or development tooling

## Supported versions
Replace this table with the repo’s exact release lines if they differ.

| Branch / release line | Supported | Notes |
| --- | --- | --- |
| `main` (or the protected default branch) | ✅ | Primary maintained line |
| Latest tagged release | ✅ | Security fixes should land here or be backported if required |
| Older tags, stale branches, forks, and personal mirrors | ❌ | Reproduce on a supported line before filing |

## Security boundaries and scope
KFM treats the following as high-value security boundaries:
- the **trust membrane** between user-facing clients and governed backend services
- promotion gates from **RAW → WORK/QUARANTINE → PROCESSED → cataloged/published**
- policy enforcement for rights, sensitivity, sovereignty, and evidence resolution
- contributor/reviewer/operator separation of duty
- CI/CD provenance, SBOMs, attestations, and release approvals
- secrets handling, IAM/OIDC federation, branch protection, and protected environments

If you find a path that lets a user, workflow, model, or external client bypass those boundaries, treat it as a security issue.

## Reporting a vulnerability
**Do not open a public GitHub issue for an undisclosed vulnerability.**

Report privately using one of the channels below:
1. **Primary:** `TODO-security@your-org.example`
2. **Backup:** private GitHub Security Advisory (if enabled for this repo)
3. **Fallback:** `TODO-governance@your-org.example`

If you support encrypted reporting, add your PGP or age public key here:
- **PGP / age key:** `TODO`

Please include as much of the following as you can:
- affected repository, branch, tag, or commit SHA
- affected environment (`dev`, `stage`, `prod`, local, CI, etc.)
- issue type and expected impact
- exact reproduction steps
- proof of concept, logs, screenshots, or request/response traces
- whether sensitive data was accessed, and if so, the **minimum** evidence needed to prove impact
- suggested remediation, if you have one

### Sensitive data handling in reports
If the issue involves protected records, precise coordinates, Indigenous/culturally sensitive material, personal data, or private evidence bundles:
- do **not** paste full raw datasets into the report
- redact values wherever possible
- share the minimum reproducible sample needed for validation
- prefer hashes, record IDs, EvidenceRefs, catalog IDs, or affected object paths over raw payloads
- if precise coordinates are the problem, report the fact of exposure before sharing the coordinates themselves

## Response targets
These are the repo’s default targets unless maintainers publish stricter SLAs:
- **Acknowledgement:** within 3 business days
- **Initial triage:** within 10 business days
- **Status updates:** at least every 10 business days for active cases
- **Coordinated disclosure target:** 90 days by default, extended when necessary for sensitive data, third-party coordination, or public-sector/legal review

Severity and remediation timelines may vary based on exploitability, blast radius, affected policy boundaries, and whether protected data was exposed.

## Disclosure process
KFM follows a review-first, auditable remediation path:
1. privately acknowledge and triage the report
2. reproduce on a supported branch or release
3. classify severity and identify affected boundaries, datasets, and environments
4. contain the issue (revoke, rotate, quarantine, disable, or block promotion as needed)
5. fix through a reviewed change set with tests, docs, and rollback notes
6. validate the fix with CI, policy checks, and any required steward/governance review
7. publish an advisory or release note when safe to do so

Where required, remediation artifacts should include evidence of review, validation, and rollback readiness.

## Safe-harbor expectations for researchers
We support good-faith security research conducted to help protect the project and its users.

Please:
- avoid social engineering, phishing, or physical attacks
- avoid destructive testing, persistence, or privilege escalation beyond what is necessary to prove the issue
- avoid bulk exfiltration or unnecessary retention of data
- stop and report promptly if you encounter sensitive or regulated information
- do not publicly disclose the issue before coordinated remediation is complete
- respect rate limits, shared infrastructure, and service availability

If your testing may affect live systems, contact us first.

## Baseline hardening expectations
The following expectations apply to this repository and its release process:
- no long-lived secrets in source control
- least-privilege IAM and short-lived credentials where possible
- protected branches and required reviews for policy-significant changes
- automated scans for secrets, PII/sensitive content, and classification/sensitivity regressions
- CI gates for schema validity, API contracts, data quality, catalog integrity, and policy checks
- SBOM/provenance/attestation checks where required by the release lane
- auditable receipts, versioned rollback paths, and immutable release logs
- docs updated with behavior changes that affect lifecycle, policy, or contributor workflow

## Security review triggers
The following changes require heightened review and may need governance sign-off:
- introduction of a new external data source
- exposure of a new public API, search, graph, tile, or evidence endpoint
- changes to policy rules, rights labels, sensitivity handling, or sovereignty controls
- new AI/Focus behavior that can produce public-facing claims or summaries
- cloud IAM, OIDC, secrets, signing, or deployment-workflow changes
- changes that broaden access to raw, work, processed, or protected publication surfaces

## Dependency and supply-chain issues
When reporting supply-chain issues, include:
- package / image / action name and exact version
- SBOM reference if available
- whether the issue affects build-time, run-time, or release-time trust
- whether attestation, signature, or provenance verification can be bypassed

## Incident handling notes
Maintainers should treat confirmed incidents as auditable events. Each incident should have:
- a timestamped report record
- severity and scope assessment
- containment and remediation notes
- rollback or mitigation record
- follow-up tasks for hardening, monitoring, docs, or policy updates

## Public communication
Public communication should happen **after** containment and validation, unless earlier disclosure is legally required or clearly necessary to protect users. Advisories should describe:
- affected versions and environments
- impact
- remediation or upgrade path
- whether data exposure occurred
- credits, if the reporter wants to be acknowledged

## Contact placeholders to replace before public use
Before publishing this file, replace:
- `TODO-security@your-org.example`
- `TODO-governance@your-org.example`
- `TODO` PGP / age key
- supported version matrix, if `main` / latest release are not the right policy