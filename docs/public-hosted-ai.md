# Public hosted AI: discussion and released evidence

Current candidate (2026-10-18): the active model implementation is Qwen3-0.6B
INT8. See [Hosted Qwen preview candidate](hosted-qwen-preview-20261018.md) for
its exact identity, memory bounds and LIMITED quality screen. The SmolLM2
model, cache and qualification statements below are historical checkpoints,
not current Qwen acceptance. Public publication remains ON HOLD.

GoDaddy Preview startup follow-up (2026-10-17): the dashboard was running
`npm run dev`, which launched Vite on port 5173 and failed with EACCES. The
standalone Node composition now makes that command build and start the same
production server as Publish, using the existing validated `PORT` handling.
Local hot-reload development remains available through `npm run dev:local`.
This also makes Preview run the same explicit AI startup switches as Publish.
The core delivery workflow checks the actual preview command on an assigned
port and verifies that the hosted AI route and guest interface are present.
No model, inference limit, domain, database or credential change is involved.
Local verification passed: production build, TypeScript, 43 focused AI tests,
15 real HTTP checks against `PORT=5184 npm run dev`, and the two built AI/account
HTTP suites. An initial cross-session HTTP attempt could not reach the local
listener; the same-session startup-and-test replay passed. Actual GoDaddy
activation and public browser acceptance remain to be verified for this follow-up.

Status: SmolLM2-360M q4 passes the four-task CI screen and actual GoDaddy v2
conversation acceptance at 8096f439c85cfc3ceda997031e14734a61554a43. All four
hosted replies completed without an output limit or memory-guard trip.
Guest browser checks must also be recorded with each activation.
Public publication is a separate owner decision.

## Model and execution

The single identity in server/embedded-ai-model.json is
HuggingFaceTB/SmolLM2-360M-Instruct, Apache-2.0, revision
a10cc1512eabd3dde888204e902eca88bddb4951. Its seven files have pinned byte sizes
and SHA-256 hashes. The q4 ONNX file is 387,943,246 bytes; SHA-256 is
a4ffda96e65beafc6f6cef0cbcf9fdc1cbdd79c230906bf3897d190547c7a596.
Publisher: https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct/tree/a10cc1512eabd3dde888204e902eca88bddb4951

The installer verifies downloads into owner-only directories and files under
/private/kfm-embedded-smollm2-360m-q4-wasm-20261016/model. The runtime rehashes
them before loading. Inference uses locked single-thread ONNX Runtime Web
WebAssembly inside a Node worker, without native addons, Ollama daemons,
subprocesses, extra ports, PC inference or paid inference services. Model files
are downloaded from the pinned publisher only during explicit installation;
questions and replies are never sent to an inference provider.

The selected server-owned profile is concise-sampled-v1: temperature 0.2,
top-k 40, repetition penalty 1.15, no repeated three-token sequences and a
prompt-derived deterministic seed. Browser input cannot set model identity,
paths, decoding parameters or profiles. The internal baseline/greedy profiles
are comparison controls, not additional models or visitor options.

## Visitor flexibility and security

Explore is the default: brainstorming, explanations, fiction and follow-ups,
with plain/technical language and brief/expanded reply preferences. Up to two
turns from the same guest are untrusted conversational context. Older context
can be dropped to fit 512 input tokens, with a visible notice. The current
question is rejected at the context limit rather than silently truncated.

Explore remains ABSTAIN / UNVERIFIED_AI_DISCUSSION with interpretation text,
answer=null and no evidence references. React renders plain text with a visible
unverified label. Sensitive questions are denied before generation. Control
characters, URLs, invented KFM references, repeated phrases and protected precise
locations are withheld. Model text has no tools or authority over accounts,
files, networks, publication or server configuration.

Evidence mode uses the existing governed reader. Factual model selection remains
HELD_UNQUALIFIED. There is no released-knowledge binding in this Node composition,
so real evidence requests return NO_RELEASED_EVIDENCE. When released references
exist they must be rechecked against the same release. A discussion pass does
not turn model output, source capture or uploaded documents into evidence.

