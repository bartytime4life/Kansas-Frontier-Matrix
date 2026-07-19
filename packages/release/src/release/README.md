<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-release-src-release-readme
title: packages/release/src/release/ — Python Namespace and Governed Release-Candidate Scaffold
type: readme
version: v1.1
prior_version: v1
status: draft
owners: OWNER_TBD — Release steward · Promotion steward · Rollback/correction steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Security/signing steward · Validation steward · Package steward · Runtime/API steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target existed before this evidence-grounded revision
updated: 2026-07-19
policy_label: "public-doctrine; python-namespace; greenfield-placeholder; candidate-only; fail-closed; release-authority-external; signing-key-external; no-publication-authority; correction-aware; rollback-aware"
truth_posture: >
  CONFIRMED kfm-release 0.0.0 stub, empty __init__.py, comment-only core.py, uneven
  draft/PROPOSED release-object enforcement, and explicit release-dry-run holds /
  PROPOSED deterministic candidate mechanics / CONFLICTED prior fictional API, A–G
  vocabulary, and CorrectionNotice placement / UNKNOWN accepted API/build/signer/
  consumer/tests/runtime / NEEDS VERIFICATION ownership, accepted contracts/schemas/
  policy, validators, fixtures, security, compatibility, correction, and rollback
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 66adcd917bc77232f6eac2218849f812019631dd
  prior_blob: b9d312c0ac4bcb58d1ecb4762a718eef9d0df257
  package_metadata_blob: b50731922626e9eb12b69f62dd8e71b11f00068b
  namespace_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  namespace_core_blob: 1c98feb4fb83b956decc0f55171a732d4a3233c0
  release_manifest_schema_blob: 727db0a781900aa3816dcdce723fe355fec2e786
  promotion_decision_schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  rollback_card_schema_blob: 779ffcf282201ba4dba9689e622f92723db55b4e
  correction_notice_schema_blob: 8f260eb5a5adba0b4966adfeffebfbcf6960277d
  release_dry_run_workflow_blob: c91e794ae68a99edf6b618e9e3992c30ab0e4fe5
related:
  - ../../README.md
  - ../README.md
  - ../../pyproject.toml
  - __init__.py
  - core.py
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/architecture/publication/RELEASE_GATES.md
  - ../../../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../../../docs/standards/SIGNING.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../contracts/release/promotion_decision.md
  - ../../../../contracts/release/rollback_card.md
  - ../../../../contracts/correction/correction_notice.md
  - ../../../../release/README.md
  - ../../../../.github/workflows/release-dry-run.yml
tags: [kfm, packages, release, python, namespace, scaffold, promotion-decision, release-manifest, rollback-card, correction-notice, signing, fail-closed, rollback]
notes:
  - "v1.1 removes fictional modules/imports/exports and records verified placeholder state."
  - "Candidate mechanics do not approve promotion, mutate release state, hold keys, persist trust artifacts, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release Python Namespace and Governed Release-Candidate Scaffold

`packages/release/src/release/`

