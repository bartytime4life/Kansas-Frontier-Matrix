# evidence_ref

> Status: PROPOSED
> Schema: https://schemas.kfm.local/contracts/v1/evidence/evidence_ref.schema.json
> Schema file: schemas/contracts/v1/evidence/evidence_ref.schema.json
> Validator: PROPOSED — not yet wired
> Authority: contracts/ owns meaning; schemas/contracts/v1/ owns shape (ADR-0001, ADR-0002).

## 1. Purpose
`evidence_ref` is the smallest governed pointer to supporting material used in claim assembly and runtime explanation. It answers what item is being referenced and what kind of evidence it is. It is not the closure artifact and does not by itself guarantee citation completeness or policy clearance.

## 2. Lifecycle role
`evidence_ref` appears during WORK evidence collection and normalization, then is validated as part of bundle assembly before PROCESSED closure. In CATALOG / TRIPLET and PUBLISHED-facing envelopes it is carried as traceable linkage back to bundle-closed proof material. Pre-closure refs may exist without a bundle assignment; closure binds them.

## 3. Fields
| field | type | required | meaning | examples or enum | policy/sensitivity notes |
|---|---|---|---|---|---|
| `ref` | string | yes | Canonical pointer/id for the evidence item. | `ev:usgs:station:06892350:2026-05-01` | Must resolve through governed resolver paths before publish-grade use. |
| `kind` | string | yes | Declares evidence category for downstream policy and rendering behavior. | enum: `measurement`, `record`, `dataset`, `artifact` | Certain kinds may require additional checks before exposure. |
| `bundle_ref` | string | no | Identifier of the `evidence_bundle` that closed this reference. Unset when still pre-closure. | `bundle:hydrology:2026-05-08:001` | When absent, treat as pre-closure pointer and avoid claim-final ANSWER release. |

## 4. Invariants
- Required fields `ref` and `kind` must be present (enforced by schema `required` — CONFIRMED).
- `kind` must be one of `measurement | record | dataset | artifact` (enforced by schema `enum` — CONFIRMED).
- No undeclared top-level fields are permitted (enforced by `additionalProperties: false` — CONFIRMED).
- PROPOSED: if `bundle_ref` is set, it SHOULD resolve to an existing `evidence_bundle` identifier.
  - NEEDS VERIFICATION: enforce in `packages/evidence-resolver/` or a dedicated validator for `evidence_ref`.

## 5. Cross-references
- Sibling contracts: `contracts/evidence/evidence_bundle.md`, `contracts/evidence/kfm_geo_manifest.md`.
- Schema file: `schemas/contracts/v1/evidence/evidence_ref.schema.json`.
- Governing ADRs: `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`, `docs/adr/ADR-0002-contracts-vs-schemas-split.md`, `docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`.
- Policy paths: `policy/evidence/` (PROPOSED — scaffold-level).
- Validator: `tools/validators/validate_evidence_ref.py` (PROPOSED — schema points here, but not wired in `tools/validators/_common/run_all.py`).

## 6. Status
- Doc status: PROPOSED until reviewed and merged.
- Schema status: PROPOSED (from schema `x-kfm.status` — CONFIRMED).
- NEEDS VERIFICATION: confirm resolver contract for `bundle_ref` referential integrity.
