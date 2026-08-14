# Fauna–Habitat public-safe assignment validator

This directory owns the **pair-specific executable validator** for a synthetic Fauna-to-Habitat assignment candidate. It composes the generic `tools/joins/join_candidates.py` assessment and adds only the Fauna–Habitat constraints defined in `contracts/cross_domain/fauna_habitat/public_safe_assignment_profile.md`.

## Boundary

The validator is fixture-only, no-network, and non-publishing. It consumes no coordinate or geometry bytes. A successful `ALLOW` remains a `CANDIDATE_RELATION`; it does not establish Fauna occurrence truth, Habitat truth, a canonical join, EvidenceBundle support, policy permission, review approval, release, or publication.

## Directory Rules basis

Accepted ADR-0029 adopts Directory Governance Standard v2. Its cross-domain seam rule places shared validators at `tools/validators/cross_domain/<seam_id>/`. The `fauna_habitat` segment matches the existing test lane and does not create a root or lead-domain authority.

## Run

```bash
python tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py --fixtures
python -m pytest tests/cross_domain/fauna_habitat/test_public_safe_assignment.py -q --strict-config --strict-markers
```

The path-scoped workflow also runs the generic join fixture/test suite so pair-specific work cannot silently weaken the shared assessment.

## Finite behavior

- public-safe generalized synthetic endpoints may yield `ALLOW / JOIN_CANDIDATE`;
- missing evidence, role conflict, or restricted generalized context yields `ABSTAIN`;
- exact restricted/prohibited geometry yields `DENY`;
- dependency failure yields `ERROR`;
- wrong pair profile, domain order, fixture provenance, or public-candidate precision fails pair validation.

## Rollback

Revert the bounded commit that introduces this directory and its paired contract, fixtures, tests, workflow, receipt, and test README update. No data, source, proof, release, or publication state is mutated.
