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

Each candidate fixture under `valid/` or `invalid/` has exactly two top-level
members:

- `request` — the explicit candidate input;
- `expected` — one internal status and the exact sorted issue-code set.

All identifiers and content are synthetic. No fixture contains a real source
row, location, person, credential, endpoint, or production evidence.

The inventory contains two positive fixtures (initially active and active
after re-verification) plus exact negatives for all prior resolver outcomes and
for corrected, superseded, revoked, unknown, per-event temporal inconsistency,
effective-order inversion, and subject-mismatched verification history.

`repository/hydrology_bundle_manifest.json` is separate adapter configuration,
not a candidate fixture. Its one closed entry binds stable ID `hb1` to the sole
allowlisted synthetic Hydrology payload and the packet-local complete-object
digest profile. Candidate-suite discovery is restricted to `valid/` and
`invalid/`; it cannot interpret this manifest as a resolver request. The
manifest is not an evidence registry, catalog, proof store, policy record,
source registry, release record, or production authority.
