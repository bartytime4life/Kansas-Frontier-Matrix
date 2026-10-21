# KFM home inference kit

> Longer-answer candidate: the sample expanded timeout is for the outbound poll
> transport. For HTTPS, retain at most 90 seconds until the actual path is
> qualified. See [coordinated rollout](#longer-answer-candidate--2026-10-21).

These files go on the owner's **second Linux PC**, the one meant to supply chat
compute for kansasfrontiermatrix.com. They put one small signed gateway in front
of a loopback-only Ollama. Visitors never reach this PC: the KFM server calls
the gateway, and the gateway calls Ollama. The plan, its gates and the
server-side switch are in [`docs/home-ollama-inference.md`](../../docs/home-ollama-inference.md).

Nothing here is deployed by GoDaddy, and nothing here turns on public chat.
Each step below is something the owner runs deliberately on the home PC.

| File | Purpose |
| --- | --- |
| `inventory.sh` | Phase 0. Read-only hardware/OS/GPU/network/power inventory with redaction |
| `systemd/ollama-kfm.conf` | Drop-in for the official Ollama service: loopback, `OLLAMA_NO_CLOUD=1`, one model, one generation |
| `gateway.mjs`, `signature.mjs` | The gateway: Node.js 22, no dependencies, two signed routes, owner-approved profiles only |
| `profiles.example.json` | Template for the approved model profiles; refuses to load until a real digest is pinned |
| `systemd/kfm-inference-gateway.service` | Hardened unit: no fixed account, read-only filesystem, loopback-only network (offline `systemd-analyze security` exposure 1.3) |
| `host-check.sh` | Read-only check after install, reboots and updates: bindings, boot start, local-only mode, clock, sleep, firewall |
| `probe.mjs` | Phase 2/5. Refusal cases plus synthetic-only timings, written as a JSON receipt |
| `cloudflared.example.yml`, `nftables.example.conf` | Examples for the named tunnel and inbound firewall; use only after their gates |

## What the gateway does and refuses

- Listens on `127.0.0.1:8787` only, and only calls Ollama on `127.0.0.1:11434`.
  Both are checked in code at startup, and the systemd unit enforces them in the kernel.
- `GET /v1/health` and `POST /v1/chat` exist. Every request must carry an
  HMAC-SHA256 signature over method, path, body hash, a timestamp within 60 s
  and a single-use nonce. Unsigned, stale, replayed, forged and unknown-key
  requests all get the same `401`. Every other path, including all of Ollama's
  own `/api/*` routes (pull, delete, create, copy), is unreachable.
- Every authenticated health, chat and error response carries an HMAC-SHA256
  signature over its exact bytes and HTTP status, bound to the request's key ID,
  nonce, timestamp, method, path and body hash with a separate response domain.
  The server and probe reject unsigned, altered and replayed responses. A
  request-ID echo alone is not authentication across a TLS-terminating tunnel.
- A chat names a **profile**, a depth (`brief`/`expanded`) and up to 16 messages.
  The profile, not the caller, sets the model tag, its pinned digest, context
  window, output length, sampling options and time limit. Extra fields are refused.
- A profile only serves when `ollama list` has that tag **with the same digest**,
  and the model is not cloud-hosted. A changed or substituted model is held, never served.
  Admission rechecks the runtime after leaving the queue rather than trusting
  cached health. The streamed model name must also match the approved tag.
- One generation at a time with a short bounded queue (`429 GATEWAY_BUSY` beyond it).
  A caller that disconnects cancels its generation. At the time limit the reply so far
  comes back marked length-limited; the visitor can choose to continue it.
  Each profile is limited to 90000 ms, covering queue wait, readiness inspection
  and generation together. Expired queued work never starts generation.
- An over-long prompt is refused (`MODEL_CONTEXT_LIMIT`) rather than letting
  Ollama silently truncate it. Model "thinking" text is never returned.
  Before generation, the gateway reads `/api/show` thinking controls so an
  always-thinking model uses Ollama's separate reasoning channel. Inline,
  implicit and unfinished `<think>` blocks are also removed before either a
  complete answer or a deadline-limited partial can be returned.
- Logs one JSON line per request with timings, token counts and codes. Logs
  never contain prompts, replies, headers or secrets.

## Phase 0: inventory (read-only)

```bash
bash inventory.sh > ~/kfm-inventory-$(date +%F).txt
```

Keep the output private and read it before sharing it. Also measure, over a few days:
upload speed and latency, power draw under load (a plug-in meter is fine),
temperatures during a 10-minute generation loop, and whether the PC comes back
by itself after a power cut (BIOS: "Restore on AC power loss").
Choose the model only after this. Size it to fit VRAM, or RAM for CPU-only
inference, with room for the context cache.

## Phase 1: local qualification

Use Ollama's official Linux install, then pin its version. Run all of this on the inference PC.

```bash
# Ollama service: loopback, local-only, one model
sudo install -D -m 0644 systemd/ollama-kfm.conf /etc/systemd/system/ollama.service.d/kfm.conf
sudo systemctl daemon-reload && sudo systemctl restart ollama

# Never suspend: an inference server that sleeps is an outage
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

# Pull one candidate deliberately, then read its full digest
ollama pull qwen3:8b
curl -s http://127.0.0.1:11434/api/tags | node -e 'for (const m of JSON.parse(require("fs").readFileSync(0)).models) console.log(m.name, "sha256:" + m.digest)'
```

`qwen3:8b` is only an example tag. Record the publisher, tag, digest,
quantization, licence and your own evaluation before you admit any model.
Prefer wired Ethernet. Put the PC on a guest/IoT VLAN if your router supports it.
Turn off UPnP on the router: nothing here needs an inbound port.

## Gateway install

Node.js 22 or newer is required (`node --version`).

```bash
sudo install -d -m 0755 /opt/kfm-inference /etc/kfm-inference
sudo install -m 0644 gateway.mjs signature.mjs probe.mjs README.md /opt/kfm-inference/
sudo install -m 0755 host-check.sh /opt/kfm-inference/

# Approved profiles: copy the template, set the real digest, review every limit
sudo install -m 0644 profiles.example.json /etc/kfm-inference/profiles.json
sudoedit /etc/kfm-inference/profiles.json

# One key per environment. Never reuse a production key for staging.
node /opt/kfm-inference/gateway.mjs --new-key kfm-staging-202610 staging
node /opt/kfm-inference/gateway.mjs --new-key kfm-prod-202610 production
# Put the printed entries in {"keys":[ ... ]}:
sudo install -m 0600 /dev/null /etc/kfm-inference/gateway-keys.json
sudoedit /etc/kfm-inference/gateway-keys.json

sudo install -m 0644 systemd/kfm-inference-gateway.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now kfm-inference-gateway
sudo bash /opt/kfm-inference/host-check.sh
```

The gateway refuses to start if the key file can be read by other accounts.
Give each secret only to the environment it belongs to. Production goes in
GoDaddy's Publish secrets and staging in Preview's; never put one in Git or a
chat message.

**Rotate or revoke a key:** add the new entry, `sudo systemctl restart
kfm-inference-gateway`, update the KFM secret, then remove the old entry and
restart again. Restarting cancels any generation in progress. **Change
profiles:** edit `profiles.json` and `sudo systemctl reload kfm-inference-gateway`.
Reload preserves active and queued requests in FIFO order; they retain their
validated profile and receive a fresh model inspection against that profile
before generation. New requests use the new profiles. Lower admission limits
take effect as accepted work drains, without cancelling it; higher concurrency
can admit queued work immediately. A smaller queue limit refuses new waiters
until the existing queue falls below it.

## Phase 2: protected transport (synthetic data only)

Choose the transport in phase 0 (see the plan). For the named-tunnel option,
start from `cloudflared.example.yml`. Create the Access application and a
Service Auth policy for a service token first, then route DNS. Then run the
probe from another machine:

```bash
KFM_HOME_INFERENCE_URL=https://inference.example.org \
KFM_HOME_INFERENCE_KEY_ID=kfm-staging-202610 KFM_HOME_INFERENCE_SECRET=... \
KFM_HOME_INFERENCE_PROFILE=kfm-default-chat KFM_HOME_INFERENCE_DIGEST=sha256:... \
KFM_HOME_INFERENCE_ACCESS_ID=....access KFM_HOME_INFERENCE_ACCESS_SECRET=... \
node probe.mjs --runs 5 > probe-$(date +%F).json
```

The probe exits non-zero unless every refusal check passes, the pinned digest
matches and the synthetic chats complete. Keep the receipt privately. It records
this path at this time; it is not a capacity or quality guarantee.

**Gateway deadline.** The parser refuses profile `timeoutMs` values over 90000;
this is an application limit independent of the transport provider's timeout.
Ollama's `outputTokens` allowance includes private reasoning as well as the
answer. The example allows 1024 tokens for brief replies and 2048 for expanded
replies so an always-thinking model can reach its answer. The gateway separately
caps visible answers at public chat's 4096-byte limit, preserving UTF-8 and
returning longer answers as partials that the visitor can continue. Hidden
reasoning never becomes a partial answer. Keep the deadline bounded for the PC.

**Compatibility and activation.** Update `gateway.mjs`, `signature.mjs` and
`probe.mjs` together on the inference PC before selecting the home provider on
the server. The new server refuses an older unsigned gateway; it never falls
back to another provider. Updating repository source does not install the kit,
change the GoDaddy application, select home inference, configure a tunnel or
authorize home-network access. Complete the plan's independent gates first.

The trusted home operator must not replace model tags during active requests.
Ollama reports the model tag in its chat stream, not a weights digest. Fresh tag
inspection detects changes before admission, but cannot attest a compromised
local runtime or an operator swapping weights between inspection and generation.

## Poll transport (no tunnel, DNS change or Cloudflare)

The worker connects out to the website and fetches signed chat requests for the
gateway, so nothing reaches this PC from outside. It is a relay: it has its own
worker key, never the gateway key, so it cannot create or change requests or
answers. The website verifies every reply.

```bash
cd ~/kfm-hosted/scripts/home-inference
sudo install -m 0644 worker.mjs /opt/kfm-inference/
# A separate key for the worker. Never reuse a gateway key.
WK=$(node /opt/kfm-inference/gateway.mjs --new-key kfm-worker-prod-202610 worker)
sudo install -m 0600 /dev/null /etc/kfm-inference/worker-key.json
printf '%s\n' "$WK" | sudo tee /etc/kfm-inference/worker-key.json >/dev/null; unset WK
sudo install -m 0644 systemd/kfm-inference-worker.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now kfm-inference-worker
sudo bash /opt/kfm-inference/host-check.sh
```

The website needs the worker key's ID and secret (`KFM_HOME_WORKER_KEY_ID` and
`KFM_HOME_WORKER_SECRET`), the production gateway key, the profile, the digest
and `KFM_HOME_INFERENCE_TRANSPORT=poll`; see the plan's server activation
table. Until the website has them, the worker logs `poll_failed` with
`SITE_HTTP_404` (the route is off) or `SITE_HTTP_401` (the key does not match)
and backs off; nothing else happens. `node /opt/kfm-inference/worker.mjs --check`
makes one signed poll and reports whether the site accepts the worker key.

