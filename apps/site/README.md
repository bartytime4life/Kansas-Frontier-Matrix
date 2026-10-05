> **Local maintenance candidate — 2026-10-05:** five files under `source/`
> carry local candidate `aa10a86fde8ca80cdd52a1c02bf50def4a4ab2e8` on top of
> Site v153: dotenv startup refusal, its regression, and three setup/recovery
> documents. This candidate has not been saved or deployed through Sites.
> `site_mirror.py --diagnose` lists the five differences; `--check` retains
> `MIRROR_REVIEW_REQUIRED` until source reconciliation and mirror review.
> The historical receipt is preserved, not rewritten to approve these changes.

> **Recorded v153 source checkpoint — 2026-10-05:** the [v153 file-level receipt](../../data/receipts/generated/site-mirror-v153-water-paths-candidate-20261005.json)
> pins 370 byte-identical Site source paths at `da94de300c1b20dc98e9f527ba54613cfd696f8b`.
> Site v153 is saved and privately deployed; v152 is the previous deployed version. Source parity does not
> establish hosted behavior, reviewed data, or acceptance. The dated notes
> below are historical. See the [water runbook](../../docs/runbooks/water-pilot.md).

> **Water delivery candidate — 2026-09-30:** source/ mirrors unpublished standalone candidate `6aced94d7bc935723c92441a7caa0bba416aeab1`, based on private Site v130 and including the Kansas-only historical-map filter. The live owner-private Site v131 was separately built from v130 with only that six-file fix, source `75d749ed5711ab20e3edabeb1c6ba135417ec1c0`. The [file-level receipt](../../data/receipts/generated/site-water-mirror-20260930.json) records source digests, the reviewed synthetic-recipe retirement, this follow-up, and the distinct hosted checkpoint. Repository-only Earth Engine and soil-state fixes were reconciled first. The dated checkpoints below are historical; hosted parity is not claimed. See the [water runbook](../../docs/runbooks/water-pilot.md).

> **Historical overlay and radar candidate — 2026-09-30:** The standalone Site candidate `6e8d79e507741608e8f5475c53fe82fb668b44fa` adds on-demand Kansas GeoTIFF layers and the complete bounded NOAA live loop. The [file-level comparison](../../data/receipts/generated/site-historical-overlay-mirror-20260930.json) records 232 identical files, 19 inherited repository overlays, and no missing or unexpected differences. This candidate is not deployed or activated; local browser acceptance was blocked by the admin browser security check. The repository retains its separate water and soil controls.

# GPT Site source

> **Repository checkpoint (2026-09-28):** `main@de2dcbd38a70af7668a18eac968e2b217390adfb`
> includes the v106 weather playback mirror, v107 demo-layer retirement, and a
> later repository-only Earth Engine restoration. The private Explorer uses
> [the stable Site address](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site).
> The Site project and this GitHub repository retain separate Git histories.

`source/` is the GitHub source for the private Explorer Site. Its version
history is distinct from the hosted deployment history:

