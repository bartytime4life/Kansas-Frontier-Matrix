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

Open the local address printed by Wrangler. The launcher uses the built Site in
a local Cloudflare Worker simulator, creates an empty local D1 schema on first
run, and keeps local D1/R2 state under the ignored `source/.wrangler/` directory
across builds. It binds to `127.0.0.1:4173` by default; set `SITE_HOST` or
`SITE_PORT` to change the listening address or port. The Site source has its own
npm lockfile and is deliberately outside the repository's root pnpm workspace.
Run its npm commands from `apps/site/source/`.

### Local configuration

| Setting or binding | Current use |
| --- | --- |
| `SITE_HOST`, `SITE_PORT` | Read by `serve-local.sh`; default `127.0.0.1:4173`. |
| `DB`, `BUCKET` | Names declared in `source/.openai/hosting.json`; local Vite/Worker configuration supplies simulated D1/R2 bindings. |
| `KFM_STEWARD_EMAILS`, optional `KFM_STEWARD_USER_IDS` | Private server-side allowlists for hosted steward review. Do not commit values. |
| `.wrangler/local-state/`, `.sites-runtime/` | Ignored local simulator state and install cache; neither contains hosted data. |

The local launcher uses the built Worker and binds to loopback by default. The source's `npm run dev` uses Vite's separate development configuration, which currently binds to `0.0.0.0`; choose the launcher for a loopback-only check. Changing a template environment variable does not change a hosted Site setting.

The snapshot includes checked-in static assets and the D1 schema migration.
Live provider responses, private D1 submission and review records, private R2
uploads, and external local archives are not copied into Git. Local D1/R2
development bindings do not grant access to production records. Read the
[Site README](source/README.md) for feature details and historical notes.
