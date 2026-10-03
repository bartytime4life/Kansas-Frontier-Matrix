# Local map archive browser

Open **Map layers → Roads, rail & bridges → Local road & bridge map archive**,
then **Browse local map archive**. The existing Map Workbench comparison panel
also contains this entry. This restores the workflow from the older local
100-sheet historic county/township browser without replacing the current Site,
HUD, imagery, bridge inspection or candidate road-line comparison.

The discovery index covers 596 operator-held PDFs across six collections:
105 bridge sheets, 55 state road maps, 105 county roadway plans, 100 historic
county/township sheets, 191 past county maps and 40 urban roadway plans. Counts
refer to the checked inventory snapshot, not a live scan of the user's disk.
The whole index loads only on request; results show 20 per page. Search and
collection/year filters operate locally. The map timeline is unaffected.

## Identity, dates and preview

Select a record, then choose its PDF from the device. Exact filename, byte size,
PDF header and SHA-256 must match before a local `application/pdf` blob URL is
created. Open the matched original with the explicit link. The file is never
uploaded or served from an internal data store. No original PDF or scan pixels
are bundled in the Site. One verification may run at a time, even if the panel
is quickly closed and reopened; the maximum supported file is 100 MiB. All
596 inventory entries fit that bound. Native file reads and WebCrypto hashing
may finish after cancellation, but their stale result cannot create a preview.
Changing the selection, clearing or closing the panel revokes its blob URL.

A matching hash establishes byte identity only. It does not establish rights,
source authenticity, factual accuracy or review/release status. A native PDF
viewer may be needed; PDF rendering/interactive acceptance remains unverified
while browser access is blocked by the admin-policy check.

Year filters explicitly distinguish filename clues, OCR title-block clues,
visual title-block clues and previously checked printed editions. They do not
use file modification or PDF creation timestamps as map dates. Two-year editions
match both years and display the full range. This does not fill missing years or
date construction, closures, demolition or route validity. The original 100
historic county/township records preserve their 97 OCR and 3 visual readings.
That collection still lacks Gove, Graham, Grant, Gray and Greeley sheets.

## Review flags

The current index has four flagged records:

- `KFM Past Published County Maps/1972 Kansas.pdf` and `Crawford1936.pdf` contain
  identical bytes under conflicting names. Date/place claims are withheld;
  both remain searchable by filename, and both originals remain untouched.
- `KFM Past Published County Maps/doniphan1999.pdf` produced a recovered PDF
  cross-reference warning. Source-integrity review is needed before preparation.
- `Kansas Road Maps/1967 Kansas.pdf` is the previously recorded blank source.

The 185 embedded-control candidates remain **alignment unreviewed**; the other
411 have no embedded controls recorded. None is a released geographic overlay.
The separately pinned Allen County preparation below supports opt-in device-only
review. County and urban functional-classification planning maps retain a
warning that proposed roads are not present conditions. The original source
legend, rights and independent georeferencing still govern preparation.

## Projection and placement

`scripts/project-local-map-archive.py` deterministically projects four explicit
local evidence inputs into `app/local-map-archive-inventory.json`: the hash
reconciliation, additional-file structural screening, existing sheet catalog
and existing georeference screening. Input SHA-256 values accompany the index.
It rejects duplicate metadata identities, invalid paths/sizes/digests,
unbounded year ranges and any prior metadata bound to different PDF bytes.
It reads no PDFs, acquires nothing, makes no lifecycle transition and writes
only the explicit output. Reverify the originals separately before refreshing.

```sh
python3 scripts/project-local-map-archive.py \
  --reconciliation /path/to/archive-reconciliation.json \
  --additional /path/to/additional-pdf-screening.json \
  --sheets /path/to/map_sheets.csv \
  --screening /path/to/sheet_screening.csv \
  --output /path/to/candidate-inventory.json
```

Generate separately and compare with the reviewed app index before replacing it.
The standalone Site's existing `app/`, `scripts/`, `tests/` and `docs/` own this
application projection under Directory Rules v2 §10.1 and accepted ADR-0029.
This is not a parallel canonical source registry, catalog or georeferencing
pipeline. Canonical RAW/QUARANTINE/processed records remain in their existing
external-store responsibilities. No uploaded data, evidence, report, saved
workspace, release, private storage binding or approval is created here.

## Validation and recovery

Run the focused `tests/local-map-archive.test.mjs`, TypeScript, production build
and full Site suite. Verify all record hashes against explicitly selected
originals, and check preservation of the older 100-sheet identities and dates.
Tests cover range/unknown/flagged filters, wrong files, byte limits, cancellation,
single-flight hashing, URL revocation and stale provenance rejection.

