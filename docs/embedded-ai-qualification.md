# Embedded server-side SmolLM2 qualification

Historical record: current candidate execution uses Qwen3-0.6B INT8. See
[Hosted Qwen preview candidate](hosted-qwen-preview-20261018.md) for its
current identity and limits. None of the earlier model results below qualify
Qwen or authorize public publication; that remains ON HOLD.

Status: **PROPOSED app integration; native GoDaddy failure CONFIRMED; WASM qualification pending**.

The owner authorized a free, non-trial alternative to Ollama on October 16, 2026.
This candidate embeds Transformers.js 4.3.1 / ONNX Runtime Node 1.30.0 in the existing
GoDaddy Node app. Inference occurs in a Node worker thread on the hosting server.
There is no Ollama daemon, executable subprocess, extra listening port, browser
model execution, paid inference API, new subscription, or commercial trial.

## Scope and observed evidence

The previous Ollama preview receipt denied private execution and loopback binding
with EACCES. This candidate uses the library's documented server-side API and
normal npm native addon loading; it does not change provider isolation or relocate
an Ollama executable. Whether GoDaddy admits this library is still unverified.

A separate Linux x64 Node 22.23.3 CI experiment at
`1879540a78ed207d006b2201d47b277efeb53979` successfully loaded CPU inference and
returned `The sample marker is blue.` from a fixed synthetic sentence.
Load time was 3,912 ms; generation was 626 ms; sampled final RSS was 948,060,160 bytes.
Those are CI observations, not GoDaddy performance or app quota measurements.
The final pinned, local-files-only probe subsequently passed at
`0e2ff851e718eb03399e0c991a10298a6e6f46c7`, CI run 38928256962.
It returned the same synthetic answer in 904 ms, with 799 ms model load,
3,950 ms download, 5,847 ms total, and sampled peak process RSS of
1,007,284,224 bytes. npm ci, six negative-path tests, and the app production
build passed in that run. The separate existing Public core repair candidate
workflow also passed at the same head (run 38928326902).

The primary publisher's Apache-2.0 model is
`HuggingFaceTB/SmolLM2-360M-Instruct`, revision
`a10cc1512eabd3dde888204e902eca88bddb4951`.
The q4 ONNX file is 387,943,246 bytes, SHA-256
`a4ffda96e65beafc6f6cef0cbcf9fdc1cbdd79c230906bf3897d190547c7a596`.
Every required metadata/tokenizer/model file has a pinned size and SHA-256 in
`server/embedded-ai-model.json`. The model card is retained beside the weights.
npm package versions, URLs and integrity values are locked in the app's existing
lockfile; CPU-only installation skips optional GPU binary downloads.

The GoDaddy preview source was changed to the candidate; File Manager confirmed
its runtime files under the existing app-owned server directory. The dashboard
reported candidate commit `786b7bac9d97d8cd50bf1ef5f972956092101186` during
its build. No embedded-test private directory or receipt was visible at the
last inspection. The provider then required a fresh sign-in. **GoDaddy native
load, model download, inference, final preview health and resource fit remain
NEEDS VERIFICATION.** The earlier CI worker-start failure caused by inherited
`--input-type=module` was corrected; it was not a GoDaddy denial.

## Preview-only execution

Only `KFM_EMBEDDED_AI_PROBE=1` enables the one-shot startup check. It starts after
the web server and contains failure without making map startup depend on inference.
No public diagnostic or model route is added and no user question is processed.

The private directory `/private/kfm-embedded-smollm2-20261016` is owner-only, with
an exclusive attempt marker and no automatic retries, overwrite or cleanup.
Downloads use HTTPS only, fixed publisher paths/revision, bounded redirects within
the publisher's domains, exact byte limits, incremental SHA-256 verification and
0600 files. No credentials are sent. The runtime downloads only model artifacts;
prompts are never sent to Hugging Face or an inference provider. After installation,
remote model loading is disabled and all weights are loaded from private files.

One worker, one CPU inference thread, at most 16 generated tokens and a fixed
synthetic prompt are used. Parent monitoring requests termination after 240 seconds
or when sampled process RSS exceeds 1,200 MiB. The worker's JS heap is capped at
256 MiB. **These are application safeguards, not a hard native-memory or provider
quota guarantee:** native memory can grow between samples, and termination during
a native call depends on worker/runtime behavior. Existing GoDaddy effective
RAM/CPU/private-storage quotas remain unknown. The test is preview-only.

The receipt records model identity, exact source-file hashes, observation time,
sampled peak process RSS, stage, timings and finite failure/success. It contains
only the synthetic output and no accounts, jobs, environment dumps, KFM evidence,
private location or user prompts. Read it in authenticated GoDaddy File Manager.

## Evidence, integration and release gates

`SYNTHETIC_INFERENCE_PASS` proves only that the test model response ran in that
observed environment. It is not a public chat deployment, citation-quality
acceptance, admission of data, or a released-evidence answer.

