<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/habitat/ecoregions/readme
title: Habitat Ecoregions Runbooks — Operational Procedure Boundary
type: readme
subtype: sublane-runbook-boundary
version: v0.1.0
status: draft; repository-grounded; documentation-only; incomplete-procedure-lane; non-authoritative; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Habitat, ecoregions, source, spatial, evidence, policy, validation, release, rollback, and independent-review stewards"
created: 2026-08-25
updated: 2026-08-25
policy_label: public-review; habitat; ecoregions; operational-documentation; fail-closed; no-publication-authority
current_path: docs/runbooks/habitat/ecoregions/README.md
owning_root: docs/
responsibility: "Define the human-facing procedure boundary, current maturity, safe entry conditions, stop states, and handoffs for Habitat ecoregion operations without granting source admission, evidence, policy, lifecycle, review, release, deployment, promotion, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational-documentation boundary
canonical_relationship: same-path completion of an existing tracked one-byte blank file; no sibling procedure or authority home created
repository: bartytime4life/Kansas-Frontier-Matrix
evidence_snapshot:
  base_ref: main
  base_commit: 434195e8727e6e8649fd6a9e7de06808c3e15261
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  direct_child_count_including_this_readme: 2
  source_refresh_blob: d4cc1c429c7d2894cbb5f2b70eb3e36863cd6490
  proposed_omernik_descriptor_blob: d1d05fd638e115a3108b3b31ddfb16584ac0b56a
  source_registry_readme_blob: 55ea86c6eb12456570a47b630315329c34aa45c8
  schema_readme_blob: 36a47240f9a9d3e4d2e389b974c7a85061b657fd
  pipeline_readme_blob: fbe2a74412cb88e299db5532b27c541f5c95cf67
  fixture_tree:
    entries: [".gitkeep", "README.md"]
  test_tree:
    entries: [".gitkeep", "README.md"]
related:
  - docs/runbooks/README.md
  - docs/runbooks/habitat/README.md
  - docs/runbooks/habitat/ecoregions/SOURCE_REFRESH.md
  - docs/domains/habitat/sublanes/ecoregions.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - data/registry/habitat/sources/ecoregions_omernik.yaml
  - data/registry/sources/habitat/ecoregions/README.md
  - contracts/domains/habitat/ecoregions/README.md
  - schemas/contracts/v1/domains/habitat/ecoregions/README.md
  - pipelines/domains/habitat/ecoregions/README.md
  - pipeline_specs/habitat/ecoregions/README.md
  - fixtures/domains/habitat/ecoregions/README.md
  - tests/domains/habitat/ecoregions/README.md
  - release/candidates/habitat/ecoregions/README.md
notes:
  - "The prior target contained only a newline. This edition supplies the missing local procedure boundary without moving, renaming, creating, activating, or executing an ecoregion operation."
  - "SOURCE_REFRESH.md remains an explicit PROPOSED scaffold and is not upgraded by this README."
  - "The current Omernik descriptor is a PROPOSED greenfield template with unresolved role, authority, rights, sensitivity, cadence, access, and citation fields."
  - "The ecoregion fixture and test directories contain only README.md plus .gitkeep at the pinned snapshot; no executable ecoregion fixture/test proof is claimed."
  - "Google Drive Habitat architecture material is retained as planning lineage only; current repository evidence controls current-state claims."
  - "This document changes no source, connector, contract, schema, policy, fixture, test, validator, pipeline, workflow, lifecycle object, evidence object, release record, deployment, promotion, rollback execution, publication, or repository setting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Ecoregions Runbooks — Operational Procedure Boundary

