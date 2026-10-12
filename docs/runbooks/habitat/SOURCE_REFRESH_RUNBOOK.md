<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/habitat/source-refresh-runbook
title: Habitat Source Refresh Inspection Runbook
type: runbook
subtype: domain-source-refresh-inspection
version: v0.2
status: draft; repository-grounded; documentation-only; inspection-and-handoff-only; source-inactive-by-default; fail-closed; non-authoritative; non-activation; non-review; non-promotion; non-release; non-deployment; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Habitat, source, connector, land-cover, wetlands, ecological-model, regulatory, rights, sensitivity/geoprivacy, evidence, policy, validation, review, release, correction, rollback, security, and operations stewards"
created: 2026-05-12
updated: 2026-08-25
policy_label: public-review; habitat; source-refresh-inspection; operational-documentation; rights-aware; sensitive-location-aware; fail-closed; no-publication-authority
current_path: docs/runbooks/habitat/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Explain how to inspect an already-authorized Habitat source-head signal, classify bounded
  no-change or material-change evidence, and prepare a non-authoritative handoff without
  admitting or activating a source, fetching live bytes, performing policy or review, crossing
  a lifecycle boundary, promoting, releasing, deploying, or publishing.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: >-
  Existing direct child of docs/runbooks/habitat/ and reconciled in place under the accepted
  docs/ responsibility root. The lane README exists but is blank, and a duplicate proposal-era
  runbook remains under docs/domains/habitat/; this update creates no alias, mirror, migration,
  connector, watcher, or sibling authority and does not adjudicate those conflicts.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: b9eaecdda2ad72980e91e24bfc3b8ff073a6190e
  target_prior_blob: 1fecc4e6337ba2c897f4c4b328a33ea3bdba97e8
  lane_readme_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  source_descriptor_implementation_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  source_descriptor_plural_alias_blob: 42da54b28a527850cce88ad89f68921c101fc56b
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  subtype_source_registry_readme_blob: 5d9c90f88ff7e2e2b0d4f2064bc835589196d8b8
  domain_first_registry_readme_blob: 0dc7d3bb92cfb03d62cb35c9f375150f372c0952
  connector_compatibility_index_blob: 62e0a0df3934eb2dc534960be8f49e5079351091
  habitat_policy_readme_blob: cf6dd24db1a06cb857806c000500471bbe918ad7
  domain_habitat_workflow_blob: 59771c027f688d7028a46c4635c0ec710b34e3ab
  materiality_profile_contract_blob: c7ad48b435d8cc7fcdcf2910fb675e9c9778e7e7
  materiality_workflow_blob: fd73a098c1dbf8fd07135ce3cdab04b280b30904
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../domains/habitat/README.md
  - ../../domains/habitat/SOURCE_REFRESH_RUNBOOK.md
  - ../../domains/habitat/SOURCE_REGISTRY.md
  - ../../domains/habitat/SOURCE_FAMILIES.md
  - ../../domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../domains/habitat/SENSITIVITY.md
  - ../../domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../domains/habitat/REASON_CODES.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/habitat/README.md
  - ../../../data/registry/habitat/README.md
  - ../../../data/registry/sources/habitat/usfws-critical-habitat.source.yaml
  - ../../../data/registry/sources/habitat/usfws_ecos.yaml
  - ../../../connectors/habitat/README.md
  - ../../../policy/domains/habitat/README.md
  - ../../../contracts/domains/habitat/land_cover/materiality_profile.md
  - ../../../tools/validators/domains/habitat/validate_land_cover_materiality.py
  - ../../../tests/validators/domains/habitat/test_land_cover_materiality.py
  - ../../../.github/workflows/habitat-land-cover-materiality.yml
  - ../../../.github/workflows/domain-habitat.yml
tags: [kfm, habitat, runbook, source-refresh, inspection, source-head, material-change, no-network, rights, sensitivity, geoprivacy, evidence, fail-closed]
notes:
  - "This revision removes illustrative live watcher, conditional-GET, fetch, lifecycle-write, release, and publication instructions that current repository evidence does not authorize."
  - "The machine source-authority projection is PROPOSED, projection-only, implementation-absent, empty, and non-activating."
  - "The inspected Habitat registry YAMLs are PROPOSED inventory placeholders rather than accepted SourceDescriptor instances."
  - "Habitat source-registry topology remains conflicted between subtype-first and domain-first lanes; this runbook does not select or write either lane."
  - "The standalone connectors/habitat/ path is a documentation-only compatibility index; source access remains source-first and product-specific, with several path conflicts still unresolved."
  - "The Habitat policy boundary records proposed rule scaffolds without an accepted bundle, evaluator, or production consumer."
  - "The only repository-grounded comparison path used here is the inactive, synthetic, no-network Habitat land-cover materiality profile; it does not fetch or admit a live source and does not generalize to every Habitat source family."
  - "This document creates no source descriptor, activation, fetch, source-head observation, receipt, evidence, policy decision, review, candidate, lifecycle transition, promotion, release, deployment, or public state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Source Refresh Inspection Runbook

