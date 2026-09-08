<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/esbuild-security-remediation
title: Explorer esbuild remediation regression guard
type: app-maintenance-note
version: 0.3.1
status: branch candidate; independent review pending
owning_root: apps/
responsibility: regression coverage for the esbuild dependency remediation candidate
truth_posture: cite-or-abstain; candidate validation is not advisory closure
updated: 2026-09-08
[/KFM_META_BLOCK_V2] -->

# esbuild remediation regression guard

## Current branch reconciliation — 2026-09-08

The preserved candidate branch was reconciled with
`main@2bddc4b4e453a7396d654d5f988911e9ee3af1ef` by non-force merge
commit `1cf5d24ae72566703b4b206e846f1c11d38af22e`. Its exact parents are
the previously validated candidate
`fdabf5797b13e6bf7bf178fc236c916dba88da74` and that current
`main` commit. The 16 incoming commits changed ten unrelated
cross-domain, taxonomy, workflow, and generated-receipt paths; none overlaps
the seven-file esbuild candidate. At the merge commit the seven candidate
blobs remained byte-identical, and the branch became five commits ahead and
zero behind `main`.

The exact pre-reconciliation candidate
[run 34249165957](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34249165957)
passed both the frozen pnpm-workspace job and the standalone `npm ci` job,
including static guards and runtime probes. The merge itself changed only
incoming non-esbuild paths, so the security workflow's path filter did not
rerun. This documentation refresh deliberately enters the existing path
filter so the new branch head receives a separate hosted result. Read that
result from GitHub; do not infer it from the earlier run or this text.

No pull request was opened. Issue #4024 still holds this execution path at
`VALIDATED_BRANCH_ONLY`; branch reconciliation and a passing check do not
authorize draft creation, ready-for-review, approval, merge to `main`,
advisory dismissal, release, deployment, or publication.

## Current candidate: effective pnpm 11 override and dual-lock repair

