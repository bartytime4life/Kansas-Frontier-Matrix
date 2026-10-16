# Public hosted AI: flexible discussion and released evidence

Status: This isolated candidate branch qualifies SmolLM2-360M uint8; NOT ACTIVATED.
The connected GoDaddy preview and public site are not changed by this branch.
Historical 135M observations below describe that model only.
Public publication remains a separate owner decision.
The owner requested server-hosted free AI, chat without login, and adaptable
conversation without compromising security.

## Confirmed engine and limitations

## Isolated 360M candidate, 2026-10-16

The owner rejected an external Cloudflare inference provider. This branch uses
the existing single manifest for the official Apache-2.0 360M uint8 model, revision
a10cc1512eabd3dde888204e902eca88bddb4951. Its 364,564,671-byte onnx/model_uint8.onnx file has SHA-256
57987a3a24dc34ad2cb5e7e566840ccaece095e35a24ae4fc5b3086c7ddd6918, verified
from the publisher's LFS pointer. The six support files retain their pinned
sizes/hashes from the earlier qualification. The hosted/probe workers validate its 960-dimensional hidden
state, 15 attention heads, five KV heads, 32 layers and 64-dimensional head.
The downloader's per-file size bound becomes 400 MB only for that exact pinned
model. This unconnected branch uses a 2,048 MiB process-RSS diagnostic budget.
The connected hosted app retains the 1,200 MiB guard. One WASM thread, 256 MiB worker heap,
512 input tokens, 18-second generation budget and 30-second watchdog remain.

Candidate private paths are /private/kfm-embedded-smollm2-360m-uint8-wasm-20261016
and /private/kfm-hosted-smollm2-360m-uint8-chat-20261016. These isolate experimental
bytes/receipts from the existing 135M install and refuse overwrite. They are
runtime qualification artifacts, not admitted evidence or new authority roots.
The single tracked identity remains server/embedded-ai-model.json.

CI first installs and checks synthetic inference, then uses a fresh process for
four fixed tasks: a short greeting, a polite rewrite retaining supplied details,
a fictional blue-marker scene and a red-paper-kite follow-up. Complete, bounded
outputs and subject retention are required; raw synthetic replies remain in the
receipt for inspection. This small suite cannot establish general correctness.
Model evidence selection stays held. Real KFM/user data is never test input.

Qualification CI is scoped to existing server code and its worker/resource tests.
Production build/type/HTTP checks and actual GoDaddy resource/quality acceptance
must be run before any later activation. No passing result is inferred here.
Directory basis remains ADR-0029 and Directory Rules v2 §§10.1/10.4, using the
standalone app's existing server/, tests/, docs/ and .github/workflows/ homes.
No roots, routes, schemas, policy or released-evidence bindings are added.
Rollback is to discard this unconnected branch and retain owner base b19e4cd38a11c0fee62fcb8c9417003f87198f5c.

The preceding q4 experiment at b93fce003cdd889fd6b202f4fac1430865695704 failed
CI run 38947478454 during MODEL_LOAD: EMBEDDED_MEMORY_LIMIT, sampled peak
1,679,233,024 bytes versus cap 1,258,291,200 bytes. Eight resource-control tests
passed; all four quality checks were SKIPPED. This does not prove a GoDaddy
provider quota or total model requirement, because the run stopped at the guard.
The uint8 candidate at 00b1b5ad28cf0c8979b11070ff5a35f2d487a8c2 also hit the
1,200 MiB guard during MODEL_LOAD in CI run 38947799372. Sampled peak was
1,316,384,768 bytes, with eight resource-control tests passing and quality checks
SKIPPED. Both are stopping-point measurements, not full requirements or GoDaddy
quota evidence. The next diagnostic keeps the uint8 weights and raises only
this unconnected candidate branch's cap to 2 GiB. This is safe for the bounded
CI experiment, not authorization or proof of safety for GoDaddy activation.
No hosted configuration, subscription or connected branch is changed.
The GoDaddy dashboard confirms Plus Launch and 2/25 app slots on 2026-10-16,
but its General/Change plan views do not expose the Node app's RAM allocation.
No assumption of 4 GB per Node app is made from cPanel plan advertising.
The uint8 candidate follows ONNX Runtime Web's CPU guidance to prefer uint8
quantized models; complete peak memory, speed and quality remain unverified.
Sources: https://onnxruntime.ai/docs/tutorials/web/performance-diagnosis.html
and https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct/raw/main/onnx/model_uint8.onnx

## Historical 135M observations

## 2 GiB diagnostic result

