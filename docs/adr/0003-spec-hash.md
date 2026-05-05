# ADR 0003: Canonical spec_hash

## Status

Accepted

## Context

The promotion process needs a stable digest that identifies the exact evidence state being approved and published. A raw file hash is brittle when the EvidenceBundle embeds its own hash or signature metadata.

## Decision

Use `canonical-json-v1` for `spec_hash`:

1. Parse `artifacts/EvidenceBundle.json` as JSON.
2. Remove these root-level fields before hashing: `spec_hash`, `computed_spec_hash`, `signatures`, `attestations`, `_signature`.
3. Serialize the remaining JSON using UTF-8, sorted keys, compact separators, and `ensure_ascii=false`.
4. Compute SHA-256 of the canonical bytes.
5. Store the digest in `artifacts/spec_hash.txt` and, when present, `EvidenceBundle.spec_hash`.

After any transform that changes evidence or releasable content, recompute `spec_hash` and update downstream receipts.

## Consequences

The digest is stable across formatting changes but sensitive to semantic EvidenceBundle changes. Signature material is external to the hash to avoid recursion. Teams must not hand-edit `spec_hash.txt`.

## Validation / Enforcement

`tools/validators/check_spec_hash.py` implements the algorithm. Gate A invokes it and writes `.promotion/spec_hash_check.json` as a receipt.

## Rollback

A future algorithm must be introduced as `canonical-json-v2` with a migration plan. Existing bundles using v1 remain verifiable under v1.
