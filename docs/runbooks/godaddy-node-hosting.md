<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/godaddy-node-hosting
title: KFM GoDaddy Node application operation and source alignment
type: runbook
version: v2
status: source-grounded operation guide; earlier deployment observations retained as dated history
owners: ["@bartytime4life"]
created: 2026-10-17
updated: 2026-11-19
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
