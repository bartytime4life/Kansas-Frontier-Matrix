<!-- [KFM_META_BLOCK_V2]
doc_id: kfm.runbook.correction.v1
title: Correction Runbook
type: runbook
version: v1
status: active
owners: kfm-maintainers
created: 2026-04-28
updated: 2026-04-28
policy_label: fail_closed
related:
  - docs/runbooks/README.md
  - docs/runbooks/publication.md
  - docs/runbooks/rollback.md
[/KFM_META_BLOCK_V2] -->

# Correction Runbook

Use this runbook to correct a published error without obscuring lineage.

## Trigger

- A published claim, payload, or artifact is found to be inaccurate, incomplete, or unsafe.

## Severity levels

- **SEV-1:** Trust/safety impact; immediate containment required.
- **SEV-2:** Material error; correction required before next normal release.
- **SEV-3:** Minor issue; correction can ship in next scheduled release.

## Procedure

1. Triage and assign severity.
2. Contain impact (hide endpoint, add banner, or freeze publication lane).
3. Prepare correction artifact with clear "what changed" and "why".
4. Link superseded output to the corrected output.
5. Request review and merge the correction.
6. Publish correction notice and update downstream docs.

## Validation checklist

- [ ] Correction notice includes affected versions/date window.
- [ ] Superseded artifact is still discoverable for audit.
- [ ] Corrected artifact passes contracts/schemas/tests.
- [ ] Public-facing messaging reflects corrected state.

## Roll-forward vs rollback

- Prefer roll-forward when a safe correction is available quickly.
- Use rollback when correction cannot be validated quickly enough.
