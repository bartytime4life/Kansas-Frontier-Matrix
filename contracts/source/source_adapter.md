<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-adapter
title: SourceAdapter Contract
type: semantic-contract; protocol
version: v0.2.0
status: proposed; source-agnostic-protocol-implemented; no-live-adapter; no-source-activation
owners: OWNER_TBD — Connector steward · Source steward · Contracts steward · Security reviewer
created: 2026-08-04
updated: 2026-08-09
policy_label: public; source-adapter; least-privilege; non-publisher
related:
  - ./source_descriptor.md
  - ./ingest_receipt.md
  - ./source_artifact.md
  - ../../docs/architecture/source-verification.md
  - ../../docs/intake/exploratory/briefing-source-adapter-protocol-source-map.md
  - ../../packages/connectors-core/README.md
  - ../../packages/connectors-core/src/connectors_core/SOURCE_ADAPTER.md
  - ../../packages/connectors-core/src/connectors_core/source_adapter.py
  - ../../tests/packages/connectors_core/test_source_adapter.py
  - ../../.github/workflows/connector-gate.yml
tags: [kfm, source-adapter, discover, fetch, parse, source-health, finite-outcomes, no-publish]
notes:
  - "v0.2 binds the semantic protocol to a pure source-agnostic implementation in connectors-core."
  - "No source-specific adapter, live transport, source activation, lifecycle write, evidence closure, release, or publication is added."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SourceAdapter Contract

> A `SourceAdapter` is a source-specific implementation boundary that can discover approved locators, retrieve one approved source surface, parse immutable captured bytes, and report source health. It cannot admit or activate a source, publish, release, clear an advisory, mutate lifecycle state, or merge repository work.

## Current implementation status

The reusable source-agnostic protocol and boundary value objects are implemented under the existing `packages/connectors-core/` responsibility root:

| Surface | Current bounded role |
|---|---|
| `source_adapter.SourceAdapter` | Runtime-checkable structural protocol for discover, fetch, parse, and source-health mechanics. |
| `DiscoveryCursor` | Caller-supplied discovery scope with explicit observation time, opaque cursor, and bounded result limit. |
| `SourceLocator` | Canonical, secret-safe source locator with deterministic digest, source reference, native ID, profile, parameter names, and expected media types. |
| `ParseResult` | Immutable parser result bound to one SourceArtifact identity and finite parser outcome. |
| `SourceHealth` | Source-health observation that can never authorize clearing a domain event. |
| `assert_source_adapter_boundary` | Non-invoking structural check that rejects explicitly authority-bearing adapter method names. |

The implementation is pure and no-network. It creates no source-specific adapter and performs no source discovery, fetch, parse, storage, registry, receipt, policy, lifecycle, release, or publication operation by itself.

## Protocol

```python
class SourceAdapter(Protocol):
    @property
    def adapter_id(self) -> str: ...

    def discover(self, cursor: DiscoveryCursor) -> Sequence[SourceLocator]: ...
    def fetch(self, locator: SourceLocator) -> RetrievalResult: ...
    def parse(self, artifact: SourceArtifactView) -> ParseResult: ...
    def source_health(self) -> SourceHealth: ...

# Explicitly forbidden adapter capabilities include:
# activate_source(), admit_source(), clear_advisory(), create_evidence_bundle(),
# merge_pr(), publish(), release(), write_lifecycle()
```

Structural conformance does not prove that a source-specific implementation is safe. Every concrete adapter still requires source-profile review, injected-transport tests, rights and sensitivity review, stable identity, parser fixtures, finite failure behavior, correction handling, and explicit activation authority.

## Bounded context

| Adapter may own | Adapter must not own |
|---|---|
| Source-specific locator discovery under an accepted profile | Source admission or activation |
| One least-privilege retrieval operation | Source truth, rights clearance, or policy approval |
| Finite transport outcome and safe metadata | EvidenceBundle closure |
| Exact byte handoff to governed storage | Hidden lifecycle promotion |
| Parser invocation against immutable bytes | Release or publication |
| Source-health observations and freshness signals | Clearing a volatile event from missing data or failed retrieval |

## Finite parser outcomes

