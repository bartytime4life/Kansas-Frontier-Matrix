<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures/domains/people-dna-land/consent-overlay
title: People/DNA/Land Consent-Safe Genealogy Overlay Fixtures
type: fixture-readme
version: v0.1.0
status: proposed; synthetic; fixture-only; not-released
owners: OWNER_TBD - People/DNA/Land steward; consent steward; privacy steward; validation steward
created: 2026-08-03
updated: 2026-08-03
policy_label: restricted-review; synthetic-fixture-only; no-network; no-real-person; no-raw-dna; no-public-release
owning_root: fixtures/
related:
  - ../../../../contracts/domains/people-dna-land/consented_genealogy_overlay.md
  - ../../../../schemas/contracts/v1/domains/people-dna-land/consented_genealogy_overlay.schema.json
  - ../../../../schemas/contracts/v1/domains/people-dna-land/genealogy_overlay_revocation_manifest.schema.json
  - ../../../../tools/validators/domains/people-dna-land/validate_consent_overlay.py
  - ../../../../tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py
tags: [kfm, fixtures, people-dna-land, consent, revocation, genealogy, privacy, no-network]
[/KFM_META_BLOCK_V2] -->

# Consent-safe genealogy overlay fixtures

Frozen, synthetic fixtures for the bounded
`ConsentedGenealogyOverlayCandidate` profile.

> [!IMPORTANT]
> These files contain no real people, real kits, raw DNA, exact locations,
> parcels, addresses, production consent records, release state, or public
> artifacts. County FIPS `99999` is a non-real fixture sentinel.

## Layout

```text
consent_overlay/
├── README.md
├── revocation_manifest.json
├── valid/
│   ├── historical_documentary_context.json
│   └── restricted_active_consent.json
└── invalid/
    ├── expired_consent.json
    ├── high_score_weak_evidence.json
    ├── identifying_kit_field.json
    ├── living_person_without_active_consent.json
    ├── missing_evidence.json
    ├── non_synthetic_county.json
    ├── precise_location.json
    ├── public_release_claim.json
    ├── raw_genomic_material.json
    ├── recent_time_overprecision.json
    ├── revocation_root_mismatch.json
    ├── revoked_consent.json
    ├── spec_hash_mismatch.json
    └── *.expected_error.txt
```

## Positive cases

| Fixture | Bounded proof |
|---|---|
| `restricted_active_consent.json` | Synthetic DNA-derived summary with active, scoped fixture consent, matching revocation root, coarse geography/time, evidence refs, and explicit non-release state. |
| `historical_documentary_context.json` | Synthetic documentary context for a deceased-or-historical posture with no kit hash and `consent.status=not_required`. |

## Negative cases

| Fixture | Primary guardrail |
|---|---|
| `living_person_without_active_consent.json` | Living-person and DNA-derived material require active consent. |
| `revoked_consent.json` | Revoked consent fails closed. |
| `expired_consent.json` | Evaluation outside the consent interval fails closed. |
| `identifying_kit_field.json` | Cleartext/vendor kit fields are denied. |
| `raw_genomic_material.json` | Raw genotype or genomic material is denied. |
| `precise_location.json` | Exact coordinate material is denied. |
| `public_release_claim.json` | Public/released/promotion-eligible state is denied by the fixture profile. |
| `spec_hash_mismatch.json` | Deterministic profile hash must reproduce. |
| `missing_evidence.json` | Candidate and event evidence references are required. |
| `high_score_weak_evidence.json` | High-confidence summaries need at least two evidence refs. |
| `recent_time_overprecision.json` | Recent-era time buckets cannot be over-precise. |
| `non_synthetic_county.json` | Real county identifiers are not allowed in this fixture family. |
| `revocation_root_mismatch.json` | Candidate and revocation manifest must bind to the same root. |

Each invalid JSON file has a same-name `.expected_error.txt` sidecar with exact
sorted `CODE<TAB>JSON_PATH` findings.

## Run

```bash
python tests/domains/people-dna-land/consent/revocation/test_consent_overlay_safety.py

python tools/validators/domains/people-dna-land/validate_consent_overlay.py \
  --revocation-manifest \
  fixtures/domains/people-dna-land/consent_overlay/revocation_manifest.json \
  fixtures/domains/people-dna-land/consent_overlay/valid/*.json
```

Known-invalid fixtures must return a non-zero exit code.

## Boundary

Passing fixtures do not prove real consent, identity, kinship, DNA support,
source rights, policy approval, release readiness, or publication safety. The
profile has no network access and performs no lifecycle or external side effect.
