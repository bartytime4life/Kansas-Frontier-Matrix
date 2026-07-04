# `schemas/contracts/v1/domains/settlements-infrastructure/runtime/`

## Purpose

Draft schema index for Settlements / Infrastructure runtime-facing object shapes.

This path is for machine-checkable schema notes and future JSON Schema files that describe runtime-facing envelopes, layer descriptors, drawer payload references, decision envelopes, feature-detail payloads, and public-safe view models for the Settlements / Infrastructure domain after placement is confirmed.

This README is documentation only. It is not a schema file, contract, policy, validator, pipeline, application code, lifecycle data, registry record, proof, receipt, catalog record, release record, public API implementation, map implementation, or publication authority.

## Status

| Field | Value |
|---|---|
| Status | Draft |
| Owning root | `schemas/` |
| Path role | Runtime-facing schema index |
| Parent lane | `schemas/contracts/v1/domains/settlements-infrastructure/` |
| Canonical posture | PROPOSED / NEEDS VERIFICATION |
| Current schema inventory | NEEDS VERIFICATION |
| Last reviewed | 2026-07-03 |

## Placement basis

`schemas/` owns machine-checkable shape.

ADR-0001 places domain schemas under `schemas/contracts/v1/domains/<domain>/...` and keeps semantic meaning in `contracts/`.

Directory Rules keep schemas, contracts, policy, data, registries, proofs, receipts, fixtures, tests, pipelines, applications, and releases in separate responsibility roots.

`schemas/contracts/v1/domains/settlements-infrastructure/README.md` exists as the broader schema lane scaffold, but it still needs expansion and does not prove runtime schema maturity.

Settlements / Infrastructure API contracts identify governed API surfaces, finite outcomes, and trust-membrane rules for public, semi-public, and AI-mediated access. Those docs describe contract meaning; schema files must remain under `schemas/`.

Settlements / Infrastructure Map/UI contracts identify governed manifests, envelopes, and drawer payloads used by the MapLibre shell, Evidence Drawer, and Focus Mode runtime. They do not themselves create schema files or runtime implementation.

Current search found API/UI, package, app, registry, docs, and semantic contract surfaces, but did not confirm concrete `.schema.json` files under this requested runtime schema path.

## Related lanes

```text
schemas/contracts/v1/domains/settlements-infrastructure/runtime/  # this index
schemas/contracts/v1/domains/settlements-infrastructure/          # parent schema lane
contracts/domains/settlements-infrastructure/                     # semantic meaning, not schema shape
docs/domains/settlements-infrastructure/API_CONTRACTS.md          # governed API contracts
docs/domains/settlements-infrastructure/MAP_UI_CONTRACTS.md       # map/UI contract surface
apps/explorer-web/src/features/domains/settlements_infrastructure/ # app feature code, not schema shape
packages/domains/settlements-infrastructure/                      # package code, not schema shape
```

## Candidate schema names

| Candidate | Status |
|---|---|
| `feature_detail_payload.schema.json` | NEEDS VERIFICATION |
| `domain_layer_descriptor.schema.json` | NEEDS VERIFICATION |
| `layer_manifest_ref.schema.json` | NEEDS VERIFICATION |
| `map_context_envelope.schema.json` | NEEDS VERIFICATION |
| `evidence_drawer_payload.schema.json` | NEEDS VERIFICATION |
| `focus_mode_request.schema.json` | NEEDS VERIFICATION |
| `decision_envelope.schema.json` | NEEDS VERIFICATION |
| `runtime_feature_summary.schema.json` | NEEDS VERIFICATION |
| `public_safe_view_model.schema.json` | NEEDS VERIFICATION |
| `runtime_error_envelope.schema.json` | NEEDS VERIFICATION |

## What belongs here

- This README.
- Future runtime-facing JSON Schema files after placement is confirmed.
- Schema index notes.
- Migration notes for runtime-facing schema placement.
- Links to paired contracts, fixtures, validators, schema registry records, tests, policy references, release references, correction references, and rollback references.

## What does not belong here

- Contract prose beyond this boundary README.
- Policy rules.
- Validator code.
- Application code.
- Package code.
- Pipeline code.
- Lifecycle data.
- Source registry records.
- Proof or receipt records.
- Catalog records.
- Release records.
- Public map, API, or UI implementation artifacts.
- Schema files until placement is confirmed by steward decision, ADR, or migration note.

## Review checklist

- [ ] Confirm whether `runtime/` should exist as a child schema lane or whether runtime-facing schemas belong directly under `schemas/contracts/v1/domains/settlements-infrastructure/`.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, release, correction, and rollback references.
- [ ] Confirm no application code, lifecycle data, release records, proof records, receipt records, or source registry records are stored here.
