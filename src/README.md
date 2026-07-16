<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/src-readme
title: src/ — Root Python Distribution Source Layout and Compatibility Boundary
type: readme; directory-readme; root-source-layout; packaging-boundary; compatibility-root-index
version: v0.2
status: draft; repository-grounded; hatch-packaged; root-src-drift; migration-decision-open; public-api-unestablished; non-authoritative
owners: OWNER_TBD — Architecture steward · Package steward · Python packaging steward · Developer tooling steward · Validation steward · CI steward · Release steward · Docs steward
created: NEEDS VERIFICATION — empty README was replaced by v0.1 on 2026-07-04
updated: 2026-07-16
supersedes: v0.1 root Python package compatibility lane guide
policy_label: "public-doctrine; python; packaging; src-layout; compatibility-root; no-parallel-implementation-authority; no-hidden-facade; no-public-api-claim; no-runtime-authority; no-lifecycle-authority; no-release-authority; adr-required-for-retention-or-migration; rollback-aware"
current_path: src/README.md
truth_posture: >
  CONFIRMED target v0.1 README; root Hatch configuration for distribution kfm version 0.0.0;
  Python >=3.11, jsonschema dependency, pytest test extra, and wheel selection src/kfm;
  src/kfm README v0.2; minimal src/kfm/__init__.py; packages responsibility-root README;
  Makefile schema/test targets; schema-validation editable install; separate kfm-cli metadata;
  Directory Rules classification of root src/ as drift; and no dedicated root-src drift-register row /
  PROPOSED containment, dependency, import-safety, validation, ADR, migration, correction, and rollback rules /
  CONFLICTED active Hatch packaging versus Directory Rules exclusion of src/ from canonical roots;
  prior README packaging and CI uncertainty versus current repository evidence /
  UNKNOWN clean artifacts, publication, accepted package role, consumers, versioning, and operational use /
  NEEDS VERIFICATION owners, accepted ADR or migration record, drift-register synchronization, build/import proof,
  dependency ownership, compatibility policy, deprecation window, correction propagation, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 0c9df2b0ed87753ff482bdd2da87f35507517eed
  prior_blob: c64a49e6b15eb543a78cac29fee5b4fe650010be
  child_readme_blob: d8cd7a5fc70357eb78c52b9311e32cec8c7063f5
  namespace_init_blob: b0c8ae94b22045818b6af9db40260acdf40338f1
  root_pyproject_blob: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  packages_root_readme_blob: fc18fb3334fefe992a551fe12aa98c812232cd17
  makefile_blob: 4dc8cf633581893d83fba53219c6ea847992e6be
  schema_validation_workflow_blob: 4656da9884ec7cccef453c06ae26e8eee90992da
  cli_pyproject_blob: ad5b1772fa73ff6d673c9510c72a2283ac961caa
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  drift_register_blob: 97a775522dcd058299f752ac7862d0fc56c13280
related:
  - kfm/README.md
  - kfm/__init__.py
  - ../pyproject.toml
  - ../packages/README.md
  - ../apps/README.md
  - ../apps/cli/README.md
  - ../tests/README.md
  - ../Makefile
  - ../.github/workflows/schema-validation.yml
  - ../docs/doctrine/directory-rules.md
  - ../docs/registers/DRIFT_REGISTER.md
tags: [kfm, src, python, hatch, root-distribution, source-layout, compatibility-root, packaging, boundary, migration, adr, rollback]
notes:
  - "This revision changes src/README.md and its required generated-work receipt only."
  - "It reconciles the parent README with src/kfm/README.md v0.2 and current packaging evidence."
  - "It adds no code, exports, entry points, dependencies, tests, workflows, release artifacts, runtime behavior, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `src/` — Root Python Distribution Source Layout and Compatibility Boundary

> **Purpose.** Orient maintainers to the root Python source layout, document the configured `kfm` distribution boundary, and prevent `src/` from becoming a parallel implementation authority while its retention or migration remains unresolved.

