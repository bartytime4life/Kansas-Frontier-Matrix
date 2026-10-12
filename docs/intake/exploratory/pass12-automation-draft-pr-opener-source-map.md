# Pass 12 automation draft-PR opener source map

**Status:** PROPOSED adaptation record · no activation · no publication authority

## Source idea

Pass 12 calls for PR-first automation that can propose repository changes with receipts and deterministic policy outcomes while retaining no merge or publication power. The repository already contains the `AutomationPrProposal` guard that binds an exact `main` base SHA, an `automation/` head branch, candidate paths under `data/work/automation/`, artifact digests, a receipt reference, policy outcome, and all-false terminal authority flags.

## Repository fit

Current workflow doctrine places GitHub event/permission/orchestration logic under `.github/workflows/`, reusable validation under `tools/validators/`, executable proof under `tests/validators/`, semantic meaning under `contracts/`, and operator procedure under `docs/runbooks/`.

The smallest safe implementation after the proposal guard is therefore **not** a general repository writer. It is a trusted-default-branch pull-request opener that:

1. consumes a structurally write-eligible `AutomationPrProposal`;
2. fetches an already-existing candidate branch as data only;
3. verifies exact base, merge-base, live diff, path, blob mode, and SHA-256 binding;
4. rechecks remote base/head refs immediately before mutation;
5. creates at most one draft pull request; and
6. verifies the resulting pull request remains bound to the validated base/head and draft state.

## Authority deliberately omitted

The opener receives no repository-content write permission. It cannot create or update the candidate branch, merge, enable auto-merge, approve review, release, deploy, promote, publish, change repository settings, or grant public-use authority.

## Residual risk

GitHub pull-request creation is branch-name based rather than an atomic expected-head-SHA compare-and-swap. The implementation bounds that race with an immediate pre-create remote-ref check and an immediate post-create head/base/draft verification. A detected mismatch closes only the newly created draft pull request fail-safe. This residual race remains review-visible rather than being hidden behind a stronger claim.

## Follow-on boundary

Branch-producing automation remains a separate, higher-authority problem. It should not be added merely to make this opener end-to-end. Any future branch writer must receive its own contract, least-privilege threat model, deterministic candidate assembly, receipt binding, and rollback review.
