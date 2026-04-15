<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Hydro Identity Bridge Profile
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-04-14
updated: 2026-04-14
policy_label: public
related: [
  ../README.md,
  ../../../docs/domains/hydrology/usgs-hydrography-services.md,
  ../../../docs/domains/hydrology/hydrology-indexing-analytics-pipeline.md,
  ../../../data/receipts/README.md,
  ../../../schemas/README.md,
  ../../../schemas/contracts/README.md,
  ../../../schemas/tests/README.md,
  ../../../policy/README.md
]
tags: [kfm, hydrology, identity, crosswalk, nhdplus, permanent-identifier, comid]
notes: [
  Narrow contract profile for bridging current NHDPlus HR identity to legacy COMID-bearing dependencies.
  Exact mounted path remains NEEDS VERIFICATION against the checked-out branch.
]
[/KFM_META_BLOCK_V2] -->

# Hydro Identity Bridge Profile

Profile note for a governed hydrology identity-translation object that keeps **current NHDPlus HR identity** and **legacy COMID compatibility** visible without letting legacy keys silently replace canonical identity.

> [!IMPORTANT]
> **Canonical posture:** prefer `permanent_identifier` and/or `nhdplusid` for current NHDPlus HR linkage.  
> **Compatibility posture:** retain `comid_legacy` only when a declared downstream dependency still requires it.  
> **Fail-closed posture:** a bridge object must not pretend legacy-v2 identity is authoritative for HR without an explicit documented bridge basis.

## Purpose

This profile exists to make identity translation inspectable when a KFM lane must connect:

- current **NHDPlus HR** flowline or catchment identity
- current **WBD/HUC12** watershed context
- legacy **COMID**-indexed downstream metrics or artifacts

It is intentionally narrow.

This is **not** a replacement for:
- source descriptors
- dataset versions
- emitted run receipts
- release manifests
- broad hydrology mapping objects

## Why this profile exists

Current hydrology doctrine in the repo already distinguishes:

- `huc12` for watershed joins
- `nhdplusid` and/or `permanent_identifier` for current NHDPlus HR linkage
- legacy `COMID` only for explicitly documented crosswalks or downstream dependencies

That means a bridge object is useful when legacy and current identity systems must coexist visibly instead of being flattened into one ambiguous “ID”.

## Required reading rule

Interpret fields in this order:

1. `permanent_identifier` = persistent source identity when available
2. `nhdplusid` = current fabric join key for current HR service/package use
3. `comid_legacy` = compatibility key only
4. `huc12` = watershed context, not reach identity

## Minimal object shape

A `hydro_identity_bridge` object should minimally carry:

- `kind`
- `version`
- `bridge_id`
- `subject_kind`
- `permanent_identifier`
- `nhdplusid`
- `comid_legacy` *(nullable / optional when no downstream legacy dependency exists)*
- `huc12` *(required when watershed context is part of the declared use case)*
- `crosswalk_basis`
- `crosswalk_version`
- `hydrofabric_version`
- `spec_hash`
- `status`
- `reason_codes`
- `recorded_at`

## Field semantics

| Field | Meaning | Required |
| --- | --- | :---: |
| `kind` | discriminator; must equal `hydro_identity_bridge` | ✓ |
| `version` | contract version; start with `v1` | ✓ |
| `bridge_id` | stable KFM-local object id for this bridge record | ✓ |
| `subject_kind` | `flowline` \| `catchment` \| `waterbody` | ✓ |
| `permanent_identifier` | persistent upstream hydro identifier | ✓ |
| `nhdplusid` | current HR fabric linkage key | ✓ |
| `comid_legacy` | legacy compatibility key only |  |
| `huc12` | watershed context key when declared by lane |  |
| `crosswalk_basis` | how legacy/current linkage was established | ✓ |
| `crosswalk_version` | version/date/ref of the admitted crosswalk | ✓ |
| `hydrofabric_version` | declared HR/source release | ✓ |
| `spec_hash` | deterministic rule identity for this bridge policy | ✓ |
| `status` | `ACTIVE` \| `LEGACY_ONLY` \| `UNRESOLVED` \| `SUPERSEDED` | ✓ |
| `reason_codes` | bounded machine-readable explanation codes | ✓ |
| `recorded_at` | RFC3339 timestamp for this object | ✓ |
| `notes` | bounded optional reviewer-facing note |  |

## Required interpretation rules

### Rule 1 — canonical identity outranks compatibility identity

A consumer must not treat `comid_legacy` as the authoritative current identity when `permanent_identifier` or `nhdplusid` are present.

### Rule 2 — legacy-only state must stay visible

If only a legacy COMID is known and no admitted bridge basis exists yet, emit `status = UNRESOLVED` or `LEGACY_ONLY`, not a fake HR identity.

### Rule 3 — crosswalk basis must be explicit

A bridge object is invalid if it carries `comid_legacy` plus current HR keys without a declared `crosswalk_basis` and `crosswalk_version`.

### Rule 4 — watershed context does not replace reach identity

`huc12` may enrich the bridge object but must not stand in for `nhdplusid` or `permanent_identifier`.

### Rule 5 — finite status only

Open-ended prose statuses are forbidden.

## Reason code starter set

| Code | Meaning |
| --- | --- |
| `CROSSWALK_ADMITTED` | An admitted bridge basis connects current and legacy identity |
| `DOWNSTREAM_COMID_DEPENDENCY` | A declared downstream dependency still requires COMID compatibility |
| `CURRENT_IDENTITY_MISSING` | Current HR identity not yet established |
| `LEGACY_ONLY_INPUT` | Input arrived with COMID-only legacy identity |
| `FABRIC_VERSION_UNDECLARED` | Declared hydrofabric version is missing |
| `CROSSWALK_VERSION_UNDECLARED` | Bridge basis version/date/ref is missing |
| `SUPERSEDED_BY_NEWER_BRIDGE` | A newer admitted bridge record replaced this one |

## Invalid states

A validator should reject at minimum:

- missing `permanent_identifier`
- missing `nhdplusid`
- `comid_legacy` present but no `crosswalk_basis`
- `comid_legacy` present but no `crosswalk_version`
- freeform `status`
- missing `spec_hash`
- ambiguous timestamp
- `huc12` used as the only hydro identity
- status says `ACTIVE` while current identity fields are missing

## Relationship to receipts

This object is a **contract-bearing identity record**, not process memory.

Join runs and reconciliation runs should emit separate receipt objects under the receipt lane, with refs back to this bridge object.

## Relationship to mapping outputs

A mapping record may point to one admitted `hydro_identity_bridge` object when a legacy dependency is involved.

That mapping record should still carry its own decision, `spec_hash`, and `run_receipt_ref`.
