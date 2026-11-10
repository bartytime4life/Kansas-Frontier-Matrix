# Saved investigations and evidence scope

This bounded correction starts at PR #5792 head
`05642be1bced8cfbd4bd1ab03e5c83dcc0c2e41f`. It preserves the standalone Site,
existing review holds and device-local drafts while correcting reproduced source
and interface failures. The PR is stacked while its predecessor remains open.

## Confirmed problems and corrections

| Surface | Reproduced problem | Resulting behaviour |
|---|---|---|
| New stories | Four retired demonstration references failed the existing storage validator; the editor nevertheless said saved, then discarded prose on restore | Start from the actual captured map with available references; validate before writing and disclose failed local saves |
| Report and story switching | A valid independent story was rejected because its snapshot differed from the report; switching tabs overwrote its saved prose | Restore both drafts independently; explicit creation from the map replaces only the requested draft |
| Gauge-height history | The station route trusted the provider's datetime filter and accepted older/future samples; the drawer then labelled them latest | Validate exact observation instants against the inclusive requested window before projection; independently validate drawer clocks and scope |
| Selected gauge read | Stalled headers or body never completed; errors had no local retry | Bound the whole read to fifteen seconds; keep recovery available and suppress abandoned or superseded results |
| Earthquake and storm exports | Month-only checks admitted wrong-year and impossible-date rows | Require each contract's valid calendar date and matching metadata/evidence year before enabling export |
| Keyboard aviation inspection | Inspect map center removed the focused button and left focus on the document body | Move keyboard focus into the corresponding completed inspector, including a finished side view |

Storage keys and strict snapshot, evidence and privacy validators remain. The
story creator does not fabricate evidence or resurrect retired demonstrations.
Source time checks preserve true zero, nulls and valid inclusive endpoints;
invalid station responses use the existing unavailable response. This change does
not establish measurement-unit completeness or scientific/provider accuracy.

## Validation

Final production build and containment checks, TypeScript and all **1,652 Site
tests** pass. Lint reports zero errors and the same 77 inherited warnings.
Water-conformance passes **372 tests**, including **71 mirror regressions**.
Strict inventory covers **927 files** with all **262 withheld paths absent**.
Disposable backend smoke passes **110 checks across 79 routes**; 14 provider-only
routes remain outside that offline check. Its run preceded the final aviation-only
source correction; no backend source changed afterward.

Independent reviews cover strict timestamp/offset precision, date/year exports,
workspace identity and persistence, and both UI lifecycles. The first full run
caught outdated mirror totals and an older direct-handler fixture without a React
event; both fixtures were updated, preserving their behavioural assertions. A
separate independent review found that invalid aviation side-view B removed its
control. The correction retains A and B, including repeated map clicks, and
checks listener cleanup on success, Escape, cancellation, hiding and unmounting.
The final complete Site and water runs pass after these changes.

Actual built-app browser checks:

1. **Story resume — pass.** The baseline said Saved on this device, then lost
   labelled synthetic prose on reload. The corrected app retains that prose after
   reload and Reports → Stories switching. The new scene reflects the captured map
   instead of retired synthetic evidence. Component fixtures additionally cover
   independent A/B snapshots, explicit new-from-map, exports and denied storage.
2. **Gauge recovery — pass with synthetic response.** A labelled loopback proxy
   supplies one synthetic discharge marker and stalls only its separate gauge-height
   body. The baseline stays loading beyond a minute. The corrected check times out;
   Enter on Retry accepts a valid in-window synthetic sample and retains focus as
   the same button becomes Refresh. The proxy blocks application writes. These
   readings are fixtures, not USGS measurements. The accepted recovery screenshot
   shows the stage card; earlier context captures above that card do not themselves
   prove the timeout message. The inspected DOM supplies that before/timeout proof.
3. **Aviation keyboard — pass.** Layers → aviation → enable → expand controls →
   Pick a point → Enter on Inspect map center focuses the new matching inspector.
   Side view → center A → same center B keeps the distinct-points error and B focus.
   Focusing the map, using its Right arrow, then Enter on B focuses the completed
   cross-section region. The baseline instead left focus on BODY after inspection.

Screenshots were saved and inspected outside Git. The gauge and story browser
checks used the first corrected build; the final build changed only aviation's
invalid-B path, whose point, error and corrected-result paths were then rechecked.
One preview navigation attempted before server readiness left a connection-error
tab; a fresh tab after readiness completed the final flow. Provider context and
basemap availability vary; these UI checks do not qualify external services,
private authentication, full WCAG/assistive-technology coverage or production.

No dependency, schema, access, operational store, source activation, admission,
release, merge, deployment or publication change is included. The original dirty
owner checkout is preserved.

## Inventory and rollback

The append-only `site-v268-evidence-workspaces-overlay-20261109.json` successor
inherits its predecessor's source identity, withheld inventory and review holds.
Authority remains CONTENT_PARITY_ONLY, status REVIEW_ONLY, source/overlay review
pending, human acceptance and hosted equivalence false. Site identity remains an
inherited declaration without fresh hosted-source readback.

Undo through a focused inverse commit or reviewed forward correction. Revert the
successor and selector together, preserving every historical receipt and withheld
carrier. Device-local user prose is not migrated or deleted by this source patch.
