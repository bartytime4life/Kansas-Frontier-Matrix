---
title: Repository topology ratchet review packet for job 108649601361
status: proposed; draft review only
repository_ref: main@87b144126135d058823bf3be4b56070abb6c5f47
scope: directory-governance validator and baseline reconciliation
---

# Repository topology ratchet review packet

This is an exploratory review packet for [the failed validator job](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/36329859079/job/108649601361). It does not amend Directory Rules, accept a correction, bind the correction register, replace a baseline, authorize a merge, or make the job green.

## Verified failure at the tested revision

The push job tested `main@87b144126135d058823bf3be4b56070abb6c5f47`. Its `repository-topology` step reported 13,654 tracked paths, zero invariant findings, four new drift fingerprints, 118 baselined warnings, and four stale baseline entries. The other validator-suite steps in that job completed successfully. The topology step failed in both its live-baseline tests and its command-line scan.

| Finding | Live evidence | Current baseline | Disposition |
|---|---|---|---|
| `KFM-TOPO-001` nonportable punctuation | Seven paths: five historical documents and two Site API routes using required bracket parameters | Five historical documents | [PR #4769](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4769) removes only the route false positive; it was merged while the aggregate topology check remained red. |
| `KFM-TOPO-001` uppercase | 830 tracked paths | No entry | Historical accepted evidence at `main@27202a0595ecdc6afd6f98b3aedaa236243e07b3` had 892 paths. Current evidence has 12 additions and 74 removals relative to that set; the additions need individual path review. |
| `KFM-TOPO-009` scaffold-only leaves | 1,257 tracked leaf directories | No entry | Historical accepted evidence had 1,270; the current set is a strict 13-directory reduction. Review why the entry disappeared before any recovery. |
| `KFM-TOPO-004` frozen `catalog/` | 43 members; fingerprint `sha256:71a120ae8ca2b69896266c9ddd52f6b03577ea91fa2de4390b7d57b9ceeb912f` | No entry in the current file | Eight README blob replacements differ from the last accepted 43-member evidence. [ADR-0040](../../adr/ADR-0040-catalog-redirect-metadata-corrections.md) accepts the target text only and explicitly holds the machine binding and baseline transition. |
| Stale `KFM-TOPO-014` entries | Three old `apps/explorer-web/tests/` references are absent from the live scan | Three entries remain | Candidate for a reviewed monotonic removal; do not alter the detector. |
| Stale punctuation entry | The five-document fingerprint no longer matches the seven-path live group | Five-document entry remains | The bounded route-syntax draft restores the existing five-document fingerprint without editing the baseline. |

The current baseline has 122 entries. The earlier accepted snapshot at `main@27202a0595ecdc6afd6f98b3aedaa236243e07b3` had 127, including uppercase, scaffold, and `catalog/` groups absent from the current file. The present file and the earlier snapshot are not interchangeable: current path and blob evidence changed. Copying old or newly computed entries into the current file is not an authorized repair.

## Why a direct baseline edit is unsafe

`validate_baseline_transition` compares a candidate with the trusted base and rejects added waiver identities, same-identity evidence expansion, expiry extension, and metadata mutation. A locally constructed candidate that matches the current noncatalog scan still returns `ERROR_VALIDATOR` when checked against the trusted base. Without that check it would leave one `catalog/` new finding and one stale catalog entry; that apparent reduction is not an authorization. The current trusted-base guard is doing its intended work.

The [owner decision in issue #4228](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4228#issuecomment-5736885489) keeps the seven catalog register entries proposed and unbound, Stage 1B under `CATALOG_MULTI_ENTRY_BINDING_HOLD`, and Stage 2 unauthorized. This packet preserves that decision.

## Draft sequence for review

1. **Path classifier:** [PR #4769](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4769) was marked ready and merged by the repository owner account at 2026-09-27 16:08 UTC, although it was submitted as a draft under a hold instruction. Its exact-head hosted topology check remained red with three new and three stale fingerprints. The route exception is confined to valid bracket segments in Site API `route.ts` paths; focused negative cases passed locally. The merge did not change the baseline or lift the catalog hold. The lifecycle transition needs separate owner review.
2. **Historical baseline discrepancy:** establish why the current 122-entry file omitted previously reviewed groups. Review the 12 added uppercase paths individually, and validate the 13 scaffold removals and three retired test references. Draft an explicit recovery decision and tests before changing the baseline. The trusted-base transition must remain fail-closed on unauthorized additions.
3. **Catalog Stage 1B design:** propose one atomic, exact eight-blob batch from the old catalog fingerprint `sha256:521388927153c91a67ca8cead55af9d688a6064517d109aa556cffca91505006` to the accepted target fingerprint `sha256:71a120ae8ca2b69896266c9ddd52f6b03577ea91fa2de4390b7d57b9ceeb912f`. It must bind a trusted-base accepted decision, exactly 43 unchanged paths, eight reviewed replacements, and no independent intermediate live states. Reject omitted, added, reordered, duplicate, or changed blobs; preserve the proposed status until owner and independent control review accept the machine binding.
4. **Catalog Stage 2:** only from a later trusted base that contains accepted Stage 1B binding, implement one-time consumption and the exact baseline transition with positive and negative replay tests. Stage 2 remains unauthorized under the current owner decision.
5. **Final verification:** rerun the full repository-topology target and linked validator-suite on the exact eventual head. Attribute each red job to its own finding. Do not call a draft, passing focused test, or receipt a merge or release authorization.

## Review boundary and rollback

This packet is proposal text. It changes no validator, register, baseline, catalog blob, repository setting, or lifecycle state. Revert this file and its paired generated receipt to remove the proposal. The last accepted catalog decision and the failing guardrail remain in force either way.
