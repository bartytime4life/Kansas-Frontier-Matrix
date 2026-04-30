# EBIRD MAINTENANCE (Layer 11)
Layer 11 adds contract diff/check, compatibility testing, deprecations, inventory/reporting, and migration plan/apply/verify.

- `kfm-ebird-maintain --mode diff|check|compat-test|deprecate|maintenance-report|inventory|public-safety-scan`
- `kfm-ebird-migrate --mode plan|apply|verify`

Migrations are copy-on-write by default. Never publish exact coordinates.
