<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/f8375fd0-0f12-4ad4-bb38-f3048c11cfad
title: .github Automation & Governance
type: standard
version: v1
status: draft
owners: KFM Maintainers (see CODEOWNERS)
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - .github/
tags:
  - kfm
  - github
  - ci
  - governance
  - devsecops
notes:
  - This file documents intended responsibilities and guardrails for repository automation.
[/KFM_META_BLOCK_V2] -->

# .github Automation & Governance

How this repo uses GitHub community health files + Actions workflows to **enforce KFM governance invariants** (fail-closed, evidence-first).

**Status:** Draft • **Owners:** see `CODEOWNERS` • **Badges:** `ci:merge-blocking` `policy:default-deny` `docs:link-checked` `security:actions-hardened`

---

## Navigate

- [Scope](#scope)
- [Directory layout](#directory-layout)
- [What belongs in workflows](#what-belongs-in-workflows)
- [Merge-blocking gates](#merge-blocking-gates)
- [Promotion Contract alignment](#promotion-contract-alignment)
- [Security and secrets](#security-and-secrets)
- [Changing this folder](#changing-this-folder)
- [Troubleshooting](#troubleshooting)
- [Appendix: terms](#appendix-terms)

---

## Scope

This README is the **operational index** for the `.github/` folder.

It should answer:

- What “governance-by-construction” means for CI in this repo.
- Where workflows live and what they MUST check.
- How to safely modify CI/CD without breaking policy, provenance, or security.

Non-goals:

- It is **not** a full repo overview (see the root `README.md`).
- It is **not** a substitute for the actual workflow YAML (YAML is the source of truth for automation behavior).

> **WARNING:** Do not put credentials, private URLs, or sensitive infrastructure details in this folder’s docs. Assume `.github/` is highly visible.

---

## Directory layout

The exact contents of `.github/` will vary by repo maturity. The table below describes the *intended* responsibilities.

~~~text
.github/
  README.md                   # this document (responsibilities + guardrails)
  workflows/                  # GitHub Actions workflows (CI lanes, release, policy gates)
  actions/                    # optional: composite actions pinned + reviewed like code
  ISSUE_TEMPLATE/             # optional: issue templates
  PULL_REQUEST_TEMPLATE.md    # optional: PR template (checklists + governance prompts)
  SECURITY.md                 # optional: security policy + vulnerability reporting
  dependabot.yml              # optional: dependency update configuration
  CODEOWNERS                  # optional: required reviewers for sensitive paths
~~~

### “Sensitive paths” we usually treat as governance-critical

- `.github/workflows/**`
- `.github/actions/**`
- `policy/**` (if policy-as-code is present)
- `schemas/**` (if contract schemas are present)
- `docs/reports/story_nodes/**` (if Story Nodes are in-repo)

If you add new sensitive paths, update `CODEOWNERS` accordingly.

---

## What belongs in workflows

Workflows are not “developer convenience.” In KFM posture they are **promotion gates**: they decide what is allowed to ship.

### CI flow in one picture

~~~mermaid
flowchart LR
  pr[Pull Request] --> lanes[CI lanes (merge gates)]
  lanes -->|pass| reviews[Required reviews / CODEOWNERS]
  reviews --> merge[Merge]
  merge --> promote[Promotion / Release jobs]
  promote --> published[Published artifacts + catalogs]
  published --> surfaces[Map • Story • Focus trust surfaces]
  lanes -->|fail| blocked[Fail closed (nothing ships)]
~~~

### Recommended workflow “lanes”

Use separate jobs or reusable workflows so failures are easy to interpret.

- **Quality lane**: lint, typecheck, unit tests.
- **Contract lane**: schema validation for catalogs + contracts.
- **Policy lane**: policy-as-code checks (deny-by-default).
- **Evidence lane**: link checking / citation resolution (no broken citations).
- **Security lane**: dependency scanning, SBOM/provenance attestations (as adopted).
- **UX lane**: accessibility smoke checks for UI trust surfaces.

---

## Merge-blocking gates

These are the *minimum* merge-blocking checks this repo should enforce when the corresponding surfaces exist.

### Minimum required gates (baseline)

- **lint + typecheck** (frontend + backend)
- **schema validation** for any changed catalog artifacts (DCAT/STAC/PROV)
- **Story Node template validation** (if Story Nodes exist)
- **policy tests** must pass (deny-by-default with explainable failures)
- **spec_hash tests** must pass (deterministic identity)
- **link checker** must pass (no broken citations / cross-links)
- **security scanning** (dependency vulnerabilities); SBOM generation where adopted
- **accessibility smoke checks** for UI changes (at least keyboard navigation for evidence drawer)

> **NOTE:** If your repo does not yet include a given surface (e.g., Story Nodes), gate it when that surface is introduced—not before. But once introduced, gates are not optional.

---

## Promotion Contract alignment

KFM uses a “Promotion Contract” concept: a dataset/version (or governed story) is only promotable when the evidence, policy inputs, and integrity signals are present.

Map CI checks to Promotion gates so people know *why* something failed.

| Promotion gate | What it typically asserts | Where it usually runs |
|---|---|---|
| A — Identity & versioning | Deterministic IDs, version increments, `spec_hash` invariants | CI (PR + main) |
| B — Licensing & rights | License + rights holder present for every distribution | CI (PR) + publish gate |
| C — Sensitivity & redaction | Policy label set; obligations recorded (generalize/redact) | CI (PR) + runtime |
| D — Catalog triplet validation | DCAT/STAC/PROV schema-valid + cross-linked | CI (PR) |
| E — Run receipt & checksums | Run receipts emitted; artifact digests match | CI (main) + release |
| F — Policy + contract tests | OPA/Conftest fixtures pass; API contracts stable | CI (PR) |
| G — Recommended extras | SBOMs, attestations, e2e tests, perf smoke | CI (PR/main) |

> **TIP:** Keep gate failures explainable. A denial message should point to the missing field, violated constraint, and remediation.

---

## Security and secrets

The `.github/` folder is a high-impact supply-chain surface. Treat it as sensitive code.

### GitHub Actions hardening checklist

- [ ] Workflows use **least privilege** permissions (don’t default to broad write permissions).
- [ ] Secrets are stored only in GitHub Secrets / Environments (never committed).
- [ ] Avoid `pull_request_target` for untrusted PRs (or lock it down so it never checks out PR code).
- [ ] Third-party Actions are pinned to a **commit SHA** (not a mutable tag).
- [ ] Critical workflow changes require review via `CODEOWNERS`.
- [ ] Branch protection requires PR review + passing checks; no force-push to protected branches.

### Secret and token guidance

- Prefer short-lived credentials (OIDC / keyless flows) over long-lived PATs.
- Never echo secrets to logs, even if they are “masked.”
- Keep environment variables policy-safe (no leaking restricted identifiers into job summaries).

---

## Changing this folder

Treat modifications under `.github/` as a governed change.

### When you change workflows/actions/templates

1. **Describe intent** in the PR: what risk it reduces, what gate it affects.
2. **Classify impact**:
   - Low: formatting, comments, non-executing docs.
   - Medium: workflow logic changes without new privileges.
   - High: permissions, secrets handling, deployment/promotion logic, policy gates.
3. **Run/observe**: confirm the workflow run shows the intended checks and no secrets leak.
4. **Require review**: if `CODEOWNERS` is present, don’t bypass it.

### Definition of Done for governance-critical workflow changes

- [ ] Required checks still merge-block.
- [ ] Permissions are explicitly set (least privilege).
- [ ] Any new third-party Actions are pinned + reviewed.
- [ ] Policy/contract checks remain fail-closed.
- [ ] Documentation in this README is updated if responsibilities changed.

---

## Troubleshooting

### “Link checker” fails

Common causes:

- A Story Node references a missing citation.
- DCAT/STAC/PROV cross-links aren’t reciprocal.
- An EvidenceRef points to an object that no longer exists after a refactor.

Fix by:

- Validating citations locally (if a local tool exists), then updating the references at the source.

### “Policy gate” fails (deny-by-default)

Common causes:

- Missing license/rightsholder fields.
- Missing or invalid policy label.
- Required obligations not declared for sensitive data.

Fix by:

- Adding explicit metadata rather than weakening the policy.

### “spec_hash mismatch”

Common causes:

- Non-canonical JSON ordering / whitespace changes.
- Inputs changed without bumping version or updating manifests.

Fix by:

- Canonicalizing inputs and ensuring versioning rules are followed.

---

## Appendix: terms

- **Promotion Contract:** The minimum conditions required before publishing/promoting a dataset version or governed story.
- **Fail closed:** If a gate can’t prove safety/compliance, the default outcome is “no.”
- **Policy-as-code:** Governance rules expressed as executable policy (deny-by-default + tests) used in CI and runtime.
- **Catalog triplet:** DCAT (dataset), STAC (assets), PROV (lineage) — cross-linked so evidence resolution is deterministic.
- **Run receipt:** Per-run record capturing inputs/outputs/digests/timestamps/policy decisions for auditability.
- **EvidenceRef:** A stable reference scheme used to resolve citations into evidence bundles.

---

_This file is intentionally “boring.” If it’s hard to read, it will not be followed._
