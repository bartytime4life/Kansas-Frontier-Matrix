# Underground browser endurance and current-Site reconciliation

Review evidence, 2026-10-11 (America/Chicago). This report records executed
browser checks and a repository mirror candidate. It does not admit sources,
activate data, approve the mirror receipt, or establish comprehensive device
acceptance.

## Pinned identities and preservation

- Authoritative owner-private Site: v246, source
  `7f3f89e9b181f213ce3a32080cc1c4cdda672f52`.
- Saved version:
  `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_696cc1170b188191a7d1248360c71f0d`.
- Successful deployment: `appgdep_6acc24279f1481918759bdbba682ac9d`;
  one owner, no editors or external visitors, environment revision 5.
- Initial repository base: `e960d6d47e5c43813b25e7aa6f1a9c7100469e89`.
  Main advanced to `9196163527b79787192d04b163e29b40ec5c5221` during
  validation; its six non-Site files were merged without conflict. The Site
  application content and its successful browser/build checks did not change.
- The primary PC repository was fast-forwarded from merged #5029 to that main
  commit with a clean checkout. Other worktrees were preserved.
- The PC Site was updated to `KFM-Explorer-Site-browser-checked-20261011-v246` through
  its existing current-version alias and existing port 4173 service. All 954
  tracked source paths and 427 build files match the authoritative checkout.
- The v229 folder and the existing v109 persistent store remain recoverable.
  Source schema files match the prior installed application; no migration,
  source admission, package activation, or access change was performed.

## Executed browser matrix

The recorded session ran from 19:10:27 to 19:27:48 CDT (17.36 minutes), with
interactions interleaved across the hosted application, an isolated current
local build, the installed local service, and a composed repository build.
This was ordinary browser interaction, not continuous maximum-load saturation.

| Check | Observed result |
| --- | --- |
| High Plains selection | 50 records, 28 plotted columns, one aquifer overlap region; partial coverage and unbounded-class withholding remain explicit. |
| Rapid record-year changes | Four hosted and five local timeline/surface round trips restored the same full-record view. |
| Narrow Battery saver | 390 × 844 viewport, no document horizontal overflow; source counts and independent time/coverage labels preserved. |
| Detail choices | Complete 2048 × 1718 desktop and 2048 × 2011 narrow-area surfaces; Maximum produced 4096 × 4022 for that same narrow selection. Aspect ratio follows the selected extent. |
| Navigation | Keyboard Top/Reset controls worked; selector zoom changes completed with new surface zoom and source-coverage labels. |
| Record playback | Playback advanced through supported dated records and stopped at the final 2019 record year. All-loaded-records selection remained available. |
| Teardown | Five canvases with the cutaway active, three after closure, five after restoration; no accumulating canvas count in the recorded view round trips. |
| Record inspection | WWC5 312847 retained 2000-05-12, ten intervals, feet and land-surface reference, PLSS location approximation, and its official KGS link. |
| Composed repository build | Real map journey restored 50 records, 28 columns, one aquifer range, and a complete 2048 × 1718 surface. |
| Console observations | No error or warning entries were returned at the recorded checkpoints. |

The well's KGS NAD83-to-WGS84 display approximation remains labeled EPSG:1188
(4 m), without a verified trajectory or common elevation registration.
Aquifer source years remain separate from record filtering; record playback
does not reconstruct historical groundwater occupancy.

No reproducible Underground application defect was found in this matrix, so
the Underground renderer, record semantics, native-value handling, and source
assets were not changed. Initial transient browser locator deadlines were
resolved by inspecting the actual settled DOM and using visible pointer or
keyboard controls. They are not counted as application failures or timing
measurements.

## Repository alignment

The repository mirror was still pinned to v232. Nineteen new Site paths and
the intervening Site changes were reconciled from the exact v232 source base.
`page.tsx` and its layer test merged without conflicts; repository-specific
governed-water, soil, weather, and release safeguards were retained. There
were no file deletions.

