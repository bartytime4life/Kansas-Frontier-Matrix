<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/public-staging-alignment-20261018
title: Restricted Public Staging portable alignment
type: verification-record
version: v1
status: bounded source update; review pending
owners: ["@bartytime4life"]
created: 2026-10-18
updated: 2026-10-18
policy_label: public
owning_root: docs/
responsibility: Record the exact source/deployment comparison, portable update, checks and remaining acceptance limits
truth_posture: CONFIRMED dated observations and local checks; human review and rendered WebGL acceptance NEEDS VERIFICATION
[/KFM_META_BLOCK_V2] -->

# Restricted Public Staging alignment

This change adds a task-oriented Explorer guide, keyboard section navigation,
responsive source details, and a bounded build-identity endpoint to the existing
restricted Public Staging Worker. It does not promote the private mirror or a
Node source tree into this Site. CONTRACT_VERSION is `3.0.0`.

## Actual starting point

| Surface | Exact identity observed on 2026-10-18 | Meaning |
|---|---|---|
| Monorepo main | `cefd19e66857f8bf98b4d6995174c14801deb629` | Repository/governed source; not the deployed Node root |
| Private mirror | `main:apps/site/source`, 875 tracked files | Separate preservation instructions, DB/R2 and mirror receipt; not replaced |
| GoDaddy Published | App `q9r9beo47t`, Node.js 22; `4b3cc837e9c131e5eb214427e0a55646fc76e52a` | Fresh provider Published-tab readback; canonical `https://kansasfrontiermatrix.com/` |
| GoDaddy Preview | Provider reported Idle | Current preview commit was not exposed in the inspected idle view; historical `500a099…` is not reasserted as current |
| Production-review branch | `codex/published-kfm-4b3cc-20261017@57bf6c8b3b2c09cb489ee939bb28ceab1318c97f` | Contains merged #5245 and documentation-only dependency #5249; not proof of publication |
| Newer hosted AI branch | `a0-hosted-ai-web-20261017@663eedb7845f1a8cd2f4ffeca884c5130c62ac6e` | #5230/#5233/#5248/#5250 merged; publication held; draft #5251 stays separate |
| Public Staging | `appgprj_6acd1aafe0d88191a4306ea2ab44ed91`, v7 | Native succeeded deployment `appgdep_6ad4226fba8881919d8ca0699ff604b6` |
| Deployed Staging source | `8fd126d2f0acc3a7ae99a66c4a37bb258c7840bd`, 896 files; tree `02f9a1ff7ebbe5180c0b2a13946a62418521b49f` | Same-Site source helper checkout exactly matches the native v7 saved source |
| GitHub Staging review baseline | `review-base/public-staging-v7-20261018@9043534702e853523efa7506d4fbe611fd5a5301` | Newly recorded exact v7 tree; distinct Git commit/history, no deployment implication |

Sites reports a custom access policy containing only the owner, zero external
visitors and no additional editors/groups. Its `current_live_url` metadata
returns the GoDaddy canonical domain; the native succeeded v7 deployment URL is
`https://kfm-public-staging-20261012.blackbart-55.chatgpt.site`. A matching domain,
page title or source commit alone does not establish routing or browser parity.

The existing v7 record, `docs/repository-sync-20261017.json`, already records the
Effects header, Explore/Appearance/Measure controls, map-mode/menu repair,
source status, mobile Data-sheet fix and fixed hosted-chat handoff. Those
features were inspected and tested again; this task does not redo their port.
PR #5246 updated hosting docs only. Its main merge is not a runtime release.

## File comparison at the baseline

| Comparison with v7 | Equal blobs at same path | Different blobs at same path | Staging-only paths | Other-only paths |
|---|---:|---:|---:|---:|
| main private mirror | 765 | 94 | 37 | 16 |
| production-review root at 57bf6c8 | 581 | 139 | 176 | 368 |

These are tracked source comparisons, not runtime or data parity. The public
profile, deny policy and sanitization account for deliberate differences.

## Portable change and explicit exclusions

