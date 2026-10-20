# Home Linux Ollama inference

Task KFM-HOME-OLLAMA-20261019 · plan dated 2026-10-19 · base
`a0-hosted-ai-web-20261017` at `1d81882b2addb8f286b9ed49f516a3f8288045cc`.

**Status: PROPOSED, default off.** This change adds the home gateway kit and a
server provider adapter, with negative tests. It does not install anything on
either home PC, open router ports, change DNS, configure Cloudflare, set GoDaddy
secrets, deploy or publish. Hardware, connectivity, model quality and live
acceptance are still unverified. With no new environment variables set, the
server behaves exactly as before.

## Goal and request path

The goal is to let the owner's second Linux PC supply chat compute for
kansasfrontiermatrix.com. The public site stays on its GoDaddy Node app, and
visitors install nothing and sign in to nothing.

```
visitor ─▶ kansasfrontiermatrix.com (GoDaddy, same origin)
            guest job, rate limits, evidence/context rechecks, output checks
              │  HTTPS to one fixed origin, HMAC-signed, Access service token
              ▼
         Cloudflare named tunnel  (or: outbound polling worker, see below)
              │  outbound from the home PC; no inbound port
              ▼
         home PC: kfm-inference-gateway  127.0.0.1:8787   profiles, limits, admission
              ▼
         Ollama 127.0.0.1:11434  OLLAMA_NO_CLOUD=1, one model, one generation
```

The browser never calls the home PC, Ollama or the tunnel hostname, and never
receives a machine credential. The result returns through the existing
`server/public-ai-handler.mjs` checks, so a discussion stays
`ABSTAIN / UNVERIFIED_AI_DISCUSSION`, and factual answers stay withheld.

When the home PC is the selected provider and it is down, generation is
unavailable. Maps, source links, evidence discovery and exports keep working.
**Nothing falls back** to the embedded model, a paid API or another profile.

## What is in this change

| Area | Files | Default |
| --- | --- | --- |
| Home PC kit | [`scripts/home-inference/`](../scripts/home-inference/README.md): inventory, Ollama drop-in, gateway, hardened unit, host check, probe, tunnel/firewall examples | Inert until the owner installs it |
| Server adapter | `server/home-inference.mjs` | Loaded only when `KFM_AI_PROVIDER=home-ollama` |
| Provider selection | `server/public-ai-handler.mjs` (`selectAiProvider`) | `hosted-qwen3`, as before |
| Truthful model label | `/api/ai/status` `provider`, `model`, `modelLabel`; `app/assistant/workspace.tsx` | Embedded build still shows "Qwen3 0.6B" |
| Tests | `tests/home-inference.test.mjs`, `tests/assistant-status.test.mjs` | — |

The adapter implements the same `ready`/`online`/`discuss()` interface as
`HostedAiModel`. Guest sessions, job ownership, cancellation, budgets,
sensitivity checks, context rechecks and output qualification are reused
unchanged, and there is no second public chat authority. Selecting
`home-ollama` never forks the embedded model process, so it adds no model
memory to the GoDaddy app.

The fixed Sites adapter (`server/sites-qwen-handler.mjs`) requires provider
`hosted-qwen3` and the exact WebAssembly model. With `home-ollama` selected it
fails closed with `QWEN_MODEL_MISMATCH`. That is intended: changing the Sites
contract is a separate decision.

## Connection decision (phase 0 gate)

**Preferred:** a persistent named Cloudflare Tunnel behind Access Service Auth,
plus the gateway's own signature. The home PC dials out, so no router
forwarding, public home IP or dynamic DNS is involved.

Before choosing it, inspect the actual DNS authority and account eligibility.
A standard named tunnel needs a domain on Cloudflare. A partial (CNAME) setup
that keeps external authoritative DNS is a Business/Enterprise feature, and a
plain GoDaddy CNAME is not enough. This plan authorizes no nameserver move,
purchase or subscription. An already-controlled, eligible separate domain may be
evaluated without moving the website.

**Fallback:** an outbound home worker that polls KFM for jobs over HTTPS. Use it
when DNS must stay untouched. This is new server work: the current guest queue is
process-local, so it needs bounded leases, expiry, worker-scoped capability,
duplicate-result rejection and cancel propagation in an existing approved
persistence lane. The gateway in this change serves both options unchanged,
because the worker would call it on loopback.

**Excluded:** router port forwarding, any public Ollama, and Quick Tunnels in
production. A VPS relay and a private overlay/VPN are deferred.

**Deadline fact for the tunnel path:** Cloudflare's documented proxy read
timeout on non-Enterprise plans is 100 s (HTTP 524). Responses are bounded and
non-streamed, so gateway profiles cap each call at 90 s. At the deadline the
gateway returns the reply so far as length-limited, and the existing **Continue**
flow picks it up. Streaming would need a deliberate NDJSON-to-SSE choice and
full-path tests. It is not part of this change.

