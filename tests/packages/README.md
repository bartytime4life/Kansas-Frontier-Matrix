# Package tests

`tests/packages/` contains executable conformance and boundary tests for
reusable code under [`packages/`](../../packages/README.md). Production code
must not import this tree. This README is an authored navigation and execution
guide; test modules and the package implementations remain the evidence for
the behavior they exercise.

## Suite inventory

| Test path | Package surface | Confirmed coverage |
| --- | --- | --- |
| [`connectors_core/`](connectors_core/) | [`packages/connectors-core/`](../../packages/connectors-core/README.md) | Import safety, source-head and ETag distinctions, bounded retries, streaming digests, integrity mismatch, metadata allowlisting, and diagnostic redaction |
| [`domains/flora/normalizers/`](domains/flora/normalizers/) | [`packages/domains/flora/`](../../packages/domains/flora/README.md) | Fixture-only Darwin Core occurrence normalization and intake-governance decisions, including schema conformance, deterministic identity, sensitivity holds, and fail-closed inputs |
| [`envelopes/`](envelopes/) | [`packages/envelopes/`](../../packages/envelopes/README.md) | Closed finite-outcome AI receipt, runtime-response, mock-adapter, and map-context candidate helpers; deterministic output; and non-authority and precision-disclosure bounds |
| [`evidence_resolver/`](evidence_resolver/) | [`packages/evidence-resolver/`](../../packages/evidence-resolver/README.md) | Bounded evidence-reference candidate resolution, fixture adapters, result schema, runtime projection, path confinement, and negative outcomes |
| [`pipelines_core/`](pipelines_core/) | [`packages/pipelines-core/`](../../packages/pipelines-core/README.md) | Planning-only backfill windows and pipeline-resilience decisions, including retry, circuit-breaker, queue, replay, emergency-stop, and CLI projection behavior |
| [`schema_registry/`](schema_registry/) | [`packages/schema-registry/`](../../packages/schema-registry/README.md) | Local schema discovery and lookup, deterministic snapshots, duplicate and size rejection, symlink denial, and no-network CLI behavior |

Directory names use Python import-style underscores where the corresponding
package directory uses hyphens. Use the paths in this table rather than
deriving a test path from a distribution name.

## Run the suites

Run commands from the repository root after installing the repository's Python
test dependencies. These commands do not admit sources, modify lifecycle
state, release, deploy, or publish anything.

### Connectors core

```bash
PYTHONPATH=packages/connectors-core/src \
  python -m pytest tests/packages/connectors_core \
  -q --strict-config --strict-markers
```

### Flora normalizers

```bash
python -m unittest discover \
  --start-directory tests/packages/domains/flora/normalizers \
  --pattern 'test_*.py' \
  --verbose
```

This suite uses repository fixtures and local command-line entry points. It
does not retrieve GBIF, USDA PLANTS, or another live source.

### Envelope helpers

```bash
python -m pytest -q tests/packages/envelopes
```

### Evidence resolver

```bash
make evidence-resolver
make evidence-resolver-deny
```

The Make targets run the bounded validator profile and the package tests with
the repository's no-network and deterministic-environment settings.

### Pipelines core

```bash
python -m pytest -q tests/packages/pipelines_core
```

### Schema registry

```bash
python -m pytest -q tests/packages/schema_registry
```

## Confirmed workflow bindings

Current workflow definitions directly invoke these suites:

- [Connector Gate](../../.github/workflows/connector-gate.yml) runs
  `tests/packages/connectors_core`.
- [Flora Darwin Core Normalizer](../../.github/workflows/flora-dwc-normalizer.yml)
  and [Flora Occurrence Intake Governance](../../.github/workflows/flora-occurrence-intake-governance.yml)
  run the two Flora normalizer modules.
- [Evidence Resolver](../../.github/workflows/evidence-resolver.yml) runs the
  Make profiles and the runtime-projection fixture test.
- [Schema Registry Package](../../.github/workflows/schema-registry-package.yml)
  runs `tests/packages/schema_registry`.

No direct hosted-workflow binding is claimed here for the envelope or
pipelines-core directories. A passing local command is not evidence that a
hosted check is required, current, or successful at another commit.

## Interpret results

- A pass supports only the assertions executed against the checked-out commit
  and fixtures.
- A schema-valid candidate is not an admitted source, EvidenceBundle, policy
  decision, proof, release, or published artifact.
- A fail-closed or negative fixture that is rejected as expected is a passing
  test outcome, not an operational incident.
- An import, collection, or dependency error means the suite did not establish
  its behavioral claims; do not reinterpret it as a product failure or waiver.
- Fixture-only and no-network checks do not prove live-source availability,
  runtime confinement, deployed controls, or public-interface behavior.

## Maintenance

When package tests are added, moved, or removed:

1. update the inventory and command in this README in the same change;
2. keep test imports pointed at package code, never the reverse;
3. link a hosted workflow only when its current YAML directly invokes the
   suite; and
4. preserve the distinction between test evidence and review, merge, release,
   deployment, promotion, or publication authority.
