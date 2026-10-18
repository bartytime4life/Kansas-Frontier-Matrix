# Hosted Qwen preview candidate — 2026-10-18

Status: PRIVATE PREVIEW CANDIDATE. Public publication remains ON HOLD.

## Identity and scope

Base: `115c3d246bb861a939a1d1f56f891d04bbb057c3` on the GoDaddy Node
composition. This implements the owner-requested replacement of the active
SmolLM2 model with pinned `onnx-community/Qwen3-0.6B-ONNX` INT8, revision
`58ca03a5e7b354b480b1a82b34bde8dc7b854cc0`. The manifest records the Apache-2.0
license, upstream identity, exact file sizes and SHA-256 digests. The ONNX file
is 617,687,478 bytes. This small hosted Qwen is distinct from the larger PC model.
No model weights or training changes are part of the application commit.

Ownership: existing standalone `server/`, `app/`, `tests/`, and `docs/` roots
retain their responsibilities. The fixed `/private/` model cache is runtime
material, not a new catalog, release, or source-of-truth root. Directory Rules
responsibility boundaries and ADR-0029 remain in force.

## Operation and preservation

The existing hosted-AI flag and origin guard still control the model. One
worker lazily prepares the pinned model in a separate private Qwen cache. HTTPS
redirects are provider-restricted, downloads have time/size bounds, files use
exclusive creation, and every model file is rehashed before execution. Existing
and interrupted attempts are retained rather than overwritten. The legacy
startup probe cannot run concurrently with enabled chat. A partial download
requires operator inspection; it is not automatically erased or retried.

The artificial process-RSS ceiling rises from 2 GiB to 4 GiB for controlled
preview testing. The 256 MiB worker JavaScript heap, one WASM thread, bounded
load/inference deadlines, cancellation, queue limits and output checks remain.
The worker refuses startup when reported available memory is below 3 GiB or a
reported process constraint is below 4.5 GiB. Unknown host limits do not establish
sufficient capacity. This does not change the hosting plan or OS protections.
Direct-buffer loading avoids an additional model-buffer copy.

Qwen non-thinking chat formatting and publisher sampling settings replace the
SmolLM2-specific layout and sampling penalty. Truncated or repeated answers stay
partial or withheld; larger limits do not guarantee complete or correct replies.
Factual model selection remains HELD_UNQUALIFIED. Source summaries and released
record discovery remain server-resolved and rechecked independently of inference.

Account/session/job store code, the AI database, PC worker, knowledge data,
map geometry, numeric values and dependency lock are unchanged. Historical
receipts and old private model files remain recoverable; they are not fallback
models. Neither production stores nor installed PC services are migrated.

## Local verification and limits

Build and TypeScript pass. The focused checks pass: 62 assertions across seven
AI/assistant test files, six probe checks and one built HTTP route check (69
total). The HTTP test verifies
origin denial and 404 responses for private Qwen weights, old model weights and
the AI account database. Changed-area lint has zero errors and 40 existing
warnings in the retained application files. These results are distinct from
exact-head CI and hosted browser acceptance.

Isolated actual Qwen loads and three expanded discussions completed with sampled
peak process RSS of 2,749,685,760 bytes. Example response times were roughly
10–55 seconds on the PC during other verification work; they are not a hosted
latency benchmark. The fixed four-task instruction-following quality screen
remains LIMITED. A missing-water example also failed to explain the requested
missing-versus-zero distinction well. A separate thinking-mode experiment was
slower and still failed one instruction; it is not used by this candidate.
No general accuracy or full-answer qualification is claimed.

Hosted preview/browser/CI results must be recorded separately after deployment.
The prior observed preview was `c139713f59a8475e6154a4fb293977bbc86283b9`;
Published was `4b3cc837e9c131e5eb214427e0a55646fc76e52a`. Those are checkpoints,
not proof that this candidate is deployed.

## Rollback

Restore the previously verified preview commit/package if loading or browser
checks fail. Do not publish, alter stores, restore data receipts, or delete the
new/old private caches as part of rollback. Keep existing account/database files
and immutable source evidence intact. The owner must separately authorize a
future public publication or new PR merge.
