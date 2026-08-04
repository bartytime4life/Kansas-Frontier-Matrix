<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-adapter
title: SourceAdapter Contract
type: semantic-contract; protocol
version: v0.1.0
status: proposed; no-live-adapter; no-network-fixture-profile
owners: OWNER_TBD — Connector steward · Source steward · Contracts steward · Security reviewer
created: 2026-08-04
updated: 2026-08-04
policy_label: public; source-adapter; least-privilege; non-publisher
related:
  - ./source_descriptor.md
  - ./ingest_receipt.md
  - ./source_artifact.md
  - ../../docs/architecture/source-verification.md
  - ../../packages/connectors-core/README.md
  - ../../.github/workflows/connector-gate.yml
tags: [kfm, source-adapter, discover, fetch, parse, source-health, finite-outcomes, no-publish]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceAdapter Contract

> A `SourceAdapter` is a source-specific implementation boundary that can discover approved locators, retrieve one approved source surface, parse immutable captured bytes, and report source health. It cannot admit or activate a source, publish, release, clear an advisory, mutate unrelated lifecycle state, or merge repository work.

## Proposed protocol

```python
class SourceAdapter(Protocol):
    def discover(self, cursor: DiscoveryCursor) -> list[SourceLocator]: ...
    def fetch(self, locator: SourceLocator) -> RetrievalResult: ...
    def parse(self, artifact: SourceArtifact) -> ParseResult: ...
    def source_health(self) -> SourceHealth: ...

# Explicitly absent:
# publish(), release(), activate_source(), clear_advisory(), merge_pr()
```

This is a semantic protocol, not an implemented live adapter in this slice. The current implementation work establishes the immutable `SourceArtifact` metadata and local no-network validation/store boundary that future adapters must satisfy.

## Bounded context

| Adapter may own | Adapter must not own |
|---|---|
| Source-specific locator discovery under an accepted profile | Source admission or activation |
| One least-privilege retrieval operation | Source truth, rights clearance, or policy approval |
| Finite transport outcome and safe metadata | EvidenceBundle closure |
| Exact byte handoff to governed storage | Hidden lifecycle promotion |
| Parser invocation against immutable bytes | Release or publication |
| Source-health observations and freshness signals | Clearing a volatile event from missing data |

## Finite retrieval outcomes

The first shared vocabulary distinguishes byte-producing from no-byte results:

| Outcome | Bytes? | Required behavior |
|---|---:|---|
| `FETCHED` | yes | Digest and preserve bytes; create SourceArtifact candidate. |
| `NOT_MODIFIED` | no new bytes | Reference the prior artifact; update process/source-health receipt only. |
| `NOT_FOUND` | no | Preserve status uncertainty; never infer rescission or deletion. |
| `ACCESS_DENIED` | no | Quarantine/deny; do not scrape around the control. |
| `RATE_LIMITED` | no | Apply bounded retry policy; retain prior state with freshness warning. |
| `TIMEOUT` | no | Record failure and retry state; never false-clear. |
| `REDIRECT_BLOCKED` | no | Reject unapproved target/host transition. |
| `WRONG_MEDIA_TYPE` | bytes may be held in quarantine | Preserve bounded diagnostics; no parse or claim support until reviewed. |
| `RESPONSE_TOO_LARGE` | partial/no governed artifact | Abort under declared budget; do not emit a complete SourceArtifact. |
| `MALFORMED` | yes | Preserve exact bytes and parser failure as a SourceArtifact. |
| `SOURCE_CONFLICT` | yes | Preserve each official surface separately and link conflict lineage. |
| `ERROR` | unknown | Fail closed; do not substitute cached or generated certainty without an explicit prior-state rule. |

## Security and reproducibility

- The adapter receives credentials through caller-owned secret handling; credentials never enter locators, artifacts, logs, fixtures, receipts, or exception text.
- Redirects, hosts, schemes, status codes, content types, and size limits are controlled by source-specific profiles.
- Request context records only safe method/profile/name metadata and body digests, never secret values.
- Parser inputs are immutable SourceArtifact bytes, not mutable live responses.
- Adapters do not perform hidden writes. The caller explicitly supplies a storage or lifecycle handoff.
- Pull-request CI remains no-network and uses fake transports/synthetic fixtures.

## Relationship to existing objects

```text
SourceDescriptor = source identity, role, rights, sensitivity, access, cadence
SourceAdapter    = source-specific discovery/fetch/parse/health mechanics
RunReceipt       = broader execution/process memory, including no-byte outcomes
IngestReceipt    = source capture run and captured-unit digests
SourceArtifact   = one exact captured byte stream and immutable metadata
ParseResult      = parser identity, records, diagnostics, unsupported flags
EvidenceRef      = claim/field-scoped pointer into admissible source support
```

No object above can substitute for the others.

## Graduation path

A later pull request may add a pure source-agnostic protocol/types module under the verified reusable connector package, with fake-transport tests. A separate later source-specific pull request may implement one structured official adapter. That adapter must not land in the same change as a new schema or source activation decision, and no live connector may run in pull-request CI.

## Rollback

This document may be reverted without touching source data or live systems because this slice creates no adapter runtime or source activation. Any later code relying on the protocol requires a compatibility or migration note before a breaking change.

[Back to top](#top)
