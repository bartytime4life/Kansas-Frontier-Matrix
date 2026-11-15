# Explorer welcome and explicit navigation — 2026-10-19

## Short-window Status scrolling follow-up — November 15, 2026 candidate

This follow-up is based on merged source
`1b61903fe5fc6196ddd2cc03104807abd2fc9fb5`. That base's complete tree is identical to
PR #5867 head `ce5e646d07a094c909bc60d91323f061e2a95762`. Existing CI supplies
the failing baseline below. The user authorized the prepared six-path follow-up;
its CSS and test bytes match the reviewed patch. Local candidate outcomes and
pending rendered acceptance are recorded separately below.

Navigation job 132975734771 in run 43767480914 reported 18 passes, two failures
and one cancelled test. The four KDOT roads / NASA fire-point cases at
1280 × 800 and 390 × 844 passed both keyboard round trips, visible returned
focus, Status wheel movement, unchanged source controls and generic Status
return. At 681 × 468 both sources opened with visible, focused details, but
the real Status-ancestor wheel assertion failed before Back was activated.
Those failures do not establish a failure of the new return-focus effect.

Full Explorer job 132975735129 in the same PR run reported 157 passes, three
failures and five opt-in skips. It repeats those two wheel failures and the
1280 × 800 expanded-welcome geometry premise failure described in the welcome
guide. It adds no other failure or cancellation.

Merge-commit navigation job 132976153506 in run 43767614572 repeated the same
four source passes and two short-window wheel failures: 19 passes, two failures,
no cancellations. The retained intercepted-API case that timed out in the
PR run passed on the identical merged tree. That intermittent observation has
no established root cause and is outside this correction. A NASA 390 × 844
return screenshot also shows an unavailable-provider notice partly covering
the return label despite automated geometry/hit-test passes. That separate
visual-usability qualification is retained rather than claimed fixed here.

Captured geometry shows an inner Status element with no scroll range while
the outer Layers panel has range. The existing max-height:600px layout releases
the catalogue body's overflow but leaves Status as a contained scroll container.
That source/geometry combination supports a scroll-chaining explanation; the
candidate CSS correction still requires rendered verification at authoring. It adds Status to
the existing overflow:visible rule for Layers/live at that height breakpoint.
The six source-case assertions, scroll-padding and sticky heading are retained;
tall-window scrolling rules are unchanged.

Core job 132975735016 separately reported 2,992 passes, one failure and 25 skips.
Its unchanged workspace-help callback fixture omits the newly read
`sourceStatusReturnPendingRef` and throws a ReferenceError; the same test
passed on the preceding base. The application declares the ref. This candidate
supplies the fixture dependency while retaining all frame/focus assertions.
This is an introduced harness integration omission, not evidence of the same
ReferenceError in the rendered application.

At candidate authoring, the seven-file focused suite passed 129 tests with no
failures or skips. The production build and TypeScript verification passed.
The complete standalone Node suite passed 2,993 tests with zero failures and
25 explicit skips. Its first local attempt had 2,982 passes, five failures and
23 skips because the sparse checkout omitted an existing tracked hosting-metadata
fixture. Restoring that file's exact base bytes in the isolated checkout allowed
the complete rerun; no configuration value or candidate source path changed.
Both attempts are retained in `KFM-STATUS-SCROLL-FOLLOWUP-EXECUTION-20261115`.

Candidate rendered CI is pending at authoring. Existing CI supplies the failing
comparison and does not validate this follow-up. Local Chromium's recorded
pre-page socket denial remains a separate environment limit; no repeat launch
or browser-policy bypass was attempted.

Placement retains the existing app/tests/docs roots and generated-receipt lane
under AGENTS, accepted ADR-0029 and Directory Rules. No permission, source,
schema, authority or workflow changes are included. A reviewed revert restores
this bounded correction while preserving evidence history. CI, merge and public
deployment remain separate. No public deployment, physical-device acceptance,
live-provider delivery or complete map-rendering claim is established here.

## Source-details return focus — November 15, 2026 candidate

Independent public-UI verification, alongside inspection of hosted source
`0dc7bb6d8a34ee6ced5ee061bdba80d65bf662b7`, confirmed #5859's source-opening
behavior for disabled KDOT roads and NASA fire points. Public build metadata
matched the inspected source-input digest but did not establish an exact deployed
commit or built-byte identity. At a 681 × 468 CSS viewport produced by 200% desktop zoom,
Back to layers focused the correct source action below the visible Layers panel.
This is an observed return-path defect; the evidence does not establish that
#5859 introduced it. The review record is `KFM-5859-INDEPENDENT-20261115`.

