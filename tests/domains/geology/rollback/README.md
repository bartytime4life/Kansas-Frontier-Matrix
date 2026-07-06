<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-rollback-readme
title: Tests — Geology Rollback
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED test matrix / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <release-steward> + <rollback-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - docs/runbooks/ROLLBACK_RUNBOOK.md
  - docs/domains/geology/RELEASE_INDEX.md
  - docs/domains/geology/SENSITIVITY.md
  - data/rollback/geology/README.md
  - data/published/geology/README.md
  - data/catalog/domain/geology/README.md
  - data/proofs/geology/README.md
  - data/receipts/geology/README.md
  - release/README.md
  - release/manifests/README.md
  - tests/domains/geology/catalog-closure/README.md
  - tests/domains/geology/public-safe-geometry/README.md
  - tests/domains/geology/governed-ai/README.md
  - fixtures/domains/geology/
tags:
  - kfm
  - tests
  - geology
  - rollback
  - correction-notice
  - rollback-card
  - release-manifest
  - derivative-invalidation
  - stale-state
  - governed-release
  - fail-closed
notes:
  - "This README governs the rollback test lane under tests/domains/geology/rollback/."
  - "It documents intended Geology rollback test coverage; it does not claim that all tests already exist."
  - "Rollback is a governed state transition, not deletion, erasure, silent edit, or hidden file copy."
  - "Tests should prove release-plane rollback decisions, data-plane revert support, derivative invalidation, stale-state markers, and public-surface withdrawal behavior without using live services."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Rollback

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fgeology%2Frollback-blue?style=flat-square)
![posture](https://img.shields.io/badge/posture-governed__rollback-critical?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20PROPOSED%20matrix-lightgrey?style=flat-square)

> **Purpose.** This folder is the Geology-domain test lane for rollback behavior. It proves that a failed or superseded Geology release can be withdrawn, marked stale, corrected, invalidated, and restored to a prior safe release through governed release paths instead of hidden file changes.

---

## 1. Placement and authority

`tests/domains/geology/rollback/` is a domain-specific test lane. It belongs under `tests/` because its primary responsibility is to prove Geology rollback rules are enforceable.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/geology/` |
| Test lane | `rollback/` |
| Primary runbook | `docs/runbooks/geology/PROMOTION_RUNBOOK.md` |
| Data-plane rollback lane | `data/rollback/geology/` |
| Release authority | `release/` |
| Fixture counterpart | `fixtures/domains/geology/` |
| Adjacent catalog lane | `tests/domains/geology/catalog-closure/` |
| Adjacent geometry lane | `tests/domains/geology/public-safe-geometry/` |
| Adjacent AI lane | `tests/domains/geology/governed-ai/` |
| Current implementation status | README path exists; executable tests, fixtures, validators, rollback harnesses, and CI wiring remain `UNKNOWN` until verified. |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific proof lanes under `tests/domains/<domain>/`. This lane tests rollback behavior; it must not become a release authority, data rollback store, fixture home, proof store, receipt store, catalog store, policy home, or implementation package.

---

## 2. What this lane must prove

| Test area | Required behavior | Expected failure posture |
|---|---|---|
| Rollback target | A release has a resolvable prior safe release or explicit first-release rollback posture. | `ROLLBACK_TARGET_MISSING` or hold. |
| Release manifest linkage | Rollback references the active `ReleaseManifest` and restored release manifest. | `RELEASE_MANIFEST_INVALID` or hold. |
| RollbackCard | Rollback decision is recorded as a governed release-plane artifact. | `ROLLBACK_CARD_MISSING` or hold. |
| CorrectionNotice | Rollback emits or references a correction/withdrawal notice explaining what changed. | `CORRECTION_NOTICE_MISSING` or hold. |
| Digest verification | Active and prior artifact digests match their manifests before rollback. | `ROLLBACK_DIGEST_MISMATCH` or error. |
| Derivative invalidation | Tiles, exports, catalog projections, drawer payloads, AI receipts, reports, and graph artifacts tied to the failed release are invalidated or marked stale. | `DERIVATIVES_UNRESOLVED` or hold. |
| Public surface withdrawal | Governed API, map, drawer, Focus Mode, and story/export surfaces no longer serve failed release content. | Public edge denied or test fail. |
| Audit preservation | Failed release records remain inspectable; rollback is not deletion or erasure. | `ROLLBACK_AUDIT_GAP` or fail. |
| Source-role and claim-class preservation | Rollback does not collapse geology source roles or claim classes while restoring prior state. | `ROLE_COLLAPSE` or `CLAIM_CLASS_COLLAPSE`. |
| Sensitivity and rights posture | Rollback handles restricted or rights-limited material fail-closed. | `SENSITIVITY_UNRESOLVED`, `RIGHTS_UNKNOWN`, or hold. |
| Stale-state markers | Prior and failed releases carry visible stale/withdrawn/superseded state as appropriate. | `STALE_STATE_MISSING` or fail. |
| Finite outcomes | Rollback returns bounded outcomes and reason codes; no silent empty success. | Structured fail. |

---

## 3. Expected test families

This folder should eventually contain focused rollback tests, not one broad release simulation.

```text
tests/domains/geology/rollback/
├── README.md
├── test_rollback_target_required.py         # PROPOSED
├── test_release_manifest_linkage.py         # PROPOSED
├── test_rollback_card_required.py           # PROPOSED
├── test_correction_notice_required.py       # PROPOSED
├── test_digest_verification.py              # PROPOSED
├── test_derivative_invalidation.py          # PROPOSED
├── test_public_surface_withdrawal.py        # PROPOSED
├── test_audit_preservation.py               # PROPOSED
├── test_source_role_claim_class_preserved.py # PROPOSED
├── test_sensitivity_rights_rollback.py      # PROPOSED
├── test_stale_state_markers.py              # PROPOSED
├── test_finite_rollback_outcomes.py         # PROPOSED
└── conftest.py                              # PROPOSED, only if shared fixtures are needed
```

If executable module names use underscores, keep Python filenames with underscores while preserving this requested `rollback/` directory path unless a repository-wide naming migration says otherwise.

---

## 4. Fixture expectations

Tests in this lane should be no-network by default. They should use synthetic release manifests, rollback cards, correction notices, derivative indexes, public-surface payloads, and digest manifests.

Recommended fixture groups:

```text
fixtures/domains/geology/rollback/
├── valid/
│   ├── rollback_to_prior_safe_release.json
│   ├── correction_notice_with_derivatives.json
│   ├── stale_state_marked_release.json
│   ├── public_surface_withdrawn.json
│   └── rollback_preserves_audit_lineage.json
├── invalid/
│   ├── rollback_target_missing.json
│   ├── release_manifest_missing.json
│   ├── rollback_card_missing.json
│   ├── correction_notice_missing.json
│   ├── digest_mismatch.json
│   ├── derivatives_not_invalidated.json
│   ├── public_surface_still_serves_failed_release.json
│   ├── failed_release_deleted.json
│   ├── source_role_collapsed_on_restore.json
│   └── empty_success_without_outcome.json
└── golden/
    ├── geology_rollback_minimal.json
    └── geology_rollback_negative_outcomes.json
```

Fixture rules:

- Use synthetic release IDs, artifact IDs, digests, public-surface payloads, and derivative indexes.
- Do not include restricted real-world coordinates, private operational details, credentials, source payloads, or live service responses.
- Invalid fixtures should fail for one primary rollback reason where practical.
- Golden fixtures should make release lineage, rollback target, derivative invalidation, stale state, and audit preservation easy to inspect.

---

## 5. Rollback outcome vocabulary

The vocabulary below is a proposed testing vocabulary, not a new runtime contract.

| Outcome | Meaning in Geology rollback tests | Example trigger |
|---|---|---|
| `ROLLBACK_READY` | Required release, correction, target, digest, and derivative checks pass. | Prior safe release identified and verified. |
| `ROLLBACK_APPLIED` | Data-plane/public-surface state reflects the approved rollback decision. | Current alias points back to prior safe release. |
| `HOLD` | Required review, target, correction, digest, or derivative evidence is missing. | RollbackCard missing. |
| `DENY` | Requested rollback would violate policy, sensitivity, rights, or trust membrane. | Restore target not safe. |
| `ERROR` | Integrity or resolver failure prevents safe rollback decision. | Digest mismatch or malformed manifest. |
| `STALE` | Release remains visible only as stale/superseded/withdrawn history. | Prior failed release kept for audit. |

---

## 6. Minimal acceptance matrix

A first useful implementation of this lane should include at least these no-network checks:

| ID | Scenario | Given | Then |
|---|---|---|---|
| `GEOL-ROLL-001` | Valid rollback passes. | Active release, prior safe release, RollbackCard, CorrectionNotice, digests, and derivative index. | Rollback validation passes. |
| `GEOL-ROLL-002` | Missing rollback target fails. | ReleaseManifest lacks previous release or rollback plan. | Hold with target failure. |
| `GEOL-ROLL-003` | Missing RollbackCard fails. | Data-plane revert support exists but no release-plane rollback decision. | Hold with card failure. |
| `GEOL-ROLL-004` | Missing CorrectionNotice fails. | Rollback does not explain changed/invalidated public claims. | Hold with correction failure. |
| `GEOL-ROLL-005` | Digest mismatch fails. | Restored artifact digest differs from prior manifest. | Error or hold. |
| `GEOL-ROLL-006` | Derivatives must invalidate. | Tiles/exports/catalog/drawer/AI fixtures remain linked to failed release. | Hold or fail. |
| `GEOL-ROLL-007` | Public surface must withdraw failed release. | Governed public payload still serves failed release. | Test fails. |
| `GEOL-ROLL-008` | Failed release cannot be deleted. | Rollback fixture removes prior failed release audit records. | Test fails. |
| `GEOL-ROLL-009` | Role/class preserved on restore. | Restored release collapses source role or claim class. | Test fails closed. |
| `GEOL-ROLL-010` | Empty success forbidden. | Rollback harness returns success without outcome/reason. | Test fails. |

---

## 7. Surfaces under test

Rollback tests should verify both release-plane authority and data/public-surface effects.

| Surface | What the test should verify |
|---|---|
| Release manifest | Has rollback block, prior target, correction path, and artifact digests. |
| RollbackCard | Names decision, target, affected release, reason, reviewer, and rollback scope. |
| CorrectionNotice | Lists invalidated derivatives and public claim changes. |
| Data rollback lane | Holds only data-plane support, not release authority. |
| Catalog/proof lanes | Preserve EvidenceBundle, catalog, and proof lineage. |
| Public API/map/drawer | No longer serves the failed release as current. |
| Governed AI | Cannot cite rolled-back content as current truth. |
| Reports/exports | Carry stale, withdrawn, or superseded state if retained. |

---

## 8. Non-goals

This folder must not:

- store release manifests, rollback cards, correction notices, data-plane rollback artifacts, proofs, receipts, fixtures, schemas, policies, or package code;
- call live source, map, API, cache, tile, model, or release services by default;
- perform real rollback operations;
- delete prior releases or treat rollback as erasure;
- silently edit old ReleaseManifests, EvidenceBundles, proofs, or catalog records;
- bypass release authority, review state, correction path, derivative invalidation, or rollback target;
- treat documentation as proof of rollback implementation; or
- silently convert `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, missing artifact, missing target, missing digest, or missing correction notice into a passing response.

---

## 9. Review checklist

Before adding or changing tests in this lane, confirm:

- [ ] The test is deterministic and no-network.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] ReleaseManifest, rollback target, RollbackCard, and CorrectionNotice expectations are explicit.
- [ ] Digests and artifact identities are checked.
- [ ] Failed release history remains inspectable.
- [ ] Derivatives are invalidated or marked stale.
- [ ] Public surfaces no longer expose the failed release as current.
- [ ] Governed AI cannot cite rolled-back material as current.
- [ ] Source role, claim class, sensitivity, rights, and cross-lane boundaries are preserved.
- [ ] Failure emits finite reason codes rather than silent success.

---

## 10. Current implementation note

This lane is documentation-first. The target README existed as an empty placeholder before this update. The Geology promotion runbook defines rollback and correction procedures, and `data/rollback/geology/README.md` describes a data-plane rollback support lane. This README does not prove that executable rollback tests, fixtures, validators, rollback harnesses, or CI wiring already exist.

---

## 11. Definition of done

This README becomes implementation-backed when:

- at least the `GEOL-ROLL-001` through `GEOL-ROLL-010` scenarios exist as executable tests;
- fixtures exist under the repository's approved Geology fixture home and use synthetic release/derivative identities;
- tests verify ReleaseManifest rollback blocks, RollbackCard, CorrectionNotice, digest validation, derivative invalidation, stale state, and public-surface withdrawal;
- tests prove failed release records remain inspectable rather than deleted;
- governed AI and Evidence Drawer fixtures cannot cite rolled-back content as current truth;
- source-role, claim-class, sensitivity, rights, and cross-lane boundaries remain intact during rollback; and
- CI runs this lane without network access or real rollback side effects.
