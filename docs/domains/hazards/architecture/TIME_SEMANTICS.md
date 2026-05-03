# Hazards Time Semantics

Role-aware time semantics prevent stale or misleading hazard interpretations.

## Time fields by role

| Role family | Required fields |
| --- | --- |
| Historical events | `event_begin`, `event_end` (or source equivalent) |
| Warnings/advisories/watches | `issue_time`, `expiry_time` or `valid_until`, `retrieval_time` |
| Administrative declarations | `declaration_time`, optional incident period and amendment time |
| Regulatory context | `effective_time`, layer version/revision time |
| Scientific observations | `observed_time`, optional uncertainty interval |
| Remote-sensing detections | `product_time`, `analysis_time`, `retrieval_time` |
| Modeled derivatives | `model_run_time`, `input_release_refs`, `method_version` |
| Resilience analysis | `analysis_period`, `input_refs`, `review_time` |

## Freshness expectations

- Operational context must expose freshness and expiry status prominently.
- Historical records should not be rendered as active conditions.
- Detections and model outputs must show latency and uncertainty posture.
- Missing required time fields -> validation failure and non-promotion.
