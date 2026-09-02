<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/county-year-panel
title: CountyYearPanel Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD - Frontier Matrix steward; Data steward; Evidence steward; Contract steward; Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; data; county-year; aggregate; no-network
owning_root: contracts/
responsibility: Define a synthetic county-year composition over pinned definitions and observation references without loading values, classifying frontier status, or changing release state.
truth_posture: CONFIRMED source and repository gap / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ../../schemas/contracts/v1/data/county_year_panel.schema.json
  - ../../fixtures/contracts/v1/data/county_year_panel/cases.json
  - ../../tools/validators/data/validate_county_year_panel.py
  - ../../tests/data/test_county_year_panel.py
  - ../../docs/intake/exploratory/pass-20-county-year-panel-source-map.md
  - ../common/geography_version.md
  - ../evidence/frontier_definition.md
tags: [kfm, data, frontier-matrix, county-year, aggregate, fixture-only]
notes:
  - "Implements the synthetic county-year panel next step named by Pass 20 KFM-IDX-APP-008 after GeographyVersion and FrontierDefinition."
  - "A coherent panel is only a review candidate or hold; it is not a classification, evidence resolution, policy decision, release record, or publication authority."
[/KFM_META_BLOCK_V2] -->

# CountyYearPanel Candidate

> A deterministic, aggregate-only composition declaring which versioned observation records would support one synthetic county-year panel.

## Purpose

Pass 20 recommends definitions and synthetic fixtures before data harvesting or public analytical claims. `GeographyVersion` and `FrontierDefinition` now provide the two required definition seams. This profile adds only the composition that connects those declarations to population, economic, agriculture, and access observation references.

A `CountyYearPanel` records:

- one synthetic county identity digest and calendar year;
- one digest-bound `GeographyVersion` and `FrontierDefinition` reference;
- exactly one population, economic, agriculture, and access observation slot;
- digest-bound indicator, source-role, observation, uncertainty, evidence, and optional geography-crosswalk references;
- explicit available, missing, suppressed, and not-applicable states;
- same-version, crosswalk-referenced, or unresolved geography alignment;
- a validator-derived complete, partial, or insufficient panel state; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

The object contains no county name, coordinates, geometry, source payload, observation value, unit-bearing measure, threshold, score, frontier classification, map layer, or released artifact.

## Observation and alignment rules

Every candidate declares the exact observation-kind set `ACCESS`, `AGRICULTURE`, `ECONOMIC`, and `POPULATION` in lexical order.

| Availability | Required posture |
|---|---|
| `AVAILABLE` | Observation, uncertainty, and at least one evidence reference are present; geography alignment is not unresolved. |
| `MISSING` | Observation and uncertainty references are absent; reason identifies source absence or unresolved geography alignment. |
| `SUPPRESSED` | Observation and uncertainty references are absent; at least one evidence reference supports the declared suppression posture. |
| `NOT_APPLICABLE` | Observation, uncertainty, and evidence references are absent; reason is `OUT_OF_SCOPE`. |

`SAME_VERSION` requires the observation geography reference to equal the panel geography and forbids a crosswalk reference. `CROSSWALK_REFERENCED` requires a different observation geography and a digest-bound crosswalk reference. `UNRESOLVED` requires a different geography, no crosswalk reference, and a non-available observation.

## Derived panel state

| Derived state | Decision | Meaning |
|---|---|---|
| `COMPLETE` | `REVIEW_CANDIDATE` | All four observation slots are available and geography-aligned. |
| `PARTIAL` | `HOLD` | At least one observation is available, but a gap, suppression, or unresolved alignment remains. |
| `INSUFFICIENT` | `HOLD` | No observation slot is available. |

Even `COMPLETE` is not a frontier result, scientific fitness decision, policy approval, or release candidate. The profile deliberately has no classification-result field.

## Evidence and authority boundary

All references remain opaque and unresolved. The validator performs no source fetch, value calculation, aggregation, geography resolution, crosswalk execution, evidence resolution, threshold evaluation, frontier classification, policy evaluation, promotion, release, publication, or deployment.

A passing fixture proves declaration coherence only. It does not prove any observation, definition, geography, source role, uncertainty, evidence record, crosswalk, review, release, or public product exists or is correct.

## Deterministic identity

The validator removes only `panel_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash = SHA-256(JCS(identity subject))
panel_id  = kfm:county-year-panel:<first 24 digest hex>
```

## Directory Rules basis

The primary responsibility is a derived data-product declaration, so semantic meaning belongs in the existing `contracts/data/` family. Machine shape belongs in `schemas/contracts/v1/data/`; synthetic replay in `fixtures/contracts/v1/data/`; reusable validation in `tools/validators/data/`; executable conformance in `tests/data/`; read-only orchestration in `.github/workflows/`; source reconciliation in `docs/intake/exploratory/`; and authoring provenance in `data/receipts/generated/`.

These are existing responsibility roots under ADR-0029. The packet creates no root, Frontier Matrix data store, source or evidence registry, policy home, release candidate, public API, map surface, or publication path.

## Validation

```bash
python -m unittest -v tests.data.test_county_year_panel
python tools/validators/data/validate_county_year_panel.py --fixtures
```

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the additive packet. No source, observation, evidence, geography, crosswalk, lifecycle, policy, deployment, release, or public state requires restoration.
