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
