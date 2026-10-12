# EvidenceResolutionRecord

Status: PROPOSED_INACTIVE  
Profile: `kfm.governance.evidence-resolution-record.v1`

`EvidenceResolutionRecord` is the deterministic, no-network control-loop record that states whether a bounded set of `EvidenceRef` values was resolved strongly enough for a later query or compile step to proceed.

It does not create evidence, authenticate a source, evaluate policy, approve review, write lifecycle state, promote, release, deploy, or publish.

## Finite outcomes

- `COMPLETE`: every requested evidence reference resolved to a non-empty `EvidenceBundle` identifier and digest.
- `PARTIAL`: at least one reference resolved and at least one remains unresolved.
- `UNRESOLVED`: no requested reference resolved.
- `DENIED`: resolution was intentionally withheld by an upstream rights, sensitivity, or access decision.
- `ERROR`: the record is malformed, internally inconsistent, or claims authority/effects it does not possess.

## Required invariants

1. `requested_refs` is sorted, unique, and non-empty.
2. Every resolution row refers to exactly one requested ref.
3. Resolution rows are sorted by `evidence_ref` and contain no duplicates.
4. `RESOLVED` rows require `bundle_id` and lowercase SHA-256 `bundle_digest`.
5. `UNRESOLVED` and `DENIED` rows must not carry bundle identity.
6. The declared `outcome` must exactly match the derived outcome.
7. All effect flags are fixed `false`.
8. `record_id` is `kfm:evidence-resolution:<sha256-hex>` where the digest is computed over canonical JSON of the record with `record_id` omitted.

## Trust boundary

This record is process memory for the query-save-recompile loop. `COMPLETE` means only that the declared references resolve coherently inside this candidate record. It is not EvidenceBundle truth, policy approval, human review, promotion, release, or public-use authority.
