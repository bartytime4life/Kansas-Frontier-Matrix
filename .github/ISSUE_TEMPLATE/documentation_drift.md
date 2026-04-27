---
name: Documentation drift
about: Report KFM documentation that conflicts with evidence, source authority, repo state, policy posture, or implementation reality.
title: "docs: drift — <path or topic>"
labels: ""
assignees: ""
---

# Documentation drift report

> [!IMPORTANT]
> Use this issue when documentation may be out of sync with evidence, source authority, repository state, policy posture, or implementation reality. Do **not** paste secrets, private endpoints, exact sensitive locations, living-person data, DNA/genomic material, controlled archaeology locations, rare-species occurrence details, or other restricted evidence into this issue.

## Drift summary

<!-- One or two sentences. What appears wrong, stale, overclaimed, conflicting, or under-specified? -->



## Affected documentation

| Field | Value |
|---|---|
| Primary path | `TODO: docs/path.md` |
| Related path(s) | `TODO: related docs, README, schema, policy, contract, fixture, workflow, release artifact, or issue template` |
| Area / lane | `TODO: governance / source registry / schema / policy / UI / AI / MapLibre / Cesium / domain lane / release / other` |
| Public-facing? | `TODO: yes / no / unknown` |

## What kind of drift is this?

- [ ] Documentation claims implementation behavior that is not currently verified.
- [ ] Documentation conflicts with current repository files, schemas, tests, workflows, manifests, logs, or generated artifacts.
- [ ] Documentation treats `PROPOSED`, `LINEAGE`, `EXPLORATORY`, or `UNKNOWN` material as current canon.
- [ ] Documentation collapses source roles, evidence roles, review state, release state, or policy posture.
- [ ] Documentation implies public release before promotion, proof, validation, rights review, or sensitivity review.
- [ ] Documentation exposes or encourages unsafe access to `RAW`, `WORK`, `QUARANTINE`, unpublished candidates, direct model output, or canonical/internal stores.
- [ ] Documentation presents AI, maps, tiles, scenes, dashboards, search, vector indexes, summaries, or derived layers as sovereign truth.
- [ ] Documentation has stale or unverified badges, workflow names, route names, DTOs, owners, branch names, versions, endpoints, licenses, source terms, or deployment claims.
- [ ] Documentation has broken links, broken anchors, missing successor links, or unclear archive/lineage placement.
- [ ] Documentation omits rollback, correction, validation, or review requirements for a material behavior change.
- [ ] Other: `TODO`

## Current documented claim

<!-- Quote only the smallest useful excerpt or summarize the claim. Include the path, heading, line range, screenshot, rendered page, or artifact reference when available. -->



## Evidence that challenges or refines the claim

| Evidence type | Location / command / artifact | What it shows |
|---|---|---|
| Current repo evidence | `TODO` | `TODO` |
| Test / workflow / validator evidence | `TODO` | `TODO` |
| Runtime / log / dashboard evidence | `TODO` | `TODO` |
| KFM doctrine or source corpus | `TODO` | `TODO` |
| External official source | `TODO` | `TODO` |
| Generated artifact / proof object | `TODO` | `TODO` |

> [!WARNING]
> If evidence is not directly visible, mark the issue `UNKNOWN` or `NEEDS VERIFICATION`. Do not upgrade plausible design language into current implementation fact.

## Evidence mode

- [ ] `LOCAL_REPO_CONFIRMED` — mounted checkout evidence is available.
- [ ] `PARTIAL_REPO` — some repo files are visible, but key tests/workflows/runtime/proof objects are missing.
- [ ] `PUBLIC_REPO_EVIDENCE` — public repository evidence only; not proof of this working branch.
- [ ] `CORPUS_ONLY` — attached docs/source corpus only.
- [ ] `NO_REPO_EVIDENCE` — no direct repo evidence available.
- [ ] `NEEDS_VERIFICATION` — live source, version, security, rights, license, endpoint, branch, workflow, deployment, or runtime state must be checked.

## Proposed truth label for the affected claim

- [ ] `CONFIRMED`
- [ ] `INFERRED`
- [ ] `PROPOSED`
- [ ] `UNKNOWN`
- [ ] `NEEDS VERIFICATION`
- [ ] `CONFLICTED`
- [ ] `LINEAGE`
- [ ] `EXPLORATORY`
- [ ] `SUPERSEDED`
- [ ] `DENY`
- [ ] `ABSTAIN`
- [ ] `ERROR`

## KFM risk screen

- [ ] Low — wording, navigation, formatting, link, or clarity issue.
- [ ] Medium — affects contributor behavior, schema placement, source classification, validator expectations, or release readiness.
- [ ] High — could cause unsupported publication, policy bypass, evidence laundering, unsafe access, or false implementation confidence.
- [ ] Sensitive — involves archaeology, sacred/cultural sites, rare species, critical infrastructure, private landownership, living people, DNA/genomics, exact locations, credentials, private endpoints, or source terms.

If sensitive, describe only the public-safe shape of the issue:



## Expected correction

- [ ] Add missing truth label or evidence boundary.
- [ ] Correct unsupported implementation claim.
- [ ] Move material to lineage/archive with successor link.
- [ ] Mark material as `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, or `EXPLORATORY`.
- [ ] Add or update source authority / canon / lineage / exploratory register entry.
- [ ] Add or update ADR.
- [ ] Add or update schema, contract, policy, fixture, validator, or test reference.
- [ ] Add or update release, correction, rollback, proof, receipt, or catalog reference.
- [ ] Remove or replace stale badge, workflow claim, owner, route, endpoint, version, or deployment statement.
- [ ] Other: `TODO`

## Impacted surfaces

- [ ] `README.md`
- [ ] `.github/`
- [ ] `docs/`
- [ ] `docs/registers/`
- [ ] `docs/adr/`
- [ ] `docs/runbooks/`
- [ ] `contracts/`
- [ ] `schemas/`
- [ ] `policy/`
- [ ] `tests/`
- [ ] `tools/validators/`
- [ ] `data/registry/`
- [ ] `data/catalog/`
- [ ] `data/receipts/`
- [ ] `data/proofs/`
- [ ] `release/`
- [ ] `apps/`
- [ ] `packages/`
- [ ] `ui/` or `web/`
- [ ] Other: `TODO`

## Validation requested

- [ ] Verify affected path(s), heading(s), anchors, and links.
- [ ] Verify repo branch, dirty state, and current file contents before editing.
- [ ] Verify whether the claim is doctrine, implementation, lineage, proposal, or exploratory intake.
- [ ] Verify related schema/contract/policy/test/fixture/workflow references.
- [ ] Verify public-facing badges and status claims.
- [ ] Verify rights, sensitivity, source role, review state, release state, and correction lineage where publication is involved.
- [ ] Verify rollback/correction path if the document influences release, policy, or public output.

## Rollback or correction note

<!-- What should happen if the correction is wrong, incomplete, or later superseded? -->



## Maintainer triage

| Field | Value |
|---|---|
| Assigned owner | `TODO: verify owner` |
| Target PR | `TODO` |
| Severity | `TODO: low / medium / high / sensitive` |
| Resolution path | `TODO: docs edit / ADR / registry update / schema or policy update / test update / archive move / deny publication / other` |
| Review needed | `TODO: docs / architecture / source steward / policy / security / domain / release` |
