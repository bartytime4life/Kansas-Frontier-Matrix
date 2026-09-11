<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/esbuild-security-remediation
title: Explorer esbuild remediation regression guard
type: app-maintenance-note
version: 0.3.0
status: draft repair; independent review pending
owning_root: apps/
responsibility: regression coverage for the merged esbuild dependency remediation
truth_posture: cite-or-abstain; candidate validation is not advisory closure
updated: 2026-09-10
[/KFM_META_BLOCK_V2] -->

# esbuild remediation regression guard

## September 10 dependency-audit repair

The current repair closes the unresolved pnpm 11 override-location failure
recorded below. It moves the exact
`@esbuild-kit/core-utils>esbuild@0.25.12` override from the ignored
`package.json#pnpm.overrides` location to `pnpm-workspace.yaml#overrides`,
then regenerates the workspace lock with pnpm 11.17.0. The resolved pnpm graph
contains no esbuild version below the patched `0.25.0` floor.

The same dependency-audit repair pins Miniflare's vulnerable transitive Sharp
edge to `sharp@0.35.4` in both package-manager graphs, pins the standalone
Explorer's transitive `fflate` edge to `0.7.5`, and synchronizes its stale
npm lock with the existing manifest. These overrides are dependency-resolution
constraints; they do not approve install scripts or broaden runtime authority.

Local Node 22.23.2 checks passed the static guard, frozen pnpm install,
standalone npm CI dry run, and both audit classifiers with zero reported
vulnerabilities. Runtime probes and exact-head hosted checks remain required
on the draft pull request. Rollback requires restoring the root and Explorer
manifests, both locks, `pnpm-workspace.yaml`, this guard, and this note
together; removing the guard alone is not a valid rollback.

## September 8 dependency-update follow-up

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

**Historical security failure resolved by the September 10 candidate:** at the rebased head, the
[esbuild guard](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34239490070/job/102105690197)
rejects `@esbuild/android-arm64@0.18.20` in the pnpm lock. The install log
also warns that pnpm 11 ignores `package.json#pnpm.overrides`. This repair
does not change the lockfile, waive the patched floor, claim that the override
is effective, or close the security finding. Correcting the override location,
regenerating the lock with the pinned package manager, and passing both
resolver/runtime probes remain required before integration.

Placement is same-path maintenance of the root package-manager configuration
and its existing app-local test/document consumers; no new responsibility
root or authority home is added. Rollback this follow-up's three files
together to the rebased head; the nine dependency updates are independent
pre-existing changes and are not reverted by this follow-up.

## Current finding

The following remediation and validation record describes the September 6
baseline, not the current dependency tree. The September 8 finding above
supersedes its implication that the current pnpm lock is remediated.

[PR #4318](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4318) merged the bounded dependency repair into
`main`. At the current authoring base `main@11cb4b51125db18d952d9f00e997beab89791cea`, the direct path
`drizzle-kit@0.31.10` → `@esbuild-kit/esm-loader@2.6.5` →
`@esbuild-kit/core-utils@3.3.2` resolves to `esbuild@0.25.12` in both
lockfiles. The root pnpm override is in `package.json` under
`pnpm.overrides`; the standalone npm override is in the Explorer
`package.json`.

[GHSA-67mh-4wv8-2f99](https://github.com/advisories/GHSA-67mh-4wv8-2f99) affects esbuild through `0.24.2`;
`0.25.0` is the first patched release. The finding describes permissive
cross-origin reads from the development server; it does not prove that KFM
exposed a production development server.

The quality gap addressed here is missing executable regression coverage after
that merged repair. This candidate does not duplicate the manifests or
lockfiles and does not claim alert closure or complete dependency
modernization. The deprecated `@esbuild-kit` packages remain a separate
upstream replacement follow-up.

## Guarded invariants

- All inventoried esbuild and platform-binary versions in the pnpm and npm
  locks must meet the patched floor.
- The pnpm-workspace and standalone npm parent-scoped overrides must remain
  present in their package-manager-specific authority locations and resolve
  to `0.25.12`.
- The six original version-specific `allowBuilds` decisions plus the September 8
  exact-version Workerd denial are compared byte-for-byte; no approval is added
  and no denial is spoofed or removed.
- Runtime probes resolve the actual loader edge, transform synthetic
  TypeScript, check the loopback development server's cross-origin response
  headers, and generate synthetic Drizzle SQL without a database.

## Validation and boundaries

`tests/esbuild-security.test.mjs` performs static checks by default and
enables runtime probes only with `KFM_ESBUILD_RUNTIME_PROBE=1`. The
read-only [workflow](../../../.github/workflows/esbuild-security.yml) runs
the static checks, frozen pnpm install, standalone npm `ci`, and runtime
probes. Lockfile checksums ensure the install commands do not rewrite the
reviewed inputs.

Local repository command validation was unavailable in this session because
the command runner was rejected by an environment usage limit. The exact-head
hosted workflow must supply that result. The initial exact-head run `34013101178` failed two static guard assertions: the standalone key still used the pre-merge version-qualified npm shape, and one workspace mutation was a no-op after the merged override moved to `package.json`. The candidate now corrects both cases; the rerun is the authoritative result. The corrected exact-head [workflow run 34013210029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/34013210029) passed both the pnpm and npm jobs, including installation and runtime probes.

The prior merged PR's record reports
partial hosted validation and a failed topology validator; this follow-up
does not relabel those outcomes.

This is one security/quality proof slice for [issue #3366](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3366).
It changes only tests, read-only CI, documentation, and a generated receipt.
No source admission, policy authority, data lifecycle, release, deployment,
publication, repository settings, or review requirement is changed.

Before authorized integration, close the draft or restore the preimages. After
separately authorized integration, revert the four candidate files together
if needed; do not remove the guard to obtain green CI or broaden build-script
admission.
