<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-policy-sensitivity-fauna
title: Fauna Sensitivity Guidance — Containment and Routing Crosswalk
type: compatibility-document; routing-crosswalk; proposal-scaffold; noncanonical-doc-lane
version: v0.2-draft
status: draft; repository-grounded; proposal-only; containment-crosswalk; noncanonical-under-directory-rules; no-policy-authority; no-sensitive-payload; migration-hold; non-release; non-publication
owners:
  - "@bartytime4life — verified CODEOWNERS fallback only"
owner_status: "@bartytime4life is the confirmed repository review route. Independent fauna, taxonomy, source, rights, sensitivity, geoprivacy, security, policy, evidence, review, release, correction, rollback, and documentation stewardship remains NEEDS VERIFICATION."
created: 2026-08-23
updated: 2026-08-23
policy_label: repository-public
current_path: docs/policy/sensitivity/fauna.md
owning_root: docs/
responsibility: "Contain and route human-readable fauna-sensitivity guidance while preventing this noncanonical documentation path from becoming sensitivity-policy source, protected-data storage, contract or schema authority, test authority, release authority, or publication authority."
truth_posture: "CONFIRMED current path, parent containment contract, accepted Directory Rules placement, fauna documentation and policy surfaces, proposal-only policy scaffolds, SensitivityLabel semantics, and bounded test inventory / LINEAGE Drive fauna blueprints and prior fixture-first reports / PROPOSED safe human crosswalk and review-packet guidance / UNKNOWN accepted fauna sensitivity vocabulary, active policy bundle, evaluator binding, deployed enforcement, external consumers, and final path lifetime / NEEDS VERIFICATION independent stewardship, source rights, policy convergence, consumer closure, and required-check coupling"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: af0797e91a467a626497abc9f5f090f33a8f01c0
  target_prior_blob: 31be13d0ce49779bc0de3d6829842ef439ba07ec
  parent_readme_blob: 40af7f1b4a6501c90294d4f74c7c61c97946a9f0
  policy_sensitivity_fauna_readme_blob: aac9f7b6316b89238d209c7ef4045fbf4df15ea9
  fauna_identity_model_blob: edea05cfbefa09a369a3cbc18f165fe1c6ee6f31
  fauna_sensitivity_posture_blob: b24f0c16bde517a58038e26e1ab082ae6c486c44
  sensitivity_label_contract_blob: d6ddf1eb7db9bc955e56de76a0d997b6e4ecd231
  redaction_receipt_contract_blob: c686cdf5c79a8b99ac66d4b01cd30d2f450f645f
inspection_boundary: >-
  Current-session GitHub reads covered current main, the complete prior target,
  the parent containment contract, accepted Directory Rules and ADR-0029, the
  fauna identity, sensitivity, Map UI, domain-policy, sensitivity-policy,
  SensitivityLabel, RedactionReceipt, and bounded test surfaces. Google Drive
  reads covered the Fauna Architecture planning report, Habitat + Fauna
  thin-slice blueprint, and prior Habitat + Fauna implementation report as
  lineage sources. No protected fauna payload, live source connector, accepted
  source admission, policy bundle, evaluator, authenticated reviewer,
  RedactionReceipt instance, PolicyDecision, release candidate, deployment,
  public endpoint, correction propagation, or rollback execution was exercised.
related:
  - ./README.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/IDENTITY_MODEL.md
  - ../../domains/fauna/SENSITIVITY.md
  - ../../domains/fauna/SENSITIVITY_POSTURE.md
  - ../../domains/fauna/MAP_UI_CONTRACTS.md
  - ../../security/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../policy/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../policy/sensitivity/fauna/README.md
  - ../../../policy/domains/fauna/README.md
  - ../../../contracts/policy/sensitivity_label.md
  - ../../../contracts/shared/redaction_receipt.md
  - ../../../schemas/contracts/v1/policy/sensitivity_label.schema.json
  - ../../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../../fixtures/domains/fauna/README.md
  - ../../../tests/domains/fauna/README.md
  - ../../../tests/policy/README.md
  - ../../../tools/validators/domains/fauna/README.md
  - ../../../tools/validators/policy/README.md
  - ../../../packages/policy-runtime/README.md
  - ../../../apps/governed-api/README.md
  - ../../../release/README.md
  - ../../../data/receipts/README.md
  - ../../../data/proofs/README.md
  - ../../../.github/CODEOWNERS
non_effects:
  - does_not_create_or_modify_executable_policy
  - does_not_define_an_accepted_sensitivity_tier_or_transform
  - does_not_store_or_classify_a_protected_fauna_fact
  - does_not_admit_or_activate_a_source
  - does_not_create_or_modify_a_contract_schema_fixture_test_validator_or_workflow
  - does_not_bind_or_execute_a_policy_bundle_or_evaluator
  - does_not_authenticate_rights_review_or_release_authority
  - does_not_create_a_PolicyDecision_RedactionReceipt_review_proof_or_release_record
  - does_not_change_lifecycle_API_UI_map_AI_release_deployment_or_publication_state
  - does_not_move_rename_deprecate_delete_merge_promote_publish_or_change_repository_settings
