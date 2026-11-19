# Synthetic USGS water replay packet

`replay.json` contains a fixed 2026-09-29/30 one-day capture, two invented station
metadata pages, and two invented provisional discharge observations. Both values
are 12.5 ft³/s at synthetic point coordinates (-98, 38); neither is a measurement.
The capture clock is 2026-09-30T18:01:00Z. Source URLs are inert manifest lineage.

The packet was assembled by `acquired()` in
[the water-normalizer test](../../../../tests/domains/hydrology/test_usgs_water_normalizer.py).
Its base64 bytes are keyed by SHA-256 and its expected candidate ID pins replay
identity. The [fixture harness](../../../../pipelines/fixture_replay.py) validates
closure before transformation. See the
[runbook](../../../../docs/runbooks/pipeline-fixture-replay.md) for commands.

This is fixture data only. It grants no admission, review, storage, release, or
publication authority and provides no current water-condition evidence.
