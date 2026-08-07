# Structural GeoJSON Feature Digests

**Status:** implemented on main by merged PR #2099; validation and receipt integrity remain governed by `.github/workflows/spec-hash.yml`.  
**Authority:** none. Digest equality is integrity evidence under a declared profile, not evidence, policy, review, release, publication, or public-use authority.

## Purpose

`packages/hashing/src/hashing/geojson.py` implements the bounded `kfm-geojson-feature-digest-v1` profile derived from the attached *New Ideas.pdf* pattern for separate geometry and record digests.

For one GeoJSON `Feature`, it emits:

- `geometry_sha256`: hashes only the normalized geometry subject plus the declared CRS and coordinate precision.
- `record_sha256`: hashes `geometry_sha256`, filtered `properties`, the same profile inputs, and optionally the top-level Feature `id`.

Both identifiers use the repository's current executable `sha256:<64 lowercase hex>` grammar and RFC 8785 JCS implementation.

## Directory Rules basis

- Reusable deterministic implementation: `packages/hashing/src/hashing/`.
- Operator/CI command surface: `tools/spec_hash/spec_hash.py`.
- Executable tests: `tests/validators/test_validate_spec_hash_geojson.py`.
- Workflow orchestration: `.github/workflows/spec-hash.yml`.
- Authoring receipt: `data/receipts/generated/`.

No parallel schema, contract, policy, registry, receipt, proof, release, or publication home is created.

## Declared profile

The caller must provide a non-empty CRS label and may select a coordinate precision from 0 through 15 decimal places. The default is 7. Finite coordinates are quantized with decimal round-half-even semantics; negative zero becomes zero. JSON object order is removed by RFC 8785 JCS.

The profile supports `Point`, `MultiPoint`, `LineString`, `MultiLineString`, `Polygon`, `MultiPolygon`, `GeometryCollection`, and a Feature-level null geometry. It strips geometry foreign members such as `bbox` from the geometry hash domain.

Top-level property exclusions are **never inferred**. Volatile fields affect `record_sha256` unless named with repeated `--exclude-property` options. Feature `id` is excluded by default and included only with `--include-feature-id`.

## Command

```bash
python tools/spec_hash/spec_hash.py geojson-feature feature.json \
  --crs EPSG:4326 \
  --precision 7 \
  --exclude-property updated_at \
  --include-feature-id
```

A successful report contains the profile, CRS, precision, separate digests, explicit exclusions, Feature-ID posture, `authority: NONE`, and the established non-effects list. Invalid JSON, unsupported geometry, missing Feature fields, invalid coordinate nesting, non-finite numbers, empty CRS, or out-of-range precision returns exit code `2` and a bounded failure status.

## Deliberate non-capabilities

This implementation does not:

- reproject coordinates;
- repair or validate topology;
- rotate polygon rings or canonicalize line direction;
- sort geometry collections or feature collections;
- establish topological or real-world spatial equivalence;
- choose object-family volatile fields automatically;
- create SourceDescriptors, EvidenceBundles, PolicyDecisions, receipts, proofs, signatures, release manifests, or published artifacts.

A domain requiring those transforms must define, version, review, and test its own pre-hash normalization contract before using this generic structural profile.

## Validation

Focused tests cover a stable golden vector, key-order and sub-precision invariance, separate geometry and record domains, explicit property exclusions, CRS/precision/Feature-ID binding, input immutability, fail-closed invalid input, deterministic CLI output, and the no-authority boundary.

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_spec_hash*.py' \
  --verbose
```

## Rollback

Revert the additive implementation commit. The slice performs no source activation, data migration, release, publication, cache change, or public lifecycle transition.
