# GoDaddy Node dependency audit — 2026-10-18 UTC

## Decision

Investigation complete; dependency remediation remains **BLOCKED / UNRESOLVED**.
The eight HIGH affected-package entries are propagation of **one advisory**,
[GHSA-vfj7-8cjw-p6xm / CVE-2026-93687](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm),
through two dependency chains. There are nine affected installation locations
because `fast-glob` has two installed versions. There is one installed Braces
copy. They are not eight independent vulnerabilities.

Fresh npm registry metadata still identifies `braces@3.0.3` as latest, and the
reviewed advisory lists no patched version. No compatible complete correction
was established. Keep `package.json`, `package-lock.json`, the Vinext archive,
overrides and application architecture unchanged. Do not regenerate the lockfile
without an actual dependency change. This report is neither an audit exception
nor permission to publish.

## Exact scope and evidence

The inspected production-review branch is
`codex/published-kfm-4b3cc-20261017` at
`1d02be5083c9ddd207e0ddcea97f0f3017334365`, the merge of
[PR #5245](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5245).
Its successful [original CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39085765215)
does not clear the separate dependency finding. The connected/newer AI branch
and GoDaddy publication are outside this investigation.

The [machine-readable evidence](dependency-audit-20261018.json) retains the raw
full and production-omit audit results, installed dependency tree, input hashes,
registry observations, bounded reproduction results and runtime/bundle summaries.
It contains no environment values, private stores, prompts or model files.
The root `AGENTS.md` and hosting/rollback documentation apply. No root or scoped
`SECURITY.md` exists in this standalone composition; do not infer the separate
monorepo's runtime or policy from its repository name.

## All eight entries and their actual roles

Every row is in root `dependencies` transitively or directly, with no lockfile
`dev` flag. This is intentional for the GoDaddy build/start installation model.
Both `npm audit --json` and `npm audit --omit=dev --json` return eight HIGH,
zero CRITICAL and the same package names. **Production-installed does not mean
executed on a public request; build/lint use does not mean absent from production.**

| Audit entry | Locked and installed version(s) | Immediate parent / advisory relationship | Observed use |
|---|---|---|---|
| `@next/eslint-plugin-next` | 16.3.8 | `eslint-config-next`; affected through `fast-glob` | Lint tooling |
| `braces` | 3.0.3 | `micromatch`; the only direct advisory | Recursive pattern compilation/expansion |
| `eslint-config-next` | 16.3.8 | Root dependency; affected through `@next/eslint-plugin-next` | Lint configuration |
| `fast-glob` | 3.3.1 and 3.3.3 | Next ESLint plugin and dynamic-import plugin; affected through `micromatch` | Lint and build pattern expansion |
| `micromatch` | 4.0.8 | Both `fast-glob` copies; affected through `braces` | Shared pattern helper |
| `vinext` | 0.0.50-kfm.2, local archive | Root dependency; affected through `vite-plugin-commonjs` | Build plugin and a separate production-server export |
| `vite-plugin-commonjs` | 0.10.4 | Vinext; affected through dynamic-import plugin | Build source transformation |
| `vite-plugin-dynamic-import` | 1.6.0 | CommonJS plugin; affected through its nested `fast-glob` | Build-time glob generation |

The complete chains are:

1. `eslint-config-next@16.3.8 → @next/eslint-plugin-next@16.3.8 → fast-glob@3.3.1 → micromatch@4.0.8 → braces@3.0.3`.
2. `vinext@0.0.50-kfm.2 → vite-plugin-commonjs@0.10.4 → vite-plugin-dynamic-import@1.6.0 → fast-glob@3.3.3 → micromatch@4.0.8 → braces@3.0.3`.

`next@16.3.8`, `vite@8.2.2`, `react/react-dom@19.2.8` and
`maplibre-gl@6.9.0` are not separate affected entries in this captured audit.
That statement is specific to these findings, not a general security clearance.

## Exposure and limits

The [upstream report](https://github.com/micromatch/braces/issues/70) describes
recursive AST walkers without a structural-depth guard. In this installation,
`braces/lib/compile.js` and `lib/expand.js` contain the recursive operations.
Both `fast-glob` copies enable brace expansion by default:
`out/managers/tasks.js` calls `expandPatternsWithBraceExpansion`, then
`out/utils/pattern.js` calls `micromatch.braces(pattern, {expand: true, ...})`.

**Build:** `vite.config.ts` installs Vinext. Its `dist/index.js` imports and
enables the CommonJS plugin. That plugin derives patterns from parsed dynamic
`require` expressions; `vite-plugin-dynamic-import/dist/index.mjs` builds
`fileGlobs` from the source expression, resolver and extension configuration,
then invokes `fastGlob.sync`. Thus the affected implementation is reachable in
build tooling. Source, dependency or configuration changes influencing those
patterns are the relevant input boundary. An end-to-end malicious-source build
was not attempted, and no additional attacker privilege is assumed from the
dependency graph alone.

**Lint:** `@next/eslint-plugin-next/dist/utils/get-root-dirs.js` passes
`settings.next.rootDir` to `fast-glob.globSync` when it is a string or array.
The current `eslint.config.mjs` does not set it; that observed default uses
`context.cwd` directly. Changing this setting changes the exposure assessment.

**Production server and browser bundles:** `server/start.mjs` imports the
separate `vinext/server/prod-server` export and serves existing build output.
It does not invoke `vinext build` for each request. Some Vinext modules under
`dist/build/` are shared runtime helpers; their directory names alone do not
establish build-plugin loading. In an isolated Node 22.13.1 run, ESM-load and
CommonJS-load instrumentation observed 90 unique module files during startup
and 15 actual HTTP checks. Vinext runtime modules were loaded; none of the
other seven affected package names was observed loaded. A textual scan of
97 emitted JS/source-map files (18,844,036 bytes) found no affected package
imports/paths or the selected brace-expansion helper markers.

No HTTP-controlled route to the vulnerable parser was identified in the
inspected source or exercised requests. These observations do **not** prove
all routes, optional modes, dynamic imports or minified copies unreachable.
Text scanning can miss renamed/inlined code. This is not comprehensive browser
or hosted runtime acceptance, and dependency presence remains confirmed.

**Bounded package reproduction:** caught local calls on Node 22.13.1 reproduce
`RangeError: Maximum call stack size exceeded` with a 9,003-character pattern
containing 4,500 nested brace groups through Braces compile/expand and each
installed `fast-glob.generateTasks`. Ordinary `app/{page,layout}.tsx` controls
return successfully. A 9,001-character nested-parenthesis variant fails in
Braces compile but returns in expand and both fast-glob paths. No uncaught
application crash or remotely exploitable KFM request was demonstrated.

The component defect remains present. Product-boundary exploitability remains
`needs_review`, rather than confirmed public-service exploitation or a false
positive. The eight original package entries remain individually visible in
the evidence; they are grouped here only to explain their shared root cause.

## Compatible-fix assessment

| Candidate observed in registry/audit | Assessment |
|---|---|
| Braces latest 3.0.3; advisory patched versions: none | Already installed; no patch upgrade available. Older versions are also in the affected range. |
| Micromatch latest 4.0.8 | Already installed; still depends on `braces ^3.0.3`. |
| Fast-glob latest 3.3.3 | Nested copy already uses it; moving the lint copy from 3.3.1 would retain the same affected Braces chain. |
| Dynamic-import latest 1.6.0 / CommonJS latest 0.10.4 | Already installed; retain the affected chain. |
| Next ESLint plugin latest 16.4.2 | Still declares `fast-glob 3.3.1`; upgrading Next lint configuration would not remove the advisory. |
| Audit suggestion: `eslint-config-next@14.2.35` | Partial chain avoidance, not a complete fix. Its ESLint peer range is `^7.23.0 || ^8.0.0`, incompatible with installed ESLint 9.39.4; the Vinext chain remains. Do not use `npm audit fix --force`. |
| Upstream Vinext latest 1.2.1 | Still depends on CommonJS `^0.10.4`; also changes React/RSC peers to `^19.3.1` and RSC plugin to `^0.5.37`. Replacing the local repaired archive is neither a narrow compatible fix nor a solution to this advisory. |

Moving packages to `devDependencies` would change counts or installation shape,
not repair the component; this hosting composition requires build tools during
deployment. No audit suppression, fabricated patched version, blanket override,
framework replacement or custom vendor backport is introduced.

## Practical mitigations and remaining work

Keep runtime on the existing `npm start` → `server/start.mjs` production path;
do not expose Vite's local development server. The existing provider preview
`npm run dev` builds and then starts that same production server; it is distinct
from `dev:local`. Keep uploaded/remote data and request values out of build/lint
glob configuration, generated source and dynamic-import templates. Review code,
dependency and build-config changes before deployment. Isolate builds from
private stores and runtime credentials and retain existing CI time limits.
These are mitigations and review requirements, not newly verified provider
controls or a repair for arbitrary attacker-controlled patterns.

Recheck the advisory and npm registry before the next dependency update. A
patched upstream Braces release accepted by the existing dependency ranges, or
a compatible upstream consumer change eliminating **both** affected chains,
would justify a focused package/lock update. Verify every installed copy, keep
existing overrides, run clean installation, audit, build, types, relevant lint,
ordinary/malformed pattern checks and the application regressions below. If an
untrusted runtime pattern feature is later added, bound/reject pattern structure
at its shared input boundary and test compile/expand variants; current package
length defaults alone did not prevent the reproduced failures.

Until then, retain the HIGH audit result and unresolved public reachability
question. Passing functionality tests does not constitute dependency-security
acceptance. No risk acceptance, owner approval or publication exception is
recorded by this report.

## Validation and reproducibility

No application or dependency byte changes were made. `npm ci --no-audit
--no-fund` installed 528 packages with npm 11.9.0 / Node 24.19.0; build, type,
focused and HTTP checks used Node 22.13.1, matching the existing CI version.

| Check | Result |
|---|---|
| Fresh full and `--omit=dev` npm audits | FAIL: eight HIGH, zero CRITICAL; one advisory |
| Locked installation / `npm ls ... --all --json` | PASS; installed versions match lock |
| `npm run build` including staging and identity | PASS; 58 browser assets staged |
| `npx --no-install tsc --noEmit` | PASS |
| Existing identity/assets/security/menu/mobile/navigation/compressed-file tests | 42 PASS, zero failed/skipped |
| Existing `godaddy-node-runtime.test.mjs` against local built Node server | 15 PASS, zero failed/skipped |
| `scripts/build-identity.mjs --verify` against that server | `APPLICATION_INPUTS_MATCH` |
| Deeply nested library/fast-glob patterns | Defect reproduced; ordinary controls succeed |
| Hosted publication, browser rendering, model operation, full suite, broad lint | Not performed; no change to these surfaces |

Two preliminary HTTP runs could not connect to a server started in a different
execution. The final server and tests shared one execution, waited for readiness,
passed all 15 checks, verified identity and terminated the local process. No
application change was made to obtain the pass; no hosted failure is inferred.

Reproduce the dependency observations from the exact source checkout:

```bash
npm ci
npm ls braces micromatch fast-glob vite-plugin-dynamic-import vite-plugin-commonjs vinext eslint-config-next @next/eslint-plugin-next --all --json
npm audit --json
npm audit --omit=dev --json
npm view braces version versions dist-tags --json
npm view micromatch version dependencies --json
npm view fast-glob version dependencies --json
npm view vite-plugin-dynamic-import version dependencies --json
npm view vite-plugin-commonjs version dependencies --json
npm view @next/eslint-plugin-next version dependencies --json
npm view eslint-config-next@14.2.35 peerDependencies --json
npm view vinext version dependencies peerDependencies --json
```

Audits are expected to exit nonzero while the advisory remains. The focused
checks were:

```bash
npm run build
npx --no-install tsc --noEmit
node --test tests/build-identity.test.mjs tests/build-identity-http.test.mjs tests/public-client-assets.test.mjs tests/site-security-http.test.mjs tests/header-focus.test.mjs tests/explorer-menu-dismissal.test.mjs tests/mobile-compatibility.test.mjs tests/workspace-map-navigation.test.mjs tests/workspace-help-navigation.test.mjs tests/node-compressed-assets.test.mjs
# Start an isolated local production server and wait until /api/build is ready.
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5190 node --test tests/godaddy-node-runtime.test.mjs
node scripts/build-identity.mjs --verify http://127.0.0.1:5190
```

The unchanged application-input digest is
`sha256:4d57cc63b876327eb2841fe2f383d2d8ebf6896ecbcedf50153baa20af0cea8e`.
The evidence includes hashes of package, lock and vendor archive. This digest
does not attest build bytes, settings, live data or release authority.

## Preservation and rollback

This documentation/evidence change reuses existing `docs/` and
`data/receipts/generated/` responsibilities under Directory Rules v2 / ADR-0029.
It adds no schema, dataset, registry or release authority. The private Sites
composition, GoDaddy source selection, production configuration, source identity
code, public assets, private stores and rollback assets are unchanged.

Reverting this documentation PR changes no application bytes and does not fix
or worsen the inherited advisory. Continue to use the separate
[source/live acceptance and rollback procedure](repository-live-alignment.md).
The dated published baseline remains `4b3cc837e9c131e5eb214427e0a55646fc76e52a`
in that procedure; no fresh provider observation or publication is claimed here.
