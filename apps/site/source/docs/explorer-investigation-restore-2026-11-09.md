# Investigation restore and observation-time integrity

This bounded correction starts at PR #5793 head
`7fdd160adb38ccaceeb6d625b9b26a8cc46486e1`. It extends the existing standalone
Site without changing its identity, providers, authority or publication holds.

## Confirmed problems and corrections

| Surface | Reproduced problem | Resulting behaviour |
|---|---|---|
| Saved Places | Public source visibility, opacity, archive days and terrain provider were omitted; restoring A retained B's settings while announcing success | New records retain validated public source preferences and committed days; older records disclose their incomplete source settings |
| Smoke playback at Place restore | A late publication request or in-flight map upload could overwrite the restored smoke day | Synchronously cancel playback and transfer frame ownership; abandoned commits, rollbacks and fades cannot modify the restored source |
| Restore before map readiness | A loaded Place's camera was not queued for the map constructor | Queue the safe saved camera for initialization as well as restoring a ready map |
| Places layer counts | Registry-only totals showed zero layers while public layers were selected | Count public and registry selections truthfully without claiming successful loading or verified evidence |
| Report/story preview | A stalled map adapter or style remained loading indefinitely, without recovery; later load could erase an error | Bound readiness to fifteen seconds, retain errors until a new successful attempt, provide enabled recovery and ignore abandoned callbacks |
| Terrain preview | Saved 72-degree terrain pitch was clamped to 60 degrees | Retain the Explorer's 72-degree terrain capability while preserving the ordinary 60-degree preview bound |
| Latest reviewed water reading | Lexical sorting put a whole-second timestamp before a newer fractional reading | Compare exact accepted microsecond instants |
| Shared reviewed release clock | Millisecond rounding admitted a release still one microsecond in the future | Apply existing exact microsecond comparisons to creation, review, release, current time and expiry |

No cached measurement rows become saved evidence. Location-derived cameras retain
the generalized Kansas fallback; existing private/research/subsurface validators
and public source/date guards remain. Restoring preferences performs the existing
bounded source checks, not admission or operational activation. Old saved Places
cannot reconstruct fields they never recorded.

## Validation

Final Site build/containment, TypeScript and 1,696 Site tests pass. Lint has
zero errors and 77 inherited warnings. Disposable backend smoke passes 110 checks
across 79 routes, with 14 provider-only routes unexercised. Exact-clock parity
matches 21 cases in the actual Python policy runtime. Independent reviews cover
water selection/release ordering, preview teardown/readiness and saved Place
privacy, camera construction and HMS download/upload/timer handoff.

Actual final built-app browser restores a new September 20 Place after changing
to September 21 and hiding earthquakes: the layer returns selected with its
September 20 source clock. The valid public response has zero returned records;
no event frame is invented. The new save records six selected layers; the
untouched older record explicitly lacks public source/date/DEM settings.

The labelled local synthetic-style rehearsal reaches a finite preview timeout
with an enabled Retry action. Enter on Retry recovers saved map context, retains
keyboard focus as the action becomes Refresh, and keeps the provider-overlay
non-replay caveat. Accepted before/after screenshots stay outside the repository.
The successor receipt records the final water-conformance and strict mirror
results; GitHub metadata is authoritative for submitted-head CI.
Baseline built-app browser evidence reproduced a September 20 saved Place
reopening with hidden September 21 earthquake context despite its restored notice.
It also shows zero recorded layers next to six public selections. A labelled
loopback fixture stalls only subsequent synthetic map styles; the old report
preview remains loading without a recovery action. Source and browser fixtures
are not provider, private-authentication or production acceptance evidence.

## Inventory and rollback

The append-only `site-v268-investigation-restore-overlay-20261109.json` successor
binds fifteen changed Site paths, including two additions, and retains every
predecessor, source-identity declaration, withheld carrier and review hold.
Authority remains CONTENT_PARITY_ONLY, status REVIEW_ONLY;
source/overlay review pending, human acceptance and hosted equivalence false.
Historical Site identity is an inherited declaration, without hosted readback.

The owner checkout stays untouched. No dependency, schema, access, operational
store, admission, release authority, merge, deployment or publication change.
Undo with a focused inverse commit or reviewed forward correction; revert the
successor and selector together, preserving all historical receipts and withheld
paths. Device-local saved work is not bulk-migrated or deleted by this patch.
