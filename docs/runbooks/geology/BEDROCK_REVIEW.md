<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-geology-bedrock-review
title: Geology Bedrock Review Runbook
type: runbook
profile: candidate-review-and-handoff
version: v0.1
prior_version: unversioned scaffold
status: draft; repository-grounded; fixture-first; operational-admission-hold; non-authoritative; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Accountable geology, bedrock, source, rights, sensitivity, evidence, spatial, validation, policy, release, correction, rollback, and independent-review assignments remain NEEDS VERIFICATION."
created: 2026-08-25
updated: 2026-08-25
policy_label: public; no sensitive source payloads; no exact restricted point locations
current_path: docs/runbooks/geology/BEDROCK_REVIEW.md
owning_root: docs/
responsibility: "Provide a bounded human procedure for reviewing an immutable bedrock-geology candidate or fixture packet and handing off a truthful finite disposition without admitting a source, mutating lifecycle state, approving policy, releasing, deploying, promoting, or publishing."
truth_posture: "Cite or abstain. CONFIRMED statements are pinned to current repository evidence; planning-corpus material is LINEAGE; unverified runtime, source, rights, ownership, review, release, deployment, and publication claims remain UNKNOWN or NEEDS VERIFICATION."
prepared_under_prompt: "KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a125b5b949627898f5a0b0f52a0a09f53b0c0483
  target_prior_blob: b748f87dde046d4b10b32a7d1c9e89136f7429e1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  bedrock_sublane_blob: 36da8f88b4731d4ac5d23c4ba9c73080a35e04fb
  geologic_unit_schema_blob: e955613a2602d6ddc69ac03935b543a12aa41200
  ksgs_bedrock_descriptor_blob: bd4e74bb152f1fa3be461603e81e243ad7097e25
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  bedrock_pipeline_spec_blob: a8f4fb1e34f10e2253ee7022791cc903ca8b2328
  public_safe_geometry_policy_blob: 885369629be7ef92a219b8ae07625bfaea13c505
  public_safe_geometry_validator_blob: e523d0314fb5bc7eed18af1fed4dcf1204275e0b
  source_probe_fixture_blob: 094394e4ae2566e9be5f2181de7fef30b781ce08
inspection_boundary:
  - "Current repository bytes and directory listings were inspected through the GitHub connector."
  - "The connected Google Drive geology architecture report was used only as read-only planning lineage."
  - "No live KGS endpoint, source payload, credentials, deployed runtime, operational data store, release system, or public service was contacted or exercised."
  - "No active bedrock review candidate, admitted bedrock SourceDescriptor, completed EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, or RollbackCard was verified."
related:
  - docs/runbooks/README.md
  - docs/runbooks/geology/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - docs/runbooks/geology/ROLLBACK_RUNBOOK.md
  - docs/runbooks/geology/SOURCE_REFRESH_RUNBOOK.md
  - docs/domains/geology/README.md
  - docs/domains/geology/SUBLANE-BEDROCK.md
  - docs/domains/geology/sublanes/bedrock.md
  - docs/domains/geology/sublanes/bedrock_geology.md
  - contracts/domains/geology/GeologicUnit.md
  - schemas/contracts/v1/domains/geology/geologic_unit.schema.json
  - pipeline_specs/geology/bedrock_units.spec.yaml
  - pipelines/domains/geology/bedrock_units/README.md
  - connectors/kgs_bedrock/README.md
  - docs/sources/catalog/kansas/ksgs.md
  - data/registry/geology/sources/ksgs_bedrock.yaml
  - control_plane/source_authority_register.yaml
  - fixtures/contracts/v1/source/source_probe_envelope/valid/kgs_bedrock_changed.json
  - policy/domains/geology/
  - tools/validators/domains/geology/
  - fixtures/domains/geology/
  - tests/domains/geology/
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, runbook, geology, bedrock, geologic-unit, review, evidence, source-role, geometry, scale, uncertainty, rights, sensitivity, correction, rollback]
notes:
  - "This same-path update replaces a 762-byte PROPOSED scaffold with a repository-grounded review procedure."
  - "The runbook records current implementation gaps rather than converting planning documents, README depth, placeholders, or fixture presence into operational maturity."
  - "The default current disposition is HOLD unless a named immutable candidate packet and every applicable authority-bearing prerequisite are independently verified."
  - "Runbook outcomes are review-handoff labels, not canonical policy or lifecycle enums."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Bedrock Review Runbook

