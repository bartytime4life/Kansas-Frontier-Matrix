<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/site/atlas-studio-blueprint-20261018
title: Atlas Studio campaign blueprint and Prairie Field Desk foundation
type: implementation-blueprint
version: v0.2
status: selected Prairie Field Desk; A1 source implemented and locally validated; rendered acceptance and human review pending
owning_root: docs/
responsibility: Explain one coordinated product campaign, its existing boundaries, dependency order, acceptance and rollback.
truth_posture: CONFIRMED pinned source inspection; PROPOSED product and architecture targets; NEEDS VERIFICATION runtime and milestone acceptance.
[/KFM_META_BLOCK_V2] -->

# Atlas Studio: investigation, chat, evidence and time

Task `KFM-20261018-ATLAS-01`. Recorded for the October 18, 2026 America/Chicago
campaign. This blueprint explains proposed application work and its evidence
boundary. It creates no contract, source registry, corpus admission or release
authority. The owner merged the A0 request-isolation foundation in PR #5275.
The user selected concept **1, Prairie Field Desk**. A1 implements its bounded
workspace foundation below; the entire campaign and Milestone A are not complete.

## Visitor outcome and acceptance scope

**PROPOSED campaign:** interest → Kansas county/place → unified question/search
→ useful layers → supported dates → inspectable evidence → attributed export.
The map remains a first-class workspace. Chat, discovery, evidence, selection
and time share one visible investigation scope. Each milestone must produce
working behavior over eligible existing data before increasing coverage.

**Historical A0 boundary:** prevent responses and actions belonging to an earlier
investigation generation from changing a newer one. An A → B → A navigation
must receive a fresh generation even when the final context has the same values
as the first A. Preserve useful drafts, truthful cancellation, source-rechecked
exports and existing public/admin boundaries. A0 does not implement the visual
redesign or assert that all campaign acceptance has been completed.

## Historical A0 starting point

| Surface | Status and evidence |
| --- | --- |
| Hosted source | **CONFIRMED:** `a0-hosted-ai-web-20261017@508db6073f3602e461c7b9bd33ced648417c37d8`; tree `7790aa8711faa3513b92fc3ad6cba2b6f60359af`. |
| Governing repository snapshot | **CONFIRMED:** default `main@ca54cf54653731e133d8ef9c2234531054bbdfc7`; separate monorepo responsibility and application layout. |
| Hosting destination | **CONFIRMED source configuration:** root `AGENTS.md` identifies the separate GoDaddy Node composition and app `q9r9beo47t`; original Sites preservation, audience and bindings remain separate. |
| Deployed revision | **UNKNOWN:** matching screens, model labels, merges and repository checks do not identify the currently served production or preview commit. |
| Current browser observation | **CONFIRMED bounded baseline:** the observed preview has separate global search and chat, Evidence/Chat views in one drawer, visible answer preferences and repeated anonymous-access wording. Ellsworth scope distinguishes map display year 2026 from Census 2020 context. The Qwen3 0.6B ready label is interface state, not inference or quality qualification. |
| Mobile acceptance | **NEEDS VERIFICATION:** a viewport override changed accessibility state, but the capture scaled the physical desktop screen. That does not establish phone or virtual-keyboard acceptance. |
| Local candidate browser | **CONFIRMED environment limit:** the task's loopback listener probe at `127.0.0.1` / port 0 returned `EPERM`. No local candidate server or rendered acceptance is claimed, and no permission/network workaround was attempted. |
| Hosting connector | **CONFIRMED capability gap:** the available GoDaddy tools provide domain availability/suggestions, not hosting or deployed-source readback. |
| Prior search work | **CONFIRMED GitHub history:** #5264 supplies truthful pending/current-query county search; #5265 repairs clean development identity/navigation; #5269 adds hydrated controlled-response browser coverage; all are in the pinned hosted source. |
| Overlap at orientation | **CONFIRMED bounded query:** open #5274 concerns main historical-topo tooling. No open hosted application overlap was returned. Recheck before publishing a candidate. |

The task checkout reproduces the exact remote signed source commit and complete
tree. It is a shallow authoring checkout; existing developer worktrees and
synced reference files are preserved. Node 22.13.1 and existing locked
dependencies are available. The listener restriction above was measured in
this task rather than inferred from a previous failure.

