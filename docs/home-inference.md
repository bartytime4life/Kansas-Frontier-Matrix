# Home Linux inference PC (Ollama) for public chat

Task: KFM-HOME-OLLAMA-20261019. Status: **IMPLEMENTED DEFAULT-OFF / NOT DEPLOYED /
NOT QUALIFIED**. The provider adapter, gateway and operating files exist and pass
local tests. No home PC, tunnel, DNS record, GoDaddy secret or live site was
inspected or changed. Hardware, connectivity, model quality and live acceptance
remain unverified.

This is not the retired account-based PC integration ([pc-inference.md](pc-inference.md)).
Visitors stay anonymous and never contact the PC. No `KFM_PC_*` secret, login or
`/api/pc-ai` route is reused.

## Request path

```
visitor ─▶ KFM Node server (/api/ai, guest jobs, checks) ─HTTPS─▶ Cloudflare Access
        ─▶ named tunnel ─▶ 127.0.0.1:8787 gateway ─▶ 127.0.0.1:11434 Ollama
```

| Part | File | Responsibility |
| --- | --- | --- |
| Provider adapter | `server/home-ai-model.mjs` | Same `discuss()` interface as the embedded model. Builds the prompt with the existing `discussionSystem`, trims old turns to the gateway's byte budget, signs requests, verifies signed replies, pins profile and model digest, reports health. |
| Provider selection | `server/public-ai-handler.mjs` (`selectAiModel`) | `KFM_AI_PROVIDER` starts exactly one provider. Unknown or incomplete settings are unavailable, never a fallback. |
| Wire contract | `scripts/home-inference/home-ai-contract.mjs` | HMAC request signing (key ID, timestamp, nonce, body digest), replay cache, reply signatures, the only accepted request shape. |
| Gateway | `scripts/home-inference/home-inference-gateway.mjs` | Loopback listener; two routes; one run plus a short queue; pinned Ollama options; digest recheck per run; bounded, signed replies. |
| Host files | `scripts/home-inference/*.service`, `*.conf`, `*.example.*`, `inventory.sh` | Read-only inventory, Ollama drop-in, hardened gateway unit, config and tunnel examples. |

Public guest controls are unchanged: anonymous jobs, ownership cookie, same-origin
writes, rate and queue limits, sensitivity denial, context rechecks, output
screening and ANSWER/ABSTAIN/DENY/ERROR outcomes. Discussion stays
`ABSTAIN / UNVERIFIED_AI_DISCUSSION`; factual model selection stays held for
every provider. The Sites adapter keeps its fixed `hosted-qwen3` contract and
returns `QWEN_MODEL_MISMATCH` while the home provider is selected.

## Security properties

- **Two layers of machine authentication.** Cloudflare Access service-token
  headers (optional in code, required for production) and a gateway HMAC key.
  The HMAC covers method, path, a 13-digit millisecond timestamp (±60 s), a
  single-use nonce and the body digest. Keys are revocable by ID without
  changing the hostname; up to four keys allow overlap during rotation.
- **Replies are signed too.** The gateway binds each reply to the request nonce,
  HTTP status and body. A misrouted hostname, stale cache or forged response is
  rejected (`HOME_AI_REPLY_UNVERIFIED`). Unsigned edge errors are reported as
  `HOME_AI_UNREACHABLE` or `HOME_AI_ACCESS_DENIED`.
- **No model substitution.** KFM pins `KFM_HOME_AI_PROFILE` and
  `KFM_HOME_AI_MODEL_DIGEST`. The gateway checks the installed digest on every
  health check and every run. A re-pulled tag changes its digest and makes chat
  unavailable until the owner re-qualifies and updates both sides.
- **Small surface.** Only `GET /v1/health` and `POST /v1/discuss` exist. The body
  must be exactly `{profile, depth, messages}` with a system message and
  alternating turns. Tools, images, formats, model names and sampling options
  cannot be sent. Ollama stays on loopback; the tunnel ingress admits only the two
  gateway paths.
- **Contained host process.** The gateway unit uses `DynamicUser`, receives its
  config through `LoadCredential`, may only use loopback (`IPAddressDeny=any`),
  and runs with a read-only system, no devices and no capabilities.
- **No content logging.** Both sides log fixed codes and timings only: no
  prompts, replies, headers, keys or hostnames.

Requests still pass through GoDaddy and Cloudflare, which terminate TLS. "Local
inference" describes where compute runs, not end-to-end secrecy from those
providers. State this in the visitor privacy text before activation.

## Time budget

