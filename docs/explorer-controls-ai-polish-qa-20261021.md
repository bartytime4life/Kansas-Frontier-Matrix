# Explorer controls and AI interface review · 2026-10-21

Status: implementation candidate. Final result: **blocked** for full live-map visual acceptance.

## Scope and placement

Base: `a0-hosted-ai-web-20261017@4e0377e35fe5aa1440819b93bb51de304780a3b5`.
This is the separate GoDaddy Node composition identified by `AGENTS.md`; the
preserved Sites project, monorepo mirror, runtime bindings, and home-PC model
configuration are outside this change.

Directory basis: current `main` canonical `docs/doctrine/directory-rules.md`
(implementation/operations ownership, sections 3–4 and 7) and accepted ADR-0029;
this standalone application's existing `app/`, `tests/`, `scripts/`, and `docs/`
placements remain in use. No responsibility root or source/policy/schema home
is introduced. The generated knowledge pack is refreshed only for the revised
NIFC display limitation, using its existing deterministic generator.

## Resulting behavior

- One stationary yellow clock opens and closes the time transport and settings.
  The hourglass and its animation preference are absent from the active menu.
  Hover no longer opens it and pointer departure no longer closes it. Escape,
  outside click, keyboard activation, date selection, and playback remain.
- On phones, the settings sheet stops above the clock; its stacking context
  places settings above map navigation. The same clock stays clickable.
- NASA thermal detections retain their existing animated flames and footprint
  display. NIFC incident records also use animated flames, retaining their own
  source and feature identities. Both flame symbol layers participate in hit
  testing. Transparent circles retain generous hit areas without visible dots.
- The generic selected-point dot, glow, and ping are filtered out for these
  fire sources. Other point selections keep their existing presentation.
- Both fire layers share the existing animation ticker. Visibility, opacity,
  globe sizing, hidden-tab and reduced-motion gates remain in force. Incident
  locations and thermal detections remain distinct external context, not proof
  of the same event or measured flame intensity.
- The attribution button keeps a 44 × 44 CSS pixel footprint. Source text opens
  above the time row, constrained to the map width with a scroll limit; a single
  centered icon replaces background tiling at the larger touch size.
- Chat uses softer panel corners, pill controls, a compact context surface,
  calmer suggestions, and one rounded composer. The map chat starts in Ask;
  explicit Find requests still open discovery. AI identity, readiness, source
  limits, cancellation, draft isolation, and citations remain visible. Evidence
  search appears only after the runtime reports that capability available.

## Executed checks

- Production build: passed, with existing large-chunk and route-classification
  notices. TypeScript: passed. Changed TypeScript/TSX lint: 0 errors, 41 warnings
  in the existing large page; the other changed modules produced no warnings.
- Full Node suite: 1,636 passed, 19 skipped, 0 failed (1,655 total). Build-dependent tests ran
  against the production output, not an absent or inherited build.
- New behavior regressions cover clock toggle and Escape, fire visibility and
  opacity, globe icon sizing, flame hit identity, real MapLibre filter evaluation
  for fire versus ordinary points, and initial Ask versus explicit Find modes.
- The obsolete hourglass CSS assertion was retired; the archived component's
  reduced-motion/hidden-tab compatibility test remains. The accessibility audit
  now accepts a workspace prop before `active` without losing its active-state
  assertion. No security/policy assertion was relaxed.

## Browser evidence and limits

Source visual truth: the seven owner-supplied photographs in this conversation,
particularly the clock, fire selection, attribution, and chat views. They are
perspective photographs, not matched CSS viewport captures; no pixel-fidelity
claim is made. Implementation screenshots were inspected in the cloud browser
at 1363 × 936 and in a 390 × 844 CSS pixel iframe. The rendered review snapshot
used actual production HTML, CSS, and client bundles. Its APIs intentionally
returned unavailable; it did not connect to the home PC or emulate AI answers.
The full Node runtime could not be started in the cloud preview because its
installed MapLibre package lacked the required worker module. The local Vite
attempt also failed on restricted network-interface enumeration.