| Outcome | Required posture |
|---|---|
| `PARSED` | At least one immutable parsed record; no conflict or unsupported marker. |
| `MALFORMED` | No parsed records; one or more stable findings. Exact source bytes remain a separate SourceArtifact responsibility. |
| `UNSUPPORTED` | No parsed records; one or more canonical unsupported-content flags. |
| `CONFLICT` | At least two preserved source-native records, a conflict reference, and a `SOURCE_CONFLICT` finding. |
| `ERROR` | No parsed records; one or more stable findings; no generated fallback. |

A parser result never creates evidence, policy, review, lifecycle, receipt, release, publication, public-use, or repository-mutation authority.

## Finite retrieval outcomes

The existing shared transport vocabulary distinguishes byte-producing from no-byte results:

| Outcome | Bytes? | Required behavior |
|---|---:|---|
| `FETCHED` / package-local transport success | yes | Digest and preserve bytes; create a SourceArtifact candidate through the reviewed handoff. |
| `NOT_MODIFIED` | no new bytes | Reference the prior artifact; update process/source-health memory only. |
| `NOT_FOUND` | no | Preserve status uncertainty; never infer rescission or deletion. |
| `ACCESS_DENIED` | no | Quarantine or deny; do not scrape around the control. |
| `RATE_LIMITED` | no | Apply bounded retry policy; retain prior state with freshness warning. |
| `TIMEOUT` | no | Record failure and retry state; never false-clear. |
| `REDIRECT_BLOCKED` | no | Reject an unapproved target or host transition. |
| `WRONG_MEDIA_TYPE` | bytes may be held in quarantine | Preserve bounded diagnostics; no parse or claim support until reviewed. |
| `RESPONSE_TOO_LARGE` | partial or no governed artifact | Abort under the declared budget; do not emit a complete SourceArtifact. |
| `MALFORMED` | yes | Preserve exact bytes and parser failure as separate objects. |
| `SOURCE_CONFLICT` | yes | Preserve each official surface separately and link conflict lineage. |
| `ERROR` | unknown | Fail closed; do not substitute cached or generated certainty without an accepted prior-state rule. |

## Source-health and false-clear rule

`SourceHealth` records a bounded observation such as `HEALTHY`, `DEGRADED`, `UNREACHABLE`, `AUTH_REQUIRED`, `RATE_LIMITED`, or `UNKNOWN`. Its `clear_signal_allowed` value is fixed to `false`.

A successful source-health check is not an authoritative advisory rescission. A failed, incomplete, missing, unauthorized, stale, or rate-limited check cannot clear a volatile domain event. Domain-native event contracts and accepted source semantics remain controlling.

## Security and reproducibility

- Credentials remain caller-owned and never enter locators, artifacts, parser results, health results, logs, fixtures, receipts, or exception text.
- Locators are canonical and secret-safe before they enter the value object.
- Observation time, cursor, transport, parser, and clock behavior are injected; the module samples no ambient state.
- Parser inputs expose exact immutable bytes and metadata through a structural SourceArtifact view.
- Parsed records are deeply immutable inside the result object.
- Pull-request CI remains no-network and exercises only fake adapters and deterministic values.
- The boundary checker does not invoke adapter methods and cannot substitute for code review or source-profile tests.

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

## Directory Rules basis

The accepted Directory Rules v2 place reusable source-agnostic implementation in `packages/`, source-specific mechanics in `connectors/`, semantic meaning in `contracts/source/`, source identity in `data/registry/sources/`, enforceability in `tests/`, and CI orchestration in `.github/workflows/`. This change uses the existing `packages/connectors-core/` package and creates no new root or parallel source, registry, contract, schema, policy, receipt, evidence, release, or publication authority.

## Graduation path

A later pull request may implement one structured official source adapter only after its canonical connector home is resolved, its source profile and rights posture are current, and its parser/transport fixtures are accepted. That source-specific change remains separate from source activation, live pull-request CI, public API, map, alert, release, or publication work.

The existing NOAA/NWS connector topology remains conflicted among family, service, and product lanes; this protocol implementation does not choose that source-specific home.

## Validation

```bash
python -m pytest tests/packages/connectors_core/test_source_adapter.py -q --strict-config --strict-markers
python -m pytest tests/packages/connectors_core -q --strict-config --strict-markers
```

## Rollback

Before merge, close the draft pull request and retire its feature branch through normal controls. After an authorized merge, revert the bounded implementation commit. No source, credential, registry, lifecycle, evidence, policy, review, receipt, release, deployment, cache, or public state requires operational cleanup.

[Back to top](#top)
