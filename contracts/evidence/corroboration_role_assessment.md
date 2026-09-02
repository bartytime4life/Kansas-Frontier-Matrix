<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/corroboration-role-assessment
title: CorroborationRoleAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Evidence steward · Source steward · Policy steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; evidence; corroboration; source-role; cite-or-abstain
owning_root: contracts/
responsibility: fixture-only deterministic assessment of declared corroboration roles, freshness, independence, and spatiotemporal overlap without fetching evidence, calculating confidence, selecting truth, or authorizing a claim
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../source/source_descriptor.md
  - ./evidence_ref.md
  - ./source_conflict_influence_assessment.md
  - ../../schemas/contracts/v1/evidence/corroboration_role_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/corroboration_role_assessment/cases.json
  - ../../tools/validators/evidence/validate_corroboration_role_assessment.py
  - ../../tests/validators/test_validate_corroboration_role_assessment.py
  - ../../docs/intake/exploratory/corroboration-role-assessment-source-map.md
tags: [kfm, evidence, corroboration, source-role, independence, freshness, overlap, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-037 / KFM-CAND-0109..0111 as a bounded declaration profile."
  - "A valid assessment cannot convert source count into confidence or grant evidence, claim, policy, review, release, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

# CorroborationRoleAssessment Candidate Contract

`CorroborationRoleAssessmentCandidate` records how a bounded set of already
declared evidence references relate to one subject. It keeps source role,
freshness, independence, spatial overlap, temporal overlap, support,
qualification, contradiction, and dependency visible without treating all
sources as interchangeable votes.

## Source-derived gap

Full Atlas triad `KFM-TRIAD-037` rejects raw source-count corroboration. It
calls for qualified relationships among observation, regulatory,
remote-sensing, forecast, simulation, contextual, and derived sources, with
explicit source independence, freshness, overlap, support, contradiction, and
role limitations. Current KFM contracts preserve source roles and pairwise
conflict, but the reviewed base has no reusable object that evaluates this
specific corroboration topology.

## Authority boundary

The object validates declarations only. It does not fetch a source, resolve an
`EvidenceRef`, validate a `SourceDescriptor`, compare payload values, calculate
a probability or confidence score, select truth, authorize a claim, evaluate
policy, approve review, or release or publish an artifact.

Source roles are copied exactly from the current `SourceDescriptor`
vocabulary. A role is never upgraded by appearing in a corroboration packet.
The finite declared relationships are:

```text
SUPPORTS | QUALIFIES | CONTRADICTS | DUPLICATES | CANNOT_EVALUATE
```

## Qualified corroboration

Every unordered source pair is represented exactly once. A pair can contribute
to independent support only when all of these declarations hold:

- `independence` is `INDEPENDENT`;
- spatial and temporal overlap are each `FULL` or `PARTIAL`;
- role compatibility is `COMPATIBLE`; and
- both sources are current and declare `SUPPORTS`.

`SHARED_UPSTREAM`, `DERIVED_FROM`, and `UNKNOWN` independence do not count as
independent support. `NONE` or `UNKNOWN` overlap does not count. Two supporting
rows therefore remain `INSUFFICIENT` when their only relationship is shared or
derived. `source_count_is_confidence` is always false.

The reproduced outcome uses this fail-safe order:

```text
CANNOT_EVALUATE > CONTRADICTED > SUPPORTED_WITH_QUALIFICATION > SUPPORTED > INSUFFICIENT
```

Role collapse, prohibited role combinations, stale or unknown freshness, or
unknown pair compatibility force `CANNOT_EVALUATE`. A current contradiction is
preserved as `CONTRADICTED`. Qualification or partial overlap keeps successful
independent support qualified rather than silently promoting it.

## Deterministic invariants

- Source rows are sorted and unique by `source_id`.
- Descriptor references are unique and every evidence reference is explicit.
- Freshness state reproduces `fresh_until` relative to `assessed_at`.
- Stale or unknown-freshness sources use `CANNOT_EVALUATE` with the matching
  fixed reason.
- Relationship reason codes match the declared relationship exactly.
- Pair rows form the complete unordered pair matrix and are sorted by
  `pair_id`.
- Pair reason codes reproduce independence, overlap, and role compatibility.
- Summary inventories, independent-support pairs, and outcome reproduce source
  and pair rows.
- No numeric confidence or threshold field exists.
- Every governance or operational effect flag is false.

`spec_hash` is RFC 8785 JCS plus SHA-256 over the object excluding only
`assessment_id` and `spec_hash`. The assessment ID is derived from the first 24
digest characters.

## Validator status

`PASS` means shape, identity, ordering, freshness, relationship, complete pair
topology, independence, overlap, role compatibility, outcome, and
non-authority checks passed. It does not mean a real-world claim is true or
authorized. `DENY` identifies a declaration defect; `ERROR` identifies unsafe
input.

## Directory Rules basis

Meaning belongs in `contracts/evidence/`; machine shape in
`schemas/contracts/v1/evidence/`; synthetic cases in
`fixtures/contracts/v1/evidence/`; executable validation in
`tools/validators/evidence/`; conformance tests in `tests/validators/`;
read-only orchestration in `.github/workflows/`; source adaptation in
`docs/intake/exploratory/`; and authoring accountability in
`data/receipts/generated/`.

No source registry, source-role vocabulary, evidence store, confidence model,
policy bundle, claim authority, release object, proof authority, or publication
path is created.

## Rollback

Before merge, close the draft PR and retire its branch. After an authorized
merge, revert the additive packet. It is fixture-only and has no runtime
consumer, so no evidence correction, release withdrawal, cache invalidation,
or public correction is required.
