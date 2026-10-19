# Hosted Qwen memory fit — 2026-10-19

Status: CANDIDATE. The operator uploads the derived model to the host by hand
before Preview can load it. Public chat stays off (`KFM_HOSTED_AI=0` on Publish)
until a hosted Preview run and the owner clear it.

## Why

GoDaddy Web Hosting Plus Launch allows 2 CPU cores and 4 GB of memory for the
whole hosting account
([GoDaddy resource limits](https://www.godaddy.com/help/resource-limits-12001)).
On 2026-10-19 the OS killed the Published model process during load
(`MODEL_UNAVAILABLE:MODEL_PROCESS_KILLED`). Preview loaded the same model, and
Preview and Published share that account limit.

Local measurement of the previous loader (onnxruntime-web, one WASM thread,
greedy, 200-token reply), peak process RSS:

| Prompt tokens | Previous loader | This candidate |
|---|---|---|
| After load | 2.09 GB | 1.4–1.6 GB load spike, 0.87 GB steady |
| 529 | 2.68 GB | 1.69 GB |
| 1,529 | 3.14 GB | 2.55 GB (not admissible here) |

WASM memory never shrinks, so the peak stays resident until the model process
restarts. The old limits (2,048 input + 768 reply tokens) allowed peaks above
3.5 GB.

## What changed

1. **Derived model.** `scripts/derive-hosted-qwen.py` turns the pinned upstream
   `onnx-community/Qwen3-0.6B-ONNX` INT8 file into a derived model. The tied
   output layer used
   to transpose and dequantize the whole 151,936 × 1,024 embedding table on
   every token (about 780 MB of scratch). It now reads 8 pre-transposed uint8
   vocabulary slices of the same table, with the same scale and zero point.
   Weights move to `onnx/model_int8.onnx_data`. Nothing is retrained or
   requantized. The tokenizer and configuration files are byte-identical. The
   script checks every upstream SHA-256 and its output is byte-reproducible;
   two runs produced identical files. `server/embedded-ai-model.json` pins the
   output and records the lineage.
2. **Manual installation, no download.** The app no longer fetches model files.
   The model process checks the uploaded folder: every file's size and SHA-256
   must match the manifest, and links, hard links and files owned by another
   user are refused. Files the app owns are tightened to owner-only
   permissions, because File Manager uploads arrive group- and world-readable.
   A missing upload reports `HOSTED_MODEL_NOT_INSTALLED` and creates nothing.
3. **Loader.** The worker passes the weights as external data and drops its
   file buffer once onnxruntime-web holds them. The model process runs with
   `--expose-gc` and collects after each step, so each step's key/value copies
   don't pile up. Graph optimization stays disabled: `basic` and `all` raised
   the load to 2.4 GB.
4. **Limits.** Input context goes from 2,048 to 1,024 tokens, older turns are
   trimmed first, and the expanded reply goes from 768 to 256 tokens. Brief
   stays at 160. The model-process RSS guard drops from 4 GiB to 2.5 GiB, so the
   app stops the model before the host does. The startup headroom check is
   derived from that guard.
5. **New model directory.**
   `/private/kfm-embedded-qwen3-06b-int8-sliced-wasm-20261019/model/`. The
   earlier single-file cache is retained, not overwritten. The acceptance and
   probe receipts use new directories, apart from the uploaded model.

## Verification (local PC, not hosted)

- Greedy output was identical (same SHA-256 of the reply text) between the
  previous model and the derived model at 529 and 1,529 prompt tokens.
- The real forked worker with the derived files loaded in 2.2–2.3 s, with a 1.4–1.6 GB
  load peak. A short brief question peaked at 1.40 GB. The longest admissible
  expanded discussion (2,400-byte context, two long prior turns, history
  trimmed to 1,024 tokens) completed in 87 s and peaked at 2.17 GB.
- These figures come from a 32-core PC. Hosted speed on 2 cores, the host's
  accounting of WASM memory and the quality screen still need a hosted Preview
  run.

## Operating on Plus Launch

Run the model in one place at a time. While Preview has `KFM_HOSTED_AI=1`, keep
Publish at 0, and the reverse. Two model processes plus two web servers can
exceed the account's 4 GB.

## Install

1. Run the script on the PC against the verified upstream files. Compare the
   printed sizes and SHA-256 values with `server/embedded-ai-model.json`.
2. In GoDaddy's File Manager, upload the output folder's contents to
   `/private/kfm-embedded-qwen3-06b-int8-sliced-wasm-20261019/model/`, keeping
   the `onnx/` subfolder. That is seven files, including the 772,771,840-byte
   `onnx/model_int8.onnx_data`.
3. Deploy this source to Preview and restart it. The Preview log shows
   `HOSTED_MODEL_INTEGRITY` for a partial or changed file and
   `HOSTED_MODEL_NOT_INSTALLED` for a missing one. Replace the file and restart.

## Rollback

Restore the previous source. Its manifest and cache directory are untouched, so
the earlier model loads again without a download. Set `KFM_HOSTED_AI=0` first if
the host is under memory pressure.