The current account-backed PC queue and UI are preserved during qualification.
Do not label this model as Qwen or fake a PC worker heartbeat. A later admitted
embedded profile must retain login, same-origin controls, sensitivity/rights
checks, released-evidence resolution, cancellation, supported-citation validation,
release rechecks, and finite ANSWER/ABSTAIN/DENY/ERROR outcomes. The existing missing
released-knowledge binding remains a separate limitation. Model language cannot
supply that missing authority.

## Placement, validation and rollback

Directory Rules v2 §§10.1/10.4 and accepted ADR-0029 support these existing
standalone app `server/`, `tests/`, `docs/`, app-manifest and CI responsibilities.
No new canonical schema, policy, evidence or release home is introduced.
This scope leaves the original Sites app and published GoDaddy source unchanged.

Local negative-path tests use injected workers and do not prove native inference.
CI native inference and actual GoDaddy inference must be reported independently.
The qualification workflow is restricted to the candidate branch with read-only
repository permissions. Its earlier dependency-resolution/model-identity step
does not imply deployment approval.

Rollback removes the preview flag and restores the prior source branch
`a0-crawler-guidance-20261015` at
`e298f023d50878fc954e2037094236b2c15ebffc`.
Retain private attempts/receipts; no data migration or destructive cleanup is needed.

Sources checked this session:
- https://huggingface.co/docs/transformers.js/tutorials/node
- https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct
- https://github.com/huggingface/transformers.js/releases/tag/4.3.1
- https://onnxruntime.ai/docs/get-started/with-javascript/node.html
- https://github.com/microsoft/onnxruntime/blob/main/js/node/script/install-utils.js

## Post-merge preview startup follow-up

The owner merged both qualification PRs (#5203 and #5202). The resulting source
`a0-crawler-guidance-20261015@5c6f287b2fbd9ecd070073c98796f04a1e3ad847`
retains both probe modules but invokes neither from `server/start.mjs`.
A separate preview candidate restores only the embedded probe behind the exact
`KFM_EMBEDDED_AI_PROBE=1` startup condition. With the flag absent, normal startup
does not import the AI probe. The previous Ollama probe remains uninvoked.
No model, dependency, access, account, evidence or published-site behavior changes.
Directory Rules basis remains the existing app-owned server/docs responsibilities
above. Rollback for this follow-up removes the flag or returns preview to this
post-merge base; preserve private receipts and attempts. Hosted inference remains
NEEDS VERIFICATION until an actual private receipt is inspected.

## Single-threaded WebAssembly follow-up

The actual private GoDaddy receipt `6e9df539-0946-482f-96e7-03f31c7b146b`
observed `LIMITED / ERR_DLOPEN_FAILED` at `NATIVE_IMPORT` at
2026-10-16T16:00:44.144Z, Node 22.23.3 linux x64, 376 ms, sampled RSS
120,946,688 bytes. No model download occurred. The exact native-loader cause is
UNKNOWN; CI success did not establish host compatibility. This supersedes the
pending native-host status above; earlier measurements remain historical CI evidence.

The current follow-up replaces the probe worker with ONNX Runtime Web's documented
Node.js single-threaded WebAssembly backend and pure JavaScript tokenization.
It imports neither Transformers.js nor onnxruntime-node. The locked versions are
`onnxruntime-web@1.31.0-dev.20260914-8d85527a0` and
`@huggingface/tokenizers@0.2.0`; existing transitive package bytes are reused.
The smaller Apache-2.0 `HuggingFaceTB/SmolLM2-135M-Instruct` model is pinned at
`12fd25f77366fa6b3b4b768ec3050bf629380bac`; its 182,068,553-byte q4 ONNX
SHA-256 is `933577110303a2964096d19b6f15d3b4639bef7f99481ac0b61d9f3ad72f392a`.
The single existing model manifest owns this candidate identity. Old identity and
native result remain in git history and the retained private attempt.

The CI-only prototype at `c8059a9acf9c2065d9b1998b496c10dfcc8b25fa`,
run 38930813663, generated `The sample marker is blue.` in 2,080 ms after a
684 ms load. Its final process RSS was 1,607,512,064 bytes, above the bounded
hosted probe's 1,200 MiB safeguard. It is not resource qualification. The bounded
follow-up streams verified downloads, loads from a file path without retaining an
extra JavaScript model copy, disables CPU memory arena, memory pattern, graph
optimization and prepacking. Its exact-head memory and inference check is pending.

The new owner-only attempt directory is
`/private/kfm-embedded-smollm2-wasm-20261016`; the native directory is retained
untouched. The same flag, fixed prompt, token limit, 240-second timeout, sampled
1,200 MiB safeguard, 256 MiB worker JS heap, no overwrite/retry and private receipt
rules apply. WebAssembly memory also lies outside the JavaScript heap limit.
No platform security settings change. Public chat and released-evidence integration
remain unimplemented. Rollback returns preview to post-merge base
`5c6f287b2fbd9ecd070073c98796f04a1e3ad847` with the preview flag removed.

Primary sources: https://github.com/microsoft/onnxruntime/blob/main/js/web/README.md
and https://github.com/huggingface/tokenizers.js/blob/main/README.md.
