# Frontier trails layer — November 14, 2026

A new off-by-default layer, **Frontier trails · Santa Fe, Oregon, Pony
Express** (`nps-historic-trails`), draws the 19th-century routes that cross
Kansas. It also adds a **Trails west** starter. The layer is external display
context (`EXTERNAL_CONTEXT_ONLY`), not KFM evidence.

| Trail | NPS layer | Status shown |
|---|---|---|
| Santa Fe National Historic Trail | `SAFE_NHT` (Kansas rows) | Designated by Congress |
| Oregon National Historic Trail | `OREG_NHT` | Designated by Congress |
| California National Historic Trail | `CALI_NHT` | Designated by Congress |
| Pony Express National Historic Trail | `POEX_NHT` | Designated by Congress |
| Chisholm, Ellsworth and Western cattle trails | `NTIR_OTHER_ChisholmGreatWesternNHTFSEA_ln` (Kansas rows) | Studied by NPS; not designated |

All five layers come from the NPS National Trails Office on
`services1.arcgis.com/fBc8EJBxQRMcHlei`. A local readback on November 14,
2026 returned 101 segments in about 127 KB: 37 Santa Fe, one line each for
Oregon, California and Pony Express, and 61 cattle-trail segments.

## How it behaves

- **Map.** Designated trails draw as solid colored lines with a dark casing.
  The study routes draw as dashed lines. Where the Oregon, California and Pony Express
  trails share a route across northeast Kansas, they draw side by side so no
  trail hides another. Names appear along the lines at zoom 7
  and closer. Each trail has its own legend chip.
- **Clicking a line** shows the trail, the route segment, its designation
  status and the mapped accuracy.
- **Trails west starter.** It turns on the trails, National Register places,
  rivers and terrain shading.

## Trail sites layer

**Trail sites · forts, crossings & ruts** (`nps-trail-places`) adds the public
points of interest NPS lists for these four trails: forts, river crossings,
wagon ruts, museums and similar sites. Click a site to see its place, its
trails, whether it is NPS-certified, a short history and the NPS or partner
page. The **Trails west** starter now pairs it with the trail lines, rivers
and terrain.

- **Private sites are left out.** Sites whose NPS access note says they are
  private, restricted, not accessible or not open to visitors are dropped. The
  access note itself is never published, because it can contain phone numbers.
- **Fields never requested:** telephone, email, address, notes and editor
  fields.
- **Off-topic corridors are dropped.** Sites tagged for none of the four
  trails, such as Route 66 stops, are not shown.
- **Links** are kept only when they point to `nps.gov`, `kshs.org` or
  `kansasmemory.org`.
- **Live check (November 14):** a readback returned 96 sites. 16 private sites
  and 6 sites on other corridors were left out.

## Source and safety boundaries

- **Rows requested.** For the two layers that carry access fields, the adapter
  asks only for rows marked `PUBLICDISPLAY='Public Map Display'` and
  `DATAACCESS='Unrestricted'`.
- **Fields requested.** Only the identifier, trail name, alternate name and
  mapped accuracy. The free-text `NOTES`, editor, user and `GlobalID` fields
  are never requested, and a test checks this.
- **Clipping.** National trails are clipped to the line parts that touch the
  Kansas window, so a part may run a little beyond the state line.
- **What a line is not.** The lines are approximate 1:100,000 alignments, and
  most of the land along them is private. A line is not public access, a
  property boundary or a precise location of wagon ruts.
- **Failures.** If one NPS layer fails, the others still draw. The feed is then
  labeled `partial` and names the missing trail.

## Rollback

Revert the commit. The change touches no data, settings or provider
configuration. The local companion's official-source cap goes from 57 to 58.
