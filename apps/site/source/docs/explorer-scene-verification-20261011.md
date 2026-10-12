# Scene reliability and presentation verification — 2026-10-11

## Authority and preservation

The authoritative source was opened through the Sites source workflow for
`appgprj_6aa0b1c41bc08191bfd86003920f1631`. The opening commit was
`225c67e8fca9bbdafc8397da9eaacfcaec7a59db`, matching deployed owner-private
Site v229. Deployment `appgdep_6acbd3d112dc8191ae125e4ef0379e64` read back
`succeeded`. GitHub main and its `apps/site/source` mirror are integration
context, not replacement authority. The Notion and Drive Kansas-first roadmap
was read as supporting guidance; its older version pins retain their dates.

Before publication, the same Site advanced to v230, source
`1c04b3c08201fdce68bc49d2b51674e812d34127`, deployment
`appgdep_6acbeb44d7288191bc54121965623bef` (`succeeded`). A fresh source-helper
checkout retained that update's governed-water validation changes. This patch
applied cleanly; the original candidate and its preview state were preserved.

This patch changes presentation, river-display accounting, queue preparation
and browser-location redaction in reports and newly saved workspaces.
It does not change source payloads, acquisition budgets, admission, activation,
DB/BUCKET bindings, audience, persisted preference keys or existing data.
Original local services on ports 4173 and 4175 were retained. A fresh checkout,
isolated simulator state and origin on port 4176 were used for verification.

## Reproduced problems and changes

- Off effects still said “Shows in this view.” Cards now distinguish Off,
  Battery saver pause, waiting for the map, supported views, night-sky conditions
  and direction-only water motion. Stable switch names retain source and status
  descriptions through `aria-describedby`. Whole-card dimming is removed so
  inactive controls remain readable; card borders and status chips separate
  preference, reading and availability without promising successful rendering.
- River geometry stopped at 60,000 segments but its count included reaches
  that were not drawn. Counts now describe represented reaches and gauge cues,
  retain the loaded reach count, and explicitly disclose omitted geometry as
  partial coverage. A synthetic 400-reach/200,000-segment case reports 120
  represented reaches and no cue for a gauge on omitted geometry.
- Gauge-only changes could update geometry without notifying status listeners:
  metrics were mutated before equality comparison. Status now commits once,
  after computing the new metrics. The real sourcedata callback regression
  verifies notification when the gauge layer is hidden with cells unchanged.
- Nearest-first terrain ordering recalculated two distances on every comparator
  call. Distances are now computed once per vertex; order is byte-identical in
  the benchmark fixture. Geometry, source coordinates and sample budgets stay
  unchanged.
- Custom reports withheld a private browser-location camera but still included
  exact viewport bounds, analysis bounds and point measurement labels. Reports
  now apply the immediate state/ref privacy guard to those fields and coordinate
  metadata. New private workspaces omit analysis bounds. Existing saved data is
  preserved. Two regression tests execute the actual report builder with
  synthetic coordinates, checking both private guards and normal exports.
- Historical-map search captured a private center while requests were held;
  clearing privacy could later send that retained center to USGS. The initializer
  now avoids reading a private camera and retains only the generalized Kansas
  fallback. Actual initializer/request-effect tests cover the held-to-cleared
  transition and deliberate public-center searches.
- The final phone check caught a more-specific inherited CSS dimming rule.
  Its override now matches that selector, and status-chip selectors preserve
  readable colors. Browser computed opacity is 1 for all seven effect cards.

## Measured performance

Command: `node --test tests/water-flow-motion.test.mjs` (also in the full suite).
Synthetic deterministic 60,000-vertex queue, seven alternating before/after
runs after an ordering check, Node v22.13.1 on Linux x64. Median baseline 62.76 ms;
candidate 15.32 ms, about 76% less time. Distance calculations per ordering:
1,743,986 versus 60,000. Exact ordering was asserted. Timings vary with host
load. These results measure queue preparation, not real-provider latency,
end-to-end startup, frame rate, memory retention or mobile hardware performance.

## Local checks and browser observations

Production build, TypeScript and changed-file ESLint checks passed. The full
application suite passed 1,030 tests on the original candidate. The reconciled
v230 candidate passed 1,050 tests after its production build, plus TypeScript
and changed-file ESLint (zero errors; inherited warnings remain).
The final follow-up candidate passed 1,052 tests after rebuilding, plus TypeScript
and historical-control ESLint. No errors were recorded in the browser console.
Existing reduced-motion, hidden-tab,
Battery saver and bounded repaint regressions remain in that suite.

Chrome extension-controlled browser on the Linux workstation, measured desktop
viewport 1258 × 1323 CSS pixels. Actual CSS sizes were measured rather than
inferred from viewport overrides. Phone
checks used measured 390 × 844 and 320 × 640 CSS pixels. Both matched their
document scroll widths, with the Scene sheet inside the viewport. Keyboard
Space toggled water; Escape closed the panel and returned focus to its trigger.

The High Plains Underground example loaded 50 eligible records, 28 plotted
columns and one aquifer overlap with explicit partial coverage. Detail reached
2048 × 1752 pixels at zoom 13.5. A Through-2000 record update retained the
high-detail surface while overlays loaded. Returning to the map showed 1,274
USGS-directed reaches with partial provider coverage, not a measured velocity
or complete wet-channel inventory. Source dates and values were not changed.

## Remaining qualification

Independent static review covered all 362 app paths: 357 were fully read,
including all 330 implementation/type files; five large CSS/JSON assets received
structural resource/schema review with their consuming controls fully read.
The concurrent v230 governed-water delta was reviewed separately. Two confirmed
location privacy defects were repaired and covered by synthetic regressions.
This is a bounded source audit, not a whole-system security clearance.
Real GPS access was not requested in browser verification.
Hosted dispatch behavior, external
companion services and dependency-native parsers need their own evidence.
Real reduced-motion device settings, screen-reader use, touch hardware,
WebGL loss, long-session cleanup and end-to-end cold/warm performance have
not been established by these checks. This record does not claim GitHub
integration, mirror review, user acceptance or governed-data admission.

Rollback: revert this narrow source patch or deploy the existing saved v230
to the same project. No storage migration or settings reset is needed.
