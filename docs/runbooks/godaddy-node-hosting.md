<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-node-hosting
title: KFM GoDaddy Node application operation and source alignment
type: runbook
version: v2
status: source-grounded operation guide; earlier deployment observations retained as dated history
owners: ["@bartytime4life"]
created: 2026-10-17
updated: 2026-10-21
policy_label: public
current_path: docs/runbooks/godaddy-node-hosting.md
owning_root: docs/
responsibility: Identify the existing Node deployment, select its exact standalone source, validate changes and verify or roll back application delivery
truth_posture: CONFIRMED source inspection at main 91ca0314 and hosted 65d56575 on 2026-10-21; historical dashboard observations are not a fresh live readback
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

## Implementation snapshot, 2026-10-21

This review inspected monorepo
[`91ca0314f0158736f69f953d7973457c19442fde`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/91ca0314f0158736f69f953d7973457c19442fde)
and hosted source
[`65d5657536e4c42a7a8ea0772ed12ca0b78bc939`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/65d5657536e4c42a7a8ea0772ed12ca0b78bc939).
Code and test presence are **CONFIRMED**; this documentation-only review did
not execute the application suite, inspect GoDaddy settings or verify a live
browser, database or physical PC. The earlier provider readbacks below remain
dated history. They do not establish today's Published source or AI settings.

| Area | Implementation at the hosted checkpoint | Evidence and limit |
|---|---|---|
| Application and access | Standalone Node/Vinext server with React 19 and MapLibre 6.9.0. Public pages/chat have no visitor login. Private browser contribution/steward/account pages are removed. | [Package](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/package.json), [startup](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/start.mjs), [login-removal record](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/docs/login-removal-20261019.md). The record's embedded-model instructions are historical; use the AI section below. |
| Map and time | Provider context, layer controls, Underground, Observatory and 2D/terrain/globe. Calendar exit cancels HMS playback and retires historical payloads before Present hydration. | [Map wiring](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/app/page.tsx), [late-HMS regression](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/tests/hms-calendar-exit.test.mjs). Presence of this correction does not prove the live site runs it. |
| Search and nearby research | County-search readiness, loaded-point proximity, saved investigation settings and dated report snapshots. Provider context remains separate from admitted evidence. | [Search tests](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/tests/global-search-status.test.mjs), [research guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/docs/map-research-tools.md). Nearby counts cover eligible loaded points, not all county records. |
| AI and exports | Anonymous guest jobs, submitted-context binding, queue/progress/cancel, brief/expanded replies, conditional continuation and checked draft exports. Selected-source summaries and evidence discovery use deterministic paths. | [Public handler](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/public-ai-handler.mjs), [export projection](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/app/assistant-investigation.ts). Discussion remains unverified; no factual model answer or publication approval is asserted. |
| Welcome and compact time UI | Category/facet choices use the existing layer-workspace taxonomy; selected recorded capability animations replace welcome video players. A decorative hourglass transfers sand and flips with reduced-motion/visibility gates. | [Behavior and limits](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/docs/living-welcome.md). Captures show past software output; unsupported categories disclose missing captures. Browser/mobile polish requires separate acceptance. |
| Private capture and MySQL | Parameterized MySQL store, capacity/fencing controls, additive schema, capture-token run/control routes and separate public status. | [Store](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/ingestion-store.mjs), [access gate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/capture-worker-access.mjs), [capture runbook](godaddy-hosted-capture.md). Applied schema, production credentials, capacity and scheduled operation are unverified. |
| Aviation | Main has a private FAA candidate adapter/transform/schema and proposed MySQL migration; the hosted airport route validates bounded queries then returns `ABSTAIN / AVIATION_RELEASE_PROFILE_REQUIRED` before any store/upstream access. | [Aviation intake](aviation-intake-20261021.md), [held reader](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/server/aviation-read.mjs). No released aircraft tracking, airport rendering or OpenSky activation is claimed. |

