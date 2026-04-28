<!-- [KFM_META_BLOCK_V2]
doc_id: kfm.runbook.publication.v1
title: Publication Runbook
type: runbook
version: v1
status: active
owners: kfm-maintainers
created: 2026-04-28
updated: 2026-04-28
policy_label: evidence_first
related:
  - docs/runbooks/README.md
  - docs/runbooks/correction.md
  - docs/runbooks/rollback.md
[/KFM_META_BLOCK_V2] -->

# Publication Runbook

Use this runbook when promoting a candidate change to a public or shared KFM surface.

## Trigger

- A change is approved and ready to move from review to released/public state.

## Preconditions

- Contracts/schemas touched by the change are versioned and reviewed.
- Required tests are green in CI.
- Evidence artifacts (release notes, receipts, or manifests) are prepared.

## Procedure

1. Confirm branch is up to date and review is approved.
2. Run local verification for the touched surface.
3. Verify release artifacts are reproducible.
4. Merge through the governed path (no direct pushes to protected branches).
5. Publish artifacts and notes.
6. Post-release, run smoke checks and record outcomes.

## Validation checklist

- [ ] CI is green for the merge commit.
- [ ] Release note references exact commit SHA.
- [ ] Public-facing docs/routes resolve and return expected envelopes.
- [ ] Any stale-derived-state warning is absent (or explicitly documented).

## Failure handling

If any validation check fails after promotion:

- Freeze further promotion.
- Open an incident/correction ticket.
- Follow [Correction Runbook](./correction.md) or [Rollback Runbook](./rollback.md).

## Outputs

- Release notes entry
- Published artifact references
- Post-release verification log
