## Purpose
Human-governed review artifacts and promotion-preflight eligibility only.

## Lifecycle placement
RELEASE_CANDIDATE -> REVIEW -> PROMOTION_PREFLIGHT (not PUBLISHED).

## Human review decision model
Captures reviewer identity, scope refs, decision, and blocked actions.

## Sensitivity review model
Scans refs for coordinate/geometry leakage and keeps publication blocked.

## Rights attestation model
Attests USDA public-domain posture and citation requirement.

## Review audit ledger model
Hashes and records review artifacts for auditability.

## Promotion-preflight model
Computes eligibility for a future promotion request only.

## Why preflight is not promotion
This layer does not promote.

## Why preflight is not publication
This layer does not publish.

## Policy gates
Rego denies publication claims, promotion claims, missing hashes, and leaked geometry/coordinates.

## Optional reviewer-gated workflow
Manual dispatch workflow produces artifacts only.

## CI and no-network posture
No USDA fetch, no network required.

## What is intentionally not implemented
No publication, promotion, PR open, PR merge, county geometry generation, public tile generation.

## Future work
A future explicit promotion layer with separate human approval.