**Pending outside this snapshot:** [PR #5394](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5394)
proposes a Census-boundary county selector for Near here, saved settings and
report context. It was open at review, with head
`988a44c4367f48b419977108533ac84be48a71e9`; it is not included in the pinned
hosted commit. Check current GitHub metadata before describing it as merged.

## AI and second-PC boundaries

The inspected `selectAiProvider` accepts only explicit
`KFM_AI_PROVIDER=home-ollama`, with the existing master switch, exact origin,
paired transport/profile and pinned model identity. Missing, malformed, unknown
or retired provider selections fail closed. `server/start.mjs` contains no
embedded model startup; `hosted-qwen3` is retired for this public composition.
The retained Sites adapter has its own contract and must not be substituted.

Visitors talk to the website. GoDaddy applies guest-job, context, evidence and
output checks. The paired gateway performs inference through signed HTTPS or
the outbound polling relay; browser clients receive no home endpoint or machine
credential. An unavailable model does not select another provider. Evidence
search and source summaries have separate paths when the public AI service is
configured. Generated discussion stays `ABSTAIN / UNVERIFIED_AI_DISCUSSION`;
factual model answers remain withheld pending qualification and evidence.

The hosted [home-inference guide](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/65d5657536e4c42a7a8ea0772ed12ca0b78bc939/docs/home-ollama-inference.md)
records an earlier functional remote response and queue-aware timeout changes.
That is repository-recorded history, not a fresh physical-PC/process inspection.
Longer allowances require compatible deployed gateway/worker/profile settings;
a source merge alone does not apply them to the PC.

The owner intends the largest files to live on the second AI Linux PC. Its
actual storage paths, free space, connectivity, resource contention with AI,
backup arrangements and restore proof remain **NEEDS VERIFICATION**. Existing
capture code still stores bounded archive chunks in MySQL; it does not implement
the intended bulk-file relocation. Follow the [aviation placement assessment](aviation-intake-20261021.md#physical-placement-and-database-reconciliation)
and [private store runbook](local-pc-data-store.md) before choosing physical paths.
Preserve the installed AI setup, keys, model weights and original copies.

## Provider readback, 2026-10-20

The repository record dated October 20 reports app `urdng3v1vk` connected to
`a0-hosted-ai-web-20261017`. Its Published tab reports commit
`c59c38a58248793b651bb265c082573663473d31`, with Infra and Site status OK.
That record reports the public Explorer opened anonymously. This revision observation
supersedes the earlier connected-branch and Published-source rows below; it does
not independently verify public build-digest parity or model configuration.

The monorepo `godaddy-public-site` workflow is build-only after retirement of
its historical static transfer job. It retains validation and a review artifact
but cannot acquire hosting credentials or create a competing deployment. Keep
the GoDaddy Node application as the sole intended public production path.
Private Sites preservation and Public Staging remain separate; neither is
unpublished by this source change. Historical deployment records are retained.

<a id="verified-starting-point-2026-10-19"></a>

## Historical verified starting point, 2026-10-19

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

The temporary `a0-qwen-ui-readiness-20261019` branch was the delivery route at
this October 19 checkpoint. The October 20 readback above records a later
connection to `a0-hosted-ai-web-20261017`; do not require the temporary branch
today. A merge is not evidence that Preview or Published updated. Verify the
current provider connection, actual deployed commit and resulting runtime.
Any build/publication action needs its own applicable authorization.

The 2026-10-17 baseline in app `q9r9beo47t` (Published `4b3cc837`, Preview
`500a0993`, connected branch `a0-hosted-ai-web-20261017`) is superseded. The
private Sites history and old checkpoints are not evidence of current public
routing.

<a id="hosted-model-on-plus-launch"></a>

### Historical embedded-model failure on Plus Launch

At the October 19 checkpoint, the attempted Qwen3-0.6B model load exceeded the
Published environment's observed capacity. On Published the
operating system killed the model process during load, and the Publish log
recorded `[KFM hosted AI] MODEL_UNAVAILABLE:MODEL_PROCESS_KILLED`. Before
[PR #5328](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5328) the model ran inside the web process, so the same kill took the whole
server down and GoDaddy answered 503. Since PR #5328 the model runs in its own
child process and the Explorer keeps serving when it is killed. The recorded response was to keep hosted chat off on Published
(`KFM_HOSTED_AI=0`). These are historical settings and an embedded-model incident,
not instructions to turn off the newer paired-home provider. Current source has
removed that embedded runtime. Preview success never establishes Published
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

For local review of the October 21 inspected application, prepare a separate
checkout (this is not a claim that the commit is Published):

```bash
git clone --no-checkout https://github.com/bartytime4life/Kansas-Frontier-Matrix.git kfm-godaddy-review
git -C kfm-godaddy-review checkout --detach 65d5657536e4c42a7a8ea0772ed12ca0b78bc939
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

The inspected source implements `scripts/build-identity.mjs` and public
`/api/build`; the earlier public readback is dated above. Prebuild generates an application-input digest from allowlisted source
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

On 2026-10-19 the hosted build reported `sourceCommit: null` and
`commitState: WORKTREE_MODIFIED`; its digest matched a clean checkout of
`70af1b5225`. Compare a fresh response with the selected candidate rather than
reusing that result. A missing commit must not be inferred from a branch label.

## Preview, publication and acceptance

1. In the dashboard, confirm the app ID (`urdng3v1vk`), its source branch
   (`a0-hosted-ai-web-20261017` in the dated 2026-10-20 readback) and the Published commit.
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

During the earlier outage, proxy 503s lacked KFM CSP/HSTS headers and arrived
after about 3.5 seconds. Treat that pattern as a clue that the application may
not have answered; verify with current provider logs and a fresh response. The
inspected server installs application headers, including on its error responses. Read the **Publish** log in the dashboard,
not the Preview log: Preview runs separately and can be healthy while Published
is down. Look for a build failure, a crash on start or an out-of-memory kill.
For older embedded-model deployments, [PR #5328](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5328) isolated the model so a
`MODEL_UNAVAILABLE:MODEL_PROCESS_KILLED` could leave the Explorer serving. The
October 21 inspected source removes that embedded execution path entirely.

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

Placement follows the adopted [Directory Rules](../doctrine/directory-rules.md)
and accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md):
operator documentation belongs in existing `docs/runbooks/`; the Node composition
retains its existing application roots. No parallel schema, policy, registry,
release or canonical data authority is introduced.
