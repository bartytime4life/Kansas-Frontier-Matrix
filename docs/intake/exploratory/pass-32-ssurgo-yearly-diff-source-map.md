<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-ssurgo-yearly-diff-source-map
title: Pass 32 SSURGO and gNATSGO Yearly-Diff Source Map
type: source-adaptation-record
version: v0.1.0
status: draft
owners: OWNER_TBD — Soil steward · Source steward · Evidence steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; fixture-only
owning_root: docs/
responsibility: Record the bounded adaptation of Pass 32 yearly soil versioning candidates into a fixture-only repository slice.
truth_posture: cite-or-abstain
related:
  - ../../../contracts/domains/soil/ssurgo_yearly_diff_profile.md
  - ../../../pipeline_specs/soil/ssurgo_yearly_diff_profile.v1.json
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/domains/soil/soil_watcher_spec.md
tags: [pass-32, soil, ssurgo, gnatsgo, yearly-diff, source-map]
notes:
  - The Pass 32 atlas is a downstream carrier and does not itself authorize repository placement, source activation, release, or publication.
[/KFM_META_BLOCK_V2] -->

# Pass 32 SSURGO and gNATSGO Yearly-Diff Source Map

## Goal

Adapt the smallest dependency-closed portion of two Pass 32 candidates into deterministic repository evidence:

| Candidate | Source-supported statement | Adapted repository behavior |
|---|---|---|
| `KFM-P32-IDEA-0010` | Annual SSURGO and gNATSGO refreshes should produce year-pinned STAC, diff, and PROV outputs. | A closed profile requires consecutive snapshots and opaque year-pinned STAC/PROV references. |
| `KFM-P32-PROG-0013` | A yearly soil refresh pipeline should produce current/previous-year diff outputs and provenance for fetch, validation, diff, and publication activities. | The fixture-only slice binds fetch, validation, and diff activity references while deliberately requiring publication activity to remain absent. |

## Current repository evidence

At base `main@d5b67a6cf916319ba34796f9feb92c3cce0fc0a1`:

- `contracts/domains/soil/soil_watcher_spec.md` already defines an inactive, no-network SSURGO/gNATSGO watcher candidate and preserves source-role anti-collapse.
- `pipeline_specs/watchers/soil_ssurgo_gnatsgo.json` already carries placeholder-only source scope and WORK/QUARANTINE outputs.
- `data/registry/sources/soil/nrcs-ssurgo.yaml` and `nrcs-gnatsgo.yaml` are the existing source-placeholder homes referenced by the watcher profile.
- `pipeline_specs/soil/` is the existing declarative soil-pipeline responsibility lane.
- ADR-0029 is accepted and makes Directory Governance Standard v2 the placement authority.
- No exact `SSURGO yearly diff pipeline` implementation was found in the inspected current repository search.

## Adaptation boundary

The implementation intentionally stops at a **fixture-only profile and validator**. It does not:

- fetch, cache, or compare live NRCS bytes;
- declare source rights, source activation, authority, or currentness;
- emit real STAC items, PROV graphs, `TransformReceipt`s, EvidenceBundles, proofs, catalogs, or release manifests;
- write RAW, PROCESSED, CATALOG, TRIPLET, or PUBLISHED state;
- execute the inactive watcher;
- promote, release, deploy, publish, or authorize public use.

## Directory Rules basis

The packet uses existing responsibility roots only: semantic meaning in `contracts/`, machine shape in `schemas/`, declarative profile in `pipeline_specs/soil/`, validation in `tools/`, fixtures in `fixtures/`, tests in `tests/`, CI orchestration in `.github/workflows/`, this adaptation record in `docs/intake/exploratory/`, and authoring memory in `data/receipts/generated/`.

## Follow-up candidates

A later PR may add a dry-run builder that consumes two locally supplied synthetic snapshot manifests and emits an actual diff report. Live NRCS acquisition, source terms, STAC/PROV record emission, promotion, release, and public delivery remain separately governed work.
