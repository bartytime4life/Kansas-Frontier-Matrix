<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/fauna
title: Fauna Domain Policy Boundary and Activation Contract
type: readme; directory-readme; domain-policy-boundary; policy-index
version: v0.2
status: draft; repository-grounded; mixed-maturity; T4-baseline-projection; direct-proposed-rego-scaffolds; one-inactive-fixture-profile; evaluator-unbound; fail-closed-public-edge; non-release; non-publication
owners: "@bartytime4life — verified CODEOWNERS review route; Fauna, taxonomy, source, rights, sensitivity/geoprivacy, evidence, policy, contract/schema, validation, runtime, release, security, and documentation stewardship assignments NEEDS VERIFICATION"
created: 2026-06-15
updated: 2026-08-13
supersedes: unversioned greenfield scaffold
policy_label: restricted-review; policy; fauna; biodiversity; T4-baseline; source-role-aware; rights-aware; sensitivity-aware; geoprivacy-aware; reconstruction-resistant; evidence-bound; cite-or-abstain; release-gated; correction-aware; rollback-aware; no-public-authority
current_path: policy/domains/fauna/README.md
owning_root: policy/
responsibility: >-
  Define and index the Fauna-specific admissibility-policy boundary: the animal-domain
  operations that may be evaluated, the governed context they require, the finite decisions
  and obligations an accepted evaluator would emit, and the conditions that must remain held
  or denied. This README does not establish animal truth, activate a policy bundle, perform a
  geoprivacy transform, approve evidence, release data, or authorize publication.
truth_posture: >-
  CONFIRMED direct lane inventory of this README, five proposed Rego scaffolds, one proposed
  eBird redistribution scaffold, and one closed inactive fixture-only tile-field allowlist;
  CONFIRMED deterministic Fauna fixture, occurrence-evidence, and tile-field validation slices,
  a domain-fauna workflow with one accepted seven-test fixture-safety job, and explicit proof
  and release holds; PROPOSED Fauna T4 baseline machine projection, domain and sensitivity
  rule semantics, decision normalization, package convergence, and activation requirements;
  CONFLICTED deny-named Rego stubs that default deny to false versus allow-named stubs that
  default allow to false, plus multiple package namespaces and unaccepted responsibility split
  between domain and sensitivity lanes; UNKNOWN accepted Fauna bundle, manifest, selector,
  evaluator, normalized input assembler, native Rego test harness, production consumer,
  obligation handlers, decision receipts, promotion binding, runtime enforcement, and rollback
  drill; NEEDS VERIFICATION functional steward assignments, accepted default-result semantics,
  source and taxonomy authority, rights currency, sensitivity tiers and transforms, independent
  review, public-surface enforcement, correction propagation, cache invalidation, and emergency
  deactivation.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 9fa82de35cb665840a071013fb5f1813fcc05a6a
  prior_blob: 39b7c7dd859614ab9ae9a72208f693056c97f2c6
  policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
  policy_domains_parent_blob: ed9be975c9da2c7d77d94fab621db39f23953813
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  domain_lane_register_blob: 1bfc6f91cfa713a5e3d51ece011b63b46310734f
  fauna_docs_readme_blob: ab08f2d63e03d37ff8cd9f308720c3503bfdb58f
  fauna_policy_doc_blob: 36f9ddaa5dd3ce7d2f8499ae3ca18acbbdfe772c
  fauna_sensitivity_posture_blob: b24f0c16bde517a58038e26e1ab082ae6c486c44
  fauna_contract_readme_blob: 192f680bc2ebdc69a9f76fcb986aac168601a1e3
  fauna_schema_readme_blob: 4bd3dd8696a5c29a8c746aced9cf14604e272d16
  fauna_fixture_readme_blob: dd02bd0d50aa880b718bcd12a95ca46773ff42c1
  fauna_test_readme_blob: 72e93e4abcf48567942fb1a3a588944df1c83e3c
  fauna_validator_readme_blob: f5d4d8a299318fb2eda45f9a987c7c02843434cd
  fauna_workflow_blob: 69b28755f933cd9d1f786058143211d82a102598
  abstain_on_ambiguous_blob: 52a9c0e896b9bec4eebfe8b08e0daf3c4ff310e4
  api_envelope_blob: 505dac94e9d7c419fe690657cd32ed6fcad90560
  deny_unpublished_blob: c7cdf53ad5e93dc56d55aee91ed4ccdae9ed13c9
  rare_species_redaction_blob: a7269d357bb7570fc3680c299486e5d62cb33a68
  sensitivity_blob: 925efbdfacb5e63252793f27e1386a247a36ad1f
  tile_field_allowlist_blob: 3f743b21f3d13b100a1a5bb7c3a7b2bb6d48df69
related:
  - ../README.md
  - ../../README.md
  - ../../sensitivity/fauna/README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/fauna/POLICY.md
  - ../../../docs/domains/fauna/SENSITIVITY_POSTURE.md
  - ../../../contracts/domains/fauna/README.md
  - ../../../schemas/contracts/v1/domains/fauna/README.md
  - ../../../fixtures/domains/fauna/README.md
  - ../../../tests/domains/fauna/README.md
  - ../../../tools/validators/domains/fauna/README.md
  - ../../../pipeline_specs/fauna/README.md
  - ../../../pipelines/domains/fauna/README.md
  - ../../../packages/domains/fauna/README.md
  - ../../../data/registry/sources/fauna/README.md
  - ../../../release/candidates/fauna/README.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "Accepted ADR-0029 adopts the exact Directory Rules v2 bytes despite the adopted document's preserved proposal-era header. The ADR controls decision status."
  - "Fauna is a domain segment inside responsibility roots, never a repository root and never a parallel authority system."
  - "The proposed domain-lane machine projection records fauna with a T4 sensitivity baseline; the projection cannot authorize disclosure or lower sensitivity."
  - "No source, policy bundle, evaluator, release, deployment, or publication is activated by this README."
  - "Exact or reconstructable sensitive animal locations, identities, private endpoints, source payloads, credentials, transform parameters, and operational exposure aids do not belong in this public repository README."
-->

<a id="top"></a>

# policy/domains/fauna

> **One-line purpose.** `policy/domains/fauna/` is the Fauna-specific admissibility boundary: it may define how governed animal-domain operations are allowed, restricted, held, abstained from, denied, or failed closed, but it cannot create animal truth, lower sensitivity, approve release, or publish data.

