# Low-cost-sensor calibration fixtures

`fixtures/domains/atmosphere/low_cost_sensor_calibration/`

Status: frozen synthetic fixture profile / noncanonical / no-network / non-release.

This lane proves only a bounded calibration-qualification and anti-collapse shape for repository-owned synthetic records. It does not train or apply a correction model, establish reference-grade equivalence, validate a scientific method, admit a source, evaluate policy, release data, or publish an air-quality value.

## Frozen profile

- Profile ID: `kfm-atmosphere-low-cost-sensor-calibration-fixture-v1`
- Object family: `PM25Observation`
- Knowledge character: `LOW_COST_SENSOR`
- Source role: `observed`
- References: exact repository-owned `fixture://` identities only
- Spatial support: fictional generalized-county sentinel `99999` only
- Governance: fixture-only, not released, and `promotion_eligible: false`
- CLI scope: `atmosphere-low-cost-sensor-calibration-fixture`

The profile preserves two positive controls:

| Fixture | Boundary |
|---|---|
| `valid/caveated_context.json` | Uncorrected low-cost context with explicit caveat, confidence, limitations, and no reference or release claim |
| `valid/corrected_with_lineage.json` | Synthetic corrected-pair lineage with method/version, exact model/training/specification identities, full SHA-256 identity-string digests, raw/reference/evaluation evidence binding, declared meteorology, held-out-evaluation metadata, transfer/drift states, caveats, and no release claim |

Every invalid JSON file has one same-stem `.expected_error.txt` sidecar containing exact sorted `CODE<TAB>$.path` findings.

## Exact negative inventory

- missing caveat;
- missing correction version and model/training/specification digests;
- missing bound model identity in the exact evidence set;
- raw/corrected pair collapse;
- modeled output presented as raw;
- missing reference-collocation evidence;
- peer consensus presented as the reference anchor;
- missing declared meteorology inputs;
- missing held-out uncertainty and validity-bound state;
- unknown transferability and drift states;
- unbounded deployment-regime transfer;
- a single metric paired with promotion eligibility;
- missing confidence, limitations, and rollback state;
- reference-grade, regulatory, and public-release overclaim; and
- precise-site exposure or a real county identifier on the fictional fixture surface.

The three digest fields are SHA-256 pins of the exact fixture identity strings.
They prevent arbitrary identity substitution inside this frozen profile; they are
not hashes of trained model bytes, source data, or scientific evidence.

These are profile-local denials. They do not establish a canonical Atmosphere schema, policy bundle, correction equation, scientific threshold, source descriptor, EvidenceBundle, review decision, or release state.

## Run

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/atmosphere/test_low_cost_sensor_caveat_required.py --verbose

python tools/validators/domains/atmosphere/validate_low_cost_sensor_caveats.py \
  fixtures/domains/atmosphere/low_cost_sensor_calibration/valid/*.json
```

The validator emits finite, sorted, non-echoing code/path findings and exits `0` for all-pass input, `1` when any finding exists, and `2` for CLI usage failure.