This follow-up originally started from
`main@03138e81f19b801cf6d16d767a4c0e01ab36d717`,
which merged [PR #4427](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4427).
It is authored on `agent/esbuild-security-pnpm11-20260908`. The merge of #4427
is historical repository state, not evidence that its remaining checks passed.

At that base, `pnpm-lock.yaml` contains affected esbuild `0.18.20` entries,
while the remediation text is still under `package.json#pnpm.overrides`.
The standalone Explorer npm lock also describes older direct dependencies
than its manifest. These are distinct failures: an ineffective workspace
security setting and a stale standalone installation graph.

The candidate moves the existing parent-scoped override, without broadening it,
to the effective configuration described in the [pnpm 11 release notes](https://pnpm.io/blog/releases/11.0):

```yaml
# pnpm-workspace.yaml
overrides:
  "@esbuild-kit/core-utils>esbuild": "0.25.12"
```

The ignored root `pnpm` field is removed. The standalone npm override remains
in the app manifest. Native regeneration of both existing lockfiles preserves
the current direct dependency declarations; this is not a rollback of the nine
updates in #4427. All seven existing version-specific `allowBuilds` decisions
remain unchanged, including both Workerd denials. No wildcard approval,
interactive approval, security-floor waiver, or relaxed validation install is
introduced.

### Regression closure

The existing app-local security suite now also rejects ignored root pnpm
settings, missing/duplicated/broadened lockfile overrides, and stale, missing,
or extra standalone dependency declarations. Its workspace snapshot includes
the effective override and the unchanged build decisions. Negative mutations
exercise the guards rather than accepting text merely because it names a fix.
The existing all-platform esbuild inventory and resolver, cross-origin, and
synthetic Drizzle probes remain enforced.

Native candidate generation is recorded in
[run 34248375449](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34248375449),
with authoring inputs at `9cc310123cf9eacb4628ac409698a6e7cf928d04`.
Generation uses pinned pnpm `11.17.0` and the runner's recorded Node 22/npm
versions. Lock-only authoring disables dependency scripts; subsequent validation
uses frozen pnpm installation and standalone `npm ci`, not unlocked installs.
The generation job checks input hashes, requires an unchanged pnpm importer
section, runs security/runtime probes and the Explorer build/unit and MapLibre
unit consumers, and binds emitted bytes to SHA-256 and Git blob identities.
These are candidate-generation results, not final-commit CI or independent
approval. Read the final branch-head workflow result separately.

The temporary exact-branch generation workflow is removed in the final repair
commit. Its isolated generation job has read-only credentials. A separate
checkout-free job stores only the two generated, unreferenced Git blobs; it
calls no branch, pull-request, review, merge, release, or deployment API.
The final tree retains only the existing read-only security workflow, with an
exact branch trigger so the committed repair can be checked without a PR.
That named-branch push selector is branch-only validation plumbing. Before any
separately authorized integration PR, remove the selector and validate through
the pull-request trigger; do not carry it into `main` unintentionally.
No generated credentials, logs, or intermediate package trees are committed.

### Delivery, limits, and rollback

The current delivery target is branch-only while
[issue #4024](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024)
holds the implicated PR-state mutation path. Successful security probes do not
supply independent review, merge authority, advisory closure, browser/platform
coverage, or production-readiness evidence. The separately observed
object-family-register, aggregate validator-suite, and MapLibre performance
failures are not waived or claimed fixed by this dependency slice.

Placement is same-path maintenance under adopted
[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the [Directory Rules](../../../docs/doctrine/directory-rules.md): existing
root package-manager files, the app-owned test/document consumers, and the
platform-owned read-only workflow. No parallel policy, schema, registry, or
release home is created.

The final delta changes seven existing files: root `package.json`,
`pnpm-workspace.yaml`, `pnpm-lock.yaml`, the app's `package-lock.json`, this note,
the app-local security test, and `.github/workflows/esbuild-security.yml`.
Before integration, preserve or close the candidate without modifying main.
After separately authorized integration, revert this seven-file delta together
through a reviewed change; restoring the base reintroduces the known dependency
regression and is not itself a security remedy. The temporary workflow must
remain absent, and the named-branch push selector must be removed before any
separately authorized integration. No rollback was executed.

## Historical September 8 Workerd installation repair

This section records the earlier #4427 repair. Statements about its unresolved
esbuild failure describe that earlier head; the current candidate above is a
separate repair, not a rewrite of its validation history.

[PR #4427](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4427)
rebased to `3224b240811b602fda57b86e9a39ba1e31ecffc3` on
`main@f4a00307fe0bf8cffd598117196249f0637d0826`. Its Wrangler update
introduces `workerd@1.20260903.1`. The original
[UI install log](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34219261909/job/102038261891)
reports `ERR_PNPM_IGNORED_BUILDS` for that version, before build or tests run.

The bounded repair adds `"workerd@1.20260903.1": false` to the existing
root workspace policy and matching regression snapshot. All six prior
decisions remain unchanged, including the old Workerd denial. This is an
explicit denial, not permission to run Workerd's install script; pnpm's
[build-decision documentation](https://pnpm.io/cli/approve-builds) distinguishes
`false` from both approval and an unlisted decision. No wildcard approval,
interactive approval, `strictDepBuilds` relaxation, or unlocked CI install
is introduced. Future Workerd versions still require explicit decisions.

The new negative cases reject deletion, commenting-out, approval, or removal
of the exact-version restriction for either Workerd denial. The focused
policy tests and syntax check were run locally using Node 22.16.0 on
blob-verified copies of the affected files. This is not a full checkout,
locked dependency installation, browser test, or Workerd compatibility proof.
Hosted results must be read at the pushed head, separately from review.

**Separate unresolved security failure at that head:** the
[esbuild guard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34239490070/job/102105690197)
rejects `@esbuild/android-arm64@0.18.20` in the pnpm lock. The install log
also warns that pnpm 11 ignores `package.json#pnpm.overrides`. That repair
did not change the lockfile, waive the patched floor, establish an effective
override, or close the security finding. Override relocation and native lock
regeneration remained necessary after the three-file Workerd correction.

Its same-path placement and three-file rollback preserve the nine pre-existing
dependency updates. That rollback is separate from the current seven-file
follow-up described above.

## Historical September 6 baseline

The following remediation and validation record describes the September 6
baseline, not the current dependency tree. It does not establish that the
post-#4427 pnpm lock was remediated.

[PR #4318](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4318) merged the bounded dependency repair into
`main`. At the authoring base `main@11cb4b51125db18d952d9f00e997beab89791cea`, the direct path
`drizzle-kit@0.31.10` → `@esbuild-kit/esm-loader@2.6.5` →
`@esbuild-kit/core-utils@3.3.2` resolves to `esbuild@0.25.12` in both
lockfiles. The root pnpm override was in `package.json` under
`pnpm.overrides`; the standalone npm override was in the Explorer
`package.json`. That root configuration location is superseded by the current
candidate's effective workspace setting.

[GHSA-67mh-4wv8-2f99](https://github.com/advisories/GHSA-67mh-4wv8-2f99) affects esbuild through `0.24.2`;
`0.25.0` is the first patched release. The finding describes permissive
cross-origin reads from the development server; it does not prove that KFM
exposed a production development server.

The quality gap addressed in that slice was missing executable regression
coverage after the merged repair. It did not claim alert closure or complete
dependency modernization. The deprecated `@esbuild-kit` packages remain a
separate upstream replacement follow-up.

## Guarded invariants

- All inventoried esbuild and platform-binary versions in both locks must meet
  the patched floor, not merely the currently installed platform.
- Effective pnpm workspace and standalone npm parent-scoped overrides must
  remain present and resolve to `0.25.12`.
- All seven existing version-specific build decisions remain unchanged.
- The standalone npm lock root must agree with every direct dependency section.
- Runtime probes resolve the actual loader edge, transform synthetic TypeScript,
  check loopback development-server cross-origin response headers, and generate
  synthetic Drizzle SQL without a database.

## Validation and historical boundaries

`tests/esbuild-security.test.mjs` performs static checks by default and
enables runtime probes only with `KFM_ESBUILD_RUNTIME_PROBE=1`. The
read-only [workflow](../../../.github/workflows/esbuild-security.yml) runs
the static checks, frozen pnpm install, standalone npm `ci`, and runtime
probes. Lockfile checksums ensure validation installs do not rewrite inputs.

The September 6 record reported local command validation unavailable due to an
environment usage limit. Initial hosted run `34013101178` failed two static
guards: the standalone key used a pre-merge npm shape, and one workspace
mutation was a no-op after the override moved to `package.json`. Corrected
[run 34013210029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34013210029)
passed both package-manager jobs, including installation and runtime probes.
Those results belong to that historical revision, not the current candidate.
The prior merged PR's partial validation and failed topology validator are not
relabelled as passing.

This remains security/quality work for
[issue #3366](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3366).
It grants no source admission, data-lifecycle transition, release, deployment,
publication, repository-settings change, or independent review approval.
