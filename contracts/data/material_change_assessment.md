<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/material-change-assessment
title: MaterialChangeAssessment Contract
type: semantic-contract; change-classification; non-event-receipt
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Data steward · Domain steward · Contract steward · Validation steward · Release steward
created: 2026-08-04
updated: 2026-08-04
policy_label: public; data; materiality; process-memory; non-publisher
related:
  - ./README.md
  - ../../docs/intake/exploratory/new-ideas-4-16-source-map.md
  - ../../tools/diff/README.md
  - ../../schemas/contracts/v1/data/material_change_assessment.schema.json
  - ../../fixtures/contracts/v1/data/material_change_assessment/
  - ../../tools/validators/validate_material_change_assessment.py
  - ../../tests/validators/test_validate_material_change_assessment.py
tags: [kfm, material-change, semantic-change, non-event, receipt, deterministic, fixture-first]
notes:
  - "This object classifies one candidate-versus-baseline comparison. It does not define domain thresholds or authorize promotion."
  - "A NON_EVENT assessment is process memory explaining why a byte change did not become a release candidate."
[/KFM_META_BLOCK_V2] -->

# MaterialChangeAssessment

> `MaterialChangeAssessment` records whether a candidate differs from a declared baseline at the byte, semantic, and materiality levels. It gives watchers and pipelines one deterministic handoff for `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, or `ERROR` without allowing a hash change or threshold result to become policy, proof, review, release, or publication authority.

## Why this object exists

The New Ideas 4-16-26 packet separates content hashing from materiality and says non-material changes should stop while still being recorded. The repository already has stable structural diff tooling and many domain watcher notes, but no shared executable object was found that preserves this three-step distinction:

```text
byte identity changed?
  -> semantic meaning changed?
    -> declared materiality profile triggered?
      -> NON_EVENT | PROMOTION_CANDIDATE | HOLD | ERROR
```

A `NON_EVENT` assessment is the bounded non-event receipt. It preserves process memory and replay inputs; it does not write `PUBLISHED`, clear a real-world event, or erase the candidate.

## Responsibility boundary

| This contract owns | It does not own |
|---|---|
| Meaning of byte, semantic, and material change | Hash implementation or canonicalization algorithms |
| Finite assessment outcomes and reason codes | Domain threshold selection |
| Baseline/candidate/profile bindings | Source admission, rights, or sensitivity decisions |
| Criterion result recording | Policy evaluation or review approval |
| Non-event process-memory semantics | Promotion, release, publication, or rollback authority |

Companion responsibilities remain separate:

- hash/canonicalization code belongs in the accepted hashing or comparison implementation lane;
- domain materiality profiles belong with the domain's governed pipeline/specification responsibility;
- policy remains in `policy/`;
- promotion and release remain in release-governance objects;
- actual assessment instances belong in the appropriate receipt/process-memory lane, not in `contracts/`.

## Required states

| `change_class` | Required outcome | Meaning |
|---|---|---|
| `UNCHANGED` | `NON_EVENT` | Baseline and candidate byte digests are identical. |
| `BYTE_ONLY` | `NON_EVENT` | Bytes differ but the declared semantic comparison finds no meaning change. |
| `SEMANTIC_NON_MATERIAL` | `NON_EVENT` | Meaning changed, but no required materiality criterion triggered. |
| `MATERIAL` | `PROMOTION_CANDIDATE` | Meaning changed and the declared profile's required criteria passed. This is only a candidate input to later gates. |
| `UNDETERMINED` | `HOLD` | Baseline, profile, metric, or evidence is insufficient. |
| `ERROR` | `ERROR` | A trustworthy assessment could not be produced. |

## Profile and criterion rules

The assessment references, but does not author, a materiality profile. The profile binding includes a stable profile ID, semantic version, SHA-256 `spec_hash`, canonicalization profile, and digest algorithm. Criteria record only reproducible inputs and results:

- stable `criterion_id` and metric name;
- whether the criterion is required;
- `PASS`, `FAIL`, `UNKNOWN`, or `ERROR`;
- observed value, threshold, unit, and evidence references.

A `MATERIAL` assessment requires at least one criterion and every required criterion must be `PASS`. A `SEMANTIC_NON_MATERIAL` assessment requires at least one failed criterion. `HOLD` and `ERROR` remain explicit rather than guessing.

## Semantic invariants

The no-network validator enforces:

1. SHA-256 values are not all-zero placeholders;
2. `byte_changed` agrees with baseline/candidate digest equality;
3. the finite `change_class`, `material`, and `outcome` combination is coherent;
4. byte-only and semantic states agree with `semantic_changed`;
5. material candidates have passing required criteria;
6. non-material semantic changes have at least one failed criterion;
7. hold/error records use bounded reason families and nullable materiality;
8. baseline time does not follow candidate time, and candidate time does not follow assessment time;
9. lineage cannot point to the current assessment;
10. stable arrays and criterion IDs are unique and sorted;
11. governance fields cannot claim authority, policy evaluation, public use, promotion, or release.

## Trust and lifecycle boundary

A passing assessment proves only schema shape and local consistency. It does **not** prove:

- that the baseline or candidate exists or is admissible;
- that the referenced profile is accepted or scientifically appropriate;
- that evidence references resolve;
- that rights, sensitivity, source role, or policy passed;
- that review occurred;
- that a watcher may publish;
- that a promotion candidate is release-ready.

The allowed forward path is:

```text
MaterialChangeAssessment(PROMOTION_CANDIDATE)
  -> evidence / policy / review / promotion gates
  -> release decision and rollback target
```

`NON_EVENT`, `HOLD`, and `ERROR` stop that path while retaining the assessment for replay and correction.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_material_change_assessment.py' \
  --verbose

python tools/validators/validate_material_change_assessment.py --fixtures
```

The validator performs no network access and diagnostics expose codes and JSON pointers, not candidate values.

## Rollback

Before merge, close the draft pull request and delete the feature branch. After merge, revert this dependency-closed contract/schema/validator/fixture/test slice. If downstream records begin using the stable object identity, preserve them and use correction or supersession rather than deleting process memory.
