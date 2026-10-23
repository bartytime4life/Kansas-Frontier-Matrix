# Hosted flowline request efficiency

Status: **DRAFT_REVIEWABLE**, 2026-10-23. Source and synthetic behavior are
confirmed below; production capacity, publication, and human approval are not.
This is a separate follow-up to [PR #5431](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5431),
not a dependency or additional acceptance gate for its geometry optimization.

## Behavior and scope

The hosted `/api/hydrology/flowlines` handler previously issued one USGS read per
accepted request. Its browser cap of nine requests applied to each map, while
its private browser cache did not share reads between visitors.

The handler now owns one module-local pool. Its identity is the validated detail
and numeric fixed-grid cell; equivalent valid query spellings share work, while
local, regional and overview data remain separate. Invalid parameters are rejected
before pool lookup. The upstream URL, query, provider-directed filtering, stream
order checks, 6 MiB streamed input bound, 400-feature/80,000-vertex validation,
coordinate rounding and payload format remain unchanged. `EXTERNAL_CONTEXT_ONLY`,
source URL, truncation, original retrieval time and all existing limitations are
retained. Reuse does not become a new observation or source admission.

| Bound per live module instance | Value | Behavior |
|---|---:|---|
| Active provider loader operations | 9 | A new distinct cell over the bound receives 503; no queue |
| Waiting requests across all active cells | 96 | Includes duplicate subscribers; excess receives 503 |
| Successful response freshness | 1 hour | Absolute expiry; hits never extend it; no stale fallback |
| Cache entries | 36 | Bounded LRU, including short failure entries |
| Serialized successful cache bytes | 12 MiB total / 6 MiB per entry | UTF-8 accounting; larger results may be served but are not retained |
| Failure cooldown | 1 second per key | No successful/error payload substitution; then retry is permitted |
| Shared operation deadline | 30 seconds | Includes fetch, bounded body read and validation |

Nine active reads preserve room for one map's usual nine-cell burst. Under
multi-visitor saturation some cells are unavailable until retry; the existing
browser still marks those cells failed and waits its existing 60-second retry
interval. It does not yet use `Retry-After`. Errors and overload keep the existing
503/error shape, add `Retry-After: 1`, and use `Cache-Control: no-store`.
Successful responses remain private and receive the remaining freshness lifetime,
so cache reuse does not restart another full browser-cache hour.

One departing subscriber detaches and releases its admission slot without
aborting survivors. The last departure aborts the shared operation and removes
all subscriber callbacks. Failed HTTP bodies are cancelled before their operation
releases its slot. A timed-out or cancelled transport that ignores abort keeps
its active slot until its loader actually settles; late success is never cached.
This fails closed rather than admitting replacement reads over stuck work.

## Reproduce the synthetic measurements

After installing the locked dependencies in an isolated checkout, run:

```sh
node tests/flowline-requests.test.mjs
node tests/water-flow-motion.test.mjs

git show c336e8b38135d7110a79b44f038faee756006f21:app/api/hydrology/flowlines/route.ts > /tmp/kfm-flowline-baseline-route.ts
node tests/flowline-capacity.benchmark.mjs /tmp/kfm-flowline-baseline-route.ts

npm run build
node tests/flowline-capacity-http.test.mjs
```

A shallow checkout must first obtain the named base commit from the repository.
The diagnostic compiles the actual baseline and candidate route source and counts
every invocation of the substituted provider fetch. A held synthetic provider
response keeps the wave concurrent; there is no latency threshold. It prints
source hashes and counts. Every substituted URL must use the fixed USGS host.
The final HTTP regression uses the built Vinext route and 24 native loopback HTTP
clients, denies unexpected outbound fetches, and checks duplicate/cache behavior
and nine-admitted/fifteen-rejected distinct-cell admission.

Observed Node 22.13.1 source-route measurements:

| Synthetic wave | Baseline reads / peak active | Candidate reads / peak active | Candidate HTTP statuses |
|---|---:|---:|---|
| 24 identical cells | 24 / 24 | 1 / 1 | 24 × 200 |
| Replay 24 identical cells while cached | 24 additional | 0 additional | 24 × 200 |
| 24 different cells, held provider | 24 / 24 | 9 / 9 | 9 × 200; 15 × 503 |

The duplicate wave uses 95.83% fewer upstream fetch invocations. The distinct-cell
reduction is admission refusal, not faster delivery of all 24 cells. Tests cover
valid identity normalization, detail separation, bad queries, provider HTTP and
network failures, redirects, invalid JSON, provider error objects, duplicate
source IDs, declared/streamed byte overflow, timeouts, cancellation, recovery,
absolute expiry, empty responses, waiter limits, LRU and byte budgets, and
non-cooperative transports. They use synthetic data only.

## Validation and limits

Local source-route regressions passed: 13 new capacity tests and 18 retained
water-flow tests. Production build, TypeScript and changed-file lint passed using
an existing linked dependency set (Next 16.3.8, TypeScript 5.9.3), not the locked
Next 16.4.2 installation. A clean local `npm ci` could not retrieve packages
because registry DNS requests failed with `EAI_AGAIN`; its final npm error was
`Exit handler never called`. Initial type checking before build lacked generated
build-identity JSON; it passed after the build generated that file.

The local built-HTTP regression could not bind loopback (`listen EPERM`). It is
included in the ordinary built Node suite for exact-head CI; this local failure
is an environment limitation, not a passing check. Exact-head CI is recorded in
the PR after upload. No existing workflow or performance gate is weakened.

An independent review agent found and reproduced cancelled-subscriber retention
and uncancelled rejected-provider bodies. Both were corrected. Its reread found
no remaining blocking runtime defect and independently passed all 28 pre-integration focused
regressions. A separate 20,000-cancellation weak-reference/GC diagnostic retained
zero cancelled signals after collection. This is an independent AI review of the
recorded runtime hashes, not human approval or production qualification.

This protection is **per module instance in a process/isolate**. Inspection of
`server/start.mjs` confirms the standalone Node/Vinext entrypoint; it does not
establish the hosting replica count, concurrency, memory allocation, autoscaling
or maximum safe request rate. Replicas, isolated runtimes, process restarts and
cold starts have separate empty pools. There is no distributed coordination,
durable cache, paid service, background prefetch or deployment-wide ceiling.

The measured bound concerns application loader/fetch work, not proof of
synchronously closed TCP sockets, a hard process-RSS ceiling, sustained provider
rate or hosting capacity. Nine 6 MiB input reads, parsing, transient responses and
up to 96 consumers can still allocate substantial memory. Serialized cache bytes
are not total JS heap. Existing bounded-reader cancellation and fetch abort are
best effort at the transport level. A non-cooperative loader can temporarily
consume all slots, causing overload until it drains or its instance restarts.
Actual provider limits and production utilization remain unmeasured.

## Ownership and rollback

The accepted ADR-0029 adopts canonical Directory Rules v2 at
`docs/doctrine/directory-rules.md` (blob `fd49a0b83e55cef52c1124281f093e263526898d`),
superseding the supplied unversioned Directory Rules artifact. In this existing
standalone hosted composition, adjacent application implementation remains in
`app/`; conformance and the opt-in diagnostic belong to existing `tests/`;
this human explanation belongs to `docs/`; generation accountability belongs to
existing `data/receipts/generated/`. No new root, source, contract, schema, policy,
registry, release lane, storage binding or authority home is created.

The only shared changed path with #5431 is `tests/water-flow-motion.test.mjs`:
this change isolates simulated endpoint instances; #5431 adds geometry cases at
the end. PR #5431 merged as `15ec2493a7cf2e4b014b0d8d25069f1f7877d728`
during authoring; this follow-up retains its exact source tree and all 18 water
regressions pass on that integrated base. Application geometry and #5431's browser/doc files are untouched. Keep
its independent review and merge decision separate; reconcile test hunks if
integration order changes. Roll back by reverting this focused application/test/
documentation change while preserving subsequent work. No migration, data import,
provider refresh, environment change, deployment or publication is required.
