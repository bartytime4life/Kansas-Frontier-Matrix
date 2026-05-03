# ADR-0012: Authority Boundary Compatibility Map (`contracts/` vs `schemas/`, `policy/` vs `policies/`)

- Status: proposed
- Date: 2026-05-03
- Deciders: KFM maintainers (pending CODEOWNERS confirmation)

## Context

The repository currently contains both `contracts/` and `schemas/`, and both `policy/` and `policies/`. This creates a recurring risk of accidental dual authority.

## Decision (proposed)

1. `schemas/` is the machine-shape authority surface. `contracts/` is semantic/narrative authority unless a later ADR grants a specific machine-contract exception.
2. `policy/` is the active policy-authority lane in this repository revision. `policies/` is treated as compatibility/documentation-only until an explicit superseding ADR is accepted.
3. Promotion remains a governed state transition; no directory move is treated as promotion evidence.

## Compatibility map

| Boundary | Current homes (CONFIRMED) | Allowed interim use | Prohibited duplication | Next decision required |
|---|---|---|---|---|
| Machine contract shape vs semantic contract docs | `schemas/` and `contracts/` | Cross-link both lanes and keep explicit pointers to canonical schema paths | Maintaining parallel machine-contract truth in both lanes | Accept/confirm ADR-0001 with repo-verified validators and fixtures |
| Policy authority lane | `policy/` and `policies/` | Keep `policies/` as non-authoritative compatibility docs only | Treating both directories as simultaneous normative policy sources | Accept follow-up ADR that either retires `policies/` or formalizes migration |

## Consequences

- Reduces ambiguity for contributors during reorganization.
- Preserves backward compatibility while preventing quiet authority drift.
- Requires follow-up ADR acceptance and validation evidence before any merge/re-home operation.

## Guardrails

- Do not merge `contracts/` with `schemas/` in this ADR.
- Do not merge `policy/` with `policies/` in this ADR.
- Do not move machine contracts or policy bundles based only on this proposed note.
