# Bounded NLCD native-grid fixture ingestion

The [NLCD candidate entrypoint](../../pipelines/domains/habitat/ingest_nlcd.py)
replaces the former empty executable with actual GeoTIFF processing. It verifies
an explicit class-scheme candidate, reads a native grid in memory, preserves
class codes and support, and emits an unreleased LandCoverObservation candidate.
Its CLI exposes aggregate status for two committed synthetic packets.

Use a separate Python 3.12 virtual environment for the locked imagery stack:

```bash
python3.12 -m venv /tmp/kfm-nlcd-fixture-env
/tmp/kfm-nlcd-fixture-env/bin/python tools/ci/install_python_ci.py project-test
/tmp/kfm-nlcd-fixture-env/bin/python tools/ci/install_python_ci.py connectors-core
/tmp/kfm-nlcd-fixture-env/bin/python tools/ci/install_python_ci.py crop-casma-tiles
export KFM_NO_NETWORK=1
export PROJ_NETWORK=OFF
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
/tmp/kfm-nlcd-fixture-env/bin/python -B -m pipelines.domains.habitat.ingest_nlcd base
/tmp/kfm-nlcd-fixture-env/bin/python -B -m pipelines.domains.habitat.ingest_nlcd changed
/tmp/kfm-nlcd-fixture-env/bin/python -B -m pytest tests/pipelines/domains/habitat/test_nlcd_ingest.py tests/validators/domains/habitat/test_nlcd_candidate_schemas.py -q
```

Install dependencies before enabling the guard. The two existing locks share the
same attrs version; this stack uses the tile profile's pyproj 3.8.0. The general
geometry profile pins a different pyproj and is qualified separately. The Python
guard is process-level egress control, not native-library or host-wide isolation.

| Input or output | Bounded meaning |
|---|---|
| Class scheme | Closed `ClassSchemeProfile` candidate, explicit scheme ID/version, source product/vintage, sorted unique canonically encoded integer uint8 codes and declared labels, nodata 0, source-descriptor reference, canonical hash and denied authority |
| Capture metadata | Separate valid-time interval and retrieval instant; valid time ends no later than retrieval; equivalent offsets normalize to UTC |
| Native source | Supplied classic GeoTIFF bytes, at most 8 MiB, one uint8 band, EPSG:5070, north-up finite transform, at most 2,048 per dimension and 1,048,576 pixels; source block sizes are also bounded |
| Pixel support | Nonzero source class and nonzero native mask; mask normalized to 0/1 for its digest; valid plus nodata counts equal grid size |
| Class counts | Exact integer histogram over valid pixels; no interpolation or class recoding; unknown codes are rejected |
| Semantic identity | Source ID, class-scheme hash, native spatial scope, canonical valid time and normalized grid/mask digest |
| Byte identity | SHA-256 of the exact supplied GeoTIFF; recompression may change it while semantic identity stays stable |
| Uncertainty | Classification accuracy, source coverage and vintage-gap assessment remain explicitly unevaluated |
| Authority | Review required; source admission, policy evaluation, lifecycle write, promotion, release, publication and public use remain false |

Library callers use `normalize_capture(source_bytes, class_scheme, capture)` and
receive a private in-memory candidate. `validate_candidate(candidate, scheme)`
checks schema, canonical hashes, identities, scheme binding, support arithmetic
and native-grid consistency. It does not authenticate a provider or recompute
raster counts from a candidate alone. The preparation function computes those
counts directly from the supplied bytes.

The implementation reads self-contained bytes through a GTiff-only MemoryFile;
virtual datasets and network URLs are not accepted. Auxiliary-directory scanning
and PAM are disabled; the native cache is capped. Input/grid bounds are not a
native-code process sandbox. Internal masks and nodata present in the supplied bytes
are honored. Completeness of a provider capture, including any omitted external
sidecar, is not established. No reprojection, resampling, tile delivery, habitat
inference, crosswalk, sensitive join, public generalization or lifecycle storage
occurs.

The [source descriptor](../../data/registry/habitat/sources/nlcd.yaml) remains
proposed with unresolved role, rights and sensitivity. The [fixtures](../../fixtures/domains/habitat/nlcd_ingest/)
use a synthetic product and synthetic class labels, not a reviewed NLCD legend.
The profile does not select or admit an Annual NLCD or legacy NLCD release.
A future source-specific capture must bind its exact product/version, reviewed
legend, rights and provenance through separate review.

The nested [class-scheme](../../schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json)
and [observation](../../schemas/contracts/v1/domains/habitat/land_cover/observation.schema.json)
schemas are closed. The [top-level schema](../../schemas/contracts/v1/domains/habitat/land_cover_observation.schema.json)
is a read-only reference to the nested observation definition. Empty objects and
authority overclaims now fail; validation no longer accepts arbitrary objects.
The [imagery workflow](../../.github/workflows/crop-casma-tile-compatibility.yml)
runs the native tests alongside existing Crop CASMA and historical-topographic
regressions. Lightweight schema tests also run without GDAL.

An additional all-pipeline run in the raster environment reached 330 passing
tests and one existing EPSG:6923 roundtrip failure. It reproduced without the
NLCD module: pyproj 3.8.0 / PROJ 9.8.1 reported that `us_noaa_kshpgn.tif` was
unavailable for its selected operation. The repository's general geometry
profile (pyproj 3.7.2 / PROJ 9.5.1) passes its pipeline suite. The
[PROJ resource guidance](https://proj.org/en/stable/resource_files.html) describes
these separately distributed grids. This build keeps the qualified environments
separate; NLCD preparation reads its native EPSG:5070 grid without reprojection.
No grid download or ballpark transformation is enabled by this pipeline.
