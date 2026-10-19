# Hosted Qwen readiness and map interaction

Status: review candidate; public publication remains on hold.

## Problem and change

The map assistant previously checked AI readiness every five seconds, including
while the visitor used Find, which needs no model. A readiness request can last
12 seconds, so slow responses could overlap. Cold startup was also described as
unavailability even when the server said the worker was online and still loading.

The client now starts readiness checks only outside Find, permits one pending
read per active polling lifecycle, and aborts the read when the panel closes or
the visitor returns to Find. Late responses cannot update the newer lifecycle.
The existing five-second cadence and 12-second request timeout remain. Startup
copy distinguishes a loading model from an offline model and keeps the map and
source inspection available.

Non-JSON responses produce a fixed diagnostic code plus the HTTP status rather
than losing that distinction as a JSON parsing exception. The alert's
`data-ai-error` is restricted to fixed codes; `data-http-status` is restricted to
valid HTTP status numbers. Response bodies, arbitrary exception messages,
credentials and internal addresses are not rendered. Successful readiness clears
the diagnostics. Question drafts survive readiness failures.

## Scope and preservation

Base: composition branch `a0-hosted-ai-web-20261017` at
`1e6e06643f8c3c78fe4fc12b6e028f8e968e5be7`. Its tree matches the initially
inspected published `62f1bff1a1e8aa5eef72fdd7eb61c2db80e5b0b0`.

Changes use the existing `app/`, `tests/` and behavior documentation `docs/`
responsibility roots. The adopted Directory Governance Standard v2 and ADR-0029
were checked in the primary repository; the supplied reference directory did not
contain Directory Rules.pdf. No authority root or storage location was added.

This patch changes no model, dependency, database, source data, geometry,
authentication, origin authorization, queue capacity, inference deadline,
completion/repetition guard or release decision. It was authored in a fresh
isolated clone, without copying environment secrets or opening production stores.
The installed local composition and other worktrees were not reset or restarted.

## Validation

Six new component regressions cover Find without AI startup, non-overlapping slow
readiness, honest cold-start copy, non-JSON HTTP diagnostics, bounded exception
diagnostics/recovery, and abort/late-response isolation when returning to Find.
The first four were reproduced failing on the unchanged baseline before the fix.

The 99 focused assistant, hosted-model and public queue/HTTP contract tests pass.
These use controlled fixtures, not real hosted inference. The production build,
TypeScript and changed-area ESLint checks pass. The initial TypeScript attempt
ran before the build-generated identity existed; rerunning after the build
passed. Existing build chunk-size warnings remain.

## Browser observations and open checks

Before the repair, Chrome loaded the public map, but Ask moved from model loading
to connection unavailable and Send remained disabled. No question was accepted.
Later the same public tab showed `ERR_BLOCKED_BY_CLIENT`, as did the owner's
screenshot. Do not bypass Chrome protections or equate that page with a server
port collision.

A separate GoDaddy readback reported published Gateway error with infra OK at
the unchanged commit. The latest inspected runtime logged startup on the assigned
port 20011 and the same source digest, with a loopback EACCES result. No Qwen
crash, memory-exhaustion or address-in-use marker was present in the inspected
tail. The loopback result alone does not establish the cause of the gateway
error. No domain, DNS, secret or published runtime setting was changed here.

Live short/expanded reply, continuation, cancellation while moving the map,
measured latency and factual quality remain unverified. Passing fixtures are not
proof that this patch repairs the separate hosted connection/gateway failure.
Private preview acceptance must record its exact candidate and the unchanged
Published identity separately. Do not publish or merge based on this report.

## Rollback

Revert this candidate's client and test/document changes through review. No
database rollback, data migration or model replacement is needed. If privately
selected for preview, restore the prior preview selection; public publication is
a separate owner decision and remains on hold.
