# Fauna public-safe migration fixture validator

`validate_public_safe_migration_fixture.py` validates only the synthetic,
no-network candidates in `fixtures/domains/fauna/migration_route/`.

It requires a generalized `LineString`, a bounded synthetic non-wrapping
seasonal window,
fixture-only identities, explicit denial of telemetry and individual-tracking
truth, and unreleased/non-promotable governance state. It fails closed on exact
track precision, malformed or unbounded positions, exact timestamps, undeclared
fields, real-source references, and reversed seasonal windows.

The paired `migration_route.schema.json` remains a proposed permissive
scaffold. This executable does not promote it, validate production routes,
retrieve telemetry, evaluate policy, release a layer, or publish geometry.

```bash
python tools/validators/domains/fauna/movement/validate_public_safe_migration_fixture.py --fixtures
python -m unittest tests.domains.fauna.test_public_safe_migration_fixture
```
