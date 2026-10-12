<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-classification-framework-v1
title: Data Classification Framework — Current Architecture and Enforcement Map
type: architecture-reference
version: v2.0-draft
status: draft
owners:
  - "@bartytime4life — CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable architecture, source, sensitivity, policy, evidence, and release stewardship"
created: 2026-05-24
updated: 2026-08-18
policy_label: public
owning_root: docs/
responsibility: Explain how KFM composes source role, authority, sensitivity, rights, audience, lifecycle, release, correction, and bounded product classifications without becoming a semantic contract, machine schema, policy rule, evidence record, release decision, or implementation proof.
truth_posture: cite-or-abstain
current_path: docs/architecture/data-classification-framework.md
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0af1823ff5a54d2fa3b5f0dfe5db18e5056aa372
  prior_blob: 861e7689fbfcfb03dd00e4134cf8f48adc8726d3
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_decision: ADR-0029 accepted
related:
  - README.md
  - contract-schema-policy-split.md
  - sensitivity-tiers.md
  - ../doctrine/directory-rules.md
  - ../doctrine/lifecycle-law.md
  - ../doctrine/sensitivity.md
  - ../doctrine/policy-aware.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../security/DATA_CLASSIFICATION.md
  - ../standards/SENSITIVITY_RUBRIC.md
  - ../../contracts/source/source_descriptor.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../tools/validators/source_role/IMPLEMENTATION.md
  - ../../policy/sensitivity/README.md
  - ../../contracts/common/classification_release.md
  - ../../release/README.md
notes:
  - "Same-path documentation modernization only; no schema, contract, policy, source, lifecycle, release, runtime, deployment, publication, or repository-setting state changes."
  - "Current repository evidence replaces the prior document's no-mounted-repository and all-paths-proposed posture."
  - "The overlapping security-focused document at docs/security/DATA_CLASSIFICATION.md remains unresolved; this change does not select a canonical winner, create an alias, or retire either file."
  - "Legacy section anchors from v1.0 are preserved so existing fragment links continue to resolve."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Data Classification Framework — Current Architecture and Enforcement Map

> **Purpose.** Explain how KFM keeps source authority, sensitivity, rights, audience, lifecycle, release state, and domain/product classification separate; show the bounded repository surfaces that currently implement parts of that model; and keep unresolved authority and enforcement seams visible.

| Field | Current result |
|---|---|
| **Document role** | Cross-cutting architecture explanation under `docs/architecture/`; not doctrine, contract, schema, policy, evidence, review, release, or runtime authority. |
| **Evidence snapshot** | `main@0af1823ff5a54d2fa3b5f0dfe5db18e5056aa372`. |
| **Directory authority** | Directory Rules v2 is adopted through [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md). |
| **Source admission** | A schema-paired, draft [`SourceDescriptor`](../../contracts/source/source_descriptor.md) exists. It records source role, authority rank, rights, a sensitivity default, admissibility limits, review state, release state, and lifecycle posture without proving source claims. |
| **Source-role validation** | A deterministic, no-network, `PROPOSED_INACTIVE` validator exists with `PASS / ABSTAIN / RESTRICT / HOLD / DENY / ERROR`. It creates no source, evidence, policy, review, release, publication, or public permission. |
| **Sensitivity enforcement** | Doctrine, standards, policy source, and validator-routing docs exist, but current evidence does not prove one accepted crosswalk, active general bundle, evaluator binding, complete native tests, or public-runtime enforcement. |
| **Product classification** | [`ClassificationRelease`](../../contracts/common/classification_release.md) is a fixture-only broad-scale classification-product profile—not a sensitivity label, observation, policy decision, release manifest, or public authorization. |
| **Document overlap** | [`docs/security/DATA_CLASSIFICATION.md`](../security/DATA_CLASSIFICATION.md) overlaps this page. Canonical ownership and supersession remain **NEEDS VERIFICATION**. |
| **Path result** | `PLACE` at the existing requested path; no structural migration. |
| **Publication effect** | None. Documentation, a commit, a workflow, or a pull request is not promotion, release, deployment, or publication. |

> [!IMPORTANT]
> **KFM has no universal classification number.** Source role, authority rank, support type, sensitivity, rights, consent or sovereignty obligations, audience tier, lifecycle phase, review state, release state, and domain/product class answer different questions. Preserve them independently and compose them only through governed evidence, policy, review, transform, and release decisions.

