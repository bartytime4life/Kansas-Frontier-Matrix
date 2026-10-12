<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-settlements-infrastructure-readme
title: release/candidates/settlements-infrastructure/ — Settlements / Infrastructure Candidate Review Lane
version: v2
status: draft
policy_label: public
owners:
  - <settlements-infrastructure-domain-steward>
  - <release-steward>
  - <data-steward>
  - <policy-sensitivity-reviewer>
updated: 2026-07-22
tags: [kfm, release, candidates, settlements-infrastructure, pre-publication, evidence, identity, rights, sensitivity, review, validation, correction, rollback]
truth_posture: "CONFIRMED repository paths, contract/schema contents, and bounded workflow holds; PROPOSED dossier guidance; CONFLICTED settlement versus settlements-infrastructure segment; NEEDS VERIFICATION for semantic enforcement, proof production, release dry run, release inventory, and public adoption"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 640fc2f3c9720cf17d640f0267bf540328e973f0
  prior_blob: 8fbb7928f6f9b8caca5336c7fb977ff18fe36b57
notes:
  - "This README governs a candidate-review lane. It is not a candidate, PromotionDecision, ReleaseManifest, PolicyDecision, proof, released artifact, or publication authority."
  - "Directory Rules use settlements-infrastructure as the working compound-domain segment; repository doctrine also records an unresolved settlement versus settlements-infrastructure path conflict. This README does not resolve or migrate that conflict."
  - "The inspected domain workflow performs bounded static readiness checks and explicit holds. It does not establish semantic validation, proof production, release approval, or public readiness."
[/KFM_META_BLOCK_V2] -->