## Existing seams to extend

**CONFIRMED from the pinned source:**

- `app/assistant-context.ts` defines the version-1 context with frame, view,
  layers, selection, page surface, filters and comparison. Snapshot-derived
  browser-location details already have a withholding path.
- `app/assistant/workspace.tsx` owns the public conversation, job status,
  retries/cancellation and source-rechecked investigation actions.
- `app/api/ai/[...path]/route.ts` composes the existing server-owned context
  resolver and evidence reader with the public job handler. Origin, guest,
  queue, source eligibility and expiry remain server responsibilities.
- `app/knowledge-read.ts` reads `/api/governed/v1/knowledge` and validates
  released envelopes, release identity, record identity and a 20-record search
  bound. Its server implementation uses established store/bucket interfaces.
  A valid hosted storage binding and actual eligible corpus are **UNKNOWN**
  until inspected; source existence does not establish runtime availability.
- Existing county search uses the loaded Census response as labelled external
  context. Existing job exports recheck sources. Reuse both boundaries.
- `docs/scene-studio.md` describes the existing light/camera workspace; its
  responsibilities remain intact as the wider investigation experience evolves.

## Proposed experience and component behavior

Three visual concepts have been presented: **1 Prairie Field Desk**, **2 Atlas
Canvas**, and **3 Investigation Notebook**. **CONFIRMED: the user selected 1,
Prairie Field Desk.** All
generated maps, labels, text and numbers in those concepts are illustrative
mockup content, not geographical or scientific evidence. Runtime maps, charts
and source cards must use permitted real data and accurate tools.

The selected concept provides the direction for one reachable multiline composer for
discovery, questions and supported map actions; a readable conversation; a
compact county/layer/time scope; and evidence summaries with intentional deeper
inspection. Move advanced preferences and diagnostics into compact tools.
Preserve administrator access while reducing repeated anonymous-access copy.
The shared proposed composition is a map-dominant desktop with a resizable
360–440 CSS-pixel chat dock; on phones, one active Map or Ask surface with
intentional Evidence and Time sheets. Widths and responsive transitions remain
design targets to test, not measured current behavior.
Remove the separate header search only after unified discovery demonstrates
parity for existing places, layers, records and source results. Preserve routes
to reports, stories, layers, map views and exports, using compact overflow where
appropriate rather than dropping existing functions.

Enter sends and Shift+Enter inserts a newline where appropriate for the tested
input method. Stop, Retry, copy, source-rechecked save/export, New investigation
and Jump to latest have explicit behavior. Respect an upward-scrolling reader.
Conversation history and recent investigations must state their actual
retention, persistence, privacy and deletion behavior before promising storage.

Search remains directly usable when inference is unavailable. Distinguish
places, layers, records, source-context results, supported answers and generated
discussion. A city/county ambiguity requires explicit choices. Validated
reversible map actions show their affected scope; unsupported actions fail
with useful guidance. No model output can select arbitrary URLs or execute code.

Use request events actually exposed by the implementation. The existing
`preparing`, `queued` and `running` job states must not be presented as token
streaming, invented search
stages, percentages or hidden reasoning. A future streaming contract must apply
eligibility checks before disclosure and distinguish partial from finalized
content. Display only sanitized counts, sources and timestamps actually known.

Compact evidence preserves access to source/record identity, EvidenceRef →
EvidenceBundle where applicable, time kinds, scale, rights, sensitivity,
release/trust state, limits and lineage. Desktop inspection may collapse or
resize; phone inspection should provide compact peek, expanded and full-screen
states through the selected tested sheet pattern. A claim's citation resolves
the record and source version bound to that claim, rather than opening the
latest global map selection. Open full evidence intentionally, without
automatically expanding it for every reply. Restore focus to the invoking
citation/control and preserve camera, layers, time and conversation.
Avoid nested scrolling traps and keep the composer reachable with the keyboard.

