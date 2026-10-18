<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/site/chat-composer-reach-20261018
title: Keep the Chat with KFM question box reachable at every viewport
type: implementation-verification-record
version: v0.1
status: draft
owning_root: docs/
responsibility: Record this standalone application's bounded chat-layout repair, its evidence, limits and rollback.
truth_posture: CONFIRMED local rendered observations named below; NEEDS VERIFICATION hosted preview and production acceptance.
[/KFM_META_BLOCK_V2] -->

# Keep the Chat with KFM question box reachable at every viewport

Recorded 2026-10-18. Draft application change on the standalone GoDaddy Node
composition. Not deployment, publication, model qualification or data admission.

## Starting point

| Surface | Identity | Meaning |
| --- | --- | --- |
| Authoring base | `a0-hosted-ai-web-20261017@9aa26f1ec7724253c05a605b3f6b96d9c454d0aa` | Standalone Node app including merged #5251 county search and investigation exports. |
| Monorepo main | `907cc58c72844bf56923b63c970b83a202fa5e75` | Different layout and responsibilities; not touched. |
| Public application | `https://kansasfrontiermatrix.com/` | Anonymous browser, 2026-10-18. `/api/build` returns branded 404; exact deployed source **UNKNOWN** here (runbook records `4b3cc83`, NEEDS VERIFICATION). |
| Open PRs | none at authoring | No overlap. |

## Journey walk and chosen slice