![status](https://img.shields.io/badge/status-draft-yellow)
![distribution](https://img.shields.io/badge/distribution-kfm-0a7ea4)
![build](https://img.shields.io/badge/build-Hatch-blueviolet)
![placement](https://img.shields.io/badge/placement-drift%20%2F%20ADR%20open-orange)
![api](https://img.shields.io/badge/public%20API-unestablished-critical)

> [!IMPORTANT]
> `src/` is not an unused placeholder. The root [`pyproject.toml`](../pyproject.toml) builds distribution `kfm` from `src/kfm`, and schema CI installs the root project before validation. That proves packaging use—not a supported facade, shared-library root, runtime surface, or released package.

> [!WARNING]
> Directory Rules exclude `src/` from canonical responsibility roots and explicitly classify the existing root `src/kfm/` lane as drift. Retention, facade adoption, migration into `packages/`, or retirement requires a reviewed ADR or migration record. This README documents the boundary; it does not decide the outcome.

> [!CAUTION]
> Do not place substantial implementation here merely because the directory is packaged. Shared libraries belong under [`packages/`](../packages/README.md); deployables under `apps/`; source integrations under `connectors/`; transformations under `pipelines/`; runtime adapters under `runtime/`; and trust tooling under `tools/`.

**Quick navigation:** [Status](#status-and-evidence-boundary) · [Inventory](#bounded-current-inventory) · [Placement](#repository-fit-and-conflict) · [Child namespace](#parent-and-child-readme-contract) · [Content rules](#content-and-authority-rules) · [Trust](#trust-and-import-boundary) · [Validation](#validation-and-ci-boundary) · [Decision](#adr-and-migration-decision) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Rollback](#maintenance-correction-and-rollback)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

| Surface | Status | Safe conclusion |
|---|---|---|
| `src/README.md` | **CONFIRMED** | Existing parent README; v0.1 carried stale packaging uncertainty. |
| [`src/kfm/README.md`](kfm/README.md) | **CONFIRMED v0.2** | Detailed namespace, facade, import-safety, build, test, and migration contract. |
| [`src/kfm/__init__.py`](kfm/__init__.py) | **CONFIRMED minimal** | Contains only `"""Kansas Frontier Matrix root package."""`; no exports or behavior are established. |
| Root [`pyproject.toml`](../pyproject.toml) | **CONFIRMED** | Hatchling builds `kfm` version `0.0.0` from `src/kfm`; Python `>=3.11`; `jsonschema` dependency; pytest test extra. |
| Schema-validation workflow | **CONFIRMED definition** | Runs `pip install -e .` before `make schemas`. |
| Root [`Makefile`](../Makefile) tests | **CONFIRMED narrow** | Runs schema and contract tests, not package artifact or import-safety tests. |
| [`packages/`](../packages/README.md) | **CONFIRMED responsibility root** | Canonical home for shared reusable implementation. |
| `apps/cli` | **CONFIRMED separate distribution** | Declares `kfm-cli`; root `kfm` does not own CLI behavior by implication. |
| Directory Rules | **CONFIRMED doctrine** | Root `src/` is non-canonical drift requiring migration or ADR-backed retention. |
| Dedicated drift-register entry | **Not present in inspected register** | Formal synchronization remains open. |
| Clean artifacts, package publication, production consumers | **UNKNOWN** | Configuration and editable CI installation are not release or operational proof. |

**Evidence boundary:** claims are pinned to `bartytime4life/Kansas-Frontier-Matrix@0c9df2b0ed87753ff482bdd2da87f35507517eed`. Absence claims are bounded to inspected paths and searches.

**Authority:** this is an orientation and containment document. Accepted ADRs, packaging metadata, owning packages, tests, workflow runs, artifacts, releases, and steward decisions outrank it.

[Back to top](#top)

---

<a id="bounded-current-inventory"></a>

## Bounded current inventory

```text
src/
├── README.md
└── kfm/
    ├── README.md
    └── __init__.py
```

| Path | Confirmed role | Explicit limit |
|---|---|---|
| `src/README.md` | Parent source-layout index and placement guardrail | Does not define package exports or settle root retention. |
| `src/kfm/README.md` | Package-level namespace and unratified-facade contract | Does not create API stability or implementation. |
| `src/kfm/__init__.py` | Minimal import marker | No commands, registries, adapters, domain objects, or side effects are established. |

No additional child directory is claimed. Add future children to this inventory only after repository inspection and placement review.

[Back to top](#top)

---

<a id="repository-fit-and-conflict"></a>

## Repository fit and conflict

Directory Rules organize implementation by responsibility:

```text
apps/        deployable applications and services
packages/    shared reusable libraries
connectors/  source-admission integrations
pipelines/   executable transformations
runtime/     runtime adapters and harnesses
tools/       validators, generators, builders, proof/release/QA tooling
scripts/     small operational helpers
tests/       enforceability proof
```

`src/` has no independent canonical responsibility, but the root project currently uses a Python `src` layout. Both facts must remain visible:

| Question | Determination |
|---|---|
| Is `src/kfm` actively included in root packaging? | **CONFIRMED.** |
| Is `src/` a canonical KFM responsibility root? | **No under current Directory Rules.** |
| Is `packages/` the shared-library authority? | **CONFIRMED.** |
| Is `kfm` an accepted umbrella facade? | **UNKNOWN / NEEDS VERIFICATION.** |
| May the root distribution remain temporarily? | **PROPOSED yes**, if minimal, non-authoritative, tested, and ADR/migration governed. |

Current containment model:

```text
src/kfm/       configured root distribution namespace; minimal and unratified
packages/*     canonical shared implementations
apps/*         deployable behavior
other roots    retain their own authority
```

Do not silently treat repository convention as doctrine. Do not silently remove active packaging. Record the conflict, decide it through governance, and keep changes reversible.

[Back to top](#top)

---

<a id="parent-and-child-readme-contract"></a>

## Parent and child README contract

| Document | Owns | Must not duplicate or claim |
|---|---|---|
| `src/README.md` | Directory inventory, placement conflict, child index, root-wide containment, decision and rollback summary | Detailed facade API, symbol-level exports, package artifact contract, or package test matrix |
| `src/kfm/README.md` | Distribution metadata, namespace contract, import safety, facade admission, artifact proof, package tests, compatibility and retirement detail | Canonical shared-library authority or deployable behavior |

Update the parent when children or the directory-level decision changes. Update the child when package metadata, exports, imports, tests, consumers, artifacts, facade behavior, or compatibility changes.

[Back to top](#top)

---

<a id="content-and-authority-rules"></a>

## Content and authority rules

Allowed by default:

- this README and child package README;
- a minimal `__init__.py` marker;
- tightly scoped, tested compatibility shims after review;
- migration, deprecation, and correction notes;
- pure package metadata helpers only when their ownership is explicit.

Review required before adding any export, facade module, alias, dynamic version loader, typed-public-API marker, optional dependency, entry point, plugin, generated code, or package data.

| Do not place in root `src/` | Correct responsibility root |
|---|---|
| Shared or domain implementation | `packages/` |
| CLI, service, worker, API, or UI shell | `apps/` |
| Source fetchers or clients | `connectors/` |
| Executable pipelines | `pipelines/` |
| Runtime providers | `runtime/` |
| Validators, builders, proof/release helpers | `tools/` |
| Operational scripts | `scripts/` |
| Contract meaning, schemas, policy | `contracts/`, `schemas/`, `policy/` |
| Tests and fixtures | `tests/`, `fixtures/` |
| Lifecycle records, receipts, proofs, catalogs | `data/` |
| Release decisions, corrections, rollback cards | `release/` |
| Public API, UI, map, or AI behavior | governed app and released-artifact roots |

A re-export does not transfer ownership. An installable package is not implementation proof. A successful import is not a supported API.

[Back to top](#top)

---

<a id="trust-and-import-boundary"></a>

## Trust and import boundary

`src/` must not bypass the KFM trust membrane. It has no authority to:

- read or write RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED state;
- resolve or create `EvidenceBundle`, policy, review, promotion, correction, or rollback authority;
- expose canonical/internal stores to public clients;
- activate connectors, pipelines, runtime providers, models, routes, plugins, or release handlers;
- treat map tiles, graph projections, indexes, dashboards, summaries, or model output as truth.

`import kfm` must remain side-effect free. It must not perform network, filesystem, secret, environment, database, queue, model, logging, signal, event-loop, repository-scan, `sys.path`, or global-registry mutation.

Preferred dependency direction:

```text
apps / pipelines / tools
  -> accepted owning packages under packages/*
```

Unreviewed umbrella direction to avoid:

```text
all repository code -> kfm -> arbitrary internal roots
```

[Back to top](#top)

---

<a id="validation-and-ci-boundary"></a>

## Validation and CI boundary

Current schema workflow:

```text
checkout -> Python 3.11 -> pip install -e . -> make schemas
```

Current root test target:

```text
python -m pytest tests/schemas tests/contracts -q
```

These definitions do not directly prove wheel/sdist contents, isolated import, side effects, exports, compatibility, or consumers.

Before changing the root package role, require evidence for:

- metadata and license intent;
- clean wheel and sdist build;
- artifact-content inspection;
- isolated wheel install and import;
- import-side-effect denial;
- API/export snapshot;
- editable-versus-wheel parity;
- dependency-direction enforcement;
- `kfm` versus `kfm-cli` separation;
- consumer inventory and migration tests;
- correction and rollback.

The inspected pull-request workflows use GitHub-hosted runners. The general docs, link, and control-plane workflows are stubs; a passing stub is not substantive validation. This documentation change does not modify executable code, workflow, schema, policy, runtime, infrastructure, release, or publication state.

[Back to top](#top)

---

<a id="adr-and-migration-decision"></a>

## ADR and migration decision

| Option | Meaning | Minimum evidence |
|---|---|---|
| Retain as marker/dependency carrier | Keep `src/kfm` minimal for root-tooling compatibility | ADR, owners, dependency rationale, build/import tests, consumer and rollback evidence |
| Curated facade | Re-export a small stable API from canonical packages | Facade contract, owner approval, API snapshot, versioning, consumer inventory, deprecation and rollback |
| Migrate to `packages/kfm` or `packages/kfm-core` | Move packaging/shared implementation into the canonical package root | Approved destination, import map, atomic build/CI change, migration window, tests, reversible move |
| Retire root distribution | Remove root wheel selection and editable-install dependency | Workflow replacement, dependency ownership, consumer proof, final migration note, artifact/import regression tests |

Until a decision is accepted:

1. keep the namespace minimal;
2. add no opportunistic facade exports or implementation;
3. route reusable work to `packages/`;
4. document and test any temporary shim;
5. preserve migration and rollback evidence.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

- [ ] Root distribution role and owners are accepted.
- [ ] An ADR or migration record covers retention, facade, migration, or retirement.
- [ ] Root-`src` drift is registered or explicitly closed by ADR.
- [ ] License, version source, dependency ownership, and publication metadata are resolved.
- [ ] Clean sdist and wheel builds pass and artifacts are inspected.
- [ ] Isolated import, side-effect, API snapshot, and editable/wheel parity tests pass.
- [ ] Substantive package CI exists.
- [ ] `kfm` and `kfm-cli` boundaries are tested.
- [ ] Consumers are inventoried.
- [ ] Any facade maps only to accepted owning-package APIs.
- [ ] Trust-membrane bypass tests pass.
- [ ] Compatibility, deprecation, correction, and rollback policies are accepted.

Until then: **configured root source layout with a minimal, non-canonical, unratified namespace**.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Status |
|---|---|---|
| KFM-SRC-01 | Assign distribution and source-layout owners. | NEEDS VERIFICATION |
| KFM-SRC-02 | Accept a retention, facade, migration, or retirement decision. | NEEDS VERIFICATION |
| KFM-SRC-03 | Synchronize root-`src` drift into `docs/registers/DRIFT_REGISTER.md` or close it by ADR. | NEEDS VERIFICATION |
| KFM-SRC-04 | Build and inspect clean artifacts; verify isolated import and editable/wheel parity. | NEEDS VERIFICATION |
| KFM-SRC-05 | Add import-side-effect, API-snapshot, dependency-direction, and `kfm`/`kfm-cli` tests. | NEEDS VERIFICATION |
| KFM-SRC-06 | Inventory repository, workflow, and external consumers. | NEEDS VERIFICATION |
| KFM-SRC-07 | Resolve `jsonschema` dependency ownership, license, versioning, and registry posture. | NEEDS VERIFICATION |
| KFM-SRC-08 | Define facade admission, compatibility, deprecation, correction, and rollback. | NEEDS VERIFICATION |
| KFM-SRC-09 | Verify generated, mirrored, localized, or compatibility copies requiring synchronization. | NEEDS VERIFICATION |

[Back to top](#top)

---

<a id="maintenance-correction-and-rollback"></a>

## Maintenance, correction, and rollback

Update this README when children, packaging, dependency, workflow, ADR, migration, or root-level policy changes. Update [`src/kfm/README.md`](kfm/README.md) when package exports, imports, tests, consumers, facade behavior, compatibility, or artifact proof changes.

**Documentation rollback:** before merge, close the draft PR and abandon the branch. After merge, use a transparent revert or restore the prior blob through review. No runtime, data, policy, evidence, release, or deployment rollback is required for this documentation-only change.

**Package correction:** halt promotion; preserve artifacts, hashes, logs, and consumer evidence; identify affected versions; correct through review; rebuild and test in isolation; notify known consumers when compatibility changed; retain correction and rollback lineage.

**Migration or retirement:** inventory consumers, accept the governing decision, update packaging and workflows atomically, use a bounded compatibility shim only when justified, test old and new paths, publish deprecation guidance, preserve history, and remove the old lane only after migration evidence closes.

[Back to top](#top)

---

## No-loss revision note

This v0.2 revision preserves the v0.1 rule that root `src/` must not become a shadow `packages/` tree. It corrects stale packaging/CI uncertainty, adds the merged child README to the inventory, surfaces the Directory Rules conflict, separates parent and child documentation responsibilities, and adds explicit ADR, validation, correction, and rollback guidance. No implementation, API, dependency, workflow, test, lifecycle, release, or publication behavior changes.
