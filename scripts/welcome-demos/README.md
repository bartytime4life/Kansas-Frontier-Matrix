# Render tours of actual Explorer capabilities

This is local development tooling, not a public endpoint or a real-time
performance benchmark. It exports **120 separate, source-ready frames from the
actual production MapLibre renderer**, then an external encoder turns those
frames into a smooth map tour. Only camera positions and the elapsed time of
illustrative wind trails are interpolated. Source measurements, model values,
source editions, and observation times are never invented or interpolated.

The browser compositor in this environment throttles requestAnimationFrame and
native video capture to approximately one frame per second when its window is
occluded, even with `document.hidden === false`. This was measured separately
from timers (approximately 30 callbacks/second). These exports are therefore
labeled **Rendered map tour**, not recordings of real-time application speed.

## Start the local workbench

```sh
KFM_WELCOME_DEMO_RECORDER=1 npm run dev:local -- --port 5191 --strictPort
```

`app/page.tsx` imports `app/living-welcome/dev-recorder.tsx` only for an explicitly
opted-in Vite development session. The capture sink also requires both Vite's
`serve` command and the environment flag. The opted-in server binds to
`127.0.0.1`; production builds remove the recorder branch and do not install the
sink. Do not expose this development server through a public proxy.

Open `http://127.0.0.1:5191/` through CUA. The workbench fixes the local map
container at 1280×720 native pixels and ratio 1 while rendering, then restores its
prior inline style and normal render-quality ratio on completion or cancellation.
It never enlarges a small source image. Use a sufficiently large browser viewport
so the map and workbench remain readable.

- **Render selected map tour** renders the selected recipe.
- **Render from selected onward** resumes a batch at the selected recipe.
- **Render all 16 map tours** processes two recipes for each of eight categories.
- **Export source preview** saves one labeled frame and its actual layer states.
- **Cancel rendering** aborts waits/uploads and restores the map viewport.
- **Measure 10s browser clocks** measures timers and rAF without copying pixels.

Use an isolated localhost session. No AI request, database change, source
admission or activation is performed. Run only one exporter **per recipe ID**:
raw filenames are fixed and a retry replaces that recipe's files. Preserve a
rejected attempt outside the capture directory before retrying. Disjoint IDs
can be captured separately, but competing GPU work can slow both exporters.

## What each export does

1. Reuse existing production representation, source, terrain and opacity controls.
2. Warm actual start, midpoint and end viewports, then return to the start.
3. For each of 120 camera poses, call public `jumpTo()` and `redraw()`. Inside that
   render event, verify the actual basemap and requested sources have loaded for
   the pose. Retry only pending sources for up to 10 seconds; unrelated hidden
   sources do not block the tour. An explicit provider failure rejects the tour.
4. Copy that same source-ready native render to a 1280×720 frame canvas. Add the
   real production wind painter when applicable and source/date/limitation/
   attribution captions, then synchronously export bounded JPEG at 0.9 quality.
   This is a new geographical render at every pose, not a distorted still image.
5. Await each frame's local save before advancing. The wind tour pins a verified
   forecast grid with its original valid/retrieval times. Trail motion uses that
   actual grid and does not represent measured wind parcels.
6. Mark the manifest complete only after all 120 frames and final source checks
   pass. Failures retain only incomplete local output.

Local capture disables ambient effect timers and display raster fades only in
its own map session. Public `redraw()` supplies timestamp zero, so ordinary tile
fades would otherwise remain transparent. This does not change source raster
values or production defaults. Terrain uses the existing Mapzen provider at
1.0× vertical display. The 1918 tour uses opaque orange dashed KDOT route lines
on explicitly modern imagery; it is not a 1918 landscape reconstruction.

Warm-up is bounded at 60 seconds per viewpoint and frame export at 20 seconds.
Status reports actual frame count, phase timings and wall time, without a
real-time fps claim. Cancel/unmount clears pending waits/listeners and restores
the viewport, render-quality ratio and repaint setting.

## Raw outputs and metadata

All raw files are outside Git and deployment assets:

```text
/tmp/kfm-welcome-demo-recordings/weather-1.frame-000.jpg
...
/tmp/kfm-welcome-demo-recordings/weather-1.frame-119.jpg
/tmp/kfm-welcome-demo-recordings/weather-1.json
/tmp/kfm-welcome-demo-recordings/weather-1.png
```

The JSON includes:

- `kind: "rendered-software-tour"` and `state: "complete"` only after success.
- `frameCount: 120`, `playbackFps: 24`, `durationSeconds: 5` before endpoint holds.
- Actual `captureWallSeconds`, independent of intended playback duration.
- Measured `nativeMapViewport` CSS/backing dimensions and pixel ratio.
- Start/end camera, requested source IDs, source clocks, attribution and limits.
- Actual captured layer visibility, opacity, order and source-loaded state.
- `frameBytes` for all 120 inputs, first-three-frame phase timings and
  `annotations: "burned-in"`.

The PNG is the transparent caption overlay for inspection. Captions are already
burned into the JPEG frames; **do not overlay them again**. A preview writes
`.preview.jpg`/`.preview.json` and never marks a complete video. Older
`.rejected.webm`/`.rejected.json` files are failed real-time diagnostics, not tour
inputs or public assets.

The sink accepts only exact known IDs, `frame-000` through `frame-119`, loopback
same-origin POSTs, valid image signatures and at most 2 MB per frame. It rejects
arbitrary paths, queries, unknown IDs, excess frames and unexpected content
types. Writes use fixed temporary filenames and atomic rename.

## Review and package

Require a complete manifest, exactly 120 consecutive frames, correct native
resolution and expected source clocks. Inspect first/middle/last frames: the
relevant layer must actually be visible and useful, not just selected or loaded.
Reject blank output, absent source detail, clipping and misleading dates. Missing
data must never be replaced with invented content.

The portable packager requires an external `ffmpeg` binary and Python Pillow;
no encoder dependency belongs in the application. Package to a staging directory:

```sh
python3 scripts/welcome-demos/package-rendered-tours.py \
  --raw /tmp/kfm-welcome-demo-recordings \
  --output /tmp/kfm-approved-map-tours \
  --ffmpeg /path/to/ffmpeg
```

It verifies input dimensions/byte counts/distinct frames, preserves ordered
SHA256 input hashes and exact encoder settings, and encodes all 120 actual
frames at 24 fps with one-second endpoint holds: 168 frames, seven seconds.
Only endpoint holds repeat frames; it synthesizes no intermediate source values.
The final poster comes from the encoded output. `--allow-incomplete` packages
available complete recipes while work continues; a full runtime manifest is
written only when all 16 recipes are complete.

Review final playback and decoded duration/frame count before copying approved
WebM/poster files to `public/welcome/demos/`. Retain capture wall time separately.
Keep raw inputs and rejected attempts outside public delivery. Rendered provider
data must never be labeled live. Modern reference services are not historical
reconstructions, and classified KGS estimates are not present conditions, parcel
measurements or well-yield advice. Source admission, activation and publication
remain distinct.
