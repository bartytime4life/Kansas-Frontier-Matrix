# source_descriptor

> Status: PROPOSED
> Schema: https://schemas.kfm.local/contracts/v1/source/source_descriptor.schema.json
> Schema file: schemas/contracts/v1/source/source_descriptor.schema.json
> Validator: tools/validators/validate_source_descriptor.py (CONFIRMED — wired in tools/validators/_common/run_all.py)
> Authority: contracts/ owns meaning; schemas/contracts/v1/ owns shape (ADR-0001, ADR-0002).

## 1. Purpose
`source_descriptor` captures the governed admission profile for a source before its records can influence downstream claims. It answers whether KFM may ingest and cite the source under stated rights, sensitivity, and access posture constraints. It is not a runtime answer object and it does not prove claim truth by itself.

## 2. Lifecycle role
This object is authored at RAW intake planning and used during RAW → WORK / QUARANTINE admission checks. It is validated before promotion into PROCESSED evidence assembly, then referenced indirectly through source records in CATALOG / TRIPLET and PUBLISHED outputs. Superseding a source descriptor requires a newer descriptor that re-evaluates rights/sensitivity rather than skipping lifecycle stages.

## 3. Fields
| field | type | required | meaning | examples or enum | policy/sensitivity notes |
|---|---|---|---|---|---|
| `id` | string | yes | Stable source descriptor identifier used by admission and audit paths. | `usgs_water_data` | Used as a join key for policy decisions and source registry lookups. |
| `domain` | string | yes | Domain lane where this source is intended to operate. | `hydrology` | Domain-specific policy gates may differ by lane. |
| `role` | string | yes | Declares evidentiary role expected from the source. | enum: `primary`, `corroborating`, `context`, `restricted` | Restrictive roles can trigger stricter promotion checks. |
| `authority` | string | yes | Human-readable authority statement naming publisher or steward. | `USGS Water Data` | Used during review when weighing source trust posture. |
| `rights` | object | yes | Rights bundle governing license and attribution obligations. | object with `license`, `attribution_required` | Rights obligations can force deny/restrict when incompatible with target publication surface. |
| `sensitivity_floor` | string | yes | Minimum allowed sensitivity level for this source's admitted use. | enum: `public`, `generalized`, `restricted`, `quarantine` | Policy-evaluable floor; a source admitted at one floor MUST NOT be silently re-admitted at a lower floor (PROPOSED enforcement in policy/source). |
| `update_cadence` | string | yes | Expected refresh rhythm used for stale and review timing. | `daily`, `monthly`, `irregular` | Impacts freshness policy expectations. |
| `access_posture` | string | yes | Access mode required to retrieve the source. | enum: `open`, `credentialed`, `restricted`, `closed` | Policy-evaluable posture for capability/access gates; downgrades require explicit review (ADR-0017). |
| `citation_template` | string | yes | Canonical citation pattern for downstream evidence/citation rendering. | `USGS Water Data ({retrieval_date})` | Missing/weak templates can block publishability when citation duties cannot be met. |

## 4. Invariants
- Required fields `id`, `domain`, `role`, `authority`, `rights`, `sensitivity_floor`, `update_cadence`, `access_posture`, and `citation_template` must be present (enforced by schema `required` — CONFIRMED).
- `role` must be one of `primary | corroborating | context | restricted` (enforced by schema `enum` — CONFIRMED).
- `sensitivity_floor` must be one of `public | generalized | restricted | quarantine` (enforced by schema `enum` — CONFIRMED).
- `access_posture` must be one of `open | credentialed | restricted | closed` (enforced by schema `enum` — CONFIRMED).
- `rights` must contain `license` and `attribution_required` and disallow undeclared members (enforced by nested schema object — CONFIRMED).
- PROPOSED: source re-admission MUST NOT lower `sensitivity_floor` without explicit policy review and receipt linkage.
  - NEEDS VERIFICATION: enforce in `policy/source/` and/or a dedicated validator beyond `validate_source_descriptor.py`.

## 5. Cross-references
- Sibling contracts: `contracts/source/ingest_receipt.md`.
- Schema file: `schemas/contracts/v1/source/source_descriptor.schema.json`.
- Governing ADRs: `docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`, `docs/adr/ADR-0002-contracts-vs-schemas-split.md`, `docs/adr/ADR-0017-source-descriptor-admission-process.md`.
- Policy paths: `policy/source/` (PROPOSED — policy lane currently scaffold-level).
- Validator: `tools/validators/validate_source_descriptor.py` (CONFIRMED — wired in `tools/validators/_common/run_all.py`).

## 6. Status
- Doc status: PROPOSED until reviewed and merged.
- Schema status: PROPOSED (from schema `x-kfm.status` — CONFIRMED).
- NEEDS VERIFICATION: confirm which `policy/source/` rego package enforces sensitivity-floor downgrade blocking.
- OPEN: whether `update_cadence` should be constrained to a controlled enum in a follow-up schema revision.
