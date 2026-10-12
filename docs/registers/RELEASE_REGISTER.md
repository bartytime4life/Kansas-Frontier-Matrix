<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registers/release-register
title: Release Register - Evidence Navigation and Review Guide
type: register-guide
version: v0.1
status: draft; repository-grounded; documentation-only; review-required
owners: NEEDS VERIFICATION - domain and documentation stewardship
created: 2026-10-08
created_note: Date of this substantive documentation edition; the tracked path existed earlier.
updated: 2026-10-08
policy_label: repository-facing; cite-or-abstain; no-operational-approval
owning_root: docs/
responsibility: Navigate release evidence and human index preparation while preserving canonical release decisions and explicit incomplete projection coverage.
truth_posture: CONFIRMED pinned repository inventory and source inspection; PROPOSED review-required documentation guide; NEEDS VERIFICATION accountable stewardship and operational acceptance
evidence_snapshot: main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
related:
  - docs/registers/README.md
  - docs/registers/RELEASE_STATE.md
  - release/README.md
  - contracts/release/release_manifest.md
  - control_plane/release_state_register.yaml
  - docs/domains/fauna/RELEASE_INDEX.md
  - docs/domains/flora/RELEASE_INDEX.md
[/KFM_META_BLOCK_V2] -->

# Release Register

Use this page to find the records needed to assess a claimed KFM data release and to prepare a human-readable index entry without creating a second release authority. The actual release, promotion, correction, withdrawal and rollback decisions belong to [release/](../../release/README.md); published payloads and their consumers remain separate.

No production release is newly certified or entered by this documentation edition.

## Current source posture

At `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`, the [machine release-state projection](../../control_plane/release_state_register.yaml) declares `PROPOSED`, `projection_only`, `implementation_status: ABSENT`, `completeness: empty` and `entries: []`. That describes this projection's coverage. It does not prove that every other release surface is empty.

The [ReleaseManifest contract](../../contracts/release/release_manifest.md) describes a dual-profile schema: permissive legacy compatibility plus a closed, proposed inactive fixture-only candidate. Its bounded validator does not resolve real references, verify live signatures, execute production policy or authenticate a release decision.

The repository contains candidate directories and manifest-shaped examples. Their names and presence are not release certification. Inspect each object's actual role and supporting decisions before making a state claim.

## Follow the evidence in order

| Question | Read first | Required interpretation |
|---|---|---|
| What owns release decisions? | [Release root](../../release/README.md) | Decision plane, not a published-payload store |
| What does the object mean? | [ReleaseManifest contract](../../contracts/release/release_manifest.md) | Semantics and current profile limits |
| What machine shape applies? | [ReleaseManifest schema](../../schemas/contracts/v1/release/release_manifest.schema.json) | Distinguish legacy and strict candidate branches |
| What was validated? | [Release validator](../../tools/validators/release/validate_release_manifest.py) and exact output | Fixture/declaration conformance is narrower than operational release |
| Where are candidates and manifests? | [Candidates](../../release/candidates/README.md) and [manifests](../../release/manifests/README.md) | A candidate or template is not an active release |
| How are states explained? | [Release State register](RELEASE_STATE.md) | Reconcile explanatory vocabulary to the current owning contract |
| Where are domain pointers? | [Fauna release index](../domains/fauna/RELEASE_INDEX.md) and [Flora release index](../domains/flora/RELEASE_INDEX.md) | Historical/proposed domain guidance needs exact-object verification |

The Flora index's current body is titled as Flora domain guidance. Treat that mismatch as an editorial verification item rather than assuming a populated release ledger exists there.

## Prepare a reviewable entry

Record the immutable release identity and manifest digest, owning domain, artifact references, intended audience, state as expressed by the owning object, observation time, source/evidence closure, rights and sensitivity support, policy/review decisions, validation scope, publication readback, and correction/rollback references.

Every affirmative claim needs the supporting record. Keep absent, unresolved, stale, synthetic and not-run evidence explicit. Do not use a GitHub merge, passing build, Site deployment or completed download as a substitute for release eligibility.

Keep this Markdown entry small enough to review. Link canonical objects instead of copying writable versions of manifests, signatures or policy decisions into the table.

## Check a claimed release

1. Pin the repository/source and exact object versions.
2. Identify whether the subject is a draft, fixture, template, candidate, actual decision record or application deployment.
3. Validate only against the profile that applies; record the command and exact result.
4. Resolve the required evidence, policy, accountable review, artifact-byte and rollback claims through their owning processes.
5. Inspect the actual consumer/publication state if that is part of the claim.
6. If any prerequisite remains unresolved, retain a hold at that transition. A successful bounded check can coexist with a release hold.
7. Add or correct the human pointer only after the stated facts are supported; preserve predecessor and correction links.

## Correction and maintenance

A stale pointer should receive a source-pinned forward correction. A withdrawn or corrected release requires its owning lifecycle records and downstream propagation; deleting a Markdown row is not withdrawal.

Re-review this guide when the projection gains real entries, the manifest profile changes, a domain index becomes an operational ledger, or publication/correction consumers change. Accountable release and review roles remain subject to verification. Restoring the prior document changes explanation only and never reverses an operational transition.