Cloudflare answers HTTP 524 when a proxied origin takes 100 seconds to respond.
The gateway therefore limits each run, including queue wait, to 90 seconds
(`MAX_RUN_MS`) and returns the bounded partial reply with
`finishReason: time_limit`. The visitor sees the existing "incomplete reply /
Continue" notice. KFM's own job deadline (270 s) remains the outer bound. Real
streaming is deferred; it needs an SSE translation and full-path tests.

## Phase 0: inventory and decisions (owner)

1. On the second PC run `bash scripts/home-inference/inventory.sh > ~/kfm-inventory.txt`.
   It is read-only. Keep the output private; it contains hardware identifiers.
2. Also record: sustained upload and latency over a day, power draw at idle and
   under load (kWh/day × local rate), temperatures after 30 minutes of
   generation, and whether the PC returns on its own after power loss (BIOS
   "restore on AC power loss"). Disable sleep: `sudo systemctl mask sleep.target
   suspend.target hibernate.target hybrid-sleep.target`.
3. Verify the live GoDaddy app, deployed commit and runtime flags. The current
   Publish setting is `KFM_HOSTED_AI=0` ([public-hosted-ai.md](public-hosted-ai.md)).
4. Verify `https://www.kansasfrontiermatrix.com/<path>?<query>` redirects to the
   apex with path and query preserved. The AI origin gate accepts only
   `https://kansasfrontiermatrix.com` and named previews; do not add a wildcard.
   This session could not reach the live site to check.
5. **Transport gate.** A named tunnel needs a hostname on a Cloudflare-managed
   zone. Check where the domain's authoritative DNS lives. Do not move
   `kansasfrontiermatrix.com` nameservers or buy a plan for this. Options:
   an already-owned eligible separate domain on Cloudflare; otherwise the
   outbound polling fallback in the plan (not implemented here).
6. Confirm GoDaddy's Node runtime can make outbound HTTPS requests to that
   hostname (Phase 2 proves it). The October 16 loopback `EACCES` result was a
   different operation on a different app.

## Phase 1: local inference (owner, on the PC)

```bash
# Ollama (official installer creates the 'ollama' user and systemd unit)
curl -fsSL https://ollama.com/install.sh | sh
sudo install -D -m 0644 scripts/home-inference/ollama.override.conf /etc/systemd/system/ollama.service.d/kfm.conf
sudo systemctl daemon-reload && sudo systemctl restart ollama
systemctl show ollama -p Environment        # confirm every OLLAMA_* value
ss -ltn | grep 11434                        # must show 127.0.0.1:11434 only

# One candidate model, chosen from the inventory (fit RAM/VRAM with context).
ollama pull <tag>
ollama list                                 # the ID column is the digest to pin

# Gateway (Node.js 22+)
sudo install -d -m 0755 /opt/kfm-inference
sudo install -m 0644 scripts/home-inference/home-inference-gateway.mjs scripts/home-inference/home-ai-contract.mjs /opt/kfm-inference/
sudo install -d -m 0700 /etc/kfm-inference
node /opt/kfm-inference/home-inference-gateway.mjs keygen kfm-prod-1   # prints {"kfm-prod-1":"<secret>"}
sudoedit /etc/kfm-inference/gateway.json    # start from gateway.example.json; mode 0600, root
sudo KFM_GATEWAY_CONFIG=/etc/kfm-inference/gateway.json node /opt/kfm-inference/home-inference-gateway.mjs check
sudo install -m 0644 scripts/home-inference/kfm-inference-gateway.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now kfm-inference-gateway
journalctl -u kfm-inference-gateway -n 20
```

`check` prints PASS only when each profile's tag is installed with the pinned
digest; on FAIL it prints the installed digest. Pin the full 64-hex value:
`ollama list` shows an abbreviated ID (`curl -s 127.0.0.1:11434/api/tags` shows it all).

Profile guidance: start with one general profile. Keep `num_ctx` explicit and
include the KV cache in the memory budget. Set `"think": false` only for
thinking-capable models (such as Qwen3) and omit it otherwise. Pick tokens so a reply fits in about
60 s (brief) and 90 s (expanded) on this hardware; the gateway refuses longer
limits. Record publisher, tag, digest, quantization, license, measured
tokens/second, peak RAM/VRAM and evaluation result for each admitted profile.
Model weights stay outside Git and deployment bundles.

Local proof, still on the PC:

```bash
KFM_HOME_AI_KEY_ID=kfm-prod-1 KFM_HOME_AI_SECRET=<secret> KFM_HOME_AI_PROFILE=kfm-general-v1 \
  node /opt/kfm-inference/home-inference-gateway.mjs smoke http://127.0.0.1:8787
```

