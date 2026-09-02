<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-common-source-native-quality-translation
title: SourceNativeQualityTranslation Fixtures
type: fixture-readme
version: v0.1.0
status: draft; PROPOSED; synthetic; no-network
owners: OWNER_TBD — Fixture steward · Contracts steward · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; fixtures; synthetic; quality-translation; non-authoritative
related:
  - ../../../../../contracts/common/source_native_quality_translation.md
  - ../../../../../schemas/contracts/v1/common/source_native_quality_translation.schema.json
  - ../../../../../tools/validators/validate_source_native_quality_translation.py
  - ../../../../../tests/validators/test_validate_source_native_quality_translation.py
[/KFM_META_BLOCK_V2] -->

# SourceNativeQualityTranslation fixtures

This directory contains synthetic, non-joinable fixtures for the proposed shared source-native quality translation and health/validity separation profile.

## Inventory

### Valid records

| File | Behavior proved |
|---|---|
| `valid/valid_mapped_online_valid.json` | Exact native-code mapping, online health, and independently valid observation. |
| `valid/valid_unmapped_degraded_not_assessed.json` | Unmapped native code is preserved; normalized quality remains unknown; validity is not fabricated. |
| `valid/valid_offline_historical_valid.json` | Current outage affects availability but does not invalidate a historical reading. |
| `valid/valid_ambiguous_degraded_suspect.json` | Ambiguous mapping retains semantic loss, requires review, and supports a suspect assessment. |
| `valid/valid_not_applicable_health_only.json` | Health-only record does not invent a quality or observation assessment. |

### Invalid records

The manifest at `invalid/expected_findings_manifest.json` binds each negative file to its exact reviewed finding-code set.

Negative cases cover:

- unmapped-to-accepted collapse;
- health vocabulary used as validity vocabulary;
- health directly deciding validity;
- ambiguous mapping without review;
- hidden semantic loss;
- inconsistent outage availability;
- missing observation support;
- noncanonical references;
- deterministic hash mismatch;
- governance overclaim;
- timing inversion; and
- incomplete native-vocabulary identity.

Every `invalid_*.json` file includes `schema_negative_canary`. The closed schema rejects that field while the dedicated validator still exercises the intended semantic finding. This preserves the repository-wide convention that files under `fixtures/contracts/v1/**/invalid/invalid_*.json` are JSON-Schema invalid.

## Boundary

These fixtures do not contain real station identifiers, real provider quality codes, current source terms, live endpoints, people, sensitive geometry, or operational status. They do not admit a source, establish evidence, evaluate policy, release data, or publish anything.

## Commands

```bash
python tools/validators/validate_source_native_quality_translation.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_source_native_quality_translation.py' \
  --verbose
```
