# tests/domains/people-dna-land

Deterministic People/DNA/Land enforceability tests.

## Executable bounded profile

The repository currently executes one synthetic, no-network profile:

- `consent/revocation/test_consent_overlay_safety.py`
- fixtures: `fixtures/domains/people-dna-land/consent_overlay/`
- validator:
  `tools/validators/domains/people-dna-land/validate_consent_overlay.py`

The profile checks active/expired/revoked consent, revocation-manifest
membership, deterministic hashes, evidence references, identifying kit-field
denial, raw-genomic denial, exact-location denial, coarse time/place buckets,
and explicit `not_released` governance.

A passing test does not establish real person identity, kinship, consent
validity, DNA support, title, rights, EvidenceBundle closure, policy approval,
release, or publication. Broader People/DNA/Land tests remain documentation or
placeholder lanes until deliberately graduated.