tags:
  - kfm
  - docs
  - fauna
  - sensitivity
  - geoprivacy
  - containment
  - routing
  - proposal-scaffold
  - fail-closed
  - public-safe
  - non-authoritative
  - cite-or-abstain
notes:
  - "v0.2 replaces a short planned-path placeholder with a repository-grounded, proposal-only containment and routing crosswalk."
  - "This file remains subordinate to the parent lane contract and does not authorize substantive growth under docs/policy/."
  - "Executable policy source remains under policy/; fauna-domain explanation remains under docs/domains/fauna/."
  - "Drive documents are retained as design lineage and do not prove current repository implementation."
  - "Physical migration, compatibility, retirement, or deletion remains HOLD pending accepted disposition and consumer closure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Sensitivity Guidance — Containment and Routing Crosswalk

> **One-line purpose.** Make the current fauna-sensitivity safety boundary and repository routes inspectable without turning `docs/policy/sensitivity/fauna.md` into policy source, a protected-location store, a second fauna standard, or evidence of release.

[![Status: proposal scaffold](https://img.shields.io/badge/status-proposal%20scaffold-d4a72c?style=flat-square)](#status-and-authority)
[![Placement: containment only](https://img.shields.io/badge/placement-containment%20only-bc6f00?style=flat-square)](#directory-rules-basis)
[![Policy authority: policy root](https://img.shields.io/badge/policy%20authority-policy%2F-1f883d?style=flat-square)](#routing-matrix)
[![Sensitive geometry: fail closed](https://img.shields.io/badge/sensitive%20geometry-fail%20closed-b42318?style=flat-square)](#inherited-safety-posture)
[![Protected payloads: prohibited](https://img.shields.io/badge/protected%20payloads-prohibited-b42318?style=flat-square)](#protected-content-and-safe-authoring)
[![Publication effect: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#non-effects)

> [!IMPORTANT]
> **This file is a proposal-only human crosswalk, not sensitivity policy.** Normative allow, restrict, hold, abstain, deny, redaction, generalization, and release-gating source belongs under the canonical [`policy/`](../../../policy/README.md) responsibility root. Current fauna policy surfaces remain mixed-maturity and evaluator-unbound; this page cannot activate or normalize them.

> [!CAUTION]
> **Do not place protected fauna information here.** This public repository page must contain no exact sensitive occurrences, nest/den/roost/hibernacula/spawning locations, private-land joins, steward-only identifiers, source credentials, restricted evidence, hidden review notes, live transform secrets, or parameters that could reconstruct a protected location.

> [!WARNING]
> **A public-looking map, tile, API response, screenshot, export, search result, graph edge, or AI answer is not proof of safe release.** Sensitive geometry must be handled before public delivery through governed source, evidence, policy, review, transform, release, correction, and rollback controls. Style-only hiding is not a security boundary.

**Quick navigation:** [Purpose](#purpose) · [Status](#status-and-authority) · [Evidence](#evidence-basis) · [Directory Rules](#directory-rules-basis) · [Safety posture](#inherited-safety-posture) · [Protected classes](#protected-interest-classes) · [Identity](#identity-source-role-and-evidence-separation) · [Representations](#public-safe-representation-crosswalk) · [Routing](#routing-matrix) · [Review packet](#minimum-human-review-packet) · [Public surfaces](#public-api-map-search-export-and-ai-boundary) · [Validation](#validation) · [Migration](#migration-correction-and-rollback) · [Open work](#open-verification-register) · [Non-effects](#non-effects)

---

## Purpose

This page has one bounded responsibility: preserve a safe, current, human-readable crosswalk for fauna sensitivity while the repository resolves the relationship among:

- fauna domain explanation under [`docs/domains/fauna/`](../../domains/fauna/README.md);
- cross-domain sensitivity-policy source under [`policy/sensitivity/`](../../../policy/sensitivity/README.md);
- fauna-specific sensitivity candidates under [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md);
- fauna-domain admissibility candidates under [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md);
- semantic meaning in [`contracts/`](../../../contracts/README.md);
- machine shape in [`schemas/`](../../../schemas/README.md);
- executable conformance in [`tests/`](../../../tests/README.md);
- runtime evaluation in an accepted policy evaluator;
- and release, correction, withdrawal, and rollback under [`release/`](../../../release/README.md).

It may explain current repository evidence, inherited safety invariants, safe authoring boundaries, and the evidence needed for later review. It may not define accepted sensitivity classes, exact transform thresholds, source admission, operational access, or publication permission.

The file remains a **proposal scaffold** so the parent [`docs/policy/sensitivity/README.md`](README.md) remains the lane contract. Its same-path update is containment, not promotion.

[Back to top](#top)

---

## Status and authority

| Field | Current bounded result |
|---|---|
| Repository path | `docs/policy/sensitivity/fauna.md` — **CONFIRMED** tracked at the pinned base |
| Prior target | Short `PROPOSED scaffold`; blob `31be13d0ce49779bc0de3d6829842ef439ba07ec` |
| Current role | Human containment, status crosswalk, safe routing, and review preparation |
| Owning root | `docs/` — explanation only |
| Placement result | **`PLACE`** for same-path containment; **`HOLD`** for authority growth, new children, move, deletion, or substantive policy text |
| Parent contract | [`README.md`](README.md) — containment-only, noncanonical, migration held |
| Domain explanation route | [`docs/domains/fauna/`](../../domains/fauna/README.md) |
| Executable sensitivity-policy route | [`policy/sensitivity/`](../../../policy/sensitivity/README.md) |
| Fauna policy relationship | **CONFLICTED / NEEDS VERIFICATION** between `policy/sensitivity/fauna/` and `policy/domains/fauna/` |
| Accepted fauna policy bundle | **UNKNOWN / not established in reviewed evidence** |
| Evaluator and consumer binding | **UNKNOWN / not established in reviewed evidence** |
| Public release authority | None |
| Deployment or publication effect | None |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified in this work session from pinned repository bytes, accepted decisions, or connected source material |
| `LINEAGE` | Useful prior plan or implementation report that does not prove current repository behavior |
| `PROPOSED` | Human guidance, placement, vocabulary, transform, or future behavior not accepted or operationally verified |
| `UNKNOWN` | Evidence is insufficient |
| `NEEDS VERIFICATION` | A concrete repository, rights, reviewer, evaluator, consumer, or runtime check remains |
| `CONFLICTED` | Current surfaces use overlapping or incompatible authority, vocabulary, package, or placement claims |
| `HOLD` | Do not expose, expand, migrate, or infer authority until the named evidence closes |

[Back to top](#top)

---

## Evidence basis

### Current repository evidence

| Surface | Current evidence-backed posture | What it supports |
|---|---|---|
| [`docs/policy/sensitivity/README.md`](README.md) | Containment-only, noncanonical docs lane; fauna child retained as proposal scaffold | This file may route and contain but must not become policy authority |
| [`docs/domains/fauna/IDENTITY_MODEL.md`](../../domains/fauna/IDENTITY_MODEL.md) | Draft domain model; owners and implementation details remain unverified | Occurrence Evidence, Occurrence Restricted, and Occurrence Public are distinct identities; sensitive identity disclosure fails closed |
| [`docs/domains/fauna/SENSITIVITY.md`](../../domains/fauna/SENSITIVITY.md) | Draft explanatory crosswalk; tier scheme and transform details remain proposed | Domain-level deny-by-default intent and review/receipt separation |
| [`docs/domains/fauna/SENSITIVITY_POSTURE.md`](../../domains/fauna/SENSITIVITY_POSTURE.md) | Draft summary only | Quick orientation; no authority beyond its cited companions |
| [`docs/domains/fauna/MAP_UI_CONTRACTS.md`](../../domains/fauna/MAP_UI_CONTRACTS.md) | Draft Map UI seam | Renderer is downstream; style-only hiding is invalid; clicks and Focus Mode require governed resolution |
| [`policy/sensitivity/README.md`](../../../policy/sensitivity/README.md) | Canonical rule-source boundary with a mixed proposed scaffold corpus | Policy source belongs here, but current enforcement is not proved |
| [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md) | README, Rego, and YAML candidates; proposal-only | Candidate fauna sensitivity source, not an accepted bundle |
| [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md) | Substantive mixed-maturity boundary; evaluator unbound | Candidate fauna admissibility composition and an explicit fail-closed public edge |
| [`SensitivityLabel`](../../../contracts/policy/sensitivity_label.md) | Draft/proposed semantic contract paired with a proposed schema | Finite context labels `public`, `generalized`, `restricted`, `quarantine`; label is not a decision or release |
| [`RedactionReceipt`](../../../contracts/shared/redaction_receipt.md) | Draft/proposed shared semantic contract; paired schema remains permissive scaffold | A transform receipt records protective work but does not prove sufficiency or publication |
| [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) | Mixed test inventory and bounded fixture-oriented slices | Tests can support declared predicates; they do not activate policy or approve release |

### Connected Google Drive lineage

The connected Drive sources used for this revision are design and continuity inputs:

| Source | Status in this revision | Supported contribution |
|---|---|---|
| `KFM_Fauna_Architecture_PDF_Only_Report.pdf` | `LINEAGE / PROPOSED` | Whole-fauna sensitivity classes, source-role separation, geoprivacy planning, public-safe derivatives, and first-slice cautions |
| `KFM_Habitat_Fauna_Thin_Slice_Extended_Pro_Blueprint.pdf` | `LINEAGE / PROPOSED` | Controlled public-safe fixture posture, one derivation proof, finite API outcomes, EvidenceBundle closure, and release separation |
| `KFM habitat& fauna Crossover.pdf` | `LINEAGE / prior standalone scaffold` | Earlier fixture-first implementation ideas and reported local test results; not current-repository proof |

The Drive reports consistently recommend withholding live rare-species connectors and exact location products until rights, sensitivity, source role, review, transform, and release controls are verified. They do not prove that current repository rules, routes, tests, or runtime enforcement exist.

[Back to top](#top)

---

## Directory Rules basis

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [`Directory Rules v2`](../../doctrine/directory-rules.md) bytes. Applied here:

1. A path is an authority claim.
2. `docs/` owns human-readable explanation, not executable policy or protected data.
3. `policy/` owns normative admissibility source.
4. `contracts/` define semantic meaning; `schemas/` define machine shape.
5. `fixtures/` and `tests/` own reusable public-safe examples and executable conformance.
6. Fauna is a domain segment inside responsibility roots, not an authority root.
7. One artifact has one authority owner; overlapping writable homes fail closed.
8. A scaffold, rule filename, passing test, generated artifact, or map render does not establish authority or maturity.
9. Migration requires a verified target, consumer closure, single-write discipline, validation, correction, and rollback.
10. Sensitive detail is a hard exclusion from public documentation.

Finite placement result:

- **`PLACE`** — retain and update this existing path as a proposal-only containment crosswalk;
- **`HOLD`** — no substantive policy, exact transform details, protected examples, or new topic children;
- **`MIGRATE` or retire later** — only after accepted disposition, reference migration, and consumer closure;
- **`DENY`** — any use of this page as executable policy, protected-data storage, release approval, or public-serving authority.

[Back to top](#top)

---

## Inherited safety posture

The following is the bounded posture inherited from KFM doctrine, current fauna docs, current policy boundaries, and the connected fauna plans. It is **not** a claim that an active evaluator currently enforces every row.

1. **Fail closed on uncertainty.** Missing, stale, contradictory, or untrusted rights, source role, sensitivity, evidence, review, release, correction, or harmful-precision context blocks public exposure.
2. **Separate exact and public identities.** `Occurrence Evidence`, `Occurrence Restricted`, and `Occurrence Public` are distinct governed objects, not display modes of one record.
3. **Transform before delivery.** Sensitive geometry or attributes are generalized, aggregated, delayed, suppressed, or withheld upstream of public APIs, tiles, search, graph, export, and AI surfaces.
4. **Never rely on style-only hiding.** Browser filters, opacity, zoom thresholds, popups, clustering, and undocumented field omission are not policy enforcement.
5. **Preserve evidence and source role.** A public derivative retains resolvable evidence and source lineage without exposing protected payloads.
6. **Keep object families separate.** A `SensitivityLabel`, `PolicyDecision`, `RedactionReceipt`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, and `RollbackCard` have different responsibilities.
7. **Public is not released.** A `public` or `generalized` sensitivity label does not replace validation, evidence, rights, policy, review, release, correction, or rollback gates.
8. **AI remains interpretive.** Generated language may summarize released public-safe evidence; it cannot infer permission, invent an exact location, or override a deny/hold/abstain result.
9. **Corrections propagate.** A source correction, sensitivity change, rights revocation, or transform defect must invalidate affected derivatives, caches, indexes, tiles, exports, and AI-facing results through governed correction and rollback.
10. **Use the safest useful representation.** Public need does not create entitlement to maximum precision.

### Failure posture

When a request cannot be supported safely, the owning policy/runtime path should return its accepted finite outcome and public-safe reason. This page does not normalize engine-native outputs. Human authoring should use plain descriptions such as:

- **hold for policy or rights review**;
- **withhold exact geometry**;
- **produce only a generalized or aggregated candidate**;
- **abstain because evidence or source role is insufficient**;
- **deny public exposure**;
- **return a safe error without falling back to allow**.

[Back to top](#top)

---

## Protected-interest classes

The categories below identify review pressure without publishing the protected fact.

| Safe category | Why sensitivity may be material | Public-document rule |
|---|---|---|
| Exact sensitive occurrence | Precision may enable collection, disturbance, poaching, harassment, or habitat damage | Never include the location or reconstruction aids |
| Nest, den, roost, hibernacula, spawning, breeding, or congregation site | Sites may be repeatedly occupied and disproportionately vulnerable | Describe the class only; exact identity and geometry remain restricted |
| Steward-controlled record | Agency, tribal, landowner, researcher, or partner terms may restrict use or redisclosure | Cite the governing authority; do not infer permission |
| Re-identifying join | Individually public datasets may reveal a protected location when combined | Treat joinability as a sensitivity input; do not publish the join recipe |
| Telemetry or movement track | Dense sequences can reveal home ranges, migration corridors, or recurring sites | Use only reviewed public-safe derivatives |
| Small-count aggregate | Sparse cells or narrow time windows can reconstruct individuals or sites | Require suppression/generalization review |
| Media and metadata | Images, audio, captions, EXIF, filenames, timestamps, and thumbnails can leak location | Strip or transform before public delivery and record the action |
| Temporal sensitivity | Breeding, migration, embargo, active investigation, or temporary threat may make timing harmful | Delay or withhold under an accepted policy profile |
| Rights or license uncertainty | Occurrence and media rights may differ by record, source, and use | Unknown rights block publication |
| Source-role ambiguity | Aggregator, community science, agency, model, range product, and legal-status source roles differ | Do not let one source role impersonate another |
| Correction or withdrawal state | Previously safe output may become unsafe or unsupported | Invalidate and correct; do not leave stale public carriers active |

These categories are not an accepted machine enum. Contracts and policy own any persisted vocabulary.

[Back to top](#top)

---

## Identity, source-role, and evidence separation

### Fauna occurrence identities

Current fauna identity guidance distinguishes:

| Object | Role | Public-boundary rule |
|---|---|---|
| `Occurrence Evidence` | Source-faithful evidentiary record or reference | Never assume public eligibility |
| `Occurrence Restricted` | Governed internal/reviewer identity with exact or sensitive context | Never serve through a normal public route |
| `Occurrence Public` | Separately identified released public-safe derivative | Must resolve to evidence, policy, transform/review, release, and correction lineage |

A public derivative must not overwrite or masquerade as its restricted source. Identity continuity is carried through explicit references, digests, receipts, supersession, and correction records.

### Source-role anti-collapse

The connected fauna architecture report and current repository docs support a claim-relative source-role posture:

| Source role | May support | Must not be treated as |
|---|---|---|
| Legal or conservation-status authority | Statutory/listing/status facts within its scope and effective time | Automatic occurrence or release authority |
| Agency or steward record | Governed domain record within declared scope | Permission to republish exact geometry |
| Occurrence aggregator | Discovery and occurrence evidence with source lineage | Legal-status authority or universal rights grant |
| Community-science platform | Observation evidence subject to record/media terms and quality limits | Exact-location release permission |
| Taxonomic authority or crosswalk | Taxon identity and synonym resolution | Occurrence truth or sensitivity decision |
| Range or model product | Modeled/generalized distribution support | Direct observation |
| Synthetic fixture | Deterministic tests and bounded demonstrations | Real-world fauna evidence |

A source can be strong for one claim and insufficient for another. Evidence quantity does not override rights or sensitivity.

[Back to top](#top)

---

## Public-safe representation crosswalk

This table is a **human authoring crosswalk**, not a policy matrix or accepted transform catalog.

| Candidate representation | Human posture | Required supporting surfaces before public use |
|---|---|---|
| Exact protected point, route, site, or dense track | **WITHHOLD / restricted review** | Accepted policy and access path; never normal public delivery |
| Generalized geometry | **Candidate only** | Governed sensitivity context, transform profile, safe receipt, validation, review, release, correction, rollback |
| Aggregated count or density | **Candidate only** | Small-count/re-identification checks, time/space scope, aggregation or redaction accountability, review |
| Range or seasonal polygon | **Candidate only** | Source role, model/observation distinction, valid time, uncertainty, sensitivity review, release |
| Existence-only statement | **Candidate only** | Evidence closure and steward determination that existence itself is safe |
| Non-spatial taxon information | **Candidate only** | Taxonomic anchors, rights, evidence, freshness, and release state |
| Withheld result with safe reason | **Preferred when support is incomplete** | Public-safe reason code; protected detail retained only in an authorized system |
| Public media or audio | **Candidate only** | Rights, metadata stripping, location leakage review, transform receipt when material |
| Public API, tile, search, graph, export, or AI summary | **Downstream carrier only** | Released public-safe source object plus governed envelope and correction state |

### SensitivityLabel crosswalk

The current proposed [`SensitivityLabel`](../../../contracts/policy/sensitivity_label.md) uses:

- `public`;
- `generalized`;
- `restricted`;
- `quarantine`.

Those values are semantic context, not access grants. Existing fauna docs also contain a proposed T0–T4 vocabulary and other ranking language. Their relationship is **CONFLICTED / NEEDS VERIFICATION**. This page does not select, merge, or translate them.

### RedactionReceipt crosswalk

A [`RedactionReceipt`](../../../contracts/shared/redaction_receipt.md) records that a protective transform occurred. It must not reveal the protected input or reversal-enabling parameters. It does not prove the transform was sufficient, authenticate review, or authorize release.

[Back to top](#top)

---

## Routing matrix

Route each change by the responsibility it owns.

| Work item | Owning route | Boundary |
|---|---|---|
| Fauna identity, occurrence triad, taxonomy, source-role, and domain explanation | [`docs/domains/fauna/`](../../domains/fauna/README.md) | Human domain guidance only |
| Cross-domain threat, privacy, geoprivacy, re-identification, and exposure guidance | [`docs/security/`](../../security/README.md) or an accepted standards/runbook lane | Human guidance; no protected examples |
| Normative cross-domain sensitivity rules | [`policy/sensitivity/`](../../../policy/sensitivity/README.md) | Rule source only |
| Fauna sensitivity rule/profile candidates | [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md) | Current proposal-only candidates; activation not implied |
| Fauna domain admissibility composition | [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md) | Current mixed-maturity boundary; relationship to sensitivity child unresolved |
| SensitivityLabel meaning | [`contracts/policy/sensitivity_label.md`](../../../contracts/policy/sensitivity_label.md) | Semantic contract only |
| SensitivityLabel shape | [`schemas/contracts/v1/policy/sensitivity_label.schema.json`](../../../schemas/contracts/v1/policy/sensitivity_label.schema.json) | Machine shape only |
| RedactionReceipt meaning | [`contracts/shared/redaction_receipt.md`](../../../contracts/shared/redaction_receipt.md) and domain companion | Transform accountability only |
| RedactionReceipt shape | [`schemas/contracts/v1/receipts/redaction_receipt.schema.json`](../../../schemas/contracts/v1/receipts/redaction_receipt.schema.json) | Current permissive/proposed schema; no enforcement claim |
| Synthetic examples and negative fixtures | [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) | Public-safe and non-reconstructable only |
| Fauna conformance tests | [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) | Tests prove only declared predicates |
| Policy conformance and boundary tests | [`tests/policy/`](../../../tests/policy/README.md) | No authority or release effect |
| Validator implementation | [`tools/validators/domains/fauna/`](../../../tools/validators/domains/fauna/README.md) and [`tools/validators/policy/`](../../../tools/validators/policy/README.md) | Validation is bounded |
| Runtime evaluation | Accepted evaluator/bundle under the verified implementation boundary | Must fail closed; current binding remains unproved |
| Governed client delivery | [`apps/governed-api/`](../../../apps/governed-api/README.md) plus released public-safe carriers | No direct RAW/WORK/QUARANTINE/restricted-store path |
| Receipts and proofs | [`data/receipts/`](../../../data/receipts/README.md) and [`data/proofs/`](../../../data/proofs/README.md) | Separate accountability families |
| Release, correction, withdrawal, rollback | [`release/`](../../../release/README.md) | Separate decision and state authority |
| Path, vocabulary, or owner conflict | [`docs/registers/`](../../registers/README.md) | Track and resolve; do not silently normalize |

[Back to top](#top)

---

## Minimum human review packet

A request to expose, generalize, aggregate, delay, export, or otherwise transform fauna material should provide a public-safe packet sufficient for qualified review. The packet is a human checklist, not a contract or policy input schema.

| Required area | Minimum inspectable content |
|---|---|
| Candidate identity | Stable candidate/object refs and exact repository/release snapshot |
| Operation and audience | What is being requested, by whom, for which audience and purpose |
| Source role | Source identity, role for this claim, upstream authority, and limitations |
| Evidence | Resolvable EvidenceRef/EvidenceBundle support or an explicit gap |
| Taxonomy | Taxonomic anchors/crosswalk state and unresolved ambiguity |
| Spatial and temporal scope | Requested representation, precision class, valid/observed/release time, and freshness |
| Rights and terms | Record/media rights, redistribution constraints, attribution, embargo, and unresolved conditions |
| Sensitivity context | Accepted label/profile refs without protected values |
| Re-identification risk | Joins, small counts, media metadata, time precision, and downstream reconstruction risk |
| Proposed public derivative | Fields and representation proposed for release, not the restricted payload |
| Transform accountability | Named versioned transform profile and proposed receipt reference without reversal secrets |
| Validation | Positive, negative, fail-closed, reconstruction, and stale/correction checks |
| Review | Required fauna, sensitivity, rights-holder, security, evidence, and release reviewer classes |
| Release and correction | Candidate/release state, correction propagation, cache/index invalidation, and rollback target |
| Residual unknowns | Concrete unresolved questions and the hold/deny/abstain posture |

### Reviewer separation

The reviewed repository confirms only `@bartytime4life` as a GitHub routing identity. It does not prove independent fauna, sensitivity, rights-holder, security, evidence, or release authority. High-consequence exposure must remain pending until required assignments and review records exist.

### Authoring dispositions

For documentation and review preparation, use bounded phrases rather than pretending to issue policy decisions:

- `ROUTE_TO_DOMAIN_GUIDANCE`;
- `HOLD_FOR_POLICY_OR_RIGHTS_REVIEW`;
- `REQUIRE_RESTRICTED_REVIEW`;
- `PUBLIC_SAFE_DERIVATIVE_CANDIDATE`;
- `WITHHOLD_EXACT_REPRESENTATION`;
- `ABSTAIN_FOR_MISSING_EVIDENCE`;
- `NEEDS_VERIFICATION`.

These are not accepted machine enums.

[Back to top](#top)

---

## Protected content and safe authoring

### Permitted

- public-safe categories and reason codes;
- current repository status and exact non-sensitive paths;
- source-role and authority boundaries;
- synthetic or irreversibly generalized examples;
- public-safe descriptions of obligations;
- migration, verification, correction, and rollback requirements;
- links to governing contracts, schemas, policy, tests, validators, and release surfaces.

### Prohibited

- exact sensitive coordinates, routes, recurring sites, or high-resolution geometry;
- taxon/site combinations that make a protected location obvious;
- private parcel/landowner/person joins;
- telemetry tracks, timestamp sequences, raw EXIF, or filenames that reconstruct location;
- source credentials, private endpoints, signed URLs, access tokens, or restricted attachments;
- exact transform radii, seeds, secret salts, reversal methods, or operational weaknesses;
- real restricted fixtures or screenshots;
- private review rationale that reveals the protected fact;
- policy decisions, receipts, proofs, or release records copied into prose as decorative authority.

When a useful explanation would disclose the protected fact, publish a safe category and route the details through an authorized review system instead.

[Back to top](#top)

---

## Public API, map, search, export, and AI boundary

| Surface | Required public-boundary behavior | Prohibited shortcut |
|---|---|---|
| Governed API | Serve only released public-safe identities and finite envelopes; resolve evidence or fail closed | Direct source/restricted-store read |
| MapLibre/UI | Render released carrier; expose generalization/restriction/stale/correction state | Style-only hiding or browser-side redaction |
| Evidence Drawer | Show public-safe claim, citations, source role, freshness, limitations, policy/release/correction state | Copy restricted evidence or exact hidden values |
| Search/index | Index only released public-safe fields and geometry | Index exact restricted coordinates “for internal ranking” in a public service |
| Graph/triplet projection | Project public-safe identities and explicit derived relations | Treat graph proximity as source authority or leak restricted joins |
| Export/download | Apply the same policy, field, geometry, rights, and release constraints as interactive surfaces | Treat bulk export as exempt from UI restrictions |
| Screenshot/story/share | Preserve public-safe representation and trust state | Reveal hidden layers, metadata, or exact viewport clues |
| Focus Mode/AI | Retrieve released evidence, apply policy, cite or abstain, and retain bounded confidence | Direct browser-to-model path, location inference, or fluent override |
| Cache/CDN | Key by release/policy-safe identity and support invalidation | Continue serving superseded or withdrawn derivatives |

The public client never becomes the last sensitivity gate.

[Back to top](#top)

---

## Validation

This documentation-only change should trigger documentation QA. Green documentation checks do not prove geoprivacy, policy correctness, source rights, evaluator binding, public enforcement, review independence, or release safety.

| Check | Expected use | Authority limit |
|---|---|---|
| `docs-meta-block` | Validate changed metadata and emit a review-only registry delta | Does not admit this page as canonical policy |
| `link-check` | Validate repository-relative links | Does not verify external rights or runtime |
| `docs-document-graph` | Update bounded documentation relations | Graph projection is not authority |
| `docs-stale-scan` | Surface freshness/verification debt | Staleness result does not decide policy |
| `docs-build` | Exercise the docs build | Build success is not publication |
| Directory topology validator | Confirm no new authority lane or forbidden path | Does not settle final migration |
| Secret/sensitive-content review | Confirm no protected payload or private locator is introduced | Manual and automated review remain bounded |
| Full diff and remote read-back | Confirm only the intended file changed and bytes match | Delivery evidence only |

### Changed-file acceptance checks

- One H1 and one closed `KFM_META_BLOCK_V2`.
- All local links resolve at the exact PR head.
- No executable policy, schema, fixture, test, validator, workflow, source record, or release object changes.
- No exact sensitive fauna value, private locator, or reconstruction-enabling parameter.
- Drive-derived ideas are labeled `LINEAGE` or `PROPOSED`.
- Current policy and runtime maturity is not overstated.
- Parent containment contract remains controlling.
- Rollback restores the prior blob without touching policy, data, runtime, release, or publication state.

[Back to top](#top)

---

## Migration, correction, and rollback

### Current migration posture

This page exists under a noncanonical documentation lane. Its final disposition remains `HOLD` because:

- `docs/domains/fauna/` already owns primary fauna human guidance;
- `policy/sensitivity/fauna/` and `policy/domains/fauna/` both claim related policy responsibilities;
- current vocabularies and package boundaries are not accepted as one coherent profile;
- external and internal consumers of this path are not closed;
- independent stewardship is not assigned.

Do not solve that tension through a silent move, copy, or deletion.

### Before merge

- Close or abandon the unmerged draft PR and branch if review rejects the change.
- Preserve the prior target blob `31be13d0ce49779bc0de3d6829842ef439ba07ec` as the exact rollback target.
- Do not delete this path or create a replacement home merely to simplify the tree.

### After an authorized merge

- Revert the exact merged documentation commit or restore prior blob `31be13d0ce49779bc0de3d6829842ef439ba07ec` through a reviewed follow-up.
- If a statement proves wrong, correct this file in place and retain the evidence snapshot.
- If a later accepted migration moves or retires the path, preserve stable links, consumer inventory, a tombstone/redirect where required, source lineage, correction notes, and a reversible target.
- No policy bundle, restricted data, source activation, API, map, AI, release, deployment, or publication rollback is required for this docs-only change.

### Correction triggers

Correct or supersede this page when:

- Directory Rules or the parent containment contract changes;
- one fauna policy lane is accepted as the survivor;
- sensitivity vocabulary or transform/receipt contracts are accepted or superseded;
- source terms, rights, or legal/conservation authority change materially;
- a public consumer is found to rely on this page as policy authority;
- active evaluator, bundle, review, release, correction, or rollback evidence becomes available;
- a cited repository path is moved, retired, or reclassified.

[Back to top](#top)

---

## Open verification register

| Priority | Open item | Closure evidence |
|---|---|---|
| P0 | Decide the responsibility split and survivor relationship between `policy/sensitivity/fauna/` and `policy/domains/fauna/` | Accepted policy architecture/ADR, package and entrypoint map, migration/compatibility plan, tests, consumer binding |
| P0 | Establish accepted fauna sensitivity input/output vocabulary | Paired contract/schema, finite outcomes and obligations, negative fixtures, validator/evaluator tests |
| P0 | Verify an accepted bundle, selector, evaluator, normalized input assembler, and public consumer | Exact version/digest, runtime tests, fail-closed errors, governed API binding |
| P0 | Verify source rights and geoprivacy posture before any live fauna connector or public occurrence product | SourceDescriptor/admission record, terms snapshot, rights review, sensitivity review, release class |
| P0 | Assign fauna, sensitivity, rights-holder, evidence, security, policy, release, correction, and rollback review duties | Accepted assignments, authority binding, recusal/expiry rules, ReviewRecords |
| P1 | Reconcile `SensitivityLabel` levels with proposed T0–T4 and other rank vocabularies | Accepted crosswalk or retirement decision; no lossy translation |
| P1 | Complete RedactionReceipt schema, validator, fixtures, and safe public presentation | Accepted schema/contract pairing, polarity tests, no-reconstruction checks |
| P1 | Prove field, geometry, media, search, graph, export, screenshot, cache, and AI parity | Cross-surface negative tests and correction-invalidation drill |
| P1 | Verify current fauna test coverage and required-check coupling | Exact-head hosted runs and ruleset/check evidence |
| P1 | Inventory repository and external consumers of this noncanonical path | Zero-writer/consumer map or accepted compatibility plan |
| P2 | Decide final disposition of `docs/policy/sensitivity/fauna.md` | Accepted `PLACE`, `MIGRATE`, `MIRROR`, or retirement decision with rollback |

[Back to top](#top)

---

## Non-effects

This documentation-only update does **not**:

- create, alter, accept, activate, or evaluate sensitivity policy;
- define an accepted tier, rank, reason code, transform, radius, seed, or release profile;
- store, classify, generalize, redact, aggregate, delay, or expose a real fauna record;
- admit or activate KDWP, USFWS, NatureServe, GBIF, eBird, iNaturalist, EDDMapS, museum, telemetry, or other live sources;
- resolve taxonomy, evidence, rights, consent, source role, or review authority;
- create a `SensitivityLabel`, `PolicyDecision`, `RedactionReceipt`, `ReviewRecord`, proof, receipt, release manifest, correction notice, withdrawal notice, or rollback card instance;
- change a contract, schema, fixture, test, validator, package, app, workflow, data object, release object, or repository setting;
- alter the `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` lifecycle;
- authorize a public API, map layer, tile, search index, graph, export, dashboard, screenshot, story, or AI answer;
- merge, release, deploy, promote, publish, or change branch protection or rulesets.

A branch, pull request, merge, passing check, or this page's presence proves only the corresponding repository/documentation state.

[Back to top](#top)

---

## Related surfaces

### Containment, placement, and domain guidance

- [`docs/policy/sensitivity/README.md`](README.md)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [`docs/domains/fauna/README.md`](../../domains/fauna/README.md)
- [`IDENTITY_MODEL.md`](../../domains/fauna/IDENTITY_MODEL.md)
- [`SENSITIVITY.md`](../../domains/fauna/SENSITIVITY.md)
- [`SENSITIVITY_POSTURE.md`](../../domains/fauna/SENSITIVITY_POSTURE.md)
- [`MAP_UI_CONTRACTS.md`](../../domains/fauna/MAP_UI_CONTRACTS.md)

### Policy, semantics, shape, validation, and release

- [`policy/sensitivity/README.md`](../../../policy/sensitivity/README.md)
- [`policy/sensitivity/fauna/README.md`](../../../policy/sensitivity/fauna/README.md)
- [`policy/domains/fauna/README.md`](../../../policy/domains/fauna/README.md)
- [`SensitivityLabel`](../../../contracts/policy/sensitivity_label.md)
- [`RedactionReceipt`](../../../contracts/shared/redaction_receipt.md)
- [`SensitivityLabel schema`](../../../schemas/contracts/v1/policy/sensitivity_label.schema.json)
- [`RedactionReceipt schema`](../../../schemas/contracts/v1/receipts/redaction_receipt.schema.json)
- [`Fauna fixtures`](../../../fixtures/domains/fauna/README.md)
- [`Fauna tests`](../../../tests/domains/fauna/README.md)
- [`Policy tests`](../../../tests/policy/README.md)
- [`Fauna validators`](../../../tools/validators/domains/fauna/README.md)
- [`Policy validators`](../../../tools/validators/policy/README.md)
- [`policy-runtime`](../../../packages/policy-runtime/README.md)
- [`governed-api`](../../../apps/governed-api/README.md)
- [`release/`](../../../release/README.md)

---

**Truth posture:** CONFIRMED current repository boundaries / LINEAGE connected Drive fauna planning / PROPOSED containment crosswalk / UNKNOWN operational enforcement / NEEDS VERIFICATION policy convergence and independent stewardship.

[Back to top](#top)
