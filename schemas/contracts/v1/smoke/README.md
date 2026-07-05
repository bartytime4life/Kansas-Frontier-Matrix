# README

This directory is a draft placeholder under `schemas/contracts/v1/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct schema files | not confirmed |
| Placement | needs verification |

## Boundary

This location is for possible machine-checkable object shape only. It is not a data, code, fixture, or release location.

## Next checks

```bash
find schemas/contracts/v1/smoke -maxdepth 3 -type f | sort
find schemas/contracts/v1/smoke -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```
