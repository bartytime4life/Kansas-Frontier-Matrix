# Hazards Change Surfaces Matrix

Use this matrix to determine which files/systems need updates for common hazard-lane changes.

| Change type | Must review/update |
| --- | --- |
| New source descriptor | `SOURCE_INDEX.md`, source registry descriptor, fixtures, validators, policy allowlists/denylists |
| New source role | `SOURCE_ROLES.md`, `TIME_SEMANTICS.md`, drawer labels, policy checks, fixtures |
| New time field | `TIME_SEMANTICS.md`, contracts/schemas, fixtures, freshness UI |
| Promotion logic update | `PROMOTION.md`, validator outputs, CI checks, runbook notes |
| Drawer payload update | `UI_AND_EVIDENCE_DRAWER.md`, API payload contract, frontend mapping tests |
| Correction process change | `ROLLBACK_AND_CORRECTION.md`, operational runbooks, audit references |
| Naming/supersession change | `NAMING_AND_SUPERSESSION_RULES.md`, lineage validation tests |
