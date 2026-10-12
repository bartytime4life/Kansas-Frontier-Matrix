# Contract fixture manifests

This directory owns deterministic **test inventory**, not semantic meaning, schema shape,
policy, evidence, release, or publication authority.

## Purpose

`contract_fixture_families.v1.json` declares a bounded first wave of existing KFM
contract-schema fixture families. The repository validator resolves each declared schema and
canonical fixture root, requires nonempty `valid/` and `invalid/` lanes, and proves the
expected JSON Schema polarity without copying fixture bytes into a second test home.

The initial wave covers:

| Family | Schema | Canonical fixture root |
|---|---|---|
| `decision-envelope` | `schemas/contracts/v1/runtime/decision_envelope.schema.json` | `fixtures/contracts/v1/runtime/decision_envelope` |
| `evidence-bundle` | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | `fixtures/contracts/v1/evidence/evidence_bundle` |
| `runtime-response-envelope` | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` | `fixtures/contracts/v1/runtime/runtime_response_envelope` |

## Authority and placement

- `tests/contracts/manifests/` owns executable test discovery and review inventory.
- `schemas/contracts/v1/` remains the machine-shape authority.
- `fixtures/contracts/v1/` remains the reusable valid/invalid fixture authority.
- `tools/validators/validate_contract_fixture_manifest.py` owns reusable validation behavior.
- `.github/workflows/contracts-validate.yml` owns CI orchestration only.
- `data/receipts/generated/` records AI authoring provenance and grants no approval.

This placement follows accepted Directory Rules responsibility-root routing. No new root,
contract family, schema home, fixture authority, policy lane, lifecycle stage, proof store,
release lane, or public path is created.

## Commands

```bash
python tools/validators/validate_contract_fixture_manifest.py \
  tests/contracts/manifests/contract_fixture_families.v1.json \
  --format text

python -m unittest discover \
  --start-directory tests/contracts \
  --pattern 'test_contract_fixture_manifest.py' \
  --verbose
```

`make test` also discovers the focused test module because the root Makefile includes
`tests/contracts`.

## Finite outcomes and exit codes

| Outcome | Exit | Meaning |
|---|---:|---|
| `PASS` | `0` | Every declared path exists, both fixture lanes are nonempty, valid cases pass, and invalid cases fail. |
| `FAIL` | `1` | At least one declared valid case was rejected or one declared invalid case was accepted. |
| `ERROR` | `2` | Manifest shape, path safety, file safety, schema loading, fixture inventory, or evaluation failed. |

Reports are deterministic and do not echo fixture values. Findings expose only stable codes,
family identifiers, and repository-relative paths.

## Negative examples

The `invalid/` directory contains exact manifest-level failures for path escape, duplicate
family identity, and an empty family inventory. Additional schema-polarity and missing-lane
failures are built in temporary test repositories so they cannot interfere with canonical KFM
fixtures.

## Trust boundary

A green result proves only:

1. the declared schemas and fixture roots exist at the tested revision;
2. each lane has at least one valid and one invalid JSON case; and
3. JSON Schema polarity matches the lane declaration.

It does **not** prove semantic truth, schema completeness, policy correctness, evidence
resolution, source admission, review, promotion, release, deployment, or publication.

## Maintenance

- Keep family identifiers unique and alphabetically ordered.
- Reuse canonical fixture roots; do not duplicate fixture payloads under `tests/`.
- Add a family only after its schema and both fixture lanes exist.
- Preserve no-network behavior and deterministic output.
- Treat a polarity change as a reviewed contract/schema/fixture change, not a manifest-only fix.
- Update this README and the generated receipt whenever the first-wave inventory changes.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge,
revert the scoped manifest, validator, tests, workflow update, documentation, and generated
receipt. No lifecycle data, source activation, release state, deployment, or public artifact
requires rollback.