The new append-only v246 receipt records 943 identical paths, nine inherited
repository overlays, 42 repository-only paths, and the two canonical tool
mappings. No authoritative Site path is missing. The selector's authority
remains **CONTENT_PARITY_ONLY** and its receipt remains **REVIEW_ONLY**;
repository overlays are not represented as deployed to the Site.

Placement follows Directory Rules v2 as adopted by ADR-0029: application
mirroring under `apps/site/source`, operational review under `docs/reports`,
machine evidence under the existing `data/receipts/generated` responsibility,
and the existing `tools/qa/site_mirror.py` consumer. No new authority root was
introduced.

## Validation

- Standalone build and TypeScript: PASS; 1,096 tests passed.
- Focused Underground contracts, cleanup, camera, worker, and detail checks:
  115 passed.
- Reconciled mirror build and TypeScript: PASS; 1,129 tests passed.
- Initial mirror/release Python checks: 32 passed. After the main update,
  mirror, water-release, and weather-hosted checks: 43 passed.
- Mirror content check: PASS with explicitly retained overlays.
- Hosted exact-head CI is reported separately on the accompanying PR; local
  execution does not establish its result.

Machine observations:
[browser evidence](../../data/receipts/generated/underground-browser-endurance-20261011.json)
and [v246 mirror receipt](../../data/receipts/generated/site-v246-underground-browser-review-20261011.json).

## Limits and recovery

Battery saver changes the existing map request/worker/render budget; it does
not silently lower the independently selected 2048/4096 cutaway detail. The
connector did not provide hardware CPU/GPU/network throttling, live reduced-
motion emulation, heap inspection, or physical-device testing. Existing
reduced-motion and disposal tests are implementation evidence, not executed
physical-device acceptance. Stable canvas counts are not proof of zero GPU
or heap leakage. Multi-hour sessions, fully cold network, broader keyboard and
assistive-technology acceptance, and hosted rollback remain separate checks.

For local application rollback, atomically point `KFM-Explorer-Site-current`
back to the retained v229 folder and restart only the existing local Site
service. Keep its existing persistent-store path. For repository rollback,
revert this mirror follow-up and restore its v232 selector; the old receipt
remains unchanged. The subsequent CI correction published v247 as described below.


## CI correction and final identity

The first exact-head hosted run rejected a test fixture's `this` alias and
three new uppercase documentation paths. The same corrections were applied
to the authoritative Site and its mirror: the mock retains its closest-ancestor
behavior, and the new documents now use lowercase names under the same owning
root. No lint rule or topology baseline was weakened. Topology reports zero
new drift and 110 inherited warnings; all 29 topology tests pass after fetching
the exact historical baseline commit omitted from the shallow clone. Full Site
lint has zero errors and 66 existing warnings.

Final owner-private Site v247 source is
`b2bf41b1149d393d49909c4962e320f7f05cc422`, saved version
`appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_67b88754cc64819195a2d721b2a03ea7`,
successfully deployed as `appgdep_6acc2c0c694c8191bbab77f1c75d7b04`.
All production `app/` source and client assets match the v246 browser-tested
application. Three generated server/manifest files differ after rebuilding;
full deployment bytes are therefore not claimed identical. The PC retains a
complete v247 copy in `KFM-Explorer-Site-browser-checked-20261011-v247`, alongside
v246 and v229. Persisted state and bindings remain unchanged.

The append-only [v247 receipt](../../data/receipts/generated/site-v247-underground-ci-corrections-20261011.json)
is selected for CONTENT_PARITY_ONLY checks; its review and human-acceptance
holds remain explicit. The 17-minute endurance evidence describes v246, with
post-correction v247 smoke and code/client-content comparison as separate proof.

