# Hosted Qwen reply and dependency follow-up

Status: private test candidate; **PUBLICATION HOLD**. General factual quality
remains LIMITED. This change does not qualify AI as evidence.

## Identity and preservation

PR #5260 merged as `4f7bc5ac6045c797592ebaa97347398e06a11083` on
`a0-hosted-ai-web-20261017`; its tree equals reviewed head `a658be3`.
This follow-up starts at that merge in an isolated working copy. It does not
merge a PR or replace the installed PC site, model, local API capsule or stores.
The Qwen manifest/weights, AI SQLite store and account/session handlers, PC
contract, source geometry and native values are unchanged. No schema migration,
reseed, account/access change or model-training operation is included.

Directory Rules/ADR-0029 responsibility placement: `server/` owns inference and
prompt handling; `tests/` owns regressions; the existing `vendor/` precedent owns
the bounded dependency patch; `docs/` owns this behavior/rollback record.
Private QA outputs and existing recovery bundles remain outside Git and public
assets. The active preview and Published identities must be read separately.

## Reply behavior

The input ceiling increases from 512 to 2,048 tokens and the expanded answer
budget from 384 to 768 tokens. The 240-second expanded generation deadline,
255-second parent deadline, 4-GiB sampled process ceiling, single worker/thread,
queue admission, cancellation, 4,096-byte cumulative answer limit and output
privacy/repetition checks remain. These are finite budgets, not a promise that
every question completes. Whole original questions and partial replies are
preserved; only older turns may be omitted, with disclosure.

Prompt prefill now runs in 64-token chunks, preserving every token, attention
mask, position and KV-cache update. Only the final prompt chunk can sample a
reply token. This bounds the all-token logits allocation per prefill; it is not
a measured GPU/FPS or host-latency improvement. All owned tensors are disposed
on completion, cancellation, deadline or error.

The server-owned `context-aware-v2` profile retains Qwen's non-thinking template,
temperature 0.7, top-p 0.8 and top-k 20, with a modest 0.5 presence penalty on
generated/continued answer tokens. It makes map context optional background
and explicitly distinguishes missing data, display dates and animation speed
from observations. Browser input cannot change those settings. Acceptance
receipts use a new v2 directory; older receipts and failed experiments remain
historical. No legacy model fallback is added.

## Verification and limitations

The same local three-question comparison reproduced a baseline long reply that
repeated text, ended early and could not continue (`MODEL_CONTEXT_LIMIT`). The
new expanded reply reached an end without the repeated-phrase trigger. A
separate real brief reply was token-limited, then continued to completion with
no copied/repeated fragment (791 cumulative UTF-8 bytes). Its continuation input
was 411 tokens; the larger 2,048-token boundary has separate deterministic cache
and allocation tests, not a claim that this small case exercised that ceiling.

**Quality screen remains LIMITED:** the model still failed requested sentence
counts and produced misleading scale/date explanations in a longer guide.
The first 1.5-penalty prompt and a slower thinking-mode experiment were not
adopted. The refined profile is a private candidate, not accepted general
accuracy. Generated discussion stays visibly unverified; factual selection
remains HELD_UNQUALIFIED. Deterministic source summaries and source rechecks
remain independent of model language. No generated answer changes source data.

Local validation: 108 focused assertions passed, including actual ephemeral
HTTP boundaries, account isolation, queue/cancellation, source withdrawal,
continuation joins, prompt escaping, tensor cleanup and Braces regressions.
Build, TypeScript and changed-area lint passed. Initial sandboxed HTTP tests
were denied loopback listeners; the authorized isolated replay passed. Peak RSS
observations around 2.8 GiB occurred during local synthetic runs with other
work; they are neither a controlled speed benchmark nor hosted capacity proof.
Exact-head CI and Chrome preview observations are recorded separately.

## Dependency repair

See [the Braces patch record](../vendor/braces-kfm.README.md). The original stack
exhaustion was reproduced. Independent investigation covered both dependency
chains, all AST walkers and parent cycles. Independent patch review identified
an additional nested-array AST bypass; the final patch also bounds append and
flatten and rejects malformed non-string AST values before coercion. Six
focused regressions pass after a fresh pinned install, including ordinary glob
compatibility. No public KFM request path to Braces was established.

The registry still reports eight high affected-package entries from the one
unpatched upstream advisory. The local mitigation does not suppress that
result, disguise the version or grant risk acceptance. Review of these patched
bytes is separate from an upstream advisory fix or full-tree security scan.

## Rollback and open gates

Revert the follow-up source commit and restore the previous verified private
preview package if necessary. Preserve `/private/` account/job data, model
caches, current secrets and all historical receipts. Reverting the Braces
override reintroduces upstream vulnerable bytes and needs risk review.
Public deployment remains `4b3cc837e9c131e5eb214427e0a55646fc76e52a` at the
pre-update dashboard read; no publication is authorized. Merge, broader model
quality acceptance, governed-data activation and public publication remain
separate decisions.
