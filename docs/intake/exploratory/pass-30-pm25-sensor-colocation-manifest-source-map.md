<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-30-pm25-sensor-colocation-manifest-source-map
title: Pass 30 PM2.5 Sensor Co-location Manifest Source Adaptation
type: source-adaptation-map
version: v1.1.0
status: proposed; implementation-reconciled; fixture-only; review-pending
created: 2026-08-09
updated: 2026-08-25
policy_label: internal; intake; atmosphere; source-map; no-network
source_card: KFM-P30-PROG-0003
related:
  - ../../../contracts/domains/atmosphere/pm25_sensor_colocation_manifest.md
  - ../../../contracts/domains/atmosphere/pm_sensor_trust_profile.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, intake, pass-30, atmosphere, pm25, colocation]
[/KFM_META_BLOCK_V2] -->

# Pass 30 PM2.5 Sensor Co-location Manifest Source Adaptation

## Evidence basis

- **CONFIRMED:** Consolidated-atlas card `KFM-P30-PROG-0003` is active and unchanged through Pass 32 with spec hash `sha256:7bc2ca941e28838e5e44f436ad3eaed4cdf2da041e36c506604e1a4ccb771285`.
- **CONFIRMED:** The normalized source statement requires sensor IDs, reference site, start/end, data completeness, seasonal coverage, and validation split.
- **CONFIRMED:** Exact-card, title, field-set, PR, and branch searches found no pre-existing implementation at assayed base `4e4eb979caae21922af2217247ade970bd70cf82`; that historical result does not describe current repository state.
- **CONFIRMED:** The existing PM sensor trust profile references calibration and a reference anchor but does not define this study-design manifest.
- **CONFIRMED:** The introduced contract, schema, fixtures, validator, tests, and workflow are present on `main@75e47a5785d02fdc82e4a0f3f6f7d7dab2ac4f05` and form an executable synthetic validation packet.
- **PROPOSED_INACTIVE:** The packet remains fixture-only and review-pending; its generated authoring receipt does not grant policy, scientific, source-admission, release, or publication authority.

## Adaptation map

| Source requirement | Repository adaptation | Deliberate limit |
|---|---|---|
| Sensor IDs | Canonical synthetic `sensor_ids` plus exact coverage/split membership | No live station or registry lookup |
| Reference site | Fixture reference, source descriptor, and evidence bindings | No reference-grade or regulatory equivalence |
| Start/end | UTC-aware bounded `window` | No source access or clock authority |
| Data completeness | Reproduced expected/observed fractions per sensor | No sufficiency threshold or scientific fitness claim |
| Seasonal coverage | Finite meteorological-season declarations | No transferability inference |
| Validation split | Bounded partitions with non-overlap and validation-presence checks | No model training, execution, or approval |

## Placement decision

Directory Rules assigns domain meaning to `contracts/domains/atmosphere/`, machine shape to `schemas/contracts/v1/domains/atmosphere/`, synthetic evidence to `fixtures/`, validation to `tools/validators/` and `tests/`, orchestration to `.github/workflows/`, and authoring provenance to `data/receipts/generated/`. No new authority root is introduced.

## Current executable packet

The card is **IMPLEMENTED only as a `PROPOSED_INACTIVE` / `FIXTURE_ONLY` profile** through:

- semantic contract: [`contracts/domains/atmosphere/pm25_sensor_colocation_manifest.md`](../../../contracts/domains/atmosphere/pm25_sensor_colocation_manifest.md);
- machine shape: [`schemas/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest.schema.json`](../../../schemas/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest.schema.json);
- synthetic cases: [`fixtures/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest/cases.json`](../../../fixtures/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest/cases.json);
- deterministic validator: [`tools/validators/domains/atmosphere/validate_pm25_sensor_colocation_manifest.py`](../../../tools/validators/domains/atmosphere/validate_pm25_sensor_colocation_manifest.py);
- focused proof: [`tests/validators/domains/atmosphere/test_pm25_sensor_colocation_manifest.py`](../../../tests/validators/domains/atmosphere/test_pm25_sensor_colocation_manifest.py); and
- read-only workflow: [`.github/workflows/pm25-sensor-colocation-manifest.yml`](../../../.github/workflows/pm25-sensor-colocation-manifest.yml).

This closure proves only deterministic shape, internal arithmetic, canonical ordering, evidence-reference closure, and finite synthetic outcomes. It does not establish scientific sufficiency, source rights, reference-grade equivalence, live evidence validity, policy approval, promotion, release, deployment, or publication.

## Open verification

Scientific minimum duration, completeness thresholds, seasonal representativeness, split design, reference-site suitability, source rights, and live evidence resolution remain **NEEDS VERIFICATION**. This packet does not select or encode those decisions.

## Rollback

Revert this source-map reconciliation independently. The executable packet, generated authoring receipt, source state, evidence state, policy state, lifecycle state, release state, and public state are unchanged.
