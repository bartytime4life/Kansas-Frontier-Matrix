# Mobile layer recovery and keyboard checks — 2026-10-11

Authoritative starting point: owner-private Kansas Frontier Matrix Explorer,
project `appgprj_6aa0b1c41bc08191bfd86003920f1631`, deployed v243 at
`fdec96cd545a1eb3a51992bf07b4540d4feccf8a`. This includes v242's lossless River
Pulse transport and the concurrent v243 guide change. The task worktree and
earlier experiment artifacts remain intact. Audience, DB/BUCKET, source assets,
provider limits, eligibility and admission boundaries are unchanged.

## Reproduced defects and repairs

In hosted Chrome, mobile Layers declared `aria-modal=true` but the header and
map remained actionable. Opening the header Map menu while Layers was open
reproduced background input. The compact left panel now isolates its background
within `.site-root`, hides that background from accessibility navigation, and
keeps focus inside. Cleanup restores exact previous inert/ARIA values. Desktop
panels retain their existing behavior. Close/Escape returns to the explicit
Layers/Places opener; closed menu buttons return to their visible summary,
with the map as fallback for absent or disconnected triggers.

An injected historical request failure showed Unavailable, withheld readings,
and exposed Retry correctly. However, Retry silently requested the current
network and discarded 2024-09-02. Retry, ordinary refresh and hide/show after a
failed read now use the committed station/day owner. The day is read at action
time, separately from the editable draft. Archives always request the 24-hour
station window, even if the previous successful range was longer. Existing
abort, coalescing and generation checks remain in the actual loader.

Source tracing also found that tab history omitted the selected River Pulse
archive day. The existing history projection now retains optional `hydroDay`,
station, range and exact frame while the layer is hidden. Restoration validates
calendar day, adapter floor, current UTC day and station identity before using
that owner. Current network clears the archive key. Embedded history remains
untouched. This is display context, not provider data persistence or admission.

## Reproducible browser measurements

Native Chrome 154 on the same Linux workstation. Hosted baseline was inspected
at 390 × 844 CSS pixels. Local production browser tests use the same locked
dependencies; an external QA proxy injects PerformanceObserver/rAF metrics.
No QA code is included in Site source or deployment assets. Existing localhost
zoom is 150%; viewport overrides are adjusted to verify actual CSS dimensions
without changing that preference. The first 260 × 563 sample is retained and
not mislabeled as 390 × 844. The corrected narrow sample is 320 × 568 CSS pixels.

| Observation | Measured result |
|---|---|
| Hosted baseline modal background | Header Map menu opened behind Layers |
| Patched compact panel | Background inert; Tab wrap remains within dialog |
| Narrow map width | 320 CSS pixels; document scroll width 320 |
| Visible layer controls | 44 px minimum target height; toggle 44 × 44 |
| Three repeated keyboard open/Escape cycles | No stuck input; opener regained focus |
| Six rapid county toggles | Five selected layers retained; one map canvas |
| Counties opacity Home/End | Exact 0%/100% native slider controls |
| River Pulse Home/End with overlapping counties | Exact first/last source frames; selected station retained |
| Five-second 320 × 568 navigation sample | rAF p50/p95 33.4/66.7 ms; max 66.8 ms |
| Long tasks within that five-second sample | 0 |
| EventTiming entries within sample | p50/p95 80/120 ms; max 120 ms |
| Injected historical HTTP 503 | 502.7 ms browser resource; no archive point displayed |

rAF measures callback cadence, not GPU FPS. EventTiming entries are not a
deduplicated INP metric. There is no measured rendering-speed improvement claim.
The full session includes startup tasks and an intentionally retained earlier
oversized/zoomed QA overlay; those are not used as acceptance targets. Preview
and proxy processes stopped during export; they were restarted and the complete
metrics snapshot was retained. A rendered cached map is not proof that its
server remains reachable. Only explicit failure-injection records count as
controlled network failure evidence.

Raw browser exports, proxy events, failure states, callback before/after
arguments, build/test output and reproducible harness files are retained outside
application source under the task's `.layer-system-work/mobile-accessibility-evidence/`.
Run the actual production build with Vite preview on 4196 and the QA proxy on
4195. Use QA fail requests, select Ellsworth USGS-06864500, set/check 2024-09-02,
then restore QA normal network and Retry layer. Verify the station/day, exact
frame and map status. Hide/show and reload must retain that same owner. Verify
date input and derived archive link after a native key because CUA fill alone
can update the DOM without committing React's date state.

## Verification boundary

Focused tests execute the actual panel effect, retry/show callbacks and history
projection. They test prior inert state restoration, closed/disconnected
openers, other tool/workspace ownership, committed versus draft day, warm
hide/show, invalid restored dates, missing stations and explicit Current.
Final build, TypeScript/full-test counts and deployed browser acceptance are
recorded in the task receipt rather than inferred from this source document.

Physical touch devices, screen-reader speech, OS reduced-motion emulation and
GPU performance are not certified. The available browser capability supports
viewport changes but does not expose media-preference emulation. Existing
reduced-motion guards and exact-frame alternatives remain intact; source/unit
coverage does not replace testing an actual reduced-motion browser preference.
No GitHub merge, mirror waiver, source admission or owner acceptance is implied.