The existing /api/pc-ai account/admin surface remains separate and authenticated.
Guest /api/ai exposes only status and opaque job submit/read/cancel operations.
A random Secure, HttpOnly, SameSite=Strict host-only cookie protects each guest's
jobs. Writes require the exact configured HTTPS origin; arbitrary forwarded
hosts and browser-supplied roles/evidence are not trusted.

## Resource and privacy bounds

One worker and one inference run at a time; at most three active/waiting jobs,
one per guest. Limits remain ten guest and thirty whole-process submissions per
hour, including cookie resets. These counters are process-local; scaling to
multiple replicas requires shared admission control and renewed qualification.

Source and evidence reads use a separate process-local buffer: two actual
resolver operations may run and eight may wait for at most one second. A caller
timeout does not release an actual operation's slot before it settles. At most
two result reads per guest and ten per process may remain pending, including
waiters sharing one check. Result polling is limited to sixty reads per guest
and three hundred per process per rolling minute; cookie resets cannot reset
the shared budget. Status and cancellation remain accessible during pressure.
Excess reads return HTTP429 with `AI_READ_BUSY` or `AI_READ_RATE_LIMIT` and
`Retry-After`; they return no unchecked answer or context. The client retains
the accepted job and draft, honors bounded retry delays, and never resubmits a
question to retry its status. Temporary read pressure is not source withdrawal.

Overlapping reads of one job share one fresh check. A later read always checks
again: no successful-result TTL bypasses source changes, and verified withdrawal
remains irreversible. These controls include preparation, pre-inference checks
and result reads, without changing source geometry, native values or detail.
They bound work within one process, not the number of replicas or all HTTP
traffic; hung resolvers retain their two slots and fail closed until settlement.
They do not qualify model accuracy or grant publication authority.

Guest capability expires after one hour. Questions, replies and context expire
after fifteen minutes; cleanup runs every thirty seconds. No visitor prompts,
answers, cookies or credentials are logged. Questions/output are at most 4,096
bytes; request body is at most 8 KiB with a five-second read deadline.
Evidence lookup is eight seconds. Evidence jobs expire after ninety seconds.
Discussion jobs have a bounded 810-second admission lifetime including queue
wait; once started, each run has at most 270 seconds. The three-job capacity,
single inference worker, generation watchdog and 15-minute retention stay fixed.

Model load is at most ninety seconds; inference has a 255-second parent
watchdog. Brief replies allow 160 tokens and 120 seconds; More detail replies
allow 384 tokens and 240 seconds between-token generation time. More detail is
the UI default. Limit notices and same-context continuation are shown. Completed
replies include a safe next-step question. Selected subsurface questions return
a deterministic server source summary with explicit unknowns, without factual
model generation or evidence promotion. These budgets cannot guarantee a
complete or correct model reply; the 512-token input-context limit remains.
The worker JS heap is 256 MiB, with one WASM thread. Whole-process RSS is sampled
every 100 ms; exceeding 2 GiB stops the worker without automatic retry. WASM
memory is outside the JS heap and may grow between samples. The guard is an
application budget, not an OS-enforced allocation or a verified GoDaddy quota.

KFM_HOSTED_AI_RESOURCE_PROBE=1 prints one owner-only startup record with Node's
constrainedMemory(), availableMemory() and process RSS. It allocates no test
buffers, reads no secrets or files, loads no model and adds no public route.
Zero/invalid/failed readings become null, never unlimited capacity. The hosted
observation did not reveal a per-app OS constraint. Host-reported free memory
does not establish a dedicated app quota; provider/shared limits remain unknown.
Reference: https://nodejs.org/docs/latest-v22.x/api/process.html#processconstrainedmemory

## Qualification evidence

CI 38954023188 at cb6c77e618f229e5faebf0b5f6dec9a6d9a1c1c2 passed installation
and all four checks with the selected profile: a short greeting, polite map
rewrite, child drawing with a blue marker, and the same child's red-paper-kite
follow-up. All four replies completed, taking about 10–29 seconds each; sampled
discussion peak RSS was about 1.79 GiB. Eleven focused local tests also passed.
This is a small screen, not general correctness or a performance guarantee.

