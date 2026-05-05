# Naming and Supersession Rules

## Naming guidance

- Use stable, explicit ids with domain prefix: `hazards.<object-class>.<id>`.
- Keep human labels mutable; ids should be immutable.
- Avoid encoding temporary status in ids.

## Supersession semantics

- `supersedes`: points to directly replaced object(s).
- `superseded_by`: backlink set by newer object.
- Supersession requires reason code (correction, schema migration, policy fix, source update).
- UI should surface latest active object while allowing lineage drill-through.
