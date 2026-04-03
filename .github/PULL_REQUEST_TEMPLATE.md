<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/REVIEW-REQUIRED
title: Pull Request Template
type: standard
version: v1
status: published
owners: @bartytime4life
created: REVIEW-REQUIRED
updated: REVIEW-REQUIRED
policy_label: public
related: [README.md, CHANGELOG.md, CONTRIBUTING.md, .github/README.md, .github/CODEOWNERS, .github/SECURITY.md, SECURITY.md]
tags: [kfm, github, pull-request, governance]
notes: [doc_id and created/updated remain REVIEW-REQUIRED until canonical doc registry and target-branch git history are verified.]
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
-->

<!-- Keep this template synchronized with README.md, CHANGELOG.md, CONTRIBUTING.md, .github/README.md, .github/SECURITY.md, SECURITY.md, and .github/CODEOWNERS on the same branch. -->

> Fill every applicable section.  
> Use `N/A` rather than deleting sections.  
> Keep truth labels honest and keep `UNKNOWN` / `NEEDS VERIFICATION` visible until closed.  
> Link validation evidence, CI runs, proof packs, screenshots, reviewer notes, or follow-up issues where they exist.  
> If the working branch proves repo state that public `main` docs do not yet show, say so explicitly below.

## Summary
- What changed:
- Why:
- Linked issue / ADR / discussion:
- Evidence / proof-pack / run links:
- Working-branch evidence delta (if public `main` is stale for this PR):

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

### Truth posture summary
Fill only the labels that apply to this PR.

- CONFIRMED:
- INFERRED:
- PROPOSED:
- UNKNOWN:
- NEEDS VERIFICATION:

---

## What changed

### Behavior
- N/A

### Files / paths / contracts
- N/A

### User-visible or operator-visible impact
- N/A

### Evidence / publication impact
- Authoritative / derived boundary impact:
- Evidence / citation path:
- Runtime answer / abstain / deny / error impact:
- Policy / review / release state impact:
- Correction / supersession implications:

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

### Evidence
- CI / workflow / report links:
- Proof pack / manifest / attestation links:
- Commands / jobs / reports:
- Sample inputs / fixtures:
- Screenshots / visual diffs / recordings:
- Negative-path coverage (deny / abstain / stale / generalized / rollback / correction):
- Not applicable / gaps still open:

---

## Docs, contracts, and policy
- [ ] CHANGELOG updated or explicitly not needed
- [ ] README / docs updated
- [ ] Runbook / ADR update included
- [ ] OpenAPI / schema / contract updated
- [ ] Policy bundle / fixtures / decision logic updated
- [ ] No docs / contract / policy change required (explained below)

Explanation:
- N/A

---

## Risk, rollout, and rollback
- Risk level: low / medium / high
- Rollout plan:
- Rollback plan:
- Correction / supersession / quarantine implications:
- Operational impact:
- Public / trust-surface implications:

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

</details>

<details>
<summary>API / contract / schema</summary>

- [ ] Backward-compatibility impact described
- [ ] Stable envelope / error behavior reviewed
- [ ] Example valid inputs / outputs updated
- [ ] Invalid fixtures or failure cases updated
- [ ] `audit_ref`, evidence, or policy fields preserved where relevant

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
