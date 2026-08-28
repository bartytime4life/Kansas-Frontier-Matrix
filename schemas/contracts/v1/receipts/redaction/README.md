# Receipt Schema Child Path

This README documents a requested child path under `schemas/contracts/v1/receipts/`.

Status: draft / README-only / NEEDS VERIFICATION.

Boundary: this folder is for schema documentation only. It is not a data root, policy root, release root, proof root, runtime root, or public artifact root.

Do not add schema files here until the schema-home decision is reviewed by the receipt, schema, contract, validation, policy, and release stewards.

Related nearby surfaces to review before promotion:

- `schemas/contracts/v1/receipts/redaction_receipt.schema.json`
- `schemas/contracts/v1/governance/redaction_receipt.schema.json`
- `schemas/contracts/v1/policy/redaction-receipt.json`
- `contracts/shared/redaction_receipt.md`

Validation commands:

```bash
find schemas/contracts/v1/receipts/redaction -maxdepth 2 -type f | sort
python tools/validate_all.py || true
```

Rollback: revert the commit that changed this README.
