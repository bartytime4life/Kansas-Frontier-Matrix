<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://register/milestone-progress-2026-10-08
title: KFM Milestone and Issue Progress — 2026-10-08
type: dated-progress-ledger
version: v1.3
status: draft; repository-grounded; non-authoritative
owner: "NEEDS VERIFICATION — review routes through current CODEOWNERS (@bartytime4life)"
created: 2026-10-08
updated: 2026-10-22
policy_label: repository-facing
owning_root: docs/
responsibility: "Record per-milestone progress across the 37 native GitHub milestones and 56 open issues since the 2026-09-16 portfolio audit, name the merged work that moved each milestone, record the issue state changes made in this pass, and list counter anomalies and owner actions, without creating review, policy, source, lifecycle, release, or publication authority."
truth_posture: "CONFIRMED main commit, merge census, local command results, issue states read through the GitHub API on 2026-10-08, and the issue closures made in this pass / REPORTED milestone counters as GitHub displays them, including two known-stale counters / NEEDS VERIFICATION hosted workflow results for this snapshot, which were not re-read, and every owner or independent acceptance named below"
evidence_snapshot: "main@897f0df195 (merge of PR #4932, 2026-10-08); 0 open pull requests; 56 open issues before this pass and 53 after; 239 merge commits on main since the 2026-09-16 portfolio audit; local checks on Python 3.12 with the hash-locked all-local-test profile and KFM_NO_NETWORK=1"
related:
  - docs/registers/README.md
  - docs/registers/repository-gap-fill-goal-2026-10-02.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - control_plane/program_baseline.json
  - control_plane/verification_backlog.yaml
  - artifacts/qa/validation/milestone-1/ci_conformance_report.json
notes:
  - "Successor to the 2026-09-16 portfolio audit ledger on issue #2768 (comment 5705060423). That ledger stays the per-issue next-proof record; this file records only what changed after it."
  - "Milestone completion percentages are GitHub issue-count ratios. They do not measure acceptance, and closing a checkpoint issue does not close its milestone's objective."
  - "Counts are snapshot facts. Re-read GitHub and re-run the commands in section 6 before citing them later."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Milestone and Issue Progress — 2026-10-08

## Currentness addendum — 2026-10-22

