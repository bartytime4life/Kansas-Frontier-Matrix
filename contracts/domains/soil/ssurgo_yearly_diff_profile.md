<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/soil/ssurgo-yearly-diff-profile
title: SSURGO and gNATSGO Yearly Diff Profile Contract
type: semantic-contract
version: v0.2.0
status: proposed-inactive
owners: OWNER_TBD — Soil steward · Source steward · Evidence steward · Validation steward
created: 2026-08-08
updated: 2026-08-10
policy_label: internal; fixture-only; no-network; non-authoritative
owning_root: contracts/
responsibility: Define the bounded meaning of a year-pinned soil snapshot-diff profile without activating sources or authorizing publication.
truth_posture: cite-or-abstain; implementation claims require current repository evidence
related:
  - ../../../schemas/contracts/v1/domains/soil/ssurgo_yearly_diff_profile.schema.json
  - ../../../pipeline_specs/soil/ssurgo_yearly_diff_profile.v1.json
  - ../../../tools/validators/domains/soil/validate_ssurgo_yearly_diff_profile.py
  - ../../../tools/generators/build_soil_yearly_diff.py
  - ../../../fixtures/domains/soil/yearly_diff/cases.json
  - ../../../docs/intake/exploratory/pass-32-ssurgo-yearly-diff-source-map.md
  - soil_watcher_spec.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [soil, ssurgo, gnatsgo, yearly-diff, stac, prov, fixture-only, no-network]
notes:
  - This profile is a downstream candidate carrier and not a source, EvidenceBundle, release, or publication record.
  - The profile reuses the accepted responsibility roots and does not create a parallel schema, receipt, proof, catalog, or release authority.
[/KFM_META_BLOCK_V2] -->

# SSURGO and gNATSGO Yearly Diff Profile

## Status

**PROPOSED, inactive, fixture-only.** This contract implements a bounded first slice of Pass 32 candidates `KFM-P32-IDEA-0010` and `KFM-P32-PROG-0013`. It does not fetch NRCS data, activate the existing soil watcher, admit RAW material, validate a real STAC or PROV document, promote, release, or publish.

## Purpose

`SoilYearlyDiffProfile` binds two consecutive, year-pinned snapshots from one soil source family to deterministic diff, STAC-reference, provenance-reference, and receipt-reference metadata. The profile exists so downstream analysis can state exactly which soil representation it used instead of silently following a mutable current view.

The two source roles remain distinct:

| Source family | Support type | Diff profile |
|---|---|---|
| `SSURGO` | `AUTHORITATIVE_STATIC_SOIL_SURVEY` | `SSURGO_KEYED_RECORD_DIFF_V1` |
| `GNATSGO` | `GRIDDED_DERIVATIVE_SOIL` | `GNATSGO_GRID_METADATA_DIFF_V1` |

A gNATSGO profile must never masquerade as authoritative keyed SSURGO survey evidence, and SSURGO must not be interpreted as a gridded model surface.

## Required profile closure

A valid profile contains:

1. a previous-year and current-year snapshot whose years differ by exactly one;
2. immutable-looking artifact references and SHA-256 digests for both snapshots;
3. separate STAC item, PROV entity, source-snapshot receipt, and validation receipt references;
4. explicit geometry and attribute normalization flags;
5. one or more `TransformReceipt` references whenever normalization changed geometry or attributes;
6. a deterministic diff artifact with added, removed, and modified counts;
7. canonical, duplicate-free changed-property names;
8. a hard denial of observed-property relabeling;
9. fetch, validation, and diff provenance activities, with no publication activity;
10. `WORK` or `QUARANTINE` output only; and
11. all source activation, network, RAW admission, promotion, release, and publication authority flags set to `false`.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape and bounded semantic checks pass for a synthetic profile. |
| `DENY` | Schema or semantic checks reject the candidate. |
| `ERROR` | The validator cannot safely read or evaluate the input. |

A `PASS` is not evidence that NRCS source bytes, source terms, rights, real STAC items, PROV graphs, release state, or publication readiness are valid.

## Deterministic dry-run builder

`tools/generators/build_soil_yearly_diff.py` implements the source map's next bounded step. It accepts two explicit local `SoilSyntheticSnapshotManifest` JSON files, requires one source family and consecutive years, compares canonical record keys, and emits a candidate build result containing:

- the existing validated `SoilYearlyDiffProfile`;
- sorted added and removed record keys;
- sorted modified-record entries with before/after RFC 8785 hashes;
- canonical changed-property names; and
- a deterministic hash binding the detailed synthetic record diff to the profile's diff artifact declaration.

The default command writes only to stdout. `--write PATH` is required for filesystem output, and existing output is preserved unless `--force` is explicit. Inputs must remain fixture-only and no-network. The helper does not fetch NRCS bytes or create STAC, PROV, receipt, evidence, promotion, release, or publication authority.

```bash
python tools/generators/build_soil_yearly_diff.py \
  fixtures/domains/soil/yearly_diff/snapshots/ssurgo-2025.json \
  fixtures/domains/soil/yearly_diff/snapshots/ssurgo-2026.json
```

## Stable semantic findings

The validator emits value-free reason codes including:

- `SOIL_YEARLY_SPEC_HASH_MISMATCH`
- `SOIL_YEARLY_SOURCE_ROLE_INVALID`
- `SOIL_YEARLY_YEAR_SEQUENCE_INVALID`
- `SOIL_YEARLY_TRANSFORM_RECEIPT_REQUIRED`
- `SOIL_YEARLY_TRANSFORM_RECEIPT_UNEXPECTED`
- `SOIL_YEARLY_CHANGED_PROPERTIES_NOT_CANONICAL`
- `SOIL_YEARLY_OBSERVED_PROPERTY_RELABEL_DENIED`
- `SOIL_YEARLY_DIFF_SUMMARY_INCOHERENT`
- `SOIL_YEARLY_AUTHORITY_OVERREACH`

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. Semantic meaning belongs in `contracts/domains/soil/`; machine shape belongs in `schemas/contracts/v1/domains/soil/`; declarative pipeline profiles belong in the existing `pipeline_specs/soil/` lane; executable validation belongs in `tools/validators/domains/soil/`; fixtures and tests remain under their responsibility roots; source adaptation records belong in `docs/intake/exploratory/`; and generated authoring receipts belong in `data/receipts/generated/`.

No new root or parallel authority is created.

## Rollback

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive commit. No live source, schedule, network permission, RAW data, release, API, map layer, cache, or public artifact exists to unwind.
