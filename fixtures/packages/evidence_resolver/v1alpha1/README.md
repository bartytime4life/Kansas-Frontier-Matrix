# Evidence resolver candidate profile v1alpha1

Deterministic, public-safe fixtures for
`kfm/evidence-ref-bundle-candidate/v1alpha1`.

The profile checks only explicit shape, bundle identity, EvidenceRef
membership, caller-supplied current-head context, caller-supplied canonical
policy-outcome projection, and caller-supplied correction context. `RESOLVED`
means that this
bounded candidate check found no listed issue. It does not mean evidence truth,
claim-scope equivalence, rights clearance, policy evaluation, human review,
release approval, a public `ANSWER`, or publication authority.

Each fixture has exactly two top-level members:

- `request` — the explicit candidate input;
- `expected` — one internal status and the exact sorted issue-code set.

All identifiers and content are synthetic. No fixture contains a real source
row, location, person, credential, endpoint, or production evidence.
