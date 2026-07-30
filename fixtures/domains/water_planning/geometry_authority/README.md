# Water-planning geometry-authority fixtures

Synthetic, public-safe envelopes for the deterministic checks in
`tools/validators/domains/water_planning/validate_geometry_authority.py`.

The valid fixture freezes the 14 public KWO RAC names and a KFM-assigned
`kwo-rac-01` through `kwo-rac-14` ordinal inventory. The KWO page is the name
source; the numeric suffix is explicitly not represented as a KWO-native ID.
The identity-authority digest covers the authority metadata plus the ordered
`region_id`, `rac_number`, and `name` tuples.

Geometry and county-crosswalk authority records are synthetic,
reference-only test records. They contain version, digest, correction, and use
boundary metadata but no coordinates, polygons, county membership, or other
geometry payload. They do not create records in `data/registry/`, admit a
source, construct proof, or authorize release or publication.

Run:

```bash
python tools/validators/domains/water_planning/validate_geometry_authority.py \
  fixtures/domains/water_planning/geometry_authority/valid/valid_1.json

python -m unittest discover \
  --start-directory tests/domains/water_planning \
  --pattern 'test_geometry_authority.py' \
  --verbose
```

The CLI returns zero only for its declared validation scope. Findings use
finite codes and JSON paths, are sorted deterministically, and do not echo
input values.
