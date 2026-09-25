# Kansas Frontier Matrix Explorer

A map-first spatial evidence demonstration for exploring how Kansas features,
time, provenance, correction state, access limits, and bounded Focus outcomes
fit together.

## Current public scope

This directory is the monorepo implementation. The working Site is preserved in
a standalone-root source history, while this application retains the monorepo
layout and package boundaries. Do not merge a standalone Site mirror into
monorepo `main`. See the [current identity and source-alignment
hold](docs/sites-source-alignment.md).

- The renderer-neutral shell exposes site-local synthetic or generalized GeoJSON catalog metadata; renderer source and layer loading remain held.
- Nothing in this build is a released operational KFM dataset.
- Evidence resolution fails closed: missing, stale, restricted, denied, and
  error states never become unsupported answers.
- Public-safe exports preserve evidence context and withhold protected geometry.
- The repository and source briefing reports implementation boundaries; it does
  not release or publish data.


## Safe UI failure fallback

[`main.tsx`](main.tsx) mounts the React recovery boundary from
[`app/error.tsx`](app/error.tsx) around the Explorer, About route, and auxiliary
UI. A child render or lifecycle failure replaces that tree with an alert and
focuses its heading. **Try again** remounts the view once per user action; a
persistent failure returns to the fallback. Saved browser-local workspaces are
not cleared, but unsaved component state may be lost. **Return to Explorer**
opens `/` when retry cannot recover the current view.

The fallback and React root diagnostics expose only `KFM-UI-UNEXPECTED-ERROR`
and a bounded, sanitized own-data correlation digest. Raw exceptions, component
stacks, and request data are not passed to the diagnostic logger. A missing or
unsafe digest is reported as `unavailable`; recovery never invokes digest getters.