Maintain a restrained navy/teal/wheat identity with readable legends, scale,
attribution and uncertainty. Trust uses words and symbols as well as color.
Verify reduced motion, visible keyboard focus, contrast, text reflow, touch
targets, safe areas and virtual-keyboard reachability; pause unnecessary
background effects. Compare useful-feedback time, composer response, scrolling,
map interaction, layout shifts, memory, network bytes and frame cost using an
explicit revision, device/emulation, cache state, dataset, scenario, repetitions
and method. Choose budgets from measurements; pure helper CPU timings do not
establish phone latency or acceptance.

## Proposed retrieval and corpus boundary

Inventory actual hosted stores, adapters, eligible records, geography, dates,
rights, update cadence and gaps before expanding. Corpus size means measured
retrievable coverage. Metadata-only discovery must remain distinguishable from
available record content. The model is a retrieval client and interpreter.

Adapt the existing server contracts for bounded discovery, evidence resolution,
coverage planning, supported map actions/frame reads and attributed draft
creation. The logical tool names and envelopes remain **PROPOSED**, not adopted
parallel contracts. Request validation must bind identifiers, permissions,
pagination, scope, time, context generation and explicit result/byte budgets.
The server resolves identity and authorization; Qwen receives no SQL access,
credentials, unrestricted URLs, internal-store access or code execution.

Start with deterministic lexical/place retrieval. Introduce semantic retrieval
only after relevance and resource evaluation. Indexes and embeddings are
rebuildable derivatives. Admit collections incrementally with provenance,
validation, rights/sensitivity, correction and withdrawal handling. Keep
released evidence, permitted external context and interpretation separate.
Do not import unbounded collections, activate a new service or add a paid tier
to make a prototype appear complete. Retrieval and inference stay hosted and
must not depend on the owner's workstation.

Partition caches by authorization, source/release, scope, time, resolution and
transformation. Revalidate controlled reads, saved investigations and new
exports after restriction or withdrawal; previously downloaded text/files
cannot be recalled. Minimize location and conversation data in logs. Separate
bounded retrieval and inference queues so a model outage does not block search.

## Proposed county time plan

County → active layers → period → coverage preview → play. Account for every
selected layer as eligible, held, incompatible, missing or unavailable. A
county clip does not imply a county average or redefine Tribal jurisdiction.
Keep a compact county/time strip with Play/Pause, previous/next supported
frame, speed and range. Expand it into layer tracks, available dates, gaps,
timezone and coverage. Auto-loading an eligible historical frame does not
start playback; Play remains an intentional visitor action.

| Clock or control | Required meaning |
| --- | --- |
| Source clock | Actual observation/valid interval, forecast issue/run, edition, publication and retrieval as applicable; preserve precision and timezone. |
| Map clock | The investigation's visible instant or interval, with explicit pin/Auto-fit state. |
| Playback clock | Wall time over which the visitor watches the plan; hours/day per second or a desired duration in seconds through hours. |
| Data step | Source-supported frame selection or declared sampling, independent of playback speed. |

Auto-fit applies only to a new unpinned investigation and must announce the
chosen range/frame. A pinned time stays fixed and offers an explicit fit action.
Static edition years do not constrain dynamic observations. A missing shared
period produces a coverage conflict and useful choices; do not silently remove
layers. Distinguish shared-date playback from plans with per-layer gaps.

Plan actual source timestamps and valid intervals, retaining irregular cadence,
date-only precision, daylight-saving semantics, forecast identity and staleness
limits. No universal source cadence or invisible gap fill. Carry-forward,
aggregation and interpolation need a validated source-specific method and
visible provenance. Geological/BCE uncertainty requires an appropriate scale
instead of forced operational timestamps.

Preview frame/read/byte/provider/cache/prefetch costs before fetching. Calibrate
budgets from measured host/device capacity and offer explicit narrowing or
sampling when necessary. Do not fetch on every animation tick. Version the
plan and pin source/release identities where supported; cancel/supersede old
plans when county/layers/time/selection changes. Save permitted scope, time
semantics, transformations and source versions for an attributed replay.

## Proposed welcome and mission coverage

Offer a dismissible, reopenable welcome with Explore freely, county/place and
useful example missions. Organize by goal, optional audience and topic. Extend
existing profile/catalog mechanisms after inventory; stable IDs describe views,
not permissions or claims of coverage. Every mission names eligible layers,
available geography/dates, source limits and an optional walkthrough.

