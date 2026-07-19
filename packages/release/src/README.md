<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-release-src-readme
title: packages/release/src/ — Python Source Envelope and Governed Release-Candidate Boundary
type: readme
version: v1.1
prior_version: v1
status: draft
owners: OWNER_TBD — Release steward · Promotion steward · Rollback/correction steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Security/signing steward · Validation steward · Package steward · Runtime/API steward · CI steward · Docs steward
created: NEEDS VERIFICATION — target file existed before this evidence-grounded revision
updated: 2026-07-19
policy_label: "public-doctrine; package-source-boundary; python-source-envelope; greenfield-placeholder; no-supported-api; explicit-inputs; no-hidden-fetches; no-network-by-default; deterministic-candidate-mechanics; fail-closed; release-authority-external; signing-key-external; receipt-proof-external; no-publication-authority; correction-aware; rollback-aware"
current_path: packages/release/src/README.md
truth_posture: >
  CONFIRMED target README v1, repository-present packages/release/src source envelope,
  merged child namespace README v1.1, kfm-release distribution metadata version 0.0.0,
  empty release/__init__.py, comment-only release/core.py greenfield placeholder,
  packages responsibility-root doctrine, authoritative release-governance root, draft
  ReleaseManifest, PromotionDecision, RollbackCard, and CorrectionNotice contracts,
  uneven PROPOSED schema/validator/test maturity, draft signing standard, proposed
  promotion-gate ADR, and explicit release-dry-run holds / PROPOSED a small reusable
  Python source envelope for deterministic candidate normalization, injected validation,
  public verification result handling, replay-safe comparison, and sanitized test support /
  CONFLICTED prior README implications that proposed modules, imports, and custom helper
  outcomes were usable implementation; competing draft A–G gate vocabularies;
  CorrectionNotice release-vs-correction family placement / UNKNOWN accepted import name,
  public API, build backend, Python support, package discovery, dependencies, source-module
  decomposition, signer integration, first consumer, package-local test home, CI enforcement,
  deployment, operational health, and release use / NEEDS VERIFICATION owners, package
  metadata completion, API approval, contract/schema/policy acceptance, validators,
  fixtures, security review, compatibility policy, correction process, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 7af75ca2b7c3bfe75325e41f4fbfca664bfcd7fd
  prior_blob: 38f2122cec30f2194ccd5b8ffdcabdafeb52ab44
  package_readme_blob: e0f2aad3f3b1e70b15bd1f1b410c60852c9d41dd
  package_metadata_blob: b50731922626e9eb12b69f62dd8e71b11f00068b
  namespace_readme_blob: 1fc83f7549c1258da3f121ba3b364db9877ca333
  namespace_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  namespace_core_blob: 1c98feb4fb83b956decc0f55171a732d4a3233c0
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  release_root_blob: 089c4a394c5cbf3b9e5a2a1963e68e16be485dce
  release_manifest_contract_blob: 9ca1c9d4a5b247196aa84a31a158fe734c8a6720
  release_manifest_schema_blob: 727db0a781900aa3816dcdce723fe355fec2e786
  promotion_decision_contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  promotion_decision_schema_blob: a2d087a46772cf60e4b9dfb394892690e8a88b31
  promotion_decision_validator_blob: ead33d6c5c073f319627ee42d99c5933c0e370d1
  promotion_decision_test_blob: 495c76aa9d3a016b7a60831e47c15d3a21efaa0c
  rollback_card_contract_blob: 72ab9e148491243cc8a374556350ab94c2557ab4
  rollback_card_schema_blob: 779ffcf282201ba4dba9689e622f92723db55b4e
  rollback_validator_placeholder_blob: b80dd40e93733c7fa76f8f9a78e9ec55b6090b4b
  correction_notice_contract_blob: 4716f2bc6e714ad2ab873d95144417d7855f5beb
  correction_notice_schema_blob: 8f260eb5a5adba0b4966adfeffebfbcf6960277d
  promotion_gate_adr_blob: d7604ab92b915abaec8d7d9bac3da5d40d51e7f3
  signing_standard_blob: b719251e5f7d0abb954da4f043f8ea5d95e6283f
  release_dry_run_workflow_blob: c91e794ae68a99edf6b618e9e3992c30ab0e4fe5
  bounded_path_checks:
    - packages/release/src/README.md existed at version v1 before this revision
    - packages/release/pyproject.toml declares only project name kfm-release and version 0.0.0
    - package metadata declares no build system, Python requirement, package discovery, dependencies, scripts, entry points, license, authors, or test configuration
    - packages/release/src/release/README.md exists at version v1.1 on main
    - packages/release/src/release/__init__.py is empty
    - packages/release/src/release/core.py is a comment-only greenfield placeholder
    - bounded repository search surfaced no functional release namespace consumer import or package-local test reference
    - PromotionDecision has a concrete PROPOSED schema, validator, and repository fixture test
    - ReleaseManifest, RollbackCard, and CorrectionNotice enforcement remains thin, incomplete, or conflicted
    - release-dry-run workflow explicitly emits holds and no release or publication artifact
related:
  - ../README.md
  - ../pyproject.toml
  - release/README.md
  - release/__init__.py
  - release/core.py
  - ../../README.md
  - ../../../pyproject.toml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/trust-membrane.md
  - ../../../docs/doctrine/lifecycle-law.md
  - ../../../docs/architecture/release-discipline.md
  - ../../../docs/architecture/publication/RELEASE_GATES.md
  - ../../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../../docs/standards/SIGNING.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/release/rollback_card.md
  - ../../../contracts/correction/correction_notice.md
  - ../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../schemas/contracts/v1/correction/correction_notice.schema.json
  - ../../../tools/validators/release/validate_promotion_decision.py
  - ../../../tools/validators/validate_rollback_card.py
  - ../../../tests/release/test_promotion_decision_schema.py
  - ../../../release/README.md
  - ../../../.github/workflows/release-dry-run.yml
  - ../../../data/receipts/generated/README.md
  - ../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, packages, release, src, python, source-envelope, scaffold, release-candidate, promotion-decision, release-manifest, rollback-card, correction-notice, signing, fail-closed, compatibility, correction, rollback]
