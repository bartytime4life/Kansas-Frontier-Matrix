<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/esbuild-security-remediation
title: Explorer esbuild development dependency remediation
type: app-maintenance-note
version: 0.2.0
status: branch candidate; independent review pending
owning_root: apps/
responsibility: paired npm/pnpm dependency maintenance and app-local regression coverage
truth_posture: cite-or-abstain; candidate validation is not default-branch alert closure
updated: 2026-09-05
[/KFM_META_BLOCK_V2] -->

# esbuild development dependency remediation

## Scope

[GHSA-67mh-4wv8-2f99](https://github.com/advisories/GHSA-67mh-4wv8-2f99)
affects esbuild through 0.24.2; 0.25.0 is the first patched release. The issue is
in esbuild's development server. A dependency finding does not prove that a
production site exposes that server. Loopback binding alone is not a fix for
cross-origin reads from a developer's browser.

At `main@702e97d824d7305698cd66bc1f9a57edc4063440`, the remaining affected
chain was `drizzle-kit -> @esbuild-kit/esm-loader -> @esbuild-kit/core-utils@3.3.2
-> esbuild@0.18.20`. The repair overrides only the last dependency edge to
**0.28.2**, a version already present in the workspace. It does not upgrade
Drizzle, Vite, Vinext, MapLibre, or other consumers of esbuild.

Both installation entrypoints must retain this decision:

| Entrypoint | Declaration | Resolved dependency graph |
|---|---|---|
| pnpm workspace | [`pnpm-workspace.yaml`](../../../pnpm-workspace.yaml), parent-qualified `overrides` | [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) |
| Standalone npm app | [`package.json`](../package.json), parent-qualified `overrides` | [`package-lock.json`](../package-lock.json) |

The existing pnpm `allowBuilds` decisions are unchanged. In particular, the
explicit denial for `esbuild@0.18.20` remains a deny entry, not an installed
package or a mitigation substitute. No audit exclusion or forced broad upgrade
is part of this repair. The legacy loader remains deprecated; replacing it is
separate maintenance work.

## Validation and reproducibility

The [regression tests](../tests/esbuild-security.test.mjs) reject affected,
malformed, and prerelease versions. Workspace CI requires both lockfiles and
both override declarations. Standalone app exports explicitly skip the two
workspace-only tests; npm lock and runtime tests still execute.

From the repository root:

```bash
KFM_ESBUILD_REQUIRE_WORKSPACE=1 node --test apps/kansas-frontier-matrix-explorer/tests/esbuild-security.test.mjs
corepack enable
pnpm install --frozen-lockfile
KFM_ESBUILD_REQUIRE_WORKSPACE=1 KFM_ESBUILD_RUNTIME_PROBE=1 node --test apps/kansas-frontier-matrix-explorer/tests/esbuild-security.test.mjs
```

Runtime probes use synthetic TypeScript, a temporary loopback esbuild server,
and temporary SQLite migration files. They check normal bundle/source-map
responses, absence of cross-origin read permission, the actual overridden
package version, and Drizzle SQL generation. They do not open a live database,
access production data, or prove browser/Sites deployment behavior. Default
test execution performs no network requests; runtime probes are explicit.

The [read-only CI matrix](../../../.github/workflows/esbuild-security.yml)
tests frozen pnpm installation and a separate real `npm ci`, including lockfile
immutability and the runtime probes for each resolver. Neither resolver skips
dependency scripts or disables Dependabot. Advisory-service results remain a
distinct security check and are not a claim that every dependency is safe.

[Candidate generation run 33974360827](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/33974360827)
verified the scoped lock changes, frozen pnpm install, initial runtime probes,
canonical `explorer-web` build/tests, and absence of this GHSA in npm audit.
Other advisory findings are not cleared by that result. The final CI matrix's
exact commit result must be read separately; a declared test is not a pass.

For future dependency changes, regenerate with the root-pinned pnpm version and
with npm from an isolated copy of this app's manifest and lockfile. Review both
diffs together. The original npm regeneration refreshed unrelated platform
metadata; this patch preserves those existing non-esbuild records rather than
shipping collateral changes. Native `npm ci` and frozen pnpm validation must
still pass. Do not hand-invent integrity values or accept unrelated version drift.

## Current-main reconciliation: 2026-09-05

The earlier evidence above belongs to its original execution, not to later main.
The [reconciliation run 33981346520](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/33981346520)
compared actual `main@3d6b8a6e81ed65a726156feae67fa73875b5b069` with a
three-way integration of that main and the existing repair head
`8705c0788cf9f90b63b32d7dd35b258510f586eb`.

| Identity | Value |
|---|---|
| Workflow execution commit | `860ea5c0223e9f0ad9dfba37a0d45eb45e8137bb` |
| Tested integration tree | `284de7da03c0674561e1d95accda5bed0ffca455` |
| npm lock Git blob | `d3d470e9f99b04f896c7ba4cfb564bbe714434b9` |
| npm lock SHA-256 | `48ea4a55a8c95e186754cee1eef5cbcfcaab08cb7a4f3088ddf72e2f399c629a` |
| Evidence artifact | `esbuild-current-base-evidence`, artifact `9973882585` |
| Evidence archive SHA-256 | `56e3bcf55d713ee1d638da6f9e5fad452962467ecb309ca108890806fa4a8b49` |
| Native toolchain | Ubuntu 24.04; Node 22.23.2; npm 10.9.8; pnpm 11.17.0 |

Scope assertions passed: the integration retained every current-main non-esbuild
npm package record, including all of PR #4296's Babel records and
`@babel/core@7.29.7`. The root pnpm lock remained the previously generated
candidate. The complete `pnpm-workspace.yaml` base bytes were retained, with
only the two-line parent-qualified override appended. All six build-script
allow/deny decisions therefore remain unchanged. KDOT and temporal source
changes from current main were retained, not replaced with an older app tree.

| Executed check | Actual base | Integration candidate |
|---|---|---|
| `pnpm install --frozen-lockfile` | PASS | PASS |
| Separate app `npm ci` | PASS | PASS |
| Root/app lock and workspace-policy byte immutability after commands | PASS | PASS |
| `pnpm --filter explorer-web test` | 445 unit tests and 128 browser tests passed | 445 unit tests and 128 browser tests passed |
| `pnpm --filter explorer-web build` | FAIL: seven temporal TypeScript errors | FAIL: the same seven diagnostics |
| `pnpm --filter kansas-frontier-matrix-explorer build` | PASS | PASS |
| App-only exported tree: `npm run build` | FAIL: missing sibling MapLibre source | FAIL: the same missing sibling source |
| pnpm security/runtime probes | Not run against vulnerable base | 7 passed; no skips |
| Standalone npm security/runtime probes | Not run against vulnerable base | 5 passed; 2 explicit workspace-only skips |

The seven matching compiler diagnostics are in
`apps/explorer-web/src/features/temporal/index.ts`: TS2322 at `(330,71)` and
TS18047 for nullable `start.raw`/`end.raw` at lines 370, 373, and 376. The build
stops before Vite bundling. This is a demonstrated same-base failure, not a
passing build and not a reason to weaken TypeScript checks in this patch.

The app-only npm build fails resolving `../../packages/maplibre/src/index.ts`
from the existing `@kfm/maplibre` import. The export deliberately contains this
app alone, not its sibling package. This establishes a packaging/environment
limit for that exact export, not a failure of `npm ci`, a new esbuild regression,
or a tested claim about the live Sites deployment. The complete pnpm workspace
build passes. Closing the standalone export is separate dependency-closure work.

Candidate `npm audit --json` returned exit 1 with **one moderate finding**:
`fflate`, [GHSA-px8p-9vwx-vf98](https://github.com/advisories/GHSA-px8p-9vwx-vf98).
The target esbuild GHSA is absent; the audit is not globally clean. No audit
ignore, blanket script approval, package-manager change, or broad dependency
upgrade was used. No live source, database, production server, or deployment
was contacted by the synthetic probes.

The integration tree was tested in an isolated checkout. Final handoff changes
only this maintenance note and a new reconciliation receipt relative to that
tested tree; final-commit installer/probe results must be read separately from
the permanent `esbuild-security` workflow. Collection success does not erase the
two reported build failures. Full repository CI, a production-browser test,
GitHub security-alert closure, independent review, and incident-control exit
remain unverified by these checks.

The [original receipt](../../../data/receipts/generated/esbuild-alert-63-20260905.json)
is preserved unchanged and binds its old artifact hashes to the original
repair head. Its pending or skipped fields are historical, not silently upgraded.
The [reconciliation receipt](../../../data/receipts/generated/esbuild-current-main-reconciliation-20260905.json)
binds this updated note and npm lock. The temporary reconciliation workflow is
removed from the final tree; its historical commit and run remain inspectable.

## Review, closure, and rollback

Placement follows accepted ADR-0029: app maintenance/tests under `apps/`, root
workspace build files at the repository root, Actions under `.github/`, and the
[generated-work receipt](../../../data/receipts/generated/esbuild-alert-63-20260905.json)
under the existing receipt lane. No schema, policy, source, or release home is added.

This branch does not merge, dismiss alert #63, deploy Sites/Vercel, or alter
repository settings. Alert #63's exact state and default-branch closure require
an authenticated Dependabot read after separately authorized integration. The
PR-transition safety boundary is not waived by successful dependency tests.
Issue #4024's closed metadata does not establish the exit proof required by the
current contributor and coordination records. Delivery remains branch-only
until the applicable PR-creation path is independently cleared.

Before integration, abandon the candidate branch to roll back authoring. After
an authorized integration, revert the paired override declarations and both
locks together only with security review: restoring the old dependency
reintroduces the advisory. Keep affected development serving disabled until a
patched replacement is restored. Do not silently revert just one lockfile,
remove the regression checks to obtain green CI, or treat rollback as permission
to reopen a vulnerable development server. Preserve #4296's Babel repair during
any forward correction or rollback; do not restore the old pre-Babel npm lock.
