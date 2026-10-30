# Archived KGS geology reference for private review

This collection makes the preserved **Surficial Geology of Kansas**, KGS Map
M-118, 2008 edition, available as a dated document in the working PC's private
review desk. The publisher's recorded map scale is 1:500,000. It is useful
statewide reference context; the edition year is not an observation interval.
No vector geology, quantitative measurements or georeferenced overlay is created.

## Selection and provenance

The imported library's domain labels are keyword hints. During selection, NOAA
station identifiers containing `CDL` appeared under agriculture, and `KGS` airport
identifiers appeared under geology. Those labels do not establish dataset topic
or Kansas coverage. The selected document instead has explicit KGS source
metadata, its title/year on the visible sheet, and a completed capture receipt.
Classifier correction and bounded catalog refresh remain separate follow-up work.

`tools.local_data.historical_geology` accepts an explicit capture job identifier
and SHA-256 pins for the receipt and source record. It checks:

- Completed, unreviewed, unadmitted and unreleased capture state, one complete
  file, matching asset, expected bytes, stored bytes and hash.
- The exact KGS M-118 source identity, 2008 edition, 1:500,000 scale, JPEG asset
  URL and held rights state.
- Freshly read original bytes against the captured digest, with bounded JPEG
  headers/dimensions. These are integrity checks, not scientific validation or
  provider-checksum verification.

The original archive is read only. Old absolute paths in the receipt are retained
as evidence and never used to locate files on this PC. The helper resolves only
the expected relative archive paths, rejects static symlinks, and writes to a
separate initialized store. No network access is needed.

```sh
python3 -m tools.local_data.historical_geology \
  --source-root /absolute/imported-archive \
  --root /absolute/initialized-working-store \
  --job-id EXACT_CAPTURE_JOB_ID \
  --receipt-sha256 EXACT_RECEIPT_SHA256 \
  --source-sha256 EXACT_SOURCE_RECORD_SHA256
```

Run under the PC's shared capture/analysis/backup operation lock. The helper also
holds the working-store lock. It creates an immutable WORK review package with
the unchanged JPEG, source record, capture receipt, coverage, validation and
README. Identical inputs verify existing output rather than overwriting it.
Input and implementation hashes identify the derivation. The returned manifest
binding joins the existing private water and climate review bindings.

## Bounded private image previews

The desk supports PNG and JPEG document images through the existing authenticated
review routes. Every selected member's size and hash are checked before serving.
JPEG headers must identify an 8-bit baseline or progressive image with one or
three components, dimensions at most 8,192 per side, and at most 16 million
pixels. Segment count and header bytes are bounded. PNG retains its existing
4,096-per-side and 16-million-pixel limits. Browser decoding is separate from
header validation. HTML, SVG and raw PDFs remain outside this reader.

The actual archive JPEG is 5,348,461 bytes, 5,004 × 2,880 pixels; its capture
completed October 9, 2026 at 14:10:51 UTC. Its SHA-256 is
`77b136d8d1025d0dca565d49f8892a412fdc9712a32cb439ccfd71bf3eefdefb`.
No image conversion, resizing or georeferencing is applied to the stored member.
Two complete archived JPEG captures share that digest; only the explicitly
selected capture enters this collection. Partial PDF downloads are excluded.

Rights remain held. Source admission, activation, independent scientific review,
release and publication remain pending. The collection adds private document
context without adding raw-intake index rows or changing public card payloads.
Working-store backup and restore checks cover the new package; full independent
backup of the imported archive remains a separate task.