> **Use this runbook to inspect a source-head signal that an already-authorized source operation produced, classify the bounded evidence, and prepare a non-authoritative handoff.** This runbook is not a watcher, connector, scheduler, source-admission decision, fetch command, policy evaluator, reviewer, lifecycle writer, or publisher.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![Source authority: empty](https://img.shields.io/badge/source%20authority-empty-b42318?style=flat-square)](#current-repository-posture)
[![Registry records: placeholders](https://img.shields.io/badge/registry-placeholders-d4a72c?style=flat-square)](#current-repository-posture)
[![Policy: inactive scaffolds](https://img.shields.io/badge/policy-inactive%20scaffolds-d4a72c?style=flat-square)](#current-repository-posture)
[![Materiality: synthetic no-network](https://img.shields.io/badge/materiality-synthetic%20no--network-0969da?style=flat-square)](#validation-and-command-boundary)
[![Authority: inspection only](https://img.shields.io/badge/authority-inspection%20only-0969da?style=flat-square)](#authority-and-negative-authority)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b42318?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Current safe determination at `main@b9eaecdda2ad…`: `HOLD — NO ACTIVE HABITAT SOURCE REFRESH PATH ESTABLISHED`.** The machine source-authority projection has no entries; the inspected Habitat registry YAMLs are proposal placeholders; the Habitat connector directory is documentation-only; source-specific connector paths remain conflicted; the Habitat policy bundle and evaluator are unaccepted; and the domain workflow explicitly holds proof and release while running only bounded synthetic no-network validation.

> [!CAUTION]
> A source descriptor filename, endpoint URL, schedule proposal, workflow dispatch button, manual download, changed upstream page, HTTP status, `ETag`, timestamp, digest, material-change result, pull request, or green validation job is not source admission, activation, evidence closure, policy approval, review, promotion, release, deployment, or publication.

> [!WARNING]
> Never place credentials, private endpoints, exact or reverse-engineerable rare-species, rare-plant, nest, den, roost, hibernaculum, spawning, breeding, stewardship, cultural, archaeological, private-land, or infrastructure-adjacent coordinates; protected joins; redaction offsets; controlled taxon attributes; or source-native restricted payloads in an ordinary refresh packet, log, issue, pull request, screenshot, or generated summary.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [State](#current-repository-posture) · [Outcomes](#finite-procedure-outcomes) · [Triggers](#recognized-inspection-triggers) · [Preconditions](#preconditions-and-stop-conditions) · [Packet](#required-inspection-packet) · [Procedure](#procedure) · [No change](#no-change-candidate-path) · [Material change](#material-change-candidate-path) · [Habitat controls](#habitat-specific-controls) · [Validation](#validation-and-command-boundary) · [Handoff](#handoff-boundary) · [Anti-patterns](#anti-patterns-to-refuse) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback) · [Non-effects](#non-effects)

---

<a id="purpose"></a>

## Purpose

This runbook supports a narrow, evidence-preserving inspection:

1. freeze the exact repository revision and the separately produced source-head signal;
2. verify that source identity, source role, authority, rights, sensitivity, and connector path are already established by owning surfaces;
3. compare immutable prior/current metadata without making a network request here;
4. run only a separately accepted, deterministic, no-network comparison profile when one applies;
5. classify a no-change candidate, material-change candidate, or fail-closed outcome;
6. record non-sensitive findings and immutable pointers; and
7. hand the result to the owning source, evidence, policy, review, lifecycle, correction, and release processes.

It does not:

- create, admit, activate, suspend, or withdraw a `SourceDescriptor`;
- choose between competing source-registry, schema, or connector paths;
- schedule a watcher, call an upstream API, issue a conditional request, or fetch bytes;
- store, move, transform, overwrite, or delete RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED material;
- manufacture a source-head observation, checksum, `RunReceipt`, `EvidenceBundle`, `PolicyDecision`, review record, promotion candidate, release manifest, correction notice, withdrawal notice, or rollback card;
- perform geoprivacy, generalization, redaction, crosswalk, model execution, or ecological interpretation;
- invalidate caches, rebuild tiles, change aliases, deploy, promote, release, or publish; or
- certify source freshness, completeness, accuracy, ecological meaning, regulatory effect, rights, safety, or public usability.

[Back to top](#top)

---

<a id="authority-and-negative-authority"></a>

## Authority and negative authority

This file is explanatory operational documentation under `docs/runbooks/habitat/`. It describes safe inspection and handoff. It does not own a source, a source operation, a policy decision, or a lifecycle transition.

| Concern | Owning surface | This runbook may do | This runbook must not do |
|---|---|---|---|
| Source identity and admission | accepted source registry plus authority/activation records | Require exact resolvable state | Mint, admit, activate, suspend, or withdraw |
| Source access | one accepted source-first connector or runtime | Inspect an already-produced bounded signal | Choose a connector path, fetch, authenticate, or schedule |
| Source role and authority | `SourceDescriptor`, source doctrine, and owning domain contracts | Check preservation and surface conflicts | Upgrade a role or convert context/model/aggregate into observation or regulation |
| Rights, terms, and citation | accepted rights policy and accountable review | Require finite state and obligations | Infer permission from public reachability or provider identity |
| Sensitivity and geoprivacy | accepted sensitivity/geoprivacy policy and accountable review | Require finite state and public-safe obligations | Reveal protected detail or invent a transform |
| Source payload lifecycle | governed `data/` lanes and authorized writers | Reference immutable identities | Write, move, transform, overwrite, or delete payloads |
| Evidence and receipts | receipt/proof families and evidence resolver | Require support pointers | Manufacture evidence, receipts, proof, or closure |
| Materiality | accepted contract/profile and accountable steward | Run a bounded existing fixture profile | Generalize one profile to every source family |
| Habitat policy | accepted policy source, bundle, selector, evaluator, and reviewers | Prepare an input/handoff checklist | Treat current scaffolds as active policy |
| Neighbor-domain truth | Fauna, Flora, Hydrology, Soil, Agriculture, Archaeology, People/Land, and other owning lanes | Preserve references and ownership | Absorb occurrence, taxon, wetland-law, water, soil, cultural, or ownership authority |
| Promotion and release | `release/` and accountable release operations | Identify downstream prerequisites | Promote, release, deploy, or publish |
| Correction and rollback | release-accountability objects and owning operations | Preserve lineage requirements | Execute correction, invalidation, withdrawal, or rollback |

A README cannot turn a proposal placeholder into an admitted source, an endpoint into permission, a changed source head into ecological evidence, a materiality classification into review, or a candidate into release.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

The observations below are pinned to `main@b9eaecdda2ad72980e91e24bfc3b8ff073a6190e`.

| Surface | Confirmed repository evidence | Bounded conclusion |
|---|---|---|
| Requested runbook path | `docs/runbooks/habitat/SOURCE_REFRESH_RUNBOOK.md` exists as an operational-documentation path | Same-path reconciliation is `PLACE`; no new path is needed |
| Habitat runbook lane README | `docs/runbooks/habitat/README.md` contains only a newline | Lane index, ownership, and direct-child boundary remain `NEEDS VERIFICATION` |
| Duplicate domain runbook | `docs/domains/habitat/SOURCE_REFRESH_RUNBOOK.md` exists and itself says operational procedures belong under `docs/runbooks/` | Duplicate responsibility is `CONFLICTED`; this change neither edits nor deletes it |
| SourceDescriptor contract | Rich v1 contract and validator references exist, but the paired schema remains `PROPOSED` and plural/singular schema paths are a compatibility relationship | Schema presence is not source admission or activation |
| Machine source authority | `PROPOSED`, `projection_only`, implementation `ABSENT`, completeness `empty`, `entries: []` | No active source authority is established by the projection |
| Habitat source registry | The subtype-first README is experimental; the domain-first parent is compatibility/routing; both warn against divergent records | Registry topology remains `CONFLICTED`; do not write either by convenience |
| Inspected Habitat registry YAMLs | USFWS ECOS and critical-habitat records are seven-line `PROPOSED` placeholders generated from documentation inventory; the connector index reports the same pattern for several other Habitat records | No accepted, refreshable Habitat `SourceDescriptor` was established by bounded inspection |
| Habitat connector directory | `connectors/habitat/` is a documentation-only compatibility index with no client, parser, package, activation record, fixture suite, or runtime beneath it | No domain-scoped Habitat connector/runtime path is established |
| Source-specific connector topology | NLCD, USFWS ECOS, KDWP, LANDFIRE, and iNaturalist have mixed or duplicate path forms documented by the compatibility index | A refresh operator may not choose a source path by convenience |
| Habitat policy | The policy boundary records proposed default-only scaffolds, mixed result relations, no accepted entrypoint, no native Rego test suite, no accepted bundle, and no verified evaluator/consumer | Current policy files cannot authorize a refresh or outward use |
| Habitat land-cover materiality profile | Inactive, synthetic, no-network adapter emits `NON_EVENT`, `PROMOTION_CANDIDATE`, or `HOLD` process memory | Bounded comparison evidence only; no live source, admission, policy, review, or release |
| Domain Habitat workflow | Runs the synthetic materiality suite and explicitly holds Habitat proof and release-dry-run producers | A green workflow is not evidence closure, promotion, release, or publication |
| Drive Habitat blueprints | Planning reports explicitly lacked a mounted repository and labeled paths, routes, workflows, and live-source behavior as proposed | Useful lineage for risks and scope; not current implementation proof |

### Current safe determination

```text
procedure_disposition: HOLD
reason: NO_ACTIVE_HABITAT_SOURCE_REFRESH_PATH
source_fetch_performed: false
lifecycle_effect: none
public_effect: none
```

This is a documentation conclusion for the pinned revision. It is not a source-state record, activation decision, policy outcome, receipt, review, or release decision.

[Back to top](#top)

---

<a id="finite-procedure-outcomes"></a>

## Finite procedure outcomes

This runbook does not create a canonical repository-wide enum. Machine records must use the selected accepted contract and validator vocabulary. For human inspection, record one bounded disposition:

| Disposition | Meaning | Permitted next step |
|---|---|---|
| `NO_CHANGE_CANDIDATE` | Authorized prior/current metadata appear unchanged under the named bounded profile | Hand off for owning audit/receipt handling; do not claim a receipt exists |
| `MATERIAL_CHANGE_CANDIDATE` | A bounded comparison found declared dimensions requiring accountable inspection | Hand off; do not create review, promotion, or release state |
| `HOLD` | Authority, identity, rights, sensitivity, baseline, connector, evidence, profile, or ownership is absent or conflicted | Preserve the prior safe state |
| `ABSTAIN` | Available evidence cannot support a change/no-change conclusion | Obtain admissible evidence or narrow scope |
| `RESTRICT` | Handling may continue only through approved restricted controls | Remove protected material from ordinary surfaces |
| `DENY` | Requested access, comparison, storage, join, or exposure violates a governing rule | Stop and record only a non-sensitive reason |
| `ERROR` | Inspection or validation could not produce a reliable result | Preserve inputs and diagnostics; make no materiality claim |

The current inactive Habitat land-cover profile uses its own machine vocabulary:

| Profile result | Human interpretation here | Non-effect |
|---|---|---|
| `NON_EVENT` | Potential `NO_CHANGE_CANDIDATE` after provenance and authority checks | Does not prove freshness or an authentic source-head observation |
| `PROMOTION_CANDIDATE` | Potential `MATERIAL_CHANGE_CANDIDATE` | Is not promotion, review, release, or publication authority |
| `HOLD` | `HOLD` | Preserves the prior safe state |
| Invalid input / failed validation | `ERROR` | Emits no authoritative assessment |

[Back to top](#top)

---

<a id="recognized-inspection-triggers"></a>

## Recognized inspection triggers

An inspection may begin only from one of these separately governed inputs:

- an immutable source-head signal already emitted by an accepted source-first connector or authorized source operation;
- an upstream version, edition, revision, or effective-date notice preserved by the owning source process;
- a rights, terms, attribution, access, sensitivity, or citation change recorded by an accountable reviewer;
- an accepted `SourceDescriptor` revision or supersession;
- a correction, withdrawal, deprecation, or replacement notice tied to an existing source identity;
- a replay request for an accepted deterministic comparison profile; or
- an authorized investigation of a previously emitted validation finding.

These are not sufficient triggers:

- a changed web page viewed manually;
- a timestamp generated during this runbook;
- an HTTP `200`, `Last-Modified`, `ETag`, digest, file size, or download URL without authenticated provenance;
- a proposed schedule, watcher YAML, connector README, or workflow button;
- a Drive PDF, architecture plan, source-family list, or repository issue;
- a branch, commit, pull request, merge, green check, badge, or release note by itself; or
- an AI-generated claim that a source changed.

When the trigger's producer, identity, authority, or immutability cannot be verified, use `HOLD`, `ABSTAIN`, or `ERROR`.

[Back to top](#top)

---

<a id="preconditions-and-stop-conditions"></a>

## Preconditions and stop conditions

Before comparing anything, confirm all items below. A failed item is a stop condition, not permission to improvise.

1. **Repository revision:** pin the exact commit and re-check the target file, applicable contracts, registries, policy boundaries, workflows, and open overlapping work.
2. **Accepted source identity:** resolve one exact source ID to one accepted `SourceDescriptor`; proposal placeholders do not qualify.
3. **Authority and activation:** resolve an accepted authority/activation record whose scope includes the intended access and comparison. An empty projection does not qualify.
4. **Connector identity:** resolve one accepted source-first connector/runtime and the exact operation that produced the signal. `connectors/habitat/` does not qualify.
5. **Source role:** preserve the descriptor's exact machine role and authority limits. Do not resolve current vocabulary conflicts inside this runbook.
6. **Rights and citation:** require finite, current, review-backed terms, attribution, redistribution, and access posture.
7. **Sensitivity and handling:** require a finite sensitivity class, join-induced sensitivity assessment, and approved handling obligations.
8. **Immutable baseline:** identify the prior source-head observation, upstream version, observation time, producer, and immutable pointer.
9. **Immutable candidate:** identify the current source-head observation using the same scope and comparison basis.
10. **Product semantics:** record product family, native classification/version, spatial and temporal scope, scale or resolution, CRS/datum, regulatory/model/observation/aggregate character, and known uncertainty.
11. **Comparison profile:** identify an accepted versioned profile, criteria, canonicalization method, and `spec_hash`; otherwise perform descriptive inspection only.
12. **No protected payload:** keep source bytes, credentials, precise protected geometry, controlled fields, and redaction mechanics out of the ordinary packet.
13. **No overlap:** confirm no open branch, pull request, migration, or steward operation owns the same source record or refresh surface.
14. **Rollback-preserving posture:** confirm the prior released state remains untouched throughout inspection.

### Current stop condition

At the pinned revision, preconditions 2 through 7 are not established for a general Habitat live-source refresh. Therefore the default executable outcome is:

```text
HOLD: NO_ACTIVE_HABITAT_SOURCE_REFRESH_PATH
```

The synthetic land-cover materiality fixtures may be validated independently, but that activity is not a live-source refresh and does not cure missing source authority.

[Back to top](#top)

---

<a id="required-inspection-packet"></a>

## Required inspection packet

The packet is pointer-based and contains no protected source payload.

| Field | Requirement |
|---|---|
| `repository_commit` | Exact commit inspected |
| `runbook_blob` | Exact runbook blob used |
| `source_id` and `descriptor_version` | Resolvable accepted source identity |
| `source_type`, `source_role`, and authority limits | Exact descriptor values, not human inference |
| `source_family` and `product_id` | Product-specific identity such as land cover, wetland inventory, regulatory designation, stewardship, model, or occurrence context |
| `authority_or_activation_ref` | Accepted record authorizing the bounded source operation |
| `connector_ref` and operation identity | Accepted source-first connector/runtime, version, and producing operation |
| `prior_source_head_ref` | Immutable prior observation pointer |
| `current_source_head_ref` | Immutable candidate observation pointer |
| `source_head_methods` | Declared methods such as upstream version, revision ID, checksum, `ETag`, last modified, or content length; methods are evidence dimensions, not authority |
| `observed_at` and `producer` | Time and accountable producer of each observation |
| `rights_review_ref` | Current rights, terms, attribution, redistribution, and access decision |
| `sensitivity_review_ref` | Current sensitivity, geoprivacy, and join-obligation decision |
| `native_classification` and `native_version` | Preserved source-native system and edition |
| `spatial_scope` | Coverage, scale/resolution, CRS/datum, geometry type, and precision class |
| `temporal_scope` | Valid, observed, publication, retrieval, effective, and correction times when applicable |
| `knowledge_character` | Observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, or the accepted machine equivalent |
| `uncertainty_and_limitations` | Known model, inventory, sampling, completeness, temporal, or spatial limitations |
| `comparison_profile` | Profile ID/version, canonicalization, criteria, and `spec_hash`, if used |
| `comparison_outputs` | Immutable output pointers and validator result; no unsupported summary |
| `neighbor_domain_refs` | Fauna, Flora, Hydrology, Soil, Agriculture, Archaeology, People/Land, or other authority dependencies |
| `public_safe_obligations` | Generalization, redaction, aggregation, delayed release, staged access, or denial obligations |
| `open_conflicts` | Path, identity, role, rights, sensitivity, baseline, profile, or ownership conflicts |
| `requested_handoff` | Exact owning process requested to inspect the result |

Use `UNKNOWN` or `NEEDS VERIFICATION`; do not substitute a plausible value.

[Back to top](#top)

---

<a id="procedure"></a>

## Procedure

### 1. Freeze repository and authority inputs

Record the exact `main` commit, target blob, accepted Directory Rules bytes, relevant ADRs, source contract/schema, registry records, connector boundary, policy boundary, validator/profile, and open overlapping work.

Stop with `HOLD` if the branch moved materially, the target changed, or another change owns the same source/refresh surface.

### 2. Resolve one source identity

Resolve the source ID and descriptor version through the accepted source registry. Verify that the record satisfies the active schema and is not a documentation-generated placeholder, compatibility copy, deprecated alias, or unresolved duplicate.

Stop with `HOLD` when:

- no accepted descriptor exists;
- two writable homes claim authority;
- the descriptor relies only on deprecated minimal fields;
- source role, rights, sensitivity, access, or lifecycle state is unknown; or
- a domain-first and subtype-first record diverge.

### 3. Resolve authority and connector provenance

Verify the accepted activation/authority record and the one source-first connector/runtime that produced the signal. Confirm the operation did not use the Habitat compatibility index as a runtime path.

Stop with `HOLD` when:

- the source-authority projection is empty or non-operative;
- connector path identity is conflicted;
- activation is disabled, candidate-only, or absent;
- producer identity cannot be authenticated; or
- the signal came from a manual browser/download or generated prose.

### 4. Re-check rights, citation, and access

Use the accountable review record, not assumptions. Confirm terms apply to the specific product, version, endpoint, payload, fields, redistribution, derivative use, public display, and intended downstream operation.

Use `RESTRICT`, `DENY`, or `HOLD` when obligations are unresolved or more restrictive than the requested handling.

### 5. Re-check sensitivity and join-induced risk

Evaluate the candidate's own sensitivity and the most restrictive plausible governed join. A public land-cover or wetland layer can become restricted when combined with exact occurrence, rare-species, rare-plant, nest, den, roost, spawning, stewardship, cultural, archaeological, private-land, or infrastructure context.

Style filters, hidden layers, client-side suppression, and omitted popup fields are not geoprivacy controls.

### 6. Preserve source role and native semantics

Record the exact accepted source role and product character. Preserve native class systems, legends, versions, effective dates, model/run identities, scale, resolution, CRS/datum, uncertainty, and limitations.

Do not:

- call modeled suitability observed habitat;
- call land cover a species occurrence;
- call an inventory a legal determination;
- call a regulatory designation a biological observation;
- call stewardship status habitat condition; or
- treat a crosswalk as replacement truth.

### 7. Compare immutable source-head observations

Compare only already-produced, immutable prior/current observations under the same scope. Do not issue a network request from this runbook.

At minimum compare:

- source and product identity;
- upstream version, edition, revision, or effective date;
- declared source-head methods;
- publication/retrieval/observation times;
- spatial and temporal coverage;
- native classification or schema version;
- scale/resolution and CRS/datum;
- rights, access, citation, and sensitivity posture;
- source role and authority limits;
- model/run identity and uncertainty, if applicable; and
- correction, withdrawal, or supersession state.

A byte or metadata difference is not automatically material. An unchanged digest is not proof the source is current, complete, authorized, or safe.

### 8. Run only an accepted bounded no-network profile

When a separately accepted profile applies, run its exact repository-native validator over local fixtures or authorized immutable inputs. Record the profile ID, version, criteria, canonicalization method, `spec_hash`, command, result, and immutable output pointer.

The current Habitat land-cover profile is `PROPOSED_INACTIVE` and synthetic. It is useful for validating the adapter and shared assessment contract, not for deciding live source state.

### 9. Classify the bounded result

Choose one disposition from [Finite procedure outcomes](#finite-procedure-outcomes). State what the evidence supports and what remains unresolved.

Never translate:

- `NON_EVENT` into “source current”;
- `PROMOTION_CANDIDATE` into promotion;
- a green job into approval;
- a material difference into ecological significance; or
- no detected difference into evidence closure.

### 10. Record a minimal non-sensitive finding

Record:

- frozen identities and pointers;
- selected profile and criteria;
- observed comparison result;
- finite disposition;
- non-sensitive reason codes;
- unresolved authority, rights, sensitivity, role, or topology issues; and
- the exact owning handoff requested.

Do not claim this document emitted a canonical receipt or decision object.

### 11. Hand off without crossing a boundary

Send the packet to the owning source, rights, sensitivity, evidence, policy, review, lifecycle, correction, and release processes as applicable. Each owner independently decides whether to act.

Preserve the prior published state until all later governed transitions close.

[Back to top](#top)

---

<a id="no-change-candidate-path"></a>

## No-change candidate path

A no-change candidate is appropriate only when:

- source identity and scope match;
- the comparison basis is accepted and version-pinned;
- prior/current observations are authentic and immutable;
- required source-head dimensions match;
- no rights, sensitivity, citation, access, role, classification, model, scale, time, correction, or authority change is present; and
- the selected validator returns its no-change-equivalent result.

Record:

```text
disposition: NO_CHANGE_CANDIDATE
profile: <accepted profile id and version>
evidence_scope: <exact bounded dimensions>
source_fetch_performed_by_this_runbook: false
receipt_created_by_this_runbook: false
lifecycle_effect: none
public_effect: none
```

A no-change candidate does not prove:

- that a watcher or live connector ran;
- that the source is globally current or complete;
- that omitted upstream dimensions are unchanged;
- that rights or sensitivity remain safe outside the bounded review;
- that a no-op receipt, EvidenceBundle, policy decision, or review exists; or
- that any public artifact should be rebuilt, retained, or released.

[Back to top](#top)

---

<a id="material-change-candidate-path"></a>

## Material-change candidate path

A material-change candidate may be appropriate when the accepted profile or accountable inspection finds one or more declared changes, including:

- a new product vintage, edition, revision, effective date, or correction;
- native class, legend, schema, field, or identifier changes;
- spatial coverage, geometry, precision, scale, resolution, CRS, or datum changes;
- temporal coverage, publication cadence, or validity-window changes;
- source role, authority scope, rights, terms, attribution, redistribution, access, citation, or sensitivity changes;
- regulatory designation boundaries or effective-date changes;
- model algorithm, input set, run identity, calibration, uncertainty, or applicability changes;
- a new exact-location or harmful-join exposure;
- a withdrawal, supersession, deprecation, or source-head conflict; or
- a change exceeding an accepted profile's explicit materiality criteria.

Record:

```text
disposition: MATERIAL_CHANGE_CANDIDATE
profile: <accepted profile id and version>
changed_dimensions:
  - <bounded, evidence-backed dimension>
requested_handoff:
  - source stewardship
  - rights and sensitivity review
  - evidence and validation
  - downstream impact analysis
source_fetch_performed_by_this_runbook: false
promotion_effect: none
release_effect: none
public_effect: none
```

The candidate may justify further work. It does not itself:

- admit or activate a source;
- prove ecological, regulatory, legal, or management significance;
- create a review request, policy decision, lifecycle transition, correction, or release;
- authorize a new public-safe transform;
- supersede prior evidence or published artifacts; or
- permit a direct RAW-to-PUBLISHED path.

[Back to top](#top)

---

<a id="habitat-specific-controls"></a>

## Habitat-specific controls

### Source and knowledge anti-collapse

| Must remain distinct | Why |
|---|---|
| Land-cover observation or aggregate vs. habitat condition | Cover class is not a complete ecological assessment |
| NWI wetland inventory vs. site-specific legal wetland determination | Inventory context does not replace jurisdictional or legal review |
| Regulatory critical-habitat designation vs. modeled suitability | Issued legal/regulatory scope and modeled ecological inference have different authority |
| GAP/LANDFIRE ecological or vegetation model vs. direct observation | Model inputs, run identity, uncertainty, and applicability must remain visible |
| Habitat patch/context vs. species occurrence | Habitat does not own Fauna or Flora occurrence truth |
| Specimen/observation aggregator vs. authoritative taxon or occurrence claim | Aggregation, source provenance, licenses, and geoprivacy survive the join |
| PAD-US or stewardship boundary vs. habitat quality or conservation outcome | Administrative/stewardship status is not ecological condition |
| Ecoregion, HUC, PLSS, county, or survey unit vs. habitat truth | Context fabric supports grouping and analysis; it does not prove habitat state |
| Native source classification vs. KFM crosswalk | Crosswalks are derived, loss-bearing, versioned interpretations |
| Public tile, map, summary, or AI answer vs. evidence | Rendered and generated carriers remain downstream of governed evidence |

### Native classification, scale, and time

For every comparison, preserve:

- source-native class codes and labels;
- legend/classification version and crosswalk version;
- source vintage, effective date, observation window, publication date, retrieval date, and correction date;
- nominal and effective spatial resolution;
- map or survey scale and minimum mapping unit where applicable;
- CRS, datum, vertical reference, and geometry precision;
- aggregation unit and method;
- model/run version and uncertainty; and
- completeness, provisional status, and known limitations.

A source refresh must not silently rewrite prior vintages into a timeless surface.

### Sensitive joins and geoprivacy

Apply the most restrictive governed posture across joined inputs. Exact or reverse-engineerable ecological locations must be transformed before public artifacts are created. Record transform identity and reason through the owning process; do not expose the transform mechanics in ordinary public documentation.

When safety cannot be established, prefer:

- quarantine;
- restricted/steward-only handling;
- generalization or aggregation;
- delayed release;
- redaction;
- narrowed scope;
- abstention; or
- denial.

### One capture, multiple governed consumers

Habitat, Fauna, Flora, Hydrology, Soil, Agriculture, and other domains must not independently capture the same upstream source merely because they use it differently. Source acquisition belongs to one accepted source identity and source-first connector. Domains receive lineage-preserving candidates and apply their own contracts, policy, evidence, and release controls downstream.

### Regulatory and management language

This runbook does not:

- designate critical habitat;
- determine wetlands jurisdiction;
- establish species presence or absence;
- declare habitat suitability or restoration success;
- provide legal, conservation, land-management, or permitting advice; or
- upgrade a map or model to regulatory authority.

[Back to top](#top)

---

<a id="validation-and-command-boundary"></a>

## Validation and command boundary

### Current repository-grounded commands

The following commands are verified from the inactive synthetic Habitat land-cover materiality profile:

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/habitat \
  --pattern 'test_land_cover_materiality.py' \
  --verbose

python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
```

The focused workflow installs declared project runtime dependencies and executes those commands against synthetic no-network fixtures. The aggregate Habitat workflow also invokes the same bounded suite and explicitly records the profile as `PROPOSED_INACTIVE`.

A passing result proves only:

- the selected synthetic fixture/profile shape can be evaluated;
- the adapter's deterministic mapping can be exercised;
- emitted assessment objects pass the shared validator; and
- the tested revision satisfies the bounded workflow checks.

It does not prove:

- any live Habitat source was accessed, admitted, refreshed, or compared;
- source identity, rights, sensitivity, authority, freshness, or completeness;
- Habitat, species, wetlands, land-cover, or regulatory truth;
- policy evaluation, evidence closure, steward review, public-safe geometry, proof construction, promotion, release, deployment, or publication; or
- that the profile's thresholds are scientifically, legally, or operationally accepted.

### Commands this runbook does not authorize

Do not add or run live-source commands here, including `curl`, `wget`, browser automation, ArcGIS/REST queries, STAC searches, API clients, cloud downloads, object-store sync, credentialed requests, or connector dispatch.

A live-source command requires a separately accepted source descriptor, authority/activation record, connector path, rights and sensitivity review, secret handling, no-network test coverage, bounded output contract, receipt path, correction path, and rollback plan.

[Back to top](#top)

---

<a id="handoff-boundary"></a>

## Handoff boundary

A handoff is a request for accountable inspection, not a state transition.

| Potential recipient | Minimum question |
|---|---|
| Source steward | Is the source identity, role, authority, version, and source-head evidence valid? |
| Connector steward | Is the producing connector/runtime accepted, deterministic, secure, and operating within activation scope? |
| Rights reviewer | Do current terms permit the intended acquisition, transformation, retention, citation, redistribution, and public use? |
| Sensitivity/geoprivacy reviewer | Does the source or any plausible join require restricted handling, generalization, delay, redaction, or denial? |
| Habitat steward | Are native semantics, ecological limits, scale, time, and model/observation/regulatory distinctions preserved? |
| Neighbor-domain steward | Does the packet depend on Fauna, Flora, Hydrology, Soil, Agriculture, Archaeology, People/Land, or another authority? |
| Evidence/validation steward | Does admissible evidence support the bounded change conclusion, and are outputs valid? |
| Policy steward | Is there an accepted policy bundle, selector, evaluator, and normalized decision path for the requested operation? |
| Review/release steward | Is a later candidate eligible for independent review, correction planning, rollback planning, and release consideration? |
| Security/operations steward | Are credentials, access, logging, storage, monitoring, and failure handling safe and auditable? |

The handoff packet must include:

- the finite disposition;
- exact immutable references;
- bounded changed/unchanged dimensions;
- source role and limitations;
- rights and sensitivity state;
- protected-data handling requirements;
- comparison profile identity;
- unresolved conflicts;
- explicit non-effects; and
- the requested decision owner.

Do not include source-native restricted bytes or exact sensitive geometry.

[Back to top](#top)

---

<a id="anti-patterns-to-refuse"></a>

## Anti-patterns to refuse

Refuse or fail closed on any request to:

1. treat a seven-line `status: PROPOSED` registry placeholder as an admitted source;
2. choose between subtype-first and domain-first registry records by convenience;
3. implement runtime behavior under `connectors/habitat/` without an accepted placement decision;
4. choose among duplicate source-specific connector paths without migration authority;
5. fetch a live source because an endpoint is documented or publicly reachable;
6. infer rights, source role, sensitivity, cadence, or authority from a provider name;
7. treat `ETag`, timestamp, digest, file size, or HTTP status as source truth;
8. treat `NON_EVENT` as proof that a source is current;
9. treat `PROMOTION_CANDIDATE` as promotion, review, release, or publication;
10. treat a green fixture workflow as proof, policy approval, or public safety;
11. relabel modeled, aggregate, regulatory, administrative, candidate, or occurrence context as observed Habitat truth;
12. overwrite a prior vintage instead of preserving identity and lineage;
13. hide sensitive geometry only through client-side styling;
14. place exact protected ecological or cross-domain join details in a PR or ordinary log;
15. let Habitat absorb Fauna, Flora, wetland-law, cultural, land, or infrastructure authority;
16. use a Drive blueprint or proposal-era runbook as current implementation evidence;
17. manufacture receipts, EvidenceBundles, policy decisions, review records, or release objects from documentation prose; or
18. collapse source refresh, evidence closure, review, promotion, release, deployment, and publication into one step.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Status | Verification need | Safe posture |
|---|---|---|---|
| `HAB-SR-01` | `NEEDS VERIFICATION` | Populate and review the Habitat runbook lane README | Do not infer lane ownership or direct-child status beyond path presence |
| `HAB-SR-02` | `CONFLICTED` | Reconcile the duplicate `docs/domains/habitat/SOURCE_REFRESH_RUNBOOK.md` | No delete, redirect, or supersession in this PR |
| `HAB-SR-03` | `CONFLICTED` | Decide subtype-first vs. domain-first Habitat source registry topology | One authoritative record only; no parallel writes |
| `HAB-SR-04` | `HOLD` | Replace proposal inventory YAMLs with schema-valid, reviewed descriptors or retire them through migration | Placeholders remain non-activating |
| `HAB-SR-05` | `HOLD` | Populate an accepted source-authority/activation surface | Empty projection grants no authority |
| `HAB-SR-06` | `CONFLICTED` | Reconcile NLCD, USFWS ECOS, KDWP, LANDFIRE, and iNaturalist connector path/identity collisions | Use no source path by convenience |
| `HAB-SR-07` | `NEEDS VERIFICATION` | Resolve SourceDescriptor schema canonical/implementation alias posture and validator wiring | Validate only against the explicitly selected revision |
| `HAB-SR-08` | `HOLD` | Accept one Habitat policy package, entrypoint, decision shape, bundle, selector, evaluator, tests, and consumer | Current scaffolds remain inactive |
| `HAB-SR-09` | `HOLD` | Establish an accepted live-source signal producer with rights, sensitivity, secrets, receipts, correction, and rollback | No live fetch |
| `HAB-SR-10` | `HOLD` | Establish Habitat proof and release-dry-run producers | Domain workflow holds both lanes |
| `HAB-SR-11` | `NEEDS VERIFICATION` | Assign accountable Habitat, source, connector, rights, sensitivity, evidence, policy, review, release, and operations stewards | Use the verified repository-owner review route only |
| `HAB-SR-12` | `NEEDS VERIFICATION` | Verify product-specific endpoints, fields, terms, attribution, cadence, source-head method, classifications, and sensitivity | Do not copy planning values into operational records |
| `HAB-SR-13` | `NEEDS VERIFICATION` | Determine whether materiality thresholds/profile status are accepted for any live product | Keep the current profile synthetic and inactive |
| `HAB-SR-14` | `NEEDS VERIFICATION` | Inventory downstream consumers and harmful joins before any source revision is admitted | Fail closed on unknown impact |
| `HAB-SR-15` | `NEEDS VERIFICATION` | Verify hosted required-check significance and exact-head validation for future operational changes | Green checks remain bounded evidence |
| `HAB-SR-16` | `NEEDS VERIFICATION` | Reconcile other proposal-era Habitat runbooks with current repository evidence | This one-file update does not upgrade sibling maturity |

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

### Current repository evidence

| Evidence | What it supports | What it does not support |
|---|---|---|
| Accepted ADR-0029 and pinned Directory Rules | Existing `docs/` responsibility, same-path reconciliation, no parallel authority | Source admission, rights, sensitivity, or publication |
| Prior target blob | Confirms proposal-era live-refresh instructions being replaced | Proof that any proposed watcher or gate exists |
| Blank Habitat runbook README | Confirms lane README presence and missing content | Lane ownership or canonical child inventory |
| Duplicate domain runbook | Confirms a responsibility/path conflict | Authority to delete or migrate it |
| SourceDescriptor contract and schemas | Required source-governance concepts and proposed machine shape | An admitted Habitat source |
| Source-authority register | Empty, projection-only, implementation-absent posture | Activation or permission |
| Habitat registry READMEs and sampled YAMLs | Topology conflict and proposal-placeholder posture | Schema-valid accepted descriptors |
| Habitat connector compatibility index | Source-first posture, path conflicts, and no runtime under `connectors/habitat/` | A selected live connector |
| Habitat policy README | Proposed scaffold inventory and inactive evaluator/bundle posture | Active policy behavior |
| Habitat materiality contract/workflow | Synthetic no-network comparison vocabulary and exact validation commands | Live-source change, ecological truth, or promotion |
| Domain Habitat workflow | Bounded validation plus explicit proof/release holds | Evidence closure, release readiness, or publication |

### Google Drive planning lineage

The Drive Habitat architecture blueprint and Habitat + Fauna thin-slice blueprint are used only for planning lineage: source-family separation, model-versus-observation boundaries, native-classification preservation, geoprivacy, no-network fixtures, and the principle that Habitat assignments are derived rather than sovereign truth.

Both documents explicitly reported that no KFM repository was mounted in their authoring session and labeled concrete paths, routes, connectors, workflows, and implementation maturity as proposed or unknown. Current repository evidence therefore controls this runbook's implementation claims.

No external endpoint, current source release, license, cadence, or scientific threshold was verified in this documentation-only change.

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

### Before merge

- Keep the pull request draft.
- Close it if the repository evidence, placement basis, or one-file boundary is rejected.
- Delete or abandon only the feature branch after review policy permits.
- Do not modify source, connector, registry, policy, lifecycle, proof, release, or published state as part of documentation rollback.

### After merge

Revert the documentation commit through normal review or restore prior blob:

```text
1fecc4e6337ba2c897f4c4b328a33ea3bdba97e8
```

Then re-run repository-native documentation, link, topology, and changed-area validation.

Documentation rollback does not:

- reactivate the proposal-era watcher instructions;
- activate or deactivate a source;
- fetch or delete source material;
- change a registry, policy bundle, evidence object, lifecycle object, release object, deployment, or public artifact; or
- resolve the duplicate domain runbook or registry/connector topology conflicts.

[Back to top](#top)

---

<a id="non-effects"></a>

## Non-effects

This revision does not:

- activate, admit, suspend, refresh, or withdraw any Habitat source;
- call any external endpoint or connector;
- create or edit a `SourceDescriptor`, source-head observation, authority record, activation record, receipt, evidence object, policy decision, review record, lifecycle object, candidate, proof, release manifest, correction notice, withdrawal notice, or rollback card;
- select a registry, schema, connector, policy, evidence, or release authority;
- move, rename, delete, redirect, or supersede the duplicate domain runbook;
- populate the blank Habitat runbook lane README;
- change materiality criteria, validator behavior, fixtures, tests, workflows, policy source, runtime behavior, or public surfaces;
- cross RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED boundaries;
- approve review, promotion, release, deployment, or publication; or
- certify ecological, regulatory, legal, rights, sensitivity, freshness, completeness, or public-safety claims.

---

## Change history

| Version | Date | Change |
|---|---|---|
| `v0.1` | 2026-05-12 | Proposal-era full refresh procedure with illustrative watchers, conditional requests, lifecycle writes, gates, and release steps |
| `v0.2` | 2026-08-25 | Repository-grounded inspection-and-handoff runbook; live-source, activation, policy, lifecycle, promotion, release, deployment, and publication effects removed |

[Back to top](#top)
