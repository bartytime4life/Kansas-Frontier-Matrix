# KFM AI usefulness review — 2026-10-17 UTC

Status: evidence-backed assessment and locally validated change, prepared for
an owner-requested draft PR. No live deployment, model activation, data admission
or independent approval.

The largest opportunity is to make KFM an assistant for real map tasks: find
the right released records, explain their limits, compare places and dates,
and turn an answer into an inspectable map or report. Model capacity matters,
but the current evidence and map-context connections are equally important.

## Evidence and scope

- Monorepo main was pinned at `eff57a91471dc37911e1c83b89692d4f34dacf4a`.
- This change uses the separate GoDaddy application composition at
  `e3c8175884c844fbd917155b24424de69dddb507`, branch
  `a0-hosted-ai-smollm2-360m-q4-20261016`. It is not based on the monorepo root
  application layout. No open PR was returned in the initial repository listing.
- The public page at <https://kansasfrontiermatrix.com/> was inspected in a
  logged-out cloud browser. Its exact deployed source SHA was not established.
- The original Explorer Sites project returned NOT_FOUND in this session;
  the current listing showed the separate restricted KFM staging project.
  Neither result proves the original application's data was removed.
- No PC model, private host account, private release store or model weights
  were accessed or changed. No actual inference was run for this review.

## Product flow observed

| Step | Observed state | Health and implication |
| --- | --- | --- |
| 1. Open Ask Qwen on the public map | The panel says “OLLAMA · YOUR PC”, “PC offline”, and asks for login; the message field and Send are disabled. | Blocked for this logged-out visitor. The screen does not independently prove the owner's PC status. The hosted guest implementation inspected below is a different source state. |
| 2. Expand Evidence search filters | Search terms, place, From and Through are available, with a note that dates exclude undated records; sending remains disabled. | Filters are discoverable, but cannot complete a search from this state. Separate evidence availability from model/account readiness. |

Screenshots were captured for both steps during this run. They are audit
evidence, not evidence that the changed branch has been deployed. This browser
reported WebGL2 unavailable, so map rendering and feature selection were not
tested. Authentication blocked real chat testing. Semantic labels were visible;
keyboard, screen-reader, contrast and mobile acceptance were not established.

## Confirmed code findings and ranked improvements

| Priority | Finding | Proposed improvement and proof of usefulness |
| --- | --- | --- |
| 1 | The Node AI resolver delegates to `kansasKnowledgeRead`, whose production adapter expects D1/R2 bindings. Existing application notes explicitly report no released-knowledge binding for the Node composition. Current deployed store state was not inspected. | Implement a Node-compatible reader for the existing release contract, then qualify a small rights-cleared public release. Prove missing/held/withdrawn/tampered records abstain, valid records are retrievable, and every displayed claim resolves to its release. Acquisition alone must not enable answers. |
| 2 | Hosted discussion receives question, style, depth and up to two previous turns. The map passes only a selected feature title as a place-filter default; current view, time, selected layers and selection evidence are not supplied to discussion. | Add a bounded map context envelope. Use browser state only as a request for server-resolved evidence, redact sensitive precision, and show which place/time/layers the assistant used. Test that changing scope changes retrieval and prevents old-context answers. |
| 3 | Default search uses the first 120 UTF-8 bytes of the question as a literal substring. The governed reader searches title/summary and limits rows before the AI resolver applies place/date filters. | Extract bounded search terms, rank exact identifiers and named places, and apply place/date eligibility before truncation. Keep release validation unchanged. Measure retrieval separately from generation using known matches, plural/synonym variants, no-match cases and matches beyond the first page. |
| 4 | The inspected hosted branch selects SmolLM2-360M-Instruct q4. Its notes record a four-task hosted discussion screen, while factual selection stays held. Input is limited to 512 tokens and history to two turns. | Compare candidate models on representative KFM tasks before changing model or context/resource limits. Score citation correctness, unsupported claims, abstention, follow-up scope, latency and peak memory independently. A completed generation is not factual acceptance. |
| 5 | The assistant presents a general message box and generic Explore/Evidence choices. | Add task starters such as “Explain this layer”, “Compare these dates”, “Find records for this county” and “Prepare a cited report”. Offer map changes as explicit previews using existing controls, with source/date/units/limitations and working Evidence Drawer links. |

