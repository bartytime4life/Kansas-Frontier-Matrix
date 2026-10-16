# Public hosted chat

Status: PROPOSED anonymous chat integration. Owner requested chat without login
on 2026-10-16. Administrative and steward functions retain their existing login
and role checks through /api/pc-ai; this change grants no account-management,
publication, raw-data, filesystem or model-file access to visitors.

## Confirmed installation

GoDaddy preview at 96ec5ddd5c1ca619a04993c0a40efa69ea9db57b produced private receipt
62e1f9c9-8082-414a-9402-0cd77c97f0e1 at 2026-10-16T16:23:48.310Z:
SYNTHETIC_INFERENCE_PASS, 5,500 ms download, 843 ms load, 5,985 ms generation,
12,853 ms total, sampled peak process RSS 1,041,661,952 bytes. Node 22.23.3
linux x64. Seven pinned files were verified. This is actual hosted runtime
evidence; it is not proof of general answer quality or released KFM knowledge.

The same Apache-2.0 SmolLM2-135M q4 revision and SHA-256 manifest remain in
server/embedded-ai-model.json. Weights are retained under
/private/kfm-embedded-smollm2-wasm-20261016/model. The new worker reads and hashes
these private files before loading. It downloads nothing and uses no native
addon, paid API, daemon, subprocess, listening port or client-device inference.
No new model registry, policy or release authority is introduced.

## Anonymous behavior and bounds

/api/ai exposes status, job submission, owner-cookie job read and cancellation.
It has no administrative routes. Submitting the first question establishes a
random Secure, HttpOnly, SameSite=Strict, host-only guest cookie. No account,
password or invitation is needed. The cookie authorizes access only to that
browser's opaque job identifiers; it is not an administrator credential.
Requests require the exact configured HTTPS origin. Cross-origin POSTs,
browser-supplied evidence and arbitrary input fields are denied.

One model worker runs at a time. There are at most three preparing/queued/running
jobs, one per guest, ten submissions per guest per hour and thirty submissions
per process per hour. The shared budget also counts new cookies. No forwarded
client IP is trusted. State is memory-only: guest capability expires after one
hour and question/jobs expire after fifteen minutes (memory cleanup runs every thirty seconds); process restart loses jobs
and counters. These are bounded single-process controls, not a distributed
quota or a claim of DDoS protection. Do not scale replicas without shared
admission control and renewed resource qualification.

Requests are at most 8 KiB, questions 4 KiB, bodies five seconds, evidence
resolution eight seconds, jobs ninety seconds, model selection thirty seconds,
and model load ninety seconds. The model uses one WASM thread, a 256 MiB JS
heap, 512 input tokens and up to 32 generated tokens. Only a complete supplied fact matching the output after whitespace normalization can be selected; other text is withheld. Sampled whole-process
RSS over 1,200 MiB stops the model without automatic retry. WASM memory lies
outside the JS heap and may grow between samples. Provider quotas remain
UNKNOWN; the observed hosted synthetic peak is not a hosting entitlement.

Only the server-owned governed knowledge reader supplies evidence. Sensitive
questions are denied before model invocation. Missing evidence abstains. The
small model selects among at most four released documented facts and may select
none. Its free-form text is never published as a fact: the server copies the
selected assertion and citation from the verified packet. Context overflows,
malformed selections, unavailable models, withdrawn releases and cancelled or
expired jobs cannot produce a supported answer. Evidence is rechecked before
generation, before commit and on each answer read. Any omitted packet records
are disclosed as truncation. Selection accuracy remains a model limitation.

The current Node composition has no released-knowledge binding. Public chat
therefore returns NO_RELEASED_EVIDENCE until a separate governed release is
connected. Installing the model and removing chat login do not admit sources,
convert captured map data into released knowledge, or waive cite-or-abstain.
No prompts, answers, cookies or credentials are logged or sent to an AI provider.

## Preview qualification and activation

The private acceptance check is opt-in with KFM_HOSTED_AI_ACCEPTANCE=1. Keep
KFM_HOSTED_AI absent during this check to avoid concurrent model copies. It
retains one new owner-only receipt/attempt directory
/private/kfm-hosted-smollm2-chat-20261016 and checks two fixed synthetic selections.
It reads existing pinned weights, stops after checking and refuses overwrites.
Synthetic fixtures are not exposed by a public route or inserted into a reader.

After exact-head checks and owner release acceptance, enable the intended
variant with KFM_HOSTED_AI=1 and KFM_HOSTED_AI_ORIGIN set to exactly
https://kansasfrontiermatrix.com or the existing owner-protected preview origin
https://q9r9beo47t.preview.c38.airoapp.ai. Neither value is a credential.
Remove KFM_HOSTED_AI_ACCEPTANCE and the old KFM_EMBEDDED_AI_PROBE before enabling
normal chat. Do not copy published account secrets into preview. GoDaddy's own
preview login remains in force; anonymous chat means no application account.

Directory Rules v2 §§10.1/10.4 and accepted ADR-0029 place these app-owned
adapters in server/, routes/UI in app/, checks in tests/, operating notes in
docs/ and bounded CI in the existing workflow directory. The owner-merged base
is cb03737031dfab2f357984c3477d1cec4af59035. Original Sites source, audience,
bindings, accounts, PC API role checks and released-data admission are preserved.

Validation is pending at this draft's exact head: anonymous ownership and
cancellation, same-origin/input limits, shared/per-browser budgets, evidence
withdrawal, unsupported model output, existing account boundaries, built HTTP
routes and actual pinned-model selection. Host acceptance is a separate private
receipt. No public publication or general model-quality claim is made.

Rollback removes KFM_HOSTED_AI and KFM_HOSTED_AI_ACCEPTANCE, restores the exact
owner-merged base above and retains all private model files and receipts.
Anonymous state is disposable memory; no private database migration occurs.

## Output-validation correction after owner merge

The owner merged #5205 at d1725d8d45986363a74d69c9368899f733c78f62.
Its exact-head constrained-number test at f3cd651 failed: CI 38933835051
selected fact 1 for both a supported marker-color question and an unsupported
train-year question. Build, TypeScript, account/API and built HTTP checks passed;
they did not establish model selection quality. That selector must not be activated.

This follow-up removes forced-number decoding. It asks the small model to copy a
complete supporting sentence, then accepts only a complete supplied-fact match
with whitespace normalization. Unknown or other output becomes abstention through
the server-owned response path. No generated text or invented citation is emitted.
Qualification now requires two supported questions selecting distinct facts and
an unsupported question producing no selected fact (0 or null), as the actual
public handler requires. This tests withholding rather than requiring the model
to obey a particular abstention spelling. Exact-head and GoDaddy checks are pending.
Rollback restores d1725d8 with public chat disabled; keep prior receipts.
