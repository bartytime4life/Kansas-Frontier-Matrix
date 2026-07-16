<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/src-kfm-readme
title: src/kfm/ — Root Distribution Namespace and Unratified Facade Boundary
type: readme; package-readme; root-distribution-namespace; packaging-boundary; compatibility-facade-index
version: v0.2
status: draft; repository-grounded; hatch-packaged; namespace-minimal; facade-unratified; public-api-unestablished; tests-unproved; non-authoritative
owners: OWNER_TBD — Architecture steward · Package steward · Python packaging steward · Developer tooling steward · Validation steward · CI steward · Release steward · Docs steward
created: NEEDS VERIFICATION — empty README was replaced by v0.1 on 2026-07-04
updated: 2026-07-16
supersedes: v0.1 root package marker guide
policy_label: "public-doctrine; python; packaging; root-distribution; src-layout; minimal-namespace; import-safe; no-side-effects; no-parallel-implementation-authority; no-hidden-facade; no-public-api-claim; no-runtime-authority; no-lifecycle-authority; no-release-authority; migration-required; rollback-aware"
current_path: src/kfm/README.md
truth_posture: >
  CONFIRMED target v0.1 README, root pyproject Hatch configuration, distribution name kfm version 0.0.0,
  Python >=3.11 declaration, jsonschema dependency, pytest test extra, wheel selection src/kfm,
  minimal src/kfm/__init__.py docstring, root src README, packages responsibility-root README,
  root Makefile schema/test targets, schema-validation workflow editable-installing the root project,
  separate kfm-cli distribution metadata, Directory Rules implementation roots, and bounded absence
  of selected entry-point/API/typing/test files and executable consumers / PROPOSED explicit root-distribution
  role, import-safe marker contract, facade admission, dependency direction, package tests, CI, migration,
  correction, deprecation, and rollback / CONFLICTED prior README claims that packaging metadata was unverified;
  root src compatibility posture versus an actual Hatch-built distribution; root dependency-carrier role versus
  packages/ as shared-library authority; root distribution kfm versus app distribution kfm-cli / UNKNOWN clean
  wheel contents, published releases, accepted facade API, exhaustive consumers, semantic-versioning policy,
  installation outside CI, and operational use / NEEDS VERIFICATION owner assignment, role decision, metadata
  completion, clean-build evidence, import-safety tests, API snapshot, consumer graph, CI enforcement,
  compatibility policy, deprecation window, correction propagation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 15d88fceced7050abac4493b9cf66f5bc288c1e6
  prior_blob: b152a4d791f6764217d49d341310efbeed3da908
  namespace_init_blob: b0c8ae94b22045818b6af9db40260acdf40338f1
  root_pyproject_blob: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  src_root_readme_blob: c64a49e6b15eb543a78cac29fee5b4fe650010be
  packages_root_readme_blob: fc18fb3334fefe992a551fe12aa98c812232cd17
  tests_root_readme_blob: 5614de99433bca29d6a03d665fb4e00ec23eb5fb
  makefile_blob: 4dc8cf633581893d83fba53219c6ea847992e6be
  schema_validation_workflow_blob: 4656da9884ec7cccef453c06ae26e8eee90992da
  cli_pyproject_blob: ad5b1772fa73ff6d673c9510c72a2283ac961caa
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_path_checks:
    - src/kfm/__init__.py contains only the package docstring
    - root pyproject selects packages = ["src/kfm"] for the Hatch wheel target
    - root project declares kfm version 0.0.0, Python >=3.11, jsonschema, and pytest test extra
    - schema-validation workflow runs pip install -e . before make schemas
    - root Makefile test target runs tests/schemas and tests/contracts, not a kfm import suite
    - bounded searches for import kfm, from kfm, and kfm.__ did not establish an executable consumer
    - src/kfm/__main__.py was not found
    - src/kfm/core.py was not found
    - src/kfm/py.typed was not found
    - tests/test_kfm_import.py was not found
    - apps/cli declares separate distribution name kfm-cli
