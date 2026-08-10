# PublicParticipationSubmissionAssessmentCandidate

Status: **PROPOSED / INACTIVE / FIXTURE-ONLY**
Profile: `kfm.governance.public-participation-submission-assessment.v1`

## Purpose

This additive assessment carrier keeps a time-bounded `CommentWindow` distinct
from a received `Submission`. It records only synthetic, local evidence about
window timing, receipt posture, privacy posture, and publication posture.

A valid assessment proves that the declared fields are internally consistent.
It does **not** prove that a submission was accepted, reviewed, endorsed, acted
upon, released, published, or used in a decision.

## Normative boundary

- `CommentWindow` means only a bounded period during which an authority may
  accept public input.
- `Submission` means only a received comment, testimony, or document reference.
- A receipt timestamp is not acceptance or review.
- Review is not endorsement, action, recommendation, or decision.
- `RELEASE_REFERENCE_ONLY` may point to an already governed release; this
  profile cannot create that release or expose submission content.
- The payload stores only references and digests. It must not contain submitter
  names, addresses, contact details, free text, testimony, or attachments.
- Every effect flag is permanently `false` in v1.

## Deterministic identity

The validator removes `assessment_id` and `spec_hash`, canonicalizes the
remaining JSON with the repository hashing package, computes SHA-256, and sets:

```text
spec_hash    = sha256:<64 lowercase hexadecimal characters>
assessment_id = public-participation-submission-assessment:<first 24 hex>
```

## Outcome semantics

`PASS` means schema, timing, posture, reference canonicalization, deterministic
identity, and authority non-effects agree. `DENY` means a bounded semantic or
schema contradiction. `ERROR` is reserved for operational failures such as
invalid JSON, duplicate keys, non-finite numbers, unavailable hashing, or an
identity mismatch.

## Activation posture

The proposal has no runtime wiring, intake endpoint, database migration,
calendar client, publication path, or UI. Activation requires an accepted ADR,
explicit owner, privacy review, migration plan, release controls, and human
approval outside this change.
