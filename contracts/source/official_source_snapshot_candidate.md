# OfficialSourceSnapshotCandidate Contract

Status: PROPOSED implementation contract.

`OfficialSourceSnapshotCandidate` is an immutable, no-network capture record for bytes that were obtained from a declared official-source location outside this adapter. It gives later verification work a deterministic source identity, retrieval time, response metadata, byte length, and SHA-256 digest without converting the capture into evidence or activating the source.

The object is intentionally pre-evidence. `source_activation_authorized`, `evidence_bundle_emitted`, and `public_use_allowed` are fixed to `false`. The adapter never performs network access and never writes RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED state.

For a `CAPTURED` result, the adapter hashes the exact local payload bytes and derives `snapshot_id` from `source_id`, `source_url`, `retrieved_at`, and the content digest. `NOT_MODIFIED` and `FAILED` are admissible metadata outcomes but cannot claim captured bytes.

Fail-closed rules: a captured result requires a 2xx status, non-empty bytes, and a SHA-256 digest; `NOT_MODIFIED` requires HTTP 304 and no captured digest; failed retrieval cannot carry captured bytes; source `last_modified` cannot be later than `retrieved_at`; and all trust-bearing flags must remain false.

This candidate is not a `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `RunReceipt`, policy decision, review record, release manifest, or publication authority. A later source-admission and evidence-building flow must independently verify rights, sensitivity, source role, authority, citation, retrieval provenance, and release posture.