# Hosted repair and home-inference boundary review

Reviewed PR #5338 at `10dd7f616cca6a0eee8ccef74626473d9c82dcbd` and
the hosted target at `7e93a151be799956600e8baf649d8baa8bfd72de`.
GitHub records #5338 merged at 2026-10-20 14:47:44 UTC as
`87ae2eafdc74fc15eadc8c7e5b154fa2c9da73f2`, before this review began.
The only subsequent source changes were #5340's retired-origin cleanup.

The exact-head [Public core repair run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39359695955)
completed the build, TypeScript check, complete Node suite and actual HTTP/browser
boundaries. Its log records 1529 tests: 1512 passed, 17 skipped, zero failed;
all 23 home-inference tests executed successfully. The three original review
threads are resolved and their corrections remain in the hosted target.
The merged source was independently compared with GitHub's complete tree by
Git blob hash before local review, then built successfully.

## Independent assessment and corrections

| Boundary | Assessment and resulting behavior |
| --- | --- |
| Provider authority | One `selectAiProvider` decision selects hosted Qwen by default or explicitly configured home Ollama. Invalid configuration disables chat. The duplicate provider and gateway are absent. No automatic fallback. |
| Request authentication | Existing HMAC binds method, path, body hash, timestamp and single-use nonce. Scope restricts profiles; callers cannot choose raw model/options or reach model management. Retained. |
| Response authentication | HTTPS authenticates a transport endpoint, and a random request ID prevents accidental reply mixing. Neither independently authenticates the home gateway across a TLS-terminating intermediary. Add a domain-separated response HMAC bound to the exact request and response bytes/status, including health and authenticated errors. Reject unsigned, modified and replayed replies. No prior exploit is established. |
| Execution budget | A 600-second operator profile was accepted despite a 90-second example. A caller cannot override this, but queue wait was outside the generation timer. Refuse profiles above 90000 ms and enforce one deadline across queueing, fresh inspection and generation. Cancel upstream work and release admission on expiry/disconnection. Partial output remains explicitly length-limited. |
| Model identity | Both sides pin the configured digest; remote/missing/substituted models are held. Cached inspection could admit a recently changed tag. Reinspect after queue admission, require the streamed model name, and bind returned request/profile/digest/model on the server. |
| Ollama outage | A failure after readiness returns an honest unavailable result and immediately holds the adapter. A held model is unavailable even when the gateway itself is reachable. Scheduled health inspection can restore readiness; no substitute provider is selected. |
| Guest/evidence boundaries | Public handler, guest cookies, job isolation, denial gates, evidence/context rechecks and unverified-discussion labels remain unchanged. |

The two omitted safeguards merit correction before home inference is exposed:
response signing removes a transport trust assumption, while the enforced total
budget makes the documented limit reliable. Neither discrepancy alone proves
an exploitable vulnerability. Both corrections are default-inactive because
home inference still requires explicit configuration and activation.

Ollama's local operator/runtime remains trusted. Tag inspection and streamed
model-name checks do not attest the actual weights against a malicious local
runtime or a local operator swapping a tag between inspection and generation.
Do not mutate admitted tags during active requests.

## Verification and integration boundaries

Fifteen added regression tests exercise real gateway/client logic in process,
including tampering, replay, authenticated refusals, queue/inspection deadlines,
identity changes before and during queueing, model-name mismatch, outage status,
adapter request binding, stale in-flight inspection races and probe success/failure. Existing socket tests remain
mandatory in the full CI workflow. Local socket tests are blocked by the session
sandbox (`listen EPERM`); they are not treated as passing or removed.
Local build, TypeScript and focused ESLint checks passed. Reused local dependencies
are supplementary evidence; exact-head CI installs the committed lockfile.

The hosted branch reports `protected: false`. Active ruleset `Protect` (15484585)
targets only `~DEFAULT_BRANCH`, so its required build/CodeQL checks and review
rules do not apply to this hosted target. The direct branch-protection endpoint
returns 403 to the integration. No protection or bypass setting is changed.
Review resolution and a successful exact-head complete CI run are still required
for this follow-up's acceptance. Recheck the current target and head before merge.

No deployment workflow is added or invoked. The existing GoDaddy app, deployment,
hosted Qwen default, guest access and Sites composition remain unchanged. Gateway,
signature module and probe must be updated together before any separately
authorized home-provider activation; an older unsigned gateway fails closed.