related:
  - ../README.md
  - ../../pyproject.toml
  - __init__.py
  - ../../packages/README.md
  - ../../apps/README.md
  - ../../apps/cli/README.md
  - ../../apps/cli/src/kfm_cli/README.md
  - ../../tests/README.md
  - ../../Makefile
  - ../../.github/workflows/schema-validation.yml
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, src, python, hatch, root-distribution, import-namespace, package-marker, facade, compatibility, packaging, tests, migration, rollback]
notes:
  - "This revision changes only src/kfm/README.md."
  - "The root project is build-configured and schema CI installs it; the namespace itself remains minimal."
  - "This README adds no exports, entry points, modules, dependencies, tests, workflows, release artifacts, or runtime behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `src/kfm/` — Root Distribution Namespace and Unratified Facade Boundary

> **Purpose.** Define the Python namespace included in the repository's root `kfm` distribution while keeping its API, dependency direction, build proof, compatibility posture, and migration status explicit.

![status](https://img.shields.io/badge/status-draft-yellow)
![distribution](https://img.shields.io/badge/distribution-kfm-blue)
![version](https://img.shields.io/badge/version-0.0.0-lightgrey)
![build](https://img.shields.io/badge/build-Hatch-blueviolet)
![namespace](https://img.shields.io/badge/namespace-minimal-orange)
![api](https://img.shields.io/badge/API-unratified-critical)

> [!IMPORTANT]
> `src/kfm/` is not an unconfigured marker. The root `pyproject.toml` explicitly builds distribution `kfm` from this directory, and schema CI installs the root project. That confirms packaging intent—not a supported facade, CLI, runtime, domain library, public API, or released package.

> [!CAUTION]
> The namespace currently exposes only a package docstring. Do not infer exports, semantic-versioning guarantees, application behavior, lifecycle access, or release maturity from `import kfm` succeeding.

> [!WARNING]
> Root-package convenience must not collapse KFM responsibility roots. Shared implementation belongs under `packages/`; deployables under `apps/`; trust tooling under `tools/`; pipelines, runtime, authority objects, and lifecycle records remain in their owning roots.

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Purpose](#bounded-role) · [Placement](#repository-fit-and-placement) · [Packaging](#confirmed-packaging-contract) · [Namespace](#current-namespace-contract) · [Boundaries](#responsibility-and-import-boundaries) · [Facade](#facade-admission) · [Safety](#import-safety) · [Metadata](#metadata-and-versioning) · [Build](#build-install-and-artifact-proof) · [Testing](#testing-and-ci) · [Placement rules](#what-belongs-here) · [Implementation](#smallest-sound-next-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#maintenance-migration-and-rollback)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| `src/kfm/README.md` | **CONFIRMED** | Target and prior blob exist. |
| `src/kfm/__init__.py` | **CONFIRMED minimal** | Contains only `"""Kansas Frontier Matrix root package."""`; no exports or behavior are established. |
| Root `pyproject.toml` | **CONFIRMED** | Hatch builds distribution `kfm` version `0.0.0` and selects `src/kfm` for the wheel. |
| Root dependencies | **CONFIRMED** | Declares `jsonschema`; the inline comment ties it to schema-validator registry tooling. |
| Schema-validation workflow | **CONFIRMED definition** | Runs `pip install -e .` before `make schemas`. |
| Root Makefile test target | **CONFIRMED narrow** | Runs schema and contract tests, not a `kfm` namespace suite. |
| `src/README.md` | **CONFIRMED stale claim** | Says packaging is unverified despite explicit root configuration. |
| `packages/` | **CONFIRMED shared-library root** | Root namespace must not become a shadow package tree. |
| `apps/cli` | **CONFIRMED separate distribution** | Declares `kfm-cli`; root `kfm` is not proven to own CLI behavior. |
| Selected API/entry-point files | **Not found** | No checked `__main__.py`, `core.py`, or `py.typed`. |
| Executable consumers | **Not surfaced by bounded searches** | No consumer contract is established; absence is not exhaustive. |
| Clean wheel, published package, production use | **UNKNOWN** | Configuration is not release or operational proof. |

**Authority:** package-boundary and migration guidance only. Packaging metadata, accepted ADRs, implementation packages, tests, artifacts, workflow logs, releases, consumers, and steward decisions outrank this README.

[Back to top](#top)

---

<a id="bounded-role"></a>

## Bounded role

Current flow:

```text
root pyproject metadata and dependency carrier
  -> Hatch packages src/kfm
  -> minimal import namespace
  -> schema-validation environment installs root project
  -> no confirmed exports, commands, runtime behavior, or domain implementation
```

This lane may remain a marker, dependency carrier, migration shim, or deliberately curated facade. Its long-term role is not accepted yet.

This README does not:

- create a stable Python API;
- declare a CLI or console entry point;
- make `kfm` an umbrella import for child packages;
- authorize connectors, pipelines, runtime, evidence, policy, lifecycle, release, API, UI, or AI behavior;
- prove clean build artifacts, package publication, external consumers, or production use.

[Back to top](#top)

---

<a id="repository-fit-and-placement"></a>

## Repository fit and placement

Directory Rules assign implementation by responsibility:

```text
apps/        deployable applications and services
packages/    shared reusable libraries
connectors/  source-admission integrations
pipelines/   executable pipeline behavior
runtime/     internal runtime wiring and adapters
tools/       validators, generators, builders, proof/release/QA tooling
scripts/     small operational helpers before graduation
tests/       enforceability proof
```

`src/` has no independent responsibility class in the canonical root tree, but repository evidence confirms the root Python project uses a `src` layout.

| Question | Determination |
|---|---|
| Does `src/kfm/` participate in root packaging? | **CONFIRMED.** |
| Is the root distribution build-configured? | **CONFIRMED.** |
| Is this the canonical shared-implementation root? | **No.** Shared libraries belong under `packages/`. |
| Is `kfm` an accepted umbrella facade? | **UNKNOWN / NEEDS VERIFICATION.** |
| May a root distribution remain? | **Yes**, if its marker, dependency, compatibility, or facade role is explicit and non-authoritative. |
| Should substantial code or re-exports require a decision record? | **PROPOSED yes**, because they alter ownership and compatibility. |

The current dual shape is manageable only while responsibilities remain separate:

```text
src/kfm/          root distribution namespace
packages/*        canonical shared implementations
```

[Back to top](#top)

---

<a id="confirmed-packaging-contract"></a>

## Confirmed packaging contract

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "kfm"
version = "0.0.0"
requires-python = ">=3.11"

[tool.hatch.build.targets.wheel]
packages = ["src/kfm"]
```

Confirmed by configuration:

- distribution name `kfm`;
- scaffold version `0.0.0`;
- Hatchling build backend;
- Python 3.11+ declaration;
- `src/kfm` wheel package selection;
- root dependencies and pytest test extra;
- editable root installation in schema-validation workflow.

Still unverified:

- clean wheel and sdist build;
- exact artifact contents;
- editable/wheel parity;
- isolated import behavior;
- package index publication;
- external consumers;
- reproducibility, signing, or provenance.

[Back to top](#top)

---

<a id="current-namespace-contract"></a>

## Current namespace contract

Current `__init__.py`:

```python
"""Kansas Frontier Matrix root package."""
```

The supported conclusion is narrow:

- `kfm` is a configured package namespace marker;
- no symbols are documented or exported;
- no version attribute, command runner, or plugin registry exists at checked paths;
- no domain, connector, pipeline, validator, runtime, API, UI, or release API is exposed;
- no compatibility promise exists beyond the marker.

These are **not** current APIs:

```python
from kfm import EvidenceBundle
from kfm import PolicyDecision
from kfm import run_pipeline
from kfm import publish
```

[Back to top](#top)

---

<a id="responsibility-and-import-boundaries"></a>

## Responsibility and import boundaries

| Concern | Owning home | Role of `src/kfm/` |
|---|---|---|
| Shared implementation | `packages/<package>/` | Reference or re-export only after facade approval. |
| Domain implementation | `packages/domains/<domain>/` | None. |
| CLI, API, worker, UI | `apps/` | None; `kfm-cli` is separate. |
| Source clients | `connectors/` | No implementation or activation. |
| Pipeline execution | `pipelines/` | No orchestration or promotion authority. |
| Runtime adapters | `runtime/` | No provider authority. |
| Validators and trust tooling | `tools/` | Root project may supply dependencies; code stays in `tools/`. |
| Contracts, schemas, policy | authority roots | No authority. |
| Tests and fixtures | `tests/`, `fixtures/` | No storage. |
| Lifecycle, receipts, proofs | `data/` | No read/write or promotion authority. |
| Release/correction/rollback | `release/` | No authority. |
| Public interfaces | governed applications | No direct public contract. |

Prefer direct imports from the package that owns behavior:

```text
apps / pipelines / tools
  -> accepted package namespace under packages/*
```

Do not normalize an unreviewed umbrella:

```text
all repository code -> kfm -> arbitrary internal roots
```

Anti-collapse rules:

```text
installable package     != implemented API
successful import       != supported exports
root dependency         != namespace behavior
editable install        != wheel-release proof
schema workflow success != package API test
root distribution       != packages/ replacement
kfm                     != kfm-cli
re-export               != ownership transfer
```

[Back to top](#top)

---

<a id="facade-admission"></a>

## Facade admission

| Option | Current posture |
|---|---|
| Marker only | Closest to current evidence. |
| Dependency carrier | Confirmed configuration role; long-term policy unverified. |
| Compatibility shim | Allowed only when needed and tested. |
| Curated facade | Requires explicit acceptance, stable source APIs, tests, and versioning. |
| Application or mega-package | Denied by default; wrong responsibility. |

Before exporting a symbol:

1. identify the owning package;
2. confirm its API is accepted and versioned;
3. document facade stability and compatibility;
4. keep imports acyclic and side-effect-free;
5. test direct-versus-facade identity;
6. test missing optional dependencies;
7. define deprecation and rollback;
8. inventory consumers;
9. prevent truth, policy, evidence, release, or public-authority implications.

[Back to top](#top)

---

<a id="import-safety"></a>

## Import safety

`import kfm` must not:

- make network requests;
- read or mutate lifecycle stores;
- load secrets or environment-specific configuration;
- connect to databases, queues, models, or providers;
- register connectors, pipelines, policies, routes, plugins, or release handlers;
- create files, caches, receipts, logs, or temporary directories;
- inspect protected evidence or sensitive locations;
- modify global logging, warnings, signals, or event loops;
- scan the repository for packages;
- mutate `sys.path` or guess compatibility aliases.

Future initialization must be explicit and owned by the correct package or application.

[Back to top](#top)

---

<a id="metadata-and-versioning"></a>

## Metadata and versioning

| Field | Current value/posture |
|---|---|
| Distribution | `kfm` — CONFIRMED |
| Version | `0.0.0` scaffold — CONFIRMED |
| Python | `>=3.11` — CONFIRMED declaration |
| Build | Hatchling — CONFIRMED |
| License | `TBD` — incomplete |
| Runtime dependency | `jsonschema>=4.26.0,<5` — CONFIRMED |
| Test extra | `pytest>=9.1.1,<10` — CONFIRMED |
| Console scripts / entry points | none declared |
| Semantic-versioning policy | UNKNOWN |
| Package publication | UNKNOWN |

Before publication or stable dependency use, resolve license, ownership, version source, compatibility policy, changelog, Python matrix, dependency ownership, artifact provenance, registry name ownership, and relationship to `kfm-cli` and child distributions.

[Back to top](#top)

---

<a id="build-install-and-artifact-proof"></a>

## Build, install, and artifact proof

Current schema workflow:

```text
checkout -> Python 3.11 -> pip install -e . -> make schemas
```

A successful run supports only bounded claims: editable installation completed in that runner and declared dependencies supported the schema target. It does not prove wheel/sdist build, artifact contents, isolated import, API stability, publication, or external compatibility.

Proposed package proof:

```bash
python -m build
python -m venv .venv-package-check
.venv-package-check/bin/python -m pip install dist/*.whl
.venv-package-check/bin/python -I -c "import kfm; print(kfm.__doc__)"
.venv-package-check/bin/python -m pip check
```

Also inspect wheel/sdist contents, METADATA, undeclared packages, repository-only files, artifact digests, and provenance. These are proposed commands, not current results.

[Back to top](#top)

---

<a id="testing-and-ci"></a>

## Testing and CI

Current boundary:

- `make test` runs schema and contract tests;
- pytest adds repository root, not `src`, to `pythonpath`;
- schema CI editable-installs the project;
- no selected root import test exists at `tests/test_kfm_import.py`;
- bounded searches did not establish a consumer;
- no checked workflow proves the installed namespace contract directly.

Required tests:

| Test | Proof |
|---|---|
| Metadata | Name, version, Python range, dependencies, and license state are intentional. |
| Wheel contents | Only intended files are packaged. |
| Clean import | Installed wheel imports in isolated mode. |
| Side effects | Import performs no network, filesystem, environment, logging, registry, or process mutation. |
| API snapshot | Exports exactly the documented marker or facade names. |
| Editable/wheel parity | Both expose the same documented API. |
| Namespace split | `kfm`, `kfm-cli`, and child package names remain distinct. |
| Dependency direction | Root namespace does not import apps, tools, connectors, pipelines, runtime, data, or release implicitly. |
| Hidden authority | Import cannot mutate lifecycle, policy, evidence, receipt, proof, release, or publication state. |
| Build matrix | Accepted Python versions build and import. |
| Deprecation | Removed facade names follow accepted policy. |

Proposed CI:

```text
metadata lint -> build -> inspect artifacts -> clean install -> import safety
-> API snapshot -> dependency tests -> editable/wheel parity -> schema/contract suites
```

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

Allowed by default:

- this README;
- minimal `__init__.py` marker;
- pure package metadata helpers after review;
- tightly scoped, tested compatibility re-exports;
- migration and deprecation notes.

Review required:

- any exported symbol;
- `__version__` or dynamic version loading;
- facade modules and aliases;
- `py.typed` and typed-public-API claims;
- optional dependencies;
- entry points, plugins, generated code, or package data.

Do not place here:

| Item | Correct home |
|---|---|
| Shared/domain implementation | `packages/` |
| CLI or deployable services | `apps/` |
| Connectors | `connectors/` |
| Pipelines | `pipelines/` |
| Runtime providers | `runtime/` |
| Validators/builders/release/proof tooling | `tools/` |
| Operational scripts | `scripts/` |
| Contracts/schemas/policy | authority roots |
| Tests/fixtures | `tests/`, `fixtures/` |
| Lifecycle, receipts, proofs, catalogs | `data/` |
| Release decisions and rollback cards | `release/` |
| Public API/UI/map artifacts | governed app and published-artifact roots |
| Credentials or private config | approved external systems |

[Back to top](#top)

---

<a id="smallest-sound-next-sequence"></a>

## Smallest sound next sequence

1. **Preserve the marker.** Correct documentation; add no opportunistic facade exports.
2. **Prove packaging.** Build/inspect artifacts; test clean import, side effects, and editable/wheel parity.
3. **Decide the role.** Marker, dependency carrier, shim, curated facade, or retirement.
4. **Rationalize dependencies.** Verify root dependency ownership; avoid a dependency dumping ground.
5. **Admit facade symbols deliberately.** Stable source APIs, compatibility policy, tests, and acyclic imports first.
6. **Release or retire reversibly.** Inventory consumers, preserve migration notes, and retain rollback evidence.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Root distribution role and owners are accepted.
- [ ] Clean sdist and wheel builds pass.
- [ ] Artifact contents and metadata are inspected.
- [ ] Wheel installation and isolated import pass.
- [ ] Import side effects are tested and absent.
- [ ] Public exports are documented or confirmed empty.
- [ ] Editable/wheel parity is proven.
- [ ] Dependency ownership is reviewed.
- [ ] Package tests run in substantive CI.
- [ ] `kfm` and `kfm-cli` boundaries are tested.
- [ ] Consumers are inventoried.
- [ ] Facade imports map to accepted owning-package APIs.
- [ ] Lifecycle/evidence/policy/release bypass tests pass.
- [ ] Versioning, deprecation, correction, and rollback policies are accepted.
- [ ] Released artifacts carry appropriate integrity and provenance.

Until then: **build-configured root distribution with a minimal, unratified namespace**.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Status |
|---|---|---|
| KFM-PKG-01 | Assign distribution and namespace owners. | NEEDS VERIFICATION |
| KFM-PKG-02 | Decide marker, dependency carrier, shim, facade, or retirement. | NEEDS VERIFICATION |
| KFM-PKG-03 | Find or create the governing ADR/migration record. | NEEDS VERIFICATION |
| KFM-PKG-04 | Build and inspect sdist/wheel. | NEEDS VERIFICATION |
| KFM-PKG-05 | Verify clean install and isolated import. | NEEDS VERIFICATION |
| KFM-PKG-06 | Inventory executable and external consumers. | NEEDS VERIFICATION |
| KFM-PKG-07 | Confirm raw-checkout import behavior. | NEEDS VERIFICATION |
| KFM-PKG-08 | Add import-safety and API snapshot tests. | NEEDS VERIFICATION |
| KFM-PKG-09 | Resolve license and publication metadata. | NEEDS VERIFICATION |
| KFM-PKG-10 | Define versioning and compatibility policy. | NEEDS VERIFICATION |
| KFM-PKG-11 | Verify root `jsonschema` dependency ownership. | NEEDS VERIFICATION |
| KFM-PKG-12 | Confirm Python support matrix. | NEEDS VERIFICATION |
| KFM-PKG-13 | Verify editable/wheel parity. | NEEDS VERIFICATION |
| KFM-PKG-14 | Decide typed API and `py.typed` posture. | NEEDS VERIFICATION |
| KFM-PKG-15 | Define facade/re-export admission. | NEEDS VERIFICATION |
| KFM-PKG-16 | Define relationship to `kfm-cli` and child distributions. | NEEDS VERIFICATION |
| KFM-PKG-17 | Add substantive package CI. | NEEDS VERIFICATION |
| KFM-PKG-18 | Define deprecation and migration window. | NEEDS VERIFICATION |
| KFM-PKG-19 | Prove package correction and rollback. | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="maintenance-migration-and-rollback"></a>

## Maintenance, migration, and rollback

### Documentation rollback

Before merge, close the review branch. After merge, revert the commit or restore the prior blob in metadata. No runtime, data, policy, evidence, release, or deployment rollback is required.

### Package correction

If metadata or artifact contents are wrong: halt promotion, preserve artifacts/hashes/logs, identify affected versions, correct through a new reviewed version, rebuild in isolation, notify known consumers, and retain a rollback or forward-fix decision.

### Facade migration

Inventory consumers; identify the owning package; provide a bounded shim only if necessary; test warning/error behavior; document version and removal window; update examples/tests/types/release notes; avoid dual implementations; remove the shim only after migration evidence closes.

### Retirement

Freeze exports; replace workflow dependency on root editable installation; move dependency ownership to accepted roots; update build and CI; preserve a final migration note/version; remove `src/kfm` and root wheel selection through a reviewed reversible change; rerun schema, contract, API, tool, and developer workflows.

### Incident posture

If a package artifact includes protected data, private paths, environment-specific values, credentials, generated artifacts, or authority-bearing records, halt distribution, preserve evidence, remove the material, rotate affected credentials where relevant, audit consumers, and issue a corrected artifact rather than silently replacing history.

[Back to top](#top)
