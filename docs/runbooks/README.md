<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-runbooks-readme
title: docs/runbooks/ — Operational Procedure and Recovery Index
type: readme
subtype: nested-directory-landing-page
version: v1.8
prior_version: v1.7
status: draft; repository-grounded; documentation-only; non-authoritative
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable runbook, domain, security, release, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-28
policy_label: repository-facing; mixed child sensitivity
current_path: docs/runbooks/README.md
owning_root: docs/
responsibility: "Orient readers to KFM operational procedures, disclose current runbook maturity and drift, preserve fail-closed boundaries, and route executable or authority-bearing concerns to their owning responsibility roots."
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational-documentation index
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, evidence, review, lifecycle, release, correction, and rollback authorities
canonical_relationship: same-path update; no sibling authority created
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2de55d48ab35a41875eb9f094dc55dda18618ecc
  target_prior_blob: 26f9e77d329d58fb140fd4cfe814b4590e62952c
  runbooks_tree: 4c25b5e2f1254ff276e1ba5b7a10974fb33b8e85
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  adr_index_blob: dad651854ba7d37a3b29008dc8a90c0589caa030
  docs_root_readme_blob: 1f8bac189dac1d01c1185e8b4fb8e25efd11d09f
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  inventory:
    direct_entries: 42
    direct_markdown_files_including_this_readme: 29
    direct_domain_directories: 13
    recursive_markdown_files: 117
    files_with_exact_proposed_scaffold_marker: 25
    recurring_domain_packet_directories: 13
    recurring_domain_packet_files: 52
    direct_domain_directory_readme_paths: 12
    substantive_domain_boundary_readmes: 12
    one_byte_domain_readme_placeholders: 0
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/INDEX.md
  - docs/security/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - .github/CODEOWNERS
  - .github/workflows/README.md
  - control_plane/README.md
  - contracts/README.md
  - schemas/README.md
  - policy/README.md
  - tests/README.md
  - fixtures/README.md
  - tools/validators/README.md
  - data/README.md
  - release/README.md
notes:
  - "v1.8 adds the missing Roads/Rail/Trade boundary and reconciles the parent inventory against the exact current tree before and after that addition."
  - "The base subtree contains 116 Markdown files: 25 contain the exact phrase PROPOSED scaffold and 91 do not. This two-file change produces 117, 25, and 92 respectively."
  - "All 13 domain directories retain the recurring four-file packet; 12 now have substantive local README boundaries, and one still has no local README path."
  - "The Roads/Rail/Trade boundary routes maintainers to one bounded executable CorridorRoute profile while classifying all four child runbooks as proposal-era or stale guidance."
  - "Naming aliases, flat-versus-domain placement, scaffold disposition, and stale no-mounted-repo language remain separate dependency-aware cleanup work."
  - "This two-file update changes no executable procedure, contract, schema, policy, fixture, validator, workflow, evidence object, lifecycle object, release decision, deployment, promotion, publication, or repository setting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/runbooks/` — Operational Procedure and Recovery Index

