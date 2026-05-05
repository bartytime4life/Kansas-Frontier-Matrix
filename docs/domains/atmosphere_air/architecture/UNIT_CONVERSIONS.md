# Atmosphere / Air Unit Conversions

Unit handling requirements for atmospheric values.

## Required practices

- Preserve `raw_value`/`raw_unit` and `normalized_value`/`normalized_unit`.
- Attach conversion rule/version metadata.
- Validate bounds pre/post conversion.

## Priority conversions

- particulate concentration units
- gas concentration units
- meteorological unit harmonization
- visibility and optical context units

## Validation expectations

- deterministic conversion tests
- precision/rounding policy checks
- invalid-unit denial cases
