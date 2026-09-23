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

## Synchronous handler result cleanup

A synchronous handler must return a closed negative envelope. An awaitable
return remains `ERROR / INVALID_RESPONSE`, including when inspecting the result,
looking up its cleanup method, or closing it raises an ordinary exception or
`asyncio.CancelledError`. Cleanup failure does not reclassify that invalid return
as a request timeout or intentional cancellation. The WSGI guard still emits its
existing safe `500` JSON response with sanitized correlation and empty evidence.
An unstarted native coroutine is closed without executing its body.

Exceptions raised by the operation itself retain their existing finite mapping.
`KeyboardInterrupt`, `SystemExit`, and `GeneratorExit` raised to the guard remain
process-control signals; the guard does not turn them into response envelopes.
Python's native coroutine-close protocol may itself consume `GeneratorExit`.

The added regression tests exercise the synchronous and WSGI boundaries with
synthetic failures, safe and unsafe correlation identifiers, closed-envelope
schema checks, and response headers. They do not start a server or prove a
deadline for arbitrary synchronous cleanup, production recovery, telemetry,
or human acceptance. The existing app-owned source, tests, and evidence note
remain in place under accepted [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and [Directory Rules](../../../../docs/doctrine/directory-rules.md) §§7.2, 10.1,
and 14.1. No schema or finite vocabulary changes are involved.

Rollback the guard, regressions, this note, and the generated authoring receipt
together. A revert restores the invalid-result cleanup gap; prefer a bounded
forward fix.