> Future namespace for reusable release-candidate mechanics. Current evidence proves only an empty initializer and comment-only `core.py`—not an installable package, supported API, release runner, signer, rollback executor, correction publisher, ledger, or publication authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![maturity](https://img.shields.io/badge/maturity-greenfield__placeholder-lightgrey)
![authority](https://img.shields.io/badge/publication__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#evidence-and-maturity) · [Authority](#authority-boundary) · [Objects](#release-object-boundaries) · [API](#candidate-api-boundary) · [Security](#security-signing-and-effects) · [Testing](#testing-and-graduation) · [Open](#verification-register) · [Rollback](#correction-revocation-and-rollback)

> [!IMPORTANT]
> **This README is not implementation evidence.** It establishes no imports, exports, manifest construction, promotion evaluation, signing, rollback, correction publication, receipt persistence, release mutation, tests, deployment, or operational health.

> [!CAUTION]
> A valid schema, signature, promotion decision, pull request, workflow, or copied artifact cannot create evidence or publication authority or silently change `PUBLISHED` state.

---

## Purpose

The namespace may eventually provide small, explicit-input, deterministic, fail-closed candidate helpers shared by governed release workflows or validators.

Confirmed state:

- `pyproject.toml` declares only `kfm-release` `0.0.0`;
- `__init__.py` is empty and `core.py` is a one-line placeholder;
- no build backend, Python range, discovery, dependency, script, entry point, module, export, consumer, package test, signer binding, release mutation, or deployment is established.

The prior module tree, `from release...` examples, exports, and `READY`/`SIGNED`-style outcomes are design lineage—not implementation or compatibility commitments.

[Back to top](#top)

---

## Evidence and maturity

| Surface | Verified state | Limit |
|---|---|---|
| Namespace/package | Present, `0.0.0`, empty/comment-only code | No installability or behavior |
| `ReleaseManifest` | Rich draft contract; PROPOSED id-only permissive schema | No release closure |
| `PromotionDecision` | PROPOSED closed eleven-field schema; validator/test | Shape only, not authorization |
| `RollbackCard` | Rich draft contract; thin schema | Declared validator absent; other validator placeholder |
| `CorrectionNotice` | Draft contract; thin schema | Validator absent; placement conflicted |
| Signing | Draft standard | Keys/trust roots unproved |
| Release dry run | Explicit holds | No candidate or release emitted |
| Runtime | Not established | No health claim |

Do not choose between competing draft A–G gate vocabularies while ADR-0018 remains proposed.

[Back to top](#top)

---

## Authority boundary

Reusable candidate mechanics may live under `packages/`; one-off execution under `tools/` or `pipelines/`; authoritative release records under `release/`.

| Concern | Authority |
|---|---|
| Candidate computation | This namespace after implementation |
| Release records/state | `release/` |
| Meaning/shape | `contracts/`; `schemas/contracts/v1/` |
| Policy/gates/review | Policy and governed workflows |
| Evidence | EvidenceRef/EvidenceBundle surfaces |
| Receipts/proofs | `data/receipts/`; `data/proofs/` |
| Lifecycle artifacts | `data/<phase>/` |
| Keys/trust roots | Security/KMS/signing infrastructure |
| Public surfaces | Governed APIs/UI/map/AI |

This namespace must never approve, promote, publish, withdraw, revoke, set aliases, mutate release/lifecycle stores, write trust artifacts, evaluate policy as authority, resolve evidence as truth, store keys, or expose public authority.

[Back to top](#top)

---

## Release object boundaries

### `ReleaseManifest`

Its PROPOSED schema requires only `id` and permits extra fields. A future adapter may normalize explicit refs/digests, but must not persist manifests or equate schema validity with evidence, rights, sensitivity, policy, review, attestation, receipts/proofs, correction, rollback, or publication closure.

### `PromotionDecision`

Its PROPOSED schema is closed, requires eleven fields, and uses `APPROVE | DENY | ABSTAIN`. A validator and fixture test prove bounded shape validation—not policy evaluation, accountable review, release approval, or publication.

### `RollbackCard`

The schema is thin; its declared validator is absent, while a different validator raises `NotImplementedError`. Do not claim rollback validation or execute alias movement, invalidation, restoration, or notice publication.

### `CorrectionNotice`

The contract lives under `contracts/correction/`; its schema is thin and validator absent. Release-vs-correction placement is unresolved. Preserve append-only history and do not expose restricted correction details.

[Back to top](#top)

---

## Candidate API boundary

Future code must be reusable, explicit-input, deterministic where promised, no-network by default, and candidate-only.

Allowed mechanics:

- normalize explicit manifest refs/digests;
- invoke injected shape validators;
- compare canonical hashes or public verification results;
- assemble PromotionDecision inputs without deciding them;
- normalize rollback target/invalidation metadata without executing;
- preserve correction/supersession refs without publishing;
- compare replay expectations;
- build sanitized deterministic fixtures.

Every function receives explicit identity, artifact, evidence, policy/review, receipt/proof, signing, rollback/correction, replay, and time context as applicable. It must not fetch missing facts from stores, UI state, logs, secrets, or generated prose.

| Vocabulary | Use |
|---|---|
| `APPROVE | DENY | ABSTAIN` | PromotionDecision |
| `ANSWER | ABSTAIN | DENY | ERROR` | Runtime/policy envelope |
| Release record states | `release/` governance |
| `PASS | FAIL | SKIPPED` | Validation/workflow reporting |

Unknown, stale, conflicted, or unverifiable support fails closed. No helper result is publication.

[Back to top](#top)

---

## Lifecycle and trust membrane

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This namespace may assist candidate computation; it does not own lifecycle state. Release still requires validated semantics, resolvable evidence, rights/sensitivity posture, policy, accountable review, receipts/proofs, integrity, manifest and rollback/correction lineage, authoritative release records, and governed downstream interfaces.

A file move, merge, deployment, signature, workflow success, or local helper result is not a release.

[Back to top](#top)

---

## Security, signing, and effects

Private keys, KMS clients, OIDC credentials, certificate issuance, trust-root policy, and transparency-log authority do not belong here.

A future verifier accepts explicit canonical payload and public verification context; binds digest, payload type, identity, issuer, and policy; distinguishes invalid, unverifiable, stale, revoked, and error states; avoids secret leakage; and fails closed.

Core mechanics are pure and no-network by default. Forbidden hidden effects include release/lifecycle store access, KMS access, source retrieval, alias mutation, cache invalidation, receipt persistence, and environment-dependent decisions.

| Threat | Control |
|---|---|
| Package becomes release ledger | No authoritative writes |
| Schema-valid but unsafe | Separate shape from governance readiness |
| Gate drift | Versioned mapping; no proposed enum hard-code |
| Signature treated as truth | Integrity-only semantics |
| Key leakage | No secrets in code, fixtures, logs, exceptions |
| TOCTOU/stale support | Digest/version/time binding and reverification |
| Rollback substitution | Digest-bound target and reviewed lineage |
| Resource exhaustion | Size, depth, count, time limits |

Logs may include safe ids, result class, reason code, timing, and version—not payloads, evidence bodies, keys, tokens, signatures, protected locations, or personal data.

[Back to top](#top)

---

## Consumer contract

The first consumer must be internal, governed, reviewable, and reversible. It pins API version, supplies explicit validated inputs, preserves governance refs, handles all negative results, avoids release/lifecycle mutation through the package, persists authoritative objects only through release-owned workflows, adds replay/rollback tests, and retains a kill switch.

Public clients consume governed release state through approved APIs and manifests, never this namespace directly.

[Back to top](#top)

---

## Testing and graduation

Minimum tests cover imports/exports, deterministic normalization, PromotionDecision valid/invalid shapes, exhaustive outcome mapping, hash/signature mismatch/stale/revoked/error paths, rollback completeness, correction append-only safety, replay drift, no-network/no-store/no-KMS boundaries, secret/protected-data leakage, and resource limits.

The current dry-run workflow confirms explicit holds: no real candidate packet, comment-only helper, TODO Make target, thin ReleaseManifest enforcement, PromotionDecision shape testing only, and incomplete rollback support. These holds document incompleteness; they do not prove release readiness.

Graduation sequence:

1. resolve owners, import name, gate vocabulary, and CorrectionNotice family;
2. complete packaging and dependency policy;
3. ratify candidate types and exhaustive result mapping;
4. implement pure normalization, canonicalization, hashes, and limits;
5. harden ReleaseManifest, RollbackCard, and CorrectionNotice enforcement;
6. add an injected public-key verifier after security review;
7. add positive, negative, replay, privacy, and authority tests;
8. integrate one governed consumer without release mutation;
9. prove governance handoff;
10. add compatibility, correction, kill switch, and rollback drills.

[Back to top](#top)

---

## Verification register

| Item | Status |
|---|---|
| Owners, rulesets, import name, build/dependencies | NEEDS VERIFICATION / UNKNOWN |
| Accepted exports/results and first consumer | UNKNOWN |
| Parent README reconciliation | NEEDS VERIFICATION |
| ReleaseManifest hardening/validator | NEEDS VERIFICATION |
| PromotionDecision policy/review/runtime wiring | NEEDS VERIFICATION |
| RollbackCard validator/fixtures | NEEDS VERIFICATION |
| CorrectionNotice family/validator | CONFLICTED / NEEDS VERIFICATION |
| Accepted A–G vocabulary | CONFLICTED / NEEDS VERIFICATION |
| Canonicalization, verifier, trust roots, revocation | NEEDS VERIFICATION / UNKNOWN |
| Effects, resources, telemetry, package CI | NEEDS VERIFICATION / UNKNOWN |
| Receipt/proof handoff and release mutation separation | NEEDS VERIFICATION / UNKNOWN |
| Compatibility, correction, revocation, rollback drill | NEEDS VERIFICATION |
| Public integration and runtime health | UNKNOWN |

[Back to top](#top)

---

## Correction, revocation, and rollback

Any future API change needs versioned contract/schema mapping, changelog, migration notes, consumer impact, deprecation window, negative/replay tests, correction path, rollback target, and kill switch.

If package behavior emitted incorrect candidate metadata: stop consumers; identify affected versions/runs/releases; preserve prior records; issue governed correction/withdrawal when public state was affected; invalidate derivatives through release authority; patch or revert through review; rerun validation and rollback drills.

**Documentation rollback:** before merge, close the PR and abandon the branch. After merge, use a revert PR and preserve history. This README changes no release state, artifact, receipt, proof, signature, correction, or public surface.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Finding | Limit |
|---|---|---|
| Namespace/package | Empty init, placeholder core, `0.0.0` | No behavior/installability |
| ReleaseManifest | Rich meaning, thin schema | No production closure |
| PromotionDecision | Concrete proposed shape/test | No authorization |
| RollbackCard | Rich meaning, thin schema | Validator incomplete |
| CorrectionNotice | Rich meaning, thin schema | Placement/validator unresolved |
| Signing/ADR | Draft/proposed | No production authority |
| Release dry run | Explicit holds | No release emitted |
| CODEOWNERS | Review routing | Not independent approval |

### Maintainer checklist

- [ ] Keep release authority outside the package.
- [ ] Add tests before exports.
- [ ] Protect keys, sensitive data, and release payloads.
- [ ] Record compatibility, correction, revocation, and rollback impact.
- [ ] Update docs and generated receipt.
- [ ] Require human review separate from release/publication approval.

[Back to top](#top)
