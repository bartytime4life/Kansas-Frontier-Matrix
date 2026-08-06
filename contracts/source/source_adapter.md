<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-adapter
title: SourceAdapter Contract
type: semantic-contract; protocol
version: v0.1.1
status: proposed; internal-transport-boundary; no-live-adapter
owners: OWNER_TBD — Connector steward · Source steward · Contracts steward · Security reviewer
created: 2026-08-04
updated: 2026-08-06
policy_label: public; source-adapter; least-privilege; non-publisher
related:
  - ./source_descriptor.md
  - ./ingest_receipt.md
  - ./source_artifact.md
  - ../../docs/architecture/source-verification.md
  - ../../packages/connectors-core/README.md
  - ../../packages/connectors-core/src/connectors_core/PRIMITIVES.md
  - ../../packages/connectors-core/src/connectors_core/TRANSPORT.md
  - ../../packages/connectors-core/src/connectors_core/transport.py
  - ../../tests/packages/connectors_core/README.md
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

This remains a semantic protocol, not a live source adapter. The repository now has a **PROPOSED internal** source-agnostic transport boundary and deterministic fake-transport tests. It supplies no concrete HTTP client, endpoint, source profile, credential provider, persistence handoff, receipt emitter, or lifecycle writer.

## Bounded context

| Adapter may own | Adapter must not own |
|---|---|
| Source-specific locator discovery under an accepted profile | Source admission or activation |
| One least-privilege retrieval operation | Source truth, rights clearance, or policy approval |
| Finite transport outcome and safe metadata | EvidenceBundle closure |
| Exact byte handoff to governed storage | Hidden lifecycle promotion |
| Parser invocation against immutable bytes | Release or publication |
| Source-health observations and freshness signals | Clearing a volatile event from missing data |

## Finite adapter outcomes

The adapter-level vocabulary distinguishes byte-producing from no-byte results:

| Outcome | Bytes? | Required behavior |
|---|---:|---|
| `FETCHED` | yes | Digest and preserve bytes; create a `SourceArtifact` candidate through a separate governed handoff. |
| `NOT_MODIFIED` | no new bytes | Reference the prior artifact; update process/source-health memory only. |
| `NOT_FOUND` | no | Preserve status uncertainty; never infer rescission or deletion. |
| `ACCESS_DENIED` | no | Quarantine/deny; do not scrape around the control. |
| `RATE_LIMITED` | no | Apply bounded retry policy; retain prior state with freshness warning. |
| `TIMEOUT` | no | Record failure and retry state; never false-clear. |
| `REDIRECT_BLOCKED` | no | Reject unapproved target or host transition. |
| `WRONG_MEDIA_TYPE` | bytes may be held in quarantine | Preserve bounded diagnostics; no parse or claim support until reviewed. |
| `RESPONSE_TOO_LARGE` | partial/no governed artifact | Abort under declared budget; do not emit a complete `SourceArtifact`. |
| `MALFORMED` | yes | Preserve exact bytes and parser failure as a `SourceArtifact` candidate. |
| `SOURCE_CONFLICT` | yes | Preserve each official surface separately and link conflict lineage. |
| `ERROR` | unknown | Fail closed; do not substitute cached or generated certainty without an explicit prior-state rule. |

The internal transport package uses lower-level transport observations such as `SUCCESS`, `PARTIAL`, `RETRY_EXHAUSTED`, `INTEGRITY_MISMATCH`, and `UNSAFE_METADATA`. A source-specific adapter must map those observations into this adapter vocabulary without collapsing evidence, policy, review, release, or lifecycle meaning.

## Security and reproducibility

- Credentials remain caller-owned and never enter locators, artifacts, logs, fixtures, receipts, result representations, or exception text.
- Redirects, hosts, schemes, ports, status codes, content types, timeouts, and size limits are controlled by a source-specific profile.
- Request context records only safe method/profile/name metadata and body digests, never secret values.
- Parser inputs are immutable `SourceArtifact` bytes, not mutable live responses.
- Adapters do not perform hidden writes. The caller explicitly supplies a storage or lifecycle handoff.
- Pull-request CI remains no-network and uses fake transports or synthetic fixtures.
- Clock, sleep, jitter, cancellation, and transport effects are injected so retries and tests are deterministic.
- A successful transport result is not source admission, evidence closure, or public-use approval.

## Relationship to existing objects

```text
SourceDescriptor = source identity, role, rights, sensitivity, access, cadence
SourceAdapter    = source-specific discovery/fetch/parse/health mechanics
TransportResult = source-agnostic attempt/payload observation; no authority
RunReceipt       = broader execution/process memory, including no-byte outcomes
IngestReceipt    = source capture run and captured-unit digests
SourceArtifact   = one exact captured byte stream and immutable metadata
ParseResult      = parser identity, records, diagnostics, unsupported flags
EvidenceRef      = claim/field-scoped pointer into admissible source support
```

No object above can substitute for another.

## Current implementation boundary

**CONFIRMED in repository paths after the corresponding implementation merges; otherwise PROPOSED on its review branch:**

- `connectors_core.core` supplies pure ETag, source-head, retry, integrity, and redaction primitives.
- `connectors_core.transport` supplies the internal injected transport facade and deterministic executor.
- Package-level exports remain empty; both surfaces are internal and pre-stable.
- `connector-gate` compiles/imports the package and runs no-network tests plus existing connector non-publisher and `IngestReceipt` checks.

**Still PROPOSED or UNKNOWN:**

- any source-specific adapter;
- any live transport implementation;
- `SourceDescriptor` resolution or source activation;
- credential-provider integration;
- exact-byte storage/lifecycle handoff;
- connector-emitted authoritative receipt correspondence;
- parser integration, evidence closure, release, deployment, or publication.

## Graduation path

A later, separate pull request may implement one structured official adapter against an already governed source profile. That change must not also introduce a new source schema, source-activation decision, rights decision, or public product, and no live connector may run in pull-request CI.

Before stable package-level exports, require consumer evidence, ownership, compatibility tests, source-profile fixtures, and review of error, retry, redirect, integrity, and redaction semantics.

## Rollback

The internal transport implementation and this documentation update can be reverted without touching source data or live systems because the slice creates no live adapter, source activation, external object, lifecycle state, or public product. Any later consumer requires a compatibility or migration note before a breaking change.

[Back to top](#top)
