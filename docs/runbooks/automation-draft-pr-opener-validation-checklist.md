# Automation draft-PR opener validation checklist

Use this checklist when reviewing the proposed `automation-draft-pr-opener` workflow. A checked item is review evidence only; it is not release or publication authority.

- [ ] The privileged workflow is triggered only by `repository_dispatch` type `automation-pr-proposal-v1`.
- [ ] The privileged job has exactly `contents: read` and `pull-requests: write` permissions.
- [ ] Checkout credentials are not persisted and candidate branch code is never executed.
- [ ] The structural `AutomationPrProposal` validator must return `PASS` and `write_eligible=true` before the head ref is fetched.
- [ ] Current `main` equals the proposal base SHA and the head merge-base equals that exact base.
- [ ] The complete live diff equals the declared candidate path set and contains only additions/modifications below `data/work/automation/`.
- [ ] Candidate Git objects are ordinary `100644` blobs and every blob hash matches the declared SHA-256 value.
- [ ] Remote base/head SHAs are re-read immediately before pull-request creation.
- [ ] At most one open PR may exist for the head/base pair.
- [ ] Creation always uses draft state.
- [ ] The created PR is re-read and must match the expected head SHA, base SHA, and `draft=true` state.
- [ ] A post-create binding mismatch closes only the newly created draft PR fail-safe.
- [ ] No branch/content write, merge, auto-merge, review approval, release, deployment, promotion, publication, repository-setting, secret, package, or OIDC capability is present.
- [ ] The read-only conformance workflow passes on the exact proposed head.
- [ ] Repository-wide failures are classified as introduced, inherited, or merge-context drift before any corrective patch is added.

## Rollback

Before merge, close the implementation pull request and abandon the feature branch. After an authorized merge, revert the bounded opener packet through a reviewed pull request. Do not delete or rewrite an existing candidate branch as part of opener rollback.
