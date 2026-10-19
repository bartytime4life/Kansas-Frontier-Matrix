<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/published-delivery-diagnostics-20261019
title: Bounded GoDaddy published HTTP delivery diagnosis
type: verification-record
version: v1
status: source validated; exact-commit CI and hosted readback pending
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-19
policy_label: public
owning_root: docs/
responsibility: Distinguish a failed local startup check from public gateway delivery
truth_posture: Live 503 root cause UNKNOWN; no recovery claim
[/KFM_META_BLOCK_V2] -->

# Published HTTP delivery diagnosis

The replacement GoDaddy app `urdng3v1vk` serves the preview but the published
custom and provider hostnames return Service Unavailable. The domain is now
assigned to this replacement, the prior app is absent from the active app list,
and Public Staging has no custom-domain attachments. A production restart at
2026-10-19 07:45:26 UTC completed, but both published hostnames still failed.
These observations do not establish the original outage's root cause.

The current source follows GoDaddy's assigned-port contract: `server/start.mjs`
reads `process.env.PORT`, validates it and binds `0.0.0.0`. Local verification
using production mode, assigned port 20011 and the production AI/origin/trusted
host configuration serves both the apex and provider root/build routes and the
fixed www redirect. It does not exercise hosted model inference or prove
GoDaddy gateway availability.

The existing `KFM_NODE_STARTUP` loopback check reports UNREACHABLE without the
transport error. The check connects directly to the bound port on loopback and
does not resolve or test the custom domain. Its result alone cannot diagnose DNS
or the provider gateway, particularly because the hosted preview previously
served public routes while reporting the same loopback failure.

## Bounded diagnostics

Startup now includes the connection stage and an allowlisted transport error
code. Unknown errors become OTHER_ERROR. Raw messages, stacks, addresses,
response headers and response bodies are never logged. The existing five-second
check, identity validation, body/header limits and no-redirect behavior remain.

A passive observer watches only the first GET/HEAD of exactly `/` or `/api/build`
for at most 60 seconds after startup. It logs REQUEST_RECEIVED followed by a
fixed response outcome and status, or a bounded no-request/timeout/close result.
It removes every diagnostic listener on completion and does not keep the
process alive. The marked local startup request is excluded from this delivery
observation; that marker grants no authority and cannot alter application
responses. This is not an access log or a public endpoint.

NO_PUBLIC_REQUEST_OBSERVED means no matching unmarked root/build read was
observed during that startup window. It does not prove no request ever reached
the application, and it says nothing about other routes or requests after the
window. A finished Node response does not prove the CDN delivered it to a
visitor. Hosted readback must be compared with a contemporaneous browser test.

## Validation and scope

Ten focused real-HTTP diagnostic checks pass, covering valid identity, redirects,
invalid/oversized/stalled responses, a non-listening server, refused/reset
connections, private/query request exclusion, observer expiry/cleanup, stalled
or closed delivery, and unknown-parser-error redaction. Build, TypeScript and
changed-file ESLint pass. A separate real startup process with production
configuration passes apex/provider root and build checks, the www redirect,
and successful startup/delivery-report assertions. Exact-commit CI and hosted
preview/published readback remain pending at this source checkpoint.

The change stays in existing server, tests, docs and generated-receipt homes.
It changes no route, browser feature, login, authorization, model, DNS, secret,
subscription, database, private storage, original Site audience or source.
Reverting the source commit removes the diagnostic extension without migrating
stored state. Historical incident receipts remain unchanged.

References:
- https://developer.godaddy.com/en/docs/api-users/hosting/app-requirements
- https://github.com/godaddy/nodejs-hosting-agent-skill/blob/main/skills/godaddy-nodejs-hosting/contract.md