Observed UI checks:

- Desktop chat panel measured 490.67 CSS pixels wide with no horizontal overflow.
  Phone chat measured 390 CSS pixels wide with no horizontal overflow. Composer,
  explicit AI identity, supported mode actions, and Map return remained visible.
- Phone clock opened settings, then closed them from the same button. An earlier
  screenshot caught settings covering the clock; the sheet bottom was corrected
  to leave the clock accessible, and this interaction was repeated successfully.
- An isolated component fixture used the actual MapLibre 6.9 AttributionControl,
  production CSS, and explicitly synthetic attribution text, without WebGL.
  Desktop button coordinates stayed (1310,647), 44 × 44 pixels, across toggles;
  phone coordinates stayed (337,587), 44 × 44 pixels. Popup clearance above the
  synthetic transport was 15 pixels on desktop and 75 pixels on phone. Phone
  popup extent was x=15 through x=381, within the 390-pixel viewport.
- Browser console inspection surfaced an extension metadata error; it is not
  attributed to this app. The isolated source fixture's initial failed module
  fetch was corrected by serving module MIME types and restarting the fixture.

Open verification: the cloud browser reports WebGL2 unavailable, including on
production. Flame rendering and map-hit-to-drawer acceptance could not therefore
be visually exercised. Live home-PC inference and real provider refresh were
not tested. Screenshot comparison is qualitative and the temporary shared
preview was subsequently replaced by another project; stable captured image
paths are unavailable. No working-preview or pixel-comparison pass is claimed.

## Review, rollback, and release boundary

Author self-review only; independent review and hosted exact-head CI remain
separate. Revert this UI, display metadata, generated pack, tests, and docs as
one change. No database migration, source admission, release, merge, deployment,
or home-PC change is authorized or performed by this candidate.

final result: blocked


## 2026-10-22 follow-up: connected-browser acceptance and remaining release hold

This follow-up supersedes the earlier WebGL limitation only for the executed
checks below. It extends the same draft PR #5401, rather than adding a second
fire renderer or competing pull request.

### Published/source comparison

GoDaddy app `urdng3v1vk`'s **Published** tab reported commit
`00e59603e6012c144fcb7dbf1119f6b0e6ea29a4`. Its preview was out of sync.
The hosted branch remained `4e0377e35fe5aa1440819b93bb51de304780a3b5`;
the corrective PR started at `f31227c4b24ff499401e368e23bd6d15f27d703f`.
A Git comparison confirmed no fire-renderer or compact-time-control differences
between the reported published revision and hosted branch. Their differences
include AI discussion and aviation-layout changes; a whole-branch publication
would therefore carry more than this UI correction.

The public page was reloaded and showed VIIRS flames plus the unwanted
hourglass. GoDaddy's commit report is deployment metadata, not a byte-identity
proof: the browser blocked direct navigation to /api/build, and no matching
application-input digest was obtained. The published runtime was not changed.
The available GoDaddy connector supports domain discovery, not deployment;
existing hosting UI was inspected read-only.

The source findings remain distinct: NIFC incident points have their own style,
and the generic selection dot previously covered selected thermal detections.
The existing PR treats both using the established flame renderer and provider
identities. The local NIFC response contained no features, so a real incident
flame/hit test was unavailable; its behavior is covered with labeled test data.

### Additional corrections within existing owning roots

- app/explorer-theme.css: overflow:clip prevents browser focus from scrolling
  the map stage. The reproduced stage scrollTop was 265.6 pixels, displacing
  attribution and other map controls. Child dialogs retain their own scroll
  regions. The normal phone attribution anchor gains 60 pixels of clearance
  above the time row; live observation docks and Underground retain their
  existing positioning rules.
- app/compact-time-sweep.css: constrain the non-phone settings height using the
  actual toolbar allowance. At 911 x 600 CSS pixels the header previously rose
  under the toolbar; it now starts at y=67, below the y=54 toolbar edge.