This catches React child rendering/lifecycle failures. It does not catch module
load failures before mounting, event-handler errors, arbitrary asynchronous
callbacks, or errors in the fallback itself. Expected evidence denial, stale,
and abstention states retain their existing UI. Full cross-surface and hosted
acceptance remain open under [issue #4416](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4416).

Run `node --test tests/error-boundary.test.mjs` for composition, transpilation,
and diagnostic-negative checks. Run `node tests/error-boundary.browser.mjs`
from this directory and open its printed loopback URL for a mounted React
regression. The page reports PASS/FAIL and its assertions. Repeat with `/about`,
`/?surface=spine`, `/?surface=repair`, and `/?kind=effect` (also `null`,
`undefined`, `string`, and `unsafe-digest`). Stop the server with Ctrl+C.
The browser fixture uses the real entrypoint and boundary with synthetic child
components and no styles or network data; it checks cleanup, repeated failure,
retry, focus, stored workspace bytes, provenance labels, and safe diagnostics.
It does not establish full application, WebGL, hosted, or independent acceptance.

## Authoritative hosting and in-place replacement

| Field | Current boundary |
|---|---|
| OpenAI Sites project | `appgprj_6aa0b1c41bc08191bfd86003920f1631` from [`.openai/hosting.json`](./.openai/hosting.json) |
| Existing slug | `kansas-frontier-matrix-explorer` |
| Existing public URL | <https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site> |
| Authoritative host | OpenAI Sites; [issue #4232](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4232) records the adapter decision |
| Current evidence | [Identity and source-alignment hold](./docs/sites-source-alignment.md); the older replacement handoff and v1 receipt are historical |
| Hosted version state | The 2026-09-17 Sites readback records a successful v45 deployment, but v45 mirror equality, production-browser acceptance, and recovery remain `HOLD` |

The staged 2026-09-03 replacement ZIP is an external, digest-bound Sites execution
input. It is not the canonical repository source and must not be copied over this
application or used to import its standalone CDN MapLibre acquisition pattern.
Repository integration continues through the accepted package-owned renderer seam;
this app remains renderer-neutral until that separate dependency and validation path
is closed.

A Sites-enabled operator must verify the active project and exact candidate source,
save and inspect a new version before deployment, retain the immediately preceding
Site version as the rollback target, and return current-project evidence. The
historical v1 receipt and 2026-09-03 replacement ZIP are not current execution
inputs. Repository branch work does not deploy or restore a Site version. The
repository homepage already points to the existing Sites URL.

The checked-in v1 receipt schema, fixture, validator, and replacement handoff retain
the historical project binding as lineage. They must not validate a current-project
operation. A current deployment stays held until an exact current-project receipt
contract and source-equivalence proof are reviewed. Neither repository metadata nor
a Sites deployment record authorizes a release or publication.

The repository application uses Vite and React, with `/` and `/about` selected
in `main.tsx`, through the package-owned
`NullMapRuntime`. TypeScript and Vite resolve the `@kfm/maplibre` facade to the
accepted workspace package root, following the same renderer-neutral pattern as
`explorer-web`; the child manifest acquires no renderer or internal package by
an external or `file:` dependency. Styles, sources, layers, workers, hit
testing, and screen measurement remain held pending a dependency-closed
consumer migration. D1 and R2 are intentionally unbound in this monorepo
hosting manifest; that does not describe or modify the active Site's hosted
bindings.

## Prerequisites

- Node.js `>=22.13.0`
- Linux with `flock`, `curl`, and GNU `timeout`

## Sites Lifecycle

The Sites lifecycle CLI runs the locked dependency install before returning this checkout. Edit the source under `app/`, then checkpoint when a coherent milestone is ready to inspect or share. The remote Sites builder runs `npm run build` against the pushed commit. Do not repeat install or build as a normal pre-checkpoint step.

This project does not use `wrangler.jsonc`.

`install:ci` is intentionally a single, non-retrying `npm ci`. It refuses a concurrent install for the same project, consumes a matching image-seeded npm cache with `--prefer-offline` while retaining registry fallback for a missing cache object, otherwise uses the registry, limits npm to one socket, and terminates a stalled install. `build` first requires a strict TypeScript no-emit pass, then applies a short timeout to Vite. These helpers target Linux and use GNU `timeout`; they are not native macOS scripts.

Scripts that need writable project-scoped home, npm, XDG, and temporary paths use `scripts/sites-env.sh`. The `dev` and `start` scripts honor the caller's runtime environment and keep Wrangler logs inside the checkout. The generated `.sites-runtime/` directory is disposable and ignored by Git.

## Implementation shape

- `main.tsx` composes the React client, sanitized root diagnostics, and recovery
  boundary, then selects the Explorer or About view.
- `app/` contains the Explorer UI, local fixtures, and finite evidence behavior.
- `vite.config.ts` builds the client and Worker and resolves the sibling map package.
- `.openai/hosting.json` preserves the existing Sites identity; D1/R2 are unbound here.
- `worker/index.ts` serves the built assets. The removed database, Drizzle, and
  Next-specific authentication helpers are not available in this application.
- The remaining orphan D1 notes example was removed because its database module,
  schema, and dependency had already been removed. No live database was changed.

## Authentication boundary

The client does not implement server request-header access or ChatGPT sign-in
helpers. Do not treat browser state as authenticated identity or import removed
server helpers. Hosted audience and authentication behavior require independent
verification against the existing Sites deployment; repository checks do not
change those controls.

## Browser-local waveform preview

The Import utility includes a bounded Raspberry Shake-compatible **local file** preview. It accepts one MiniSEED file plus matching StationXML, one NSLC channel, a 10-minute/100,000-sample limit, and only the uncompressed encodings listed in `app/waveform-preview.ts`.

The preview is deliberately `UNADMITTED_BROWSER_PREVIEW`: no provider URL, FDSN query, proxy, cache, upload, download, source registry entry, evidence/release handoff, response correction, event detection, or deployment is present. Matching response metadata and visible attribution are blocking checks; the resulting state remains `HOLD` even when the raw-value sparkline is available. See [`docs/sources/catalog/raspberry-shake-waveforms.md`](../../docs/sources/catalog/raspberry-shake-waveforms.md) for the provider-term and rollback gate.

## Diagnostic Commands

- `npm run install:ci`: perform the one bounded lockfile install
- `npm run dev`: start the Vite development server
- `npm run build`: require TypeScript no-emit success, then build the Vite artifact
- `npm run start`: preview the built Vite application
- `npm test`: type-check, build, and run the repository app and lint-compatibility tests
- `node --test tests/hosting-boundary.test.mjs`: verify Sites identity, replacement handoff, and host non-effects
- `npm run typecheck`: check all included TypeScript without emitting files

Use build commands for targeted diagnosis after a remote failure, not as part of the normal checkpoint path.

The timeout defaults can be overridden for a controlled canary with `SITES_INSTALL_TIMEOUT`, `SITES_INSTALL_KILL_AFTER`, `SITES_BUILD_TIMEOUT`, and `SITES_BUILD_KILL_AFTER`. A timeout fails the command; the helpers never retry an unchanged install or build.

## Learn More

- [Vite guide](https://vite.dev/guide/)
