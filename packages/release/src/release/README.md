<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-release-src-release-readme
title: packages/release/src/release/ — Python Namespace and Governed Release-Candidate Scaffold
type: readme
version: v1.1
prior_version: v1
status: draft
owners: OWNER_TBD — Release steward · Promotion steward · Rollback/correction steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Security/signing steward · Validation steward · Package steward · Runtime/API steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target file existed before this evidence-grounded revision
updated: 2026-07-19
policy_label: "public-doctrine; python-namespace; greenfield-placeholder; no-supported-api; candidate-only; fail-closed; release-authority-external; signing-key-external; no-publication-authority; correction-aware; rollback-aware"
truth_posture: >
  CONFIRMED kfm-release 0.0.0 metadata stub, empty __init__.py, comment-only core.py,
  release-governance root, draft object contracts, uneven PROPOSED schema/validator/test
  maturity, draft signing standard, proposed promotion-gate ADR, and explicit release-dry-run
  holds / PROPOSED deterministic candidate mechanics only / CONFLICTED prior fictional API,
  competing A–G gate vocabularies, and CorrectionNotice placement / UNKNOWN accepted import
  name, API, build, dependencies, signer, consumer, tests, runtime binding, and health /
  NEEDS VERIFICATION ownership, rulesets, package metadata, accepted contracts/schemas/policy,
  validators, fixtures, signing review, compatibility, correction, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 66adcd917bc77232f6eac2218849f812019631dd
  prior_blob: b9d312c0ac4bcb58d1ecb4762a718eef9d0df257
  package_metadata_blob: b50731922626e9eb12b69f62dd8e71b11f00068b
  namespace_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  namespace_core_blob: 1c98feb4fb83b956decc0f55171a732d4a3233c0
  release_manifest_schema_blob: 727db0a781900aa3816dcdce723fe355fec2e786
  promotion_decision_schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  promotion_decision_validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  promotion_decision_test_blob: 495c76aa9d3a016b7a60831e47c15d3a21efaa0c
  rollback_card_schema_blob: 779ffcf282201ba4dba9689e622f92723db55b4e
  rollback_validator_placeholder_blob: b80dd40e93733c7fa76f8f9a78e9ec55b6090b4b
  correction_notice_schema_blob: 8f260eb5a5adba0b4966adfeffebfbcf6960277d
  promotion_gate_adr_blob: d7604ab92b915abaec8d7d9bac3da5d40d51e7f3
  signing_standard_blob: b719251e5f7d0abb954da4f043f8ea5d95e6283f
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
  - ../../../../docs/architecture/release-discipline.md
  - ../../../../docs/architecture/publication/RELEASE_GATES.md
  - ../../../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../../../docs/standards/SIGNING.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../contracts/release/promotion_decision.md
  - ../../../../contracts/release/rollback_card.md
  - ../../../../contracts/correction/correction_notice.md
  - ../../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../../schemas/contracts/v1/correction/correction_notice.schema.json
  - ../../../../tools/validators/release/validate_promotion_decision.py
  - ../../../../tools/validators/validate_rollback_card.py
  - ../../../../tests/release/test_promotion_decision_schema.py
  - ../../../../release/README.md
  - ../../../../.github/workflows/release-dry-run.yml
tags: [kfm, packages, release, python, namespace, scaffold, promotion-decision, release-manifest, rollback-card, correction-notice, signing, fail-closed, rollback]
notes:
  - "v1.1 removes fictional modules/imports/exports and records the verified placeholder state."
  - "Candidate mechanics do not approve promotion, mutate release state, hold keys, persist trust artifacts, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release Python Namespace and Governed Release-Candidate Scaffold

`packages/release/src/release/`

