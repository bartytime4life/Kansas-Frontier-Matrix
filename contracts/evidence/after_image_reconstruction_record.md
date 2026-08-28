<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/after-image-reconstruction-record
title: AfterImageReconstructionRecord Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Temporal steward · Correction steward · Release steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; evidence; temporal; tracking-log; after-image; reconstruction
responsibility: Define a fixture-only, reference-only after-image record for report-time reconstruction without storing state payloads, writing history, applying corrections, or granting evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED attached Pass 18 card, visual review, Drive metadata, and bounded repository gap; PROPOSED inactive reconstruction record; UNKNOWN lifecycle adoption and retention policy; NEEDS VERIFICATION evidence, temporal, privacy, correction, release, and validation review plus hosted exact-head CI"
related:
  - ./as_of_snapshot_disclosure.md
  - ../correction/correction_impact_assessment.md
  - ../release/rollback_card.md
  - ../../schemas/contracts/v1/evidence/after_image_reconstruction_record.schema.json
  - ../../fixtures/contracts/v1/evidence/after_image_reconstruction_record/cases.json
  - ../../tools/validators/evidence/validate_after_image_reconstruction_record.py
  - ../../tests/validators/evidence/test_validate_after_image_reconstruction_record.py
  - ../../docs/intake/exploratory/pass-18-after-image-reconstruction-record-source-map.md
[/KFM_META_BLOCK_V2] -->

# AfterImageReconstructionRecord Candidate

`AfterImageReconstructionRecordCandidate` is an additive, fixture-only
declaration that binds one tracking-log transition to an externally stored or
withheld after-image posture. It implements the smallest reviewable portion of
supplied Pass 18 card `KFM-P18-INV-145`: preserve enough state lineage to
explain why reports differed and which recorded state was available for an
audit, correction, disputed release, or rollback analysis.

The record contains references and digests only. It never embeds the after-
image payload.

## After-image modes

| Mode | Required declaration | Outcome posture |
|---|---|---|
| `EXTERNAL_REFERENCE` | External state reference and digest plus schema reference and digest. | May pass when all other controls close. |
| `MINIMIZED_REFERENCE` | The same bindings plus `minimization_state: APPLIED`. | May pass for the retained, minimized representation only. |
| `DIGEST_ONLY` | Digest without a retrievable state or schema reference. | `ABSTAIN`; identity can be compared but state cannot be reconstructed. |
| `WITHHELD` | No state or schema binding and an opaque withholding-reason reference. | `ABSTAIN`; no access or release authority is inferred. |

A `PASS` does not prove that a referenced after-image exists, is complete, is
accurate, or may be disclosed. It proves only that a synthetic declaration is
locally coherent.

## Reconstruction scope

Use cases are explicit and support-bound:

- `AUDIT` requires a run-receipt reference;
- `CORRECTION` requires a correction-notice reference;
- `DISPUTED_RELEASE` requires a release-manifest reference and an
  `AsOfSnapshotDisclosureCandidate` reference; and
- `ROLLBACK_ANALYSIS` requires a rollback reference.

These references are opaque. The validator does not dereference or
authenticate them, reconstruct a report, compare state payloads, or decide
which state is true.

## Retention and minimization

Every candidate declares a retention class, policy binding, minimization
posture, and sensitivity posture. `TRANSIENT` and `BOUNDED` retention require a
future UTC expiry. `ARCHIVAL` and `WITHHELD` forbid an expiry in this profile.
An unresolved policy, minimization, or sensitivity posture yields `ABSTAIN`.

The record does not establish retention policy. It makes the source card's
privacy, cost, and minimization tension visible so that full after-image
retention is never treated as an automatic requirement.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Tracking-log, transition, after-image, reconstruction support, retention, review, timestamps, and content hash are locally coherent. |
| `ABSTAIN` | The after-image is digest-only or withheld, or tracking-log, retention, minimization, sensitivity, or review posture is unresolved. |
| `DENY` | A binding, use-case support, retention, review, ordering, timestamp, or content-hash declaration is contradictory. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

## Boundary

The candidate does not:

- store or reveal an after-image, source row, report, geometry, credential, or
  protected state;
- write a tracking log, event, receipt, correction, snapshot, or rollback;
- execute temporal reconstruction or compare two reports;
- decide retention, privacy, sensitivity, evidence, policy, or review;
- mutate lifecycle state or authorize promotion, release, deployment,
  publication, or public use.

## Directory Rules basis

The object is reference-only reconstruction evidence, so semantic meaning
belongs under `contracts/evidence/`. Shape, fixtures, validator, tests,
read-only CI, source reconciliation, and authoring provenance remain within
their established responsibility roots. No temporal database, payload store,
tracking-log store, policy source, correction lane, release path, or new root is
created.

## Validation and rollback

```bash
python -m unittest tests.validators.evidence.test_validate_after_image_reconstruction_record -v
python tools/validators/evidence/validate_after_image_reconstruction_record.py --fixtures
```

Rollback is one additive commit revert. The inactive profile has no stored
after-images, temporal rows, corrections, lifecycle writes, release,
deployment, cache, publication, or public-state side effect.