# `release/candidates/settlements-infrastructure/` — Settlements / Infrastructure Candidate Review Lane

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-settlements--infrastructure-7048e8)
![publication](https://img.shields.io/badge/publication-not__authorized-orange)
![posture](https://img.shields.io/badge/default-fail__closed-red)

> [!CAUTION]
> **A candidate is not a release.** A dossier, file, directory, passing shape check, pull request, merge, deployment, map layer, export, or AI summary does not promote or publish KFM material. Publication remains a governed state transition supported by evidence, policy, validation, review, manifest, correction, and rollback records.

> [!IMPORTANT]
> **Settlements / Infrastructure is sensitivity-bearing.** Exact facility geometry, network dependencies, operator-sensitive detail, condition observations, cultural or sovereignty-sensitive information, living-person associations, and private-land joins fail closed until policy, review, public-safe transformation, and release requirements are satisfied. This lane must not expose candidate payloads merely to make review convenient.

## Quick jump

[Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Lifecycle](#candidate-lifecycle) · [Dossier](#canonical-candidate-dossier-contract) · [Gates](#release-readiness-gates) · [Sensitivity](#sensitivity-and-no-leak-controls) · [Handoff](#manifest-handoff) · [Example](#illustrative-candidate-dossier) · [Open items](#open-verification-items) · [Rollback](#rollback)

## Purpose

`release/candidates/settlements-infrastructure/` is the working pre-publication review lane for Settlements / Infrastructure candidate dossiers.

It helps authorized stewards determine whether a bounded candidate should:

- remain under assembly;
- enter formal review;
- advance toward manifest preparation;
- be deferred, repaired, blocked, withdrawn, or superseded; or
- remain unavailable because evidence, rights, time, sensitivity, validation, proof, review, correction, or rollback support is incomplete.

The lane stores review records and pointers. It does not store lifecycle payloads, create domain truth, replace contracts or policy, or authorize a public surface.

The lifecycle boundary remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Candidate review occurs before `PUBLISHED`. Promotion is a governed state transition, not a file move.

## Authority level

**Release-candidate guidance under the `release/` responsibility root; non-authoritative for settlement truth, infrastructure truth, evidence, policy, proof, released artifacts, or public behavior.**

The [Directory Rules](../../../docs/architecture/directory-rules.md) assign candidate dossiers to `release/candidates/<domain>/`, release decisions to `release/`, and released public-safe artifacts to `data/published/`. The [Domain Placement Law](../../../docs/architecture/domain-placement-law.md) places domains as lane segments under responsibility roots. The domain [Canonical Paths](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md) document uses this long-form lane as the working path while recording `settlement` versus `settlements-infrastructure` as unresolved variance.

### Repository fit

```text
release/
├── candidates/
│   ├── settlement/                    # compatibility/index lane
│   └── settlements-infrastructure/    # working candidate-review lane; you are here
├── promotion_decisions/               # PromotionDecision records
├── manifests/                         # ReleaseManifest records
├── rollback_cards/                    # rollback records
├── correction_notices/                # correction records
└── withdrawal_notices/                # withdrawal records

data/
├── receipts/                           # process memory
├── proofs/                             # evidence/proof closure
└── published/                          # released public-safe artifacts
```

This README does not make the path conflict disappear, declare every proposed domain path canonical, accept an ADR, or establish runtime aliases. New candidate dossiers use this working compound-domain lane unless accepted governance establishes a different path.

### Authority boundaries

| Surface | Authority | This lane may do | This lane must not do |
|---|---|---|---|
| Domain meaning | `contracts/` and domain doctrine | Link the applicable object family and scope. | Redefine `Settlement`, `Municipality`, `Facility`, `Dependency`, or another family. |
| Machine shape | `schemas/contracts/v1/` | Name schema/version expectations. | Invent a local schema or treat README examples as wire contracts. |
| Evidence | `EvidenceBundle`, evidence contracts, and proofs | Bind immutable EvidenceRefs and closure status. | Use generated prose, screenshots, maps, or candidate notes as sovereign evidence. |
| Rights and sensitivity | `policy/` plus governed decisions | Record decision refs, obligations, and public-safe transforms. | Self-approve restricted or exact-location release. |
| Validation | validators, tests, reports, and receipts | Link exact validation evidence and unresolved failures. | Turn a static workflow check into semantic proof. |
| Release decision | `PromotionDecision`, `ReleaseManifest`, and authorized review | Prepare a reviewable handoff. | Approve promotion, publish, or activate a public surface by itself. |
| Published artifact | `data/published/` behind governed interfaces | Name the proposed immutable target. | Store or serve the artifact from this lane. |

## Status

### Evidence snapshot

| Field | Current finding |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Visibility | Public |
| Base ref | `main` |
| Pinned evidence commit | `640fc2f3c9720cf17d640f0267bf540328e973f0` |
| Prior target blob | `8fbb7928f6f9b8caca5336c7fb977ff18fe36b57` |
| Document lifecycle | `draft` |
| Owning responsibility root | `release/` |
| Working candidate lane | `release/candidates/settlements-infrastructure/` |
| Short-name lane | [`release/candidates/settlement/`](../settlement/README.md), a compatibility and navigation lane |
| Segment authority | `CONFLICTED`; the working long-form follows Directory Rules pending accepted ADR/migration resolution |
| GitHub review route | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) routes `release/` to `@bartytime4life`; this is review routing, not semantic ownership or release approval. |
| Semantic owner assignments | `NEEDS VERIFICATION`; metadata role names are not verified GitHub identities or StewardshipAssignments. |
| Candidate inventory | `UNKNOWN`; this revision did not establish a complete governed inventory. |
| Public effect of this README | None; it is guidance, not a decision, proof, manifest, release, or publication record. |

### Maturity matrix

| Surface | State at the pinned commit | Safe conclusion |
|---|---|---|
| Candidate README | `CONFIRMED` existing compact draft | The lane exists, but its README does not prove an active or review-ready candidate. |
| Domain-path decision | `CONFLICTED / NEEDS VERIFICATION` | Long and short forms coexist; no accepted migration was established. |
| Domain tests | `CONFIRMED` documentation; substantive execution held | The test lane documents guardrails; it does not prove semantic coverage. |
| Domain workflow | `CONFIRMED` bounded static checks and explicit holds | Green held execution is not settlement, infrastructure, evidence, policy, proof, release, or publication truth. |
| Proof producer | `WORKFLOW_HOLD` | No accepted deterministic Settlements / Infrastructure proof producer or proof command is established by the inspected workflow. |
| Release dry run | `WORKFLOW_HOLD` | No accepted domain release-dry-run command or candidate-manifest contract is established by the inspected workflow. |
| Promotion decision shape | `CONFIRMED` paired `PROPOSED` schema | The schema requires evidence, policy, review, rollback, and `APPROVE` / `DENY` / `ABSTAIN`; enforcement remains bounded. |
| Release manifest shape | `CONFIRMED` thin `PROPOSED` stub | The schema requires only `id` and allows additional properties; schema acceptance would not establish release closure. |
| Sensitivity posture | `CONFIRMED` fail-closed doctrine; implementation `NEEDS VERIFICATION` | Exact critical-infrastructure and other sensitive detail require restriction or reviewed public-safe transformation. |
| Released domain inventory | `UNKNOWN` | No complete manifest, public-artifact, correction, withdrawal, or rollback inventory was established here. |

## What belongs here

- This folder README and safe sublane indexes.
- Candidate dossiers containing metadata, status, review findings, and immutable pointers.
- Readiness checklists and explicit `HOLD`, repair, defer, withdrawal, or supersession notes.
- Pointers to admitted sources, EvidenceBundles, proofs, validation reports, policy decisions, review records, receipts, and proposed release targets.
- Public-safe transform summaries that point to their RedactionReceipts or equivalent records.
- Manifest-handoff notes that identify remaining blockers without pretending a manifest exists.
- Correction, withdrawal, supersession, and rollback planning pointers.

Each dossier must be safe to review in a public repository. A pointer may be recorded here when the target is access-controlled; restricted payloads and reconstructive details remain outside this lane.

## What does NOT belong here

- Raw, work, quarantine, processed, catalog, triplet, or published payloads.
- Bulk datasets, tiles, GeoPackages, GeoParquet, PMTiles, exports, API payloads, map-ready files, screenshots, graph dumps, or model context packets.
- Source descriptors, EvidenceBundles, proofs, receipts, schemas, contracts, policies, validators, fixtures, tests, pipelines, manifests, decisions, correction notices, withdrawal notices, or rollback cards copied out of their authority roots.
- Exact critical-facility coordinates or footprints, dependency topology, vulnerability context, operator-sensitive details, condition observations, security controls, or continuity-sensitive information.
- Restricted cultural, sacred, burial, archaeological, sovereignty-sensitive, living-person, DNA/genomic, private-address, title, ownership, or private-land associations.
- Generated language, maps, tiles, graphs, vector indexes, embeddings, dashboards, or summaries used as sovereign evidence.
- Final release approval, self-issued promotion, direct public-surface activation, or a mutable `latest` pointer presented as release identity.
- Secrets, credentials, internal endpoints, private logs, or production operational material.

## Inputs

A candidate dossier may be assembled only from resolvable, appropriately scoped references such as:

- a stable candidate ID and immutable artifact digest;
- object-family and deterministic-identity references;
- admitted SourceDescriptors with source roles, rights, license, retrieval, and temporal metadata;
- EvidenceRefs that resolve to EvidenceBundles when claims depend on evidence;
- validation reports and run/transform/redaction receipts;
- rights, sensitivity, access, cultural/sovereignty, and policy decisions;
- review records and separation-of-duties evidence appropriate to risk;
- a proposed release target and consumer-impact inventory;
- correction, withdrawal, supersession, and rollback targets; and
- cross-lane dependencies that remain citations rather than reauthored truth.

An unresolved required input produces a visible hold. It must not be filled with a guess, an unverified path, or generated prose.

## Outputs

This lane supports only pre-publication review outputs:

- a candidate dossier state;
- a finite reviewer recommendation;
- a named blocker, repair plan, or abstention reason;
- an evidence-, policy-, validation-, and review-linked manifest-handoff recommendation; or
- a withdrawal, supersession, correction-planning, or rollback-planning pointer.

It does not emit a released artifact, proof, PolicyDecision, PromotionDecision, ReleaseManifest, correction, withdrawal, rollback execution, public alias, deployment, or publication event.

## Validation

### Candidate-content checks

Every dossier should be checked for:

1. stable candidate identity and immutable artifact pointer;
2. domain segment and object-family correctness;
3. source-role preservation and EvidenceRef-to-EvidenceBundle closure;
4. geographic and temporal scope, including source, observed, valid, retrieval, release, correction, and supersession time where applicable;
5. rights, license, access, sensitivity, cultural/sovereignty, living-person, land, and critical-infrastructure posture;
6. deterministic identity and no-collapse behavior across legal, census, historic, facility, operator, condition, and dependency roles;
7. validation reports, negative cases, proof linkage, and unresolved failures;
8. public-safe transformation and no-reconstruction review;
9. independent review and finite decision semantics;
10. manifest closure, correction, withdrawal, supersession, and rollback readiness; and
11. governed-interface impact, cache/derivative invalidation, and consumer migration.

### Current automation boundary

The [domain workflow](../../../.github/workflows/domain-settlements-infrastructure.yml) is `CONFIRMED` to use read-only repository permissions and to perform bounded static readiness checks. It explicitly records:

- `WORKFLOW_HOLD: semantic Settlements/Infrastructure validation is not established`;
- `WORKFLOW_HOLD: no accepted Settlements/Infrastructure proof producer or deterministic proof command`; and
- `WORKFLOW_HOLD: no accepted Settlements/Infrastructure release dry-run command or candidate manifest contract`.

The workflow also fails closed if a candidate file appears before the held dry-run is deliberately replaced. Do not add a dossier merely because its Markdown looks complete. Graduate the workflow, validators, fixtures, tests, proof path, policy binding, candidate contract, and release dry run through reviewed changes first.

## Review burden

### Required semantic roles

At minimum, a material candidate should identify review from:

- Settlements / Infrastructure domain steward;
- release steward or release authority;
- data steward;
- evidence and validation reviewer;
- rights and policy/sensitivity reviewer; and
- correction/rollback reviewer when public or semi-public state may change.

Additional cultural/sovereignty, security, critical-infrastructure, emergency/safety, living-person/privacy, land/title, or source-rights review is required when the candidate touches those risks.

The GitHub route in [CODEOWNERS](../../../.github/CODEOWNERS) is `CONFIRMED` as `@bartytime4life` for `release/`. It does not prove that semantic reviewers exist, that independent review occurred, or that separation of duties is enforced. The generator or dossier author must not be treated as the sole approver for a policy-significant release.

## Related folders

| Responsibility | Related location | Relationship |
|---|---|---|
| Candidate parent | [`release/candidates/`](../README.md) | Parent vocabulary and cross-domain candidate index. |
| Short-name compatibility | [`release/candidates/settlement/`](../settlement/README.md) | Compatibility/navigation only; new dossiers route here instead. |
| Release governance | [`release/`](../../README.md) | Root guidance; decisions and manifests outrank this README. |
| Promotion decisions | [`release/promotion_decisions/`](../../promotion_decisions/README.md) | Auditable lifecycle-transition decisions. |
| Manifests | [`release/manifests/`](../../manifests/README.md) | Canonical release-manifest lane. |
| Rollback | [`release/rollback_cards/`](../../rollback_cards/README.md) | Rollback decision and execution planning. |
| Correction | [`release/correction_notices/`](../../correction_notices/README.md) | Public correction lineage. |
| Withdrawal | [`release/withdrawal_notices/`](../../withdrawal_notices/README.md) | Governed withdrawal records. |
| Domain doctrine | [`docs/domains/settlements-infrastructure/`](../../../docs/domains/settlements-infrastructure/README.md) | Domain boundaries, object families, time, lifecycle, and release index. |
| Domain meaning | [`contracts/domains/settlements-infrastructure/`](../../../contracts/domains/settlements-infrastructure/README.md) | Semantic authority for domain objects. |
| Domain shapes | [`schemas/contracts/v1/domains/settlements-infrastructure/`](../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md) | Machine shapes; status must be checked per schema. |
| Domain policy | [`policy/domains/settlements-infrastructure/`](../../../policy/domains/settlements-infrastructure/README.md) | Admissibility and sensitivity posture; current implementation remains bounded. |
| Fixtures | [`fixtures/domains/settlements-infrastructure/`](../../../fixtures/domains/settlements-infrastructure/README.md) | Synthetic validation inputs, not production payloads. |
| Tests | [`tests/domains/settlements-infrastructure/`](../../../tests/domains/settlements-infrastructure/README.md) | Domain guardrails; substantive coverage remains held. |
| Validators | [`tools/validators/domains/settlements-infrastructure/`](../../../tools/validators/domains/settlements-infrastructure/README.md) | Validator lane; executable semantics remain subject to verification. |
| Source registry | [`data/registry/sources/settlements-infrastructure/`](../../../data/registry/sources/settlements-infrastructure/README.md) | Source admission and provenance pointers. |
| Proofs | [`data/proofs/settlements-infrastructure/`](../../../data/proofs/settlements-infrastructure/README.md) | Proof boundary; emitted domain proof objects remain unverified. |
| Published artifacts | [`data/published/settlements-infrastructure/`](../../../data/published/settlements-infrastructure/README.md) | Released public-safe artifacts only; consumers use governed interfaces. |

## ADRs

The following records are relevant but are not accepted or activated by this README:

- [ADR-0010 — Deny-by-Default for DNA, Rare Species, Archaeology, and Critical Infrastructure](../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md): `draft / proposed / number-conflicted`; doctrine supports fail-closed handling, while ADR identity and enforcement remain unresolved.
- [ADR-0018 — Promotion Gate Sequence](../../../docs/adr/ADR-0018-promotion-gate-sequence.md): `proposed`; the gate vocabulary and runtime/CI realization are not treated as accepted enforcement.
- [ADR-0024 — Steward Separation of Duties for Release](../../../docs/adr/ADR-0024-steward-separation-of-duties-for-release.md): `proposed`; role doctrine is informative, while tooling enforcement remains unverified.

The `settlement` versus `settlements-infrastructure` segment remains an ADR-class reconciliation issue recorded by domain doctrine. This README preserves the working long-form lane and the compatibility pointer without claiming authority to rename, alias, migrate, or delete either path.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-22 |
| Evidence boundary | Repository files at pinned commit `640fc2f3c9720cf17d640f0267bf540328e973f0` plus attached Directory Rules PDF and authoring prompt |
| Review status | Draft replacement prepared; semantic and human review pending |
| Next review trigger | First governed dossier, accepted path ADR, substantive validator/test/proof producer, accepted domain dry run, manifest-schema graduation, release decision, correction, withdrawal, or rollback |

## Candidate lifecycle

### Dossier states

These are candidate-management states from the parent lane. They are not policy outcomes, promotion decisions, manifest states, or runtime response outcomes.

| State | Meaning | Advancement posture |
|---|---|---|
| `PROPOSED` | Candidate has a stable identity but closure has not been demonstrated. | Hold. |
| `ASSEMBLING` | Required references and reviews are being gathered. | Hold. |
| `READY_FOR_REVIEW` | The dossier is complete enough for bounded human review. | Review only; not release-ready. |
| `APPROVED_FOR_MANIFEST` | Authorized review supports manifest preparation. | Handoff only; not released. |
| `PROMOTED` | A separate governed release path records the transition. | Verify manifest and public state; never infer from this label alone. |
| `DEFERRED` | Candidate remains in consideration but is not timely or complete. | No public change. |
| `REPAIR_REQUIRED` | A remediable gap blocks progress. | Repair and revalidate. |
| `BLOCKED` | A non-remediated or policy-significant blocker prevents progress. | Fail closed. |
| `WITHDRAWN` | Candidate is no longer under consideration. | Preserve lineage and invalidate affected review assumptions. |
| `SUPERSEDED` | Another candidate replaces this candidate. | Preserve forward/back links and consumer impact. |

### Finite vocabularies must not collapse

| Surface | Vocabulary | Rule |
|---|---|---|
| Candidate dossier | States above | Organizes review; does not authorize transition. |
| `PromotionDecision` | `APPROVE`, `DENY`, `ABSTAIN` | Separate evidence-, policy-, review-, and rollback-bound decision object. |
| Governed runtime | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Public response contract; not a release decision. |
| Validation | `PASS`, `FAIL`, plus explicit hold/error posture where defined | Validation evidence; a pass is not release approval. |

No state transition is automatic. `READY_FOR_REVIEW` does not imply `APPROVED_FOR_MANIFEST`; `APPROVED_FOR_MANIFEST` does not imply `APPROVE`; `APPROVE` does not imply a complete `ReleaseManifest`; a manifest does not imply that every public carrier is activated or safe.

## Canonical candidate dossier contract

Each dossier should be a bounded, reviewable record. Field names below are documentation guidance until a candidate schema is accepted.

| Dossier section | Required content | Fail-closed condition |
|---|---|---|
| Identity | Stable candidate ID, version, domain, owner, creation/update time, immutable dossier digest. | Missing or mutable identity. |
| Scope | Object families, geography, temporal scope, intended public/semi-public surfaces, explicit exclusions. | Unbounded or ambiguous scope. |
| Artifact pointers | Immutable processed/catalog/triplet candidate refs and proposed public-safe targets; no payload copies. | Floating or inaccessible identity; candidate payload stored here. |
| Object identity | Deterministic identity method, object-role separation, external-id mappings, merge/split/supersession rules. | Municipality/census/townsite/settlement/facility roles collapse. |
| Sources | SourceDescriptor refs, source roles, rights/license, retrieval state, currency, authority limits. | Unadmitted source, rights gap, or source-role upcast. |
| Evidence | EvidenceRefs, resolving EvidenceBundles, proof refs, claim-to-evidence coverage, citation validation. | Unresolved ref, missing closure, generated prose used as evidence. |
| Time | Source, observed, valid, retrieval, release, correction, supersession, and stale-state handling as applicable. | Current-state claim without valid-time support. |
| Rights and policy | Policy bundle/decision refs, obligations, restrictions, consent or authority where required. | Missing, stale, ambiguous, or non-reproducible decision. |
| Sensitivity | Classification, exact-harm review, cultural/sovereignty review, critical-infrastructure review, access tier. | Unreviewed exact or reconstructive sensitive detail. |
| Public-safe transforms | Generalization/redaction/aggregation method, digest, receipt, no-reconstruction analysis, residual risk. | Transform not receipted or derivative remains reconstructive. |
| Validation | Schema, identity, geometry, topology, temporal, citation, policy, accessibility, and negative-case results. | Required validator missing, failing, held, or stale. |
| Cross-lane effects | Roads/rail, hydrology, hazards, people/land, archaeology/cultural, graph, map, API, AI, and cache dependencies. | Cross-lane truth reauthored or invalidation impact unknown. |
| Review | Reviewer roles, identities, timestamps, ticket/record refs, conflicts, dissent, separation-of-duties state. | Self-approval or required role absent. |
| Handoff | Proposed PromotionDecision and ReleaseManifest refs/status, included artifact digests, public carrier plan. | Thin/placeholder manifest treated as closure. |
| Reversibility | Correction path, withdrawal conditions, rollback card, supersession lineage, derivative/cache invalidation. | No credible rollback or public correction path. |

### Required dossier assertions

Every dossier should state explicitly:

- what is `CONFIRMED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION`;
- which claims are excluded from the candidate;
- which source role supports each material claim class;
- what temporal slice the candidate represents;
- what a public consumer may and may not infer;
- which exact details were withheld or transformed and why;
- which checks ran, their immutable outputs, and which checks did not run;
- who may approve the next transition and who may not self-approve;
- what remains held; and
- how to correct, withdraw, supersede, and roll back the candidate or its derivatives.

## Release-readiness gates

| Gate | Minimum evidence | Pass condition | Failure outcome |
|---|---|---|---|
| Placement | Directory Rules, working domain segment, authority-root review | Dossier and pointers occupy their proper responsibility roots. | `BLOCKED` / placement review. |
| Candidate identity | Stable ID/version/digest and immutable artifact refs | Candidate can be reproduced and distinguished from predecessors. | `REPAIR_REQUIRED`. |
| Object-family integrity | Contract and identity refs | Legal, census, historic, facility, operator, condition, and dependency roles remain distinct. | `DENY` or `ABSTAIN`. |
| Source admission | SourceDescriptors, roles, rights, retrieval/currency | Every material input is admitted and role-bounded. | Quarantine / `BLOCKED`. |
| Evidence closure | EvidenceRefs, EvidenceBundles, proofs, citation report | Material claims resolve to inspectable evidence. | `ABSTAIN` / hold. |
| Temporal validity | Valid-time and stale-state analysis | The proposed surface cannot imply unsupported currentness. | `ABSTAIN` / repair. |
| Rights and license | Rights record and obligations | Proposed use is permitted and obligations are satisfiable. | `DENY` / quarantine. |
| Sensitivity and exact harm | Policy decision, reviewers, transform receipts | Public output is safe at its released precision and not reconstructive. | `DENY` / restricted hold. |
| Semantic validation | Accepted validators, fixtures, negative cases, reports | Required checks pass with no unresolved hold. | `REPAIR_REQUIRED` / `BLOCKED`. |
| Proof closure | Accepted proof producer and immutable proof refs | Proof objects cover the release-significant assertions and transforms. | `ABSTAIN` / hold. |
| Independent review | Review records and separation state | Required roles reviewed without impermissible self-approval. | `BLOCKED`. |
| Manifest closure | Mature schema, complete manifest, signatures/receipts as required | Included artifacts, evidence, decisions, transforms, consumers, correction, and rollback close. | `ABSTAIN` / no handoff. |
| Public-carrier review | Governed API/map/tile/export/AI/cache inventory | No carrier bypasses release state or reconstructs restricted detail. | `DENY` / no activation. |

The current static domain workflow does not satisfy these gates. Its explicit holds are evidence that the lane is not yet ready for a real dossier or deterministic release dry run.

## Sensitivity and no-leak controls

### Critical infrastructure

- Do not record exact facility locations, service dependencies, network topology, vulnerability context, operational condition, operator-sensitive detail, or continuity-critical relationships in a public dossier.
- Use access-controlled references for restricted material and record only the minimum safe metadata here.
- Generalization, aggregation, redaction, or omission must be policy-authorized, receipted, and tested against reverse reconstruction.
- Absence of a secrecy marking is not evidence that a detail is safe to publish.

### Cultural, sovereignty, archaeology, land, and living-person joins

- Settlement history can intersect missions, forts, reservation communities, sacred or burial sites, archaeological locations, private land, titles, addresses, genealogy, or living persons.
- A public candidate must not expose or infer restricted location, affiliation, ownership, occupancy, or identity through joins, labels, search, map popups, graph edges, screenshots, exports, or AI responses.
- Domain reviewers must cite other lanes through evidence; they must not copy and reauthorize those lanes' truth.

### Public carriers

No map, tile, graph, API, search index, download, screenshot, Focus Mode packet, AI context, or generated narrative may consume this lane directly as public truth. Public carriers bind to governed release state and public-safe artifacts, enforce policy at request time where required, preserve citations and time, and invalidate derivatives after correction, withdrawal, supersession, or rollback.

## Manifest handoff

`APPROVED_FOR_MANIFEST` means only that authorized reviewers support preparing a manifest. Before handoff, require:

- immutable candidate and artifact identities;
- admitted-source and EvidenceBundle closure;
- rights, sensitivity, and policy closure;
- accepted semantic validation and proof outputs;
- public-safe transform receipts and no-reconstruction review;
- independent review records;
- included/excluded artifact inventory;
- governed consumer and carrier inventory;
- correction, withdrawal, supersession, and rollback targets; and
- an explicit statement of all residual `UNKNOWN` and `NEEDS VERIFICATION` items.

The current [`ReleaseManifest` schema](../../../schemas/contracts/v1/release/release_manifest.schema.json) is a `PROPOSED` greenfield stub that requires only `id` and permits additional properties. Passing that schema is not manifest closure. Use the semantic [ReleaseManifest contract](../../../contracts/release/release_manifest.md), governing policy, accepted schemas, validation, signatures/receipts, and human review appropriate to the release.

The paired [`PromotionDecision` contract](../../../contracts/release/promotion_decision.md) and [schema](../../../schemas/contracts/v1/release/promotion_decision.schema.json) require a finite decision plus evidence, EvidenceBundle, policy, rollback, time, and reviewer bindings. Their presence does not prove end-to-end enforcement or authorize public activation.

## Illustrative candidate dossier

> [!NOTE]
> This example is synthetic documentation guidance. It is not a schema-valid record, real candidate, policy decision, review, proof, manifest, or release.

```markdown
# si-example-generalized-historic-place-index-v1

## Status
ASSEMBLING

## Truth posture
- CONFIRMED: candidate identity and bounded source inventory
- PROPOSED: public generalized historic-place index
- NEEDS VERIFICATION: accepted validator, proof producer, policy decision, and manifest contract
- UNKNOWN: public adoption and consumer migration impact

## Scope
- Domain: settlements-infrastructure
- Object families: Settlement, Townsite
- Geography: county-level generalized study area
- Valid time: historical interval stated per assertion
- Intended surface: governed API and map after release only
- Excluded: current facilities, dependencies, operator/condition data, private addresses, living-person joins, cultural/restricted locations

## Immutable pointers
- Candidate artifact: <processed-or-catalog-ref + sha256/spec_hash>
- Proposed public-safe artifact: <target ref + expected digest>

## Evidence, rights, and time
- SourceDescriptor refs: <immutable refs>
- EvidenceBundle refs: <resolving refs>
- Rights/policy refs: <decision refs or HOLD>
- Stale-state rule: <bounded rule>

## Public-safe transformation
- Method: county-level aggregation; exact coordinates omitted
- Receipt: <redaction/generalization receipt ref>
- Reconstruction review: <report ref or HOLD>

## Validation and proof
- Reports: <immutable refs>
- Negative cases: <refs>
- Domain workflow: HELD; no accepted proof producer or release dry run

## Review and handoff
- Required roles: domain, release, data, evidence/validation, rights/sensitivity
- Current recommendation: ABSTAIN
- Manifest handoff: NOT READY

## Correction and rollback
- Correction path: <planned ref>
- Withdrawal condition: <condition>
- Rollback target: <planned ref>
```

## Open verification items

- [ ] Resolve `settlement` versus `settlements-infrastructure` through accepted ADR and migration evidence; preserve the compatibility lane until inbound consumers and rollback are covered.
- [ ] Establish a complete candidate inventory and confirm that no real dossier is present before the held workflow is graduated.
- [ ] Confirm semantic steward assignments and enforce appropriate author/approver separation.
- [ ] Accept candidate naming, ID, digest, and schema conventions.
- [ ] Implement and validate substantive no-network domain tests and validators with public-safe fixtures and negative cases.
- [ ] Establish an accepted deterministic proof producer, proof schemas, validator, and release linkage.
- [ ] Establish an accepted fail-closed domain release-dry-run command and candidate-manifest contract.
- [ ] Graduate the thin ReleaseManifest schema only through contract-, fixture-, validator-, policy-, and compatibility-aware review.
- [ ] Verify rights, sensitivity, critical-infrastructure, cultural/sovereignty, living-person, land, exact-harm, and no-reconstruction enforcement across every public carrier.
- [ ] Establish a governed inventory of released domain artifacts, manifests, corrections, withdrawals, supersessions, rollbacks, caches, and consumers.
- [ ] Synchronize the path conflict with the drift register without treating a registry entry as resolution.

Until these items are closed with evidence, keep candidate advancement fail closed.

## Rollback

Rollback this README revision if it:

- causes this lane to store payloads or trust-bearing records that belong elsewhere;
- implies that the path conflict is resolved or that the working lane is an accepted universal canonical segment;
- turns static readiness checks into semantic, proof, manifest, release, or publication claims;
- weakens evidence, source-role, time, rights, sensitivity, review, correction, withdrawal, or rollback requirements;
- exposes restricted or reconstructive settlement/infrastructure detail; or
- allows a dossier state, PR, merge, deployment, map, or generated summary to stand in for governed release.

Before merge, close the review branch or revert the scoped commits through normal Git history. After merge, use a transparent revert PR that restores the prior README and removes only its paired generated-work receipt if appropriate. Do not rewrite shared history. Reverting this documentation does not resolve the underlying path conflict, remove any independent trust record, or roll back a real release; those actions require their own governed records.
