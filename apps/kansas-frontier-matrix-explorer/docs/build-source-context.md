# Sites build source context

## Scope and authority

This application composes the existing Kansas Frontier Matrix Explorer Sites
adapter. It is not an independently vendored copy of the reusable MapLibre
package. Vite and TypeScript currently resolve `@kfm/maplibre` to
`../../packages/maplibre/src/index.ts`. The package root exports the neutral
runtime facade; concrete renderer acquisition remains package-owned.

The owning responsibility is `apps/`: application build composition and its
local regression tests. Adopted Directory Rules `DIR-EXEC-001`, `DIR-DEP-003`,
and the existing application-local test convention support this change. No
new root, alias, schema, renderer, source admission, or hosting decision is made.

## Required source input

Build in the repository layout with this application under `apps/` and the
existing MapLibre source package under root `packages/`. Preserve the app's
`package.json` and `package-lock.json` for its documented npm entrypoint. Root
workspace consumers still use `pnpm-lock.yaml` and `pnpm-workspace.yaml`,
including the existing build-script allow/deny policy. These are different
installer consumers, not redundant lockfiles to delete.

`npm ci` supplies locked npm dependencies. It does **not** supply the sibling
source tree used by the alias. An export containing only this application is
therefore not a complete build context unless a separate, verified assembly
process supplies its permitted source dependencies and preserves or deliberately
adapts both aliases. No such source-assembly process is added here.

The build wrapper now checks that the sibling facade entry is a regular-file
input before invoking `vinext`. When the entry is missing or is a directory,
it returns exit **66** with `BUILD_CONTEXT_INCOMPLETE`. It does not retry an
installation, use a global renderer, acquire a CDN script, or change a lockfile.
The existing Linux timeout, app-local/workspace-hoisted `vinext` selection,
project-scoped environment, and builder exit-status propagation remain intact.

This is a **minimum-input check**, not a dependency-closure validator. A present
entry may still contain broken imports, require unavailable packages, or fail to
compile. Only a successful build of the intended source context can establish
compilation; it still cannot establish renderer, browser, deployment, data-release,
or operational readiness.

## Focused validation

From the repository root on Linux:

```bash
node --test apps/kansas-frontier-matrix-explorer/tests/build-verified.test.mjs
bash -n apps/kansas-frontier-matrix-explorer/scripts/build-verified.sh
```

The focused suite exercises ten cases: workspace-hoisted builder selection;
missing and non-package builders; app-local fallback; absent and directory-shaped
sibling entries; nonzero builder status; environment initialization with spaces
in the source path; TypeScript/Vite alias parity; and the existing Vercel
non-deployment configuration assertion. The last assertion also reads the
existing `connectors/usgs/vercel.json` boundary; do not move or narrow that test
without preserving its coverage and repository-relative discovery.

Fixtures in these tests are temporary, synthetic wrapper inputs. They are not
compiled MapLibre, released data, or runtime demonstration fixtures. Builder
executables are test doubles. No install, actual `vinext` compilation, browser,
GPU, real model, live source, or deployment is exercised by this command.

The app's existing `npm test` still builds before running its native test files.
Run the intended npm build/install profile only in a suitable isolated source
context, following the existing installation instructions. Do not count the
focused suite as a substitute for that build or for Explorer Web's separate
Vitest/Playwright path.

## Assembly and output boundary

A future exporter must inventory transitive source imports, framework entrypoints,
workers, CSS, protocols, installer inputs, and admitted package exports. Its
output selection must distinguish application runtime demonstration data from
test-only fixtures, development doubles, secrets, repository documentation, and
unreleased lifecycle data. Copying the repository wholesale into a deployable
artifact is not a substitute for that boundary review.

This patch changes no Site version, slug, public URL, rollback history, D1/R2
binding, Vercel setting, renderer acquisition, or deployment builder. Repository
source and the live Site remain independently verified surfaces.

## Correction and rollback

Revert the wrapper guard, corresponding test changes, and this guide together;
retain the generated-work receipt as historical process evidence. The previous
wrapper and tests are pinned at
`d1b430ca51887777766050e5582659ab34322286`. Re-run the original wrapper tests and
inspect installer inputs after rollback. No data or deployment rollback is
implied or executed. A future alias or source-layout change must update the
wrapper, both aliases, tests, and assembly documentation coherently.
