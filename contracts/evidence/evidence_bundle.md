# evidence_bundle

> Status: PROPOSED
> Schema: https://schemas.kfm.local/contracts/v1/evidence/evidence_bundle.schema.json
> Schema file: schemas/contracts/v1/evidence/evidence_bundle.schema.json
> Validator: tools/validators/validate_evidence_bundle.py (CONFIRMED — wired in tools/validators/_common/run_all.py)
> Authority: contracts/ owns meaning; schemas/contracts/v1/ owns shape (ADR-0001, ADR-0002).

## 1. Purpose
`evidence_bundle` is the closure artifact that packages all material needed to support a governed claim scope. It answers whether evidence is sufficiently assembled (refs, source records, citations, rights, sensitivity, transforms, checksums, and spec linkage) to support downstream decisions. It is not a release manifest and not a policy decision object.

## 2. Lifecycle role
This object is formed in PROCESSED as the closure result of WORK evidence collection, where referenced materials are normalized and linked. It is validated before CATALOG / TRIPLET publication indexing and then referenced by runtime/release surfaces in PUBLISHED. Supersession happens via a new bundle with updated claim scope or evidence lineage; prior bundles remain auditable.

## 3. Fields
| field | type | required | meaning | examples or enum | policy/sensitivity notes |
|---|---|---|---|---|---|
| `bundle_id` | string | yes | Stable identifier for the closure package. | `bundle:hydrology:2026-05-08:001` | Anchor id used in audit and publish gating. |
| `claim_scope` | string | yes | Human/machine scope statement describing what claims this bundle supports. | `flood-risk-baseline:ks:county:shawnee` | Scope guides whether evidence is fit for intended exposure. |
| `evidence_refs` | array | yes | Set of constituent `evidence_ref` members included in closure. | array of `evidence_ref` objects | `minItems: 1` ensures non-empty proof linkage. |
| `source_records` | array | yes | Source-level record handles used to reconstruct provenance. | `raw/hydrology/usgs/2026-05-08/run-001.json` | Supports rights/sensitivity traceback during review. |
| `citations` | array | yes | Publication-ready citation strings backing the claim scope. | `USGS Water Data, retrieved 2026-05-08` | Missing citations can block publish release. |
| `rights` | object | yes | Effective rights summary after bundle assembly. | object with `license` | Must remain compatible with exposure channel obligations. |
| `sensitivity` | object (via `$ref`) | yes | Sensitivity labeling for bundle exposure constraints. | sensitivity label object | Drives deny/redact behavior in policy evaluation. |
| `transforms` | array | yes | Ordered transformations applied from source evidence to derived artifacts. | `reproject:EPSG:4326`, `aggregate:county` | Enables review of derivation risk and reproducibility. |
| `checksums` | object | yes | Hash map covering critical inputs/outputs in closure. | `{"source.csv":"sha256:..."}` | Detects tampering/drift before promotion and publish. |
| `spec_hash` | string (via `$ref`) | yes | Deterministic spec identity tying the bundle to contract/schema baseline. | `sha256:<64 hex>` | Allows policy/runtime to detect schema/spec drift. |

## 4. Invariants
- All required fields must be present (enforced by schema `required` — CONFIRMED).
- `evidence_refs`, `source_records`, and `citations` must be arrays, with `evidence_refs`/`source_records`/`citations` non-empty where schema `minItems: 1` is set (enforced by schema — CONFIRMED).
- `rights` must include `license` and no undeclared fields (enforced by nested schema object — CONFIRMED).
- `checksums` must contain at least one property and each checksum must match `^sha256:[a-f0-9]{64}$` (enforced by schema — CONFIRMED).
- PROPOSED: every runtime `outcome == ANSWER` should reference at least one bundle-closed evidence chain.
  - NEEDS VERIFICATION: enforce via `packages/evidence-resolver/` integration and/or runtime policy in `policy/runtime/`.

## 5. Cross-references
- Sibling contracts: `contracts/evidence/evidence_ref.md`, `contracts/evidence/kfm_geo_manifest.md`.
- Schema file: `schemas/contracts/v1/evidence/evidence_bundle.schema.json`.
- Governing ADRs: `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`, `docs/adr/ADR-0002-contracts-vs-schemas-split.md`, `docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md`.
- Policy paths: `policy/evidence/` (PROPOSED — scaffold-level).
- Validator: `tools/validators/validate_evidence_bundle.py` (CONFIRMED — wired in `tools/validators/_common/run_all.py`).
- Resolver package: `packages/evidence-resolver/` (PROPOSED — stub status).

## 6. Status
- Doc status: PROPOSED until reviewed and merged.
- Schema status: PROPOSED (from schema `x-kfm.status` — CONFIRMED).
- NEEDS VERIFICATION: define explicit resolver failure mode when an `evidence_ref` cannot be closed into a bundle.
