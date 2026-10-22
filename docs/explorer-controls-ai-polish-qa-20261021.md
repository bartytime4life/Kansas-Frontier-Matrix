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