The website defers routine health probes while an admitted generation is using
the serial worker, preserving the last verified readiness state. Its bounded
chat deadline, response authentication and outage checks still apply. Finishing
or cancelling that generation triggers a fresh health probe immediately.

Logs (`journalctl -u kfm-inference-worker`) carry fixed codes and timings only.

## Stopping and rollback on this PC

- Disconnect from the website (poll transport): `sudo systemctl disable --now kfm-inference-worker`.
- Stop generation for everyone: `sudo systemctl stop kfm-inference-gateway`
  (KFM shows chat as unavailable; maps and source discovery are unaffected).
- Cut the network path: `sudo systemctl stop cloudflared`, or delete the tunnel's DNS route.
- Revoke the KFM server's access: remove its key entry and restart the gateway.
- Model weights, receipts and logs are left in place; delete nothing as part of a rollback.

## Longer-answer candidate — 2026-10-21

This source revision raises the website/gateway UTF-8 reply ceiling from
4,096 to 16,384 bytes, including the cumulative continuation ceiling. Export
capacity is 16,384 characters, so any accepted UTF-8 reply fits without being
cut at the former 12,000-character export boundary. Limits remain finite;
`finishReason: length` still produces a visibly incomplete reply with a
continuation option. A continuation that exceeds the cumulative ceiling or
available model context is withheld rather than silently discarded.

