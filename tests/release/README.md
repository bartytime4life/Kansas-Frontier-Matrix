<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-release-readme
title: tests/release/ — Release-Prerequisite Test Inventory and Authority Boundary
type: readme; directory-readme; release-test-boundary; executable-inventory
version: v1.2
status: repository-grounded; executable; mixed-dependency; no-release-authority
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent QA, release, and separation-of-duties stewardship remain NEEDS VERIFICATION"
created: 2026-07-06
updated: 2026-08-30
supersedes: v1.1 documentation at the same path; no test, fixture, validator, workflow, release object, or public surface is superseded
policy_label: public-doc; tests; release-prerequisites; promotion-safety; synthetic; fail-closed; non-authoritative
current_path: tests/release/README.md
truth_posture: CONFIRMED fifteen direct modules and 124 source-defined tests at the pinned snapshot / PARTIAL aggregate local execution and cross-family coverage / UNKNOWN required-check status, complete collection count, and independent stewardship
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: db23a8bfa9fa126e87009a41240576619ccaac02
  target_prior_blob: 8e4e14eb35dcd2026b7bf0de37ec9751f75a710d
  direct_modules: 15
  source_defined_tests: 124
  count_note: source-defined test functions or methods; parametrization and collection behavior may change collected-case totals
related:
  - ../README.md
  - ../../release/README.md
  - ../../contracts/release/README.md
  - ../../schemas/contracts/v1/release/README.md
  - ../../fixtures/release/README.md
  - ../../tools/release/README.md
  - ../../tools/validators/release/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../Makefile
  - ../../pyproject.toml
