# eBird Independent Verification (Layer 32)

Layer 32 adds local-only verifier kit generation and offline verification reports.

- No network calls.
- No credentials or secrets.
- No real eBird rows or boundary geometries.
- Exact points remain restricted.
- Public verification covers governance/public-safety artifacts only.

## Workflows
1. Build kit: `kfm-ebird-verifier-kit --mode build ...`
2. Verify offline: `kfm-ebird-verify-offline --mode run ... --strict`

## Deterministic IDs
- `verifier_kit_id`: SHA-256 canonical-json recipe from aggregate targets, input hashes, bundle, adapter version.
- `verification_id`: SHA-256 canonical-json recipe from kit/proof/checksum hashes + strict + adapter version.

## Artifacts
- verifier manifest
- proof index
- checksum inventory
- invariant checklist
- audit handoff
- offline verification report
- failed-proof diagnostics

## Safety
Verifier bundles must never contain exact coordinates, restricted observations, quarantines, suppression receipts, suppressed group hashes/details, or raw rows.
