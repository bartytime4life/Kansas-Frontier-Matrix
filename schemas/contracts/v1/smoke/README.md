# `schemas/contracts/v1/smoke/`

Draft schema-family placeholder under `schemas/contracts/v1/`.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-smoke-readme
title: schemas/contracts/v1/smoke/ README
type: readme
version: v0.1
status: draft; placeholder; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, contracts-v1, placeholder]
[/KFM_META_BLOCK_V2] -->

## Status

| Item | Status |
|---|---|
| README | present |
| Direct schema files | not confirmed |
| Placement | needs verification |
| Current role | placeholder |

## Boundary

This location is for possible machine-checkable object shape only.

It is not a data, code, fixture, or release location.

## Directory checks

```bash
find schemas/contracts/v1/smoke -maxdepth 3 -type f | sort
find schemas/contracts/v1/smoke -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```

## Open questions

| Question | Status |
|---|---|
| Should this directory remain README-only? | NEEDS VERIFICATION |
| Should future schema files live here? | NEEDS VERIFICATION |
| Which contracts and examples would support future schemas here? | NEEDS VERIFICATION |
