<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/sites-qwen-service-adapter-20261019
title: Optional Sites adapter for the existing Node Qwen runtime
type: verification-record
version: v1
status: default-off source proposal; deployment and human review pending
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-19
policy_label: public
owning_root: docs/
responsibility: Explain the bounded adapter, configuration, checks and recovery
truth_posture: CONFIRMED source and synthetic checks; live deployment NEEDS VERIFICATION
[/KFM_META_BLOCK_V2] -->

# Optional Sites Qwen service adapter

The owner requested the existing GoDaddy Node 22 Qwen experience in Public
Staging. Source is `a0-hosted-ai-web-20261017@7b02dc22369f97b68577f821dc9dc7021e91cde5`.
CONTRACT_VERSION is `3.0.0`. This is a source proposal only; no GoDaddy deployment,
environment, access, database, weights, private cache or public publication changes.

The new `/api/sites-qwen/v1/[...path]` route is default-off without a strong
`KFM_SITES_QWEN_TOKEN`. The authenticated recipient must identify exact Site
`appgprj_6acd1aafe0d88191a4306ea2ab44ed91` and a bounded opaque actor. Token
comparison is constant-time after length validation. The fixed origin must match
the existing public Qwen runtime configuration.

The adapter delegates to the same `app/api/ai/[...path]/route.ts` handler. It does
not instantiate a new inference runtime, queue, model, source resolver or account
store. Existing public Qwen guest ownership, global/user admission budgets,
source restrictions and resource/cancellation checks remain authoritative. Only
unverified discussion is accepted; Evidence, private selections, held layers,
account/admin/worker routes and the prior SmolLM2 model cannot be reached through
this route. The only projected context is a map display year/view, with no layer
IDs, location, source attributes or selection. The original public handler still
validates the question and bounds sensitive topics.

Opaque actor partitions map to existing short-lived public guest cookies in Node
memory, capped at 100 and one hour; cookies never leave the adapter. This is not
a durable archive or an account role. Node accounts, PC jobs and secrets are not
copied to Sites. The Site uses native ChatGPT identity for its own access.

After review, configure the same new random 32-byte base64url secret in Node
`KFM_SITES_QWEN_TOKEN` and Sites `KFM_STAGING_QWEN_TOKEN`, and set Site
`KFM_STAGING_QWEN_ORIGIN` to the reachable reviewed Node origin. The existing
preview API returned HTTP 401, so its provider access layer must explicitly
support this service request; token configuration alone is not proof of access.
Keep production publication held. Never use a browser session or administrator
password as the adapter credential.

Verification: 45 focused existing/new cases pass, including four actual adapter
cases (token/Site/actor refusal, exact model identity, cookie/session separation,
and discussion-only context). Model responses are synthetic, not inference
qualification. Build/types/lint and exact-head CI are recorded in the PR. No
full-suite, live inference, production deployment or independent approval claim.

Rollback disables the new token or reverts the bounded source addition after
review; retain all existing accounts, caches, sessions, source geometry and data
stores. The companion Site can remain usable for deterministic Find and local
release checks with Qwen disconnected. Existing ownership roots follow accepted
Directory Rules v2 / ADR-0029; no new canonical authority or schema home.
