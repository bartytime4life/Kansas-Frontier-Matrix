# Fauna public-safe range fixture validator

`validate_public_safe_range_fixture.py` validates only the synthetic candidate
profile in `fixtures/domains/fauna/range_polygon/`.

It requires:

- synthetic fixture, source, taxon, range, and evidence identities;
- no network access, release, promotion, or policy/review claim;
- a finite closed GeoJSON-style Polygon carrier;
- `public-safe-synthetic` precision with an explicit synthetic generalization
  method; and
- explicit denial of occurrence and absence truth.

It fails closed on undeclared fields, non-synthetic references, malformed or
unbounded polygon positions, open rings, exact precision, missing derivation,
unsafe sensitivity posture, or any occurrence/absence truth claim.

The paired `range_polygon.schema.json` remains a proposed scaffold. This
validator does not promote it or validate production `RangePolygon` records.
It does not retrieve data, resolve evidence, evaluate policy, release a layer,
or publish geometry.

```bash
python tools/validators/domains/fauna/range/validate_public_safe_range_fixture.py --fixtures
python -m unittest tests.domains.fauna.test_public_safe_range_fixture
```
