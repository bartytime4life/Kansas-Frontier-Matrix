<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-contracts-readme
title: tests/contracts/README.md — Contract Test Lane
type: README
version: v0.3
status: draft; repository-grounded; direct-executable-suite
owners: OWNER_TBD — QA steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Runtime steward · Release steward · Security steward · Domain stewards · Docs steward
created: 2026-01-06
updated: 2026-08-31
supersedes: v0.2
policy_label: public-doctrine; tests; contracts; bounded-enforceability; fail-closed; no-contract-authority; no-schema-authority; no-policy-authority; no-release-authority
owning_root: tests/
responsibility: bounded inventory, execution, and interpretation guidance for repository-owned contract tests without authoring contract meaning or granting policy, review, lifecycle, release, deployment, promotion, or publication authority
current_path: tests/contracts/README.md
truth_posture: CONFIRMED four direct executable modules, fifteen test functions or methods, manifest-driven validation for three fixture families, Makefile collection of tests/schemas and tests/contracts, and direct contracts-validate workflow binding / UNKNOWN complete semantic coverage for every contract document, promotion-gate dependency, and accepted accountable owners
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_visibility: public
evidence_base_ref: main
evidence_base_commit: d1f7ed51cf4d9c9c2fdf94cdc81644744ae464ce
evidence_target_prior_blob: 41027c98f62cadb894f7fdd50da67a72fe27c245
direct_test_module_count: 4
related:
  - ../README.md
  - ./manifests/README.md
  - ../../contracts/README.md
  - ../../contracts/OBJECT_MAP.md
  - ../../schemas/contracts/v1/
  - ../../fixtures/contracts/
  - ../../tools/validators/validate_contract_fixture_manifest.py
  - ../../tests/schemas/test_common_contracts.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../../.github/workflows/contracts-validate.yml
notes:
  - "v0.3 replaces the obsolete README-only posture with the current executable inventory and workflow boundary."
  - "Direct tests cover four bounded invariant groups; they are not complete semantic validation of every contract."
  - "Passing tests do not create contract, schema, policy, evidence, review, lifecycle, release, deployment, promotion, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Contract test lane

> Repository-owned tests for bounded contract, schema, fixture, projection, and
> wiring invariants. This lane proves the assertions implemented by its test
> modules; it does not define contract meaning or grant policy, review, release,
> or publication authority.

<a id="top"></a>

## Purpose and authority

`tests/contracts/` is an executable test lane under the canonical `tests/`
responsibility root. Its tests inspect current repository contracts, schemas,
fixtures, validators, and declared links. They may reject drift in those
relationships, but they must not silently redefine the relationships they test.

| Responsibility | Authority home | Role here |
|---|---|---|
| Semantic meaning and exclusions | [`contracts/`](../../contracts/README.md) | Assert selected documented invariants without copying canonical prose. |
| Machine shape | [`schemas/contracts/v1/`](../../schemas/contracts/v1/) | Inspect declared fields, references, and metadata; do not author schemas in tests. |
| Reusable fixtures | [`fixtures/contracts/`](../../fixtures/contracts/) | Consume deterministic valid and invalid cases without creating a second fixture authority. |
| Validator behavior | [`tools/validators/`](../../tools/validators/) | Exercise repository validators; keep reusable logic out of test modules. |
| Contract enforceability evidence | `tests/contracts/` | Own the bounded assertions inventoried below. |
| Policy, evidence, lifecycle, and release decisions | Their governed roots and accountable reviewers | Remain outside this lane. |

A passing test is evidence only for the checked-out revision and the assertions
that executed. It does not prove that every Markdown contract is semantically
complete, that evidence is sufficient, that policy permits use, or that an
artifact is reviewed, released, deployed, promoted, or published.

## Current inventory

Current `main` contains four direct test modules with 15 test functions or
methods, plus the manifest inventory under
[`manifests/`](manifests/README.md).

| Test module | Executable assertions | Confirmed boundary |
|---|---:|---|
| [`test_contract_fixture_manifest.py`](test_contract_fixture_manifest.py) | 8 `unittest` methods | Validates the three-family manifest, deterministic reporting, exact invalid-manifest failures, schema polarity, required invalid lanes, no-network behavior, CLI exit codes, and non-echoing output. |
| [`test_evidence_bundle_projection_aggregate.py`](test_evidence_bundle_projection_aggregate.py) | 2 `unittest` methods | Requires declared domain EvidenceBundle projections to delegate to the canonical schema without independent schema semantics and to name an existing validator. |
| [`test_identity_token_wiring.py`](test_identity_token_wiring.py) | 4 pytest functions | Checks declared IdentityToken surfaces, non-vacuous JSON fixture lanes, the finite kind vocabulary, and validator references to the declared schema and fixtures. |
| [`test_runtime_response_contract_alignment.py`](test_runtime_response_contract_alignment.py) | 1 pytest function | Checks RuntimeResponseEnvelope schema metadata, contract/precision cross-links, documented schema fields, and documented `ANSWER` versus non-answer precision rules. |

