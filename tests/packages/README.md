<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-packages-readme
title: tests/packages/ — Shared Package Test Index
type: README
version: v0.2
status: draft; repository-grounded; six-suite-inventory; mixed-workflow-binding; deterministic-by-suite; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; package, QA, security, domain, CI, and release stewardship remain NEEDS VERIFICATION"
created: 2026-08-03
updated: 2026-08-31
policy_label: repository-facing; tests; shared-packages; fixture-backed; fail-closed; no-source-admission; non-publisher
owning_root: tests/
responsibility: executable conformance and boundary tests for selected reusable package implementations without becoming package, contract, schema, policy, evidence, lifecycle, release, deployment, or publication authority
truth_posture: CONFIRMED six test suites, 24 test modules, 183 source-defined test functions or methods, five directly bound workflow definitions, and two workflows triggered by this parent README at the pinned snapshot / UNKNOWN complete package coverage, full-lane hosted collection, required-check status, production parity, accountable stewardship, correction propagation, and operational rollback
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 5d835798e09a4dd14735779cb44206a8a3e8b2d3
evidence_prior_blob: 23b50b8b57e024407121092f97b7c520cf202dd8
direct_suite_count: 6
test_module_count: 24
source_defined_test_count: 183
direct_workflow_binding_count: 5
parent_readme_triggered_workflow_count: 2
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../packages/README.md
  - ../../.github/workflows/connector-gate.yml
  - ../../.github/workflows/flora-dwc-normalizer.yml
  - ../../.github/workflows/flora-occurrence-intake-governance.yml
  - ../../.github/workflows/evidence-resolver.yml
  - ../../.github/workflows/schema-registry-package.yml
notes:
  - "Counts describe source-defined test functions or methods at the pinned Git tree, not parametrized collection totals, coverage, supported APIs, or production behavior."
  - "Only Connector Gate and Evidence Resolver are triggered by a change limited to this parent README; the three path-filtered focused workflows exclude it."
  - "Passing package tests do not admit sources, close evidence, approve policy, release, deploy, promote, or publish."
[/KFM_META_BLOCK_V2] -->

# Package tests

`tests/packages/` contains six suites, 24 modules, and 183 source-defined tests
for executable conformance and boundary behavior in
reusable code under [`packages/`](../../packages/README.md). Production code
must not import this tree. This README is an authored navigation and execution
guide; test modules and the package implementations remain the evidence for
the behavior they exercise.

## Suite inventory

| Test path | Modules | Tests | Package surface | Confirmed coverage |
| --- | ---: | ---: | --- | --- |
| [`connectors_core/`](connectors_core/) | 8 | 40 | [`packages/connectors-core/`](../../packages/connectors-core/README.md) | Import safety, source-head and ETag distinctions, bounded retries, streaming digests, integrity mismatch, metadata allowlisting, and diagnostic redaction |
| [`domains/flora/normalizers/`](domains/flora/normalizers/) | 2 | 21 | [`packages/domains/flora/`](../../packages/domains/flora/README.md) | Fixture-only Darwin Core occurrence normalization and intake-governance decisions, including schema conformance, deterministic identity, sensitivity holds, and fail-closed inputs |
| [`envelopes/`](envelopes/) | 4 | 30 | [`packages/envelopes/`](../../packages/envelopes/README.md) | Closed finite-outcome AI receipt, runtime-response, mock-adapter, and map-context candidate helpers; deterministic output; and non-authority and precision-disclosure bounds |
| [`evidence_resolver/`](evidence_resolver/) | 6 | 46 | [`packages/evidence-resolver/`](../../packages/evidence-resolver/README.md) | Bounded evidence-reference candidate resolution, fixture adapters, result schema, runtime projection, path confinement, and negative outcomes |
| [`pipelines_core/`](pipelines_core/) | 3 | 37 | [`packages/pipelines-core/`](../../packages/pipelines-core/README.md) | Planning-only backfill windows and pipeline-resilience decisions, including retry, circuit-breaker, queue, replay, emergency-stop, and CLI projection behavior |
| [`schema_registry/`](schema_registry/) | 1 | 9 | [`packages/schema-registry/`](../../packages/schema-registry/README.md) | Local schema discovery and lookup, deterministic snapshots, duplicate and size rejection, symlink denial, and no-network CLI behavior |
| **Total** | **24** | **183** | — | Source-defined functions or methods; not collected-case or coverage evidence |

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

| Workflow | Direct suite coverage | Does this parent README trigger it? |
| --- | --- | --- |
| [Connector Gate](../../.github/workflows/connector-gate.yml) | All eight `connectors_core` modules | Yes; it runs on every pull request |
| [Flora Darwin Core Normalizer](../../.github/workflows/flora-dwc-normalizer.yml) | `test_dwc_occurrence.py` | No; its path filter names the module and related implementation inputs |
| [Flora Occurrence Intake Governance](../../.github/workflows/flora-occurrence-intake-governance.yml) | `test_intake_governance.py` | No; its path filter names the module and related implementation inputs |
| [Evidence Resolver](../../.github/workflows/evidence-resolver.yml) | The Make profiles and runtime-projection fixture test | Yes; it runs on every pull request |
| [Schema Registry Package](../../.github/workflows/schema-registry-package.yml) | The `schema_registry` module and fixture snapshot | No; its path filter covers the child suite, not this parent README |

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