Local production build of the authoring base, `PORT=4191 npm start`, in-app
Chromium, 2026-10-18. The AI model was not configured locally ("Awaiting owner
setup"); that is an environment limit, not a finding.

| Step | Public site | Candidate (local) |
| --- | --- | --- |
| 1. Choose a place | **FAILS** — "Sedgwick", "Wichita", "Topeka", "Douglas County" return no match; only source names match. | Works for counties ("Sedgwick" → Sedgwick County). City names do not resolve ("Lawrence" → no match; "Wichita" → Wichita County only). |
| 2. Understand available data | Not reached by search. | Evidence Drawer opens with source, 2020 edition, retrieval time, limits, "not KFM evidence". Strong. |
| 3. Inspect evidence | — | Data / metadata / trace / correction state visible. Strong. |
| 4. Ask a context-aware question | — | **FAILS by layout.** The context card is correct, but the message box and Send are clipped below the panel at 1024×768, 1366×768, 1440×900 and 375×812. Only 1920×1080 fits. |
| 5. Save / export | — | Per-turn Copy / Markdown / JSON actions exist (#5251) but sit in the same clipped chat. |

Step 1 on the public site is already fixed in the candidate and awaits owner
publication. Step 4 is the weakest link in the candidate: a visitor on a common
laptop or any phone cannot type a question. That is the slice.

### Cause (CONFIRMED, 1366×768)

The chat region is 506 px tall. Its non-shrinking children total 693 px:
toolbar 38, context card 149, guide 34, composer **423**, footer 49. Only the
conversation log can shrink, so it collapses to 32 px and the composer overflows
an `overflow: hidden` parent. Commit `8f9f00d` ("Keep HUD chat composer visible
while conversation scrolls") intended the opposite; later context, guide, prompt
and option additions (#5230, #5233, #5251) accumulated in the fixed regions.

## Experience brief

- **Visitor:** someone who has picked a county and wants to ask about it, on a
  laptop, tablet or phone.
- **Problem:** the question box is invisible and unreachable by pointer.
- **Direction:** a pinned question bar. The question box, the Send/Search button
  and the current mode's trust line are always visible at the bottom of the chat.
  Everything else — context card, help, welcome, conversation, suggested
  questions — lives in one scroll region above it. Less-used answer options
  (mode, style, length, evidence filters) fold into one disclosure whose summary
  always names the current mode.
- **Non-goals:** no copy rewrite, no model, server, policy, data or export change;
  no redesign of the Evidence tab or panel chrome.

### Visual specification (Creative Lead acting in the design role)

- Pinned bar order: options summary row → textarea → action row (trust line left,
  Send right). Existing tokens, borders (`#30424f`), focus ring (`#e3c883`, 3 px)
  and ≥ 44 px targets.
- The options summary reads `Answer options · Explore ideas` or
  `Answer options · Find evidence`, so mode is visible as words, not colour.
- Opened options scroll internally (bounded height) and never push the
  textarea out of view.
- Scroll region keeps the context card first, so "what this question concerns"
  is the first thing above the conversation.

## Acceptance criteria

1. With a county selected and the chat tab open, the textarea and Send/Search are
   fully visible without scrolling at 1920×1080, 1440×900, 1366×768, 1024×768,
   768×1024, 390×844 and 375×667.
2. Everything else in the chat is reachable by wheel/touch scroll and by Tab; no
   chat content is clipped by an `overflow: hidden` ancestor.
3. New turns still scroll into view.
4. Current mode and its disclosure ("unverified discussion" / "released records")
   remain visible without opening options.
5. The submitted form still carries mode, style, depth, term, place, start and end.
6. Existing tests pass; a regression test covers the pinned-bar structure.
7. Keyboard focus order is scroll region → options → textarea → Send; Escape and
   focus-visible behaviour are unchanged.

## Implementation

| File | Change |
| --- | --- |
| `app/assistant/workspace.tsx` | Context, help, conversation log, suggested questions and the footer disclosure share one scroll region (`.body`). The form keeps an "Answer options · {mode}" disclosure (mode, style, length, mode hint, evidence filters), the textarea and the action row. All seven submitted fields stay inside the form. Autoscroll now brings the end of the latest turn into view in the scroll region. Explore-mode action line gains "· unverified discussion". |
| `app/assistant/workspace.module.css` | `.body` is the only shrinking region (`flex:1 1 0%`); the log no longer scrolls on its own; options scroll internally with a bounded height; 44 px summary and buttons; compact padding below 820 px height. |
| `app/inspection-panel.css` | Compact sheet only (≤ 1100 px): the duplicate "Chat with KFM" heading is visually hidden but kept as the dialog's accessible name; the context strip stays on one row. Desktop is unchanged. |
| `tests/chat-composer-reach.test.mjs` | Rendered-markup and stylesheet regression tests for the structure above. |

Design decisions taken during implementation: the scroll region gives up space
first (`0%` basis); options may shrink so the textarea never does; autoscroll
targets the end of the log rather than the bottom of the region so the context
card is not scrolled away on open.

## Rendered acceptance (CONFIRMED, local production build)

Rebuilt candidate, `PORT=4191 npm start`, in-app Chromium with viewport
emulation, Sedgwick County chosen by search, Chat opened from the Evidence
Drawer. "Visible" means the element's box lies inside the viewport and every
clipping ancestor.

| Viewport | Before: Send | After: textarea / Send / options (closed) | After (options open) | Scroll region height before → after |
| --- | --- | --- | --- | --- |
| 1920×1080 | visible | visible / visible / visible | all visible | not measured → 586 |
| 1440×900 | clipped | visible | all visible | — → 406 |
| 1366×768 | clipped | visible | all visible | 32 (log) → 308 |
| 1024×768 | clipped | visible | all visible | — → 158 |
| 768×1024 | not measured | visible | all visible | — → 253 |
| 390×844 | not measured | visible | all visible | — → 141 |
| 375×667 / 375×812 | absent from view (375×812) | visible (375×667) | all visible | — → 58 |

No horizontal document overflow at any size. Keyboard order from the
conversation log: suggested questions → "Answer options" → message box → Send.
The options summary switches between "Explore ideas" and "Find evidence" with
the mode select, and the action line switches to "Released records · no model
required". Context strip labels do not overflow at 375 px.

![Before, 1366×768: composer clipped](images/kfm-chat-before-1366x768-20261018.jpg)
![Before, 375×812: no composer](images/kfm-chat-before-375x812-20261018.jpg)
![After, 1366×768](images/kfm-chat-after-1366x768-20261018.jpg)
![After, 375×667](images/kfm-chat-after-375x667-20261018.jpg)

Public site, same day, 1366×768, nothing selected: composer visible but the
conversation log is 63 px tall. Cramped chat is **inherited**; full clipping
appears when a selected-record context card is present, which county search
(#5251) makes the common path.

Not verified: a real AI turn (no model configured locally, so Send stays
disabled — the turn autoscroll is covered by unit tests only), touch scrolling on
a physical phone, screen-reader output, and the hosted preview. No motion was
added, so reduced-motion behaviour is unchanged.

## Validation

| Check | Result |
| --- | --- |
| `npx tsc --noEmit --incremental false` | PASS |
| `npx eslint app/assistant/workspace.tsx` | PASS, 0 errors, 0 warnings |
| `node --test tests/chat-composer-reach.test.mjs tests/assistant-*.test.mjs tests/pc-ai-http.test.mjs tests/mobile-compatibility.test.mjs` (after rebuild) | 49/49 PASS |
| `npm run build` | PASS |
| `git diff --check` | PASS |
| Full `node --test tests/*.test.mjs`, clean build | 1,330 pass, 51 fail, 1 skipped of 1,382 |
| Same suite on unchanged base `9aa26f1`, separate clean worktree | 1,326 pass, 51 fail, 1 skipped of 1,378 |
| Failure diff (sorted test names) | **Identical 51 failures; none introduced.** The four added tests pass. Sampled inherited causes are `fetch failed` in built-route tests in this sandbox. |

Failure attribution note: an earlier full run on a non-clean `dist/` failed
`underground-load-boundary` because the asset-staging step intentionally retains
prior builds' hashed chunks (three Underground chunks after three local
rebuilds). It passes after `rm -rf dist public/assets` and one build. This is a
local repeated-build artifact, not a change effect.

## Performance (independent reviewer, before this change)

The candidate is +2.3% initial-route JS and +10% HTML versus the published site;
county search costs ~0.14 ms per debounced query with no network; each save is
one rechecking GET. This change is CSS and markup reordering, adds no request,
dependency or motion, and was not separately measured. Inherited findings are
in the backlog below.

## Review

Independent code review (correctness, accessibility, security): **in progress** at draft-PR creation; results will be added to this record and the PR. Performance baseline: completed by a separate reviewer (above). Product acceptance: Creative Lead, rendered checks above. No release authorization is requested or implied.

## Proposed backlog (not in this change)

- PROPOSED: resolve Kansas city/town names (Wichita, Lawrence, Topeka) to a place
  with an honest source; today "Wichita" offers only Wichita County, which is ~200
  miles from the city. Needs a released gazetteer source, not geocoding guesswork.
- PROPOSED: before the Census county feed arrives, search says "No current
  place … matches" instead of "Places still loading". Show an honest loading
  state.
- PROPOSED (perf reviewer, INHERITED): the county feed is re-fetched from Census
  on every page load (Cloudflare `DYNAMIC`, ~0.6–0.9 s). Memoize the fixed 2020
  edition server-side for 24 h. Owner: backend/hosting.
- PROPOSED (perf reviewer, INHERITED): hashed assets are served gzip, not brotli,
  and without `immutable`. Owner: hosting.
- PROPOSED (perf reviewer): `SiteAssistant` in the root layout now loads a 33 kB
  chunk on every route; lazy-load it on first open. Owner: frontend.
- PROPOSED: on phones the scroll region is 58 px at 375×667; consider a taller
  chat sheet when the composer is focused.
- NEEDS VERIFICATION: "Find evidence" says "no model required" but Search is
  disabled when the hosted model is not configured. Check whether evidence
  search should stay available without the model.

## Rollback

Revert this commit. No database, model, data, DNS or audience change.
