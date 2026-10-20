# Smaller Ollama model on the existing GoDaddy app

> **Superseded context (2026-10-19).** The "accepted PC integration" and server
> login mentioned below were retired on October 19 ([login removal](login-removal-20261019.md),
> [PC inference](pc-inference.md)). The loopback `EACCES` result below concerns
> running a daemon inside the old GoDaddy app `q9r9beo47t`. It does not show that the
> replacement app blocks outbound HTTPS. Home-PC compute is now planned in
> [home Ollama inference](home-ollama-inference.md); that path needs no daemon on GoDaddy.

Status: **HOSTED BASELINE LIMITED / INSTALLATION BLOCKED / NOT INSTALLED**.
Owner constraints recorded October 16, 2026: keep inference off the owner's PC,
use Ollama with a smaller model, and add no hosting subscription, paid API,
commercial trial, or paid fallback.

This first change measures the existing GoDaddy runtime before downloading or
starting a model. It does not replace the accepted PC integration, create an
account, process a question, admit evidence, or change published source.

## Observed GoDaddy preview result

**CONFIRMED October 16, 2026:** the probe ran in app `q9r9beo47t` preview on
Node.js 22.23.3, Linux x64. The authenticated Preview logs reported
`BASELINE_LIMITED`; the private receipt was inspected and downloaded through
the provider File Manager. Its run ID is
`d85e2b43-275d-428a-9f06-0614340ca477`, observed at
`2026-10-16T15:31:36.529Z`. The candidate source was
`066ba0938f76c5cdbece522da4e25527d5eb0c64`.

| Check | Actual hosted result |
| --- | --- |
| Node subprocess with fixed marker | PASS |
| Execute fixed private program | UNAVAILABLE: EACCES |
| Bind/request an ephemeral private loopback port | UNAVAILABLE: EACCES |
| Mounted cgroup v2 app RAM/CPU values | UNKNOWN: unavailable |
| Ollama installation / model execution | NOT ATTEMPTED |

This blocks the proposed private Ollama daemon setup in the observed runtime.
It does not establish a SmolLM2 quality or performance result, prove an exact
provider policy cause, or establish that every GoDaddy product has the same
restrictions. A smaller model does not change these denied runtime operations.
Do not change bind addresses, use a public port, relocate executables to evade
the denial, or weaken isolation. Reopening this path requires provider-supported
native execution and private daemon communication on the existing plan, plus
verified app resource allocations. No additional paid plan is authorized.

The earlier dashboard sync attempt reported an overlapping import and an
upload failure, but the later Preview logs and private receipt prove the probe
itself executed. They do not prove a clean production build, general preview
health, native Ollama compatibility, or live acceptance. Preserve the private
receipt; do not publish the full runtime resource observations as app quotas.

## Current evidence and candidate models

At the authenticated dashboard inspection, app `q9r9beo47t` was attached to
Web Hosting Plus Launch and sourced from `a0-crawler-guidance-20261015` at
`e298f023d50878fc954e2037094236b2c15ebffc`, using Node.js 22. The cPanel plan
documentation lists 4 GB RAM for Launch. **The dashboard did not establish the
Node app's own effective allocation; cPanel limits must not be treated as a
measurement of that app.** The current PC model is a 5.2 GB download, which is
not itself a runtime-memory measurement.

These are candidate artifacts, not approved replacements or measured quality:

| Candidate | Published download size | License | Initial use |
| --- | --- | --- | --- |
| `smollm2:360m-instruct-q4_K_M` | 271 MB | Apache-2.0 | Smallest installation/structured-output experiment |
| `qwen3:0.6b` | 523 MB | Apache-2.0 | Alternative small model; thinking must be disabled |
| `smollm2:1.7b-instruct-q4_K_M` | 1.1 GB | Apache-2.0 | Later candidate only if memory/latency permit |

Verified provider pages on October 16, 2026:

- https://ollama.com/library/smollm2:360m-instruct-q4_K_M
- https://ollama.com/library/qwen3:0.6b
- https://ollama.com/library/smollm2:1.7b-instruct-q4_K_M
- https://www.godaddy.com/help/resource-limits-12001
- https://github.com/godaddy/nodejs-hosting-agent-skill/blob/main/skills/godaddy-nodejs-hosting/contract.md

