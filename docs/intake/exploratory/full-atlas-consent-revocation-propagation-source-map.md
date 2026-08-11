<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-consent-revocation-propagation-source-map
title: Full Atlas Consent Revocation Propagation Source Map
type: source-map
version: v0.1.0
status: proposed; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - Intake steward; Consent steward; Privacy steward; People/DNA/Land steward
created: 2026-08-11
updated: 2026-08-11
policy_label: restricted-review; provenance; implementation-intake; no-source-activation; no-publication
owning_root: docs/
responsibility: Record the source chain, current-main gap decision, placement, and non-effects for the bounded consent revocation propagation assessment.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Full Atlas consent revocation propagation source map

## Selected idea and source identity

| Item | Evidence reference | Use |
|---|---|---|
| Drive Full Atlas | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`; current Drive revision `3`; modified `2026-07-12T16:59:46.342Z` | Supplies KFM-TRIAD-038, Purpose-Bound Consent and Revocation Propagation. |
| Repository mirror | `docs/kfm_full_atlas_seed_cards.md`; SHA-256 `07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445` | Reviewable local copy of the exact triad wording and candidate keys KFM-CAND-0112 through KFM-CAND-0114. |
| Intake reconciliation | `docs/intake/exploratory/new-ideas-4-16-source-map.md` | Records extensive consent/revocation doctrine but partial executable status, lookup, dependency, and cleanup behavior. |
| Existing bounded implementation | `contracts/domains/people-dna-land/consented_genealogy_overlay.md` and its paired schema, manifest, validator, fixtures, and tests | Already denies revoked fixture overlays but explicitly does not prove cleanup or downstream propagation. |
| Directory authority | `docs/doctrine/directory-rules.md`; SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e` | Requires contract, schema, fixtures, validator, tests, and docs to stay in their responsibility roots. |

The atlas and intake packet are synthesis and exploratory carriers. They do not issue consent or authorize implementation by themselves.

## Current-main repository-gap check

The reviewed base is `main@f2ef6741430f93270eb38a4ee9170f8a3726e5b3`. No open user pull request was returned by the connected GitHub PR listing at review time.

Current main contains:

- a closed fixture-only consented-genealogy overlay profile;
- a fixture revocation manifest that denies a listed overlay;
- consent policy and runbook documentation; and
- UI consent-card projections.

Current main does not contain a closed, machine-enforced assessment that inventories all seven consequential surfaces named by KFM-TRIAD-038 and proves that revoked/expired consent blocks immediate use while invalidating or purging derived materializations. The existing overlay contract explicitly states that it does not execute or prove deletion, withdrawal, cache invalidation, graph cleanup, search cleanup, or publication rollback.

## Decision and boundaries

Status: `REPO_GAP`, accepted only as an inactive synthetic assessment.

The dependency-closed slice defines:

- exact active, revoked, expired, unknown, and error status postures;
- seven purpose/scope dimensions;
- an exact ordered dependency inventory for read, answer, export, tile, graph, index, and cache;
- receipt-bound block/invalidate/purge declarations; and
- deterministic no-network fixture validation with finite outcomes.

It does not define a production `ConsentGrant`, consent token, representative authority, legal sufficiency, real subject, cleanup executor, credential, KMS, evidence resolver, policy engine, release workflow, public API, UI, or publication path.

`SATISFIED` is local to the consent dimension and passes nothing automatically. Evidence, rights, sensitivity, policy, review, release, correction, rollback, and publication remain independent gates.

## Placement

Directory Rules place object meaning in `contracts/domains/people-dna-land/`, machine shape in `schemas/contracts/v1/domains/people-dna-land/`, synthetic examples in `fixtures/domains/people-dna-land/`, validation in `tools/validators/domains/people-dna-land/`, proof in `tests/domains/people-dna-land/`, and this intake record in `docs/intake/exploratory/`.

No new root or parallel consent, schema, policy, source, receipt, release, or proof authority is created.

## Rollback

Revert the bounded feature commit. No real consent record, cleanup action, cache mutation, graph mutation, index mutation, source activation, lifecycle transition, release, or publication requires operational rollback.
