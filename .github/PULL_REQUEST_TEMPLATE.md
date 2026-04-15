<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/REVIEW-REQUIRED
title: Pull Request Template
type: standard
version: v1
status: published
owners: @bartytime4life
created: REVIEW-REQUIRED
updated: 2026-04-15
policy_label: public
related: [
  README.md,
  CHANGELOG.md,
  CONTRIBUTING.md,
  .github/README.md,
  .github/CODEOWNERS,
  .github/SECURITY.md,
  SECURITY.md,
  .github/workflows/README.md,
  apps/governed_api/README.md,
  schemas/contracts/v1/runtime/README.md,
  schemas/contracts/v1/runtime/runtime_response_envelope.schema.json,
  schemas/contracts/v1/source/source_descriptor.schema.json,
  tests/contracts/test_runtime_response_schema.py,
  tests/contracts/test_source_descriptor_schema.py,
  tests/e2e/runtime_proof/soil_moisture/README.md,
  tools/ci/render_runtime_proof_summary.py
]
tags: [kfm, github, pull-request, governance, runtime-proof, contracts]
notes: [
  doc_id and created/updated remain REVIEW-REQUIRED until canonical doc registry and target-branch git history are verified.
  This revision preserves the stronger old PR template while adding explicit runtime-proof, governed API, source-descriptor, validator, and runtime-schema review prompts.
]
[/KFM_META_BLOCK_V2] -->

<!--
Kansas Frontier Matrix pull request contract.

Complete every section that applies.
If a section does not apply, write "N/A" rather than deleting it.
Keep the change small, reversible, and explicit about what is CONFIRMED, INFERRED, PROPOSED, UNKNOWN, or NEEDS VERIFICATION.
For undisclosed security findings or exploit details, use the private reporting lane described in `.github/SECURITY.md` rather than describing them in a public PR.

Helpful references:
- README.md
- CHANGELOG.md
- CONTRIBUTING.md
- .github/README.md
- .github/CODEOWNERS
- .github/SECURITY.md
- SECURITY.md
- .github/workflows/README.md
- apps/governed_api/README.md
- schemas/contracts/v1/runtime/README.md
-->

<!-- Keep this template synchronized with README.md, CHANGELOG.md, CONTRIBUTING.md, .github/README.md, .github/CODEOWNERS, .github/SECURITY.md, SECURITY.md, workflow docs, and governed runtime / contract docs on the same branch. -->

> **Use this template completely.**
>
> Write `N/A` instead of deleting sections.
> Keep truth labels explicit.
> Link evidence, CI runs, proof packs, screenshots, reviewer notes, runtime-proof summaries, or follow-up issues where they exist.
> If working-branch evidence proves something that public `main` docs do not yet show, state that explicitly.

## Summary

- **What changed:**
- **Why:**
- **Linked issue / ADR / discussion:**
- **Evidence / proof-pack / run links:**
- **Working-branch evidence delta (if public `main` is stale for this PR):**

---

## Change type

- [ ] Documentation
- [ ] API / contract / schema
- [ ] Policy / governance
- [ ] Data / source onboarding / catalog
- [ ] UI / UX / Story / Evidence Drawer / Focus Mode
- [ ] Runtime / app code
- [ ] Infra / delivery / release
- [ ] Security-affecting
- [ ] Breaking / migration-significant

## Affected repo surfaces

- [ ] `.github/`
- [ ] `apps/`
- [ ] `brand/`
- [ ] `configs/`
- [ ] `contracts/`
- [ ] `data/`
- [ ] `docs/`
- [ ] `examples/`
- [ ] `infra/`
- [ ] `migrations/`
- [ ] `packages/`
- [ ] `pipelines/`
- [ ] `policy/`
- [ ] `schemas/`
- [ ] `scripts/`
- [ ] `tests/`
- [ ] `tools/`
- [ ] Other:

---

## KFM doctrine impact

### Truth path touched

- [ ] Source edge / RAW
- [ ] WORK / QUARANTINE
- [ ] PROCESSED
- [ ] CATALOG / TRIPLET
- [ ] PUBLISHED
- [ ] None

### Guardrails

