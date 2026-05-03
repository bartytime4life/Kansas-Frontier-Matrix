# Hazards Rollback and Correction

Corrections and rollbacks preserve lineage; they do not erase history.

## Correction triggers

- Incorrect role assignment.
- Incorrect time basis or freshness fields.
- Rights/sensitivity misclassification.
- Broken evidence reference resolution.
- Misleading UI wording (especially emergency posture).

## Correction workflow

1. Open correction record with reason code.
2. Link affected release/object ids.
3. Produce replacement artifact(s).
4. Re-run validation/policy/promotion checks.
5. Publish correction notice and lineage links.

## Rollback workflow

1. Identify rollback target and scope.
2. Declare rollback reason and impact summary.
3. Re-point active release pointer to prior safe release.
4. Emit rollback receipt.
5. Ensure public surfaces reference corrected lineage.

## Invariants

- No destructive deletes of released evidence lineage.
- Supersession chains stay traversable.
- Public history remains auditable.
