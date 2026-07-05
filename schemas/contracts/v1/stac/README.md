# `schemas/contracts/v1/stac/`

Draft schema-family placeholder under `schemas/contracts/v1/`.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct schema file | `kfm-profile-v1.schema.json` found |
| Current role | schema placeholder |
| Placement | needs verification |

## Boundary

This directory is for possible machine-checkable object shape only.

It is not a data, code, fixture, or documentation-standard location.

## Directory checks

```bash
find schemas/contracts/v1/stac -maxdepth 3 -type f | sort
find schemas/contracts/v1/stac -name '*.json' -print0 | xargs -0 -r -I{} python -m json.tool {} >/dev/null
```

## Open questions

| Question | Status |
|---|---|
| Should this path remain the schema home for the KFM profile? | NEEDS VERIFICATION |
| What fields should the profile schema require? | NEEDS VERIFICATION |
| Which examples and tests support this schema? | NEEDS VERIFICATION |
