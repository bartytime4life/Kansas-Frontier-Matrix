<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-contracts-v1-telemetry-map-build-sustainability-readme
title: Map Build Sustainability Telemetry Fixtures
type: README
version: v1.0.0
status: proposed-inactive; synthetic; fixture-only; no-network
owners: OWNER_TBD — Observability steward · Map artifact steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: fixtures/
policy_label: internal; synthetic; telemetry; sustainability
responsibility: Provide reusable synthetic positive abstention and denial cases for the inactive map-build sustainability telemetry profile.
truth_posture: CONFIRMED synthetic fixture polarity / PROPOSED profile / NEEDS VERIFICATION steward adoption and hosted CI
related:
  - ../../../../../contracts/telemetry/map_build_sustainability.md
  - ../../../../../schemas/contracts/v1/telemetry/map_build_sustainability.schema.json
  - ../../../../../tools/validators/telemetry/validate_map_build_sustainability.py
  - ../../../../../tests/validators/telemetry/test_map_build_sustainability.py
[/KFM_META_BLOCK_V2] -->

# Map Build Sustainability Telemetry Fixtures

`cases.json` contains only synthetic build references, digests, method references, factors, and numeric values. It covers `PASS`, `ABSTAIN`, and `DENY` without representing a live build, provider, factor source, release, environmental observation, or public artifact.

The fixture replay requires exact outcome and finding-code equality. Candidate values are never copied into findings.

```bash
python tools/validators/telemetry/validate_map_build_sustainability.py --fixtures
```
