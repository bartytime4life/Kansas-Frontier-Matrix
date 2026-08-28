# AgentOperationEnvelope fixtures

This directory contains deterministic, synthetic cases for the fixture-only `AgentOperationEnvelope` contract.

- `cases.json` contains compact definitions for six schema-valid role/disposition records and seven negative records.
- `tools/generators/agent_operation_envelope/build_agent_operation_envelope.py` renders each candidate deterministically in memory and pins valid operation IDs.
- The Watcher, Planner, and Executor records use no real source payload, credential, policy decision, review, attestation, branch, pull request, or Kansas fact.
- A valid Executor record describes only a capability ceiling for an unprotected `agent/...` branch and a draft pull request. Effective permissions remain false.
- Invalid cases cover role overreach, protected-branch targeting, forbidden Planner output, missing Executor attestation, idempotency drift, disposition drift, and unsorted evidence references.

Run:

```bash
python tools/validators/governance/validate_agent_operation_envelope.py --fixtures
```

A passing fixture suite proves deterministic local conformance only. It does not activate an agent, source, token, workflow mutation, merge, release, deployment, publication, or public use.
