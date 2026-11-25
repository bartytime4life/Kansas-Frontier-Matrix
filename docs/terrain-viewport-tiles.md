# Terrain cells across the visible map

The optional Ground, Surface and Canopy cell layer uses adjoining, stable
Web Mercator request tiles across the full visible map bounds. It no longer
acquires a single center window or pins that window after a camera inspection.
Base landscape remains independently available without a cell overlay.

Ground chooses a pyramid level with at most 12 visible tiles (8 in lightweight
mode). Native modes retain up to 12 initial tiles on either device policy so a camera tilt cannot silently drop a supported viewport; lightweight geometry still targets 150,000 vertices. Native tiles start at level 16 or finer, keeping each complete native
analysis within the existing 1 km² limit. A native source-budget result can
subdivide into four adjoining children, to level 18 and at most 24 tiles in the
view. This is additional acquisition, not interpolation. Wider native views
ask for a closer view. Actual missing/classification support remains missing.

Two source acquisitions run at a time, prioritized near the actual map target rather than a distant oblique-bounds midpoint. A transient failed tile gets one delayed recovery attempt; targeted retry leaves successful tiles intact. Stable overlapping tiles and bounded
in-memory receipts are reused during pans. Old jobs outside the new plan are
canceled; obsolete completions cannot restore coverage. The existing bounded
public browser cache remains expendable and does not renew source timestamps.

All visible grids share one worker-prepared vertex buffer and one terrain
color/picking framebuffer. The existing 300,000-vertex limit remains aggregate;
lightweight preparation targets 150,000. Rendering remains bounded at 4 Mi
pixels, or 1 Mi in lightweight mode. Display LOD uses exact representative
source samples with larger visual footprints. Any display block containing an
unsupported source cell is omitted. Readings retain the original tile and cell
ID and unscaled values. A common mosaic color domain prevents independent
per-tile color legends. Scientific derivatives run in the preparation worker.

Loaded tiles remain readable as adjoining tiles arrive. Camera movement pauses
picking. Geometry and ID attachments always change together. A changed source
receipt for an existing query prepares new geometry; progress-only replies do
not. The rise animation remains one-shot user intent and does not replay on
automatic tile arrivals or pans. Reduced motion and lightweight drawing remain
static. The Base landscape action releases both cell and raw point graphics.

The source metadata and terrain-study download describe the selected tile.
Ground is a provider-resampled USGS 3DEP mosaic, not uniformly native LiDAR.
Native surface and canopy retain their existing same-survey support rules.
Display pedestals are not subsurface measurements; DEM registration and
independent scientific accuracy remain unverified. First acquisition still
requires upstream processing; no fixed latency or universal source coverage is
claimed.

Regression coverage includes full viewport bounds, stable overlap reuse, two-job
concurrency, automatic bounded native subdivision, source ID mapping across
multiple tiles, shared vertex limits, NoData blocks, canceled/hidden/late work,
same-query source refresh, independent clean landscape, and camera inspection
without a center-window lease. Real-data browser verification and hosted source
identity remain separate release checks.
