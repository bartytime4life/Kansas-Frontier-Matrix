# Synthetic Seasonal Streamflow Tail Evaluator

Fixture-only implementation of the `StreamflowTailEventAssessment` contract.

```text
ordered IV fixtures + seasonal percentile fixture
  -> recency / qualifier / authority / persistence checks
  -> NO_EVENT | HOLD | ANSWER_CANDIDATE | ABSTAIN | DENY | ERROR
```

## Focused tests

```bash
python -m pytest \
  tests/pipelines/domains/hydrology/streamflow_tail_event/test_evaluate_fixture.py \
  -q --strict-config --strict-markers
```

This package performs no network access and has no operational-alert, promotion, release, or publication authority.
