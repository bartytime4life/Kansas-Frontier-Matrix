# Site v252 mirror and review-image repair

This candidate starts from main `62479504bba719ca5da066b93febb8e37ab3faf8`.
Current-main water conformance rejected seven files whose bytes no longer
matched the selected v251 receipt: README, five Qwen scripts and the Qwen
knowledge test. The older receipt remains unchanged. This follow-up selects
an append-only receipt generated from the actual current mirror and exact
owner-private Site v252 source `190d16acb2f866cb9c2eb108dbd204ca30465269`.

## Reconciliation and boundaries

The authoritative v252 archive-authorization changes are copied exactly into
the mirror. They overlap eleven Site paths in open #5088; no obsolete receipt,
selector or approval from that PR is imported. The dependent smoke checks are
aligned with v252 owner authorization as described below.
Existing Qwen, companion-session, governed water/weather/soil/storm-event/
earthquake and release overlays remain in the repository. No file is deleted.
The receipt records 953 identical application paths, 29 inherited overlays,
67 repository-only paths and two canonical tool mappings. No Site path is
missing. Content parity does not approve the receipt or establish deployment
of repository-only overlays, data admission, activation or hosted equivalence.

Source geometry, public data, aquifer/Underground renderer, 2048/4096 detail,
units, source time and uncertainty semantics are unchanged. Site v252 remains
owner-only with the same project and DB/BUCKET declarations, deployment
`appgdep_6acc55fe0bb08191b36cbde3d61c1986`, environment revision 6. This follow-up
neither edits nor republishes its authoritative source or runtime settings.

## Container repair

The failing image is the application-free security-review placeholder, not a
running API or Site deployment. The reported packages are bundled inside pip;
the current PyPI pip wheel still names the reported versions in vendor.txt.
The top-level setuptools lock therefore does not repair those bundled copies.
After the hash-locked build-tool installation, remove pip and ensurepip's
bundled wheel from the final filesystem. The build checks both installers are
absent and that the locked setuptools/wheel/packaging versions remain installed.
Non-root execution, digest-pinned base, OS repair floors and the existing
HIGH/CRITICAL vulnerability/secret failure policy remain intact.

Pip remains a build-time bootstrap input. This final-image repair does not
claim every build-time dependency or historical image layer was remediated.
No scan ignore, severity reduction or baseline waiver is used. Local Docker
could not resolve the registry, so an actual hosted image build and the existing
Trivy scan are required before calling container verification complete.

## Validation and recovery

Standalone v252: build, TypeScript and 1,138 tests pass. Composed mirror: build,
TypeScript and 1,196 tests pass. Both lint runs have zero errors and 66 existing
warnings. Current-source parity, Python checks, browser and exact-head hosted
CI outcomes are recorded separately in the new receipt and accompanying PR.
No fresh exhaustive Site security scan or broad physical-device acceptance
is asserted.

The local copy uses a fresh v252 folder through the existing current alias and
port 4173 service. All 984 tracked source files and prepared build files are
checksum verified. The v251 folder and earlier recovery copies remain in place;
old immutable client assets are retained for open tabs. The v109 persisted
store is retained without a migration, reseed, capture or data activation.
Rollback points the alias back to v251 and restarts the existing service using
that store. Repository rollback reverts this follow-up and its selector;
container rollback reverts the Docker change and rebuilds the previous review
image. These operations do not roll back a governed data release.

Placement follows adopted Directory Rules v2 / ADR-0029: application mirror
under apps/site/source, exposure/build-image configuration under infra/docker,
review documentation under docs/reports and immutable recorded comparison
under data/receipts/generated, consumed by existing tools/qa/site_mirror.py.


Fresh installed-local browser verification rendered 50 records, 28 plotted
columns, one aquifer region and a complete 2048 × 1718 surface at zoom 13.4.
Partial coverage and one withheld unbounded class remain visible. No captured
console warnings or errors were returned. A bounded anonymous archive GET
returns 401, preserving v252 authorization rather than serving private content.
Twenty-three mirror/infra Python checks pass. The topology ratchet passes with
zero new drift/invariants and 93 inherited warnings; its baseline is unchanged.
The local copy includes 428 prepared build files and 44 retained prior assets.
Actual container repair verification remains the hosted exact-head scan.


Hosted Site CI initially failed only the local Worker smoke: the old script
expected an anonymous archive GET to return an empty catalog (200) and POST to
return its old CSRF denial (403). v252 denies both before storage access (401).
The script now requires that status and the explicit owner-access error text.
This repairs the dependent test rather than weakening archive authorization.
The actual hosted image build/scan and water conformance already passed at
head ac9ecf2891542c9475cf2ac76a490cb9eab1fd39; final-head execution is separate.


The isolated local Worker smoke passes all 103 checks across 74 routes after
the expectation fix (port 4189, fresh empty test store, no operator-store changes).
Owner merged #5097 at ac9ecf2891542c9475cf2ac76a490cb9eab1fd39 while that
fix was being pushed. That exact head had 108 successes, two skipped and one
Site smoke failure; do not call it fully passing. Its image build, container
scan, security-result and water-conformance passed. The small follow-up retains
that merge and updates only the dependent smoke expectations and this evidence.
Final follow-up CI execution is separate from the earlier successful scans.

## Completed main CI and v252 browser verification

