# Subsurface geophysical context

The Underground workspace can show published electrical-conductivity logs as
independent measurements versus depth. These profiles are external context, not
included evidence, a resource estimate, a continuous geological model, or a new
canonical registry. A conductive interval does not uniquely identify a rock type.

## Qualified numerical profiles

The [KGS Kansas River Alluvial Aquifer Index Well Program report, OFR 2022-6](https://www.kgs.ku.edu/Publications/OFR/2022/OFR2022-6/index.html)
publishes five Excel workbooks with location tables and direct-push electrical
conductivity (DPEC) logs. Section 5.4 of the report describes surface-down logging
at approximately 0.05-foot intervals. The display asset preserves the original
`Depth (ft)` and `EC (mS/m)` values without interpolation, smoothing, inversion,
resampling, or conversion to geological classes. Sampling interval is not an
assertion of positional or measurement accuracy.

Retrieved **2026-10-06T02:26:53.810755Z** from KGS, with 21 usable profiles and
25,479 numerical samples:

| Workbook | Displayed profiles | Held profiles | SHA-256 of downloaded XLSX |
| --- | ---: | ---: | --- |
| [DG02](https://www.kgs.ku.edu/Publications/OFR/2022/OFR2022-6/DG02%20EC%20Transect%20Data.xlsx) | 7 | 0 | `0fe30b96f9d826b4bcf4ec31678bfa60a90cacc6b4455dab6b18d636093f65e2` |
| [DG03](https://www.kgs.ku.edu/Publications/OFR/2022/OFR2022-6/DG03%20EC%20Transect%20Data.xlsx) | 0 | 6 | `c9b8ceac0fdfe7e49bf2c7fca78fce666167e0d6d1554182d0a00528ca08def7` |
| [JF01](https://www.kgs.ku.edu/Publications/OFR/2022/OFR2022-6/JF01%20EC%20Transect%20Data.xlsx) | 1 | 2 | `14090c05ffe586838f04bda7e0da35bee5379479c536c41c5040a761e6febf8a` |
| [RL01](https://www.kgs.ku.edu/Publications/OFR/2022/OFR2022-6/RL01%20EC%20Transect%20Data.xlsx) | 7 | 0 | `cf30bfbdff5b35576fba492e3244a40bf0cc5fca573e2964121e07a55b254f64` |
| [WB01–PT02](https://www.kgs.ku.edu/Publications/OFR/2022/OFR2022-6/WB01%20to%20PT02%20EC%20Transect%20Data.xlsx) | 6 | 1 | `c0db284efd934bbed3d8b8ef9115a4a2a45e8bb3587d8f4f759465f9d46428d2` |

The four used workbooks explicitly describe their coordinates as taken from
Google Earth images. Locations are approximate horizontal display context, not
survey-grade registration. `North` and `West` become `[negative abs(West), North]`;
the source's explicit datum and horizontal uncertainty are unspecified. Each
profile remains relative to its own land surface. Workbook elevations are omitted:
they are not used to align samples with sea-level terrain or another borehole.
No connecting curtain or footprint is inferred from isolated log locations.

The following anomalies are deliberately retained as holds, with no coordinate
repair or reassignment:

- DG03 uses location aliases (`SS01`, etc.) and differently named data sheets.
  The individual sheets contain coordinate headers that may permit subsequent
  reconciliation, but the identity mapping has not been admitted in this capture.
- JF01-EC1 and JF01-EC2 contain identical depth/conductivity arrays: 1,073 pairs
  each from 0 to 53.6 feet, despite distinct listed locations. Both are excluded
  pending clarification; JF01-well remains available.
- PT01's published `West` value is `29.278079999999999`, outside Kansas. Its
  numerical profile is held rather than moved to an assumed location.

## Reproduction and checks

`public/data/subsurface/geophysics.json` is a versioned presentation capture under
the standalone application's existing `public/data` responsibility. Documentation
belongs under `docs`; the GitHub projection remains under `apps/site/source`.
This follows the adopted Directory Rules via accepted ADR-0029 and the standalone
Site preservation record. It creates no evidence, registry, policy, or release home.

To reproduce, download the five linked workbooks and compare their hashes first.
Read worksheet relationships from `xl/_rels/workbook.xml.rels` and shared strings
from `xl/sharedStrings.xml`, then identify columns by their exact header labels.
Do not assume a fixed EC column: RL01 places conductivity in column C while the
other used workbooks place it in column B. Join exact worksheet names to the
`Locations` table, with the explicitly recorded RL01-EC1-Well → RL01 alias. Apply
the holds above. Read finite nonnegative depths and finite conductivity values in
source order; retain valid zero conductivity values. Reject missing/nonnumeric
rows and report their count. Do not silently sort or deduplicate a nonmonotonic log.

Capture validation confirmed 21 unique profile identities, valid Kansas display
coordinates, finite values, strictly increasing depths, and no duplicate complete
series among the admitted profiles. The 25,479 sample values were extracted from
the original numeric cells. The resulting JSON SHA-256 is
`5150c0eb992a333142ce0754b8acd17db8cb9009125cb34ed1c32a50b6e03359`.
This source qualification does not substitute for renderer or browser acceptance.

## Remaining source holds

- **GPR:** [KGS GEMS borehole radar, OFR 98-48](https://www.kgs.ku.edu/PRS/publication/OFR98_48/index.html)
  contains report figures and methods for the October 7 and 12, 1998 surveys near
  Lawrence. No downloadable numerical traces were verified. The report identifies
  uncertain time-zero calibration and casing-top depth references. Link to the
  report; do not synthesize traces, derive a depth image, or imply statewide GPR
  coverage. Radar travel time and borehole antenna depth are distinct quantities.
- **tTEM:** the [Remote Sensing Hydrology research page](https://www.remote-sensing-hydrology.com/research/ttem)
  describes Kansas resistivity surveys and links a visualization. Native numerical
  soundings, inversion geometry, depth-of-investigation arrays, and source-specific
  redistribution terms were not qualified. Keep the record reference-only.
- **Published geological pilot:** OFR 2022-6 describes a 200-metre horizontal,
  5-foot vertical hydrostratigraphic grid derived from well logs. Native grid files
  and complete datum metadata were not located. The asset lists this under
  `modelReferences`, outside the geophysical-method filters. Detailed model
  activation remains held; displayed report colors are not numerical model data.

## Rights and attribution

The [KGS terms](https://www.kgs.ku.edu/General/copyright.html) permit reuse,
modification, and redistribution with retained notices and source credit. They do
not establish rights for third-party linked sites. KGS supplies data without
warranty and its name must not imply endorsement. Retain this required credit with
the capture and downstream exports:

> The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved.

## Additional verified integrations

The [USDA Soil Data Access REST query service](https://sdmdataaccess.nrcs.usda.gov/WebServiceHelp.aspx)
accepts a `POST` to `https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest` with
`format: "JSON+COLUMNNAME"`. A point query using
`SDA_Get_Mukey_from_intersection_with_WktWgs84('POINT(-95.25 39.0)')` joined through
`mapunit`, `component`, and `chorizon` returned seven horizons on 2026-10-06.
The map unit is Eudora-Kimo complex; its Eudora, Kimo, and Sarpy components have
reported proportions of 65%, 25%, and 10%. These are alternative descriptions
within a mapped unit, not measured layers stacked at the cursor. `hzdept_r` and
`hzdepb_r` are centimetres below soil surface. Numeric fields arrive as strings;
missing values must remain missing. Requests should be bounded and explicit about
partial response limits. The source service returned browser CORS `*` in this check.

The [KGS core photograph index](https://chasm.kgs.ku.edu/ords/qualified.cimg2.SelectWells)
links per-well pages by KID. For example,
[well 1028187622](https://chasm.kgs.ku.edu/ords/qualified.cimg2.CoreImages?f_well=1028187622)
has photographed box intervals, gaps and overlaps, and original image links.
Those labels should be retained rather than interpreted as a continuous recovered
core. Links alone do not establish photographic coverage for other core records.
