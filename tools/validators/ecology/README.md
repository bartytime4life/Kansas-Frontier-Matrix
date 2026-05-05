# Ecology validators

This directory contains the local KFM governed-ingestion proof validator and the cosign helper.

```bash
python3 tools/validators/ecology/validate_run.py validate --root . --allow-unsigned
python3 tools/validators/ecology/validate_run.py negative --root .
tools/validators/ecology/sign_and_verify.sh sign .
```

`--allow-unsigned` is intended for local fixture validation only. Production verification should require real cosign bundles.
