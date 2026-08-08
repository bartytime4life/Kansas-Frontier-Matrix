# PolicyObligation fixtures

This fixture family exercises the inactive, no-network `PolicyObligation` profile defined by:

- `contracts/policy/policy_obligation.md`
- `schemas/contracts/v1/policy/policy_obligation.schema.json`
- `tools/validators/policy/validate_policy_obligation.py`

The examples are synthetic. A fixture pass proves shape and deterministic semantic checks only. It does not prove that policy ran, an obligation was enforced, a transform was applied, or promotion, release, publication, export, or public use is authorized.

## Reviewed polarity

`expected_findings_manifest.json` pins each fixture to an exact outcome and a value-free finding-code set.

Valid examples cover citation attachment, geometry generalization, aggregation-only access, and export withholding. Invalid examples cover unknown vocabulary codes, policy-family mismatch, missing code-specific parameters, incoherent enforcement state, noncanonical arrays, spec-hash drift, and governance overclaim.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_obligation.py' \
  --verbose

python tools/validators/policy/validate_policy_obligation.py --fixtures
python tools/validators/policy/validate_policy_decision_vocabulary.py --registry
```
