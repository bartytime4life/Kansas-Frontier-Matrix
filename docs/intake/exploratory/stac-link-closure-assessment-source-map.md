<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/stac-link-closure-assessment-source-map
title: STAC Link-Closure Assessment - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Catalog steward · STAC steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; intake; data; stac; graph-closure; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from the Drive idea corpus and governed Atlas triad to one offline STAC link-closure fixture family without conflating record, graph, API, availability, or release claims.
truth_posture: CONFIRMED source lineage and current-main collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION steward approval and later-main collisions
related:
  - ./new-ideas-4-16-source-map.md
  - ../../kfm_full_atlas_seed_cards.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/data/stac_link_closure_assessment.md
tags: [kfm, intake, stac, local-graph, link-closure]
[/KFM_META_BLOCK_V2] -->

# STAC link-closure assessment - source map

## Outcome

The Google Drive document *New Ideas 4-16-26* contributes pressure to align KFM catalog behavior with interoperable STAC practice. The governed repository synthesis narrows that pressure into `KFM-TRIAD-040`: record conformance, local graph closure, API behavior, and availability must remain separate reviewer states. This packet implements only deterministic, no-network local graph closure.

## Source lineage

| Source | Relevant pressure | Posture used here |
|---|---|---|
| Google Drive `New Ideas 4-16-26` (`1IqoqVHWERGK8VtLSUX69VBBmFNXqS62xBC2HE380Jrc`) | Interoperable STAC fields, links, API behavior, and external-catalog alignment. | Design pressure only; external availability and adoption claims are not carried forward. |
| `docs/intake/exploratory/new-ideas-4-16-source-map.md` | Classifies STAC record conformance, link closure, API behavior, and live availability as distinct unresolved surfaces; recommends offline synthetic fixtures first. | Repository routing authority for the bounded next step. |
| `docs/kfm_full_atlas_seed_cards.md` | `KFM-TRIAD-040` and `KFM-CAND-0120` call for deterministic no-network local link-closure fixtures without collapsing neighboring checks. | Governed candidate lineage. |
| Directory Rules and accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules. | Placement authority. |

## Current-main collision review

The inspected tree at `main@52675a800825c071ddc9df9476b543c49d73efd8` contains a KFM STAC record profile, record validators, catalog-health and catalog-closure responsibilities, STAC search-behavior fixtures, STAC GeoParquet mirror parity, and a decision-only CDL/PMTiles profile packet. That packet intentionally creates no profile or machine shape. No contract, schema, fixture family, validator, test, or workflow was found that accepts a supplied multi-record Catalog/Collection/Item graph and deterministically separates local target, type, reciprocity, and root-reachability closure from record-profile, API, and availability results. This finding is **CONFIRMED for that inspected tree**, not timeless.

## Bounded adaptation

The packet accepts synthetic local record projections with references to separate record-conformance results. It checks unique canonical records and links, a Catalog root, target presence and declared type, reciprocal `child`/`parent` and `item`/`collection` edges, and reachability through the declared hierarchy. Partial samples return `ABSTAIN` even when locally closed.

It does not parse full STAC records, resolve URLs, test HTTP, validate API search or pagination, inspect assets, mutate a catalog, resolve evidence, decide policy, approve review, release, deploy, publish, or authorize public use.

## Directory placement

| Responsibility | Path |
|---|---|
| Catalog-data semantic meaning | `contracts/data/stac_link_closure_assessment.md` |
| Canonical machine shape | `schemas/contracts/v1/data/stac_link_closure_assessment.schema.json` |
| Reusable synthetic inputs | `fixtures/contracts/v1/data/stac_link_closure_assessment/cases.json` |
| Catalog validator | `tools/validators/catalog/validate_stac_link_closure_assessment.py` |
| Executable evidence | `tests/validators/test_validate_stac_link_closure_assessment.py` |
| Hosted orchestration | `.github/workflows/stac-link-closure-assessment.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

## Verification and rollback

Catalog and STAC stewards must still decide how record-profile results are bound, how remote and relative links are resolved, how API conformance and availability are tested, and how catalog closure joins evidence, rights, correction, rollback, and release controls. Rollback is an ordinary revert of this additive packet; it changes no live catalog or publication state.