At runtime head 82baa562f38c42da938343acb64bad6ca7fadd52, CI run 38948058929
passed all eight resource-control tests and pinned uint8 synthetic inference.
Install receipt 7c910c76-4da4-44d2-8537-5ab36c6ee4ef observed "Blue", load
371 ms, inference 669 ms, peak RSS 1,713,278,976 bytes (download/load included).
Fresh-process discussion receipt 4ddcdadf-dc16-47e3-b240-e0d9141a97af observed
peak RSS 1,675,726,848 bytes and four requests taking 1,161/1,634/2,178/3,168 ms.
The kite follow-up passed; the polite rewrite simply repeated the original and
the scene omitted the requested marker. The greeting text was filtered by an
overly strict ten-character minimum in the qualification harness, so its model
quality is INDETERMINATE in that run. The harness now accepts nonempty short
replies, matching the existing public handler; a short "Hello!" must not fail
merely for having fewer than ten characters. Other quality requirements remain.

The 1,200 MiB guard was an agent-selected conservative code budget, not a
GoDaddy quota. Raising the isolated diagnostic guard proves more runtime fit,
not production safety or useful general instruction following. Activation is
HELD pending real hosted allocation/headroom and reply-quality acceptance.
No preview/public source, secrets, subscription or hosted guard was changed.

## Historical 135M observations (continued)

GoDaddy preview at 96ec5ddd5c1ca619a04993c0a40efa69ea9db57b produced private receipt
62e1f9c9-8082-414a-9402-0cd77c97f0e1 at 2026-10-16T16:23:48.310Z:
SYNTHETIC_INFERENCE_PASS, 5,500 ms download, 843 ms load, 5,985 ms generation,
12,853 ms total, sampled peak process RSS 1,041,661,952 bytes, Node 22.23.3
linux x64. This confirms actual hosted generation, not answer-quality acceptance.

SmolLM2-135M's later fact-selection tests FAILED. Constrained-number head f3cd651
selected fact 1 for an unsupported train-year question (CI 38933835051).
Evidence-copy head 06097547 also selected fact 1 for a gate-color question and
the unsupported question (CI 38934383002). Build, type, API and account tests
passed independently. These observations do not qualify factual selection.
Public evidence selection is therefore disabled in this follow-up.

The same Apache-2.0 SmolLM2-135M q4 revision and seven file sizes/hashes remain
in server/embedded-ai-model.json. The worker rehashes owner-only files under
/private/kfm-embedded-smollm2-wasm-20261016/model. It downloads nothing, loads the
locked single-threaded ONNX Runtime Web backend, and has no tools, native addon,
daemon, subprocess, extra listening port, paid inference API or PC dependence.

## User flexibility and truth boundary

Explore is the default UI choice. Users can ask follow-ups, brainstorm, request
plain/technical language and choose brief/expanded replies. Up to two prior
discussion turns from the same guest are supplied as untrusted conversational
context. Older turns are dropped to fit the 512-token input budget, with a
visible context-limit notice. The current question is never silently truncated.

Explore returns ABSTAIN / UNVERIFIED_AI_DISCUSSION with interpretation text,
answer=null and no EvidenceRefs/citations. The UI names it generated, unverified
discussion. It is not a KFM factual answer, EvidenceBundle, approval or release.
Output is plain text rendered by React. URLs, invented KFM references, protected
location precision and control characters are withheld. Sensitive questions are
denied before any generation. A prompt can influence wording, not server access,
publication authority, filesystem/network access, model identity or resource caps.

Evidence mode uses the existing server-owned governed reader. Missing knowledge
abstains. If released records exist, the user may inspect their source references,
but the model cannot turn its failed selection into an answer. References are
rechecked against the same release before return and on every read. Browser
input cannot supply evidence, release state or an administrator role.
The Node composition still has no released-knowledge binding; current real
evidence questions therefore return NO_RELEASED_EVIDENCE. Source capture is not
release authority. General model correctness is not guaranteed by runtime tests.

## Anonymous privacy and resource controls

/api/ai exposes status, job submit/read/cancel only. Steward/admin operations
remain on the existing authenticated /api/pc-ai surface; no account-management
or publication permission is given to visitors. A random Secure, HttpOnly,
SameSite=Strict host-only guest cookie protects that browser's opaque jobs.
Chat needs no username, password or invitation.

Writes require the exact configured HTTPS origin. Only declared mode/style/depth
values are accepted. One worker runs at a time, with at most three active/waiting
jobs, one per guest, ten guest submissions/hour and thirty process submissions/hour
across cookie resets. No forwarded client IP is trusted. These are single-process
limits; restart loses memory state and counters. Replica scaling requires shared
admission control and renewed qualification.

Guest capability expires after one hour. Questions, replies and follow-up context
expire after fifteen minutes with memory cleanup every thirty seconds. No prompts,
answers, cookies or credentials are logged or sent to an inference provider.
Input is at most 8 KiB, question 4 KiB, body read five seconds, evidence lookup eight
seconds, job ninety seconds, selection/discussion thirty seconds, model load
ninety seconds. Discussion has 32/64 output tokens for brief/expanded replies;
the UI discloses output/context limits. One WASM thread and a 256 MiB worker JS
heap are used. Sampled whole-process RSS over 1,200 MiB stops the worker without
automatic retry. WASM memory is outside the JS heap and may grow between samples.
Provider quotas and multi-replica fit remain UNKNOWN.

