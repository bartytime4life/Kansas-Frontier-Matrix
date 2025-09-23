# Checks & Reproducibility

## Validation

- `make stac-validate`
- `kgt validate-stac stac/items --no-strict` (or strict with `jsonschema`)

## Provenance

- Stamp `_meta.json` for processed outputs (origin, command, timestamp, hash)
- Add `checksum:sha256` to COG assets when files exist

## CI Notes

- Validate STAC in PRs
- Publish `web/` on `main`
- Keep sources & STAC small initially (one county), then scale