> [!CAUTION]
> **Repository presence is not operational enforcement.** Draft contracts, schemas, Rego, READMEs, validators, fixtures, tests, and green workflows prove only their stated bounded scope.

**Quick navigation:** [Role](#1-purpose-and-scope) · [Authority](#2-doctrine-basis-and-authority) · [Dimensions](#3-the-three-classification-axes) · [Source role](#4-source-role-anti-collapse-register) · [Tiers](#5-sensitivity-tier-scheme--t0-to-t4) · [Rubrics](#6-sensitivity-rubric--0-to-5-per-record-field) · [Risk families](#7-per-domain-classification-matrix) · [Transitions](#8-tier-transitions-allowed-motion) · [Support records](#9-receipts-required-for-classification-operations) · [Lifecycle](#10-lifecycle-integration) · [Rights and CARE](#11-fair--care-alignment) · [SourceDescriptor](#12-classification-fields-on-the-sourcedescriptor) · [Anti-patterns](#13-failure-modes-and-anti-patterns) · [Implementation](#14-governance-and-enforcement-points) · [Validation](#15-open-questions-and-verification-backlog) · [Related](#16-related-docs)

---

<a id="1-purpose-and-scope"></a>

## 1. Purpose and scope

This page owns the human-readable cross-root map of classification concerns. It explains the independent dimensions, `SourceDescriptor` posture, bounded source-role validation, sensitivity/access/release distinctions, rights and sovereignty constraints, lifecycle and release transitions, and the fixture-only `ClassificationRelease` context.

It does not own placement law, normative policy, semantic meaning, machine shape, evidence, lifecycle instances, release decisions, or executable/deployed behavior. Those remain with accepted ADRs and Directory Rules, `contracts/`, `schemas/`, `policy/`, governed data/evidence roots, `release/`, applications, validators, tests, workflows, configuration, and runtime evidence.

**Truth labels:** `CONFIRMED` is verified at the pinned snapshot; `PROPOSED` is draft; `UNKNOWN` lacks evidence; `NEEDS VERIFICATION` names a check; `CONFLICTED` marks overlapping authority; `HOLD` stops graduation.

The file already belongs under explanatory `docs/architecture/`, so this change is in place. The overlap with [`docs/security/DATA_CLASSIFICATION.md`](../security/DATA_CLASSIFICATION.md) remains unresolved and is not silently consolidated.

[Back to top](#top)

---

<a id="2-doctrine-basis-and-authority"></a>

## 2. Doctrine basis and authority

[`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). This page maps responsibilities; it cannot absorb them.

| Evidence | Supports | Does not prove |
|---|---|---|
| [`SourceDescriptor`](../../contracts/source/source_descriptor.md) + [schema](../../schemas/contracts/v1/source/source_descriptor.schema.json) | Draft fields, vocabularies, rights/public-release constraints | Accepted admission, registry population, claim truth, or public release |
| [`source_role` implementation](../../tools/validators/source_role/IMPLEMENTATION.md) | Bounded deterministic no-network assessment | Human role assignment, policy approval, or production integration |
| Sensitivity [doctrine](../doctrine/sensitivity.md), [rubric](../standards/SENSITIVITY_RUBRIC.md), and [tiers](sensitivity-tiers.md) | Draft terminology and fail-closed architecture | Accepted crosswalk, selected bundle, or runtime enforcement |
| [`policy/sensitivity/README.md`](../../policy/sensitivity/README.md) | Current policy-source inventory and maturity boundary | That tracked rules are active |
| [`ClassificationRelease`](../../contracts/common/classification_release.md) packet | Fixture-only product profile and anti-collapse proof | Live source, release, or general classification authority |
| [`CODEOWNERS`](../../.github/CODEOWNERS) | Review routing | Stewardship, approval, or release authority |

**Authority by question:** contracts define meaning; exact schemas define shape; policy/review/release records decide admissibility and public state; receipts prove runs; deployment evidence proves operational enforcement.

[Back to top](#top)

---

<a id="3-the-three-classification-axes"></a>

## 3. Classification dimensions: compose, do not collapse

| Dimension | Question | Anti-collapse rule |
|---|---|---|
| Source type, role, authority rank | What kind of source is this and which claim roles may it support? | Publication, popularity, citation, or AI cannot upgrade authority. |
| Support type and domain/product semantics | Observation, model, forecast, aggregate, classification, candidate, context, or synthetic? | Classification is not observation; model is not measurement. |
| Sensitivity | Could full-precision content enable harm? | Public visibility elsewhere is not proof of safety. |
| Rights, consent, sovereignty, obligations | May KFM acquire, retain, transform, join, or expose it? | Strong authority never overrides rights or sovereignty. |
| Audience/exposure | Which audience may receive which representation? | Audience tier is not content sensitivity. |
| Lifecycle phase | Where is the object in `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED`? | Lifecycle motion does not strengthen role or reduce sensitivity. |
| Release/correction state | Has a governed release occurred and is it current? | Files, commits, tests, and workflows do not imply publication. |

Before consequential use, independently resolve source posture, support type, rights/sensitivity, requested audience and precision, evidence, policy/review, lifecycle, release, correction, and rollback. Missing or contradictory answers do not become an optimistic default.

[Back to top](#top)

---

<a id="4-source-role-anti-collapse-register"></a>

## 4. Source-role anti-collapse register

The draft [`SourceDescriptor`](../../contracts/source/source_descriptor.md) and paired schema expose the working source-role vocabulary. The exact active schema enum—not this page—is machine-shape authority.

The current no-network packet binds `source_role_use_request`, the SourceDescriptor schema, synthetic fixtures, validator code under `tools/validators/source_role/`, and focused tests.

| Outcome | Bounded meaning |
|---|---|
| `PASS` | Descriptor and use request are locally compatible; no authority is created. |
| `ABSTAIN` | Confidence cannot support the requested primary claim role. |
| `RESTRICT` | Internal/steward use remains bounded by rights or sensitivity. |
| `HOLD` | Evidence, review, release, correction, rollback, or role-change lineage is incomplete. |
| `DENY` | Role collapse, incompatible use, public leakage, AI-inferred role, or another hard boundary failed. |
| `ERROR` | Shape, canonicalization, identity, input, or dependency safety failed. |

Current code denies AI-inferred roles, checks source/version and role/rank/claim compatibility, requires public-use support references, holds explicit role changes for lineage/review, and leaves every authority effect false.

The fixture-only [`ClassificationRelease`](../../contracts/common/classification_release.md) uses `source_role = CLASSIFICATION` and `support_type = DERIVED_CLASSIFICATION` in its own bounded context. Those values are not aliases for `SourceDescriptor.source_role`.

**Invariants:** models/forecasts/aggregates/candidates/synthetic derivatives are not observations; legal/regulatory context is not measurement; descriptors do not prove claims; downstream carriers cannot strengthen roles; derivatives preserve limitations; corrections are versioned and reviewed.

[Back to top](#top)

---

<a id="5-sensitivity-tier-scheme--t0-to-t4"></a>

## 5. Sensitivity, audience, and the draft T0–T4 release-tier scheme

[`sensitivity-tiers.md`](sensitivity-tiers.md) documents a proposed vocabulary: `T0` open public-safe representation; `T1` reviewed generalized/redacted derivative; `T2` authenticated reviewer/steward; `T3` named restricted parties under agreement or authority; `T4` denied.

`T0` is not a missing label. Wider exposure still requires evidence, rights, policy, review, release, correction, and rollback. A public-safe derivative is a distinct object from its restricted input.

A join, tile, screenshot, search result, graph edge, embedding, Focus Mode answer, or export may be more sensitive than its inputs. Classify the produced object; strictest applicable obligations win until reviewed transformation proves safety.

Restricted bytes must not reach public clients and be “protected” only by zoom, opacity, filters, omitted fields, popups, or client-side state.

[Back to top](#top)

---

<a id="6-sensitivity-rubric--0-to-5-per-record-field"></a>

## 6. Do not alias sensitivity rank, access class, release tier, or source default

- `SourceDescriptor.sensitivity_default` is a categorical source-admission default.
- Draft S0–S5 or numeric `sensitivity_rank` describes possible harm from full precision where an accepted object carries it.
- Draft C0–C5 describes access/audience.
- Draft T0–T4 describes release transform/review posture.
- `rights`, `review_state`, `release_state`, and lifecycle answer separate questions.

The old claim that every record has one `(source_role, sensitivity_tier, lifecycle_phase)` triple is too strong for current schemas. Exact fields belong to the applicable contract/schema.

Never silently map `rank 3 == T1 == C1`. Crosswalks must be explicit, versioned, policy-owned, fixture-backed, domain/operation-bounded, and reviewable.

[Back to top](#top)

---

<a id="7-per-domain-classification-matrix"></a>

## 7. Risk families and safe default posture

The prior page's universal per-domain tier table came from planning material and is not operational authority.

| Risk family | Safe default |
|---|---|
| Living persons, genealogy, DNA/genomics, private joins | Deny/hold exact content; allow only authorized reviewed derivatives. |
| Archaeology, cultural/sacred or sovereign-controlled material | Deny exact disclosure; require qualified authority. |
| Rare species and sensitive habitat | Deny exact locations; require reviewed geoprivacy/generalization. |
| Infrastructure interiors, vulnerabilities, dependency graphs | Deny exploit-enabling detail; require security review. |
| Private wells, land/title, ownership/occupancy joins | Separate identity, legal context, observation, and geometry; restrict by purpose. |
| Models, AI, synthetic scenes, reconstructions | Mark derived/synthetic; preserve method, uncertainty, evidence, reality boundary. |
| Hazards/advisories | Preserve issuing authority/currentness; KFM is not an emergency-alert authority. |
| Sensitive-by-composition outputs | Reassess the output; strictest obligations win until reviewed transformation proves safety. |

Domain contracts and accepted policy own finer decisions. Public docs must not expose protected-location hints, hidden thresholds, or reconstruction-enabling parameters.

[Back to top](#top)

---

<a id="8-tier-transitions-allowed-motion"></a>

## 8. Governed classification transitions

| Transition | Required support | Safe failure |
|---|---|---|
| Role assignment/correction | Versioned descriptor, active vocabulary, rationale, lineage, review | Hold or deny; no silent mutation |
| Wider audience/precision | Evidence, rights/consent/sovereignty, policy, review, transform receipt when needed, release support | Deny or hold |
| Narrower audience/precision | Immediate restriction, correction/withdrawal lineage, downstream invalidation | Retreat to safety |
| Lifecycle promotion | Validation, evidence/proof, policy, review, correction, rollback | Stay or quarantine |
| Product correction/supersession | Native lineage/times and preserved identity | Do not overwrite history |
| Public release | Decision/manifest, public-safe artifact binding, correction, rollback, delivery controls | Remain unreleased |

Wider exposure requires affirmative closure; restriction may occur immediately. Promotion never rewrites source role, support type, rights, sensitivity, or history.

[Back to top](#top)

---

<a id="9-receipts-required-for-classification-operations"></a>

## 9. Support records for classification operations

Requirements vary by object, operation, audience, and consequence. Common families are `SourceDescriptor`, source-role-use assessment, sensitivity/rights/consent records, `EvidenceRef`/`EvidenceBundle`, validation reports, `PolicyDecision`, transform receipts, `ReviewRecord`, release/promotion records, and correction/withdrawal/rollback records.

Each proves only its own scope. In particular:

- a descriptor does not prove a claim;
- a validator pass does not approve policy or release;
- an EvidenceBundle does not grant rights;
- a transform receipt does not prove review;
- a release record does not prove every cache or client converged.

Receipts remain distinct from evidence, policy, review, proofs, catalogs, release, correction, and public artifacts. A generated report cannot approve its own release.

[Back to top](#top)

---

<a id="10-lifecycle-integration"></a>

## 10. Lifecycle integration

| Stage | Classification responsibility | Public posture |
|---|---|---|
| Candidate / RAW | Record source identity, possible role, rights/currentness/sensitivity questions; preserve source without upgrading it | Internal only |
| WORK / QUARANTINE | Normalize, assess joins/derivatives, hold conflict, harmful precision, stale state, or missing support | Deny public access |
| PROCESSED | Preserve role, support type, rights, sensitivity, time, space, and lineage in validated objects | Still unreleased |
| CATALOG / TRIPLETS | Project discoverability/relations without turning indexes or graph edges into truth or permission | Catalog visibility is not exposure authority |
| PUBLISHED | Bind a reviewed public-safe or role-gated derivative to evidence, policy, release, correction, and rollback | Governed interfaces/released carriers only |

Classification can become stricter at any stage. Correction, withdrawal, and rollback must reach maps, APIs, exports, search, graphs, caches, and AI.

[Back to top](#top)

---

<a id="11-fair--care-alignment"></a>

## 11. Rights, sovereignty, CARE, and public reason hygiene

Rights and sensitivity are independent: non-sensitive data may be redistribution-denied; open terms may still contain harmful precision; authoritative sources may remain inadmissible for a requested use.

The draft SourceDescriptor therefore separates `rights`, `sensitivity_default`, `access`, `citation`, `admissibility_limits`, `public_release`, `review_state`, `release_state`, and `lifecycle`.

FAIR never overrides CARE, consent, rights, or sovereignty. Public availability elsewhere does not replace authority-to-control, stewardship, revocation, or culturally appropriate review.

Public outcomes use stable public-safe reason codes rather than exact sensitive locations, private/genomic details, hidden identities, redaction parameters, confidential agreements, or exploit-enabling detail.

[Back to top](#top)

---

<a id="12-classification-fields-on-the-sourcedescriptor"></a>

## 12. Current `SourceDescriptor` classification surface

| Surface | Current result |
|---|---|
| Semantic contract | [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) |
| Legacy-case pointer | [`contracts/source/SOURCE_DESCRIPTOR.md`](../../contracts/source/SOURCE_DESCRIPTOR.md) |
| Paired schema | [`schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) |
| Maturity | Draft / `PROPOSED`; registry, accepted policy, complete wiring, and runtime use remain **NEEDS VERIFICATION** |

The contract records unresolved singular `source/` versus declared plural `sources/` migration. This page links the confirmed current file and does not decide that migration.

Current groups cover identity/version; source type/role/authority; publisher/steward; rights and sensitivity default; cadence/access/citation/source head; admissibility limits; public-release, review, lifecycle, governance refs, and optional deterministic hash.

The paired profile records fail-closed rights/public-release conditions, review requirements for sensitive/live-candidate posture, `fixture_only` restrictions, and a closed shape. Those invariants do not prove admission, activation, evidence, policy runtime, or release.

A descriptor is not evidence. Consequential use still needs record identity/scope, `EvidenceRef -> EvidenceBundle`, rights/sensitivity closure, policy/review, release, correction, and rollback.

[Back to top](#top)

---

<a id="13-failure-modes-and-anti-patterns"></a>

## 13. Failure modes and anti-patterns

| Anti-pattern | Counter-rule |
|---|---|
| One universal scalar | Preserve independent dimensions and compose explicitly. |
| Popularity or AI assigns authority | Use admitted descriptor, schema, claim limits, and evidence. |
| Promotion changes model to observation | Keep source role and support type fixed and traceable. |
| Sensitivity rank equals release tier | Keep risk, access, audience, rights, and release separate. |
| Missing classification means open | Fail closed or route to review. |
| Rego presence means enforcement | Prove selected bundle, evaluator, tests, consumer binding, runtime. |
| Validator `PASS` means release | Keep validation, policy, review, and release distinct. |
| Style hides sensitive bytes | Produce a public-safe derivative upstream. |
| Carrier becomes evidence | Resolve evidence/release or abstain. |
| Correction touches only canonical record | Invalidate/reissue every affected carrier. |
| Denial reason leaks protected facts | Use public-safe codes and role-gated detail. |
| Docs select canonical winners by prose | Use authority/migration evidence, links, tests, rollback. |

[Back to top](#top)

---

<a id="14-governance-and-enforcement-points"></a>

## 14. Current repository implementation and enforcement map

| Surface | Current state | Safe conclusion |
|---|---|---|
| [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted | Same-path placement is confirmed |
| [`SourceDescriptor`](../../contracts/source/source_descriptor.md) + schema | Draft paired profile | Boundary exists; admission/registry/runtime use unproved |
| [`source_role` validator](../../tools/validators/source_role/IMPLEMENTATION.md) | Executable deterministic no-network `PROPOSED_INACTIVE` profile | Bounded anti-collapse exists; no production authority |
| Sensitivity docs + [`policy/sensitivity/`](../../policy/sensitivity/) | Multiple drafts and mixed scaffold source | Accepted crosswalk/bundle/evaluator/enforcement unresolved |
| [`tools/validators/sensitivity/`](../../tools/validators/sensitivity/) | README + `.gitkeep` | No executable validator in that inspected lane |
| [`ClassificationRelease`](../../contracts/common/classification_release.md) packet | Inactive fixture-only schema/validator/tests/workflow | Bounded product profile; no live release/public use |
| [`docs/security/DATA_CLASSIFICATION.md`](../security/DATA_CLASSIFICATION.md) | Separate draft | Canonical overlap unresolved |

**CONFIRMED bounded implementations:** source-role anti-collapse and ClassificationRelease fixtures.  
**UNKNOWN / HOLD:** universal admission, accepted sensitivity runtime, governed public classification, and end-to-end correction/rollback parity.

The authority split remains: docs explain; contracts mean; schemas shape; policy admits; fixtures/tests prove; tools check; data carries lifecycle/proof; release decides; apps deliver after closure.

[Back to top](#top)

---

<a id="15-open-questions-and-verification-backlog"></a>

## 15. Validation, review, and open verification

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/test_validate_source_role.py
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/source_role/validate_source_role.py --fixtures
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest tests.validators.test_validate_classification_release --verbose
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/validate_classification_release.py --fixtures
```

Hosted metadata, link/document-graph, Markdown, and aggregate checks apply as selected by current workflows. Green docs CI proves documentation QA only.

**Reviewer questions:** Is one bounded context, contract, and exact schema authoritative? Are source role, support type, sensitivity, rights, audience, lifecycle, and release independent? Are policy/evaluator, accountable review, evidence, transforms, release, correction, rollback, negative fixtures, downstream invalidations, and non-parallel homes explicit?

| Open item | Status | Needed evidence |
|---|---|---|
| Security-page overlap | `CONFLICTED / NEEDS VERIFICATION` | Steward scope decision, backlinks, migration/rollback |
| Source-role vocabulary/path and universal adoption | `NEEDS VERIFICATION / UNKNOWN` | Accepted decision, migration tests, registry/pipeline coverage |
| Sensitivity vocabulary/crosswalk/bundle/evaluator | `UNKNOWN / HOLD` | Versioned decision, bundle digest, evaluator, tests, consumer binding |
| Executable sensitivity validator | `ABSENT in inspected lane` | Contract/schema, fixtures, code, tests, workflow |
| Rights/consent/sovereignty/composition | `NEEDS VERIFICATION` | Authority/policy, negative tests, correction/cache drill |
| Public classification and rollback parity | `HOLD / UNKNOWN` | Evidence, policy, review, release, correction, rollback, runtime rehearsal |

**Rollback:** close the draft PR/discard the branch before merge, or revert the one-file commit after authorized merge. No runtime, policy, source, data, release, cache, or public artifact requires restoration.

[Back to top](#top)

---

<a id="16-related-docs"></a>

## 16. Related repository evidence

**Architecture/doctrine:** [`README`](README.md) · [`split`](contract-schema-policy-split.md) · [`tiers`](sensitivity-tiers.md) · [`Directory Rules`](../doctrine/directory-rules.md) · [`lifecycle`](../doctrine/lifecycle-law.md) · [`sensitivity`](../doctrine/sensitivity.md) · [`policy-aware`](../doctrine/policy-aware.md) · [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) · [`security classification`](../security/DATA_CLASSIFICATION.md) · [`rubric`](../standards/SENSITIVITY_RUBRIC.md)

**Source:** [`contract`](../../contracts/source/source_descriptor.md) · [`legacy pointer`](../../contracts/source/SOURCE_DESCRIPTOR.md) · [`schema`](../../schemas/contracts/v1/source/source_descriptor.schema.json) · [`use request`](../../contracts/source/source_role_use_request.md) · [`validator note`](../../tools/validators/source_role/IMPLEMENTATION.md)

**Sensitivity/release:** [`policy boundary`](../../policy/sensitivity/README.md) · [`validator lane`](../../tools/validators/sensitivity/README.md) · [`release`](../../release/README.md)

**Classification product:** [`contract`](../../contracts/common/classification_release.md) · [`schema`](../../schemas/contracts/v1/common/classification_release.schema.json) · [`validator`](../../tools/validators/validate_classification_release.py) · [`test`](../../tests/validators/test_validate_classification_release.py) · [`workflow`](../../.github/workflows/classification-release.yml)

---

**Final rule:** classify source, content, rights, audience, lifecycle, release state, and produced derivative independently; compose them through evidence, policy, review, and release; fail closed rather than convert unknown into public permission.

[Back to top](#top)