The empty `__init__.py` makes the lane importable; it is not a test or a
validation result.

## Manifest-driven fixture wave

[`contract_fixture_families.v1.json`](manifests/contract_fixture_families.v1.json)
declares a bounded first wave:

| Family | Schema | Canonical fixture root |
|---|---|---|
| `decision-envelope` | [`decision_envelope.schema.json`](../../schemas/contracts/v1/runtime/decision_envelope.schema.json) | [`decision_envelope/`](../../fixtures/contracts/v1/runtime/decision_envelope/) |
| `evidence-bundle` | [`evidence_bundle.schema.json`](../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | [`evidence_bundle/`](../../fixtures/contracts/v1/evidence/evidence_bundle/) |
| `runtime-response-envelope` | [`runtime_response_envelope.schema.json`](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | [`runtime_response_envelope/`](../../fixtures/contracts/v1/runtime/runtime_response_envelope/) |

The validator requires safe repository-relative paths, unique ordered families,
nonempty valid and invalid lanes, loadable Draft 2020-12 schemas, and expected
fixture polarity. Exact negative manifests cover duplicate family identity,
empty inventory, and path escape. Other failure cases use temporary synthetic
repositories.

This wave is an inventory, not a complete list of KFM contract families. A
green result proves path presence and the evaluated schema/fixture polarity
only; it does not prove semantic truth, evidence closure, or release fitness.

## Run the lane

From the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m pytest -q tests/contracts
```

Run only the manifest validator and its focused tests:

```bash
python tools/validators/validate_contract_fixture_manifest.py \
  tests/contracts/manifests/contract_fixture_families.v1.json \
  --format text

KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover \
    --start-directory tests/contracts \
    --pattern 'test_contract_fixture_manifest.py' \
    --verbose
```

The root [`Makefile`](../../Makefile) defines:

```make
test:
	python -m pytest tests/schemas tests/contracts -q
```

`make test` is broader than the direct lane. It also runs companion schema and
fixture tests, including the dynamically parameterized families in
[`tests/schemas/test_common_contracts.py`](../schemas/test_common_contracts.py).
Do not attribute that companion coverage to a direct module above.

Do not append `|| true`, suppress collection failures, or treat a zero-test run
as success.

## Hosted workflow binding

[`contracts-validate.yml`](../../.github/workflows/contracts-validate.yml) runs
on pull requests, pushes to `main`, and manual dispatch. It:

1. installs the repository test dependencies;
2. runs the manifest validator directly; and
3. runs `make test`, which collects `tests/schemas` and `tests/contracts`.

The workflow has no path filter, so a pull request run is not evidence that all
changed paths are contract-related. Its name and green state do not establish
branch-protection status, promotion dependency, semantic completeness, or
authority beyond the commands that ran.

## Fixture and execution safety

- Keep fixtures synthetic, deterministic, public-safe, and free of credentials,
  private records, live source payloads, and harmful precision.
- Preserve no-network behavior for the default lane.
- Keep discovery bounded, symlink-safe, and repository-relative.
- Do not write to canonical data, evidence, proof, receipt, policy, release, or
  published roots.
- Do not echo fixture values in failure reports when stable codes and paths are
  sufficient.
- Treat schema or fixture polarity changes as reviewed contract/schema work,
  not as a manifest-only repair.

## Interpret failures

| Failure area | First investigation |
|---|---|
| Manifest shape or path safety | Check required fields, ordering, uniqueness, path prefixes, traversal, symlinks, and size/complexity bounds. |
| Fixture polarity | Check the canonical schema and valid/invalid lane intent before changing an expected result. |
| Projection delegation | Check the canonical EvidenceBundle reference, projection metadata, forbidden independent keywords, and declared validator path. |
| IdentityToken wiring | Check schema metadata, fixture presence, kind vocabulary, and validator targets together. |
| Runtime response alignment | Reconcile schema properties, both contract documents, precision rules, and cross-links without choosing a new semantic rule in the test. |
| Hosted workflow only | Compare the exact workflow command, dependency installation, checked-out SHA, and pytest collection with the focused local command. |

Do not weaken a fail-closed assertion merely to make a workflow pass. When a
canonical contract intentionally changes, update its directly affected schema,
fixture, validator, test, and documentation surfaces in an independently
reviewable boundary.

## Maintenance and open gaps

- Update the direct inventory when a module or test count changes.
- Keep manifest family identifiers unique and alphabetically ordered.
- Link every new assertion to its canonical contract, schema, fixture, or
  validator surface.
- Separate direct `tests/contracts` coverage from companion schema, policy,
  release, runtime, API, UI, and domain tests.
- Record missing or conflicting authority as `UNKNOWN` or
  `NEEDS VERIFICATION`; do not fill gaps with generated prose.

Still unresolved:

- complete semantic coverage across every document under `contracts/`;
- accepted accountable owner identities;
- whether `contracts-validate` is a required promotion check;
- the exhaustive contract-to-schema, policy, consumer, correction, and release
  crosswalk;
- operational evidence, correction, rollback, and public read-back.

<p align="right"><a href="#top">Back to top</a></p>
