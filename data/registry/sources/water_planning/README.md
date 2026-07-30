# Water-planning source registry

This canonical source-registry child contains SourceDescriptor candidates for
the exact public geometry inputs used by the RAC dataset and county crosswalk.
The descriptors are `needs_review`, `proposed`, and `not_released`; their
connector activation state is `disabled`.

## Concrete inventory

| Descriptor | Role | Upstream version |
|---|---|---|
| `kwo_rac_feature_service.source.json` | Official KWO RAC planning-area geometry | Item modified 2026-06-24 |
| `census_tigerweb_counties_2025.source.json` | Official Census county geometry used for intersection | January 1, 2025 vintage |

Both records conform to
`schemas/contracts/v1/source/source_descriptor.schema.json`. They pin the
observed GeoJSON response digest but do not activate a recurring connector or
authorize public release.
