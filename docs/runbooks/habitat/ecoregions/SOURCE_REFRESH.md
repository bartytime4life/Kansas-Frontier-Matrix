<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/habitat/ecoregions/source-refresh
title: Habitat Ecoregions Source Refresh Inspection Runbook
type: runbook
version: v0.1.0
status: draft; repository-grounded; documentation-only; inspection-and-handoff-only; source-inactive-by-default; fail-closed; non-activation; non-review; non-promotion; non-release; non-deployment; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Habitat, ecoregions, Spatial Foundation, source, connector, rights, sensitivity/geoprivacy, evidence, policy, validation, review, correction, rollback, release, security, and operations stewards"
created: NEEDS VERIFICATION — prior file was an unversioned scaffold
updated: 2026-08-25
policy_label: public-review; habitat; ecoregions; source-refresh-inspection; regionalization-context; rights-aware; join-sensitivity-aware; fail-closed; no-publication-authority
current_path: docs/runbooks/habitat/ecoregions/SOURCE_REFRESH.md
owning_root: docs/
responsibility: >-
  Inspect an immutable source-head signal produced by an already-authorized source
  operation, classify bounded no-change or material-change evidence, and prepare a
  non-authoritative handoff without contacting upstream, changing source or lifecycle
  state, applying policy or review, or promoting, releasing, deploying, or publishing.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
canonical_relationship: >-
  Existing direct child of docs/runbooks/habitat/ecoregions/, reconciled in place under
  the adopted docs/ responsibility boundary. It is narrower than the domain-wide
  Habitat source-refresh runbook. The local README remains a one-byte placeholder.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 434195e8727e6e8649fd6a9e7de06808c3e15261
  target_prior_blob: d4cc1c429c7d2894cbb5f2b70eb3e36863cd6490
  local_readme_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  habitat_source_refresh_runbook_blob: 80a91eedd27b369963ebe7a12d9ef5a0e75aa769
  ecoregions_domain_charter_blob: fe9a5a90cc540fb68dfee6f2c420947c728ea7e8
  ecoregions_source_registry_readme_blob: 55ea86c6eb12456570a47b630315329c34aa45c8
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  habitat_connector_compatibility_blob: 62e0a0df3934eb2dc534960be8f49e5079351091
  ecoregions_pipeline_spec_readme_blob: f1d32230ba95e233a1f523e7a851c4e51ec3181a
  ecoregions_pipeline_readme_blob: fbe2a74412cb88e299db5532b27c541f5c95cf67
  ecoregions_fixture_readme_blob: 87a3e10ff24be8146b7a4a704becc73b984a1a8d
  ecoregions_test_readme_blob: c58907150611f231d6b61db306f8de07e53c98c8
  habitat_policy_readme_blob: cf6dd24db1a06cb857806c000500471bbe918ad7
  habitat_workflow_blob: 59771c027f688d7028a46c4635c0ec710b34e3ab
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - ./README.md
  - ../SOURCE_REFRESH_RUNBOOK.md
  - ../NO_NETWORK_TEST_RUNBOOK.md
  - ../PROMOTION_RUNBOOK.md
  - ../ROLLBACK_RUNBOOK.md
  - ../../../domains/habitat/sublanes/ecoregions.md
  - ../../../doctrine/directory-rules.md
  - ../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../data/registry/sources/habitat/ecoregions/README.md
  - ../../../../connectors/habitat/README.md
  - ../../../../pipeline_specs/habitat/ecoregions/README.md
  - ../../../../pipelines/domains/habitat/ecoregions/README.md
  - ../../../../fixtures/domains/habitat/ecoregions/README.md
  - ../../../../tests/domains/habitat/ecoregions/README.md
  - ../../../../policy/domains/habitat/README.md
  - ../../../../.github/workflows/domain-habitat.yml