- tests/fire-detection-style.test.mjs: one ticker for independently visible fire
  sources; reduced-motion and hidden-tab cancellation; still selectable symbols;
  hiding one fire source does not stop the other source's animation.
- tests/explorer-startup.browser.mjs: actual component geometry at desktop,
  tablet, short-window and phone sizes, stationary attribution, keyboard/focus,
  and an emulated touch close from the same clock. Provider responses are
  isolated fixtures; these tests do not assert data admission or release.

Placement follows the adopted Directory Rules v2 and accepted ADR-0029 read
from current main: this is an existing standalone composition. UI stays in app/,
regressions in tests/, and human QA in docs/. No responsibility root, mirror,
contract, policy, source-admission or release home was created or moved. The
unversioned Directory Rules.pdf was not available in the supplied sources;
the accepted successor was used as placement authority.

### Executed validation

- Production build: passed after the CSS corrections. TypeScript: passed.
- Complete ordinary Node suite: 1,639 passed, 17 skipped, 0 failed, 1,656 total.
  These are current-session results, not inherited PR claims.
- Fire/time focused suite: 11 passed, including the new motion-lifecycle check.
- New browser-test file content: syntax checked; execution is pending hosted CI.
  It was not run through a separate automation driver in the connected browser.
- Manual connected Chrome acceptance used the actual loopback production build,
  without hosting credentials, AI configuration or home-PC access. The local
  runtime acquired public provider context normally; this is not data admission.

| CSS viewport | Observed outcome |
|---|---|
| 1366 x 900 | Animated flames visible; pointer selection opened a NASA record with acquisition time and provider fields; selected flame stayed unobscured. Enter and Escape operated the clock and returned focus. |
| 1024 x 768 | Settings top y=67 below the 54-pixel toolbar; row y=626..682; information button y=687.47..731.47; source popup ends y=615.47; no horizontal overflow. |
| 911 x 600 | Settings top y=67 and height=382; toolbar ends y=54; map-stage scrollTop=0. |
| 390 x 844 | 56-pixel clock remains below settings; information button y=643.73..687.73 clears row y=702.27..758.27; source popup fits x=15.48..381.87 and ends y=571.73; focus does not scroll the map; no horizontal overflow. |

Additional real-map checks: flames remained visible in pitched Terrain 3D with
DEM and in globe projection; clicking a pitched flame selected its original
NASA record. An exact provider-pixel view at zoom 12 with satellite imagery,
terrain and motion=off showed the ember footprint. The opacity slider at zero
removed the fire display, and the visibility toggle removed the source. No
independent renderer, replacement provider record, evidence promotion, changed
source clock or inference configuration was introduced. Pointer interactions
at resized viewports were inconsistent through the browser connection; keyboard
and measured geometry were used for repeatable acceptance. Physical-device
and real touch acceptance remain unverified. Motion=off is an application
setting; system reduced-motion cancellation was verified by the unit regression,
not by changing the user's operating-system setting.

### CI and publication boundary

The original PR head's verify-core-delivery check failed in run 39785360544,
job 119846991366: 19 browser checks passed and 14 failed. Eleven failures involve
welcome assertions that still require eight topic cards/portals while the
rendered welcome has 17 topics. Three failures report Shift+Tab modal wrapping.
The welcome/browser-test source is unchanged between the hosted base and the
original PR head, but no exact-base browser rerun was executed; this is not a
claim that all failures are unrelated or harmless. No assertion was weakened.

Independent review, new exact-head hosted CI, physical touch devices and broader
provider/device combinations remain open. Do not publish while those release
checks are held. Roll back this follow-up by reverting its CSS, regressions and
documentation together; the whole PR retains its existing rollback boundary.
No merge, production publication, runtime binding, AI or home-PC change occurred.

Follow-up status: SOURCE_CORRECTED / RELEASE_HELD.
