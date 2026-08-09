<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/outcome-projection-parity
title: OutcomeProjectionParity Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Contract steward · Policy steward · Runtime steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; common; finite-outcome; parity; cite-or-abstain
owning_root: contracts/
responsibility: fixture-only declaration of cross-layer finite-outcome, visibility, reason, and support lineage without executing or authorizing any policy, release, runtime, API, UI, export, cache, or publication action
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../runtime/runtime_response_envelope.md
  - ../governance/gate_outcome_mapping.md
  - ../../schemas/contracts/v1/common/outcome_projection_parity.schema.json
  - ../../fixtures/contracts/v1/common/outcome_projection_parity/cases.json
  - ../../tools/validators/validate_outcome_projection_parity.py
  - ../../tests/validators/test_validate_outcome_projection_parity.py
  - ../../docs/intake/exploratory/outcome-projection-parity-source-map.md
tags: [kfm, common, outcome, projection, parity, reason-lineage, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-066 / KFM-CAND-0196..0198 as one bounded declaration profile."
  - "Parity evidence cannot authorize or upgrade an outcome, surface, claim, release, or publication state."
[/KFM_META_BLOCK_V2] -->

# OutcomeProjectionParity Candidate Contract

OutcomeProjectionParityCandidate records how one synthetic finite outcome is represented across the policy, release, runtime, API, UI, export, and cache layers. It makes native naming, shared semantic meaning, visibility changes, reason-code mappings, omitted fields, and support lineage inspectable.

## Source-derived gap

Full Atlas triad KFM-TRIAD-066 proposes a versioned matrix of allowed transformations, permitted degradations, and prohibited upgrades across consequential layers. The Drive sources New Ideas 4-14-26 and New Ideas 4-15-26 provide lane-specific finite-outcome and runtime-parity examples. Current KFM contracts define finite outcomes and several individual projections, but the reviewed base has no reusable object that proves parity across the complete seven-layer chain.

## Authority boundary

This profile validates declarations only. It does not run policy, assemble or approve a release, execute a runtime, call an API, render a UI, create an export, mutate a cache, resolve evidence, or authorize public use.

Every layer preserves two distinct values:

- native_outcome records the layer-local label;
- semantic_outcome uses the closed ANSWER, ABSTAIN, DENY, or ERROR vocabulary for comparison.

A native rename is not a semantic change. A semantic difference is accepted only when the pinned profile permits the pair, a degradation rule is referenced, a new reason is declared, and prior support is not silently dropped.

## Versioned projection matrix

The v1 fixture profile uses this layer order:

~~~text
POLICY -> RELEASE -> RUNTIME -> API -> UI -> EXPORT -> CACHE
~~~

The profile permits semantic preservation and bounded fail-safe degradation. It never permits ABSTAIN, DENY, or ERROR to become ANSWER. Visibility may move from FULL toward REDACTED, STALE, or UNAVAILABLE, but never in the opposite direction.

STALE or UNAVAILABLE material cannot remain ANSWER. REDACTED material may remain ANSWER only when the redaction is declared, reason-bearing, profile-bound, and support-preserving.

## Reason and support lineage

Each step maps every input reason exactly once:

- PRESERVED requires the same input and output code;
- TRANSLATED records a declared rename;
- added_reason_codes records new degradation context;
- output reasons must equal mapped reasons plus added reasons;
- support_refs are append-only across a projection chain.

An ANSWER without support is an empty success and fails closed. omitted_fields is disclosure only; it cannot excuse reason or support loss.

## Reproduced report

The validator reproduces one of three report states:

- PARITY_CONFIRMED — semantic outcome and visibility are preserved;
- AUTHORIZED_DEGRADATION — the profile permits a declared, reason-bearing degradation;
- PARITY_FAILURE — a prohibited upgrade, reason loss, support loss, empty success, continuity defect, or other parity violation exists.

The report always sets trusted_surface_allowed to false and separate_policy_review_required to true. A passing fixture proves only that the declaration matches the closed profile.

## Deterministic invariants

- Layer order and all six adjacent transitions are exact.
- Step input is byte-equivalent as JSON data to the preceding output.
- Outcome and visibility matrices are closed and cannot be weakened by the candidate.
- Reason and support arrays are sorted and unique.
- Every input reason is preserved or explicitly translated.
- No support reference disappears.
- Every degradation is rule-bound and adds a reason.
- Report terminal state, failure indexes, and finding codes are reproduced.
- spec_hash is RFC 8785 JCS plus SHA-256 over the object excluding only assessment_id and spec_hash.
- assessment_id is derived from the first 24 digest characters.
- Every governance or operational effect flag is false.

## Validator outcomes

PASS means the declaration, identity, chain, matrix, lineage, report, and non-authority flags agree. DENY identifies a declaration or parity defect. ERROR identifies unsafe JSON input. PASS does not mean any real layer exists, ran, agreed, or is trusted.

## Directory Rules basis

The object is a shared semantic contract spanning several responsibility lanes, so meaning belongs in contracts/common/ under DIR-SCOPELANE-004. Its machine shape belongs in schemas/contracts/v1/common/ under DIR-AUTHROOT-001. Synthetic cases, repository validation, tests, read-only CI, source mapping, and authoring accountability remain in their existing fixture, tool, test, platform, docs, and receipt roots.

No policy source, release decision, runtime adapter, API route, UI component, export, cache, evidence object, or publication carrier is created.

## Rollback

Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet. It has no runtime consumer or live state, so rollback requires no release withdrawal, cache invalidation, evidence correction, or public notice.