> **Start here before attempting an ecoregion source refresh, validation rehearsal, lifecycle handoff, release review, correction, or rollback.** This directory documents how an authorized actor should orient and stop safely; it does not supply the authority, evidence, executable implementation, policy decision, review, release decision, or public state that an operation requires.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![Direct procedure files: 1](https://img.shields.io/badge/direct%20procedure%20files-1-0969da?style=flat-square)](#direct-child-map)
[![Operational closure: HOLD](https://img.shields.io/badge/operational%20closure-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Network: not authorized](https://img.shields.io/badge/network-not%20authorized-b91c1c?style=flat-square)](#source-refresh-entry-gate)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Ecoregions are regionalization context.** A polygon may classify a place under a named framework, hierarchy level, source version, and boundary version. It does not prove species occurrence, plant occurrence, habitat quality, regulatory critical habitat, hydrologic truth, soil truth, hazard truth, land/title truth, management priority, or release state.

> [!CAUTION]
> **The only direct procedure file is still a scaffold.** [`SOURCE_REFRESH.md`](./SOURCE_REFRESH.md) names the Habitat ecoregions sublane but does not provide verified owners, source admission, commands, validators, fixtures, tests, pipeline entry points, release gates, or rollback evidence. Treat operational execution as `HOLD`.

> [!WARNING]
> Ecoregion polygons are generally low-sensitivity context, but joins can expose or help infer rare species, rare plants, archaeological or cultural resources, private land, infrastructure, or other protected detail. Sensitive joins fail closed until the owning domain, policy, evidence, review, public-safe transform, release, correction, and rollback authorities resolve them.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [Placement](#placement-and-canonical-relationship) · [State](#current-repository-state) · [Children](#direct-child-map) · [Start here](#start-here) · [Operating law](#ecoregion-operating-law) · [Lifecycle](#lifecycle-and-state-separation) · [Refresh gate](#source-refresh-entry-gate) · [Handoffs](#inputs-outputs-and-responsibility-handoffs) · [Outcomes](#finite-outcomes-and-stop-conditions) · [Sensitivity](#sensitivity-and-cross-lane-joins) · [Validation](#validation-and-rehearsal-boundary) · [Maintenance](#maintenance-and-review-triggers) · [Open work](#open-verification-backlog) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback)

---

## Purpose

`docs/runbooks/habitat/ecoregions/` is the human-readable operational-procedure sublane for Habitat ecoregions. It helps a maintainer, reviewer, steward, developer, or operator answer bounded questions before touching a source or candidate:

- What ecoregion procedure exists at the current revision?
- Is the procedure repository-grounded, proposal-era, executable, reviewed, admitted, or held?
- Which source identity, native framework, hierarchy, version, rights, sensitivity, evidence, policy, validation, release, correction, and rollback records must exist first?
- Which action belongs to a source registry, connector, pipeline, validator, policy engine, lifecycle store, evidence resolver, review surface, or release system rather than Markdown?
- Which condition requires `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, quarantine, or escalation?
- Which records must remain inspectable after a source change, correction, supersession, withdrawal, or rollback?

This directory is documentation-first. It may route readers to owning systems and record safe procedure boundaries. It must not become a second source registry, semantic contract, schema authority, policy engine, validation implementation, evidence store, release plane, or publication path.

[Back to top](#top)

---

## Authority and negative authority

Accepted [`ADR-0029`](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the Directory Rules bytes at [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md). Those rules place human operational procedures under `docs/runbooks/` and require local README boundaries to explain responsibility, inheritance, exposure, lifecycle behavior, and non-effects without creating parallel authority.

| Concern | Owning authority | This directory's role |
|---|---|---|
| Documentation placement and inheritance | Accepted Directory Rules, the [root runbook contract](../../README.md), and the [Habitat runbook parent](../README.md) | Define the ecoregion procedure boundary and disclose current drift |
| Habitat ecoregion meaning | [Habitat ecoregions sublane](../../../domains/habitat/sublanes/ecoregions.md) plus accepted semantic contracts | Orient readers; do not redefine the domain |
| Source identity, role, rights, cadence, access, and admission | `SourceDescriptor`, source-registry, source-head, and activation-decision authorities | Require and reference them; do not admit or activate a source |
| Object meaning | [`contracts/domains/habitat/ecoregions/`](../../../../contracts/domains/habitat/ecoregions/README.md) | Cite semantics; do not duplicate them |
| Machine shape | [`schemas/contracts/v1/domains/habitat/ecoregions/`](../../../../schemas/contracts/v1/domains/habitat/ecoregions/README.md) | Cite an accepted schema; do not define one here |
| Executable transformation | [`pipelines/domains/habitat/ecoregions/`](../../../../pipelines/domains/habitat/ecoregions/README.md) and accepted source connectors | Point to verified entry points when they exist; do not embed implementation in Markdown |
| Declarative run configuration | [`pipeline_specs/habitat/ecoregions/`](../../../../pipeline_specs/habitat/ecoregions/README.md) | Cite accepted specs; do not make prose executable |
| Allow, restrict, deny, hold, or abstain | [`policy/domains/habitat/`](../../../../policy/domains/habitat/README.md) plus required human review | Explain how to obtain and respond to a decision |
| Expected behavior | [`fixtures/domains/habitat/ecoregions/`](../../../../fixtures/domains/habitat/ecoregions/README.md) and [`tests/domains/habitat/ecoregions/`](../../../../tests/domains/habitat/ecoregions/README.md) | Require deterministic proof; do not manufacture it |
| Lifecycle instances | Governed `data/` phases and accountability families | Describe a transition; do not perform one through documentation |
| Evidence, receipts, proofs, and catalog closure | Their governed `data/` object families | Require resolvable support; do not treat a runbook as evidence |
| Promotion, release, correction, withdrawal, rollback | `release/` and linked accountability objects, including the [ecoregion candidate lane](../../../../release/candidates/habitat/ecoregions/README.md) | Describe an authorized procedure; do not approve or execute it |
| This README | Human navigation, maturity disclosure, stop rules, and maintenance contract | No source, policy, evidence, lifecycle, review, release, deployment, promotion, rollback-execution, or publication authority |

A procedure must stop when its named authority, source identity, permission, evidence, policy result, review, executable entry point, correction path, or rollback target is unresolved. A README cannot turn `UNKNOWN`, `NEEDS VERIFICATION`, or `HOLD` into permission.

[Back to top](#top)

---

## Placement and canonical relationship

**Placement outcome: `PLACE` — CONFIRMED for this same-path additive completion.**

| Property | Current result |
|---|---|
| Path | `docs/runbooks/habitat/ecoregions/README.md` |
| Owning root | `docs/` — human-readable operational documentation |
| Scope | Habitat ecoregions procedure sublane |
| Prior path state | Existing tracked one-byte blank file at blob `8b137891…` |
| Structural effect | None; no create, move, rename, split, mirror, compatibility lane, or delete |
| Authority effect | None; documents current boundaries and evidence only |
| Verified GitHub review route | `@bartytime4life` through the repository default route |
| Accountable domain and independent stewardship | `NEEDS VERIFICATION` |
| Release and publication effect | None |

This README is the local procedure boundary for its direct children. The [Habitat parent README](../README.md) currently contains only a newline and therefore adds no substantive local procedure contract at the pinned revision. The [repository-wide runbook index](../../README.md) supplies inherited operating doctrine but is pinned to an earlier inventory snapshot. Neither parent should be silently rewritten by this narrow leaf completion.

The domain charter at [`docs/domains/habitat/sublanes/ecoregions.md`](../../../domains/habitat/sublanes/ecoregions.md) owns human-facing ecoregion meaning. It is not an operational procedure and does not make its proposed paths, source choices, commands, or implementation claims current by repetition.

[Back to top](#top)

---

## Current repository state

The observations below are pinned to `main@434195e8727e6e8649fd6a9e7de06808c3e15261`. They describe tracked repository bytes and bounded directory inventories, not deployed behavior, source activation, operational admission, release readiness, or publication.

| Surface | CONFIRMED evidence at the pinned revision | Bounded conclusion |
|---|---|---|
| This README | Existing tracked file contained only a newline | Local ecoregion procedure boundary was absent in substance |
| Direct directory | This README plus [`SOURCE_REFRESH.md`](./SOURCE_REFRESH.md) | One direct procedure file exists; there is no local no-network, promotion, correction, or rollback procedure |
| `SOURCE_REFRESH.md` | Exact `PROPOSED scaffold` marker; asks maintainers to fill owners, validation, and links | Planning placeholder only; no live refresh is authorized |
| Domain charter | Substantive draft that defines ecoregions as framework/versioned regionalization context | Useful semantic orientation; several implementation and source claims remain proposals |
| Omernik descriptor | [`data/registry/habitat/sources/ecoregions_omernik.yaml`](../../../../data/registry/habitat/sources/ecoregions_omernik.yaml) is labeled `PROPOSED — greenfield template`; role, authority, rights, sensitivity, cadence, access, and citation remain `TBD` | It is not an admitted, activation-ready source descriptor |
| Source-registry guidance | [`data/registry/sources/habitat/ecoregions/README.md`](../../../../data/registry/sources/habitat/ecoregions/README.md) is substantive but experimental and reports unresolved domain-first versus subtype-first registry topology | Source-registry authority and final path topology remain `NEEDS VERIFICATION`; do not write divergent descriptors |
| Contract lane | Ecoregion contract README exists, but candidate contract files are proposed | Semantic object-family closure is not established |
| Schema lane | Ecoregion schema README exists and reports no confirmed concrete schema inventory | Machine-shape closure is not established |
| Pipeline lane | Pipeline README exists and labels concrete behavior, source activation, schedules, CI, and release wiring `NEEDS VERIFICATION` | No executable ecoregion pipeline is proven by its README |
| Fixture lane | Directory contains only `.gitkeep` and `README.md` | No deterministic ecoregion fixture payload is present in that lane |
| Test lane | Directory contains only `.gitkeep` and `README.md` | No executable ecoregion test module is present in that lane |
| Public or release state | Documentation lanes exist for candidates and published carriers | File presence does not prove a release decision, released artifact instance, hosting, deployment, or publication |
| Owners and separation of duties | Default GitHub review route exists; named domain/source/policy/release stewards are placeholders | Accountable review, independent review, and operational authorization remain `NEEDS VERIFICATION` |
| Live source access | No current source terms, endpoint, credentials posture, retrieval rehearsal, or activation decision was verified for this change | Network access and source refresh remain `HOLD` |

### State separation

Do not collapse these states:

| Axis | Example |
|---|---|
| File presence | README or YAML bytes exist |
| Documentation state | Blank, scaffold, draft, repository-grounded, corrected, or current at a pinned revision |
| Source-admission state | Candidate, denied, quarantined, admitted, suspended, or superseded |
| Executable state | No implementation, partial implementation, tested implementation, or operationally admitted implementation |
| Validation state | Schema/contract/geometry/source-role checks pass or fail against named inputs |
| Rehearsal state | Procedure ran in an approved non-public environment with recorded outputs |
| Evidence state | `EvidenceRef` resolves to an admissible `EvidenceBundle` |
| Review state | Required accountable and independent reviewers acted |
| Lifecycle state | Governed data/object transition occurred |
| Release state | A specific immutable candidate received a release decision |
| Publication state | A public-safe carrier is actually exposed through governed delivery |

[Back to top](#top)

---

## Direct-child map

Directory Rules require a leaf README to show only the directory it governs and its direct children.

```text
docs/runbooks/habitat/ecoregions/
├── README.md
└── SOURCE_REFRESH.md
```

| Child | Primary question | Current posture | Use boundary |
|---|---|---|---|
| [`SOURCE_REFRESH.md`](./SOURCE_REFRESH.md) | How might the ecoregion source-refresh procedure eventually be documented? | `PROPOSED scaffold` | Do not use to admit, activate, fetch, schedule, transform, promote, release, or publish a source |

Missing procedures are not silently invented here. A no-network rehearsal, validation, promotion, correction, withdrawal, or rollback procedure may be added later only when a verified task requires it, placement is checked, direct dependencies are closed, and exact executable evidence supports the instructions.

[Back to top](#top)

---

## Start here

| Intended task | Current entry point | Current result |
|---|---|---|
| Understand ecoregion meaning and non-ownership | [Habitat ecoregions sublane](../../../domains/habitat/sublanes/ecoregions.md) | Use as draft semantic orientation |
| Inspect current source-registry posture | [Ecoregions source-registry README](../../../../data/registry/sources/habitat/ecoregions/README.md) | Review topology conflict and admission requirements |
| Inspect the only named source record | [Omernik descriptor template](../../../../data/registry/habitat/sources/ecoregions_omernik.yaml) | `HOLD`; required fields remain unresolved |
| Plan a source refresh | [`SOURCE_REFRESH.md`](./SOURCE_REFRESH.md) | `HOLD`; scaffold only |
| Run a deterministic no-network ecoregion test | [Fixture lane](../../../../fixtures/domains/habitat/ecoregions/README.md) and [test lane](../../../../tests/domains/habitat/ecoregions/README.md) | `HOLD`; no fixture payload or executable test module present in those lanes |
| Run an ecoregion pipeline | [Pipeline lane](../../../../pipelines/domains/habitat/ecoregions/README.md) | `HOLD`; README does not prove implementation |
| Promote or release an ecoregion carrier | [Candidate lane](../../../../release/candidates/habitat/ecoregions/README.md) plus governing release authorities | `HOLD` unless an exact candidate, proof, policy, review, correction, and rollback chain resolves |
| Correct or roll back public state | Governing correction/rollback objects and a future repository-grounded procedure | `HOLD`; no local executable procedure is present |

[Back to top](#top)

---

## Ecoregion operating law

### Required distinctions

| Distinction | Rule |
|---|---|
| Framework | Keep EPA/Omernik, USFS/Bailey, state, regional, and other frameworks separately addressable unless an accepted crosswalk explicitly relates them |
| Hierarchy | Preserve framework-native levels and parent/child relations; do not silently promote Level III to Level IV or flatten hierarchy |
| Source version | Pin edition, publication/source time, retrieval time, and content identity where material |
| Boundary version | Treat geometry changes as versioned changes, not cosmetic redraws |
| Source role | Use the repository's accepted source-role vocabulary; legacy words such as `authority`, `context`, or `model` require explicit mapping before claim-bearing use |
| Observation versus context | Ecoregion geometry classifies a place; it does not observe an organism, habitat condition, or regulatory action |
| Crosswalk | Record source frameworks, method, loss, confidence, review, correction, and rollback; a crosswalk is not automatic equivalence |
| Derived carrier | PMTiles, MVT, GeoParquet, map styling, summaries, indexes, and graph edges remain downstream representations |
| Evidence | Claim-bearing output resolves `EvidenceRef -> EvidenceBundle` or returns a finite non-answer |
| Release | A file path, green test, map render, commit, pull request, merge, or generated artifact is not promotion or publication |

### Forbidden truth upgrades

```text
ecoregion polygon -> species occurrence truth
ecoregion polygon -> plant occurrence truth
ecoregion polygon -> habitat condition or suitability truth
ecoregion polygon -> regulatory critical-habitat truth
ecoregion context -> hydrology, soil, hazard, agriculture, or land/title truth
framework A -> framework B without a governed crosswalk
source version A -> source version B without lineage and correction handling
pipeline success -> evidence closure
test success -> source admission
release-candidate bytes -> release approval
map visibility -> publication authority
generated summary -> sovereign truth
```

[Back to top](#top)

---

## Lifecycle and state separation

The inherited lifecycle remains:

```text
SOURCE EDGE / ADMISSION
    -> RAW
    -> WORK or QUARANTINE
    -> PROCESSED
    -> CATALOG / TRIPLET
    -> RELEASE DECISION
    -> PUBLISHED public-safe carrier
    -> CORRECTION / WITHDRAWAL / ROLLBACK / RECOMPILE
```

| Stage | Permitted procedure concern | Prohibited shortcut |
|---|---|---|
| Source edge | Verify source identity, role, rights, access, cadence, versioning, sensitivity, and activation decision | Fetch because a URL or YAML template exists |
| RAW | Preserve immutable source bytes or references plus content identity and intake receipt | Rewrite the source or expose it publicly |
| WORK | Normalize, compare, inspect hierarchy, validate geometry/CRS, and record candidate transforms | Treat work output as canonical or released |
| QUARANTINE | Hold malformed, rights-unclear, source-role-conflicted, over-precise, or unsupported material | Auto-promote after a documentation edit |
| PROCESSED | Store validated candidate records with source/version/evidence lineage | Upgrade regionalization context into observation truth |
| CATALOG / TRIPLET | Create downstream discovery and relationship projections from governed records | Treat catalog or graph projection as root truth |
| RELEASE | Evaluate immutable candidate, validation, policy, evidence, review, rights, sensitivity, correction, and rollback closure | Publish because a candidate directory exists |
| PUBLISHED | Serve only released, public-safe carriers through governed interfaces | Let public clients read RAW, WORK, QUARANTINE, source registry, or direct model output |
| Correction / rollback | Preserve supersession, withdrawal, cache invalidation, lineage, prior release, and rollback target | Silently overwrite or delete history |

Promotion is a governed state transition, not a file move. This README cannot advance any stage.

[Back to top](#top)

---

## Source-refresh entry gate

A future ecoregion refresh must remain `HOLD` until every applicable prerequisite below is supported by current evidence.

### 1. Authority and task contract

- [ ] Exact source and refresh scope are named.
- [ ] Base revision, target paths, actors, permissions, non-goals, acceptance criteria, stop conditions, and rollback are pinned.
- [ ] Open pull requests, branches, migrations, and active source work were checked for overlap.
- [ ] Accountable Habitat/ecoregions steward and required independent reviewers are identified.

### 2. Source admission

- [ ] One canonical `SourceDescriptor` resolves with a stable source identifier.
- [ ] Source role uses the accepted enum and is appropriate for the claim.
- [ ] Native framework, hierarchy, edition/version, authority scope, spatial scope, and temporal scope are explicit.
- [ ] Rights, attribution, redistribution, derivative use, access, citation, and retention are reviewed.
- [ ] Sensitivity and precision posture are recorded.
- [ ] Activation state permits the named controlled intake.
- [ ] Domain-first versus subtype-first registry topology is resolved for the exact descriptor; no divergent writable record is created.

### 3. Deterministic identity and change detection

- [ ] Upstream version or source head can be identified reproducibly.
- [ ] Retrieval time and source publication/effective time remain distinct.
- [ ] Content checksum, ETag, Last-Modified value, release identifier, or another approved source-head signal is recorded.
- [ ] No-change replay is idempotent.
- [ ] Boundary, hierarchy, attribute, rights, and metadata changes are classified separately.
- [ ] Materiality and correction handling are deterministic and reviewable.

### 4. Contract, schema, fixture, and test closure

- [ ] Accepted semantic contract exists for every emitted object family.
- [ ] Accepted machine schema exists at the canonical schema home.
- [ ] Valid, invalid, denied, abstain, and error fixtures exist where applicable.
- [ ] Default CI and rehearsal are deterministic and no-network.
- [ ] Executable tests prove framework/version/hierarchy/source-role boundaries and negative truth-upgrade cases.
- [ ] Geometry, CRS, topology, public-safe attributes, and crosswalk behavior are validated where material.

### 5. Executable and lifecycle closure

- [ ] Exact reviewed connector or retrieval entry point exists.
- [ ] Exact reviewed pipeline/spec entry point exists.
- [ ] Failure routes to `WORK`, `QUARANTINE`, `ABSTAIN`, `DENY`, or `ERROR` without public side effects.
- [ ] Receipts identify inputs, transforms, outputs, versions, hashes, and finite outcomes.
- [ ] Catalog/triplet projections are downstream and reproducible.
- [ ] Watchers or refresh automation cannot promote or publish directly.

### 6. Public-use closure

- [ ] Consequential claims resolve to admissible evidence.
- [ ] Cross-lane joins preserve owning-domain authority and sensitivity.
- [ ] Public geometry and attributes are generalized, minimized, or denied before delivery where required.
- [ ] Policy and required human review are complete.
- [ ] Immutable release candidate, release decision, correction path, cache invalidation plan, and rollback target resolve.
- [ ] Public clients use governed APIs or released public-safe artifacts only.

> [!IMPORTANT]
> The current repository evidence inspected for this README does **not** close this gate. The correct current outcome for live refresh is `HOLD`, not an inferred command sequence.

[Back to top](#top)

---

## Inputs, outputs, and responsibility handoffs

| Procedure phase | Required input | Permitted output | Owning destination | Stop condition |
|---|---|---|---|---|
| Scope | Authorized task contract and pinned revision | Bounded work plan | Issue/PR or approved work record | Ownership, overlap, or authority unresolved |
| Source admission | SourceDescriptor, rights, role, access, sensitivity, activation state | Admission/activation decision reference | Source-governance authority | Missing or conflicting source support |
| Retrieve | Approved source head and connector | Immutable RAW capture/reference and intake receipt | Governed RAW and receipt lanes | Network, rights, identity, or integrity failure |
| Normalize | RAW identity plus accepted contract/schema | WORK candidate or quarantine record | WORK / QUARANTINE | Shape, hierarchy, geometry, CRS, role, or evidence failure |
| Validate | Candidate plus deterministic fixtures and validators | Validation report and finite outcome | Tests/validation/accountability lanes | Required negative case absent or validator error |
| Process | Validated candidate and provenance | PROCESSED record | Governed PROCESSED lane | Source/version/evidence lineage incomplete |
| Project | Processed records | Catalog/triplet candidate | Catalog/triplet lanes | Projection would become independent truth |
| Review | Immutable candidate, evidence, policy, rights, sensitivity, proof, correction, rollback | Review and release decision | Review/release authorities | Required reviewer or gate unresolved |
| Deliver | Released public-safe carrier | Governed API/map/evidence response | Released delivery surface | Direct internal-store access or citation failure |
| Correct | Correction trigger and affected release identity | Correction, withdrawal, supersession, rollback, or recompile record | Release/accountability authorities | Prior state or rollback target cannot be reconstructed |

Markdown may explain these handoffs. It must not write the trust-bearing objects on their owners' behalf.

[Back to top](#top)

---

## Finite outcomes and stop conditions

| Condition | Procedure outcome | Required action |
|---|---|---|
| All scoped prerequisites pass and the named rehearsal is authorized | `PASS` for that bounded step | Record exact evidence; do not infer promotion or publication |
| Required authority, owner, source role, rights, schema, fixture, test, validator, evidence, review, release, or rollback is unresolved | `HOLD` | Stop mutation and open/continue verification work |
| Claim support cannot resolve but exposure is not independently prohibited | `ABSTAIN` | Return no consequential claim; record missing support |
| Rights, sensitivity, source-role substitution, harmful precision, or unauthorized truth upgrade prohibits use | `DENY` | Quarantine or reject the operation; preserve reason |
| Retrieval, parse, schema, topology, transform, evidence resolution, policy evaluation, or release verification fails unexpectedly | `ERROR` | Stop safely, preserve diagnostics, and avoid public side effects |
| Candidate is malformed, ambiguous, conflicted, or under-supported but may be reviewable | `QUARANTINE` | Preserve immutable input, reason, reviewer route, and exit criteria |
| A prior released carrier is wrong or unsafe | `CORRECT`, `WITHDRAW`, or `ROLLBACK` only through owning authority | Preserve lineage, affected releases, cache action, and restoration target |
| Scope or risk exceeds the approved task contract | `ESCALATE` | Narrow the task or obtain explicit authority; do not improvise |

A `PASS` is local to the named gate. It does not mean source admission, evidence truth, policy approval, release, deployment, promotion, or publication.

[Back to top](#top)

---

## Sensitivity and cross-lane joins

### Intrinsic versus joined sensitivity

| Material | Default posture |
|---|---|
| Public ecoregion framework boundaries alone | Usually low intrinsic sensitivity, subject to source rights and release state |
| Framework crosswalks | Review method, loss, version compatibility, and potential inference effects |
| Fauna or Flora occurrences | Owning domain controls; exact or inferable protected locations fail closed |
| Critical habitat or other regulatory designations | Regulatory source role remains distinct; do not infer from ecoregion context |
| Archaeological, cultural, or sovereignty-sensitive locations | Steward/community authority and public-safe transformation required |
| Private land, living-person, infrastructure, or other restricted joins | Minimize, generalize, stage access, quarantine, or deny as policy requires |
| Aggregated summaries | Require aggregation/model receipt, source/evidence lineage, uncertainty, and release review |

### Required join rules

- Preserve each lane's identity, source role, time, evidence, policy, review, and release state.
- Perform redaction/generalization before a public carrier is built; client-side hiding is not a safety control.
- Record the transform and its reason without exposing protected transform secrets or exact sensitive inputs.
- Prevent reverse inference where region-level summaries could reveal a small or unique protected population.
- Deny a join that would let regionalization context masquerade as occurrence, condition, regulatory, ownership, or title truth.
- Keep public output downstream of a governed API or immutable released public-safe artifact.

[Back to top](#top)

---

## Validation and rehearsal boundary

### Documentation validation for this README

The update is complete only when:

- the KFM metadata block is present and truthfully bounded;
- the file has exactly one H1 and a logical heading hierarchy;
- direct-child inventory matches the pinned directory;
- every repository-relative link resolves at the pinned branch;
- tables and fenced blocks are structurally balanced;
- no command is presented as operationally verified;
- no placeholder owner or policy value is invented;
- no exact sensitive location, credential, private endpoint, or restricted payload is introduced;
- no release, deployment, promotion, rollback execution, or publication effect is implied;
- the final file has a newline and the diff remains limited to the README plus its required generated-work receipt.

### Operational validation not established here

The following remain separate work:

- live source endpoint and terms verification;
- canonical source-registry topology;
- accepted source-role mapping;
- concrete ecoregion semantic contracts and schemas;
- synthetic fixture payloads;
- executable positive and negative tests;
- source-specific connector and pipeline implementation;
- geometry/topology/CRS validators;
- evidence and catalog closure;
- policy and sensitivity enforcement;
- release-candidate, correction, withdrawal, and rollback rehearsal;
- hosted or deployed behavior.

A documentation-only pass cannot satisfy these operational gates.

[Back to top](#top)

---

## Maintenance and review triggers

Update this README when any of the following changes materially:

- a direct child procedure is added, moved, renamed, superseded, or retired;
- `SOURCE_REFRESH.md` is reconciled against current repository evidence;
- the source-registry topology conflict is resolved;
- a source descriptor is admitted, suspended, corrected, or superseded;
- source role, rights, cadence, access, sensitivity, or citation posture changes;
- an executable connector, pipeline, spec, validator, fixture, or test becomes available;
- the accepted ecoregion contract or schema family changes;
- a no-network rehearsal, promotion, correction, or rollback procedure is added;
- public-safe precision or attribute policy changes;
- a released ecoregion carrier, correction, withdrawal, or rollback changes the operator path;
- CODEOWNERS or accountable steward assignments change;
- a repository inventory shows that a current-state statement here is stale.

For every update, re-pin the repository snapshot, recheck open work, preserve historical claims at their original revision, and keep documentation state separate from operational state.

[Back to top](#top)

---

## Open verification backlog

| Priority | Item | Current state | Closure evidence |
|---|---|---|---|
| P0 | Replace or retire the `SOURCE_REFRESH.md` scaffold through a repository-grounded procedure update | `HOLD` | Exact source, commands, owners, gates, negative cases, receipts, and rollback verified |
| P0 | Resolve source-registry topology for `data/registry/sources/habitat/` versus `data/registry/habitat/sources/` | `CONFLICTED / NEEDS VERIFICATION` | Accepted authority/migration decision and one canonical writable descriptor |
| P0 | Replace the Omernik greenfield template with an admitted source record or explicitly deny/retire it | `HOLD` | Role, authority, rights, access, cadence, version, citation, sensitivity, and activation decision |
| P0 | Identify accountable Habitat/ecoregions, source, evidence, policy, validation, release, rollback, and independent reviewers | `NEEDS VERIFICATION` | Current ownership/reviewer record and enforced review route where required |
| P1 | Establish concrete semantic contract and machine schema closure | `PROPOSED` | Reviewed contracts, canonical schemas, versions, fixtures, validators, and compatibility tests |
| P1 | Add public-safe synthetic ecoregion fixtures and executable no-network tests | `ABSENT in inspected lanes` | Deterministic valid/invalid/deny/abstain/error fixtures and passing exact-revision tests |
| P1 | Verify connector and pipeline implementation | `UNKNOWN` | Reviewed entry points, locked dependencies, receipts, negative paths, and bounded CI evidence |
| P1 | Define framework/hierarchy/boundary change and crosswalk materiality rules | `PROPOSED` | Deterministic validator/tests and reviewer-approved thresholds |
| P1 | Close evidence, catalog, policy, release, correction, and rollback path for one public-safe fixture | `HOLD` | Complete inspectable no-network thin slice |
| P2 | Add local no-network, promotion, correction, and rollback procedure docs after implementation proof exists | `PROPOSED` | Small dependency-closed documentation PRs tied to actual behavior |
| P2 | Populate the blank Habitat parent runbook README through a separate inventory-grounded change | `NEEDS VERIFICATION` | Parent-lane inventory and dependency reconciliation |

[Back to top](#top)

---

## Related surfaces

### Operational and governance

- [Root runbook index](../../README.md)
- [Habitat runbook parent](../README.md)
- [Ecoregion source-refresh scaffold](./SOURCE_REFRESH.md)
- [Directory Rules](../../../doctrine/directory-rules.md)
- [ADR-0029 — Directory Governance Standard v2](../../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

### Domain, source, and meaning

- [Habitat ecoregions sublane](../../../domains/habitat/sublanes/ecoregions.md)
- [Ecoregions source-registry guidance](../../../../data/registry/sources/habitat/ecoregions/README.md)
- [Omernik source-descriptor template](../../../../data/registry/habitat/sources/ecoregions_omernik.yaml)
- [Ecoregion semantic-contract lane](../../../../contracts/domains/habitat/ecoregions/README.md)
- [Ecoregion schema lane](../../../../schemas/contracts/v1/domains/habitat/ecoregions/README.md)

### Implementation, proof, and release handoff

- [Ecoregion pipeline lane](../../../../pipelines/domains/habitat/ecoregions/README.md)
- [Ecoregion pipeline-spec lane](../../../../pipeline_specs/habitat/ecoregions/README.md)
- [Ecoregion fixture lane](../../../../fixtures/domains/habitat/ecoregions/README.md)
- [Ecoregion test lane](../../../../tests/domains/habitat/ecoregions/README.md)
- [Habitat policy lane](../../../../policy/domains/habitat/README.md)
- [Ecoregion release-candidate lane](../../../../release/candidates/habitat/ecoregions/README.md)

[Back to top](#top)

---

## Evidence basis

| Evidence | Use in this README | Limit |
|---|---|---|
| Current repository `main@434195e8727e6e8649fd6a9e7de06808c3e15261` | Target bytes, direct-child inventory, registry/template state, contract/schema/pipeline/test/fixture posture, placement, and link targets | Does not prove deployment, source activation, operational admission, release, or publication |
| Accepted Directory Rules and ADR-0029 | Same-path documentation placement and responsibility separation | Does not decide source truth, rights, policy, implementation, or release |
| [`docs/runbooks/README.md`](../../README.md) | Inherited runbook authority and non-authority posture | Its inventory snapshot predates this leaf completion |
| [`docs/domains/habitat/sublanes/ecoregions.md`](../../../domains/habitat/sublanes/ecoregions.md) | Ecoregion context/anti-collapse doctrine and planned responsibilities | Draft and partly proposal-era; not current implementation proof |
| Google Drive `kfm_habitat_architecture_pdf_only_blueprint_2026-04-21.pdf` | Planning lineage for lifecycle, source-role separation, cite-or-abstain, public-safe joins, and no-network thin-slice posture | The document explicitly reported no mounted repository; it cannot prove current paths or behavior |
| Attached KFM repository build prompt v6 | Task execution, smallest coherent change, draft-PR, validation, review, and terminal-boundary requirements | Implementation method only; not KFM source, evidence, policy, or release authority |

### Truth-label summary

- **CONFIRMED:** current target and direct-child bytes, same-path placement, source-template unresolved fields, source-registry conflict disclosure, documentation-only contract/schema/pipeline posture, and empty executable fixture/test inventory in the inspected ecoregion lanes.
- **PROPOSED:** future procedure files, concrete source-refresh mechanics, object-family closure, tests, validators, release gates, and operational sequencing not backed by current implementation.
- **UNKNOWN:** live source status, deployed runtime, operational admission, actual public carrier instances, hosting, release execution, and rollback rehearsal.
- **NEEDS VERIFICATION:** accountable owners, source rights/role/cadence/access, canonical registry topology, accepted contracts/schemas, executable connectors/pipelines/tests, policy enforcement, evidence closure, release state, correction, and rollback.
- **HOLD:** any live ecoregion refresh, promotion, release, public exposure, or sensitive cross-lane join until the applicable gates close.

[Back to top](#top)

---

## Document change rollback

This README update is documentation-only.

- Before merge: close the draft pull request and delete or abandon its feature branch.
- After merge: revert the documentation commit through a normal reviewed pull request; do not rewrite shared history.
- Restore target lineage from prior blob `8b137891791fe96927ad78e64b0aad7bded08bdc` only when an explicit review decides that returning to a blank boundary is preferable.
- No source, RAW/WORK/QUARANTINE/PROCESSED data, catalog/triplet record, evidence object, policy decision, release, deployment, public carrier, or cache requires rollback because none is changed here.
- Reverting this file does not authorize or execute an operational rollback.

**Last reviewed:** 2026-08-25 against `main@434195e8727e6e8649fd6a9e7de06808c3e15261`.  
**Next review:** when a direct child procedure changes or any P0 verification item closes.

[Back to top](#top)
