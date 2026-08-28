<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidate-agriculture-county-year-panel-v0
title: Agriculture County-Year Panel v0 Candidate Dossier
type: release-candidate-dossier
version: v0.2
candidate_id: county_year_panel_v0
candidate_version: v0
status: draft; repository-grounded; blocked
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
candidate_lane: release/candidates/agriculture/
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: e0cf911663e5dd37d72a90ea549923ed3a8bc31d
  prior_blob: 0ecabb6ddc5616aa08dfe2101fa2775d4f2d42ca
related:
  - ../README.md
  - ../../README.md
  - ../../../agriculture/README.md
  - ../../../manifests/agriculture/README.md
  - ../../../promotion_decisions/README.md
  - ../../../rollback_cards/README.md
  - ../../../../data/processed/agriculture/README.md
  - ../../../../data/published/agriculture/README.md
  - ../../../../data/registry/sources/agriculture/README.md
  - ../../../../pipeline_specs/agriculture/README.md
  - ../../../../contracts/domains/agriculture/aggregation-receipt.md
  - ../../../../schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json
  - ../../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../../policy/domains/agriculture/README.md
  - ../../../../tests/release/README.md
  - ../../../../docs/domains/agriculture/PIPELINE.md
  - ../../../../docs/domains/agriculture/MISSING_OR_PLANNED_FILES.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../.github/CODEOWNERS
  - ../../../../.github/workflows/domain-agriculture.yml
  - ../../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidate, agriculture, county-year-panel, aggregate, evidence, sensitivity, rollback]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `county_year_panel_v0/` — Agriculture County-Year Panel v0 Candidate Dossier

> Repository-grounded review contract for a proposed county-by-year Agriculture candidate. It remains blocked because no concrete artifact, admitted source set, evidence closure, enforceable aggregation policy, substantive validation, accepted release handoff, correction path, or rollback target is established.

