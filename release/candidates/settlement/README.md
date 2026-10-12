<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-settlement-readme
title: release/candidates/settlement/ — Settlement Candidate Compatibility Lane
version: v2
status: draft
policy_label: public
owners:
  - <settlements-infrastructure-domain-steward>
  - <release-steward>
  - <data-steward>
  - <policy-sensitivity-reviewer>
updated: 2026-07-22
tags: [kfm, release, candidates, settlement, settlements-infrastructure, compatibility, pre-publication, evidence, sensitivity, review, validation, correction, rollback]
truth_posture: "CONFIRMED repository paths and bounded workflow evidence; PROPOSED compatibility and dossier guidance; CONFLICTED settlement versus settlements-infrastructure segment; NEEDS VERIFICATION for accepted migration authority, semantic enforcement, release inventory, and public adoption"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f37a8c8bb77840d1189d731d1043ad1d05ec5fc0
  prior_blob: 2b9045ea2de5723cc97acca176dcdc82f3234cb9
notes:
  - "This README is compatibility and release guidance. It is not a candidate, PromotionDecision, ReleaseManifest, PolicyDecision, proof, released artifact, or publication authority."
  - "Directory Rules use settlements-infrastructure as the working release-candidate segment; repository doctrine also records an unresolved settlement versus settlements-infrastructure slug conflict. This README does not resolve, mirror, or migrate that conflict."
  - "The inspected domain workflow performs bounded static readiness checks and explicit holds. It does not establish semantic validation, proof production, release approval, or public readiness."
  - "Base advanced from 8db841822c111cb5b6477003dc72f0455f6c41ad to f37a8c8bb77840d1189d731d1043ad1d05ec5fc0 before mutation; comparison showed only pipelines/publish/fauna/README.md changed, so the target and inspected settlement/release evidence remained unchanged."
[/KFM_META_BLOCK_V2] -->

