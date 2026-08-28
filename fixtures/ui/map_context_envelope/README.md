# MapContextEnvelope fixtures

`cases.json` contains sixteen synthetic no-network records: two valid candidates, four true JSON-Schema negatives, and ten schema-valid semantic negatives. Cases cover renderer-specific leakage, unpublished layers, temporal/TTL failures, selection/layer closure, release/evidence unions, canonical ordering, internal references, deterministic identity, viewport order, and filter arity.

No case resolves evidence, evaluates policy, creates release authority, authorizes public use, or mutates a map/runtime store.