Visible interests include farming/agriculture; science/research; government
officials/workers; learning/education/entertainment/creative exploration;
business/local opportunity; weather/climate/water; history/archaeology;
hunting/wildlife; roads/rail/air traffic; Tribal nations/reservations/Indigenous
history; public utilities/projects; fauna/flora/natural resources; demos; news;
and money/public budgets/grants/economic context. Mark unsupported missions
PROPOSED or unavailable rather than implying data exists.

Use appropriate Tribal/cultural authority and rights-cleared sources. Protect
sensitive archaeology, species, private land/hunting and infrastructure details.
Preserve source dates and aviation/weather/news delays, economic limitations,
free reports/downloads, and unmistakable synthetic/demo labels.

## Dependency-ordered delivery

| Milestone | Useful deliverable | Dependency and acceptance |
| --- | --- | --- |
| A0 — merged foundation | Generation-bound async conversation actions using existing contracts. | Owner-merged PR #5275; historical local checks below. |
| A1 — current source milestone | Prairie Field Desk composer, deterministic Find, compact evidence summaries, welcome discussion starters and server history isolation. | Selected concept 1; source checks below pass. Rendered phone and hydrated candidate acceptance remain open. |
| A2 — complete selected workspace | Tested mobile/evidence composition and truthful conversation management over verified existing data. | Build on A1; validate phone topic/county → permitted result → evidence → return, keyboard/scroll, persistence/privacy and source-rechecked export. |
| B — county Time Sweep | Coverage planner and working player over demonstrably compatible layers. | Source-clock adapters and budget measurements; account for all active layers, actual dates/gaps, pinned/Auto-fit behavior, rapid-context cancellation and attributed replay. |
| C — measured corpus and retrieval quality | Incremental eligible collection growth and evaluated lexical/semantic/tool use. | Verified hosted stores/capacity and admission; measure relevance, temporal understanding, citation faithfulness, withdrawal, outage fallback and resource cost. |

Each PR is dependency-closed and reversible. Re-read target/overlap before
publication, run proportionate changed-area checks, and distinguish inherited,
introduced and environmental failures. Visual selection is resolved. Later
milestones must stay explicitly held until their
actual dependencies are satisfied; a blueprint does not complete them.

## Historical A0 ownership, validation and rollback

The Master Coder owns lifecycle changes in the existing conversation workspace
and focused request/status tests. The Lead Developer owns this blueprint,
bounded behavior documentation, receipt and integration. The Creative Lead owns
product acceptance; the Design Artist owns concepts and responsive direction;
the non-author Performance Reviewer owns independent measurement and review.
Assign shared files before edits and serialize integration.

Acceptance must include late request acceptance, late polling/error/cleanup,
same-value A → B → A scope transitions, Stop/cancellation and unmount.
Only an owning generation can publish conversation state or clear another
request's busy state. Best-effort cancellation of a late accepted opaque job
must not restore obsolete content or claim server cancellation before an
acknowledgement. Existing server deadlines remain the resource bound when
acceptance/cancellation cannot be confirmed. Preserve the current draft.

**CONFIRMED A0 source behavior:** each submitted question owns a request and a
monotonic scope generation. Changes in context, account actor or pending-work panel activity,
Stop and unmount invalidate ownership. A late observable accepted ID receives
a best-effort cancellation request; its reply cannot return to the newer UI.
Polling, source rechecks and export completion cannot revive obsolete state or
unlock a newer request. Continue is generation-bound as well as context-bound.
A pure hide/reopen cycle preserves a completed compatible turn's Continue;
closing live pending work still cancels/supersedes it. Context/actor changes,
including A → B → A, do not revive an earlier continuation.
The existing styled action now offers Stop during admission and accepted work,
with separate pending, confirmed and unconfirmed cancellation wording. The
admission transport is retained to observe a late opaque ID; if the network
never returns one, remote cancellation remains unconfirmed and existing server
deadlines apply. No server or model resource limit is changed.

