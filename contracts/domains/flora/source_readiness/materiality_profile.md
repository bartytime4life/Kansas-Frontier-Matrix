<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/flora/source-readiness-materiality-profile
title: Flora Source-Readiness Materiality Profile
type: semantic-contract; domain-materiality-profile
version: v0.1.0
status: draft; PROPOSED_INACTIVE; fixture-first; no-source-activation; no-release-authority
owners: OWNER_TBD — Flora steward · Source steward · Rights steward · Sensitivity steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; flora; source-readiness; materiality; synthetic; no-network; review-candidate-only
related:
  - ../../../../docs/domains/flora/EXPANSION_BACKLOG.md
  - ../../../../contracts/data/material_change_assessment.md
  - ../../../../schemas/contracts/v1/domains/flora/source_readiness/materiality_profile.schema.json
  - ../../../../schemas/contracts/v1/domains/flora/source_readiness/materiality_candidate.schema.json
  - ../../../../pipeline_specs/flora/source_readiness/materiality_profile.v1.json
  - ../../../../fixtures/domains/flora/source_readiness/materiality/
  - ../../../../tools/validators/domains/flora/validate_source_readiness_materiality.py
  - ../../../../tests/validators/domains/flora/test_source_readiness_materiality.py
notes:
  - "Implements a bounded, inactive part of Flora backlog EXP-001/003/008 and source-readiness ideas from New Ideas 5-19-26."
  - "Thresholds are fixture profile values, not adopted source, rights, sensitivity, or publication policy."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Source-Readiness Materiality Profile

> Classify whether a **synthetic, already-normalized** Flora source-readiness
> comparison is unchanged, byte-only, semantically non-material, materially
> changed, or unresolved—without fetching or activating any source.

## Goal

The Flora backlog calls for source-drift monitoring, a registry of
environmental probes, and a threshold-policy surface. The attached idea packet
adds concrete readiness dimensions: georeference completeness, specimen
backing, license resolution, API availability, freshness, coordinate
uncertainty, and sensitivity posture.

This slice turns those dimensions into an explicit,
`PROPOSED_INACTIVE` materiality profile and a deterministic adapter that emits
the shared `MaterialChangeAssessment` object. It deliberately stops before
source admission, policy, evidence closure, promotion, release, or public use.

## Directory Rules basis

| Responsibility | Home | Artifact |
|---|---|---|
| Domain meaning | `contracts/domains/flora/source_readiness/` | This contract |
| Machine shape | `schemas/contracts/v1/domains/flora/source_readiness/` | Profile and candidate schemas |
| Declarative inactive profile | `pipeline_specs/flora/source_readiness/` | Versioned profile instance |
| Synthetic examples | `fixtures/domains/flora/source_readiness/materiality/` | Positive and exact-negative fixtures |
| Reusable validation | `tools/validators/domains/flora/` | Deterministic adapter |
| Enforceability proof | `tests/validators/domains/flora/` | Unit and CLI tests |
| CI orchestration | `.github/workflows/` | Read-only focused workflow |

The slice creates no new root and no parallel source, schema, policy, receipt,
proof, release, or publication home.

## Candidate boundary

A candidate contains:

- stable assessment, subject, baseline, and candidate references;
- non-placeholder SHA-256 baseline and candidate digests;
- a declared semantic-change state;
- `analysis_unit_kind = occurrence_dataset`;
- baseline and candidate values for each reviewed metric;
- canonical, sorted evidence-reference arrays;
- timezone-aware assessment, baseline, and candidate times.

Metrics are intentionally disaggregated. A single opaque readiness score is
not accepted because it could hide license, sensitivity, geometry, or source
access uncertainty. This profile is limited to occurrence datasets; checklist,
conservation-status, modeled-range, and contextual sources need their own
source-role-specific profiles rather than inheriting these criteria.

## Fixture profile

All numeric comparisons use absolute delta and a **strictly greater than**
operator.

| Criterion | Fixture threshold | Material when |
|---|---:|---|
| Georeferenced fraction | `0.05` | Absolute delta is greater than 0.05 |
| Specimen-backed fraction | `0.10` | Absolute delta is greater than 0.10 |
| License-resolved fraction | `0.00` | Any resolved-license fraction change occurs |
| P95 coordinate uncertainty | `5 km` | Absolute delta is greater than 5 km |
| Freshness | stale after `90 days` | Baseline and candidate fall on opposite sides of the stale boundary |
| API accessibility | state comparison | Boolean access state changes |
| Sensitivity posture | state comparison | `public/generalized/controlled/restricted/unknown` posture changes |

These values are synthetic acceptance thresholds for an inactive profile.
Changing or activating them requires separate source, rights, sensitivity,
domain, and policy review.

## Finite behavior

| Condition | `MaterialChangeAssessment` result |
|---|---|
| Digests equal | `UNCHANGED / NON_EVENT` |
| Bytes differ and semantic change is false | `BYTE_ONLY / NON_EVENT` |
| Semantic metrics are available and below all triggers | `SEMANTIC_NON_MATERIAL / NON_EVENT` |
| Any numeric trigger passes | `MATERIAL / PROMOTION_CANDIDATE` with `MATERIALITY_THRESHOLD_MET` |
| Any license, freshness, access, or sensitivity state changes | `MATERIAL / PROMOTION_CANDIDATE` with `DOMAIN_STATUS_CHANGE` |
| Semantic state, required metric, or profile binding is unresolved | `UNDETERMINED / HOLD` |

A `PROMOTION_CANDIDATE` is process memory for review. It grants no authority.

## Trust and safety boundary

The adapter:

- performs no network calls;
- never reads or writes RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS,
  PUBLISHED, receipt, proof, or release stores;
- does not decide whether GBIF, USDA PLANTS, iDigBio, NatureServe, or any
  herbarium is admitted or authoritative;
- does not determine rights, redistribution, rare-plant sensitivity,
  cultural authority, taxonomy truth, or geoprivacy;
- emits no source record, `EvidenceBundle`, `PolicyDecision`,
  `PromotionDecision`, `ReleaseManifest`, notification, map layer, or public
  claim;
- keeps all governance flags false and `release_ref` null.

Missing metrics produce `HOLD`; invalid input fails closed with stable reason
codes. CLI output contains file names, classifications, and finding paths but
does not echo candidate source references or metric values.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/flora \
  --pattern 'test_source_readiness_materiality.py' \
  --verbose

python tools/validators/domains/flora/validate_source_readiness_materiality.py \
  --fixtures
```

A green result proves only the reviewed synthetic profile, profile digest,
fixture polarity, shared assessment shape, deterministic behavior, and
no-network/non-echoing boundary.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, revert the feature commit. No live source, lifecycle record,
receipt, proof, policy decision, release object, deployment, public route, or
published artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
