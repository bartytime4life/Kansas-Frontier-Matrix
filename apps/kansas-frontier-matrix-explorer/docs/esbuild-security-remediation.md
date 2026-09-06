<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/esbuild-security-remediation
title: Explorer esbuild remediation regression guard
type: app-maintenance-note
version: 0.1.0
status: branch candidate; independent review pending
owning_root: apps/
responsibility: regression coverage for the merged esbuild dependency remediation
truth_posture: cite-or-abstain; candidate validation is not advisory closure
updated: 2026-09-06
[/KFM_META_BLOCK_V2] -->

# esbuild remediation regression guard

## Current finding

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
- The root pnpm and standalone npm parent-scoped overrides must remain present
  and resolve to `0.25.12`.
- The six existing version-specific `allowBuilds` decisions are compared
  byte-for-byte; no approval is added and no denial is spoofed or removed.
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
hosted workflow must supply that result. The prior merged PR's record reports
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
