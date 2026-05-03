# eBird Consumer Certification (Layer 28)

## Status

Layer 28 is planned as a **local-only** downstream consumer certification and integration-audit lane for KFM eBird public aggregate artifacts.

## Safety constraints

- Local artifact generation only.
- No network calls.
- No credentials or secrets.
- No real eBird data.
- No exact coordinates or point geometries in public outputs.
- No restricted observations, quarantines, suppression receipts, suppressed hashes, or raw row numbers in public artifacts.
- Certification is compatibility/public-safety only; it is not ecological correctness certification.

## Planned CLIs

- `kfm-ebird-integration-audit`
- `kfm-ebird-consumer-certify`

Both CLIs should support `--help`, `--version`, deterministic IDs, and offline fixture-based validation.

## Planned deterministic IDs

- `audit_id`: first 16 lowercase hex chars of SHA256 over canonical JSON of aggregate target + supplied artifact hashes + adapter version + contract hash + strict mode.
- `consumer_certification_id`: first 16 lowercase hex chars of SHA256 over canonical JSON of aggregate target + consumer ID + audit/certification evidence hashes + decision + validity + adapter version + contract hash.

## Planned public outputs

- Public integration audit summary JSON/Markdown.
- Public consumer certification summary JSON.
- Public compatibility badge JSON/SVG (static, no scripts/links/external assets).
- Public registry entry JSON.

## Planned non-public outputs

- Integration audit manifest/report/lint/route/dto/claims/test/diff/operator report.
- Consumer certification plan/packet/receipt/validation/operator report.
- Registry update and revocation plan (no-delete).
