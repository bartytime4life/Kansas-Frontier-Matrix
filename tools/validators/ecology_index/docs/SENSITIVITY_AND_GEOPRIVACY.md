# Sensitivity and Geoprivacy Notes

This validator does not currently classify geoprivacy sensitivity directly, but it protects prerequisites needed for downstream policy checks.

## What this validator guarantees

- Row structure is schema-valid.
- Domain and join-key requirements are satisfied.
- Evidence references are present.

## What this validator does not guarantee

- Restricted-coordinate redaction.
- Public-safe geometry generalization policy.
- Embargo windows or steward-review disposition.
- Release authorization.

## Required downstream checks

Before publication, downstream policy gates should verify:

1. Coordinate precision policy by sensitivity class.
2. Redaction/generalization receipts for restricted records.
3. Rights and redistribution posture.
4. Release-state and correction/rollback readiness.
