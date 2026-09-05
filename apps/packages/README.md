<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/apps-packages/readme
title: apps/packages/ — Dormant Workspace-Risk and Drift-Guard Boundary
type: directory-readme; architecture-drift-guard; deprecation-candidate
version: v0.3
status: draft; repository-grounded; non-implementation; disposition-open
owners: "OWNER_TBD — Apps, Package, Architecture, Build, Security, Validation, and Docs stewards"
created: 2026-06-16
updated: 2026-09-05
policy_label: public
current_path: apps/packages/README.md
owning_root: apps/
responsibility: "Document the existing non-implementation lane and route contributors to the correct responsibility owner without activating, removing, or reclassifying it."
authority_level: drift-guard-only
truth_posture: "CONFIRMED pinned files and configuration; PROPOSED future enforcement and disposition; UNKNOWN complete consumers and independent review controls"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: cbd6d82bad962a58ab62cfb776ee31696b575107
  target_prior_blob: 5a9f5b2b7019cca476631cad3533bbdc2dbc9199
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  apps_readme_blob: 95b3b021cad9bcafbd53fd1ddd18f6b51df22d80
  packages_readme_blob: 7b672f4d834b648f4b30ce7e2e9a5e214efa2c71
  workspace_yaml_blob: 3eece3b536797f3bee593b2ce286964b62cc5391
  root_package_blob: 5cba790c88c40b885cc65fe2d585f3205aa1ef9d
  root_python_blob: cbfc1af273f125caca0c2eea055af1ad39baf2b8
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  inventory_method: "Complete GitHub contents listing for this two-file directory; no child directories returned"
  tracked_lane_files:
    - apps/packages/.gitkeep
    - apps/packages/README.md
related:
  - ../README.md
  - ../../packages/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../CONTRIBUTING.md
  - ../../package.json
  - ../../pnpm-workspace.yaml
  - ../../pnpm-lock.yaml
  - ../../pyproject.toml
  - ../../.github/CODEOWNERS
  - ../../.github/PULL_REQUEST_TEMPLATE.md
  - ../../data/receipts/generated/README.md
tags: [kfm, apps, packages, drift-guard, workspace-boundary, non-implementation, reversible-change]
notes:
  - "v0.3 corrects the earlier README-only inventory: the pinned tree also contains an empty .gitkeep. Neither file is changed into implementation."
  - "ADR-0029 adopts the pinned v2 doctrine despite its retained PROPOSED_FOR_ADOPTION source label. The architecture-path rules copy remains read-only compatibility."
  - "This README describes a boundary; it is not an executable workspace exclusion, import guard, accepted migration decision, or release gate."
  - "Historical receipts remain unchanged. New authoring provenance belongs in data/receipts/generated/, not inside this lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `apps/packages/` — Dormant Workspace-Risk and Drift-Guard Boundary

**Looking for reusable code? Use [top-level `packages/`](../../packages/README.md).**
For deployable applications, use the [parent application index](../README.md).
This directory is a retained drift warning, not an app, a shared-library root,
or an accepted compatibility package.

**Status:** documentation-only lane; implementation expansion held; final disposition open.
**Evidence:** `main@cbd6d82bad962a58ab62cfb776ee31696b575107`, inspected 2026-09-05.

