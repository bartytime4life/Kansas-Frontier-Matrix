<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-rollback-readiness
title: Hydrology Rollback Readiness Companion
type: operational-readiness-companion
version: v2.1.0
status: DRAFT_REPOSITORY_GROUNDED; PRIMARY_PROCEDURE_SEPARATE; GENERIC_SYNTHETIC_REHEARSAL_AVAILABLE; HYDROLOGY_SPECIFIC_REHEARSAL_ABSENT; OPERATIONAL_ROLLBACK_HELD; NOT_FOR_LIFE_SAFETY; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hydrology, source, evidence, policy, correction, rollback, release, operations, and public-surface stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; hydrology; rollback-readiness; correction-aware; synthetic-proof-bounded; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
current_path: docs/runbooks/hydrology/ROLLBACK.md
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
responsibility: "Provide a compact Hydrology rollback-readiness snapshot, decision boundary, validation entry point, and accountable handoff index while the detailed procedure remains in ROLLBACK_RUNBOOK.md."
authority_effect: none
source_activation_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0ba766bde4be5338c0523b1d19b9b845720faa77
  target_path: docs/runbooks/hydrology/ROLLBACK.md
  target_prior_main_blob: 38814958fe9209be59ba35a62f486b50ee6cbd5a
  original_scaffold_blob: 4ec794c5bad3b13368de88b8b258c10b9972cb1b
  primary_runbook_path: docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md
  primary_runbook_blob: 5ea7b9c922f7a39ab80663af9700996b9ba160d1
  rollback_card_contract: contracts/release/rollback_card.md
  rollback_card_schema: schemas/contracts/v1/release/rollback_card.schema.json
  rollback_card_validator: tools/validators/release/validate_rollback_card.py
  generic_synthetic_helper: tools/release/rollback_apply.py
  generic_synthetic_tests: tests/release/test_synthetic_rollback_rehearsal.py
  readiness_workflow: .github/workflows/rollback-drill.yml
  hydrology_workflow: .github/workflows/domain-hydrology.yml
  tracked_hydrology_candidate_payloads: 0
  tracked_hydrology_published_payloads: 0
  hydrology_specific_rollback_rehearsal: ABSENT
  production_rollback_pipeline: PLACEHOLDER
  published_alias_auditor: PLACEHOLDER
source_lineage:
  - title: KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf
    source_class: PLANNING_LINEAGE
    use: Hydrology-first, HUC12, source-role, temporal, evidence, correction, and rollback framing only; its no-repository assumptions do not describe current implementation
  - title: KFM Alignment Register — 2026-08-23
    source_class: NOTION_COORDINATION_ONLY
    use: preserve validation, review, merge, rollback authorization, execution, release, deployment, promotion, and publication as separate states
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and focused draft-pull-request delivery
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../architecture/publication/ROLLBACK.md
  - ../ROLLBACK_RUNBOOK.md
  - ROLLBACK_RUNBOOK.md
  - PROMOTION_RUNBOOK.md
  - NO_NETWORK_TEST_RUNBOOK.md
  - VALIDATION.md
  - ../../domains/hydrology/README.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../fixtures/release/rollback_card/
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tests/release/test_synthetic_rollback_rehearsal.py
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../.github/workflows/domain-hydrology.yml
  - ../../../release/candidates/hydrology/README.md
  - ../../../data/published/hydrology/README.md
  - ../../../policy/domains/hydrology/README.md
notes:
  - This path began as an unversioned proposal scaffold and briefly expanded into a second full procedure while ROLLBACK_RUNBOOK.md was modernized concurrently.
  - Version 2.1 narrows this file to a readiness companion so the two paths do not remain parallel operational authorities.
  - ROLLBACK_RUNBOOK.md owns the detailed classification, preflight, synthetic rehearsal, review-handoff, invalidation, and graduation procedure.
  - The shared RollbackCard profile proves candidate shape and bounded local consistency only; authority, policy, review, execution, public mutation, and release remain separate.
  - The hosted readiness workflow runs generic and Hazards rehearsal tests, not a Hydrology-specific rollback rehearsal.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology Rollback Readiness Companion

