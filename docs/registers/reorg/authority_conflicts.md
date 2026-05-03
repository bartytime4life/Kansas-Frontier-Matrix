# Authority Conflicts (2026-05-03)

## 1) Schema authority split (`contracts/` vs `schemas/`)
- Status: CONFLICTED (managed)
- Evidence: both homes are active and documented; ADRs exist, but dual-home drift risk remains if machine assets are moved without explicit ADR authorization.
- Run decision: CONFIRMED no schema file moves across homes.

## 2) Policy authority split (`policy/` vs `policies/`)
- Status: CONFLICTED (managed)
- Evidence: both directories exist with policy-facing material.
- Run decision: CONFIRMED no policy-code relocation between homes; authority map retained as control surface.

## 3) Domain documentation refactor breadth
- Status: BLOCKED for this run
- Evidence: `move_plan.tsv` contains large-scale domain doc relocation candidates; bounded reference rewrite proof for all candidates was not executed in this run.
- Run decision: keep moves PROPOSED until lane-scoped execution batches are validated.
