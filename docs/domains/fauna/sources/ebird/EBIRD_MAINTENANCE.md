# EBIRD MAINTENANCE (Layer 11)
Layer 11 adds contract diff/check, compatibility testing, deprecations, inventory/reporting, and migration plan/apply/verify.

- `kfm-ebird-maintain --mode diff|check|compat-test|deprecate|maintenance-report|inventory|public-safety-scan`
- `kfm-ebird-migrate --mode plan|apply|verify`

Migrations are copy-on-write by default. Never publish exact coordinates.


## Layer 12 federation/export
See `docs/domains/fauna/EBIRD_FEDERATION.md` for federation index, discovery, semantic graph, STAC-lite/RO-Crate-lite/warehouse/search exports, and public-safety constraints.