- [ ] Truth path preserved
- [ ] Trust membrane preserved
- [ ] Cite-or-abstain preserved where relevant
- [ ] Fail-closed behavior preserved where relevant
- [ ] Docs / tests / templates / runbooks updated in the same change set where behavior changed
- [ ] No new direct client -> store or client -> model-runtime bypass

### Public claim surface

- [ ] No public claim surface affected
- [ ] Public claim surface affected (described below)

### Authoritative vs derived boundary

- [ ] No authoritative / derived boundary affected
- [ ] Authoritative / derived boundary affected (described below)

### Runtime outcome surface

- [ ] No runtime answer / abstain / deny / error behavior affected
- [ ] Runtime answer / abstain / deny / error behavior affected (described below)

### Governed runtime / source-admission impact

- [ ] No governed runtime or source-admission impact
- [ ] Source descriptor / source-admission impact (described below)
- [ ] Validator impact (described below)
- [ ] Runtime envelope / governed API impact (described below)
- [ ] Runtime-proof workflow / reviewer-summary impact (described below)

### Truth posture summary

Fill only the labels that apply to this PR.

- **CONFIRMED:**
- **INFERRED:**
- **PROPOSED:**
- **UNKNOWN:**
- **NEEDS VERIFICATION:**

---

## What changed

### Behavior

- N/A

### Files / paths / contracts

- N/A

### User-visible or operator-visible impact

- N/A

### Evidence / publication impact

- **Authoritative / derived boundary impact:**
- **Evidence / citation path:**
- **Runtime answer / abstain / deny / error impact:**
- **Policy / review / release state impact:**
- **Correction / supersession implications:**

### Governed runtime impact

- **Boundary impacted:** <!-- yes/no; explain if governed API boundary changed -->
- **Runtime envelope changed:** <!-- yes/no; list changed fields or outcomes -->
- **Source admission changed:** <!-- yes/no; describe source descriptor/schema/fixture impact -->
- **Validator behavior changed:** <!-- yes/no; describe rule/result impact -->
- **Workflow / reviewer summary changed:** <!-- yes/no; describe workflow or runtime-proof summary impact -->

---

## Validation

### Checks run

- [ ] Docs / link check
- [ ] Lint / format / type check
- [ ] Unit tests
- [ ] Integration tests
- [ ] Schema / contract validation
- [ ] Policy tests
- [ ] Reproducibility / generated-artifact checks
- [ ] Security-affecting checks
- [ ] Manual verification
- [ ] Not applicable (explained below)

### Contract / runtime checks

- [ ] Source descriptor schema test reviewed
- [ ] Runtime response schema test reviewed
- [ ] Validator tests reviewed
- [ ] Governed API route/app tests reviewed
- [ ] Runtime-proof tests reviewed
- [ ] Runtime-proof summary linked or attached when runtime behavior changed
- [ ] Not applicable (explained below)

### Evidence

- **CI / workflow / report links:**
- **Proof pack / manifest / attestation links:**
- **Commands / jobs / reports:**
- **Sample inputs / fixtures:**
- **Screenshots / visual diffs / recordings:**
- **Negative-path coverage (deny / abstain / stale / generalized / rollback / correction):**
- **Runtime-proof summary:**
- **Source descriptor schema test evidence:**
- **Runtime response schema test evidence:**
- **Governed API route/app test evidence:**
- **Not applicable / gaps still open:**

---

## Docs, contracts, and policy

- [ ] CHANGELOG updated or explicitly not needed
- [ ] README / docs updated
- [ ] Runbook / ADR update included
- [ ] OpenAPI / schema / contract updated
- [ ] Policy bundle / fixtures / decision logic updated
- [ ] No docs / contract / policy change required (explained below)

### Focused contract / runtime review

- [ ] Source descriptor impact reviewed (`contracts/source/`, `schemas/contracts/v1/source/`, source fixtures, or source schema tests)
- [ ] Validator impact reviewed (`tools/validators/`, validator rules, validator tests)
- [ ] Runtime contract impact reviewed (`schemas/contracts/v1/runtime/`, runtime schema fixtures/tests)
- [ ] Governed API impact reviewed (`apps/governed_api/`, routes, runtime builders, app assembly)
- [ ] Workflow / reviewer-summary impact reviewed (`.github/workflows/`, `tools/ci/`, runtime-proof artifacts)

