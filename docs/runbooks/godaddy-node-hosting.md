<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-node-hosting
title: KFM GoDaddy Node application operation and source alignment
type: runbook
version: v2
status: source-grounded operation guide; earlier deployment observations retained as dated history
owners: ["@bartytime4life"]
created: 2026-10-17
updated: 2026-11-23
policy_label: public
current_path: docs/runbooks/godaddy-node-hosting.md
owning_root: docs/
responsibility: Identify the existing Node deployment, select its exact standalone source, validate changes and verify or roll back application delivery
truth_posture: CONFIRMED source inspection at main 91ca0314 and hosted 65d56575 on 2026-10-21; CONFIRMED public build-identity parity with 43ea4988 on 2026-11-13 and b2f20e01 on 2026-11-19; historical dashboard observations are not a fresh live readback
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

<a id="public-readback-2026-11-13"></a>

## Public readback after owner publication, 2026-11-13

This is a public-endpoint observation, not a dashboard inspection. The owner
performed **Publish**; settings, secrets and Preview were not read here.

| Step | Observation |
|---|---|
| Before | Public `/api/build` reported `sourceCommit` `82786c3e`, then the head of `a0-hosted-ai-web-20261017` |
| Merges | [#5830](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5830) (discovery layers port), [#5832](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5832) (globe zoom sizes) and [#5833](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5833) (basemap warning and Kansas Sky lifecycle fixes) merged into that branch; head `43ea4988` |
| Merge alone | For more than 20 minutes after the #5830 merge, `/api/build` (`Cache-Control: no-store`, Cloudflare `DYNAMIC`) still reported `82786c3e` |
| After Publish | `/api/build` reported `43ea4988ec31f62ebe200fd6cc915d4e5f8a3b1d`, `CLEAN_CHECKOUT`, digest `sha256:049c7791…cf4e09`, 1,254 inputs, about three minutes after the owner published |
| Parity | `node scripts/build-identity.mjs --verify https://kansasfrontiermatrix.com` from a clean checkout of `43ea4988`: `APPLICATION_INPUTS_MATCH` |
| Live checks | `/api/live-context?feed=nps-nrhp-places` returned 1,344 points (1,331 listings); its source download returned 200; a headless browser showed the drought outlook and National Register layers, NEW markers, legend chips, the four new starters and **Surprise me**, with no page errors |

Operational consequence, reconfirmed: merging into the connected branch does
not update the public application; an explicit **Publish** does. Verify with
`/api/build` and the identity checker rather than the dashboard label alone.
Input parity is not browser-asset, provider, release or accessibility acceptance.

<a id="public-readback-2026-11-13-later"></a>

### Later publications the same day: outdoor layers and a privacy correction

| Step | Observation |
|---|---|
| Merge and publish | [#5835](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5835) added the KDWP wildlife-area and Walk-In Hunting Access (WIHA) feeds and the SSURGO soil layer; merge head `c300b594`. After the owner published, the identity checker reported `APPLICATION_INPUTS_MATCH`. The feeds returned 273 wildlife-area polygons and 3,591 WIHA tracts |
| Finding | In that live readback, the WIHA payload included KDWP's free-text `NOTES` field. A few notes held landowner contract numbers, per-acre payment rates and conservation-contract expiries, which broke the layer's stated boundary |
| Correction | [#5837](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5837) stopped requesting `NOTES` and removed it from the payload and drawer; merge head `f2ff9516`. [#5838](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5838) applied the same fix to the repository Explorer |
| After Publish | `APPLICATION_INPUTS_MATCH` for `f2ff9516`. The live WIHA feed still returned 3,591 tracts, with no `notes` property and no contract or payment text. A headless browser showed both KDWP layers statewide, with no page errors and no basemap-tile warning after repeated zooming and panning |
| External outage seen | At about 23:25 UTC the NPS `nrhp_locations` MapServer itself returned `502 Bad Gateway` (Azure Application Gateway). The `nps-nrhp-places` feed reported 502, and Cloudflare replaced its JSON body with `error code: 502`. The Explorer shows the layer as unavailable; no substitute data is produced |
| CI note | One `explorer-browser` run (#5835) failed a header "More" menu focus test that the diff does not touch. The re-run on #5837 passed, and three local runs of the merged code passed |

Lesson: before merging a new external feed, read back a real provider payload
and review every free-text field, not only the declared identifier fields. The
fix was found only after publication.

<a id="public-readback-2026-11-14"></a>

### Publications on 2026-11-14: frontier trails and a chat answer fix

Each change was merged into `a0-hosted-ai-web-20261017` and published by the
owner. After each publish, the identity checker reported
`APPLICATION_INPUTS_MATCH` for the merge commit.

| Change | Merge commit | Live readback |
|---|---|---|
| [#5840](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5840) frontier trails layer | `0e119c59` | `nps-historic-trails` returned 101 segments in 127 KB, with no notes or editor fields. A headless browser showed the trails statewide, with no page errors |
| [#5842](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5842) side-by-side shared trails | `0c3f3a4c` | Oregon, California and Pony Express were visible side by side along the Topeka route |
| [#5844](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5844) trail sites | `a0b6779e` | `nps-trail-places` returned 96 sites. It left out 16 private sites and 6 sites on other corridors. No phone, email or access-note text was found |
| [#5848](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5848) chat repetition check | `24aa5e99` | "What was the Santa Fe Trail?" returned an answer twice, after failing twice before the fix |

**Chat diagnosis.** Chat with KFM reported `ready` on the home compute model
`qwen3.5:4b`, but some ordinary questions came back as "did not pass the
public output checks" (`MODEL_OUTPUT_UNQUALIFIED`). The cause was the
repetition guard. It treated any four-word phrase that appeared three times as a
loop, which rejected correct answers that repeat a name such as "the Santa Fe
Trail". After #5848, capitalized names and phrases from the visitor's own
question need five repeats, and other phrases still need three.

**After every publish.** `/api/ai/status` reads `KFM home compute (connecting)`
until the restarted app finishes its first health check of the home gateway.
On 2026-11-14 that took about 10 seconds. It is not an outage unless the status
moves to unavailable.

**Answer quality.** Answers are labeled unverified AI discussion, and the small
model can still get details wrong. In test replies it got the Santa Fe Trail's
starting point wrong and gave overstated route lengths. Model choice belongs to
the home PC, not to this repository.

<a id="public-readback-2026-11-15"></a>

### Publications on 2026-11-15: map guides, bridge clusters and outage messages

The owner published twice. After each publish, the identity checker reported
`APPLICATION_INPUTS_MATCH` for the merge commit named below.

**First publish, verified at `b95017ea`**

| Change | Live readback |
|---|---|
| [#5854](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5854) map guide pages | `/explore` and its four guides returned 200 with their titles. An unknown guide returned 404. The sitemap listed all five pages |
| [#5855](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5855) DeFlock outage backoff | The feed failed in about 0.4 s instead of about 25 s. Its explanation did not reach visitors; see the correction below |
| [#5856](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5856) one catalog category per source | The download route served a trail-site download and refused a source with no on-site download with 400 |
| [#5860](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5860) derived connection tables | No visible change; the generated connection list was byte-identical before and after |

**Second publish, verified at `1761a351`**

| Change | Live readback |
|---|---|
| [#5861](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5861) KDOT bridges as numbered clusters | All five bridge feeds returned 200: 5,580 state and 19,291 local bridges, 51 historic, 4,486 built before 1950 and 91 recorded closed. The local list was about 420 KB compressed. In a headless browser, hovering a circle summarised its bridges, selecting it zoomed in and split it, and selecting a bridge showed its full KDOT record. No page errors |
| [#5862](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5862) feed outage explanation | The DeFlock feed returned 503 with its JSON explanation, and the layer card showed "Next provider check in about 1 minute" |

**Correction to #5855.** Its description said visitors would see when the
provider is checked next. They did not, for three reasons: the host replaced the
body of a 502 with a bare `error code: 502` page, the browser reader discarded
the body of any failed response, and the layer card showed a fixed sentence.
#5862 fixed all three. That the host passes a 503 body through could only be
confirmed after publishing.

**First bridge read of the day.** The first request for a bridge layer reads
KDOT's inventory and took about 7 seconds for state bridges. Later requests are
served from the site's copy for a day and took under one second.

**Chat model.** On 2026-11-15 `/api/ai/status` reported the home compute model
as `qwen3.5:9b-q4_K_M`, replacing `qwen3.5:4b`. The "connecting" status after a
publish cleared within about 20 seconds.

**CI note.** The `explorer-browser` suite failed twice on #5862's commit, in
two different tests that change does not touch. Both were timing races in the
tests: one resized the window while a focus return was still pending, and one
reached for a panel button without waiting for it.
[#5864](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5864)
fixed both.

<a id="public-readback-2026-11-16"></a>

### Publications verified on 2026-11-16 and 2026-11-18: focus fixes, Register circles and a bridges guide

After each publish, the identity checker reported `APPLICATION_INPUTS_MATCH`
for the commit named below.

**Verified on 2026-11-16 at `58ddea48`**

| Change | Live readback |
|---|---|
| [#5870](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5870) Layers focus guard | In a headless browser, closing Layers and moving straight to the More menu left focus on More. Closing Layers without moving returned focus to the Layers button |
| [#5867](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5867) and [#5869](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5869) welcome wheel scrolling | On the welcome screen at 1280×800, a mouse-wheel scroll moved the content down 600 px |
| Bridge layers, rechecked | Hovering a circle showed its summary and selecting a bridge opened its record |

Not rechecked by hand: the "source details" focus return and the short-window
Status scrolling from #5867 and #5869. Their own browser tests passed on the
merged commit.

**Verified on 2026-11-18 at `54d4d71a`**

| Change | Live readback |
|---|---|
| [#5872](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5872) National Register markers as numbered circles | The feed returned 200 with 1,344 public points. In a headless browser at statewide scale the layer drew numbered circles. Hovering the Wichita circle showed "142 National Register markers in this area · 129 buildings · 5 districts · 1 site · 7 structures". Selecting it zoomed in and split it into 122 and 20. At zoom 13.4 in Topeka, selecting a single marker opened its record. No page errors |
| [#5873](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5873) Kansas bridges guide | `/explore/kansas-bridges` returned 200 with its title, and its map link opens the state, historic and closed bridge layers. `/explore` linked five guides, the sitemap listed all six pages, and an unknown guide returned 404 |

The commit published at `54d4d71a` also carries changes from other work that
this readback did not check beyond the identity match: Labs and data-lab changes
([#5879](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5879), [#5880](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5880), [#5881](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5881),
[#5892](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5892)), [#5878](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5878), [#5884](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5884) and
[#5885](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5885).

**DeFlock after a restart.** The provider was still down on 2026-11-16. The
first request after the publish took about 25 seconds, because a restart clears
the site's memory of the outage. The second failed in half a second with the
"next provider check" explanation.

**Feed states on 2026-11-18.** The National Register and state-bridge feeds
report `partial` because each leaves out records it cannot place: one Register
record with an invalid location or identifier, and two state bridges without a
usable Kansas location. Each layer note says so. The state feed returned 5,580
bridges, and the historic and closed feeds 51 and 91.

**Chat model.** `/api/ai/status` reported ready on `qwen3.5:9b-q4_K_M` on both
dates.

**Mirror.** [#5874](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5874) carried #5870, #5872 and #5873 into
`apps/site/source`.

<a id="public-readback-2026-11-19"></a>

### Publication verified on 2026-11-19: instant DeFlock outage answers and trail-site circles

The identity checker reported `APPLICATION_INPUTS_MATCH` for `9d472887` at
about 00:45 UTC on 2026-11-19.

| Change | Live readback |
|---|---|
| [#5906](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5906) DeFlock answers at once while its provider is failing | The provider was still down. The first request after a restart took 26.2 seconds and returned the outage sentence; the next two took 0.3 seconds. After the one-minute cooldown, the request that started the re-check returned in 0.4 seconds with "Next provider check is running now; try again in about a minute". Once that background check had failed, requests returned in under a second with "Next provider check in about 2 minutes" |
| [#5909](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5909) trail sites as numbered circles | In a headless browser at statewide scale the layer drew numbered circles along the trails. Hovering one showed "14 trail sites in this area · 7 NPS-certified · Santa Fe 9 · Oregon 6 · California 7". Selecting it zoomed in and split it (15, 8, 6 and smaller). At zoom 11 near Council Grove, selecting a single site opened its record. No page errors |

The published commit also carries [#5908](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5908) and [#5912](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5912)
from other work. This readback did not check them beyond the identity match.

**What #5906 does not change.** The first DeFlock request after a restart still
waits up to 25 seconds for the provider, because a restart clears the site's
memory of the outage. The layer still shows no cameras: its own rule is that an
unavailable provider leaves it unavailable, with no substitute locations.

**Other feeds.** The other 14 feeds answered 200 in under two seconds. The
National Register feed returned 1,344 points, trail sites 96, trail lines 101
features, and walk-in hunting access 3,591 tracts.

**Chat model.** `/api/ai/status` reported ready on `qwen3.5:9b-q4_K_M`.

**Mirror.** [#5910](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5910) carried #5909 into `apps/site/source`. That tree
has no DeFlock layer, so #5906 has no mirror change.

<a id="public-readback-2026-11-19-later"></a>

### Later publication verified on 2026-11-19: hunting-access overview

At about 20:45 UTC the identity checker reported `APPLICATION_INPUTS_MATCH` for
`c393a352`, the head of the connected branch at that time.

| Change | Live readback |
|---|---|
| [#5924](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5924) walk-in hunting access overview | The tract feed returned 3,591 tracts. In a headless browser at statewide scale the layer drew numbered circles over the tract specks. Hovering one showed "86 walk-in hunting tracts in this area · 46,677 recorded acres · 3 archery-only". Selecting the 364 circle zoomed in one step (scale bar 50 mi to 30 mi). At zoom 8.3 only tract outlines were drawn, and selecting one opened "WIHA tract 44656 · Logan County". No page errors |

**Build identity reads differently.** `/api/build` returned the matching source
digest but `sourceCommit: null` and `commitState: WORKTREE_MODIFIED`. Earlier
readbacks returned the commit and `CLEAN_CHECKOUT`. The application inputs match
`c393a352` exactly, so the difference is in how the host's checkout reports
itself, not in what is served. A clean install, build and start of `c393a352`
in a separate checkout reported `CLEAN_CHECKOUT` with the commit, so no build or
start step dirties the tree by itself. The checker reports `WORKTREE_MODIFIED`
when `git status` on the host is not empty, which an untracked or edited file
anywhere in the host's checkout would cause. Which file was not determined from
outside the host.

**Not checked.** The published commit carries 17 other merged changes since the
previous readback (#5916 to #5947, from other work). This readback covered them
only through the identity match.

**DeFlock after a restart, seen again.** The provider was still down. The first
request took 25.6 seconds and the next 0.6 seconds, as after the earlier publish
the same day; chat showed "connecting" for about 25 seconds at the same moment.
Both point to a freshly started process. [#5906](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5906) removes the wait for
every request after the first failure in a process, but each restart still costs
one visitor up to 25 seconds while the provider is down.

**Other feeds.** The other 14 feeds answered 200 in under two seconds.

**Mirror.** [#5926](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5926) carried #5924 into `apps/site/source`.

<a id="public-readback-2026-11-20"></a>

### Publication verified on 2026-11-20: DeFlock answers promptly on the first check

At about 01:35 UTC on 2026-11-20 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `fd177091`. The connected branch was one merge
ahead at `213e62b7`, which was not yet published.

| Change | Live readback |
|---|---|
| [#5961](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5961) DeFlock returns promptly on the first provider check | The provider was still down. On a freshly started process (chat still showed "connecting"), the first request returned in 0.8 seconds with "Next provider check is running now; try again in about a minute". The second returned in 0.4 seconds. About 40 seconds later a request returned in 0.6 seconds with "Next provider check in about 1 minute" |
| [#5957](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5957) test limit for the network-isolation browser test | Test-only; nothing to read back on the site |

**This supersedes two earlier notes.** The readbacks of
[2026-11-19](#public-readback-2026-11-19) and
[later that day](#public-readback-2026-11-19-later) say the first DeFlock
request after a restart still waits up to 25 seconds. With #5961 it no longer
does: a cold read starts the provider check in the background and answers at
once. The layer still shows no cameras while its provider is down.

**Build identity.** `/api/build` still returned `sourceCommit: null` and
`commitState: WORKTREE_MODIFIED`, as on 2026-11-19. The application inputs match
`fd177091` exactly.

**Other feeds.** The other 14 feeds answered 200 in about two seconds or less.
Chat reported ready on `qwen3.5:9b-q4_K_M` about 40 seconds after the first
request.

<a id="public-readback-2026-11-21"></a>

### Publication verified on 2026-11-21: guide text for the counted circles

At about 05:35 UTC on 2026-11-21 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `804132d1`, the head of the connected branch.

| Change | Live readback |
|---|---|
| [#5975](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5975) guide text for the counted circles | `/explore/historic-places`, `/explore/frontier-trails` and `/explore/hunting-and-wildlife-areas` returned 200 and each carried its new sentence about numbered circles. The historic places page carried the light-ring tip, and the hunting page the "about 3,600" tract count and the reworded last tip. `/explore/kansas-bridges` was unchanged |
| [#5967](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5967) water-quality metadata | From other work; covered only by the identity match |

**Build identity.** `/api/build` still returned `sourceCommit: null` and
`commitState: WORKTREE_MODIFIED`, as on 2026-11-19 and 2026-11-20. The
application inputs match `804132d1` exactly.

**Feeds and chat.** DeFlock returned its outage answer in 0.2 seconds; its
provider was still down. Thirteen of the other 14 feeds answered 200 in under
two seconds and the FEMA declarations feed in 5.9 seconds. Chat reported ready on
`qwen3.5:9b-q4_K_M`.

**Mirror.** [#5976](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5976) carried #5975 into `apps/site/source`.

<a id="public-readback-2026-11-21-later"></a>

### Later publication verified on 2026-11-21: what is in view, and what the host's checkout holds

At about 22:07 UTC on 2026-11-21 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `f08ae04f`, the head of the connected branch,
with 1,386 inputs.

| Change | Live readback |
|---|---|
| [#6010](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6010) what is in this view | A headless browser read the new line in each counted layer's row under Map layers. Statewide: "All 1,344 National Register markers are in this view" and "All 5,580 bridges are in this view". Topeka at zoom 12: "82 of 1,344 National Register markers in this view". Western Kansas: "837 of 3,591 walk-in hunting tracts in this view" with 240,275 recorded acres. An empty view near Bird City read "No trail sites in this view" and "about 120 mi south"; **Go to the nearest** moved the map to "3 of 96 trail sites in this view". On a phone layout the line was visible with no horizontal overflow, the button was 44 px high and worked. No page errors |
| [#6007](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6007) checkout change counts | `/api/build` carried the new field; see below |

**Build identity: the open question is narrowed.** `/api/build` still returned
`sourceCommit: null` and `commitState: WORKTREE_MODIFIED`, and now also:

```json
"worktreeChanges": { "trackedInputs": 0, "trackedOther": 0, "untrackedInputs": 0, "untrackedOther": 1 }
```

The host's checkout holds exactly one new entry (a file or a directory) outside
the application inputs. Git reports no committed file as changed.
The application inputs match `f08ae04f` exactly, so the published code is the
merged code. The field publishes no name; naming the entry needs `git status`
on the host, which this check cannot run.

**Feeds and chat.** DeFlock returned its outage answer in 0.3 seconds; its
provider was still down. The other 14 feeds answered 200, each in under two
seconds. Chat read `KFM home compute (connecting)` just after the publish and
reported ready on `qwen3.5:9b-q4_K_M` about three minutes later.

**Mirror.** [#6011](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6011) carried #6010 into `apps/site/source`.
The build identity script lives only on the connected branch.

<a id="public-readback-2026-11-21-third"></a>

### Third publication verified on 2026-11-21: in-view counts in the status bar

At about 23:49 UTC on 2026-11-21 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `ed9f8b27`, the head of the connected branch,
with 1,386 inputs.

| Change | Live readback |
|---|---|
| [#6013](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6013) in-view counts in the status bar | A headless browser read the status bar. With no counted layer on, the bar was unchanged. With local bridges and National Register places on over Topeka it read "In view: 305 local bridges · 90 Register markers", then 133 and 61 bridges after two zoom-ins. Walk-in hunting access read "In view: 2,611 hunting tracts". The line showed at 900 px wide and was hidden on a phone layout, where the bar's other cells were as before. No horizontal overflow and no page errors |

**Build identity.** Unchanged from the reading earlier the same day:
`WORKTREE_MODIFIED` with `untrackedOther: 1` and zeros elsewhere. The
application inputs match `ed9f8b27` exactly.

**Feeds and chat.** DeFlock returned its outage answer in 0.1 seconds; its
provider was still down. The other 14 feeds answered 200, each in under two
seconds. Chat read `KFM home compute (connecting)` at 23:51 UTC and reported
ready on `qwen3.5:9b-q4_K_M` within the same minute.

**Mirror.** [#6014](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6014) carried #6013 into `apps/site/source`.

<a id="public-readback-2026-11-22"></a>

### Publication verified on 2026-11-22: go to what stands out in view

At about 03:15 UTC on 2026-11-22 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `cf1c5f19`, the head of the connected branch,
with 1,386 inputs. A read at 03:12 UTC still showed the previous build; the new
one appeared at about 03:14 UTC.

| Change | Live readback |
|---|---|
| [#6015](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6015) buttons to the records that stand out | A headless browser pressed the buttons under the in-view line. Local bridges over Topeka offered "Show the oldest (1900)" and "Show the longest (3,376 ft)"; the second moved the map to a view of 3 bridges that still held the 3,376 ft one. National Register places statewide offered "Show one of 9 National Historic Landmarks" and moved to a view with one landmark. Walk-in hunting access offered "Show the largest tract (8,166 acres)" and moved to that tract. On a phone layout state highway bridges offered "Show one of 8 from 1955" and "Show the longest (5,535 ft)", with buttons 44 px high and no horizontal overflow. No page errors |

**Build identity.** Unchanged: `WORKTREE_MODIFIED` with `untrackedOther: 1` and
zeros elsewhere. The application inputs match `cf1c5f19` exactly.

**Feeds.** DeFlock returned its outage answer in 0.4 seconds; its provider was
still down. Twelve other feeds answered 200 in under two seconds. Two did not at
first:

- The county outlines feed returned 503 "This operation was aborted" after about
  18 seconds on five of nine requests between 03:15 and 03:20 UTC, and 200 in
  about 0.6 seconds on the others, including the last three. The Census
  TIGERweb county query it reads hung for 40 seconds on one of three direct
  requests made from outside the host in the same minutes and answered the other
  two in about half a second. The provider was intermittently slow; this publish
  does not touch the feed.
- The FEMA declarations feed, which reads the same county outlines, returned 503
  after 18 seconds once and 200 in one second on the next request.

**Chat.** Ready on `qwen3.5:9b-q4_K_M` at 03:17 UTC.

**Mirror.** [#6017](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6017) carried #6015 into `apps/site/source`.

<a id="public-readback-2026-11-22-later"></a>

### Later publication verified on 2026-11-22: county outlines kept, highlight buttons select

At about 17:26 UTC on 2026-11-22 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `578caf26`, the head of the connected branch,
with 1,386 inputs. At 17:25 UTC `/api/build` briefly answered "Service
Unavailable" while the application restarted.

| Change | Live readback |
|---|---|
| [#6019](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6019) county outlines keep one good Census answer and retry once | Eight requests in a row for the county outlines feed, made within a few seconds shortly after the restart, all returned 200 with 105 counties and the same `retrievedAt` (17:25:58 UTC). The first took 1.2 seconds and the rest 0.2 to 0.6 seconds. The FEMA declarations feed returned 200 twice in under a second. One further county request two minutes later returned 200 in 0.2 seconds. The failure seen after the earlier publish the same day did not recur; whether Census hung during these minutes is not known |
| [#6021](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6021) highlight buttons select the record | A headless browser pressed the buttons under the in-view line. "Show the longest (3,376 ft)" on local bridges opened the details of **Kaw River**. "Show one of 9 National Historic Landmarks" opened **Constitution Hall**. "Show the largest tract (8,166 acres)" opened that tract's record, and keyboard focus moved to the line because the button was gone. On a phone layout "Show the longest (5,535 ft)" opened the bridge's details. No page errors |
| [#6022](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6022) CI job time limit | Workflow file only; nothing to read on the site |

**Build identity.** Unchanged: `WORKTREE_MODIFIED` with `untrackedOther: 1` and
zeros elsewhere. The application inputs match `578caf26` exactly.

**Feeds and chat.** DeFlock returned its outage answer in 0.3 seconds; its
provider was still down. The other 14 feeds answered 200, each in under two
seconds. Chat read `KFM home compute (connecting)` at 17:28 UTC and reported
ready on `qwen3.5:9b-q4_K_M` within the same minute.

**Mirror.** [#6020](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6020) carried #6019 and [#6023](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6023) carried #6021 into
`apps/site/source`. #6022 changes only the connected branch's workflow.

<a id="public-readback-2026-11-22-third"></a>

### Third publication verified on 2026-11-22: kept feed answers, Observatory radar

At about 19:03 UTC on 2026-11-22 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `a4902425`, the head of the connected branch,
with 1,386 inputs.

| Change | Live readback |
|---|---|
| [#6025](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6025) and [#6028](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6028) live feeds keep one good answer for their declared lifetime | Each of the thirteen kept feeds was requested twice, two seconds apart, between 19:04 and 19:07 UTC. Both requests returned 200 with the same `retrievedAt` for every feed; the second took 0.15 to 0.46 seconds. Requested again 30 to 70 seconds later, the earthquakes feed (five-minute lifetime), the National Register feed (a partial answer, kept five minutes) and the walk-in hunting feed (one day) still returned the same `retrievedAt`, while the weather alerts feed (30 seconds) returned a new one. The `Cache-Control` each feed sends is unchanged |
| [#6026](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6026) Event Observatory radar loads again | The `/observatory` response carries `connect-src 'self' https: blob:`. A headless browser loaded the page and waited 15 seconds: radar returns were drawn over Kansas, the page recorded no content security policy violation, showed no alert and received no failed response |

**Not kept by this change, as designed.** The county outlines keep their own
answer (see [the earlier readback](#public-readback-2026-11-22-later)) and the
bridge feeds have their own store; the state and local bridge feeds answered 200
in 6.4 and 3.0 seconds. The congressional districts and DeFlock feeds declare no
lifetime and are not kept.

**Build identity.** Unchanged: `WORKTREE_MODIFIED` with `untrackedOther: 1` and
zeros elsewhere. The application inputs match `a4902425` exactly.

**Feeds and chat.** DeFlock returned its outage answer in 0.3 seconds, twice;
its provider was still down and no failure is kept. The other 14 feeds in the
sweep answered 200, each first request in under 1.5 seconds. Chat read
`KFM home compute (connecting)` at 19:05 UTC and reported ready on
`qwen3.5:9b-q4_K_M` within the same minute.

**Mirror.** [#6027](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6027) carried #6025 and [#6029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6029) carried #6028 into
`apps/site/source`. #6026 changes a file only the connected branch carries.

<a id="public-readback-2026-11-22-fourth"></a>

### Fourth publication verified on 2026-11-22: the Kansas drought series answers again

At about 20:33 UTC on 2026-11-22 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `86ece22f`, the head of the connected branch,
with 1,386 inputs.

**What had been wrong.** A sweep of every public data route earlier the same
day found `/api/drought-series` answering 502 on every request, so the Field
view's "Kansas over time" chart did not appear. The USDM data services had
begun answering `aoi=KS` with an empty list; the same request with the state
FIPS code, `aoi=20`, returned every week.

| Change | Live readback |
|---|---|
| [#6031](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6031) the Kansas series asks by state code and is kept through a failed read | `/api/drought-series` returned 200 with 1,403 weeks, from 2000-01-04 to 2026-11-17, and a `source` naming `aoi=20`. A second request returned the same `retrievedAt` (20:32:53 UTC) in 0.3 seconds. A headless browser opened the Agriculture view with the Drought Monitor on: the page requested the series and received 200, and the week's map drew over Kansas. The dock that holds the chart was not opened in that check, so the chart itself was not seen |

**Still as before this publish.** Four related changes were open and not yet
merged: `/api/event-atlas/radar-frame` still answered `error code: 502`
([#6032](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6032)), `/api/historical-topo` still answered 502
([#6035](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6035)), and `/api/build` did not yet report the kept browser files
([#6033](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6033)).

**Build identity.** Unchanged: `WORKTREE_MODIFIED` with `untrackedOther: 1` and
zeros elsewhere. The application inputs match `86ece22f` exactly.

**Feeds and chat.** DeFlock returned its outage answer in 0.2 seconds. Chat
read `KFM home compute (connecting)` at 20:33 UTC, within a minute of the
restart.

**Mirror.** None needed: `apps/site/source` does not carry the Drought Monitor.

<a id="public-readback-2026-11-22-fifth"></a>

### Fifth publication verified on 2026-11-22: error messages kept, historical maps, kept browser files counted

At about 21:12 UTC on 2026-11-22 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `0bfffe2f`, the head of the connected branch,
with 1,386 inputs.

| Change | Live readback |
|---|---|
| [#6032](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6032) a public read that ends in 502 or 504 leaves as 503 with its body | `/api/event-atlas/radar-frame` with no frame named returned `503`, `x-kfm-upstream-status: 502`, `content-type: application/json` and the route's own sentence, "The exact historical radar frame is unavailable. No latest-image fallback was used." Before this publish the same request returned the proxy's text, `error code: 502` |
| [#6033](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6033) the build records the kept browser files it started with | `/api/build` carries `retainedClientAssets`: **970 entries and 38,848,175 bytes (37 MB)**, against limits of 4,096 entries and 256 MB. That is 24% of the entry limit and 15% of the byte limit, measured before this build added its own files |
| [#6034](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6034) one read per Drought Monitor week, two weeks at a time | `/api/drought-monitor?date=20120807` returned 200 in 1.2 seconds and `/api/drought-series` 200. The waiting line and the refusal past it were not exercised against the public site; they are covered by the unit test |
| [#6035](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6035) historical map catalog address; empty outlook times | `/api/historical-topo?lng=-95.69&lat=39.05` returned 200, `available`, with 24 sheets in 0.9 seconds (it returned 502 before). `/api/spc-outlook?day=1&product=torn` returned no risk areas with `issuedAt` 19:47 UTC and a valid period of 20:00 UTC to 12:00 UTC the next day (all three were null before) |

**Kept browser files: what the number means.** The count is the first real
reading of the host's folder. The estimate made from outside earlier the same
day was "at least 845 entries and 34 MB". At the growth seen in development
builds (about 26 entries a publish) the entry limit is on the order of a
hundred publishes away. The next publish's reading will give the host's own
growth per publish. Nothing is pruned yet; that decision is open.

**Build identity.** Otherwise unchanged: `WORKTREE_MODIFIED` with
`untrackedOther: 1` and zeros elsewhere. The application inputs match
`0bfffe2f` exactly.

**Chat.** Read `KFM home compute (connecting)` at 21:12 UTC, shortly after the
restart.

**Mirror.** The historical map catalog address is carried into
`apps/site/source` by the same change that adds this section. #6032, #6033,
#6034 and the outlook part of #6035 touch files only the connected branch
carries.

<a id="public-readback-2026-11-23"></a>

### Publication verified on 2026-11-23: county pages and a complete sitemap

At about 01:57 UTC on 2026-11-23 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `f3a44dca`, the head of the connected branch.
That head also carries three changes merged by other work the same hour
(#6043, #6045, #6046); this section reads back only the county pages.

| Change | Live readback |
|---|---|
| [#6044](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6044) a page for each of the 105 Kansas counties | `/counties` returned 200 with its canonical address. `/counties/sedgwick`, `/counties/allen` and `/counties/wyandotte` returned 200, each with its own title, canonical address and figures (median household income $69,365 ±$1,409, $60,689 ±$4,364 and $63,631 ±$1,779). `/counties/nowhere` returned 404. The guides index links to `/counties` |
| [#6044](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6044) sitemap | `/sitemap.xml` lists 129 addresses, 105 of them county pages (it listed 9 before) |

Not repeated on the public site: the browser checks made on the built
application before merging (no accessibility violations at desktop and phone
widths; the "Open the map" button landing on the county with outlines on).

**Kept browser files: second reading.** `/api/build` again reports 970 entries
and 38,848,175 bytes, exactly the figures of the
[previous publish](#public-readback-2026-11-22-fifth). The folder the build
starts with did not grow between these two publishes, although a script file
from an earlier build was still served by the origin (not from the CDN's cache).
So the growth of about 26 entries a publish seen in a development checkout is
not what the host shows, and the earlier "about a hundred publishes" estimate
should not be relied on. Why the host's starting folder is unchanged is not
known from outside; a third reading will show whether it is fixed.

**Build identity.** Otherwise unchanged: `WORKTREE_MODIFIED` with
`untrackedOther: 1` and zeros elsewhere.

**Mirror.** None: `apps/site/source` carries neither the county bundle nor the
sitemap module.

<a id="public-readback-2026-11-23-later"></a>

### Later publications verified on 2026-11-23: county population and bridges; a clean host checkout

At about 05:20 UTC on 2026-11-23 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `1bb85d15`, the head of the connected branch,
with 1,393 inputs. That head also carries two county-page changes merged by
other work (#6048, #6050); this section reads back #6049 and the build record.

| Change | Live readback |
|---|---|
| [#6049](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6049) county population and bridges | `/counties/allen` reads "The Census Bureau estimates that 12,302 people lived in Allen County on July 1, 2025. That is 231 fewer than its estimate of 12,533 for July 1, 2020" and "bridge inventory lists 226 bridge records in Allen County: 43 on state highways and 183 on local roads. The oldest recorded built year is 1910. The longest structure is 1,204 feet", with "Inventory as of 2026-11-16". `/counties/greeley` carries the link that opens the map with both bridge layers on |

**The host's checkout was clean for the first time on record.** `/api/build`
reports `commitState: CLEAN_CHECKOUT` with `sourceCommit` set to `1bb85d15`,
no `worktreeChanges` and no `retainedClientAssets`. Every earlier reading in
this runbook was `WORKTREE_MODIFIED` with one untracked entry outside the
inputs. So this build started from a fresh checkout whose `public/assets` was
absent or empty.

**Kept browser files: what three readings and this one show.**

| Publish | Entries | Bytes |
|---|---|---|
| `0bfffe2f` (2026-11-22, about 21:12 UTC) | 970 | 38,848,175 |
| `f3a44dca` (2026-11-23, about 01:57 UTC) | 970 | 38,848,175 |
| one publish between 03:25 and 05:20 UTC, digest `sha256:c346bcc8…` | 1,107 | 45,176,966 |
| `1bb85d15` (2026-11-23, about 05:20 UTC) | none reported | clean checkout |

- The folder a build starts with does grow on the host (137 entries in one
  step), but not at every publish, and it was reset when the checkout was
  replaced.
- Script files from earlier builds were still served by the origin after the
  clean build (60 of 60 older files tried). So the files visitors' open pages
  need are kept somewhere other than the build's own folder.
- The limit of 4,096 entries applies to the build's folder. While the host
  replaces its checkout from time to time, that folder starts again from
  nothing. How often that happens is not known from outside, so the limit
  remains worth watching on `/api/build` rather than a settled question.

**Mirror.** None: `apps/site/source` does not carry the county bundles.

<a id="public-readback-2026-11-23-third"></a>

### Third publication verified on 2026-11-23: Kansas records

At about 05:52 UTC on 2026-11-23 the identity checker reported
`APPLICATION_INPUTS_MATCH` for `9c8e5447`, the head of the connected branch.

| Change | Live readback |
|---|---|
| [#6054](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6054) Kansas records | `/records` returned 200 with the title "Kansas records · Kansas Frontier Matrix", its canonical address and 22 entries in four groups, from "Most people: 636,906" to "Rated F5 or EF5: 6 tornadoes". Each group carries its source line, and the tornado deaths entry carries the note that deaths are for the whole track. `/sitemap.xml` lists 130 addresses, `/records` among them. `/counties` and `/explore` each link to it |

Not repeated on the public site: the browser accessibility checks made on the
built application before merging.

**Build record.** The checkout was no longer clean: `WORKTREE_MODIFIED` with
`untrackedOther: 1` again, one publish after the
[clean checkout](#public-readback-2026-11-23-later). The build started with
**333 kept entries and 10,826,486 bytes**. That is what the single clean build
before it staged, so one whole build is about 333 entries; later builds add
only the files that changed. Against the 4,096-entry limit that leaves room
for the folder to grow for a long time between resets.

**Mirror.** None: `apps/site/source` does not carry these bundles.

<a id="verified-starting-point-2026-10-19"></a>

<a id="public-record-lab-2026-11-19"></a>

### Public acceptance on 2026-11-19: connected records and portable investigations

Fresh Chrome reads of the canonical public application matched a clean standalone
checkout of [`b2f20e0171875795a28f85134a90b65e14c5cd17`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/b2f20e0171875795a28f85134a90b65e14c5cd17).
The application was already serving those inputs during preparation; this check
did not perform a dashboard Publish or inspect hosting settings. The earlier
independently observed public source `9d472887` was retained as source-only
rollback material, not asserted to be the provider's current rollback selection.

| Check | Observed result and limit |
|---|---|
| Public identity | [`/api/build`](https://kansasfrontiermatrix.com/api/build) reported app `urdng3v1vk`, 1,353 application inputs and digest `sha256:719caeab9b6d64c422bf92056dee41d8d193e9316ad62cc5f9b7ad9e4f72326e`, matching the clean checkout |
| Git stamp | Published `sourceCommit` was null and `commitState` was `WORKTREE_MODIFIED`. Input parity was verified; a clean deployment checkout was not claimed |
| Local release checks | Production build, type check and full suite passed: 3,143 tests, 25 existing skips, zero failures |
| [Record Lab](https://kansasfrontiermatrix.com/data-lab?collection=observations-usgs-daily-values) | All 135 documented FAA/USGS fields were available across six collections. Three live water investigations preserved 1,250 distinct sampled records / 2,000 record instances through linked metadata, JSON/story exports and reopening; desktop/phone layout passed |
| Metadata interpretation | Station and daily/peak series samples retain exact provider keys, repeated captures, units, datums, time fields and missing matches. These bounded links neither select a current metadata version nor establish a temporal or archive-wide join |
| [County Observatory](https://kansasfrontiermatrix.com/labs/observatory) | County histories, peer selection and both evidence CSV exports worked. Changing the comparison county retained the anchor county |
| [Science notebook](https://kansasfrontiermatrix.com/labs/notebook) | A clearly named, browser-local QA investigation saved, exported, imported and reopened the same counties/settings with four source fingerprints. The QA entry was removed; no user notebook was overwritten |
| [2012 drought replay](https://kansasfrontiermatrix.com/labs/drought-replay) | First/last assessment controls and source JSON download worked; the export retained 17 weekly assessments and 119 daily readings |
| Existing map | The normal Welcome → Explore freely path completed renderer startup, showed the toolbar and map canvas, and produced no browser errors |
| Public boundaries | Anonymous `/admin` returned 404; the retired report-pricing endpoint returned 404 on POST. Free exports remained available |
| Home AI | Public [`/api/ai/status`](https://kansasfrontiermatrix.com/api/ai/status) returned configured/online/ready via `home-ollama`, labeled `qwen3.5:9b-q4_K_M`. This was readiness verification, not factual-answer qualification |

All native intake/data gateway/data worker/Ollama services remained active. No
hosting, signing-key, database, model or original Sites audience/storage setting
was changed by this verification. The notebook test used an isolated browser
context; raw source replies and screenshots stayed in task-local recovery.

Operational details: command-line requests received Cloudflare 1010 while Chrome
could read the public endpoints. The map's live background requests and Welcome
screen also made generic network-idle waiting unsuitable: acceptance used the
visible entry control and completed renderer state. Preserve these distinctions
when repeating checks rather than declaring an outage or bypassing a gate.

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

Since [#6007](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/6007), a build whose `git status` is not empty also
reports `worktreeChanges`: four counts of the entries Git sees as changed
(tracked or untracked, inside or outside the application inputs) and no names.
On 2026-11-21 the hosted build reported one untracked entry outside the inputs
and nothing else ([readback](#public-readback-2026-11-21-later)). The digest
comparison, not this field, is what binds the application inputs.

## Preview, publication and acceptance

1. In the dashboard, confirm the app ID (`urdng3v1vk`), its source branch
   (`a0-hosted-ai-web-20261017` in the dated 2026-10-20 readback; public
   `/api/build` matched that branch's head on [2026-11-13](#public-readback-2026-11-13)) and the Published commit.
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
