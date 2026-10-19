<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://report/site-route-safeguards-20261019
title: Site route safeguards — tested replay and source-access hold
type: report
version: v1.0
status: draft; current-source application blocked
owners: ["@bartytime4life"]
created: 2026-10-19
updated: 2026-10-19
policy_label: public
owning_root: docs/
responsibility: Record a bounded standalone-source patch proposal, its verification, and the source-access hold without changing the governed mirror.
truth_posture: CONFIRMED replay evidence; UNKNOWN current standalone source; PROPOSED application
[/KFM_META_BLOCK_V2] -->

# Site route safeguards — source-access hold

This contribution prepares a tested standalone patch for the safeguards reverted
by #5314. **It does not apply them to the current authoritative Site.** Both
`get_site` and `create_source_repository_write_credential` returned `NOT_FOUND`
for preserved project `appgprj_6aa0b1c41bc08191bfd86003920f1631` on 2026-10-19.
The owner Sites inventory omitted that project. This establishes an access
failure, not deletion or its cause. Public Staging and the GoDaddy branch are
separate applications and have not been substituted for it.

## Exact evidence and status

| Evidence | Status and bounded conclusion |
|---|---|
| Repository `main@2b3f15870fbb63a99b4f7847be7de03d06bd92e8` | CONFIRMED initial remote base |
| [#5313](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5313), head `ac56ce03392f5ddbff587d8fdb5bac152143c054` | CONFIRMED original seven application edits and three test edits |
| [#5314](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5314), head `81812cd80d5d6b491a96c3f278a8399b1e9c6656` | CONFIRMED reversion and outstanding standalone work |
| Mirror tree `cacb6aa737c49ee30e0603d4ba81bfbf2e1fd4c7` | CONFIRMED identical at remote base and cached repository snapshot `326452d14ed52438cc98fd51966d6c894e16bac8` |
| [Existing mirror receipt](../../data/receipts/generated/site-v268-focus-mode-test-reconciliation-20261018.json) | Records Site v268 source `358280aee889e2e2cf832bd598155ca21653c8de`; seven application preimages and two existing test preimages are recorded as identical to that source |
| Current authoritative standalone revision | UNKNOWN; source access failed before a checkout could be opened |
| Proposed patch | CONFIRMED local replay/build/typecheck; PROPOSED for current-source application |

The last recorded source lacks all seven application safeguards. Their absence
from the **current** source remains NEEDS VERIFICATION. The replay baseline is
the public mirror snapshot, including its recorded overlays, not an invented
current standalone checkout or a replacement authority.

## Review packet

- [Standalone patch](../../apps/site/evidence/route-safeguards-20261019/standalone.patch)
- [Preimage/postimage hashes and verification](../../apps/site/evidence/route-safeguards-20261019/verification.json)

Patch paths are relative to the standalone source root. Never apply this patch
under `apps/site/source` to repair mirror parity. The packet is a review carrier,
not a second deployable source, registry, receipt authority, or release proof.

| Proposed change | Intended behavior |
|---|---|
| Daily archive POST | Malformed JSON and non-object owner input return 400; existing 413 size and authentication behavior remain |
| Historical overlay/review POST | Client JSON parsing returns 400 for malformed/non-object/invalid UTF-8 input; corrupt stored metadata still returns 503 |
| USGS historical catalog lookup | Read incrementally under 512,000 bytes with the existing timeout; an absent or understated Content-Length cannot bypass the limit |
| NOAA lightning PNG | Read incrementally under 1 MiB; cancel on overflow and release the reader; retain PNG signature checks |
| Daily archive catalog | Hide `api:` captures from entries, day counts and date span; keep their shared storage charge |

The day-count filter completes #5313's entry/span filtering. It is the only
application adjustment beyond the original port. Twelve tests fail against the
unpatched baseline and pass with the patch; the new tests exercise actual
route/helper code and archive SQL. Platform identity, D1/R2 and provider access
are replaced with synthetic boundaries; the archive SQL runs in in-memory
`node:sqlite`. This is not a full D1/Worker integration test.

## Validation

Dependencies came from an existing cache with a byte-identical package lock:
`c976735961394d47a19564c9b2a2b41643647d28a879e82e6f377ac83e1a21db`.
Node was 22.13.1. No dependency input changed.

| Check in isolated replay | Result |
|---|---|
| `node tests/site-route-safeguards.test.mjs` | PASS: 24; same tests on unpatched baseline: 12 pass, 12 fail |
| `node tests/bounded-json.test.mjs` | PASS: 3 |
| `node tests/historical-topo-routes.test.mjs` | PASS: 2, including activation/rollback coverage |
| `node tests/lightning-data.test.mjs` | PASS: 5 |
| `node node_modules/typescript/bin/tsc --noEmit` | PASS |
| `npm run build` | PASS; subsurface containment checks pass |
| New test syntax | PASS |
| `node tests/daily-archive.test.mjs` | UNAVAILABLE: Miniflare's before hook cannot bind loopback (`EPERM`); 18 cancelled, zero passing |
| Complete Site suite, lint and Worker HTTP smoke | NOT RUN; required on restored current source before acceptance |
| Production or browser acceptance | NOT RUN |

The unchanged mirror check passed for 875 files and 48 overlays, with 258
withheld paths absent. The checked mirror tree, receipt blob
`e577fac27ed1d6cd7d3f57bcc902dfd726a4c70e`, and validator blob
`1422318b72267c4a752735d73dfed536f7435439` match the remote base exactly.
This establishes **CONTENT_PARITY_ONLY**. The receipt still says `REVIEW_ONLY`,
source/overlay review `PENDING`, human acceptance false, and review acceptance
`NOT_EVALUATED`; no existing governance hold has been waived.

## Remaining source, synchronization and deployment work

1. Restore access to the exact preserved project and open its latest source
   through the Sites source helper. Read its preservation instructions, preserve
   advanced/unpublished work, and record the exact current source revision.
2. Compare all eleven patch paths. Use the packet's before hashes to detect
   divergence. From that verified standalone checkout, run `git apply --check`
   on the packet before applying it. If a preimage differs or a new test already
   exists, reconcile it manually; do not force an old source over newer work.
3. Run locked dependency checks, lint, typecheck, production build, the complete
   Site suite, and disposable Worker smoke. Run the four focused test files
   above. Obtain separate source review. Record the resulting source commit.
4. Prepare mirror comparison through `tools/qa/site_mirror.py --source` using
   a clean verified source checkout. This is a review-only comparison, not a
   synchronizer. Account for canonical mappings, 48 overlays, and all 258 withheld
   paths; never restore withheld source bytes as a parity fix. Prepare a separate
   reviewed successor receipt and exact matching mirror diff together. Keep the
   predecessor immutable, retain review holds, and rerun mirror/conformance
   checks on that exact proposed head.
5. Publication is a later, separately authorized transition. Preserve project
   identity, owner-only audience, DB/BUCKET bindings and private evidence
   restrictions. No Site version was saved, deployed or published in this work;
   no source credential was obtained and no platform source push was attempted.

## Placement and rollback

Directory Rules §§3–4 and accepted ADR-0029 place explanatory reporting under
the existing `docs/reports` lane and application-scoped review carriers under
existing `apps/site/evidence`. The generated authoring receipt uses the existing
`data/receipts/generated` lane. ADR-0048's external mirror boundary remains in
force. No schema, policy, registry, source, or release authority home is added.

Close this unmerged draft or revert its packet/report/generated receipt together.
There is no runtime rollback to perform because no authoritative application or
data state changed. After a future source port, reverse only the reviewed port
commit; after a future mirror update, revert its source/receipt selector unit
together. Preserve saved versions and existing stores; do not reset storage.
