# Hazards Source Index (Proposed)

Human index of first-wave hazard sources and intended role mapping.

| Source | Candidate descriptor path | Primary role | Notes |
| --- | --- | --- | --- |
| NOAA/NCEI Storm Events | `data/registry/hazards/sources/noaa-storm-events.v1.yaml` | `historical_event_record` | Historical records; not active alerts. |
| NWS Alerts | `data/registry/hazards/sources/nws-alerts.v1.yaml` | `operational_warning` / `operational_advisory` / `operational_watch` | Contextual only; not life-safety replacement. |
| FEMA Declarations | `data/registry/hazards/sources/fema-disaster-declarations.v1.yaml` | `administrative_declaration` | Administrative action, not observation. |
| FEMA NFHL | `data/registry/hazards/sources/fema-nfhl.v1.yaml` | `regulatory_context` | Regulatory area context only. |
| USGS Earthquake Catalog | `data/registry/hazards/sources/usgs-earthquake-catalog.v1.yaml` | `scientific_observation` | Observation feed with uncertainty and cadence rules. |
| NOAA HMS Smoke/Fire | `data/registry/hazards/sources/noaa-hms-smoke.v1.yaml` | `remote_sensing_detection` | Detection product; latency and limits required. |
| NASA FIRMS | `data/registry/hazards/sources/nasa-firms-active-fire.v1.yaml` | `remote_sensing_detection` | Detection feed; rights/rate limits must be confirmed. |
| Kansas/local context | `data/registry/hazards/sources/kansas-local-em-context.v1.yaml` | `local_context` | Disabled by default until steward and rights review pass. |

## Admission checklist

- Rights and attribution confirmed.
- Primary `source_role` assigned.
- Time fields specified.
- Freshness behavior specified.
- Evidence resolver mapping provided.
- Policy notes for restriction/generalization included.