This candidate queues the source return until React commits the closed Status
view. It resolves the existing return target, uses `revealPanelControl` to reveal
that target inside Layers, and then focuses it without a second implicit scroll.
A newer source opening or a different committed workspace/panel cancels the
pending return. The existing source-opening behavior, layer selection, history
rules and exact source-download allowlist are retained. The separate generic
Layers return timer discussed in #5864 is outside this correction.

The added callback tests check committed ordering, one-time consumption and
superseded navigation. The browser suite defines cases for both sources at 1280 × 800,
390 × 844 and 681 × 468, two keyboard round trips each, actual ancestor clipping,
Status wheel scrolling, generic Status return and unchanged rendered official
source controls. It never scrolls the expected return target after Back.
Its name remains in the existing focused source-status CI selector.

For PR #5867, local validation passed 119 focused tests, the production build
and TypeScript verification. All three new focus-control unit cases failed
against baseline runtime and passed with that candidate. The local browser
attempt aborted before page creation because Chromium could not create its
socket; it is not a rendered failure reproduction. Subsequent exact-head CI
passed the four 1280 × 800 / 390 × 844 cases and exposed the two 681 × 468 wheel
failures described above. The PR and follow-up evidence keep those stages distinct.
A 681 × 468 emulated viewport does not reproduce 200% browser zoom;
390 × 844 emulation does not establish physical-phone or software-keyboard use.
Isolated unavailable-provider fixtures establish navigation and selection state,
not live provider data or complete rendered map-layer visibility. Missing-source
fallback retains its existing callback regression; rendered fallback acceptance
remains separate. Baseline, candidate, CI and public results must stay distinct.

Placement retains this standalone hosted composition's existing `app/`, `tests/`
and `docs/` responsibilities under its AGENTS record and accepted ADR-0029 /
Directory Rules §§5, 7.2, 10.1 and 14. No root, source, policy, schema, release or
publication authority is introduced. Rollback reverts the bounded candidate
change; preserve data, settings and the original verification record. Merge and
public deployment require their own authority and evidence.

## Finding and scope