The integrated branch at 57df03d9b944e7f7df84a7b11bb403f32fd3101b also passed
CI 38954903912: 49 targeted tests, production build, TypeScript, two built HTTP
test suites, verified installation and the same four selected-profile checks.
Actual hosted acceptance at cb6c77e returned LIMITED after explicit 0/1 flags
isolated the test. The existing receipt's bounded report confirmed
DISCUSSION_OUTPUT_UNQUALIFIED: greeting/rewrite/story passed in about 21/16/31
seconds, and the follow-up hit its 35-second soft cutoff. Sampled memory stayed
under the 2 GiB guard. This is a latency hold, not an observed memory failure.
The v2 check uses the same model/decoding, allows a 60-second soft cutoff with
a 75-second parent watchdog, and writes a fresh receipt rather than overwriting
v1. The ninety-second job deadline, cancellation, queue and rate bounds remain.
The earlier diagnostic head a2b3ced also passed all 50 targeted tests, build, types,
two HTTP suites, the selected model screen and the existing core-repair checks.

CI 38956673726 at 8096f439c85cfc3ceda997031e14734a61554a43 passed all 50
targeted tests, production build, TypeScript, two built HTTP test suites and
the v2 four-task model screen. GoDaddy Preview built that exact source Healthy
and its fresh v2 receipt reported HOSTED_DISCUSSION_PASS with all four tasks
qualified and complete. The 2 GiB guard remained in force. This confirms the
bounded hosted screen, not general factual accuracy or unlimited provider
capacity. Browser activation/acceptance is recorded in the follow-up PR.

With KFM_HOSTED_AI_ACCEPTANCE=1 and guest chat explicitly 0, startup can report
the already-created synthetic receipt as KFM_HOSTED_CHAT_CHECK instead of
rerunning or overwriting it. This reads one owner-only regular receipt file
with O_NOFOLLOW and a 64 KiB bound. Only fixed status/reason codes, timings,
RSS/limit numbers and per-task booleans are logged; prompt/reply text, source
paths/hashes and account data are omitted. No new public route is added.

The 135M model and 360M uint8 candidate had material instruction-following
failures. The pinned 360M q4 reference improved rewrites and continuity but still
invented a town name in a summary and missed some formatting instructions.
The selected WASM profile was screened directly; native CI reference behavior
is not used as proof of GoDaddy compatibility.

Regression tests accept a quoted single-sentence greeting and girl/boy as child
synonyms, while rejecting an unchanged imperative, two-sentence greeting and
follow-up missing the kite. The longer CPU cutoff permits a complete follow-up;
it does not weaken the four requested tasks or input/output security gates.

## Private activation and rollback

Use explicit 0/1 flag values: removed flags remained observable after a saved
GoDaddy restart during testing. Do not rely on deleting a flag to disable it.
When replacing an existing flag through GoDaddy's UI, delete and save it first,
then add the same name with its new 0/1 value and save again. Deleting and
re-adding the same name in one save removed the new value during this rollout.
This procedure applies to these known non-secret flags, not account credentials.

1. On the private Preview source, set KFM_HOSTED_AI=0,
   KFM_HOSTED_AI_ACCEPTANCE=0, KFM_HOSTED_AI_RESOURCE_PROBE=0 and
   KFM_EMBEDDED_AI_PROBE=1; restart and verify SYNTHETIC_INFERENCE_PASS in the
   owner-only log. Installation is one-shot and refuses overwriting files.
2. Set KFM_EMBEDDED_AI_PROBE=0 and KFM_HOSTED_AI_ACCEPTANCE=1, keeping
   KFM_HOSTED_AI=0; restart and verify HOSTED_DISCUSSION_PASS. Four fixed
   synthetic tasks save a private receipt under
   /private/kfm-hosted-smollm2-360m-q4-chat-20261016-v2-concise-sampled-v1.
   No fixture route or real KFM/user data is used. Acceptance stops its worker.
3. Set KFM_HOSTED_AI_ACCEPTANCE=0, then KFM_HOSTED_AI=1 for ordinary guest chat.
   Keep the other probe flags at 0. After the final build finishes, restart
   Preview explicitly before opening chat. A clean restart recovered a failed
   first model startup after deployment during this rollout; automatic model
   retries remain disabled. Verify logged-out discussion and follow-up in the
   browser before public activation.