| Checkpoint | Recorded relationship |
| --- | --- |
| Private Site v104, source `b6d1c7471ffd95a40934bbc0b768ceacf7ebe751` | Historical 2026-09-28 publication and 224-file source parity recorded by [the v104 mirror receipt](../../data/receipts/generated/genrec-explorer-site-v104-mirror-20260928.json) and merged PR #4786. That parity applies to the v104 snapshot only. |
| Private Site v106, source `26ca5ad192a7a911acd0f75c6e2b2b37d7bd5e64` | Weather playback fixes were privately hosted and eight changed files were mirrored in [PR #4787](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4787), merged as `e2bdc7a9abbcb649f3047ccc0725c9e0d9577c5c`. |
| Private Site v107, source `8012c8a0d8cc9d86aa2d6868bce163a742460c63` | Demo extent and county starter layers were retired in the privately published Site, then mirrored in [PR #4788](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4788), merged as `19a8147702ec80bdf9556d691c37f170addee51a`. |
| Repository after v107 | [PR #4789](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4789), merged as `de2dcbd38a70af7668a18eac968e2b217390adfb`, restored Earth Engine inventory export, zoom-0 tiles, and preview parity in GitHub. No matching Site deployment is established by that merge. |

The current repository source must not be described as byte-identical to a
deployed Site without a fresh same-version comparison and hosted readback.
The v104 receipt remains an immutable record of its historical comparison;
it does not attest to later repository heads. Repository merge, source admission,
Site deployment, publication, and acceptance require separate evidence and decisions.

The repository-local
`.gitattributes` remains outside `source/`; private hosted D1/R2 records and
local development state are excluded.

## Run locally

The repository-wide dependency and configuration map is in [Installation](../../docs/installation.md). This Site uses its own npm lockfile, separate from the root pnpm workspace.

Use Node.js 22.13 or newer on Linux. The install helper also needs `flock`,
`curl`, `sha256sum`, and GNU `timeout`.

```bash
cd apps/site/source
npm run install:ci
npm run build
../serve-local.sh
```

Open the printed local address. The launcher uses the built Site in a local
Cloudflare Worker simulator, creates an empty local D1 schema on first
run, reapplies the additive `drizzle/` migrations (governed water, Kansas
knowledge and crop CASMA tables) on every launch, and keeps local D1/R2 state
under the ignored `source/.wrangler/` directory across builds. It refuses to
start if a later migration is not purely `CREATE ... IF NOT EXISTS`, or if
the `drizzle/*.sql` files and `drizzle/meta/_journal.json` disagree (an
unlisted file, a listed file that is missing, or entries out of sequence). It binds
to `127.0.0.1:4173` by default; set `SITE_HOST` or `SITE_PORT` to change the
listening address or port. The Site source has its own npm lockfile and is
deliberately outside the repository's root pnpm workspace. Run its npm commands
from `apps/site/source/`.

After a build, `../smoke-local.sh` (run from `apps/site/source/`) starts the
launcher on a temporary empty state and checks every API route that can answer
without a provider: D1-backed reads give their empty-store answers, and the
other routes give their deliberate validation (400), sign-in (401),
same-origin (403) or not-configured (503) refusals. It then stops the launcher.
It needs no provider network. The script lists every `app/api` route as either
smoke-checked or provider-only, and fails if a route file is in neither list.
The `explorer-site` workflow runs lint, typecheck, `npm test` and this smoke
check for changes under `apps/site/`; a green run is not evidence of hosted
behaviour or release.

The smoke runner refuses an occupied or invalid port before launching or making
HTTP requests. If the normal local Site already uses 4173, run
`SITE_PORT=4175 ../smoke-local.sh` with an unused port. It verifies its launched
process remains alive and stops with a startup failure if bounded readiness
checks expire; that failure is not reported as a set of route failures.
Startup regressions run with `python3 tests/qa/test_site_smoke.py` from the
repository root and use disposable stub processes, never the operator's store.

After applying migrations, `serve-local.sh` serves through the Site's direct
Miniflare launcher, `source/scripts/serve-local-worker.mjs`. Wrangler's
development proxy can return an intermittent 500 for the request after one
whose body the Worker never read; see `source/docs/local-pc-consolidation.md`.
The direct launcher binds only to loopback, requires Node 22.x and refuses
`.dev.vars`. When `SITE_HOST` is not `127.0.0.1`, `SITE_PORT` is below 1024,
Node is not 22.x or a `.dev.vars` or `.env` file is present (Wrangler loads
local secrets from either), the launcher falls back to
`wrangler dev` and prints why. Both runtimes read the same local D1/R2 state.
The smoke check sends bodies only to routes that read them, so it also passes
under that fallback.

### Local audit scope — 2026-10-05

At repository base `8537dc9a1f650ccdcbfe8d08d9d440562e4488db`, the local Site
served its home, Earth Engine, Data, Stewards, and Knowledge pages. Its reviewed
water, knowledge, and soil reads reported their explicit no-active-package
states; the local reviewed-imagery catalog answered successfully. These are
HTTP checks, not rendered map acceptance. Browser inspection was denied because
the admin-enforced security check could not be verified.

The local source candidate passed build, lint, TypeScript, and 386 Node tests.
The repository smoke runner passed 48 checks across 41 routes with disposable
storage; nine provider-only routes remained unprobed. Three new startup tests
first failed on the original runner, then passed with busy-port, invalid-port,
and failed-readiness guards. This audit changed no provider adapters, data
admission, active packages, hosted storage, or Site audience.

The initial repository documentation scan checked 1,813 documents and 62,208
local targets, finding 141 missing targets and 39 missing anchors. Twelve
unambiguous navigation links in the atmosphere/fauna runbooks and source
descriptor standard were repaired; the changed-document link check passes.
The remaining 168 findings include unresolved authority documents, proposed
paths, retired application references and historical navigation. They remain
open; no placeholder file or doctrine redirect was created to silence them.
External links were not requested. Earlier audit and dependency results in
dated documents remain historical.

Rollback the local runtime by selecting the preserved v153 source/build and
restarting only its local service with the same explicit physical state path.
Reverting the repository candidate restores its previous smoke runner and
documentation. Neither operation changes hosted versions or releases.

### Local configuration

| Setting or binding | Current use |
| --- | --- |
| `SITE_HOST`, `SITE_PORT` | Read by `serve-local.sh`; default `127.0.0.1:4173`. A non-loopback host or a port below 1024 selects the `wrangler dev` fallback. |
| `SITE_STATE_DIR` | Optional local D1/R2 state directory for `serve-local.sh`; default `source/.wrangler/local-state`. `smoke-local.sh` sets it to a temporary directory that it removes afterwards. |
| `DB`, `BUCKET` | Names declared in `source/.openai/hosting.json`; local Vite/Worker configuration supplies simulated D1/R2 bindings. |
| `KFM_STEWARD_EMAILS`, optional `KFM_STEWARD_USER_IDS` | Private server-side allowlists for hosted steward review. Do not commit values. |
| `KFM_EARTH_ENGINE_OWNER_EMAILS`, `KFM_EARTH_ENGINE_OWNER_IDS` | Comma-separated owner allowlists for the Earth Engine context API (catalog, staging, activation, tiles) and its installer page. Unset, the API answers 503 "not configured" to signed-in users (401 when signed out) and the installer page is a 404. |
| `KFM_HISTORICAL_OWNER_EMAILS`, `KFM_HISTORICAL_OWNER_IDS` | Comma-separated owner allowlists for historical-map review and activation. Unset answers 503 "not configured" to signed-in users. |
| `KFM_HISTORICAL_WORKER_TOKEN` | Bearer secret of at least 32 characters shared with the local historical-map worker for `/api/historical-topo/queue` and `/stage`. Unset answers 503 "not configured". Do not commit it. |
| `KFM_LOCAL_REVIEWED_IMAGERY_ORIGIN` | Set only by `scripts/serve-local-worker.mjs --local-reviewed-imagery`; allows reviewed Earth Engine imagery reads from that exact loopback origin. |
| `QWEN_ENDPOINT` (or `QWEN_OLLAMA_URL`, `OLLAMA_BASE_URL`), `QWEN_MODEL` (or `OLLAMA_MODEL`, default `qwen3:8b`), optional `QWEN_API_KEY` | Server-side Qwen/Ollama endpoint for `/api/qwen`; it must be HTTPS or loopback HTTP. Unset answers 503 `not_configured`, and the browser offers the copyable grounded prompt instead. |
| `.wrangler/local-state/`, `.sites-runtime/` | Ignored local simulator state and install cache; neither contains hosted data. |

The local launcher uses the built Worker and binds to loopback by default. The source's `npm run dev` uses Vite's separate development configuration, which currently binds to `0.0.0.0`; choose the launcher for a loopback-only check. Changing a template environment variable does not change a hosted Site setting.

The snapshot includes checked-in static assets and the D1 schema migrations.
Live provider responses, private D1 submission and review records, private R2
uploads, and external local archives are not copied into Git. Local D1/R2
development bindings do not grant access to production records. Read the
[Site README](source/README.md) for feature details and historical notes.
