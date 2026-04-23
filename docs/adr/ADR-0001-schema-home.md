<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: ADR-0001: Canonical Schema Home for Machine Contracts
type: standard
version: v1
status: draft
owners: NEEDS-VERIFICATION
created: 2026-04-23
updated: 2026-04-23
policy_label: NEEDS-VERIFICATION
related: [../../README.md, ../README.md, ./README.md, ../../schemas/README.md, ../../contracts/README.md, ../../tests/README.md, ../../policy/README.md]
tags: [kfm, adr, schema-home, contracts, governance]
notes: [
  Draft ADR created to resolve canonical schema authority conflict documented in root backlog.
  Current repo contains both `schemas/contracts/v1/` JSON Schema files and `contracts/` narrative contract surfaces.
  Owners, policy label, and acceptance state remain NEEDS VERIFICATION until steward review.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0001: Canonical Schema Home for Machine Contracts

Decide where machine-checkable contract truth lives, and how non-canonical mirrors/aliases are governed.

| Field | Value |
|---|---|
| Status | proposed |
| Date | 2026-04-23 |
| Decision area | contracts / schemas / validation / release governance |
| Related contradictions | Root backlog marks schema home as `CONFLICTED / NEEDS ADR` |
| Related objects | DecisionEnvelope, EvidenceBundle, ReleaseManifest, source and policy schemas |
| Owners | NEEDS VERIFICATION |

## Context

KFM currently exposes two nearby surfaces that can be interpreted as contract authority:

1. `schemas/contracts/v1/` contains machine-readable JSON Schema artifacts across common, policy, evidence, runtime, release, source, correction, and data families.
2. `contracts/` exists as a parallel contract lane used for API/object/vocabulary documentation and boundary explanation.

Without a canonical-home decision, teams risk contract drift, ambiguous validator targets, mismatched fixture paths, and unclear upgrade/migration behavior.

## Decision

**Canonical machine-contract home is `schemas/contracts/v1/`.**

`contracts/` remains a human-facing companion surface for:

- explanatory narratives,
- API shape guides,
- object semantics,
- vocabulary and implementation-facing orientation.

Normative rules:

1. Any machine-checkable contract that gates validation, policy, promotion, or release must be authored and versioned under `schemas/contracts/v1/` (or a future `vN` path approved by ADR).
2. Files under `contracts/` must not silently become machine-truth substitutes for schema artifacts.
3. If compatibility aliases are needed, alias mapping must be explicit and tested (no implicit duplication).
4. Validators and tests must fail closed when contract path resolution is ambiguous.

## Alternatives considered

- **Alternative A — Canonicalize `contracts/`:** rejected because this conflicts with existing JSON Schema concentration in `schemas/contracts/v1/` and would increase migration burden now.
- **Alternative B — Dual authority (`schemas/` and `contracts/` both canonical):** rejected because it guarantees drift risk and weakens enforcement clarity.
- **Alternative C — Do nothing:** rejected because the current state is explicitly flagged as conflicted and blocks reliable validation governance.

## Evidence used

| Evidence | Status | What it supports |
|---|---|---|
| Root README backlog item naming schema home conflict and ADR need | CONFIRMED | This decision is required before stronger implementation claims |
| Presence of machine-readable schema files under `schemas/contracts/v1/` | CONFIRMED | Existing practical center of machine-contract gravity |
| Presence of parallel `contracts/` tree with narrative sublanes | CONFIRMED | Need to distinguish narrative contract docs from machine authority |
| Existing ADR README guidance that `ADR-0001-schema-home` is priority-high | CONFIRMED | This ADR is expected and should be first in sequence |

## Consequences

### Positive

- Validator tooling gets a single authoritative root for schema resolution.
- Fixture layout and CI checks can reference one canonical path.
- Contract review discussions can cleanly separate normative machine schemas from explanatory documentation.
- Promotion/release gates become easier to reason about and audit.

### Costs and follow-up burden

- Existing docs that imply dual authority must be updated.
- Any scripts referencing `contracts/` as schema origin must migrate to `schemas/contracts/v1/`.
- A compatibility/alias period may be required for downstream consumers.

## Verification required

Before upgrading this ADR from proposed to accepted:

1. Confirm maintainers and stewards for schema and contracts surfaces.
2. Inventory all validators/tests/scripts/workflows that resolve schema paths.
3. Add or update checks that fail when machine schemas are introduced outside canonical homes.
4. Add fixtures demonstrating valid/invalid contract path resolution.
5. Confirm `contracts/README.md` and `schemas/README.md` wording aligns with this authority split.

## Migration / implementation plan (proposed)

1. **Inventory:** enumerate schema-path consumers in `tools/`, `tests/`, and workflows.
2. **Enforce:** add validator rule for canonical schema path policy.
3. **Refactor:** update references to use `schemas/contracts/v1/`.
4. **Document:** patch root/docs/contracts/schemas READMEs to reference this ADR.
5. **Gate:** make canonical-path check part of CI.
6. **Review:** upgrade ADR status after evidence links and reviewer sign-off.

## Rollback or supersession path

If this decision proves incorrect:

- Create a superseding ADR (e.g., ADR-00xx) with explicit migration rationale.
- Preserve this ADR; do not delete history.
- Provide backward-compatible path aliases during transition.
- Attach validation evidence showing no silent contract drift during rollback/supersession.

## Open verification items

- Final owners and review sign-off set.
- Policy label confirmation for ADR publication scope.
- Whether any hidden automation currently treats `contracts/` as normative schema authority.

<p align="right"><a href="#top">Back to top ↑</a></p>
