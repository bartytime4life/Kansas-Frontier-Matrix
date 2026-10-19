<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/production-startup-audit-20261019
title: GoDaddy source, production startup and composer timing repair
type: verification-record
version: v4
status: source repair; hosted diagnosis and publication pending
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-19
policy_label: public
owning_root: docs/
responsibility: Record source identity, startup diagnostics, standalone Node verification and first-open composer timing repair
truth_posture: CONFIRMED reproduced identity defect; live 503 root cause UNKNOWN
[/KFM_META_BLOCK_V2] -->

# Production startup and source identity audit

The owner requested an audit of the GitHub application files after the public
GoDaddy application continued returning Service Unavailable. The audit starts
from `a0-hosted-ai-web-20261017@0ad31b2c993e6d6973b678192f689650ab66e8da`.
Its files are identical to deployed candidate
`dd81892ee5ad5fcd0d09f5bbc88562226405e7b7`; the former is the merge commit of
PR #5290. Work uses an isolated checkout and preserves unrelated work.

## Confirmed source identity defects

`applicationIdentity()` previously treated a clean `git status` as proof that
every hashed application input belonged to `HEAD`. A Git-ignored file under an
application root can change the source digest while leaving Git status clean.
The regression creates an ignored `app/leftover-runtime.mjs` after committing
its fixture and reproduces the incorrect non-null commit on the unchanged code.

Git's `assume-unchanged` and `skip-worktree` flags can also hide changed or deleted
tracked files from status. Regression fixtures reproduced a non-null commit for
those mismatched bytes. Finally, the full test suite generated Python bytecode
under `scripts/__pycache__/`, which changed the application digest despite no
application source change.

The repair compares every included file's observed bytes with the immutable
commit's Git blobs, including checks for missing committed inputs. It withholds
`sourceCommit` and reports `UNTRACKED_APPLICATION_INPUTS` for extra application
files or `WORKTREE_MODIFIED` for changed/deleted inputs. It explicitly excludes
generated `__pycache__` directories, while retaining ignored application source
in the digest. Existing generated-asset exclusions and archive-build behavior
remain. These states describe identity limitations, not data-release decisions.

The healthy hosted preview reported 782 inputs and digest
`sha256:57541ff2d06c1c67eff1eecdbfac7434074681bf909d74bfed73507595415540`.
The initial sparse Git checkout reported 773 inputs and digest
`sha256:1289932684fdc2a05699729922707dd0cb1ffb6cc07dadd82466865614222d0c`.
The final clean-commit check identified nine committed `drizzle/` migration and
metadata files excluded by that checkout's sparse configuration. Hashing the
complete immutable `dd81892` tree exactly reproduces the hosted preview's digest
and count; omitting those nine files exactly reproduces the initial local
values. This discrepancy is **resolved** and is not evidence of a hosting-file
defect. The complete isolated checkout was restored before final validation.
The new identity check correctly withholds commit identity for an incomplete
sparse checkout, even when Git status is clean.

## Startup verification gap and repair

The existing Vinext listening message proves a socket bind. It does not prove
that the built application answers HTTP or remains reachable through the public
gateway. The existing CI started its Node HTTP server without explicitly setting
the `NODE_ENV=production` value used by GoDaddy's published serve command.

Startup now makes one bounded, direct loopback GET to the existing public
`/api/build` route on the actual bound port. The private stdout line prefixed
`KFM_NODE_STARTUP` reports the runtime, production-mode flag, port, HTTP outcome
and validated public build digest/count. It does not log response text, request
headers, secrets, accounts or private-store contents. It does not load the model,
contact an external provider, add a public endpoint, follow redirects or change
authorization. The read has a five-second deadline, a 4 KiB body limit and a
16 KiB response-header limit. Failure is diagnostic and does not replace the
application's existing error or access-control behavior.

CI now uses Node.js 22.23.3, checks out the exact pull-request head, sets
production mode explicitly and verifies the actual process's startup
report after its existing HTTP and hydrated browser checks. Network tests cover
the assigned port, valid identity, HTTP errors/redirects, placeholders, malformed
or wrong-application identities, oversized/stalled bodies and a non-listening
server. No model download or inference is part of this check.

## Standalone test compatibility

The first complete Node run reported 1,479 tests: 1,404 passed, 72 failed and
three skipped. This initial run used the incomplete sparse checkout described
above. Failures included outdated Worker-style calls to the Node build,
an HTTP harness requiring an undocumented external listener, stale assertions
for retired PC controls, missing local migration files, and integrations whose
Cloudflare runtime or separate Python source prerequisites are not shipped in
this composition. Committed D1 migrations are present in the complete source
and their SQL tests must execute.

Node rendering tests now call the production build's Fetch handler. HTTP tests
start and clean up an ephemeral production listener when no external test origin
is provided; CI separately exercises the real `server/start.mjs` process.
Component tests verify the current hosted controls and preserve provider
provenance, invalid-input checks, network denial, accessibility and private
operation boundaries.

Only tests needing absent platform prerequisites are explicitly skipped, with
the missing package, platform build configuration or separate source checkout
named in the test output. Portable checks and committed-migration SQL tests
still execute. Missing committed source and unexpected import,
configuration, permission and runtime errors fail normally. An explicitly
configured incomplete Python checkout also fails rather than skipping. These
skips do not establish Cloudflare, D1 or Python parity qualification. Both
`npm test` and CI run all `tests/*.test.mjs` with concurrency bounded to four.

