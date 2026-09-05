<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/esbuild-security-remediation
title: Explorer esbuild development dependency remediation
type: app-maintenance-note
version: 0.1.0
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

## Review, closure, and rollback

Placement follows accepted ADR-0029: app maintenance/tests under `apps/`, root
workspace build files at the repository root, Actions under `.github/`, and the
[generated-work receipt](../../../data/receipts/generated/esbuild-alert-63-20260905.json)
under the existing receipt lane. No schema, policy, source, or release home is added.

This branch does not merge, dismiss alert #63, deploy Sites/Vercel, or alter
repository settings. Alert #63's exact state and default-branch closure require
an authenticated Dependabot read after separately authorized integration. The
PR-transition safety boundary is not waived by successful dependency tests.

Before integration, abandon the candidate branch to roll back authoring. After
an authorized integration, revert the paired override declarations and both
locks together only with security review: restoring the old dependency
reintroduces the advisory. Keep affected development serving disabled until a
patched replacement is restored. Do not silently revert just one lockfile,
remove the regression checks to obtain green CI, or treat rollback as permission
to reopen a vulnerable development server.
