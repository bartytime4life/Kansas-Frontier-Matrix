# Historical NOAA climate normals for private enrichment

The owner prioritizes useful historical context over new live feeds. This bounded
collection reuses the preserved NOAA 1991–2020 monthly station normals capture.
These are calendar-month climate aggregates, not current weather, forecasts, an
annual time series, or an interpolated climate surface.

`tools.local_data.historical_normals` takes exact pins for a WORK readiness
manifest and the original capture manifest. It verifies the capture identity,
reads at most 1,000 station files plus the inventory (32 MiB total), and replays
the existing NOAA parser and normalizer. Every field of both selected CSV tables
must match that replay, including source URLs, retrieval dates, raw tokens,
measurement/completeness flags and contributing years. An absent station element
is counted separately from a published element whose value is missing. Neither
is converted to zero.

Only the two tables and dated rights assessment are selected from the old
readiness packet. Other members, including its transformed maps and prior
accuracy claims, are not republished or represented as freshly verified.
Coordinates remain native NAD83 table fields; the helper produces no GeoJSON or
new coordinate transformation. Generator, parser, normalizer and canonicalizer
hashes accompany the source and capture pins.

Run from the monorepo with Python's standard library:

```sh
python3 -m tools.local_data.historical_normals \
  --source-root /absolute/imported-archive \
  --root /absolute/initialized-working-store \
  --source-manifest data/work/atmosphere/SELECTED-PACKET/review-manifest.json \
  --manifest-sha256 EXACT_SOURCE_MANIFEST_SHA256 \
  --capture-id sha256:EXACT_CAPTURE_ID \
  --capture-manifest-sha256 EXACT_CAPTURE_MANIFEST_SHA256
```

Use the PC's existing shared capture/analysis/backup lock. The helper also locks
the working store. The source archive stays untouched; the destination must be a
separate initialized store. Static symlinks, invalid hashes, changed members,
excess sizes and unexpected output members are rejected. Repeating identical
inputs checks immutable existing bytes rather than overwriting them.

The resulting WORK package contains two CSV tables, candidate, coverage,
validation, retained rights assessment and README. Add its returned binding to
the private intake service's existing `--review-package` list, preserving prior
bindings. The existing authenticated, bounded review previews apply. This adds a
private review collection; it does not add records to the general raw-intake
index or change the live capture allowlist, timers or public website.

## Verified archive checkpoint

Fresh offline replay reproduced candidate
`sha256:03eea29f4f55872d2fda4a8e8a1974267dc796cfa0568cb6e71fa433f93c2e06`
from 569 captured objects totaling 11,123,202 bytes, captured October 1, 2026.
Both archived tables matched all 568 Kansas stations × 12 months: 13,632 cells.
Temperature and precipitation retain degF and inches respectively. The original
normal period is 1991–2020 regardless of capture or review date.

Tests cover offline/idempotent replay, missing versus unpublished elements,
flags, unchanged originals, rehashed edited tables, pinned manifests, raw bytes,
capture identity, input limits, symlinks, immutable output and private previews.

Admission, activation, independent source review, release and publication remain
pending. The retained source rights notes are dated evidence, not a new approval.
Full independent backup of the imported archive and reboot acceptance remain
separate work; the new working package uses the established working-store backup
and restore checks.
