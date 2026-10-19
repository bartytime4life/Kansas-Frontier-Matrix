# Explorer welcome and explicit navigation — 2026-10-19

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
