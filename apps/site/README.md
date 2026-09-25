# GPT Site source

`source/` imports the 187-file Kansas Frontier Matrix Explorer Site version 71,
saved from commit `62c6ef9da35bdcd11929502a386f4f9da07448ac`. The deployed
Site's saved version points to that commit. Two corrections were made in this
repository: `scripts/earth-engine/requirements.txt` pins Pillow 12.3.0 instead
of the vulnerable 11.3.0, and the About page uses "1 m" instead of "one-meter"
for a static USGS source title to avoid a false telemetry keyword match. The
other 185 imported files retain their original bytes. The repository-local
`.gitattributes` file sits outside `source/` to preserve the imported formatting.

## Run locally

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

The snapshot includes checked-in static assets and the D1 schema migration.
Live provider responses, private D1 submission and review records, private R2
uploads, and external local archives are not copied into Git. Local D1/R2
development bindings do not grant access to production records. Read the
[Site README](source/README.md) for feature details and historical notes.
