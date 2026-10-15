# Statewide flowing water and direct effects controls — October 14, 2026

This candidate starts from public composition 7ec66876075b32746e6f3d2a0568351beb0b25bd and local composition 88a8332a8c86eeedde8fc646a58473a8fbb35696. Both prior core repairs, account operations, Underground controls and retained source assets are preserved. It changes display requests and navigation, not source admission or release state. The original native Site is separate.

Effects is now beside Layers in the top map toolbar. Its shared controls expose Flowing water first, rendering quality and ambient motion. Light, land and camera remain available in an advanced section; Appearance uses the same saved settings. The previous floating Scene control is removed from the map. Escape and outside-click close behavior remain in the shared panel.

## Source-bounded detail

Official USGS layer-50 metadata was inspected this session and advertises streamorder. The existing adapter still requires the explicit downstream flag and allowed feature types. It never infers direction or discharge from stream order, names, terrain or visual width.

| Map zoom | Display selection | Fixed cells | Provider stream-order filter | Display simplification |
| --- | --- | --- | --- | --- |
| 4.5 to below 8 | Major rivers across the Kansas view | 2 degrees, at most 12; a full Kansas overview uses 8 | 6 and higher | 0.001 degrees |
| 8 to below 10 | Rivers and tributaries near the camera | 0.5 degrees, at most 12 | 4 and higher | 0.0005 degrees |
| 10 and closer | Local directed channels | Existing 0.25 degrees, at most 9 | All returned directed channels | Existing 0.0002 degrees |

Simplification is a display derivative, roughly 100/50/20 metres in latitude, not improved survey accuracy. Original vertex order controls the animation. Widths are screen-space presentation widths, not physical channel widths or wet extent. Stream order ranks drainage topology, not measured flow. A named river may have gaps where directions, coverage or returned data are missing.

Legacy local-cell requests and v1 payloads remain compatible. Optional detail and streamOrder fields identify ranked profiles. Cache identities include the profile, and mismatched source responses fail closed. Requests remain restricted to fixed Kansas cells, the existing source, a 30-second deadline, 6 MB and 400 returned reaches. Redirects are not followed. Truncation, a restricted view selection and the existing 60,000-segment drawing budget remain disclosed. Failed cells keep the existing retry delay, abort and stale-response guards.

Gauge emphasis is applied only at local detail, where the prior geometry/snap rule is unchanged. Generalized overview/regional lines never borrow gauge measurements. Gauge points and their actual values remain independent. Motion is the same illustrative direction speed; reduced motion holds it still and Battery saver withholds the effect.

A bounded live source probe of one major-river cell returned 400 features, stream orders 6/7/9, 84,962 bytes in 6.1 seconds, with truncation true. This confirms compatibility, not full Kansas coverage or a general timing guarantee. No acquisition package or approved evidence was created.

## Placement and runtime

Directory Rules v2, accepted by ADR-0029, place the consumer/adapter in the existing app responsibility, local dispatch in scripts, regression checks in tests and this behavior record in docs. No new schema, source, dataset, registry or release authority root is created.

The local composition routes only the exact stateless /api/hydrology/flowlines path to its checked Node adapter. Other hydrology, governed APIs and existing D1/R2 data remain in the retained native API capsule. Origin and injected-owner-header rejection are unchanged; no store is migrated or reseeded.

## Validation and rollback

Candidate build/type, focused/full-suite results, installed browser observations and GitHub checks are recorded separately on its PR. Until those observations are appended, this document makes no executed browser or hosted acceptance claim. Hosting publication is separate and remains subject to the existing GoDaddy gateway/session issue.

Rollback restores the privately preserved prior source/build in the same local installation. The existing scene-effect preference key remains compatible; switching Flowing water off stops its requests and animation. No stored source data requires rollback.


### Reviewed boundary correction

Automated review flagged that the fixed query envelope extended into narrow strips rejected by the old geometry validator. The shared server/client geometry envelope now covers the entire fixed-cell extent while retaining the older eastern compatibility margin. The new regression passes actual adapter output through the client validator for west/south/north edge coordinates, asserts the provider coordinates are unchanged and still rejects points beyond the bounded envelope. No clipping, stretching or invented connectors are introduced.


### Executed candidate validation

The reviewed boundary revision passes build/TypeScript, 73 focused public source/menu checks and 220 local composition checks. The public mixed-runtime suite reports 1,156 passes, 47 failures and one skip; the untouched 7ec6687 base reports 1,150 passes, the same 47 failure names and one skip. Those inherited failures remain unresolved, and this is not a full-suite green claim.

Installed local browser observations before the boundary follow-up: 2,890 directed major-river reaches at the Kansas overview, 3,418 regional reaches and 2,311 local reaches (three gauge cues at local detail). All three displayed incomplete-coverage notices. Two captures of a fixed blue river region showed visual change during motion; the paused region was substantially still. This is no FPS, latency, hydraulic-velocity or device benchmark. The exact boundary fix still requires installed readback, recorded separately on the PR.

The 390-pixel layout had no document overflow. Its Effects dialog stayed inside the viewport; keyboard focus reached the lower Light, land & camera action by scrolling its own panel. Escape returned focus to Effects. Battery saver paused water as intended. The temporary viewport and the original rendering/ambient/flow preferences were restored. Six external OpenFreeMap glyph 404 warnings used local glyph fallback; no app/shader error was captured. Full physical-device, reduced-motion emulation, long-session and hosted acceptance remain separate.
