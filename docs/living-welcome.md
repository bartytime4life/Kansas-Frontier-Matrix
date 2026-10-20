# Living welcome integration · 2026-10-20

The accepted living welcome is integrated into the standalone public Explorer
on `a0-hosted-ai-web-20261017`, starting at
`ad37e47a1192a8e70786b76c85da6e64ac5f4019`. The preserved private Site and the
monorepo application remain separate. This source change does not publish a
GoDaddy release or change database, model, account, DNS or hosting settings.

## Real application connections

`app/explorer-guide.tsx` retains first-visit dismissal, blocked-storage handling,
URL-aware startup, the **?** entry point and all original question starters.
Its lazy living welcome uses the existing live map; the prototype's sample
basemap, fake place results and example AI implementation are not imported.
The old guide remains the loading fallback and **All questions & tools** view.

| Welcome entry | Existing application destination |
| --- | --- |
| County/place search | Indexed Find composer with the entered query |
| Ask the atlas / header Ask AI | Existing Ask composer, without sending a question |
| Weather & skies | Weather source workspace |
| Follow the rivers | Water source workspace |
| Science & land | Science source workspace |
| Look underground | Groundwater sources; separate Underground Explorer action |
| History & time | History source workspace |
| Roads & Rail | Transport source workspace |
| Farming | Agriculture source workspace |
| Government | Land ownership and public-land source workspace |

Topic actions filter the source catalogue without selecting layers, changing
the map year or claiming that a dataset has been admitted. The feature guide
links to these same destinations; **Coming** opens current source coverage.

## Motion and source materials

The 30 accepted scenes use 90 packaged files in `public/welcome/motion/`,
**82,380,456 bytes** in total. Their hashes match the accepted prototype.
`scripts/welcome-history/runtime-assets.json` records every path, byte count and
SHA-256. Each scene's artist, original source, location, adaptation, dimensions,
license and license URL remain in `app/living-welcome/motion-clips.json` and
are visible in the credits. Example footage is not a live observation and
non-Kansas locations are labeled. Recheck rights before adding new material.

History contains Bleeding Kansas, the Lawrence raid, Mine Creek, Nicodemus,
the Dust Bowl and Brown v. Board of Education. These are archival images with
1080p30 animated schematic locators and timelines, not filmed historical
events. They use today's Kansas outline and approximate place positions.
Historical references remain in `app/living-welcome/kansas-history.json`.

To maintain these chapters, `scripts/prepare-kansas-history.py` reads those
records and the six original plates under
`scripts/welcome-history/source-images/`. `archive-sources.json` alongside them
preserves retrieved rights and attribution metadata. These are authoring inputs,
not public runtime assets. With Python, Pillow, DejaVu fonts and FFmpeg available:

```sh
python scripts/prepare-kansas-history.py /path/to/ffmpeg
```

An optional list of asset names after FFmpeg regenerates only those chapters.
The script produces the HD video, small preview and poster. It does not download
new sources. Update the asset manifest deliberately after regeneration.

The player retains source proportions, crossfades posters, runs at most two
small idle previews and one HD focused scene, and pauses background scenes for
the detail popup. An explicit pinned scene takes priority over passive focus.
The existing Effects control and welcome pause control share a preference.
Reduced motion and document visibility pause both video and the feature guide.
Offscreen previews do not run. No shader warping or per-frame pixel rendering
is used. The header guide holds text for seven seconds and transitions for
1.15 seconds, with hover/focus and manual navigation controls.

The feature guide schedules only the two transition deadlines, replacing its
50 ms polling interval. A normal 8.15-second cycle needs two timer callbacks
instead of 163 in a deterministic before/after clock replay. Hidden tabs cancel the pending timer; returning starts a
fresh seven-second reading interval. Pause, reduced motion, hover/focus and
manual navigation cancel or reset the same schedule. This is a bounded timer
reduction, not a measured map FPS or whole-application CPU improvement. Component
tests verify deadlines, suspension, manual reset and cleanup; browser rendering
and physical-device acceptance remain separate.

## Pending data and database alignment

The hosted branch already has the bounded Node/MySQL ingestion adapter in
`server/ingestion-store.mjs`. Its TLS, admission, source-date, capacity and
review checks remain authoritative. The prototype's optional SQLite server,
migrations and fixtures are not imported. No credentials or live database
connection are needed for the welcome to work.

For future coverage, add reviewed data through that existing source/ingestion
path, then update the typed destinations in `app/living-welcome/features.ts`
and scene metadata as appropriate. Keep presentation metadata separate from
observations. A future remote scene catalogue must validate bounded records
against known categories and approved local media; it must not execute database
HTML, scripts, arbitrary media URLs or model instructions. Do not advertise a
pending dataset as connected based on a visual preview.

## Validation and delivery boundary

The focused startup, guide navigation, map starters, interface, welcome handoff
and playback suite contains 45 tests. Browser checks cover all 30 decoded,
advancing clips, real Find/Ask/topic handoffs, pause and responsive layouts.
Type checking and a production build are required for the final integration.
This is a repository candidate; local checks do not establish deployment or
production browser acceptance. Roll back by reverting this feature's commits;
no database rollback or provider-setting change is involved.