# `release/candidates/settlement/` — Settlement Candidate Compatibility Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![class](https://img.shields.io/badge/class-compatibility-orange)
![working lane](https://img.shields.io/badge/working__lane-settlements--infrastructure-purple)
![publication](https://img.shields.io/badge/publication-not__authorized-orange)
![posture](https://img.shields.io/badge/default-fail__closed-red)

> [!CAUTION]
> **This is a compatibility and navigation lane, not an independent Settlement release authority.** Current Directory Rules use `settlements-infrastructure` as the working compound-domain segment and record the shorter `settlement` form as unresolved path variance. Place new candidate dossiers under [`release/candidates/settlements-infrastructure/`](../settlements-infrastructure/README.md) unless an accepted ADR and migration plan establish another canonical path.

> [!IMPORTANT]
> **A candidate is not a release.** A file, directory, passing shape check, pull request, merge, deployment, generated manifest, map layer, export, or AI summary does not promote or publish KFM material. Publication remains a governed state transition supported by separate evidence, policy, validation, review, manifest, correction, and rollback records.

## Quick jump

[Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Lifecycle](#candidate-lifecycle) · [Dossier contract](#canonical-candidate-dossier-contract) · [Decisions](#decision-vocabulary) · [Handoff](#manifest-handoff) · [Example](#illustrative-candidate-dossier) · [Open items](#open-verification-items) · [Rollback](#rollback)

## Purpose

`release/candidates/settlement/` preserves discoverability for short-name or lineage references to Settlement release-candidate work while routing current dossiers into the working Settlements/Infrastructure bounded context.

It may contain only:

- this compatibility README;
- migration, deprecation, or supersession pointers approved through repository governance;
- safe indexes that point to canonical dossiers without copying their contents; and
- temporary, non-authoritative placement notes needed to reconcile a legacy reference.

It must not become a second place to assemble, approve, manifest, or publish Settlement candidates.

The lifecycle boundary remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Candidate review occurs before `PUBLISHED`. Promotion is a governed state transition, not a file move.

## Authority level

**Compatibility/index guidance under the `release/` responsibility root; non-authoritative for place truth, infrastructure truth, policy, proof, released artifacts, or public behavior.**

The [Directory Rules](../../../docs/architecture/directory-rules.md) assign release candidates to `release/candidates/<domain>/`, release decisions to `release/`, and released public-safe artifacts to `data/published/`. The [Domain Placement Law](../../../docs/architecture/domain-placement-law.md) identifies `settlements-infrastructure` as the canonical filesystem segment and classifies the shorter atlas form as lineage pending reconciliation. The domain [Canonical Paths](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) document uses `release/candidates/settlements-infrastructure/` as the working form and records `settlement` versus `settlements-infrastructure` as `CONFLICTED` pending ADR-class resolution.

### Repository fit

```text
release/
├── candidates/
│   ├── settlement/                    # compatibility/index lane; you are here
│   └── settlements-infrastructure/    # working compound-domain candidate lane
├── promotion_decisions/               # PromotionDecision records
├── manifests/                         # ReleaseManifest records
├── rollback_cards/                    # rollback records
└── correction_notices/                # correction records

data/
├── receipts/                           # process memory
├── proofs/                             # evidence and proof closure
└── published/                          # released public-safe artifacts
```

This README does not rename or remove either candidate lane, declare a migration complete, create a runtime alias, or make the two domain segments interchangeable outside this bounded compatibility purpose.

### Compatibility contract

Required behavior:

- Treat `settlement/` as a short-name compatibility surface only.
- Route each new candidate dossier to [`../settlements-infrastructure/`](../settlements-infrastructure/README.md) unless accepted governance changes the working domain identity.
- Preserve legacy references long enough to inventory and migrate their consumers safely.
- Use repository-relative pointers rather than duplicating canonical dossier material.
- Mark any active dossier discovered here `HOLD` for placement review before further advancement.
- Preserve history through an explicit migration, supersession, or deprecation record; do not silently rewrite identity.
- Keep this lane non-publishing and free of lifecycle payloads and sensitive operational detail.

Prohibited behavior:

- Do not create new dossier subdirectories under `settlement/`.
- Do not mirror a canonical dossier and allow both copies to evolve.
- Do not infer that `settlement` and `settlements-infrastructure` are interchangeable in contracts, schemas, policy packages, source registries, object identifiers, pipeline routes, tests, or runtime routes.
- Do not copy exact critical-infrastructure geometry, dependency detail, operator-sensitive data, condition observations, restricted cultural data, living-person data, or private land associations into this lane.
- Do not use compatibility language to bypass evidence, rights, sensitivity, review, manifest, correction, or rollback gates.
- Do not delete or redirect this path until inbound references, generated consumers, candidate inventory, migration authority, deprecation period, and rollback impact have been checked.

### Reconciliation state

The existence of both candidate lanes is repository evidence of path variance, not proof that KFM has two independent Settlement domains. Current Directory Rules provide the working `settlements-infrastructure` form, while domain doctrine records the conflict as `OPEN-CP-01` / `OPEN-SI-01`. Removal, aliasing, or migration of the short path remains `NEEDS VERIFICATION` because this revision does not establish a complete inbound-reference inventory, accepted migration ADR, deprecation window, or rollback manifest.

No matching Settlement entry was found in the inspected [`docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md). That absence does not resolve the conflict; drift-register synchronization remains an open governance action outside this one-README revision.

## Status

### Evidence snapshot

| Field | Current finding |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Visibility | Public |
| Base ref | `main` |
| Pinned evidence commit | `f37a8c8bb77840d1189d731d1043ad1d05ec5fc0` |
| Prior target blob | `2b9045ea2de5723cc97acca176dcdc82f3234cb9` |
| Document lifecycle | `draft` |
| Owning responsibility root | `release/` |
| Path class | Compatibility/index lane; no independent release authority |
| Working compound domain segment | `settlements-infrastructure` |
| Working candidate lane | [`release/candidates/settlements-infrastructure/`](../settlements-infrastructure/README.md) |
| Segment authority | `CONFLICTED`; the working form follows Directory Rules pending accepted ADR/migration resolution |
| GitHub review route | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) routes `release/` to `@bartytime4life`; this is review routing, not proof of semantic ownership, independent approval, or release authority. |
| Semantic owner placeholders | `NEEDS VERIFICATION`; role names in the metadata are not verified GitHub identities or StewardshipAssignments. |
| Candidate inventory in this lane | `UNKNOWN`; the scoped inspection verified this README but did not establish a complete directory tree or governed candidate dossier. |
| Public effect of this README | None; it is guidance and a compatibility boundary, not a `PromotionDecision`, `ReleaseManifest`, policy decision, proof, or publication record. |

### Maturity matrix

| Surface | State at the pinned commit | Safe conclusion |
|---|---|---|
| Short candidate lane | `CONFIRMED` README path | The path exists. Its presence does not establish canonical domain identity or an active candidate. |
| Compound candidate lane | `CONFIRMED` README path | The working candidate lane exists, but its README and existence do not prove release readiness. |
| Domain-path decision | `CONFLICTED / NEEDS VERIFICATION` | `settlement` and `settlements-infrastructure` forms coexist; no accepted migration was established. |
| Domain test parent | `CONFIRMED` documentation; executable coverage `NEEDS VERIFICATION` | [`tests/domains/settlements-infrastructure/`](../../../tests/domains/settlements-infrastructure/README.md) documents intended no-network guardrails but does not establish a substantive passing suite. |
| Domain workflow | `CONFIRMED` bounded static checks and holds | The inspected [workflow](../../../.github/workflows/domain-settlements-infrastructure.yml) reports semantic-validation, proof-producer, and release-dry-run holds; green execution is not release evidence. |
| Promotion decision shape | `CONFIRMED` `PROPOSED` schema | The schema defines `APPROVE`, `DENY`, and `ABSTAIN`; schema presence does not prove end-to-end enforcement. |
| Release manifest shape | `CONFIRMED` thin `PROPOSED` stub | The inspected schema requires only `id` and allows additional properties; shape acceptance is not manifest closure. |
| Sensitive-infrastructure posture | `CONFIRMED` doctrine; enforcement `NEEDS VERIFICATION` | Exact facility geometry, dependencies, operator-sensitive details, and condition observations fail closed pending public-safe transformation and review. |
| Released Settlement inventory | `UNKNOWN` | No complete manifest, published-artifact, correction, or rollback inventory was established by this revision. |

Repository-relative links and commit-pinned evidence make the boundary inspectable. They do not upgrade draft docs, proposed ADRs, stub schemas, or held workflows into verified runtime enforcement.

## What belongs here

- This README.
- A safe compatibility index that points to a dossier under `../settlements-infrastructure/`.
- A reviewed migration, deprecation, or supersession pointer.
- A placement `HOLD` note that contains no candidate payload or sensitive detail.
- A correction to stale navigation that preserves lineage and rollback.

Any pointer should identify the canonical target immutably when possible and must not claim that the target is approved, released, or public merely because it exists.

## What does NOT belong here

- New or actively evolving candidate dossiers.
- Raw, work, quarantine, processed, catalog, triplet, or published payloads.
- Bulk datasets, tiles, exports, service payloads, screenshots, map-ready artifacts, or graph projections.
- Source descriptors, evidence bundles, proofs, receipts, schemas, contracts, policies, validators, fixtures, tests, pipelines, or manifests copied into this lane.
- Exact critical-infrastructure locations, network dependencies, operator-sensitive information, condition observations, security details, private addresses, living-person joins, or restricted cultural information.
- Generated language, map content, dashboards, indexes, or model output used as sovereign evidence.
- Final release approval, self-issued promotion, or direct public-surface activation.
- Floating `latest` pointers without immutable identity, release state, correction lineage, and rollback support.

## Inputs

This compatibility lane accepts only reviewed navigation and migration information derived from:

- the parent [candidate index](../README.md) and [release root](../../README.md);
- the working [`settlements-infrastructure` candidate lane](../settlements-infrastructure/README.md);
- Directory Rules and accepted ADRs;
- the repository's [Domain Placement Law](../../../docs/architecture/domain-placement-law.md);
- the domain [Canonical Paths](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md), [Data Lifecycle](../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md), and [Release Index](../../../docs/domains/settlements-infrastructure/RELEASE_INDEX.md);
- verified candidate, migration, supersession, correction, or rollback records; and
- reviewer-approved repository-relative links that do not expose restricted material.

A prose reference, issue, pull request, branch, or search result is not sufficient evidence of canonical identity or release state by itself.

## Outputs

Permitted outputs are limited to:

- a safe route to the working canonical dossier;
- a visible `HOLD`, deprecation, migration, or supersession notice;
- an auditable statement of unresolved path variance; and
- reviewer guidance that prevents parallel authority.

This lane emits no lifecycle payload, proof, policy decision, promotion decision, manifest, published artifact, public API response, or release state.

## Validation

### Compatibility checks

- Confirm that every relative link resolves at the reviewed commit.
- Confirm that no new dossier or payload is being created under `settlement/`.
- Confirm that a pointer targets the compound-domain candidate lane and does not create a mutable mirror.
- Confirm that the linked candidate has immutable identity, or mark the gap `HOLD` / `NEEDS VERIFICATION`.
- Confirm that path variance remains visible until an accepted ADR and migration close it.
- Confirm that no source, contract, schema, policy, proof, receipt, manifest, catalog, or released-artifact authority is duplicated here.
- Confirm that prose does not overstate runtime enforcement, release readiness, public adoption, or candidate inventory.

### Canonical dossier review gates

These gates apply to the dossier under `../settlements-infrastructure/`; they do not authorize storing the dossier here.

| Gate | Minimum question | Fail-closed result |
|---|---|---|
| Placement | Is the dossier in the working compound-domain lane with no evolving short-name copy? | `HOLD` and reconcile placement. |
| Identity | Are candidate, dataset, place, geography, object role, and version identities stable and collision-aware? | `REPAIR_REQUIRED` or `ABSTAIN`. |
| Source role | Is each source used only for claims it is competent to support? | `REPAIR_REQUIRED` or `ABSTAIN`. |
| Evidence | Do consequential references resolve to scoped EvidenceBundles with provenance and integrity closure? | `ABSTAIN`. |
| Time | Are source, observed, valid, retrieval, build, release, correction, and supersession times distinct where material? | `REPAIR_REQUIRED` or `ABSTAIN`. |
| Rights and policy | Are license, redistribution, attribution, sovereignty, cultural review, privacy, and access obligations resolved? | `DENY`, `ABSTAIN`, or `HOLD`. |
| Sensitivity | Are exact infrastructure, dependency, operator, condition, location, and combination risks evaluated with receipted public-safe transforms? | `DENY` or `HOLD`. |
| Cross-lane ownership | Are Roads/Rail, Hydrology, Hazards, and People/Land evidence linked without silently transferring ownership? | `REPAIR_REQUIRED` or `ABSTAIN`. |
| Validation | Did applicable schema, semantic, identity, temporal, spatial, evidence, policy, no-leak, negative, and citation checks run and pass? | `REPAIR_REQUIRED`, `DENY`, or `ABSTAIN`. |
| Review | Are required roles identified, conflicts visible, and independent approval satisfied where applicable? | `HOLD`. |
| Release readiness | Are the promotion decision, manifest inputs, immutable targets, correction path, and rollback support complete? | `DENY`, `ABSTAIN`, or `HOLD`. |

### Workflow-trigger finding

The inspected domain workflow runs on ordinary `pull_request`, `push`, and manual events with `contents: read`. It checks repository boundaries and records explicit holds for semantic validation, proof production, and release dry-run readiness. It does not use `pull_request_target`, write permissions, self-hosted runners, or a publication step in the inspected file.

Because its triggers are broad, this documentation change may run the workflow even though the workflow reads the compound-domain candidate lane rather than this compatibility README. A green held result means the bounded check executed; it does not mean Settlement material is validated, approved, released, or published.

### README validation checklist

- [ ] One H1 outside the illustrative nested dossier.
- [ ] Consecutive heading hierarchy and unique local anchors.
- [ ] Balanced code fences, valid tables, and final newline.
- [ ] All repository-relative file links resolve at the result commit.
- [ ] KFM Meta Block preserves the stable `doc_id` and labels unresolved owners.
- [ ] Core truth labels and conflict qualifiers remain distinct.
- [ ] No unsupported route, schema, workflow, release, or candidate claim is presented as implemented.
- [ ] No secrets, private data, sensitive coordinates, or restricted operational details appear.
- [ ] AI-authored changes carry a schema-valid generated receipt with human review pending.

## Review burden

| Change class | Minimum review burden | Boundary |
|---|---|---|
| Compatibility README or navigation pointer | Release reviewer + Settlements/Infrastructure domain reviewer + docs reviewer | GitHub CODEOWNERS routing alone does not prove semantic review. |
| Path migration, alias, or deprecation | Governance/docs + release + domain reviewers; accepted ADR when authority changes | Requires inbound-reference inventory, migration plan, deprecation window, and rollback. |
| Candidate dossier | Domain + data/evidence + release reviewers; policy/sensitivity reviewer when applicable | Must occur in the compound-domain lane. |
| Place identity or legal-status claim | Domain + evidence/source-role reviewer | A census place, legal municipality, townsite, and historical settlement must not be silently collapsed. |
| Critical-infrastructure or restricted-location candidate | Domain + policy/sensitivity + release reviewers and any required cultural/sovereignty reviewer | Default fail closed; public-safe transformation and no-leak evidence required. |
| Promotion or manifest handoff | Authorized release reviewer plus required independent reviewers | A candidate status or README cannot issue approval. |

The semantic owner role names above remain `NEEDS VERIFICATION`; [CODEOWNERS](../../../.github/CODEOWNERS) currently routes `/release/` to `@bartytime4life` but does not establish steward assignment, separation of duties, or completed review.

## Related folders

| Concern | Owning surface | Relationship to this README |
|---|---|---|
| Working candidate dossier | [`release/candidates/settlements-infrastructure/`](../settlements-infrastructure/README.md) | Create and review new dossiers there. |
| Candidate-parent guidance | [`release/candidates/`](../README.md) | Supplies shared candidate statuses and minimum review fields. |
| Release-root guidance | [`release/`](../../README.md) | Defines the release-governance boundary. |
| Promotion decisions | [`release/promotion_decisions/`](../../promotion_decisions/README.md) and [`PromotionDecision`](../../../contracts/release/promotion_decision.md) | Referenced by a canonical dossier; never replaced by README status. |
| Release manifests | [`release/manifests/`](../../manifests/README.md) and [`ReleaseManifest`](../../../contracts/release/release_manifest.md) | Bind an approved release path; candidate prose does not self-manifest. |
| Correction and rollback | [`release/correction_notices/`](../../correction_notices/README.md), [`release/rollback_cards/`](../../rollback_cards/README.md), and [`CorrectionNotice`](../../../contracts/correction/correction_notice.md) | Must be reachable for a material release; not stored here. |
| Domain meaning | [`docs/domains/settlements-infrastructure/`](../../../docs/domains/settlements-infrastructure/README.md) | Human-facing bounded-context doctrine. |
| Domain segment | [`domain-placement-law.md`](../../../docs/architecture/domain-placement-law.md) | Identifies the long compound filesystem segment and keeps short-name reconciliation visible. |
| Domain path posture | [`CANONICAL_PATHS.md`](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) | Records the working compound slug and unresolved short-name variance. |
| Domain lifecycle | [`DATA_LIFECYCLE.md`](../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md) | Preserves phase and promotion boundaries. |
| Domain release posture | [`RELEASE_INDEX.md`](../../../docs/domains/settlements-infrastructure/RELEASE_INDEX.md) | Describes proposed release families and open verification burden. |
| Evidence closure | [`EvidenceBundle`](../../../contracts/evidence/evidence_bundle.md) and `data/proofs/` | A dossier resolves evidence; this README is not evidence. |
| Machine shape | [`release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json) and [`promotion_decision.schema.json`](../../../schemas/contracts/v1/release/promotion_decision.schema.json) | Schema authority stays outside this lane; current manifest shape is proposed and thin. |
| Admissibility | [`policy/README.md`](../../../policy/README.md) | Policy authority stays outside this lane. |
| Domain tests | [`tests/domains/settlements-infrastructure/`](../../../tests/domains/settlements-infrastructure/README.md) | Documents intended guardrails; passing coverage remains separately verified. |
| Domain workflow | [`.github/workflows/domain-settlements-infrastructure.yml`](../../../.github/workflows/domain-settlements-infrastructure.yml) | Bounded readiness checks and explicit holds; not release authority. |
| Generated-work provenance | [`data/receipts/generated/`](../../../data/receipts/generated/README.md) | Records AI authorship; a generated receipt is process memory, not proof or release approval. |

No path or example in this README authorizes a parallel schema, contract, policy, registry, receipt, proof, catalog, release, or public-data home.

## ADRs

| ADR or open item | Status at the evidence snapshot | Relevance |
|---|---|---|
| `OPEN-CP-01` / `OPEN-SI-01` in the domain path and lifecycle docs | `CONFLICTED / NEEDS VERIFICATION` | Governs `settlement` versus `settlements-infrastructure` reconciliation. No accepted migration was established. |
| [`ADR-0018 — Promotion Gate Sequence`](../../../docs/adr/ADR-0018-promotion-gate-sequence.md) | `PROPOSED`, not accepted | Describes a proposed gate sequence; do not claim workflow enforcement from it. |
| [`ADR-0024 — Steward Separation of Duties`](../../../docs/adr/ADR-0024-steward-separation-of-duties-for-release.md) | `PROPOSED`, not accepted | Describes proposed release-role separation; CODEOWNERS does not prove enforcement. |
| [`ADR-0010 — Deny by Default`](../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | `PROPOSED / CONFLICTED` | Supports conservative infrastructure handling but has unresolved numbering and overlap. |

This README does not accept an ADR, resolve the segment conflict, or authorize a migration. Any future ADR that changes the working path must preserve lineage, links, candidate identity, review history, correction references, and rollback.

## Last reviewed

| Field | Value |
|---|---|
| Date | **2026-07-22** |
| Repository snapshot | `main@f37a8c8bb77840d1189d731d1043ad1d05ec5fc0` |
| Review type | Repository-grounded compatibility-lane revision; no candidate, policy, schema, workflow, release, or public artifact changed. |
| Next review trigger | Accepted path ADR, candidate added to either lane, migration or deprecation proposal, manifest handoff, sensitivity-posture change, correction, rollback, or six months after this date. |

## Candidate lifecycle

The parent candidate index documents the statuses below. They are review workflow labels, not public-release authority.

| Candidate status | Meaning in a canonical dossier |
|---|---|
| `PROPOSED` | Candidate is named but is not ready for review. |
| `ASSEMBLING` | Evidence, validation, rights, sensitivity, review, and rollback support are being gathered. |
| `READY_FOR_REVIEW` | The dossier is complete enough for the named reviewers to evaluate. |
| `APPROVED_FOR_MANIFEST` | A separately governed decision permits manifest preparation; this is not publication. |
| `PROMOTED` | A governed release path records the transition; verify the decision, manifest, and released artifact rather than trusting the label alone. |
| `DEFERRED` | Work is intentionally paused without declaring the candidate invalid. |
| `REPAIR_REQUIRED` | A named defect must be corrected before review continues. |
| `BLOCKED` | A policy, rights, sensitivity, evidence, implementation, authority, or placement blocker prevents advancement. |
| `WITHDRAWN` | The candidate is removed from consideration while audit history remains. |
| `SUPERSEDED` | A newer candidate replaces it through explicit lineage. |

Discovery of a dossier under this short-name lane should produce a placement `HOLD`, not automatic status advancement.

## Canonical candidate dossier contract

A Settlement-focused candidate remains part of the working `settlements-infrastructure` bounded context. Its dossier should answer each field below or explicitly record `UNKNOWN`, `NEEDS VERIFICATION`, or a blocking reason.

| Field | Required content |
|---|---|
| Candidate identity | Stable candidate ID, version, domain `settlements-infrastructure`, and immutable run/build reference |
| Scope | Included and excluded object classes, geography, temporal extent, precision, intended public surface, and non-goals |
| Artifact pointer | Immutable pointer to the candidate artifact in its owning lifecycle path; never the payload itself |
| Proposed target | Exact released artifact family; no floating `latest` alias |
| Source closure | SourceDescriptor references, source roles, retrieval context, rights, attribution, authority limits, and freshness |
| Evidence closure | `EvidenceRef` plus resolvable `EvidenceBundle`, claim scope, integrity digest, citation-validation state, and conflicts |
| Place identity | Strategy for Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, and unresolved collisions |
| Time | Source, observed, valid, retrieval, build, release, correction, and supersession times where material |
| Geometry | CRS, boundary version, uncertainty, positional support, precision, generalization, and reverse-engineering risk |
| Sensitivity | Critical-infrastructure, dependency, operator, condition, cultural, sovereignty, living-person, land, and combination-risk findings |
| Cross-lane relations | Roads/Rail, Hydrology, Hazards, and People/Land references with ownership and source roles preserved |
| Transform receipts | Redaction, aggregation, generalization, withholding, or other public-safe transformation references |
| Validation | Schema, semantic, identity, temporal, spatial, evidence, policy, no-leak, negative, citation, and deterministic-build results |
| Review | Author, reviewer roles, independence requirement, conflicts, review record, and current disposition |
| Manifest handoff | `PromotionDecision` reference, manifest-readiness state, exact blockers, and intended manifest family |
| Correction and rollback | Correction path, invalidation targets, rollback target, supersession link, and safe prior state |

### Source and evidence discipline

- A legal municipality source, census geography, gazetteer, historic map, local record, infrastructure operator source, transport source, or hazard source proves only what its role and scope support.
- `Settlement`, `Municipality`, `CensusPlace`, `Townsite`, and `GhostTown` must not be collapsed merely because labels or geometries overlap.
- Historical existence does not prove current legal status, current population, current boundary, public access, current service, or current infrastructure condition.
- A search index, OCR transcript, map label, geocoder result, graph edge, model output, or AI extraction is not automatically identity or legal-status evidence.
- Cross-lane relations link evidence without transferring authority between Settlements/Infrastructure, Roads/Rail, Hydrology, Hazards, and People/Land.
- A bare citation is not evidence closure. Consequential claims must resolve to a scoped EvidenceBundle with source identity, provenance, integrity, uncertainty, review state, and release state.

### Sensitive-data safeguards

Before manifest handoff, reviewers should verify:

- exact facility, network, dependency, operator, condition, security, and continuity-sensitive details are denied or restricted unless explicitly cleared;
- public geometry is generalized, aggregated, redacted, or withheld at a reviewed precision with a transform receipt;
- reverse-engineering and combination risk are evaluated across layers, attributes, time, screenshots, search, exports, graph relations, and AI text;
- reservation-community, cultural, sacred, archaeological, burial, or sovereignty-sensitive context receives the required review and withholding posture;
- living-person, private-address, private-land, and person-to-place joins do not leak through settlement context;
- sensitive values do not appear in filenames, logs, receipts, examples, diffs, issue text, or pull-request text;
- caches, derived tiles, indexes, exports, graph projections, and AI context have invalidation targets; and
- denial and abstention reasons are safe to disclose.

This README does not set numeric precision thresholds or invent source authority, cultural-review rules, or policy semantics. Those decisions require governing contracts, schemas, policy, fixtures, tests, and authorized review in their owning roots.

## Decision vocabulary

Keep candidate status, promotion decisions, policy outcomes, and public runtime responses distinct.

### Promotion decision

The inspected [`PromotionDecision` contract](../../../contracts/release/promotion_decision.md) and paired [schema](../../../schemas/contracts/v1/release/promotion_decision.schema.json) define:

| Decision | Meaning |
|---|---|
| `APPROVE` | The evaluated transition has enough governed support to proceed through the remaining release process. It is not publication by itself. |
| `DENY` | A blocking condition prevents the transition; preserve the prior state and record a safe reason. |
| `ABSTAIN` | The gate cannot decide from available, current, safe evidence; preserve the prior state and route for remediation or review. |

### Review dispositions

`HOLD` and `REPAIR_REQUIRED` are review/workflow dispositions used to stop advancement safely. Do not add them to a machine enum unless the owning contract and schema authorize them.

### Governed public response

Public API, UI, map, export, graph, search, and AI surfaces use their governed response contract, commonly `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. A promotion `APPROVE` does not authorize a public `ANSWER`; released artifact state, manifest, evidence, policy, sensitivity, staleness, correction state, and request context still govern delivery.

## Manifest handoff

A dossier in the compound-domain lane may move toward manifest preparation only after a separately governed `PromotionDecision` records `APPROVE` and all applicable gates are satisfied.

The handoff should identify:

- immutable candidate, dataset, run, geography, and version identifiers;
- exact processed, catalog, or triplet inputs;
- EvidenceBundle digests, source roles, citation-validation state, and unresolved conflicts;
- rights, attribution, cultural/sovereignty, privacy, and sensitivity decisions;
- geometry precision and public-safe transform receipts;
- validation reports, policy-bundle identity, and negative/no-leak results;
- author and reviewer role bindings and independence state;
- proposed released artifacts and content hashes;
- correction, cache/derivative invalidation, supersession, withdrawal, and rollback targets; and
- every remaining `UNKNOWN`, `NEEDS VERIFICATION`, or `CONFLICTED` item.

The inspected common [`release_manifest.schema.json`](../../../schemas/contracts/v1/release/release_manifest.schema.json) identifies itself as a `PROPOSED` greenfield stub, requires only `id`, and permits additional properties. Acceptance against that shape is not release closure. Do not describe manifest enforcement as complete until the contract, schema, validator, fixtures, policy, review records, signatures, and end-to-end release evidence agree.

## Illustrative candidate dossier

The example below is documentation only. It is not a schema, real candidate, release record, or permission to place a dossier in this compatibility directory.

```markdown
# <candidate-id> — Settlement candidate dossier

## Status

ASSEMBLING

## Placement

- Canonical working lane: release/candidates/settlements-infrastructure/<candidate-id>/
- Short-name copy: none

## Scope

- Object classes: <bounded settlement object classes>
- Geography and boundary version: <immutable reference>
- Valid/source/retrieval/build time: <explicit values>
- Intended public surface: <governed layer, API, report, or N/A>
- Excluded: <critical-infrastructure precision, restricted cultural data, private joins>

## Governed support

- Artifact: <immutable lifecycle pointer>
- Sources and roles: <SourceDescriptor references>
- Evidence: <EvidenceRef and EvidenceBundle digest>
- Rights and sensitivity: <PolicyDecision and transform receipts>
- Validation: <ValidationReport references>
- Review: <ReviewRecord references and independence state>

## Release handoff

- PromotionDecision: <reference or BLOCKED>
- Proposed manifest: <reference or N/A>
- Correction path: <reference>
- Rollback target: <reference>

## Open items

- <UNKNOWN, NEEDS VERIFICATION, CONFLICTED, or none>
```

Placeholder angle-bracket values are deliberate prompts for a reviewer. They must be replaced with exact, safe references or a visible blocking state before review advancement.

## Open verification items

- **CONFLICTED / NEEDS VERIFICATION** — resolve `settlement` versus `settlements-infrastructure` through an accepted authority decision and migration plan.
- **NEEDS VERIFICATION** — inventory all files, inbound links, generated consumers, and candidate records under both release-candidate lanes.
- **NEEDS VERIFICATION** — add or confirm a matching path-variance entry in the canonical drift register.
- **NEEDS VERIFICATION** — verify semantic steward assignments and independent release/sensitivity review beyond CODEOWNERS routing.
- **NEEDS VERIFICATION** — establish substantive executable domain tests, validators, safe fixtures, and no-network commands.
- **NEEDS VERIFICATION** — establish an accepted proof producer and deterministic release dry-run path; the inspected workflow intentionally reports holds.
- **NEEDS VERIFICATION** — mature and enforce the ReleaseManifest contract/schema beyond the current thin proposed shape.
- **NEEDS VERIFICATION** — verify current source rights, source-role assignments, public-safe precision, cultural/sovereignty review, and critical-infrastructure policy enforcement.
- **UNKNOWN** — whether any Settlement candidate has completed evidence, policy, validation, review, manifest, correction, and rollback closure.
- **UNKNOWN** — whether any released public-safe Settlement artifact is currently adopted by governed API, map, export, search, graph, or AI surfaces.

## Rollback

Before merge, rollback is to leave the draft pull request unmerged or revert the scoped branch commit. After merge, restore the previous README through a transparent revert commit or follow-up pull request; do not rewrite shared history.

Rollback is required if this lane begins to:

- host new or evolving candidate dossiers;
- duplicate the compound-domain lane;
- store lifecycle payloads, sensitive details, proofs, receipts, policy, contracts, schemas, manifests, or published artifacts;
- treat a compatibility pointer as canonical authority;
- treat a check, merge, manifest stub, map layer, or generated summary as publication; or
- bypass evidence, source-role, time, rights, sensitivity, review, correction, or rollback controls.

Restoring the prior README does not resolve the underlying path conflict. Any later migration must preserve stable candidate identifiers, links, history, review records, correction lineage, and rollback targets.
