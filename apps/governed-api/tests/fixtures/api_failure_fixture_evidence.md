# API failure fixture evidence

This fixture-only #4416 slice is deterministic and offline. It translates
negative-path cases through the existing RuntimeResponseEnvelope fields without
adding a route, calling a live endpoint, emitting telemetry, or adopting a
public error-code registry.

| Evidence class | Status |
|---|---|
| Introduced | Ten-case fixture profile; sync/async operation adapter; WSGI handler guard; schema, determinism, invalid-response, timeout, cancellation, and no-leak tests |
| Inherited | WSGI 404/405 scaffold, closed envelope schema, Explorer root error boundary and retry/reset action |
| Skipped | Live endpoint, provider/dependency calls, telemetry, deployment, human acceptance |
| Not run | Hosted CI, APIsec, browser acceptance, production health, release checks |

ABSTAIN remains the outcome for unsupported scope, missing evidence, stale
dependency, and cancellation. DENY remains the outcome for policy denial.
Unsafe correlation input is replaced with unavailable; exception text, paths,
stack traces, secrets, and payloads are not included. The fixture
transport_status field is comparison metadata only and does not activate the
inactive HTTP binding profile.

The WSGI scaffold now accepts only its closed non-`ANSWER` envelope shape from
registered handlers. A synchronous exception or invalid handler return becomes
`500 Internal Server Error` with a safe `ERROR` envelope. The offline operation
adapter also proves rejected async work, timeout, and cancellation mapping. It
does not add a route, dependency call, telemetry sink, or production health
claim.
