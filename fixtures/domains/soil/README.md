<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-domains-soil-readme
title: Soil Domain Fixtures README
type: fixture-lane-readme
version: v0.2
status: draft; bounded-public-safe-fixture-profile-confirmed
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - QA steward
created: NEEDS VERIFICATION - greenfield stub existed before v0.2
updated: 2026-08-02
policy_label: public-safe; synthetic; tests; soil; no-network; non-authoritative
owning_root: fixtures/
responsibility: reusable synthetic Soil inputs and expected fail-closed outcomes
truth_posture: fixture validation is not Soil truth, source admission, policy approval, release, or publication
related:
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../tests/domains/soil/README.md
  - ../../../tests/domains/soil/test_soil_smoke.py
  - ../../../tools/validators/domains/soil/README.md
  - ../../../tools/validators/domains/soil/validate_public_safe_fixture.py
  - ../../../.github/workflows/domain-soil.yml
notes:
  - "v0.2 replaces the greenfield stub with the boundary contract for the accepted synthetic public-safe fixture profile."
  - "The profile is intentionally fixture-only, not released, and ineligible for promotion."
[/KFM_META_BLOCK_V2] -->

# Soil domain fixtures

`fixtures/domains/soil/` owns reusable synthetic inputs and expected outcomes
for bounded Soil tests. It does not own Soil meaning, schemas, policy, source
records, lifecycle data, evidence, proofs, receipts, release decisions, or
published carriers.

## Accepted bounded profile

The executable profile under `valid/` and `invalid/` exercises only the current
public-safe synthetic candidate contract:

- explicit support type;
- non-empty synthetic source and evidence references;
- generalized county spatial support with precise-location aliases rejected;
- ordered depth intervals and bounded volumetric-water-content units;
- fixture-only rights, sensitivity, review, and rollback state; and
- explicit non-release and non-promotion posture.

Positive and negative JSON files are small, deterministic, no-network, and
contain no real soil observations, farm or owner data, exact locations, source
payloads, credentials, or live URLs. Invalid cases have exact expected-finding
sidecars so an unrelated rejection cannot satisfy fixture polarity.

## Current direct children

```text
fixtures/domains/soil/
├── README.md              # This fixture-lane boundary
├── golden/                # Reserved compatibility scaffold; no accepted golden output
├── invalid/               # Synthetic fail-closed cases and expected findings
├── smap/                  # Existing scaffold; consumer and maturity NEED VERIFICATION
├── soil_moisture/         # Existing scaffold; consumer and maturity NEED VERIFICATION
├── spec_hash/             # Existing scaffold; consumer and maturity NEED VERIFICATION
├── ssurgo_mapunit/        # Existing scaffold; consumer and maturity NEED VERIFICATION
└── valid/                 # Synthetic accepted public-safe candidate
```

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_smoke.py --verbose
```

A pass proves only the declared fixture profile and deterministic finding
behavior. It does not resolve the open Soil support-type taxonomy, validate
MUKEY/COKEY/CHKEY lineage, admit a source, close an EvidenceBundle, apply policy,
construct proof, approve release, or publish data.

## Rollback

Before merge, close the draft pull request or abandon its feature branch. After
any separately authorized merge, use a focused revert of the validator,
fixtures, tests, workflow documentation, and generated receipt; do not rewrite
shared history or alter lifecycle data.
