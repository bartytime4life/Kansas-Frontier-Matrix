<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/friday-natural-systems-pulse
title: FridayNaturalSystemsPulseCandidate Contract
type: semantic-contract; material-change aggregation; fixture-first
version: v0.1.0
status: proposed; inactive; no-network; no-automation
owners: OWNER_TBD — Data steward · Domain stewards · Validation steward · Release steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; data; material-change; pulse; non-authoritative
related:
  - ./material_change_assessment.md
  - ../../schemas/contracts/v1/data/friday_natural_systems_pulse.schema.json
  - ../../fixtures/contracts/v1/data/friday_natural_systems_pulse/
  - ../../tools/validators/validate_friday_natural_systems_pulse.py
  - ../../tests/validators/test_validate_friday_natural_systems_pulse.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, natural-systems, material-change, weekly-pulse, fixture-only, no-publish]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# FridayNaturalSystemsPulseCandidate

> A `FridayNaturalSystemsPulseCandidate` deterministically summarizes already-validated `MaterialChangeAssessment` records for the five natural-systems scopes `atmosphere`, `fauna_habitat`, `hydrology`, `soil`, and `vegetation`. It is review process memory only. It is not a watcher, source fetch, rebuild instruction, pull-request instruction, policy decision, release, or publication object.

## Source-derived need

*New Ideas 3-19-26* proposes a Friday natural-systems bundle that:

- covers soil, air, vegetation, hydrology, and fauna/habitat;
- emits only when at least one tracked dataset has a material change;
- preserves deterministic `spec_hash` identity;
- carries machine-readable and human-reviewable change information; and
- keeps policy and provenance visible.

The source packet also sketches `NONE`, `REBUILD`, `REVIEW`, and `PR` actions. This v1 fixture profile deliberately admits only `NONE` and `REVIEW`. `REBUILD` and `PR` remain vocabulary values so attempted automation fails with the stable finding `EXECUTION_ACTION_NOT_ADMITTED`.

## Directory Rules basis

ADR-0029 makes Directory Rules v2 the effective placement authority. The object is a shared data-change summary, so its semantic meaning belongs in `contracts/data/`. Its machine shape, examples, validator, tests, workflow, and authoring provenance remain in their separate existing responsibility roots.

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/data/` |
| Machine shape | `schemas/contracts/v1/data/` |
| Synthetic inputs | `fixtures/contracts/v1/data/` |
| Executable validation | `tools/validators/` |
| Enforceability | `tests/validators/` |
| Read-only CI | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root or parallel domain, source, policy, evidence, proof, receipt, release, or publication authority is created.

## Bounded context

The pulse consumes five domain-scoped assessments but does not own their materiality rules.

```text
domain-specific comparison
    -> MaterialChangeAssessment
    -> FridayNaturalSystemsPulseCandidate
    -> steward review candidate only
```

Domain adapters remain responsible for deciding whether a source-specific change is `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, or `ERROR`. The pulse may only:

1. bind the exact assessment bytes and declared assessment `spec_hash`;
2. verify complete, canonical five-domain coverage;
3. derive counts and one finite pulse outcome; and
4. recommend `NONE` or `REVIEW`.

## Weekly window

The fixture profile uses one UTC window:

- `window.start`: Monday at `00:00:00Z`;
- `window.end`: Friday at `23:59:59Z`;
- `window.assessed_at`: no earlier than the window end and no later than 24 hours afterward.

This records cadence semantics without creating a scheduled workflow.

## Finite pulse outcomes

Precedence is fail closed:

```text
ERROR > HOLD > PULSE_CANDIDATE > NO_EVENT
```

| Assessment set | Pulse outcome | `emit_candidate` | Meaning |
|---|---|---:|---|
| Any assessment is `ERROR` | `ERROR` | false | Pulse construction is not dependable. |
| No errors and any assessment is `HOLD` | `HOLD` | false | One or more domain assessments require resolution. |
| No errors/holds and any assessment is `PROMOTION_CANDIDATE` | `PULSE_CANDIDATE` | true | The complete bundle is eligible for human review only. |
| All five assessments are `NON_EVENT` | `NO_EVENT` | false | Operational implementations should emit no review bundle. |

A `PULSE_CANDIDATE` is not a release candidate and not publication authority.

## Deterministic identity

For this fixture profile:

1. remove top-level `pulse_id` and `spec_hash`;
2. serialize the remaining object as sorted, compact UTF-8 JSON with finite numbers;
3. compute SHA-256;
4. set `spec_hash = "sha256:<hex>"`;
5. set `pulse_id = "natural-systems-pulse:<window-end-date>:<first-24-hex>"`.

Each entry also binds:

- the repository-relative assessment path;
- the assessment's exact-byte SHA-256;
- the assessment ID;
- the assessment governance `spec_hash`; and
- the assessment outcome.

## Governance boundary

Every v1 candidate fixes all execution and authority fields:

- fixture only;
- no source activation;
- no network access;
- no rebuild execution;
- no issue or pull-request creation;
- no authority creation;
- no policy evaluation;
- no authenticated review;
- no promotion authorization;
- release state `HOLD`;
- no publication; and
- no public use.

The hosted workflow is intentionally not scheduled. A later operational PR would need admitted source inputs, current rights and sensitivity review, a governed scheduler, separately authorized issue/PR behavior, runtime receipts, policy, accountable review, and release/correction/rollback integration.

## Rollback

Before merge, close the pull request and abandon its branch. After an authorized merge, revert the additive contract/schema/fixtures/validator/tests/workflow/receipt slice. No source, scheduled job, external service, lifecycle data, issue, pull request, rebuild, release, deployment, or public artifact requires cleanup.

[Back to top](#top)