> **One-line purpose.** Provide a compact, repository-grounded checkpoint for Hydrology rollback readiness and route maintainers to the detailed procedure without mutating public state or treating synthetic rehearsal as production rollback.

[![Primary procedure](https://img.shields.io/badge/primary%20procedure-ROLLBACK__RUNBOOK.md-0969da?style=flat-square)](ROLLBACK_RUNBOOK.md)
[![Operational rollback](https://img.shields.io/badge/operational%20rollback-HOLD-b42318?style=flat-square)](#current-disposition)
[![Hydrology drill](https://img.shields.io/badge/Hydrology%20drill-ABSENT-6e7781?style=flat-square)](#current-repository-evidence)
[![Public effect](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-document-relationship)

> [!CAUTION]
> **KFM Hydrology is not an emergency-alerting, flood-warning, navigation, engineering, insurance, permitting, dam-safety, or regulatory-determination system.** This page does not retrieve current water conditions or authorize official warnings, protective instructions, or public recovery. Refer urgent and authoritative decisions to the responsible official source.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `GENERIC_SYNTHETIC_REHEARSAL_AVAILABLE / HYDROLOGY_SPECIFIC_REHEARSAL_ABSENT / OPERATIONAL_ROLLBACK_HOLD`.** Shared candidate validation and marker-protected generic synthetic mechanics exist. Hydrology-specific affected/target fixtures, domain rollback tests, accountable approval, production execution, alias mutation, invalidation receipts, and public read-back do not.

The highest result supported by this companion is:

```text
BOUNDED_HYDROLOGY_ROLLBACK_READINESS_ASSESSMENT
```

That is not `ROLLBACK_AUTHORIZED`, `ROLLBACK_EXECUTED`, `RECOVERED`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

**Quick navigation:** [Relationship](#authority-and-document-relationship) · [Evidence](#current-repository-evidence) · [Use](#when-to-use-each-document) · [Decision](#finite-decision-boundary) · [Blockers](#current-operational-blockers) · [Validation](#bounded-validation-entry-points) · [Handoff](#minimum-accountable-handoff) · [Maintenance](#maintenance-and-document-rollback) · [Related](#related-repository-surfaces)

---

<a id="authority-and-document-relationship"></a>

## Authority and document relationship

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../doctrine/directory-rules.md) place human procedures under `docs/runbooks/`, semantic meaning under `contracts/`, machine shape under `schemas/`, policy under `policy/`, executable mechanics under `tools/` and `pipelines/`, behavioral evidence under `tests/`, release decisions under `release/`, receipts under governed data lanes, and public-safe carriers under governed published-data lanes.

This file is a **readiness companion and compatibility entry point**. The detailed Hydrology procedure is [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md).

| Surface | Responsibility | Authority boundary |
|---|---|---|
| `ROLLBACK.md` | Compact current-state snapshot, decision guard, validation index, and handoff minimum | Documentation only; no state transition |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Detailed defect classification, preflight, candidate selection, rehearsal interpretation, invalidation planning, review handoff, and graduation requirements | Primary Hydrology rollback procedure; still non-executing |
| [Publication rollback architecture](../../architecture/publication/ROLLBACK.md) | Cross-domain object and responsibility map | Architecture, not an operator |
| [General rollback runbook](../ROLLBACK_RUNBOOK.md) | Cross-domain doctrine and procedure lineage | Does not prove Hydrology or production readiness |
| [`RollbackCard` contract](../../../contracts/release/rollback_card.md) | Candidate semantic meaning | Candidate-only; every authority/public-mutation flag remains false or null |
| Schema, validator, fixtures, and tests | Candidate shape and bounded local consistency | Do not prove safe target, evidence closure, policy, review, or execution |
| Synthetic helper | Plan/apply within exact marker-protected synthetic roots | Never a production operator |

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Rollback changes governed release state and downstream carriers. It does not rewrite RAW evidence or move objects backward through lifecycle directories.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

This checkpoint is pinned to `main@0ba766bde4be5338c0523b1d19b9b845720faa77`.

| Surface | CONFIRMED evidence | Bounded conclusion |
|---|---|---|
| Primary Hydrology procedure | `ROLLBACK_RUNBOOK.md` is repository-grounded v2.0.0 | Detailed procedure now has a clear home |
| Shared candidate profile | Draft contract, closed schema, three valid fixtures, six invalid fixtures, expected findings, no-network validator, tests, and workflow exist | Candidate shape/local consistency only |
| Generic helper | Requires exact synthetic marker, safe paths, current-alias identity, manifest/artifact digests, distinct target, and complete invalidations | Deterministic synthetic mechanics only |
| Generic rehearsal | Eight generic tests cover plan, rollback, withdrawal, history, marker, target, digest, invalidation, and non-synthetic denial | Generic mechanics are executable |
| Hosted rollback workflow | Adds four Hazards-specific tests to the generic eight | Generic plus Hazards, not Hydrology proof |
| Hydrology validation | Domain workflow exercises bounded synthetic shape, polarity, type separation, identity, ambiguity, and context routing | Useful validation, not rollback evidence |
| Hydrology candidate lane | README only | No tracked affected or prior candidate dossier |
| Hydrology published lane | `.gitkeep` and README only | No repository-tracked public payload or prior target |
| Hydrology-specific rollback rehearsal | Absent | Domain recovery behavior remains unproved |
| Production rollback pipeline | One-line placeholder | No accepted production operator |
| Published-alias auditor | Comment-only placeholder | No accepted alias inventory, audit, or mutation path |
| Hydrology policy | Mixed-maturity and evaluator-unbound | Operational rights, sensitivity, source-role, freshness, and release-policy checks remain held |
| Accountable authority | CODEOWNERS routes review; functional and independent roles remain unverified | Routing is not approval or rollback authority |
| Deployment/public runtime | No runtime, external storage, cache, CDN, alias, or public read-back evidence inspected | Deployed state remains `UNKNOWN` |

> [!WARNING]
> No repository-tracked Hydrology payload does **not** prove that no external or deployed Hydrology state exists.

[Back to top](#top)

---

<a id="when-to-use-each-document"></a>

## When to use each document

Use this companion to answer three quick questions:

1. What is the current rollback maturity?
2. Which finite candidate dispositions are available?
3. Which repository-owned checks and blockers must appear in a reviewer handoff?

Use [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) for the detailed workflow, including:

- defect and source-role classification;
- affected-release and prior-target preflight;
- evidence, identity, time, unit, rights, sensitivity, policy, and review requirements;
- rollback versus withdrawal versus forward-correction analysis;
- invalidation and cross-lane impact;
- generic synthetic rehearsal procedure and interpretation;
- Hydrology-specific proof gap;
- operational graduation gates; and
- document rollback.

Neither document may be used to edit a public alias, copy prior bytes into a published path, activate a source, authenticate an approver, execute invalidations, emit a rollback receipt, or claim recovery.

[Back to top](#top)

---

<a id="finite-decision-boundary"></a>

## Finite decision boundary

| Condition | Candidate posture | Required next step |
|---|---|---|
| Distinct prior release is immutable, digest-verifiable, currently admissible, evidence-supported, policy-safe, reviewable, and compatible | `ROLLBACK_CANDIDATE` | Prepare the exact candidate and stop before execution |
| Current carrier must leave public use and no safe prior target exists | `WITHDRAWAL_CANDIDATE` | Prepare correction/withdrawal review and expected public non-answer |
| Evidence, target, rights, sensitivity, policy, review, operator, alias, invalidation, or read-back is unresolved | `HOLD` | Name each blocker and preserve history |
| Input is malformed, contradictory, unverifiable, or unsafe to evaluate | `ERROR` | Record a public-safe reason code and no state change |
| Corrected successor can use the normal governed promotion path | Forward correction | Use the promotion/correction path; retain rollback readiness |

Hydrology-specific safeguards include:

- NFHL remains regulatory context, never observed inundation or a warning;
- gauge parameter, unit, datum, qualifier, provisional/final state, and material time kinds remain explicit;
- NHDPlus HR identifiers and legacy COMIDs remain separate; split, merge, retired, and unresolved relations abstain;
- modeled or derived hydrography never becomes observation by rollback;
- WBD/HUC material change requires accepted geometry/version evidence, not metadata timestamps alone; and
- Hydrology cannot approve dependent Hazards, Soil, Agriculture, Geology, Infrastructure, Habitat, Fauna, or Flora recovery.

At the current checkpoint the operational default is:

```text
HOLD — PREPARE ASSESSMENT AND ACCOUNTABLE REVIEW HANDOFF ONLY
```

[Back to top](#top)

---

<a id="current-operational-blockers"></a>

## Current operational blockers

Operational rollback remains held until all applicable items close for one exact affected release and one exact revision.

- [ ] Immutable affected release, artifact digests, audience, time, and public-surface inventory.
- [ ] Distinct safe prior target with current evidence, role, rights, sensitivity, time/freshness, validation, policy, and review.
- [ ] Accepted correction or withdrawal relationship and public-notice requirements.
- [ ] Authenticated domain, correction, release, operations, and required independent/specialist reviewers.
- [ ] Accepted policy bundle, evaluator, normalized outcome, obligations, and consumer enforcement.
- [ ] Hydrology-specific synthetic rollback and withdrawal fixtures and negative tests.
- [ ] Accepted production operator with deterministic plan/apply, no-write planning, idempotency, concurrency, recovery, safe-path, target, digest, policy, review/signature, and negative checks.
- [ ] Accepted published-state/alias profile and read-only auditor.
- [ ] Least-privilege invalidation adapters for API cache, CDN, tiles, catalog, triplets, search, vector index, AI cache, and downstream derivatives.
- [ ] Append-only execution receipt with before/after identity, actors, policy, review, operations, invalidations, and result.
- [ ] Independent public read-back through API, map, Evidence Drawer, search, export, cache, and AI surfaces.
- [ ] Separate recovery decisions from every affected sibling lane.

A schema pass, CI green state, pull request, CODEOWNERS route, deadline, or feature value cannot compensate for these missing gates.

[Back to top](#top)

---

<a id="bounded-validation-entry-points"></a>

## Bounded validation entry points

Run from the repository root at a recorded commit. These commands validate bounded behavior only.

### Candidate profile

```bash
python tools/ci/install_python_ci.py project-test
python tools/validators/release/validate_rollback_card.py --fixtures
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

### Generic plus Hazards synthetic mechanics

```bash
python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

The current workflow requires twelve tests with `OK`; this is **not** Hydrology-specific proof.

### Hydrology bounded validation

Follow the exact current commands in [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) and the hosted [Hydrology workflow](../../../.github/workflows/domain-hydrology.yml). Those checks validate committed synthetic profiles, not a release, source accuracy, complete EvidenceBundle closure, active policy, or rollback readiness.

### Documentation links

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hydrology/ROLLBACK.md
```

Interpret results at the exact revision. `PASS`, `FAIL`, `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, skipped, pending, and not-run states are not interchangeable.

[Back to top](#top)

---

<a id="minimum-accountable-handoff"></a>

## Minimum accountable handoff

```yaml
assessment_type: hydrology_rollback_readiness
repository_sha: <40-character-commit>
detected_at: <timezone-aware-timestamp>

affected_scope:
  release_ref: <required-or-UNKNOWN>
  artifact_refs: []
  public_surface_refs: []
  geography: <declared-scope>
  time_scope: <declared-scope>
  source_roles: []

state_separation:
  tracked_repository_payload_found: false
  deployed_public_state: UNKNOWN
  official_source_state: OUTSIDE_KFM_AUTHORITY

candidate:
  disposition: HOLD
  target_release_ref: null
  correction_notice_ref: null
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
  invalidations: []

validation:
  rollback_card_profile: NOT_RUN
  generic_synthetic_rehearsal: NOT_RUN
  hydrology_domain_profile: NOT_RUN
  hydrology_specific_rehearsal: ABSENT
  documentation_links: NOT_RUN

blockers:
  - HYDROLOGY_ROLLBACK_REHEARSAL_ABSENT
  - PRODUCTION_ROLLBACK_OPERATOR_ABSENT
  - PUBLISHED_ALIAS_MECHANISM_UNESTABLISHED
  - ACTIVE_RELEASE_POLICY_UNESTABLISHED
  - ACCOUNTABLE_ROLLBACK_AUTHORITY_UNVERIFIED
  - EXECUTION_RECEIPT_PROFILE_ABSENT

non_effects:
  source_activation: none
  lifecycle_mutation: none
  public_state_mutation: none
  release: none
  deployment: none
  promotion: none
  publication: none
```

The detailed reviewer questions and procedure live in [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md).

[Back to top](#top)

---

<a id="maintenance-and-document-rollback"></a>

## Maintenance and document rollback

Reconcile this companion when the primary Hydrology runbook, RollbackCard profile, synthetic helper/tests, rollback workflow, Hydrology validation inventory, candidate/proof/receipt/policy/published lanes, production operator, alias/audit mechanism, invalidation adapters, correction/release decisions, source-role/time/rights/sensitivity doctrine, or deployment/runtime evidence changes.

### Current adjacent drift

The primary runbook was merged from a branch prepared before this companion replaced its scaffold. Any remaining sentence in [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) that describes `ROLLBACK.md` as a proposal scaffold is stale coordination prose, not authority to ignore this current file. Correct that wording in a separate narrow compatibility edit or the next revision of the primary runbook; do not duplicate the full procedure here.

### Roll back this documentation change

Revert the commit replacing this file if it misstates repository evidence, breaks local links or document identity, recreates parallel procedure authority, overstates rollback/review/release/deployment/promotion/publication status, conflicts with accepted governance, or causes focused documentation checks to fail.

Reverting this Markdown does not mutate a source, lifecycle object, RollbackCard, manifest, alias, cache, receipt, release, deployment, public carrier, or published state.

[Back to top](#top)

---

<a id="related-repository-surfaces"></a>

## Related repository surfaces

| Surface | Current role |
|---|---|
| [Primary Hydrology Rollback Runbook](ROLLBACK_RUNBOOK.md) | Detailed current procedure and handoff boundary |
| [Publication Rollback Discipline](../../architecture/publication/ROLLBACK.md) | Cross-domain architecture and maturity boundary |
| [General Rollback Runbook](../ROLLBACK_RUNBOOK.md) | Cross-domain doctrine and procedure lineage |
| [Hydrology Promotion Runbook](PROMOTION_RUNBOOK.md) | Promotion readiness and operational hold |
| [Hydrology No-Network Test Runbook](NO_NETWORK_TEST_RUNBOOK.md) | Offline validation boundary |
| [Hydrology Validation](VALIDATION.md) | Adjacent validation guidance |
| [Hydrology domain README](../../domains/hydrology/README.md) | Domain meaning, source-role, time, identity, and public-use boundary |
| [RollbackCard contract](../../../contracts/release/rollback_card.md) | Candidate semantics and non-authority boundary |
| [RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Closed candidate shape |
| [RollbackCard fixtures](../../../fixtures/release/rollback_card/) | Deterministic valid/invalid candidates |
| [RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py) | Shape and local consistency |
| [Synthetic helper](../../../tools/release/rollback_apply.py) | Marker-protected synthetic plan/apply only |
| [Generic synthetic tests](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Eight deterministic rehearsal tests |
| [`rollback-drill` workflow](../../../.github/workflows/rollback-drill.yml) | Read-only generic/Hazards readiness checks and production holds |
| [Hydrology workflow](../../../.github/workflows/domain-hydrology.yml) | Bounded fixture validation and proof/release holds |
| [Hydrology candidate lane](../../../release/candidates/hydrology/README.md) | Pre-publication review guidance; no tracked dossier at snapshot |
| [Hydrology published lane](../../../data/published/hydrology/README.md) | Released-carrier responsibility; no tracked payload at snapshot |
| [Hydrology policy boundary](../../../policy/domains/hydrology/README.md) | Mixed-maturity policy inventory and evaluator hold |

[Back to top](#top)
