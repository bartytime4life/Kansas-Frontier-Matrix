# Local mine-map and geology validation — 2026-10-08

## Identity and preservation

Implementation began on KFM main `3b39b948919b51433db369b816e3ea748c54df1f`.
The active local standalone Site at `d596a8616c2e268fc7f6a9b988a6732ddfd121ae`
matched all 751 repository Site files byte-for-byte before editing. The current
same Sites project remained `appgprj_6aa0b1c41bc08191bfd86003920f1631`, saved
version 185. Later main changes through `7d79ce10ace694e3bedb5e1a01b96bd479759577`
were confined to unrelated repository documentation.

The local delivery preserves origin `http://127.0.0.1:4173`, the existing D1/R2
state directory, local browser storage, credentials, and the external KFM data
root. Source/runtime directories are installed separately; prior directories
remain rollback points. No hosted Site save, publication, audience change,
source admission, or mirror-review approval was performed.

## Catalog and retained archive

The metadata receipt and compact index are under
`tools/local_data/catalogs/public-maps/` in the repository. Discovery reconciled
2,270 distinct NGMDB IDs across 23 successful pages: 944 USGS and 741 KGS records.
The Site lists 1,695 records including ten retained references. NMMR TLS failure
leaves its statewide inventory unknown. The original URLs remain in the receipt.

All 596 pre-existing archive identities and the Allen County preparation hashes
remain unchanged. New provider records are separate from hash-verified local
map sheets. The pinned preparation registry rejects unknown source identities
before reading files.

## Browser observations

The installed production worker and loopback download operator were exercised
through Chrome at the existing local origin:

- Loaded the full catalog and filtered KGS / M-118; keyboard Enter selected the
  matching record and Tab entered the map canvas.
- Opened M-118 context, loaded five real KGS features, selected Alluvium through
  the keyboard-accessible feature list, and inspected its original attributes.
  The map displayed source attribution, amber-feature legend and 1:500,000 limit.
- Opened the original JPEG in a separate document tab; the image loaded at
  5,004 by 2,880 pixels. This is a document, not a georeferenced overlay.
- Selected the 5,348,461-byte M-118 JPEG with a 6 MiB maximum. It completed as a
  private candidate with SHA-256
  `77b136d8d1025d0dca565d49f8892a412fdc9712a32cb439ccfd71bf3eefdefb`.
- Started the 37,386,469-byte M-118 PDF with a 36 MiB maximum, observed progress,
  then cancelled through the UI. The retained partial is 19,922,944 bytes with
  SHA-256 `a1f1e0885cfe586c085142a9ca14ee0cb5a82ed26a2baf67e12be1689d670aa1`.
  The UI reported cancelled rather than complete; the receipt marks it incomplete.
- Both receipts retain `UNREVIEWED`, `NOT_ADMITTED`, `NOT_RELEASED` and
  `providerChecksumVerified: false`. Stored hashes are not provider checksums.
- Loaded CNGM v2 Earth-surface polygons (five features), selected a feature and
  retained its MapSourceID/DataSourceID attributes. Switched to the separate
  Precambrian product (one feature), with inferred-buried-geology limits visible.
  The national archive sizes were visible before selection; none was downloaded.
- No browser console errors were observed for these feature-preview interactions.

These bounded browser checks do not establish comprehensive accessibility,
mobile/touch, provider availability, geological accuracy, or source admission.
The two test captures consume about 25.3 MB plus small metadata files in RAW.
They remain inspectable, with no automatic deletion or completion retry.

## Automated checks

TypeScript and the production build passed. The final full Site suite passed
709 tests. Focused backend checks passed 63 tests and 96 subtests, covering existing
Earth Engine/library behavior plus discovery, streaming limits, cancellation,
redirect rejection, checksums, missing receipts and interrupted workers.

## Final follow-up checks

After implementation commit `d22e013a9024894cb1374d34b414e9dd189d16b3`, scoped
MapLibre control styles restore 44-pixel white buttons. The background override
uses `!important` because the download workbench's global rule also uses it.
The production build passed. On the final local installation (r4), browser
inspection confirmed white `rgb(255, 255, 255)` zoom buttons measuring 44 by 44
pixels with zero padding. The KGS preview loaded five features with source
attribution visible.

The four ScienceBase MD5 values for the Limon/Lamar ZIPs are preserved as provider
metadata in the seed catalog and subsequent capture receipts. They remain
unverified (`providerChecksumVerified: false`), separate from the local stored
SHA-256 and byte-readback checks; none of these four ZIPs was downloaded for this
metadata correction.

Initial follow-up Python checks passed 24 tests and 80 subtests: 21
download-manager tests and three smoke-runner startup tests. The new preview
route is included in the smoke inventory with its offline missing-input `400`
check, repairing the three introduced startup failures.

The final follow-up rerun passed TypeScript, the production build, and all 709
Site tests. The build and Site test logs are
`/tmp/kfm-public-maps-final-build.log` and
`/tmp/kfm-public-maps-final-tests.log`. Final focused Python checks passed 45 tests
and 80 subtests: 18 catalog, 21 download-manager, three control, and three
smoke-runner startup tests. The earlier 63-test/96-subtest backend regression
result above remains evidence for the prior functional implementation; that
broader backend selection was not rerun in this follow-up.

The final installed local catalog returned 1,695 records and retained all four
provider MD5 metadata values. The actual local Site smoke run passed 57 checks
across 47 routes, with nine provider-only routes explicitly listed; its log is
`/tmp/kfm-public-map-smoke-final.log`. These final installation and browser
observations were verified by the coordinating agent and retain the bounded
acceptance and admission limits above.

The coordinating agent compared the remaining CI failures with prior main/base
runs and identified four inherited failures:

- Repository gap scan: main reports 139 broken links against a 138-link baseline.
  `.github/workflows/README.md:392` still references `.github/README.md`, removed
  by `ffe4216` / PR #4943. See [main run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37818760238).
- Water lane: `MIRROR_REVIEW_REQUIRED`, present in the
  [base run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37817906594)
  and [main run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37818760514).
- People lane: missing documentation-only marker, present in the
  [base run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37817907173)
  and [main run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37818760462).
- Soil lane: changed release index, present in the
  [base run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37817906861)
  and [main run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37818760638).

These findings do not clear the inherited gates or grant admission, release,
mirror-review approval, or hosted publication.
