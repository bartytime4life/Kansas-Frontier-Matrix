<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-oci-artifact-browser-source-map
title: Pass 32 OCI artifact browser - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; implementation-mapped; fixture-only; non-authoritative
owners: OWNER_TBD - UI steward; artifact steward; release steward; security reviewer
created: 2026-08-10
updated: 2026-08-10
policy_label: internal
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0002 and connected Drive OCI artifact ideas with current repository surfaces and the bounded Explorer implementation
truth_posture: CONFIRMED source statement repository and pull-request gap plus focused local proof / PROPOSED unmounted fixture-only UI / UNKNOWN registry integration signature verification release wiring and hosted exact-head proof
related: [../../../apps/explorer-web/src/features/oci_artifact_browser/README.md, pass-32-attestation-badge-source-map.md, signed-rollback-token-source-map.md]
[/KFM_META_BLOCK_V2] -->

# Pass 32 OCI artifact browser - governed implementation source map

## Source statement

`KFM-P32-FEAT-0002` in the supplied *KFM Domains v1.1 + Pass 23/Pass 32 Consolidated Atlas* proposes a release-review table for artifact tags, digests, referrers, signatures, and rollback candidates. The card was visually checked on physical PDF page 1130; its extracted source-card record hashes to `sha256:65a75ca1f6b979145ae9eff4a30e4a732525e79283e37117be548fbf76048f6c`.

Connected Google Drive material proposes OCI/ORAS/Cosign geospatial artifact storage with tags, immutable digests, and referrers. The inspected Drive sources were the consolidated atlas (`1w7Qrf5Na7PSvwdTuplZnFbyueToPtQaa`), *KFM Full Atlas seed cards* (`1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho`), and *New Ideas* (`142-qzQIydi1Erd3FJherlxxQ9BZqkbCjV06IuuQ-THc`). These sources describe candidate architecture; they do not prove that a registry, signature, artifact, rollback decision, or repository implementation exists.

## Repository reconciliation

At inspected `main@463381703bcd6eada8eea05e95c4a88912ed4b02`, the repository already contained attestation, promotion-gate, rollback-token, release, and artifact-related contract surfaces. Repository, branch, issue, and pull-request searches found no implementation for the exact OCI artifact browser card.

No new registry client, artifact contract, signature verifier, promotion gate, rollback executor, release authority, or public route is justified by the gap. The smallest dependency-closed slice is an unmounted Explorer adapter and text-first table over exact synthetic governed projections.

## Implemented boundary

The positive projection carries a synthetic OCI registry scope, canonical UTC-second review time, unique mutable tags, digest-pinned artifact identities, bounded media types and sizes, ordered signature/provenance/SBOM referrer records, subject-digest equality, and one rollback candidate reference. The UI labels tags as mutable, digest as identity, every present referrer as recorded but unverified, and rollback as a candidate only.

Finite `ABSTAIN`, `DENY`, and `ERROR` states contain no registry, time, artifact, signature, referrer, or rollback detail. Unknown fields, malformed references, tag/digest drift, duplicate tags or digests, subject mismatch, referrer-order drift, missing recorded signature, noncanonical time, positive-detail leakage into negative states, or any true governance flag fail closed and render nothing.

Six false governance flags make the non-effects explicit: the fixture did not contact a registry, verify a signature, authorize rollback, authorize release, authorize publication, or allow public use. The component is not mounted in a route and has no fetch, storage, cryptography, ORAS, Docker, registry, lifecycle, model, promotion, rollback, release, deployment, or publication client.

## Directory Rules basis

App-local parsing and presentation remain under `apps/explorer-web/`; synthetic projections remain under `fixtures/ui/`; source adaptation remains under `docs/intake/exploratory/`; and authoring accountability remains under `data/receipts/generated/`. Existing artifact, attestation, policy, rollback, and release authorities remain authoritative in their current roots and are not copied.

## Validation and rollback

Validation comprises focused Vitest adapter/feature tests, the complete Explorer unit suite, strict TypeScript and Vite production build, isolated browser-fixture typecheck, Playwright spec discovery/execution where Chromium is available, repository policy-boundary guards, and generated-receipt byte binding. Hosted exact-head proof, real registry admission, cryptographic verification, and release integration remain pending. Rollback is a focused revert of this additive packet; it changes no registry, artifact, signature, release, deployment, or public state.
