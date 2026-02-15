<!--
GOVERNED ARTIFACT NOTICE
FILE: .github/README.md
This README defines repo governance + CI enforcement surfaces. Changes are production changes.
If you change meaning (not just phrasing), route through governance review (CODEOWNERS + CI gates).
-->

# .github/ — KFM GitHub Operations, Governance & CI Gates

![Governed Artifact](https://img.shields.io/badge/governed-artifact-critical)
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-enforced-important)
![Policy](https://img.shields.io/badge/policy-default%20deny-111827)
![Promotion Contract](https://img.shields.io/badge/promotion%20contract-required-red)
![Receipts](https://img.shields.io/badge/receipts-run__manifest%20%7C%20spec__hash-6a5acd)
![Catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-2563eb)
![Supply Chain](https://img.shields.io/badge/supply%20chain-SBOM%20%7C%20attestations%20optional-6b7280)
![CI](https://img.shields.io/badge/CI-required-success)
![Focus Mode](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-critical)
![Kill Switch](https://img.shields.io/badge/kill--switch-required-orange)

> [!IMPORTANT]
> **Why this file exists**
>
> This `.github/README.md` is the **single source of truth** for repo governance and CI enforcement:
> what must exist in `.github/`, which checks are mandatory, and which rules are **non-negotiable**.
>
> **Change impact:** Treat changes to this file as **production changes** (governance surface).

---

## 📌 Quick links

- Repo root README: `../README.md`
- CODEOWNERS: `./CODEOWNERS` *(required)*
- Security policy: `./SECURITY.md`
- PR template: `./PULL_REQUEST_TEMPLATE.md`
- Workflows: `./workflows/`
- Dependabot: `./dependabot.yml`
- Release drafter: `./release-drafter.yml`

Governed planes:
- Docs: `../docs/README.md`
- Data: `../data/README.md`
- Backend: `../src/README.md`
- Web UI: `../web/README.md`
- Tools: `../tools/README.md`
- Tests: `../tests/README.md`
- Releases: `../releases/README.md`

---

## 🧭 Table of contents

- [Governance header](#governance-header-treat-as-production)
- [Non-negotiables](#non-negotiables-kfm-invariants)
- [Governance surfaces](#governance-surfaces-what-is-protected)
- [Branch protections and required checks](#branch-protections-and-required-checks)
- [CI gates](#ci-gates-no-merge-without-proof)
- [Promotion Contract enforcement](#promotion-contract-enforcement)
- [Evidence resolver contract](#evidence-resolver-contract)
- [Kill switch requirements](#kill-switch-requirements)
- [Workflow security](#workflow-security)
- [Supply chain](#supply-chain-release-and-deploy)
- [When CI fails](#when-ci-fails-quick-diagnosis)
- [Definition of done](#definition-of-done-for-githubreadmemd)

---

## Governance header (treat as production)

| Field | Value |
|---|---|
| Document | `.github/README.md` |
| Status | **Governed** (changes require review) |
| Applies to | workflows, branch protections, CODEOWNERS, templates, release gating, promotion enforcement |
| Version | `v1.6.0` |
| Effective date | **2026-02-15** |
| Review cadence | quarterly + out-of-band for security advisories/toolchain changes |
| Owners | defined in `.github/CODEOWNERS` *(required)* |
| Review triggers | changes touching `.github/**`, `policy/**`, `contracts/**`/`schemas/**`, `data/**`, `docs/**`, `releases/**` |

> [!WARNING]
> **Fail-closed governance rule:** If a required enforcement surface is missing (policy, receipts, catalogs, contract tests), the system denies promotion/merge/release by default.

---

## Non-negotiables (KFM invariants)

1) **Trust membrane**
- UI/external clients never access databases or object storage directly.
- All access is via governed API gateway + policy decision point.
- Core backend logic never bypasses repository interfaces to talk to storage.

2) **Fail-closed policy**
- Default deny at policy boundaries (runtime + CI).
- Missing policy inputs / missing receipts / missing catalogs / missing citations → deny/abstain.

3) **Promotion Contract is mandatory**
- Raw → Work → Processed promotion requires:
  - receipts (run manifest/record) + validation reports
  - deterministic checksums
  - catalogs (DCAT always; STAC conditional; PROV required)
  - sensitivity classification + redaction provenance
- No contract → no publish.

4) **Deterministic identity**
- `spec_hash = sha256(JCS(spec))` (RFC 8785 canonical JSON).
- Receipts include `spec_schema_id` + `spec_recipe_version` where applicable.

5) **Evidence-first**
- Evidence references are resolvable (`prov://`, `stac://`, `dcat://`, `doc://`, `graph://`, optional `oci://`).
- Focus Mode must cite or abstain and always returns `audit_ref`.

6) **Immutability**
- `releases/` is append-only; never edit an existing release folder.

---

## Governance surfaces (what is protected)

These paths are governance-critical and must be CODEOWNED and CI-gated:

- `.github/**` (workflows, templates, CODEOWNERS, security policy)
- `policy/**` (OPA/Rego, tests, bundles)
- `contracts/**` and/or `schemas/**` (Promotion Contract + receipt/catalog/api schemas)
- `data/**` (zones, catalogs, receipts, checksums)
- `docs/**` (standards, templates, governance docs, Story Nodes)
- `src/**` (API boundary, pipelines, evidence resolver, audit)
- `releases/**` (immutable shipping records)

> Any attempt to weaken gates for these surfaces is a governance incident until reviewed and resolved.

---

## Branch protections and required checks

### Required branch protection settings (e.g., `main`)
- PRs required; no direct pushes
- CODEOWNERS reviews required
- required status checks must pass (no bypass)
- no force push
- signed commits/tags strongly recommended
- “require branches up to date” recommended

### Required status checks (minimum)
- `docs`
- `stories`
- `contracts`
- `receipts`
- `catalogs`
- `policy`
- `api-contract`
- `build`

Recommended:
- `security`
- `supply-chain` (release)
- `e2e` (nightly/pre-release)
- `watchers` (if watchers exist)

---

## CI gates (no merge without proof)

CI must validate:

### Docs & Story Nodes
- markdown lint + link-check + template validation
- Story Node v3 validator + citation resolvability checks

### Contracts & schemas
- Promotion Contract schema + receipt schemas + catalog minimums
- API contract diff: no breaking changes on `/api/v1`

### Receipts & promotion proofs
- run manifest schema validation
- `spec_hash` semantics validation where applicable
- checksums verification

### Catalogs & provenance
- DCAT validation (always)
- STAC validation (when spatial assets exist)
- PROV validation (required lineage)
- cross-link integrity / link-check

### Policy-as-code
- `opa test` unit tests
- `conftest test` regression suite (default deny, promotion guard, cite-or-abstain)

---

## Promotion Contract enforcement

Promotion is merge-blocking:
- any change that results in new/updated `data/processed/**` must also include valid receipts and catalogs
- CI must deny if receipts/catalogs/checksums are missing or invalid
- policy must deny serving artifacts that lack required promotion proofs

---

## Evidence resolver contract

Acceptance criteria (non-negotiable):
- every `citation.ref` returned by Focus Mode resolves to a human-readable evidence view in ≤ 2 API calls
- missing refs → 404
- unauthorized/policy denied → 403 (non-leaky)
- supported schemes: `prov://`, `stac://`, `dcat://`, `doc://`, `graph://` (+ optional `oci://`)

---

## Kill switch requirements

KFM must be able to disable risky surfaces without redeploying code.

Required behavior:
- if kill switch enabled (`KFM_GOVERNANCE_KILL_SWITCH=true` or equivalent):
  - publish/promote workflows must fail closed
  - release workflows must not publish artifacts
  - Focus Mode can be disabled via policy without code changes

---

## Workflow security

- pin third-party actions by commit SHA
- least-privilege `GITHUB_TOKEN` permissions per job
- avoid `pull_request_target` unless absolutely necessary
- secrets scanning/push protection enabled
- prefer OIDC/GitHub Apps over long-lived PATs

---

## Supply chain (release and deploy)

When enabled:
- SBOM (SPDX) produced/verified
- provenance attestations (in-toto/SLSA) produced/verified
- signatures verified (cosign/rekor)

Release records in `releases/` must be immutable and verifiable by checksums.

---

## When CI fails (quick diagnosis)

| Failure | Usually means | Fix |
|---|---|---|
| `contracts` | schema mismatch | update schema + fixtures; keep fail closed |
| `receipts` | run manifest invalid / checksum mismatch | regenerate deterministically; fix spec_hash or checksums |
| `catalogs` | invalid DCAT/STAC/PROV or broken links | repair catalogs; fix cross-links |
| `policy` | policy regression | update policy/tests; do not weaken deny |
| `api-contract` | `/api/v1` breaking change | refactor or bump to `/api/v2` |
| `docs/stories` | template/citation failures | fix headings/citations/resolution |
| `build` | build/smoke failures | align Docker contexts; fix env wiring |

---

## Definition of done for `.github/README.md`

- [ ] required `.github` items exist and are CODEOWNED
- [ ] branch protections enforce PR + CODEOWNERS + required checks
- [ ] CI gates run on every PR and fail closed
- [ ] promotion contract enforced via receipts + catalogs + checksums
- [ ] evidence resolver and cite-or-abstain contracts are enforced
- [ ] releases are immutable and verifiable via `releases/`
```
::contentReference[oaicite:0]{index=0}