Fresh readback on 2026-10-12 confirmed owner-merged #5098 at
`50073291154da2c461b5a053c9b78028868debc2`, merged main
`3ec5f0d9640a88117ff45ae31d3347609b165e67`. Main completed **104 successful
checks and two skipped**, with no failures or unfinished checks. The earlier
#5097 smoke failure remains historical; it is not rewritten as a pass.

The authoritative Site still reports saved v252 source
`190d16acb2f866cb9c2eb108dbd204ca30465269`, successfully deployed as
`appgdep_6acc55fe0bb08191b36cbde3d61c1986`, environment revision 6. Access
remains one owner, no editors/groups/external visitors. This verification did
not edit, save another version, or republish the Site.

Executed local and owner-private hosted browser observations ran from
16:50:41 to 17:03:05 UTC, about **12.4 minutes**, with interaction interleaved
across the installed local tab, a temporary local tab and a temporary hosted
tab. This is a bounded session, not a multi-hour endurance or continuous-load
test. [Machine observations](../../data/receipts/generated/site-v252-underground-browser-checks-20261012.json)
retain the checkpoints and source identities; they carry no human acceptance
or data-release authority.

| Executed check | Observed behavior |
| --- | --- |
| Matching High Plains area | Both views restored 50 records, 28 plotted columns and one aquifer range; partial coverage and one unbounded/missing class withheld remained explicit. These are UI observations, not an independent audit of all provider records. |
| High and Maximum detail | Local and hosted surfaces completed at 2048 × 1718 and 4096 × 3437 in the initial selected extent. Narrow 390 × 844 views completed at 2048 × 2011 and 4096 × 4022; dimensions follow the selected geographic aspect ratio. |
| Existing efficiency mode | The installed local view already used Battery saver. Hosted Battery saver also completed the independently selected 4096 × 4022 surface. Its original High detail preference was restored afterward. This is not hardware CPU/GPU/network throttling. |
| Time filtering | 1976 showed one record/column; 2000 showed 17 records/11 columns; All loaded records restored 50/28 in the matching area. Aquifer ranges retained their separate 2022–2024 source clock. |
| Playback | Hosted playback stopped at the final 2019 record year. Local pause held 2018 and 49 records through a later checkpoint; All loaded records restored 50 afterward. Record availability does not reconstruct historical groundwater or geology. |
| Navigation and display | Top and Reset operated by keyboard; canvas arrow pan/modified-arrow orbit inputs and Reset were exercised. Surface-map/cutaway round trips restored the recorded view. Opacity 0/100/65 and Exact pixels toggling preserved record counts. |
| Scope changes | Local rapid selector zoom in/out and hosted zoom in settled with complete surfaces and partial-coverage labels. The smaller hosted extent showed 27 plotted columns/50 records; coverage changes were not presented as lost or fabricated data. |
| Record and aquifer inspection | WWC5 312847 showed 2000-05-12, ten intervals, feet/land-surface reference, PLSS location approximation and its KGS link. Aquifer legend identified possible outer depth ranges, depth clipping, generalization and withheld open-ended classes, without a filled-reservoir claim. |
| Teardown and focus | Local and hosted repeated closure returned from five canvases to three; restored area views returned to five. Entry focused Close Underground; explicit closure focused the map. Surface-map mode used four canvases. Counts did not accumulate at the recorded checkpoints; this does not prove zero heap/GPU leakage. |
| Responsive and logs | Recorded 390-pixel views had no document horizontal overflow. Captured warning/error logs were empty for all three tabs at final readback. Some automation locator/CDP calls reached short deadlines despite a subsequently visible completed view; these are recorded tool limits, not source-data defects or timing benchmarks. |

No reproducible Underground application defect was established, so no renderer,
geometry, source asset, native value, interpretation, request limit, or detail
control was changed. The user's original local tab remains open with its
2048 detail, 65% opacity and WWC5 465949 selection restored. Temporary tabs
were closed and the temporary viewport override reset. Ordinary display tile
cache activity occurred through the existing browser path; no source admission,
governed acquisition job, store migration, archive write or data activation ran.

Final file verification found **984 source paths and 428 prepared build files**
identical between the authoritative local v252 checkout and installed PC copy.
Both source checkouts and primary PC main were clean. Primary main and remote
main matched `3ec5f0d…`. Local `/about` returned 200, the served aquifer asset
matched disk, and anonymous `/api/daily-archive` remained 401. The existing
mirror check passed CONTENT_PARITY_ONLY with 953 identical paths, 29 inherited
overlays and 67 repository-only paths; the selected receipt and its pending
review/human-acceptance gates were unchanged. Repository-only overlays are not
claimed deployed to v252.

Remaining checks are physical devices and assistive technology, live reduced-
motion emulation, heap/GPU profiling, fully cold network, multi-hour soak and
hosted rollback. This browser matrix does not establish comprehensive hosted
equivalence, certify every provider's accuracy, or replace source/evidence review.
The prior tests/builds/security scans remain dated evidence; none was relabeled
as newly executed by this browser-only follow-up.

This append and observational JSON use the existing docs/report and data/receipt
responsibilities under adopted Directory Rules v2 / ADR-0029, without adding a
new authority root or generated writer. Removing this appended section and its
observation file reverses the documentation change; application rollback remains
the retained v251 copy and existing persistent store described above. No rollback
was invoked during these checks.
