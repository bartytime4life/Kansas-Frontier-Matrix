# Aviation held workspace — October 21, 2026

Base: `a0-hosted-ai-web-20261017@c27e2b2cd193a8a93ae14603fafda4514fd8fce5`.
The existing map's Explore tools include an aviation reference control. This
addition does not activate an aviation layer or introduce another Explorer.

## Navigation and responsive disclosures

Aviation research sits below the compact Other map tools link grid. Expand
Explore, then Aviation research, then Evidence & AI with a tap, click, or native
keyboard disclosure action. The full-width controls and source link have 44px
minimum touch targets and visible keyboard focus.

Explore scrolls within the existing panel bounds and retains its summary while
scrolling. In windows at most 600px tall, the panel scrolls as one region instead;
its heading and close button stay visible. This avoids stacking a pinned summary
and large fixed controls above a scroll viewport too short for one control.
Expansion keeps the panel and map bounds stable. Close Explorer navigation to
recover the map space. Neither disclosure requires hover or adds animation.

Regression coverage: [aviation-layout.browser.mjs](../tests/aviation-layout.browser.mjs)
runs against the production build at an uncredentialed loopback origin. It checks
320×568 and 390×844 phones, 844×390 landscape, 768×1024 and 1024×768 tablets,
and 1440×900 desktop; native touch/mouse, keyboard traversal, visible focus,
scroll containment, map/panel geometry, reduced motion, and held availability.
External requests and unrelated APIs are isolated; no fixture is aviation evidence.
The existing public-core workflow runs this check alongside browser acceptance.
For a locally started production candidate:

```bash
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 \
  KFM_TEST_CHROME=google-chrome node --test tests/aviation-layout.browser.mjs
```

Browser emulation does not establish physical-device or deployed-host acceptance.
The source admission, release and publication holds below still apply.

## Held data and private tooling

`GET /api/aviation/airports` accepts only bounded county, edition and text-search
parameters, then returns ABSTAIN/AVIATION_RELEASE_PROFILE_REQUIRED before any
DB, credential, filesystem or upstream access. No environment setting overrides
this hold. Unknown/duplicate/sensitive export/SQL parameters are rejected.
Present, edition/county changes, close/unmount and AI interaction retire pending
requests; generation checking rejects a delayed result even if cancellation is
ignored by the transport. There is no observation playback or synthetic traffic.

`server/aviation-candidates.mjs` is private operator code, not imported by routes.
It offers parameterized transactional candidate import, idempotent integrity
readback and bounded county queries. It has no connection constructor, public
writer, scheduler, approval or release method. The main repository's proposed
MySQL migration and FAA capture/pipeline/schema own the corresponding source and
storage responsibility; no SQLite/D1 schema is copied into GoDaddy.

AI exposes only explicit county/selected-facility intents and abstains for lack
of released evidence. Unrecognized tools (SQL, ownership, missions, raw export)
are denied. No aircraft identities, raw archives, private addresses, Ollama or
second-PC filesystem access are introduced. Future factual AI must use existing
release/policy/evidence replay rather than turning this hold into an enable flag.

Map rendering, Evidence Drawer/report exports and surveillance frames remain
blocked pending rights/sensitivity, horizontal datum, aviation release profile,
verified release binding and browser acceptance. FAA reference editions are
separate from surveillance observation clocks. Research/context only, never
navigation or flight planning. OpenSky remains disabled; independent radio
observations or adsb.lol require their own source/terms/coverage assessment.

Placement: current hosted AGENTS.md and preservation record were inspected;
this separate app reuses app/, server/, tests/ and docs/ under their existing
application responsibilities. Main ADR-0029 / DIR-PLACE-002 and DIR-EXEC-001
preserve the public/private boundary. Governed mirror, database bindings,
second PC, AI configuration and existing production assets are unchanged.

Validation: targeted tests plus production build and TypeScript check are
recorded in the draft PR. Live MySQL migration/import, provider coverage,
second-PC integration, visual/mobile browser QA and production readback are
unrun. Revert this change to remove the held control and route. No live data
rollback is needed. This is implementation only, not deployment or publication.

Original PR #5392 acceptance: eight targeted Node tests; full standalone suite 1,613 passed, 19 explicitly skipped, zero failures (1,632 total). Production build, TypeScript and built HTTP 200 ABSTAIN / 400 invalid-query checks passed. Final context-retirement binding passed the same build, TypeScript and complete-suite rerun. No Chrome executable was available for that original visual QA. Corrective layout validation is recorded separately in its pull request.