| Upstream behavior | Staging decision |
|---|---|
| #5245 About jump navigation, original-provider links and source disclosure | Adapted to the restricted Worker's actual capabilities; no provider-data availability claims imported |
| #5245 bounded `/api/build` identity | Adapted to `kfm.sites-application-inputs/v1`, this project identity, Worker/build inputs and symbolic hosting manifest |
| Node immutable asset staging / `server/browser-headers.mjs` | Not copied: Worker build already packages hashed assets in `dist/client`; compiled Worker responses are compared with emitted bytes |
| Existing current layout/navigation | Retained from v7; new More-menu link names the Explorer guide + source |
| Node hosted inference, filesystem/model/process/account services | Not portable; no Node service is activated or published here |
| Newer AI/context/export candidates | Not imported; fixed existing external chat link transfers no staging camera, records or drafts |
| Private data and provider overlays | Still held; public profile, trusted catalog, all release readers and DB/R2 bindings retained |

Identity hashes allowlisted application sources/configuration and package inputs.
It excludes runtime secrets, private stores, generated MapLibre/h5wasm assets,
tests/docs and its own generated JSON. Browser asset delivery is checked
separately. Symlinked inputs are refused. Dirty/archive builds explicitly omit a
source commit; the visible branch link is labeled as mutable, not deployment
attestation. The API reads no environment, identity, DB or R2. Existing origin
and read-only route policy applies; `/api/build` is the only added route.

## Validation and remaining limits

- Production build, TypeScript and focused lint passed locally.
- 83 distinct focused/adjacent tests passed: 60 identity/public-boundary/release/
  map/navigation/CSS cases, 22 layout/evidence/topic cases, one compiled-Worker
  integration case. No full-suite green claim; inherited private-data/full-suite
  expectations remain outside the bounded check.
- Compiled Worker: home, guide, topics, almanacs and provider-history routes 200;
  source digest/count match current inputs; guide targets resolve; emitted
  JavaScript/CSS response hashes match build files. Private/legacy routes,
  alternate origin and identity POST remain refused; empty public catalog grants
  no data authority.
- Browser desktop guide and 390 × 844 CSS-pixel same-origin frame inspected.
  All fragment targets resolve; mobile root clientWidth and scrollWidth both 390.
  Source digest/project ID wrap, map/topic links remain usable, and section jump
  navigation works. Temporary responsive harness was removed before final build.
- Local browser Layers and reviewed-water evidence panel remain operable. Water
  reports storage unavailable / map hidden / evidence withheld in disposable
  preview state; no populated record or data-release acceptance is asserted.
- Browser reports WebGL2 unavailable; fallback and readable controls verified.
  Rendered basemap, terrain/globe/Underground and real touch-device acceptance
  remain NEEDS VERIFICATION. No actual AI/model or export-download acceptance is
  claimed. Broad accessibility, performance and independent review remain open.
- One integration attempt correctly rejected a digest mismatch while the temporary
  responsive harness was present; after removing it, the unchanged compiled
  application matched and the integration test passed.
- Dependencies/lock/vendor are unchanged. Existing production Braces findings and
  publication holds remain; this task claims no dependency remediation or
  security acceptance.

The native Site save/deployment result and PR body record any later restricted
publication identity. This authoring record is not that result. No GoDaddy
Update Preview, Publish, restart, DNS, model, audience or data-activation action
is part of this change.

## Placement, review and recovery

Directory Rules v2 and accepted ADR-0029 route this standalone surface to its
existing `app/`, `worker/`, `scripts/`, `tests/`, `docs/` and build responsibilities.
The GitHub review branch records the actual isolated public composition instead
of replacing `apps/site/source`. Its generated-work receipt uses the repository's
established `data/receipts/generated/` family; no parallel canonical schema,
policy, source registry, release store or proof authority is created. New CI is
read-only, scoped to this isolated review baseline, and contains no deployment
step or secrets. Human review remains pending; the PR stays draft.

Application recovery selects the retained v7 saved version
`appgprj_6acd1aafe0d88191a4306ea2ab44ed91~appgver_ad152997d094819199655f162f914d81`
on this same restricted Site. Preserve newer source edits and retained versions
before rollback. Keep DB/R2, private releases, owner controls, GoDaddy deployment
and all data pointers intact. Close or revert the isolated PR to undo its GitHub
proposal; merging it never publishes either host.
