<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/apps-packages/readme
title: apps/packages/ — Dormant Workspace-Risk and Drift-Guard Boundary
type: app-readme; directory-readme; architecture-drift-guard; deprecation-candidate
version: v0.2
status: draft; repository-grounded; bounded-readme-only-evidence; dormant-workspace-risk; frozen-for-new-authority; disposition-open
owners: OWNER_TBD — Apps steward · Package steward · Architecture steward · Build/workspace steward · Security steward · Validation steward · Docs steward
created: 2026-06-16
updated: 2026-07-19
policy_label: "public-governance; restricted-review; architecture-drift; workspace-risk; no-package-authority; no-app-authority; no-public-trust-path; migration-or-removal-required"
current_path: apps/packages/README.md
owning_root: apps/
responsibility: document, freeze, inspect, and retire or explicitly govern the anomalous apps/packages path without allowing it to become a deployable app, JavaScript workspace package, Python package namespace, shared-library root, runtime adapter, public trust surface, or parallel authority home
authority_level: drift-guard-and-disposition-boundary-only
truth_posture: CONFIRMED target README and prior drift-guard intent, Directory Rules apps deployable root, Directory Rules top-level packages shared-library root, apps root classification of this path as an anomaly, top-level packages root authority, root JavaScript workspace selector apps/* and packages/*, current root Python wheel target src/kfm only, absence at checked paths of apps/packages/package.json, apps/packages/pyproject.toml, and apps/packages/__init__.py, historical broad apps* Python package-discovery commit, current read-only all-PR UI workflow readiness failure posture, default CODEOWNERS routing, and bounded absence of overlapping open PR/branch work / PROPOSED dormant-workspace-risk classification, freeze policy, activation sentinels, deterministic drift test, explicit review route, removal sequence, and ADR-backed transitional exception / UNKNOWN exhaustive recursive lane inventory, every import/build reference, branch-protection requirements, retained external consumer, or maintainer disposition / NEEDS VERIFICATION named owners, recursive inventory, package-manager behavior under every supported tool, accepted migration/ADR, dedicated drift test, explicit CODEOWNERS pattern, expiry, removal approval, and current full-suite pass state
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 5cf7386b17a85feeadbb82a0eb9ec92bded68279
  prior_blob: f96476a05d8eba03e538fe9f9053d7e0e5a77033
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  apps_root_readme_blob: e0c26da27d45f287db1de88967c98546f3a9e3a9
  packages_root_readme_blob: fc18fb3334fefe992a551fe12aa98c812232cd17
  root_package_manifest_blob: 62f45306aef7376a2d68042b0c9e7f556edf0e78
  root_python_manifest_blob: e3bd40e8e6ce14dfcde78ff5c09608095c3eca76
  ui_build_workflow_blob: 12f7936e5f83301311f6100bb41e9c78f2dd10f5
  docs_build_workflow_blob: 202360a8bee431b50633e78c442cc70ca939206a
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  initial_drift_guard_commit: 8e262da92f3d5d7620b75fa169e46f0bad681a8e
  historical_broad_python_discovery_commit: c9c1b7efabc82ba5e59d9ccc8806256a1b6604b4
  inventory_method: exact GitHub file reads and probes, target-history inspection, bounded commit/code/branch/pull-request searches, and current manifest/workflow inspection
  direct_lane_files_confirmed:
    - apps/packages/README.md
  checked_absent_activation_paths:
    - apps/packages/package.json
    - apps/packages/pyproject.toml
    - apps/packages/__init__.py
  bounded_inventory_note: exact probes and commit history did not establish an active package manifest, Python package marker, implementation source, tests, build script, or runtime consumer in this lane; the connector did not expose a recursive directory listing, so permanent absence is not asserted
related:
  - ../README.md
  - ../../packages/README.md
  - ../../package.json
  - ../../pyproject.toml
  - ../../docs/architecture/directory-rules.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../governed-api/README.md
  - ../explorer-web/README.md
  - ../../packages/api/README.md
  - ../../packages/domains/README.md
  - ../../packages/ui/README.md
  - ../../packages/temporal/README.md
  - ../../tests/policy/README.md
  - ../../.github/workflows/ui-build.yml
  - ../../.github/workflows/docs-build.yml
  - ../../.github/CODEOWNERS
tags:
  - kfm
  - apps
  - packages
  - architecture-drift
  - dormant-workspace-risk
  - compatibility
  - deprecation-candidate
  - shared-libraries
  - deployables
  - workspace-glob
  - import-boundary
  - trust-membrane
  - fail-closed
  - reversible-change
notes:
  - "This v0.2 revision preserves the stable document identity and existing path while replacing broad uncertainty with a pinned repository evidence boundary."
  - "Directory Rules define apps/ as deployable applications and top-level packages/ as shared reusable libraries; apps/packages/ is absent from the canonical app map."
  - "The root JavaScript manifest selects apps/* and packages/* as workspaces. No apps/packages/package.json was found at the checked base, but adding one would place a manifest inside a selected app-child path and could activate this anomaly in workspace tooling."
  - "The current root Python build targets src/kfm only. A historical commit temporarily used broad apps* and packages* setuptools discovery; that history is a drift warning, not current behavior."
  - "The long-term disposition is not decided here. Safe outcomes are transparent removal or an ADR/migration-backed transitional exception with owner, consumer evidence, tests, expiry, and rollback."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `apps/packages/` — Dormant Workspace-Risk and Drift-Guard Boundary

`apps/packages/` is an existing anomalous child of the deployable-app root. It is **not** the KFM shared-package root, **not** a deployable app, and **not** an accepted compatibility package. Current bounded evidence shows the README and no checked activation manifest; the directory remains frozen against new code or authority until it is removed or governed as a temporary migration exception.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Classification: dormant workspace risk" src="https://img.shields.io/badge/classification-dormant%20workspace%20risk-orange">
  <img alt="Authority: none" src="https://img.shields.io/badge/authority-none-critical">
  <img alt="Shared packages: top-level packages" src="https://img.shields.io/badge/shared%20packages-top--level%20packages-blue">
  <img alt="New files: frozen" src="https://img.shields.io/badge/new%20files-frozen-critical">
  <img alt="Disposition: remove or govern" src="https://img.shields.io/badge/disposition-remove%20or%20govern-blueviolet">
</p>

**Status:** draft, repository-grounded drift guard<br>
**Path:** `apps/packages/README.md`<br>
**Owning root:** `apps/` by physical placement; no deployable authority granted<br>
**Canonical shared-library root:** [`../../packages/`](../../packages/README.md)<br>
**Default action:** freeze expansion; prefer transparent removal after verification<br>
**Quick links:** [Purpose](#purpose) · [Current evidence](#current-repository-evidence) · [Placement](#directory-rules-and-repository-fit) · [Classification](#classification-and-disposition) · [Workspace risk](#workspace-and-import-activation-risk) · [Freeze](#freeze-contract) · [Validation](#validation-and-negative-cases) · [Removal](#removal-migration-and-transitional-exception) · [Done](#definition-of-done) · [Open](#open-verification-register)

> [!IMPORTANT]
> **CONFIRMED:** `apps/` owns deployable applications; top-level `packages/` owns shared reusable libraries; the root JavaScript manifest selects immediate `apps/*` and `packages/*` children; the current root Python wheel targets `src/kfm`; no package manifest or Python package marker was found at three checked `apps/packages/` activation paths.
>
> **PROPOSED:** classify this path as a dormant workspace risk and freeze it against any file other than this README or a separately approved migration/deprecation pointer.
>
> **UNKNOWN / NEEDS VERIFICATION:** exhaustive recursive contents, every historical or external consumer, branch protection, explicit owner, and the final decision to remove or retain temporarily.

> [!CAUTION]
> Do not add `package.json`, `pyproject.toml`, `setup.py`, `setup.cfg`, `__init__.py`, source code, tests, generated output, runtime configuration, or package-manager metadata here. Such a change would convert a documented anomaly into an implementation surface and could create a shadow package root or workspace without an accepted placement decision.

---

## Purpose

This README is a **drift guard**, not a package README and not an app README in the ordinary implementation sense.

It exists to:

1. make the path anomaly visible;
2. prevent top-level `packages/` authority from being duplicated beneath `apps/`;
3. prevent an immediate `apps/*` workspace selector from silently normalizing this child as a package location;
4. prevent Python namespace or build-discovery drift from reappearing here;
5. keep public, policy, data, release, evidence, schema, contract, runtime, and deployment authority out of the lane;
6. define the evidence required before removal or temporary retention;
7. preserve a reversible, reviewable disposition path.

This README does **not** establish that the directory is needed. Documentation presence is not a retention decision.

---

## Current repository evidence

### Status matrix

| Surface | Evidence | Status | Safe conclusion |
|---|---|---:|---|
| Target README | `apps/packages/README.md` exists; prior blob `f96476a0…` | **CONFIRMED** | Existing document is being revised in place. |
| Initial lane history | Commit `8e262da9…` replaced an empty file with the original drift guard | **CONFIRMED** | The path was documented as an anomaly, not introduced as a working package. |
| Canonical app map | Directory Rules §7.1 lists governed API, Explorer Web, review console, CLI, workers, and admin; it does not list `apps/packages/` | **CONFIRMED** | This path has no canonical deployable-app role. |
| Canonical package root | Directory Rules §7.2 and `packages/README.md` assign reusable libraries to top-level `packages/` | **CONFIRMED** | Shared code does not belong here. |
| Apps-root index | `apps/README.md` names this path as a drift guard/anomaly | **CONFIRMED** | Parent documentation does not grant implementation authority. |
| JavaScript workspace selector | Root `package.json` declares `apps/*` and `packages/*` workspaces | **CONFIRMED** | Every immediate app child is inside a workspace-selection pattern; manifest creation here is a concrete activation risk. |
| Local JavaScript manifest | `apps/packages/package.json` returned not found at the pinned base | **CONFIRMED checked absence** | No checked JavaScript workspace package is established here. |
| Local Python manifest | `apps/packages/pyproject.toml` returned not found | **CONFIRMED checked absence** | No checked Python distribution is established here. |
| Python namespace marker | `apps/packages/__init__.py` returned not found | **CONFIRMED checked absence** | No checked regular Python package marker is established here. |
| Current root Python build | Root `pyproject.toml` uses Hatchling and packages only `src/kfm` | **CONFIRMED** | Current root wheel configuration does not intentionally package `apps/packages/`. |
| Historical Python discovery | Commit `c9c1b7ef…` temporarily broadened setuptools discovery to `apps*`, `packages*`, `runtime*`, and `tools*` | **CONFIRMED history / superseded current behavior** | Broad namespace discovery is a demonstrated drift mode and must not be reintroduced casually. |
| UI workflow | `ui-build` runs on every PR with read-only permission and currently fails closed on unrelated Explorer Web workspace readiness | **CONFIRMED** | A PR check may fail even when this README is structurally valid; success/failure is not app/package authority. |
| Docs workflow | `docs-build` is an explicit read-only readiness hold; it does not render or publish docs | **CONFIRMED** | A green hold is not documentation publication or completeness proof. |
| Review routing | `.github/CODEOWNERS` has a default owner and explicit routes for canonical app/package lanes, but no explicit `apps/packages/` pattern | **CONFIRMED** | The anomaly lacks a dedicated visible review route; default routing is not independent approval. |
| Overlapping work | No matching open PR or branch surfaced in bounded searches | **CONFIRMED bounded result** | No known concurrent update blocks this revision. |
| Recursive lane inventory | Connector exact probes and history were available; recursive directory enumeration was not | **UNKNOWN / NEEDS VERIFICATION** | Do not claim permanent README-only status without a checkout or tree inventory. |

### Evidence limit

The strongest current statement is:

> **`apps/packages/` is README-only in bounded evidence and has no checked activation manifest.**

Do not upgrade that sentence to “the directory is empty except for README” until a recursive tree or checkout proves it at the reviewed commit.

---

## Directory Rules and repository fit

Directory Rules encode responsibility by root:

```text
apps/       = deployable application boundaries
packages/   = reusable shared implementation libraries
tools/      = long-lived validators, generators, and operator tooling
pipelines/  = executable lifecycle transformations
runtime/    = local/provider adapters behind governed interfaces
```

The canonical `apps/` map contains:

```text
apps/governed-api/
apps/explorer-web/
apps/review-console/
apps/cli/
apps/workers/
apps/admin/
```

The canonical reusable-library map is top-level:

```text
packages/<package-name>/
```

`apps/packages/` therefore fails both normal placement tests:

- it is not a named deployable application;
- it is not the canonical shared-library root.

### Directory Rules basis for keeping this README temporarily

Retaining the README is justified only as a **small, reversible drift warning** while the path is inspected and dispositioned. It must not become a compatibility root by assertion.

Directory Rules recognize compatibility classes such as `legacy`, `mirror`, `deprecated`, `external-export`, and `transitional`. No evidence inspected here assigns one of those accepted classes to `apps/packages/`.

Accordingly:

| Claim | Status |
|---|---:|
| `apps/packages/` is a canonical app | **DENIED** |
| `apps/packages/` is the shared-package root | **DENIED** |
| `apps/packages/` is an accepted compatibility root | **NOT ESTABLISHED** |
| The README may warn against drift pending disposition | **PROPOSED bounded exception** |
| The directory should be removed if no consumer or migration need exists | **PROPOSED preferred outcome** |
| Temporary retention may be allowed by ADR/migration record | **PROPOSED exception** |

No new root, authority family, lifecycle stage, public path, or compatibility authority is created by this document.

---

## Classification and disposition

### Current proposed classification

```text
dormant-workspace-risk / deprecation-candidate
```

Meaning:

- the path exists;
- no checked activation manifest exists;
- its name collides semantically with the canonical top-level `packages/` root;
- it sits beneath a broad immediate-child workspace selector;
- it has no accepted app identity;
- it should remain frozen while removal or a temporary migration exception is reviewed.

This label is descriptive, not a new Directory Rules compatibility class.

### Allowed long-term outcomes

Only two outcomes are sound:

| Outcome | Required support | Default posture |
|---|---|---|
| **Remove** | recursive inventory, import/build/reference search, parent-link update, review, rollback commit | **Preferred when no dependency exists** |
| **Transitional exception** | accepted ADR or migration note, named owner, exact consumers, target canonical home, expiry, tests, workspace/import controls, rollback | **Fail closed until complete** |

The following are not acceptable outcomes:

- indefinite “just in case” retention;
- adding shared utilities because the folder already exists;
- adding an app package manifest to make tooling convenient;
- allowing workspace discovery to decide architecture;
- treating the README as an ADR;
- treating a passing build as placement approval.

---

## Authority boundary

This lane owns no implementation or governance authority beyond documenting the anomaly.

| Responsibility | Owning home | `apps/packages/` authority |
|---|---|---:|
| Deployable service/UI/CLI/worker/admin | `apps/<named-app>/` | **None** |
| Shared reusable library | `packages/<named-package>/` | **None** |
| App-local source | owning app `src/` | **None** |
| JavaScript workspace package | accepted app or top-level package lane | **None** |
| Python distribution/package | accepted package root and manifest | **None** |
| Schema shape | `schemas/contracts/v1/` | **None** |
| Semantic contracts | `contracts/` | **None** |
| Policy/admissibility | `policy/` | **None** |
| Lifecycle data, receipts, proofs | `data/` | **None** |
| Release, correction, withdrawal, rollback | `release/` | **None** |
| Runtime/model adapters | `runtime/` behind governed API | **None** |
| Source admission | `connectors/` | **None** |
| Pipeline execution/specification | `pipelines/`, `pipeline_specs/` | **None** |
| Repository validators/generators | `tools/` | **None** |
| Deployment/configuration | `infra/`, `configs/` | **None** |
| Public trust membrane | `apps/governed-api/` | **None** |

A file under this path does not inherit package or app legitimacy from the parent folder name.

---

## Workspace and import activation risk

### JavaScript workspace risk

The root manifest currently contains:

```json
{
  "workspaces": [
    "apps/*",
    "packages/*"
  ]
}
```

`apps/packages/` is an immediate child matching the structural scope of `apps/*`. No local `package.json` was found at the checked base, so an active workspace package is not established. Adding one would place a package manifest inside the selected app-child pattern and could cause package-manager, install, filter, build, test, or dependency-graph behavior to treat this anomaly as a workspace.

Therefore:

- local `package.json` creation is an architecture-significant change;
- workspace activation must not occur as a side effect of scaffolding;
- a package-manager accepting the path does not make the placement valid;
- a future lockfile entry or successful build is not an ADR or migration decision.

### Python import/build risk

The current root Python build config is narrow:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/kfm"]
```

Checked activation files under `apps/packages/` are absent. However, repository history contains a prior broad discovery configuration that included `apps*` and `packages*`. That history demonstrates why the lane must prohibit:

- `__init__.py` namespace activation;
- broad recursive discovery that sweeps in `apps/packages`;
- import compatibility shims without migration tests;
- relying on `PYTHONPATH=.` or editable-install side effects to normalize the path.

Current safety is configuration-specific and reversible; it must be tested, not assumed permanently.

### Activation sentinels

The appearance of any item below is a **review stop** until placement is resolved:

```text
apps/packages/package.json
apps/packages/pnpm-workspace.yaml
apps/packages/pyproject.toml
apps/packages/setup.py
apps/packages/setup.cfg
apps/packages/__init__.py
apps/packages/src/
apps/packages/lib/
apps/packages/tests/
apps/packages/tsconfig.json
apps/packages/vite.config.*
apps/packages/index.*
```

This list is a detection surface, not permission to add unlisted implementation files.

---

## Freeze contract

Until a removal or transitional decision is approved, the lane follows this contract.

### Allowed

- this README;
- a reviewed edit that tightens the drift boundary;
- a pointer to an accepted ADR or migration record after that record exists;
- an explicit deprecation/removal marker when coordinated with parent indexes.

### Denied by default

- implementation source;
- package manifests or workspace metadata;
- app manifests, entry points, routes, workers, or deploy scripts;
- tests local to this anomaly;
- compatibility imports or re-export shims;
- generated files;
- schemas, contracts, policy, receipts, proofs, data, release records, or runtime adapters;
- secrets, credentials, environment files, or private configuration;
- symlinks or path aliases that make canonical tooling resolve here;
- child directories created for future use.

### Review stop conditions

Stop a proposed change when any of these occur:

1. a new non-document file appears under `apps/packages/`;
2. a root workspace/build pattern explicitly names or starts packaging the path;
3. an import, alias, test, script, CI job, or deployment references the path;
4. a package manager writes lock or metadata state for the path;
5. a public app reads through the path;
6. a proposed move lacks a target responsibility root;
7. retention lacks owner, expiry, migration target, tests, and rollback;
8. the path is presented as canonical without an ADR that amends Directory Rules.

---

## Public trust and sensitive-data boundary

`apps/packages/` must never become a shortcut around the trust membrane.

It must not:

- serve public or semi-public traffic;
- load RAW, WORK, QUARANTINE, PROCESSED, catalog, triplet, registry, receipt, proof, or release internals for a client;
- select policy bundles or create policy decisions;
- resolve evidence or generate citations as authority;
- expose living-person, genomic, archaeology, cultural, rare-species, private-land, infrastructure, or exact protected-location detail;
- host AI/model adapters or generated language as truth;
- publish maps, tiles, exports, screenshots, reports, or stories;
- approve release, correction, withdrawal, supersession, or rollback.

Normal public clients continue through `apps/governed-api/` and approved public-safe carriers only.

---

## Dependency and ownership rules

### Dependency direction

```text
apps/<named-app>  -> packages/<named-package>
apps/packages     -X packages authority
apps/packages     -X public clients
apps/packages     -X lifecycle/internal stores
```

No accepted dependency should originate from or target this lane while it remains a drift guard.

### Ownership

Current CODEOWNERS evidence routes this path through the repository default because no explicit `apps/packages/` pattern was found.

That is sufficient for GitHub notification only. It does not establish:

- an Apps steward;
- a Package steward;
- an Architecture steward;
- independent author/reviewer separation;
- required approval rules;
- permission to retain the path.

A future transitional exception should add an explicit review route using only verified GitHub identities. Placeholder role names must not be encoded as executable CODEOWNERS entries.

---

## Validation and negative cases

### Minimum deterministic checks

A future repository-structure test should verify:

1. the only permitted regular file is `README.md`, unless an accepted migration record names another pointer;
2. no activation sentinel exists;
3. no repository import or build reference targets `apps/packages` or `apps.packages`;
4. root workspace/build discovery does not explicitly activate this path;
5. no public app or governed API code reads from the lane;
6. no authority-bearing artifact is stored here;
7. the parent apps index continues to classify the lane as drift until removal;
8. removal or transitional status remains explicit and non-expired.

### Negative cases

| Case | Expected result |
|---|---|
| Add `apps/packages/package.json` | **FAIL / architecture review required** |
| Add `apps/packages/__init__.py` | **FAIL / import-boundary review required** |
| Add reusable helper source | **FAIL; move to top-level `packages/`** |
| Add app-local implementation | **FAIL; move to owning app** |
| Add schema or contract | **FAIL; use canonical authority root** |
| Add release/data/proof/receipt material | **FAIL; use lifecycle/release roots** |
| Add a compatibility shim without expiry/tests | **FAIL** |
| Remove directory without reference inventory | **HOLD** |
| Retain path indefinitely without ADR/migration | **DENY** |
| Workspace/build succeeds with the path | **No authority effect; placement still invalid** |

### Proposed test placement

A structure-boundary test may fit the existing repository policy/boundary test family, but the exact file and workflow binding are **PROPOSED** until the test owner confirms placement. The test should be deterministic and no-network.

### CI limits

The current `ui-build` workflow:

- runs on all pull requests;
- uses hosted runners and read-only repository permission;
- does not deploy or publish;
- currently fails closed because Explorer Web build/test scripts, exact package-manager pinning, and lockfile readiness are incomplete.

Consequently, a failure of `ui-build` on a README-only change may reflect known Explorer Web readiness rather than a defect in this lane. It must not be mislabeled as path-specific validation.

The current `docs-build` workflow is a readiness hold and does not render or publish this document.

---

## Removal, migration, and transitional exception

### Preferred removal sequence

Removal is the preferred outcome when no consumer exists.

1. Pin the reviewed base commit.
2. Recursively inventory `apps/packages/`.
3. Search repository imports, aliases, workspaces, package-manager metadata, CI, tests, deployment, docs, and external compatibility notes.
4. Confirm no runtime or external consumer depends on the path.
5. Update `apps/README.md` and any navigation that links to this README.
6. Remove the directory in one scoped review branch.
7. Run structure, link, workspace, import, UI, and repository checks.
8. Preserve the removal commit and prior blob as rollback targets.
9. Record the disposition in an accepted migration/deprecation register if the repository adopts one.

Do not leave a broken parent link or silent tombstone.

### Transitional exception requirements

If a real consumer requires temporary retention, the exception must state:

| Field | Requirement |
|---|---|
| Classification | `transitional` or another Directory Rules-recognized class |
| Governing record | Accepted ADR or migration note |
| Owner | Verified responsible identity and stewardship assignment |
| Consumer inventory | Exact imports, workspaces, scripts, CI, deployments, or external users |
| Canonical destination | Existing responsibility-root path checked against Directory Rules |
| Compatibility surface | Exact files and behavior retained temporarily |
| Security posture | No secrets, public bypass, internal-store shortcut, or sensitive-data leak |
| Tests | Positive compatibility and negative bypass/activation cases |
| Expiry/removal trigger | Date, version, consumer migration, or other deterministic condition |
| Rollback | Revert target and forward-remediation path |
| Review | Apps + package + architecture + affected security/runtime reviewers |

Directory presence alone satisfies none of these requirements.

### Migration rules

- Shared reusable code moves to top-level `packages/<name>/`.
- App-local code moves into the owning named app.
- One-off scripts move to `tools/`, `scripts/one_off/`, or `pipelines/` according to duration and responsibility.
- Runtime adapters move to `runtime/` behind governed interfaces.
- Tests move to the owning app/package test lane or accepted repository test family.
- Authority-bearing content moves to its canonical root with an ADR/migration note when necessary.

A move is not complete until imports, build manifests, lockfiles, workflows, docs, tests, ownership, and rollback references are updated.

---

## Smallest sound implementation sequence

The next useful implementation work is intentionally small:

1. **Keep the freeze visible.** Merge this README revision without adding code.
2. **Add a recursive inventory receipt/report.** Use a mounted checkout or tree API; record exact files and references.
3. **Add a deterministic drift guard.** Fail when activation sentinels or imports appear.
4. **Make review routing explicit.** Add a verified path-specific CODEOWNERS rule if the path remains during review.
5. **Choose disposition.** Remove when unused; otherwise accept a time-bounded migration record.
6. **Execute the disposition in a separate PR.** Update parent navigation, tests, and rollback together.

Do not scaffold a package merely to make the path appear purposeful.

---

## Definition of done

This README update is complete when:

- [x] The stable `doc_id` and existing path are preserved.
- [x] `apps/` and top-level `packages/` responsibilities are grounded in current Directory Rules and root READMEs.
- [x] The JavaScript workspace-selector risk is documented.
- [x] Current Python build posture and historical broad-discovery drift are separated.
- [x] Checked absent activation paths are recorded without overstating recursive inventory.
- [x] The lane is frozen against new authority and implementation.
- [x] Removal and transitional-exception paths are reversible and explicit.
- [x] Current CI limitations are disclosed.
- [ ] Named owners are accepted.
- [ ] A recursive inventory is captured.
- [ ] A deterministic drift test exists and runs in CI.
- [ ] A dedicated verified review route exists while the path remains.
- [ ] The final remove-or-transitional decision is approved.
- [ ] Parent navigation is updated if the path is removed.

---

## Open verification register

| ID | Question | Why it matters | Status |
|---|---|---|---:|
| `APP-PKG-01` | Is `README.md` truly the only current file in the lane? | Required for exact classification and removal | **NEEDS VERIFICATION** |
| `APP-PKG-02` | Do any imports, aliases, scripts, tests, CI jobs, lockfiles, or external users reference the path? | Required before removal | **NEEDS VERIFICATION** |
| `APP-PKG-03` | How do all supported package managers interpret an immediate app child without a manifest? | Prevents tooling-specific activation surprises | **NEEDS VERIFICATION** |
| `APP-PKG-04` | Should the root workspace selector be narrowed or guarded? | Prevents future manifest activation | **PROPOSED / NEEDS VERIFICATION** |
| `APP-PKG-05` | Is transparent removal preferred by maintainers? | Resolves indefinite anomaly retention | **UNKNOWN** |
| `APP-PKG-06` | Does any accepted ADR or migration record require temporary compatibility? | Required to classify as transitional | **NOT ESTABLISHED** |
| `APP-PKG-07` | Which verified GitHub identities should review the path? | Makes drift review visible | **NEEDS VERIFICATION** |
| `APP-PKG-08` | Which accepted test family should own the drift guard? | Required for enforceable freeze | **NEEDS VERIFICATION** |
| `APP-PKG-09` | Are branch protection and required checks configured for this path? | Prevents bypass of review gates | **UNKNOWN** |
| `APP-PKG-10` | Have historical broad Python discovery assumptions been fully retired from docs/scripts? | Prevents regression to `apps*` packaging | **NEEDS VERIFICATION** |

---

## Evidence ledger

| Evidence | Observation used | Truth label |
|---|---|---:|
| `apps/packages/README.md@5cf7386b…` | Existing v0.1 drift guard and prior identity | **CONFIRMED** |
| `apps/README.md@5cf7386b…` | Deployable root; path identified as anomaly | **CONFIRMED** |
| `packages/README.md@5cf7386b…` | Top-level shared reusable package authority | **CONFIRMED** |
| `docs/architecture/directory-rules.md@5cf7386b…` | Canonical apps map, packages root, compatibility discipline | **CONFIRMED live artifact; document status remains review** |
| `package.json@5cf7386b…` | `apps/*` and `packages/*` workspace selectors | **CONFIRMED** |
| `pyproject.toml@5cf7386b…` | Current Hatch wheel packages only `src/kfm` | **CONFIRMED** |
| exact probes for local manifests/marker | `package.json`, `pyproject.toml`, `__init__.py` not found | **CONFIRMED checked absence** |
| commit `8e262da9…` | Original README replaced an empty file | **CONFIRMED history** |
| commit `c9c1b7ef…` | Historical broad Python discovery included `apps*` | **CONFIRMED history / superseded** |
| `.github/workflows/ui-build.yml` | All-PR read-only readiness failure posture | **CONFIRMED** |
| `.github/workflows/docs-build.yml` | Read-only documentation readiness hold | **CONFIRMED** |
| `.github/CODEOWNERS` | Default route; no path-specific anomaly route | **CONFIRMED** |
| branch and PR searches | No overlapping open work surfaced | **CONFIRMED bounded result** |
| recursive lane contents and all consumers | Not fully enumerable in connector session | **UNKNOWN / NEEDS VERIFICATION** |

---

## Rollback and maintenance

### Rollback

Before merge, close the review PR or reset/delete its branch. After merge, revert the README commit and generated-work receipt commit in reverse order. The prior README blob is:

```text
f96476a05d8eba03e538fe9f9053d7e0e5a77033
```

Rollback restores documentation only. It does not authorize package activation or settle disposition.

### Maintenance triggers

Review this README when any of the following changes:

- a file appears under `apps/packages/`;
- root workspaces or package-manager tooling changes;
- Python package discovery changes;
- an import/build/deployment reference appears;
- Directory Rules changes app or package placement;
- an ADR/migration record is accepted;
- CODEOWNERS or branch protection changes;
- the path is removed;
- a recursive inventory proves a different current state.

### No-loss preservation note

The v0.1 README already established the essential rule: this path must not become a shadow package root. v0.2 preserves that rule and adds current repository evidence, workspace/import activation risks, a strict freeze, removal/transitional decision criteria, validation expectations, CI limits, explicit rollback, and an evidence ledger.

The old statement that all contents beyond the README were simply unknown is narrowed, not erased: exact activation probes are now confirmed absent, while exhaustive recursive inventory remains `NEEDS VERIFICATION`.

---

## Changelog

### v0.2 — 2026-07-19

- pinned current repository evidence and prior blob;
- classified the lane as a dormant workspace risk/deprecation candidate;
- documented root JavaScript workspace selectors;
- documented current narrow Python build and historical broad-discovery drift;
- recorded checked absent activation files;
- established a freeze contract and activation sentinels;
- separated removal from ADR-backed transitional retention;
- added deterministic validation and negative cases;
- documented CODEOWNERS and CI limitations;
- added implementation sequence, definition of done, open register, evidence ledger, and rollback.

### v0.1 — 2026-06-16

- replaced an empty README with the initial bounded drift-guard contract.

<p align="right"><a href="#top">Back to top</a></p>
