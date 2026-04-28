# Source Role Boundaries

The ecology index validator enforces structural safety only. It does not assign authority across source roles.

## Role boundary rules

1. **Observed occurrence is not legal authority**
   - Observation or occurrence data supports presence claims, not regulation or legal status.
2. **Modeled habitat is not direct observation**
   - Habitat suitability and grid-level predictions cannot replace event-level evidence.
3. **Air/station telemetry is environmental context**
   - Station data may support context but does not identify taxa by itself.
4. **Hydrology joins are spatial context**
   - Watershed joins anchor place; they do not establish species presence without evidence refs.

## Validator implication

Because source-role metadata is enforced in upstream contracts/policy, this validator relies on:

- non-empty `domains`
- non-empty `evidence_refs`
- domain-specific join key conditionals

These constraints prevent the most common source-role collapse pattern: publishing structurally joined rows with no evidence anchor.
