# tests/domains/people-dna-land

Deterministic, no-network People/DNA/Land enforceability tests using repository-owned synthetic fixtures only.

## Executable bounded profiles

The current [`domain-people-dna-land` workflow](../../../.github/workflows/domain-people-dna-land.yml) executes two profiles.

### Consent-safe genealogy overlay

- Test: [`consent/revocation/test_consent_overlay_safety.py`](./consent/revocation/test_consent_overlay_safety.py)
- Fixtures: [`fixtures/domains/people-dna-land/consent_overlay/`](../../../fixtures/domains/people-dna-land/consent_overlay/README.md)
- Validator: [`tools/validators/domains/people-dna-land/validate_consent_overlay.py`](../../../tools/validators/domains/people-dna-land/validate_consent_overlay.py)

This profile checks explicit valid and invalid fixture inventories, deterministic hashes, revocation-manifest membership, active/expired/revoked consent behavior, forbidden identifying and genomic fields, exact-location denial, coarse time/place buckets, stable non-echoing results, bounded file size, and no-network execution.

### Consent-revocation propagation assessment

- Test: [`consent/revocation/test_consent_revocation_propagation_assessment.py`](./consent/revocation/test_consent_revocation_propagation_assessment.py)
- Fixtures: [`fixtures/domains/people-dna-land/consent_revocation_propagation/`](../../../fixtures/domains/people-dna-land/consent_revocation_propagation/README.md)
- Validator: [`tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py`](../../../tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py)

This profile checks active in-scope consent, scope mismatch, revoked, expired, unknown, and evaluation-error states. It requires a closed seven-surface dependency set—`READ`, `ANSWER`, `EXPORT`, `TILE`, `GRAPH`, `INDEX`, and `CACHE`—plus deterministic profile hashing, action/receipt coherence, fail-closed outcomes, and no-network replay. The schema remains `PROPOSED_INACTIVE`; a satisfied result is consent-dimension-only.

## Workflow commands

The workflow invokes these repository-owned entry points:

```bash
python tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/valid/*.json

python tests/domains/people-dna-land/consent/revocation/test_consent_revocation_propagation_assessment.py --verbose
python tools/validators/domains/people-dna-land/validate_consent_revocation_propagation_assessment.py --fixtures
```

Run them only against synthetic repository fixtures. Do not substitute real personal, genealogical, DNA, consent, land, title, assessor, tax, parcel, or protected cultural data.

## Evidence boundary

A passing profile proves only the named deterministic behavior at the tested revision. It does not establish:

- real person identity, kinship, living status, consent validity, legal sufficiency, or DNA support;
- title, ownership, legal boundary, or rights;
- complete revocation, deletion, notification, cache invalidation, or derivative cleanup in deployed systems;
- EvidenceBundle closure, active policy-runtime binding, accountable review, source admission, lifecycle promotion, proof, release, deployment, or publication; or
- that documentation-only, placeholder, or scaffold lanes elsewhere in this directory are executable.

The workflow deliberately reports holds for broader People/DNA/Land semantics, policy runtime, proof production, and release dry-run capability. Preserve those holds until their owning implementations and review evidence exist.

## Related boundaries

- [People/DNA/Land runbook boundary](../../../docs/runbooks/people-dna-land/README.md)
- [Consent review and revocation runbook](../../../docs/runbooks/people-dna-land/CONSENT_RUNBOOK.md)
- [Living-person review runbook](../../../docs/runbooks/people-dna-land/LIVING_PERSON_REVIEW.md)
- [Domain policy boundary](../../../policy/domains/people-dna-land/README.md)
- [Validator boundary](../../../tools/validators/domains/people-dna-land/README.md)
