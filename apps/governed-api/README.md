# governed-api

ABSTAIN-only trust membrane stub for KFM.

## Run locally

```bash
python -m governed_api.main
```

Or with make:

```bash
make governed-api-dev
```

## What ABSTAIN-only means

Every scaffolded route returns a deterministic `DecisionEnvelope` with:
- `decision = "ABSTAIN"`
- `reason_code = "NOT_IMPLEMENTED"`
- `evidence_refs = []`

No data retrieval, policy evaluation, or external connector/model calls are performed.

Real handlers come later per ADR-0004.