tags: [kfm, habitat, ecoregions, runbook, source-refresh, source-head, framework, hierarchy, material-change, no-network, rights, sensitivity, geoprivacy, evidence, fail-closed]
notes:
  - "Replaces a 779-byte proposal scaffold with a repository-grounded inspection procedure."
  - "No admitted ecoregion descriptor, activation decision, active spec, executable comparison profile, ecoregion fixture payload, ecoregion test module, accepted Habitat policy bundle, or ecoregion refresh workflow was verified."
  - "Legacy role words authority, context, and model do not override the documented canonical roles: observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic."
  - "This document creates no source, network, lifecycle, evidence, policy, review, promotion, release, deployment, or public effect."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Ecoregions Source Refresh Inspection Runbook

> Inspect a separately produced immutable source-head signal and prepare a bounded handoff. This runbook is not a connector, watcher, scheduler, source-admission decision, network client, pipeline, policy evaluator, lifecycle writer, reviewer, release service, or publisher.

> [!IMPORTANT]
> **Current determination at `main@434195e8727e`: `HOLD — NO ACTIVE HABITAT ECOREGIONS SOURCE REFRESH PATH ESTABLISHED`.** The source-authority projection has `entries: []`; the ecoregion registry child has no descriptor payload; the Habitat connector path is documentation-only; the ecoregion pipeline-spec, pipeline, fixture, and test lanes do not establish executable refresh behavior; Habitat policy has no accepted bundle or evaluator; and the Habitat workflow contains no ecoregion refresh job.

> [!CAUTION]
> A public page, source name, endpoint, schedule, HTTP status, `ETag`, modified time, checksum, map layer, changed upstream page, PR, or green workflow is not source admission, activation, ecological evidence, accountable review, promotion, release, deployment, or publication.

> [!WARNING]
> Do not place credentials, private endpoints, restricted source payloads, exact or reconstructable rare-species/plant locations, nests, dens, roosts, hibernacula, spawning or breeding sites, stewardship/cultural/archaeological/private-land details, sensitive infrastructure, redaction offsets, or controlled joins in packets, logs, issues, PRs, screenshots, maps, or generated text.

