<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-habitat-habitat-fauna-thin-slice-readme
title: Habitat × Fauna Thin-Slice Release Candidate Review Lane
type: cross-domain-release-candidate-index
version: v2
status: draft; repository-grounded; cross-domain; deny-by-default; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
domain_scope: habitat + fauna
lane_role: cross-domain thin-slice candidate dossier index and sensitive-join pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 527ac01444c23046f0406dbb9e4cf5b2a74cd4cc
  prior_blob: 38cf93f4261e47bb031b88f5477d45915efb730f
  bounded_candidate_inventory: parent README only; no child candidate dossier established
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../manifests/README.md
  - ../../../promotion_decisions/README.md
  - ../../../correction_notices/README.md
  - ../../../rollback_cards/README.md
  - ../../../withdrawal_notices/README.md
  - ../../../changelog/README.md
  - ../../../../docs/domains/habitat/RELEASE_INDEX.md
  - ../../../../docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/fauna/CROSS_LANE_RELATIONS.md
  - ../../../../docs/runbooks/habitat/PROMOTION_RUNBOOK.md
  - ../../../../pipelines/proofs/habitat_fauna_thin_slice/README.md
  - ../../../../schemas/contracts/v1/relations/habitat_fauna/README.md
  - ../../../../schemas/contracts/v1/joins/habitat-fauna-join.schema.json
  - ../../../../fixtures/domains/habitat/habitat_fauna_thin_slice/README.md
  - ../../../../tests/domains/habitat/thin-slice.habitat-fauna.test/README.md
  - ../../../../tests/domains/habitat/test_habitat_fauna_thin_slice.py
  - ../../../../tests/cross_domain/fauna_habitat/README.md
  - ../../../../data/proofs/habitat/README.md
  - ../../../../policy/domains/habitat/README.md
  - ../../../../policy/domains/fauna/README.md
  - ../../../../tools/validators/domains/habitat/README.md
  - ../../../../tools/validators/habitat-fauna/README.md
  - ../../../../tools/validators/geoprivacy/habitat-fauna/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/CODEOWNERS
  - ../../../../.github/workflows/domain-habitat.yml
  - ../../../../.github/workflows/domain-fauna.yml
  - ../../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, habitat, fauna, thin-slice, cross-domain, geoprivacy, evidence, sensitivity, rollback]
notes:
  - "This README indexes Habitat × Fauna thin-slice release-candidate dossiers and defines their public-safe pre-publication review boundary. It is not Habitat truth, Fauna truth, a relation schema, proof result, EvidenceBundle, geoprivacy transform, policy decision, release decision, or publication authority."
  - "The bounded repository search establishes no child candidate dossier under this lane."
  - "The literal sentence 'A candidate is not a release.' is retained as a release-boundary invariant; it is not release proof."
  - "Habitat owns habitat context, patches, suitability, corridors, restoration, stewardship, and related uncertainty. Fauna owns taxon, occurrence, range, status, sensitive-site, and animal-event truth. The relation transfers no ownership."
  - "Cross-domain join products inherit the most restrictive sensitivity of their inputs and fail closed until evidence, policy, geoprivacy, review, release, correction, and rollback support exists."
  - "CODEOWNERS routing is not domain stewardship, sensitivity review, independent approval, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/habitat/habitat_fauna_thin_slice/` — Habitat × Fauna Thin-Slice Release Candidate Review Lane

