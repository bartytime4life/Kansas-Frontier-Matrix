<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/soil/promotion-materiality-profile
title: Soil Promotion Materiality Profile
type: semantic-contract; domain-adapter; material-change; fixture-first
version: v0.1.0
status: proposed; inactive; no-network; non-publisher
owners: OWNER_TBD — Soil steward · Data steward · Validation steward · Release steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public; soil; materiality; process-memory; non-publisher
related:
  - ../../data/material_change_assessment.md
  - ../../../pipeline_specs/soil/promotion_materiality_profile.v1.json
  - ../../../schemas/contracts/v1/domains/soil/promotion_materiality_profile.schema.json
  - ../../../schemas/contracts/v1/domains/soil/promotion_materiality_input.schema.json
  - ../../../tools/validators/domains/soil/validate_promotion_materiality.py
  - ../../../fixtures/domains/soil/promotion_materiality/
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, soil, materiality, promotion-candidate, non-event, deterministic]
[/KFM_META_BLOCK_V2] -->

# Soil promotion materiality profile

> A fixture-first soil adapter for the shared `MaterialChangeAssessment` object. It makes retrieval-time-only change a deterministic `NON_EVENT` and treats a change to content, source descriptor, schema, validator, or policy identity as a `PROMOTION_CANDIDATE`. Neither outcome authorizes promotion or release.

## Source-derived rule

The soil architecture requires meaningful content, source, schema, validator, or policy change before promotion consideration and explicitly rejects retrieval timestamp alone as a promotion trigger.

The adapter compares five substantive SHA-256 dimensions:

1. `content_spec_hash` — normalized soil content, schema, and transform identity;
2. `source_descriptor_hash` — source role, rights, endpoint/profile, and source metadata identity;
3. `schema_hash` — effective machine-shape identity;
4. `validator_hash` — effective validator/profile identity;
5. `policy_hash` — effective policy/profile identity.

`retrieved_at` is retained for audit and byte-level comparison but excluded from semantic materiality.

## Finite outcomes

| Condition | Shared change class | Outcome |
|---|---|---|
| Full snapshot unchanged | `UNCHANGED` | `NON_EVENT` |
| Only `retrieved_at` changed | `BYTE_ONLY` | `NON_EVENT` |
| One or more substantive hashes changed and evidence is complete | `MATERIAL` | `PROMOTION_CANDIDATE` |
| Baseline is absent or evidence is incomplete | `UNDETERMINED` | `HOLD` |
| Input/profile/schema evaluation fails | no assessment | `ERROR` |

A `PROMOTION_CANDIDATE` means only that later evidence, policy, review, promotion, release, correction, and rollback gates may inspect the candidate.

## Responsibility-root placement

| Responsibility | Home |
|---|---|
| Domain meaning | `contracts/domains/soil/` |
| Machine shapes | `schemas/contracts/v1/domains/soil/` |
| Inactive profile instance | `pipeline_specs/soil/` |
| Synthetic inputs and expected shared assessments | `fixtures/domains/soil/` |
| Executable adapter | `tools/validators/domains/soil/` |
| Tests | `tests/validators/` |
| Read-only CI | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

The shared assessment contract/schema remains authoritative for output meaning and shape. This profile does not create a second assessment object family.

## Trust boundary

A passing adapter result proves only deterministic local classification and shared-assessment conformance over synthetic inputs. It does not prove that either soil artifact exists, that a source is admitted, that rights or sensitivity are safe, that evidence resolves, that policy or review passed, or that promotion/release/publication is authorized.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive profile packet. No live source, lifecycle data, release, cache, or public artifact is changed by this profile.