tags: [kfm, tests, release, promotion, rollback, publication-deny, compatibility, no-network, fail-closed]
notes:
  - "v1.2 replaces a stale three-module thin-slice inventory and proposed future tree with the complete direct current-main inventory."
  - "Every direct module has a workflow binding, but the workflows use different dependency sets and commands; no single canonical full-lane target is established."
  - "Passing tests and workflows are bounded evidence only and never approve review, promotion, release, deployment, publication, correction, withdrawal, or rollback."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/release/` — Release-Prerequisite Test Inventory and Authority Boundary

`tests/release/` contains executable checks for bounded release prerequisites,
negative publication behavior, compatibility assessments, review projections,
promotion verification, and synthetic rollback behavior. It does not create or
approve a release.

> [!IMPORTANT]
> A green test or workflow supports only its named assertions at the checked
> revision. It does not establish source truth, evidence sufficiency, policy
> approval, human review, promotion, release, deployment, publication, or
> successful operational rollback.

## Status

At `main@db23a8bfa9fa126e87009a41240576619ccaac02`, this directory has
15 direct `test_*.py` modules containing 124 source-defined `test_*` functions
or methods. The prior README described three direct modules and a proposed
future tree, so it materially understated current implementation.

The count is a source inventory, not a pytest collection result. Parametrized
tests can produce more collected cases, and dependency or discovery behavior
can prevent collection.

| Property | Confirmed boundary |
|---|---|
| Placement | Canonical executable conformance evidence under `tests/` |
| Direct inventory | 15 modules; 124 source-defined tests |
| Runners | Mix of pytest-compatible `unittest` and pytest functions |
| Inputs | Repository-owned synthetic fixtures, schemas, validators, helpers, and temporary files |
| Network posture | Bounded tests and workflows deny or avoid network use; no universal lane-wide network guard is proven |
| Side effects | Tests use temporary paths or read-only fixtures; some probe workflows build synthetic carriers in controlled environments |
| Aggregate command | No canonical dependency-complete full-lane target is established |
| Review route | `/tests/` routes to `@bartytime4life` through CODEOWNERS |
| Authority | Test evidence only; never a release, review, policy, or publication decision |

## Authority and placement

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
makes the [Directory Rules](../../docs/doctrine/directory-rules.md) the writable
human placement authority. Those rules assign executable conformance,
boundary, negative, integration, and end-to-end evidence to `tests/`. This
same-path README update does not create a new authority root or move an
artifact.

| Responsibility | Authority home | Role of this lane |
|---|---|---|
| Release records and state | [`release/`](../../release/README.md) | Exercise prerequisites and denial paths; never create state |
| Semantic meaning | [`contracts/release/`](../../contracts/release/README.md) | Assert bounded invariants; never redefine them |
| Machine shape | [`schemas/contracts/v1/release/`](../../schemas/contracts/v1/release/README.md) | Validate selected profiles; never select schema authority |
| Reusable synthetic examples | [`fixtures/release/`](../../fixtures/release/README.md) and `fixtures/contracts/v1/release/` | Consume reviewed inputs; never become fixture authority |
| Release helpers | [`tools/release/`](../../tools/release/README.md) | Exercise deterministic behavior and non-effects |
| Release validators | [`tools/validators/release/`](../../tools/validators/release/README.md) and specialized validator paths | Test diagnostics, polarity, and fail-closed behavior |
| Executable evidence | `tests/release/` | This lane |

Promotion, review, merge, release, deployment, publication, correction,
withdrawal, supersession, and rollback are distinct states. Test naming,
fixture validity, workflow success, or a generated report does not collapse
those distinctions.

## Direct module inventory

| Module | Source-defined tests | Implemented boundary |
|---|---:|---|
| [`test_cosign_attestation_verification_plan.py`](test_cosign_attestation_verification_plan.py) | 10 | Draft 2020-12 schema, valid/invalid fixture polarity, unsafe JSON and path rejection, deterministic CLI output, and absence of network or Cosign execution |
| [`test_geoparquet_2_rc_compatibility_assessment.py`](test_geoparquet_2_rc_compatibility_assessment.py) | 10 | Exact synthetic toolchain matrix, finite `READY`/`HOLD`/`ERROR` assessment, evidence-ref uniqueness, and non-governance boundary |
| [`test_geoparquet_2_rc_gdal_consumer_probe.py`](test_geoparquet_2_rc_gdal_consumer_probe.py) | 8 | Synthetic GDAL-probe result classification, carrier and image integrity, semantic comparison, and refusal of interoperability or governance claims |
| [`test_geoparquet_2_rc_pyarrow_carriers.py`](test_geoparquet_2_rc_pyarrow_carriers.py) | 6 | Synthetic PyArrow carrier generation, digest and CRS checks, malformed-carrier rejection, partial outcome, and governance-claim denial |
| [`test_geospatial_carrier_readiness.py`](test_geospatial_carrier_readiness.py) | 14 | Closed schema, finite carrier-readiness cases, MVT/COG/GeoParquet profile rules, deterministic case CLI, and no-network validation |
| [`test_promotion_decision_schema.py`](test_promotion_decision_schema.py) | 1 | PromotionDecision fixture validation through the release validator |
| [`test_promotion_gate.py`](test_promotion_gate.py) | 19 | Bounded A–G candidate readiness, outcome precedence, review separation, temporal/identity checks, safe diagnostics, no-network behavior, and finite CLI exits |
| [`test_promotion_receipt.py`](test_promotion_receipt.py) | 6 | Receipt schema metadata, gate ordering, positive/negative fixtures, fail-closed status precedence, deterministic CLI, and no network/process client imports |
| [`test_promotion_verification_execution.py`](test_promotion_verification_execution.py) | 5 | Synthetic verification execution, subject/spec/tool binding, result-schema validation, and explicit non-authorization of promotion |
| [`test_publication_deny_dry_run.py`](test_publication_deny_dry_run.py) | 4 | Five required negative publication paths, deterministic no-network report, no file emission, and no authority or assembly claim |
| [`test_review_record.py`](test_review_record.py) | 11 | Synthetic ReviewRecord fixture polarity, identity/time/separation rules, supersession and expiry boundaries, safe diagnostics, and non-emission of governed state |
| [`test_signed_bundle_timestamp_evidence.py`](test_signed_bundle_timestamp_evidence.py) | 7 | Closed timestamp-evidence schema, finite fixture outcomes, public identity replay, unsafe-input rejection, deterministic CLI, and no cryptographic or network effect |
| [`test_synthetic_rollback_rehearsal.py`](test_synthetic_rollback_rehearsal.py) | 8 | Deterministic plan mode, synthetic alias switch or withdrawal, history preservation, invalidation completeness, digest/target checks, and denial of non-synthetic input |
| [`test_tile_delivery_strategy_assessment.py`](test_tile_delivery_strategy_assessment.py) | 11 | Closed schema, 20-case finite strategy matrix, public-safety and mediation checks, identity binding, deterministic no-network replay, and non-effect claims |
| [`test_trust_projection_manifest.py`](test_trust_projection_manifest.py) | 4 | Valid/invalid trust projection types, digest-equality meaning, read-only review packets, expiry, and denial of approval authority |

### What the inventory proves

The inventory proves that these files and assertions exist at the pinned
revision. It does not prove complete semantic coverage, a complete fixture
crosswalk, dependency-complete local collection, required-check status, or
production parity.

## Execution

Install the repository test extra before running Python tests:

```bash
python -m pip install -e '.[test]'
```

The following repository targets are confirmed:

```bash
# ReviewRecord and promotion-gate fixtures and tests.
make publish-check

