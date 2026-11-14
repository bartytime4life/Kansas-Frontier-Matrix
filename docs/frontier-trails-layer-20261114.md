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
- **Trails west starter.** It turns on the trails, trail sites,
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
- **Links** are clickable in the site drawer and kept only when they use HTTPS
  and point to `nps.gov`, `kshs.org` or `kansasmemory.org` (including `www`).
  Invalid or overlong links are omitted rather than shortened into another URL.
  The same validator runs in the adapter and in the drawer.
- **History** preserves the feed's full bounded excerpt of up to 900 characters;
  other drawer fields retain their existing 240-character display limit.
- **Bounds and completeness.** The query orders by `OBJECTID`, requests at most
  301 rows and emits at most 300 unique sites. Unsafe or duplicate identifiers
  are omitted and disclosed. An upstream transfer-limit flag, including the
  GeoJSON `properties.exceededTransferLimit` form, produces `partial` and
  `truncated: true` even when fewer than 300 sites are returned. Downloaded
  GeoJSON retains that partial-state label and limitation.
- **Initial PR live check (November 14):** the contributor reported 96 sites,
  with 16 private sites and 6 sites on other corridors left out. That dated
  provider observation is separate from the synthetic repair tests below.

## Source and safety boundaries

- **Trail-line rows requested.** For the two line layers that carry access fields, the adapter
  asks only for rows marked `PUBLICDISPLAY='Public Map Display'` and
  `DATAACCESS='Unrestricted'`.
- **Trail-line fields requested.** Only the identifier, trail name, alternate name and
  mapped accuracy. The free-text `NOTES`, editor, user and `GlobalID` fields
  are never requested, and a test checks this.
- **Clipping.** National trails are clipped to the line parts that touch the
  Kansas window, so a part may run a little beyond the state line.
- **What a line is not.** The lines are approximate 1:100,000 alignments, and
  most of the land along them is private. A line is not public access, a
  property boundary or a precise location of wagon ruts.
- **Failures.** If one NPS layer fails, the others still draw. The feed is then
  labeled `partial` and names the missing trail.

## PR #5844 repair verification

The repair reconciles original candidate `16aa698b1c1ac49817672ba5086944397344ee53`
with hosted base `aad6064`, preserving the merged WIHA public-record correction
in PR #5845. It does not merge the trail feature into the hosted branch or publish it.

Regression checks reproduced the original false-complete transfer-limit label,
duplicate and unsafe map identifiers, and absent deterministic ordering. A
separate check reproduced a 543-character history being cut to 240 characters
and the site record URL being rendered as non-clickable text.

The focused repair tests cover both transfer-limit placements, unique and safe
IDs, the input and marker caps, URL validation, the full bounded history,
production drawer link markup, marker visibility and opacity, zoom-8 labels,
GeoJSON attribution and partial-state metadata, and failed download responses.
All use synthetic fixtures; provider availability and public deployment are
separate acceptance states.

## Rollback

Revert the commit. The change touches no data, settings or provider
configuration. Trail lines raised the local companion's official-source cap
from 57 to 58; trail sites raise it from 58 to 59.
