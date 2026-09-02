<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/briefing-conditions-source-role-readiness
title: Briefing Conditions Source-Role Readiness Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED adaptation; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; conditions; no-authority
owning_root: docs/
responsibility: Reconcile the connected briefing architecture's conditions-role backlog against current repository profiles and record the smallest non-duplicative implementation seam.
truth_posture: "CONFIRMED connected-source and repository inspection; PROPOSED compatibility matrix; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/common/conditions_source_role_readiness_matrix.md
  - ../../../contracts/common/classification_release.md
  - ../../../contracts/common/forecast_product.md
  - ../../../contracts/common/condition_relation.md
  - ../../../contracts/domains/soil/domain_observation.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, exploratory, briefing, conditions, observation, classification, forecast, readiness]
[/KFM_META_BLOCK_V2] -->

# Briefing Conditions Source-Role Readiness Source Map

## Goal

Implement the next conditions-framework seam from the connected
Briefing-to-System Integration Architecture without creating a duplicate shared
`ObservationRecord` authority.

## Source requirement

The source's Phase 4 conditions framework separates:

1. classification releases;
2. observation series and records;
3. forecast products;
4. modeled or survey products;
5. aggregate statistics; and
6. typed contextual relations.

Its exit condition calls for a synthetic USDM/Mesonet reference that proves
source-role and scale separation before live ingestion, public APIs, maps,
dashboards, or AI answers.

The connected source is design input. Private locator and connector metadata are
not copied into this public repository artifact.

## Current repository inspection

Inspection base:

```text
main@463381703bcd6eada8eea05e95c4a88912ed4b02
```

CONFIRMED at that base:

- `ClassificationRelease` has a closed fixture-only common profile requiring
  `CLASSIFICATION` / `DERIVED_CLASSIFICATION`.
- `ForecastProduct` has a closed fixture-only common profile requiring
  `FORECAST` / `PREDICTION`.
- the Soil `DomainObservation` fixture family contains a synthetic
  Mesonet-style station observation with native direct-observation and
  station-soil-moisture support semantics.
- `ConditionRelation` already defines the common observation,
  classification, forecast, model, advisory, and context role/support pairs
  used for typed relations.
- the existing classification/observation boundary test proves that the
  classification and Soil observation candidates pass only their own profiles.
- repository search found no current conditions source-role readiness matrix,
  matching pull request, or matching branch.
- an older empty observation-record candidate branch has no implementation
  commit or pull request.

## Reconciliation decision

The classification source map deliberately declined to create a shared
`ObservationRecord` because domain observation profiles already own their
domain meaning. That boundary remains sound.

The smallest dependency-closed next step is therefore:

```text
source role requirements
  -> one inactive common readiness matrix
  -> closed machine shape
  -> exact BOUND/HOLD mutations
  -> deterministic no-network validator
  -> cross-domain dependency tests
  -> read-only path-scoped workflow
  -> byte-bound generated receipt
```

The matrix binds classification, forecast, and one domain-owned observation
reference. It holds aggregate, model, and survey until an exact compatible
profile is selected through separate review.

## Why this is not a new observation authority

- no `ObservationRecord` contract or schema is added;
- the matrix references the existing Soil domain contract and fixture;
- the matrix cannot create or mutate an observation;
- role mapping remains compatibility metadata, not domain semantics;
- every bound candidate must still pass its owning validator; and
- held roles cannot borrow another role's profile merely to appear complete.

## Directory Rules basis

The accepted Directory Rules v2 responsibility signature yields one common
semantic owner and established roots:

| Artifact | Owning responsibility root | Placement result |
|---|---|---|
| Matrix meaning | `contracts/common/` | `PLACE` |
| Closed shape | `schemas/contracts/v1/common/` | `PLACE` |
| Synthetic cases | `fixtures/contracts/v1/common/` | `PLACE` |
| Repository validator | `tools/validators/` | `PLACE` |
| Cross-domain conformance | `tests/cross_domain/` | `PLACE` |
| Source reconciliation | `docs/intake/exploratory/` | `PLACE` |
| CI orchestration | `.github/workflows/` | `PLACE` |
| Authoring accountability | `data/receipts/generated/` | `PLACE` |

Applicable rules include `DIR-SIGNATURE-001`, `DIR-PLACE-001`,
`DIR-PLACE-005`, `DIR-AUTHROOT-001`, `DIR-SCOPELANE-003`,
`DIR-SCOPELANE-004`, and `DIR-DEP-001`. No root, domain, compatibility writer,
policy home, source registry, lifecycle lane, release plane, or public surface is
created.

## Validation boundary

The packet can prove:

- exact role cardinality and canonical ordering;
- intended role/support pairs;
- complete local dependency paths for bound entries;
- no binding paths or native mappings for held entries;
- explicit reasons for every hold;
- adjacent fixture success and cross-substitution denial;
- deterministic identity and finite diagnostics; and
- all-false authority effects.

It cannot prove scientific fitness, source admission, source currentness,
rights, evidence closure, policy, review, release readiness, public usefulness,
or operational adoption.

## Deliberate holds

This slice does not:

- select shared model, survey, or aggregate profiles;
- revise any existing domain or common contract;
- add a live USDM, Mesonet, NWS, or other adapter;
- read or write lifecycle data;
- build a conditions API, map, explorer, alert, dashboard, or AI answer;
- create EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest,
  correction, or rollback instances; or
- change repository settings, merge, deploy, release, or publish.

## Rollback

Before merge, close the draft and abandon the feature branch. After an
authorized merge, revert the additive packet. The selected underlying profiles
are referenced but unchanged, so rollback requires no source, lifecycle,
release, deployment, cache, or public-state restoration.
