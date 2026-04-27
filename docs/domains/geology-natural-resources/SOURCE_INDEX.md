# Geology & Natural Resources Source Index

Working map of source families and the claim classes they can support.

## Source family map

| Source family | Typical role | Can support | Cannot support by itself |
| --- | --- | --- | --- |
| State geologic maps and publications | `authoritative_interpreted` | Unit boundaries, lithologic interpretation, map-scale context. | Exact field measurement truth for every feature. |
| Borehole / well / core records | `borehole_reference` | Subsurface references, intervals, linked logs/sections. | Public exact coordinates unless policy explicitly allows. |
| Geophysical / geochemical observations | `observed_measurement` | Method-bounded observations with uncertainty and detection limits. | Region-wide interpretation without additional support. |
| Regulatory and administrative records | `official_regulatory_administrative` | Permit/lease/operator/compliance context. | Physical occurrence/reserve truth. |
| Derived interpretation/model products | `derived_interpreted` or `derived_modeled` | Correlations, potential/susceptibility surfaces, generalized public layers. | Declaring modeled outputs as observed deposits. |
| Legacy/historical archives | `legacy_corroborative_external` | Historical context and corroboration. | Current authoritative state without steward review. |

## Required source descriptor fields

- `source_id`
- `authoritative_role`
- `geographic_scope`
- `temporal_scope`
- `rights_license_use_constraints`
- `sensitivity_defaults`
- `review_state`
- `verification_status`

## Stewardship reminders

- Do not activate live connectors from this index.
- Keep rights and sensitivity states explicit before publication.
- Promote source descriptors only with closure artifacts (fixtures/tests/policy evidence).
