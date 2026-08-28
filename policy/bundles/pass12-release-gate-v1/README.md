# Pass 12 release gate v1

**Status:** PROPOSED_INACTIVE · fixture-first · fail-closed · no publication authority

This directory defines the packaging profile for the Pass 12 release-gate proof slice. The executable Rego source remains under the existing `policy/rego/` responsibility lane; this bundle directory records the exact source and validation surface to package later if KFM adopts an executable OPA bundle format.

## Purpose

Pass 12 calls for a small policy bundle that proves four release conditions deterministically: release scope, evidence completeness, sensitivity review, and required attestation closure. The implementation also requires human review, a release-manifest reference, a correction path, and a rollback path so a green policy result cannot stand in for governed publication.

## Inputs

The profile evaluates a declared candidate containing:

- `release_scope`: `public` or `semi_public`;
- `spec_hash`: lowercase `sha256:<64 hex>` identity;
- non-empty `evidence_refs`;
- `sensitivity.reviewed` and `sensitivity.class`;
- `attestation.required`, `attestation.verified`, and `attestation.ref` when required;
- `review.state` plus `review.review_ref`;
- `release_manifest_ref`;
- `correction_ref`;
- `rollback_ref`.

## Finite result

The Rego package exposes:

- `allow`: boolean, default `false`;
- `deny`: deterministic set of stable reason codes;
- `decision`: `{profile, allow, deny_reasons}` with sorted reasons.

This profile is intentionally not normalized into `PolicyDecision`; that integration belongs to the existing policy runtime/binding contract and remains a separate follow-on. It therefore cannot create `ANSWER`, release approval, promotion, publication, or deployment state.

## Source and fixtures

- policy source: `policy/rego/release_gate_v1.rego`
- policy tests: `policy/rego/release_gate_v1_test.rego`
- positive fixture: `fixtures/policy/release_gate_v1/allow_public.json`
- negative fixtures: missing evidence, sensitivity review, and required attestation
- hosted validation: `.github/workflows/pass12-release-policy-v1.yml`

The workflow installs checksum-pinned OPA 1.19.0, checks formatting, runs native Rego tests, evaluates fixture polarity, and asserts stable deny reasons.

## Directory Rules basis

`policy/` owns admissibility and deny-by-default evaluation. `policy/rego/` is already an executable Rego lane in the current repository, while `policy/bundles/` is the existing policy-bundle packaging boundary. Fixtures remain under `fixtures/`, and CI remains under `.github/workflows/`. No new authority root is introduced.

## Non-effects

Passing this profile does not resolve evidence, verify cryptography, authenticate a reviewer, assemble a release, promote lifecycle state, deploy, publish, or authorize public use. Those remain separate governed transitions.

## Rollback

Before merge, close the pull request and delete the feature branch. After merge, revert the additive files through a reviewed pull request. No data migration or external cleanup is required.
