# Atmosphere / Air Parameter Registry

Registry contract for atmospheric parameters and unit discipline.

## Required parameter fields

- `parameter_id`
- raw unit set
- normalized unit
- conversion rule reference
- value bounds
- caveats and interpretation notes
- allowed knowledge characters

## Guardrails

- Conversions must be deterministic and test-covered.
- Parameter semantics must not drift by source.
- AQI-like indexes are not concentration parameters.
