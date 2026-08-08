<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-diff-review-handoff
title: Diff review handoff renderer
type: deterministic-qa-renderer-contract
version: v0.1.0
status: draft; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Review steward · Policy steward · QA steward · CI steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; diff; review; policy-impact; no-approval-authority
related:
  - ./README.md
  - ./stable_diff.py
  - ./render_review_handoff.py
  - ../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../tests/diff/test_render_review_handoff.py
tags: [kfm, diff, renderer, policy-impact, review-handoff, deterministic, fixture-first]
[/KFM_META_BLOCK_V2] -->

# Diff review handoff renderer

`render_review_handoff.py` realizes the Pass 6 diff-review family as one
deterministic derived-QA renderer with three sections:

1. bundle summary;
2. policy-impact summary; and
3. review handoff bound to exact input digests.

It consumes the current `stable_diff.py` report. It does not compute a second
diff, display raw changed values, create a competing ReviewRecord schema, or
record an approval.

## Inputs

```bash
python tools/diff/render_review_handoff.py \
  --diff-report /tmp/stable-diff.json \
  --context /tmp/review-context.json \
  --policy-map /tmp/field-policy-map.json \
  --format json \
  --output /tmp/review-handoff.json
```

The context supplies digest-bound left/right artifact refs, a review scope,
required canonical reviewer roles, and source-card references. The optional
policy map relates changed top-level fields to policy families.

## Output and review binding

The output contains only field names, governed refs, finite states, and exact
input digests. `review_handoff.subject_ref` is content-derived from:

- the three input digests;
- digest-bound artifact refs;
- review scope and required roles;
- bundle summary; and
- policy-impact summary.

A later human `ReviewRecord` may use that value as `subject_ref`. The current
canonical schema remains
`schemas/contracts/v1/governance/review_record.schema.json`, whose decisions
are `approve`, `reject`, and `request_changes`. The source atlas term `deny` is
not introduced as a competing review enum.

## Finite states and exits

| State | Meaning |
|---|---|
| `NO_CHANGE` | The stable diff reports no changed fields. |
| `READY_FOR_REVIEW` | All changed fields have an explicit policy mapping. |
| `HOLD_UNMAPPED_POLICY_IMPACT` | One or more changed fields lack a mapping and require review. |
| `ERROR` | A bounded input, contract, or output failure occurred. |

Exit `0` means a handoff was rendered. Exit `1` is available only when
`--fail-on-unmapped-impact` makes the hold blocking. Exit `2` is an input or
system error.

## Safety boundary

- Inputs must be bounded regular UTF-8 JSON files; symlinks, duplicate keys,
  non-finite numbers, malformed reports, and unbound artifact refs fail closed.
- Output never includes changed field values.
- Markdown is generated from the same normalized object as JSON.
- The tool does not resolve EvidenceBundle support, decide policy, authenticate
  reviewer identity, approve, promote, release, deploy, or publish.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After
an authorized merge, revert the renderer/fixture/test/workflow packet. No
review decision, lifecycle data, release, cache, deployment, or public artifact
requires cleanup.