> Index public-safe review dossiers for the Habitat × Fauna thin slice, preserve cross-domain ownership and blockers, and prevent habitat context, fauna evidence, relation projections, proof-harness output, generalized derivatives, or generated explanations from being treated as occurrence truth, habitat truth, policy clearance, proof closure, or release authority before evidence, rights, sensitivity, geoprivacy, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![scope](https://img.shields.io/badge/scope-habitat%20%C3%97%20fauna-2E7D32)
![lane](https://img.shields.io/badge/lane-thin--slice-blueviolet)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![sensitivity](https://img.shields.io/badge/sensitivity-most--restrictive%20wins-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@527ac014…`:** bounded repository search establishes this README as the only directly indexed file under `release/candidates/habitat/habitat_fauna_thin_slice/`. No child candidate dossier, candidate payload, executable proof harness, verified fixture payload, executable thin-slice test suite, accepted relation schema, emitted EvidenceBundle, PromotionDecision, ReleaseManifest, or public Habitat × Fauna artifact was established. The Habitat release index contains an explicitly illustrative thin-slice row, not evidence that a release exists.
>
> Differently named, unindexed, generated, history-only, external, restricted-system, or runtime-only material remains **UNKNOWN** until directly verified.

## Quick navigation

[Purpose](#purpose) ·
[Status](#status-and-evidence-boundary) ·
[Authority](#authority-and-repository-fit) ·
[Inventory](#current-candidate-inventory) ·
[Lifecycle](#candidate-lifecycle) ·
[Contents](#what-belongs-here) ·
[Exclusions](#what-does-not-belong-here) ·
[Admission](#candidate-admission-contract) ·
[Ownership](#domain-ownership-and-relation-identity) ·
[Anti-collapse](#cross-domain-anti-collapse) ·
[Sensitivity](#sensitivity-geoprivacy-and-public-safe-representation) ·
[Sources and time](#source-role-evidence-time-and-stale-state) ·
[Gates](#thin-slice-release-gates) ·
[Dossier](#required-dossier-structure) ·
[Validation](#validation-proof-fixture-schema-and-policy-posture) ·
[Automation](#automation-posture) ·
[Handoff](#review-and-release-handoff) ·
[Correction](#correction-withdrawal-supersession-and-rollback) ·
[Public boundary](#public-api-map-export-graph-and-ai-boundary) ·
[Maintenance](#maintenance-and-definition-of-done) ·
[Evidence](#evidence-ledger) ·
[Open items](#open-verification) ·
[Rollback](#rollback-for-this-readme)

---

## Purpose

`release/candidates/habitat/habitat_fauna_thin_slice/` is a cross-domain, pre-publication review lane beneath the Habitat candidate namespace and the `release/` responsibility root.

It exists to answer bounded questions:

1. Which Habitat × Fauna thin-slice candidate dossiers are currently indexed?
2. What Habitat-owned objects, Fauna-owned objects, and neutral relation records are in scope?
3. Which admitted sources, source roles, rights, evidence, sensitivity, policy, validation, and review records support the proposed output?
4. Does the candidate preserve domain ownership, model-versus-observation distinctions, and the most-restrictive sensitivity rule?
5. Does the public representation prevent direct or inferential exposure of sensitive fauna context?
6. Does every consequential claim resolve through evidence or return a finite non-answer?
7. Which shared release record owns the next governed state transition?
8. Can every public derivative be corrected, withdrawn, superseded, and rolled back without restoring unsafe material?

**A candidate is not a release.**

A dossier in this lane is a review packet. It does not create an active relation, proof result, EvidenceBundle, public-safe transform, PolicyDecision, PromotionDecision, ReleaseManifest, published layer, or governed API authority.

The lifecycle boundary remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Cross-domain composition does not bypass either domain's lifecycle. Promotion is a governed state transition, not a file move, proof pass, schema validation, fixture success, branch merge, map render, graph projection, or generated narrative.

[Back to top](#top)

---

## Status and evidence boundary

| Question | Repository-grounded answer |
|---|---|
| Does this path exist? | **CONFIRMED.** |
| Does the direct lane contain a child candidate dossier? | **No verified child dossier surfaced in bounded indexed search.** |
| Is an active Habitat × Fauna candidate established? | **No.** |
| Is the proof-harness lane present? | **Yes, as a draft README.** Concrete executable behavior remains unverified. |
| Are thin-slice fixture payloads established? | **No verified payload inventory.** The fixture README states none were verified. |
| Are executable thin-slice tests established? | **No.** The dedicated test lane is README-backed; the direct Habitat test module is a one-line `PROPOSED` placeholder. |
| Is an accepted relation schema established? | **No.** The relation lane is README-only; the existing join schema is a permissive scaffold with empty properties. |
| Are EvidenceBundles or proof outputs emitted for this slice? | **No verified inventory.** |
| Are Habitat and Fauna policy bundles executable? | **Not established.** Both domain policy READMEs remain greenfield scaffolds. |
| Is a thin-slice release established? | **No.** The Habitat release-index row is explicitly illustrative. |
| Is release automation established? | **No.** Domain workflows are maturity checks; the general release dry run is TODO-only. |

### Truth labels used here

- **CONFIRMED** — verified from current repository files, workflow definitions, comparisons, or generated artifacts in this session.
- **PROPOSED** — intended behavior, contract, field, placement, or control not established as implemented.
- **UNKNOWN** — not verified strongly enough to make a claim.
- **NEEDS VERIFICATION** — checkable, but not sufficiently checked or accepted.
- **CONFLICTED** — repository evidence exposes incompatible or unresolved paths, vocabularies, or authority descriptions.
- **LINEAGE** — historically useful planning or documentation evidence that is not current implementation proof.

This README does not turn a planned thin slice into an implementation claim.

[Back to top](#top)

---

## Authority and repository fit

### Directory Rules basis

The requested path already exists under `release/`, the responsibility root for candidate review and release decisions:

```text
release/
└── candidates/
    └── habitat/
        └── habitat_fauna_thin_slice/
            └── README.md
```

This placement may index a review packet. It must not absorb the authorities that own Habitat, Fauna, relations, schemas, proof orchestration, policy, lifecycle data, or public artifacts.

| Responsibility | Owning path | Relationship to this lane |
|---|---|---|
| Habitat candidate parent | [`../README.md`](../README.md) | Parent candidate orientation and shared Habitat release boundary. |
| Cross-domain candidate guidance | [`../../README.md`](../../README.md) | Candidate-family guidance. |
| Release authority | [`../../../README.md`](../../../README.md) and shared release record lanes | Owns promotion, manifest, correction, withdrawal, and rollback objects. |
| Habitat release mirror | [`docs/domains/habitat/RELEASE_INDEX.md`](../../../../docs/domains/habitat/RELEASE_INDEX.md) | Navigational mirror; its thin-slice row is illustrative. |
| Habitat sensitivity profile | [`docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md`](../../../../docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md) | Profiles join-induced sensitivity; not policy enforcement. |
| Fauna relation doctrine | [`docs/domains/fauna/CROSS_LANE_RELATIONS.md`](../../../../docs/domains/fauna/CROSS_LANE_RELATIONS.md) | Defines ownership-preserving relation posture. |
| Habitat promotion procedure | [`docs/runbooks/habitat/PROMOTION_RUNBOOK.md`](../../../../docs/runbooks/habitat/PROMOTION_RUNBOOK.md) | Draft operational guidance; not implementation proof. |
| Proof orchestration | [`pipelines/proofs/habitat_fauna_thin_slice/`](../../../../pipelines/proofs/habitat_fauna_thin_slice/README.md) | Proposed executable proof harness; does not own proof data or release. |
| Relation-schema guardrail | [`schemas/contracts/v1/relations/habitat_fauna/`](../../../../schemas/contracts/v1/relations/habitat_fauna/README.md) | README-only relation placement guardrail. |
| Existing join scaffold | [`schemas/contracts/v1/joins/habitat-fauna-join.schema.json`](../../../../schemas/contracts/v1/joins/habitat-fauna-join.schema.json) | Permissive proposed scaffold; not safety proof. |
| Synthetic fixtures | [`fixtures/domains/habitat/habitat_fauna_thin_slice/`](../../../../fixtures/domains/habitat/habitat_fauna_thin_slice/README.md) | Intended public-safe fixture support; no verified payload inventory. |
| Thin-slice tests | [`tests/domains/habitat/thin-slice.habitat-fauna.test/`](../../../../tests/domains/habitat/thin-slice.habitat-fauna.test/README.md) | Test-lane guidance; no verified executable modules. |
| Cross-domain tests | [`tests/cross_domain/fauna_habitat/`](../../../../tests/cross_domain/fauna_habitat/README.md) | Adjacent cross-domain verification guidance. |
| Habitat proof support | [`data/proofs/habitat/`](../../../../data/proofs/habitat/README.md) | Proof-data support; implementation depth remains unknown. |
| Habitat policy | [`policy/domains/habitat/`](../../../../policy/domains/habitat/README.md) | Policy authority home; current README is a scaffold. |
| Fauna policy | [`policy/domains/fauna/`](../../../../policy/domains/fauna/README.md) | Policy authority home; current README is a scaffold. |
| Habitat validators | [`tools/validators/domains/habitat/`](../../../../tools/validators/domains/habitat/README.md) | Validator index; accepted thin-slice command not established. |
| Cross-domain validators | [`tools/validators/habitat-fauna/`](../../../../tools/validators/habitat-fauna/README.md) | Cross-domain validator guidance. |
| Geoprivacy validators | [`tools/validators/geoprivacy/habitat-fauna/`](../../../../tools/validators/geoprivacy/habitat-fauna/README.md) | Geoprivacy validation guidance. |

### Authority boundary

This lane may record candidate state, blockers, and public-safe pointers. It must not:

- define Habitat or Fauna semantic truth;
- transfer object ownership between domains;
- admit or activate a source;
- establish a relation schema;
- execute or certify the proof harness;
- create an EvidenceBundle or proof pack;
- select or reveal geoprivacy parameters;
- decide policy, sensitivity tier, or reviewer authority;
- declare a sensitive occurrence public-safe;
- create a PromotionDecision or ReleaseManifest;
- publish, correct, withdraw, supersede, or roll back an artifact.

[Back to top](#top)

---

## Current candidate inventory

### Direct inventory

| Candidate | Status | Evidence | Public effect |
|---|---|---|---|
| _None established_ | `NO_ACTIVE_CANDIDATE` | Bounded indexed search surfaced this README only in the direct lane. | None |

The parent Habitat candidate README names this sublane. Naming a sublane is not creating a candidate.

### Adjacent planning and guidance

| Surface | Current posture | Why it is not a candidate |
|---|---|---|
| Proof-harness README | Draft / proposed executable lane | It defines intended proof orchestration, not a candidate artifact. |
| Fixture README | Draft / no verified payloads | Fixtures are examples, not release units. |
| Thin-slice test README | Draft / no verified executable modules | Tests prove bounded behavior; they do not create candidate state. |
| Direct test module | One-line proposed placeholder | No test function or candidate payload. |
| Relation README | README-only guardrail | Placement guidance, not a relation instance. |
| Join schema | Empty properties; `additionalProperties: true` | Shape scaffold, not safety, semantics, or release evidence. |
| Habitat release-index row | Explicitly illustrative | The document says not to treat it as evidence that a release exists. |

### Inventory limits

The inventory does not prove the absence of ignored, generated, history-only, external, restricted, runtime-only, local-only, or differently named material. Such material remains **UNKNOWN** until directly inspected and admitted.

### Empty-lane behavior

When no candidate exists:

- do not invent a candidate ID;
- do not promote an illustrative release-index row into fact;
- do not treat a fixture, proof plan, test placeholder, relation schema, graph edge, or generated receipt as a candidate;
- keep automation in an explicit hold posture;
- keep public clients on released governed surfaces only;
- report `NO_ACTIVE_CANDIDATE`, `ABSTAIN`, `DENY`, `HOLD`, or another accepted finite non-release outcome.

[Back to top](#top)

---

## Candidate lifecycle

A finite candidate state vocabulary should include:

| State | Meaning | Public effect |
|---|---|---|
| `PROPOSED` | A public-safe dossier shell exists; admission is incomplete. | None |
| `ASSEMBLING` | Cross-domain pointers and support records are being collected. | None |
| `READY_FOR_REVIEW` | Required fields are present for bounded review. | None |
| `RESTRICTED_REVIEW` | Review requires non-public evidence or sensitive-fauna context. | None |
| `BLOCKED` | A hard gate is unresolved or failed. | None |
| `STALE` | Source, evidence, policy, review, or relation freshness exceeded tolerance. | None |
| `REPAIR_REQUIRED` | The candidate can continue only after documented correction. | None |
| `DEFERRED` | Review intentionally paused without approval. | None |
| `APPROVED_FOR_MANIFEST` | Independent review permits manifest preparation; release has not occurred. | None |
| `PROMOTED` | Separate accepted PromotionDecision and ReleaseManifest establish release state. | Governed downstream effect only |
| `SUPERSEDED` | A newer governed candidate or release replaces it. | Historical only |
| `WITHDRAWN` | Candidate removed from consideration. | None |

`PROMOTED` cannot be set by editing a README.

### Explicit hold outcomes

Use the narrowest applicable hold:

- `HOLD_FOR_CANDIDATE_IDENTITY`
- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_HABITAT_SCOPE`
- `HOLD_FOR_FAUNA_SCOPE`
- `HOLD_FOR_RELATION_CONTRACT`
- `HOLD_FOR_DOMAIN_OWNERSHIP`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_SOURCE_ROLE`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_TIME`
- `HOLD_FOR_SENSITIVITY`
- `HOLD_FOR_GEOPRIVACY`
- `HOLD_FOR_PUBLIC_SAFE_REPRESENTATION`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_PROOF`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_CATALOG_CLOSURE`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`

[Back to top](#top)

---

## What belongs here

This lane may contain public-safe, pointer-based review material:

- child candidate dossier READMEs;
- compact candidate indexes after a producer and schema are accepted;
- stable candidate identity and version notes;
- immutable pointers and digests for processed or staged artifacts;
- Habitat-owned scope summaries;
- Fauna-owned scope summaries;
- neutral relation scope and relation-contract references;
- source, rights, evidence, sensitivity, policy, validation, proof, review, catalog, correction, and rollback pointers;
- public-safe representation and audience summaries;
- geoprivacy review state without transform secrets or reverse-engineering aids;
- explicit finite outcomes and blockers;
- handoff notes to shared release record lanes.

A dossier should reference trust objects, not duplicate them.

[Back to top](#top)

---

## What does not belong here

| Excluded material | Correct authority home |
|---|---|
| Habitat or Fauna RAW source payloads | owning `data/raw/` lanes |
| WORK, QUARANTINE, or PROCESSED payloads | owning lifecycle lanes |
| Sensitive occurrence geometry, site records, or re-identification keys | restricted Fauna lifecycle/evidence systems |
| Habitat patches, models, corridors, or uncertainty payloads | Habitat lifecycle lanes |
| Fauna taxon, occurrence, range, status, mortality, disease, or invasive records | Fauna lifecycle lanes |
| Relation instances or graph/triplet projections | accepted relation, catalog, or triplet lanes |
| Semantic contracts or JSON Schemas | `contracts/` and `schemas/` |
| Proof-harness code | `pipelines/proofs/habitat_fauna_thin_slice/` |
| Fixtures, tests, or validator code | `fixtures/`, `tests/`, and `tools/validators/` |
| SourceDescriptor or activation records | source-registry lanes |
| EvidenceBundle, ProofPack, ValidationReport, or receipts | proof and receipt lanes |
| Policy rules or sensitivity decisions | `policy/` and accepted decision-record homes |
| PMTiles, GeoJSON, GeoParquet, APIs, exports, screenshots, or dashboards | released public carrier lanes after promotion |
| PromotionDecision, ReleaseManifest, CorrectionNotice, WithdrawalNotice, or RollbackCard | shared `release/` record lanes |
| Credentials, private review substance, or protected-location detail | approved restricted systems |
| AI text presented as evidence, policy, proof, or approval | governed AI output with citations and finite status only |

[Back to top](#top)

---

## Candidate admission contract

A child dossier must not enter `READY_FOR_REVIEW` until all consequential fields are explicit or blocked.

### Candidate identity

- stable `candidate_id`;
- candidate version and digest;
- owner and review contacts;
- creation, update, and supersession times;
- finite candidate state;
- target audience classes;
- proposed artifact and release family.

### Habitat scope

- Habitat object references and versions;
- object families such as patch, ecological system, land-cover context, suitability, corridor, restoration, stewardship, or uncertainty;
- source roles;
- model identity, version, assumptions, and uncertainty where modeled;
- geometry, scale, time, and release state;
- EvidenceRef pointers;
- explicit statement that Habitat context is not Fauna occurrence truth.

### Fauna scope

- Fauna reference types;
- taxon/occurrence/range/status authority owner;
- source roles;
- sensitivity and precision posture;
- time and evidence state;
- steward-controlled or restricted status;
- public-safe derivative reference, when one exists;
- explicit statement that Fauna evidence is not a Habitat object.

### Relation identity

- stable relation ID and relation version;
- relation type;
- Habitat reference;
- Fauna reference;
- direction and cardinality;
- relation time/season;
- derivation method;
- confidence and uncertainty;
- source-role preservation;
- evidence support;
- sensitivity result;
- correction and rollback lineage.

### Artifact identity

- immutable artifact pointer;
- artifact format and digest;
- producer/run/spec identifiers;
- proposed public target;
- object and relation counts where safe;
- candidate-manifest reference when accepted;
- no direct pointer to restricted source material.

### Rights, evidence, and review

- admitted SourceDescriptor references;
- rights and derivative-use posture;
- EvidenceRef-to-EvidenceBundle resolution;
- validation and proof refs;
- PolicyDecision and obligations;
- Habitat steward review;
- Fauna steward review;
- sensitivity/geoprivacy review;
- independent release review when material.

### Public representation

- public audience;
- public-safe geometry reference;
- permitted fields;
- excluded internal fields and join keys;
- aggregation/generalization/redaction receipt refs;
- safe evidence resolver keys;
- stale/correction state;
- proof that public clients cannot recover restricted inputs.

### Release support

- catalog closure;
- proposed PromotionDecision target;
- proposed ReleaseManifest target;
- correction notice target;
- withdrawal target;
- rollback target;
- derivative invalidation plan.

Missing support blocks review rather than being guessed.

[Back to top](#top)

---

## Domain ownership and relation identity

### Ownership lattice

| Concern | Owning lane | Thin-slice behavior |
|---|---|---|
| Habitat patch, class, ecological system, suitability, connectivity, corridor, restoration, stewardship, uncertainty | Habitat | Reference the Habitat object; do not copy it into Fauna authority. |
| Taxon, occurrence, range, status, sensitive site, animal mortality/disease/invasive record | Fauna | Reference the Fauna object or approved derivative; do not copy it into Habitat authority. |
| Habitat assignment or seasonal-support relation | Neutral cross-domain relation | Preserve both owners, evidence, sensitivity, and release state. |
| Source admission | Source registry | Candidate references admitted records. |
| Evidence | EvidenceBundle/proof lane | Candidate resolves pointers; it does not author root evidence. |
| Sensitivity and policy | Policy/review lanes | Candidate records outcomes and obligations. |
| Release | Shared release lanes | Candidate hands off; it does not approve itself. |

### Relation identity tuple

A relation should be identified by at least:

```text
relation_type
+ habitat_ref
+ fauna_ref
+ relation_version
+ valid_time_or_season
+ derivation_method
+ evidence_bundle_ref
```

A co-location, overlap, model score, shared polygon, or graph edge is not automatically a valid relation.

### Relation direction

Fauna relation doctrine states that Fauna may cite released, public-safe Habitat context to support habitat assignment or seasonal-support claims. Habitat remains the owner of patch and suitability truth; Fauna remains the owner of occurrence and taxon truth.

A relation record must preserve:

- owner of each endpoint;
- relation direction;
- source role of each endpoint;
- sensitivity of each endpoint;
- relation evidence;
- uncertainty and time;
- release state of each referenced public surface.

[Back to top](#top)

---

## Cross-domain anti-collapse

The candidate must keep these distinctions explicit:

| Material | Must not become |
|---|---|
| Habitat context | Fauna occurrence or taxon truth |
| Fauna occurrence | Habitat patch, suitability, corridor, or restoration truth |
| Suitability model | Observed occurrence |
| Range polygon | Exact occurrence |
| Candidate corridor | Regulatory habitat authority |
| Habitat assignment relation | Transfer of endpoint ownership |
| Generalized derivative | Unrestricted source geometry |
| Redaction/generalization result | Release approval |
| Proof-harness pass | EvidenceBundle or release approval |
| Fixture success | Live-data truth |
| Schema validation | Semantic validity, policy safety, or release readiness |
| Join schema | Accepted relation contract |
| Graph/triplet projection | Canonical truth |
| Catalog record | Evidence closure or release |
| AI or UI summary | Source, evidence, policy, or release authority |
| Candidate state | Published state |

### Source-role anti-collapse

Preserve the accepted source-role vocabulary and source-specific authority limits. Do not upgrade:

- modeled to observed;
- aggregate to per-record;
- candidate to admitted;
- administrative or regulatory to occurrence;
- contextual use to source authority;
- synthetic fixtures to live evidence.

Older documents use terms such as `context`, `authority`, and `model`. These may describe use or authority scope, but they must not be silently inserted into a canonical role field unless accepted by the governing source-role contract.

[Back to top](#top)

---

## Sensitivity, geoprivacy, and public-safe representation

### Most-restrictive sensitivity rule

The resulting product inherits the most restrictive sensitivity of its inputs and joins.

A public Habitat object joined to a restricted Fauna record is restricted by default. The exact join result does not become public merely because a generalized derivative may be reviewable.

### Fail-closed surfaces

Apply the sensitivity decision to every observable surface:

- geometry;
- properties and internal IDs;
- relation endpoints;
- tiles and metadata;
- APIs and exports;
- caches and indexes;
- graph edges;
- Evidence Drawer payloads;
- logs and error messages;
- screenshots and reports;
- AI-generated summaries.

### Public-safe derivative requirements

A public candidate requires:

- a named, reviewed representation profile;
- a public-safe derivative distinct from the restricted original;
- receipts for aggregation, generalization, suppression, or redaction where required;
- Habitat and Fauna steward review;
- PolicyDecision and audience obligations;
- no-leak tests;
- safe field allowlists;
- correction and rollback linkage;
- proof that public outputs cannot reconstruct the protected input at an unacceptable level.

This public README must not disclose transform seeds, offsets, thresholds, masks, hidden buffers, internal precision rules, protected identifiers, or other reversal aids.

### Sensitivity is product-specific

A source record, Habitat patch, or range surface may be public in isolation while the joined product is restricted. Review the **resulting product**, not just each input.

### No laundering by aggregation or rendering

Aggregation, map tiling, styling, clipping, or AI paraphrase does not make sensitive content safe by itself. The transform must be governed, receipted, reviewed, and validated.

[Back to top](#top)

---

## Source role, evidence, time, and stale state

### Source closure

Every input must resolve:

- source identity;
- canonical role;
- authority scope;
- rights and terms;
- retrieval/source-head state;
- cadence and stale tolerance;
- citation;
- activation/admission state;
- correction and withdrawal state.

### Evidence closure

Every consequential claim must resolve:

```text
EvidenceRef -> EvidenceBundle
```

Missing, incomplete, revoked, inaccessible, or mismatched evidence produces `ABSTAIN`, `HOLD`, `DENY`, or `ERROR` according to the accepted contract. Generated language cannot fill the gap.

### Time kinds

Keep these time kinds distinct where material:

| Time | Meaning |
|---|---|
| `habitat_valid_time` | When Habitat context applies. |
| `fauna_observed_or_valid_time` | When Fauna evidence applies. |
| `relation_valid_time` | When the relation is asserted to apply. |
| `source_time` | Source edition/publication time. |
| `retrieval_time` | When KFM captured the source. |
| `processing_time` | When inputs or relation candidates were produced. |
| `candidate_time` | When the dossier was assembled. |
| `release_time` | When a separate release decision took effect. |
| `correction_time` | When public posture changed. |

A habitat assignment is not timeless. Seasonal, migratory, breeding, hydrologic, land-cover, model, and source-vintage differences must remain visible.

### Stale-state rules

A candidate becomes `STALE` when:

- a Habitat or Fauna source exceeds cadence;
- a model, patch, range, or occurrence derivative is superseded;
- relation evidence no longer resolves;
- policy or rights change;
- an upstream correction invalidates an endpoint;
- a public-safe transform profile is withdrawn;
- review expires;
- release or rollback targets no longer resolve.

Stale is not the same as wrong, but stale candidates do not remain release-ready silently.

[Back to top](#top)

---

## Thin-slice release gates

A candidate cannot advance to `APPROVED_FOR_MANIFEST` until all applicable gates close.

| Gate | Minimum support | Fail-closed outcome |
|---|---|---|
| Candidate identity | Stable ID, version, owner, digest, state | `HOLD_FOR_CANDIDATE_IDENTITY` |
| Artifact identity | Immutable pointer, digest, format, target | `HOLD_FOR_ARTIFACT` |
| Habitat scope | Habitat refs, object families, roles, time, evidence | `HOLD_FOR_HABITAT_SCOPE` |
| Fauna scope | Fauna refs, authority, sensitivity, time, evidence | `HOLD_FOR_FAUNA_SCOPE` |
| Relation contract | Relation type, direction, cardinality, version, semantics | `HOLD_FOR_RELATION_CONTRACT` |
| Domain ownership | Both endpoint owners remain explicit | `HOLD_FOR_DOMAIN_OWNERSHIP` |
| Source admission | Admitted descriptors and activation state | `HOLD_FOR_SOURCE_ADMISSION` |
| Source role | Accepted role without authority upgrade | `HOLD_FOR_SOURCE_ROLE` |
| Rights | Terms, attribution, redistribution, derivative use | `HOLD_FOR_RIGHTS` |
| Evidence | Consequential claims resolve to EvidenceBundle | `HOLD_FOR_EVIDENCE` |
| Time | Endpoint and relation time support; stale posture | `HOLD_FOR_TIME` |
| Sensitivity | Resulting-product tier and audience resolved | `HOLD_FOR_SENSITIVITY` |
| Geoprivacy | Reviewed derivative and required receipts | `HOLD_FOR_GEOPRIVACY` |
| Public representation | Fields, geometry, metadata, logs, exports are safe | `HOLD_FOR_PUBLIC_SAFE_REPRESENTATION` |
| Policy | Accepted finite policy result and obligations | `HOLD_FOR_POLICY` |
| Validation | Deterministic semantic/schema/ownership/no-leak checks | `HOLD_FOR_VALIDATION` |
| Proof | Governed proof results and references | `HOLD_FOR_PROOF` |
| Catalog closure | Catalog/provenance refs resolve | `HOLD_FOR_CATALOG_CLOSURE` |
| Review | Habitat, Fauna, sensitivity, evidence, release reviewers | `HOLD_FOR_REVIEW` |
| Correction | Derivative inventory and invalidation route | `HOLD_FOR_CORRECTION_PATH` |
| Rollback | Verified prior target or safe withdrawal | `HOLD_FOR_ROLLBACK` |
| Release topology | PromotionDecision and ReleaseManifest homes resolved | `HOLD_FOR_RELEASE_TOPOLOGY` |

No passing proof, schema, test, or review substitutes for another gate.

[Back to top](#top)

---

## Required dossier structure

A child candidate dossier should remain public-safe and pointer-based.

```markdown
# <candidate title>

## KFM metadata
- candidate_id:
- candidate_version:
- owner:
- state:
- created_at:
- updated_at:
- supersedes:
- digest:

## Candidate artifact
- artifact_ref:
- artifact_sha256:
- producer_ref:
- proof_run_ref:
- proposed_public_targets:
- audience_classes:

## Habitat scope
- habitat_refs:
- habitat_object_families:
- habitat_source_roles:
- habitat_time_scope:
- habitat_evidence_refs:
- habitat_release_refs:
- habitat_uncertainty:

## Fauna scope
- fauna_refs:
- fauna_reference_types:
- fauna_source_roles:
- fauna_time_scope:
- fauna_evidence_refs:
- fauna_sensitivity_posture:
- fauna_public_derivative_refs:

## Relation
- relation_id:
- relation_type:
- direction:
- cardinality:
- relation_version:
- valid_time_or_season:
- derivation_method:
- confidence:
- uncertainty:
- relation_evidence_refs:

## Rights and sources
- source_descriptor_refs:
- activation_refs:
- rights_state:
- attribution:
- redistribution_state:
- stale_after:

## Sensitivity and public representation
- resulting_sensitivity:
- audience:
- public_safe_representation_ref:
- geoprivacy_receipt_refs:
- field_allowlist_ref:
- excluded_fields:
- no_leak_validation_refs:
- reconstruction_risk:

## Evidence, validation, proof, and catalog
- evidence_bundle_refs:
- validation_report_refs:
- proof_refs:
- receipt_refs:
- catalog_refs:
- finite_outcomes:
- blockers:

## Policy and review
- policy_decision_ref:
- obligations:
- habitat_review_ref:
- fauna_review_ref:
- sensitivity_review_ref:
- evidence_review_ref:
- independent_release_review_ref:

## Release handoff
- promotion_decision_target:
- release_manifest_target:
- published_artifact_target:
- correction_notice_target:
- withdrawal_notice_target:
- rollback_card_target:

## Decision
- recommendation:
- reason_codes:
- unresolved_items:
```

This template is **PROPOSED** until accepted contracts and schemas exist. It does not authorize candidate-local copies of shared release records.

[Back to top](#top)

---

## Validation, proof, fixture, schema, and policy posture

### Current repository posture

| Surface | Confirmed evidence | Current limit |
|---|---|---|
| Candidate lane | This README exists; no child dossier surfaced | No active candidate established |
| Habitat release index | Thin-slice row exists | Row is explicitly illustrative |
| Habitat sensitivity profile | Detailed draft exists | Profiles doctrine; does not enforce policy |
| Fauna cross-lane register | Detailed draft exists | Repo embodiment remains proposed |
| Proof-harness lane | Detailed README exists | Concrete executable behavior and CI remain unverified |
| Fixture lane | Detailed README exists | Its inventory says no payload files were verified |
| Dedicated test lane | Detailed README exists | No executable modules verified |
| Direct Habitat test module | One-line proposed placeholder | No test behavior |
| Relation-schema lane | README-only guardrail | No direct relation schema files established |
| Join schema | Proposed scaffold with empty properties and permissive extras | Cannot establish meaning, safety, or completeness |
| Habitat proof lane | Draft proof guidance | Implementation depth remains unknown |
| Habitat policy | Greenfield scaffold | No executable policy proof |
| Fauna policy | Greenfield scaffold | No executable policy proof |
| Habitat validators | Index plus placeholder modules | Accepted thin-slice command not established |
| Domain workflows | Maturity detectors and explicit holds | Not candidate validation or release proof |
| General release dry run | TODO echo jobs | Not assembly, gate enforcement, or rollback proof |

### Minimum positive cases

Future deterministic tests should prove:

- Habitat and Fauna endpoint ownership remains distinct;
- a synthetic relation carries stable refs, direction, time, source roles, evidence, sensitivity, and uncertainty;
- EvidenceRef resolves to fixture EvidenceBundle support;
- policy returns a finite result;
- a reviewed public-safe derivative omits restricted fields and geometry;
- public clients access released carriers rather than lifecycle stores;
- correction and rollback references resolve;
- proof output remains separate from release approval.

### Minimum negative cases

Future tests should fail closed when:

- either endpoint owner is missing;
- Habitat context is presented as Fauna occurrence truth;
- Fauna evidence is presented as a Habitat object;
- modeled suitability is labeled observed occurrence;
- a range polygon is treated as an exact observation;
- relation direction or cardinality is ambiguous;
- source role is missing or upgraded;
- EvidenceBundle support is missing;
- endpoint times are incompatible or stale;
- sensitive fauna context reaches a public output;
- internal IDs, join keys, or hidden fields leak through tiles, metadata, logs, or exports;
- a public derivative lacks required receipts or review;
- the proof harness reads RAW, WORK, QUARANTINE, or direct source APIs;
- fixture or schema success is treated as proof closure;
- proof success is treated as release approval;
- release, correction, withdrawal, or rollback references are absent;
- generated summaries create unsupported relation claims.

### Permissive schema warning

The current join scaffold has empty `properties` and permits additional properties. Passing it cannot establish:

- endpoint ownership;
- relation semantics;
- evidence closure;
- sensitivity;
- geoprivacy;
- time compatibility;
- policy;
- review;
- release readiness.

[Back to top](#top)

---

## Automation posture

### Domain workflows

The Habitat and Fauna workflows are repository-maturity checks. They inspect required boundaries and look for signals that tests, validators, proof producers, or candidate records have appeared.

Their green held outcomes mean only that documented assumptions remain true. Their failures may indicate that repository maturity detectors require deliberate graduation. Neither outcome proves this candidate is valid, safe, or released.

### Habitat workflow detector boundary

The current Habitat workflow:

- AST-inspects Habitat tests for collected test nodes;
- AST/content-inspects several Habitat and Habitat–Fauna validator roots;
- checks for accepted Make targets;
- holds proof production when no accepted producer is wired;
- holds release dry-run behavior when no accepted candidate record or command is wired.

Existing placeholder files and evolving validator/test inventories must be evaluated deliberately. Do not suppress detector failures merely to make documentation green.

### Fauna workflow boundary

The Fauna workflow independently protects Fauna-owned evidence and sensitive-location posture. Habitat approval cannot satisfy Fauna gates.

### General release dry run

The general `release-dry-run` jobs currently execute TODO echo steps. Green results are not candidate assembly, promotion enforcement, rollback verification, or release proof.

### Watchers, AI, and generators

A watcher or generator may propose a source, relation, evidence, or stale-state change. It must not:

- activate a source;
- decide a relation is true;
- lower sensitivity;
- choose hidden geoprivacy parameters;
- mark a candidate approved;
- promote or publish;
- silently update correction or rollback state.

[Back to top](#top)

---

## Review and release handoff

### Required review roles

A mature thin-slice candidate may require:

- Habitat domain steward;
- Fauna domain steward;
- cross-domain relation steward;
- source and rights steward;
- evidence/proof reviewer;
- sensitivity and geoprivacy reviewer;
- policy steward;
- validation/QA steward;
- map/API/export reviewer;
- release steward;
- independent approver where materiality warrants separation of duties.

CODEOWNERS routing does not prove any of those reviews occurred.

### Separation of duties

At minimum:

- candidate author does not self-approve release;
- proof producer does not convert proof pass into policy clearance;
- domain steward does not override another domain's ownership;
- sensitivity reviewer does not silently change source geometry;
- release authority verifies the manifest, rollback target, and review record;
- public client maintainers consume only released governed surfaces.

### Handoff routing

| Review result | Next authority lane |
|---|---|
| Candidate needs repair | Owning Habitat/Fauna lifecycle lanes plus this dossier |
| Candidate blocked | This dossier with explicit hold and reason codes |
| Candidate approved for promotion review | `release/promotion_decisions/` |
| Candidate approved for manifest assembly | `release/manifests/` |
| Public artifacts emitted after release | accepted released Habitat/Fauna/cross-domain carrier lanes |
| Correction required | `release/correction_notices/` |
| Withdrawal required | `release/withdrawal_notices/` |
| Rollback required | `release/rollback_cards/` |
| Release history update | `release/changelog/` |

Candidate-local release objects create parallel authority unless an accepted ADR or migration explicitly permits them.

[Back to top](#top)

---

## Correction, withdrawal, supersession, and rollback

### Correction triggers

Correction review is required when:

- endpoint ownership is wrong;
- a Habitat or Fauna source is corrected, withdrawn, or superseded;
- relation direction, cardinality, method, confidence, or time is wrong;
- evidence no longer resolves;
- model/observation or range/occurrence labels were collapsed;
- sensitivity was underestimated;
- a public derivative enables reconstruction;
- a policy or rights decision changes;
- a proof or validation result is invalidated;
- a public artifact digest differs from its manifest;
- a stale-state marker was omitted.

### Derivative inventory

A correction plan must identify affected:

- source and processed records;
- relation records;
- catalogs and triplets;
- EvidenceBundles, proofs, and receipts;
- candidate dossiers and release records;
- public maps, tiles, APIs, exports, caches, and indexes;
- graph relations;
- Evidence Drawer and Focus Mode references;
- reports, screenshots, and generated summaries.

### Withdrawal and revocation

Withdrawal may be required when:

- rights are revoked;
- a sensitive source must be removed;
- a public-safe derivative is no longer safe;
- evidence is retracted;
- steward review is withdrawn;
- a relation should not have been asserted.

The candidate and release indexes retain auditable lineage rather than deleting history silently.

### Rollback requirements

A rollback must:

1. identify the affected candidate or release;
2. bind to a verified prior target or safe withdrawal state;
3. invalidate relation and downstream derivatives;
4. remove or supersede public pointers;
5. purge unsafe caches and indexes;
6. update correction, withdrawal, and changelog records;
7. preserve audit lineage;
8. avoid restoring stale, rights-invalid, evidence-invalid, or sensitive-leaking material.

[Back to top](#top)

---

## Public API, map, export, graph, and AI boundary

### Public clients

Public clients must not read:

- RAW, WORK, or QUARANTINE stores;
- processed candidates directly;
- candidate dossiers as data APIs;
- restricted Fauna records;
- source-registry internals;
- proof or receipt stores as public truth;
- direct model outputs;
- unreleased relation projections.

### Map and tile behavior

A public thin-slice carrier may expose only release-approved:

- Habitat context;
- Fauna public-safe derivative references;
- relation character and limitations;
- safe time and uncertainty;
- source attribution;
- safe EvidenceRef resolver keys;
- release, stale, correction, and withdrawal state.

It must not imply:

- exact or current species presence beyond evidence;
- habitat suitability as observation;
- unrestricted access to protected geometry;
- legal or regulatory habitat status;
- management recommendation;
- source, evidence, policy, or release authority.

### Exports

Exports require independent field, geometry, metadata, join, rights, evidence, release, correction, and reconstruction-risk review. Approval for a map popup is not approval for a downloadable dataset.

### Graph and vector indexes

Graph edges and vector embeddings are derived carriers. They must:

- preserve endpoint ownership;
- exclude restricted detail;
- retain evidence and release state;
- invalidate on correction or withdrawal;
- avoid becoming sovereign truth.

### Governed AI

AI may explain released, policy-admitted, citation-closed relations. It may not:

- infer a relation from proximity alone;
- create missing evidence;
- upgrade a model or range to occurrence;
- lower sensitivity;
- reveal protected join context;
- treat proof or candidate state as release state;
- make legal, regulatory, management, or life-safety claims from the slice.

Use finite outcomes:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

Every non-`ANSWER` should carry an accepted reason code.

[Back to top](#top)

---

## Maintenance and definition of done

### Maintenance triggers

Update this README when:

- the first child candidate dossier is created;
- a relation contract or schema is accepted;
- fixture payloads or executable tests appear;
- the proof harness gains executable behavior;
- a proof producer emits accepted artifacts;
- source descriptors are admitted;
- policy bundles become executable;
- a candidate enters review;
- a PromotionDecision or ReleaseManifest is created;
- public artifacts are emitted;
- a correction, withdrawal, supersession, or rollback occurs;
- workflow maturity detectors change;
- ownership, relation, geoprivacy, or release topology is resolved.

### Definition of done

This lane becomes implementation-backed when:

- candidate inventory is deterministic and reviewable;
- candidate identity and artifact-manifest contracts are accepted;
- Habitat, Fauna, and neutral relation contracts are accepted;
- schema overlap between relation and join lanes is resolved by ADR or migration;
- source admission, roles, rights, and stale-state are machine-resolvable;
- synthetic public-safe fixtures exist;
- deterministic no-network tests and validators are wired;
- proof-harness execution is bounded, receipted, and validated;
- EvidenceRef-to-EvidenceBundle resolution is enforced;
- most-restrictive sensitivity and no-leak behavior are enforced;
- policy and reviewer obligations are machine-resolvable;
- candidate-to-PromotionDecision-to-ReleaseManifest routing is accepted;
- correction, withdrawal, cache invalidation, and rollback drills are tested;
- public clients consume only released governed carriers;
- branch protection and independent review requirements are verified.

Until then, this README remains governance documentation, not proof of implementation.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limitation |
|---|---|---|---|
| This target README | `CONFIRMED prior file` | Existing candidate sublane and minimal review fields | Did not establish a candidate or implementation maturity |
| Parent Habitat candidate README | `CONFIRMED` | Parent path, lifecycle, and sibling lanes | Draft guidance; no child candidate instance |
| Habitat release index | `CONFIRMED navigational draft` | Shared release object families and illustrative thin-slice shape | Thin-slice row is explicitly illustrative |
| Habitat sensitivity profile | `CONFIRMED file / draft profile` | Most-restrictive sensitivity and join-induced risk | Profiles doctrine; not executable policy |
| Fauna cross-lane register | `CONFIRMED file / draft relation doctrine` | Ownership, source role, sensitivity, EvidenceBundle support | Concrete repo embodiment remains proposed |
| Habitat promotion runbook | `CONFIRMED file / draft runbook` | Lifecycle, correction, rollback, separation of duties | Implementation claims remain proposed |
| Thin-slice proof-harness README | `CONFIRMED file / draft harness` | Intended proof gates and no-direct-publish boundary | Concrete code, CI, fixtures, and outputs unverified |
| Thin-slice fixture README | `CONFIRMED file` | Synthetic/public-safe fixture rules | Reports no verified payload inventory |
| Thin-slice test README | `CONFIRMED file` | Expected deterministic guardrails | No executable modules verified |
| Direct Habitat thin-slice test file | `CONFIRMED placeholder` | Path presence | One-line docstring; no test behavior |
| Relation-schema README | `CONFIRMED README-only guardrail` | Relation placement and overlap warning | No direct relation schemas established |
| Join schema | `CONFIRMED permissive scaffold` | Existing path and proposed status | Empty properties; cannot validate meaningful relation safety |
| Habitat proof README | `CONFIRMED file / proposed proof lane` | Proof closure expectations | Implementation depth remains unknown |
| Habitat and Fauna policy READMEs | `CONFIRMED scaffolds` | Policy homes | No executable enforcement proof |
| Domain workflows | `CONFIRMED definitions` | Maturity checks and holds | Not candidate validation or release proof |
| General release dry run | `CONFIRMED TODO scaffold` | Workflow presence | Echo jobs do not enforce release gates |
| CODEOWNERS | `CONFIRMED routing surface` | GitHub review routing | Not proof of stewardship or approval |

No external web research is required for this repository-state documentation update.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive recursive inventory under this candidate lane.
- [ ] Confirm candidate naming, stable identity, versioning, digest, and audience conventions.
- [ ] Confirm accepted Habitat, Fauna, and neutral relation contracts.
- [ ] Resolve `schemas/contracts/v1/relations/habitat_fauna/` versus `schemas/contracts/v1/joins/habitat-fauna-join.schema.json`.
- [ ] Replace or formally retire the permissive join scaffold before relying on schema validation.
- [ ] Confirm relation type, direction, cardinality, time, confidence, and uncertainty vocabularies.
- [ ] Confirm Habitat and Fauna source-role mapping and authority limits.
- [ ] Confirm admitted source descriptors, rights, terms, attribution, cadence, and stale tolerance.
- [ ] Confirm synthetic fixture payload inventory and golden outputs.
- [ ] Confirm executable thin-slice tests and proof-harness behavior.
- [ ] Confirm accepted validator ownership and deterministic no-network commands.
- [ ] Confirm EvidenceRef-to-EvidenceBundle resolution and proof output contracts.
- [ ] Confirm most-restrictive sensitivity calculation and audience rules.
- [ ] Confirm named geoprivacy profiles, receipts, reviewer obligations, and no-leak tests.
- [ ] Confirm public fields, geometry, metadata, logs, exports, graph, cache, and AI reconstruction tests.
- [ ] Confirm PolicyDecision, ReviewRecord, ValidationReport, proof, and catalog closure.
- [ ] Confirm candidate-to-PromotionDecision-to-ReleaseManifest handoff.
- [ ] Confirm CorrectionNotice, WithdrawalNotice, supersession, RollbackCard, and derivative invalidation.
- [ ] Confirm public map/API/export/search/graph/Evidence Drawer/AI consumption through governed routes only.
- [ ] Confirm workflow detector behavior, branch protection, required checks, immutable action pinning, and independent reviewers.
- [ ] Confirm generated candidate indexes never become sovereign truth.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced minimal thin-slice candidate notes with a repository-grounded cross-domain candidate index and pre-publication review contract.
- Recorded that no child candidate dossier or active thin-slice candidate is established.
- Added finite states and holds, admission fields, ownership and relation identity, source-role and model/observation anti-collapse, most-restrictive sensitivity, geoprivacy and public-safe representation controls, time and stale-state discipline, release gates, a public-safe dossier template, validation and automation posture, review handoff, correction and rollback discipline, public-client boundaries, evidence ledger, definition of done, and open verification.
- Preserved the exact candidate-not-release sentence and added `publication-not_yet`.
- Added `CONTRACT_VERSION = "3.0.0"` and commit-pinned evidence metadata.

### v1 — prior state

- Minimal README replacing a blank file.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
38cf93f4261e47bb031b88f5477d45915efb730f
```

No Habitat object, Fauna object, relation, source, evidence, policy decision, proof result, candidate, release manifest, public artifact, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