Post-correction local and owner-private hosted smoke restored the same 50
records, 28 columns, aquifer withholding, and complete 2048 × 1718 surface
with no console warnings/errors. Both corrected full suites reran successfully
(1,096 standalone / 1,129 composed). GitHub records owner merge of #5057 at
its earlier head `6ccd1a9721b7402085a4775e2b55c8a137f36837` while these
corrections were being checked; merge commit is
`79d401c069d927e6595b7166d732cc52606f381d`. The correction follow-up retains
that merge and its initial failures as history, rather than claiming they
passed or rewriting it.


## Final #5059 review and current-source alignment

PR #5059 was already owner-merged to `b194938f9e8abc076f82c75b32e0dbec25add8ca`
when final review began. Its exact head had 107 successful and two skipped checks;
merged main completed 104 successful and two skipped checks. The automated review
identified stale v246 reconciliation metadata in the historical v247 receipt.
That historical receipt is retained unchanged. A new append-only
[reconciliation receipt](../../data/receipts/generated/site-v251-final-review-reconciliation-20261011.json)
binds the selected current source and current paths. The parity validator now
rejects a declared reconciliation naming another source or a removed path;
receipts without that historical section remain readable. These checks do not
grant human acceptance, source admission or data activation.

The authoritative Site had advanced concurrently to v251 source
`4d81543389496b6c789a47a9282a3d10740542c9`, deployed successfully as
`appgdep_6acc33d78064819196684fc4ef727761`, owner-only at environment revision 5.
The new mirror starts from merged main and preserves soil, review and release
controls. Four page conflicts were retained repository-only soil additions;
the weather catalog test already includes the weather changes plus soil.
Source aquifer/Underground geometry, public data assets, native values and the
2048/4096 detail controls are unchanged from v247. The Site's new focus, hover,
layer-order and request-retirement fixes are retained. No source edits or
publication were made to the authoritative Site in this review.

Current validation: 1,131 standalone tests and 1,146 composed tests passed;
both TypeScript checks and builds passed; 45 mirror/water/weather Python checks
passed. Both full lint runs have zero errors and 66 existing warnings. Topology
passes with zero new drift or invariants and 93 inherited warnings on the current
main baseline; this follow-up did not alter that baseline. The mirror records
969 identical application files, nine retained overlays, 21 repository-only
paths and two canonical tool mappings; no authoritative path is missing.

The PC now has a separate exact v251 source copy (980 tracked files), its
prepared build (428 files), and 24 retained prior client assets for already-open
tabs. The existing current alias and port 4173 service use this copy. The v247,
v246 and v229 copies and v109 persistent store remain in place. No migration
or data activation ran. Rollback switches the alias to retained v247 and restarts
the existing service, retaining that store; repository rollback reverts this
follow-up and restores the historical v247 selector.

Fresh browser evidence and follow-up exact-head CI are recorded separately.
The earlier long-session observations do not establish v251 physical-device,
GPU/heap, hardware-throttling, multi-hour or hosted-rollback acceptance.


Fresh v251 installed-local and private-hosted browser checks both restored 50
records, 28 plotted columns, one aquifer region, partial coverage and unbounded-
class withholding, with a complete 2048 × 1718 surface at zoom 13.4. No captured
console warnings/errors were returned. Loading focus entered Close Underground
and transferred to the mounted close control; explicit re-entry focused it again.
Observed local canvases were three with Underground closed and five after
reapplying the example; this is a smoke check, not leak proof. Closing the
workspace and reopening requires applying the example/area again. The main
map also disclosed one external-source issue; no claim that all live sources
were ready is made by this Underground verification.

Main advanced through #5060/#5061 to
`d9887c7e2a8b5625a5151e51e6543239cb57637e` during review. Those changes did not
modify the Site mirror or receipt validator; the branch was merged without
conflict and all 45 Python checks and topology were rerun successfully. The
primary PC repository was fast-forwarded safely; other worktrees were retained.
Follow-up PR #5063 carries this reconciliation and the stale-provenance fix.
