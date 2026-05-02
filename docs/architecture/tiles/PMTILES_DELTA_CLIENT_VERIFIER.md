# KFM Meta Block v2
- object_family: delta_apply.v1
- status: draft
- updated_at: 2026-05-01

Purpose: fail-closed client verification and apply engine for PMTiles delta manifests.

Uses `delta_manifest.v1` schema/validator, verifies digest/tombstone semantics, replay/time-order checks, and emits governed apply receipts.

Fixture model: JSON tile stores (`base_tile_store.json`, `delta_tile_store.json`) with base64 payloads; no real PMTiles binary required.

Digest rules: added/modified digest = SHA-256(decoded payload). Removed digest = SHA-256 canonical tombstone JSON with sorted keys and compact separators.

Verifier behavior: schema + semantic checks, spec hash binding, forbidden RAW/WORK/QUARANTINE refs, produced count parity, unique z/x/y keys, masked pct threshold, change-type-specific prior/payload validation, replay mismatch failure.

Apply behavior: atomic in-memory apply; writes output store/receipt only after successful verification. Idempotent ledger append for same delta_id + manifest hash.

Rollback/replay protections: mismatched prior_digest or replay hash fails; older time_end fails by default.

CI/test paths: `tests/test_kfm_delta_apply.py`, `policy/tiles/delta_apply*.rego`, `tools/tiles/kfm_delta_apply.py`.

Limitations / NEEDS_VERIFICATION: real PMTiles extraction bridge deferred; currently fixture-based payload model only.