The model author's [limitations](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct#limitations)
also describe factual and reasoning reliability limits. That supports evaluating
the exact application tasks; it does not select a replacement model or prove
the quality of KFM's particular runtime.

## Bounded improvement implemented in this branch

Find evidence no longer waits for model readiness or another guest's generation.
The UI exposes search availability separately, retains the user's draft across
mode changes, and labels the search action and pending state appropriately.

Only governed, rechecked source links can be returned. The result remains
ABSTAIN, with no generated answer or authoritative EvidenceRefs. The existing
origin, guest ownership, sensitivity, rate/queue, expiry, citation-link and
withdrawal checks remain in force. Search capability is not a claim that a
released corpus is present. The missing Node knowledge binding remains open.

Affected existing files: `server/public-ai-handler.mjs`,
`app/assistant/workspace.tsx`, `tests/public-ai.test.mjs`,
`tests/assistant-status.test.mjs`, and `docs/public-hosted-ai.md`.
This review is the only new file.

Placement basis: accepted ADR-0029 and Directory Rules v2 responsibility
routing, plus this application's existing AGENTS.md and documented standalone
layout. Runtime behavior stays in its existing server/UI files, regression
checks in existing tests, and human explanation in docs. No new repository
root, canonical schema, policy, source registry or release authority is created.

## Validation and remaining acceptance

Before the correction, new tests reproduced both failures: MODEL_UNAVAILABLE
for released evidence while the model was offline, and an evidence job stuck
behind a different guest's discussion. After the correction, 43 focused local
tests passed. The final copy-only edit passed all 18 directly affected tests.
Local environment: Node 24.19.0; component harness: TypeScript 5.9.3.

```sh
node --test tests/assistant-status.test.mjs tests/public-ai.test.mjs \
  tests/hosted-ai.test.mjs tests/hosted-ai-acceptance.test.mjs \
  tests/pc-ai.test.mjs tests/pc-ai-login-admission.test.mjs
git diff --check
```

New coverage includes offline-model search; concurrent discussion; missing,
sensitive and malformed evidence; release changes before completion and on
later reads; cancellation/expiry during recheck; UI mode switching and draft
retention; and fail-closed behavior when the capability is absent or disabled.
Tests use synthetic evidence and mocked inference. No test establishes actual
released data availability or model answer quality.

Full production build, target Node 22 replay, changed-UI browser acceptance,
hosted resource measurements and independent review are NOT_RUN. The public
UI inspection describes the existing site, not this implementation's rendering.

Recommended next acceptance packet: ten answerable release-backed questions,
five missing/stale/withdrawn-evidence cases, five map/time/selection changes,
five ordinary follow-ups and five sensitivity/injection cases. Expected sources
and outcomes must be fixed before evaluating any candidate model. Report each
failure class; do not hide an unsafe answer behind an aggregate score.

## Delivery and rollback

Initial delivery stopped at `VALIDATED_BRANCH_ONLY` under the current
[repository incident](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024).
The owner subsequently requested “Make the PRs”, authorizing submission of this
prepared change and review as a draft PR. The target is the standalone GoDaddy
source branch `a0-hosted-ai-smollm2-360m-q4-20261016` at the base pinned above.
This task-specific request does not establish incident closure, effective
platform enforcement, independent approval, or permission to merge or deploy.
No host flags or data-admission state are changed.
Revert the implementation commit to restore the prior evidence/model coupling; no
persistent data or migration is involved. Keep the original Sites and GoDaddy
source histories distinct and verify the exact target before a future rollout.
