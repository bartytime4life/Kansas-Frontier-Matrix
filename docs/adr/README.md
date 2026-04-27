# Architecture Decision Records (ADRs)

This directory stores durable architecture decisions for the Kansas Frontier Matrix repository.

## Purpose

ADRs capture:
- **Context** for a decision.
- **Decision** selected by maintainers.
- **Alternatives** that were considered.
- **Consequences** (tradeoffs, follow-up, and verification).

Use ADRs for cross-cutting decisions that affect contracts, governance, publication, policy, provenance, security, and system boundaries.

## ADR lifecycle

- `proposed`: Draft, under review.
- `accepted`: Approved and active.
- `superseded`: Replaced by a newer ADR.
- `rejected`: Considered and declined.

## Naming and numbering

- File format: `ADR-XXXX-short-kebab-case-title.md`
- Four-digit sequence (`0001`, `0002`, ...)
- Keep numbers stable forever; never renumber historical ADRs.

## Current index

| ADR | Title | Status |
|---|---|---|
| [ADR-0001](./ADR-0001-schema-home.md) | Canonical Schema Home for Machine Contracts | proposed |
| [ADR-0002](./ADR-0002-governed-api-path-canonicalization.md) | Governed API Path Canonicalization (`governed_api` vs `governed-api`) | accepted |
| [ADR-0003](./ADR-0003-source-ledger-authority.md) | Source Ledger Authority and Source-State Gating | proposed |
| [ADR-0004](./ADR-0004-evidencebundle-contract.md) | EvidenceBundle as the Public Unit of Inspection | proposed |
| [ADR-0005](./ADR-0005-promotion-gate.md) | Promotion Gate as a Governed State Transition | proposed |
| [ADR-0006](./ADR-0006-maplibre-layer-manifest.md) | MapLibre Layer Manifest Contract | proposed |
| [ADR-0007](./ADR-0007-governed-ai-runtime-envelope.md) | Governed AI Runtime Response Envelope | proposed |
| [ADR-0008](./ADR-0008-domain-lane-template.md) | Domain Lane Template Standardization | proposed |
| [ADR-0009](./ADR-0009-sensitive-location-policy.md) | Sensitive-Location Publication Policy | proposed |
| [ADR-0010](./ADR-0010-local-exposure-security.md) | Local Exposure Security Posture | proposed |
| [ADR-0011](./ADR-0011-catalog-proof-release-separation.md) | Catalog, Proof, and Release Separation | proposed |
| [ADR-PROV-STAC-DCAT-CATALOG-MAPPING](./ADR-PROV-STAC-DCAT-CATALOG-MAPPING.md) | PROV, STAC, and DCAT Catalog Mapping | draft |

## How to author a new ADR

1. Copy [`ADR-TEMPLATE.md`](./ADR-TEMPLATE.md).
2. Assign the next ADR number.
3. Fill in **Status**, **Date**, **Context**, **Decision**, **Alternatives**, and **Consequences**.
4. Add verification steps and migration/rollback notes.
5. Update this README index in the same PR.

## Lightweight quality checklist

Before merging a new ADR:
- Problem is stated clearly and concretely.
- Decision is testable and unambiguous.
- At least one alternative is recorded.
- Consequences include both benefits and costs.
- Validation/CI follow-ups are named if needed.
- Supersession path is documented when relevant.