![status](https://img.shields.io/badge/status-BLOCKED-critical)
![candidate](https://img.shields.io/badge/candidate-county__year__panel__v0-blueviolet)
![release](https://img.shields.io/badge/release-not__approved-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Candidate status:** `PROPOSED` — blocked; not released and not approved for manifest preparation.

> [!IMPORTANT]
> At `main@e0cf9116…`, direct probes did not find candidate or shared-lane instances of the planned `ReleaseManifest`, `PromotionDecision`, or `RollbackCard`. The exact county-year pipeline specification is absent. The candidate remains `BLOCKED_FOR_EVIDENCE_AND_VALIDATION`. Differently named or unindexed material remains **UNKNOWN**.

[Purpose](#purpose) · [Status](#status) · [Authority](#authority) · [Snapshot](#snapshot) · [Candidate contract](#candidate-contract) · [Release gates](#release-gates) · [Validation](#validation) · [Automation](#automation) · [Review](#review) · [Evidence](#evidence) · [Open items](#open-items) · [Rollback](#rollback)

---

## Purpose

This directory records pre-publication review state for `county_year_panel_v0`. It may preserve blockers and point to governed support records. It must not store data, admit sources, execute pipelines, invent evidence or policy, create release objects, publish artifacts, or treat a README, workflow, test, schema, merge, or generated receipt as release approval.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move or repository event.

## Status

| Field | Current posture |
|---|---|
| Identity/version | **CONFIRMED from path:** `county_year_panel_v0`, `v0` |
| Meaning | **PROPOSED:** county-by-year Agriculture panel |
| Direct inventory | **CONFIRMED bounded search:** README only |
| Status/decision | `BLOCKED` / `BLOCKED_FOR_EVIDENCE_AND_VALIDATION` |
| Release/manifest readiness | Not released; not approved |
| Artifact, target, sources, evidence, policy, validation | **UNKNOWN / not established** |
| Manifest, promotion, rollback instances | **NOT FOUND in checked paths** |
| Human review | Pending |
| Public/release effect of this README | None |

`CONFIRMED` means verified here; `PROPOSED` means design or interpretation; `UNKNOWN` is unresolved; `NEEDS VERIFICATION` is checkable but open; `CONFLICTED` is an unresolved disagreement; `LINEAGE` is planning history only.

## Authority

The path belongs under [`release/candidates/agriculture/`](../README.md). It owns the dossier, not candidate bytes or final release records.

| Concern | Owning lane |
|---|---|
| Agriculture release orientation | [`release/agriculture/`](../../../agriculture/README.md) |
| Manifest | [`release/manifests/`](../../../manifests/agriculture/README.md) or accepted successor |
| Promotion decision | [`release/promotion_decisions/`](../../../promotion_decisions/README.md) |
| Rollback/review card | [`release/rollback_cards/`](../../../rollback_cards/README.md) or accepted successor |
| Candidate artifact | [`data/processed/agriculture/`](../../../../data/processed/agriculture/README.md) or accepted staging lane |
| Published carrier | [`data/published/agriculture/`](../../../../data/published/agriculture/README.md) |
| Source admission | [`data/registry/sources/agriculture/`](../../../../data/registry/sources/agriculture/README.md) |
| Meaning / shape / policy | `contracts/` / `schemas/` / `policy/` |

[`MISSING_OR_PLANNED_FILES.md`](../../../../docs/domains/agriculture/MISSING_OR_PLANNED_FILES.md) proposed candidate-local release files. Current release guidance routes those families to shared lanes, so the candidate-local paths are **LINEAGE / CONFLICTED** until an ADR or migration resolves topology.

## Snapshot

| Surface | Safe status |
|---|---|
| Candidate directory and checked release-instance paths | README only; planned instances absent at checked paths |
| Exact county-year pipeline specification | Not established |
| QuickStats source/spec records | Eight-line `PROPOSED` placeholders; not admitted/active |
| AggregationReceipt | Draft contract plus empty permissive schema; not enforced |
| ReleaseManifest | Permissive stub requiring only `id`; declared validator absent |
| NASS tests and direct release tests | Docstring/README-only; dedicated suite not established |
| Agriculture policy | Draft intent; concrete enforcement unknown |
| Agriculture workflow | Read-only readiness holds; not validation or proof |
| Release dry-run workflow | TODO-only scaffold; not release proof |

Path presence does not prove source admission, artifact production, evidence closure, policy enforcement, release readiness, or publication.

## Candidate contract

The candidate name supports a proposed county-by-year aggregate panel. It does not establish fields, counties, years, measures, units, sources, suppression rules, or public products.

Every field must preserve source identity/role, rights, query or snapshot identity, spatial/temporal support, units, revision/suppression state, and EvidenceRef lineage. Aggregate statistics must not become field observations; classified/modelled products must not become direct observation; Soil and other domain truth must remain owned by their domains.

Before `READY_FOR_REVIEW`, provide:

- immutable candidate artifact pointer, digest, and artifact manifest;
- accepted grain, keys, fields, units, time, geography, and typed schema;
- admitted SourceDescriptors, roles, rights, and reproducible source-head/query identity;
- claim/field-to-EvidenceBundle mapping;
- accepted aggregation/suppression profile and typed `AggregationReceipt`;
- PolicyDecision with audience, obligations, and safe reason codes;
- schema, uniqueness, unit, time, geography, source-role, evidence, and sensitivity validation;
- verified human reviewer assignments;
- governed PromotionDecision and ReleaseManifest pointers; and
- correction, withdrawal, supersession, and rollback records/drills.

## Release gates

Exact field/operator, parcel-adjacent, small-cell, facility, irrigation, chemical, livestock, storage, logistics, and cross-domain inference fail closed for public exposure. Use reviewed aggregation, suppression, redaction, generalization, audience restriction, or denial. Style-only hiding is not a sensitivity control.

Current holds: `HOLD_FOR_EVIDENCE`, `HOLD_FOR_VALIDATION`, `HOLD_FOR_POLICY`, `HOLD_FOR_REVIEW`, `HOLD_FOR_RELEASE_TOPOLOGY`, and `HOLD_FOR_ROLLBACK`.

`PROMOTE_TO_MANIFEST` would authorize manifest preparation only, not publication. `DENY`, `ABSTAIN`, and `ERROR` remain fail-closed outcomes. The current decision authorizes no promotion or release.

## Validation

A mature public-safe, no-network suite must reject missing artifacts/digests, unadmitted or rights-unclear sources, source-role collapse, unstable county/crop/year keys, mixed units, unclear suppression, unresolved EvidenceRefs, missing aggregation receipts, small-cell or identity inference, stale/revised sources, missing policy/review/manifest/rollback, direct public access to candidate/processed data, and AI prose offered as evidence.

Current repository evidence does not establish a candidate-specific executable suite or accepted command. [`tests/release/`](../../../../tests/release/README.md) is README-only in its bounded direct inventory.

## Automation

| Workflow | Current boundary |
|---|---|
| [`domain-agriculture`](../../../../.github/workflows/domain-agriculture.yml) | Read-only readiness holds; does not validate Agriculture truth, build proof, or release |
| [`release-dry-run`](../../../../.github/workflows/release-dry-run.yml) | TODO-only echo scaffold; does not assemble candidate or enforce gates |

Both use ordinary pull-request/push triggers, `ubuntu-latest`, and floating `actions/checkout@v7`. No inspected workflow uses `pull_request_target`, secrets, OIDC, deployment, upload, or publication writes. Branch-protection coupling remains **UNKNOWN**.

> [!CAUTION]
> `domain-agriculture` excludes one known placeholder test path and treats another Agriculture `test_*.py` as an implementation signal. A second docstring-only placeholder exists. Do not assume the readiness workflow passes; its run result and placeholder-detection logic remain **NEEDS VERIFICATION**.

A green hold or TODO result is not validation, EvidenceBundle closure, proof, manifest readiness, release approval, or publication authority.

## Review

[`CODEOWNERS`](../../../../.github/CODEOWNERS) routes `/release/` to `@bartytime4life`. That is review routing only, not a StewardshipAssignment, independent review, PolicyDecision, release approval, or publication authority.

Before manifest preparation, verify distinct responsibilities for domain meaning, candidate data/pipeline, source/rights, evidence, policy/sensitivity/aggregation, validation, release decision, and correction/rollback. Merge approval remains separate from release/publication approval.

## Evidence

| Evidence | Bounded conclusion |
|---|---|
| Prior README `0ecabb6d…` and candidate parent READMEs | Identity, states, packet and handoff expectations; prior file was a shell |
| [`release/agriculture/README.md`](../../../agriculture/README.md) | Agriculture release index/router; shared record lanes |
| Direct probes/search | Planned instances and exact spec not found at checked paths |
| Agriculture planning and [`PIPELINE.md`](../../../../docs/domains/agriculture/PIPELINE.md) | Thin-slice, lifecycle, source-role, aggregation intent; wiring remains proposed |
| Agriculture spec/source records | QuickStats placeholders only |
| [`AggregationReceipt` contract](../../../../contracts/domains/agriculture/aggregation-receipt.md) and schema | Draft meaning; path and enforcement unresolved |
| [`ReleaseManifest` schema](../../../../schemas/contracts/v1/release/release_manifest.schema.json) | Minimal permissive scaffold; validator absent |
| [`policy/domains/agriculture/README.md`](../../../../policy/domains/agriculture/README.md) | Fail-closed intent; enforcement unknown |
| Workflows and CODEOWNERS | Readiness/TODO signals and review routing; no release authority |
| Directory Rules and drift register | Responsibility separation and unresolved topology |

## Open items

- [ ] Exact artifact, digest, manifest, fields, keys, measures, units, counties, years, geography version, time/revision semantics, missing values, and suppression.
- [ ] Admitted sources, roles, rights, query/snapshot identity, and field-to-evidence mapping.
- [ ] Accepted aggregation profile, typed receipt, candidate schema, validators, fixtures, and executable positive/negative tests.
- [ ] Executable field/operator/small-cell/inference denial policy and public-boundary tests.
- [ ] Accepted release topology, PromotionDecision, ReleaseManifest, correction consumers, rollback target, and drill.
- [ ] Verified independent approval, branch protection, promotion-blocking checks, and reproducible no-network build.

The dossier is ready for manifest review only when these gates close. No workflow, README, test, schema, merge, or generated receipt may substitute for release authority. Until then, the candidate remains `BLOCKED`.

## Rollback

This revision changes documentation only. Before merge, close the pull request or delete the branch. After merge, revert the generated-receipt commit and README commit in reverse order and restore:

```text
0ecabb6ddc5616aa08dfe2101fa2775d4f2d42ca
```

No candidate data, source admission, pipeline activation, evidence, policy, validation, manifest, release, publication, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
