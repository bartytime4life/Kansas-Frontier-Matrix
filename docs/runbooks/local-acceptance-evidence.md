<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks-local-acceptance-evidence
title: Local Acceptance and Evidence in Intake Studio
type: runbook
version: v1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-11-15
updated: 2026-11-15
policy_label: public
owning_root: docs/
responsibility: Explain the private acceptance-evidence module and its boundaries.
truth_posture: CONFIRMED targeted synthetic tests; NEEDS VERIFICATION rendered browser, full Studio integration, installed machine and independent review.
[/KFM_META_BLOCK_V2] -->

# One workspace, distinct decisions

Intake Studio already hosts Intake, Working Data and the read-only Data Library.
**Acceptance & evidence** adds software/source verification to that same local
navigation and origin. It does not merge verification with private-file intake
review or Qwen's local-use recommendation. A locally accepted file is not a
verified Explorer feature, and a passing test does not clear sensitivity.

This is a new repository implementation of a receipt-compatible local desk,
not a recovered copy of the hosted Category Acceptance Site application.
The hosted Site and its ledger remain unchanged. There is no automatic sync,
cloud upload, provider request, repository write, model call or deployment action.

## Open and import

After a separately reviewed and authorized installation of this candidate,
start Studio using its established launcher and existing configuration. Select
**Acceptance & evidence** in the sidebar. The page uses
`/api/workspace/acceptance/page` on that same exact loopback origin; it needs no
additional listener, hosted service or account.

Choose the original `KFM_5856_Acceptance_Receipt_2026-11-15.json`, then **Import
locally**. The initial adapter supports only the existing
`kfm-pr5856-continuation-evidence/v1` envelope: 59 distinct source cases, 13 distinct
download observations, full candidate revision, and matching top-level and
nested SHA-256 payload digests. Other schemas fail closed. This is a bounded
adapter, not a new canonical KFM evidence contract.

The exact original bytes are retained and can be downloaded unchanged. A second
identical import is idempotent. Each imported receipt starts **UNREVIEWED**, even
when its original report contains PASS or VERIFIED claims. Historical timestamps,
limits, holds, expected drawer labels, source plans and build comparisons remain
part of the original. The UI labels them historical, not fresh observations.

A checksum identifies bytes. It does not authenticate a signer, establish source
truth, confirm a deployed revision, or provide acceptance or release authority.
No attachments or URLs named inside the receipt are opened or fetched. The 52
external evidence files in the original archive are not silently imported or
reverified by this adapter; preserve the archive separately.

## Record, review and retest

Select a source plan and record only checks actually performed. Use distinct
lanes for repository inspection, focused tests, browser catalog/fallback,
rendered feature/drawer behavior, installed machine, deployment identity and
download/provider checks. Keep candidate, installed, deployed and public
contexts separate. Enter the original observation time with a timezone, run ID,
expected and observed results, reproduction steps, and evidence references.

PASS requires evidence and build identity. A PASS for rendered, installed or
deployment checks also requires a full revision. A rendered PASS additionally
requires target-browser details, viewport and WebGL2 availability. A fallback
observation belongs in the separate browser-catalog lane; WebGL2 unavailable is
not a successful rendered-feature test. These validations check completeness of
operator declarations, not the factual truth of the attached references.

An optional 32-character Intake file ID is a reference only: it neither reads nor
changes the file, confirms its existence, nor copies its review or clearance.

Observations are immutable. Reusing the same run ID with identical fields is
idempotent; changed content under that ID is refused. A retest appends a record
linked to a prior observation in the same receipt, source, lane and environment.
Changing the selected receipt clears unsaved forms so stale evidence cannot be
silently reassigned to a different candidate snapshot.

A review is a separate append-only record with **HOLD**, **RETEST**, or
**ACCEPT_EVIDENCE**. Only a PASS observation can receive ACCEPT_EVIDENCE. Later
review records supersede earlier review labels for that observation; the earlier
records remain visible. A new retest starts unreviewed. Names are audit
attribution under the existing local-session capability, not an independent
administrator identity or cryptographic signature.

Overall public acceptance remains **HOLD** in this first integration. The module
cannot promote a release, authorize a merge, admit a source, clear sensitivity,
update private intake review, or change the public website. It is deliberately
not a replacement for the existing governed release and policy processes.

## Storage, access and export

The additive `acceptance.sqlite3` ledger lives below Studio's private root,
separate from original-file objects, intake records, Working Data and Library.
Reading an empty evidence desk does not initialize it. Explicit imports and
appends use transactions; no update/delete routes are exposed. Existing exact
Host, same-origin and workspace-session guards remain in force. POST also
requires exact Origin, bounded JSON, no Transfer-Encoding and the existing
volume check. No permissions, exposure, CSP, CORS or session guard is weakened.

Limits: 2 MiB per receipt, 32 receipts, 1,000 local events and 16 MiB total stored
body bytes. Full stores refuse new writes rather than deleting history. Original
bytes and event-chain consistency are checked on read/export. These are
corruption checks, not protection against an owner who can rewrite the database
and recompute every hash. Back up the private ledger through the existing
approved backup procedure; do not delete or move live SQLite files casually.

**Export ledger** emits canonical UTF-8 JSON with sorted keys, preserved arrays,
all saved receipts and events, and a SHA-256 digest of its payload. Unchanged
state exports byte-identically; there is no newly generated export timestamp.
**Download unchanged original** returns the selected receipt's original bytes.
The export is portable evidence, not an automatic-import request for the hosted
Site. Ledger re-import and general receipt-schema support are not implemented.

## Validation and acceptance

Run the targeted tests from a full repository checkout:

```sh
python -m unittest discover -s tests/local_data -p test_intake_acceptance.py -v
node --check tools/local_data/intake_studio/local-web/acceptance.js
```

Preparation executed 50 synthetic unit/request-dispatch tests, JavaScript syntax,
and a smoke test against the supplied historical receipt in a disposable store.
The dispatch test isolates unrelated Desk dependencies; it is not a full Studio
server, installed-machine or rendered-browser test. No native OCR, real-model,
provider, camera, mobile or public acceptance is claimed. Run the normal
`make local-data-check` and a fresh full-Studio browser session before merge or
installation approval. Keep all failures visible.

Browser acceptance should cover navigation from every shared view, keyboard and
mobile layout, persistence after restart, import rejection/duplicate handling,
context changes, review/retest transitions, downloads, and scrolling beyond long
source tables. Confirm no external requests and no changes to Intake, Library,
Working Data or public-release state. Verify the running source fingerprint;
its existing file enumeration includes these new Python and local-web assets.

## Rollback

Before merge, close or revise the draft. After a separately approved merge,
revert this bounded code change and return to the retained prior installed
release through the normal installation procedure. Preserve `acceptance.sqlite3`,
original receipts, exported ledgers and existing intake data. Removing code must
not erase review history. No public or hosted rollback is needed because this
change does not deploy or modify those systems.
