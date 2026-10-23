# Compact calendar time sweep

Status: implementation candidate; browser acceptance and publication are separate gates.

The main time menu rests as a stationary yellow clock in a 56 × 56 pixel
control. Click, tap, Enter, or Space toggles the transport and settings from
that same position. Arrow Up opens it; Escape, the close button, or an outside
click dismisses it. Hover and pointer departure do not change the open state.
Configuration does not resize the map or reserve a bottom timeline row.

The stationary clock keeps its dark background, border, and shadow on hover,
including above light terrain and street basemaps. The legacy transparent
decorative-emblem style excludes this button. Moving onto or away from the
clock and transport leaves the menu's open state unchanged.

The hourglass is no longer mounted by the Explorer, and its animation option
has been removed. Earlier artwork and the unused component remain recoverable
for compatibility; they are not part of the active time control. On phones,
the scrollable settings sheet ends above the clock and transport so the same
clock remains available to close it. The expanded time panel stacks above
map navigation. The original playback, date range, source clocks, and A/B
behavior remain governed by their existing source and time rules.

The small progress indicator reports the requested cursor position in the user's
range, not source completeness or a measurement.

Year, month, and day selectors share a UTC cursor. Calendar arithmetic handles
leap dates, month ends, and DST boundaries. Years and months are dated snapshots,
not averages. Scrubbing previews immediately and coalesces source requests;
release, keyboard completion, or a short quiet period applies the date without a
separate Commit action. Playback waits for source requests and map-source settling,
pauses when hidden, respects reduced motion, and stops at the range boundary.
Only previously checked empty dates can be skipped; unchecked dates are not gaps.

Exact-day adapters currently connected here: USGS earthquakes, NOAA HMS smoke,
NASA NOAA-20 thermal points, and Raspberry Shake station inventory. Query floors
are limits on requests, not promises of continuous coverage. Only a validated,
checked payload for the exact requested day may pass the calendar display gate.
Current-only sources remain held on historical dates; independent basemap,
terrain, climatology, and fixed historical context retain their own limitations.
Station inventory is metadata, and thermal points are not confirmed wildfires.
A changed date clears the old feature selection so its drawer/AI binding cannot
follow a different day. Provider errors do not reuse another day's features.

Compare pins A and switches the main map between the two checked dates. The
existing approved Earth Engine comparison remains available for same-product
imagery swipe; its ownership, integrity, rights, pair-compatibility, and tile
validation are unchanged. No image differences or causal conclusions are inferred.

The calendar cursor, range, step, and A/B pin are retained in the existing
same-tab history/share parameters. Invalid, oversized, future, and reversed input
is rejected. This does not extend the report/story schema with a daily axis;
those workflows retain their existing annual catalog fields and source metadata.
Advanced atlas modes, original preview/commit controls, and interpretation remain
available in the expandable atlas section.

## Placement and review

Directory Rules §§3–4 assign deployable UI and its adapters to the application
responsibility root. This is the existing standalone GoDaddy composition: code
stays in app/, delivery artwork in public/, regressions in tests/, and explanation
in docs/. Per docs/history-comparison.md, these correspond to apps/site/source/
responsibilities in the governed mirror (ADR-0029); that mirror is not edited.
No schema, policy, registry, source-admission, receipt, or release home is added.
The artwork is generated interface decoration, not dataset evidence. Small SVG
transport icons are unmodified Phosphor Icons core 2.1.1 assets with its MIT license.

Rollback: revert this candidate's UI, calendar helper, artwork, tests, and docs as
one unit. No database, released data, runtime bindings, model configuration, or
hosting settings are changed. No production publication is authorized by the PR.

Validation: record exact executed results and browser acceptance in the PR and
docs/compact-calendar-time-sweep-qa.md (the durable copy of the local root design-qa.md). Builds and unit checks do not prove hover, mobile, rendered
animation quality, or live provider behavior.

2026-10-22 follow-up: the map stage cannot scroll during control focus; phone attribution clears the time row, and short-window settings retain their header below the toolbar. See docs/explorer-controls-ai-polish-qa-20261021.md for current browser evidence and the separate CI/publication hold.
