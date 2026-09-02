# AirNow-to-AQS Fixture Reconciliation

Validates one synthetic `AirnowAqsReconciliationCandidate`, preserves AirNow as provisional lineage, and emits a minimized report indicating whether a matching validated and certified AQS concentration is available for steward-reviewed supersession.

```bash
python tools/validators/domains/atmosphere/airnow_aqs_reconciliation/validate_reconciliation.py \
  fixtures/domains/atmosphere/airnow_aqs_reconciliation/valid/certified_replacement.json
```

The evaluator is no-network and non-authoritative. It performs no source access, regulatory certification, lifecycle write, alerting, promotion, release, or publication.
