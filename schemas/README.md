# schemas

## Purpose
Machine-checkable shape for every KFM object family. Pairs 1:1 with `contracts/`.

## Authority level
canonical

## What belongs here
JSON Schema (draft 2020-12). Tests under `schemas/tests/valid` and `schemas/tests/invalid`.

## What does not belong here
Semantic prose (lives in `contracts/`), policy rules (live in `policy/`), data, code.

## Inputs
See related folders.

## Outputs
See related folders.

## Validation
See `tests/` and `tools/validators/`.

## Review burden
Maintainer review; steward review for trust-bearing changes.

## Related folders
`contracts/`, `policy/`, `tests/schemas/`, `fixtures/`.

## Status
PROPOSED

## Domain alias schemas
When a domain alias schema wraps a shared runtime contract via `allOf` + `$ref`, enforce strictness with `unevaluatedProperties: false` (not wrapper-level `additionalProperties: false`) so inherited properties are recognized under JSON Schema 2020-12. This preserves alias strictness without false rejections; see Directory Rules schema-home guidance (§7.4).