# Five synthetic publication-denial paths and their focused test module.
make release-dry-run
```

Focused modules can be run with the runner used by their workflow, for example:

```bash
python -m pytest -q tests/release/test_geospatial_carrier_readiness.py
python -m unittest -q tests.release.test_promotion_receipt
python -m pytest -q tests/release/test_tile_delivery_strategy_assessment.py
```

For inventory or collection investigation, pytest can target the directory:

```bash
python -m pytest -q tests/release
```

That directory command is not a canonical full-lane target. Several carrier
and execution modules have additional pinned dependencies or synthetic tool
setup in their dedicated workflows. Use the matching workflow definition as
the environment contract before interpreting a local import or collection
failure as an assertion failure.

`make test` does not run this directory. It is limited to `tests/schemas` and
`tests/contracts`.

## Workflow bindings

Every direct module is named by at least one current workflow definition.
Bindings are still bounded: a path filter can skip a workflow, a command can
name only selected modules, and a workflow definition does not prove required
branch protection.

| Workflow | Direct release modules named by its current definition |
|---|---|
| [`cosign-attestation-verification-plan.yml`](../../.github/workflows/cosign-attestation-verification-plan.yml) | Cosign verification plan |
| [`geoparquet-2-rc-compatibility-assessment.yml`](../../.github/workflows/geoparquet-2-rc-compatibility-assessment.yml) | GeoParquet compatibility assessment |
| [`geoparquet-2-rc-gdal-consumer-probe.yml`](../../.github/workflows/geoparquet-2-rc-gdal-consumer-probe.yml) | PyArrow carriers and GDAL consumer probe |
| [`geoparquet-2-rc-pyarrow-carrier-probe.yml`](../../.github/workflows/geoparquet-2-rc-pyarrow-carrier-probe.yml) | PyArrow carriers |
| [`geospatial-carrier-readiness.yml`](../../.github/workflows/geospatial-carrier-readiness.yml) | Geospatial carrier readiness |
| [`promotion-gate.yml`](../../.github/workflows/promotion-gate.yml) | PromotionDecision shape, promotion gate, and ReviewRecord |
| [`promotion-receipt.yml`](../../.github/workflows/promotion-receipt.yml) | Promotion receipt |
| [`promotion-verification-execution.yml`](../../.github/workflows/promotion-verification-execution.yml) | Verification execution, Cosign plan, and promotion gate |
| [`release-dry-run.yml`](../../.github/workflows/release-dry-run.yml) | Publication deny, PromotionDecision shape, promotion gate, ReviewRecord, and synthetic rollback references |
| [`rollback-drill.yml`](../../.github/workflows/rollback-drill.yml) | Synthetic rollback rehearsal |
| [`signed-bundle-timestamp-evidence.yml`](../../.github/workflows/signed-bundle-timestamp-evidence.yml) | Signed-bundle timestamp evidence |
| [`tile-delivery-strategy-assessment.yml`](../../.github/workflows/tile-delivery-strategy-assessment.yml) | Tile-delivery strategy assessment |
| [`source-and-trust-projection-profiles.yml`](../../.github/workflows/source-and-trust-projection-profiles.yml) | Trust projection manifest |

## Inputs, outputs, and side effects

### Inputs

Depending on the module, tests read:

- versioned schemas and semantic contracts;
- synthetic valid, invalid, hold, deny, partial, and error fixtures;
- validator or release-helper source;
- pinned compatibility and toolchain declarations;
- temporary files created inside the test process;
- controlled fake executables or generated synthetic carriers in dedicated
  probe workflows.

### Outputs

Normal test output is runner status and diagnostics. Temporary carriers,
packets, aliases, and reports are test evidence only and must remain isolated
from governed release and public artifact stores.

The tests do not create a PromotionDecision, ReleaseManifest, ReviewRecord,
PromotionReceipt, release approval, deployment, publication, correction,
withdrawal, or operational rollback by passing.

### Safety boundary

- Keep committed fixtures synthetic and public-safe.
- Do not place credentials, private keys, real reviewer identities, restricted
  payloads, or harmful-precision locations in tests or logs.
- Preserve no-network and safe-diagnostic assertions when validators change.
- A probe that invokes a tool in a controlled workflow must not gain ambient
  credentials, writable production mounts, or publication side effects.
- Treat missing rights, sensitivity, sovereignty, provenance, review, or
  rollback support as a hold, deny, abstention, or explicit unknown according
  to the tested contract; never infer permission from test success.

## Failure interpretation

| Failure class | First check | Safe conclusion |
|---|---|---|
| Import or collection failure | Compare the module's dedicated workflow dependencies and command | The test did not establish an assertion result |
| Schema or fixture polarity failure | Schema version, fixture family, expected findings, and validator change | The bounded profile drifted or the test/fixture is stale |
| Integrity or identity failure | Digest, subject, tool pin, timestamp, and stable-ID inputs | Required binding is absent or mismatched for this case |
| Network, unsafe path, or diagnostic leak | Validator/helper effect surface and redaction behavior | Fail closed; do not retry with broader access or expose input values |
| Review or promotion-gate failure | Evidence, identity, time, separation, obligations, and rollback context | Candidate remains unapproved; tests cannot self-approve |
| Publication-deny failure | Negative case inventory and report non-effects | Potential boundary regression; never downgrade to a warning |
| Rollback rehearsal failure | Synthetic marker, target, digest, invalidations, alias, and history | Reversal evidence is incomplete; no operational rollback conclusion is valid |
| Workflow skipped by paths | Workflow trigger and changed paths | No exact-head execution evidence for that workflow |
| Infrastructure error | Install/tooling logs and base-versus-head attribution | No release-prerequisite conclusion is valid |

Do not change implementation, schema, fixture, policy, workflow, or release
state merely to make this README or a green check appear consistent. Repair the
owning artifact in a separately scoped, reviewed change.

## Maintenance

Update this README when a direct module is added, removed, renamed, or split;
when its source-defined count changes materially; or when a Make target,
workflow binding, dependency, fixture family, authority limit, or side-effect
posture changes.

For a test or fixture change:

1. identify the owning contract, schema, validator, helper, and workflow;
2. preserve positive and negative polarity and finite outcomes;
3. verify deterministic replay and safe diagnostics;
4. review rights, sensitivity, sovereignty, privacy, and harmful precision;
5. run the narrow module in its declared dependency environment;
6. update workflow and fixture links without duplicating authority;
7. record unresolved collection, required-check, ownership, or production
   questions as `UNKNOWN` or `NEEDS VERIFICATION`.

## Open verification register

| Question | Status |
|---|---|
| What is the exact pytest collected-case count for the complete lane in one dependency-complete environment? | `UNKNOWN` |
| Is there an accepted canonical target that composes all 15 modules and their extra dependencies? | `NOT ESTABLISHED` |
| Are all named workflows required checks for protected branches or release review? | `UNKNOWN` |
| Do README-only changes trigger each path-filtered dedicated workflow? | `NO` for definitions whose filters omit this path; check exact workflow evidence before claiming execution |
| Is the current no-network posture universal across every runner and imported helper? | `PARTIAL / NEEDS VERIFICATION` |
| Do the modules cover every accepted release contract, schema, policy, correction, withdrawal, and public consumer? | `NOT ESTABLISHED` |
| Who provides accountable independent QA, release, security, sensitivity, and separation-of-duties review? | `NEEDS VERIFICATION`; CODEOWNERS supplies routing only |
| Have rollback, deployment, release, publication, or public-state correction been exercised operationally? | `UNKNOWN`; synthetic tests do not prove them |

## Evidence used

This inventory was reconciled against the complete prior README, all 15 direct
test modules, their named validators and helpers, the 13 directly relevant
workflow definitions, the Makefile, `pyproject.toml`, CODEOWNERS, the tests-root
README, accepted ADR-0029, and the adopted Directory Rules at the pinned
commit.

Connected Drive reliability guidance and the Notion Repository Workbench were
consulted read-only for exact-SHA, failure-attribution, and active-work
coordination lineage. They were not treated as implementation, adoption, or
repository authority, and no external prose was imported.

## Documentation rollback

Before merge, close the draft pull request or restore the prior blob on the
feature branch. After merge, revert the documentation commit or make a focused
forward correction. Do not rewrite shared history.

Rolling back this README changes no test, fixture, validator, workflow,
release, deployment, promotion, publication, correction, withdrawal, or
operational rollback state.

[Back to top](#top)
