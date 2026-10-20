# Public AI workflow continuation · 2026-10-17

## Investigation handoff candidate · 2026-10-18

The existing selected-source workflow now has source-rechecked copy, Markdown
and JSON investigation actions. These preserve the submitted scope and source
dates while keeping source context, generated discussion, release identities
and withholding outcomes distinct. A changed source removes old content from
the saved draft; a failed recheck saves nothing. Loaded Census counties are
also discoverable from the existing global search without changing map time.
These are local implementation results, not a deployed or fully release-backed
investigation. See [the bounded review record](investigation-handoff-20261018.md)
for the public screenshots, model-quality failure, validation, remaining browser
and release gates, placement and rollback. Historical checkpoints below retain
their original date and scope.

## Full-prefix repetition repair · 2026-10-17

Actual GoDaddy Preview at merged #5243 revision
`500a09935951b5bec7965174236c6aac33c3e933` returned unsupported Google Maps
and access-history details for a date question. Its ordinary follow-up copied
the entire preceding reply, then appended unsupported and contradictory core
date claims. The new text diluted the existing 75% phrase-overlap threshold.
Both outputs remain failed answer-quality evidence, not source facts.

The repetition check now also withholds a full leading copy of the immediately
preceding reply, normalized to case-insensitive Unicode words. The existing
24-word minimum and phrase-overlap fallback remain. A partial shared opening
with new detail remains allowed; intentional full repetition may be withheld
because the prior turn remains readable. The existing handler/UI already return
ABSTAIN and explain withholding without storing duplicate history or exposing
duplicate draft/continuation actions. No new response contract is needed.

Local validation passed 79 direct/in-process checks and two production built
Fetch-handler checks, with zero failed/skipped; production build, TypeScript,
changed-file ESLint and whitespace checks passed. Real HTTP and assigned-port
startup require exact-head CI because local TCP listeners remain restricted.
No new-head CI, deployment or live rejection outcome is claimed here.

The actual two observed outputs are replayed with a fake model through the
public handler. The regression fails on the unchanged merged source, then
passes with the repair. This qualifies the rejection behavior only. The first
unsupported answer and factual claims in otherwise novel output remain beyond
this heuristic. Production acceptance is still held; no model/file/settings,
private store, source admission, paid service or PC dependency is changed.

Existing `server/`, `tests/` and `docs/` own this bounded repair. Rollback is
application reversion and redeployment, with no migration or store reset.

## Page time and repeated follow-up repair · 2026-10-17

GoDaddy Preview at `1e5c783f5b62ade5fdbb4159682922968663a7ca`
completed an About-page date question and an ordinary follow-up, but returned
near-identical governance boilerplate instead of the requested explanation.
The page assistant displayed a map year, while the server omitted it from
unselected public-page prompts. Those prompts now retain the selected display
year and view, explicitly separate from collection/drilling dates, beside the
existing page guide. Browser-provided dates remain display context, not source
observations or evidence. No question text is parsed into source facts.

The existing phrase-overlap check now applies to ordinary same-context
follow-ups as well as the explicit Continue command. It withholds a reply when
both replies have at least 24 words and at least 75% of the current four-word
phrases occur in the immediately preceding reply. `MODEL_FOLLOWUP_REPEATED`
returns ABSTAIN, no interpretation/answer/EvidenceRefs and no duplicate history;
the existing continuation code remains compatible. New details and short
replies are outside this repetition check. Deliberate requests to repeat a long
reply can also be withheld; the visitor can read the earlier turn. This is a
repetition heuristic, not a correctness or relevance classifier.

Both regressions fail on the unchanged merged base: missing page time and an
ordinary repeated reply incorrectly emitted as UNVERIFIED_AI_DISCUSSION. The
replay fixture uses the two actual observed texts with a fake model; it does
not prove improved live generation. Keep production acceptance held pending
new exact-head hosted tests. The first generic answer can still be unhelpful;
this patch does not qualify the 360M model, replace its private files, change
budgets, admit sources, enable publication or require another service/PC.

Local verification: 78 direct/in-process checks plus two production built
Fetch-handler checks passed, with zero failed/skipped; production build,
TypeScript and changed-file ESLint passed. The existing local TCP-listener
restriction remains, so real-HTTP/startup acceptance is delegated to exact-head
CI and the existing GoDaddy Preview. No new-head CI, deployment, improved live
answer or production acceptance is claimed by these local results.