The sample expanded profile moves from 2,048 to 4,096 generation tokens and
from 90 to 180 seconds. These are candidate budgets, not measurements or
installation evidence. Brief stays at 1,024 tokens / 60 seconds. The gateway
accepts profile timeouts up to 210 seconds, the site's poll lease lasts 220
seconds, the PC worker's gateway call lasts 230 seconds, and the public
inference job remains bounded at 270 seconds. Guest/hourly budgets, one active
generation, signature verification, model/digest pinning, loopback restrictions,
sensitivity checks, context rechecks and data-retention windows are unchanged.

**Coordinated rollout, not performed here:** first verify the active transport.
For `poll`, update the installed gateway and worker from this reviewed revision,
then change only the existing profile's expanded output/timeout values after a
resource measurement. Preserve its existing ID, model, digest, scopes, input
budget, context window, options, credentials and service configuration. Do not
copy the example profile over an admitted profile: its model is illustrative
and its digest is intentionally invalid until pinned. The website relay and
public-handler changes must also be deployed before the complete chain can
accept the larger reply. If only one side is updated, earlier limits still win.

For `https`, retain an expanded timeout of at most 90 seconds until that
specific tunnel/proxy path is measured and qualified for a longer response.
The 180-second sample is for the outbound poll path. No automatic transport
switch, service restart, model substitution or credential change is included.

Before production acceptance, exercise a long reply, a UTF-8 cap, a deadline,
Stop during generation, an unavailable PC and a source-context change. Observe
PC memory/latency and queue wait under the new profile. If accepted, record the
exact website revision and installed gateway/worker/profile revisions.

Rollback the existing profile's output/timeout first to its recorded prior
values, then revert the website and PC source as a coordinated reviewed change.
The old profile values remain valid under the new parser. Keep the paired
provider, identity, credentials, services and stored data intact. A website
source change alone does not prove that installed PC files or live limits changed.