> **Human-facing index for KFM procedures used to inspect, rehearse, contain, correct, recover, and safely hand off governed work.** Runbooks explain how an authorized actor should proceed; they do not grant authority, make evidence true, approve policy, change lifecycle state, or release anything by themselves.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-evidence-boundary)
[![Tracked Markdown: 117](https://img.shields.io/badge/tracked%20Markdown-117-0969da?style=flat-square)](#status-and-evidence-boundary)
[![Direct domain lanes: 13](https://img.shields.io/badge/direct%20domain%20lanes-13-1f6feb?style=flat-square)](#domain-lane-inventory)
[![Scaffold phrase files: 25](https://img.shields.io/badge/scaffold%20phrase%20files-25-d4a72c?style=flat-square)](#scaffolds-aliases-and-drift)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)
[![Evidence refreshed: 2026-08-28](https://img.shields.io/badge/evidence%20refreshed-2026--08--28-0969da?style=flat-square)](#last-reviewed-and-rollback)

> [!IMPORTANT]
> **A runbook is an instruction surface, not an authority surface.** It may cite an accepted decision, policy result, EvidenceBundle, ReviewRecord, ReleaseManifest, CorrectionNotice, RollbackCard, validator result, or workflow conclusion. It cannot create or replace any of them.

> [!CAUTION]
> A tracked path, long document, copy-paste command, green workflow, successful rehearsal, merged pull request, or operator action is not publication authority. Promotion remains a governed state transition through the owning evidence, policy, review, lifecycle, release, correction, and rollback surfaces.

> [!WARNING]
> KFM is not an emergency-alert or life-safety authority. Hazard, atmosphere, hydrology, and incident procedures must preserve official-source redirection and must not convert KFM guidance into actionable public warning instructions.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [Status](#status-and-evidence-boundary) · [Direct children](#direct-child-map) · [Start here](#start-here) · [Root index](#root-level-runbook-index) · [Domain lanes](#domain-lane-inventory) · [Belongs](#what-belongs-here) · [Prohibited](#what-does-not-belong-here) · [Inputs and outputs](#inputs-outputs-and-permitted-writers) · [Exposure](#exposure-and-sensitivity) · [Authoring](#runbook-authoring-contract) · [Outcomes](#procedure-states-and-finite-outcomes) · [Validation](#validation-and-rehearsal-evidence) · [Review](#ownership-review-and-escalation) · [Drift](#scaffolds-aliases-and-drift) · [Related](#related-responsibility-roots) · [ADRs](#adrs) · [Change discipline](#change-discipline-and-correction) · [Open work](#open-verification-backlog) · [Evidence](#evidence-basis) · [Last reviewed](#last-reviewed-and-rollback)

---

## Purpose

`docs/runbooks/` is the operational-procedure lane under KFM's human-readable `docs/` responsibility root. It helps maintainers, reviewers, stewards, developers, and operators answer bounded questions such as:

- Which procedure applies to this source, validation, promotion, correction, rollback, incident, or review state?
- What authority, evidence, permissions, fixtures, revision, and safe environment are required before beginning?
- What must be recorded before, during, and after the procedure?
- Which conditions produce `PASS`, `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, `ROLLBACK`, or `ESCALATE`?
- Which executable tool, workflow, policy, contract, schema, lifecycle family, or release object actually owns the action?
- How is the action stopped, corrected, reversed, or handed off without weakening KFM's trust membrane?

The lane is documentation-first. Executable implementation stays in its owning root. Runbooks should make the correct governed path usable without embedding a second implementation, policy engine, evidence store, or release authority in Markdown.

[Back to top](#top)

---

## Authority and negative authority

Accepted [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Those rules identify `docs/runbooks/` as the operational-procedure child of `docs/` and require risk-based README boundaries where ownership, exposure, mutation, generation, or lifecycle behavior changes.

| Concern | Owning authority | Runbook role |
|---|---|---|
| Placement and documentation boundary | Accepted Directory Rules and `docs/` root contract | Explain procedure placement and surface drift |
| Object meaning | `contracts/` | Cite semantics; do not redefine them |
| Machine shape | `schemas/` | Cite required fields and versions; do not host schema authority |
| Allow, deny, restrict, hold, or abstain | `policy/` plus governed review | Explain how to obtain and respond to a decision |
| Source admission and identity | SourceDescriptor and source-registry authorities | Describe approved handling; do not activate a source |
| Evidence and citations | EvidenceRef, EvidenceBundle, receipt, and proof authorities | Resolve and record support; do not manufacture evidence |
| Executable behavior | `tools/`, `packages/`, `pipelines/`, `connectors/`, `apps/`, `runtime/`, workflows, and scripts according to role | Point to exact reviewed entry points and expected outcomes |
| Lifecycle instances | Governed `data/` phases and accountability families | Describe a transition; do not write state by documentation alone |
| Release, correction, withdrawal, rollback | `release/` and linked accountability objects | Describe the authorized procedure; do not approve it |
| This README | Human navigation and current-state disclosure | No operational, policy, release, or publication authority |

A procedure must stop when its named authority, input, permission, review, evidence, or rollback target is unresolved. A README cannot turn `UNKNOWN` into approval.

[Back to top](#top)

---

## Status and evidence boundary

The observations below are pinned to `main@2de55d48ab35a41875eb9f094dc55dda18618ecc` and include the focused Roads/Rail/Trade README added by this change. They describe tracked repository bytes, not deployed behavior or operational approval.

| Surface | CONFIRMED observation | Bounded conclusion |
|---|---|---|
| This README | Prior v1.7 blob `26f9e77d...`, current before this change | Same-path v1.8 reconciliation; no sibling authority |
| Direct subtree | 42 direct entries: this README, 28 other Markdown files, and 13 domain directories | Current direct-child map is known at the pinned revision |
| Recursive Markdown inventory | 116 Markdown files on the pinned base; 117 after adding the Roads/Rail/Trade boundary | The lane is materially implemented as documentation, but document count is not procedure maturity |
| Exact scaffold phrase | 25 files contain the exact phrase `PROPOSED scaffold` before and after this change | This is a lexical drift signal, not proof that every matching file is presently a scaffold |
| Remaining Markdown | 91 files on the pinned base and 92 after this change do not contain that exact phrase | Absence of the phrase is not validation, rehearsal, review, admission, or release proof |
| Domain packet pattern | Every one of the 13 domain directories contains `NO_NETWORK_TEST_RUNBOOK.md`, `PROMOTION_RUNBOOK.md`, `ROLLBACK_RUNBOOK.md`, and `SOURCE_REFRESH_RUNBOOK.md` | A repeated documentation pattern exists; parity and current correctness remain separate checks |
| Domain-lane boundary READMEs | 11 of 13 direct domain directories contain a substantive `README.md` on the pinned base; 12 after this change | The Roads/Rail/Trade gap is closed; Settlements/Infrastructure remains unclosed |
| Sampled long-form runbooks | Promotion, rollback, correction, release dry-run, and incident response are substantive drafts | Useful content exists, but several retain May 2026 proposal or no-mounted-repo language |
| Naming and alias consistency | Flat, domain-nested, upper-snake, lower-snake, kebab, and mixed legacy forms coexist | Identity and migration work is required before renaming or deleting anything |
| CODEOWNERS | Default repository route is `@bartytime4life`; no separate `docs/runbooks/` rule is present | GitHub review routing exists; accountable stewardship and independent approval remain unverified |
| Dedicated aggregate runbook validator | No `validate_runbook` implementation was found in bounded search | Structural and semantic runbook conformance is not established by a dedicated gate |
| Hosted workflows | Some workflows reference individual runbooks; generic documentation workflows also exist | Workflow presence proves orchestration only, not procedure correctness or operational admission |
| Runtime, source, evidence, policy, release, deployment, publication | Not established by this README or inventory | Remains `UNKNOWN` unless proven by owning surfaces and exact-revision evidence |

### State separation

Do not collapse these states:

| Axis | Example |
|---|---|
| File presence | Tracked Markdown exists |
| Documentation state | Scaffold, draft, corrected, or current at a pinned revision |
| Procedure validation | Commands, paths, inputs, and negative states were checked |
| Rehearsal state | Procedure was run in an approved non-public environment with recorded outputs |
| Review state | Authorized human or policy-significant review is complete |
| Operational admission | Procedure is approved for a named environment, scope, and actor class |
| Lifecycle state | Governed data/object transition has occurred |
| Release state | Release authority approved a specific immutable release |
| Publication state | Public-safe carrier is actually exposed through governed delivery |

[Back to top](#top)

---

## Direct-child map

This map shows only the directory governed by this README and its direct children, as required by Directory Rules. Deeper detail belongs in child boundary documents.

```text
docs/runbooks/
├── README.md
├── AUTOMATION_DRAFT_PR_OPENER.md
├── DOCTRINE_ARTIFACT_PREFLIGHT.md
├── EVIDENCE_CORRECTION.md
├── FIRST_GOVERNED_PR_RUNBOOK.md
├── FIRST_INGEST.md
├── INCIDENT_RESPONSE.md
├── NO_NETWORK_TEST_RUNBOOK.md
├── PROMOTION_RUNBOOK.md
├── QUARANTINE_HANDLING.md
├── RELEASE_DRY_RUN.md
├── ROLLBACK_RUNBOOK.md
├── SENSITIVITY_ESCALATION.md
├── SOURCE_REFRESH_RUNBOOK.md
├── STABLE_DIFF_REVIEW_HANDOFF.md
├── VALIDATOR_ORCHESTRATOR.md
├── agriculture/
├── archaeology/
├── atmosphere/
├── automation-draft-pr-opener-validation-checklist.md
├── fauna/
├── flora/
├── flora_BACKBONE_ROTATION.md
├── flora_SOURCE_REFRESH.md
├── geology/
├── habitat/
├── hazards/
├── hydrology/
├── hydrology_VALIDATION.md
├── mrts-06-ci-conformance-handoff.md
├── people-dna-land/
├── pipeline-resilience.md
├── retention-agriculture.md
├── revocation.md
├── roads-rail-trade/
├── roads_rail_trade_source_refresh.md
├── rollback-rehearsal.md
├── settlements-infrastructure/
├── soil/
├── ui_LOCAL_DEV.md
├── ui_ROLLBACK.md
└── ui_VALIDATION.md
```

[Back to top](#top)

---

## Start here

| Need | Current entry point | Boundary |
|---|---|---|
| First governed repository contribution | [`FIRST_GOVERNED_PR_RUNBOOK.md`](./FIRST_GOVERNED_PR_RUNBOOK.md) | Procedure does not approve or merge its own change |
| First ingest rehearsal | [`FIRST_INGEST.md`](./FIRST_INGEST.md) | Source admission, rights, and lifecycle authority remain external |
| No-network validation posture | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | A fixture-only pass does not prove a live source or public release |
| Quarantine handling | [`QUARANTINE_HANDLING.md`](./QUARANTINE_HANDLING.md) | Exit requires an authorized, recorded resolution; quarantine is not a failure to hide |
| Source refresh | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Refresh is not source admission, promotion, or publication |
| Promotion preparation | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Promotion requires the owning gates and decision objects |
| Release rehearsal | [`RELEASE_DRY_RUN.md`](./RELEASE_DRY_RUN.md) | Dry-run must not write any public state |
| Evidence correction | [`EVIDENCE_CORRECTION.md`](./EVIDENCE_CORRECTION.md) | Corrections preserve supersession and affected derivative lineage |
| Release rollback | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Rollback uses a named prior safe state and emits governed records |
| Sensitivity escalation | [`SENSITIVITY_ESCALATION.md`](./SENSITIVITY_ESCALATION.md) | Unknown rights, sovereignty, consent, or harmful precision fails closed |
| Internal KFM incident response | [`INCIDENT_RESPONSE.md`](./INCIDENT_RESPONSE.md) | Not a public emergency-response or life-safety procedure |
| Doctrine artifact intake | [`DOCTRINE_ARTIFACT_PREFLIGHT.md`](./DOCTRINE_ARTIFACT_PREFLIGHT.md) | A document cannot adopt itself or authorize dependent structural work |
| Validator orchestration guidance | [`VALIDATOR_ORCHESTRATOR.md`](./VALIDATOR_ORCHESTRATOR.md) | Documentation does not replace the executable orchestrator or its tests |

[Back to top](#top)

---

## Root-level runbook index

### Repository automation and review handoff

| File | Current role | Evidence posture |
|---|---|---|
| [`AUTOMATION_DRAFT_PR_OPENER.md`](./AUTOMATION_DRAFT_PR_OPENER.md) | Bounded automation procedure | Tracked; exact current workflow behavior must be checked separately |
| [`FIRST_GOVERNED_PR_RUNBOOK.md`](./FIRST_GOVERNED_PR_RUNBOOK.md) | First governed contribution path | Tracked long-form guidance; no merge authority |
| [`STABLE_DIFF_REVIEW_HANDOFF.md`](./STABLE_DIFF_REVIEW_HANDOFF.md) | Stable-diff review handoff | Tracked procedure; review state remains external |
| [`VALIDATOR_ORCHESTRATOR.md`](./VALIDATOR_ORCHESTRATOR.md) | Validator orchestration guidance | Tracked guidance; executable path and exit semantics require current verification |
| [`automation-draft-pr-opener-validation-checklist.md`](./automation-draft-pr-opener-validation-checklist.md) | Narrow validation checklist | Tracked checklist; not equivalent to end-to-end automation proof |
| [`mrts-06-ci-conformance-handoff.md`](./mrts-06-ci-conformance-handoff.md) | MRTS-06 CI conformance and closure handoff | Proposed blocked handoff; it grants no review, issue-closure, release, or publication authority |

### Intake, source, lifecycle, and resilience

| File | Current role | Evidence posture |
|---|---|---|
| [`FIRST_INGEST.md`](./FIRST_INGEST.md) | Initial ingest procedure | Tracked long-form guidance; live source activation is out of scope |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Deterministic fixture-oriented procedure | Tracked long-form guidance; no-network pass is bounded evidence |
| [`QUARANTINE_HANDLING.md`](./QUARANTINE_HANDLING.md) | Quarantine entry, review, and exit guidance | Tracked long-form guidance; exit authority remains external |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Cross-cutting source refresh procedure | Tracked long-form guidance; source-specific terms and currentness require review |
| [`pipeline-resilience.md`](./pipeline-resilience.md) | Pipeline resilience and recovery guidance | Tracked guidance; runtime resilience is not established by prose |

### Promotion, release, correction, and recovery

| File | Current role | Evidence posture |
|---|---|---|
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Lifecycle promotion procedure | Substantive draft; current gate bindings require verification |
| [`RELEASE_DRY_RUN.md`](./RELEASE_DRY_RUN.md) | No-public-write release rehearsal | Substantive draft; dry-run output is not release approval |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Cross-cutting rollback procedure | Substantive draft; prior-safe target and actual drill evidence remain per release |
| [`rollback-rehearsal.md`](./rollback-rehearsal.md) | Synthetic rollback, withdrawal, and correction rehearsal | Marker-protected synthetic procedure; not an operational rollback or release mutation |
| [`EVIDENCE_CORRECTION.md`](./EVIDENCE_CORRECTION.md) | Published-evidence correction procedure | Substantive draft; several linked paths retain verification notes |

### Explorer Web development and recovery

| File | Current role | Evidence posture |
|---|---|---|
| [`ui_LOCAL_DEV.md`](./ui_LOCAL_DEV.md) | Locked local setup and focused app validation | Repository-grounded; no live API, deployment, release, or publication path is established |
| [`ui_ROLLBACK.md`](./ui_ROLLBACK.md) | Source-control recovery and rollback handoff | Repository-grounded; operational deployment and governed release rollback remain outside its authority |
| [`ui_VALIDATION.md`](./ui_VALIDATION.md) | Scope-based Explorer checks and workflow-result interpretation | Repository-grounded; axe, WCAG, live integration, deployment, release, and publication remain unproven or held |

### Security, sensitivity, and doctrine handling

| File | Current role | Evidence posture |
|---|---|---|
| [`INCIDENT_RESPONSE.md`](./INCIDENT_RESPONSE.md) | KFM trust-path incident procedure | Substantive restricted-labeled draft; environment and named responders need verification |
| [`SENSITIVITY_ESCALATION.md`](./SENSITIVITY_ESCALATION.md) | Sensitive-material escalation guidance | Substantive guidance; qualified review authority is not established by this README |
| [`DOCTRINE_ARTIFACT_PREFLIGHT.md`](./DOCTRINE_ARTIFACT_PREFLIGHT.md) | Doctrine intake and authority preflight | Substantive guidance; it cannot adopt a source or decision by itself |

### Direct scaffold and compatibility candidates

The following direct files are small scaffold or compatibility-shaped documents. They must not be represented as complete procedures merely because links resolve:

- [`flora_BACKBONE_ROTATION.md`](./flora_BACKBONE_ROTATION.md)
- [`flora_SOURCE_REFRESH.md`](./flora_SOURCE_REFRESH.md)
- [`hydrology_VALIDATION.md`](./hydrology_VALIDATION.md)
- [`retention-agriculture.md`](./retention-agriculture.md)
- [`revocation.md`](./revocation.md)
- [`roads_rail_trade_source_refresh.md`](./roads_rail_trade_source_refresh.md)

Their canonical target, consumers, replacement procedure, and retirement path remain `NEEDS VERIFICATION`. Do not hand-edit one alias and its apparent target as competing authorities.

[Back to top](#top)

---

## Domain-lane inventory

Every current direct domain directory contains this recurring four-file packet:

```text
<domain>/
├── NO_NETWORK_TEST_RUNBOOK.md
├── PROMOTION_RUNBOOK.md
├── ROLLBACK_RUNBOOK.md
└── SOURCE_REFRESH_RUNBOOK.md
```

That pattern is **CONFIRMED current repository structure**, not proof that the four procedures are identical, current, tested, appropriate, or accepted for every domain.

| Domain lane | Recurring packet | Additional tracked material | Current boundary finding |
|---|---:|---|---|
| [`agriculture/`](./agriculture/README.md) | 4 files | Substantive local `README.md` | Boundary contract is documented; no-network, rollback, and source-refresh are repository-grounded v0.2 drafts, while promotion remains the older v0.1 draft |
| [`archaeology/`](./archaeology/README.md) | 4 files | Substantive local `README.md` | Sensitive-domain boundary is documented and all four packet files are repository-grounded drafts; their declared proof, live-source, operational-rollback, and release holds remain |
| [`atmosphere/`](./atmosphere/README.md) | 4 files | Substantive local `README.md`; correction, release, release-rollback, stale-state, and validation documents | Boundary contract and nine substantive repository-grounded child procedures are documented; operational source, promotion, release, deployment, and rollback execution remain held |
| [`fauna/`](./fauna/README.md) | 4 files | Substantive local `README.md`; EBD derivative, publication dry-run, rollback drill, sensitive-occurrence, and taxonomy documents | Sensitive-domain boundary is documented; eight children are repository-grounded drafts, one rollback child remains proposal-era, and exact sensitive occurrences fail closed |
| [`flora/`](./flora/README.md) | 4 files | Substantive local `README.md`; flat sibling compatibility/scaffold paths remain | Boundary contract is documented; four direct children retain proposal-era assumptions and rare or culturally sensitive geometry fails closed |
| [`geology/`](./geology/README.md) | 4 files | Substantive local `README.md`; bedrock review procedure | Boundary contract is documented with mixed child maturity; private-well and sensitive subsurface detail still requires policy review |
| [`habitat/`](./habitat/README.md) | 4 files | Substantive local `README.md`; nested `ecoregions/` boundary and source-refresh procedure | Boundary contract and one bounded synthetic profile are documented; modeled habitat is not occurrence or regulatory designation and broader operations remain held |
| [`hazards/`](./hazards/README.md) | 4 files | Substantive local `README.md`; not-for-life-safety audit, no-network, promotion, source-refresh, rollback, and rollback-drill procedures | Boundary contract is documented; executable coverage remains bounded and KFM never becomes alert authority |
| [`hydrology/`](./hydrology/README.md) | 4 files | Substantive local `README.md`; bounded validation, promotion preflight, proposal-era no-network/source-refresh/rollback guides, and one explicit rollback scaffold | Boundary and child maturity are documented; current executable coverage is synthetic and fixture-bounded, broader operations remain held, and NFHL is regulatory context rather than observed inundation |
| [`people-dna-land/`](./people-dna-land/README.md) | 4 files | Substantive local `README.md`; one repository-grounded living-person review, four proposal-era packet procedures, and six explicit scaffolds | Sensitive boundary and two bounded synthetic consent profiles are documented; real-person material, active policy runtime, proof, release, deployment, and publication remain held |
| [`roads-rail-trade/`](./roads-rail-trade/README.md) | 4 files | Substantive local `README.md`; one executable no-network CorridorRoute profile and four proposal-era or stale packet procedures | Boundary routes the bounded synthetic profile, preserves infrastructure and cultural-corridor restrictions, and keeps broader source, policy, proof, promotion, rollback, release, deployment, and publication work held |
| `settlements-infrastructure/` | 4 files | — | No local README; critical-asset and dependency detail fails closed |
| [`soil/`](./soil/README.md) | 4 files | Substantive local `README.md` | Boundary routes four bounded synthetic fixture profiles and classifies all four packet procedures as proposal-heavy; live source, proof, policy activation, promotion, rollback, release, deployment, and publication remain held |

### Inheritance gap

Directory Rules assigns `BOUNDARY_COMPACT` treatment to domain and sensitive boundaries. Agriculture, Archaeology, Atmosphere, Fauna, Flora, Geology, Habitat, Hazards, Hydrology, People/DNA/Land, Roads/Rail/Trade, and Soil now have substantive local boundary READMEs. Settlements/Infrastructure has no local README path, so one lane still lacks a substantive local contract closing inherited authority, scope, exposure, permitted writers, validation, related policy, and open verification.

This README records the remaining gap. It does not create a boilerplate file, assign stewards, normalize sensitive rules, or imply that one generic packet is sufficient for every domain.

[Back to top](#top)

---

## What belongs here

A runbook belongs in this lane when its primary responsibility is human-readable operational guidance and it has a real, bounded procedure to describe. Suitable material includes:

- repository preflight, review handoff, and constrained automation procedures;
- source admission preparation, source refresh, ingest, quarantine, and recovery guidance;
- deterministic local or no-network validation procedures;
- promotion preparation and release dry-runs that do not self-authorize public writes;
- correction, withdrawal, rollback, stale-state, cache invalidation, and recovery procedures;
- internal security, evidence-integrity, sensitivity, and trust-membrane incident response;
- domain-specific procedures that inherit global controls and add only real local differences;
- drill plans and post-drill interpretation guidance;
- escalation paths, stop conditions, and finite outcome handling;
- compatibility or retirement notices when a reviewed migration requires a human procedure.

A proposed path alone is not enough. Create a new runbook only when the procedure, owning system, inputs, outputs, stop conditions, validation, review, correction, and rollback can be stated without inventing implementation.

[Back to top](#top)

---

## What does not belong here

| Material | Owning surface |
|---|---|
| Architecture or doctrine | `docs/architecture/` or `docs/doctrine/` |
| Decision records | `docs/adr/` |
| Human drift and verification registers | `docs/registers/` |
| Security doctrine or threat model not organized as an operational procedure | `docs/security/` |
| Machine governance projection | `control_plane/` |
| Semantic contract | `contracts/` |
| Machine-valid schema | `schemas/` |
| Policy rule source | `policy/` |
| Executable validator or generator | `tools/validators/` or another tool lane |
| Reusable code, deployable application, connector, pipeline, runtime adapter, infrastructure | Its owning execution root |
| Valid, invalid, negative, golden, or runtime fixture | `fixtures/` |
| Executable conformance test | `tests/` |
| Workflow trigger, permission, runner, or orchestration | `.github/workflows/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED instance | Governed `data/` lane |
| Receipt, proof, catalog, evidence, or source-registry instance | Its governed accountability family |
| Release decision, manifest, correction notice, withdrawal, or rollback card | `release/` and linked governed families |
| Generated QA output, logs, coverage, or render previews | `artifacts/qa/`, `artifacts/docs/`, or approved external CI storage |
| Secret, credential, private endpoint, signed URL, restricted payload, or protected precise location | Never in repository-facing runbook text |

A command snippet may appear here when it is part of a verified human procedure. The reusable implementation still belongs in the owning executable root; do not duplicate substantial logic in Markdown to avoid review or testing.

[Back to top](#top)

---

## Inputs, outputs, and permitted writers

### Inputs

A runbook may depend on:

- accepted doctrine and ADRs;
- current code, configuration, contracts, schemas, policy, tests, fixtures, workflows, and manifests tied to a named revision;
- source admission, rights, sensitivity, and authority records;
- EvidenceRefs, EvidenceBundles, receipts, proofs, catalogs, and validation results;
- candidate, lifecycle, release, correction, withdrawal, and rollback objects;
- an approved environment, actor class, permissions, credentials boundary, and network posture;
- prior drill, incident, or correction records when they remain applicable.

Missing or stale authority input is a stop condition, not permission to improvise.

### Outputs

A runbook can guide a human or constrained automation toward outputs owned elsewhere, such as:

- a validation result, review packet, or issue/PR handoff;
- a source-intake, quarantine, correction, or rollback candidate;
- a receipt, proof, catalog, promotion, or release candidate;
- a controlled stop, denial, abstention, escalation, or recovery record.

The runbook itself emits documentation only. An output acquires its real state through the owning producer, validator, policy, review, lifecycle, or release process.

### Permitted writers

Normal changes are reviewed feature-branch edits by maintainers or authorized automation. Writers must preserve stable identity, current paths, public-safe content, links, metadata, status, limitations, correction history, and rollback instructions.

CODEOWNERS currently routes repository review to `@bartytime4life`. That is not proof of domain expertise, operational authorization, independent review, incident command, policy approval, or release authority.

[Back to top](#top)

---

## Exposure and sensitivity

This README is repository-facing, but child procedures may carry stricter exposure requirements. A public index may identify that a restricted procedure exists without disclosing sensitive commands, infrastructure topology, protected coordinates, private identities, source credentials, exploit details, or denial reasons that increase harm.

For archaeology, sacred or cultural material, rare species, rare plants, living persons, DNA/genomics, private land/title-like records, wells, critical infrastructure, and other harmful precision:

- default to deny, quarantine, redaction, generalization, staged access, or abstention;
- name the qualified review needed without inventing the reviewer;
- keep sensitive inputs and outputs in their governed stores;
- do not place real protected examples in a public runbook;
- test with synthetic or explicitly public-safe fixtures;
- preserve transformation, review, correction, and rollback records.

Incident procedures must not publish operational security detail merely to appear complete. Link to a restricted authority or internal system only when that relationship is safe and verified.

[Back to top](#top)

---

## Runbook authoring contract

Directory Rules replaces a single uniform README template with risk-based profiles. Runbooks should likewise carry the smallest complete structure that fits their risk and procedure. Do not force empty headings merely to satisfy an old template.

A substantive runbook should normally make these concerns inspectable:

1. **Identity and status** — stable document ID, current path, version, status, evidence revision, owner route, and sensitivity label.
2. **Purpose, audience, and non-goals** — who uses it, when, and what it cannot authorize.
3. **Scope and authority preflight** — systems, domains, lifecycle states, actor class, accepted decisions, and stop conditions.
4. **Preconditions and inputs** — exact versions, permissions, environment, source/evidence/review state, fixtures, and rollback target.
5. **Procedure** — numbered, deterministic steps with destructive or public-impacting actions visibly gated.
6. **Finite outcomes** — allowed completion, hold, abstain, deny, error, escalation, correction, and rollback states with reason codes where available.
7. **Outputs and ownership** — what is produced, where its authority lives, and who may write it.
8. **Validation and negative checks** — expected positive evidence and fail-closed cases.
9. **Correction, withdrawal, and rollback** — prior-safe target, affected derivatives, cache/client behavior, and audit trail.
10. **Review and escalation** — required roles, separation of duties where material, and unresolved questions.
11. **Related authorities** — contracts, schemas, policy, fixtures, tests, workflows, evidence, release records, and adjacent procedures.
12. **Review triggers** — authority, path, environment, source, dependency, sensitivity, incident, correction, or release changes that invalidate the procedure.

### Command discipline

Commands must identify their expected working directory, prerequisites, environment, network behavior, write surface, outputs, exit semantics, and safe failure behavior. Never include real secrets. Use placeholders that cannot be mistaken for valid credentials.

A command copied from a planning document remains `PROPOSED` until checked against current repository evidence. A command that mutates public or trust-bearing state must not be presented as ordinary copy-paste setup.

### Generated and mirrored procedures

A generated or mirrored runbook must identify its canonical source, generator, version, digest, edit policy, parity check, owner, and retirement rule. Manual edits to a verified mirror are denied.

[Back to top](#top)

---

## Procedure states and finite outcomes

The vocabulary below separates document maturity from execution outcome. It is an indexing aid, not an independent approval system.

### Documentation maturity

| State | Meaning |
|---|---|
| `SCAFFOLD` | Path and intent only; not executable |
| `DRAFT` | Substantive procedure exists; current implementation or review may remain incomplete |
| `REPOSITORY_VERIFIED` | Paths, commands, inputs, and expected outputs were checked against a named revision |
| `REHEARSED` | The procedure was executed in an approved non-public or synthetic setting and produced reviewable results |
| `OPERATIONALLY_ADMITTED` | Authorized reviewers admitted the procedure for a named environment, scope, and actor class |
| `STALE` | A trigger changed and the procedure must not be relied upon until reverified |
| `DEPRECATED` | Read-only compatibility or retirement state with a named target |

No state should be inferred from filename, length, badge, commit, or merge alone.

### Execution outcomes

| Outcome | Meaning | Required posture |
|---|---|---|
| `PASS` | Declared acceptance criteria were met for the tested scope | Record revision, evidence, and limitations |
| `HOLD` | Authority, input, review, identity, or target is unresolved | Stop without weakening the gate |
| `ABSTAIN` | Evidence is insufficient for a claim or interpretation | Preserve missing/conflicted support |
| `DENY` | Policy, sensitivity, rights, or invariant blocks the action | Do not perform or expose it |
| `ERROR` | Tooling or environment failed | Correct or escalate; never convert to allow |
| `ROLLBACK` | Revert to a named prior safe state | Record affected outputs and lineage |
| `ESCALATE` | Qualified authority or additional review is required | Preserve state and avoid broadening access |
| `NO_ACTION` | The safe result is no change | Record why when material |

[Back to top](#top)

---

## Validation and rehearsal evidence

### Documentation validation

For a change to this lane, use the smallest repository-native set that covers the actual delta. Applicable checks may include:

- one valid `KFM_META_BLOCK_V2`, one H1, balanced fences, valid tables, and a final newline;
- repository-relative path, case, link, and fragment checks;
- document-graph and stale-document checks;
- generated-receipt integrity when a receipt is part of the change;
- Directory Rules topology checks for additions, moves, aliases, or new boundaries;
- sensitive-content and secret scanning;
- changed-area validation tied to the exact branch head.

Current generic documentation workflows do not establish a dedicated semantic runbook-conformance gate.

### Procedure validation

A procedure is not validated merely because its Markdown passes. Depending on risk, evidence can include:

- current file and command resolution at a pinned revision;
- deterministic positive, negative, malformed, stale, denied, and rollback fixtures;
- no-network or simulation-first execution;
- exact output hashes, receipts, logs, reports, and finite outcome checks;
- policy and sensitivity denial cases;
- proof that public/canonical stores are not reachable from unauthorized paths;
- correction and rollback rehearsal with derivative invalidation;
- hosted exact-head results and required-check coupling when relevant;
- authorized human review for policy-significant or public-impacting procedures.

### Evidence record

A rehearsal or operational-use record should state:

- runbook ID, version, content digest, and repository revision;
- environment and actor class without leaking credentials;
- inputs, outputs, start/end times, and tool versions;
- decision, reason codes, policy and review state;
- introduced and inherited findings;
- affected carriers and rollback target;
- reviewer disposition and unresolved residue.

[Back to top](#top)

---

## Ownership, review, and escalation

| Change or use | Minimum review posture |
|---|---|
| Editorial correction or verified link repair | Scoped documentation review |
| Command, path, dependency, or environment change | Owning implementation maintainer plus documentation review |
| Source admission, rights, or source-role procedure | Source/evidence review and policy review as applicable |
| Sensitive-domain procedure | Appropriate domain, rights, sensitivity, sovereignty, consent, or security review |
| Promotion, release, correction, withdrawal, rollback | Owning release/correction authority and separation of duties where required |
| Incident response or security containment | Security/incident authority, affected system owner, correction/release review as applicable |
| New domain runbook lane or alias migration | Directory Rules preflight, consumer inventory, compatibility, validation, and rollback |
| Operational admission | Named environment, actor class, accepted inputs, validation evidence, authorized review, and expiration/review triggers |

Do not encode role names as GitHub identities unless the account or team and its approved responsibility are verified. Do not treat an author as the independent approver of the same policy-significant release action.

[Back to top](#top)

---

## Scaffolds, aliases, and drift

### Exact scaffold-phrase inventory

Twenty-five files in the current subtree contain the exact phrase `PROPOSED scaffold`. That count is a lexical drift inventory, not a maturity classification: this parent index and some modernized runbooks use the phrase while describing prior bytes or historical state. Each matching file must be inspected at its pinned revision. A file that actually declares scaffold or proposed status remains `HOLD` until content, authority, owners, validation, sensitivity, and target identity are reviewed; a historical mention does not erase a newer declared draft posture or prove operational admission.

### Current identity conflicts and duplication pressure

Examples visible at the pinned revision include:

| Current surfaces | Risk |
|---|---|
| `hydrology_VALIDATION.md` and `hydrology/VALIDATION.md` | Flat and domain-nested identities may compete |
| `revocation.md` and `people-dna-land/revocation.md` | Global versus domain scope is unresolved |
| `roads_rail_trade_source_refresh.md` and `roads-rail-trade/SOURCE_REFRESH_RUNBOOK.md` | Alias, casing, and canonical-target ambiguity |
| `flora_SOURCE_REFRESH.md` and `flora/SOURCE_REFRESH_RUNBOOK.md` | Scaffold versus substantive domain procedure |
| `ui_ROLLBACK.md` and cross-cutting/domain rollback procedures | Subsystem-specific scope and inheritance are unresolved |
| Global four-file packet and 13 domain copies | Shared-kernel versus domain-delta duplication requires evidence, not mass deletion |

### Safe cleanup sequence

1. Freeze the exact tree and target revisions.
2. Classify each document's authority, scope, exposure, consumers, and maturity.
3. Identify unique content and current writers.
4. Select a canonical target only through applicable authority.
5. Add compatibility or migration records where consumers require them.
6. Move producers to single-write.
7. Repair links, indexes, tests, workflows, and generated outputs.
8. Prove parity, zero writers, and zero consumers before retirement.
9. Preserve correction and rollback history.

This README does not authorize a mass rename, deduplication, generated mirror, deletion, or replacement of domain procedures.

[Back to top](#top)

---

## Related responsibility roots

| Surface | Relationship to runbooks |
|---|---|
| [`../README.md`](../README.md) | Parent human-documentation authority boundary |
| [`../doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Adopted placement, README, compatibility, migration, and rollback law |
| [`../adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision for Directory Rules v2 |
| [`../security/README.md`](../security/README.md) | Security, threat, incident, and exposure guidance outside procedure-specific steps |
| [`../registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) | Human drift record |
| [`../registers/VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) | Human verification backlog |
| [`../../control_plane/README.md`](../../control_plane/README.md) | Machine-readable governance projections and registers |
| [`../../contracts/README.md`](../../contracts/README.md) | Semantic meaning of objects and interfaces |
| [`../../schemas/README.md`](../../schemas/README.md) | Machine-checkable shape |
| [`../../policy/README.md`](../../policy/README.md) | Admissibility, rights, sensitivity, and finite decisions |
| [`../../fixtures/README.md`](../../fixtures/README.md) | Representative valid, invalid, negative, and golden inputs |
| [`../../tests/README.md`](../../tests/README.md) | Executable conformance evidence |
| [`../../tools/validators/README.md`](../../tools/validators/README.md) | Reusable validation implementation |
| [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | GitHub Actions orchestration and hosted check boundaries |
| [`../../data/README.md`](../../data/README.md) | Lifecycle and accountability instances |
| [`../../release/README.md`](../../release/README.md) | Promotion, release, correction, withdrawal, and rollback decisions |

[Back to top](#top)

---

## ADRs

The current [`docs/adr/INDEX.md`](../adr/INDEX.md) records 36 numbered ADRs. ADR-0029 is accepted; the other 35 remain effectively proposed. This README cannot promote any decision.

| ADR | Runbook relevance | Effective status |
|---|---|---|
| [`ADR-0010`](../adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | Sensitive-domain fail-closed proposal | `proposed` |
| [`ADR-0012`](../adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) | Connector and ingest boundary proposal | `proposed` |
| [`ADR-0016`](../adr/ADR-0016-telemetry-redaction-posture.md) | Operational telemetry redaction proposal | `proposed` |
| [`ADR-0017`](../adr/ADR-0017-source-descriptor-admission-process.md) | Source admission proposal | `proposed` |
| [`ADR-0018`](../adr/ADR-0018-promotion-gate-sequence.md) | Promotion gate sequence proposal | `proposed` |
| [`ADR-0021`](../adr/ADR-0021-quarantine-has-structured-exit-paths.md) | Quarantine exit-path proposal | `proposed` |
| [`ADR-0024`](../adr/ADR-0024-steward-separation-of-duties-for-release.md) | Release separation-of-duties proposal | `proposed` |
| [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopts Directory Rules v2 | `accepted` |
| [`ADR-0031`](../adr/ADR-0031-shared-watcher-ownership-and-placement.md) | Shared watcher placement proposal | `proposed` |

A runbook may explain how to operate under an accepted decision. It must not present a proposed ADR as current authority.

[Back to top](#top)

---

## Change discipline and correction

### Editing a procedure

Before changing a runbook:

1. Pin current `main`, the target blob, current consumers, and overlapping pull requests.
2. Identify the procedure's authority, scope, exposure, current implementation, and review state.
3. Verify commands, paths, schemas, policies, fixtures, workflows, and output families against current repository evidence.
4. Preserve unique safety, failure, correction, rollback, and sensitive-domain guidance.
5. Keep proposed or unknown behavior explicitly labeled.
6. Validate the changed document and the smallest connected procedure surface.
7. Record introduced versus inherited findings and exact rollback.

### Correcting operationally harmful guidance

When a procedure is unsafe, stale, or wrong:

- stop relying on the affected step;
- identify affected executions, releases, evidence, public carriers, and downstream docs;
- contain exposure without creating a new authority path;
- correct or withdraw the guidance through reviewed change;
- issue the owning correction or rollback objects when operational state was affected;
- invalidate caches, generated copies, and references as required;
- preserve the prior version and reason for audit.

A documentation revert restores text only. It does not reverse an operational action already taken under that text.

[Back to top](#top)

---

## Open verification backlog

### P0 — safety and authority

1. **NEEDS VERIFICATION — accountable stewardship.** Establish real owners, reviewers, escalation roles, and separation-of-duties requirements for cross-cutting and sensitive procedures.
2. **NEEDS VERIFICATION — restricted-content audit.** Confirm no public runbook exposes secrets, protected locations, private identities, infrastructure detail, exploit paths, or harmful denial reasons.
3. **NEEDS VERIFICATION — operationally stale guidance.** Audit commands and paths in promotion, rollback, correction, release, incident, ingest, source-refresh, and sensitivity procedures against current implementation.
4. **NEEDS VERIFICATION — life-safety boundary.** Verify hazards, atmosphere, and hydrology procedures consistently redirect actionable warnings to official authorities.
5. **CONFLICTED — incident documentation boundary.** Reconcile procedure-specific incident content in `docs/runbooks/` with broader incident/security guidance in `docs/security/` without parallel authority.

### P1 — structure and conformance

6. **NEEDS VERIFICATION — remaining domain boundary README.** Close or deliberately inherit the remaining Settlements/Infrastructure gap. Preserve the 12 completed boundaries.
7. **NEEDS VERIFICATION — scaffold disposition.** Inspect the 25 exact-phrase matches, distinguish current scaffolds from historical mentions, and classify actual scaffolds as fill, supersede, migrate, mirror, retain as lineage, or retire; do not mass-delete by size or wording alone.
8. **CONFLICTED — naming and aliases.** Resolve flat versus nested, snake versus kebab, and duplicate-scope paths through consumer inventories and reviewed migration.
9. **NEEDS VERIFICATION — shared packet ownership.** Determine which parts of the 13 repeated four-file packets are shared kernel, generated projection, domain delta, or independent procedure.
10. **NEEDS VERIFICATION — current metadata.** Reconcile stale May 2026 owner, status, link, and no-mounted-repo statements in individual runbooks through file-specific inspection.
11. **PROPOSED — runbook registry.** Decide whether a machine-readable index is warranted; do not create one unless consumers, schema, authority, validation, and correction ownership are defined.

### P2 — validation and operations

12. **PROPOSED — semantic runbook validator.** Consider bounded checks for required identity, stop conditions, authority references, output ownership, finite outcomes, correction, rollback, and unsafe command patterns.
13. **NEEDS VERIFICATION — rehearsal evidence.** Inventory which procedures have fixture, simulation, drill, or incident records tied to exact versions.
14. **NEEDS VERIFICATION — required-check coupling.** Confirm which documentation and procedure checks are required by current rulesets and whether path filters cover this subtree.
15. **UNKNOWN — operational admission.** Determine which procedures, if any, are admitted for real environments and actors rather than merely tracked as drafts.
16. **UNKNOWN — deployed consumers.** Inventory applications, workers, operators, automation, and external users that rely on these paths or anchors.

[Back to top](#top)

---

## Evidence basis

| Evidence | Use in this edition | Limitation |
|---|---|---|
| `main@f7af2c3dcefd38ae5e86141cfbc0931c0ef7d90f` | Pins the target, runbook tree, direct children, sampled documents, ADRs, and review routing | Commit bytes do not prove runtime behavior, operational admission, release, or publication |
| Exact `docs/runbooks/` Git tree | Direct-child map and all recursive tracked paths | Tree presence does not prove content quality or use |
| Exact Git-tree and repository-text counts | Base: 42 direct entries, 116 Markdown files, 11 substantive domain README paths, no one-byte placeholders, and 25 exact `PROPOSED scaffold` phrase matches. After this change: 117 Markdown files and 12 substantive domain README paths; other counts unchanged. | Tree and text counts are not a semantic maturity audit |
| Accepted ADR-0029 and Directory Rules v2 | Placement authority, README inheritance, compatibility, migration, correction, and rollback rules | Does not validate individual procedures |
| Current ADR index | Three accepted and 34 proposed numbered decisions | Index cannot accept a decision itself |
| Current CODEOWNERS | Verifies GitHub review routing | Does not establish stewardship, expertise, independent approval, policy, or release authority |
| Twelve substantive local domain READMEs after this change | Supports the current closed and open local-boundary findings; child maturity remains lane-specific | Documentation state does not prove rehearsal, operational admission, release, or publication |
| Sampled long-form and scaffold-shaped runbooks | Supports other bounded maturity and drift findings | Not a full line-by-line audit of all 117 files |
| Bounded repository search | Dedicated validator and workflow-reference findings | Does not prove absence outside searched terms or runtime systems |

### Assumptions deliberately not made

This edition does not assume:

- a long runbook is correct or current;
- repeated files are safe to deduplicate;
- a scaffold should be deleted;
- a command is valid because it appears in Markdown;
- a green docs check proves an operational procedure;
- a rehearsal approves a release;
- a runbook grants permissions;
- a proposed ADR governs current behavior;
- CODEOWNERS assigns qualified stewardship;
- a merged pull request changes lifecycle or publication state; or
- a documentation rollback reverses a real-world action.

[Back to top](#top)

---

## Last reviewed and rollback

**2026-08-28** — v1.8 automated repository-evidence refresh against `main@2de55d48ab35a41875eb9f094dc55dda18618ecc`. Human review remains pending; this refresh records repository bytes and does not approve any procedure.

Re-review this README when:

- direct children, domain lanes, scaffold count, aliases, or generated relationships change;
- a runbook is operationally admitted, deprecated, migrated, or retired;
- accepted doctrine or an ADR changes runbook placement or authority;
- CODEOWNERS, stewardship, required checks, or validation coverage changes;
- a sensitive procedure, incident, correction, withdrawal, or rollback exposes a documentation gap;
- the shared domain packet is consolidated or generated; or
- a material command, environment, source, policy, release, or public client changes.

| Edition | Date | Change | Effect |
|---|---|---|---|
| **v1.8** | 2026-08-28 | Added the Roads/Rail/Trade boundary and recorded the resulting 117 Markdown files, 25 exact-phrase matches, 92 other files, 12 substantive boundaries, and one remaining gap. | Documentation only; Roads/Rail/Trade operations, human review, source admission, policy, proof, promotion, rollback, release, deployment, and publication remain separate |
| **v1.7** | 2026-08-28 | Added the Soil boundary, reconciled the exact base inventory from stale 114/26/88 claims to 115/25/90, and recorded the resulting 116 Markdown files, 25 exact-phrase matches, 91 other files, 11 substantive boundaries, and two remaining gaps. | Documentation only; Soil operations, human review, source admission, proof, promotion, rollback, release, deployment, and publication remain separate |
| **v1.6** | 2026-08-27 | Replaced the one-byte People/DNA/Land boundary, corrected its test overview to two executable synthetic profiles, preserved the then-recorded 114-file inventory, and recorded ten substantive boundaries with three lanes still missing a local README. | Documentation only; sensitive-data handling, human review, operational admission, release, and publication remain separate |
| **v1.5** | 2026-08-27 | Replaced the one-byte Hydrology boundary, preserved the 114-file inventory, and recorded nine substantive boundaries, no one-byte placeholders, and four lanes without a local README. | Documentation only; human review and operational admission remain separate |
| **v1.4** | 2026-08-27 | Replaced the one-byte Hazards boundary, reconciled the 114-file inventory after the one-byte Hydrology README landed, and recorded eight substantive boundaries, one placeholder, and four lanes without a local README. | Documentation only; human review and operational admission remain separate |
| **v1.3** | 2026-08-27 | Refreshed the exact 113-file inventory, ADR status count, scaffold-phrase count, and all 13 domain-boundary README findings; recognized seven substantive local boundaries, one one-byte Hazards placeholder, and five lanes without a local README. | Documentation only; human review and operational admission remain separate |
| **v1.2** | 2026-08-24 | Refreshed exact inventory and navigation; recognized the substantive Agriculture and Archaeology boundary READMEs and their mixed child maturity; distinguished one-byte placeholders and lexical scaffold-phrase matches from completed boundary contracts or semantic maturity. | Documentation only; no procedure execution or authority change |
| **v1.1** | 2026-08-14 | Replaced proposal-only inventory with current subtree counts, direct-child map, root and domain indexes, scaffold and alias disclosure, risk-based authoring contract, finite outcomes, validation boundaries, prioritized backlog, and exact rollback. | Documentation only; no procedure execution or authority change |
| **v1** | 2026-05-12 | Initial operational-runbook proposal and authoring template. | Historical documentation state |

### Documentation rollback

Restore the prior file blob:

```text
path: docs/runbooks/README.md
prior_blob: 4f33dfa18cd69fe6a6b990aac71be08d59e7d13e
```

or revert the focused content commit created by this change. That rollback restores the v1.6 documentation snapshot. It does not remove current runbooks, undo a procedure, reverse an incident response, change source/evidence/policy/release state, restore a public carrier, deploy, promote, publish, or change repository settings.

[Back to top](#top)
