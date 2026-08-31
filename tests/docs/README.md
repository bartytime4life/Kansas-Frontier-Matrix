# `tests/docs/` — Contract Navigation Test Lane

`tests/docs/` contains executable checks for one bounded section of the
draft Contract Object Map. The lane verifies navigation, local path, and
governed-API stub parity; it does not make the map authoritative or prove
ontology completeness, lifecycle behavior, policy, release, deployment, or
publication.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-docs-readme
title: tests/docs/README.md — Contract Navigation Test Lane
type: readme; directory-readme; documentation-test-index; evidence-boundary
version: v0.1
status: draft; repository-grounded; one-executable-test-module-confirmed; 9-source-defined-tests; direct-workflow-confirmed; readme-trigger-absent
owners: "@bartytime4life — CONFIRMED CODEOWNERS review route; accountable documentation-test stewardship UNKNOWN"
created: 2026-08-31
updated: 2026-08-31
policy_label: repository-facing; tests; documentation; object-map; no-network; non-publisher
current_path: tests/docs/README.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f3db18a7f519116b06fb7dbceb61d1422dd82e4e
  source_defined_test_count: 9
  executable_test_modules: 1
  required_resource_tokens: 17
  registered_stub_routes: 3
  workflow_source_defined_test_count: 15
related:
  - ../README.md
  - ./test_contract_object_map_lifecycle.py
  - ../../contracts/OBJECT_MAP.md
  - ../../tools/validators/docs/validate_contract_object_map_lifecycle.py
  - ../../apps/governed-api/src/governed_api/routes/registry.py
  - ../../apps/governed-api/tests/test_abstain_routes.py
  - ../../apps/governed-api/tests/test_boundary_guards.py
  - ../../control_plane/object_family_register.yaml
  - ../../.github/workflows/contract-object-map-lifecycle.yml
  - ../../docs/doctrine/directory-rules.md
  - ../../.github/CODEOWNERS
notes:
  - "Counts describe source-defined tests at the pinned base commit, not a current collected-case or hosted-run receipt."
  - "The dedicated workflow collects 9 tests in this lane and 6 adjacent governed-API tests."
  - "The workflow path filters exclude tests/docs/README.md at the pinned base commit."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

## Purpose and scope

This README helps maintainers find, run, and interpret
[`test_contract_object_map_lifecycle.py`](test_contract_object_map_lifecycle.py)
without mistaking a passing navigation check for semantic or operational
authority.

The test targets the marked resource-lifecycle overlay in the draft
[`contracts/OBJECT_MAP.md`](../../contracts/OBJECT_MAP.md). That map describes
itself as a non-authoritative, evidence-limited crosswalk. Contract Markdown
continues to define meaning; schemas define machine shape; policy defines
admissibility; and tests and validators provide bounded enforcement evidence.

The overlay retains a historical repository evidence pin. The validator does
not freeze current execution to that pin: when run from a checkout, it checks
the supplied Object Map, current local paths, and the current governed-API
route registry. Keep historical map claims separate from current-head
validation results.

## Current inventory

| Test module | Tests | System under test | Primary subject |
|---|---:|---|---|
| [`test_contract_object_map_lifecycle.py`](test_contract_object_map_lifecycle.py) | 9 | [`validate_contract_object_map_lifecycle.py`](../../tools/validators/docs/validate_contract_object_map_lifecycle.py) | The marked lifecycle/API overlay in [`contracts/OBJECT_MAP.md`](../../contracts/OBJECT_MAP.md) |

The count is a static inventory of source functions named `test_*` at the
pinned base. It does not prove current collection, a passing result, coverage,
mutation resistance, required-check status, or production parity.

## Tested behavior

| Assertion | Bounded evidence |
|---|---|
| Current map passes | The marked overlay satisfies the validator at the tested checkout |
| Required tokens are present | All 17 validator-declared resource family names occur in the overlay |
| Missing path fails closed | A synthetic broken `SourceDescriptor` path produces `PATH_NOT_FOUND` |
| Route inventory drift fails closed | Replacing `/layers` with `/layerz` produces `ROUTE_INVENTORY_MISMATCH` |
| Missing marker fails closed | Removing the start marker produces only `SECTION_MARKER_INVALID` |
| Non-abstaining handler fails closed | A synthetic `GRANT` route response produces `ROUTE_NOT_ABSTAIN` |
| Runtime envelope compatibility remains bounded | An `{"outcome": "ABSTAIN"}` response does not require a separate `decision` field |
| CLI output is deterministic | Two subprocess runs have identical output containing `"outcome":"PASS"` |
| Forbidden client imports are absent | Exact source markers for common network and subprocess imports are not present |

The last check is a narrow source-marker guard, not an AST audit, runtime
network sandbox, process sandbox, or repository-wide import policy.

## Run the lane

From the repository root, install the dependency profile used by the dedicated
workflow:

```bash
python tools/ci/install_python_ci.py project-test
```

Run the nine direct tests:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 KFM_NO_NETWORK=1 \
  PYTHONPATH=apps/governed-api/src \
  python -m pytest -q \
    tests/docs/test_contract_object_map_lifecycle.py \
    --strict-config --strict-markers
```

Run the validator directly:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 KFM_NO_NETWORK=1 \
  PYTHONPATH=apps/governed-api/src \
  python tools/validators/docs/validate_contract_object_map_lifecycle.py \
    contracts/OBJECT_MAP.md \
    --repo-root .
```

The validator prints compact JSON and exits nonzero when findings exist. A
`PASS` outcome covers only its declared
`contract-object-map-lifecycle-navigation-and-stub-parity-only` scope.

## Dedicated workflow binding

