# AgentOperationEnvelope fixture builder

`build_agent_operation_envelope.py` constructs synthetic Watcher, Planner, and Executor envelopes in memory from the compact case manifest under `fixtures/contracts/v1/governance/agent_operation_envelope/`.

It uses the shared RFC 8785 JCS + SHA-256 package, a pinned virtual window, a fixed commit seed, sorted bindings, and fixed role ceilings. It writes no file, uses no network, and grants no authority.

Render one case:

```bash
python tools/generators/agent_operation_envelope/build_agent_operation_envelope.py \
  --case valid-executor-ready
```

The JSON is printed to stdout only. A rendered record is a fixture, not a credential, plan approval, branch, pull request, receipt, release, deployment, publication, or public-use decision.