> **Purpose:** review one immutable bedrock-geology candidate or fixture packet for source identity, rights, map-unit meaning, geometry, scale, time, uncertainty, evidence, anti-collapse, sensitivity, correction, and rollback readiness—then emit a bounded handoff disposition without confusing review preparation with admission, policy approval, lifecycle promotion, release, deployment, or publication.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-current-determination)
[![Default disposition: HOLD](https://img.shields.io/badge/default%20disposition-HOLD-d29922?style=flat-square)](#finite-review-outcomes)
[![Network: denied by default](https://img.shields.io/badge/network-denied%20by%20default-6e7781?style=flat-square)](#fixture-first-rehearsal)
[![Source admission: not verified](https://img.shields.io/badge/source%20admission-not%20verified-d73a49?style=flat-square)](#status-and-current-determination)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)
[![Reviewed against main](https://img.shields.io/badge/base-a125b5b-0969da?style=flat-square)](#evidence-basis)

> [!IMPORTANT]
> **This runbook is an instruction surface, not an authority surface.** It may help a reviewer inspect a candidate and prepare a handoff. It cannot admit a source, establish rights, create evidence, approve policy, move an object through the KFM lifecycle, sign a review, release an artifact, deploy a service, promote a candidate, or publish a map.

> [!CAUTION]
> **A bedrock map is an interpretation at a stated source, edition, scale, vocabulary, and time.** A polygon, unit symbol, rendered tile, cross-section, source-probe event, or AI summary does not become observed field truth merely because it is authoritative-looking or visually precise.

> [!WARNING]
> **Do not mix exact borehole, well-log, sample, private-site, infrastructure, archaeology, land/title, or sensitive resource locations into an ordinary bedrock-unit review packet.** Mixed-sensitivity packets inherit the stricter handling requirement and must stop for the owning sensitivity and rights authorities.

**Quick navigation:** [Purpose](#purpose-scope-and-non-goals) · [Authority](#authority-and-negative-authority) · [Status](#status-and-current-determination) · [Outcomes](#finite-review-outcomes) · [Preconditions](#preconditions-and-stop-conditions) · [Packet](#required-review-packet) · [Procedure](#review-procedure) · [Candidate types](#candidate-type-checks) · [Rehearsal](#fixture-first-rehearsal) · [Handoff](#review-handoff-record) · [Sensitivity](#sensitivity-and-public-safe-geometry) · [Failures](#failure-modes-and-troubleshooting) · [Validation](#validation-and-claim-boundaries) · [Transitions](#promotion-release-correction-and-rollback-boundaries) · [Anti-patterns](#anti-patterns-to-refuse) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Maintenance](#maintenance-and-document-rollback)

---

## Purpose, scope, and non-goals

### Goal

Use this runbook when an authorized reviewer has a **named, immutable bedrock candidate or fixture packet** and needs to determine whether the packet is sufficiently coherent to hand to the next accountable review or governance stage.

The review concentrates on bedrock-unit and closely related representation concerns:

- mapped consolidated-rock units and source-native map-unit records;
- unit symbols, names, aliases, lithology, age, and stratigraphic references;
- contacts, structures, boundaries, and boundary-version lineage;
- map edition, source vintage, compilation scale, CRS, topology, and geometry fingerprints;
- interpreted or modeled surfaces, cross-sections, generalized layers, and their reality boundaries;
- source role, rights, attribution, evidence closure, sensitivity, correction, and rollback readiness.

### In scope

A review packet may contain one or more of the following, provided each object remains separately identified:

| Candidate kind | Review focus |
|---|---|
| Source-native bedrock map unit | Native code/name, map edition, legend relationship, source role, scale, and provenance |
| Normalized `GeologicUnit` candidate | Deterministic identity, source linkage, unit semantics, geometry lineage, and evidence |
| `GeologyBoundaryVersion` candidate | Boundary digest, source vintage, CRS, scale, uncertainty, supersession, and correction lineage |
| Contact or `StructureFeature` reference | Source evidence, feature class, interpretation status, confidence, and non-collapse with ordinary contacts |
| `CrossSection` or other interpretive representation | Method, source support, vertical/horizontal scale, uncertainty, `RealityBoundaryNote`, and `RepresentationReceipt` |
| Generalized or tiled bedrock derivative | Source candidate linkage, transform receipt, public-safe geometry, layer/release references, and rollback target |
| Fixture-only source-probe envelope | Change classification, source-role signal, no-network controls, and explicit non-effects |

### Out of scope

This runbook does not review or decide:

- live source activation, connector credentials, endpoint terms, or network access;
- surficial geology as if it were bedrock;
- borehole, well-log, core, sample, geophysics, or geochemistry truth as if it were a bedrock polygon;
- mineral occurrence, deposit, reserve, production, permit, lease, title, ownership, or economic recoverability;
- soil, hydrology measurement, hazard risk, archaeology, infrastructure, or land/title truth;
- emergency, engineering, excavation, drilling, groundwater, mineral-investment, or site-safety advice;
- publication through MapLibre, an API, a dashboard, a tile archive, a graph, a search index, or AI output;
- acceptance of any ADR, contract, schema, policy, source descriptor, release decision, or stewardship assignment.

### Success condition

The runbook succeeds when it produces a **truthful, reproducible handoff record** that:

1. pins the exact candidate and all inspected inputs;
2. records checks, evidence, gaps, and reason codes;
3. preserves the strictest applicable rights and sensitivity posture;
4. returns one finite review outcome;
5. names the next owning authority or verification action;
6. records a correction and rollback target for the review artifact itself;
7. performs no prohibited state transition.

A `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` can be the correct successful result.

[Back to top](#top)

---

## Authority and negative authority

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md). Under those rules, this file remains at its existing operational-documentation home:

```text
docs/
└── runbooks/
    └── geology/
        └── BEDROCK_REVIEW.md
```

### Directory Rules basis

| Placement axis | Determination |
|---|---|
| Artifact kind | Human operational procedure |
| Authority owner | `docs/` owns the explanation of the procedure |
| Scope | Geology domain, bedrock review |
| Lifecycle stage | Not a lifecycle data instance |
| Execution role | None; Markdown does not execute the review |
| Exposure | Public procedure; sensitive packet contents stay outside this file |
| Mutability | Versioned documentation |
| Placement outcome | `PLACE` as a same-path update; no new root, schema home, policy home, or parallel runbook authority |

### Authority map

| Concern | Owning surface | This runbook may | This runbook must not |
|---|---|---|---|
| Bedrock and geology scope | Geology doctrine and lane documentation | Cite and apply current boundaries | Settle competing doctrine documents by repetition |
| Object meaning | `contracts/domains/geology/` | Check candidate meaning against a named contract revision | Redefine `GeologicUnit` or related objects |
| Machine shape | `schemas/` | Record which schema and digest were applied | Treat a permissive scaffold as field validation |
| Source admission and role | SourceDescriptor, activation, registry, and source-policy surfaces | Verify refs and record their state | Activate KGS or assign authority by publisher name alone |
| Rights and sensitivity | Rights/sensitivity policy and authorized review | Check for a resolved decision | Infer reuse rights or public safety from web availability |
| Evidence | `EvidenceRef`, `EvidenceBundle`, receipts, and proofs | Resolve and cite support | Manufacture support from a map image or generated summary |
| Geometry validation | Spatial validators and reviewed outputs | Inspect named reports and bounded facts | Claim topology, CRS, or precision validation without evidence |
| Lifecycle state | Governed `data/` lifecycle and transition controls | Describe the candidate's recorded state | Move or relabel data by editing Markdown |
| Release and publication | `release/` plus accountable release authority | Check readiness references | Approve release, deployment, promotion, or publication |
| Correction and rollback | Correction/rollback object families and release controls | Verify a usable target exists | Silently overwrite or erase lineage |
| GitHub review routing | `.github/CODEOWNERS` | Route a PR to `@bartytime4life` | Treat routing as stewardship assignment or independent approval |

> [!NOTE]
> `.github/CODEOWNERS` verifies `@bartytime4life` as the repository review route. It explicitly does not prove that a geology steward, source steward, rights reviewer, sensitivity reviewer, evidence steward, spatial reviewer, policy authority, release authority, or independent reviewer has been assigned.

[Back to top](#top)

---

## Status and current determination

The table below is pinned to `main@a125b5b949627898f5a0b0f52a0a09f53b0c0483`. It describes repository bytes, not deployed or operational behavior.

| Surface | CONFIRMED current evidence | Review consequence |
|---|---|---|
| This file | Prior blob `b748f87...` was a 762-byte `PROPOSED scaffold` | Same-path modernization is justified |
| Bedrock scope docs | `SUBLANE-BEDROCK.md`, `sublanes/bedrock.md`, and `sublanes/bedrock_geology.md` all exist as authority-looking drafts | Bedrock documentation identity is `CONFLICTED`; this runbook applies shared noncontroversial boundaries and does not declare a winner |
| Semantic contract | `contracts/domains/geology/GeologicUnit.md` is a substantive draft contract | Useful semantic guidance exists; it is not an accepted machine contract or release decision |
| Machine schema | `geologic_unit.schema.json` exists, but has no defined properties and allows arbitrary additional properties | Schema presence does not validate a candidate's fields |
| KGS bedrock descriptor | `data/registry/geology/sources/ksgs_bedrock.yaml` is a greenfield template with role, authority, license, redistribution, sensitivity, cadence, access, and citation fields still `TBD` | No admitted KGS bedrock source is established by that file |
| Source authority register | `control_plane/source_authority_register.yaml` is `PROPOSED`, `implementation_status: ABSENT`, `completeness: empty`, with `entries: []` | Central source-authority projection does not close admission |
| KGS connector path | `connectors/kgs_bedrock/README.md` marks the path `NONCANONICAL` and records unresolved KGS path/package/slug/product-dispatch conflicts | Do not run or extend this compatibility path as a live connector |
| Bedrock pipeline spec | `pipeline_specs/geology/bedrock_units.spec.yaml` is a four-field `PROPOSED` placeholder | No executable bedrock pipeline contract is established |
| Bedrock pipeline docs | `pipelines/domains/geology/bedrock_units/README.md` is substantive documentation but says concrete behavior, activation, CI, schemas, and release wiring need verification | Documentation depth is not executable maturity |
| Source-probe fixture | A valid fixture records `profile: KGS_GEOLOGY`, `source_role: modeled`, `geology_kind: BEDROCK`, and all activation/lifecycle/promotion/publication effects as false | Safe for a no-network inspection rehearsal only |
| Geology golden fixture lane | `fixtures/domains/geology/golden/` contains a README and placeholder, not a verified bedrock candidate payload | No golden bedrock candidate was verified |
| Bedrock sublane fixture/test lane | Under `fixtures/domains/geology/sublanes/` and `tests/domains/geology/sublanes/`, only Surficial child lanes are present | No dedicated bedrock candidate fixture/test lane was verified |
| Public-safe policy | `public_safe_geometry.policy.json` is a placeholder; `public-geometry.rego` defaults to deny but has no bedrock rules | A policy decision must come from an actual evaluated, versioned policy surface—not from these placeholders |
| Ambiguity/publication policy | `abstain_on_ambiguous.rego` and `deny_unpublished.rego` are commented greenfield stubs with `default deny := false` | They do not enforce the stated names |
| Geology validators | `validate_schema.py` and `validate_evidence_bundle.py` raise `NotImplementedError`; `validate_public_safe_geometry.py` is a docstring-only placeholder | Do not claim executable validation from file presence |
| Public-safe geometry tests | The relevant test directory contains a README and `.gitkeep` only | No executable public-safe bedrock geometry test was verified |
| Active candidate and release objects | No active immutable bedrock candidate, completed review packet, release manifest, correction notice, or rollback card was verified in this inspection | Current default outcome is `HOLD` |

### Current determination

> [!IMPORTANT]
> **CONFIRMED current default:** `HOLD — NO_ACTIVE_BEDROCK_CANDIDATE_VERIFIED`.

The repository has substantial doctrine and documentation but does not currently provide enough verified source-admission, field-shape, fixture, validator, policy, ownership, or release evidence for this runbook to claim an operational bedrock review path is admitted.

This does **not** mean a reviewer can never use the procedure. It means the reviewer must bring a named immutable packet and independently satisfy the preconditions below. Missing infrastructure stays visible in the handoff rather than being papered over.

[Back to top](#top)

---

## Finite review outcomes

These are **runbook-local handoff labels**. They do not replace canonical policy outcomes, lifecycle states, review records, promotion decisions, or release states.

| Outcome | Use when | Required next action |
|---|---|---|
| `PASS_READY_FOR_ACCOUNTABLE_REVIEW` | The packet is internally coherent, all applicable checks have evidence, and no unresolved blocker remains within this runbook's scope | Hand off to the named accountable reviewer or governing transition; do not promote automatically |
| `HOLD` | A required input, authority, rights decision, source role, schema/contract revision, evidence resolution, validator result, owner, correction path, or rollback target is missing or conflicted | Preserve the prior state; create or update a bounded verification item |
| `ABSTAIN` | The reviewer cannot support a requested geology claim from the available admissible evidence, even though the packet may be technically well-formed | Narrow or remove the unsupported claim; record missing support |
| `DENY` | The packet attempts a prohibited collapse, unsafe exposure, rights bypass, direct public/internal path, fabricated evidence, or unauthorized transition | Stop processing, preserve evidence, and escalate to the owning authority |
| `ERROR` | The candidate cannot be parsed, hashes do not match, referenced objects are unavailable, validation tooling fails, or the review cannot be reproduced | Record the technical failure and retry only after the cause is resolved |
| `ESCALATE` | A qualified decision is needed from rights, sensitivity, geology, source, policy, release, Indigenous/community, security, or legal authority | Route the packet without changing its state |
| `SUPERSEDED` | A newer immutable candidate or source edition replaces the packet before review completes | Close the review against the old revision and link the successor; never silently reuse findings |
| `CANCELLED` | The requester withdraws the review or the scope is intentionally abandoned | Record cancellation and leave lifecycle/release state unchanged |

### Outcome precedence

When more than one condition applies, use the most conservative applicable result:

```text
DENY
  > ERROR
  > HOLD / ESCALATE
  > ABSTAIN
  > PASS_READY_FOR_ACCOUNTABLE_REVIEW
```

`SUPERSEDED` and `CANCELLED` describe terminal review-work states and still require lineage.

### PASS does not mean publication

`PASS_READY_FOR_ACCOUNTABLE_REVIEW` means only:

- the bounded human review procedure found no unresolved issue in the inspected packet;
- the exact evidence and limitations are recorded;
- the next authority may evaluate the handoff.

It does not mean:

- the source is admitted;
- the object is canonical;
- the policy result is allow;
- the candidate is processed, cataloged, released, deployed, promoted, or published;
- a public map may display it;
- AI may answer from it.

[Back to top](#top)

---

## Preconditions and stop conditions

### Preconditions

Before starting, the reviewer must have all applicable items below.

| Requirement | Minimum acceptable evidence |
|---|---|
| Authorized request | Issue, PR, review task, or recorded steward request naming the packet and scope |
| Immutable candidate identity | Commit/blob/content digest, object digest, or equivalent immutable reference |
| Candidate class | Source map unit, normalized unit, boundary version, structure/contact, cross-section, derivative, or fixture-only probe |
| Source identity | SourceDescriptor or explicit `NEEDS VERIFICATION` finding; publisher name alone is insufficient |
| Source material reference | Source record, map edition, legend, service layer/version, archival identifier, or immutable capture |
| Rights posture | Versioned rights/terms/attribution decision appropriate to intended use |
| Source role | Explicit observation, aggregate/compilation, modeled/inferred, administrative, candidate, contextual, regulatory, or synthetic posture |
| Spatial metadata | CRS, geometry type, source scale/resolution, geometry fingerprint, and topology status |
| Temporal metadata | Source publication/edition time, retrieval time, valid time where applicable, and supersession/stale state |
| Unit semantics | Source-native code/name plus normalized identity and linked lithology/age/interval refs as applicable |
| Evidence support | Resolvable EvidenceRefs and EvidenceBundle status for consequential claims |
| Sensitivity posture | Tier/access class and any required generalization/redaction decision |
| Validation evidence | Named validator/tool/version, exact inputs, result, and report digest; manual checks are labeled manual |
| Correction path | How an error, rename, boundary correction, rights change, or source supersession will be recorded |
| Rollback target | Prior immutable candidate/release or an explicit no-prior-state handling plan |
| Reviewer route | Named GitHub route plus accountable role assignment or `NEEDS VERIFICATION` blocker |

### Immediate stop conditions

Stop and return `HOLD`, `DENY`, `ERROR`, or `ESCALATE` when any of these apply:

- the packet revision changes during review;
- hashes, byte counts, geometry fingerprints, or cited revisions do not match;
- the source descriptor is missing or contains unresolved rights/source-role fields needed for the requested use;
- the source authority or connector path is assumed from a README, folder name, or publisher brand;
- a bedrock unit is being used as surficial, soil, hazard, resource, legal, ownership, or regulatory truth;
- a modeled or compiled boundary is presented as direct observation without interpretation disclosure;
- a cross-section or reconstructed surface lacks method, uncertainty, and reality-boundary information;
- exact borehole, well, sample, private-site, sensitive resource, infrastructure, archaeology, or land/person details appear in a routine public packet;
- an EvidenceRef does not resolve to the intended EvidenceBundle revision;
- a consequential claim has no admissible support;
- a required validator is absent, unimplemented, fails, or was run against different bytes;
- policy is inferred from a filename, default, comment, or placeholder;
- no correction route or rollback target exists for a candidate intended to affect public state;
- review authorship and accountable approval are improperly collapsed for a material or sensitive decision;
- the task asks the reviewer to publish, merge, deploy, or promote as part of the review itself.

### Safe pause behavior

On stop:

1. preserve the exact candidate and review inputs;
2. do not rewrite source bytes;
3. do not mutate lifecycle or release state;
4. record the outcome, reason code, evidence, and strictest applicable sensitivity;
5. identify the owning authority and smallest check that could resolve the blocker;
6. retain a rollback target for any review-document change;
7. hand off without speculative completion.

[Back to top](#top)

---

## Required review packet

The packet may be a governed object, review bundle, PR attachment, or structured worksheet. Because the current `geologic_unit.schema.json` is permissive and field-empty, this table is a **human review contract**, not proof of machine enforcement.

### Packet header

| Field | Requirement |
|---|---|
| `review_id` | Stable review-work identifier |
| `candidate_id` | Stable candidate identifier |
| `candidate_kind` | One finite kind from the declared scope |
| `candidate_revision` | Immutable commit/blob/digest/version |
| `candidate_content_sha256` | Digest of candidate bytes or canonicalized record |
| `requested_action` | Review-only, admission review, correction review, derivative review, or release-readiness review |
| `requested_claims` | Explicit list of claims the packet is expected to support |
| `reviewer` | Named actor or role; placeholders remain `NEEDS VERIFICATION` |
| `review_started_at` | UTC timestamp |
| `repository_revision` | Repository commit used for contracts, schemas, policy, and runbook |
| `sensitivity_ceiling` | Highest sensitivity present in the packet |
| `network_posture` | `DENIED`, `APPROVED_BOUNDED`, or governed equivalent |
| `prior_review_ref` | Prior review, or explicit `none` |
| `rollback_target_ref` | Prior immutable review/candidate/release or explicit no-prior-state plan |

### Source and rights block

| Field | Requirement |
|---|---|
| `source_descriptor_ref` | Exact descriptor revision |
| `source_id` | Source/product identifier, not only publisher |
| `publisher` | Human-readable publisher |
| `source_product` | Bedrock map/service/layer/edition/product |
| `source_record_ref` | Native record, unit, layer, map sheet, legend, or capture |
| `source_role` | Explicit claim-relative role |
| `source_publication_time` | Source edition/publication time |
| `retrieval_time` | KFM retrieval time |
| `rights_decision_ref` | Versioned rights/attribution/redistribution decision |
| `required_attribution` | Exact approved attribution or ref |
| `access_class` | Public, internal, steward-only, restricted, or governed equivalent |
| `source_limitations` | Scale, completeness, confidence, update, and authority limits |

### Unit and vocabulary block

| Field | Requirement |
|---|---|
| `source_unit_code` | Native map-unit symbol/code |
| `source_unit_name` | Native legend/unit name |
| `normalized_unit_id` | Deterministic KFM candidate identity |
| `normalized_unit_name` | Proposed normalized label |
| `unit_class` | Bedrock/source-map/composite/correlation/candidate/public-derivative/etc. |
| `lithology_refs` | Linked lithology records or explicit missing state |
| `age_refs` | Linked age records/vocabulary revision or explicit missing state |
| `stratigraphic_interval_refs` | Linked interval/correlation refs or explicit missing state |
| `vocabulary_version` | Geologic-map/stratigraphic vocabulary version |
| `aliases_and_correlations` | Source-specific aliases and reviewed correlations |
| `identity_method` | Inputs and normalization rules used to derive identity |
| `identity_conflicts` | Competing names, codes, editions, or correlations |

### Spatial, scale, and time block

| Field | Requirement |
|---|---|
| `geometry_ref` | Internal geometry reference |
| `geometry_type` | Polygon/MultiPolygon/LineString/etc. |
| `geometry_sha256` | Digest or stable fingerprint |
| `crs` | Full CRS identifier and axis/order assumptions |
| `source_scale` | Compilation/publication scale or equivalent resolution |
| `minimum_safe_use_scale` | Intended scale limit, if reviewed |
| `topology_status` | Valid/repaired/invalid/unknown plus report ref |
| `boundary_version_ref` | Versioned boundary lineage |
| `interpretation_version` | Source or KFM interpretation revision |
| `valid_time` | Time interval the assertion represents, if applicable |
| `supersedes` | Prior boundary/unit/edition ref |
| `stale_state` | Current, historical, stale, superseded, withdrawn, or unknown |
| `uncertainty` | Positional, thematic, temporal, correlation, and interpretation uncertainty |

### Evidence, validation, and governance block

| Field | Requirement |
|---|---|
| `evidence_refs` | Claim-level EvidenceRefs |
| `evidence_bundle_refs` | Resolved EvidenceBundle revisions |
| `citation_rendering` | Human-readable citations appropriate to the claims |
| `validation_report_refs` | Schema, geometry, vocabulary, identity, source-role, rights, and derivative reports |
| `manual_review_notes` | Manual checks clearly separated from automated checks |
| `policy_decision_refs` | Actual evaluated policy decisions, when required |
| `review_record_refs` | Prior or parallel review records |
| `representation_receipt_refs` | Required for generalization, tiling, interpolation, cross-sections, or other material representations |
| `reality_boundary_note_ref` | Required for reconstructed, inferred, synthetic, or interpretive representations where material |
| `correction_refs` | Corrections/supersessions already affecting the packet |
| `release_refs` | Candidate/release refs only when the requested action reaches release readiness |
| `open_findings` | Structured unresolved items |
| `requested_outcome` | Requested, not presumed, handoff result |

### Packet integrity

The packet must be:

- immutable or content-addressed;
- reproducible from named inputs;
- reviewable without network access unless a separate approved source check is in scope;
- free of credentials and unnecessary sensitive payloads;
- explicit about every missing field;
- accompanied by a manifest or inventory when more than one file is present.

[Back to top](#top)

---

## Review procedure

Use one review record for one immutable candidate revision. Restart or supersede the review if the candidate changes.

### Step 0 — Freeze scope, authority, and bytes

Record:

- candidate ID and exact digest;
- repository commit and runbook revision;
- contract, schema, policy, source descriptor, vocabulary, and validator revisions;
- requested claims and intended audience;
- expected lifecycle and release state before and after the requested action;
- packet manifest and byte/digest inventory;
- reviewer identities and unresolved role assignments;
- correction and rollback targets.

**Fail closed:** any moving ref, mutable URL without capture, unpinned schema/policy, or candidate change returns `HOLD` or `ERROR`.

### Step 1 — Classify the candidate and its requested claim

Ask:

1. Is this a source-native map record, normalized unit, boundary version, structure/contact, cross-section, derivative, or fixture event?
2. Which exact claims is the candidate expected to support?
3. Which claims are merely context?
4. Which claims belong to another object family or domain?
5. Is the requested action review-only, admission, correction, derivative, or release-readiness?
6. What is explicitly not being decided?

Record a candidate-to-claim matrix:

| Claim ID | Claim text | Candidate support role | Evidence ref | Review status |
|---|---|---|---|---|
| `<id>` | `<bounded statement>` | observation / aggregate / modeled / context / administrative / synthetic | `<ref>` | supported / unsupported / conflicted / unknown |

Unsupported consequential claims return `ABSTAIN`; prohibited substitutions return `DENY`.

### Step 2 — Verify source identity, admission, rights, and attribution

Check:

- the product-level SourceDescriptor exists and is pinned;
- its publisher, product, endpoint/capture, role, authority limits, rights, cadence, sensitivity, and citation fields are resolved;
- the source or capture used by the candidate matches that descriptor;
- rights and attribution apply to the intended storage, derivative, and exposure;
- source availability is not mistaken for redistribution permission;
- a catalog page or connector README is not used as activation authority;
- the requested use is within source terms and KFM access policy.

**Current repository warning:** the KGS bedrock descriptor template retains multiple `TBD` fields, and the central authority projection is empty. Unless a different admitted descriptor is supplied and verified, return `HOLD`.

### Step 3 — Verify native and normalized unit identity

Check:

- source-native unit symbol and name are preserved exactly;
- normalized ID construction is deterministic and documented;
- map edition/vintage participates in identity where boundaries or legend semantics differ;
- group/formation/member/composite/correlation relationships are not flattened;
- lithology, age, and interval are linked rather than silently copied into unit identity;
- aliases and correlations cite evidence and retain source-specific meaning;
- missing or ambiguous unit symbols do not receive guessed identifiers;
- renames or corrections retain predecessor/successor lineage.

Use `HOLD` for unresolved identity; use `ABSTAIN` for claims that depend on an unresolved correlation.

### Step 4 — Verify geometry, CRS, topology, and spatial identity

Check:

- geometry type is appropriate to the candidate;
- CRS is explicit, valid for the source, and not inferred from display coordinates;
- axis order, datum, units, and transformation history are recorded;
- geometry digest/fingerprint matches the inspected bytes;
- topology validation report is present and pinned;
- repairs, dissolves, clips, simplifications, reprojections, and generalizations have receipts;
- source boundaries are distinguishable from public-safe derivatives;
- geometry precision does not exceed what source scale and method support;
- no exact sensitive point records are embedded or inferable through properties or joins.

**Fail closed:** a visually plausible map is not geometry validation.

### Step 5 — Verify scale, source vintage, and temporal semantics

Check:

- compilation/publication scale or equivalent source resolution is recorded;
- use/display scale does not imply unsupported precision;
- source edition, publication time, retrieval time, and correction time are distinct;
- valid time is used only when the unit assertion genuinely has a temporal validity interval;
- historical editions are labeled historical, not stale by default;
- superseded boundaries and vocabulary revisions remain linked;
- a current-looking basemap or renderer does not silently update an old geology interpretation;
- comparison across editions uses explicit crosswalks and change methodology.

Return `HOLD` when scale or vintage is unknown and material to the claim.

### Step 6 — Verify source role and interpretation posture

Classify each supporting source or derived surface independently.

| Source pattern | Default review posture |
|---|---|
| Field observations or mapped contacts | Observation support with map-interpretation caveat |
| Statewide/county compilation or atlas | Aggregate/compiled interpretation; preserve scale and edition |
| Inferred contact, interpolated surface, or modeled extent | Modeled/inferred; uncertainty and method required |
| Legend code, catalog row, or identifier table | Administrative/vocabulary support; not geometry evidence by itself |
| Cross-section or reconstruction | Interpretive/synthetic representation; reality-boundary disclosure required |
| AI-generated wording | Interpretive only; never evidence |
| Source-probe change event | Operational signal; not source admission or domain truth |

Deny:

- modeled → observed relabeling;
- compiled map → field measurement relabeling;
- cross-section → measured subsurface truth relabeling;
- catalog metadata → unit existence proof;
- source-probe change → promotion;
- AI summary → EvidenceBundle.

### Step 7 — Resolve evidence and citations

For each consequential claim:

1. resolve every EvidenceRef;
2. verify the EvidenceBundle revision, source, excerpt/locator, spatial scope, temporal scope, and limitations;
3. verify the evidence supports the exact claim—not merely the topic;
4. confirm that source-role and interpretation caveats survive into the citation;
5. confirm citations can be rendered without exposing restricted data;
6. record conflicts rather than selecting the most convenient source;
7. use `ABSTAIN` when closure fails.

A digest proves byte identity. It does not prove authority, truth, rights, or fitness for the claim.

### Step 8 — Apply bedrock anti-collapse review

At minimum, test every applicable row.

| Prohibited collapse | Required distinction | Failure result |
|---|---|---|
| Bedrock unit → surficial unit | Consolidated-rock unit vs unconsolidated cover | `DENY` |
| Bedrock unit → soil map unit | Geology context vs Soil-owned pedologic unit | `DENY` |
| Bedrock unit → hazard risk | Physical geologic context vs Hazards-owned risk/exposure | `DENY` |
| Bedrock unit → mineral/resource claim | Rock unit vs occurrence/deposit/estimate/reserve/production | `DENY` |
| Bedrock unit → permit/lease/title/ownership | Physical geology vs administrative/legal record | `DENY` |
| Contact → fault | Ordinary boundary vs evidence-supported structural feature | `HOLD` or `DENY` |
| Unit polygon → exact field truth | Scale-bound interpretation vs direct observation | `HOLD` or `ABSTAIN` |
| Boundary version → eternal boundary | Versioned interpretation vs timeless fact | `DENY` |
| Well top/borehole point → continuous polygon | Point observation vs modeled surface | `DENY` without model receipt and evidence |
| Cross-section → observed structure | Interpretation vs measurement | `DENY` |
| Public tile → canonical geometry | Delivery carrier vs governed source/candidate | `DENY` |
| Review pass → release approval | Human handoff vs release decision | `DENY` |

### Step 9 — Check cross-lane references

For every Soil, Hydrology, Hazards, Resources, Archaeology, Infrastructure, or People/Land relation:

- identify the owning domain/object;
- preserve its ID, evidence, policy, and sensitivity state;
- ensure the bedrock candidate stores only a governed relation or context ref;
- ensure joins do not reveal protected locations;
- ensure one lane's validator is not claimed to validate another lane;
- ensure the relation is advisory unless a cross-domain contract says otherwise.

Missing owning-domain support returns `HOLD`; attempted ownership transfer returns `DENY`.

### Step 10 — Check sensitivity and public projection

Determine the strictest sensitivity among:

- source terms;
- candidate properties;
- geometry;
- joined records;
- evidence excerpts;
- derivative artifacts;
- intended audience and exposure.

Then check:

- exact restricted points are removed before rendering, not hidden by style;
- public geometry has a transform receipt and source linkage;
- attributes cannot reconstruct restricted locations;
- cross-section traces and profile data do not expose restricted subsurface records;
- the public candidate is separate from the internal source candidate;
- policy decision and reviewer obligations are explicit;
- denial/generalization reasons are preserved.

Unknown rights or sensitivity returns `HOLD` or `ESCALATE`.

### Step 11 — Check representation and derivative integrity

For generalized polygons, tiles, cross-sections, legends, or other rendered products, verify:

- source candidate and boundary version refs;
- build/transform inputs, tool versions, parameters, and output digest;
- scale/resolution/zoom limits;
- unit-code and source-layer preservation;
- generalization/simplification and topology effects;
- label, color, and symbol meaning;
- stale/correction state visibility;
- Evidence Drawer or equivalent evidence link requirements;
- `RepresentationReceipt` when the representation changes meaning or precision;
- `RealityBoundaryNote` for modeled/reconstructed/interpretive surfaces;
- rollback to the prior derivative.

A visually correct screenshot is not a representation proof.

### Step 12 — Check validation evidence

Classify each check as:

- `AUTOMATED_EXECUTED`;
- `MANUAL_EXECUTED`;
- `DOCUMENTED_ONLY`;
- `PLACEHOLDER`;
- `NOT_RUN`;
- `NOT_APPLICABLE`;
- `ERROR`.

For every executed check, record:

- tool/validator path and version;
- exact command or invocation;
- exact candidate and dependency revisions;
- start/end time;
- result and reason codes;
- report/output digest;
- environment and network posture;
- limitations.

**Current repository warning:** do not list the placeholder Geology schema/evidence/public-geometry validators as executed evidence unless a later revision implements and runs them.

### Step 13 — Check governance, correction, and rollback readiness

Before returning a pass-ready handoff, verify:

- accountable next reviewer or authority;
- policy decision ref where required;
- ReviewRecord plan;
- release candidate/ref only if release-readiness was requested;
- correction triggers for unit rename, geometry repair, source update, rights change, evidence withdrawal, vocabulary change, and source supersession;
- rollback target and cache/index/derivative invalidation plan where public state could change;
- no direct watcher/connector/pipeline/reviewer path to `PUBLISHED`;
- no author self-approval where separation is required.

Missing governance closure returns `HOLD` or `ESCALATE`.

### Step 14 — Derive and record the outcome

1. collect all findings;
2. resolve duplicate findings without deleting evidence;
3. determine the highest-precedence outcome;
4. state what the outcome proves and does not prove;
5. name the next owner and smallest resolving action;
6. pin the completed review record;
7. preserve the prior state;
8. hand off without performing the next transition.

[Back to top](#top)

---

## Candidate-type checks

Apply the common procedure above plus the appropriate focused checks.

### Source-native map-unit record

Confirm:

- map sheet/service/layer/edition identity;
- native legend row and unit symbol;
- source role and compilation caveat;
- map scale and intended use;
- original geometry and CRS;
- native attribution and rights;
- links to normalization without rewriting source-native fields.

### Normalized `GeologicUnit` candidate

Confirm:

- deterministic ID and normalization method;
- source-native fields retained;
- unit class explicit;
- lithology, age, and interval linked, not collapsed;
- geometry and boundary-version refs;
- source-role and interpretation version;
- evidence and rights closure;
- correction/supersession lineage.

Because the current schema is field-empty and permissive, a JSON Schema pass against that scaffold would prove only JSON/object compatibility, not semantic completeness.

### Boundary-version candidate

Confirm:

- source edition and prior boundary version;
- geometry digest and CRS;
- change method and materiality;
- positional/thematic uncertainty;
- correction or supersession reason;
- downstream derivative rebuild list;
- rollback to prior boundary version.

### Contact or structure candidate

Confirm:

- contact vs fault/fold/structure classification;
- source evidence and confidence;
- geometry and orientation attributes;
- source scale and method;
- no unsupported structural inference;
- Hazards relation remains advisory and separately governed.

### Cross-section candidate

Confirm:

- author/method and source data;
- section trace and coordinate reference;
- horizontal and vertical scale, including exaggeration;
- interpreted vs observed segments;
- uncertainty and alternatives;
- source borehole/well-log refs handled at their sensitivity level;
- `RealityBoundaryNote`;
- `RepresentationReceipt`;
- public-safe projection and rollback.

### Public derivative or tile candidate

Confirm:

- internal source candidate and release candidate refs;
- deterministic build manifest;
- source-layer/unit-code preservation;
- simplification/generalization parameters;
- zoom/scale limits;
- output digest and hosting assumptions;
- evidence/correction/stale-state link;
- no direct canonical/internal store access;
- release manifest and rollback target before any public use.

### Fixture-only source-probe envelope

Confirm:

- `fixture_only: true`;
- `network_access: DENIED`;
- `source_activation: false`;
- `lifecycle_write: false`;
- `promotion_allowed: false`;
- `publication_allowed: false`;
- change reason is treated as a watcher signal, not geology truth;
- referenced descriptor remains a ref, not an admission decision.

[Back to top](#top)

---

## Fixture-first rehearsal

The current repository includes:

```text
fixtures/contracts/v1/source/source_probe_envelope/valid/kgs_bedrock_changed.json
```

This fixture is useful for rehearsing **signal inspection and non-effect checks**. It is not a `GeologicUnit` fixture and does not prove KGS source admission, live access, normalization, geometry validation, evidence closure, policy enforcement, release, or publication.

### Preconditions

- use a clean checkout pinned to the intended repository commit;
- keep network access disabled;
- do not write to lifecycle, registry, receipt, proof, release, or published homes;
- do not alter the fixture during review;
- record the fixture blob or content digest;
- run only read-only standard-library checks unless a reviewed repository-native validator is separately verified.

### Read-only inspection

From the repository root:

```bash
python -m json.tool \
  fixtures/contracts/v1/source/source_probe_envelope/valid/kgs_bedrock_changed.json \
  >/dev/null
```

Then inspect the fixture's declared non-effects:

```bash
python - <<'PY'
import json
from pathlib import Path

path = Path(
    "fixtures/contracts/v1/source/source_probe_envelope/valid/"
    "kgs_bedrock_changed.json"
)
data = json.loads(path.read_text(encoding="utf-8"))
governance = data["governance"]

expected = {
    "fixture_only": True,
    "network_access": "DENIED",
    "source_activation": False,
    "lifecycle_write": False,
    "promotion_allowed": False,
    "publication_allowed": False,
}

for key, value in expected.items():
    actual = governance.get(key)
    if actual != value:
        raise SystemExit(
            f"{path}: governance.{key}={actual!r}, expected {value!r}"
        )

if data.get("profile_data", {}).get("geology_kind") != "BEDROCK":
    raise SystemExit(f"{path}: geology_kind is not BEDROCK")

if data.get("profile_data", {}).get("source_role") != "modeled":
    raise SystemExit(f"{path}: source_role is not modeled")

print("PASS: fixture declares no-network, no-activation, no-lifecycle-write, "
      "no-promotion, and no-publication behavior.")
PY
```

### Rehearsal result

Record one of:

- `PASS_FIXTURE_NON_EFFECTS_CONFIRMED`;
- `ERROR_FIXTURE_PARSE`;
- `ERROR_FIXTURE_NON_EFFECT_MISMATCH`;
- `HOLD_FIXTURE_REVISION_UNPINNED`.

These rehearsal labels remain subordinate to the runbook outcomes and are not policy, lifecycle, or release states.

### What this rehearsal proves

Only that, for the inspected bytes:

- the JSON parses;
- the expected governance flags are present;
- the fixture identifies a modeled bedrock source-probe change signal;
- the fixture declares non-activation and non-publication effects.

### What it does not prove

It does not prove:

- a live KGS product exists or changed;
- the referenced descriptor is admitted;
- rights or attribution are resolved;
- the candidate is a valid geologic unit;
- geometry exists or is valid;
- evidence resolves;
- policy ran;
- the pipeline exists;
- publication is allowed.

[Back to top](#top)

---

## Review handoff record

Use a durable review object if an accepted contract exists. Until then, the following Markdown/YAML-like structure is an **illustrative handoff template**, not a canonical schema.

```yaml
review_id: "kfm://review/geology/bedrock/<review-id>"
runbook:
  path: "docs/runbooks/geology/BEDROCK_REVIEW.md"
  revision: "<blob-or-commit>"
repository_revision: "<commit>"
candidate:
  id: "<candidate-id>"
  kind: "<candidate-kind>"
  revision: "<immutable-revision>"
  content_sha256: "sha256:<digest>"
requested_action: "<review-only|admission-review|correction-review|derivative-review|release-readiness>"
requested_claims:
  - claim_id: "<id>"
    statement: "<bounded statement>"
source:
  descriptor_ref: "<ref-or-NEEDS_VERIFICATION>"
  product: "<product>"
  source_record_ref: "<ref>"
  role: "<role>"
  publication_time: "<time>"
  retrieval_time: "<time>"
  rights_decision_ref: "<ref-or-NEEDS_VERIFICATION>"
spatial:
  geometry_ref: "<ref-or-N/A>"
  geometry_sha256: "sha256:<digest-or-N/A>"
  crs: "<crs-or-N/A>"
  source_scale: "<scale-or-N/A>"
  boundary_version_ref: "<ref-or-N/A>"
evidence:
  evidence_refs: []
  evidence_bundle_refs: []
validation:
  automated_executed: []
  manual_executed: []
  placeholders_encountered: []
findings:
  - finding_id: "<stable-id>"
    severity: "<blocker|major|minor|note>"
    status: "<open|resolved|accepted-limitation>"
    reason_code: "<code>"
    evidence_refs: []
    required_owner: "<role>"
    next_action: "<smallest resolving action>"
outcome: "<PASS_READY_FOR_ACCOUNTABLE_REVIEW|HOLD|ABSTAIN|DENY|ERROR|ESCALATE|SUPERSEDED|CANCELLED>"
outcome_reason_codes: []
proves:
  - "<bounded claim>"
does_not_prove:
  - "source admission"
  - "policy approval"
  - "lifecycle promotion"
  - "release"
  - "deployment"
  - "publication"
next_owner: "<verified identity or role NEEDS VERIFICATION>"
correction_ref: "<ref-or-plan>"
rollback_target_ref: "<ref-or-plan>"
completed_at: "<UTC timestamp>"
```

### Finding severity

| Severity | Meaning |
|---|---|
| `blocker` | Must resolve before accountable review or any state transition |
| `major` | Material semantic, evidence, rights, geometry, sensitivity, correction, or rollback defect |
| `minor` | Non-material issue that does not change the outcome but should be corrected |
| `note` | Context, limitation, or follow-up that is not a defect |

### Suggested reason-code families

These are documentation conventions, not a canonical registry:

```text
BEDROCK-AUTH-*       authority or ownership
BEDROCK-SOURCE-*     source identity, admission, role, cadence
BEDROCK-RIGHTS-*     rights, attribution, redistribution
BEDROCK-ID-*         unit identity, code, name, correlation
BEDROCK-GEOM-*       CRS, geometry, topology, scale, precision
BEDROCK-TIME-*       edition, retrieval, validity, stale/supersession
BEDROCK-EVID-*       EvidenceRef/EvidenceBundle/citation
BEDROCK-ROLE-*       observed/modeled/aggregate/admin/synthetic collapse
BEDROCK-XLANE-*      cross-lane ownership
BEDROCK-SENS-*       sensitivity, leakage, public-safe projection
BEDROCK-REP-*        representation, derivative, reality boundary
BEDROCK-VAL-*        validator, test, environment, reproducibility
BEDROCK-CORR-*       correction or supersession
BEDROCK-RB-*         rollback
BEDROCK-REL-*        release/publication boundary
```

### Handoff package

A review handoff should contain:

1. review record;
2. immutable packet manifest;
3. candidate and dependency digests;
4. claim-to-evidence matrix;
5. validation report inventory;
6. open findings;
7. strictest sensitivity label;
8. next-owner route;
9. correction and rollback refs;
10. explicit non-effects.

Do not attach unnecessary sensitive source payloads to a public PR.

[Back to top](#top)

---

## Sensitivity and public-safe geometry

Bedrock unit polygons are often lower sensitivity than subsurface points, but sensitivity is **packet-dependent**, not inherited from the word “bedrock.”

### Sensitivity inheritance

Use the strictest applicable posture from:

- source terms;
- native attributes;
- joined boreholes/wells/samples;
- private or proprietary locations;
- critical infrastructure relations;
- archaeology or cultural-resource relations;
- land/person data;
- sensitive mineral/resource occurrences;
- exact evidence locators;
- public derivative behavior.

### Public-safe review checklist

- [ ] Public geometry is a separate derivative, not the internal source geometry.
- [ ] Generalization/simplification/reprojection parameters are recorded.
- [ ] Transform receipt resolves to exact input and output digests.
- [ ] Unit identity and source edition survive the transform.
- [ ] Scale/zoom limits prevent false precision.
- [ ] Attributes do not expose restricted source IDs or exact coordinates.
- [ ] Centroids, bounding boxes, labels, URLs, and feature IDs do not leak sensitive detail.
- [ ] Cross-section traces do not reveal protected borehole/well locations.
- [ ] Public geometry policy was actually evaluated against the candidate.
- [ ] Reviewer obligations are satisfied.
- [ ] Correction and rollback invalidate affected tiles, caches, indexes, and exports where applicable.
- [ ] Evidence Drawer or equivalent public evidence view exposes only permitted support.
- [ ] Denied or generalized detail remains visible as a reasoned state, not silently absent.

### Fail-safe rule

When rights, sensitivity, geometry leakage, source authority, or review state is unresolved:

- preserve the internal candidate at its current governed state;
- do not create or expose a public derivative;
- return `HOLD`, `DENY`, or `ESCALATE`;
- record the needed authority and smallest resolving check.

[Back to top](#top)

---

## Failure modes and troubleshooting

| Symptom | Likely cause | Safe response |
|---|---|---|
| Candidate hash changes mid-review | Mutable branch/file or regenerated output | `ERROR`; freeze new revision and restart |
| Unit code is missing | Source legend loss or normalization defect | `HOLD`; recover native legend identity |
| Same unit name maps to different polygons | Different editions/scales/interpretations | Create distinct boundary versions; do not merge silently |
| Geometry renders but validator is absent | Visual inspection substituted for topology/CRS validation | `HOLD`; obtain executable validation evidence |
| Schema “passes” every object | Field-empty permissive scaffold | Record `PLACEHOLDER`; perform no completeness claim |
| KGS source is assumed admitted | Catalog/README/template mistaken for admission | `HOLD`; resolve product-level SourceDescriptor and authority |
| Source role is unclear | Publisher-level role applied to all products | `HOLD`; classify claim-relative role |
| Compiled map is labeled observed | Interpretation collapse | `DENY` or correct to aggregate/modeled/observation-with-caveat |
| Contact is labeled fault | Unsupported structural inference | `HOLD` or `DENY`; require structure evidence |
| Cross-section appears exact | Vertical exaggeration/interpretation not disclosed | `HOLD`; add reality-boundary and representation records |
| Public layer contains borehole IDs | Mixed-sensitivity join leakage | `DENY`; remove before derivative generation |
| EvidenceRef resolves to wrong revision | Stale or ambiguous evidence identity | `ERROR`/`HOLD`; pin correct bundle |
| Policy file exists but no decision record | Placeholder mistaken for evaluation | `HOLD`; require actual policy evaluation |
| Review requested to “approve and publish” | State-transition collapse | Complete review only; stop before release/publish |
| No prior release exists for rollback | First-release scenario | Require withdrawal/disable plan and immutable candidate retention |
| Bedrock docs disagree | Multiple draft authority-looking documents | Record `CONFLICTED`; apply higher authority and escalate convergence |
| Connector path differs across docs | KGS topology conflict | Do not choose by convenience; follow accepted migration authority |
| Tool raises `NotImplementedError` | Placeholder validator | Record `ERROR` or `NOT_RUN`; do not replace with manual pass silently |
| Source terms changed | Rights/cadence drift | `HOLD`; re-review rights and affected derivatives |
| Candidate was superseded | New source edition or correction | Mark `SUPERSEDED`; link successor and close old review |

### Troubleshooting discipline

- Never “fix” source bytes in place.
- Never suppress a validation error to obtain a pass.
- Never downgrade sensitivity to simplify handoff.
- Never infer missing CRS, scale, role, rights, or evidence without recording the inference and authority.
- Never let a manual check masquerade as an automated validator.
- Never delete a failed review; preserve it as lineage unless retention policy requires a governed alternative.

[Back to top](#top)

---

## Validation and claim boundaries

### Documentation validation for this runbook

A change to this file should verify at least:

- UTF-8 text with final newline;
- one top-level heading;
- balanced fenced code blocks;
- no trailing whitespace;
- valid relative-link targets for named repository paths where practical;
- no credentials, source payloads, or exact sensitive locations;
- truth labels preserved;
- current repository evidence rechecked at the PR head;
- no accidental change outside the intended file unless a direct dependency requires it.

### Candidate validation minimum

A real bedrock candidate review should include executable evidence for applicable checks:

| Check family | Minimum |
|---|---|
| Schema/shape | Field-bearing schema and validator, not the current permissive scaffold |
| Identity | Deterministic ID and duplicate/collision checks |
| Vocabulary | Unit symbol/name, lithology, age, interval, and alias checks |
| Geometry | Parse, CRS, validity, topology, bounds, coordinate range, and geometry digest |
| Scale/precision | Source-scale and intended-use constraints |
| Source role | Anti-collapse rules with negative fixtures |
| Evidence | EvidenceRef resolution and claim-level closure |
| Rights/sensitivity | Evaluated policy and reviewer obligations |
| Derivative | Deterministic transform/build and representation receipt |
| Correction/rollback | Replayable correction and rollback/withdrawal test |
| No-network | Fixture/default path proves no live access unless explicitly authorized |

### Current limitations

At the pinned repository revision:

- the bedrock schema does not enforce domain fields;
- several named geology validators are placeholders;
- relevant tests are largely documentation/placeholder lanes;
- no dedicated bedrock candidate fixture was verified;
- source admission and rights remain unresolved in the inspected KGS descriptor;
- no operational review authority or release route was verified.

Therefore a documentation-only PR can validate this runbook's structure and truthfulness, but it cannot validate a real bedrock candidate or claim operational readiness.

### Hosted CI

Hosted checks may lint Markdown, links, metadata, workflows, or broader repository constraints. A green hosted run proves only the checks actually executed against that exact head. It does not prove source admission, geology correctness, rights clearance, evidence truth, policy approval, release, deployment, or publication.

[Back to top](#top)

---

## Promotion, release, correction, and rollback boundaries

### Review-to-promotion handoff

This runbook stops at a handoff. Any later transition follows its owning procedure and authority:

```text
immutable candidate
  -> bedrock review handoff
  -> accountable domain/source/rights/spatial/evidence review
  -> validation and policy decisions
  -> governed lifecycle transition
  -> catalog/proof/release closure
  -> released public-safe carrier
  -> correction / withdrawal / rollback
```

Do not skip from review handoff to `PUBLISHED`.

### Relationship to sibling runbooks

| Procedure | Relationship |
|---|---|
| `NO_NETWORK_TEST_RUNBOOK.md` | Establishes broader fixture/no-network rehearsal posture |
| `SOURCE_REFRESH_RUNBOOK.md` | Handles authorized source refresh; a watcher signal does not activate the source |
| `PROMOTION_RUNBOOK.md` | Describes lifecycle promotion; this review does not perform it |
| `ROLLBACK_RUNBOOK.md` | Describes geology rollback; this review verifies that a usable rollback target exists |
| Root correction/revocation runbooks | Govern correction, withdrawal, or revocation when applicable |

The sibling documents are drafts and must be rechecked at the exact revision used. Their presence does not close their prerequisites.

### Correction triggers

A bedrock review or candidate may require correction when:

- unit code/name or correlation changes;
- source edition or legend is corrected;
- geometry is repaired or replaced;
- CRS/datum/scale metadata changes;
- evidence is withdrawn or superseded;
- rights or attribution changes;
- source role was misclassified;
- sensitivity leakage is discovered;
- public derivative diverges from the governed source candidate;
- a release references the wrong candidate or boundary version.

### Rollback targets

A review record should identify:

- prior runbook/review revision;
- prior candidate and boundary version;
- prior source descriptor/rights/policy revision;
- prior derivative/release where relevant;
- indexes, caches, tiles, exports, and AI/search projections affected by rollback;
- withdrawal behavior if no prior public release exists.

Rollback is not deleting history. It restores or disables exposure while preserving audit lineage.

[Back to top](#top)

---

## Anti-patterns to refuse

Refuse any request or implementation that:

- treats this runbook as approval authority;
- treats the attached planning report as current repository implementation proof;
- chooses one of the competing bedrock doctrine files without an authority/convergence decision;
- activates KGS because a catalog page, connector folder, or source template exists;
- assigns a publisher-wide source role to every KGS product;
- uses a field-empty schema as evidence of semantic completeness;
- cites placeholder validators as if they ran;
- upgrades README/test-folder presence to executable coverage;
- uses a source-probe change signal as a promotion trigger without governance;
- presents modeled, compiled, generalized, or synthetic geology as direct observation;
- infers a deposit, reserve, permit, production value, title, or hazard risk from a bedrock unit;
- hides exact sensitive records with client-side style filters;
- publishes an internal candidate or canonical geometry directly;
- lets an AI answer, map, tile, screenshot, graph, or dashboard become root truth;
- combines generation and approval into one unreviewed path;
- omits correction or rollback because “the map can be rebuilt”;
- silently edits, replaces, or deletes a failed/superseded review;
- interprets a PR, merge, green check, file move, or path under `data/published/` as governed publication.

[Back to top](#top)

---

## Open verification register

| ID | Status | Verification item | Why it blocks or limits use | Owning route |
|---|---|---|---|---|
| `BEDROCK-OPEN-001` | `CONFLICTED` | Reconcile `SUBLANE-BEDROCK.md`, `sublanes/bedrock.md`, and `sublanes/bedrock_geology.md` | Multiple draft authority-looking bedrock docs can drift | Geology + docs governance |
| `BEDROCK-OPEN-002` | `NEEDS VERIFICATION` | Assign accountable geology, bedrock, source, rights, sensitivity, evidence, spatial, validation, policy, release, correction, rollback, and independent-review roles | CODEOWNERS is only a GitHub route | Project owner / governance |
| `BEDROCK-OPEN-003` | `HOLD` | Admit a product-level KGS bedrock SourceDescriptor with rights, role, cadence, sensitivity, access, and citation resolved | Current descriptor is all-TBD template | Source + rights + geology |
| `BEDROCK-OPEN-004` | `CONFLICTED` | Resolve KGS path/package/slug/product-dispatch topology and compatibility migration | Current connector surfaces disagree | Connector + Directory Rules/ADR route |
| `BEDROCK-OPEN-005` | `NEEDS VERIFICATION` | Replace or graduate the placeholder bedrock pipeline spec with an accepted declarative contract | Current spec does not define behavior | Pipeline spec owner |
| `BEDROCK-OPEN-006` | `NEEDS VERIFICATION` | Complete the `GeologicUnit` schema and pair it with the actual contract path/casing | Current schema has no properties and is permissive | Contract + schema stewards |
| `BEDROCK-OPEN-007` | `NEEDS VERIFICATION` | Add deterministic identity, vocabulary, geometry, scale, source-role, evidence, and derivative validators | Named validators are absent or placeholders | Validation steward |
| `BEDROCK-OPEN-008` | `NEEDS VERIFICATION` | Add valid, invalid, edge, and public-safe bedrock candidate fixtures | No dedicated bedrock candidate fixture was verified | Fixture + geology stewards |
| `BEDROCK-OPEN-009` | `NEEDS VERIFICATION` | Add executable negative tests for bedrock/surficial, unit/resource, modeled/observed, contact/fault, and internal/public collapses | Documentation alone does not enforce anti-collapse | Test + policy stewards |
| `BEDROCK-OPEN-010` | `NEEDS VERIFICATION` | Implement and test ambiguity, unpublished, and public-safe geometry policy | Current files are stubs/placeholders | Policy steward |
| `BEDROCK-OPEN-011` | `NEEDS VERIFICATION` | Define the canonical review record, finding, reason-code, and handoff schema | This runbook's template is illustrative | Contract/schema governance |
| `BEDROCK-OPEN-012` | `NEEDS VERIFICATION` | Demonstrate EvidenceRef → EvidenceBundle closure for one synthetic bedrock candidate | Cite-or-abstain cannot be proven from docs | Evidence steward |
| `BEDROCK-OPEN-013` | `NEEDS VERIFICATION` | Demonstrate deterministic public-safe derivative build plus representation receipt and negative leakage tests | Public layer readiness is unproved | Spatial + release stewards |
| `BEDROCK-OPEN-014` | `NEEDS VERIFICATION` | Rehearse correction and rollback for a synthetic boundary-version change | Reversibility remains documentary | Correction + rollback owners |
| `BEDROCK-OPEN-015` | `NEEDS VERIFICATION` | Confirm hosted exact-head checks and required-check significance for a future implementation slice | CI presence is not enforcement evidence | Repository governance |
| `BEDROCK-OPEN-016` | `NEEDS VERIFICATION` | Replace the one-byte `docs/runbooks/geology/README.md` with a reviewed local index in a separate bounded change | Local navigation/ownership boundary remains weak | Docs/runbooks owner |
| `BEDROCK-OPEN-017` | `UNKNOWN` | Verify deployed runtime, source access, data stores, catalog closure, release tooling, public API/map behavior, and operational logs | Not inspected in this documentation update | Operations/runtime owners |

A future update should close only items verified from current evidence. Do not mark an item complete because a file was proposed or created.

[Back to top](#top)

---

## Evidence basis

### Current repository evidence

This edition was grounded in:

- accepted Directory Rules and ADR-0029;
- the current runbook-root contract;
- the prior target scaffold;
- the current geology landing and bedrock sublane documents;
- the `GeologicUnit` semantic contract and field-empty schema scaffold;
- the KGS source catalog, compatibility connector README, descriptor template, and empty authority projection;
- the placeholder bedrock pipeline spec and pipeline documentation;
- the fixture-only source-probe envelope;
- current policy, validator, fixture, and test surfaces;
- CODEOWNERS review routing.

### Connected Google Drive lineage

The connected **KFM Geology & Natural Resources Architecture** report was consulted as `LINEAGE / PROPOSED` planning input. It supports the enduring design pressure to:

- keep bedrock, surficial, subsurface, resource, regulatory, and modeled claims distinct;
- begin with source descriptors, schemas, fixtures, source-role policy, public-safe geometry checks, catalog closure, and an offline proof slice;
- carry source role, scale, time, evidence, rights, sensitivity, correction, and rollback;
- avoid live harvesting, UI claims, or model answers before trust closure.

That report explicitly said it had no mounted repository and that its paths and implementation details were proposed. Current repository evidence therefore outranks it for present implementation claims.

### Evidence classification

| Label | Use in this runbook |
|---|---|
| `CONFIRMED` | Verified from the pinned repository or connected source bytes |
| `PROPOSED` | A recommended procedure, packet field, role, reason code, or future implementation |
| `UNKNOWN` | Not established by accessible evidence |
| `NEEDS VERIFICATION` | A concrete check can resolve the matter |
| `CONFLICTED` | Current evidence contains competing authority-looking claims |
| `HOLD` | Work must stop until an authority or prerequisite is resolved |
| `LINEAGE` | Retained planning/history that does not prove current implementation |

### Evidence limits

This review did not verify:

- external KGS endpoints or terms;
- source activation;
- production data;
- live connectors or pipelines;
- current deployed services;
- runtime logs or dashboards;
- policy execution;
- release signer custody;
- public publication;
- actual stewardship assignments beyond CODEOWNERS routing.

[Back to top](#top)

---

## Maintenance and document rollback

### Update triggers

Re-review this runbook when any of these changes:

- accepted Directory Rules or runbook-root contract;
- canonical bedrock doctrine path;
- GeologicUnit contract or schema;
- source-role vocabulary;
- KGS source descriptor, authority, rights, or connector topology;
- bedrock pipeline spec or implementation;
- geometry/identity/evidence validators;
- policy rules or test coverage;
- review-record contract or reason-code registry;
- release/correction/rollback controls;
- public bedrock layer or governed API behavior;
- accountable ownership.

### Change discipline

For future edits:

1. freeze current `main`, target blob, open overlap, and relevant authority;
2. use the smallest complete same-path change;
3. separate current evidence from recommendations;
4. update commands only after verifying their paths and behavior;
5. preserve anchors where practical;
6. validate Markdown and relative links;
7. record changed claim boundaries;
8. keep the PR draft until human review;
9. do not merge, release, deploy, promote, or publish from this runbook update.

### Document rollback

The pre-modernization target is:

```text
path: docs/runbooks/geology/BEDROCK_REVIEW.md
blob: b748f87dde046d4b10b32a7d1c9e89136f7429e1
base: a125b5b949627898f5a0b0f52a0a09f53b0c0483
```

Rollback of this documentation change means restoring the prior blob or reverting the feature-branch commit through normal repository review. It does not roll back any data, source, policy, lifecycle, release, deployment, or publication state because this runbook update creates none.

### Final self-check

- [ ] One immutable candidate per review.
- [ ] Source product and role are explicit.
- [ ] Rights and sensitivity are resolved or fail closed.
- [ ] Native unit identity is preserved.
- [ ] Geometry, CRS, topology, scale, vintage, and uncertainty are evidenced.
- [ ] Modeled/compiled/interpretive support is not relabeled observed.
- [ ] Bedrock is not collapsed into surficial, soil, hazard, resource, legal, or ownership truth.
- [ ] Every consequential claim resolves evidence or abstains.
- [ ] Manual and automated checks remain distinct.
- [ ] Placeholder schemas, policy, validators, fixtures, and tests are labeled truthfully.
- [ ] Public-safe derivatives have transform/representation records and leakage checks.
- [ ] Correction and rollback targets exist.
- [ ] Outcome is finite and bounded.
- [ ] Review performs no admission, policy approval, promotion, release, deployment, or publication.

---

*Version `v0.1` · repository-grounded substantive replacement of the prior scaffold · base `main@a125b5b949627898f5a0b0f52a0a09f53b0c0483` · default current disposition `HOLD`*

[Back to top](#top)