Existing `server/`, `tests/` and `docs/` retain their responsibilities under the
previously inspected Directory Rules / ADR-0029 basis. Rollback is code revert
and redeployment, preserving configuration, model files and private stores.

## Evidence and scope

CONFIRMED: PR [#5230](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5230)
was merged by the owner into `a0-hosted-ai-web-20261017` at
`04dd1309d70a47c4d16e62783780a4531deba1ee`. Its source tree is
`ed2b2675debfa125a98e81f95f6443e771eb6567`. The local checkpoint
`531707c25067dbd6670622675191ef14e1d52f7f` has exactly that tree; it is
used as the original content-equivalent review base. During this task, PR #5232
merged into the same branch at `38c938f6305ef8f4295e0e32d3412e7850a2398e`,
tree `996110703c1c57620e22560b421e41fb64fe2673`. The local integration base
`22e4adec901a808ec2f07e3821c6c671fa203498` has exactly that new tree. This
successor uses the new real remote base and preserves all #5232 changes. The map
page overlap merged cleanly; the identical HTTP assertion fix is inherited. No
previous selection or navigation implementation is recreated.

CONFIRMED: #5230's workflow run `39048042733`, job `117440644625`, failed
an old HTTP assertion expecting the former “Log in” button. The implementation
now calls it “Administrator”. Merged #5232 supplies that same assertion repair;
this successor inherits it and retains the protected-operation tests. A resolved review thread did not remove the
selected-title search-term bug from the merged source; this continuation fixes it.

NEEDS VERIFICATION: the live site's source revision. The public browser showed
the older login header; the hosting control panel required sign-in. Neither a
merge nor a successful local build proves deployment. No host change, duplicate
site, new service, paid dependency, model replacement, or capacity increase is
part of this change.

## Directory and authority basis

Directory Rules and accepted ADR-0029 were inspected before placement. This is
the existing standalone GoDaddy application, not the separate monorepo site
mirror. UI stays under existing `app/`, runtime resolution under `server/`,
checks under `tests/`, and behavior/release notes under `docs/`. Existing workflow
integration stays in `.github/workflows/`. There is no parallel contract, policy,
source, registry, evidence, or release store. Synced project `sources/` are untouched.

## Visitor behavior

- The map passes its visible layer IDs, frame, evidence/time filters and optional
  comparison. Existing selected-feature, Evidence Drawer and Underground
  sample/interval handoffs are retained.
- Existing public page routes receive a small contextual assistant. Private
  stewardship/operation routes and unknown routes do not. Known compatibility
  redirects remain intact. The page sends a code-defined surface ID; only the
  Knowledge record route may also send its validated record ID. It does not read
  page text, upload contents, credentials, arbitrary URL parameters or form fields.
- Reports and stories can ask about their captured map context. Private draft
  text is not sent. Browser-location-redacted snapshots omit layer/filter/compare
  context as well as coordinates. Generated discussion can be copied into an
  explicitly unpublished draft outline with source and review placeholders.
- Static interface guides and useful question suggestions remain available when
  the model is unavailable. The small model's output stays visibly unverified.
- Accepted questions appear before slow source resolution. A failed status read
  retries the same job; manual Retry status never sends another question.
  Cancellation works while resolution is pending. Unsubmitted drafts survive
  recoverable connection failures. Completed questions offer Edit and retry.
- Source links come from the server resolver, separately from generated text.
  Released records and external KGS context have distinct labels. Visitors can
  recheck sources before reusing an earlier reply. Modal help uses native dialog
  focus containment/Escape behavior, restores opener focus, and fits narrow screens.

## Trust boundaries

Browser context is a closed, bounded selector contract. Layer titles come from
existing server-known registries. Selected Knowledge records use the existing
governed reader and its response validator, with no local-file fallback. A missing
release binding still fails closed. Selected Underground context uses the public
manifest, tile hashes and exact record/interval lookup from #5230. Coordinates are
not sent to the model. Only HTTPS KGS source links are emitted for KGS context;
released-record links remain on the canonical Knowledge route.

Released record and linked external source context are resolved again before
inference and on every result read. Changed or unavailable sources permanently withhold that job's prior
interpretation. History is isolated by visitor, complete selector and resolved
source fingerprint. Source content remains data, never privileged instructions;
the model has no tools, admin credentials, publication action or authority to
create citations. Existing origin checks, anonymous cookies, sensitivity/output
checks, rate/queue limits and separate administrator APIs remain in force.

## Validation and practical limits

Local validation: 121 direct tests passed, zero failed/skipped, covering existing
AI/context/model/resource/account boundaries, the new workflows and the overlapping
#5232 navigation/science/terrain regressions. One additional
production Fetch-handler test passed: anonymous status, disabled-host fail-closed
POST, server rendering of public help and the existing downloads redirect.
The concurrent-read release-withdrawal regression found during independent review
is also covered: an older in-flight read cannot resurrect a withheld interpretation.
Production build and TypeScript passed. Focused ESLint had zero errors and one
pre-existing report-image warning. CI includes the new context, sitewide and
compiled-route tests plus existing real HTTP/account tests.

This workspace cannot bind a TCP listener (`EPERM`); the real HTTP suite could
not run locally. The compiled handler test exercises production routing without
a socket, but does not replace CI's Node HTTP tests or a browser acceptance run
against the actual deployed host. Exact-head CI and the independent security
review are reported in the PR, not inferred from these notes.

The model remains the existing SmolLM2-360M q4 single worker with its existing
512-token prompt and bounded reply/deadline/resource settings. No factual-answer
qualification is claimed. Evidence search can return inspected released-record
links without inference; a missing governed release reader means no such records.
Broad document reasoning, exhaustive comparisons and long reports exceed this
small slice. Reports/stories receive map context, not private manuscript text.
Page help recognizes its route, not every field on the page. External source
context does not become admitted KFM evidence. Live mobile, keyboard/screen-reader,
memory/concurrency and model-quality acceptance remain required on the host.

## Deployment and rollback

1. Review the successor PR against the exact remote base/head recorded there;
   rerun changed-area tests if either revision advances. Confirm no overlap with
   another open change and require independent approval. Merge and publication
   remain separate authorized operations.
2. For subsequent operations, use replacement GoDaddy Node app `urdng3v1vk`
   (recorded 2026-10-19); the deleted `q9r9beo47t` app is historical only.
   Reverify the app and deployed source using
   [current hosting documentation](godaddy-node-preview.md). Preserve current
   environment, public data, model files, private stores and startup/port configuration.
   Use its established deployment process and the approved commit. Do not create
   another Sites application, point public AI at a PC, or invent a release binding.
3. Before admitting public traffic, verify the deployed source revision, origin,
   anonymous readiness, administrator denial, model/resource limits and governed
   evidence availability. Run a selected map feature, KGS interval, Knowledge
   record, report/story handoff, selection switch/follow-up, cancellation, status
   retry, source withdrawal/recheck and cross-visitor denial through the actual UI.
   Check source labels, limitations, keyboard focus and mobile layout. Any failed
   release/policy/integrity requirement keeps the deployment unaccepted.
4. Roll back by redeploying the previously accepted application artifact/revision
   through that same host process. `04dd1309d70a47c4d16e62783780a4531deba1ee`
   is the prior selection source; the current source base is
   `38c938f6305ef8f4295e0e32d3412e7850a2398e`. Neither identifies the last
   accepted live artifact. Restore no stores:
   this change has no migrations. Keep existing public-AI enablement/origin controls
   as the operational fail-closed switch; retain the audit record and retest public
   pages, anonymous status and protected operations after rollback.

Prepared source and review evidence do not mean merged, deployed or published.

## Catalog context recheck correction · 2026-10-17

Acceptance review against standalone branch base
`d54eda47df212496da88a7e97f82e1ad74831732` reproduced a gap: a server-resolved
catalog selection without a release ID, source-summary field or source link
skipped the freshness check. Correcting or denying that record could leave its
earlier generated discussion visible. All resolved contexts now undergo the
same bounded resolver/fingerprint check before inference and on result reads.
A failed check permanently withholds that job's interpretation. No model,
resource limit, identity, data store or publication authority changes.

The regression uses the actual catalog context resolver. It checks an updated
record after completion, monotonic withholding after the record is restored,
and denial between resolution and inference without calling the model. It
failed on the unchanged base with `UNVERIFIED_AI_DISCUSSION` instead of
`RELEASE_CHANGED`, then passed with the correction. Placement stays in existing
`server/`, `tests/` and `docs/` responsibilities under Directory Rules and
accepted ADR-0029; no new root or parallel evidence home is created. Rollback
is a reviewed revert and application redeployment; no store restoration or
migration is required.
