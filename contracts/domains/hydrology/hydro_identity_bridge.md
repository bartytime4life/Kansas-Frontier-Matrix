<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hydrology/hydro-identity-bridge/v1
title: Hydro Identity Bridge Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
policy_label: public
related:
  - ../../../schemas/contracts/v1/domains/hydrology/hydro_identity_bridge.schema.json
  - ../../../tools/validators/domains/hydrology/validate_hydro_identity_bridge.py
  - ../../../fixtures/contracts/v1/domains/hydrology/hydro_identity_bridge/
  - ../../../tests/domains/hydrology/test_hydro_identity_bridge.py
  - ./nhdplus_waterbody_crosswalk.md
tags: [kfm, hydrology, identity, nhdplus-hr, comid, crosswalk, join-receipt]
notes:
  - "Source-native NHDPlus HR identifiers and legacy COMIDs remain distinct; this object never relabels one as the other."
  - "The bridge is a no-network resolution record and does not activate a source, mutate lifecycle state, promote, release, or publish."
[/KFM_META_BLOCK_V2] -->

# Hydro Identity Bridge

## Purpose

`HydroIdentityBridge` records one bounded attempt to resolve a source-native NHDPlus High Resolution identifier and a legacy COMID through a pinned, versioned crosswalk. It exists because current HR identifiers and legacy COMIDs are different identifier families. A successful join must preserve both families and explain the release and temporal basis used to connect them.

The bridge complements the existing NHDPlus waterbody crosswalk dataset contract. The crosswalk describes the versioned mapping dataset; this bridge describes one deterministic resolution result and its `JoinReceipt` reference.

## Non-collapse rules

1. A legacy COMID must never be copied into a current `PERMANENT_IDENTIFIER` or `NHDPLUSID` field and represented as a current identifier.
2. Every current identifier is explicitly typed and marked `source_native: true`.
3. Every resolution pins the current HR release, legacy release, and crosswalk release by `spec_hash` and release identifier.
4. Geometry equality is never inferred from identifier resolution.
5. Split, merge, retired, no-legacy, and unresolved relationships return `ABSTAIN`; they do not select a winner.
6. `ANSWER` is limited to an exact one-to-one bridge with a bound join receipt.
7. A valid bridge is process evidence only. It is not an EvidenceBundle, ProofPack, PromotionDecision, ReleaseManifest, or publication event.

## Finite resolution outcomes

| Outcome | Required relationship | Meaning |
|---|---|---|
| `ANSWER` | `EXACT` | One current identifier and one legacy COMID resolve one-to-one through the pinned crosswalk. |
| `ABSTAIN` | `SPLIT`, `MERGE`, `RETIRED`, `NO_LEGACY`, or `UNRESOLVED` | The bridge cannot safely produce one current identity. |
| `DENY` | `UNRESOLVED` | The input attempts identifier relabeling, crosses incompatible source versions, or violates the bridge trust boundary. |
| `ERROR` | `UNRESOLVED` | The local validator or resolver could not complete the operation. |

Every non-error result carries a `join_receipt_ref`. The receipt records why the join answered, abstained, or was denied. It remains process memory and does not become release proof.

## Deterministic identity

The canonical projection removes `bridge_id` and `spec_hash`, serializes the remaining object as sorted compact UTF-8 JSON with non-finite numbers denied, and computes SHA-256.

- `spec_hash = sha256(canonical_projection)`
- `bridge_id = hydro-bridge:<first-24-hex-of-spec_hash>`

Arrays that act as sets are sorted and unique. Replaying identical input bytes produces the same bridge identity.

## Validation boundary

The validator is deterministic and no-network. It checks bounded UTF-8 JSON, duplicate keys, non-finite numbers, schema conformance, canonical ordering, deterministic identity, request-to-result binding, source-release binding, the finite outcome matrix, and the legacy-relabel denial rule.

It does not fetch USGS data, resolve a live ScienceBase item, inspect geometry, authenticate source authority, evaluate policy, verify signatures, alter canonical data, promote, release, deploy, or publish.

## Lifecycle and rollback

A bridge can be referenced from WORK, QUARANTINE, or PROCESSED reconciliation activity, but this contract itself writes no lifecycle data. Rollback is removal of this additive contract/schema/validator/fixture/test package. Existing crosswalk data and published state are unaffected.
