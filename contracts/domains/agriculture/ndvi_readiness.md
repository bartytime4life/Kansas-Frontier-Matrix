# Smoke-Aware NDVI Readiness Assessment Contract

**Status:** PROPOSED implementation contract  
**Authority owner:** Agriculture domain  
**Artifact family:** `NdviReadinessAssessment`  
**Source basis:** *New Ideas 4-2-26(1).pdf* — daily NDVI readiness tile and smoke-mask gating pattern  
**Directory Rules basis:** the product-level meaning belongs under `contracts/domains/agriculture/`; atmospheric inputs remain source-role references and do not transfer atmosphere-domain truth ownership.

## Purpose

Define a deterministic, fixture-only sidecar assessment that decides whether an NDVI-delta product is an `EMIT_CANDIDATE` or must remain on `HOLD`. The artifact binds readiness thresholds, area coverage, heavy-smoke overlap, input receipt resolution, county summaries, QC reasons, and non-release governance state.

This slice validates the sidecar contract. It does not fetch ABI, HMS, MAIAC, HRRR-Smoke, HLS, or any other source; calculate NDVI; build a COG; issue health guidance; authorize promotion; or publish a layer.

## Required fields

The assessment carries:

- a stable assessment ID, UTC assessment time, product, and region;
- configurable minimum mask-health and ready-area thresholds;
- the source packet's four-level readiness ladder;
- county-level readiness summaries and a critical-AOI smoke count;
- source-role-explicit inputs with `spec_hash`, `evidence_ref`, and receipt-resolution state;
- enumerated QC reason counts;
- a finite `EMIT_CANDIDATE` or `HOLD` decision;
- fixture-only, not-released governance state.

## Deterministic decision rules

A payload is an `EMIT_CANDIDATE` only when all conditions hold:

1. `readiness_score >= min_mask_health_emit`;
2. `fraction_ready >= min_area_fraction_emit`;
3. heavy-smoke overlap count is zero when `no_heavy_smoke_in_aois=true`;
4. every contributing input receipt is `RESOLVED`;
5. `primary_blocker` is null and decision reasons are empty.

Otherwise the outcome is `HOLD` and the exact, sorted reasons are derived from:

- `LOW_MASK_HEALTH`;
- `LOW_READY_AREA`;
- `HEAVY_SMOKE_AOI`;
- `INPUT_RECEIPT_UNRESOLVED`.

The readiness level must agree with the score:

| Level | Score |
|---|---|
| `0` FAIL | `< 0.30` |
| `1` SUSPECT | `0.30 <= score < 0.60` |
| `2` ACCEPTABLE | `0.60 <= score < 0.80` |
| `3` HIGH | `>= 0.80` |

## Source-role anti-collapse

Input roles are explicit:

- `observation` — measured or retrieved Earth-observation input;
- `analyst_smoke_mask` — analyst-interpreted smoke extent;
- `corroboration` — independent supporting retrieval;
- `forecast` — modeled future smoke context.

A forecast cannot masquerade as an observation, and an analyst mask cannot become a certified concentration. The sidecar records contribution and readiness only.

## Trust boundary

- `EMIT_CANDIDATE` is not `PUBLISHED`.
- A passing validator is not evidence, policy approval, review, promotion, or release.
- Missing or unresolved input receipts fail closed to `HOLD`.
- No COG bytes, source credentials, private locations, or live endpoints are handled.
- Public delivery still requires EvidenceBundle closure, policy review, ReleaseManifest, correction path, and rollback target.

## Rollback

Remove this contract and its paired schema, validator, fixtures, tests, workflow, and generated authoring receipt. No live source, COG, catalog, or published artifact is modified.
