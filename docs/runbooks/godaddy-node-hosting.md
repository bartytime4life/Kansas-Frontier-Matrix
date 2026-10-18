<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-node-hosting
title: KFM GoDaddy Node application operation and source alignment
type: runbook
version: v1
status: verified deployment observations; alignment changes pending review and publication
owners: ["@bartytime4life"]
created: 2026-10-17
updated: 2026-10-17
policy_label: public
current_path: docs/runbooks/godaddy-node-hosting.md
owning_root: docs/
responsibility: Identify the existing Node deployment, select its exact standalone source, validate changes and verify or roll back application delivery
truth_posture: CONFIRMED provider and live-browser observations on 2026-10-17; candidate publication and broader acceptance remain separate
related:
  - godaddy-hosting.md
  - godaddy-hosted-capture.md
  - ../../apps/site/README.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# GoDaddy Node application: source, verification and rollback

Open the [existing KFM dashboard](https://host.godaddy.com/nodejs/projects/q9r9beo47t)
first. The menu route is **Hosting → Node.js Hosting → My Apps → q9r9beo47t**.
Re-read the provider's Published and Preview tabs before each operation. A linked
branch, latest GitHub commit, preview and public deployment can all differ.

## Verified starting point, 2026-10-17

| Surface | Observed identity | Meaning |
|---|---|---|
| Repository | [bartytime4life/Kansas-Frontier-Matrix](https://github.com/bartytime4life/Kansas-Frontier-Matrix) | Shared repository with distinct monorepo and standalone Node histories |
| Monorepo main | `0be787703daa842bbc2d33e9d941b1c09794cd87` | Repository documentation and governed implementation; root build intentionally returns `WORKFLOW_HOLD` |
| Public application | [kansasfrontiermatrix.com](https://kansasfrontiermatrix.com/) | GoDaddy Node.js 22, app `q9r9beo47t`, North America |
| Published source | [`4b3cc837e9c131e5eb214427e0a55646fc76e52a`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/4b3cc837e9c131e5eb214427e0a55646fc76e52a) | Provider Published tab; root `package.json` and `server/start.mjs` belong to this standalone composition |
| Preview source | `500a09935951b5bec7965174236c6aac33c3e933` | Provider Preview tab after a fresh dashboard reload; separate from public source |
| Connected source branch | `a0-hosted-ai-web-20261017` at `34fb6018ea9668ae81e64aa94b3948d4351147e8` | Ahead of both observed deployments; dashboard reports preview out of sync |
| Preserved Site mirror | [`apps/site/source/`](../../apps/site/README.md) | Separate source lineage, preservation instructions and review receipts; do not replace it with the Node tree |

These are dated observations. The provider dashboard and fresh source readback
must supersede this table when state changes. The provider's `*.airoapp.ai`
delivery URL identifies this existing Node hosting app; it does not authorize
creating a different product or hosting application.

The public map reached **MapLibre 6.9.0 ready** with five selected layers in a
desktop browser. One selected source needed attention; ready rendering does not
establish that every external provider or source is healthy. The private Sites
history and old checkpoints are not evidence of current public routing.

## Choose the correct source

Preserve existing work and use a fresh checkout of the exact reviewed standalone
commit. Its root contains `app/`, `server/`, `scripts/`, `public/`, `package.json`,
`package-lock.json` and `godaddy-source.json`. The latter records migration lineage;
its historical `source_commit` is not the current deployment commit.

Never deploy monorepo `main` into this Node app: its workspace-coordinator root
package has intentional build/test/lint holds. Do not deploy the static
[`apps/public-site/`](../../apps/public-site/README.md) bundle or execute the
historical cPanel DNS plan against this working Explorer.

For the verified public baseline, a separate checkout can be prepared with:

```bash
git clone --no-checkout https://github.com/bartytime4life/Kansas-Frontier-Matrix.git kfm-godaddy-review
git -C kfm-godaddy-review checkout --detach 4b3cc837e9c131e5eb214427e0a55646fc76e52a
```

Before a later deployment, select its separately reviewed exact commit instead.
The connected branch may contain held AI candidates; selecting its newest head
is not a release decision.

## Runtime and local checks

Use Node.js 22.13 or newer within the provider's Node 22 runtime. Install from the
standalone lockfile with `npm ci`. Build with `npm run build`; then run
`npx tsc --noEmit` and proportional changed-area Node tests. The production entry
is `server/start.mjs`, and `npm start` respects the provider-assigned `PORT`.
`npm run dev` performs a production build and starts that same Node server for
the provider's preview process. The full `npm test` command also builds first.

For a bounded local smoke on a free port:

```bash
PORT=5187 npm start
```

In another terminal, target the actual production HTTP tests:

```bash
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5187 node --test tests/godaddy-node-runtime.test.mjs
```

Keep required runtime packages in `dependencies`. Exclude secrets, `node_modules`,
private stores and recovery archives from uploaded packages. Preserve database,
account, model and capture settings; a source alignment does not configure or
activate them. The [capture scheduler](godaddy-hosted-capture.md) retains its own
identity, capacity, rights and activation gates.

## Candidate build identity

The alignment candidate adds `scripts/build-identity.mjs` and public `/api/build`.
These are **pending publication**, not verified features of the public baseline
above. Prebuild generates an application-input digest from allowlisted source
roots and package/configuration inputs. Hidden state, private stores, model
caches, generated browser assets, tests and documentation are excluded. Symlinked
source inputs are held. The response contains only application identity,
digest, file count, optional clean-checkout commit and scope; it reads no live
environment or database. A dirty checkout cannot claim its parent commit as the
source of changed bytes. Archive builds without Git retain a comparable digest
and explicitly omit a commit.

Once the candidate is deployed, compare its target with the same source checkout:

```bash
node scripts/build-identity.mjs --print
node scripts/build-identity.mjs --verify https://kansasfrontiermatrix.com
```

The checker fails on differing inputs, absent/blocked/invalid identity, redirects
or oversized responses. `APPLICATION_INPUTS_MATCH` establishes bounded source
input parity only. Verify browser assets, real workflows, data rights and release
state independently. A test pass, digest or publication does not close those gates.

## Preview, publication and acceptance

1. Record the public rollback commit, preview commit, connected branch and
   unfinished work. Compare the exact candidate against the public source and
   check overlapping open PRs. Keep preservation and review receipts intact.
2. Complete build, type, changed-area and Node HTTP checks. Review dependency
   findings without relabeling inherited findings as repaired. Check desktop and
   mobile rendering, keyboard navigation and the actual changed workflows.
3. Verify the intended branch and exact commit in GoDaddy before **Update Preview**.
   Preserve ongoing preview work; preview and production may share stores.
   Do not enable a preview capture worker or alter storage during source testing.
4. Check the resulting Preview commit and browser behavior. A healthy provider
   label alone does not prove a successful cold browser load.
5. Apply required release review and owner authorization before **Publish to Live**.
   An owner publication hold was recorded on 2026-10-17 for the AI candidate;
   this runbook neither clears it nor grants a limited-publication exception.
6. Re-read Published commit, check the canonical origin and public build identity
   when present, and repeat the changed workflows in a fresh live browser.
   Report code, CI, preview, publication and browser results separately.

The production-based alignment candidate at `2cdf48a` (branch
`a0-public-alignment-20261017`) deliberately excludes the newer AI candidate
changes. Its separate review must identify that exact scope; it cannot
be used as approval for other pending commits. Free report exports, draft labels,
source uncertainty, private-operation denial and publication controls remain.

## Rollback and maintenance

Keep the previous published application commit available. Roll back application
source through a reviewed revert or the provider's verified retained deployment
mechanism, then verify the Published identity, map, assets, routes and private
denials. Do not restore or migrate a database, import datasets, change DNS or
restore an obsolete Sites host as an application rollback. Storage rollback
requires its own reviewed procedure and evidence.

After every approved release, refresh the dated source/deployment observation,
verify linked resources and repeat the input comparison. External HTTP 403 or
provider outage is **unverified availability**, not proof that a source URL is
broken. Record the limitation rather than inventing a replacement source.

Placement follows the supplied Directory Rules PDF's responsibility model and
accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md):
operator documentation belongs in existing `docs/runbooks/`; the Node composition
retains its existing application roots. No parallel schema, policy, registry,
release or canonical data authority is introduced.
