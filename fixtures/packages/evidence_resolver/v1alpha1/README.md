# Evidence resolver candidate profile v1alpha1

Deterministic, public-safe fixtures for
`kfm/evidence-ref-bundle-candidate/v1alpha1`.

The profile checks only explicit shape, bundle identity, EvidenceRef
membership, caller-supplied current-head context, caller-supplied canonical
policy-outcome projection, caller-supplied correction context, exact
EvidenceRef-to-history subject binding, and bitemporal replay of a validated
`VerificationStateHistory`. `RESOLVED` requires an eligible `ACTIVE` replay;
corrected, superseded, revoked, unknown, mismatched, or invalid history fails
closed. It does not mean evidence truth,
claim-scope equivalence, rights clearance, policy evaluation, human review,
release approval, a public `ANSWER`, or publication authority.

Each fixture has exactly two top-level members:

- `request` — the explicit candidate input;
- `expected` — one internal status and the exact sorted issue-code set.

All identifiers and content are synthetic. No fixture contains a real source
row, location, person, credential, endpoint, or production evidence.

The inventory contains two positive fixtures (initially active and active
after re-verification) plus exact negatives for all prior resolver outcomes and
for corrected, superseded, revoked, unknown, temporally inconsistent, and
subject-mismatched verification history.
