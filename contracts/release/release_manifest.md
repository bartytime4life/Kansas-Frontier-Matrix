# release_manifest

> Status: PROPOSED
> Schema: https://schemas.kfm.local/contracts/v1/release/release_manifest.schema.json
> Schema file: schemas/contracts/v1/release/release_manifest.schema.json
> Validator: PROPOSED — not yet wired
> Authority: contracts/ owns meaning; schemas/contracts/v1/ owns shape (ADR-0001, ADR-0002).

## 1. Purpose
`release_manifest` identifies a governed release artifact set at publication time and links it to a specific spec lineage. It answers which release id/version/spec hash a published package claims. It is not yet a full signed release attestation object in the current thin schema.

## 2. Lifecycle role
This object is expected at release/publish handoff from CATALOG / TRIPLET outputs into PUBLISHED artifacts. It should be validated before publication and superseded when a newer release manifest is issued. Current schema thinness means some release-governance semantics remain deferred.

## 3. Fields
| field | type | required | meaning | examples or enum | policy/sensitivity notes |
|---|---|---|---|---|---|
| `spec_hash` | string | no | Deterministic hash claiming spec lineage for the release. | `sha256:<64 hex>` | Useful for compatibility checks; currently optional in shape. |
| `id` | string | yes | Canonical release manifest identifier. | `release:hydrology:2026-05-08` | Primary governance anchor for release tracking. |
| `version` | string | no | Release version string. | `2026.05.08-1` | Supports rollback/comparison workflows when present. |

Schema asymmetry note (CONFIRMED): this schema currently uses `additionalProperties: true`, unlike the other five core family schemas that close undeclared fields. This permissive posture is intentionally thin in PR-001 and needs follow-up governance hardening.

## 4. Invariants
- Required field `id` must be present (enforced by schema `required` — CONFIRMED).
- Additional undeclared fields are currently permitted (enforced by `additionalProperties: true` — CONFIRMED).
- PROPOSED: production release manifests SHOULD include `spec_hash` and `version` even though optional today.
  - NEEDS VERIFICATION: enforce via release validator/policy in a follow-up aligned with ADR-0023.

## 5. Cross-references
- Sibling contracts: `contracts/release/promotion_decision.md`, `contracts/release/rollback_card.md`, `contracts/release/correction_notice.md`, `contracts/release/withdrawal_notice.md`.
- Schema file: `schemas/contracts/v1/release/release_manifest.schema.json`.
- Governing ADRs: `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`, `docs/adr/ADR-0002-contracts-vs-schemas-split.md`, `docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md`.
- Policy paths: `policy/release/` (PROPOSED — scaffold-level).
- Validator: `tools/validators/release/validate_release_manifest.py` (PROPOSED — not wired in `tools/validators/_common/run_all.py`).

## 6. Status
- Doc status: PROPOSED until reviewed and merged.
- Schema status: PROPOSED (from schema `x-kfm.status` — CONFIRMED).
- OPEN: Release manifest schema is intentionally permissive in PR-001; fields for signed manifests, layer manifests, and rollback linkage are PROPOSED for ADR-0023 follow-up.
- NEEDS VERIFICATION: decide when to move `additionalProperties` from `true` to `false` after explicit field expansion.
