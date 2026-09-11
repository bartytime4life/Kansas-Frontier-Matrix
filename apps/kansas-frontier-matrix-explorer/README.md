# Kansas Frontier Matrix Explorer

A map-first spatial evidence demonstration for exploring how Kansas features,
time, provenance, correction state, access limits, and bounded Focus outcomes
fit together.

## Current public scope

This section describes the tracked repository implementation, not a fresh production observation.

- The renderer-neutral shell exposes site-local synthetic or generalized GeoJSON catalog metadata; renderer source and layer loading remain held.
- Nothing in this build is a released operational KFM dataset.
- Evidence resolution fails closed: missing, stale, restricted, denied, and
  error states never become unsupported answers.
- Public-safe exports preserve evidence context and withhold protected geometry.
- The repository and source briefing reports implementation boundaries; it does
  not release or publish data.

## Repository and saved Site reconciliation

**Reviewed implementation pin:** `main@664e46697d4d237870f5a482904bb9acd8f11b20`, 2026-09-11. Repository code, saved Site source, and production/released state require separate evidence.

| Surface | Supported statement | Not established |
|---|---|---|
| This checkout | The tracked Sites-derived app retains its renderer-neutral boundary. [PR #4464](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4464) merged catalog scroll, keyboard/discovery, and requested/time-compatible count affordances. | A requested or time-compatible layer is not proof of renderer delivery, source admission, or a deployed change. The eight-fixture Library projection was not expanded by #4464. |
| Explorer Web sibling | [Explorer Web](../explorer-web/README.md) mounts a package-owned Living Atlas MapLibre composition with inline synthetic/generalized data. [The package manifest](../../packages/maplibre/package.json) pins `maplibre-gl@6.7.0`. | The sibling's renderer, test results, and catalog capabilities do not migrate into this app by documentation or shared package name. |
| Saved Site checkpoint | The [Drive backfill](https://docs.google.com/document/d/1uROL1Hkgr15oe2nH-9B2MUXdmzt2KSBo6ay1jt5dh4s/edit) records saved v24 at source `acf6499d99bd1b7c131e79b17735f95145ef808f`, including external smoke/station context and registry/control improvements. | That checkpoint says its change did not deploy. It does not establish current production version, repository byte parity, rights clearance, or released data. Its build/test totals belong to that saved-source checkpoint only. |
| Coordination | [Notion backfill coordination](https://app.notion.com/p/3d7a92021bf681a4ae8cc75930b302f2) and the [repository backfill record](../../docs/architecture/kfm-explorer-site-real-data-backfill-20260910.md) retain source lineage and handoff context. | Coordination text is not implementation, independent review, source admission, or a deployment receipt. Re-pin any post-merge branch before using its remaining delta. |

### Source handoff gates

Before a capability moves from the saved Site into a reviewable repository implementation, bind the exact source and changed paths; preserve fixed upstream allowlists, bounded payloads/time windows, finite failures, and a single owner for layer state. Do not replace the repository app wholesale or expand the fixture Library to simulate real-data integration.

| Domain or surface | Required distinction and bounded next evidence |
|---|---|
| Smoke | Keep HMS footprints, observed air quality, forecast/model transport, and alerts separate. Retain source interval, geometry/density semantics, freshness, gaps, and artifact identity. Footprint animation is not a measured surface exposure or an inferred wind field. |
| Hydrology | Bind the gauge/reach identity, parameter, statistic, unit, qualifier, observation time, and join confidence. An ambiguous reach join must abstain; missing, stale, and unavailable must not appear as zero flow. |
| Terrain / LiDAR | Distinguish rendered hillshade/slope from raw point clouds and numerical elevation. Require exact work-unit/asset, acquisition date, CRS, vertical reference, units, resolution, nodata, accuracy, and derivative lineage before admitting numeric samples; keep 1x default exaggeration. |
| Time and hazards | Separate observation, model-valid, acquisition, publication/retrieval, and UI-selection time. Preserve real frame intervals, explicit gaps, expiry/correction, and latest-selection-wins behavior; never manufacture historical coverage or an all-clear. |

**Raspberry Shake provider check — 2026-09-11:** the [FDSN manual](https://manual.raspberryshake.org/fdsn.html) describes station metadata separately from miniSEED waveforms, does not support an event service, and serves data at least 30 minutes old rather than real-time streaming. The [current license](https://raspberryshake.org/license/) restricts waveform redistribution through another server and distinguishes integration/use classes. **KFM gate:** review the exact metadata, cache/proxy, attribution, waveform, and use-class permissions separately before extending this handoff. Neither endpoint reachability nor station visibility establishes redistribution permission. No permission decision or live bridge is made here.

KFM does not issue, confirm, rescind, or replace emergency, health, engineering, regulatory, or life-safety instructions.

### Validation and rollback boundary

This refresh changes documentation only. No fresh application build, unit, browser, hosted-CI, production, saved-version, or restoration evidence is claimed. Review the documentation delta separately from all prior implementation checks. Under [issue #4024](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024), retain branch-only delivery where the PR path is quarantined; a merge elsewhere is not approval for this change. Reverting these documentation commits restores the prior text, not a prior Site runtime.

## Authoritative hosting and in-place replacement

| Field | Current boundary |
|---|---|
| OpenAI Sites project | `appgprj_6a870a079c1c8191abb7401ef092a181` from [`.openai/hosting.json`](./.openai/hosting.json) |
| Existing slug | `kansas-frontier-matrix-explorer` |
| Existing public URL | <https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site> |
| Authoritative host | OpenAI Sites/Vinext; [issue #4232](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4232) records the adapter decision |
| Vercel boundary | [`vercel.json`](./vercel.json) disables automatic Git deployment; Vercel remains non-authoritative for this app |
| Replacement procedure | [OpenAI Sites in-place replacement handoff](./docs/openai-sites-in-place-replacement.md) |
| Hosted version state | `NEEDS VERIFICATION` from the Sites version-history and production browser surfaces |

The staged 2026-09-03 replacement ZIP is an external, digest-bound Sites execution
input. It is not the canonical repository source and must not be copied over this
application or used to import its standalone CDN MapLibre acquisition pattern.
Repository integration continues through the accepted package-owned renderer seam;
this app remains renderer-neutral until that separate dependency and validation path
is closed.

A Sites-enabled operator must save and inspect a new version before deployment,
retain the immediately preceding Site version as the rollback target, and return the
receipt defined by the app-local handoff. Repository branch work does not deploy or
restore a Site version. GitHub repository-homepage metadata still requires the
separate settings-only action tracked in [issue #4246](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4246).

The application runs as a single-route Vinext site through the package-owned
`NullMapRuntime`. TypeScript and Vite resolve the `@kfm/maplibre` facade to the
accepted workspace package root. Unlike this retained null-runtime boundary,
`explorer-web` now also mounts the package-owned Vite adapter for its inline
synthetic Living Atlas canvas. The child manifest here acquires no renderer
or internal package by an external or `file:` dependency. Styles, sources, layers, workers, hit
testing, and screen measurement remain held pending a dependency-closed
consumer migration. D1 and R2 are intentionally unbound in the repository
hosting declaration; production bindings were not inspected in this refresh.

## Prerequisites

- Node.js `>=22.13.0`
- Linux with `flock`, `curl`, and GNU `timeout`

## Sites Lifecycle

The following lifecycle describes a Sites-managed checkout. A commit to a GitHub review branch is not a Sites checkpoint or deployment command.

The Sites lifecycle CLI runs the locked dependency install before returning this checkout. Edit the source under `app/`, then checkpoint when a coherent milestone is ready to inspect or share. The remote Sites builder runs `npm run build` against the pushed commit. Do not repeat install or build as a normal pre-checkpoint step.

This project does not use `wrangler.jsonc`.

`install:ci` is intentionally a single, non-retrying `npm ci`. It refuses a concurrent install for the same project, consumes a matching image-seeded npm cache with `--prefer-offline` while retaining registry fallback for a missing cache object, otherwise downloads and verifies the complete vinext tarball recorded in `package-lock.json`, limits npm to one socket, and terminates a stalled install. `build` applies a short timeout. These helpers target Linux and use GNU `timeout`; they are not native macOS scripts.

Scripts that need writable project-scoped home, npm, XDG, and temporary paths use `scripts/sites-env.sh`. The `dev` and `start` scripts honor the caller's runtime environment and keep Wrangler logs inside the checkout. The generated `.sites-runtime/` directory is disposable and ignored by Git.

## Implementation shape

- edit site code under `app/`
- `app/chatgpt-auth.ts` provides optional dispatch-owned ChatGPT sign-in helpers
- `.openai/hosting.json` declares optional Sites D1 and R2 bindings
- `vite.config.ts` simulates declared bindings for local development
- `db/index.ts` reads the D1 binding from the Cloudflare Worker environment
- `db/schema.ts` starts intentionally empty
- `examples/d1/` contains an optional D1 example surface
- `drizzle.config.ts` supports local migration generation when needed

## Workspace Auth Headers

OpenAI workspace sites can read the current user's email from
`oai-authenticated-user-email`.

SIWC-authenticated workspace sites may also receive
`oai-authenticated-user-full-name` when the user's SIWC profile has a non-empty
`name` claim. The full-name value is percent-encoded UTF-8 and is accompanied by
`oai-authenticated-user-full-name-encoding: percent-encoded-utf-8`.

Treat the full name as optional and fall back to email when it is absent:

```tsx
import { headers } from "next/headers";

export default async function Home() {
  const requestHeaders = await headers();
  const email = requestHeaders.get("oai-authenticated-user-email");
  const encodedFullName = requestHeaders.get("oai-authenticated-user-full-name");
  const fullName =
    encodedFullName &&
    requestHeaders.get("oai-authenticated-user-full-name-encoding") ===
      "percent-encoded-utf-8"
      ? decodeURIComponent(encodedFullName)
      : null;

  const displayName = fullName ?? email;
  // ...
}
```

## Optional Dispatch-Owned ChatGPT Sign-In

Import the ready-to-use helpers from `app/chatgpt-auth.ts` when the site needs
optional or required ChatGPT sign-in:

- Use `getChatGPTUser()` for optional signed-in UI.
- Use `requireChatGPTUser(returnTo)` for server-rendered pages that should send
  anonymous visitors through Sign in with ChatGPT.
- Use `chatGPTSignInPath(returnTo)` and `chatGPTSignOutPath(returnTo)` for
  browser links or actions.
- Pass a same-origin relative `returnTo` path for the destination after sign-in
  or sign-out. The helper validates and safely encodes it.
- Mark protected pages with `export const dynamic = "force-dynamic"` because
  they depend on per-request identity headers.

Dispatch owns `/signin-with-chatgpt`, `/signout-with-chatgpt`, `/callback`, the
OAuth cookies, and identity header injection. Do not implement app routes for
those reserved paths. Routes that do not import and call the helper remain
anonymous-compatible.

SIWC establishes identity only; it does not prove workspace membership. Use the
Sites hosting platform's access policy controls for workspace-wide restrictions,
or enforce explicit server-side membership or allowlist checks.

Use SIWC for account pages, user-specific dashboards, saved records, and write
actions tied to the current ChatGPT user. Leave public content anonymous.

## Diagnostic Commands

- `npm run install:ci`: perform the one bounded lockfile install
- `npm run dev`: start the Vite/Vinext development server
- `npm run build`: build the deployable Sites artifact
- `npm run start`: start the built Vinext application
- `npm test`: build and verify the rendered development-preview metadata
- `node --test tests/hosting-boundary.test.mjs`: verify Sites identity, replacement handoff, and host non-effects
- `npm run db:generate`: generate Drizzle migrations after schema changes

Use build commands for targeted diagnosis after a remote failure, not as part of the normal checkpoint path.

The timeout defaults can be overridden for a controlled canary with `SITES_INSTALL_TIMEOUT`, `SITES_INSTALL_KILL_AFTER`, `SITES_BUILD_TIMEOUT`, and `SITES_BUILD_KILL_AFTER`. A timeout fails the command; the helpers never retry an unchanged install or build.

## Learn More

- [vinext Documentation](https://github.com/cloudflare/vinext)
- [Drizzle D1 Guide](https://orm.drizzle.team/docs/get-started/d1-new)
