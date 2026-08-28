<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools/validators/runtime-verification/v1
title: Runtime Verification Validator
type: validator-readme
version: 1.0.0
status: PROPOSED
owners:
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Runtime steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; validator; no-network; fail-closed
related:
  - ../../../contracts/runtime/runtime_verification.md
  - ../../../schemas/contracts/v1/runtime/runtime_verification/README.md
  - ../../../fixtures/contracts/v1/runtime/runtime_verification/README.md
notes:
  - "Diagnostics report stable codes and JSON Pointer fields without echoing payload values."
[/KFM_META_BLOCK_V2] -->

# Runtime verification validator

`validate_runtime_verification.py` validates the narrow receipt/proof family without network access.

## What it proves

- JSON is finite, UTF-8, duplicate-key-free, and within the bounded input size.
- Object kind is a supported receipt or proof.
- Draft 2020-12 schema constraints pass.
- Receipt/proof fields do not cross boundaries.
- SHA-256 representations decode correctly.
- Outcome-specific digest and declaration invariants hold.
- The fixture corpus has exact, reviewed polarity.

## What it does not prove

A passing result does not prove that bytes were fetched, a worker ran, a manifest is authoritative, a digest declaration is trusted, evidence is closed, policy allows use, a reviewer approved anything, or a release/publication transition occurred.

## Commands

```bash
python tools/validators/runtime_verification/validate_runtime_verification.py --fixtures
python tools/validators/runtime_verification/validate_runtime_verification.py path/to/object.json
```

Exit codes are `0` for pass, `1` for validation failure, and `2` for command-usage error.
