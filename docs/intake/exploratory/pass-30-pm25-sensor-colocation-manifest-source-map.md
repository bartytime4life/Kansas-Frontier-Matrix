<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-30-pm25-sensor-colocation-manifest-source-map
title: Pass 30 PM2.5 Sensor Co-location Manifest Source Adaptation
type: source-adaptation-map
version: v1.0.0
status: proposed; exploratory; review-pending
created: 2026-08-09
updated: 2026-08-09
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
- **CONFIRMED:** Exact-card, title, field-set, PR, and branch searches found no implementation at assayed base `4e4eb979caae21922af2217247ade970bd70cf82`.
- **CONFIRMED:** The existing PM sensor trust profile references calibration and a reference anchor but does not define this study-design manifest.
- **PROPOSED:** The introduced contract, schema, fixtures, validator, tests, workflow, and receipt are inactive review candidates.

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

## Open verification

Scientific minimum duration, completeness thresholds, seasonal representativeness, split design, reference-site suitability, source rights, and live evidence resolution remain **NEEDS VERIFICATION**. This packet does not select or encode those decisions.