Rollback removes the new application projection and entry point by restoring
the preserved preceding source/build. No source PDF, canonical catalog, D1/R2
object or service configuration needs restoration for this feature. Preserve
newer work before any rollback. Browser selection, keyboard behavior, native
PDF opening and visual layout require separate browser acceptance.

## Prepared Allen County review — 2026-10-03

Select **KFM County Roadways / Allen County.pdf** in the archive. Its **Prepared
map review** control accepts the exact folder `kfm-allen-geopdf-review-20261002-v2`
from the external store's `data/work` lane. This is explicit user file selection,
not a server connection to WORK. Directory selection requires a browser supporting
`webkitdirectory`. No localhost file server, new route, upload, R2 object, D1 row,
credential, owner operation, source approval, or background acquisition is added.

The preparation manifest is pinned to SHA-256
`7796ae7a428286be480704a5e80c27e41bbcdc75edbed87fc794331dc4914cf4`.
Original PDF: `477eead68df3ed87d6c353a2bd1ba471e6064be76da61e98d739729d4e41f766`.
Candidate: `8e26f9a0eec73580a30ffe84afef8e9387b195836b730646e32c4344adc4a0b6`.
All 186 files / 3,751,691 bytes must match; every artifact and tile is hashed
before the map receives any bytes. Extra, missing, changed, duplicate, mixed-folder
or traversing selections are rejected. File reads are sequential within each
selection, at most 2 MB each. Cancellation discards a pending native read or hash
result and stops further reads; native work already started may finish. Repeated
selections do not have a global single-flight lock.
The browser verifies byte identity; it does not repeat the pipeline's geographic
validation or convert a hash match into approval. There is no runtime pin override.

One prepared sheet appears over the user's current 2D basemap with visibility,
0–100% opacity (default 65%), Fit, Remove, and verified original/full-page links.
Its 181 nearest-neighbor Web Mercator tiles have no raster fade or interpolated
colors. Below camera zoom 9, the four coarsest verified tiles are displayed as
exact Web Mercator tile-corner image quads; the higher-detail tiled source starts
at zoom 9. This makes whole-sheet fit usable on small screens without stretching
a PDF preview to an outline, fabricating coarse measurements, or double-blending
overviews and detailed tiles. Both paths use identical source bytes and opacity.

Nonzero pitch, terrain or a non-flat projection suspend a mounted review;
**Use flat map for review** uses the existing representation control. The Globe
action closes the panel and clears its review; returning requires folder selection
again. Fit respects reduced motion and the
panel's footprint. Zoom beyond the prepared range warns of enlarged pixels.
Pixels, blob URLs, the custom MapLibre protocol and event listeners are discarded
when the sheet changes, the panel closes, or review is removed. Basemap replacement
reinstalls only the current in-memory review; failed tiles withhold the overlay.
Nothing enters persisted workspaces, report inputs, public-safe JSON exports,
evidence, ordinary layer registration or release state. Fit still changes the
ordinary camera/viewport, which existing reports or Places may retain without
the review layer or its pixels. Closing the browser
requires explicit file selection again.

The source says **Functional Classification, 5–10 Year Future**, printed June
2025; county approval May 13, 2003 and FHWA approval November 7, 2003 are separate
dates. The UI preserves this meaning. Nine source-selected cartographic junctions
showed projected discrepancies of 0.225–5.058 m against Census 2025 roads, without
refitting. That evidence was produced separately by the monorepo's offline
`tools/local_data/geopdf_alignment_review.py`, using pinned NADCON5 grids and
verified TIGER originals. It is not independent surveyed ground accuracy;
reference lineage may overlap. Render detail is approximately 22.5 m per pixel.
The source's planning semantics and original legend control interpretation; this
feature cannot identify constructed, closed, or abandoned roads or bridges.

Application files `local-geopdf-review.ts`, `local-geopdf-map.ts` and
`local-geopdf-review-control.tsx` own bounded local inspection and rendering.
The custom renderer protocol is registered through the existing
`maplibre-seam.ts`; local review retains its tile callback and teardown. This
keeps the Site's single renderer acquisition boundary while preserving exact
in-memory tile bytes.
The constant pin is an application review input, not a canonical source registry.
Acquisition, preparation and lifecycle authority remain in their existing
monorepo and external-store responsibilities. No schema migration is introduced.

Run `node --test tests/local-geopdf-review.test.mjs tests/local-map-archive.test.mjs`,
TypeScript, build and the full Site suite. Tests distinguish synthetic pin fixtures
from the actual privately retained package; the latter needs a separate local
integration check. Browser/GPU rendering, keyboard/file-picker behavior and visual
alignment remain separate acceptance gates. Rollback removes this additive UI
commit or restores the saved preceding local build; it changes no data pointer.
