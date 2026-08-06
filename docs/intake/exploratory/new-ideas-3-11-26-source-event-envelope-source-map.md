# New Ideas 3-11-26 — Source Event Envelope Adaptation

## Status

- **Source:** `New Ideas 3-11-26.pdf`
- **Repository assay base:** `main@fda5e18b486d89a91dba7d886e305fde302edf12`
- **Selected increment:** fixture-only `SourceEventEnvelopeCandidate`
- **Implementation status:** `PROPOSED` until reviewed and merged
- **Network, source activation, lifecycle, release, and publication effects:** none

## Source idea

The packet proposes three integration patterns. Its event-driven pattern normalizes object-store notifications, webhooks, and feed changes into a common event shape; canonicalizes selected content; computes a deterministic hash for idempotency; hands work to an orchestrator; and signs a run receipt or attestation so provenance travels with the artifact.

The packet also proposes PR-first scheduled ETL, streaming or change-data-capture, a governed CSV-to-GeoJSON ingest runner, AI-enrichment receipts, policy gates, conditional writes, and OCI/Sigstore attestation.

## Repository assay

At the recorded base, repository search found:

- a current RFC 8785 plus SHA-256 hashing package;
- source descriptors, source activation decisions, source artifacts, ingest receipts, and source-ingestion contracts;
- watcher and source-health implementations;
- artifact-delta, trace-link, temporal-slice, advisory-event, and AI-change-proposal profiles;
- fixture-first validators and read-only workflows.

Repository search did not find a generic CloudEvents or source-event-envelope contract, schema, fixture family, validator, or focused workflow.

## Selected dependency-closed slice

This increment adds a bounded event candidate that:

- carries CloudEvents-shaped core attributes without claiming full CloudEvents conformance;
- binds one `SourceDescriptor` reference and its source-role field;
- computes deterministic payload and event identity using the current KFM hashing package;
- distinguishes source-admission review, quarantine review, and idempotent no-action routing;
- fails closed on unresolved rights or sensitivity;
- makes all source-activation, RAW-write, authority, release, publication, and network claims false;
- uses only synthetic no-network fixtures; and
- emits no operational event or source data.

## Why this increment was selected

It closes a reusable source-edge gap while depending only on already observed repository foundations: the source contract family, the canonical schema home, the hashing package, existing validator/test conventions, read-only CI, and generated authoring receipts.

It is smaller and safer than implementing a live event bus, webhook endpoint, Temporal or Dagster runtime, database replay table, Cosign signing, OCI referrers, or external source access.

## Source adaptations

| Source proposal | Repository adaptation |
|---|---|
| Normalize events to CloudEvents. | Add a CloudEvents-shaped candidate profile while fixing the conformance claim to `false` until standards and transport review are completed. |
| Use a canonical hash as the idempotency key. | Reuse the existing KFM RFC 8785 plus SHA-256 package and derive a stable `event_id`. |
| Orchestrate with Temporal or Dagster. | Deferred. The current slice performs validation only and starts no orchestrator. |
| Sign receipts and attach OCI attestations. | Deferred. The candidate records no signature claim and contacts no registry. |
| Route source changes into processing. | Route only to review proposals or no action; source activation and RAW writes remain false. |

## Directory Rules basis

Accepted ADR-0029 makes the adopted Directory Rules v2 authority effective. The implementation uses existing responsibility roots:

| Responsibility | Home |
|---|---|
| Source-edge semantic meaning | `contracts/source/` |
| Machine-checkable shape | `schemas/contracts/v1/source/` |
| Synthetic positive and negative records | `fixtures/contracts/v1/source/` |
| Repository-wide deterministic validation | `tools/validators/` |
| Executable proof | `tests/validators/` |
| Least-privilege CI orchestration | `.github/workflows/` |
| Exploratory source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, compatibility root, source registry, lifecycle lane, policy home, receipt authority, release home, proof store, queue, runtime service, or public route is created.

## Deferred candidates

- governed CSV-to-GeoJSON fixture runner;
- live webhook or object-store adapters;
- NATS, Kafka, Pub/Sub, Kinesis, or database CDC;
- Temporal or Dagster orchestration;
- replay or idempotency persistence;
- OPA/Conftest execution;
- DSSE, Cosign, Sigstore, Rekor, OCI, or ORAS integration;
- source activation and RAW admission;
- public API, MapLibre, search, vector-index, or governed-AI consumption.

Each deferred item requires a separate repository assay and trust-boundary review.

## Next implementation cursor

After this profile is reviewed, the next smallest source-derived candidate is the packet's fixture-only CSV-to-GeoJSON normalization runner. That increment should reuse this event identity boundary, the current hashing package, existing source and ingest receipt contracts, and synthetic coordinates. It must not introduce live source activation or public geometry without a separately reviewed policy profile.

## Rollback

Close the draft pull request before merge or revert the dependency-closed implementation after merge. No external state or public artifact is created.
