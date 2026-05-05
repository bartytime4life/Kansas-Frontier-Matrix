# eBird Layer 9 Operations Runbook

This runbook covers `kfm-ebird-observe` for scan, trend, attest, evidence-pack, and incident workflows.

## Safety warning
No eBird downloads, credentials, exact coordinates, restricted observations, quarantines, suppression receipts, or suppressed-group details are published.

## Scan
`kfm-ebird-observe --mode scan --aggregate huc12 --release-receipt fixtures/ebird/releases/huc12/release_receipt.json --published-root fixtures/ebird/published --out-dir /tmp/kfm-ebird-observability/scan`

## Trend
`kfm-ebird-observe --mode trend --aggregate huc12 --release-receipt fixtures/ebird/releases/huc12/release_receipt.json --history-dir data/catalog/fauna/ebird/observability --out-dir /tmp/kfm-ebird-observability/trend`

## Attest
`kfm-ebird-observe --mode attest --aggregate huc12 --release-receipt fixtures/ebird/releases/huc12/release_receipt.json --out-dir /tmp/kfm-ebird-observability/attest`

## Evidence pack
`kfm-ebird-observe --mode evidence-pack --aggregate huc12 --release-receipt fixtures/ebird/releases/huc12/release_receipt.json --out-dir /tmp/kfm-ebird-observability/evidence`

## Incidents
Open: `kfm-ebird-observe --mode incident-open --aggregate huc12 --release-receipt fixtures/ebird/releases/huc12/release_receipt.json --severity medium --summary "Synthetic public safety scan failure for test fixture" --out-dir /tmp/kfm-ebird-observability/incidents`

Update/close use `--incident-id`.

## Layer 10 handoff
Use kfm-ebird-doctor and kfm-ebird-conformance for local acceptance gates.
