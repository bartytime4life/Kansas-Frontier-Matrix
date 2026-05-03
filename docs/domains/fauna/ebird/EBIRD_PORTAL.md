# eBird Layer 14 Portal and Downloads

Layer 14 adds public-safe static portal generation and public download bundle manifests from already-public artifacts only.

- No eBird downloads.
- No credentials/API keys.
- No network calls, trackers, or remote scripts.
- No exact coordinates, restricted observations, quarantines, suppression receipts, or suppressed-group details.

## CLIs
- `kfm-ebird-downloads` (`build|validate|report|diff`)
- `kfm-ebird-portal` (`build|validate|link-check|safety-scan|report|diff`)

## Deterministic IDs
- `download_bundle_id`: sha256 over canonical bundle inputs.
- `portal_id`: sha256 over canonical portal inputs.

## Safety
Portal HTML includes restrictive CSP and uses local assets only.