[`contract-object-map-lifecycle.yml`](../../.github/workflows/contract-object-map-lifecycle.yml)
defines the hosted lane. Its primary pytest command collects:

- the nine tests documented here;
- one source-defined test in
  [`test_abstain_routes.py`](../../apps/governed-api/tests/test_abstain_routes.py);
  and
- five source-defined tests in
  [`test_boundary_guards.py`](../../apps/governed-api/tests/test_boundary_guards.py).

The resulting static command inventory is 15 tests. Actual collection may
differ if parametrization, import, dependency, or configuration behavior
changes.

The workflow also:

1. compiles the validator and direct test module;
2. runs the validator CLI against the Object Map;
3. validates the adjacent
   [Object Family Register](../../control_plane/object_family_register.yaml);
4. checks required metadata on the Object Map and exploratory source map; and
5. validates the stored generated authoring receipt.

The workflow definition establishes execution intent, not a current run,
required-check rule, or approval. Its pull-request path filters include the
test, validator, map, routes, related contracts and schemas, and receipt, but
exclude `tests/docs/README.md`. A documentation-only change here therefore
does not trigger this focused workflow.

## Current route and resource boundary

At the pinned base, the
[`ROUTES` registry](../../apps/governed-api/src/governed_api/routes/registry.py)
contains `/bootstrap`, `/evidence`, and `/layers`. The validator requires
the overlay route table to match that set and each invoked handler to return a
mapping whose `outcome` is `ABSTAIN`.

The required resource-token set contains:

- source and intake carriers;
- claim, evidence, catalog, layer, and tile carriers;
- runtime and decision envelopes;
- AI, review, and policy records;
- release, correction, rollback, and UI projection carriers.

Token presence proves only that the selected family name appears in the marked
overlay. Path validation proves only that referenced paths currently resolve
inside the repository. Neither check proves semantic correctness, complete
family registration, a schema-to-contract match, an emitted instance, a live
resolver, or public availability.

## Evidence and authority boundary

| A passing lane supports | It does not establish |
|---|---|
| One marked section has exactly one ordered marker pair | The whole Object Map is complete or canonical authority |
| All validator-required family tokens are present | Every contract family is represented or mature |
| Backtick paths in the section resolve locally | Linked documents, schemas, or code are semantically correct |
| Documented and registered route sets match | Authentication, authorization, deployment, availability, or API stability |
| Invoked handlers return `ABSTAIN` | Evidence resolution, policy evaluation, source admission, or release lookup |
| CLI output is deterministic for the checked revision | Production parity or operational monitoring |
| A workflow definition names the tests | A hosted pass, required check, human review, merge, or release |

The default lifecycle remains
`RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`.
The Object Map and this lane describe relationships around that lifecycle;
they do not move data, resolve evidence, create policy decisions, approve
review, issue releases, deploy services, or publish artifacts. Public clients
must continue to use governed interfaces or released public-safe artifacts.

## Failure interpretation

| Failure | First inspect | Do not infer automatically |
|---|---|---|
| Marker failure | Marker count, order, and accidental duplication | A contract meaning changed |
| Missing resource token | Validator set and marked resource table | The resource family was abolished |
| Missing or invalid path | Relative path spelling, moves, aliases, and repository root | The referenced artifact is semantically invalid |
| Route inventory mismatch | Object Map route table and current `ROUTES` keys | A new route is authorized for public use |
| Route handler failure | Import path, handler exception, and finite-envelope shape | Evidence or policy denied a real request |
| `ROUTE_NOT_ABSTAIN` | Handler output and stub boundary | A non-abstaining behavior is approved |
| CLI output drift | Finding ordering, serialization, path display, and environment | Publication or deployment failed |
| Receipt validation failure | Stored artifact hashes and changed receipt-bound paths | This test module necessarily failed |
| Focused workflow absent | Changed paths and workflow filters | The lane passed |

Report the exact revision, command, and finding codes. Keep a test failure
separate from evidence correction, policy review, merge, promotion, release,
deployment, publication, and operational rollback.

## Maintenance

Update this README in the same reviewable change when any of the following
changes materially:

- module or source-defined test inventory;
- overlay markers, required resource tokens, path grammar, or size limit;
- route registry, finite response envelope, or adjacent API test command;
- local invocation, Python version, or dependency profile;
- workflow command, path filters, metadata checks, or receipt binding;
- Object Map status, authority wording, or evidence pin; or
- lifecycle, evidence, policy, rights, sensitivity, privacy, release,
  deployment, publication, or public-client posture.

Keep executable documentation conformance under `tests/`, reusable validator
logic under `tools/validators/docs/`, semantic maps under their owning
contract root, and executable routes under their application root while those
placements match the accepted
[Directory Rules](../../docs/doctrine/directory-rules.md). Current
[`CODEOWNERS`](../../.github/CODEOWNERS) confirms a review route; it does not
prove review or independent stewardship.

## Known gaps

- The focused workflow does not trigger for this README.
- No Make target names or aggregates this lane.
- Required-check status and accountable documentation-test stewardship are
  unknown.
- Source counts are not a dependency-complete collection or execution receipt.
- The Object Map remains draft, evidence-limited, and explicitly incomplete.
- The stored authoring receipt is process memory, not current hosted evidence
  or release proof.
- Complete contract/schema/fixture/policy coverage, live resolvers,
  authentication, authorization, production behavior, correction propagation,
  and operational rollback remain unverified.

## Documentation correction and rollback

This new index changes documentation only. Before merge, close the draft pull
request or remove this file from its feature branch. After an authorized merge,
revert the documentation commit or submit a forward correction pinned to
current repository evidence.

Removing this README does not roll back a contract, schema, route, lifecycle
object, release, deployment, promotion, or publication. Those require their
own governed correction paths.

[Back to top](#top)
