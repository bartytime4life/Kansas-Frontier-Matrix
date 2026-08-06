<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/runtime-verification/v1
title: Runtime Verification Fixture Pack
type: fixture-readme
version: 1.0.0
status: PROPOSED
owners:
  - OWNER_TBD — Fixture steward
  - OWNER_TBD — Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: synthetic; public-safe; no-network
related:
  - ../../../../../../contracts/runtime/runtime_verification.md
  - ../../../../../../schemas/contracts/v1/runtime/runtime_verification/README.md
  - ../../../../../../tools/validators/runtime_verification/README.md
notes:
  - "Static synthetic fixtures only; no source activation or public release."
[/KFM_META_BLOCK_V2] -->

# Runtime verification fixtures

Static, synthetic, public-safe fixtures for the runtime-verification contract family.

```text
runtime_verification/
  receipts/
    valid/
    invalid/
  proofs/
    valid/
    invalid/
  expected_findings_manifest.json
```

Valid files must pass schema and semantic validation. Invalid files must fail with the exact reviewed finding-code set in `expected_findings_manifest.json`. The validator never interprets these examples as operational receipts, proofs, evidence, policy decisions, release records, or publication authority.