The Underground load-boundary test now follows the current manifest's actual
dynamic import. Immutable older browser assets are deliberately retained for
open tabs, so counting every matching filename incorrectly failed after a
second build. The test still requires one current optional module, excludes all
Underground implementation chunks from initial dependencies, and rejects static
imports, comments or filename strings as substitutes for the dynamic import.

## Verification record

Before the repair, the unchanged application passed the production build and
TypeScript check. On Node.js 22.23.3 with `NODE_ENV=production` and `PORT=20011`,
all 16 actual Node HTTP tests passed. Initially launching server and client in
separate execution environments caused connection refusals; running both in one
environment resolved that harness issue. Those failures are not attributed to
the application or reported as passes.

The identity regressions failed before their repairs and pass afterward. On
Node.js 22.23.3, the initial integrated candidate passed the production build,
TypeScript and changed-file lint. Its 1,512-test run reported 1,475 passed,
zero failed and 37 skipped. That result is **superseded** because the sparse
checkout incorrectly made committed migration tests appear unavailable.
The final complete-checkout run passed the production build, TypeScript,
changed-file lint (zero errors, two existing unused-variable warnings), and
`git diff --check`. It completed **1,512 tests: 1,492 passed, zero failed and
20 skipped**. All 17 previously unavailable SQLite migration tests execute and
pass. Remaining skips are 15 Worker integrations, two separate Python parity
checks, one unconfigured MySQL integration and two installer checks that refuse
root execution. Corrected independent review found no blocking issue and
confirmed missing application source cannot be silently skipped.

All 18 actual Node HTTP checks passed against a separate production process.
They include apex, provider-host and forwarded-host
requests for both `/` and `/api/build`, fixed www redirects, browser asset bytes
and retained private-operation denials. A real production process bound to port
20011 also emitted a successful bounded loopback build check. That outcome is
named `LOOPBACK_BUILD_READY`; it does not establish public gateway availability.

The local hydrated browser attempt could not launch Chrome: this workspace has
no `google-chrome` executable, and the existing pipe harness reported `EPIPE`.
That attempt did not reach application acceptance. Browser checks remain in CI;
no local browser pass is claimed.

GitHub run `39205323761` checked out immutable candidate
`a1a0c4a7b51a8372acc846ee9aa9d518ac329554`. Build, TypeScript, the complete
suite (1,494 passed, 18 skipped), and all 18 actual Node HTTP checks passed.
Both mobile county-browser sizes passed. The desktop first-open scenario failed
because the initial typed query remained blank; the remaining desktop scenarios
passed. The preview-command step did not run after that failure. This run is
**not a complete CI pass**.

Inspection identified two timing defects: a passive effect applies an incoming
draft after the composer becomes interactable, and the panel's deferred Close
button focus competes with the composer's focus. Both were reproduced with
regressions that failed on the prior source: early input became blank and the
focus sequence was composer then Close. The repair applies the requested draft
in a bounded layout effect and gives the opening action one focus destination.
Other chat launchers retain Close focus and their return target. Duplicate draft
requests cannot replace later visitor edits.

The two new regressions and 34 focused tests pass. Shared-harness compatibility
passed 255 tests with one existing conditional skip, and independent review
found no blocking issue. Changed-file ESLint has zero errors (41 warnings in the
large existing page component). The follow-up production build and TypeScript
check pass. Its complete suite passes **1,515 tests: 1,495 passed, zero failed
and 20 conditional skips**, including the repeated-build import boundary.
The exact cause of the observed browser failure is not inferred solely from its
timeout. The unchanged browser test must pass on the follow-up immutable head
before browser qualification.

GitHub run `39206904899` then verified exact follow-up head
`6f554d80ce04619d50f661b69bff1d9dc8394bc6`: production build and TypeScript
passed; the full suite passed 1,497 tests with 18 conditional skips and no
failures. All 18 real production HTTP checks, all 15 unchanged hydrated county
browser checks across desktop and both mobile sizes, the startup-report
assertions, and both assigned-port preview checks passed. This qualifies that
candidate's browser behavior, not the live GoDaddy gateway.

During that run, separate navigation PR #5301 merged as
`33d4f335cd97911f758ed25cad39dff65e873304`. The integration preserves its welcome
and URL/history restoration changes and its additional hydrated browser suite.
Independent read-only overlap review found separate page hunks and no concrete
behavior conflict. The combined immutable head must pass both browser suites
before deployment qualification. Historical receipts remain unchanged; a new
integration receipt records the combined artifact bytes.

Hosted diagnostic readback and public browser/3D acceptance remain pending.
No inference/model qualification
is claimed. This verification record stays in `docs/`; the final artifact hashes
and generation record use the existing `data/receipts/generated/` home.

## Scope, placement and rollback

Existing `app/`, `server/`, `scripts/`, `tests/`, `.github/workflows/`, `docs/` and
`data/receipts/generated/` own the
change under the inspected Directory Rules v2, accepted ADR-0029 and this
composition's `AGENTS.md` and preservation record. There is no new responsibility
root, data authority, source registry or release mechanism. The original Sites
application and separate Staging source are outside this repair.

No database, model, account, domain, secret or data migration is required.
Rollback reverts this bounded source change and redeploys the prior application;
private storage must not be restored or reset as an incidental part of rollback.

The live 503 is **not repaired or explained by these source checks**. Hosted
preview acceptance, the new startup report, actual published build parity and
public browser readback remain separate requirements. Do not change the assigned
port or claim a proxy defect without runtime evidence.
