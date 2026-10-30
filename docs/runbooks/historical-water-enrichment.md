# Historical water enrichment from preserved captures

The owner prioritizes useful historical records over adding new live feeds.
This first bounded collection reuses the imported USGS two-station capture for
September 29–30, 2026. Historical age does not make these observations unusable
for their stated period. They remain provisional and cannot establish current
river conditions, warnings or forecasts.

`tools.local_data.historical_water` reads an explicitly pinned private readiness
manifest, verifies all its members, checks the capture/object hashes, and replays
the existing hydrology normalizer and validator. Every CSV row and field must
match the replay, including units, missingness, qualifiers, revisions and record
digests. A rehashed edit to the CSV still fails that comparison. The original
archive is read-only to this procedure; no network request is made.

The output is a versioned WORK review package in a separate initialized private
store: the complete CSV, replayed candidate, provider station geometry, dated
coverage, validation receipt, retained source rights assessment and explanatory
notes. Input, generator, normalizer and validator hashes identify the derivation.
Replaying identical inputs verifies existing output instead of overwriting it.
Source and destination must be separate; static symlinks, changed files, excess
input sizes and unexpected output members are rejected.

From the monorepo, with its Python dependencies available:

```sh
PYTHONPATH=.:packages/connectors-core/src python3 -m tools.local_data.historical_water \
  --source-root /absolute/imported-archive \
  --root /absolute/initialized-working-store \
  --source-manifest data/work/hydrology/SELECTED-PACKAGE/review-manifest.json \
  --manifest-sha256 EXACT_REVIEW_MANIFEST_SHA256 \
  --capture-id sha256:EXACT_CAPTURE_ID
```

Run preparation under the PC's existing shared capture/analysis/backup operation
lock. It also acquires the working store lock. The two roots and identifiers
above are examples, not a live configuration or approval.

The returned `binding` pins the new review manifest. Supply it through the
existing intake service's `--review-package` option. The working desk can inspect
the package using its existing owner session and private review routes; search
and display limits continue to apply. The imported library keeps its own
separate bindings. No public endpoint or release pointer is added.

## Verified local checkpoint

The first real replay matched all 193 observations from two stations against the
saved CSV. The requested and observed interval is September 29 at 18:00 UTC
through September 30 at 18:00 UTC. Provider units remain cubic feet per second;
all observations retain their provisional flags. Station positions are the
published provider geometry, not survey measurements, and are not transformed
again. The package is pinned in the working PC's private review configuration.

These are private preparation and fidelity checks. Source admission, independent
review, activation, release and publication remain pending. The existing dated
rights assessment is retained without creating a new approval.

Validation covers offline/idempotent replay, source and output tampering,
rehashing an edited table, missing values, symlinks, separate destinations,
private review previews and preservation of original bytes. The broader intake,
session, library and health regressions also pass. Reboot acceptance and a full
independent backup of the imported archive remain separate work.