Confirmed on hosted branch commit `0ad31b2c993e6d6973b678192f689650ab66e8da`
(merge of [PR #5290](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5290)):
a visitor without the v2 guide dismissal preference sees the welcome guide over
an explicitly requested topic or map tool. The
[resolved review thread](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5290#discussion_r4310128040)
did not correspond to a source correction.

Clean-profile, hydrated Chrome reproduction at 1366×768 and 390×844 confirmed
the obstruction for direct topic URLs, tool URLs, a real keyboard-activated
Topics catalogue link, and restored topic history. All four destination cases
failed at both sizes; the normal welcome/preference case passed at both sizes.
The baseline TAP report counts the two failed parent suites too (2 pass,
10 fail); it is not ten separate destination failures.

During this task, PR #5299 advanced the hosted branch to
`80a822d0efb663594db469399e6b319ea6df6303`. Its changes did not correct or alter
the guide/topic implementation. This candidate was rebased onto that commit.
Its full standalone test workflow and production startup checks are retained;
the only additional workflow command runs the new browser navigation suite.
The GoDaddy outage investigation, hosting settings and public deployment are
outside this correction.

## Behavior

- Decide welcome visibility using the same effective URL/history parameters as
  destination restoration, before saving generated defaults to history.
- Valid topics (including explicit `all`), `mapui=open`, imagery/selected layer
  views, comparison mode, feature links, and explicit shared camera URLs bypass
  automatic welcome. Existing `layers=sources` and `maptab=localAtlas` behavior
  remains compatible.
- A plain Explorer entry retains welcome unless the explicit v2 opt-out is set.
  Unrelated query parameters and invalid topics do not suppress it. An
  automatically saved camera in a plain `/` history entry is not an intentional
  shared URL and does not suppress welcome on reload.
- Back/Forward restoration of a destination closes an open guide without
  persisting opt-out. If focus was inside that guide, return it to its trigger;
  existing compact-panel focus handling then owns the destination. History
  restoration never automatically reopens welcome within the mounted Explorer.
- Manual `?` help, keyboard dismissal and existing v2 preference semantics are
  retained. The previous v1 key is untouched; blocked storage remains usable.

This is presentation/navigation state only. No dataset, source identity,
account, storage binding, evidence state, permission, release gate or public
endpoint changes. Bypass is not consent and never writes a dismissal preference.

## Reproducible validation

Use Node 22, installed Google Chrome (or `KFM_TEST_CHROME`), and a clean checkout
of the PR's exact head. The existing CI workflow also checks out the exact PR
head, builds it, runs the full standalone suite, and runs hydrated browser tests.

```sh
npm ci
npm run build
npx tsc --noEmit
node --test tests/explorer-startup.test.mjs tests/topic-organization.test.mjs tests/explorer-interface-refresh.test.mjs tests/workspace-help-navigation.test.mjs tests/explorer-layer-history.test.mjs tests/river-startup-restoration.test.mjs tests/explorer-menu-dismissal.test.mjs tests/mobile-compatibility.test.mjs tests/workspace-map-navigation.test.mjs
```

In one terminal, start the isolated candidate:

```sh
NODE_ENV=production PORT=5186 node server/start.mjs
```

In another terminal:

```sh
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5186 node --test tests/explorer-startup.browser.mjs
```

The browser test accepts only loopback HTTP origins. It creates disposable
Chrome profiles, clears local storage and saved history for fresh-entry cases,
uses native keyboard input, and checks the actual hydrated application. It
blocks external providers and substitutes unavailable responses for application
APIs other than build identity. This tests navigation independently of provider
availability; it does not qualify maps, source data, AI inference or production.
The history-specific cases explicitly retain or restore history instead.

| Coverage | Observable assertion |
| --- | --- |
| All 17 topic definitions and their tool links | Executed destination predicate, plus existing topic catalogue tests |
| Desktop and phone direct topics | Selected engineering/groundwater topic, no guide, interactive Layers controls |
| Five catalogue tools | Measure, Compare, Inspect, Scene and History open; Tab remains in available controls; Escape closes each tool |
| Shared views and legacy routes | Camera URL and source-status routes bypass without writing opt-out |
| Normal entry/reload | Welcome autofocus, unchecked opt-out, Escape returns focus, Enter reopens help; plain reload still welcomes |
| Preferences and unavailable storage | v2 preserved, v1 alone does not opt out, blocked reads still permit welcome/dismissal |
| Real catalogue navigation | Enter activates Topics link; browser Back and Forward restore the expected page/topic |
| Saved tab/popstate | Saved topic restored; Back closes an already-open guide; Forward does not resurrect it |

Local runs passed the build, TypeScript, 49 focused tests, and all 12 browser
subtests across the two sizes (14 TAP passes including parent suites). The PR
records the final immutable head and exact-head CI result. Earlier failed
candidate preference checks were traced to test setup reusing the same history
entry on repeated `Page.navigate('/')`; fresh-entry setup now clears that state.
Plain reload behavior is separately tested without clearing it.

Chrome emulation is not physical-device Safari/VoiceOver qualification. No
independent human review or public deployment is established by these checks.

## Placement, risks and rollback

Directory Rules.pdf was not present in the supplied sources or hosted tree.
The current accepted successor was checked at monorepo
`8aac5443f94d27078f2789d01de74b15624e94d8`:
[`docs/doctrine/directory-rules.md`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/8aac5443f94d27078f2789d01de74b15624e94d8/docs/doctrine/directory-rules.md),
SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`,
and accepted ADR-0029. Its pinned internal draft label does not negate the
accepted adoption record. Responsibility placement follows §5/§7 and this
composition's `AGENTS.md`, `docs/SITE_PRESERVATION.md`, and
`docs/godaddy-node-preview.md`: existing `app/` owns view behavior, `tests/`
owns executable regressions, `docs/` owns this explanation, and `.github/`
owns test execution. No new root, policy or canonical data home is introduced.

The main compatibility risk is a future navigation parameter that opens a new
destination but is absent from the bypass predicate. Extend both destination
restoration and this test matrix together. Automatic bypass intentionally does
not alter the user's persisted preference. The change has no schema migration.
Rollback is a focused revert of this navigation commit/PR while retaining
subsequent unrelated work, followed by the same tests. Do not revert PR #5299,
reset private data, change DNS, or deploy as an incidental part of rollback.

## Welcome and Layers ownership repair - October 31, 2026

**CONFIRMED reproduction before application edits.** The GoDaddy preview for
`urdng3v1vk` allowed Layers to become active while welcome remained visible.
At mobile size, opening Map controls could leave their menu behind welcome,
and focus could fall to the page body. The local unmodified development source
`9bdf1e972223964e16ff88f5c8c7a994b300579b` reproduced the failing handoff
regressions at 1280 x 800 and 390 x 844. This is separate from the navigation
capabilities in [#5643](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5643)
and the Geology hover change in
[#5647](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5647).

The preview's `/api/build` read reported application-input digest
`sha256:38f4a86d8f6e13e698d65bf4750169b58f58e81080922c6d4d66a4e02cc35e15`,
1,158 source files, `sourceCommit: null`, and `WORKTREE_MODIFIED`. Its exact
Git revision is **UNKNOWN**. The browser observation does not establish parity
with the checkout. Subsequent authoring rebased onto development source
`022f43a5ceac8e00fb9d994396da147335b468bb`, preserving its independent
welcome-scroll repair and test changes.

### Behavior and ownership

- Layers, its keyboard shortcut, and Skip to map dismiss welcome in the same state change.
  Compact Map-menu entry also leaves welcome, so its controls are reachable.
  Reopening welcome revokes the previous panels without resetting map content.
  Skip entry uses the existing focus handoff without native hash navigation,
  which would otherwise create a history entry that restores All topics.
- Pending restoration holds the header, skip link, and map inert. Welcome
  then holds the covered map inert while its own controls and header navigation
  remain available. Nested source notes retain their existing modal ownership.
- Layers focus is scheduled after its committed opening paint and canceled
  when another opening or dismissal supersedes it. Escape closes Layers on
  desktop and compact layouts; focus returns to a visible trigger, a closed
  menu's summary, or the map when the category trigger has disappeared.
- Compact Layers excludes background focus and pointer input. A tap on inert
  background cannot blur the panel to body and strand the next Escape.
- Initial restoration can decide only an undecided welcome. Late preview
  initialization cannot resurrect a departed welcome, and repeated retained
  category handlers perform one departure before unmount.
- The renderer's actual attribution control moves to the welcome's independent
  source strip while the map is inert, then returns to the normal map or
  fullscreen host. Attribution text and provider links are not copied. Modal
  cleanup does not restore stale attributes over an already excluded branch
  whose owning render has since released it.

### Regression coverage and acceptance boundary

`tests/explorer-startup.browser.mjs` exercises both 1280 x 800 and 390 x 844:
early Layers entry with its real lazy renderer held, late renderer release,
Escape, visible-trigger/map focus restoration, compact Tab wrapping, inert
background focus and touch, and settled Science-card mouse/touch entry.
Another case delays zero-delay startup tasks before hydration restoration and
slows the real entrance animation to 5% speed, then selects a category during
that transition. It also leaves nested source notes through repeated source
actions and compares the selected category, explicit GOES layer, camera,
opacity state, motion setting, and stored device preferences before and after.
Existing welcome layout journeys now verify real provider credits remain
hit-testable and keyboard accessible outside the inert map.

These browser cases use disposable profiles, loopback builds, empty map-style
fixtures and unavailable provider/AI responses. They establish UI ownership,
focus and state preservation, not scientific accuracy, provider availability,
physical-device qualification, source admission or release. Ordinary tests
execute the production restoration and focus callbacks, test obsolete-frame
cancellation, and verify one departure for rapid retained category handlers.
Final test counts, exact review head and CI results belong in the associated
pull request; failed or skipped checks must remain separately attributed.

The unchanged-base inventory-redaction test also fails on this macOS host:
its synthetic IPv4 line is not redacted by the existing shell pipeline.
This repair changes no inventory code. Canonical `TMPDIR=/private/tmp` is used
for the full suite because macOS's usual temporary-directory alias causes
unrelated strict-path and Git-identity fixture failures. A test run during a
rebuild is not final acceptance; build first, then test the sealed candidate.

Placement retains the existing `app/`, `tests/` and `docs/` owners described
above. The source-lineage Directory Rules PDF remains unavailable in this
workspace; the canonical successor and accepted ADR-0029 were inspected.
There is no new root, contract, schema, policy or data lifecycle authority.
Rollback is a focused application/test/documentation revert followed by the
same startup matrix; saved settings and data require no migration or reset.

**Source review and hosted publication are separate acceptance steps.** This
repair does not authorize a merge, GoDaddy update/publication, original Sites
synchronization, private-store operation or data promotion. Hosted acceptance
must separately bind the reviewed application inputs to a deployed identity
and repeat the startup, keyboard and mobile journeys on that deployment.


## Browser Back, restored current reads and map keys — November 6, 2026

The owner reproduced the live-site failure by opening a category from startup
and pressing the mouse Back button: the browser left KFM. The preceding
implementation serialized the current map with replaceState only, so its
in-application destinations did not create browser navigation entries.

Deliberate category/map, topic, map-utility, source-status and supported civic
inspection actions now request one history step. The committed render writes
that step with pushState when the serialized destination differs. Camera
movement, rendering and data refreshes continue updating the current step.
Unchanged destinations do not add empty entries. The original browser entry is
not intercepted: a visitor can still leave KFM by continuing Back past it.
Router state and the current URL are retained; embedded-host history stays
untouched. Existing location-camera redaction runs before serialization.

A history entry also records whether it represents startup or the map. Back
from the first category restores startup; Forward restores that map. Ordinary
Escape dismissal does not redefine the startup entry, so its existing reload
behavior is retained. An explicitly opened map entry can reload into that map.
This is browser-tab history, not a new persistent dataset or account store.

Returning through popstate or a persisted pageshow revalidates selected current
JSON feeds after restored time and selections commit. Radar, satellite, River
Pulse and NWPS schedulers also observe restoration while retaining their own
request guards and retry windows. Archived selections and historical map time
remain dated; they are not silently replaced with current observations. Current
reads retain the existing no-store request path. Refreshing does not rewrite
provider observation/retrieval times, certify provider freshness, or manufacture
a release. Existing unavailable/error handling remains authoritative.

The category controls now put a named, keyboard-operable **Map key — Colors &
symbols** disclosure immediately below their heading, ahead of long instrument
controls. It reuses the existing selected-layer keys, crop colors, year labels
and source notes. No key appears when none is supplied. Provider-specific legends
and unimplemented story labs retain their existing states.

Validation uses the existing history, startup, map-key, crop, source-recovery,
category and workspace tests. Two hydrated browser regressions cover the owner's
startup → Government & civic → Back → startup → Forward → map → reload journey
at 1280 × 800 and 390 × 844; hosted execution is recorded in the pull request.
The available cloud browser separately passed the desktop Back/Forward journey.
It reports WebGL2 unavailable and its DevTools are administrator-disabled, so
that observation does not qualify actual map drawing, crop legend painting,
phone touch input, physical GPUs, provider freshness or the live deployment.

Placement follows accepted ADR-0029 and the canonical Directory Rules checked
at main@72c7aa14f0c1acfc0509896a3d58be05c6a08cab: existing app owns presentation,
tests owns regressions and docs owns this behavior/rollback record. No data,
policy, schema, release or storage root is introduced. Rollback is a reviewed
revert of this change; preserve browser settings and all source data. Source
review, merge and GoDaddy publication remain separate operations.


### Review corrections — November 6, 2026

PR #5747 review identified two restoration gaps. A saved startup entry could
ignore the explicit “Don't show on start” preference on a new-document reload;
a source-status entry could remain active when Back selected an ordinary map,
then contaminate that preceding entry with layers=sources. Both failures were
reproduced by executing the unchanged production restoration code before repair.

New-document restoration now checks the saved dismissal preference before
showing startup, and remembered dismissal clears the retained startup marker on
save. Deliberate Back navigation can still revisit a startup entry. Source-status
restoration assigns both true and false explicitly; ordinary selected-map entries
close its panel, direct topic links retain their catalog, and legacy source-status
links still open the status panel. Other explicit utility destinations retain
their existing handling. Browser regressions exercise remembered dismissal and
status-panel Back/Forward at desktop and phone widths. The pull request records
exact-head execution and remaining acceptance limits.


### Civic inspection restoration — November 6, 2026

A second review found that civic inspection created a history step, but Forward
could not reconstruct its official-context feature through the registry-only
lookup. Restoration now finds the exact civic identity in a checked payload for
the restored day. Congress, payload day and record day remain authoritative;
geometry and source properties are never copied from browser history.

If the dated payload has not loaded, retain the inspection identity and drawer
settings while the normal source request completes. A different navigation,
manual selection, clear action, hidden carrier or changed day cancels that
pending restoration. Missing records stay unavailable without substituting
another district or Congress. Tests cover delayed source arrival, exact dated
identity, cancellation and retention of the history destination; hydrated
synthetic browser journeys select a district through native controls, then use
Back, Forward and reload at desktop and phone widths. Their execution and any
remaining qualification gaps belong to the current-head pull request evidence.


### Delayed saves during history traversal — November 6, 2026

The independent navigation job at head f5810e7 reproduced a Forward failure at
both 1280 × 800 and 390 × 844. Startup was visible again instead of the selected
Government map. The pre-existing full matrix had passed this journey on earlier
heads; that result did not cover every timing interleaving.

A native traversal selects its entry before popstate and React passive effects
finish. The previous screen's delayed serialization could therefore replace
the newly selected entry. A regression executes the actual production save
effect with that interleaving: unchanged source overwrites the destination's
map marker; the correction preserves its topic and marker without writing.

Native entries now have an opaque browser-local identity. Restoration commits
that identity with the restored view; passive saves require the identity owned
by their render. Deliberate navigation creates a fresh identity, while camera
updates, router-state clones and reload retain it. An obsolete render cannot
adopt or overwrite a different entry. The URL, router fields, embedded-host
boundary, original exit behavior and source timestamps retain their contracts.
Blocked history remains nonfatal. No persistent data migration is required.

The browser journey repeats Back/Forward three times without a settling delay,
checks that both native entries are revisited rather than recreated, and retains
the reload assertion. Failure diagnostics include bounded history identity and
topic information. Exact-head native results, review and hosted/public identity
verification are still required before claiming publication or complete browser
acceptance. Reverting these source/test changes requires no data rollback.

Review then identified the explicit sharing helper replacing history state with
null. It now retains the current entry's router/Explorer state while updating
the URL. A helper regression fails before repair and then verifies that sharing
still permits a passive view save and a fresh map step. The native journey also
shares Government, opens Weather through the later chooser, revisits both maps
with Back/Forward and reloads the later selection. Clipboard success is not an
acceptance assumption; the existing address-bar fallback remains available.

### Save before the next chooser action — November 6, 2026

At 7981d631, the phone sharing journey retained three native steps where four
were required: the chooser could become interactive before its passive history
effect saved that destination. The next map action could replace the pending
request, losing the chooser's step. The earlier entry-identity check prevents
cross-entry contamination, but does not schedule when a visible step is saved.

History serialization now runs in the layout commit before the destination can
accept its next input. An actual-hook regression fails with passive scheduling
and passes with layout scheduling, retaining separate chooser and later-map
entries. Existing identity, source-date/privacy, embedded-host and original exit
contracts remain. Native browser assertions and deadlines are retained; local
hook tests do not replace current-head browser or deployment acceptance.

## Library return destination — November 11, 2026

The existing data-library links use `/?panel=layers`. That exact value now
bypasses automatic welcome and opens the editable Layers panel. It does not
open source status or write the device's welcome preference. Plain `/`, empty
or unknown panel values retain their existing welcome behavior. The starting
page's presentation, category cards and styles are unchanged.

At base `beed3bbcdb6ef9e65c17f9c481be171f63c3dc8d`, the added destination and
actual-restoration regressions both fail before the fix. They exercise the
production destination predicate and restoration statements, including starting
from a different panel mode. Existing preference/history tests remain in place.
This is navigation state only; no provider, data, runtime or access change.
Implementation, regression and documentation stay in the existing `app/`,
`tests/` and `docs/` responsibility roots. Revert this bounded change to roll
back; no saved-data migration is required. Publication remains separate.

Candidate validation: 59 focused model/component tests pass; production build
and TypeScript pass. The existing production-build startup browser matrix
passes 14 journeys at 1366×768 and 390×844 (16 TAP passes including parents),
including the new library destination, native-pointer Browse activation,
unobscured topic control, normal welcome, preferences and Back/Forward.
Providers were blocked and APIs isolated. An initial new browser assertion
incorrectly assumed Browse was already selected; the final fixture uses its
visible control before checking topics. No assertion or deadline was waived.
This is local synthetic navigation evidence, not actual hosted acceptance.


First-head CI found one additional fixture coupling in `local-atlas.test.mjs`:
it required the exact expression `if (restoredSourceStatus)` before executing
the actual restoration block. The fixture now bounds that complete block by its
existing status assignment and next-utility declaration. All eight legacy
source-status combinations still assert panel mode/open state, closed PC utility
and unchanged URL parameters. This is a fixture adaptation, not a waived check.