## Security properties (implemented and tested)

| Property | How |
| --- | --- |
| Raw Ollama never reachable | Gateway config refuses a non-loopback Ollama URL. No `/api/*` passthrough exists; unsigned and unknown paths get `401`. The unit sets `IPAddressDeny=any`/`IPAddressAllow=localhost` |
| Caller authentication | HMAC-SHA256 over scheme, method, path, timestamp, nonce and body hash; ±60 s skew; nonce single-use and claimed only after the signature verifies; constant-time compare; one indistinguishable `401` |
| Separate prod/staging credentials | Each key has a scope; a profile lists the scopes it serves; an out-of-scope profile looks unknown |
| Revocation without URL change | Remove the key and restart the gateway; Access service tokens are revoked separately in Cloudflare |
| No model substitution | The gateway serves a profile only when Ollama reports its exact digest and it is not remote. The KFM server also pins `KFM_HOME_INFERENCE_DIGEST` and holds chat on any mismatch |
| Caller cannot choose the model or limits | The request carries only `requestId`, `profile`, `depth` and `messages`. Context, output, sampling and time limits come from the owner's profile |
| Bounded everything | 32 KiB request, 16 messages, profile input budget, 32 KiB output, profile time limit, one generation, bounded queue; client response cap 64 KiB |
| Chat-template injection | Role markers (`<\|…`, `<start_of_turn>`, `[INST]`, `<think>`) are broken up in user and assistant text |
| Silent truncation | A prompt that fills the window is refused as `MODEL_CONTEXT_LIMIT`, not answered |
| Transport hygiene (server) | One exact HTTPS origin (HTTP only for loopback proofs); no URL credentials, path or query; `redirect: 'manual'` and any 3xx refused; JSON content type and gateway marker required; error codes from a fixed set |
| No private data in logs | Gateway and server log fixed codes and timings only; no prompts, replies, headers or secrets |
| Browser boundary | `/api/ai/status` exposes provider, model tag and label only, never the home URL, key ID or digest |

## Server activation (GoDaddy, owner action, after phases 0–2)

The existing master switch and origin rules are unchanged: `KFM_HOSTED_AI=1`,
an exact `KFM_HOSTED_AI_ORIGIN` and `VINEXT_TRUSTED_HOSTS`. Add these secrets,
staging values on Preview and production values on Publish:

| Variable | Value |
| --- | --- |
| `KFM_AI_PROVIDER` | `home-ollama` (explicit `hosted-qwen3` restores the embedded model) |
| `KFM_HOME_INFERENCE_URL` | `https://<tunnel hostname>`, origin only |
| `KFM_HOME_INFERENCE_KEY_ID` / `KFM_HOME_INFERENCE_SECRET` | The gateway key for this environment |
| `KFM_HOME_INFERENCE_PROFILE` | The approved profile ID, e.g. `kfm-default-chat` |
| `KFM_HOME_INFERENCE_DIGEST` | `sha256:<64 hex>`, the admitted model digest |
| `KFM_HOME_INFERENCE_ACCESS_ID` / `KFM_HOME_INFERENCE_ACCESS_SECRET` | Cloudflare Access service token (both or neither) |