notes:
  - "v1.1 replaces proposed source modules, imports, and custom helper outcomes with the directly verified source inventory and delegates namespace/API detail to release/README.md."
  - "This README governs what may enter packages/release/src; it does not install the package, establish a supported API, accept a release-gate vocabulary, implement release mechanics, hold signing keys, write trust artifacts, mutate release state, authorize publication, or prove operational safety."
  - "The source envelope remains a greenfield placeholder at the recorded evidence snapshot."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release Python Source Envelope and Governed Release-Candidate Boundary

`packages/release/src/`

> Source-placement and governance boundary for a future reusable Python release-support library. Current evidence establishes one evidence-grounded child namespace README, an empty package initializer, and a comment-only `core.py` placeholder—not an installable distribution, supported API, release runner, policy evaluator, signer, rollback executor, correction publisher, receipt writer, release ledger, or publication authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v1.1-informational)
![maturity](https://img.shields.io/badge/maturity-greenfield__placeholder-lightgrey)
![root](https://img.shields.io/badge/root-packages-blue)
![namespace](https://img.shields.io/badge/namespace-release-blue)
![exports](https://img.shields.io/badge/exports-none-orange)
![tests](https://img.shields.io/badge/tests-not__established-orange)
![authority](https://img.shields.io/badge/publication__authority-none-red)

**Quick links:** [Purpose](#purpose-and-audience) · [Evidence](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-source-inventory) · [Layers](#package-source-and-namespace-layers) · [Packaging](#packaging-import-api-and-ownership-status) · [Admission](#source-admission-rules) · [Allowed files](#allowed-source-file-classes) · [Exclusions](#explicit-non-responsibilities) · [Objects](#release-object-maturity-boundary) · [Inputs](#input-and-semantic-completeness-boundary) · [Outputs](#candidate-output-and-persistence-boundary) · [Outcomes](#outcome-vocabularies-and-fail-closed-behavior) · [Lifecycle](#lifecycle-and-trust-membrane) · [Dependencies](#dependency-direction) · [Effects](#side-effects-network-and-determinism) · [Security](#security-signing-and-key-custody) · [Replay](#identity-hashing-replay-and-freshness) · [Telemetry](#logging-telemetry-and-error-hygiene) · [Consumers](#consumer-runtime-and-public-surface-contract) · [Testing](#testing-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Drift](#drift-and-conflicts) · [Maintenance](#maintenance-and-change-review) · [Compatibility](#versioning-compatibility-deprecation-and-correction) · [Evidence ledger](#evidence-ledger) · [Rollback](#rollback)

> [!IMPORTANT]
> **This README is not implementation evidence.** It does not establish installation, import success, exports, accepted release objects, gate behavior, signing, rollback, correction publication, receipt/proof persistence, release mutation, consumers, tests, CI enforcement, deployment, or operational health.

> [!CAUTION]
> **Release-support code is not release authority.** A schema-valid candidate, signature, PromotionDecision, workflow result, pull request, merge, copied artifact, or generated summary cannot create evidence, satisfy release closure, or silently change `PUBLISHED` state.

---

## Purpose and audience

This README governs source placement under:

```text
packages/release/src/
```

It is written for:

- package implementers deciding what source code may enter the package;
- release, promotion, rollback, correction, policy, evidence, rights, sensitivity, privacy, security, and signing reviewers;
- contract, schema, validator, fixture, test, and CI maintainers;
- pipeline, worker, validator, runtime, governed API, map, export, and review-console consumers;
- receipt, proof, release, correction, rollback, compatibility, and documentation stewards.

The intended future role is a **small reusable source envelope** for deterministic candidate mechanics shared by more than one governed caller.

The current role is narrower:

- this README exists;
- `release/README.md` is merged at v1.1;
- `release/__init__.py` is empty;
- `release/core.py` is a comment-only placeholder;
- `../pyproject.toml` declares only `kfm-release` version `0.0.0`;
- no build backend, Python support policy, package discovery, dependency set, script, or entry point is established;
- no functional module, supported export, consumer import, package-local test suite, signer binding, release mutation, deployment, or runtime behavior was established by bounded inspection;
- the release-object, signing, and promotion-gate surfaces have uneven draft or PROPOSED maturity.

This README therefore records the **CONFIRMED placeholder state**, defines **PROPOSED source-admission rules**, and keeps release authority, contracts, schemas, policy, evidence, validation, signing, receipts, proofs, review, correction, and rollback visible before adoption.

[Back to top](#top)

---

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| Target README | **CONFIRMED v1 before revision** | The prior source guide over-described implementation. |
| Source envelope | **CONFIRMED present** | `packages/release/src/` exists. |
| Child namespace README | **CONFIRMED v1.1** | The namespace boundary is current and evidence-grounded. |
| Subpackage metadata | **CONFIRMED placeholder** | `kfm-release`, version `0.0.0`. |
| Subpackage build/discovery | **NOT DECLARED** | Build, install, and import are unproved. |
| `release/__init__.py` | **CONFIRMED empty** | No supported exports. |
| `release/core.py` | **CONFIRMED comment-only** | No release-support behavior. |
| Functional source modules | **NOT ESTABLISHED by bounded inspection** | Prior proposed module names are not facts. |
| Consumer imports | **NOT ESTABLISHED by bounded search** | No package adoption or integration behavior is proved. |
| Package-local tests | **NOT ESTABLISHED by bounded search** | No source behavior is proved. |
| `ReleaseManifest` | **DRAFT / PROPOSED / thin schema** | Rich semantics exist; machine closure is not enforced. |
| `PromotionDecision` | **DRAFT / PROPOSED / concrete schema** | Shape validator and fixture test exist; authorization is not proved. |
| `RollbackCard` | **DRAFT / PROPOSED / thin schema** | Schema-declared validator is absent; another validator is placeholder-only. |
| `CorrectionNotice` | **DRAFT / thin schema / placement conflicted** | Validator and canonical family remain unresolved. |
| Signing standard | **DRAFT** | Production key custody, trust roots, and verification binding are unproved. |
| Promotion-gate ADR | **PROPOSED** | Competing draft A–G vocabularies remain unresolved. |
| Release dry run | **CONFIRMED explicit hold** | Bounded checks run; no candidate, release, or publication artifact is emitted. |
| Runtime health | **UNKNOWN** | No operational package is proved. |

### Corrections from v1

| Prior implication | Current evidence | v1.1 correction |
|---|---|---|
| Source root and namespace were only proposed | Both paths exist | Mark placement CONFIRMED. |
| Proposed modules are expected implementation | Only README, empty initializer, and placeholder core surfaced | Remove fictional module tree. |
| `from release...` examples are usable | Build/import support is absent; import name may collide | Remove import examples and keep namespace decision open. |
| Custom helper outcomes are package contracts | No runtime type exists; KFM vocabularies differ by object family | Require accepted mapping before export. |
| Broad callers use the package | No functional consumer import surfaced | Consumer set remains UNKNOWN. |
| Release gate names are settled | ADR-0018 remains proposed and draft docs conflict | Do not encode gate vocabulary as API. |
| Signing verification can be local helper behavior | Keys, trust roots, verifier protocol, and revocation are unproved | Limit future code to injected public verification context after review. |
| Checklist prose indicates readiness | No package behavior exists | Add staged gates, definition of done, and verification register. |

Open items must not be upgraded to implementation facts without new repository evidence.

[Back to top](#top)

---

## Directory Rules and authority

Directory Rules state that placement encodes ownership and governance. The source path remains appropriate because `packages/` owns shared reusable libraries.

| Path or responsibility | Owning root | Rule |
|---|---|---|
| Package metadata and reusable implementation | `packages/release/` | Package boundary and build metadata. |
| Python source admission | `packages/release/src/` | This README. |
| Namespace/API design | `packages/release/src/release/` | Child namespace README and reviewed source. |
| Authoritative release records | `release/` | Release governance, decisions, manifests, corrections, rollback, signatures, and history. |
| Semantic meaning | `contracts/` | Object meaning. |
| Machine shape | `schemas/contracts/v1/` | JSON Schema and machine contracts. |
| Policy and admissibility | `policy/` | Release, promotion, rights, sensitivity, and access decisions. |
| Evidence authority | EvidenceRef/EvidenceBundle homes | Evidence closure. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Auditable trust artifacts. |
| Lifecycle artifacts | `data/<phase>/` | RAW through PUBLISHED state. |
| One-off release execution | `tools/`, `pipelines/`, or accepted runtime lanes | Operational orchestration, not shared source. |
| Keys and trust roots | Security/KMS/signing infrastructure | Private key custody and issuer policy. |
| Public delivery | Governed API/UI/map/AI roots | Downstream released surfaces only. |

No path is moved or renamed by this revision. No parallel release, contract, schema, policy, source, registry, receipt, proof, signing, or publication authority is created. No ADR is required for this documentation-only in-place correction.

[Back to top](#top)

---

## Confirmed source inventory

Bounded direct reads and repository search surfaced:

```text
packages/release/src/
├── README.md
└── release/
    ├── README.md
    ├── __init__.py
    └── core.py
```

| Path | Verified state | Safe interpretation |
|---|---|---|
| `README.md` | This source-envelope guide | Documentation only. |
| `release/README.md` | v1.1 namespace boundary | Design and governance, not implementation proof. |
| `release/__init__.py` | Empty | No exports. |
| `release/core.py` | Comment-only greenfield placeholder | No behavior. |

No additional functional release-source module, supported export, test module, or consumer import surfaced in the bounded inspection. This is not a claim that no hidden or future branch content exists.

[Back to top](#top)

---

## Package, source, and namespace layers

The three documentation layers are complementary.

| Layer | Owns | Must not duplicate |
|---|---|---|
| `../README.md` | Package purpose, packaging, adoption, compatibility, and package-level rollback | Source-file admission or detailed API semantics |
| This README | Source-root admission, dependency direction, side-effect rules, source-level testing burden | Package installation promises or namespace exports |
| `release/README.md` | Namespace concepts, candidate API boundary, object maturity, consumer contract | Package build policy or source-root placement doctrine |

The package README remains v1 and overstates current implementation. This source revision does not silently rewrite it; parent reconciliation is recorded as a separate verification item.

[Back to top](#top)

---

## Packaging, import, API, and ownership status

The subpackage manifest currently declares only:

```toml
[project]
name = "kfm-release"
version = "0.0.0"
```

It does not establish:

- a build backend;
- supported Python versions;
- source-layout discovery;
- dependencies or optional dependencies;
- scripts or entry points;
- package data;
- typing support;
- license, authors, or maintainers;
- test, lint, formatting, or type-check configuration;
- the accepted import name;
- a supported API or compatibility promise.

The source tree must not add API-bearing code until package metadata and ownership are reviewed together.

### Import-name risk

`release` is generic and collision-prone. The current directory name does not prove that `import release` is accepted. Before consumer adoption, maintainers must decide whether to:

- retain `release`;
- use a project-qualified namespace such as `kfm_release`;
- nest under another accepted package;
- or choose another reviewed convention.

That decision belongs in package metadata and, if compatibility or architecture significance warrants, an ADR or migration note.

### Ownership minimum

Before functional code lands, identify:

- package steward;
- release and promotion stewards;
- contract/schema/policy owners;
- security/signing reviewer;
- validation and CI owner;
- first consumer owner;
- correction and rollback owner;
- compatibility/deprecation owner.

CODEOWNERS routing alone is not independent approval or release authorization.

[Back to top](#top)

---

## Source-admission rules

A source file may enter this envelope only when all applicable rules are satisfied.

1. **Reusable responsibility.** More than one governed caller needs the mechanics, or a clear shared-library reason is documented.
2. **Explicit inputs.** The file does not discover authority from hidden globals, environment state, current working directory, mutable aliases, UI state, logs, or operator memory.
3. **Candidate-only behavior.** It may compute or validate candidates; it does not approve or persist authoritative release state.
4. **No hidden fetches.** Network, database, object-store, KMS, source-system, and lifecycle-store access are excluded from the deterministic core.
5. **Determinism.** Deterministic claims are backed by canonicalization rules and tests.
6. **Fail closed.** Unknown, stale, conflicted, invalid, unsupported, or unverifiable inputs produce explicit non-success results.
7. **Authority separation.** Contracts, schemas, policy, evidence, review, receipts, proofs, release records, and key custody remain external.
8. **Safe telemetry.** Logs and exceptions do not leak payloads, keys, tokens, evidence bodies, protected locations, or personal data.
9. **Bounded resources.** Size, count, nesting, algorithmic complexity, memory, and time limits are explicit.
10. **Test-first burden.** Positive, negative, replay, privacy, authority-boundary, and resource-limit tests accompany behavior.
11. **Compatibility discipline.** API, object-version, and result-vocabulary changes carry migration and rollback.
12. **Documentation parity.** Package, source, namespace, contracts, schemas, policy, tests, workflows, and runbooks are updated together where behavior changes.

README prose, file presence, or a merged PR does not satisfy these gates.

[Back to top](#top)

---

## Allowed source-file classes

The source envelope may eventually contain reviewed files in these responsibility classes.

| Class | Permitted purpose | Required boundary |
|---|---|---|
| Candidate data carriers | Typed immutable input/result candidates | No authoritative release records |
| Manifest normalization | Normalize explicit refs, versions, digests, and metadata | No persistence or closure claim |
| Shape-validation adapters | Call injected accepted validators | Schema validity is not release readiness |
| Promotion input assembly | Assemble explicit `PromotionDecision` inputs | Must not decide `APPROVE`, `DENY`, or `ABSTAIN` |
| Public verification adapters | Normalize explicit public-key verification results | No private-key, KMS, issuer, or trust-root authority |
| Rollback metadata normalization | Normalize affected state, target, invalidation, restoration refs | No alias movement or rollback execution |
| Correction lineage helpers | Preserve correction, withdrawal, supersession, and revocation refs | No notice publication or silent mutation |
| Canonicalization and hashing adapters | Apply accepted deterministic profiles | No ad hoc hash authority |
| Replay and drift comparison | Compare expected and observed explicit state | No certification or warning-only drift |
| Reason and obligation carriers | Preserve accepted safe codes and obligations | No policy evaluation |
| Synthetic test builders | Build deterministic sanitized examples | No production or sensitive payloads |

Concrete module names remain **PROPOSED** until the accepted API and decomposition are reviewed. Do not recreate the v1 fictional tree as empty files merely to satisfy documentation.

[Back to top](#top)

---

## Explicit non-responsibilities

Do not place these responsibilities in `packages/release/src/`.

| Excluded responsibility | Correct authority |
|---|---|
| Release approval, denial, abstention, withdrawal, correction approval | Governed policy/release workflow |
| Authoritative manifests, decisions, rollback cards, notices, signatures, release records | `release/` |
| Contract meaning | `contracts/` |
| JSON Schemas and API schemas | `schemas/` |
| Policy logic or bundle activation | `policy/` |
| Evidence resolution or evidence truth | Evidence subsystem |
| Receipt/proof storage | `data/receipts/`, `data/proofs/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED payloads | `data/<phase>/` |
| Source retrieval | `connectors/` or governed pipeline inputs |
| Release execution, publication, alias movement, cache invalidation | Release-owned tooling/pipelines/runtime |
| Private keys, KMS clients, OIDC credentials, issuer policy, trust roots | Security/signing infrastructure |
| Public API routes, UI, map rendering, AI answer generation | Governed downstream apps |
| Real release payloads, protected coordinates, personal/DNA data, secrets | Never in package source or fixtures |

The package may preserve safe references to external authority objects. A reference carrier does not inherit the authority of the referenced object.

[Back to top](#top)

---

## Release-object maturity boundary

### `ReleaseManifest`

The semantic contract describes a rich release binding. The paired PROPOSED schema currently requires only `id` and permits additional properties.

Source code may eventually normalize explicit manifest candidate fields, but it must not:

- persist a manifest;
- treat schema validity as release closure;
- infer evidence, rights, sensitivity, policy, review, signature, receipt/proof, correction, or rollback completion;
- publish or activate a release;
- replace the authoritative release record.

### `PromotionDecision`

The PROPOSED schema is materially more concrete. It requires eleven fields, rejects additional properties, and uses:

```text
APPROVE | DENY | ABSTAIN
```

A repository validator and fixture test exist. This proves bounded **shape validation** only.

Source code must not equate validation with:

- policy evaluation;
- EvidenceBundle closure;
- accountable human review;
- rollback readiness beyond supplied refs;
- release approval;
- publication.

A future helper may assemble or validate explicit candidate inputs. The decision itself remains external.

### `RollbackCard`

The semantic contract is rich, while the paired schema is thin. The schema-declared validator path is absent, and a different validator is a `NotImplementedError` placeholder.

Source code must not claim rollback validation or execute:

- alias/current-pointer mutation;
- cache, tile, graph, vector, search, API, map, or AI-cache invalidation;
- restoration;
- release withdrawal;
- correction notice publication;
- history erasure.

### `CorrectionNotice`

The semantic contract currently lives under `contracts/correction/`. Its paired schema is thin, its declared validator is absent, and the release-vs-correction family placement remains conflicted.

Source code may preserve explicit lineage candidates only. It must not:

- choose the canonical family;
- silently replace prior records;
- expose restricted correction details;
- publish a notice;
- authorize correction or withdrawal.

### Signing and attestations

The signing standard is draft. Production signer identity, trust roots, key custody, issuer policy, transparency-log requirements, media types, revocation, and verification protocol are not established here.

The source envelope may eventually contain an adapter that consumes explicit public verification context. It must never hold or retrieve private signing material.

[Back to top](#top)

---

## Input and semantic-completeness boundary

Future functions must receive explicit, inspectable inputs.

| Input family | Examples | Required posture |
|---|---|---|
| Identity | candidate id, release id, object version, spec hash, canonicalization profile | Stable and versioned |
| Artifact | explicit artifact refs, digests, media types, sizes, manifest refs | Refs only; no hidden reads |
| Evidence | EvidenceRef, EvidenceBundle ref, resolver status, freshness | Preserve; do not fabricate or resolve as truth |
| Policy/review | PolicyDecision ref, PromotionDecision candidate, obligations, reviewer/ticket refs | External authority |
| Rights/sensitivity | license, audience, redistribution, embargo, redaction/generalization posture | Unknown fails closed |
| Receipts/proofs | run, validation, redaction, promotion, generated receipt, proof refs | Preserve; do not persist |
| Signing | canonical payload digest, payload type, public identity, issuer, verification result, trust-policy version | Public verification context only |
| Rollback/correction | affected release, target, invalidation, restoration, correction, withdrawal, supersession refs | Candidate metadata only |
| Replay/freshness | expected hashes, versions, prior state, evaluated/published/valid time | Explicit comparison |
| Limits | maximum bytes, fields, artifacts, nesting, runtime | Enforced before expensive work |

### Semantic completeness is not schema validity

A candidate can pass a permissive schema and still be release-incomplete.

The source layer must distinguish:

- machine shape;
- semantic completeness;
- evidence closure;
- policy admissibility;
- review completion;
- signature integrity;
- release authorization;
- publication state.

When required support is absent, the function must return an explicit bounded failure or abstention result defined by an accepted contract. It must not invent defaults that imply release readiness.

[Back to top](#top)

---

## Candidate output and persistence boundary

Allowed future outputs are **candidates** or **local validation/comparison results**.

A candidate output may contain:

- normalized safe fields;
- explicit source object refs;
- accepted reason codes;
- validation findings;
- deterministic hashes;
- replay differences;
- required follow-up obligations;
- safe diagnostic metadata.

It must not contain or imply:

- authoritative release state;
- public publication permission;
- stored receipt/proof identity that was not actually persisted;
- signer or reviewer approval;
- evidence closure that was not resolved;
- policy outcome that was not evaluated;
- successful rollback or correction execution;
- mutable `current` alias state;
- secrets or restricted payloads.

Persistence belongs to release-owned workflows and trust-artifact stores after their own validation, policy, review, integrity, and rollback gates.

[Back to top](#top)

---

## Outcome vocabularies and fail-closed behavior

Do not collapse distinct object-family vocabularies.

| Vocabulary | Current use | Source-layer rule |
|---|---|---|
| `APPROVE | DENY | ABSTAIN` | `PromotionDecision` | Preserve only after external decision or validated candidate input |
| `ANSWER | ABSTAIN | DENY | ERROR` | Runtime/policy envelopes | Do not invent package-specific substitutes |
| `PASS | FAIL | SKIPPED` | Validation/workflow reporting | Report bounded checks, not release state |
| `DRAFT | HELD | APPROVED | RELEASED | CORRECTED | SUPERSEDED | WITHDRAWN` and related states | Release governance records | Never emit as authority from local helper logic |
| Proposed `READY`, `SIGNED`, `ROLLBACK_READY`, `DRIFT` | Prior README design lineage | Not compatibility commitments |

Before exporting a result type:

1. identify its authoritative contract;
2. pin version and enum;
3. define exhaustive mapping;
4. reject unknown values;
5. preserve safe reason codes and obligations;
6. test every negative path;
7. document consumer behavior;
8. define correction and migration rules.

Unknown, stale, conflicted, unsupported, unverifiable, revoked, or malformed inputs fail closed. Warning-only continuation is not acceptable where public or release safety is affected.

[Back to top](#top)

---

## Lifecycle and trust membrane

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The source envelope may support deterministic candidate computation near a governed transition. It does not own any lifecycle phase or transition.

A valid release still requires, as applicable:

- stable identity and content digests;
- accepted contracts and schemas;
- resolvable evidence;
- rights and sensitivity closure;
- policy evaluation;
- accountable review and separation of duties;
- receipts and proofs;
- signing/integrity support;
- ReleaseManifest and PromotionDecision linkage;
- rollback and correction lineage;
- authoritative release records;
- governed downstream interfaces.

Public clients and normal UI/map/AI surfaces must never call this source tree as an authority or read pre-publication stores through it.

[Back to top](#top)

---

## Dependency direction

Preferred dependency direction:

```text
explicit accepted input objects
        |
        v
pure candidate normalization / comparison
        |
        v
local candidate result
        |
        v
external schema + semantic + policy + evidence + review + signing gates
        |
        v
release-owned persistence and governed publication
```

The source tree may depend on small accepted shared utilities when responsibility is clear, such as deterministic identity, hashing, canonicalization, or typed contract carriers.

It must not import:

- connectors;
- source clients;
- release record writers;
- policy engines as hidden authority;
- receipt/proof stores;
- public API routers;
- UI/map components;
- model providers;
- credential or private-key stores;
- mutable lifecycle repositories.

Adapters that cross an authority boundary belong outside the deterministic core and require explicit interfaces, limits, tests, and review.

[Back to top](#top)

---

## Side effects, network, and determinism

### No-network default

Production source code is no-network by default.

Any future networked verification adapter requires:

- an accepted ADR or equivalent architecture decision;
- explicit endpoint and trust policy;
- timeout, retry, circuit-breaker, and response-size limits;
- deterministic cache and freshness semantics;
- no credential leakage;
- offline/replay fixtures;
- fail-closed handling;
- audit-safe telemetry.

### Forbidden hidden side effects

Core functions must not:

- read or write release/lifecycle stores;
- call KMS or signing services;
- mutate aliases;
- invalidate caches or derivatives;
- persist receipts/proofs;
- inspect environment variables for decision authority;
- use wall-clock time or randomness without explicit injection;
- depend on file ordering, locale, timezone, or current working directory;
- make release decisions from logs or filenames.

### Deterministic claims

A deterministic result must pin:

- canonicalization profile and version;
- hash algorithm;
- input version and digest;
- policy/review/signing context versions where included;
- explicit timestamp semantics;
- randomness/nonce rules;
- sorting and serialization rules;
- resource-limit profile.

Same accepted input under the same pinned profile must produce byte-equivalent canonical output or an explicitly documented equivalent.

[Back to top](#top)

---

## Security, signing, and key custody

Private keys, KMS clients, OIDC credentials, certificate issuance, issuer policy, trust-root policy, and transparency-log authority remain outside this source tree.

A future public-verification adapter must:

- accept canonical payload bytes or digest explicitly;
- accept payload type and object-family version explicitly;
- accept public identity, issuer, trust-policy version, and revocation context explicitly;
- bind the verification result to the exact payload digest;
- distinguish valid, invalid, unverifiable, stale, revoked, unsupported, and error states;
- avoid network access in the deterministic core;
- avoid exposing signatures or certificates where policy restricts them;
- never treat a valid signature as factual truth, legal admissibility, evidence closure, or release approval.

### Threat model

| Threat | Required control |
|---|---|
| Package becomes release ledger | No authoritative writes |
| Schema-valid but unsafe candidate | Separate shape validation from governance readiness |
| Gate-vocabulary drift | Versioned mappings; no proposed enum hard-coding |
| Signature treated as truth | Integrity-only semantics |
| Key/token leakage | No secrets in source, fixtures, logs, or exceptions |
| TOCTOU between check and release | Digest, version, authority, and time binding; reverify at persistence boundary |
| Stale evidence/policy/review | Explicit freshness and version checks |
| Rollback-target substitution | Digest-bound target and reviewed lineage |
| Warning-only drift | Typed fail-closed result |
| Dependency or parser attack | Minimal dependencies, locked versions, size/depth/count limits |
| Sensitive payload leakage | Reference-only design and safe telemetry |

[Back to top](#top)

---

## Identity, hashing, replay, and freshness

Identity and hash fields are not decorative.

Future candidate mechanics must preserve:

- object/candidate id;
- object family and version;
- canonicalization profile;
- input and output digests;
- referenced artifact digests;
- expected and observed versions;
- policy, evidence, review, receipt/proof, signing, rollback, and correction refs;
- explicit time kinds.

Replay must distinguish:

- exact match;
- semantically equivalent under an accepted profile;
- changed input;
- changed profile;
- changed dependency;
- changed policy/review/signing context;
- stale support;
- unverifiable prior state;
- unsupported legacy state;
- error.

A replay comparison is not certification. Release-owned governance decides what drift means for continued service, correction, withdrawal, or rollback.

[Back to top](#top)

---

## Logging, telemetry, and error hygiene

Allowed telemetry may include:

- safe candidate or run id;
- object family/version;
- result class;
- safe reason code;
- duration and bounded resource counts;
- canonicalization/hash/verifier profile version;
- caller component id where approved;
- correlation id that reveals no sensitive data.

Do not log:

- release payloads;
- evidence bodies;
- private or unreleased artifact content;
- keys, tokens, credentials, certificates where restricted;
- full signatures;
- protected coordinates;
- personal or genomic data;
- policy inputs containing restricted details;
- stack traces containing secrets or payloads.

Errors must be typed, safe, exhaustive, and separable from successful candidate results. Never convert an internal exception into a permissive release candidate.

[Back to top](#top)

---

## Consumer, runtime, and public-surface contract

The first consumer must be:

- internal;
- governed;
- reviewable;
- reversible;
- narrow enough to disable safely.

It must:

1. pin package/API/object versions;
2. supply explicit validated inputs;
3. preserve all evidence, policy, review, receipt/proof, signing, rollback, and correction refs;
4. handle every negative and unknown result;
5. avoid release/lifecycle mutation through the package;
6. persist authoritative objects only through release-owned workflows;
7. reverify authority-bound context before persistence;
8. add replay, correction, revocation, and rollback tests;
9. expose a kill switch;
10. document compatibility and operational ownership.

Public clients consume governed released state through approved APIs and release manifests. They must never import this package as release authority.

[Back to top](#top)

---

## Testing, fixtures, and CI

### Minimum test matrix

| Test family | Minimum burden |
|---|---|
| Import boundary | Intentional imports succeed only after packaging; unknown exports fail |
| Empty-state guard | Placeholder package cannot appear operational |
| Candidate normalization | Stable input produces stable canonical output |
| ReleaseManifest | Current thin schema and governance-incomplete cases remain distinct |
| PromotionDecision | Valid and invalid shapes; eleven required fields; closed properties |
| Outcome mapping | Exhaustive accepted values; unknown value rejection |
| Evidence | Missing, unresolved, stale, conflicted refs fail closed |
| Rights/sensitivity | Unknown or restricted posture blocks unsafe candidate |
| Policy/review | Missing or stale policy/reviewer/ticket context fails closed |
| Signing | Match, mismatch, wrong payload type, stale, revoked, unverifiable, unsupported, error |
| Rollback | Missing affected state, target, invalidation, restoration, correction lineage |
| Correction | Append-only history, supersession, withdrawal, public-summary safety |
| Replay | Input, profile, dependency, policy, signing, and time drift |
| Side effects | No network, store, KMS, alias, cache, receipt/proof writes |
| Privacy | No secrets, keys, personal/DNA data, protected coordinates in logs/errors |
| Resource bounds | Oversize, count, nesting, parser, memory, and timeout limits |
| Compatibility | Old/new API and object versions; deprecation and migration |
| Consumer | First integration handles every finite outcome and kill switch |
| Authority | Helper cannot publish, approve, persist, or mutate lifecycle state |

Fixtures must be deterministic, synthetic, sanitized, public-safe, and stored in an accepted fixture root—not hidden beside production source by default.

### Current workflow boundary

The current `release-dry-run.yml` confirms explicit holds:

- no real candidate packet payload;
- comment-only release helper;
- TODO-only Make target;
- thin ReleaseManifest schema with no declared validator/fixtures;
- PromotionDecision shape testing only;
- incomplete rollback support;
- no candidate, decision, receipt, proof, manifest, rollback action, release, or publication artifact emitted.

A successful dry-run workflow proves the documented hold behavior, not release readiness.

[Back to top](#top)

---

## Smallest sound implementation sequence

### Gate 0 — governance and naming

Resolve owners, CODEOWNERS/rulesets, import name, package build policy, accepted gate vocabulary, CorrectionNotice family, and first consumer.

### Gate 1 — package metadata

Add reviewed build backend, Python support, discovery, dependency policy, licensing, authorship, typing, and test configuration.

### Gate 2 — accepted candidate contracts

Ratify minimal input/result types, object versions, reason codes, and exhaustive outcome mapping. Do not invent package-specific release states.

### Gate 3 — pure deterministic core

Implement normalization, canonicalization, hashing, comparison, and resource limits without network or authoritative writes.

### Gate 4 — object enforcement

Harden ReleaseManifest, RollbackCard, and CorrectionNotice schemas/validators/fixtures and keep PromotionDecision shape enforcement aligned.

### Gate 5 — signing verification adapter

After security review, add an injected public verification adapter with explicit trust policy, revocation, limits, and negative tests.

### Gate 6 — first governed consumer

Integrate one internal consumer that cannot mutate release state through the package and has a kill switch.

### Gate 7 — governance handoff proof

Prove evidence, policy, review, receipts/proofs, signing, release persistence, correction, revocation, and rollback separation.

### Gate 8 — compatibility and operations

Add changelog, migration, deprecation, correction, rollback drills, observability, incident response, and operational ownership.

No stage may claim publication because the previous stage passed.

[Back to top](#top)

---

## Definition of done

The source envelope is not done until all applicable conditions are verified.

- [ ] Owners and independent review controls are assigned.
- [ ] Import name and package build are accepted.
- [ ] Supported Python versions and dependencies are pinned.
- [ ] Public API and object/result versions are ratified.
- [ ] Contracts, schemas, policy, validators, and fixtures agree.
- [ ] Functional source exists and contains no hidden authority.
- [ ] Determinism and canonicalization are executable and tested.
- [ ] Network and side-effect boundaries are enforced.
- [ ] Signing verifier protocol and key custody are security-reviewed.
- [ ] Positive, negative, replay, privacy, resource, and authority tests pass.
- [ ] First consumer is governed, reversible, and kill-switch protected.
- [ ] Receipt/proof and release persistence remain external.
- [ ] Correction, revocation, supersession, withdrawal, and rollback paths are tested.
- [ ] Compatibility, migration, deprecation, and changelog policy are active.
- [ ] CI enforces package behavior without false-green placeholders.
- [ ] Operational health is observed rather than inferred.
- [ ] Human review is complete.
- [ ] Release/publication approval remains a separate act.

[Back to top](#top)

---

## Verification register

| # | Question | Status |
|---:|---|---|
| 1 | Who owns package/source/namespace review? | NEEDS VERIFICATION |
| 2 | Are branch rules and independent review enforced for `packages/release/`? | UNKNOWN |
| 3 | Is `release` the accepted import name? | UNKNOWN |
| 4 | Which build backend and Python versions are accepted? | UNKNOWN |
| 5 | How is package discovery configured? | UNKNOWN |
| 6 | Which runtime and development dependencies are approved? | UNKNOWN |
| 7 | What is the accepted public API/version? | UNKNOWN |
| 8 | Where do package-local tests and fixtures belong? | NEEDS VERIFICATION |
| 9 | Which first governed consumer justifies the package? | UNKNOWN |
| 10 | When will the parent package README be reconciled? | NEEDS VERIFICATION |
| 11 | Which ReleaseManifest fields are required for production closure? | NEEDS VERIFICATION |
| 12 | Where is the accepted ReleaseManifest validator and fixture set? | NEEDS VERIFICATION |
| 13 | How is PromotionDecision connected to policy and accountable review? | NEEDS VERIFICATION |
| 14 | Where is the schema-declared RollbackCard validator? | NEEDS VERIFICATION |
| 15 | Which rollback fields and invalidation targets are mandatory? | NEEDS VERIFICATION |
| 16 | Is CorrectionNotice canonical under correction, release, or compatibility paths? | CONFLICTED / NEEDS VERIFICATION |
| 17 | Where is the accepted CorrectionNotice validator? | NEEDS VERIFICATION |
| 18 | Which A–G gate vocabulary is accepted? | CONFLICTED / NEEDS VERIFICATION |
| 19 | What canonicalization and hash profile is authoritative? | NEEDS VERIFICATION |
| 20 | Which result/reason-code contract will the package export? | UNKNOWN |
| 21 | What verifier protocol, trust roots, issuers, and media types are accepted? | UNKNOWN |
| 22 | How are revocation, stale signatures, and transparency logs handled? | UNKNOWN |
| 23 | Are no-network/no-store/no-KMS rules mechanically enforced? | NEEDS VERIFICATION |
| 24 | What resource-limit profile is accepted? | NEEDS VERIFICATION |
| 25 | What telemetry fields and retention policy are allowed? | NEEDS VERIFICATION |
| 26 | How are EvidenceRef/EvidenceBundle freshness and conflicts represented? | NEEDS VERIFICATION |
| 27 | How are policy/review decisions rebound at persistence time? | NEEDS VERIFICATION |
| 28 | Which receipts/proofs are required for each candidate family? | NEEDS VERIFICATION |
| 29 | How is release mutation kept outside package consumers? | NEEDS VERIFICATION |
| 30 | What compatibility and deprecation policy applies? | NEEDS VERIFICATION |
| 31 | What correction and revocation process applies to package defects? | NEEDS VERIFICATION |
| 32 | Has a rollback drill exercised package and consumer reversal? | NEEDS VERIFICATION |
| 33 | Which CI checks are required and non-vacuous? | UNKNOWN |
| 34 | Is the package deployed or imported anywhere operationally? | UNKNOWN |
| 35 | What is current runtime health? | UNKNOWN |

[Back to top](#top)

---

## Drift and conflicts

### Parent package documentation drift

`../README.md` remains v1 and still lists proposed modules, imports, and helper outcomes. This README and the child namespace README classify those claims as design lineage, not implementation.

Resolution should be a separate scoped revision of the package README so review remains inspectable.

### Gate-vocabulary conflict

`docs/architecture/publication/RELEASE_GATES.md` and proposed ADR-0018 describe different A–G mappings. This source tree must not freeze either mapping into code until the accepted authority resolves the conflict.

### Correction family conflict

CorrectionNotice appears in correction-family authority while release documentation also references it. This source tree must preserve refs without choosing a canonical family.

### Validator-path drift

RollbackCard and CorrectionNotice schema-declared validators are absent or do not match the placeholder validator that exists elsewhere. Source code must not compensate by inventing private validation semantics.

[Back to top](#top)

---

## Maintenance and change review

Any material source change should review:

- package and namespace documentation;
- package metadata;
- contracts and schemas;
- policy and review requirements;
- validator and fixture coverage;
- signing/key-custody implications;
- consumer compatibility;
- CI and runbooks;
- receipts/proofs and release persistence boundaries;
- correction, revocation, withdrawal, and rollback impact;
- security, privacy, rights, sensitivity, and public-surface exposure;
- generated-work receipt and human-review status.

### Change classes

| Change | Minimum review |
|---|---|
| Documentation-only clarification | Docs + responsible package/release steward |
| New internal source file | Package + architecture + tests |
| New export or result type | Contract/schema + package + consumers + compatibility |
| New dependency | Package + supply-chain/security + CI |
| Networked verifier | Security/signing + architecture/ADR + operations |
| Release-object semantic change | Contract/schema/policy/release + migration |
| Signing/trust policy change | Security/signing + policy + release + rollback |
| Consumer integration | Consumer owner + package + release authority + tests |
| Breaking change | Migration, deprecation, correction, rollback, and release review |

Generation, review, merge, signing, release, and publication remain separate duties.

[Back to top](#top)

---

## Versioning, compatibility, deprecation, and correction

A supported API change must include:

- API and object-version mapping;
- contract/schema/policy impact;
- consumer inventory and migration notes;
- compatibility tests;
- changelog entry;
- deprecation window;
- correction and revocation path;
- rollback target and kill switch;
- operational ownership;
- documentation and generated receipt updates.

### Package defect response

If implemented package behavior emits incorrect candidate metadata:

1. stop or disable affected consumers;
2. identify affected package versions, runs, candidates, releases, and public derivatives;
3. preserve prior records and evidence;
4. issue governed correction, withdrawal, or revocation where public state was affected;
5. invalidate derivatives through release authority;
6. patch or revert through reviewed change control;
7. rerun validation, replay, security, correction, and rollback drills;
8. document impact and supersession.

Do not silently rewrite release records or prior generated receipts.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Finding | Limitation |
|---|---|---|
| Target README v1 | Proposed source tree and API claims | Not implementation proof |
| Package metadata | `kfm-release` `0.0.0` only | No build/install/import support |
| Source inventory | README, child README, empty init, placeholder core | Bounded inspection, not universal absence proof |
| Child namespace README v1.1 | Current evidence-grounded API boundary | Still documentation, not code |
| Parent package README v1 | Package intent | Stale relative to child/source evidence |
| Release root | Governs release records | Lane conventions remain open |
| ReleaseManifest contract/schema | Rich meaning, thin shape | No production closure |
| PromotionDecision contract/schema/test | Concrete proposed shape and fixture validation | No policy/review/release authorization |
| RollbackCard contract/schema/validator | Rich meaning, thin shape, placeholder validator | No rollback readiness |
| CorrectionNotice contract/schema | Rich meaning, thin shape | Placement/validator unresolved |
| Signing standard | Draft signing model | No production key/trust authority |
| ADR-0018 | Proposed gate sequence | Not accepted |
| Release dry-run workflow | Explicitly verifies holds and bounded shape tests | No candidate or release emitted |
| Directory Rules | `packages/` is shared-library root | Does not prove package necessity |
| CODEOWNERS | Review routing | Not independent approval |

[Back to top](#top)

---

## Rollback

### Before merge

Close the draft pull request and abandon the scoped branch.

### After merge

Use a revert pull request. Preserve shared history and the generated receipt as review evidence.

### Behavioral rollback

This documentation revision changes no Python behavior, package metadata, release object, policy, schema, validator, fixture, test, workflow, signer, receipt/proof instance, release record, lifecycle artifact, public surface, or deployment.

If future source violates authority boundaries, rollback must:

- disable consumers;
- revert or supersede the package version;
- preserve affected records;
- route correction/withdrawal through release authority;
- revoke or distrust affected signatures where applicable;
- invalidate public derivatives through governed release processes;
- rerun replay and rollback tests.

No merge, release, signing, or publication authority is granted by this README.

[Back to top](#top)
