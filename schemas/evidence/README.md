# `schemas/evidence/` — Evidence Schema Compatibility Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-evidence-readme
title: schemas/evidence/ README
type: readme; compatibility-index; schema-boundary
version: v0.1
status: draft; root-level-evidence-compatibility-path; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, evidence, compatibility, spec-normalization]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/evidence/` is a root-level compatibility guardrail for evidence-related schema notes.

The inspected v1 evidence schema family lives at `schemas/contracts/v1/evidence/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct file found | `spec_normalization.md` |
| Current role | compatibility guardrail |
| Placement | NEEDS VERIFICATION |

## Boundary

This folder is under `schemas/`, so it may contain machine-checkable shape notes only if accepted here.

It is not the active v1 evidence schema family, a data root, code root, fixture root, validator root, or release root.

## Current inventory

| Path | Status | Notes |
|---|---|---|
| `schemas/evidence/README.md` | present | Empty file expanded by this README. |
| `schemas/evidence/spec_normalization.md` | PROPOSED scaffold | Source docs point to domain identity model docs. |
| `schemas/contracts/v1/evidence/README.md` | present | Inspected v1 evidence schema family index. |

## What belongs here

- This README.
- Compatibility notes for this root-level path.
- Migration notes for evidence schema notes if placement changes.

## What does not belong here

- New canonical v1 evidence schemas while `schemas/contracts/v1/evidence/` remains the active lane.
- Data records, proof outputs, fixtures, validator code, runtime code, or release records.
- Claims that an evidence object is complete or ready for downstream use merely because it validates against a schema.

## Validation

```bash
find schemas/evidence -maxdepth 4 -type f | sort
find schemas/contracts/v1/evidence -maxdepth 4 -type f | sort
find schemas/evidence -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```

## Open questions

| Question | Status |
|---|---|
| Should `spec_normalization.md` move under `schemas/contracts/v1/evidence/`? | NEEDS VERIFICATION |
| Should `schemas/evidence/` remain as a compatibility index or be retired after migration? | NEEDS VERIFICATION |
| Which examples and tests support spec normalization? | NEEDS VERIFICATION |
