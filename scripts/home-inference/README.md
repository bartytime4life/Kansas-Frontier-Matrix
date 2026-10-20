# KFM home inference kit

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
- A chat names a **profile**, a depth (`brief`/`expanded`) and up to 16 messages.
  The profile, not the caller, sets the model tag, its pinned digest, context
  window, output length, sampling options and time limit. Extra fields are refused.
- A profile only serves when `ollama list` has that tag **with the same digest**,
  and the model is not cloud-hosted. A changed or substituted model is held, never served.
- One generation at a time with a short bounded queue (`429 GATEWAY_BUSY` beyond it).
  A caller that disconnects cancels its generation. At the time limit the reply so far
  comes back marked length-limited; the visitor can choose to continue it.
- An over-long prompt is refused (`MODEL_CONTEXT_LIMIT`) rather than letting
  Ollama silently truncate it. Model "thinking" text is never returned.
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

**Tunnel deadline.** Cloudflare's documented proxy read timeout on
non-Enterprise plans is 100 seconds (HTTP 524). Keep every profile's
`timeoutMs` at or below 90000 for the tunnel path. The public chat also
caps a reply at 4096 bytes, so keep `outputTokens.expanded` at about 700 or less.

## Stopping and rollback on this PC

- Stop generation for everyone: `sudo systemctl stop kfm-inference-gateway`
  (KFM shows chat as unavailable; maps and source discovery are unaffected).
- Cut the network path: `sudo systemctl stop cloudflared`, or delete the tunnel's DNS route.
- Revoke the KFM server's access: remove its key entry and restart the gateway.
- Model weights, receipts and logs are left in place; delete nothing as part of a rollback.
