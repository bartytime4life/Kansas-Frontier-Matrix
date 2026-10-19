<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/public-staging-qwen-workspace-20261019
title: Embedded Qwen workspace and Sites account adapter
type: verification-record
version: v1
status: frontend implemented; live Qwen connection blocked; review pending
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-19
policy_label: public
owning_root: docs/
responsibility: Record recovered Node work, the bounded Sites adapter, verification and exact remaining connection steps
truth_posture: CONFIRMED source and bounded tests; live inference and hosted sign-in acceptance NEEDS VERIFICATION
[/KFM_META_BLOCK_V2] -->

# Embedded workspace and account controls

The owner reported that v9 still omitted the existing Qwen/login experience.
The prior update copied a welcome/theme subset while retaining an external Chat
link. This successor brings the embedded workspace into the same restricted Site.
CONTRACT_VERSION is `3.0.0`.

## Recovered work and exact sources

| Source | Verified role |
|---|---|
| #5163 | Node 22 HUD account controls, PC job integration and same-page conversation; private SQLite roles/sessions stay in Node |
| #5260 | Hosted SmolLM2 replaced by pinned Qwen3 0.6B INT8, distinct from the larger PC Qwen; private-preview acceptance recorded, public publication held |
| #5254 | Separate PC Qwen3.6 35B update, not a Worker or hosted small-model fallback |
| #5279–#5281 | Unified Find / Ask / Evidence, tab history, investigation isolation, source rechecks, phone layout/focus and Prairie Field Desk design |
| Hosted source | `a0-hosted-ai-web-20261017@7b02dc22369f97b68577f821dc9dc7021e91cde5`, tree `26dd6711161fd1142b57f6f35fd29769ba96e818` |
| Starting Site v9 | `appgprj_6acd1aafe0d88191a4306ea2ab44ed91`, source `2d67acf487b4846fd1388ec959ae3b60f5cd7765`, tree `002e5d6322ea11b4e923476065298b7d12a3fc2f` |
| GitHub v9 proposal | #5283, `05800628ed99a1a5ce3b413d6a5c8152d8caa77c`; exact v9 tree, open and unmerged at comparison |
| Governed main | `14ad5d8c6b34badbcf6e4c026afc9d39aeb217bd`; private `apps/site/source` remains separate |

## What now works in the source

- Same-page Find / Ask / Evidence composer, discussion drafts, conversation
  controls, source rechecks and investigation exports reuse the hosted frontend.
  The launcher no longer sends users to the other website.
- Find continues to work without a model. Existing public county/source holds
  remain truthful, and discussion starters neither autosend nor claim coverage.
- Account is reachable at desktop and phone widths. It displays platform identity
  or an ordinary top-level Sites `signin-with-chatgpt` link, plus sign-out. No
  password form, Node role grant or account migration is introduced. Existing
  GoDaddy account controls are explicitly linked as a separate realm.
- Evidence checks re-read this Site's catalog on every check/export. Empty/held
  delivery abstains. A future approved delivery does not create a knowledge index.
  Evidence IDs are untrusted correlation values only; no server question/history
  store is created, and these stateless checks contain no private request payload.
- Optional Qwen calls require platform identity, same-origin JSON POSTs and the
  authenticated Node adapter. Only submitted question + bounded display year/view
  may leave Sites. Selections, record IDs, attributes, locations, private drafts,
  filters, account fields and held data are excluded. Model discussion is always
  unverified; factual `ANSWER` responses/source citations are refused here.

The Node adapter is a separate review proposal on the existing hosted branch.
It calls the same public Qwen handler, preserving its global budgets, job/session
ownership, model pin and output checks. Its opaque actor partition is separate
from Node account/admin APIs. Node cookies remain server-side; no model weights,
SQLite records, account passwords or private caches are copied.

## Live connection is not completed

The existing preview `https://q9r9beo47t.preview.c38.airoapp.ai/api/ai/status`
returned HTTP **401** during this task. Staging environment revision **2** contains
no Qwen origin/token configuration. The model's actual service cannot run inside
the Sites 128 MB Worker: its Node preview records multi-gigabyte memory needs.
No alternative model or fabricated ready status is substituted.

Exact remaining steps, after review and using the existing Node 22 preview:

1. Install the companion `server/sites-qwen-handler.mjs` and its bounded
   `/api/sites-qwen/v1/[...path]` route from the companion GitHub proposal. Preserve
   the Node model/cache/database, existing public runtime and production version.
2. Configure a new random, shared 32-byte base64url service credential as secret
   `KFM_SITES_QWEN_TOKEN` in that Node environment and secret
   `KFM_STAGING_QWEN_TOKEN` in this Site. Keep it outside source/browser artifacts.
3. Set `KFM_STAGING_QWEN_ORIGIN` to the reviewed reachable Node origin. Only the
   canonical KFM origin and the existing GoDaddy preview origin are accepted.
   The provider's preview access layer must permit this authenticated service
   request; setting a token alone does not bypass the observed HTTP 401.
4. Retain `KFM_HOSTED_AI=1` and its matching `KFM_HOSTED_AI_ORIGIN`, and verify the
   Node adapter names pinned Qwen, not SmolLM2 or the PC worker. Verify Site status,
   one bounded unverified discussion, Stop, follow-up isolation, sign-out denial
   and unchanged evidence holds. Do not label this completed before these checks.

No GoDaddy environment, preview, production, DNS, model, account or publication
action is performed by this task. The adapter is default-off until configured.
Staging publication alone does not publish this Node feature or qualify Qwen.

## Validation and limits

- Staging: 125 focused unit/component cases pass; production Worker build, public
  asset scans, TypeScript and changed-area lint pass. The compiled Worker suite
  checks account/AI anonymous and trusted synthetic identity behavior, route/origin
  denials, guide identity and emitted bytes. Final result is recorded in the PR.
- Node adapter: 45 focused existing/new cases pass, including four adapter tests
  for authorization, exact model identity, cookie/actor separation and private
  context refusal. Production build, types and focused lint are recorded in the
  companion PR. Model output in these adapter tests is synthetic.
- Browser desktop header/workspace/account inspected. Phone 390×844 inspected;
  final 375×667 repair has root width/scrollWidth 375, first result bottom 410.34
  inside scroll region bottom 465, and composer bottom 571 inside viewport 667.
  Find input, source labels, Account link and Escape return to Find & ask verified.
  The temporary frame is removed before final build.
- WebGL2 is unavailable in the browser. No rendered 3D, real touch keyboard,
  live authenticated Node call, real model reply, full suite, account-role
  migration, production parity, general model quality or human approval claim.
- Existing public profile, catalog/release readers, source data, dependency locks,
  manifest/bindings and owner-only audience remain. Old dated receipts stay intact.

Directory Rules v2 / accepted ADR-0029 place this work in existing app, Worker,
tests, docs and generated-receipt responsibilities. No new authority/schema,
release registry or data store is created. React review checks hook cleanup,
stable investigation isolation, bounded imports, focus, native sign-in links,
derived search state and server-only identity authorization.

## Recovery

Retain v9 saved version
`appgprj_6acd1aafe0d88191a4306ea2ab44ed91~appgver_5b2cf40deba08191b1548812523c2b3f`
for same-Site rollback. Removing the optional Site token disables remote calls.
Disable the companion Node token to close its adapter, retaining existing model,
accounts, caches, public Qwen sessions, stores and release pointers. Preserve newer
source edits before any reviewed revert. Human review remains pending.