**Navigate:** [Purpose](#purpose) · [Authority](#authority) · [Repository state](#repository-state) · [Semantics](#semantics) · [Outcomes](#outcomes) · [Preconditions](#preconditions) · [Packet](#packet) · [Procedure](#procedure) · [Materiality](#materiality) · [Rights and sensitivity](#rights-and-sensitivity) · [Validation](#validation) · [Handoff](#handoff) · [Open verification](#open-verification) · [Evidence](#evidence) · [Rollback](#rollback) · [Non-effects](#non-effects)

---

<a id="purpose"></a>

## Purpose

Use this runbook only after a separately authorized source operation has produced prior and current immutable, non-sensitive source-head signals. The procedure:

1. freezes repository, source, framework, hierarchy, version, producer, and comparison-profile identity;
2. verifies that admission, activation, source role, rights, sensitivity, cadence, connector ownership, and review routes already exist in their owning systems;
3. compares immutable inputs offline with an accepted source-specific profile;
4. classifies a finite inspection outcome;
5. records evidence, limitations, and non-effects; and
6. stops after a non-authoritative handoff.

This file is subordinate to [`../SOURCE_REFRESH_RUNBOOK.md`](../SOURCE_REFRESH_RUNBOOK.md). It adds ecoregion-specific checks for framework identity, classification level, native codes and hierarchy, boundary lineage, geometry/CRS, crosswalk loss, context joins, and reconstruction risk.

A successful run does **not** create or update a `SourceDescriptor`, activation decision, source payload, lifecycle object, EvidenceBundle, proof, policy result, review approval, promotion, release, deployment, publication, or ecological conclusion.

[Back to top](#top)

---

<a id="authority"></a>

## Authority and negative authority

| Concern | Owning surface | This runbook may do | It must not do |
|---|---|---|---|
| Ecoregion meaning | Habitat doctrine and accepted contracts | Require framework/version/hierarchy checks | Redefine ecoregions, occurrences, habitat patches, or regulatory designations |
| Source identity/admission | Accepted source registry and authority objects | Require exact resolvable refs | Mint, admit, activate, suspend, or withdraw a source |
| Source access | One accepted source-first connector/source-edge runtime | Inspect an already-produced signal | Authenticate, schedule, probe, or fetch |
| Source role | Accepted descriptor vocabulary/policy | Verify preservation and expose conflict | Upgrade candidate, aggregate, administrative, or modeled material into observed/regulatory truth |
| Rights/sensitivity | Accepted policy and accountable review | Require finite state and obligations | Infer permission, expose protected detail, or invent transforms |
| Lifecycle/evidence | Governed data/evidence writers | Reference immutable objects | Write lifecycle state or manufacture evidence/proof |
| Materiality | Accepted source-specific comparison profile | Report bounded offline results | Invent thresholds or reuse an unrelated profile |
| Neighbor-domain truth | Owning domain | Preserve refs and ownership | Absorb species, plant, water, soil, hazard, cultural, land, or infrastructure authority |
| Promotion/release | Accountable release operations | Identify prerequisites | Promote, approve, release, deploy, or publish |

The existing target is human operational documentation under `docs/runbooks/`. Accepted ADR-0029 and Directory Rules support a same-path `PLACE` reconciliation. This change creates no new root, alias, mirror, registry, connector, schema, contract, policy, test, fixture, receipt, proof, release, or publication home.

[Back to top](#top)

---
<a id="repository-state"></a>

## Current repository state

Pinned to `main@434195e8727e6e8649fd6a9e7de06808c3e15261`:

| Surface | CONFIRMED evidence | Bounded result |
|---|---|---|
| Target | 779-byte proposal scaffold | No operating behavior |
| Local runbook README | One newline | Navigation/ownership remain `NEEDS VERIFICATION` |
| Domain-wide Habitat refresh runbook | Substantive inspection-only procedure | This file remains narrower and subordinate |
| Ecoregion charter | Regionalization-context intent plus older implementation-unknown and legacy-role wording | Doctrine pressure, not activation/runtime proof |
| Source-authority register | `PROPOSED`, projection-only, implementation `ABSENT`, `entries: []` | No central admission or activation |
| Ecoregion registry child | Only `.gitkeep` and README | No descriptor, activation, source head, or receipt payload |
| Registry topology | Subtype-first versus domain-first conflict documented | Do not choose a writable home by convenience |
| Roles | Canonical seven-role vocabulary conflicts with legacy `authority/context/model` wording | Mapping requires review |
| `connectors/habitat/` | Documentation-only compatibility index; no runtime package established there | No Habitat-scoped fetch path |
| Ecoregion pipeline spec | README-only; referenced exact YAML absent | No active spec/parser/registry/scheduler/consumer |
| Ecoregion pipeline | Intended responsibility documented | No executable refresh behavior proved |
| Ecoregion fixtures/tests | Each child contains only `.gitkeep` and README | No comparison payload, test module, or pass rate |
| Habitat policy | Proposed scaffolds; no accepted bundle or bound evaluator | No operational authorization |
| Habitat workflow | Synthetic land-cover materiality only; proof/release held | Not ecoregion refresh, evidence, policy, or release |

Current operational outcome:

```text
HOLD — NO ACTIVE HABITAT ECOREGIONS SOURCE REFRESH PATH ESTABLISHED
```

[Back to top](#top)

---

<a id="semantics"></a>

## Ecoregion semantics and anti-collapse

Ecoregions are **regionalization context** under a named framework, hierarchy, version, and boundary lineage. They do not independently prove species/plant occurrence, habitat-patch quality, legal designation, hydrologic/soil/hazard/agricultural truth, or public-release safety.

Keep framework, hierarchy, source version, canonical role, native identity, KFM identity, source geometry, derived geometry, time, evidence, context joins, and representation state separate.

```text
public page -> admitted source                         # forbidden
draft descriptor -> activation                         # forbidden
source-head signal -> EvidenceBundle                   # forbidden
ecoregion polygon -> occurrence or habitat quality    # forbidden
ecoregion context -> regulatory designation           # forbidden
EPA/Omernik -> USFS/Bailey                             # forbidden
Level III -> Level IV                                  # forbidden
native code -> universal identity                      # forbidden
crosswalk -> lossless equivalence                      # forbidden
newer version -> silent supersession                   # forbidden
HTTP 200, ETag, or digest -> authority or rights       # forbidden
comparison PASS -> accountable review                  # forbidden
green CI, map visibility, or generated text -> release # forbidden
```

Canonical roles documented by the registry are `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`. Legacy `authority`, `context`, or `model` text requires an explicit reviewed mapping. `context` is a use case, not an approved role. Missing/conflicted mapping yields `HOLD` or `REVIEW_REQUIRED`.

[Back to top](#top)

---

<a id="outcomes"></a>

## Finite inspection outcomes

These classify inspection work only; they are not API responses, policy decisions, lifecycle states, promotion decisions, or releases.

| Outcome | Meaning | Next step |
|---|---|---|
| `NO_CHANGE_CANDIDATE` | Accepted profile found no material difference within declared scope | Record and hand off; do not claim universal freshness/approval |
| `MATERIAL_CHANGE_CANDIDATE` | Supported differences may affect identity, rights, framework, hierarchy, geometry, time, role, or obligations | Freeze and route to accountable owners |
| `REVIEW_REQUIRED` | Evidence is ambiguous or accountable judgment is needed | Stop automation and obtain review |
| `HOLD` | A prerequisite, authority, owner, descriptor, activation, rights/sensitivity state, connector, profile, or rollback route is unresolved | Do not fetch or mutate state |
| `DENY` | Known rights, sensitivity, security, terms, or trust controls prohibit handling | Stop and preserve only safe evidence |
| `ERROR` | Deterministic inspection or input integrity failed | Preserve diagnostics and retry only after resolution |

`NO_CHANGE_CANDIDATE` is not “current”; `MATERIAL_CHANGE_CANDIDATE` is not an accepted update; `REVIEW_REQUIRED` is not approval; and no outcome is promotion, release, deployment, or publication.

[Back to top](#top)

---

<a id="preconditions"></a>

## Preconditions and stop conditions

All must resolve before inspection:

- exact repository commit and stable `source_id`;
- accepted descriptor reference/digest and activation decision/effective state;
- one accepted source-first producer/connector and authorized source operation;
- canonical source role plus reviewed mapping for legacy wording;
- framework, hierarchy system, level, edition, native identity rules, and extent;
- finite rights, terms, attribution, redistribution, derivative, caching, and citation obligations;
- finite source and join sensitivity/geoprivacy state;
- immutable, non-sensitive, comparable prior/current signals;
- accepted deterministic no-network profile for the exact source family/version pair;
- declared canonicalization, assessed fields, exclusions, geometry handling, and finite outputs;
- resolvable source, rights, sensitivity, validation, evidence, policy, review, correction, rollback, and release owners;
- correction/rollback path for affected released state; and
- no overlapping migration, branch, or PR owning the same source operation.

Stop with `HOLD`, `DENY`, or `ERROR` when any item is unresolved; registry topology must be guessed; roles conflict; framework/level/version is unknown; producer profiles differ without review; refs/digests fail; rights/sensitivity changed or are unknown; protected detail appears; live access is required; the profile is proposed or unrelated; shape drift invalidates comparison; correction/withdrawal is unresolved; or the requested action would write lifecycle/evidence/policy/release/public state.

Current repository evidence does not close these preconditions. Do not simulate them with placeholders.

[Back to top](#top)

---

<a id="packet"></a>

## Required inspection packet

Use minimum non-sensitive metadata and immutable refs, not copied payloads.

| Required field | Purpose |
|---|---|
| `inspection_id`, `repository_ref` | Stable inspection and exact controls |
| `source_id`, `source_descriptor_ref`, `activation_decision_ref` | Identity, admission, and allowed operation |
| `source_operation_ref` | Producer run/job/receipt that emitted the signal |
| `canonical_source_role`, optional legacy role/mapping ref | Role traceability |
| `framework_id`, `framework_version`, `hierarchy_system`, `hierarchy_level` | Regionalization scope |
| `native_extent`, `native_crs` | Spatial support |
| prior/current source-head refs and digests | Immutable comparison inputs |
| publication/effective/observed/recorded times | Distinct temporal evidence |
| `rights_ref`, `sensitivity_ref` | Obligations and restrictions |
| `comparison_profile_ref`, `comparison_scope` | Exact accepted method, fields, exclusions |
| `correction_ref`, `rollback_ref` | Required when released state may be affected |
| `review_routes`, `non_effects` | Accountable handoff and explicit boundary |

Illustrative shape only—not an active schema or source record:

```yaml
inspection_id: kfm://inspection/habitat/ecoregions/EXAMPLE
repository_ref: 434195e8727e6e8649fd6a9e7de06808c3e15261
source:
  source_id: SOURCE_ID_REQUIRED
  source_descriptor_ref: DESCRIPTOR_REF_REQUIRED
  activation_decision_ref: ACTIVATION_REF_REQUIRED
  source_operation_ref: PRODUCER_REF_REQUIRED
  canonical_source_role: ROLE_REQUIRED
ecoregion_scope:
  framework_id: FRAMEWORK_REQUIRED
  framework_version: VERSION_REQUIRED
  hierarchy_system: HIERARCHY_REQUIRED
  hierarchy_level: LEVEL_REQUIRED
  native_extent: EXTENT_REQUIRED
  native_crs: CRS_REQUIRED
source_heads:
  prior_ref: PRIOR_REF_REQUIRED
  current_ref: CURRENT_REF_REQUIRED
  prior_digest: PRIOR_DIGEST_REQUIRED
  current_digest: CURRENT_DIGEST_REQUIRED
governance:
  rights_ref: RIGHTS_REF_REQUIRED
  sensitivity_ref: SENSITIVITY_REF_REQUIRED
  comparison_profile_ref: PROFILE_REF_REQUIRED
  comparison_scope: SCOPE_REQUIRED
  review_routes: []
outcome:
  status: HOLD
  reasons: [EXAMPLE_ONLY_NOT_OPERATIONAL]
  non_effects: [no_network, no_lifecycle_write, no_policy_review_release_or_publication]
```

Optional HTTP metadata is permitted only when the authorized producer captured it safely. Hashes prove integrity only—not truth, authority, rights, or public safety.

[Back to top](#top)

---

<a id="procedure"></a>

## Procedure

1. **Freeze authority and scope.** Record exact repo, source, framework, versions, level, extent, descriptor, activation, producer, profile, owners, overlap, and non-goals. Inexact identity yields `HOLD`.
2. **Verify packet integrity.** Check required fields, immutable refs/digests, comparable producer profiles, distinct times, and absence of secrets/protected data. Never guess repairs.
3. **Resolve admission and activation.** Confirm source ID, accepted descriptor, allowed operation, effective versions, and authority limits. A README, placeholder YAML, proposed register, filename, or endpoint is insufficient.
4. **Resolve role and ecoregion scope.** Confirm canonical role, legacy mapping, framework/version, hierarchy/level, native codes/names/parents, extent, and source vintage. Reject substitution.
5. **Resolve rights and sensitivity.** Compare effective obligations and join risk. A rights/sensitivity change can be material even with identical bytes. Uncertainty yields `HOLD` or `DENY`.
6. **Resolve time and geometry lineage.** Compare publication/effective time, CRS/axis/units/scale/extent, feature identity, topology, boundary version, and native versus normalized/generalized/tiled geometry.
7. **Select the profile.** It must be accepted for the exact source/versions, deterministic, no-network, shape-aware, explicit about canonicalization/exclusions/geometry, replayable, finite, and read-only. Otherwise `HOLD`. Never substitute the Habitat land-cover materiality profile.
8. **Compare offline.** Assess declared immutable inputs only: identity, activation, role, framework, hierarchy, version/time, IDs/labels/parents, feature inventory, geometry/CRS/topology, rights/sensitivity, correction/supersession, producer/profile versions, and exclusions. Do not make a live request to resolve ambiguity.
9. **Classify and document.** Use one finite outcome; record reason codes, refs, scope, exclusions, differences, obligations, and result digest.
10. **Hand off and stop.** Route only the bounded packet. Do not fetch, write lifecycle data, update descriptors/activation, modify connectors, create evidence/proof, apply policy, approve review, update catalogs, rebuild public carriers, create release candidates, promote, release, deploy, publish, or generate ecological conclusions.

### No-change candidate

Use only when every material dimension inside profile scope is equivalent and no unresolved obligation exists. Required wording:

> The accepted offline comparison profile found no material difference between the referenced prior and current source-head signals within the declared scope.

Do not say the source is current, accurate, approved, or ready to republish. Route the packet to the accountable source owner.

### Material-change candidate

Possible classes include source/provider identity; descriptor/activation; role; framework/hierarchy; native IDs/parents; edition/effective time; feature inventory; geometry/extent/CRS/topology; rights/attribution/sensitivity; endpoint/packaging; profile comparability; and correction/withdrawal/deprecation.

Route by responsibility: source authority; rights; sensitivity; Habitat/ecoregions and Spatial Foundation; contracts/schemas; source-first connector/security; pipeline/spec/validator/fixture/test; evidence; policy; and release/correction/rollback. Then stop.

[Back to top](#top)

---

<a id="materiality"></a>

## Ecoregion materiality routing

This is guidance, not an accepted score or numeric threshold.

| Difference | Default posture | Owning review |
|---|---|---|
| Source/provider or descriptor/activation | `REVIEW_REQUIRED`, `HOLD`, or `MATERIAL_CHANGE_CANDIDATE` | Source authority/activation |
| Canonical role or legacy-role mapping | `MATERIAL_CHANGE_CANDIDATE` or `REVIEW_REQUIRED` | Source role/policy/contracts |
| Framework, hierarchy level, native code, parent-child relation | `MATERIAL_CHANGE_CANDIDATE` | Habitat/ecoregions and consumers |
| Edition/effective date | `MATERIAL_CHANGE_CANDIDATE` | Source/time |
| Boundary geometry, topology, CRS, extent, scale | `MATERIAL_CHANGE_CANDIDATE` or `REVIEW_REQUIRED` | Spatial Foundation |
| Feature/manifest count | `REVIEW_REQUIRED` | Field/geometry comparison |
| Rights, redistribution, attribution, citation | `DENY`, `HOLD`, or `MATERIAL_CHANGE_CANDIDATE` | Rights/source |
| Sensitivity or join risk | `DENY`, `HOLD`, or `MATERIAL_CHANGE_CANDIDATE` | Sensitivity and affected domains |
| Correction/withdrawal notice | `MATERIAL_CHANGE_CANDIDATE` | Correction/release |
| Endpoint/packaging | `REVIEW_REQUIRED` | Connector/security/operations |
| Identity-bearing label or symbology | `REVIEW_REQUIRED` | Domain/cartographic review |
| Contact/help text | Usually excluded unless tied to rights/authority | Record scope/exclusion |
| Comparison-profile version | `REVIEW_REQUIRED` | Validator/profile owner |

A one-line rights notice can be more consequential than a large geometry file, while a large byte change can be packaging-only. Route by evidence and responsibility, not size.

[Back to top](#top)

---

<a id="rights-and-sensitivity"></a>

## Rights, sensitivity, geoprivacy, and reconstruction

Public availability or provider identity is not permission. Verify terms/license identity and effective date; permitted acquisition, storage, retention, redistribution, display, derivatives, tiling, generalization, and crosswalk use; attribution/citation; automated-use limits; credentials/accounts; correction/takedown; third-party content; and whether prior approval still applies.

Use `HOLD` or `DENY` when terms cannot be identified, a public page is the only permission, obligations changed, redistribution/derivatives are ambiguous, attribution cannot survive downstream, credentials appear, or takedown lacks an accountable route. Never invent policy values.

Ecoregion polygons may be broad public context, but joins can expose protected information. Fail closed for exact rare-species/plant occurrences, nests/dens/roosts/hibernacula/spawning/breeding sites, uncleared critical-habitat or stewardship detail, cultural/archaeological/community-controlled locations, private-land/living-person data, sensitive infrastructure, small counts or filters enabling reverse inference, redaction offsets, controlled taxa, or models revealing protected inputs.

Required controls:

- classify source and join sensitivity separately;
- transform before public representation under accepted policy;
- use reviewed generalization, aggregation, suppression, redaction, staged access, or denial;
- never treat styling or hidden layers as security;
- test reconstruction across filters, exports, APIs, tiles, popups, Focus Mode, and generated text;
- preserve transform receipts and source-to-public lineage; and
- route uncertainty to `HOLD`, `DENY`, or `REVIEW_REQUIRED`.

Keep source publication, effective, signal observation, signal recording, inspection, processing, release, correction, and transaction times distinct. Compare native CRS, axis order, units, scale/resolution, extent, feature identity, validity/topology, boundary treatment, native versus derived coordinates, generalization lineage, and geometry-hash profile. Web Mercator, PMTiles, MVT, GeoJSON, styles, screenshots, and rendered pixels are downstream representations, not native geometry or truth.

[Back to top](#top)

---

<a id="validation"></a>

## Validation and command boundary

No repository-grounded ecoregion refresh command is established at this snapshot. The child registry has no descriptor payload; spec has no active profile; pipeline lacks proved executable refresh code; fixture/test children contain only README and `.gitkeep`; policy lacks accepted bundle/evaluator; and the Habitat workflow validates land-cover materiality, not ecoregions.

A maintainer with a real checkout may use read-only documentation checks:

```bash
git rev-parse HEAD
git status --short
git diff --check
git diff -- docs/runbooks/habitat/ecoregions/SOURCE_REFRESH.md
```

These prove text/repository hygiene only. This runbook must not direct `curl`, `wget`, browser automation, SDK calls, credential use, scraping, source-byte writes, descriptor/activation mutation, unaccepted pipeline execution, policy application, tile replacement, proof/release creation, deployment, or publication.

Before an executable command is admitted, a separate reviewed slice must establish accepted source/activation and connector ownership; contracts/schemas; synthetic no-network fixtures; deterministic source-specific comparison; positive/negative tests including rights/sensitivity; finite outcomes/reason codes; receipt/replay and correction/rollback; bounded CI claims; and accountable review.

[Back to top](#top)

---

<a id="handoff"></a>

## Handoff, audit, and recovery

The handoff is the terminal state. Include exact repo/source-head refs, descriptor/activation/producer/profile refs, finite outcome/reasons, field differences, scope/exclusions, framework/hierarchy/time/geometry implications, rights/sensitivity implications, affected artifacts/consumers, required owners/review order, released-state refs, correction/rollback implications, unresolved questions, non-effects, and packet digest.

Accountable reviewers decide whether source/activation remains valid; role/authority changed; rights/sensitivity remain acceptable; contracts/schemas or connector/pipeline must change; a new capture is authorized; WORK, QUARANTINE, or no intake applies; evidence/policy/review gates are available; released/public state is affected; correction/withdrawal/rollback is required; and which state remains held.

A reviewable chain is:

```text
repository base -> accepted source record -> activation decision
-> authorized producer -> prior/current signals -> accepted comparison profile
-> deterministic result -> finite outcome -> handoff -> downstream decisions, if any
```

Keep object families separate; preserve failed/held attempts and append-only correction lineage; exclude secrets/protected payloads; record canonicalization; honor retention/terms; and distinguish inspection completion from decision completion.

On input/profile failure, stop with `HOLD`, `ERROR`, or `REVIEW_REQUIRED`; preserve safe diagnostics; never fall back to live requests, timestamp-only or visual comparison, or silent profile/source changes. On rights/sensitivity failure, stop distribution and route to accountable owners. If released state may be affected, identify exact releases/carriers and route to correction, withdrawal, cache invalidation, and rollback without overwriting public state.

[Back to top](#top)

---

<a id="open-verification"></a>

## Open verification register

| ID | Item | Current state | Default |
|---|---|---|---|
| ECO-REF-001 | Accountable Habitat/ecoregions and trust-path owners | `NEEDS VERIFICATION` | `HOLD` |
| ECO-REF-002 | Canonical source-registry topology | `CONFLICTED` | `HOLD` |
| ECO-REF-003 | Admitted ecoregion descriptor and activation record | `UNKNOWN` / absent in inspected child | `HOLD` |
| ECO-REF-004 | Reviewed mapping from legacy role wording | `CONFLICTED` | `HOLD` |
| ECO-REF-005 | Preferred/default ecoregion framework | `UNKNOWN` | No default |
| ECO-REF-006 | Canonical source-first connector path | `CONFLICTED` / `NEEDS VERIFICATION` | `HOLD` |
| ECO-REF-007 | Current source-specific rights/terms | `NEEDS VERIFICATION` | `HOLD` |
| ECO-REF-008 | Accepted source-specific comparison profile | `ABSENT` | `HOLD` |
| ECO-REF-009 | Executable fixtures/tests/validators | `ABSENT` in inspected children | `HOLD` |
| ECO-REF-010 | Active spec and executable ecoregion pipeline | `ABSENT` / `UNKNOWN` | `HOLD` |
| ECO-REF-011 | Ecoregion-specific policy bundle/evaluator | `ABSENT` / unaccepted | `HOLD` |
| ECO-REF-012 | Evidence closure and public-safe representation profile | `UNKNOWN` / `NEEDS VERIFICATION` | `HOLD` |
| ECO-REF-013 | Sensitive-join reconstruction tests | `ABSENT` | `HOLD` |
| ECO-REF-014 | Catalog/release/correction/rollback closure and public read-back | `UNKNOWN` | `HOLD` |
| ECO-REF-015 | Local ecoregion runbook index | Blank README | Separate docs work |

Resolving one item does not resolve the others. Admission, comparison, policy, evidence, review, promotion, release, deployment, and publication remain separate.

[Back to top](#top)

---

<a id="evidence"></a>

## Evidence basis

CONFIRMED current-repository evidence supports only the bounded findings above: the target scaffold; accepted same-path placement; the domain-wide inspection pattern; the domain charter's context boundary; empty/non-activating source-authority projection; README-only ecoregion registry/spec/pipeline/fixture/test maturity; documentation-only Habitat connector path; unaccepted/evaluator-unbound Habitat policy; and a Habitat workflow whose substantive executable scope is synthetic land-cover materiality with proof/release holds.

The supplied Habitat architecture blueprint was reviewed as read-only planning lineage. It reinforces lifecycle separation, source-role discipline, geoprivacy, EvidenceBundle priority, no-network fixtures, correction, and rollback, but explicitly lacked a mounted repository when authored. It does not prove current paths, activation, runtime, policy, tests, workflows, or release state.

This runbook abstains from asserting current upstream versions/endpoints, provider terms, an active source, framework preference, cadence, public ecoregion content, production connector behavior, operational policy, release/deployment/publication, or ecological/regulatory conclusions.

[Back to top](#top)

---

<a id="rollback"></a>

## Document rollback

Before merge, close the draft PR and abandon only the scoped branch. After merge, use a reviewed revert or forward correction. Restoring prior blob:

```text
d4cc1c429c7d2894cbb5f2b70eb3e36863cd6490
```

restores the 779-byte scaffold only. Documentation rollback does not admit/suspend/withdraw a source, contact upstream, add/remove source bytes, change lifecycle state, create/revoke evidence/policy/review, alter release/deployment/public artifacts, or execute operational correction/rollback.

[Back to top](#top)

---

<a id="non-effects"></a>

## Non-effects

This revision creates or changes no source record/authority/activation; connector/credential/schedule/watcher/network request; source-head signal/payload; lifecycle object; contract/schema/spec/pipeline; fixture/test/validator/profile; policy bundle/evaluator/decision; receipt/EvidenceBundle/proof/catalog; accountable review; promotion decision; release manifest/carrier; deployment/API/map/tile/export/publication; correction/withdrawal/cache invalidation/operational rollback; or ecological, occurrence, habitat-quality, regulatory, legal, or conservation determination.

The only intended effect is to replace a proposal scaffold with a reviewable, fail-closed, repository-grounded inspection and handoff procedure.

[Back to top](#top)
