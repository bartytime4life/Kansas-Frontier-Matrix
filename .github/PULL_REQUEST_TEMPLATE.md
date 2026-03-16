<!--
Kansas Frontier Matrix pull request contract.

Complete every section that applies.
If a section does not apply, write "N/A" rather than deleting it.
Keep the change small, reversible, and explicit about what is CONFIRMED, INFERRED, PROPOSED, UNKNOWN, or NEEDS VERIFICATION.
For undisclosed security findings, use SECURITY.md rather than describing exploit details in a public PR.

Helpful references:
- README.md
- CONTRIBUTING.md
- .github/README.md
- SECURITY.md
- .github/CODEOWNERS
-->

## Summary
- What changed:
- Why:
- Linked issue / ADR / discussion:

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
- [ ] `configs/`
- [ ] `contracts/`
- [ ] `data/`
- [ ] `docs/`
- [ ] `examples/`
- [ ] `infra/`
- [ ] `migrations/`
- [ ] `packages/`
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
- [ ] No new direct client → store or client → model-runtime bypass

### Public claim surface
- [ ] No public claim surface affected
- [ ] Public claim surface affected (described below)

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
-

### Files / paths / contracts
-

### User-visible or operator-visible impact
-

### Evidence / publication impact
- Evidence / citation path:
- Policy / review / release state impact:
-

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
- Commands / jobs / reports:
- Sample inputs / fixtures:
- Screenshots / visual diffs / recordings:
- Negative-path coverage (deny / abstain / stale / generalized / rollback / correction):
-

---

## Docs, contracts, and policy
- [ ] README / docs updated
- [ ] Runbook / ADR update included
- [ ] OpenAPI / schema / contract updated
- [ ] Policy bundle / fixtures / decision logic updated
- [ ] No docs / contract / policy change required (explained below)

Explanation:
-

---

## Risk, rollout, and rollback
- Risk level: low / medium / high
- Rollout plan:
- Rollback plan:
- Correction / supersession / quarantine implications:
- Operational impact:
-

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
- [ ] Security disclosure concerns handled through `SECURITY.md` if needed
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
- [ ] No silent contract or policy drift
- [ ] Review burden identified
- [ ] Ready for governed merge
