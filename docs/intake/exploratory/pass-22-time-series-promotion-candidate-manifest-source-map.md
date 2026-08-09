<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-22-time-series-promotion-candidate-manifest-source-map
title: Pass 22 Time-Series Promotion Candidate Manifest Source Map
type: source-map
version: v1.0.0
status: proposed
owners: OWNER_TBD - Source steward; Data steward; Contracts steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; non-authoritative
related:
  - ../../../contracts/data/time_series_promotion_candidate_manifest.md
  - ../../../schemas/contracts/v1/data/time_series_promotion_candidate_manifest.schema.json
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-22, pass-32, time-series, manifest, source-map]
notes:
  - "The atlas card is a proposed design source, not implementation or publication evidence."
[/KFM_META_BLOCK_V2] -->

# Pass 22 Time-Series Promotion Candidate Manifest Source Map

## Assayed idea

| Field | Evidence-backed value |
|---|---|
| Stable card | `KFM-P22-PROG-0020` |
| Title | Time-series promotion candidate manifest |
| Original posture | `PROPOSED` |
| Pass 22 statement | Station batches should emit a normalized manifest with footprint, time, station IDs, variables, encoding, and `spec_hash` identity |
| Later carry-forward | `CONFIRMED`: retained `UNCHANGED` in the Pass 23/32 consolidated atlas |
| Repository status before this slice | `CONFIRMED`: no exact stable-ID, object-name, or pull-request match was found on `main@f5efa63a3600f688cb9d6ed0255e20b9dfbac6dc` |

## Source evidence

1. Google Drive `KFM_Pass_22_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, section 8.3.59, card `KFM-P22-PROG-0020`.
2. Attached `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, consolidated page 403, retaining the same normalized statement and marking repository implementation `UNKNOWN` in the source document.
3. `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` and `docs/doctrine/directory-rules.md` on the cited repository base.

## Adaptation decisions

| Source concept | Repository adaptation | Boundary |
|---|---|---|
| Footprint | Declared WGS84 bbox | Metadata only; no geometry authority |
| Time | UTC start/end extent | No observation parsing or gap analysis |
| Station IDs | Canonical sorted stable-ID array | No alias or registry resolution |
| Variables | Canonical sorted variable-ID array | No units or scientific crosswalk |
| Encoding | Media type, format, compression, record count | No payload bytes or decoder execution |
| `spec_hash` identity | Existing RFC 8785 JCS plus SHA-256 package | Identity only; not evidence or release proof |
| Dependencies | Explicit SourceDescriptor/RunReceipt refs and nullable evidence/policy refs | References do not create downstream authority |

## Deliberate omissions

- No station API, SensorThings service, Mesonet connector, credentials, or live source claim.
- No physical-range, temporal-gap, scientific-quality, rights, sensitivity, or source-currentness decision.
- No `EvidenceBundle` resolution, policy evaluation, review authentication, catalog closure, signature, promotion, release, alias mutation, deployment, or publication.
- No schema, contract, policy, proof, receipt, or release authority is duplicated outside its responsibility root.

## Verification posture

`PROPOSED`: the new object-family semantics. `CONFIRMED`: source-card wording, later unchanged carry-forward, current-base repository gap search, adopted Directory Rules placement, and deterministic local fixture evidence. `NEEDS VERIFICATION`: hosted exact-head checks and human review.

