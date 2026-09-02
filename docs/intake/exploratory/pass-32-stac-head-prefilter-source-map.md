<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-stac-head-prefilter-source-map
title: Pass 32 STAC HEAD Prefilter Source Map
type: exploratory-source-map
version: v0.1
status: draft; triaged; bounded-slice-implemented-in-pr
owners: OWNER_TBD — Intake steward · Source steward · Catalog steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; source-adaptation; no-authority
related:
  - ../new-ideas-register.md
  - ../../../contracts/source/stac_asset_head_prefilter.md
  - ../../../schemas/contracts/v1/source/stac_asset_head_prefilter.schema.json
  - ../../../tools/validators/validate_stac_asset_head_prefilter.py
tags: [kfm, pass-32, stac, head, etag, last-modified, intake, source-map]
notes:
  - "Records the bounded repository adaptation of KFM-P32-PROG-0004."
  - "The Pass 32 atlas remains a downstream carrier and does not become implementation or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pass 32 STAC HEAD Prefilter Source Map

## Source candidate

| Field | Value |
|---|---|
| Atlas | `KFM_Pass_32_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Stable card | `KFM-P32-PROG-0004` |
| Pass 32 status | `NEW` / active / `PROPOSED` |
| Source IDs | `SRC-P32-002` |
| Atlas `spec_hash` | `sha256:3e0b0c84bdc56d25d2c9de9984c0b30b4a92a6025f783869dbc5341260f3670c` |
| Normalized statement | A prefilter task should query STAC, `HEAD` candidate assets, and store `ETag` and `Last-Modified` values before downloads. |

## Repository reconciliation

**CONFIRMED at base `main@7da6dd8d6b9bb510c8a85057b15e358fa2d57810`:**

- KFM already has `SourceEventEnvelopeCandidate` with deterministic identity, prior HTTP validator fields, finite source-edge routing, and no-authority claims.
- KFM already has a fixture-only web-delta profile, but that profile addresses human-readable web extraction and license-aware content/metadata modes rather than STAC asset refresh classification.
- Machine schemas live under `schemas/contracts/v1/`; semantic contracts live under `contracts/`; fixtures, validators, tests, workflows, and generated receipts retain their existing responsibility roots.
- ADR-0029 is accepted and makes Directory Governance Standard v2 the placement authority.

**PROPOSED bounded adaptation:**

- add a STAC-specific flat payload profile carried by the existing source-event envelope;
- restrict the profile to already-known asset state so the base digest and prior validators remain bound;
- validate recorded synthetic `HEAD` results without network access;
- retain the finite outcomes `UNCHANGED`, `CHANGED`, `UNAVAILABLE`, `DENY`, and `ERROR`;
- keep every download, source activation, lifecycle transition, evidence decision, release, and publication effect denied.

## Deliberately deferred

This slice does not implement:

- live STAC search or HTTP;
- authentication, credentials, redirects, retry, or rate-limit behavior;
- download execution;
- source activation or rights decisions;
- RAW admission or artifact storage;
- STAC/DCAT/PROV publication;
- EvidenceBundle creation;
- issue creation, promotion, release, or publication.

## Acceptance evidence

The bounded slice is reviewable when:

1. the profile schema is Draft 2020-12 valid and closed;
2. the base source-event validator remains a hard prerequisite;
3. synthetic fixture polarity covers unchanged, changed, unavailable, denied, upstream-error, conflict, missing-validator, schema-deny, and decision-mismatch states;
4. diagnostics are deterministic and do not echo source values;
5. tests prove no network call is attempted;
6. workflow permissions remain read-only; and
7. the generated receipt binds the exact authored artifacts.

## Disposition

`candidate-for-promotion` into a **proposed fixture-only source profile**, not into live source operation or publication authority. Human review and hosted exact-head CI remain required.

<p align="right"><a href="#top">Back to top</a></p>
