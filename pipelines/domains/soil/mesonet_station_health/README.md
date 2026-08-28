# Synthetic Kansas Mesonet Station-Health Evaluator

This package implements the fixture-only `MesonetStationHealthAssessment` contract.

```text
synthetic normalized station batch
  -> deterministic freshness and anomaly checks
  -> HEALTHY_FIXTURE | HOLD | DENY | ERROR
  -> schema-valid candidate assessment
```

## Run the focused tests

```bash
python -m pytest \
  tests/pipelines/domains/soil/mesonet_station_health/test_evaluate_fixture.py \
  -q --strict-config --strict-markers
```

## Boundary

The evaluator does not access Kansas Mesonet, infer consent, write lifecycle data, resolve evidence, evaluate release policy, issue alerts, or publish. Live source activation and any public-facing use remain separate governed changes.
