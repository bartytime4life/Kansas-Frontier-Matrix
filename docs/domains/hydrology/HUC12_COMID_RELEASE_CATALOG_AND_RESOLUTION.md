# HUC12⇄COMID Release Catalog and Resolution

## KFM Meta Block v2
- Domain: Hydrology
- Layer: HUC12⇄COMID release catalog and resolver
- Network posture: fixture-only, no live WBD/NHD fetch
- Status: implemented with policy + schema + validator + resolver tests

This layer governs promotion from validated manifests into catalog/triplet records. Raw manifests are not client-resolvable; only `published` catalog records with evidence bundles are.

Stable IDs:
- `manifest_id = huc12@<snapshot_id>::<spec_hash>`
- `timeslice_id = huc12::<snapshot_id>::<YYYYMMDD>-<YYYYMMDD>`

Evidence Drawer fields are surfaced from catalog records and mirrored verbatim for client display.

Promotion gates enforce:
- catalog record + evidence bundle present
- digest and ID alignment across manifest/catalog/evidence
- run receipt and bundle signature verification
- steward review approval when required
- lifecycle leakage bans (`/raw/`, `/work/`, `/quarantine/`)
- overlap conflict denial

Rollback/correction behavior:
1. Revoke the bad catalog record (`release_state=revoked`).
2. Preserve prior receipts/evidence immutably.
3. Publish corrected record with new evidence bundle.
4. Never silently mutate historical evidence.

NEEDS_VERIFICATION:
- Exact long-term canonical storage URI prefixes for published hydrology artifacts.
- Operational steward identities and signing trust roots.