A non-author review reproduced adjacent draft loss: a visitor's newer text was
cleared when an earlier POST was accepted. The minimal correction captures the
verbatim submitted draft and clears it only when the current text is unchanged.
Its dedicated regression failed on the pre-correction A0 snapshot (25 passed,
one failed), then passed with the correction. The original pinned source has
the same unconditional clear, but that dedicated regression was not separately
run against the original source. The final status suite passes 27/27, compared
with 17/17 baseline cases; the initial three lifecycle regressions failed on the
unchanged pinned application before the ownership repair. These are controlled
component/hook tests, not rendered browser or real inference acceptance.
A separate non-author check caught an introduced hide/reopen continuation
regression in the first repair. Its dedicated 27th case failed before the
semantic-generation correction and now passes; the matched original baseline
kept the compatible continuation enabled. Both review findings are resolved.

| Final A0 check | Observed result and limit |
| --- | --- |
| Focused component suites | **PASS 52/52:** status 27, sitewide 11, investigation 6, composer 8. Existing controls/source boundaries remain covered. |
| Independent status rerun | **PASS 27/27** on the final corrected source; agent review reports no source blockers. Final committed SHA review remains separate. |
| Production build | **PASS** after the draft-preservation and hide/reopen corrections; inherited Vinext static-classification notice retained. |
| TypeScript | **PASS** `--noEmit --incremental false` after the final source correction. |
| Changed source/test lint | **PASS**, zero errors/warnings. |
| Whitespace and blueprint local links | **PASS**; four relative document links resolve. |
| Matched late-admission fixture | Baseline: one status, one POST, one result GET, no cancellation, obsolete reply/draft loss. Candidate: one status, one POST, zero result GET, one cancellation, suppressed reply/preserved draft. Other requests zero on both. This is a controlled request-count comparison, not browser latency or host capacity. |
| Candidate browser/mobile/WebGL | **NEEDS VERIFICATION** because the local listener probe was denied; observed live baseline is not candidate acceptance. |
| Exact-head CI and human review | Pending at this record's authoring; later PR/check evidence must identify its actual covered revision. |

Record actual commands/results, reviewed SHA, browser limitations, exact-head
CI and any unverified cases with the delivered PR. Source/helper checks are
not browser, virtual-keyboard, inference-quality or deployment acceptance.
Measure changed work under comparable conditions and avoid latency claims from
pure helper or component-harness timings.

Revert the bounded A0 source/tests/docs/receipt change through normal review to
restore prior lifecycle behavior. Preserve newer work, historical receipts,
stores, account/model settings and immutable assets. No corpus migration,
source activation, model replacement, audience/DNS/hosting change, merge,
deployment, promotion or public release is performed by this authoring task.

## A1: selected Prairie Field Desk workspace