**Explanation:**

- N/A

---

## Risk, rollout, and rollback

- **Risk level:** low / medium / high
- **Rollout plan:**
- **Rollback plan:**
- **Correction / supersession / quarantine implications:**
- **Operational impact:**
- **Public / trust-surface implications:**

---

## Review routing

- [ ] CODEOWNERS review required
- [ ] Steward / governance review required
- [ ] Product / UX review required
- [ ] Security review required
- [ ] Ops / release review required
- [ ] Keep as draft until evidence gaps are closed

---

## Optional change-specific checklists

<details>
<summary>Documentation / guidance</summary>

- [ ] Claims distinguish CONFIRMED / INFERRED / PROPOSED / UNKNOWN / NEEDS VERIFICATION where needed
- [ ] Paths / links / commands checked
- [ ] Screenshots / diagrams / examples updated if described behavior changed
- [ ] No wording silently overclaims mounted implementation, enforcement, or automation

</details>

<details>
<summary>Gatehouse / <code>.github</code> / control plane</summary>

- [ ] Current public `main` facts and working-branch-only facts are kept distinct
- [ ] `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `.github/README.md`, `.github/CODEOWNERS`, and security-routing docs stay aligned where touched
- [ ] Workflow / action / watcher claims do not overstate rulesets, required checks, OIDC wiring, or other platform-only settings
- [ ] No review, policy, or release-evidence bypass was introduced
- [ ] Runtime-proof workflow / artifact claims match visible workflow docs or branch files

</details>

<details>
<summary>API / contract / schema</summary>

- [ ] Backward-compatibility impact described
- [ ] Stable envelope / error behavior reviewed
- [ ] Example valid inputs / outputs updated
- [ ] Invalid fixtures or failure cases updated
- [ ] `audit_ref`, evidence, or policy fields preserved where relevant
- [ ] Source descriptor fixtures / schema impact reviewed where relevant
- [ ] Runtime response schema fixtures / tests updated where relevant

</details>

<details>
<summary>Dataset / source onboarding / catalog</summary>

- [ ] Source or registry entry updated
- [ ] Rights / license / policy label captured
- [ ] RAW capture and reproducibility plan described
- [ ] QA / validation checks added or updated
- [ ] Catalog / triplet impact (DCAT / STAC / PROV or equivalent) described
- [ ] Example `EvidenceRef` / `EvidenceBundle` path noted
- [ ] Public-safety / sensitivity / exact-location risk reviewed
- [ ] Source-admission / source-descriptor contract changes described where relevant

</details>

<details>
<summary>UI / UX / Story / Evidence Drawer / Focus Mode</summary>

- [ ] Map-first / time-aware behavior preserved
- [ ] Evidence visibility preserved or improved
- [ ] Accessibility impact reviewed
- [ ] Calm failure behavior reviewed
- [ ] Story / Focus changes remain evidence-bounded
- [ ] 2D / 3D decision impact explained if relevant

</details>

<details>
<summary>Infra / delivery / release</summary>

- [ ] Merge / promotion / release behavior impact described
- [ ] Observability impact described
- [ ] Backup / restore / rollback implications reviewed
- [ ] Proof / manifest / attestation / receipt impact described where relevant
- [ ] No automation self-approves policy-significant or public-truth changes
- [ ] Reviewer-summary artifact changes described where relevant

</details>

<details>
<summary>Security / rights / sensitivity</summary>

- [ ] No direct exposure of canonical stores, restricted artifacts, or model runtime
- [ ] Rights / redaction / generalization impact reviewed
- [ ] Security disclosure concerns handled through `.github/SECURITY.md` if needed
- [ ] Sensitive data / precise-location exposure reviewed
- [ ] Threat-model impact reviewed where relevant

</details>

---

## Definition of done

- [ ] Smallest reasonable change for the problem
- [ ] Reversible or rollback described
- [ ] Truth posture stated honestly
- [ ] Tests / validation evidence attached or linked
- [ ] Docs updated or explicitly justified
- [ ] No silent contract, policy, or trust-boundary drift
- [ ] Review burden identified
- [ ] Ready for governed merge
