<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-huc-crosswalk-explorer-source-map
title: Pass 32 HUC Crosswalk Explorer Source Map
type: exploratory-source-map; implementation-record
version: v0.1.0
status: proposed adaptation; fixture-first; production wiring held
owners: OWNER_TBD — UI steward · Hydrology steward · Evidence steward · Release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; source-adaptation; no-authority
related:
  - ../../../apps/explorer-web/src/features/huc_crosswalk_explorer/README.md
  - ../../../apps/explorer-web/src/adapters/HucCrosswalkProjection.ts
  - ../../../fixtures/ui/huc_crosswalk_projection/README.md
  - ../../../contracts/domains/hydrology/huc12_comid_crosswalk_manifest.md
  - ../../../contracts/domains/hydrology/nhdplus_waterbody_crosswalk.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, pass-32, huc12, nwis, crosswalk, hydrology, ui, no-authority]
notes:
  - "Records a bounded repository adaptation of KFM-P32-FEAT-0008."
  - "KFM-P32-IDEA-0018 and KFM-P32-PROG-0011 are reconciled as context, not implemented fetch, flow-stat, validator, signature, or promotion authority."
[/KFM_META_BLOCK_V2] -->

# Pass 32 HUC Crosswalk Explorer Source Map

## Source candidates

| Field | Value |
|---|---|
| Atlas | `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf` |
| Feature card | `KFM-P32-FEAT-0008` — HUC crosswalk explorer |
| Feature `spec_hash` | `sha256:90d8ebdbd2af64ab045164e734831e315e7dce648da8aa5ae06355d267ad14e8` |
| Context card | `KFM-P32-IDEA-0018` — HUC and NWIS proof slice |
| Context `spec_hash` | `sha256:362ee46929afc1798c1bdcb023c3f48e59a5de031f0dc5c02e160f14c7050567` |
| Context card | `KFM-P32-PROG-0011` — Hydrology crosswalk validator |
| Context `spec_hash` | `sha256:ec1eceb95e1aa41efcb4072e2aa4bbc3578a4fe097d11b3ed52a246a235c8eec` |
| Source ID | `SRC-P32-002` |
| Connected source | Google Drive `New Ideas 5-17-26` (`1cDAPrrPt_AxMB3lBH4z-wQGwKmcGEUt-nOMLLsAlxQQ`) |
| Retrieved evidence | Supplied consolidated atlas and connected Google Doc inspected 2026-08-10 |

The connected source proposes a county-scoped HUC12/COMID crosswalk seeded by
NWIS gages, plus fetch scripts, flow statistics, signing, policy checks,
promotion, and publication. The atlas preserves the Explorer idea as a
downstream reference candidate and explicitly marks repository placement and
runtime proof as unresolved.

## Repository reconciliation

**CONFIRMED at `main@8a671552785b773364f01d2e76d8ca6892a405ea`:**

- KFM already has a bounded HUC12/COMID crosswalk manifest contract, schema,
  fixtures, validator, tests, workflow, and generated receipt;
- KFM already has NHDPlus waterbody crosswalk ambiguity semantics and a
  hydrology identity bridge;
- those existing surfaces preserve versioning, digest binding, ambiguity, and
  fail-closed outcomes, but do not provide the selected Explorer feature;
- no Explorer feature, adapter, selected-card implementation, branch, or open
  PR for `KFM-P32-FEAT-0008` or “HUC crosswalk explorer” was found; and
- accepted ADR-0029 routes the app-local projection, browser feature, synthetic
  fixtures, tests, exploratory record, and generated receipt to existing
  responsibility roots.

## Bounded adaptation

Only `KFM-P32-FEAT-0008` is implemented. The adapter accepts one closed,
public-safe projection containing county FIPS, HUC12, a finite status, source
hash, digest-bound crosswalk and validation-receipt references, and sorted
digest-bound station references. The view renders that projection with no
button, link, callback, or transport client.

`VERIFIED_EXACT` may expose station references. Ambiguous, stale, unresolved,
or release-denied projections expose none. Unknown fields and mismatched
status/outcome/reason bindings fail closed without reflecting source detail.

## Source-pressure treatment

| Source pressure | Treatment | Boundary |
|---|---|---|
| HUC, county, source hash, station references | **IMPLEMENTED AS CLOSED PROJECTION** | Identifiers and hashes only; no geometry, source row, flow value, or count. |
| Crosswalk status | **IMPLEMENTED AS FINITE STATUS** | Does not compute, validate, or change a crosswalk. |
| Signed crosswalk | **NARROWED TO DIGEST-BOUND RECEIPT REFERENCE** | Does not create or claim verification of a digital signature. |
| NWIS pulls and flow statistics | **EXCLUDED** | No network or source-client code enters the browser. |
| Hydrology crosswalk validator | **RECONCILED TO EXISTING AUTHORITIES** | This PR creates no competing validator or schema. |
| Promotion and publication scripts | **REJECTED AS WRITTEN FOR THIS SLICE** | No release, deployment, or publication control is exposed. |
| Production projection producer | **HELD** | Requires hydrology, evidence, privacy, policy, and release steward review. |

## Non-effects and rollback

The slice performs no WBD, NHDPlus, NWIS, or other source read; network
request; crosswalk or flow-stat calculation; geometry processing; receipt or
signature creation or verification; evidence or policy decision; review;
promotion; release; deployment; publication; or public-use authorization.

Before merge, close the draft and abandon its branch. After an authorized
merge, revert the adapter, component, fixtures, tests, source map, and receipt
together. No external or public state requires restoration.