**Task and target:** `KFM-20261018-ATLAS-01`, Creative Lead coordinating the same
five-role team. Base `a0-hosted-ai-web-20261017` at
`5f8a790d58761e416592d1597db7d870cc008eaf`, tree
`d8594b1ec2189dfb655f33a621d5663f17cb122d`. This is the owner-merged A0
[PR #5275](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5275),
not evidence of deployment. The final PR records its exact resulting head and
reviewed revision; neither a commit nor a draft PR changes publication state.

**Visitor need / before → after:** the baseline has a separate top search,
permanently visible preference controls and a large shared inspector. A visitor
can now open **Find & ask**, use one multiline composer for explicit **Find**,
**Ask** or **Evidence**, choose a county or other available result, and inspect
compact source summaries without automatically expanding the full inspector.
The header shows place, map time and active layer count. Existing maps, layers,
reports, stories, administration and free exports retain their owners.

**Bounded implementation, CONFIRMED by source and controlled checks:**

- Prairie Field Desk uses navy/teal/wheat, restrained depth, a readable thread,
  closed preferences, visible intent buttons, reduced-motion rules and a pinned
  composer. Generated concept maps/numbers were not imported into application data.
- Find projects the existing local index, eligible loaded Census county response
  and source catalog through `atlas-discovery.ts`. It has no inference dependency,
  new provider fetch, corpus admission or database. Only current settled-query
  results are actionable. ArrowDown moves from the composer to an explicit result;
  Enter never guesses a county from an ambiguous city name. `/` opens Find.
- Ask remains unverified discussion; Evidence uses the existing released-evidence
  path. They are explicit modes, not a new automatic tool-routing model contract.
  Source context, released records and generated interpretation stay distinguishable.
- New investigation clears the visible tab thread and rotates the validated
  UUIDv4 history partition. Compatible follow-ups share that partition only within
  the existing guest session and server-derived context/source fingerprint. A
  context/actor change, A → B → A, Stop or closing pending work rotates it; an
  unseen completed reply cannot contaminate the next request even if cancellation
  is too late. A completed compatible hide/reopen preserves its partition. Legacy
  callers omitting the ID keep existing behavior; no permission or resource cap changes.
- Progress reflects existing preparing/queued/running/terminal events. There is no
  invented token streaming, percent complete or reasoning trace. Stop is best-effort
  server cancellation plus local supersession; unconfirmed cancellation is labelled.
- Per-turn source disclosures retain captured citations and recheck server sources
  before inspection/export. Rich map inspection is available only when the submitted
  context still matches the current inspectable selection. An old claim never changes
  the current camera, layers, selection or time. Closing the inspector returns to chat
  and the invoking control or composer. The existing single foreground panel owner is
  retained; simultaneous independent desktop chat/evidence panels are not implemented.
- The welcome groups 22 interests using stable IDs in the existing starter module.
  Topic cards prepare labelled **discussion drafts** only; they do not claim indexed
  coverage, retrieve records, add layers or send AI requests. The primary Find action
  actually opens deterministic discovery. Find/Evidence are identified as the paths
  for checking available data. Existing recipe controls remain in Layers.
- Chat history is in this tab; temporary server question expiry remains 15 minutes.
  Copy/download produces an attributed draft with rechecked permitted sources.
  No durable recent-conversation archive or persistence promise was introduced.

**Ownership:** Design Artist authored the visual/starter specifications and code;
Master Coder authored the composer and status coverage; Lead Developer delegated
the existing discovery extraction and server history isolation. After repeated
agent capacity failures, Creative Lead explicitly assumed remaining integration,
tests, documentation and PR preparation. Shared-file ownership was serialized.
The non-author Performance Reviewer reproduced the Stop/history flaw, reviewed the
correction and independently reran 102 focused cases. Agent review is not human
approval. The exact final-head review is recorded in the PR after commit.

### A1 validation and measured limits

All local results below cover the final application source. Later documentation
and receipt edits do not change application source/build inputs. Commands run
from the A1 checkout with Node 22.13.1 and existing locked dependencies.

| Check | Actual result and boundary |
| --- | --- |
| Fourteen focused suites, each `node tests/<suite>.test.mjs` | **PASS 149/149:** assistant-status 37, chat-composer-reach 8, map-starters 12, atlas-discovery 7, global-search-status 9, public-ai 29, assistant-investigation 6, county-search 4, assistant-sitewide 11, inspection-panel 4, modal-background 3, workspace-map-navigation 9, workspace-help-navigation 8, mobile-compatibility 2. Controlled component/server/static checks, not a rendered phone claim. |
| Independent reviewer subset | **PASS 102/102:** status, discovery, global search, starters, composer and public-ai suites on final application source. No remaining blocking source findings reported. |
| Stop/history reproduction | New 37th test fails before the fix (36 pass/1 fail), then passes after UUID rotation for Stop and pending-panel hide when cancellation returns `cancelled:false`. The non-author reproduced ID reuse independently. |
| `npm run build` | **PASS**, final runtime digest `a589fec1846921395afc23a5664b88f7c565e499674ce3a0ad6fffefaffa4a6a`, 777 source inputs. Existing Vinext route-classification notice remains. |
| `tsc --noEmit --incremental false` | **PASS** after final application build. |
| Changed-source/test ESLint | **0 errors / 40 warnings**, versus 0/40 on matching base files. 39 warning identities unchanged; one prior missing-dependency warning becomes an unnecessary-dependency warning on the modified close callback. No clean-lint claim. |
| `git diff --check` | **PASS**. |
| Compiled asset inventory | Manifest-selected unique JS/CSS assets: 49 on both base/candidate. Raw 1,929,439 → 1,961,226 bytes; per-file gzip9/mtime0 593,860 → 601,450 (+7,590, +1.28%). Assistant JS gzip 12,210 → 14,214; assistant CSS 1,586 → 3,059; associated page CSS 6,549 → 7,959. Package/lock/build-config hashes match. Unreferenced retained staged assets excluded. This is compiled inventory, not initial transfer, phone latency, FPS or host capacity. |
| Hydrated browser fixture | Adapted existing county-search CI fixture to open Find, use the composer, ArrowDown to an explicit result, and return focus after Evidence. **Not run locally**: loopback listener denied. CI must report its actual covered revision. |
| Phone/keyboard/accessibility/performance | **NEEDS VERIFICATION:** real virtual keyboard, touch, rendered overflow/contrast, focus behavior with assistive technology, scrolling, WebGL, frame cost and network/latency. Structural CSS/DOM assertions do not satisfy these acceptance items. |

The initial batch used a nonexistent `investigation.test.mjs` filename; the correct
`assistant-investigation.test.mjs` was then run and passed 6/6. Earlier test failures
from the removed header selector and added focus ref were corrected to exercise the
new actual composer/action; they are not reported as inherited application failures.

### A1 limits, rollback and continuation

Delivery states: **implemented; locally tested**. Candidate browser verification,
exact-head CI and final committed-head review are reported separately in the PR.
Human approval is pending. **Deployed: UNKNOWN / no deployment performed.**
Baseline browser observations do not verify this candidate. No hosted corpus size,
Qwen retrieval quality, model inference, temporal adapter or capacity claim is made.

Rollback is a reviewed revert of this bounded change, preserving subsequent work.
There is no data migration, new package, service, source admission or durable chat
store to undo. The optional server partition field remains backward-compatible;
active jobs keep existing deadlines and rate/session/source controls.

Prioritized **PROPOSED** continuation, receiving owner Lead Developer:

1. A2: run the hydrated candidate and phone/keyboard journey; resolve measured layout,
   focus, performance and accessibility findings. Then implement the independent
   evidence composition and truthful recent-investigation management against the
   verified retention model. Do not treat welcome prompts as coverage evidence.
2. B: inventory compatible temporal layers and source clocks, then implement county
   coverage planning, pinned/Auto-fit historical loading and a resource-budgeted player.
3. C: verify hosted eligible stores and measured corpus coverage before incremental
   admission and evaluated Qwen retrieval/tool improvements.

## Placement and governing references

Existing standalone `app/`, `server/`, `tests/`, `docs/` and
`data/receipts/generated/` responsibilities are reused; `.github/workflows/`
adds the new discovery/starter/composer suites to the existing CI gate; no workflow
permissions or services change. Directory Rules §§7.2, 8.2, 9.1, 10.1 and 12.4 place UI with its app,
executable conformance with tests, explanation with docs and process memory in
the existing receipt family. The dated blueprint is explanatory and proposed;
it creates no new semantic/schema/policy/source/release authority. The
governance sources below are pinned to the inspected monorepo, rather than
copied into the standalone application as competing doctrine.

- [Hosted root instructions](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/508db6073f3602e461c7b9bd33ced648417c37d8/AGENTS.md).
- [Accepted ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/ca54cf54653731e133d8ef9c2234531054bbdfc7/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules bytes.
- [Pinned Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/ca54cf54653731e133d8ef9c2234531054bbdfc7/docs/doctrine/directory-rules.md), blob `fd49a0b83e55cef52c1124281f093e263526898d`.
- [Contributor reliability guidance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/ca54cf54653731e133d8ef9c2234531054bbdfc7/docs/runbooks/pr-reliability-guide.md), a PROPOSED subordinate runbook.
- [Current repository PR template](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/ca54cf54653731e133d8ef9c2234531054bbdfc7/.github/PULL_REQUEST_TEMPLATE.md), v1.7 / CONTRACT_VERSION 3.0.0.
- [Existing sitewide AI boundaries](ai-sitewide-workflows-20261017.md), [county discovery/export record](investigation-handoff-20261018.md), [county browser acceptance](county-search-browser-20261018.md), and [Scene Studio](scene-studio.md), retaining each record's original date and validation limits.
