# Structurally invalid BriefingSignal fixtures

- `invalid_public_use.json` proves consequential permissions fail closed.
- `invalid_missing_evidence.json` proves a confirmed claim requires evidence.
- `invalid_inline_geometry.json` proves candidate payloads cannot embed guessed coordinates.
- `invalid_duplicate_issue_create.json` proves a duplicate event cluster cannot open parallel work.
- `invalid_priority_without_reasons.json` proves a declared priority requires finite reason codes.

Every file is intentionally invalid under JSON Schema so the repository-wide contract fixture harness preserves polarity. Schema-valid semantic negatives live in `../semantic_invalid/`.
