<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-stable-diff-review-handoff
title: Stable Diff Review Handoff Runbook
type: runbook
version: v1.0
status: draft
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; review-support; non-authoritative
owning_root: docs/
responsibility: Operate the deterministic stable-diff review-handoff lane without treating a diff, summary, handoff, or CI check as evidence, policy, authenticated review, promotion, release, or publication authority.
truth_posture: CONFIRMED current branch implementation and local deterministic tests; hosted exact-head checks and human review remain NEEDS VERIFICATION.
related:
  - ../../tools/diff/stable_diff.py
  - ../../tools/ci/render_stable_diff_summary.py
  - ../../tools/ci/build_stable_diff_review_handoff.py
  - ../../tests/diff/test_stable_diff.py
  - ../../tests/diff/test_render_stable_diff_summary.py
  - ../../tests/diff/test_build_stable_diff_review_handoff.py
  - ../../contracts/governance/ReviewRecord.md
  - ../../contracts/governance/review_authority_binding.md
  - ../../docs/doctrine/directory-rules.md
notes:
  - "Completes the bounded reviewer-handoff direction from KFM-P6-PROG-0012, KFM-P6-PROG-0013, KFM-P6-FEAT-0002, and KFM-P6-FEAT-0003 without creating a competing ReviewRecord schema."
  - "The policy-impact projection is declaration-based triage only; policy authority remains in policy/ and PolicyDecision objects."
  - "Stable diff compares top-level JSON keys only; the handoff binds exact artifact bytes so reviewers can detect which artifacts were reviewed without claiming a semantic nested diff."
[/KFM_META_BLOCK_V2] -->

# Stable Diff Review Handoff Runbook

The review-handoff lane turns the existing deterministic `stable-diff` report and its reviewer-facing Markdown projection into one exact-input-bound JSON handoff. It is a review aid, not a review decision.

```text
left/right JSON artifacts
  -> tools/diff/stable_diff.py
  -> stable-diff JSON report
  -> tools/ci/render_stable_diff_summary.py
  -> deterministic Markdown summary
  -> tools/ci/build_stable_diff_review_handoff.py
  -> StableDiffReviewHandoff
  -> separately governed ReviewRecord / ReviewAuthorityBinding
```

> [!IMPORTANT]
> No step in this lane resolves evidence, decides policy, authenticates a reviewer, approves a change, promotes lifecycle state, creates release proof, releases, publishes, or authorizes public use.

## Directory basis

The implementation preserves existing responsibility roots:

| Responsibility | Home | Boundary |
|---|---|---|
| Compute top-level structural change | `tools/diff/` | Comparison only; not policy or review. |
| Render and bind reviewer artifacts | `tools/ci/` | CI/reviewer projection only. |
| Prove deterministic behavior | `tests/diff/` | Test evidence only. |
| Explain operation | `docs/runbooks/` | Human guidance only. |
| Record AI-authoring process memory | `data/receipts/generated/` | Receipt only; not proof or review. |
| Record semantic review | Existing `contracts/governance/ReviewRecord.md` family | Separate downstream object; no competing schema is created here. |

## Context input

The handoff builder accepts one closed context object:

```json
{
  "schema_version": "kfm.stable-diff-review-context.v1",
  "candidate_ref": "kfm://candidate/example/v1",
  "author_ref": "urn:kfm:actor:author-example",
  "review_scope": "contract",
  "evidence_refs": [
    "urn:kfm:evidence:example-1"
  ],
  "basis_refs": [
    "repo:contracts/example.md@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  ],
  "policy_relevant_keys": [
    "policy_state",
    "rights_state"
  ],
  "required_reviewer_roles": [
    "contract_steward",
    "policy_steward"
  ],
  "rollback_target_ref": "urn:kfm:rollback:example-1"
}
```

Arrays must be sorted and unique. Context references are declarations supplied by the caller; the builder binds them but does not resolve or authenticate them.

Accepted review scopes are:

- `ai`
- `contract`
- `cross-cutting`
- `data`
- `docs`
- `domain`
- `evidence`
- `governance`
- `policy`
- `release`
- `schema`
- `sensitivity`
- `source`
- `ui`

## Commands

Compute a nonblocking top-level diff:

