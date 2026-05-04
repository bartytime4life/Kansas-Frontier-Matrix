# Release Dry Run and Rollback

- Promotion is a governed state transition, not a file move.
- Dry run validates candidate fields, policy, evidence closure, correction path, and rollback target.
- Failed evidence closure returns ABSTAIN or DENY and blocks release readiness.
- CorrectionNotice and RollbackCard remain linked to release candidate IDs for auditability.
