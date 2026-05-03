# ADR-0013: Policy Home Authority (`policy/` canonical, `policies/` compatibility-only)

- Status: proposed
- Date: 2026-05-03
- Deciders: KFM maintainers (pending CODEOWNERS confirmation)

## Context

This repository contains both `policy/` and `policies/`. Leaving both as normative policy homes creates dual-authority risk for runtime enforcement and review.

## Decision (proposed)

1. `policy/` is the canonical home for executable policy authority in this revision.
2. `policies/` is compatibility/documentation-only until a superseding ADR authorizes migration.
3. No policy release/promotion evidence is inferred from directory moves alone.

## Compatibility map

| Concern | Canonical home | Interim allowed use | Prohibited |
|---|---|---|---|
| Executable policy bundles, tests, and enforcement-facing policy references | `policy/` | Cross-link from `policies/` docs to canonical `policy/` paths | Parallel normative policy definitions in both trees |
| Human-facing compatibility notes | `policies/` | Keep explanatory docs that reference canonical policy artifacts | Storing authoritative executable policy only in `policies/` |

## Next decision required

- Accept or supersede this ADR after maintainers confirm migration/deprecation timing for `policies/`.
- Update docs/registers backlog row `VFY-005` closure evidence once this ADR is accepted.

## Guardrails

- Do not merge `policy/` and `policies/` in this ADR.
- Do not move policy bundles solely to satisfy naming symmetry.
- Do not claim runtime-policy equivalence for both directories.