```bash
python tools/diff/stable_diff.py \
  --left fixtures/review/left.json \
  --right fixtures/review/right.json \
  --output artifacts/qa/stable-diff.json
```

Render the report:

```bash
python tools/ci/render_stable_diff_summary.py \
  --report artifacts/qa/stable-diff.json \
  --output artifacts/qa/stable-diff.md
```

Build the exact-input-bound handoff:

```bash
python tools/ci/build_stable_diff_review_handoff.py \
  --left fixtures/review/left.json \
  --right fixtures/review/right.json \
  --report artifacts/qa/stable-diff.json \
  --summary artifacts/qa/stable-diff.md \
  --context fixtures/review/context.json \
  --output artifacts/qa/stable-diff-review-handoff.json
```

The five input paths must be normalized repository-relative paths. Absolute paths, `..`, symlinks, malformed JSON, duplicate keys, nonfinite numbers, oversized inputs, stale reports, and tampered summaries fail closed.

## Handoff contents

`StableDiffReviewHandoff` contains:

- exact SHA-256 bindings for left artifact, right artifact, diff report, Markdown summary, and review context;
- the stable-diff top-level added/removed/changed arrays;
- a declaration-based policy-impact projection;
- candidate, author, scope, evidence, basis, reviewer-role, and rollback declarations;
- a self-derived `handoff_id` suitable as a later `ReviewRecord.subject_ref`;
- explicit trust-boundary booleans, all `false`.

The handoff digest is computed from the handoff core before inserting the self-derived `handoff_id`, `handoff_sha256`, and `review_binding.subject_ref`. Verification removes those three fields before recomputing the digest.

## Dispositions and exit codes

| Disposition | Exit | Meaning |
|---|---:|---|
| `NO_CHANGE` | `0` | The stable-diff report says the two JSON objects are the same under the documented top-level comparison rules. |
| `REVIEW_REQUIRED` | `0` | A valid nonblocking top-level change exists and the exact review inputs are bound. Review is still pending. |
| `HOLD` | `1` | The valid stable-diff report is blocking. The handoff records the hold but does not decide how to resolve it. |
| Error payload | `2` | Input, report, summary, context, binding, or output validation failed. No handoff authority is created. |

A `0` exit does not mean approved. It means the deterministic handoff operation completed.

## Policy-impact projection

The builder does not evaluate policy. It intersects changed top-level keys with caller-declared policy-relevant keys and emits one bounded classification:

| Classification | Meaning |
|---|---|
| `NONE` | No top-level keys changed. |
| `UNKNOWN` | Changes exist, but the context declares no policy-relevant keys. |
| `POTENTIAL` | At least one changed top-level key intersects the declared set. |
| `NO_DECLARED_IMPACT` | Changes exist, but none intersects the declared set. This is not a policy clearance. |

Nested changes remain represented only by their changed top-level key because `stable_diff.py` intentionally implements a top-level first slice.

## ReviewRecord binding

A later semantic review can use:

```text
ReviewRecord.subject_ref = StableDiffReviewHandoff.handoff_id
```

The review process should also preserve the handoff SHA-256 and exact input bindings in its basis or receipt references. The handoff does not authenticate the reviewer, prove role assignment, satisfy separation of duties, or convert a ReviewAuthorityBinding into write authority.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/diff \
  --pattern 'test_build_stable_diff_review_handoff.py' \
  --verbose

python -m py_compile \
  tools/ci/build_stable_diff_review_handoff.py \
  tests/diff/test_build_stable_diff_review_handoff.py
```

The focused suite covers deterministic repeatability, exact-file hashes, changed/same/blocking dispositions, policy-impact classifications, stale report rejection, summary tamper rejection, noncanonical context rejection, and error-report refusal.

## Failure handling

- A stable-diff `error` report is not eligible for review handoff.
- A report that no longer matches the supplied artifact pair is rejected.
- A Markdown summary that does not exactly match a fresh rendering of the supplied report is rejected.
- An empty policy-key declaration produces `UNKNOWN`, not a silent no-impact claim.
- A blocking report produces `HOLD` and exit `1`.
- Errors return a finite non-echoing payload; raw artifact bytes and untrusted error messages are not copied into the error result.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive implementation commit. No evidence, policy decision, ReviewRecord, lifecycle promotion, release, published artifact, cache, or external service requires rollback because this lane has no such effects.
