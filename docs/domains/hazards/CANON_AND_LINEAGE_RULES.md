# Canon and Lineage Rules

## Canon boundaries

- Canonical truth for hazards is source-grounded and evidence-linked, not UI/render artifacts.
- Derived artifacts (tiles, summaries, cached payloads) must point back to release and evidence ids.

## Lineage rules

- Every promoted object must carry stable identity and lineage metadata.
- Corrections create successor objects linked by `supersedes` / `superseded_by`.
- Rollbacks change active pointers, not historical records.
- Unpublished work/quarantine artifacts must not appear as canonical public truth.