> Future namespace for reusable release-candidate mechanics. Current evidence proves only an empty initializer and comment-only `core.py`—not an installable package, supported API, release runner, signer, rollback executor, correction publisher, ledger, or publication authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![maturity](https://img.shields.io/badge/maturity-greenfield__placeholder-lightgrey)
![distribution](https://img.shields.io/badge/distribution-kfm--release-blue)
![authority](https://img.shields.io/badge/publication__authority-none-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Authority](#authority-boundary) · [Objects](#object-readiness) · [API](#candidate-api-boundary) · [Security](#security-signing-and-side-effects) · [Testing](#testing-and-ci) · [Implementation](#implementation-sequence) · [Open](#verification-register) · [Rollback](#correction-revocation-and-rollback)

> [!IMPORTANT]
> **This README is not implementation evidence.** It establishes no imports, exports, manifest construction, promotion evaluation, signing, rollback, correction publication, receipt persistence, release mutation, tests, deployment, or operational health.

> [!CAUTION]
> A valid schema, signature, promotion decision, pull request, workflow, or copied artifact does not create evidence or publication authority and cannot silently change `PUBLISHED` state.

---

## Purpose

The namespace may eventually provide small, explicit-input, deterministic, fail-closed candidate helpers shared by governed release workflows or validators.

Confirmed current state:

- `pyproject.toml` declares only `kfm-release` `0.0.0`;
- `__init__.py` is empty;
- `core.py` is a one-line placeholder;
- no build backend, Python range, discovery, dependencies, scripts, or entry points are declared;
- no functional module, export, consumer import, namespace test lane, signer binding, release mutation, or deployment is established.

The prior README's module tree, imports, exports, and helper outcomes are design lineage—not implementation or compatibility commitments.

[Back to top](#top)

---

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Namespace | **CONFIRMED present** | Placement exists; usability is unproved. |
| Distribution | **Placeholder** | `kfm-release` `0.0.0`; no installability. |
| Code | **Empty/comment-only** | No API or behavior. |
| Consumers/tests | **Not established** | No adoption or package proof. |
| `ReleaseManifest` | **PROPOSED, thin schema** | `id` only required; release closure not enforced. |
| `PromotionDecision` | **PROPOSED, concrete schema** | Closed eleven-field shape; validator and fixture test exist. |
| `RollbackCard` | **PROPOSED, thin schema** | Declared validator absent; different validator is placeholder. |
| `CorrectionNotice` | **Draft, thin schema** | Validator absent; family placement conflicted. |
| Signing | **Draft standard** | Production keys/trust roots unproved. |
| Release dry run | **Explicit hold** | Bounded checks only; no release emitted. |
| Runtime health | **UNKNOWN** | No operational namespace. |

### v1 corrections

- Remove nonexistent `manifests.py`, `gates.py`, `signing.py`, `rollback.py`, `corrections.py`, `receipts.py`, `replay.py`, `validation.py`, and `fixtures.py`.
- Remove `from release...` examples; the accepted import name remains unresolved.
- Remove unratified `READY`, `SIGNED`, `ROLLBACK_READY`, and `DRIFT` compatibility claims.
- Do not treat dry-run or PromotionDecision fixture success as release readiness.
- Do not choose between competing draft A–G gate vocabularies while ADR-0018 remains proposed.

[Back to top](#top)

---

## Authority boundary

Directory Rules place reusable mechanics under `packages/`, one-off execution under `tools/` or `pipelines/`, and authoritative release records under `release/`.

| Responsibility | Authority |
|---|---|
| Candidate computation | This namespace after implementation |
| Package build | `packages/release/pyproject.toml` |
| Release records/state | `release/` |
| Object meaning | `contracts/release/`, `contracts/correction/` |
| Machine shape | `schemas/contracts/v1/` |
| Policy/gates/review | Policy and governed workflows |
| Evidence | EvidenceRef/EvidenceBundle surfaces |
| Receipts/proofs | `data/receipts/`, `data/proofs/` |
| Lifecycle artifacts | `data/<phase>/` |
| Keys/trust roots | Security/KMS/signing infrastructure |
| Public surfaces | Governed APIs/UI/map/AI |

This namespace must never approve, promote, publish, withdraw, revoke, set aliases, mutate release/lifecycle stores, write trust artifacts, evaluate policy as authority, resolve evidence as truth, store keys, or expose public authority.

[Back to top](#top)

---

## Object readiness

### `ReleaseManifest`

The semantic contract is rich, but its PROPOSED schema requires only `id` and permits additional properties. A future adapter may normalize explicit inputs but must not persist manifests or equate schema validity with evidence, rights, sensitivity, policy, review, attestation, receipt/proof, correction, rollback, or publication closure.

### `PromotionDecision`

The PROPOSED schema is closed, requires eleven fields, and uses:

```text
APPROVE | DENY | ABSTAIN
```

A validator and repository fixture test exist. This proves bounded shape validation—not policy evaluation, accountable review, release approval, or publication.

### `RollbackCard`

The semantic contract exists; the schema is thin. The schema-declared validator is absent, while `tools/validators/validate_rollback_card.py` raises `NotImplementedError`. Do not claim rollback validation or execute alias movement, invalidation, restoration, or notice publication.

### `CorrectionNotice`

The semantic contract exists under `contracts/correction/`; the schema is thin and its validator is absent. Release-vs-correction family placement is unresolved. Preserve append-only history and do not expose restricted correction details.

[Back to top](#top)

---

## Candidate API boundary

Future code may be admitted only when reusable, explicit-input, deterministic where promised, no-network by default, and candidate-only.

Allowed future concerns:

- normalize explicit manifest refs/digests;
- invoke injected shape validators;
- compare canonical hashes or public verification results;
- assemble explicit PromotionDecision inputs without deciding them;
- normalize rollback affected/target/invalidation metadata without executing;
- preserve correction and supersession refs without publishing;
- compare replay expectations;
- build sanitized deterministic fixtures.

Every function must receive explicit identity, artifacts, evidence, policy/review, receipt/proof, signing, rollback/correction, replay, and time context as applicable. It must not fetch missing facts from hidden globals, stores, UI state, logs, secrets, or generated prose.

### Outcome separation

| Vocabulary | Use |
|---|---|
| `APPROVE | DENY | ABSTAIN` | PromotionDecision |
| `ANSWER | ABSTAIN | DENY | ERROR` | Runtime/policy envelope |
| Release record states | `release/` governance |
| `PASS | FAIL | SKIPPED` | Validation/workflow reporting |

Unknown, stale, conflicted, or unverifiable support must fail closed. No proposed helper result may be treated as publication.

[Back to top](#top)

---

## Lifecycle and trust membrane

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The namespace may support candidate computation near governed release transitions. It does not own lifecycle state.

A release still requires validated semantics, resolvable evidence, rights/sensitivity posture, policy, accountable review, receipts/proofs, integrity support, manifest and rollback/correction lineage, authoritative release records, and governed downstream interfaces.

A file move, merge, deployment, signature, workflow success, or local helper result is not a release.

[Back to top](#top)

---

## Security, signing, and side effects

Private keys, KMS clients, OIDC credentials, certificate issuance, trust-root policy, and transparency-log authority do not belong here.

A future verifier adapter must accept explicit canonical payload and public verification context, bind digest/payload type/identity/issuer/policy, distinguish invalid/unverifiable/stale/revoked/error states, avoid leaking secrets, and fail closed.

Core candidate mechanics must be pure and no-network by default. Forbidden hidden effects include release/lifecycle store access, KMS access, source retrieval, alias mutation, cache invalidation, receipt persistence, and environment-dependent decisions.

| Threat | Control |
|---|---|
| Package becomes release ledger | No authoritative writes |
| Schema-valid but unsafe candidate | Separate shape from governance readiness |
| Gate drift | Versioned mapping; no proposed enum hard-code |
| Signature treated as truth | Integrity-only semantics |
| Key leakage | No secrets in code, fixtures, logs, exceptions |
| TOCTOU | Digest/version binding and authority-boundary reverification |
| Stale evidence/policy/review | Explicit versions and time checks |
| Rollback substitution | Digest-bound target and reviewed lineage |
| Warning-only drift | Typed fail-closed result |
| Resource exhaustion | Size, depth, count, time limits |

Logs may include safe ids, result class, reason code, timing, and version—not payloads, evidence bodies, keys, tokens, signatures, protected locations, or personal data.

[Back to top](#top)

---

## Consumer contract

The first consumer must be internal, governed, reviewable, and reversible. It must pin API version, supply explicit validated inputs, preserve all governance refs, handle every negative result, avoid release/lifecycle mutation through the package, persist authoritative objects only through release-owned workflows, add replay/rollback tests, and retain a kill switch.

Public clients must consume governed release state through approved APIs and manifests, never this namespace directly.

[Back to top](#top)

---

## Testing and CI

Minimum tests:

- intentional imports/exports and unknown export failure;
- deterministic manifest normalization;
- PromotionDecision valid/invalid shapes;
- accepted outcome mapping and unknown outcome rejection;
- hash/signature match, mismatch, stale, revoked, unverifiable, error;
- rollback target/invalidation completeness;
- correction append-only and public-summary safety;
- replay drift;
- no-network/no-store/no-KMS boundaries;
- secret/key/personal/protected-location leakage;
- oversize, depth/count, and timeout limits.

`release-dry-run.yml` currently confirms no real candidate packet, a comment-only helper, TODO Make target, thin ReleaseManifest schema without validator/fixtures, PromotionDecision shape testing only, and incomplete rollback implementation. These holds document incompleteness; they do not prove release readiness.

[Back to top](#top)

---

## Implementation sequence

1. Resolve owners, import name, gate vocabulary, and CorrectionNotice family.
2. Complete packaging and dependency policy.
3. Ratify minimal candidate types and exhaustive result mapping.
4. Implement pure normalization, canonicalization, hashing, and limits.
5. Harden ReleaseManifest, RollbackCard, and CorrectionNotice enforcement.
6. Add an injected public-key verifier after security review.
7. Add positive, negative, replay, privacy, and authority-boundary tests.
8. Integrate one governed internal consumer without release mutation.
9. Prove evidence/policy/review/receipt/proof/rollback/correction handoff.
10. Add compatibility, deprecation, correction, kill switch, and rollback drills.

No stage may claim publication because the previous stage passed.

[Back to top](#top)

---

## Verification register

| Item | Status |
|---|---|
| Owners and independent ruleset/review enforcement | NEEDS VERIFICATION |
| Import name and build/dependency policy | UNKNOWN / NEEDS VERIFICATION |
| Accepted exports/result types and first consumer | UNKNOWN |
| Parent README reconciliation | NEEDS VERIFICATION |
| ReleaseManifest hardening/validator | NEEDS VERIFICATION |
| PromotionDecision policy/review/runtime wiring | NEEDS VERIFICATION |
| RollbackCard validator/fixtures | NEEDS VERIFICATION |
| CorrectionNotice family/validator | CONFLICTED / NEEDS VERIFICATION |
| Accepted A–G gate vocabulary | CONFLICTED / NEEDS VERIFICATION |
| Canonicalization/hash profile | NEEDS VERIFICATION |
| Verifier protocol, trust roots, revocation | UNKNOWN |
| No-network, side-effect, resource, telemetry enforcement | NEEDS VERIFICATION |
| Namespace tests/CI and receipt/proof handoff | UNKNOWN / NEEDS VERIFICATION |
| Release mutation adapter and separation of duties | UNKNOWN |
| Compatibility/deprecation/changelog | NEEDS VERIFICATION |
| Correction, revocation, rollback drill | NEEDS VERIFICATION |
| Public interface integration and runtime health | UNKNOWN |

[Back to top](#top)

---

## Correction, revocation, and rollback

Any future supported API change must include versioned contract/schema mapping, changelog, migration notes, consumer impact, deprecation window, negative/replay tests, correction path, rollback target, and kill switch.

If package behavior emitted incorrect candidate metadata: stop consumers; identify affected versions/runs/releases; preserve prior records; issue governed correction/withdrawal where public state was affected; invalidate derivatives through release authority; patch or revert through review; rerun validation and rollback drills.

**Documentation rollback:** before merge, close the PR and abandon the branch. After merge, use a revert PR and preserve history. This README changes no release state, artifact, receipt, proof, signature, correction, or public surface.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Finding | Limit |
|---|---|---|
| Namespace/package | Empty init, placeholder core, `0.0.0` manifest | No behavior/installability |
| Release root | Governs release records | Lane conventions open |
| ReleaseManifest | Rich draft meaning, thin schema | No production closure |
| PromotionDecision | Concrete proposed shape and test | No authorization |
| RollbackCard | Rich meaning, thin schema | Validator incomplete |
| CorrectionNotice | Rich meaning, thin schema | Placement/validator unresolved |
| Signing/ADR | Draft/proposed | No production authority |
| Release dry run | Explicit holds | No release emitted |
| CODEOWNERS | Review routing | Not independent approval |

### Maintainer checklist

- [ ] Verify base, owners, ADRs, and object maturity.
- [ ] Keep release authority outside the package.
- [ ] Add tests before exports.
- [ ] Protect keys, sensitive data, and release payloads.
- [ ] Record compatibility, correction, revocation, and rollback impact.
- [ ] Update documentation and generated receipt.
- [ ] Require human review separate from release/publication approval.

[Back to top](#top)
