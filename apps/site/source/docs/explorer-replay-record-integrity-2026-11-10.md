# Observatory inspection follows committed replay records

This bounded pass starts at main
`028ffa0870068741c5594c716ae2b21ea22955f3`, which includes the previous Explorer
improvements. It preserves the standalone Site, source identities, lifecycle
boundaries and publication holds.

## Reproduction and correction

In the verified base build, selecting a synthetic weather station at May 19,
1900 23:00 UTC shows its 70°F daily maximum. Advancing one hour commits May 20
and loads that day's synthetic 99°F record, but the inspector still shows the
clicked May 19 record and 70°F. This is native-browser evidence using labelled
synthetic output from the actual weather route, not provider observations.

The selection now supplies identity only. Its displayed properties come from
the records that completed the current map frame. Loading, missing, hidden and
ambiguous records receive explicit states, with no clicked-value fallback.
A station can follow its current daily record and safely rewind without another
click. River readings keep the current sample's units, quality and timestamp;
true zero remains a reading and missing frames remain missing. Earthquake and
station-epoch identity, independent Census editions and exact storm-volume
identity retain their existing scope. Reused storm IDs do not authorize a new
scan to replace the selected observation.

The frame's readiness gate now includes enabled weather, county, earthquake and
Shake GeoJSON sources. It keeps the existing fifteen-second budget and
cancellation/generation protection. The inspection snapshot is invalidated when
a new frame starts and published only after the readiness gate. Clipboard
fallback messages do not invalidate an otherwise committed observation.

## Verification

Final Site build/containment, nonincremental TypeScript and **1,754 Site tests
pass**. Lint has **zero errors and 77 inherited warnings**. Disposable backend
smoke passes **110 checks across 79 routes**; fourteen provider-only routes are
unexercised. The bounded water-conformance suite passes **376 checks**, including
**75 mirror regressions**. Strict inventory contains **939 files**, with all
**262 withheld carriers absent**.
Focused regressions execute the actual complete frame effect, selection
expression and record/status JSX with provider transport denied. They exercise
midnight transitions, delayed and failed sources, deadlines, A-to-B-to-A,
missing/hidden/ambiguous selections, all source families and genuine zero.

Final built-app browser steps:

1. **Select station — healthy.** At May 19 23:00 UTC the selected station shows
   its synthetic May 19 maximum of 70°F.
2. **Advance one hour — corrected.** At May 20 00:00 UTC the same selection now
   shows the synthetic May 20 maximum of 99°F and its matching date. The base
   build retained the prior 70°F record.
3. **Rewind — healthy.** Returning to May 19 restores 70°F and its May 19 date,
   without another feature click.

The current screenshots were saved, opened and visually inspected. External
regression controls remove context-source readiness and inspection publication
in disposable copies of the actual test input; both produce expected failures.
No repository source is mutated for these controls. This checks that the new
regressions detect both omitted guards, rather than just mirroring helper output.

The synthetic browser rehearsal uses a GET/HEAD-only local proxy, blocks other
application APIs and external provider transport, and labels every page and
station. Screenshots and logs remain outside Git. Temporary tabs and verification servers
are closed after acceptance; no viewport override was applied. Local proof does not establish
provider coverage, complete accessibility/device qualification, hosted acceptance
or submitted-head CI.

## Inventory and rollback

The append-only `site-v268-replay-record-integrity-overlay-20261110.json`
successor binds four changed Site paths and three additions. Historical receipts,
source identity, review and overlay declarations, and all 262 withheld carriers
remain unchanged. Authority remains CONTENT_PARITY_ONLY, status REVIEW_ONLY;
source/overlay review is pending, human acceptance and hosted equivalence false.

Revert the successor and selector together or apply a reviewed forward fix.
Preserve historical receipts and withheld paths. The owner checkout remains
untouched. No dependency, operational store, access, source activation, admission,
release, merge, deployment or publication change is included.
