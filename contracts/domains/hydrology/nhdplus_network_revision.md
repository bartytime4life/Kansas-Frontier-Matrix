# Synthetic NHDPlus HR Network Revision Contract

**Status:** PROPOSED fixture-only implementation contract  
**Owning domain:** Hydrology  
**Artifact family:** `NhdplusNetworkRevisionReport`  
**Source basis:** *New Ideas 4-2-26.pdf* — NHDPlus HR/WBD network-version watcher, deterministic network hash, and downstream reindex checklist  
**Directory Rules basis:** Hydrology meaning belongs under `contracts/domains/hydrology/`; deterministic watcher logic belongs under the established `tools/ingest/hydrology_watch/` review-signal boundary.

## Purpose

Define a deterministic comparison between two frozen synthetic NHDPlus HR network snapshots. The comparator detects changes that can ripple through COMID-to-HUC12 joins, NWM or forecast attachments, and linear-referenced events without contacting a live USGS service or claiming hydrologic truth.

## Frozen snapshot profile

Each input uses `kfm.nhdplus-network-revision.synthetic.v1`, is explicitly fixture-only, and carries synthetic flowline summaries:

- `comid`, `reachcode`, `hydroseq`, `from_measure`, `to_measure`, and `vpuid`;
- `huc12` assignment;
- projected catchment area and centroid metrics used only for deterministic comparison;
- source product version and metadata timestamp; and
- fixture-only source-role and rights state.

Raw geometry is not emitted in the report.

## Identity and hash rules

`network_spec_hash` binds the canonical flowline rows sorted by `comid`. `retrieval_hash` also binds source product-version and metadata-time fields. A metadata timestamp change can therefore be audited without fabricating a network revision.

## Change classes

| Change | Impact | Result |
|---|---:|---|
| COMID added | MEDIUM | `PROPOSED_WORK_RECORD` |
| COMID removed | HIGH | `ABSTAIN` |
| ReachCode, HydroSeq, measure, or VPUID change | HIGH | `ABSTAIN` |
| HUC12 assignment change | HIGH | `ABSTAIN` |
| Catchment-area delta greater than `0.1%` | HIGH | `ABSTAIN` |
| Centroid shift greater than `100 m` | HIGH | `ABSTAIN` |
| Smaller geometry correction | LOW | `PROPOSED_WORK_RECORD` |
| Retrieval metadata only | none | `NO_MATERIAL_CHANGE` |

The `0.1%` and `100 m` thresholds are frozen fixture heuristics from the source packet. They are not adopted live policy.

## Required downstream actions

The report derives a sorted action set where relevant:

- `RECOMPUTE_COMID_HUC12`;
- `REINDEX_NWM_FORECAST_ATTACHMENTS`;
- `REFRESH_LINEAR_REFERENCED_EVENTS`; and
- `REVIEW_GEOMETRY_ALIGNMENT`.

These are reviewer prompts. The comparator performs none of them.

## Finite outcomes

- `NO_MATERIAL_CHANGE` — stable canonical network content.
- `PROPOSED_WORK_RECORD` — valid low- or medium-impact revision.
- `ABSTAIN` — valid high-impact revision requiring steward review.
- `ERROR` — unsafe or invalid fixture input.

## Trust boundary

- No live NHDPlus HR, WBD, 3DHP, NWM, or data.gov access.
- No source admission, RAW/WORK write, crosswalk recomputation, EvidenceBundle resolution, policy decision, hydrologic guidance, promotion, release, or publication.
- The report is a review signal and never publication authority.

## Rollback

Remove the contract, schema, comparator, child README, fixtures, tests, workflow, and generated authoring receipt. The change is additive and has no live data or release migration.
