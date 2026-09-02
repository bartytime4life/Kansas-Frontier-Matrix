<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/inspectable-claim-carrier-assessment/v1
title: InspectableClaimCarrierAssessment
type: semantic-contract
version: 1.0.0
status: proposed-inactive
owning_root: contracts/
responsibility: Test whether a downstream carrier preserves the minimum inspectable-claim trust bindings without becoming authority.
truth_posture: fixture-only; a PASS is not evidence, policy, release, publication, or public-use authority
[/KFM_META_BLOCK_V2] -->

# `InspectableClaimCarrierAssessment`

> **Status:** `PROPOSED_INACTIVE` · **Execution:** fixture-only/no-network · **Authority:** none

## Purpose

KFM doctrine treats maps, tiles, graph projections, dashboards, exports, stories, 3D scenes, and AI answers as downstream carriers rather than sovereign truth. This profile makes that boundary testable: a carrier-shaped declaration must retain explicit references to the claim, resolved EvidenceBundle, policy decision, release manifest, correction path, rollback path, and visible negative states.

The profile does not dereference or authenticate those references. It does not create a claim or evidence, approve policy, promote lifecycle state, release, deploy, publish, or authorize public use.

## Core invariants

- every carrier binds one `claim_ref`, `evidence_bundle_ref`, `policy_decision_ref`, `release_manifest_ref`, `correction_ref`, and `rollback_ref`;
- `negative_states` is sorted, unique, and contains at least `ABSTAIN`, `DENY`, `ERROR`, and `STALE`;
- public-facing declarations additionally expose `CORRECTED` and `WITHDRAWN`;
- every effect flag is fixed false;
- `assessment_id` is deterministic SHA-256 over the canonical identity subject excluding `assessment_id`.

A valid declaration receives `PASS`. Missing trust bindings or hidden negative-state behavior receives `DENY`. Malformed structure or identity drift receives `ERROR`.

## Directory Rules basis

Accepted ADR-0029 assigns semantic meaning to `contracts/`, machine shape to `schemas/contracts/v1/`, synthetic cases to `fixtures/`, executable validation to `tools/validators/` and `tests/`, CI orchestration to `.github/workflows/`, and source adaptation to `docs/intake/exploratory/`. No new root or parallel authority is created.

## Validation

```bash
python -m unittest tests.validators.governance.test_inspectable_claim_carrier_assessment -v
python tools/validators/governance/validate_inspectable_claim_carrier_assessment.py --fixtures
```

## Rollback

Revert the additive feature commit. No source, lifecycle state, release, deployment, public artifact, or repository setting is changed by this profile.
