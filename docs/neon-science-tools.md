# NEON samples across KFM

The Terrain & vegetation lab at `/labs/terrain` is a descriptive science view of
the same validated historical Konza pilot used by the main map and acquisition
workspace. It uses the existing `/api/neon/preview` route and the existing signed
relay to dev’s 14 TB drive. It adds no provider credential, subscription, paid
API, external tile service or new dev worker route.

## Shared data contract

`app/neon-lidar-science.ts` exports `createNeonScienceDataset(input)` and
`neonScienceDatasetJSON(dataset)`. The adapter accepts only a complete validated
`kfm-neon-relay-pilot-v1` receipt with the expected site, month, run, release and
tile. A raw local or synthetic grid cannot be promoted into this provider
science view. Existing local imports remain available for explicitly labelled
raster inspection.

The adapter returns `kfm-neon-science-v1`, containing the parsed receipt and a
record bundle that the existing RecordLab/science models can use. Every preview
cell has a stable identity, one-based row/column, native sample-center easting
and northing, DTM, DSM, independent provider CHM, DSM minus DTM, and difference
QA. It retains original numeric values, nulls, valid zero and negative source
differences. An overflowing source difference is null with nonfinite QA rather
than an invented number. Coordinates and indices are inspection fields, not
default scientific measures.

There is no invented longitude/latitude, per-sample observation date, annual
series or county assignment. The catalog month is not an exact acquisition
date. Original file retrieval timestamps are unknown in this receipt; preview
preparation and relay-cache times remain separately named. The three original
filenames, products, byte lengths and SHA-256 values accompany the bundle.

Other KFM components can use the same adapter after the shared bounded client
loader returns a receipt. They must preserve its review/cache labels and use the
same receipt revision for all linked views. This is a reusable data contract,
not automatic compatibility with every notebook/import format. No static Labs
snapshot manifest, SQL dataset allowlist or governed admission gate is widened.

## Descriptive tools and exports

RecordLab’s distribution, filtering, source inspection, quartiles, sample
standard deviation, complete-pair Pearson/Spearman association, ranking and CSV
operate on these exact sample rows. Quartiles use type-7 interpolation at
`(n - 1)p`; sample standard deviation uses `n - 1`. Missing values do not become
zero and incomplete pairs do not enter a relationship calculation. These
existing mathematics are unchanged by the adapter.

The record and group-summary CSVs retain all three raw-file hashes. Their
optional `analysis_context` JSON column carries compact source identity,
sampling, reference/time distinctions, pending-review flags and native-outlier
statistics. It avoids repeating verbose CRS and review prose in every row.
The source-linked dataset JSON retains the full receipt, recorded CRS, review
notes and regenerated derived rows. Presentation precision never rounds the
stored source values. Existing CSV shapes are unchanged for datasets without
analysis context.

The preview contains regularly spaced nearest native samples; it is not a
random sample or a complete native raster population. Summary statistics and
relationships describe this selected preview only. Adjacent samples are
spatially dependent, and DSM minus DTM is arithmetically coupled to both inputs.
No correlation, fitted line or count establishes causation, independent sample
size, vegetation area, species, biomass, carbon, growth, change or field accuracy.

## Relative 3D display

In Appearance, **Explore in 3D** loads the Konza pilot if needed, enables the
column representation, fits its tile and tilts the camera in one action. It uses
the currently loaded preview when one is already present. The first 3D entry
uses a labelled 3× scale; the control remains adjustable from 1× to 5×. Return to
Flat samples for an overhead view. The separate statewide Terrain 3D preset uses
an external elevation source and does not display these local NEON samples.

The map displays a bounded column representation of the sample grid. Its shared
local height baseline and any vertical exaggeration are visualization settings. Source readings and science exports remain unscaled.
Ground/surface columns represent sampled elevations relative to that baseline;
canopy columns use valid DTM as their base and the independent provider CHM as
their height. Missing ground cannot support a placed canopy column. The
rectangular display footprints are not measured vegetation volumes or surveyed
terrain meshes. The flat overlay remains available.

Actual sampled low/high ground, highest canopy and largest DSM minus DTM can
provide deterministic story stops. A preview maximum is labelled as sampled;
it cannot stand in for the retained native canopy maximum of 83.41 m. These
outliers still need review. Globe/active external-terrain alignment is not
invented, and invalid/extreme rendered geometry is omitted rather than changing
source measurements.

## Verification and release boundary

The earlier live release’s dev-backed API, grid and map-cell reads were verified
before this usability/science/3D follow-up. That acceptance does not establish
this new interface or the new GPU rendering. The follow-up needs its own adapter,
science, component, rendering-math, type/build/CI and live/browser verification.
No dev service, data migration, credential rotation or subscription is required.
Revert the follow-up application source and redeploy to return to the previously
verified flat pilot; keep the current dev relay and original data intact.
