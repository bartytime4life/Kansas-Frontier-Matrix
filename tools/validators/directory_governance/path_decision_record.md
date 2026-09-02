# Path Decision Record Validator

`validate_path_decision_record.py` checks one reviewable placement evaluation against the pinned `control_plane/root_registry.yaml` projection.

It validates:

- strict JSON-compatible YAML parsing and Draft 2020-12 schema conformance;
- the exact root-registry digest, registry base reference, Directory Rules digest, and `ADR-0029` binding;
- canonical evidence, rule, reason, candidate-root, consumer, and split-target arrays;
- safe repository paths and registered candidate roots;
- active canonical/platform requirements for `PLACE` and `MIGRATE`;
- artifact-kind and executable-role ownership;
- `MIRROR`, `SPLIT`, `MIGRATE`, `HOLD`, and `DENY` companion-field semantics;
- public RAW/WORK/QUARANTINE denial and the prohibition on trust-bearing authority under `artifacts/`.

The validator emits `PASS`, `FAIL_INVARIANT`, or `ERROR_VALIDATOR`. A `PASS` means only that the record is internally consistent with its pinned machine projection. It does not authorize a path, accept an ADR, move bytes, grant write capability, or approve release, deployment, promotion, or publication.

## Commands

```bash
python tools/validators/directory_governance/validate_path_decision_record.py --fixtures
python tools/validators/directory_governance/validate_path_decision_record.py \
  fixtures/contracts/v1/governance/path_decision_record/valid/place_contract.yaml
python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_path_decision_record.py' \
  --verbose
```
