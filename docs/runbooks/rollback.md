# Rollback

Rollback is fail-closed:

1. Stop publication promotion.
2. Keep existing runtime responses explicit (`DENY` or `ABSTAIN` when proof requirements fail).
3. Preserve evidence and correction lineage artifacts for review.
4. Re-run schema and contract validation before re-publish.