The October 8 sections below remain historical. This addendum records a fresh
readback of [main at `e18b56879cd71ff13502c6e12f2f1f4c7f02ee6d`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/e18b56879cd71ff13502c6e12f2f1f4c7f02ee6d),
after [PR #5405](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5405).
It does not replace the historical evidence snapshot in this document's header.

| Current observation | Evidence and limit |
|---|---|
| 52 open issues; no open PRs at intake | GitHub issue and pull-request collections read October 22. Subsequent corrective PRs are separate candidates, not part of this main snapshot. |
| 67 successful and 2 skipped workflow runs for this exact main SHA in the latest 100-run collection | [Exact-main runs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions?query=branch%3Amain). The skips were APIsec and GoDaddy hosted capture. No failed exact-SHA run appeared in that collection. This is a bounded workflow readback, not a full check or acceptance census. |
| Topology ratchet passed in the exact-main validator suite | [Run 39803643350](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39803643350), both jobs successful. Historical statements that this check currently fails must not be reused without a new failure. |
| Native milestone 1 is 5 closed / 5 open; current due date is November 9, 2026, 6 p.m. America/Chicago | GitHub issue milestone metadata reports `2026-11-10T00:00:00Z`. September deadline text below is historical. Open items remain #3359, #3360, #3361, #3363, #3364. |
| 28 open Dependabot alerts: 3 critical, 16 high, 9 moderate | Both pages of the owner-visible [alert list](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot) were read. All name Pillow in the crop-tile requirements file. Open-alert state is confirmed; closure is not. |
| Crop declaration and hash lock both pin Pillow 13.0.0 | [Declaration](../../pipelines/domains/soil/crop_casma_tiles/requirements-tiles.txt), [lock](../../pipelines/domains/soil/crop_casma_tiles/requirements-tiles.lock), and [compatibility workflow](../../.github/workflows/crop-casma-tile-compatibility.yml) at the pinned main. Alert #120 names 13.0.0 as patched. [Dependabot job 119911197076](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39803708341/job/119911197076) read this exact SHA and reported no update needed for Pillow 13.0.0. The reason alerts remain open is UNKNOWN; no dismissal or deployed-version claim follows. |

### Bounded advancement queue at intake

| Issue / milestone | Confirmed gap and next proof |
|---|---|
| [#3382 / M17](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3382) | The Python advisory gate at this main audits `tools/ci/python-test.lock`, not the crop-tile lock. The accompanying candidate adds a separate Python 3.12 crop-lock audit and offline failure-propagation regression. Exact-candidate hosted audit execution, GitHub alert reconciliation, and artifact/SBOM/signature acceptance remain distinct. |
| [#3359 / native milestone 1](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3359) | [Draft PR #5406](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5406) corrects reproduced NUL/surrogate `base_ref` CLI crashes before Git subprocess use. Its partial-tree checks passed 13 tests and 11 subtests; three full-packet/history checks were deselected. Bounded JSON rejection and valid Git-pin replay passed locally; exact-candidate hosted checks are separate. Registry authority and normalization acceptance remain open. |
| [#3364 / native milestone 1](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3364) | The [conformance report](../../artifacts/qa/validation/milestone-1/ci_conformance_report.json) is historical, pinned to `c653d573c1641503215844c5c4fc85bc15060ced`. It remains BLOCKED, with no hosted runs and independent review pending. Prepare a successor bound to a stable final candidate; preserve the original. |
| [#3388 / M25](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3388) | Reconcile current issue and milestone acceptance against exact artifacts; this addendum updates the human coordination view only. |
| [#3397 / M33](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3397) | Same-candidate interaction, keyboard, touch, accessibility and device/WebGL acceptance are not established by the workflow census. |
| [#4418 / M35](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4418) | Source/build identity, hosted browser equivalence and saved-predecessor recovery still require an exact-candidate packet. The skipped GoDaddy capture cannot count as acceptance. |
| [#3396 and #4415 / M36](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/3396) | Independent acceptance and same-candidate release proof remain open. Green workflows or closed issue ratios do not authorize release. |

### October 22 follow-through

After the intake snapshot above, [main advanced to `3cc00a065d5d0849c189a9bc31a2e26c30a86909`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/3cc00a065d5d0849c189a9bc31a2e26c30a86909),
incorporating the two bounded repairs below. The intake queue remains historical.

| Work | Follow-through and remaining boundary |
|---|---|
| Registry input handling | [PR #5406](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5406) merged. Its [exact-head hosted registry job](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39830490490/job/120005027387) passed all 16 tests, fixtures, seven registries and the authoring receipt. Registry authority and normalization acceptance remain open. |
| Crop-lock advisory coverage | [PR #5407](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5407) merged. Its [hosted crop-lock audit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39830672858/job/120005647849) reported no known vulnerabilities. The alert UI was re-read after integration: 28 Pillow alerts remain open; graph/alert reconciliation is UNKNOWN. A passing audit does not establish deployed versions, SBOM, attestation or signature acceptance. |
| Critical Next.js inventory finding | The separate Site npm gate failed on Next 16.3.8. [Draft PR #5408](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5408) prepares the standalone source update to selected target 16.4.2. The accompanying main mirror candidate updates the same Next family and preserves a successor parity receipt. Local production audits report zero critical findings after repair; eight inherited high findings remain in the standalone inventory. Runtime exploitability and deployment state are not established by inventory findings. |

The mirror candidate passes 1,401 Node tests, 48 mirror regressions, production
build, typecheck, lint (zero errors; 77 warnings), and local smoke (110 checks
across 79 routes). Its parity check covers 883 paths and keeps 258 paths withheld;
source/overlay review remains PENDING, human acceptance and hosted equivalence
remain false. Topology passes with zero invariant/new-drift findings and 89
baselined warnings. The standalone candidate passes 1,639 tests with 17 skipped,
build and typecheck; source lint retains four errors also reproduced at its exact
base. These local results do not replace exact-head hosted checks or review.

Native milestone 1's five open acceptance items remain open. The historical
conformance report still needs an exact-candidate successor and independent
review. Browser interaction, accessibility, hosted equivalence, recovery and
release acceptance are not established by these repairs. No milestone, alert,
source-admission or release closure is claimed.

### Later October 22 readback

[Main `123d8645b84e705789390f2ca4cbd66cc1eb2f0e`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/123d8645b84e705789390f2ca4cbd66cc1eb2f0e)
includes merged #5406, #5407 and #5409. The separate
[hosted source base `41d7908d7eef051d76fc62a716733efdc2b60dc7`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/41d7908d7eef051d76fc62a716733efdc2b60dc7)
contains merged #5408. Earlier draft states and 28-alert counts above are historical.

[PR #5410](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5410)
now has head `ea43eea6a8d8b20f17c2f1a2361cef6aa6346d7d`. Its tree
`e44cba214aa92313ea0862c03591da07cd1464cc` matches the isolated combined tree
that passed build, typecheck, 1,643 Node tests with 17 skipped and zero failed,
and 37 browser tests using Chrome 156 and Node 22.13. The prior UI head's
[hosted job](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39838770090/job/120033941640)
also passed the complete Node, HTTP, county, aviation, welcome and preview checks.
[Exact-new-head hosted CI](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39840675088)
remains PENDING at this readback. These are source/fixture checks, not deployment
or hosted-equivalence acceptance.

**Subsequent exact-head CI readback.** At unchanged head
`ea43eea6a8d8b20f17c2f1a2361cef6aa6346d7d`, the
[first hosted attempt](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39840675088/job/120040531346)
passed 36 welcome-browser tests and failed one with a CDP `Runtime.evaluate`
timeout. Its cause remains UNKNOWN. The
[same-head retry](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39840675088/job/120048178904)
passed build, typecheck, 1,643 Node tests (17 skipped), 21 HTTP, 15 county,
6 aviation, all 37 welcome-browser and both preview-port checks. Hosted Chrome
was 155.0.8059.39. The first failure remains part of the validation history;
the successful retry does not establish deployment, hosted equivalence or
release acceptance.

A fresh owner-visible read of both alert pages shows **39 open Pillow alerts:
4 critical, 23 high and 12 moderate**.
[Alert #125](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/125),
GHSA-v9pv-5gc8-w2m6, reports affected versions `>=11.0.0,<13.0.0` and fixed
version 13.0.0; the declaration and lock already pin 13.0.0. Its logs link
returns the earlier Dependabot job. The current-main
[crop-lock audit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39838735970/job/120033822577)
reports no known vulnerabilities, and [PyPI's exact 13.0.0 metadata](https://pypi.org/pypi/Pillow/13.0.0/json)
lists no vulnerability entries at this readback. These are bounded advisory
signals. Why GitHub alerts remain OPEN is **UNKNOWN**; no alert reconciliation,
vulnerability-absence or deployed-version claim follows.

The eleven newly opened alert details were subsequently read individually.
Each explicitly names **13.0.0** as patched; the table records their displayed
affected ranges. This resolves the range lookup for this new group, not the
open-alert discrepancy or deployment state.

| Alert | Advisory | Displayed affected range |
|---|---|---|
| [#122](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/122) | GHSA-p8hx-v2p6-rp84 | `<13.0.0` |
| [#123](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/123) | GHSA-g842-9rc4-69pw | `<13.0.0` |
| [#124](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/124) | GHSA-24rc-8hj2-v98c | `>=9.1.0,<13.0.0` |
| [#125](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/125) | GHSA-v9pv-5gc8-w2m6 | `>=11.0.0,<13.0.0` |
| [#126](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/126) | GHSA-mrfp-p49p-3hf2 | `>=5.1.0,<13.0.0` |
| [#127](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/127) | GHSA-4rm8-3hmm-39fg | `<13.0.0` |
| [#128](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/128) | GHSA-3j72-p6qg-6xp7 | `<13.0.0` |
| [#129](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/129) | GHSA-g4qv-2jxx-769h | `>=11.0.0,<13.0.0` |
| [#130](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/130) | GHSA-9v9v-9qvf-h2hj | `<13.0.0` |
| [#131](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/131) | GHSA-g7cr-3p24-7wf7 | `>=9.4.0,<13.0.0` |
| [#132](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/dependabot/132) | GHSA-78g4-xqwv-q3g8 | `>=11.1.0,<13.0.0` |

The maintainer advisory headers for
[PDF append](https://github.com/python-pillow/Pillow/security/advisories/GHSA-mrfp-p49p-3hf2),
[JPEG comments](https://github.com/python-pillow/Pillow/security/advisories/GHSA-g7cr-3p24-7wf7)
and [bundled OpenJPEG](https://github.com/python-pillow/Pillow/security/advisories/GHSA-78g4-xqwv-q3g8)
also list 13.0.0 as patched. Their narrative reproductions include earlier
development/release snapshots; those do not establish the installed or deployed
KFM binary. No additional dependency change or alert dismissal is supported by
these version fields alone.

Native milestone 1 now displays five open and six closed items because merged
#5406 counts as a closed item. The same five original acceptance issues remain
open; the counter change does not establish milestone completion.

Milestone acceptance, independent review, conformance, SBOM/signature proof,
hosted equivalence and recovery remain open. These observations establish no
milestone, alert, admission or release closure.

**Validation boundary.** This pass re-read GitHub source, alert UI and workflow
results. Local candidate regressions are recorded on their PRs; historical test
counts below were not rerun by this addendum. No milestone, issue, review,
source, lifecycle, policy, release, deployment, or publication state is changed.

**Placement and recovery.** This same-path human progress ledger remains under
`docs/registers/`, per its [boundary README](README.md) and accepted
[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md).
Platform workflow changes belong under `.github/`, and executable regression
tests under `tests/`. No parallel register or proof home is introduced. Correct
this addendum in place through review; preserve historical reports and receipts.
Abandon an unaccepted candidate or revert its bounded change after authorized
integration. Do not restore a vulnerable dependency as an alert workaround.

---

> [!IMPORTANT]
> This ledger is a review aid. It records what changed after the 2026-09-16 portfolio audit and what this pass did to GitHub issue state. It does not approve, admit, release, deploy, or publish anything. A closed issue means its stated completion boundary was met. It does not mean independent review happened.

---

## 1. Snapshot

| Fact | Value |
|---|---|
| `main` | `897f0df195` (PR #4932, 2026-10-08) |
| Open pull requests | 0 |
| Merge commits since the 2026-09-16 audit (`fd03c91c88`) | 239 |
| Open issues | 56 before this pass, 53 after |
| Native milestones | 37 (MRTS milestone 1 plus M01–M36 as natives 2–37; native number = M-number + 1) |
| Milestones at 100% by issue count | M07, M11, M16 (after this pass), and M31 (after the counter recount in section 4) |

[Back to top](#top)

---

## 2. Repository-wide changes since the audit

These change the status of more than one milestone.

| Change | Evidence | Milestones affected |
|---|---|---|
| Repository topology returns **0 new drift** | `make repository-topology`: PASS, 14,237 tracked paths, 0 invariant, 0 new drift, 113 baselined warnings, 0 stale entries. Unblocked by PR #4931; baseline waivers recovered in PR #4782. | All issues whose last checkpoint names "inherited topology failures". Governance parity stays `HOLD_INHERITED` because 113 baselined warnings remain, by design of `validate_repository_governance_parity.py`. |
| Repository licensed | PR #4797: code under Apache-2.0, docs and data under CC BY 4.0; `pyproject.toml` now declares `Apache-2.0`. | M17 (#3382) and M35. The M35 checkpoint (#3399) recorded `license = TBD` as BLOCKED for publication. That blocker is resolved; dependency license review is still open. |
| `apps/explorer-web` retired | PR #4691 retired obsolete monorepo Explorer implementations; `apps/site` is the Explorer. | M08 (#3372) and M33 (#3397). Cited UI evidence such as `living-waters-fixture.ts` no longer exists on `main`. |
| Connector fetch/admit stubs replaced | PRs #4745–#4780: shared retrieval-episode and descriptor gate; role and rights resolved for seven federal connectors. | M20 (#3384), M28 (#3393), M05 (#3369) |
| Code-scanning alerts fixed | PRs #4731–#4747 (SSRF, URL sanitization, regex anchors), #4609, #4795 | M14 (#3376), M17 (#3382) |
| Finite error outcomes across validators and the governed API | PRs #4668, #4669, #4670, #4672, #4673 (2026-09-22) | M34 (#4416), M22 (#3390), M04 (#3367) and M19 (#3381) |

[Back to top](#top)

---

## 3. Milestone progress

GitHub counts are shown as reported on 2026-10-08, after this pass's closures. "Since audit" lists merged work after 2026-09-16 that moves the milestone. "No change" means no merged work or issue update was found. In that case the next proof in the 2026-09-16 ledger still applies.

| Milestone | Closed / open | Open issues | Since audit | Disposition and next proof |
|---|---|---|---|---|
| MRTS — Machine-Readable Control Plane & Trust Spine (native 1) | 5 / 5 | #3359, #3360, #3361, #3363, #3364 | PR #4869 moves `RuntimeResponseEnvelope` CONFLICTED → PARTIAL; conflicted required families 11 → 10. All MRTS make lanes pass locally (section 6). | OPEN / HOLD. The due date of 2026-09-18 has passed. The CI conformance report is still `BLOCKED` on four items. Its `TOPOLOGY_INHERITED_HOLD` detail (9 new-drift categories) is stale; topology now has 0 new drift. Hosted exact-head checks and human review remain. Next: a successor conformance report against current `main`. |
| M01 — Authority, Directory Rules & Program Baseline | 0 / 2 | #3365, #4228 | Topology at 0 new drift (#4931, #4782); KFM-TOPO-004 catalog correction entries drafted (`dec2e49e44`). | OPEN. `control_plane/program_baseline.json` is still pinned to `main@6aa1ce50`. #4228 remains Stage 1A accepted / Stage 1B HOLD / Stage 2 unauthorized. Next: refresh the program baseline to current `main`. |
| M02 — Contracts, Schemas, Policy & Compatibility | 0 / 1 | #3368 | PR #4797 retired extra `triplet` and `pipelines/specs` spellings. | OPEN / PARTIAL. No change to the first-slice contract. |
| M03 — Deterministic Identity & Temporal Authority | 0 / 1 | #3370 | No change. | OPEN. |
| M04 — Evidence Resolution & Governed Response | 0 / 1 | #3367 | PR #4672 adds finite errors for malformed evidence-resolution input. `make evidence-resolver` and `make evidence-resolver-deny` pass (65 tests each). | OPEN / PARTIAL. |
| M05 — Source Admission, Rights & Sensitive Data | 0 / 1 | #3369 | PR #4812 reconciled the USGS station identity: runbook, connector, and profile all name `USGS-06892518`. This was the next gate named in the 2026-09-30 checkpoint. Source candidates also landed: #4635 (DASC), #4636 and #4814 (NOAA normals), #4637 (KHS manual-only), #4815 and #4817 (DASC HUC12 held). | OPEN / PARTIAL / SOURCE_ADMISSION_HELD. Next: accountable source-rights and sensitivity review and independent review of the exact USGS candidate. |
| M06 — Validation, Security & Supply-Chain Gates | 1 / 1 | #3366 | PR #4868 binds the release dry-run (exact-head hosted success recorded 2026-10-03). PR #4840 disabled fabricated hydrology promotion approval. PR #4798 repaired inherited CI failures in six workflows. | OPEN / PARTIAL. APIsec was SKIPPED and water-pilot failed on mirror digests; each needs its own disposition. |
| M07 — Catalog, Provenance, Release & Rollback Closure | 2 / 0 | — | — | 100% by issue count; the milestone is still open. Owner action: close the milestone or add successor work. |
| M08 — Public-Safe Hydrology & Ecology Proof Slices | 0 / 1 | #3372 | PRs #4791 and #4792 implement the synthetic hydrology proof slice: finite outcomes, EvidenceBundle pinning, stale badge, source-role and non-public denial, and a dry-run rollback rehearsal. 35 tests pass, and the `proof-slice` lane passes. **Regression:** PR #4691 retired the `apps/explorer-web` Living Waters UI that the checkpoint cited as its map carrier. | OPEN / PARTIAL. Next: rebind the map carrier to `apps/site`, then close the checkpoint against its completion boundary. |
| M09 — Interoperable Data & Delivery Artifacts | 0 / 1 | #3374 | No change. | OPEN. |
| M10 — MapLibre Runtime, PMTiles & Evidence Drawer | 0 / 1 | #3375 | PR #4643 proves same-candidate selection reaches the Evidence Drawer. PR #4619 adds a shared EvidenceDrawer. Site v169–v173 delivered (#4913–#4915, #4932). | OPEN. Package-owned renderer and PMTiles admission stays under #2906. |
| M11 — Governed API, Focus Mode & AI | 1 / 0 | — | — | 100% by issue count; the milestone is still open. Owner action: close the milestone or add successor work. |
| M12 — Cross-Domain Atlas & Operational Readiness | 1 / 1 | #3378 | No change. | OPEN. |
| M13 — Repository Control, Review Integrity & Conformance | 2 / 9 | #2874, #4024, #3663, #3668, #3670, #3673, #3674, #3677, #3679 | PR #4678 retired the repository transition check. PR #4612 hardened transition authorization. PR #4861 added the gap-scan ratchet. | OPEN. The seven automation-design issues have had no activity since 2026-09-16 and stay under `MILESTONE_SCHEDULER_RECONCILIATION_HOLD`. Owner action: record retirement or replacement of each scheduled task so these can close. |
| M14 — Security Classification, Threat Model & Critical-Asset Exposure | 0 / 1 | #3376 | Code-scanning fixes (section 2). | OPEN. |
| M15 — Incident Response, Secrets, Key Lifecycle & Recovery | 0 / 1 | #3380 | No change. | OPEN. |
| M16 — Quality Baselines, Non-Vacuous Tests & CI Reliability | **4 / 0** | — | #4596 and #4606 closed in this pass (section 5). Also landed: PR #4798 (inherited CI repairs), #4864 and #4865 (scaffold stubs now fail closed), #4645 (pytest collisions). | 100% by issue count. Owner action: close the milestone. Independent review of #4608 and #4867 is still outstanding. |
| M17 — Dependency, Container, SBOM & Supply-Chain Assurance | 0 / 1 | #3382 | PR #4797 licensed the repository. PR #4886 audits Site npm dependencies in dependency-scan. PRs #4795, #4916, and #4918 handle alert 53. PR #4908 fixes dependency-scan regressions. | OPEN / PARTIAL. SBOM, attestation, and signature proof remain. |
| M18 — Temporal Semantics, Compatibility & Correction Lineage | 0 / 1 | #3383 | No change. | OPEN. |
| M19 — Evidence Resolver, Citation Integrity & Governed Consumer Closure | 0 / 1 | #3381 | PR #4672 (finite errors), PR #4643 (selection reaches the Drawer). | OPEN / PARTIAL. |
| M20 — Source Rights, Health, Watchers & Change Detection | 0 / 1 | #3384 | Connector role and rights (#4779, #4780). Station health receipts (#4823, #4829). Source locator and freshness evidence (#4639). | OPEN / PARTIAL. |
| M21 — Transportation, Infrastructure & Public-Safe Geometry | 0 / 2 | #3385, #2898 | No change. | OPEN. |
| M22 — Drought, Water Supply, Soil & Agriculture Observation Proof | 0 / 2 | #3390, #2899 | PR #4669 gives the drought-family validator finite outcomes and runs it in CI. PR #4670 makes the soil validator CLIs fail closed. PR #4793 adds SMAP soil-moisture context. `make hazards-validate` passes. | OPEN / PARTIAL. |
| M23 — MapLibre Runtime Admission, Accessibility & Performance | 1 / 1 (recounted; was displayed 1 / 0) | #2906 | PR #4784 confines Site MapLibre acquisition to one seam. PRs #4908 and #4909 fix the perf gate. | OPEN / HOLD. `packages/maplibre` pins `6.11.2`, while `apps/site` and the readiness classifier target `6.9.0`. All 12 probes are still NOT_RUN. The counter was corrected in this pass (section 4). |
| M24 — GeoParquet, PMTiles & COG Cross-Engine Interoperability | 0 / 2 | #3386, #2907 | No change. | OPEN / HOLD. |
| M25 — Program Decision Ledger, Ownership & Portfolio Closure | 0 / 3 | #3388, #2768, #3672 | Queue syncs on 2026-09-20, 10-03, and 10-07; this ledger. | OPEN. |
| M26 — Trust Membrane, Sensitivity & Public-Path Closure | 0 / 2 | #3389, #3022 | PR #4679 recovers render failures without exposing raw errors. PR #4843 rejects undeclared Qwen context fields. | OPEN. #3022 stays HOLD. |
| M27 — Evidence Authentication, Citation & Consumer Closure | 0 / 1 | #3392 | No change. | OPEN. |
| M28 — Source Admission Operations, Rights & Freshness | 0 / 1 | #3393 | Connectors (section 2). Bounded captures: GHCN Daily (#4919, #4920), NEXRAD (#4921, #4924), NWM (#4922). | OPEN / PARTIAL. Captures are not admissions. |
| M29 — Temporal Replay, Correction & Cross-Version Migration | 0 / 1 | #3394 | No change. | OPEN. |
| M30 — Domain Convergence & Cross-Lane Join Governance | 0 / 1 | #3391 | No change. | OPEN. |
| M31 — Catalog Graph, Provenance & Release Candidate Closure | 1 / 0 (recounted; was displayed 0 / 1) | — | — | 100% by issue count; the only issue, #3395, is closed. The milestone is still open. Owner action: close the milestone or add successor work. |
| M32 — Governed API, Query Semantics & Serving Readiness | 0 / 1 | #3400 | PR #4668 keeps timeout and cancellation out of generic 500 responses. PR #4926 fixes governed API startup. | OPEN. |
| M33 — Explorer Web, Accessibility & Interaction Continuity | 1 / 1 | #3397 | Site Explorer work through v173. PR #4691 retired the legacy Explorer. | OPEN. Browser visual, touch, device WebGL, and full keyboard acceptance remain unverified. |
| M34 — Observability, Incident, Correction & Recovery Rehearsal | 1 / 1 | #4416 | PRs #4668, #4670, #4672, #4673 (finite errors). PRs #4679 and #4681 (bounded Explorer error states). | OPEN / PARTIAL. Async rejection, workspace-preserving recovery, operator-health semantics, and independent review remain. |
| M35 — Reproducible Builds, SBOM, Attestation & Artifact Integrity | 1 / 1 | #4418 | Site v173 source and deployment identity recorded. PR #4797 resolves the license blocker named in #3399. | OPEN / HOLD. `MIRROR_REVIEW_REQUIRED` and production rollback proof remain. |
| M36 — Governed Atlas Release Readiness & Stewardship | 0 / 2 | #3396, #4415 | PR #4868 (release dry-run binding). | OPEN. |

Unassigned before this pass: #4613, now closed.

[Back to top](#top)

---

## 4. Counter anomalies and owner actions

1. **Stale counters on M23 and M31, now corrected.** #2906 was moved from M31 to M23 on 2026-09-15, but GitHub's denormalized counters were not recomputed. M23 displayed 100% complete while #2906 was open. M31 displayed 0% while its only issue, #3395, was closed. This pass re-assigned #2906's milestone (M23 → M31 → M23), which forced a recount. The API now reports M23 at 1 closed / 1 open and M31 at 1 closed / 0 open.
2. **Milestones at 100% that are still open:** M07, M11, M16, and M31. Closing a native milestone is an owner action. The connector used in this pass cannot edit milestones.
3. **Overdue MRTS milestone:** due 2026-09-18, five of ten issues still open. Owner action: set a new due date or record the hold.
4. **Repository-wide stale wording:** many issue checkpoints still say "inherited topology failures remain". On `main@897f0df195` that is no longer true for new drift (section 2). Update each one at its next checkpoint rather than in bulk.

[Back to top](#top)

---

## 5. Issue state changes in this pass

| Issue | Milestone | Action | Basis |
|---|---|---|---|
| #4596 | M16 | Closed, completed | Repairs (#4604, #4607) and checklist v1.5 (#4867) are on `main`. `make normalized-summary-check` passes 75 tests. The owner listed it as a closure candidate on 2026-10-03. |
| #4606 | M16 | Closed, completed | PR #4608 is merged and the same 75 tests pass. The owner listed it as a closure candidate on 2026-10-03. |
| #4613 | none | Closed, completed | Decision subject `a313dee962` is an ancestor of `main`, and the schema SHA-256 `0f08e216…fcf59` is unchanged. |
| #2906 | M23 | Milestone re-assigned (M23 → M31 → M23) | Counter recount only (section 4). No content change. |
| #2768, #3364, #3369, #3372, #3382, #4416 | various | Progress comment | Material change since each issue's last checkpoint (sections 2 and 3). |

Not closed: #3372 (map-carrier evidence was retired) and the M13 automation-design issues (owner scheduler disposition is required). Independent review is still outstanding for every closure above.

[Back to top](#top)

---

## 6. Commands run on the snapshot

Environment: Python 3.12 venv, `python tools/ci/install_python_ci.py all-local-test`, `KFM_NO_NETWORK=1`, `PYTHONDONTWRITEBYTECODE=1`.

| Command | Outcome |
|---|---|
| `make normalized-summary-check` | PASS, 75 tests |
| `python -m pytest tests/domains/hydrology/test_proof_slice.py tests/e2e/test_hydrology_proof_slice.py` | PASS, 35 tests |
| `make proof-slice` | exit 0, 14 cases |
| `make trust-spine-baseline` | PASS; receipt valid, review pending |
| `make control-plane-registry-packet` | PASS; receipt valid, review pending |
| `make trust-spine-fixture-slice` | PASS; 11 artifacts; receipt valid |
| `make ci-conformance-report` | validation PASS; report status `BLOCKED`, 4 unresolved items |
| `make program-baseline` | PASS against its pinned `main@6aa1ce50` projection |
| `make evidence-resolver`, `make evidence-resolver-deny` | PASS, 65 tests each |
| `make hazards-validate` | exit 0; expected DENY outcomes for invalid fixtures |
| `make repository-topology` | PASS; 0 new drift, 113 baselined warnings |
| `make repository-governance-parity` | `HOLD_INHERITED`, 0 findings |

Not run: hosted workflows for this snapshot, browser or WebGL checks, the full repository test suite, and independent review.

[Back to top](#top)

---

## 7. Non-effects and correction

This ledger and its issue updates do not accept an ADR or policy, admit or activate a source, approve review, change repository settings, transition lifecycle data, release, deploy, or publish. To correct a closure, reopen the issue and append a comment linked to its closure comment. To correct this file, make a same-path forward fix or revert it through review.

[Back to top](#top)

