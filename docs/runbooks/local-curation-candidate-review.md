<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/local-curation-candidate-review
title: Review the local KFM curation candidate bundle
type: runbook
version: v0.1
status: repository-integrated; device-local candidates only
owners: ["@bartytime4life"]
created: 2026-09-25
updated: 2026-09-25
policy_label: public-documentation
owning_root: docs/
responsibility: Explain the read-only curation review boundary and candidate layer use.
truth_posture: Local package evidence at the recorded scan time; no source admission, hosted behavior, or publication claim.
[/KFM_META_BLOCK_V2] -->

# Review the local KFM curation candidate bundle

The external store's `data/processed/kfm-store-reconciliation-20260925` package
is a device-local review snapshot. Its source inventory records 20,591 files in
ten collections at 2026-09-25T14:21:45Z. Seven active PRISM work files have no
stable hash; PRISM can continue changing after that snapshot. The package
includes its own source inventory, path mapping, data dictionary, quality
report, layer manifest, recipes, checksum list, and cleanup plan. The earlier
`kfm-local-curation-20260925` bundle remains the baseline for TIGER, airport
wind, NOAA, map sheet catalogs, and initial PRISM derivatives. The newer
`kfm-prism-review-20260925T140241Z` package is a separate completed-grid
transaction snapshot.

From the repository root, run:

```bash
python3 tools/local_data/review_curation.py \
  --root "$HOME/Projects/KFM-data" \
  --bundle kfm-store-reconciliation-20260925
```

`--root` is the **external store root** containing `data/`, not the `data/`
directory itself. `KFM_DATA_ROOT` supplies the default. The command reads the
explicit bundle, hashes its listed files and the linked PRISM layer file,
checks the recorded inventory and no-deletion state, and prints a JSON review
summary. `LOCAL_CANDIDATE_REVIEW` means the named *package* passed these checks;
it does not rescan today's `raw/` tree or verify that an updating source has
stopped changing. `HELD` with a reason and a nonzero exit means the package must
be inspected before reuse. No source bytes or local absolute paths are printed.
The command makes no writes or network requests.

## Source and layer routing

All ten raw collections remain external to Git. Read the corresponding local
`layers/layer_manifest.json` and data dictionary before choosing a rendering
adapter. These are proposed views, with source-specific legends and clocks.

| Raw collection | Local candidate role | KFM domain and time control | Current review limit |
| --- | --- | --- | --- |
| `KFM Historic County Township Maps` | Sheet and edition catalog, review queue | Roads, rail, trade; edition clue | No georeferenced historical lines |
| `KFM Past Published County Maps` | Sheet and edition catalog | Roads, rail, trade; edition clue | No construction or removal inference |
| `Kansas Road Maps` | State map edition catalog | Roads, rail, trade; edition clue or range | No historical network geometry |
| `KFM County Roadways` | County 5–10 year future functional-class cartography | Roads, rail, trade; sheet edition and planning classification | 69,750 clipped fragments are map strokes, not road assets |
| `KFM Urban Roadways` | Urban 5–10 year future functional-class cartography | Roads, rail, trade; sheet edition and planning classification | 57,941 strokes overlap county sheets |
| `Kansas bridges` | Sheet catalog, label search anchors and OCR review | Settlements and infrastructure; sheet edition | 2,832 label centers are not bridge locations |
| `TIGER data` | 2025 county, place, township, road and water references | Geography and infrastructure; fixed 2025 vintage | Modern reference only |
| `kansas-wind-all-airports-1932-2026` | Station coverage, daily summaries, and manual latest snapshot | Atmosphere; station day or snapshot time | Missing data stay missing; no continuous live feed |
| `ftp.ncdc.noaa.gov` | ASOS, GHCNDEX, and NEXRAD availability candidates | Atmosphere or hazards; each source's own date and unit | Parser, units, quality, or coverage review held by product |
| `PRISM data` | Completed modeled grid catalog and county summaries | Atmosphere; normal period or grid date by product | Updating source; modeled grids are not station observations |

The five entries in the reconciliation layer manifest are candidate controls
for county/urban road cartography, bridge label search, historical sheet
georeferencing review, and the linked PRISM snapshot. The earlier bundle has
the broader layer intent for the other collections. Keep the two road sheet
representations separate until a sheet and topology review resolves overlap.
Use 2025 TIGER polygons only as a modern clipping or join reference. A sheet's
date indicates that the edition depicts a feature, not when the feature opened
or disappeared. Weather observations, archive availability, and modeled climate
products need independent filters, units, legends, missing-value treatment,
and provenance displays.

## Steps before a KFM map adapter

1. Review the external `README.md`, `DATA_DICTIONARY.md`, `QA.md`, and
   `cleanup_plan.json`, then inspect representative original maps and legends.
2. Resolve source rights and descriptors, and complete the applicable source
   admission decision. Candidate files in `processed/` are not admitted RAW.
3. For each chosen layer, validate source-to-feature links, geometry, dates,
   units, missing values, geographic extent, and display claims. Historical
   tracing needs independent control points, positional error, per-feature
   review, connectivity, and county-seam checks. Bridge labels need symbol and
   asset verification.
4. Build a source-specific, local opt-in adapter under the accepted KFM
   contracts; keep publication, release, deployment, and hosted acceptance as
   separate reviews. The local preview in the package is only a visual sample.

The cleanup plan approves no additional deletion. Keep originals, especially
maps with legends and unique context. A duplicate digest by itself is not
permission to dismantle delivery layouts or delete source evidence.