## Qualification, activation and rollback

Private KFM_HOSTED_AI_ACCEPTANCE=1 checks two fixed fictional discussion/follow-up
prompts and saves an owner-only v3 receipt under
/private/kfm-hosted-smollm2-chat-20261016. Public chat must be disabled during this
check to avoid concurrent worker copies. It stops after testing and refuses
overwrite/retry. Fixtures are not exposed by an HTTP route or admitted as evidence.
The receipt explicitly retains evidenceSelection=HELD_UNQUALIFIED.

After exact-head and owner release acceptance, normal chat uses KFM_HOSTED_AI=1
and KFM_HOSTED_AI_ORIGIN set to exactly https://kansasfrontiermatrix.com or
https://q9r9beo47t.preview.c38.airoapp.ai for the existing owner-protected preview.
For this HTTPS reverse-proxy deployment, also set VINEXT_TRUSTED_HOSTS to the
exact origin hostname (without scheme/path). The framework otherwise constructs
HTTP request URLs and the chat origin guard withholds requests. Do not use a
wildcard, trust arbitrary forwarded hosts, or disable the origin guard.
Remove acceptance and old embedded-probe flags first. These values are not
credentials. Do not copy published account secrets into preview. GoDaddy's own
preview login remains in place; no application login is required for chat.

Directory Rules v2 §§10.1/10.4 and ADR-0029 place app adapters in server/, routes
and UI in app/, tests in tests/, notes in docs/ and CI in the existing workflow
directory. The model manifest remains the single candidate identity. This adds
no canonical schema, policy, evidence or release home and leaves original Sites
audience/bindings and PC account role checks intact.

Exact base is owner-merged d1725d8d45986363a74d69c9368899f733c78f62. Rollback
removes KFM_HOSTED_AI and KFM_HOSTED_AI_ACCEPTANCE, restores that base with chat
disabled, and retains private weights and receipts. No database migration occurs.

## Conversation quality correction

The first v3 CI receipt at 2e971479 passed the bounded-generation check but
returned repetitive American-West text for both prompts. That is a runtime
observation, not usable-conversation acceptance. Discussion decoding now uses
fixed temperature 0.7/top-k 40 sampling, repetition penalty 1.15 and no repeated
three-token sequence. A prompt-derived seed makes the same bounded request
reproducible. These settings are server-owned, not user-supplied. A server check
withholds repeated four-word phrases appearing three times. Qualification also
requires distinct synthetic replies referring to the requested marker and kite
subjects. CI 38936438219 at exact head d1010b0 passed the bounded discussion and follow-up
check. Actual GoDaddy receipt ee0270a6-04f3-43a7-bc02-d03122d07aa5,
2026-10-16T17:04:45.846Z, also returned HOSTED_DISCUSSION_PASS: 43,195 ms total,
sampled peak RSS 1,020,940,288 bytes. Its source hashes match d1010b0. Replies
were short and incomplete. This qualifies bounded execution only; factual
selection stays held regardless of discussion quality.

CI 38936069523 confirmed identical official/manual tokenizer IDs and nonrepetitive
fiction output after decoding changes. Its follow-up drifted to a bird and failed
the requested-subject check. The official native-library reference was also
limited; tokenizer mismatch is not supported by that evidence. This remains a
model-quality limitation, distinct from passing build/API/security checks.
Expanded discussion now has an 18-second soft generation budget between token
steps, disclosed as output-limited, ahead of the 30-second parent watchdog. This
bounds longer replies without making an ordinary output cap disable the worker.
The private probe tests an unambiguous paper-kite follow-up with expanded output;
its outcome must be reported as observed, not inferred from compilation.

## Guest status recovery

Guest chat readiness now settles independently of the separate account-status
request. A failed or timed-out status check shows AI connection unavailable and
retry guidance, rather than Checking hosted AI forever. An origin hold shows a
bounded owner-setup message; arbitrary raw server errors are not rendered.
Five-second status polling retries, clears the notice on recovery and preserves
the unsent draft. No login, origin, evidence, policy or resource gate is relaxed.
Component-harness tests cover delayed account status, failed chat status, draft
retention, retry recovery and the origin-hold message. They do not prove hosted
browser acceptance. On 2026-10-16 the existing preview reported SmolLM2 ready
with no KFM account after its exact-host proxy setting was applied. The logged-out guest received a first discussion reply and a follow-up with
Technical / More detail selected. Both were visibly labeled generated and
unverified, with response-limit notices. The follow-up continued the lake/town
scene but missed the requested kite; option acceptance is confirmed, stylistic
or subject adherence is not. The 135M model's quality remains a material limit.
