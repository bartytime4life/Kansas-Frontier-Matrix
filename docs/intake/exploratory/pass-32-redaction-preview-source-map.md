<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-redaction-preview-source-map
title: Pass 32 redaction preview - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; non-authoritative
owners: OWNER_TBD - UI steward; sensitivity steward; redaction steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0012 with current repository authorities and the bounded Explorer implementation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED app-local implementation / UNKNOWN production integration and runtime proof
related: [../../../apps/explorer-web/src/features/redaction_preview/README.md, ../../../contracts/shared/redaction_receipt.md, ../../standards/REDACTION_DETERMINISM.md, ../../../policy/redaction/profiles.yaml]
[/KFM_META_BLOCK_V2] -->

# Pass 32 redaction preview - governed implementation source map

## Source statement

`KFM-P32-FEAT-0012` in the connected Drive *KFM Pass 32 Idea Index, Category Atlas, and Expansion Dossier* and the supplied consolidated Pass 23/32 atlas proposes that reviewers preview generalized geometries, min-n suppression, zoom limits, and public-safe abstractions before release. The card marks repository placement, contracts, policy bundles, tests, runtime behavior, and implementation status as unresolved; it does not authorize a release surface by itself.

## Current repository reconciliation

At inspected `main@47fba107144e4f68851ea1265dae48878d4799ab`:

- `contracts/shared/redaction_receipt.md` defines a redaction receipt as auditable process memory that must not reveal protected values, reversal parameters, or grant publication authority;
- `policy/redaction/profiles.yaml` and domain sensitivity policies retain allow/deny and transform-selection authority outside the Explorer;
- `docs/standards/REDACTION_DETERMINISM.md` and `docs/standards/REDACTION_PROFILES.md` retain transform and verifier guidance;
- the redaction-receipt validator, fixtures, and workflow already prove a bounded receipt lane;
- the Explorer consent, reveal-session, denial-reason, attestation, citation, and lineage surfaces establish strict public-safe projection and no-leak UI patterns; and
- GitHub reports no open pull requests after the latest idea-slice merges.

No new redaction policy, transform recipe, receipt object, schema, release decision, or restricted-data route is justified. The bounded gap is a read-only app-local projection and reviewer summary that can describe four finite public-safe properties without accepting the protected material they summarize.

## Implemented boundary

The projection accepts four exact outcome/reason pairs. Only `ANSWER / PREVIEW_READY` carries digest-bound release-candidate, policy-decision, and redaction-receipt references plus finite values for geometry treatment, low-count treatment, maximum public zoom, and public-safe abstraction class. Every negative state carries null detail and renders fixed copy.

Unknown fields, raw or generalized geometry payloads, coordinates, counts, min-n thresholds, hidden values, reversal parameters, free-form diagnostics, missing positive closure, noncanonical timestamps, out-of-range zoom values, wrong reference families, and outcome/reason mismatches fail closed. The view model does not expose reference strings. Its only optional action delegates the parsed projection to a caller-supplied receipt-inspection callback.

The component does not read restricted or lifecycle stores, execute transforms, select policy, determine sufficiency, authenticate review, approve release, fetch data, persist state, deploy, or publish.

## Directory Rules basis

Directory Rules sections 4, 7.1, 11, and 16 place deployable Explorer implementation under `apps/explorer-web/`, synthetic public-safe inputs under `fixtures/ui/`, executable conformance beside the Explorer test harness, human source reconciliation under `docs/intake/exploratory/`, and authoring accountability under `data/receipts/generated/`. Existing contract, schema, policy, receipt, review, and release authorities are referenced rather than copied. No new root, compatibility authority, domain root, lifecycle phase, or parallel trust-object home is created.

## Validation and rollback

Validation is the full Explorer unit suite, production typecheck/build, isolated browser-fixture typecheck, hosted Playwright coverage, policy-boundary tests, generated-receipt byte binding, and changed-path review. Rollback is a focused revert of this additive packet; it has no source, restricted geometry, count, policy, receipt, review, release, deployment, publication, or public-use effect.
