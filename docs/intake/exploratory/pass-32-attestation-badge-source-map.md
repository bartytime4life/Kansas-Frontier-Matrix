<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-attestation-badge-source-map
title: Pass 32 attestation badge - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; non-authoritative
owners: OWNER_TBD - UI steward; evidence steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0011 with current repository authorities and the bounded Explorer implementation
truth_posture: CONFIRMED source statement and current-repository overlap / PROPOSED app-local implementation / UNKNOWN production integration and runtime proof
related: [../../../apps/explorer-web/src/features/attestation_badge/README.md, ../../../contracts/evidence/release_bound_run_receipt.md, ../../architecture/evidence-drawer.md, ../../architecture/ui/TRUST_BADGES.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 attestation badge - governed implementation source map

## Source statement

`KFM-P32-FEAT-0011` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a compact badge showing whether DSSE/cosign, `RunReceipt`, and `EvidenceBundle` checks passed for a derived map layer. The connected Drive seed-card corpus corroborates the evidence/receipt/release separation but does not establish repository implementation.

## Current repository reconciliation

At inspected `main@149af17075f7f12d716aa14de439ea22ee6a343e`:

- the Explorer Trust Header and Evidence Drawer already establish text-first, finite-outcome, no-leak UI patterns;
- `ReleaseBoundRunReceipt` already binds declared attestation, runtime receipt, evidence, release, correction, and rollback references while fixing every authority claim false;
- UI doctrine explicitly warns that a badge is not proof and must lead to inspectable supporting material; and
- open pull requests `#2441` and `#2442` cover reveal-session and denial-reason surfaces, not attestation-badge behavior.

No new evidence, receipt, signature, policy, review, release, or proof object is justified. The bounded gap is an app-local public-safe projection and accessible UI signal.

## Implemented boundary

The implementation accepts four exact outcome/reason pairs. Only `ANSWER / CHECKS_VERIFIED` carries bounded references for attestation, run receipt, EvidenceBundle, release manifest, layer, and evaluation time. Every negative state carries null references and renders fixed copy. Unknown fields, noncanonical timestamps, wrong reference families, missing positive closure, and outcome/reason mismatch fail closed.

The component does not verify cryptography, resolve evidence, read lifecycle stores, execute policy, authenticate review, authorize release, fetch data, persist state, deploy, or publish. Its positive action delegates the already-parsed projection to a caller-supplied inspection callback.

## Directory Rules basis

UI implementation remains under `apps/`; synthetic projections remain under `fixtures/ui/`; tests remain in the Explorer harness; this reconciliation remains under `docs/intake/exploratory/`; authoring accountability remains under `data/receipts/generated/`. Existing contract and schema authorities are referenced rather than copied.

## Validation and rollback

Validation is the Explorer unit suite, production typecheck/build, isolated browser-fixture typecheck, hosted Playwright coverage, and generated-receipt byte binding. Rollback is a focused revert of this additive packet; it has no source, lifecycle, signature, policy, review, release, deployment, or publication effect.