It sends one signed health request and one synthetic question, verifies both
reply signatures and prints `SYNTHETIC_PASS` with timings. Reboot the PC and
repeat without logging in, to prove unattended startup.

## Phase 2: protected transport (owner, synthetic only)

Only after the Phase 0 transport gate passes:

1. Create a Cloudflare Access application for the inference hostname with a
   **Service Auth** policy for one service token. Do this before routing DNS.
2. `cloudflared tunnel create kfm-inference`, install
   `scripts/home-inference/cloudflared.example.yml` as `/etc/cloudflared/config.yml`
   with the real UUID and hostname, then `cloudflared tunnel route dns` and
   `sudo cloudflared service install`.
3. From outside the home network: an unauthenticated request must be refused by
   Access; `smoke https://<hostname>` with the Access headers
   (`KFM_HOME_AI_ACCESS_CLIENT_ID/SECRET`) must pass.
4. From a GoDaddy **Preview** (not Publish), set the KFM variables below with
   `KFM_HOSTED_AI=1` and confirm `/api/ai/status` reports `provider: home-ollama`,
   `ready: true`. Then test: wrong HMAC key, revoked Access token, gateway
   stopped, Ollama stopped, model re-pulled, PC rebooted, internet unplugged.
   Each must leave maps working and chat reporting unavailable.

## KFM server settings

Set only as GoDaddy app secrets, never in source or the browser.

| Variable | Value |
| --- | --- |
| `KFM_HOSTED_AI` | `1` to enable public chat at all |
| `KFM_HOSTED_AI_ORIGIN` | exact allowed origin, unchanged |
| `KFM_AI_PROVIDER` | `home-ollama` (unset or `hosted-qwen3` keeps the embedded model) |
| `KFM_HOME_AI_URL` | `https://<inference-hostname>` — origin only |
| `KFM_HOME_AI_KEY_ID` / `KFM_HOME_AI_SECRET` | gateway key ID and secret |
| `KFM_HOME_AI_ACCESS_CLIENT_ID` / `KFM_HOME_AI_ACCESS_CLIENT_SECRET` | Access service token |
| `KFM_HOME_AI_PROFILE` | e.g. `kfm-general-v1` |
| `KFM_HOME_AI_MODEL_DIGEST` | `sha256:<64 hex>` of the qualified model |
| `KFM_HOME_AI_DISPLAY_NAME` | visitor label, e.g. `Llama 3.1 8B · KFM home PC` (optional) |

Use different gateway keys and Access tokens for Preview and Publish.
Selecting `home-ollama` never forks the embedded Qwen process, so it does not
consume GoDaddy memory.

## Operations

- **Rotate a key:** add the new key to `gateway.json`, restart the gateway, update
  the GoDaddy secret, confirm status, then remove the old key and restart.
- **Revoke:** delete the key from `gateway.json` or revoke the Access token.
  Either stops all requests immediately; the URL does not change.
- **Change model:** pull and qualify on the PC, update the profile digest, then
  update `KFM_HOME_AI_MODEL_DIGEST`. Between the two steps chat is unavailable by
  design (`HOME_AI_MODEL_IDENTITY`).
- **Diagnostics:** GoDaddy logs `[KFM home AI] <code>` on each state change;
  the PC logs `[KFM gateway] {"event":...}` with timings to the journal.

## Rollback

1. Unset `KFM_AI_PROVIDER` and set `KFM_HOSTED_AI=0` (or leave the provider
   selected; an unreachable gateway already reads as unavailable). Maps, source
   links, evidence discovery and exports do not depend on it.
2. Revoke the Access token and gateway key; `sudo systemctl disable --now
   kfm-inference-gateway cloudflared`.
3. Keep model digests, configs and acceptance records. Do not delete model caches,
   databases or evidence. Restore the embedded provider only by explicit
   selection after its own health is checked.

## Validation in this change

- `node --test tests/home-inference.test.mjs`: 13 tests covering config limits,
  signing/replay/expiry, the request shape, route and auth denial at the gateway,
  pinned options, digest mismatch, partial reply on time limit, provider config
  validation, exclusive provider selection, stale health, history trimming,
  unsigned/forged reply rejection, and a full guest job through
  `createPublicAiHandler` to a loopback gateway with a fake Ollama.
- Existing AI suites, production build, `tsc --noEmit`, the two built HTTP
  suites and ESLint on changed files pass at the candidate head.
- Not established: real Ollama compatibility on the PC, Cloudflare behavior,
  GoDaddy outbound HTTPS, latency, model quality, browser acceptance or
  publication. Production activation needs separate owner authorization.
