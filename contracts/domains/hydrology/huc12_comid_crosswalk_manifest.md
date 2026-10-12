# HUC12-COMID Crosswalk Manifest Contract

**Status:** PROPOSED fixture-first contract.  
**Scope:** one deterministic, time-bounded manifest for a HUC12-to-COMID crosswalk artifact.  
**Authority boundary:** validation of this object does not admit WBD/NHD sources, resolve evidence, approve policy, promote lifecycle state, release an artifact, or publish a map layer.

## Purpose

The manifest binds one HUC12 slice to the WBD and NHD snapshots used to build it, the digest-bound crosswalk artifact, a run receipt, an EvidenceBundle reference, and an explicit validity window. It exists so a client or promotion gate can identify the exact crosswalk slice and detect material input drift without trusting a filename or build host.

The source packet used `run_receipt_url`; this repository profile deliberately narrows that field to a digest-bound `run_receipt_ref`. A URL can be a transport locator, but it is not self-verifying evidence or release authority.

## Required invariants

- `huc12` is exactly 12 digits and is embedded in `manifest_id`.
- `manifest_id` is deterministic from `huc12`, `wbd_snapshot_id`, and the UTC start date.
- `crosswalk_ref` is digest-bound and its suffix equals `crosswalk_digest`.
- `spec_hash` is SHA-256 over canonical JSON with `spec_hash` omitted.
- `valid_from` and `valid_to` are UTC timestamps and `valid_from < valid_to`.
- `comid_count <= row_count`.
- run-receipt and evidence references are digest-bound.
- RAW, WORK, and QUARANTINE references are denied from this catalog-facing profile.
- source references preserve separate WBD and NHD identities; the manifest does not collapse their source roles.

## Change assessment

Given a previously accepted slice and a candidate slice for the same HUC12:

| Condition | Outcome | Meaning |
|---|---|---|
| candidate is invalid, changes HUC12, or overlaps the prior validity window | `DENY` | malformed or non-append-only transition |
| `nhd_snapshot_id` changed | `HOLD` | steward review and fresh evidence are required |
| `crosswalk_digest` changed | `HOLD` | join output changed; steward review and fresh evidence are required |
| neither material field changed and the validity windows do not overlap | `PASS` | structurally safe to continue to later gates |

`HOLD` is not approval. The CLI uses exit code `3` only for a structurally valid material-change hold; invalid input always returns a denial exit code and cannot be masked by the hold path.

## Directory Rules basis

- semantic meaning: `contracts/domains/hydrology/`
- machine shape: `schemas/contracts/v1/domains/hydrology/`
- synthetic examples: `fixtures/domains/hydrology/`
- executable checks: `tools/validators/`
- regression proof: `tests/validators/`
- CI integration: `.github/workflows/huc12-comid-crosswalk-manifest.yml`

These are responsibility-root lanes under accepted ADR-0029; no new root or parallel schema/policy/release home is created.

## Non-effects

This profile performs no network request, source activation, real crosswalk generation, cryptographic receipt verification, EvidenceBundle resolution, policy evaluation, catalog write, promotion, release, deployment, or publication. HUC12/COMID relations remain derived crosswalk claims, not sovereign hydrologic truth.

## Validation

```bash
python -m pytest -q tests/validators/test_huc12_comid_crosswalk_manifest.py
python tools/validators/validate_huc12_comid_crosswalk_manifest.py --fixtures
```

## Rollback

Revert the contract, schema, fixture family, validator, test, and bounded workflow wiring together. Do not rewrite or delete any external crosswalk, receipt, evidence, catalog, or release history.
