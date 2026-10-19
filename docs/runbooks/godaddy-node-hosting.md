<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-node-hosting
title: KFM GoDaddy Node application operation and source alignment
type: runbook
version: v1
status: verified deployment observations; hosted chat held off on Published
owners: ["@bartytime4life"]
created: 2026-10-17
updated: 2026-10-19
policy_label: public
current_path: docs/runbooks/godaddy-node-hosting.md
owning_root: docs/
responsibility: Identify the existing Node deployment, select its exact standalone source, validate changes and verify or roll back application delivery
truth_posture: CONFIRMED provider dashboard, Publish log and public /api/build observations on 2026-10-19; 2026-10-17 app q9r9beo47t observations superseded; broader acceptance remains separate
related:
  - godaddy-hosting.md
  - godaddy-hosted-capture.md
  - ../../apps/site/README.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# GoDaddy Node application: source, verification and rollback

Open the [existing KFM dashboard](https://host.godaddy.com/nodejs/projects/urdng3v1vk)
first. The menu route is **Hosting → Node.js Hosting → My Apps → Kansas-Frontier-Matrix
(urdng3v1vk)**. Re-read the provider's app list, source branch and Published and
Preview tabs before each operation. A linked branch, latest GitHub commit, preview
and public deployment can all differ, and on 2026-10-19 the app itself had changed.

## Verified starting point, 2026-10-19

| Surface | Observed identity | Meaning |
|---|---|---|
| Repository | [bartytime4life/Kansas-Frontier-Matrix](https://github.com/bartytime4life/Kansas-Frontier-Matrix) | Shared repository with distinct monorepo and standalone Node histories |
| Public application | [kansasfrontiermatrix.com](https://kansasfrontiermatrix.com/) | GoDaddy Node.js 22 app `urdng3v1vk`, named Kansas-Frontier-Matrix, on the Web Hosting Plus Launch plan |
| Connected source branch | `a0-qwen-ui-readiness-20261019` | The only branch this app deploys. Fast-forwarded on 2026-10-19 to `a0-hosted-ai-web-20261017` at `70af1b5225` |
| Published source | [`70af1b522563a24170a1cd4f1c1ec4b85d576a84`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/70af1b522563a24170a1cd4f1c1ec4b85d576a84) | Provider Published tab; public `/api/build` `sourceDigest` `sha256:397d915a0bd7…` matches a clean checkout of this commit |
| Hosted chat, Published | `KFM_HOSTED_AI=0` on the Publish secrets | Live `/api/ai/status` reports `HOSTED_AI_NOT_CONFIGURED` |
| Hosted chat, Preview | `KFM_HOSTED_AI` on | Preview loads the Qwen3-0.6B model successfully |
| Retired app | `q9r9beo47t` | No longer exists; `q9r9beo47t.preview.c38.airoapp.ai` returns 404. Earlier commits and receipts that name it are history |
| Unrelated app | `github-import` (`4s11gvd19s`) | A different site in the same account; never deploy KFM source to it |
| Preserved Site mirror | [`apps/site/source/`](../../apps/site/README.md) | Separate source lineage, preservation instructions and review receipts; do not replace it with the Node tree |

These are dated observations. The provider dashboard and fresh source readback
must supersede this table when state changes. The provider's `*.airoapp.ai`
delivery URL identifies the existing Node hosting app; it does not authorize
creating a different product or hosting application.

Merging a pull request into `a0-hosted-ai-web-20261017` deploys nothing. The
change reaches Preview or Published only after `a0-qwen-ui-readiness-20261019`
is fast-forwarded to it (or the app's source branch is deliberately changed) and
the provider builds and publishes that commit.

The 2026-10-17 baseline in app `q9r9beo47t` (Published `4b3cc837`, Preview
`500a0993`, connected branch `a0-hosted-ai-web-20261017`) is superseded. The
private Sites history and old checkpoints are not evidence of current public
routing.

### Hosted model on Plus Launch

The Plus Launch plan cannot hold the Qwen3-0.6B chat model. On Published the
operating system killed the model process during load, and the Publish log
recorded `[KFM hosted AI] MODEL_UNAVAILABLE:MODEL_PROCESS_KILLED`. Before
[PR #5328](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5328) the model ran inside the web process, so the same kill took the whole
server down and GoDaddy answered 503. Since PR #5328 the model runs in its own
child process and the Explorer keeps serving when it is killed. Hosted chat
stays off on Published (`KFM_HOSTED_AI=0`) until a plan or model change is
separately qualified. Preview's successful load does not establish Published
capacity.

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
git -C kfm-godaddy-review checkout --detach 70af1b522563a24170a1cd4f1c1ec4b85d576a84
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

## Build identity

`scripts/build-identity.mjs` and public `/api/build` are live in the Published
source above. Prebuild generates an application-input digest from allowlisted source
roots and package/configuration inputs. Hidden state, private stores, model
caches, generated browser assets, tests and documentation are excluded. Symlinked
source inputs are held. The response contains only application identity,
digest, file count, optional clean-checkout commit and scope; it reads no live
environment or database. A dirty checkout cannot claim its parent commit as the
source of changed bytes. Archive builds without Git retain a comparable digest
and explicitly omit a commit.

Compare the deployed target with the same source checkout:

```bash
node scripts/build-identity.mjs --print
node scripts/build-identity.mjs --verify https://kansasfrontiermatrix.com
```

The checker fails on differing inputs, absent/blocked/invalid identity, redirects
or oversized responses. `APPLICATION_INPUTS_MATCH` establishes bounded source
input parity only. Verify browser assets, real workflows, data rights and release
state independently. A test pass, digest or publication does not close those gates.

The hosted build reports `sourceCommit: null` and `commitState: WORKTREE_MODIFIED`
because the provider's checkout is not clean. Compare `sourceDigest`, not the
commit field; on 2026-10-19 the public digest matched a clean local checkout of
`70af1b5225`.

## Preview, publication and acceptance

1. In the dashboard, confirm the app ID (`urdng3v1vk`), its source branch
   (`a0-qwen-ui-readiness-20261019` as of 2026-10-19) and the Published commit.
   Compare public `/api/build` with `node scripts/build-identity.mjs --print` from
   a clean checkout of that commit. Stop and refresh this runbook if any differ.
2. Record the public rollback commit, preview commit, connected branch and
   unfinished work. Compare the exact candidate against the public source and
   check overlapping open PRs. Keep preservation and review receipts intact.
3. Complete build, type, changed-area and Node HTTP checks. Review dependency
   findings without relabeling inherited findings as repaired. Check desktop and
   mobile rendering, keyboard navigation and the actual changed workflows.
4. Verify the intended branch and exact commit in GoDaddy before **Update Preview**.
   Preserve ongoing preview work; preview and production may share stores.
   Do not enable a preview capture worker or alter storage during source testing.
5. Check the resulting Preview commit and browser behavior. A healthy provider
   label alone does not prove a successful cold browser load.
6. Apply required release review and owner authorization before **Publish to Live**.
   An owner publication hold was recorded on 2026-10-17 for the AI candidate.
   Publishing `70af1b5225` on 2026-10-19 kept hosted chat off on Published;
   this runbook neither clears that hold nor grants a limited-publication exception.
7. Re-read Published commit, check the canonical origin and public build identity
   when present, and repeat the changed workflows in a fresh live browser.
   Report code, CI, preview, publication and browser results separately.

On 2026-10-17 the production-based alignment candidate at `2cdf48a` (branch
`a0-public-alignment-20261017`) deliberately excludes the newer AI candidate
changes. Its separate review must identify that exact scope; it cannot
be used as approval for other pending commits. Free report exports, draft labels,
source uncertainty, private-operation denial and publication controls remain.

## Outage triage

A 503 from GoDaddy's proxy with no CSP or HSTS headers and about 3.5 s latency
means the Node process is down; the application did not answer. Application
errors, including 404s, carry the KFM CSP and HSTS headers. Read the **Publish** log in the dashboard,
not the Preview log: Preview runs separately and can be healthy while Published
is down. Look for a build failure, a crash on start or an out-of-memory kill.
Since [PR #5328](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5328), `MODEL_UNAVAILABLE:MODEL_PROCESS_KILLED` alone leaves the
Explorer serving with chat unavailable.

`KFM_NODE_STARTUP … outcome UNREACHABLE errorCode EACCES` is GoDaddy's loopback
sandbox refusing the startup self-check; it is not a failed start. The healthy
Preview logs the same line. Before changing code, confirm that the app ID, source
branch and Published commit still match the checklist above; on 2026-10-19 the
outage first looked like a code fault in a branch the app no longer deployed.

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