Any malformed value disables chat: `/api/ai/status` reports
`HOSTED_AI_NOT_CONFIGURED`, and the log gets one fixed code such as
`HOME_INFERENCE_DIGEST_INVALID`. As with the existing flags, **set values
explicitly; do not rely on deleting a variable to disable it** (see
[public hosted AI](public-hosted-ai.md#private-activation-and-rollback)).

## Delivery phases and gates

| Phase | Work | Gate | State after this change |
| --- | --- | --- | --- |
| 0 Inventory and reconciliation | `inventory.sh` on the second PC; reconfirm the GoDaddy app, Published commit, canonical `www` → apex redirect, DNS authority, outbound HTTPS limits | Recorded inventory; transport chosen with no purchase or DNS change | Tooling ready; **not run** |
| 1 Local qualification | Pinned Ollama, `ollama-kfm.conf`, one model, profile with digest/licence, boot start, GPU/thermal | Repeatable benchmark and model record; Ollama loopback-only (`host-check.sh`) | Tooling ready; **not run** |
| 2 Protected transport proof | Tunnel + Access + gateway; `probe.mjs` with a staging key, synthetic only | Probe receipt passes from outside the LAN; revoke/rotate proven | Probe ready; real tunnel **not configured**. The GoDaddy-runtime leg is proven by enabling Preview with the staging key in phase 5 |
| 3 Provider adapter | `server/home-inference.mjs`, exclusive selection, default off | Changed-area tests, types, build, HTTP checks at the candidate head | **Implemented; local checks in the PR** |
| 4 Model catalog and UX | Truthful status label done. Approved alternative profiles and owner status views remain | Desktop/mobile, fresh visitor, unknown profile rejected | Label done; catalog **open** |
| 5 Private acceptance and security review | Real GoDaddy-to-home path, outage/restart/capacity drills, adversarial evidence fixtures, independent review | Recorded evidence and tested rollback | **Open** |
| 6 Production activation | Separate owner authorization; bounded rollout; canonical and `www` checks | Logged-out acceptance; maps survive an inference outage | **Open** |

## Acceptance matrix: evidence held by tests

| Area | Covered by `tests/home-inference.test.mjs` | Still needs real-host evidence |
| --- | --- | --- |
| Access | Missing, malformed, stale, forged, replayed, unknown and revoked credentials; Ollama management routes; out-of-scope profile | Access policy denies a request without a service token |
| Browser boundary | Status reveals no home URL, key or signature | Network-panel check on Preview |
| Bounds | Oversized body, unknown fields/options/roles, input budget, output cap, busy refusal, bounded queue | GoDaddy outbound timeout behaviour |
| Cancellation | Caller disconnect aborts Ollama and frees the slot; cancelled waiter leaves the queue | Browser cancel through the tunnel |
| Identity | Digest mismatch, remote model, missing model, missing profile, server-side digest pin | `host-check.sh` after a real `ollama pull` |
| Outage | Gateway down → `ERROR / MODEL_UNAVAILABLE`, no substitute | Stop Ollama, kill gateway, unplug network, reboot drills |
| Evidence | Unchanged handler: discussion stays `UNVERIFIED_AI_DISCUSSION` with no evidence refs | Adversarial evidence fixtures against the real model |
| Performance | Probe computes cold/warm wall time, p95, tokens/s | Every number. Targets (warm short reply ≤ 45 s, honest queue feedback) are design targets, not promises |

## Rollback

1. Server: set `KFM_AI_PROVIDER=hosted-qwen3` with `KFM_HOSTED_AI=0`, or set
   `KFM_HOSTED_AI=0` alone, and restart. Chat shows unavailable; deterministic
   search and maps continue. Re-enable the embedded model only after its own
   health and memory qualification (it does not fit Published on Plus Launch).
2. Pending work: a restart drops the process-local guest jobs. While the server
   keeps running and the gateway is down, queued jobs end as `MODEL_UNAVAILABLE`.
   A cancelled or expired job never receives a late result.
3. Home PC: stop `kfm-inference-gateway` and `cloudflared`, and remove or rotate keys.
4. Keep model digests, profiles, probe receipts and correction history. Delete
   no evidence, databases, model caches or unrelated source.
5. Revert this change only if needed; with the variables unset it is inert.

## Corrections to earlier records

- [`hosted-ollama-qualification.md`](hosted-ollama-qualification.md) mentions
  an "accepted PC integration" and server login. The October 19
  [login removal](login-removal-20261019.md) and
  [PC inference retirement](pc-inference.md) supersede both. Its
  loopback `EACCES` result was observed in the old app `q9r9beo47t`. It is about
  running a daemon inside GoDaddy, and does not show that the replacement app
  blocks outbound HTTPS. The home path needs no daemon on GoDaddy.
- The 2026-10-16 owner constraint "keep inference off the owner's PC" predates
  this plan. The 2026-10-19 request names a separate, dedicated second PC. Record
  the owner's confirmation that it supersedes the earlier constraint before phase 6.
- Old `KFM_PC_*` variables and account secrets must not be reused. The home
  provider has its own scoped machine identity, and visitors stay anonymous.
- The controlled-origin list includes the apex and specific previews, not
  `www`. Verify that `www` redirects to the apex with path and query intact; do not add a wildcard.

## Operating costs and risks

There is no per-token cost. Electricity, hardware wear, disk and internet
still cost money, and so may a domain or tunnel plan if one is ever needed
(none is authorized). Measure kWh per day at the wall and multiply by the local
rate. A single home PC is one failure domain: power, ISP and sleep outages
disable chat. Mitigations: wired Ethernet, masked sleep targets, BIOS power-on
after AC loss, an optional UPS. Faster compute does not fix missing evidence or
hallucination; abstention and denial stay in force.

## Sources

Retrieved 2026-10-19 with the plan: Ollama FAQ (binding, `OLLAMA_NO_CLOUD`,
concurrency, context length), API (`/api/chat` streaming NDJSON, `/api/tags`
digests), Linux service and hardware support pages; Cloudflare Tunnel, named
tunnel prerequisites, partial DNS eligibility, Access service tokens, proxy
timeout and buffering, Quick Tunnel limits. Repository sources were read at
`1d81882b`: `server/public-ai-handler.mjs`, `server/hosted-ai.mjs`,
`server/hosted-ai-origins.mjs`, `server/sites-qwen-handler.mjs`, `docs/pc-inference.md`,
`docs/login-removal-20261019.md`, and `docs/runbooks/godaddy-node-hosting.md` on monorepo `main`.