[Purpose](#purpose) · [Evidence](#current-repository-evidence) ·
[Placement](#directory-rules-and-repository-fit) ·
[Workspace risk](#workspace-and-import-activation-risk) ·
[Validation](#validation-and-negative-cases) ·
[Disposition](#removal-migration-and-transitional-exception) ·
[Open work](#open-verification-register)

> [!IMPORTANT]
> The pinned directory contains exactly `README.md` and an empty `.gitkeep`,
> with no child directories. It contains no package manifest, source, local
> tests, build configuration, or runtime implementation. This is a statement
> about tracked files at the named commit, not every workstation or future ref.

> [!CAUTION]
> Do not scaffold an application or package here. A workspace glob, successful
> import, passing CI job, or existing directory does not grant placement authority.
> Corrective documentation and safe branch authoring remain possible; activating
> or removing this lane requires a separately reviewed scope.

## Purpose

Keep the `apps/` and `packages/` responsibilities distinct, make the anomalous
path visible, and preserve a reviewable route to removal or a bounded migration
exception. This README is navigation and drift documentation, not a package API,
installation guide, deployable identity, normative policy, or retention decision.

## Current repository evidence

### Status matrix

All source observations below use the pinned commit above. Definitions of checks
and manifests are distinguished from executed checks.

| Surface | CONFIRMED observation | Limit |
|---|---|---|
| Directory | Two regular files: `README.md` and zero-byte `.gitkeep`; no child directories | Does not inventory untracked or external files |
| Parent guidance | `apps/README.md` identifies this child as a drift guard, not a shared-package authority | A navigation entry is not app admission |
| Shared root | `packages/README.md` assigns reusable implementation to top-level `packages/` | This child does not inherit that role |
| pnpm workspace | `pnpm-workspace.yaml` selects `apps/*` and `packages/*`; it also records version-specific `allowBuilds` decisions | Selection patterns and script approval are different controls |
| Lockfile | The complete `importers` mapping has no `apps/packages` entry | A source inspection, not an installation experiment |
| Root JavaScript manifest | Pins `pnpm@11.17.0` and Node `>=22.13 <23`; repeats the workspace patterns | Root generic lint/test/build scripts intentionally fail with `WORKFLOW_HOLD` |
| Root Python manifest | Hatch wheel packages `src/kfm`; the source-distribution include list is explicit | Packaging configuration is not universal Python import isolation |
| Review route | CODEOWNERS catch-all is `@bartytime4life`; no explicit `/apps/packages/` rule | Routing is not an accepted steward assignment or independent approval |
| References | Parent/package READMEs and historical receipts reference this path; search also returns prose meaning “apps and packages” | Matches must be classified; zero-consumer closure is not established |

### Evidence limit

The v0.2 claim **“README-only in bounded evidence”** is superseded for this
snapshot. The exact result is **README plus empty `.gitkeep`, no implementation**.
The existing marker is retained unchanged; it is neither a package entrypoint
nor permission to add other files.

No package-manager execution, wheel build, exhaustive import audit, complete
external-consumer inventory, hosted validation of this revision, or live runtime
inspection is established by this README. A dedicated activation guard has not
been verified; the proposed checks below must not be described as deployed CI.

## Directory Rules and repository fit

Use [Directory Rules v2](../../docs/doctrine/directory-rules.md), particularly
implementation-role routing, dependency direction, README inheritance, and
migration rules, together with
[accepted ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

ADR-0029 adopts the exact doctrine blob `fd49a0b83e55cef52c1124281f093e263526898d`.
Its retained `PROPOSED_FOR_ADOPTION` header is part of the adopted bytes; it is
not evidence that adoption is still pending. The older
`docs/architecture/directory-rules.md` remains read-only compatibility, not the
current writable rules source.

| Responsibility | Correct routing |
|---|---|
| Deployable process or user interface | An existing, named application under `apps/` |
| Reusable implementation across consumers | An appropriate top-level `packages/` lane |
| Code used only by one app | That app's existing source boundary |
| Repository-wide validator or generator | Existing `tools/` responsibility |
| Source acquisition | Existing `connectors/` responsibility |
| Lifecycle transformation or run specification | `pipelines/` or `pipeline_specs/`, respectively |
| Provider composition or deployment | `runtime/` or `infra/`, respectively |

These are routing rules, not instructions to create the example lanes.
Verify the concrete destination and applicable ADR before moving or adding files.

### Directory Rules basis for keeping this README temporarily

This is a same-path maintenance edit under `apps/`, following the parent and
canonical package-root drift guidance. It does not adopt a new compatibility
class, authorize permanent retention, create package authority, or remove the
path. The authoring receipt belongs in the existing
[`data/receipts/generated/`](../../data/receipts/generated/README.md) accountability
lane; receipts are process memory, not proof or approval.

## Classification and disposition

### Current proposed classification

`dormant-workspace-risk / deprecation-candidate` remains a descriptive label.
It is not a newly accepted Directory Rules class or a package-manager state.
The implementation freeze comes from the existing lane/parent boundaries; this
revision does not claim that a machine guard enforces it.

### Allowed long-term outcomes

Prefer removal after consumer and navigation closure, or retain only a reviewed,
time-bounded transitional exception with a demonstrated need. The choice remains
**PROPOSED / disposition open**. Do not turn the lane into a shared utility dump,
activate it to satisfy a tool, or treat indefinite retention as approved.

## Authority boundary

This lane owns only its drift explanation. Contracts retain semantic meaning;
schemas retain machine shape; policy retains admissibility; governed data lanes
retain lifecycle, evidence, receipt and proof records; release retains release,
correction and rollback decisions. App, package, source, pipeline, runtime and
infrastructure implementation stay with their respective owners.

No new contract, schema, policy, source registry, receipt/proof store, release
home, public route or model integration belongs beneath `apps/packages/`.

## Workspace and import activation risk

### JavaScript workspace risk

[`pnpm-workspace.yaml`](../../pnpm-workspace.yaml) is the inspected pnpm workspace
configuration. Its `apps/*` pattern covers this immediate child structurally,
but the directory has no `package.json` and the lockfile has no matching importer.
Adding a manifest could activate it in workspace discovery. That is a risk to
review, not a behavior tested by this documentation change.

The version-specific `allowBuilds` map approves or denies dependency scripts;
it does **not** exclude this directory from workspace discovery. Preserve those
decisions and frozen-lockfile discipline. Do not broaden script approvals, add
an importer, change workspace globs, or install dependencies merely to update
this README. Use the actual owning app/package instructions for implementation.

### Python import/build risk

[`pyproject.toml`](../../pyproject.toml) specifies:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/kfm"]
```

Its source-distribution include list also excludes this lane. These are build
configuration facts, not proof that every interpreter or test environment denies
imports from repository directories. In particular, the root pytest settings
add `.` to the Python path. Absence of `__init__.py` alone is not a universal
namespace-import guard.

The v0.2 discussion of historical broad setuptools discovery is retained as
lineage in Git history, not reasserted as current configuration. Any proposed
change to discovery, aliases, editable installation or import paths needs tests
for its actual supported environment.

### Activation sentinels

Treat a new package/build manifest, Python marker, source module, re-export,
symlink, alias, local test, lockfile importer or deployment reference as a
placement-review trigger. Examples such as `package.json`, `pyproject.toml`,
`setup.py`, `setup.cfg`, `__init__.py`, `src/`, `lib/` and `tests/` are **prohibited
candidate additions here**, not a scaffold plan or an exhaustive detection list.

## Freeze contract

### Allowed

Maintain this README, preserve the already-tracked empty `.gitkeep`, and link to
an accepted disposition record when one exists. A scoped corrective document
edit is not implementation activation. A future removal may delete the marker
and README only with its own reviewed navigation and rollback scope.

### Denied by default

Do not add implementation, package/workspace metadata, tests, imports, aliases,
symlinks, generated output, lifecycle data, authority-bearing records, secrets,
private configuration or speculative child directories. The empty marker is a
specific observed retention, not a general exception for non-document files.

### Review stop conditions

Stop the affected activation or disposition when a proposed file or reference
makes this lane executable, changes packaging/discovery, creates a public bypass,
claims canonical status, or lacks a verified destination and rollback. Do not
apply these stops to unrelated safe authoring or treat this README as permission
to modify repository settings, validators or policy.

## Public trust and sensitive-data boundary

Public clients use governed APIs or reviewed released artifacts. This lane must
not expose internal lifecycle stores, direct model endpoints, protected geometry,
living-person/DNA data, archaeological or cultural detail, rare-species locations,
private-land detail or sensitive infrastructure. Unclear rights or sensitivity
stay with the appropriate quarantine, redaction, generalization or denial process.

Preserve `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`,
`EvidenceRef -> EvidenceBundle`, and cite-or-abstain. Maps, tiles, indexes,
scenes, exports and generated language are carriers, not evidence or publication
authority. This directory is not a shortcut around those controls.

## Dependency and ownership rules

### Dependency direction

Named apps consume appropriate shared packages; shared packages must not use
this anomaly as an intermediate import root. Documentation links and immutable
historical receipt references are not runtime dependencies and must not be
blindly rejected or rewritten by a string-only search.

### Ownership

[`CODEOWNERS`](../../.github/CODEOWNERS) supplies the current default review route,
not a named stewardship assignment, mandatory independent approval or proof of
review. No dedicated rule is added here. Any future exception requires verified
responsible owners and actual review controls; repeating the same account in
another pattern does not create independence.

## Validation and negative cases

### Minimum deterministic checks

For this documentation-only scope, check metadata, headings, anchors, relative
links, fences, whitespace, final newline, the exact changed paths, and the new
receipt's schema and artifact digest. Keep the marker unchanged. Report executed
checks separately from source inspection and from unrun native/hosted checks.

For a future executable guard, **PROPOSED** acceptance requirements are: a
non-vacuous inventory, exact regular-file allowlist (`README.md` plus the existing
zero-byte `.gitkeep` while retained), no symlinks or extra children, no package
activation, and context-aware import/build-reference checks. Its tests must reject
changed marker bytes as well as new implementation; documentation and historical
receipts must remain distinguishable from executable consumers.

Read-only inspection commands for a real checkout, from repository root:

```bash
BASE=cbd6d82bad962a58ab62cfb776ee31696b575107
# Expected tracked names: apps/packages/.gitkeep and apps/packages/README.md.
git ls-tree -r --name-only "$BASE" -- apps/packages/
git show "$BASE:pnpm-workspace.yaml"
git show "$BASE:pyproject.toml"
# Classify matches; grep exit 1 means no match, not an execution error.
if git grep -n -F -e 'apps/packages' -e 'apps.packages' "$BASE" -- .; then
  :
else
  rc=$?
  test "$rc" -eq 1
fi
git diff --check
```

These commands are an inspection recipe, not an installed drift validator or a
claim that a complete checkout was available for this authoring session.

### Negative cases

| Proposed guard case | Expected disposition |
|---|---|
| New manifest, source, re-export, symlink or local test | Reject expansion; route work to its owner |
| Existing `.gitkeep` becomes non-empty | Reject unreviewed content, not grandfather it |
| Lockfile/import/build alias activates the lane | Require separately reviewed placement and consumer tests |
| README or historical receipt references the path | Classify as documentation/lineage; not automatically an import violation |
| Removal leaves current navigation broken | Hold removal until links and consumers close |
| Build succeeds after unapproved activation | No placement or release authority follows |

### Proposed test placement

Use the existing repository-level validator/test responsibilities, after checking
adjacent conventions and overlap. Exact new paths and CI wiring remain
**PROPOSED**. Do not put executable tests under this frozen directory and do not
weaken a topology baseline to make new activation appear conformant.

### CI limits

[`ui-build.yml`](../../.github/workflows/ui-build.yml) now defines a real, locked
Explorer build/test lane. The earlier claim that scripts, the pnpm pin and
lockfile are missing is obsolete. A workflow definition does not establish the
result for this change; failing checks require exact-head and comparable-base
evidence before they may be called inherited.

[`docs-build.yml`](../../.github/workflows/docs-build.yml) still contains explicit
generator and preview readiness holds. A successful held job does not prove
that this Markdown was rendered, accessible or published. The generic root
JavaScript scripts are also explicit holds, not package-wide validation.

No passing result, merge, document badge or receipt authorizes package activation,
source admission, review approval, deployment or publication.

## Removal, migration, and transitional exception

### Preferred removal sequence

Re-pin the current tree; finish repository and external-consumer checks; obtain
the appropriate disposition review; update parent/package navigation and other
active links; remove the README and marker together; validate affected links,
imports, discovery and consumers; record a specific revert target. Preserve
historical receipts and source pins rather than rewriting their original hashes.
No removal is performed by this update.

### Transitional exception requirements

A justified exception needs an accepted ADR or applicable migration record,
verified owner, exact retained files and consumers, canonical destination,
compatibility contract, rights/security constraints, positive and negative tests,
expiry or deterministic retirement trigger, and rollback. A README, workspace
entry or successful build supplies none of those approvals by itself.

### Migration rules

Route content by responsibility, not by the word “packages.” Close affected
imports, build manifests, lockfiles, tests, workflows, documentation, ownership
and rollback together. Respect compatibility holds elsewhere; this child-lane
update does not migrate the Directory Rules compatibility copy or any root.

## Smallest sound implementation sequence

This revision closes the tracked-file inventory gap and refreshes the guide.
The next separate slice is to establish actual consumers and select either
removal with navigation repair or a justified bounded guard/exception. Do not
add tooling, ownership patterns or a package merely to give this directory work.

Branch authoring, draft delivery, readiness, review and merge remain distinct.
Follow current [CONTRIBUTING.md](../../CONTRIBUTING.md) and the
[PR template](../../.github/PULL_REQUEST_TEMPLATE.md). An incident-quarantined
PR-state path stops at a validated branch until the required independent
one-shot draft-delivery boundary is proven. Documentation does not clear it.

## Definition of done

For this update: preserve document identity and anchors; describe the two-file
inventory accurately; cite adopted placement authority; separate workspace
selection from script approval; correct CI claims; retain all trust boundaries;
bind the new README bytes in a pending-review receipt; and report actual delivery
and validation without claiming a PR, test or merge that did not occur.

Final disposition, a dedicated executable guard, accepted stewards, complete
consumer closure and independent review controls remain separate open work.

## Open verification register

| ID | Current disposition | First affected transition |
|---|---|---|
| `APP-PKG-01` | **CONFIRMED:** README and empty `.gitkeep`, no descendants at the pin; earlier single-file premise corrected | Re-inventory when the ref changes |
| `APP-PKG-02` | **NEEDS VERIFICATION:** complete imports, aliases, automation and external consumers | Removal or activation |
| `APP-PKG-03` | **NEEDS VERIFICATION:** behavior of each supported packaging/import tool | Tooling or packaging changes |
| `APP-PKG-04` | **PROPOSED:** executable guard or selector change only if justified | Enforcement implementation |
| `APP-PKG-05` | **UNKNOWN:** final maintainer removal/retention decision | Disposition |
| `APP-PKG-06` | **NEEDS VERIFICATION:** accepted, unexpired transitional need | Compatibility admission |
| `APP-PKG-07` | **CONFIRMED:** default CODEOWNERS route; **UNKNOWN:** accepted stewards and independent approval | Stewardship or approval claims |
| `APP-PKG-08` | **NEEDS VERIFICATION:** dedicated guard, test owner and CI wiring | Enforced-freeze claims |
| `APP-PKG-09` | **UNKNOWN:** sufficient independent PR-state and merge controls | Draft delivery through an implicated path; later integration |
| `APP-PKG-10` | **NEEDS VERIFICATION:** all historical discovery assumptions retired from active consumers | Broad packaging/import changes |

## Evidence ledger

The relative links below resolve in the reader's checkout. The immutable source
pin for every observation is `cbd6d82bad962a58ab62cfb776ee31696b575107`; nearby
READMEs may retain older evidence dates and do not override current source bytes.

| Source | Use |
|---|---|
| GitHub directory inventory for `apps/packages/` | Complete two-file tracked surface, including zero-byte marker |
| [Parent apps README](../README.md), [shared packages README](../../packages/README.md) | Drift classification and responsibility routing |
| [Directory Rules](../../docs/doctrine/directory-rules.md), [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopted placement authority and compatibility limitation |
| [Root manifest](../../package.json), [workspace YAML](../../pnpm-workspace.yaml), [lockfile](../../pnpm-lock.yaml) | Workspace selection, importer absence, separate script policy |
| [Python manifest](../../pyproject.toml) | Wheel/source distribution and pytest path configuration |
| [CODEOWNERS](../../.github/CODEOWNERS), [contributor guide](../../CONTRIBUTING.md) | Routing, review and delivery limitations |
| [UI workflow](../../.github/workflows/ui-build.yml), [docs workflow](../../.github/workflows/docs-build.yml) | Declared checks versus explicit readiness holds |
| [GeneratedReceipt lane](../../data/receipts/generated/README.md) | Authoring provenance, pending review and non-authority |

Google Drive's *Directory Rules* was consulted as design lineage; the Notion
*KFM Repository Workbench* was consulted as coordination. Neither replaces
adopted GitHub doctrine or current implementation evidence. No private page
content or source document is copied into this lane.

## Rollback and maintenance

### Rollback

Revert only this update's README/receipt commit as one unit, preserving Git
history. The prior README blob is `5a9f5b2b7019cca476631cad3533bbdc2dbc9199`.
The existing `.gitkeep`, historical receipts, packages, manifests and workflows
remain unchanged. Rollback restores documentation; it does not authorize
activation, delete a consumer, or require a data/deployment migration.

### Maintenance triggers

Reinspect on tracked-content, workspace/import/distribution, consumer, accepted
ADR, owner, delivery-control or disposition changes. Check the affected ref and
actual results; do not refresh an evidence date without refreshing its basis.

### No-loss preservation note

The original no-shadow-package rule, public trust boundary, activation risks,
negative-test requirements, disposition choices and rollback remain intact.
Earlier source snapshots and broad-discovery history remain in Git and immutable
receipts. v0.3 corrects currentness without relabeling that history as fresh proof.

## Changelog

### v0.3 — 2026-09-05

Correct the two-file inventory, reference adopted v2 doctrine, document the pnpm
workspace/importer and script-policy distinction, narrow Python isolation claims,
refresh CI guidance, distinguish planned guards from enforcement, and retain a
reversible non-implementation boundary. No package activation or deletion.

### v0.2 — 2026-07-19

Established the pinned drift-guard account, workspace/import risks, proposed
freeze and negative checks, disposition requirements, ownership/CI limits and
rollback. Its README-only inventory and missing-UI-toolchain account are historical,
not the current state described above.

### v0.1 — 2026-06-16

Replaced an empty README with the initial bounded drift-guard contract.

[Back to top](#top)
