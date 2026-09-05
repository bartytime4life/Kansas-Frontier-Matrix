<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/esbuild-security-remediation
title: Explorer esbuild and fflate dependency remediation
type: app-maintenance-note
version: 0.2.0
status: branch candidate; independent review pending
owning_root: apps/
responsibility: paired npm/pnpm dependency maintenance and app-local security regressions
truth_posture: cite-or-abstain; candidate validation is not default-branch alert closure
updated: 2026-09-05
[/KFM_META_BLOCK_V2] -->

# esbuild and fflate dependency remediation

## Alert identity and scope

[Code-scanning alert 53](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/code-scanning/53)
was read directly at `2026-09-05T16:42:06Z`: open, Scorecard v5.5.0,
`VulnerabilitiesID`, `supply-chain/local`, main commit
`3d6b8a6e81ed65a726156feae67fa73875b5b069`. It names exactly two GHSA IDs.
The historical empty PR #4057 is not remediation or a defensible current
false-positive assessment. No alert is dismissed by this work.

| Advisory | Actual dependency path | Bounded repair |
|---|---|---|
| [GHSA-67mh-4wv8-2f99](https://github.com/advisories/GHSA-67mh-4wv8-2f99) | `drizzle-kit@0.31.10 -> @esbuild-kit/esm-loader@2.6.5 -> @esbuild-kit/core-utils@3.3.2 -> esbuild@0.18.20`, in both locks | Override only the last edge to the already-workspace-used `0.28.2`; regenerate both locks. |
| [GHSA-px8p-9vwx-vf98](https://github.com/advisories/GHSA-px8p-9vwx-vf98) | `vinext@1.0.0-beta.8 -> @vercel/og@0.8.6 -> satori@0.16.0 -> @shuding/opentype.js@1.4.0-beta.0 -> fflate@0.7.4`, in the app npm lock | Resolve `fflate@0.7.5` within the existing parent range `^0.7.3`. The pnpm lock already has this patched backport and remains unchanged for fflate. |

The esbuild advisory concerns development-server cross-origin reads; a dev-only
classification or loopback bind is not a fix. Its first patched release is
0.25.0. The fflate advisory describes an infinite ZIP64 parsing loop; 0.7.5 is
the published patch for the 0.7 line. It does not require a cross-minor upgrade
to 0.8.3. Dependency presence does not by itself prove public runtime exposure.

[Baseline evidence run 33978939495](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/33978939495)
read both complete lock graphs and queried npm metadata. The current stable
Drizzle Kit, legacy loader, and core-utils versions still declare the affected
edge. There is no compatible stable parent-version update in that inspected
metadata. The narrow override crosses core-utils' declared `~0.18.20` range;
it therefore requires actual resolver, transform, serving, and Drizzle SQL
regressions, not just a clean audit. Replacing the deprecated loader is separate
maintenance work.

The baseline audits report one moderate advisory in pnpm and five affected
package records for the two advisory IDs in npm. These are different metrics.
Babel `7.29.7` and browserslist `4.28.8` in the npm lock are preserved, including
merged PR #4296's later Babel fix. The separate Docker image override lock has
neither target dependency; it is not changed.

## Resolver and permission boundaries

| Entrypoint | Declaration | Resolved graph |
|---|---|---|
| Workspace pnpm | [`pnpm-workspace.yaml`](../../../pnpm-workspace.yaml), parent-qualified override | [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) |
| Standalone npm app | [`package.json`](../package.json), same parent-qualified override | [`package-lock.json`](../package-lock.json) |

All existing pnpm `allowBuilds` entries remain byte-for-byte unchanged. The
`esbuild@0.18.20: false` entry is retained as a denial, not as an installed
package or a mitigation substitute. No audit exclusion, blind forced upgrade,
script-policy bypass, source activation, database migration, or deployment is
part of this repair.

The esbuild edge and [esbuild tests](../tests/esbuild-security.test.mjs) reconcile
preserved branch `agent/esbuild-alert-63-20260905` at
`8705c0788cf9f90b63b32d7dd35b258510f586eb`. That branch is not overwritten.
This complete alert-53 candidate replaces a separate delivery of its overlapping
dependency slice; do not merge both independently or restore its older npm lock.
Its historical validation remains lineage, not a substitute for this head's tests.

## Validation and reproducibility

Use Node 22 within the root engine range and root-pinned pnpm 11.17.0. The
candidate run and regression workflow select Node 22.23.2, whose bundled npm
was observed as 10.9.8; npm has no independent repository pin.

```bash
corepack enable
pnpm install --frozen-lockfile
KFM_ESBUILD_REQUIRE_WORKSPACE=1 KFM_ESBUILD_RUNTIME_PROBE=1 \
  node --test apps/kansas-frontier-matrix-explorer/tests/{esbuild,fflate}-security.test.mjs
pnpm audit --json
```

The [read-only CI matrix](../../../.github/workflows/esbuild-security.yml)
independently executes a real standalone `npm ci`, verifies lock immutability,
runs both suites against actual resolved packages, and audits both graphs.
Workspace-only guards are explicitly skipped only in the standalone copy.
Runtime probes are opt-in; default tests read files and synthetic values only.
The [fflate regressions](../tests/fflate-security.test.mjs) preserve normal
compression/ZIP round trips and exercise a 176-byte malformed ZIP64 archive in
a child process with a three-second hard termination limit. A timeout is a
failure, not a passing rejection. esbuild probes use loopback synthetic assets;
Drizzle generates temporary SQL without contacting or changing a database.

Regenerate pnpm from the workspace and npm from an isolated app copy. Use a
targeted `npm update fflate --package-lock-only`, not a new direct dependency.
Preserve unrelated dependency identities and metadata; never invent integrity
values. Base failures, candidate failures, skipped checks, and pending hosted
checks must remain separate. Exact run evidence and file hashes live in the
[generated-work receipt](../../../data/receipts/generated/code-scanning-alert-53-20260905.json)
and the PR, not in an evergreen claim that tests always pass.

## Review, closure, and rollback

Placement follows accepted ADR-0029: app docs/tests under `apps/`, ecosystem
manifest/locks at their established roots, orchestration under `.github/`, and
authoring provenance under `data/receipts/generated/`. No new authority root,
schema, policy, catalog, or release home is introduced.

A validated draft is not approval, merge, deployment, or scanner closure. Alert
#53 requires a fresh default-branch Scorecard read after separately authorized
integration. Issue #4024's draft-transition boundary remains in force.

Before integration, close the draft unmerged to abandon the candidate. After
an independently authorized integration, revert the paired declarations and
locks together only under security review: restoring the old locks reintroduces
the vulnerabilities. Keep affected development serving and untrusted archive
processing disabled until a patched replacement is restored. Do not remove
regressions or suppress findings to make a rollback appear safe.
