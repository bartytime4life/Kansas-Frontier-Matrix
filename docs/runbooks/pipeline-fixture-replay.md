# Replay sealed domain pipeline fixtures

The fixed replay harness runs USGS earthquakes, NOAA Storm Events, and USGS
water observations from committed synthetic capture packets. It verifies packet
bounds, exact object closure, preserved-byte digests, capture scope, normalized
record schemas, review posture, and expected candidate identity. It returns the
candidate and its existing domain validation report in memory or on stdout.

From the repository root, with Python 3.11 or later:

```bash
python tools/ci/install_python_ci.py project-test
python tools/ci/install_python_ci.py connectors-core
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
python -B -m pipelines.fixture_replay earthquake
python -B -m pipelines.fixture_replay storm-events
python -B -m pipelines.fixture_replay water-observations
python -B -m pytest tests/pipelines/test_fixture_replay.py -q --strict-config --strict-markers
```

Dependency installation precedes the Python no-network guard. Replay itself
performs no retrieval. The guard denies common Python network paths; it is not
runner-wide or host-wide network isolation. The harness has no output-file,
source-URL, store, publication, or arbitrary-module option. A library caller's
`fixture_only` label is not proof of external provenance.

| Command | Sealed capture | Expected kept records | Candidate limits retained |
|---|---|---:|---|
| `earthquake` | [2025 synthetic month pages](../../fixtures/domains/hazards/earthquakes/replay.json) | 5 | Deleted solutions withheld; context margins flagged; coverage not established |
| `storm-events` | [2025 synthetic listing and details file](../../fixtures/domains/hazards/storm_events/replay.json) | 6 | Invalid rows withheld; narratives omitted; unreported damage stays unknown |
| `water-observations` | [Two synthetic stations and discharge observations](../../fixtures/domains/hydrology/usgs_water_replay/replay.json) | 2 | Provisional measurements and provider revision times retained |

Each packet contains the exact capture manifest, base64 object bytes keyed by
SHA-256, and a golden candidate digest. Earthquake and storm-event packets were
assembled by their existing offline test fetchers. The water packet was assembled
by the synthetic transport in the existing water-normalizer tests. Capture clocks
are fixed; no live provider values or current clock readings are required.

Nonzero exit means replay failed. The CLI writes a JSON failure to stderr for
invalid packets or unreadable fixtures, and argparse rejects unknown pipeline
names. A passing replay is reproducible synthetic evidence only: source admission
and review remain PENDING, release remains UNRELEASED, and promotion, release,
and publication are unauthorized. It does not establish current provider access,
scientific accuracy, full source coverage, installed scheduling, or deployment.

The [declaration workflow](../../.github/workflows/pipeline-spec-declarations.yml)
checks the declaration corpus and runs these replays with the Python guard. Its
triggers include the bound transformations, connectors, schemas, fixtures, source
descriptors, shared byte reader, and test dependencies. Existing domain workflows
continue their broader capture, denial, private-store, and serving tests.

The [declaration inventory](../../pipeline_specs/README.md#current-inventory)
records four implemented fixture-first candidates including the separately tested
WBD HUC12 pipeline, and 35 remaining candidate implementations. Stage boundaries
and aliases stay inactive by their existing contract. This replay build-out does
not claim those remaining pipelines are complete.