Download size excludes runtime, context/KV cache, allocator and application
overhead. Smaller-model citation fidelity and useful extraction are unverified.
Do not reuse the PC profile's pinned 8B identity or 16,384-token budget for a
different model, or misrepresent a smaller model as the accepted PC profile.

## Private baseline check

The application startup hook is disabled unless
`KFM_OLLAMA_BASELINE_PROBE=1` is explicitly set. Enable it only on an isolated
preview of this exact candidate. It runs after the web server starts and catches
failures so the map does not depend on the probe.

It measures only:

- Node child-process execution with fixed arguments and bounded output/time;
- execution of a fixed, immediately exiting script in its own private directory;
- an ephemeral HTTP listener and request on `127.0.0.1` only;
- mounted cgroup v2 memory/CPU values when available;
- process RSS and clearly labeled host-memory/filesystem observations.

No environment dump, credentials, users/jobs, prompts, datasets or external
network requests are collected. It exposes no HTTP diagnostic route. It never
starts Ollama, pulls a model, contacts a cloud AI service, changes the firewall,
installs a system service or reads other private stores.

The directory `/private/kfm-hosted-ollama-probe-20261016` is mode 0700 and has
one retained attempt. An exclusive `.attempt` marker fences concurrent starts.
The fixed executable is mode 0700 and the JSON receipt is mode 0600. Repeated or
interrupted attempts are preserved and return `PROBE_ALREADY_ATTEMPTED`; there
is no automatic cleanup, overwrite, lock breaking or accumulation of retries.
Inspect the receipt through GoDaddy's authenticated private File Manager. A
receipt contains its observation time and exact run ID. Preserve it before any
separately reviewed retry.

An unavailable/unlimited cgroup value is **UNKNOWN**, not unlimited permission
or sufficient memory. Mounted cgroup values may omit ancestor restrictions.
Host RAM and filesystem free space do not prove an app allocation or quota.
`BASELINE_PRIMITIVES_PASS` proves only the observed primitives. It is not a
native Ollama load, model run, memory/latency acceptance or publication pass.

## Installation gates after the baseline

Proceed only if the existing plan permits native subprocesses and private
loopback operation with adequate measured resource headroom. Otherwise hold
this installation under the no-added-cost constraint; do not buy another server
or silently substitute a hosted API.

1. Confirm the actual effective app RAM, CPU and private-storage allowance.
2. Verify a supported native Ollama release and full artifact SHA-256 before
   executing it. Qualify ABI, extraction tools, private mount execution and
   persistent storage in the actual runtime, not only the build container.
3. Fetch exactly one candidate from the official Ollama registry into private
   model storage. Pin its full manifest/layer identities and retain license and
   integrity evidence. Model files do not belong in Git or public web assets.
4. Start the daemon as the unprivileged app user on `127.0.0.1:11434`, with cloud
   features disabled. Keep model loading lazy, single-concurrency and bounded.
   Verify restart/shutdown supervision and prevent duplicate daemon ownership.
5. Measure actual peak RSS, CPU, first-token/total latency and process recovery
   with a deliberately small context and output cap, without starving the map.
6. Add a separate admitted hosted profile. Preserve guest isolation, rights,
   sensitivity, release, cancellation, citation reconstruction and finite
   ANSWER/ABSTAIN/DENY/ERROR behavior. Do not fake the old PC heartbeat/model ID.
7. Test synthetic extraction and adversarial unsupported-citation cases, then
   independently test a real eligible released-evidence answer. The current
   Node composition's missing released-knowledge binding remains a separate
   limitation; installing a model does not release or create evidence.

## Placement, validation and rollback

Directory Rules v2 sections 10.1 and 10.4, accepted through ADR-0029, route this
bounded runtime check to the existing standalone application's `server/`,
its negative-path tests to `tests/` and operating guidance to `docs/`. These are
application-owned compatibility files, not a parallel canonical policy,
contract, infrastructure, data or release home. No original Sites source or
audience change is part of this candidate.

Run `node --test tests/hosted-ollama-probe.test.mjs`. Restricted local environments
may use `node --test --experimental-test-isolation=none` for the same tests.
Injected passing primitives in unit tests do not constitute hosted evidence.
No production build, hosted probe, model inference or live acceptance is
established by those unit tests.

Rollback unsets `KFM_OLLAMA_BASELINE_PROBE` and restores the prior accepted
startup file if needed. Preserve the private probe directory and receipts.
There is no data migration, credential rotation or destructive cleanup.
