# Security scan receipt v1

`kfm.security-scan-receipt/v1` is an import boundary for deterministic scanner
output. It records the exact repository commit, scanner and rules versions,
finite completeness state, finding counts, expiring suppressions, and a
digest-bound raw-result artifact.

The receipt does **not** run a scanner. It does not turn CodeQL, Codex Security,
or another automated service into merge authority, independent acceptance,
release approval, deployment approval, or proof of runtime containment. Those
three authority fields are fixed to `false`.

```bash
python tools/validators/security/validate_security_scan_receipt.py \
  receipt.json \
  --expected-commit "$(git rev-parse HEAD)"
```

A partial or failed scan may be represented, but it remains visibly partial or
failed. Suppressions require a reason and a future UTC expiry. The raw scanner
artifact must be retained by reference and SHA-256 digest.
