<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/source-conflict-influence-assessment
title: SourceConflictInfluenceAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Evidence steward · Source steward · Policy steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; evidence; source-conflict; influence; cite-or-abstain
owning_root: contracts/
responsibility: fixture-only deterministic declaration of finite cross-source relationships and influence roles without resolving evidence, choosing truth, authorizing claims, or granting policy, release, publication, or public-use authority
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../source/source_descriptor.md
  - ./evidence_ref.md
  - ./claim_field_binding.md
  - ../../schemas/contracts/v1/evidence/source_conflict_influence_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/source_conflict_influence_assessment/cases.json
  - ../../tools/validators/evidence/validate_source_conflict_influence_assessment.py
  - ../../tests/validators/test_validate_source_conflict_influence_assessment.py
  - ../../docs/intake/exploratory/source-conflict-influence-assessment-source-map.md
tags: [kfm, evidence, source-role, conflict, influence, order-invariance, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-065 / KFM-CAND-0193..0195 as a bounded declaration profile."
  - "A coherent relationship or influence ledger cannot choose truth, resolve evidence, or authorize a claim."
[/KFM_META_BLOCK_V2] -->

# SourceConflictInfluenceAssessment Candidate Contract

`SourceConflictInfluenceAssessmentCandidate` records how a bounded set of source declarations were compared under one versioned profile, which sources were eligible, which were excluded or revoked, and how much influence each was declared to have. It preserves conflict instead of silently selecting a winner.

## Source-derived gap

Full Atlas triad `KFM-TRIAD-065` proposes source-conflict topology and influence accounting: finite source relationships, versioned comparison axes, explicit exclusions, source-role preservation, and order invariance. Current KFM contracts preserve source roles and field-level conflicts, but the reviewed base has no reusable cross-source comparison/influence object with this bounded responsibility.

## Authority boundary

This profile validates declarations only. It does not fetch a source, resolve an `EvidenceRef`, authenticate a `SourceDescriptor`, compare source payloads, calculate confidence, decide which source is true, evaluate policy, or authorize a claim.

Source roles are copied exactly from the current `SourceDescriptor` vocabulary. Influence roles are separate:

```text
DOMINANT | CONTRIBUTING | CONTEXT_ONLY | EXCLUDED | NON_INFLUENTIAL
```

`DOMINANT` is not a source authority upgrade. It means only that the declared downstream result gave that eligible input the greatest influence under the referenced comparison profile.

## Finite source relationships

Every unordered source pair is represented exactly once with `left_source_id < right_source_id`:

```text
CONSISTENT | DIVERGENT | CONFLICTING | INSUFFICIENT | INAPPLICABLE | REVOKED_EVIDENCE
```

The overall relationship is reproduced with this fail-safe precedence:

```text
REVOKED_EVIDENCE > CONFLICTING > DIVERGENT > INSUFFICIENT > CONSISTENT > INAPPLICABLE
```

An excluded or inapplicable source cannot influence a result. Revoked evidence must be excluded and every pair containing it must remain `REVOKED_EVIDENCE`.

## Deterministic invariants

- Source rows are sorted and unique by `source_id`.
- Comparison-profile axes are sorted, unique, nonempty, and declared order-invariant.
- Pair rows form the complete unordered pair matrix and are sorted by `pair_id`.
- Pair axes are a nonempty canonical subset of profile axes.
- Eligibility, evidence-reference presence, influence role, and reason code agree.
- At most one source is `DOMINANT`.
- Relationship reason codes and ineligible-pair relationships are exact.
- Summary role inventories and overall relationship reproduce the source and pair rows.
- `claim_resolution_allowed` is false and `separate_policy_gate_required` is true.
- Every governance or operational effect flag is false.

`spec_hash` is RFC 8785 JCS plus SHA-256 over the object excluding only `assessment_id` and `spec_hash`. The assessment ID is derived from the first 24 digest characters.

## Validator status

`PASS` means shape, identity, ordering, completeness, relationship, influence, and non-authority checks passed. It does not mean the compared sources agree or support a claim. `DENY` identifies a declaration defect; `ERROR` identifies unsafe input.

## Directory Rules basis

The object’s primary responsibility is evidence comparison and influence disclosure, so meaning belongs in `contracts/evidence/`; machine shape in `schemas/contracts/v1/evidence/`; synthetic cases in `fixtures/contracts/v1/evidence/`; executable validation in `tools/validators/evidence/`; tests in `tests/validators/`; read-only orchestration in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and authoring accountability in `data/receipts/generated/`.

No source registry, source-role vocabulary, evidence store, policy bundle, claim authority, release object, proof authority, or publication path is created.

## Rollback

Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet. It is fixture-only and has no runtime consumer, so no source action, evidence correction, release withdrawal, cache invalidation, or public correction is required.
