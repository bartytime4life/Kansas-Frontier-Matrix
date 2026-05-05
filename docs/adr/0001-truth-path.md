# ADR 0001: Truth Path

## Status

Accepted

## Context

Promotion decisions require a single auditable path from evidence to release. Without a defined truth path, reviewers and CI can disagree about which artifact is authoritative, which hash represents the final state, and which decision log approved publication.

## Decision

The truth path is:

```text
EvidenceBundle.json + spec_hash.txt
        ↓
policy decisions + validator receipts
        ↓
decision_log.json + preflight_report.json
        ↓
release_manifest.json + attestations
        ↓
published release and archive
```

`EvidenceBundle.json` is the canonical evidence document. `spec_hash.txt` is the canonical digest for the hashable content of the evidence bundle. `release_manifest.json` is the canonical statement of what is published.

## Consequences

All promotion gates must read from the same artifact set. A reviewer may challenge the decision, but may not substitute a separate source of truth during promotion. Any transform that changes releasable content must update the EvidenceBundle and recompute `spec_hash` before promotion continues.

## Validation / Enforcement

CI runs gate policies A→G. Gate A validates the EvidenceBundle and spec hash. Gate G validates that the release manifest points back to the same spec hash and that published artifact hashes match local files.

## Rollback

Rollback requires a new EvidenceBundle and ReleaseManifest describing the rollback target. The previous truth path remains archived and immutable.