[![Status: draft](https://img.shields.io/badge/status-draft-d4a72c?style=flat-square)](#current-status)
[![Sensitivity: T4 baseline projection](https://img.shields.io/badge/sensitivity-T4%20baseline%20projection-b42318?style=flat-square)](#fauna-safety-invariants)
[![Runtime: evaluator unbound](https://img.shields.io/badge/runtime-evaluator%20unbound-6b7280?style=flat-square)](#activation-and-definition-of-done)
[![Public edge: fail closed](https://img.shields.io/badge/public%20edge-fail%20closed-9f1239?style=flat-square)](#public-surface-contract)

> [!IMPORTANT]
> **Policy is not evidence or release authority.** Fauna policy can evaluate only a governed input assembled from independently owned contracts, schemas, source records, evidence, rights, sensitivity, lifecycle, review, correction, and release state. A file in this directory, a passing validator, a green workflow, a map render, or a generated answer does not supply those authorities.

<!-- callout boundary -->

> [!CAUTION]
> **The direct Rego lane is not an active Fauna policy system.** Three deny-named stubs currently declare `default deny := false` and no operative deny rules; two allow-named stubs declare `default allow := false` and no positive allow rules. Those shapes conflict as a single decision interface and have no observed bundle, selector, evaluator, native Rego suite, production consumer, or release binding. Do not infer fail-closed runtime enforcement from filenames.

<!-- callout boundary -->

> [!NOTE]
> The one substantive direct profile, [`tile_field_allowlist.yaml`](./tile_field_allowlist.yaml), is explicitly `PROPOSED_INACTIVE_FIXTURE_ONLY`. Its deterministic test suite proves only the closed fixture profile and candidate-field polarity described below. It does not approve a production field set, inspect tile bytes, or authorize public use.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-current-status) · [Ownership](#ownership-and-non-ownership) · [Safety](#fauna-safety-invariants) · [Inventory](#direct-lane-inventory) · [Scope](#what-belongs-here) · [Inputs](#required-policy-input) · [Decisions](#decision-and-obligation-contract) · [Lifecycle](#lifecycle-and-temporal-behavior) · [Naming](#identity-naming-and-versioning) · [Validation](#validation-and-failure-semantics) · [Review](#review-burden) · [Activation](#activation-and-definition-of-done) · [Correction](#correction-reconsideration-and-invalidation) · [Rollback](#rollback-and-recovery) · [Map](#related-responsibility-roots) · [ADRs](#governing-decisions-and-doctrine) · [Backlog](#open-verification-register) · [Evidence](#last-reviewed-evidence) · [History](#revision-history)

---

## Purpose

This directory is the canonical `policy/` segment for **Fauna-specific admissibility questions**. It is where reviewed machine policy may eventually decide whether a bounded Fauna operation can proceed and which restrictions or obligations must follow.

Typical questions include:

- whether a Fauna candidate has enough governed context to be evaluated at all;
- whether source role, taxonomy, evidence, rights, freshness, sensitivity, and lifecycle state are mutually consistent;
- whether an exact, generalized, aggregated, withheld, or non-spatial representation is admissible for the requested audience and surface;
- whether unpublished, stale, superseded, corrected, withdrawn, embargoed, or unresolved material must be held or denied;
- whether a public candidate exposes a forbidden field or can be recombined into sensitive animal-location detail;
- whether an API, tile, Evidence Drawer, Focus Mode, export, or AI response must answer, restrict, abstain, deny, or return a safe error;
- which review, receipt, correction, invalidation, and rollback obligations remain outstanding.

This README is both a **directory boundary** and a **maturity index**. It explains what a future accepted Fauna policy system must do while recording what current repository evidence actually proves.

It does not itself:

- define Fauna object meaning or machine shape;
- admit, retrieve, rank, or activate a source;
- settle taxonomy, conservation status, occurrence truth, range truth, disease causality, or legal interpretation;
- create an `EvidenceBundle`, receipt, proof, review record, or release record;
- perform redaction, aggregation, generalization, geoprivacy, or tile production;
- move an artifact through lifecycle states;
- approve a candidate, release, deployment, publication, alert, notification, or public claim;
- replace human stewardship for sensitive species, locations, rights, or public consequence.

<p align="right"><a href="#top">Back to top</a></p>

---

## Authority and current status

### Authority chain

The governing chain is:

1. accepted [`ADR-0029`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact bytes of the [Directory Rules](../../../docs/doctrine/directory-rules.md);
2. Directory Rules place admissibility rules under singular `policy/` and use `fauna` only as a domain segment;
3. the [`policy/` root contract](../../README.md) defines the repository-wide policy boundary;
4. the [`policy/domains/` parent](../README.md) defines domain-policy composition and maturity;
5. this README narrows that responsibility to Fauna without superseding shared policy, evidence, rights, sensitivity, review, release, correction, or rollback authority.

The Directory Rules document retains proposal-era control text because ADR-0029 adopted those exact bytes. The accepted ADR—not that preserved header—controls adoption status.

### Current status

| Question | Repository-grounded answer |
| --- | --- |
| Does the directory exist? | **CONFIRMED.** It contains this README and seven sibling files. |
| Is this the canonical Fauna domain-policy segment? | **CONFIRMED placement.** `policy/` owns admissibility; `fauna` is the domain segment. |
| Is Fauna registered? | **CONFIRMED presence / PROPOSED projection.** [`domain_lane_register.yaml`](../../../control_plane/domain_lane_register.yaml) records `lane_id: fauna`, `code_alias: fauna`, documentation at `docs/domains/fauna/`, and a T4 baseline, but declares itself machine-projection-only. |
| Are operative Fauna policy rules present? | **PARTIAL / MIXED.** Five Rego files exist, but each self-identifies as a proposed scaffold. Only default values are operative. |
| Is any direct profile substantively validated? | **YES, bounded.** The inactive tile-field allowlist has a closed schema, validator, eight-case fixture replay, 12-test module, and dedicated workflow. |
| Is the direct Rego set normalized? | **NO.** Default-result names, truth polarity, package namespaces, and decision surfaces conflict. |
| Is an accepted Fauna bundle or evaluator bound? | **UNKNOWN / not observed.** Package-name searches return only the defining files. |
| Is Fauna policy active in production or release gating? | **NO evidence observed.** Runtime, selector, consumer, obligation, decision-receipt, promotion, and release bindings remain unproved. |
| May public clients consume raw or restricted Fauna material? | **NO.** Public clients remain governed-interface-only; sensitive or unresolved material fails closed. |
| Does this README activate anything? | **NO.** It changes documentation only. |

### Authority ceiling

This directory may own **Fauna-specific policy source and its local explanatory index** after each artifact satisfies its own review and activation gates. It may reference—but never absorb—the following authorities:

- semantic meaning in `contracts/`;
- source identity and admission in governed registries;
- evidence support in evidence objects and resolvers;
- rights, consent, privacy, sensitivity, and geoprivacy decisions in their owning policy lanes;
- lifecycle state in `data/`;
- executable evaluation in runtime or service code;
- receipts and proofs in their canonical stores;
- candidate, release, correction, withdrawal, and rollback state in `release/` and governed lifecycle records;
- human review and GitHub transition control.

If an answer depends on authority not represented in a current governed input, the policy path must **hold, abstain, deny, or error**. It must not reconstruct the missing authority from a filename, directory, map, model, prompt, or prior decision.

<p align="right"><a href="#top">Back to top</a></p>

---

## Ownership and non-ownership

### Local responsibility

Subject to accepted package, input, output, and activation contracts, this lane may own:

- Fauna-specific admissibility predicates;
- Fauna-specific reason and obligation codes;
- policy-source defaults and explicit deny/restrict/abstain conditions;
- policy-controlled public-field profiles;
- source-role and representation constraints that are unique to Fauna;
- composition requirements between Fauna domain policy and shared rights, sensitivity, geoprivacy, evidence, review, and release decisions;
- tests and documentation references for those rules, while executable tests remain under `tests/`.

### Non-ownership matrix

| This lane does not own | Owning responsibility | Required relationship |
| --- | --- | --- |
| Animal-domain doctrine and human scope | [`docs/domains/fauna/`](../../../docs/domains/fauna/README.md) | Cite as human guidance; do not execute prose as policy. |
| Object meaning and invariants | [`contracts/domains/fauna/`](../../../contracts/domains/fauna/README.md) | Policy consumes contract-defined concepts without redefining them. |
| JSON shape and serialization | [`schemas/contracts/v1/domains/fauna/`](../../../schemas/contracts/v1/domains/fauna/README.md) | Validate shape before semantic policy evaluation. |
| Source identity, role, authority, rights metadata, or activation | [`data/registry/sources/fauna/`](../../../data/registry/sources/fauna/README.md) and source-governance lanes | Resolve immutable governed references; never promote source role. |
| Evidence sufficiency or provenance truth | Evidence contracts, resolvers, and [`policy/evidence/`](../../evidence/README.md) | Consume current evidence state; cite or abstain. |
| Rights or redistribution approval | [`policy/rights/`](../../rights/README.md) and source-specific terms | Compose a current rights decision; local policy cannot waive it. |
| Sensitivity tiers and geoprivacy controls | [`policy/sensitivity/fauna/`](../../sensitivity/fauna/README.md) and [`policy/geoprivacy/`](../../geoprivacy/README.md) | Apply the most restrictive current decision. |
| Redaction or transform execution | Governed pipelines and [`policy/redaction/`](../../redaction/README.md) | Require transform identity and receipt; do not perform transforms in Rego. |
| Pipeline execution | [`pipelines/domains/fauna/`](../../../pipelines/domains/fauna/README.md) | Pipeline obeys policy; pipeline success cannot mint policy approval. |
| Declarative run intent | [`pipeline_specs/fauna/`](../../../pipeline_specs/fauna/README.md) | Spec requests evaluation; it cannot activate policy or release. |
| Fixtures and executable proof | [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) and [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) | Fixtures are synthetic examples; tests prove only declared scope. |
| Validator implementation | [`tools/validators/domains/fauna/`](../../../tools/validators/domains/fauna/README.md) | Validator checks inputs and profiles; it does not approve release. |
| Shared helper implementation | [`packages/domains/fauna/`](../../../packages/domains/fauna/README.md) | Helpers preserve decisions and refs; they cannot create them. |
| Lifecycle storage | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, catalogs, receipts, proofs, and published carriers | Policy emits a decision; an authorized producer performs any state transition. |
| Release approval or rollback authority | [`release/candidates/fauna/`](../../../release/candidates/fauna/README.md), manifests, corrections, and rollback lanes | Require reviewed current release state; never self-approve. |
| Public API, UI, map, export, or AI behavior | Governed application/runtime lanes | Consumers enforce authenticated decisions and obligations; they do not reinterpret them. |

### Review routing is not stewardship

The current [CODEOWNERS](../../../.github/CODEOWNERS) routes `/policy/` review to `@bartytime4life`. That is a verified GitHub review route, not proof of Fauna stewardship, independent approval, sensitivity expertise, rights authority, policy activation, release approval, or publication permission. Functional assignments remain **NEEDS VERIFICATION**.

<p align="right"><a href="#top">Back to top</a></p>

---

## Fauna safety invariants

These invariants apply even when a narrower file, fixture, workflow, or consumer is incomplete.

### 1. Sensitive animal locations fail closed

Exact or reconstructable locations for sensitive taxa, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry, mortality or disease clusters, steward-controlled records, and other vulnerable contexts must not reach public surfaces unless a current governed policy path explicitly permits a public-safe representation.

The proposed domain-lane register records a **T4 baseline** for Fauna. Because that register is a machine projection and not release authority, the mapping is a minimum caution signal—not an automatic classification, disclosure rule, or downgrade permission. When tier, transform, review, or release state is unresolved, use the most restrictive applicable posture.

### 2. Source role never upgrades through processing

An aggregator, index, model, inferred surface, taxonomy crosswalk, generalized layer, or public catalog cannot become occurrence authority merely because it was normalized, joined, validated, rendered, or cited. Source role is established by source governance and must survive every transformation.

### 3. Knowledge character remains explicit

Observed occurrence, modeled context, reported event, curated status, inferred range, generalized aggregate, and unknown material are not interchangeable. Policy must refuse any operation that collapses those distinctions.

### 4. Range is not occurrence

A range, seasonal range, migration corridor, suitability surface, density grid, richness indicator, or habitat relation must not be represented as proof that an animal occurred at a specific place or time.

### 5. Evidence outranks generated language

An `EvidenceBundle` or resolvable evidence reference outranks summaries, model output, map labels, prompts, or generated explanations. If support is absent, stale, inaccessible, conflicting, or insufficient for the requested claim, the consumer must cite the limitation and abstain or deny.

### 6. Public safety is cross-surface

A field may be harmless in isolation and unsafe when combined across tiles, APIs, drawers, exports, caches, time slices, nearby layers, or AI responses. Policy review must assess reconstruction and differencing risk across the full released surface.

### 7. Release is a separate state

Schema-valid, contract-consistent, validator-passing, policy-admissible, reviewed, released, deployed, and published are distinct states. None implies the next.

### 8. Correction can only restrict immediately

New risk, rights withdrawal, stale evidence, taxonomic correction, source retraction, or incident response may immediately hold or restrict a public edge. Relaxing a restriction requires a fresh governed evaluation and review; it cannot rely on a prior allow.

### 9. Non-publishers remain non-publishers

Connectors, watchers, validators, pipelines, packages, workflows, tests, maps, and AI components may request or enforce a decision but cannot publish on their own authority.

<p align="right"><a href="#top">Back to top</a></p>

---

## What belongs here

An artifact belongs directly in `policy/domains/fauna/` only when its **one primary responsibility** is Fauna-specific admissibility policy or the local index for that policy.

Appropriate examples:

- reviewed Rego modules with an accepted Fauna package namespace and decision contract;
- closed, versioned, machine policy profiles that constrain Fauna admissibility;
- local policy data that is safe for this public repository, non-secret, non-sensitive, and clearly distinguished from source data or lifecycle records;
- Fauna-specific reason-code and obligation mappings when the shared vocabulary designates this lane as their owner;
- compatibility notes necessary to prevent parallel Fauna policy authority;
- this README.

Every candidate must identify:

- policy identity and version;
- status and activation state;
- input profile and schema references;
- output decision profile and schema references;
- default behavior and failure behavior;
- source-role, evidence, rights, sensitivity, review, release, correction, and rollback dependencies;
- evaluator and bundle compatibility;
- deterministic positive and negative tests;
- owner and review burden;
- deactivation and rollback procedure.

### What does not belong here

Do not place the following in this directory:

- Fauna doctrine, glossaries, architecture narratives, or source guidance;
- semantic contracts or JSON Schemas;
- source descriptors, credentials, tokens, cookies, private endpoints, signed URLs, or acquisition instructions containing secrets;
- raw, restricted, steward-controlled, personal, licensed, or sensitive animal records;
- exact or reconstructable sensitive geometry, coordinate-like examples, transformation radii, jitter seeds, or exposure-aiding parameters;
- fixtures, tests, validator code, runtime code, pipeline code, UI code, map styles, tiles, exports, or model prompts;
- EvidenceBundles, receipts, proofs, review records, release manifests, correction notices, or rollback cards;
- legal conclusions, hunting or regulatory advice, emergency alerts, or claims of current agency authority;
- duplicated common policy rules that belong to evidence, rights, consent, privacy, sensitivity, geoprivacy, review, release, or another shared lane;
- speculative paths presented as implemented or active.

When placement is ambiguous, keep the change held and resolve responsibility under Directory Rules. A topic match such as “Fauna” is not enough; responsibility decides the path.

<p align="right"><a href="#top">Back to top</a></p>

---

## Direct lane inventory

The direct lane contains eight tracked files at the reviewed snapshot.

| Path | Observed shape | Current maturity | Proven effect | Missing before activation |
| --- | --- | --- | --- | --- |
| [`README.md`](./README.md) | Directory boundary and index | This v0.2 documentation proposal | Explains scope and current evidence only | Human review and acceptance |
| [`abstain_on_ambiguous.rego`](./abstain_on_ambiguous.rego) | Package `kfm.fauna_abstain_on_ambiguous`; `default deny := false`; example rule commented out | `PROPOSED greenfield stub` | Parses as a Rego source shape if the toolchain accepts it; no observed abstain decision | Accepted semantics, package, input/output contract, operative rules, native tests, bundle/evaluator/consumer |
| [`api_envelope.rego`](./api_envelope.rego) | Package `kfm.generated.policy.domains.fauna.api_envelope`; `default allow := false` | `PROPOSED scaffold` | Default has no positive allow rule | Accepted envelope semantics, decision normalization, tests, bundle/evaluator/consumer |
| [`deny_unpublished.rego`](./deny_unpublished.rego) | Package `kfm.fauna_deny_unpublished`; `default deny := false`; example rule commented out | `PROPOSED greenfield stub` | Does not deny unpublished material by default | Accepted deny semantics, lifecycle/release inputs, tests, bundle/evaluator/consumer |
| [`ebird_redistribution.md`](./ebird_redistribution.md) | Planned-path documentation scaffold | `PROPOSED scaffold` | No rights or redistribution decision | Current source terms, rights authority, review, replacement or retirement decision |
| [`rare_species_redaction.rego`](./rare_species_redaction.rego) | Package `kfm.rare_species_redaction`; `default deny := false`; example rule commented out | `PROPOSED greenfield stub` | Performs no redaction and emits no deny by default | Accepted policy semantics, transform/receipt separation, tests, bundle/evaluator/consumer |
| [`sensitivity.rego`](./sensitivity.rego) | Package `kfm.generated.policy.domains.fauna.sensitivity`; `default allow := false` | `PROPOSED scaffold` | Default has no positive allow rule | Responsibility split with `policy/sensitivity/fauna/`, tier/transform inputs, tests, bundle/evaluator/consumer |
| [`tile_field_allowlist.yaml`](./tile_field_allowlist.yaml) | Closed `FaunaTileFieldAllowlistProfile` v1.0.0; `PROPOSED_INACTIVE_FIXTURE_ONLY` | **Substantive but inactive fixture profile** | Deterministic profile and eight-case fixture replay can return `PASS`, `DENY`, or `ERROR`; all authority claims are fixed false | Production field review, accepted activation record, real tile-byte inspection, evidence/policy/review/release binding, consumer and rollback |

### Direct-lane conflicts that must remain visible

1. **Default polarity conflict:** deny-named modules default `deny` to false, while allow-named modules default `allow` to false.
2. **Decision-shape conflict:** `deny` and `allow` booleans do not form one authenticated finite decision envelope.
3. **Namespace conflict:** packages span `kfm.*` and `kfm.generated.policy.domains.fauna.*`.
4. **Responsibility conflict:** `sensitivity.rego` overlaps the separate `policy/sensitivity/fauna/` lane, whose own files are proposal-only scaffolds.
5. **Activation gap:** no direct bundle manifest, selector, evaluator binding, native Rego suite, decision receipt, consumer, or release integration was observed.

Do not “solve” these conflicts by choosing a filename or default informally. Convergence requires an accepted, dependency-closed policy change with contracts, schemas, fixtures, tests, evaluator compatibility, review, deactivation, and rollback.

<p align="right"><a href="#top">Back to top</a></p>

---

## Policy composition boundary

Fauna policy is one contributor to a composed decision. It cannot override a stricter decision from another owning lane.

| Decision dimension | Primary owner | Fauna composition rule |
| --- | --- | --- |
| Fauna operation and representation | This lane after activation | Evaluate only the bounded Fauna-specific question. |
| Evidence sufficiency | Evidence contracts, resolvers, and evidence policy | Missing or insufficient support cannot be upgraded locally. |
| Source role and authority | Source governance | Preserve role; alias or crosswalk resolution cannot promote authority. |
| Rights and redistribution | Rights policy and source terms | Any deny, restriction, expiry, or unknown state remains binding. |
| Consent, privacy, and living-person risk | Owning cross-cutting policy | Apply the stricter outcome and obligations. |
| Sensitivity and geoprivacy | Fauna sensitivity and geoprivacy lanes | Exact or reconstructable risk remains restricted unless current policy explicitly permits a public-safe derivative. |
| Review and separation of duties | Review policy and repository controls | Policy cannot self-review or self-approve. |
| Lifecycle and release | Lifecycle state plus release authority | Policy may gate a transition but cannot perform or approve it. |
| Correction, withdrawal, and rollback | Owning correction/release mechanisms | New restriction takes precedence; stale allows are invalid. |

### Composition law

Until an accepted composition contract exists, the safe normalization is conceptual only:

1. any authoritative `DENY` remains `DENY`;
2. any required restriction or unresolved mandatory review keeps the operation non-public and held;
3. any missing evidence needed to answer produces abstention or denial appropriate to the surface;
4. any evaluator, input, package, schema, or obligation-processing error fails closed;
5. an allow is usable only when every required lane returns a current compatible result and every obligation is enforceable;
6. no local policy result can create release or publication authority.

This ordering is a README-level safety contract, not proof that the current runtime implements it.

<p align="right"><a href="#top">Back to top</a></p>

---

## Required policy input

An accepted Fauna evaluator must reject or hold an input that cannot prove its identity, version, provenance, and requested operation. The minimum conceptual input is below; exact field names belong to accepted contracts and schemas.

| Input family | Required governed context | Missing, stale, or conflicting behavior |
| --- | --- | --- |
| Request identity | Request ID, operation, audience, public/internal/restricted surface, purpose, authenticated actor or service context | `ERROR` for malformed identity; otherwise `HOLD` or `DENY` |
| Policy identity | Bundle ID, version, digest, selector result, input-profile version, evaluation time | `ERROR`; never fall back to an arbitrary package |
| Domain identity | Canonical `fauna` lane ID and code alias | Unknown or colliding alias → `HOLD` or `ERROR` |
| Object identity | Stable object/candidate ID, object family, contract and schema versions | `HOLD`; malformed shape → `ERROR` |
| Source governance | Source descriptor ref, fixed source role, authority scope, access/terms status, retrieval provenance, source-state hash | Unresolved or expired → `HOLD`, `ABSTAIN`, or `DENY` |
| Taxonomy | Taxon ref, authority/crosswalk provenance, accepted-name state, uncertainty | Do not infer identity; hold or abstain |
| Knowledge character | Observed, reported, modeled, inferred, curated, generalized, aggregated, or unknown | Mismatch or unknown → hold/abstain/deny |
| Evidence | Evidence refs, resolver result, sufficiency for requested claim, caveats, freshness, conflict state | Cite-or-abstain; never synthesize support |
| Rights | License/terms identity, redistribution and derivative permissions, attribution obligations, expiry/withdrawal state | Unknown or incompatible → `DENY` or `HOLD` |
| Sensitivity | Current tier/posture, sensitive-taxon/site flags, reconstruction risk, transform identity, receipt ref, review ref | Missing or incompatible → fail closed |
| Representation | Exact/generalized/aggregated/withheld/non-spatial class, property set, geometry/time precision, intended joins | Unsafe or unreviewed → `RESTRICT` or `DENY` |
| Lifecycle | Current state, candidate/release identity, publication status, supersession, correction and withdrawal state | Unpublished/stale/superseded → hold/deny |
| Time | Observation/event/report/retrieval/processing/validation/release times, valid interval, freshness window | Future, invalid, or stale state → hold/abstain/deny |
| Review | Required roles, completed reviews, independence/separation evidence, unresolved threads or conditions | `HOLD`; no self-approval |
| Correction/rollback | Correction notice, invalidation epoch, cache keys, withdrawal status, rollback target/readiness | Missing for material public edge → `HOLD` |
| Consumer capability | API/UI/map/export/AI consumer ID, obligation support, policy-version support, enforcement acknowledgement | Unsupported obligation or version → `DENY` or `ERROR` |

### Domain and source alias handling

- The reviewed machine projection names the domain `fauna` and code alias `fauna`.
- Unknown domain aliases must not be accepted by normalization convenience.
- Two aliases resolving to different domain identities are a collision and must fail closed.
- Source aliases may resolve only through governed source identity and must preserve source role, authority, terms, and provenance.
- A source name collision, case-fold collision, renamed provider, taxonomy synonym, or aggregator/provider ambiguity must remain `HOLD_UNRESOLVED` until a current governed decision disambiguates it.
- A crosswalk is evidence of mapping, not proof that two authorities, sources, taxa, or observations are interchangeable.

### Input minimization

Policy evaluation should receive the minimum governed facts required for the decision. It must not receive raw sensitive payloads merely for convenience. Prefer stable references, coarse risk classes, boolean/finite predicates, digests, and review state over exact coordinates, identities, private notes, transform parameters, or source payloads.

<p align="right"><a href="#top">Back to top</a></p>

---

## Decision and obligation contract

### Internal policy outcomes

The repository does not yet prove one accepted Fauna decision vocabulary. Until contracts, schemas, shared registries, Rego packages, and consumers converge, use the following as a **required normalization target**, not as a claim about current runtime output:

| Outcome | Meaning | Permitted next step |
| --- | --- | --- |
| `ALLOW` | The bounded operation is admissible under the evaluated context and all obligations are enforceable. | Continue only within the authenticated scope; release/publication remains separate. |
| `RESTRICT` | A narrower representation, audience, field set, time/space precision, or access path is required. | Continue only after every obligation is applied and verified. |
| `HOLD` | Required evidence, rights, sensitivity, review, release, correction, or other authority is unresolved. | Stop consequential processing; route for resolution. |
| `ABSTAIN` | The system cannot support the requested claim or answer from governed evidence. | Return a bounded non-answer with safe reason and citations/caveats where available. |
| `DENY` | The requested operation is incompatible with current policy or authority. | Do not proceed; emit safe reasons and required audit metadata. |
| `ERROR` | Input, evaluator, package, schema, obligation, or consumer processing failed. | Fail closed; do not reuse a prior allow. |

`HOLD_UNRESOLVED` may be used as a reason or normalized hold state where current contracts support it. It must not become a seventh informal success state.

### Required decision fields

An authenticated decision should carry at least:

- decision ID and correlation/request ID;
- policy bundle ID, version, digest, selector identity, and evaluation time;
- canonical domain ID and bounded operation;
- normalized outcome;
- stable reason codes safe for the intended audience;
- obligations and the consumer capabilities required to satisfy them;
- evidence, source, rights, sensitivity, review, release, correction, and rollback refs used by the decision;
- input digest and relevant state/version digests;
- expiry, invalidation epoch, or reevaluation condition;
- audit classification that contains no sensitive payload;
- explicit statement that the decision is not evidence, release, or publication authority.

### Obligation families

Depending on accepted contracts, `RESTRICT` or `ALLOW` may require:

- field removal or an allowlisted field set;
- representation change to generalized, aggregated, withheld, or non-spatial form;
- coarse time bucketing or suppression of temporal detail;
- attribution, terms, and caveat display;
- Evidence Drawer or citation linkage;
- audience/access enforcement;
- no-cache, cache partitioning, short expiry, or invalidation hooks;
- join denial or differencing/reconstruction controls;
- AI abstention or bounded answer templates;
- review, receipt, release, correction, or rollback references;
- monitoring and emergency re-hold triggers.

If a consumer cannot prove it supports a required obligation, the result is not usable as an allow. The safe outcome is `DENY` or `ERROR` for that consumer path.

### Public response normalization

Public applications may normalize internal decisions into a finite response envelope such as `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`, but only through an accepted contract. `ALLOW` is not automatically `ANSWER`; `RESTRICT` may become a bounded answer only after obligations are enforced; `HOLD` is never a public success.

<p align="right"><a href="#top">Back to top</a></p>

---

## Public-surface contract

### Governed API

- Serve only released, current, policy-admissible representations through governed interfaces.
- Enforce authentication, audience, field, geometry, temporal, attribution, and cache obligations.
- Never expose raw/restricted/internal references, policy inputs, private reasons, or exact sensitive values.
- Treat decision expiry, correction, source withdrawal, or policy-version mismatch as an immediate revalidation requirement.

### Map and tiles

- Style hiding is not access control.
- Encoded properties require a reviewed policy allowlist and a compatible layer-manifest allowlist.
- Exact coordinate-like fields, observer/reporter identifiers, raw/internal/restricted refs, signed URLs, tokens, transform radii, offsets, seeds, and other reconstruction aids remain forbidden from public candidates unless a separately accepted policy explicitly proves safety.
- Tile bytes, properties, geometry, metadata, caches, and cross-layer reconstruction must be validated; a profile-only pass is insufficient.

The current fixture-only field profile requires `evidence_ref` and `feature_id`, and its schema fixes every authority claim to false. Those facts are test evidence, not production approval.

### Evidence Drawer and Focus Mode

- Show public-safe evidence references, source role, knowledge character, freshness, sensitivity posture, representation limits, and corrections where the released contract allows them.
- Do not show raw source payload, exact restricted geometry, private review notes, internal identifiers, hidden policy input, or exposure-aiding transform detail.
- A missing or inaccessible evidence path produces abstention or a bounded unavailable state, not invented support.

### Exports

- Apply the same or stricter field, audience, geometry, time, attribution, rights, and invalidation obligations as the interactive surface.
- Do not let a bulk export reconstruct details suppressed in the UI or map.
- Bind the export to current policy and release identities; stale snapshots require revalidation or withdrawal.

### AI and generated language

- Generated language may summarize only governed released claims with resolvable public-safe citations.
- The model cannot infer an occurrence from range, habitat, taxonomy, co-occurrence, or generalized patterns.
- Prompt text, retrieval ranking, model confidence, or a prior answer cannot override evidence, policy, rights, sensitivity, correction, or release state.
- When support or safe disclosure is insufficient, answer with a bounded abstention or denial.

<p align="right"><a href="#top">Back to top</a></p>

---

## Lifecycle and temporal behavior

### Lifecycle boundary

The repository-wide lifecycle remains:

`RAW → WORK or QUARANTINE → PROCESSED → CATALOG or TRIPLET → PUBLISHED`

Policy may evaluate a proposed transition, but it does not move or write the artifact. Receipts, proofs, catalogs, release objects, and published carriers remain distinct stores and authority classes.

| Proposed transition or use | Minimum Fauna policy posture |
| --- | --- |
| RAW intake | Source identity, role, terms, access, sensitivity, and intake purpose are explicit; otherwise quarantine/hold. |
| WORK processing | Preserve source/evidence lineage, knowledge character, sensitivity, rights, and time; no public exposure. |
| QUARANTINE | Default for unresolved source, rights, taxonomy, sensitivity, payload safety, or integrity; quarantine is not rejection or approval. |
| PROCESSED candidate | Contract/schema and semantic validation pass for the bounded object; still non-public. |
| CATALOG/TRIPLET candidate | Role, scope, evidence, sensitivity, rights, join, and representation rules pass; catalog or graph presence is not release. |
| Release candidate | Current evidence, rights, sensitivity/geoprivacy, policy, review, correction, withdrawal, and rollback requirements resolve. |
| PUBLISHED use | Current release identity and policy decision resolve; consumer enforces every obligation. |
| Correction/withdrawal | Restrict, invalidate, or re-hold affected outputs and caches before considering any later re-release. |

### Time semantics

Fauna decisions may depend on observation, event, report, retrieval, processing, validation, policy, review, release, correction, and embargo times. These are not interchangeable.

An accepted evaluator must:

- reject impossible or future-dated provenance where the contract forbids it;
- distinguish observation time from publication or retrieval time;
- evaluate seasonal and valid-time scope without converting it into current occurrence truth;
- require current source, rights, sensitivity, policy, review, and release state at use time;
- expire or invalidate decisions when a governing state changes;
- prevent a stale allow from winning a race against correction, withdrawal, or policy update.

### Race and stale-result handling

If policy state changes during evaluation or delivery:

1. bind the decision to immutable input and policy digests;
2. compare the consumer's state/version before consequential use;
3. reject a stale or mismatched decision;
4. apply a newer restriction, correction, or withdrawal immediately;
5. require fresh evaluation before any relaxation;
6. invalidate affected caches, tiles, exports, indexes, search results, and generated-answer context.

<p align="right"><a href="#top">Back to top</a></p>

---

## Identity, naming, and versioning

### Canonical identity

| Element | Current posture |
| --- | --- |
| Domain lane ID | `fauna` in the proposed machine projection |
| Code alias | `fauna` |
| Human documentation path | `docs/domains/fauna/` |
| Domain policy path | `policy/domains/fauna/` |
| Sensitivity policy path | `policy/sensitivity/fauna/` |
| Direct package namespace | **UNRESOLVED:** current files use both `kfm.*` and `kfm.generated.policy.domains.fauna.*` |
| Bundle identity | **UNKNOWN / not observed** |
| Input/output profile versions | **NEEDS VERIFICATION** |
| Active-policy register or selector | **UNKNOWN / not observed** |

### Naming rules

- Use lowercase kebab-case directory names and the registered `fauna` lane segment.
- Use descriptive lowercase filenames consistent with the accepted policy toolchain.
- Do not encode version solely in a filename when the owning format provides explicit identity/version fields.
- Package names, rule names, decision codes, and obligation codes must be globally collision-checked before activation.
- Do not introduce aliases for `fauna` without a governed alias-register decision.
- Do not let `biodiversity`, `wildlife`, a taxonomic group, a source/provider name, or a UI label become an implicit policy-domain alias.
- Keep source/provider names out of canonical policy identity unless the rule truly owns source-specific admissibility and current terms are governed.

### Versioning rules

A material policy version changes when any of the following changes:

- default result or decision polarity;
- input/output schema or semantics;
- rule logic, precedence, reason code, obligation, or audience;
- rights, sensitivity, geoprivacy, reconstruction, or lifecycle behavior;
- package/bundle identity or selector behavior;
- consumer compatibility or enforcement requirements;
- invalidation, correction, withdrawal, deactivation, or rollback behavior.

Documentation-only clarification may retain policy versions only when it cannot change evaluator or reviewer interpretation. An activated policy version must be immutable, digest-bound, reviewable, reproducible, and recoverable.

### No implicit latest

Consumers must not discover policy by taking the lexically newest filename, last commit, default branch head, or unpinned package. Selection must use an accepted register or bundle manifest and record the exact identity and digest.

<p align="right"><a href="#top">Back to top</a></p>

---

## Validation and failure semantics

### Current executable evidence

| Surface | Current evidence | What it proves | What it does not prove |
| --- | --- | --- | --- |
| Public-safe Fauna fixture validator | [`validate_public_safe_fixture.py`](../../../tools/validators/domains/fauna/validate_public_safe_fixture.py) with [`test_fauna_smoke.py`](../../../tests/domains/fauna/test_fauna_smoke.py) | Seven deterministic standard-library tests over one accepted positive and five fail-closed synthetic fixtures; network denied; safe machine envelope | Real source admission, Fauna truth, production schemas, policy evaluation, evidence closure, geoprivacy transform, release, or publication |
| Occurrence-evidence profile | [`validate_occurrence_evidence.py`](../../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py) with [`test_occurrence_evidence.py`](../../../tests/domains/fauna/test_occurrence_evidence.py) | Eight deterministic no-network tests covering closed shape, exact fixture polarity, source-role mismatch, rights mismatch, stable identity, and value-safe output | Production acceptance, active policy, source authority, release, or public use |
| Tile-field profile | [`validate_tile_field_allowlist.py`](../../../tools/validators/domains/fauna/tiles/validate_tile_field_allowlist.py) with [`test_tile_field_allowlist.py`](../../../tests/domains/fauna/test_tile_field_allowlist.py) | Twelve deterministic no-network tests and eight fixture cases covering closed inactive profile shape, allow/deny polarity, required fields, forbidden patterns, duplicate-key rejection, and authority falsehood | Tile bytes, property values, geometry, size, accessibility, evidence resolution, production field approval, deployment, or publication |
| Domain workflow | [`domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml) | Runs the seven-test fixture-safety slice on PRs and records explicit proof/release holds | No Fauna proof producer, proof pack, release dry-run command, candidate manifest, or public approval |
| Tile workflow | [`fauna-tile-field-allowlist.yml`](../../../.github/workflows/fauna-tile-field-allowlist.yml) | Runs the focused tile-profile unit and fixture suites when its bounded paths change | This README alone does not trigger that path-filtered PR workflow |
| Direct Rego files | Source presence only | Proposed default shapes are inspectable | No accepted common interface, native Rego behavior suite, bundle, evaluator, consumer, or release enforcement |

### Required validation layers before activation

1. **Document and placement:** metadata, links, anchors, authority language, status, Directory Rules, and no parallel authority.
2. **Static policy:** syntax, formatting, unsafe built-ins, package uniqueness, rule uniqueness, import restrictions, deterministic evaluation, and secret/sensitive-content hygiene.
3. **Contract and schema:** exact supported versions, closed machine shape, compatibility rules, finite outcomes, reason/obligation vocabularies, and safe errors.
4. **Semantic invariants:** source role, knowledge character, range/occurrence separation, taxonomy uncertainty, evidence sufficiency, rights, sensitivity, reconstruction, lifecycle, and time.
5. **Fixture polarity:** positive, restrict, hold, abstain, deny, malformed/error, stale, corrected, withdrawn, alias-collision, source-collision, and unsupported-consumer cases.
6. **Composition:** shared evidence, rights, consent/privacy, sensitivity/geoprivacy, review, release, correction, and rollback results combine deterministically and most-restrictively.
7. **Consumer enforcement:** API, UI, map, tile, export, cache, and AI paths authenticate the decision and enforce every obligation.
8. **Lifecycle and release:** promotion cannot bypass policy; correction/withdrawal invalidates public surfaces; rollback is rehearsed.
9. **No-network reproducibility:** focused policy and fixture suites run deterministically without live services or source access.
10. **Exact-head CI:** required workflows run against the reviewed commit; unrelated baseline failures are classified rather than repaired in this lane.

### Minimum negative cases

An activation packet must include at least:

- missing or unresolved EvidenceRef/EvidenceBundle;
- stale, superseded, conflicting, or withdrawn evidence;
- unknown, expired, incompatible, or withdrawn rights;
- source-role promotion and aggregator-as-authority attempts;
- observed/modeled/reported/inferred character collapse;
- range-, habitat-, aggregate-, or generalized-data-as-occurrence claims;
- sensitive taxon/site with missing transform, receipt, review, or release state;
- exact or disguised coordinate, identity, raw/internal ref, private endpoint, or transform-parameter leakage;
- cross-surface reconstruction and temporal differencing;
- domain alias and source alias collisions;
- duplicate keys, duplicate rules, package collisions, and bundle-selector ambiguity;
- unrecognized policy/input/output/consumer version;
- unsupported obligation;
- unpublished, corrected, withdrawn, embargoed, or stale lifecycle state;
- correction racing an older allow;
- evaluator timeout, parse error, partial input, and dependency failure;
- public consumer attempting to reinterpret `HOLD`, `RESTRICT`, or internal reasons as success.

### Failure behavior

| Failure class | Required behavior |
| --- | --- |
| Invalid or ambiguous input | Safe `ERROR` or `HOLD`; no partial allow |
| Missing governing context | `HOLD`, `ABSTAIN`, or `DENY` appropriate to the operation; never guess |
| Policy parse/load/select failure | Fail closed; record safe operational evidence; do not use cached allow unless its contract expressly remains current |
| Policy version/digest mismatch | Reject and re-evaluate with an accepted compatible bundle |
| Obligation cannot be enforced | `DENY` or `ERROR` for that consumer |
| Sensitive/logging risk | Redact operational output; do not emit payload values or exposure-aiding detail |
| Correction/withdrawal arrives | Invalidate and restrict immediately; fresh review required before relaxation |
| Unknown unexpected condition | `ERROR`; no silent fallback to allow |

<p align="right"><a href="#top">Back to top</a></p>

---

## Review burden

Fauna policy is trust-bearing because errors can expose vulnerable species or sites, misstate animal occurrence or status, violate source terms, or create unsafe public inferences.

### Change classification

| Change | Minimum review posture |
| --- | --- |
| README clarification with no semantic change | CODEOWNER route plus documentation and policy-boundary review |
| New or changed default, rule, outcome, reason, obligation, profile, or package | Fauna, policy, contract/schema, validation, and runtime review |
| Source-specific or redistribution rule | Source and rights review plus Fauna/policy review |
| Sensitivity, geoprivacy, field, geometry, time, aggregation, join, or reconstruction rule | Fauna, sensitivity/geoprivacy, security/privacy, policy, validation, and affected consumer review |
| Public API/UI/map/tile/export/AI effect | Consumer, security, accessibility where applicable, release, correction, rollback, and domain/policy review |
| Bundle, selector, evaluator, activation, or required-check change | Governance/ADR assessment, runtime, policy, validation, security, repository-control, and release review |
| Emergency restriction or deactivation | Authorized incident/release control with documented scope, evidence, invalidation, and recovery plan |

### Separation of duties

- Authoring a rule is not approving it.
- CODEOWNERS routing is not independent review.
- A validator author cannot convert validator success into policy or release authority.
- A domain steward cannot waive source rights, sensitivity, security, or release requirements outside delegated authority.
- Runtime maintainers cannot reinterpret policy semantics for convenience.
- Release authority must verify the authenticated decision and obligations; it does not rewrite them.
- Owner self-review, automated review, green CI, mergeability, or merge does not prove independent approval or policy activation.

### Reviewer questions

Reviewers should be able to answer:

1. What exact operation, audience, representation, and lifecycle transition is being decided?
2. Which authority owns every input and how is its identity/digest authenticated?
3. What is the default and how do missing, stale, conflicting, or malformed inputs behave?
4. Can any rule expose or help reconstruct sensitive animal locations or private identities?
5. Can source role, taxonomy, knowledge character, evidence, rights, or release state collapse?
6. Are outcomes, reasons, obligations, expiry, invalidation, and consumer support machine-checkable?
7. Do positive and negative fixtures cover alias collisions, stale decisions, corrections, and failures?
8. Can the change be deactivated and rolled back without deleting evidence or history?
9. Does the PR remain dependency-closed and avoid unrelated policy, runtime, workflow, or data changes?

Human review remains pending until an authorized reviewer records it. A green check is never a substitute.

<p align="right"><a href="#top">Back to top</a></p>

---

## Activation and definition of done

### Current activation state

**No general Fauna domain-policy activation is established by the reviewed repository evidence.** The tile-field profile is explicitly inactive and fixture-only. The direct Rego files are proposed scaffolds. The domain workflow validates only a bounded synthetic fixture-safety slice and deliberately holds proof and release dry-run capabilities.

### Dependency-closed activation packet

Before any Fauna policy is described as active, the repository must provide and review, at minimum:

- accepted domain/sensitivity responsibility split;
- accepted policy package namespace, bundle identity, manifest, selector, and precedence;
- accepted input, decision, reason, obligation, receipt, and audit contracts plus closed schemas;
- deterministic normalized input assembly from governed references;
- explicit safe default and finite failure semantics;
- substantive rules rather than comment-only examples;
- native Rego and host-language unit tests with exact polarity;
- public-safe, synthetic, no-network fixtures including collision, stale, correction, withdrawal, and error cases;
- composition tests with evidence, source, rights, sensitivity/geoprivacy, review, release, correction, and rollback policy;
- evaluator compatibility and pinned tool/runtime versions;
- governed consumer binding and obligation enforcement for every intended surface;
- value-safe observability and decision receipt behavior;
- activation record stating exact version/digest, scope, consumers, reviewers, effective time, and terminal conditions;
- required-check significance and branch/ruleset integration where authorized;
- deactivation switch, cache invalidation, correction propagation, rollback target, and completed drill;
- independent or otherwise explicitly governed review appropriate to the risk;
- separate release authorization for any public artifact.

### Definition of done

A Fauna policy slice is done only when:

- its placement and authority are unambiguous;
- every status and claim is evidence-backed;
- all dependencies are accepted and exact-version-bound;
- defaults and failure modes are fail-closed for consequential use;
- positive and negative tests pass deterministically with no network;
- secrets and sensitive/exposure-aiding values are absent from repository and logs;
- each consumer enforces authenticated obligations;
- review and activation records exist and remain distinct;
- correction, withdrawal, invalidation, and rollback are executable and tested;
- no source, evidence, review, release, or publication authority is implied by policy success;
- exact-head checks are classified and human review is complete.

Until then, describe the artifact as **proposed**, **inactive**, **fixture-only**, **evaluator-unbound**, or **held** as the evidence requires.

<p align="right"><a href="#top">Back to top</a></p>

---

## Contributor workflow

### Before authoring

1. Pin the exact current `main` commit and re-read the target path.
2. Search open PRs and relevant branches for overlapping Fauna policy work.
3. Read accepted ADR-0029, Directory Rules, the `policy/` root, the `policy/domains/` parent, and this README.
4. Inspect current direct files, shared policy vocabularies, sensitivity rules, contracts, schemas, validators, fixtures, tests, evaluator/runtime, consumers, release gates, and rollback paths.
5. Verify issue and repository-control posture before any GitHub mutation.
6. Classify every claim as `CONFIRMED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.
7. Stop or narrow scope when authority, ownership, sensitive handling, or dependency closure is unclear.

### While authoring

- Change only the authorized dependency-closed paths.
- Preserve current main changes and avoid stale prompt snapshots.
- Keep machine shape, semantic meaning, policy, fixtures, tests, data, receipts, proofs, and release records in their owning roots.
- Use synthetic, sanitized, no-network fixtures; never paste real sensitive animal detail.
- Make defaults, outcomes, reasons, obligations, expiry, invalidation, and rollback explicit.
- Add both allow-path and fail-closed negative tests.
- Treat prospective files and commands as proposed until tracked evidence proves them.

### Before requesting review

- run formatting, metadata, link, anchor, sensitive-content, secret, and policy/static checks;
- run focused schema, validator, fixture, native policy, composition, consumer, correction, and rollback tests appropriate to scope;
- verify exact changed paths and remote byte equality;
- compare exact-head hosted failures with the exact base before attributing them;
- document partial-checkout or unavailable-tool limits honestly;
- provide a one-change rollback plan;
- keep the pull request draft until authorized human review is complete.

Do not mark ready, merge, force-push, bypass protection, self-approve, activate policy, promote, release, deploy, publish, alter settings, or widen access merely because checks pass.

<p align="right"><a href="#top">Back to top</a></p>

---

## Correction, reconsideration, and invalidation

### Triggers

Reevaluate or invalidate a Fauna decision when any material dependency changes, including:

- source correction, retraction, role change, access change, terms change, or withdrawal;
- taxonomy revision, synonym/crosswalk correction, status revision, or identification uncertainty;
- new sensitivity classification, site vulnerability, reconstruction finding, or disclosure incident;
- evidence addition, conflict, staleness, supersession, or resolver failure;
- rights, consent, privacy, or policy change;
- transform, receipt, review, candidate, release, or consumer state change;
- policy bundle, rule, default, reason, obligation, input/output schema, evaluator, or consumer version change;
- rollback, emergency deactivation, or incident-response action.

### Reconsideration law

- New restriction applies before any relaxation.
- A previous allow is not durable evidence for a later evaluation.
- Correction must preserve lineage; do not erase the prior decision or supporting record.
- Reconsideration requires current governed inputs and the current accepted policy version.
- A reviewer may return a decision to `HOLD`; review cannot fabricate missing source, evidence, rights, or release authority.
- If public material was affected, invalidate downstream caches, tiles, exports, catalogs, search indexes, AI retrieval context, and derived representations within the governed scope.

### Safe notices

Public correction or withdrawal notices must explain the affected public claim and disposition without revealing the sensitive detail that caused the restriction. Internal audit records may reference governed evidence, but logs and PRs must remain value-safe.

<p align="right"><a href="#top">Back to top</a></p>

---

## Rollback and recovery

### This README change

Rollback is a one-file documentation revert to the prior blob `39b7c7dd859614ab9ae9a72208f693056c97f2c6`. No policy rule, schema, contract, fixture, test, validator, workflow, runtime, data, receipt, proof, release object, deployment, or published artifact changes with this README.

Before merge, close the draft PR and delete only its scoped branch if the proposal is withdrawn. After merge, use a reviewed revert commit; do not rewrite protected history.

### Future policy rollback

An activated Fauna policy rollback must:

1. identify the exact active bundle, version, digest, selector, consumers, and affected decisions;
2. state whether the safe action is re-hold, deactivate, revert, supersede, or restrict;
3. prevent fallback to an older rule set that is incompatible with current contracts, rights, sensitivity, or consumers;
4. invalidate decisions and downstream caches derived from the affected version;
5. preserve audit evidence, receipts, review, corrections, and release history;
6. verify every consumer has stopped accepting the withdrawn version;
7. run deterministic recovery and negative tests;
8. require a fresh reviewed activation before restoring a relaxed public edge.

### Emergency deactivation

Emergency triggers include sensitive-location exposure, private-identity leakage, source-rights withdrawal, unsafe reconstruction, evaluator divergence, package ambiguity, obligation bypass, stale-allow races, corrupted decision identity, or rollback failure.

The safe emergency posture is to **deny or hold affected public operations**, preserve evidence, and route recovery through authorized incident and release controls. Do not delete history, silently patch outputs, or replace a governed decision with an informal exception.

<p align="right"><a href="#top">Back to top</a></p>

---

## Related responsibility roots

| Responsibility | Canonical or current path | Relationship to this lane |
| --- | --- | --- |
| Policy root | [`policy/README.md`](../../README.md) | Canonical admissibility-root contract |
| Domain-policy parent | [`policy/domains/README.md`](../README.md) | Domain lane inventory, composition, and activation boundary |
| Fauna sensitivity policy | [`policy/sensitivity/fauna/`](../../sensitivity/fauna/README.md) | Proposed sensitivity/geoprivacy specialization; not yet accepted active policy |
| Fauna doctrine | [`docs/domains/fauna/`](../../../docs/domains/fauna/README.md) | Human scope, objects, source roles, lifecycle, and safety guidance |
| Fauna policy guidance | [`docs/domains/fauna/POLICY.md`](../../../docs/domains/fauna/POLICY.md) | Draft human policy/sensitivity posture; not executable authority |
| Sensitivity summary | [`SENSITIVITY_POSTURE.md`](../../../docs/domains/fauna/SENSITIVITY_POSTURE.md) | Draft public summary of deny-by-default posture |
| Semantic contracts | [`contracts/domains/fauna/`](../../../contracts/domains/fauna/README.md) | Meaning and invariants |
| Machine schemas | [`schemas/contracts/v1/domains/fauna/`](../../../schemas/contracts/v1/domains/fauna/README.md) | JSON shape and validation vocabulary |
| Source registry | [`data/registry/sources/fauna/`](../../../data/registry/sources/fauna/README.md) | Source identity/admission projection; cannot self-authorize |
| Fixtures | [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) | Synthetic positive and negative examples |
| Tests | [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) | Executable proof and regression guards |
| Validators | [`tools/validators/domains/fauna/`](../../../tools/validators/domains/fauna/README.md) | Deterministic validation implementations |
| Pipeline specs | [`pipeline_specs/fauna/`](../../../pipeline_specs/fauna/README.md) | Declarative run intent; current profiles remain placeholders |
| Pipelines | [`pipelines/domains/fauna/`](../../../pipelines/domains/fauna/README.md) | Execution boundary; current Python modules are tiny scaffolds |
| Shared package | [`packages/domains/fauna/`](../../../packages/domains/fauna/README.md) | Helper implementation boundary, not policy authority |
| Domain workflow | [`domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml) | Fixture-safety validation plus explicit proof/release holds |
| Proof lane | [`data/proofs/fauna/`](../../../data/proofs/fauna/README.md) | Draft proof boundary; no accepted producer observed |
| Receipt lane | [`data/receipts/fauna/`](../../../data/receipts/fauna/README.md) | Process-memory boundary; receipt is not evidence or approval |
| Release candidates | [`release/candidates/fauna/`](../../../release/candidates/fauna/README.md) | Candidate review boundary; a candidate is not a release |
| Rollback support | [`release/rollback/fauna/`](../../../release/rollback/fauna/README.md) | Fauna rollback support boundary |
| Public carrier | [`data/published/fauna/`](../../../data/published/fauna/README.md) | Governed published carrier only after release; never a direct policy output |
| Explorer surface | [`apps/explorer-web/src/features/domains/fauna/`](../../../apps/explorer-web/src/features/domains/fauna/README.md) | Public client feature boundary; must consume governed interfaces |

### Cross-domain seams

Habitat, Flora, Hydrology, Agriculture, Hazards, Atmosphere, Geology, People/DNA/Land, and other lanes may provide context, but they do not inherit Fauna occurrence or sensitivity authority. A relation or join must preserve both domains, both evidence paths, source roles, uncertainty, sensitivity, and release state.

The [`Habitat × Fauna thin-slice ADR`](../../../docs/adr/ADR-habitat-fauna-thin-slice.md) remains draft/proposed. It does not activate a proof harness or authorize a cross-domain public product.

<p align="right"><a href="#top">Back to top</a></p>

---

## Governing decisions and doctrine

| Authority | Status and effect |
| --- | --- |
| [`ADR-0029`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED.** Adopts the exact Directory Rules bytes and the responsibility-first placement model. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) | Adopted exact-byte doctrine through ADR-0029; one canonical writer, domain-as-segment, explicit lifecycle/exposure/mutability/retention, reversible migration. |
| [`policy/README.md`](../../README.md) | Canonical `policy/` root boundary: admissibility without semantic, schema, evidence, runtime, lifecycle, release, or publication collapse. |
| [`policy/domains/README.md`](../README.md) | Parent domain-policy inventory and activation contract; records mixed maturity and general evaluator holds. |
| [`domain_lane_register.yaml`](../../../control_plane/domain_lane_register.yaml) | `PROPOSED`, machine-projection-only register; records Fauna identity and T4 baseline but creates no authority. |
| [`ADR-habitat-fauna-thin-slice.md`](../../../docs/adr/ADR-habitat-fauna-thin-slice.md) | Draft, unassigned, proposed cross-domain proof boundary; no accepted implementation or activation. |
| [CODEOWNERS](../../../.github/CODEOWNERS) | Review routing only; not stewardship, approval, activation, release, or publication authority. |
| [Repository-control issue #1675](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1675) | Incident and control evidence; current repository projection remains non-self-authorizing and denies ready/merge/release/deploy/publish powers absent bounded authorization. |

No README, ADR proposal, machine projection, issue, workflow, merge, or green check can silently promote a proposed Fauna policy into active runtime authority.

<p align="right"><a href="#top">Back to top</a></p>

---

## Open verification register

| ID | Question or gap | Current disposition | Closure evidence required |
| --- | --- | --- | --- |
| `FAUNA-POL-001` | Who holds accepted Fauna, taxonomy, source, rights, sensitivity, policy, runtime, release, and rollback stewardship? | `NEEDS VERIFICATION` | Reviewed assignments and eligible reviewer identities |
| `FAUNA-POL-002` | What is the accepted package namespace and bundle identity? | `HOLD_UNRESOLVED` | Contract, manifest, selector, collision scan, tests, activation record |
| `FAUNA-POL-003` | Should direct `sensitivity.rego` remain here or converge into `policy/sensitivity/fauna/`? | `HOLD_UNRESOLVED` | Responsibility decision and compatibility/rollback plan |
| `FAUNA-POL-004` | What normalized decision, reason, obligation, and receipt vocabulary is accepted? | `HOLD_UNRESOLVED` | Contracts, closed schemas, registry status, consumer tests |
| `FAUNA-POL-005` | Which default-result semantics replace the current allow/deny polarity conflict? | `HOLD_UNRESOLVED` | Accepted semantics plus negative/native Rego tests |
| `FAUNA-POL-006` | Which input assembler authenticates source, taxonomy, evidence, rights, sensitivity, lifecycle, review, and release refs? | `UNKNOWN` | Deterministic implementation, schemas, fixtures, value-safe logs |
| `FAUNA-POL-007` | Which evaluator and toolchain versions load Fauna policy? | `UNKNOWN` | Pinned runtime, compatibility matrix, no-network tests |
| `FAUNA-POL-008` | Which consumers enforce obligations and reject unsupported versions? | `UNKNOWN` | API/UI/map/tile/export/AI conformance tests |
| `FAUNA-POL-009` | What current source-specific rights rule replaces the eBird scaffold? | `HOLD_UNRESOLVED` | Current terms evidence, rights review, source identity, expiry behavior |
| `FAUNA-POL-010` | Which sensitivity tiers, transforms, and reconstruction tests are accepted? | `HOLD_UNRESOLVED` | Sensitivity/geoprivacy review, fixtures, receipts, cross-surface tests |
| `FAUNA-POL-011` | How are domain/source alias collisions resolved without authority promotion? | `HOLD_UNRESOLVED` | Governed alias/identity resolver and exact collision fixtures |
| `FAUNA-POL-012` | Where are authenticated decision receipts retained and how are values minimized? | `UNKNOWN` | Receipt contract/schema/store, redaction rules, access and retention policy |
| `FAUNA-POL-013` | What binds policy to promotion and release without giving policy release authority? | `UNKNOWN` | Candidate/release contract, evaluator result binding, separation-of-duty tests |
| `FAUNA-POL-014` | How do correction, withdrawal, stale-result races, and cache invalidation propagate? | `UNKNOWN` | End-to-end correction/invalidation tests and rollback drill |
| `FAUNA-POL-015` | Is the tile-field profile suitable for production activation? | `NO — fixture-only` | Separate reviewed production profile, real tile inspection, consumers, evidence/release binding |
| `FAUNA-POL-016` | Which hosted checks become required for active Fauna policy? | `NEEDS VERIFICATION` | Authorized ruleset decision and stable exact-head evidence |

Unresolved items remain held. Do not fill them by inference or treat a proposed path as completed implementation.

<p align="right"><a href="#top">Back to top</a></p>

---

## Last-reviewed evidence

### Review record

| Field | Value |
| --- | --- |
| Review date | 2026-08-13 |
| Repository snapshot | `main@9fa82de35cb665840a071013fb5f1813fcc05a6a` |
| Prior target blob | `39b7c7dd859614ab9ae9a72208f693056c97f2c6` |
| Review route | `/policy/` → `@bartytime4life` in CODEOWNERS |
| Human approval | Pending; not asserted by this README |
| Direct lane | Eight tracked files: README, five proposed Rego scaffolds, one proposed rights scaffold, one inactive fixture-only YAML profile |
| Direct policy consumers | No package-name reference beyond defining files observed for the five Rego packages |
| Direct policy activation | Not established |
| Accepted executable domain slice | Seven-test synthetic public-safe fixture suite in `domain-fauna.yml` |
| Adjacent focused suites | Eight declared occurrence-evidence tests; twelve declared tile-field-profile tests |
| Proof/release posture | Explicit workflow holds; no accepted Fauna proof producer or release dry-run command/candidate manifest contract |
| Control posture | Draft PR authoring only for the bounded documentation task; no ready, merge, release, deployment, publication, or settings authority |

### Evidence ledger

| Evidence | Blob | Finding used here |
| --- | --- | --- |
| Policy root README | `6c5021f9d92778581a4e9331a9dd6ddb7efc5e35` | Canonical singular policy responsibility and mixed-maturity posture |
| Domain-policy parent | `ed9be975c9da2c7d77d94fab621db39f23953813` | Domain policy inventory, composition, evaluator and release holds |
| ADR-0029 | `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62` | Accepted Directory Rules decision |
| Directory Rules | `fd49a0b83e55cef52c1124281f093e263526898d` | Responsibility-first placement, domain-as-segment, authority separation, reversibility |
| Domain-lane register | `1bfc6f91cfa713a5e3d51ece011b63b46310734f` | Proposed machine projection of `fauna`, code alias, docs path, and T4 baseline |
| Fauna docs README | `ab08f2d63e03d37ff8cd9f308720c3503bfdb58f` | Draft doctrine, sensitive-location fail-closed posture, domain scope |
| Fauna policy guide | `36f9ddaa5dd3ce7d2f8499ae3ca18acbbdfe772c` | Draft policy/sensitivity guidance and finite public outcomes |
| Fauna sensitivity summary | `b24f0c16bde517a58038e26e1ab082ae6c486c44` | Draft public summary; most-restrictive unresolved posture |
| Fauna contracts README | `192f680bc2ebdc69a9f76fcb986aac168601a1e3` | Semantic-contract/non-policy/non-release separation |
| Fauna schemas README | `4bd3dd8696a5c29a8c746aced9cf14604e272d16` | Machine-shape responsibility and mixed maturity |
| Fauna fixtures README | `dd02bd0d50aa880b718bcd12a95ca46773ff42c1` | Accepted bounded fixture inventory and non-authority limits |
| Fauna tests README | `72e93e4abcf48567942fb1a3a588944df1c83e3c` | Seven-test accepted fixture slice and broader holds |
| Fauna validators README | `f5d4d8a299318fb2eda45f9a987c7c02843434cd` | Current deterministic validator families and limitations |
| Domain workflow | `69b28755f933cd9d1f786058143211d82a102598` | One accepted fixture-safety job; proof and release holds |
| Direct policy files | See metadata block | Proposed default shapes, inactive fixture profile, no activation evidence |

This review proves only the bounded repository facts recorded above. It does not prove exhaustive runtime behavior, GitHub ruleset enforcement, independent review, active source state, policy activation, release safety, deployment, or publication.

<p align="right"><a href="#top">Back to top</a></p>

---

## Revision history

| Version | Date | Change | Rollback |
| --- | --- | --- | --- |
| Unversioned scaffold | 2026-06-15 | Created the short greenfield directory placeholder. | Restore prior Git history if needed. |
| v0.2 | 2026-08-13 | Reconciles accepted directory governance, direct policy inventory and default conflicts, T4 baseline projection, current deterministic Fauna validation slices, policy composition, input/output/lifecycle/public-surface contracts, contributor/review burden, activation gates, correction, rollback, evidence, and open verification without changing executable behavior. | Revert this README-only commit to blob `39b7c7dd859614ab9ae9a72208f693056c97f2c6`. |

---

KFM rule: Fauna policy may decide only from explicit current governed context, must fail closed when that context or its enforcement path is incomplete, and must never let a source name, scaffold, validator, workflow, receipt, proof, map, export, or generated answer substitute for animal evidence, rights, sensitivity review, release, correction, or rollback.

<p align="right"><a href="#top">Back to top</a></p>