KFM_HOSTED_AI_ORIGIN must be exactly https://kansasfrontiermatrix.com or the
existing private preview origin https://q9r9beo47t.preview.c38.airoapp.ai.
VINEXT_TRUSTED_HOSTS must be that exact hostname without scheme/path.
Do not wildcard hosts, weaken the origin guard, or copy Publish account secrets
into Preview. GoDaddy's owner protection for Preview remains in place; KFM chat
needs no application account.

The CPU timing follow-up is based on owner head
faa5b31c506e2fbb6a8d5b824281bc2127b8af69 (merged PR 5210) and preserves its
private resource diagnostic. Rollback sets all AI/probe flags to 0, restores
that exact source with the prior 35/45-second v1 limits and restarts Preview.
Earlier source e648e51e1dda3731c5f8d77cd1518507979b51c1 and the prior 135M
weights remain available if the owner chooses that model as a fallback.
No database migration, subscription change or public activation is performed
by qualification.

## Evidence search independent of generation — 2026-10-17

The follow-up based on `e3c8175884c844fbd917155b24424de69dddb507` separates
deterministic evidence discovery from the discussion worker. Previously a
model that was unavailable stopped evidence results, and a running discussion
held another guest's evidence search in the inference queue even though that
search never called the model.

The configured status response now includes `evidenceSearchAvailable: true`.
This means the bounded search route is available, not that a release or matching
records exist. Disabled runtime status explicitly returns false. The UI enables
Find evidence only with that explicit capability and keeps discussion dependent
on model readiness. A draft survives switching modes. Search links still carry
`ABSTAIN / EVIDENCE_MODEL_UNQUALIFIED`; they are discovery results, not a
model-selected factual answer.

Search retains the same shared admission limits, guest ownership, deadlines,
sensitivity check, packet validation and release rechecks before return and on
every later read. It returns a job without awaiting the second release read,
does not wait for the discussion worker, and never restores a cancelled or
expired result. There is no new data binding, evidence admission, model download,
model execution, resource-limit change or hosted activation in this change.

Validation: 43 focused local tests passed across assistant status, public chat,
model lifecycle, synthetic acceptance logic and PC account/worker boundaries on
Node 24.19.0. The final UI-copy adjustment was followed by 18 passing affected
tests. The two new availability/queue regressions failed before the fix. These
use synthetic evidence and mocked model calls; they do not qualify actual model
quality or prove hosted records. Full production build, Node 22 hosted replay,
changed-UI browser acceptance and independent review remain NOT_RUN.

Rollback: revert this follow-up's code and documentation together. The status
field is additive and the UI fails closed against an older server without it.
No migration or persistent-data rewrite is required. The prioritized remaining
work is in [the AI usefulness review](ai-usefulness-review-20261017.md).


### 2026-10-17: source summaries during model outages

Selected Underground sample summaries resolve the original public source on the
server and remain available when inference is offline. The UI labels this path
“Source summary available” and does not imply the model is ready. General
Explore discussion still requires a ready model; configured-origin, source,
policy, integrity, ownership and correction checks remain unchanged.

Model startup/termination writes fixed allowlisted codes to operator logs so
load, memory, identity and module failures can be distinguished. Public status
still exposes only readiness; no prompts, error messages, paths or stacks are
logged or returned by this diagnostic. The existing model, resource limits,
private files and no-automatic-retry behavior are unchanged. This diagnostic
is not proof that a hosted model has recovered; preview inference must pass
before publication.

### Continuation is conditional, not guaranteed completion

Final preview testing found that the 360M model could repeat an earlier reply
and reach its resource limit again instead of completing it. Larger budgets
therefore do not establish complete answers. An explicit continuation whose
four-word phrases mostly repeat its previous reply (at least 75%, with both
replies at least 24 words) is withheld with `MODEL_CONTINUATION_REPEATED` and a
narrower-question/source-record suggestion. It is not appended as useful history
and does not offer another automatic continuation. New detail sharing ordinary
subject words remains eligible. This heuristic does not prove answer quality,
completion or accuracy. Model replacement or runtime changes require separate
qualification; this patch changes neither. Publication remains held pending the
actual acceptance outcome and the unchanged dependency-audit disposition.
