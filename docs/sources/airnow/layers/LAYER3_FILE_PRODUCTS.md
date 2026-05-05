# AirNow Layer 3 File Products

Local-only offline parser layer for already-local file-product fixtures. No HTTP/FTP/API calls, no ZIP web-service loops, no publication.

## Product support
- hourly_aq_obs: supported fixture parser
- daily_data_v2: supported fixture parser
- monitoring_site_locations: supported fixture parser
- cityzipcodes_lookup: synthetic header-driven parser (**NEEDS_VERIFICATION** for exact upstream header)
- reportingarea_candidate: manifest-defined candidate parser only (**NEEDS_VERIFICATION** for official layout)

## Governance
- AirNow data are preliminary and subject to change.
- Not for regulatory decision-making.
- reportingarea.dat layout intentionally abstains without explicit `field_order`.

## CLI
`python tools/air_quality/airnow_parse_file_product.py --manifest <manifest.json> --out-dir /tmp/out --created-at 2026-01-01T00:00:00Z`
