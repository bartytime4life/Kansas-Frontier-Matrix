<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-fauna-readme
title: Fauna Release Candidate Review Lane
type: per-domain-release-candidate-index
version: v2
status: draft; repository-grounded; deny-by-default; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
lane_role: fauna candidate dossier index and sensitivity-aware pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: eaeebdafeea381ec5532acfd5cc43091f9e81b28
  prior_blob: 360f8bdd8b5474b0ef696a033ee8aefbd1dfdd61
  bounded_candidate_inventory: parent README only; no child candidate dossier established
related:
  - ../README.md
  - ../../README.md
  - ../../manifests/README.md
  - ../../promotion_decisions/README.md
  - ../../correction_notices/README.md
  - ../../rollback_cards/README.md
  - ../../withdrawal_notices/README.md
  - ../../changelog/README.md
  - ../../../data/processed/fauna/README.md
  - ../../../data/processed/fauna/public/README.md
  - ../../../data/processed/fauna/restricted/README.md
  - ../../../data/published/fauna/README.md
  - ../../../data/registry/sources/fauna/README.md
  - ../../../data/proofs/fauna/README.md
  - ../../../contracts/domains/fauna/README.md
  - ../../../schemas/contracts/v1/domains/fauna/README.md
  - ../../../policy/domains/fauna/README.md
  - ../../../policy/sensitivity/fauna/README.md
  - ../../../tests/domains/fauna/README.md
  - ../../../fixtures/domains/fauna/README.md
  - ../../../tools/validators/fauna/README.md
  - ../../../tools/validators/domains/fauna/README.md
  - ../../../docs/domains/fauna/RELEASE_INDEX.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/fauna/ROLLBACK_RUNBOOK.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-fauna.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, fauna, wildlife, sensitive-species, geoprivacy, evidence, validation, rollback]
notes:
  - "This README indexes Fauna release-candidate dossiers and defines their pre-publication review boundary. It is not a candidate, taxonomic, source, evidence, policy, stewardship, release, legal, hunting, fishing, emergency, or publication authority record."
  - "The bounded repository search and current Fauna workflow establish no child candidate dossier under this lane."
  - "The literal sentence 'A candidate is not a release.' is retained for the current domain-fauna readiness workflow; it is a compatibility signal, not release proof."
  - "Exact or reverse-engineerable sensitive locations, private-land detail, steward-controlled records, and geoprivacy transform parameters must not appear in this public-review lane."
  - "CODEOWNERS review routing is not a stewardship assignment, rights-holder approval, independent review, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/fauna/` — Fauna Release Candidate Review Lane

> Index Fauna release-candidate dossiers, preserve blockers and safe support pointers, and prevent animal occurrence, range, seasonal-use, migration, monitoring, disease, mortality, invasive-species, or sensitive-site material from being treated as public-safe or released before evidence, rights, sensitivity, geoprivacy, policy, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-fauna-2E8B57)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![sensitivity](https://img.shields.io/badge/sensitivity-deny__by__default-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@eaeebdaf…`:** the bounded Fauna candidate inventory contains this parent README and no verified child candidate dossier. The Fauna release index is a draft navigation surface with illustrative identifiers rather than verified releases; emitted public carriers remain unverified; and current Fauna automation is a readiness-hold workflow plus a general TODO-only release dry run. No inspected README, placeholder test, proof guide, policy scaffold, workflow result, merge, or generated receipt establishes a Fauna candidate, release, or public-safe wildlife location.
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
[Identity](#fauna-identity-and-source-role-anti-collapse) ·
[Sensitivity](#sensitivity-geoprivacy-and-safe-representation) ·
[Gates](#fauna-release-gates) ·
[Dossier](#required-dossier-structure) ·
[Validation](#validation-proof-and-fixture-posture) ·
[Automation](#automation-posture) ·
[Handoff](#review-and-release-handoff) ·
[Correction](#correction-withdrawal-and-rollback) ·
[Public boundary](#public-api-map-export-and-ai-boundary) ·
[Maintenance](#maintenance-and-definition-of-done) ·
[Evidence](#evidence-ledger) ·
[Open items](#open-verification) ·
[Rollback](#rollback-for-this-readme)

---

## Purpose

`release/candidates/fauna/` is the Fauna pre-publication review lane under the `release/` responsibility root.

It exists to answer these bounded questions:

1. Which Fauna candidate dossiers are currently indexed?
2. What taxon, object family, source role, geography, time, audience, and artifact scope does each candidate claim?
3. Which source, evidence, rights, sensitivity, geoprivacy, policy, validation, and review records support it?
4. Does the proposed public representation preserve uncertainty, taxonomic conflict, source role, stewardship restrictions, and exact-location denial?
5. Which shared release lane owns the next governed record?
6. Can the candidate be corrected, withdrawn, superseded, and rolled back without exposing the restricted original?

**A candidate is not a release.** A candidate folder, README, processed artifact, generalized layer, test result, proof index, review note, pull request, merge, generated receipt, public URL, or file under `data/published/` does not by itself authorize public use.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move or repository event.

[Back to top](#top)

---

## Status and evidence boundary

| Field | Current posture |
|---|---|
| Document type | Fauna candidate-lane index and review contract |
| Owning root | `release/` |
| Candidate lane | `release/candidates/fauna/` |
| Bounded child inventory | No verified child candidate dossier |
| Active candidate | None established |
| Approved Fauna manifest | None established by inspected evidence |
| Published Fauna release | None established by inspected evidence |
| Candidate artifact inventory | **UNKNOWN** beyond README-level guidance |
| Executable candidate validation | Not established |
| Sensitivity policy runtime | Not established; current policy READMEs are scaffolds |
| Release authority of this README | None |
| Default posture | Hold, restrict, generalize, suppress, deny, or abstain rather than infer safety |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from repository files, immutable refs/blobs, workflow definitions/runs, or generated artifacts in this session |
| `PROPOSED` | Candidate contract, placement interpretation, implementation direction, transform binding, or future gate not yet established |
| `UNKNOWN` | Not resolved by the bounded inspection |
| `NEEDS VERIFICATION` | Checkable but not verified strongly enough to act as fact |
| `CONFLICTED` | Repository or doctrine sources disagree and no accepted decision selects a winner |
| `LINEAGE` | Historical or planning material retained for traceability, not current authority by itself |

Operational outcomes such as `HOLD_FOR_EVIDENCE`, `RESTRICT`, `DENY`, `ABSTAIN`, and `ERROR` do not replace these authoring labels.

[Back to top](#top)

---

## Authority and repository fit

Directory Rules place candidate review under `release/` while preserving responsibility boundaries for source admission, data lifecycle, evidence, policy, validation, receipts, release records, and public carriers.

| Responsibility | Owning lane |
|---|---|
| Fauna candidate dossiers and blocker state | This lane |
| Candidate artifacts | [`data/processed/fauna/`](../../../data/processed/fauna/README.md) or an accepted staging lane |
| Public-safe processed derivatives | [`data/processed/fauna/public/`](../../../data/processed/fauna/public/README.md) |
| Restricted processed material | [`data/processed/fauna/restricted/`](../../../data/processed/fauna/restricted/README.md) |
| Source admission, source role, rights, and cadence | [`data/registry/sources/fauna/`](../../../data/registry/sources/fauna/README.md) |
| Evidence and proof support | [`data/proofs/fauna/`](../../../data/proofs/fauna/README.md) |
| Semantic meaning | [`contracts/domains/fauna/`](../../../contracts/domains/fauna/README.md) |
| Machine-checkable shape | [`schemas/contracts/v1/domains/fauna/`](../../../schemas/contracts/v1/domains/fauna/README.md) |
| Admissibility and sensitivity | [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md) and [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md) |
| Executable tests and fixtures | [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) and [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) |
| Validator implementation | `tools/validators/` responsibility lanes |
| Release manifest | Shared manifest lane or accepted successor |
| Promotion decision | Shared promotion-decision lane |
| Correction, withdrawal, supersession, and rollback | Shared release-governance lanes |
| Published public-safe carriers | [`data/published/fauna/`](../../../data/published/fauna/README.md) |
| Public clients | Governed APIs and released artifacts only |

### Path and vocabulary conflicts

The inspected repository carries unresolved or draft distinctions that this README does not settle:

- source registry subtype-first versus domain-first paths;
- broad versus domain-specific validator homes;
- singular/plural release-manifest paths;
- rollback decision cards versus lifecycle rollback receipts/artifacts;
- release-state, review-state, and correction-state vocabularies; and
- T0–T4 release audience tiers versus per-record sensitivity ranks.

Treat these as `CONFLICTED` or `NEEDS VERIFICATION`. Do not create parallel authority sets or silently merge distinct fields.

[Back to top](#top)

---

## Current candidate inventory

The bounded repository search and current Fauna workflow establish this inventory:

| Candidate | Status | Support posture | Public effect |
|---|---|---|---|
| No verified child candidate | `NOT ESTABLISHED` | No child dossier, immutable artifact pointer, reviewed transform packet, or release handoff was verified | None |

### Inventory limits

A code-search result and workflow `find` check are not permanent recursive filesystem proofs. Other child directories, generated files, ignored workspaces, restricted systems, historical branches, Git LFS objects, or differently named records remain **UNKNOWN**.

Add a candidate row only after:

- its child path exists;
- its identity and version are stable;
- its public-safe dossier contains no protected detail;
- its status and finite decision are directly verified; and
- its support pointers resolve to the owning responsibility lanes.

Planning ideas, proposed ranges, proof-lane READMEs, public-layer placeholders, or processed public/restricted lane names are not candidate dossiers.

[Back to top](#top)

---

## Candidate lifecycle

Use finite candidate states and keep review maturity separate from release authority.

| State | Meaning | Permitted next step |
|---|---|---|
| `PROPOSED` | Candidate identity exists; packet is incomplete | Assemble bounded support records |
| `ASSEMBLING` | Artifact and support packet are being gathered | Continue closure work |
| `READY_FOR_REVIEW` | Packet is complete enough for governed review | Open domain, sensitivity, and release review |
| `BLOCKED` | One or more named gates are unresolved | Hold and remediate |
| `REPAIR_REQUIRED` | Candidate data or support records require correction | Return to owning upstream lane |
| `DEFERRED` | Candidate remains eligible but is not advancing | Preserve review trigger and status |
| `RESTRICTED_REVIEW` | Review may proceed only in an authorized restricted environment | Do not copy protected detail here |
| `APPROVED_FOR_MANIFEST` | Decision permits manifest preparation | Prepare manifest in accepted lane |
| `PROMOTED` | Candidate is bound into an approved release path | Preserve release and reversal lineage |
| `STALE` | Source, evidence, review, taxonomy, rights, or public-safe derivative aged out | Refresh, supersede, withdraw, or hold |
| `SUPERSEDED` | A newer candidate replaces this one | Link successor and preserve history |
| `WITHDRAWN` | Candidate is removed from consideration | Record reason and affected references |

`APPROVED_FOR_MANIFEST` does not mean `PUBLISHED`. `PROMOTE_TO_MANIFEST` authorizes manifest preparation only.

### Explicit hold outcomes

- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_TAXONOMY`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_SOURCE_ROLE`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_SENSITIVITY`
- `HOLD_FOR_STEWARDSHIP`
- `HOLD_FOR_GEOPRIVACY`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`

[Back to top](#top)

---

## What belongs here

- This parent README and public-safe candidate indexes.
- One child directory per distinct Fauna candidate.
- Candidate dossier Markdown containing identity, scope, support pointers, blocker state, review state, and finite decision.
- Public-safe readiness checklists and version history.
- Immutable pointers to candidate artifacts without copying payloads.
- Pointers to source admission, evidence, rights, sensitivity, policy, validation, review, release, correction, withdrawal, supersession, and rollback records.
- Public-safe explanations of why a candidate is held, restricted, deferred, repair-required, approved for manifest preparation, superseded, or withdrawn.
- Migration notes when accepted release topology changes.

Candidate dossiers should be compact and pointer-based. Restricted review substance belongs in governed restricted systems and should be represented here only by safe references, status, obligations, and reason codes.

[Back to top](#top)

---

## What does not belong here

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads.
- Occurrence exports, telemetry, tracking records, camera/acoustic files, eDNA payloads, disease surveillance, mortality records, shapefiles, rasters, GeoParquet, COGs, PMTiles, or API payloads.
- Exact or reverse-engineerable occurrence geometry.
- Nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, private-land details, access routes, or steward-controlled records.
- Geoprivacy transform parameters, thresholds, offsets, seeds, radii, masks, or private suppression logic.
- Source descriptors, credentials, tokens, API keys, private agreements, or source-native dumps.
- EvidenceBundle or proof content as the primary record.
- Contracts, schemas, policy bundles, validators, tests, or fixtures.
- Final ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, or RollbackCard records when shared lanes own those families.
- Generated prose presented as evidence, taxonomic authority, sensitivity approval, stewardship approval, or release approval.
- Hunting, fishing, legal, land-access, enforcement, collection, disease-response, emergency, or life-safety instructions.
- Silent promotion by moving, copying, renaming, merging, or publishing files.

[Back to top](#top)

---

## Candidate admission contract

A child candidate may be indexed only when it has a stable identity and an explicit non-release status.

### Minimum fields at candidate creation

| Field | Requirement |
|---|---|
| Candidate ID | Stable and deterministic where practical |
| Candidate version | Explicit and immutable for the dossier revision |
| Domain | `fauna` |
| Object family | Explicit; do not infer from filename |
| Taxon scope | Stable identifiers, authority, rank, conflict posture, and unresolved mappings |
| Geography | Public-safe scope only; protected geometry remains referenced indirectly |
| Time scope | Observation, event, validity, season, retrieval, processing, and review times as applicable |
| Candidate owner | Verified GitHub identity or `OWNER_TBD`; do not invent teams |
| Artifact state | Immutable pointer and digest or `NOT ESTABLISHED` |
| Proposed release target | Pointer or `NOT ESTABLISHED` |
| Source/evidence state | Explicit closure status |
| Rights/stewardship state | Explicit posture and blockers |
| Sensitivity/geoprivacy state | Public-safe disposition and required obligations |
| Validation state | Performed checks, failures, and not-run checks |
| Review state | Pending, approved, changes requested, rejected, or governed override |
| Finite decision | Proposed, hold, restrict, repair, defer, approve-for-manifest, supersede, or withdraw |
| Correction/rollback state | Pointer or explicit blocker |
| Evidence snapshot | Date plus immutable repository/source refs |

### Identity rules

- Do not derive object meaning from a folder name.
- Do not reuse an ID for materially different taxon, object family, source set, geography, time, transform, or audience.
- Do not mutate an approved candidate packet in place; supersede it with traceable lineage.
- Preserve artifact digests and transform/review references.
- Keep candidate ID distinct from taxon ID, occurrence ID, source ID, layer ID, release ID, run ID, and evidence ID.
- A generalized public derivative and its restricted source are separate artifacts with explicit lineage.
- A public-safe candidate must never contain enough detail to reconstruct the restricted original.

[Back to top](#top)

---

## Fauna identity and source-role anti-collapse

Fauna candidate review must preserve object family, taxonomic authority, source role, evidence character, and uncertainty.

### Object-family boundaries

| Object or claim | Must not collapse into |
|---|---|
| `OccurrenceEvidence` | Confirmed public occurrence |
| `OccurrenceRestricted` | Public occurrence derivative |
| `OccurrencePublic` | Restricted source record |
| `SensitiveSite` | Ordinary occurrence or public point |
| `RangePolygon` | Observed presence at every location |
| `SeasonalRange` | Year-round range |
| `MigrationRoute` | Verified exact path or current presence |
| `MortalityObservation` | Population trend or cause determination |
| `DiseaseObservation` | Diagnosis, outbreak authority, or public-health guidance |
| `InvasiveSpeciesRecord` | Regulatory determination or eradication instruction |
| Modeled suitability | Observation or confirmed occurrence |
| Administrative/conservation status | Current local presence |
| Aggregate count/density | Individual location |
| Generated summary | Evidence or stewardship decision |

### Source-role boundaries

| Source role | Candidate rule |
|---|---|
| `observed` | Preserve method, observer/system, QA, time, and evidence support |
| `aggregate` | Do not infer individuals or exact sites from cells/counts |
| `modeled` | Preserve model/run identity, inputs, validation, uncertainty, and reality boundary |
| `regulatory` | Preserve legal/effective scope; do not treat status as occurrence |
| `administrative` | Administrative presence does not establish ecological presence |
| `context` | May frame interpretation; cannot prove a consequential Fauna claim alone |
| `candidate` | Blocks publication until reviewed and promoted |
| `synthetic` | Must remain visibly non-real and excluded from evidence claims |
| `restricted` | Defaults to deny, restrict, redact, generalize, delay, or quarantine |

Aggregator access paths are not source roles. Origin, authority, evidence character, rights, and sensitivity must remain explicit.

### Taxonomic posture

A candidate must not silently resolve:

- accepted-name conflicts;
- synonym or crosswalk conflicts;
- rank changes;
- uncertain identifications;
- taxonomic concept changes;
- source-specific codes;
- hybrid, subspecies, population, or management-unit distinctions; or
- temporal changes to conservation status.

Unresolved taxonomy produces a bounded label, hold, or abstention—not a confident generated answer.

[Back to top](#top)

---

## Sensitivity, geoprivacy, and safe representation

Fauna exact locations and vulnerable-site information fail closed.

### Default protected classes

The public-review lane must not expose:

- sensitive-taxon exact occurrences;
- nests, dens, roosts, hibernacula, spawning sites, breeding or aggregation sites;
- telemetry trails, repeated visit patterns, access routes, or private-land targeting detail;
- steward-controlled, tribal, landowner, agency-restricted, embargoed, or agreement-bound records;
- joins that reconstruct protected locations;
- private collection, enforcement, rehabilitation, disease-response, or operational detail; or
- transform parameters that make reversal or triangulation easier.

### Safe representation contract

A public-safe candidate may proceed only when:

1. the requested audience and use are explicit;
2. the restricted original remains in its governed lane;
3. a named, versioned policy determines disposition;
4. the transform is deterministic and reproducible;
5. required `RedactionReceipt` or `AggregationReceipt` support resolves;
6. geoprivacy and sensitivity review are complete;
7. downstream fields, tiles, exports, search, graph, screenshots, logs, and AI surfaces preserve the same obligations;
8. re-identification and cross-lane joins are tested; and
9. correction and rollback can remove the public derivative without exposing the original.

This README deliberately states no operational transform parameters.

### Finite sensitivity outcomes

- `ALLOW_PUBLIC_SAFE`
- `RESTRICT_TO_REVIEWERS`
- `GENERALIZATION_REQUIRED`
- `AGGREGATION_REQUIRED`
- `REDACTION_REQUIRED`
- `DELAY_OR_EMBARGO`
- `WITHHOLD_GEOMETRY`
- `DENY`
- `ABSTAIN`
- `ERROR`

When policy, rights, review, or transform support is unresolved, use a hold, denial, restriction, or abstention.

[Back to top](#top)

---

## Fauna release gates

Every candidate fails closed when a load-bearing gate is unresolved.

| Gate | Required question | Failure posture |
|---|---|---|
| Identity | Is the candidate stable, versioned, scoped, and owned? | `HOLD_FOR_ARTIFACT` |
| Taxonomy | Are taxon identity, authority, rank, crosswalks, and conflicts explicit? | `HOLD_FOR_TAXONOMY` |
| Artifact | Is there an immutable candidate pointer and digest? | `HOLD_FOR_ARTIFACT` |
| Meaning and shape | Are object family, keys, fields, units, time, geography, and schema defined? | `REPAIR_REQUIRED` |
| Source admission | Do all sources resolve to admitted records with role, rights, cadence, and activation? | `HOLD_FOR_SOURCE_ADMISSION` |
| Source role | Are observed, modeled, aggregate, administrative, context, and restricted roles preserved? | `HOLD_FOR_SOURCE_ROLE` |
| Evidence | Do consequential `EvidenceRef` values resolve to admissible `EvidenceBundle` support? | `HOLD_FOR_EVIDENCE` / `ABSTAIN` |
| Rights/stewardship | Are license, agreement, attribution, authority, and stewardship obligations clear? | `HOLD_FOR_RIGHTS` / `HOLD_FOR_STEWARDSHIP` |
| Sensitivity | Is the most restrictive applicable posture explicit? | `HOLD_FOR_SENSITIVITY` / `DENY` |
| Geoprivacy | Is a public-safe representation supported without revealing operational parameters? | `HOLD_FOR_GEOPRIVACY` |
| Policy | Is a versioned PolicyDecision present with obligations and reason code? | `HOLD_FOR_POLICY` |
| Validation | Do deterministic positive and negative checks pass? | `HOLD_FOR_VALIDATION` |
| Review | Are required, distinct reviewers recorded? | `HOLD_FOR_REVIEW` |
| Release topology | Are decision and manifest homes accepted and non-duplicative? | `HOLD_FOR_RELEASE_TOPOLOGY` |
| Correction | Can errors, rights changes, taxonomy changes, and leaks be corrected downstream? | `HOLD_FOR_CORRECTION_PATH` |
| Rollback | Is a prior safe target or withdrawal plan defined and drilled? | `HOLD_FOR_ROLLBACK` |

Passing a schema, validator, test, geoprivacy transform, review checklist, or PR does not itself close the release gate.

[Back to top](#top)

---

## Required dossier structure

A child candidate README should include at least:

```markdown
# <candidate-id> — <public-safe candidate title>

## Candidate status
PROPOSED / ASSEMBLING / READY_FOR_REVIEW / BLOCKED / REPAIR_REQUIRED /
DEFERRED / RESTRICTED_REVIEW / APPROVED_FOR_MANIFEST / PROMOTED /
STALE / SUPERSEDED / WITHDRAWN

## Candidate identity
<id, version, domain, owner, date, evidence snapshot>

## Public-safe scope
<object family, taxon scope, coarse geography, time scope, audience, intended surface>

## Candidate artifact
<immutable processed/staged pointer, digest, artifact manifest, or NOT ESTABLISHED>

## Restricted-source relationship
<safe pointer and lineage only; no protected geometry or transform parameters>

## Source, rights, and stewardship closure
<SourceDescriptor refs, source roles, rights, authorities, cadence, blockers>

## Evidence closure
<EvidenceRef-to-EvidenceBundle mapping and unresolved claims>

## Sensitivity and geoprivacy
<disposition, named policy/profile refs, receipt refs, obligations, blockers>

## Validation
<identity, taxonomy, schema, time, source role, evidence, policy, no-leak,
public-boundary, correction, and rollback checks>

## Review
<required reviewers, states, dates, separation-of-duties posture>

## Release handoff
<review, PromotionDecision, and ReleaseManifest pointers or explicit blockers>

## Correction and rollback
<affected consumers, correction/withdrawal/supersession path, rollback target>

## Current decision
<finite outcome plus evidence-grounded reason>
```

Protected source material, review substance, private correspondence, exact locations, and transform parameters remain outside this public dossier.

[Back to top](#top)

---

## Validation, proof, and fixture posture

Current repository evidence does not establish a complete Fauna candidate-validation or release-governance suite.

| Surface | Current safe interpretation |
|---|---|
| [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) | Rich test-lane guidance; sampled direct modules are one-line `PROPOSED` placeholders |
| [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) | Fixture responsibility exists; executable coverage and exhaustive inventory remain unverified |
| [`tools/validators/fauna/`](../../../tools/validators/fauna/README.md) | Broad validator guidance; accepted executable command and ownership remain unverified |
| [`tools/validators/domains/fauna/`](../../../tools/validators/domains/fauna/README.md) | Domain validator guidance; executable maturity remains verification-bound |
| [`data/proofs/fauna/`](../../../data/proofs/fauna/README.md) | Draft proof-lane guide; concrete proof inventory, schemas, producers, access controls, and release linkage remain unresolved |
| [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md) | Greenfield scaffold with overbroad text; not executable policy proof |
| [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md) | `PROPOSED` scaffold; no verified geoprivacy policy implementation |
| Fauna schemas/contracts | Files and indexes exist with mixed maturity; presence does not establish enforcement |
| Published Fauna lane | Release-gated carrier guidance exists; emitted release-linked artifacts remain unverified |

### Required negative cases

A mature no-network suite should reject:

- missing or mutable artifact pointers;
- taxonomic conflict hidden as certainty;
- unresolved source identity, role, rights, cadence, or activation;
- modeled-to-observed, aggregate-to-individual, status-to-presence, or candidate-to-confirmed upcasts;
- exact or reverse-engineerable protected location exposure;
- public derivatives without named policy and required receipts;
- cross-lane joins that reconstruct sensitive sites;
- missing, stale, revoked, conflicted, or unauthorized evidence;
- public fields, tiles, exports, screenshots, logs, or AI responses that leak protected detail;
- hunting, legal, enforcement, collection, disease-response, or emergency-authority framing;
- missing review, correction, withdrawal, supersession, or rollback support;
- direct public access to processed, restricted, registry, catalog, or proof stores; and
- generated language presented as evidence or approval.

A passing test proves only its declared scope. It does not confirm a taxon, occurrence, sensitive site, legal right, stewardship disposition, or release.

[Back to top](#top)

---

## Automation posture

| Workflow | Current boundary |
|---|---|
| [`domain-fauna`](../../../.github/workflows/domain-fauna.yml) | Read-only readiness checks for validation, proof, and release-dry-run maturity; no Fauna truth validation or release |
| [`release-dry-run`](../../../.github/workflows/release-dry-run.yml) | TODO-only general candidate, promotion-gate, and rollback-card echo jobs |

`domain-fauna` uses ordinary pull-request/push triggers, `workflow_dispatch`, `contents: read`, GitHub-hosted runners, concurrency cancellation, timeouts, and disabled persisted checkout credentials.

It intentionally fails when executable tests, validator files, proof artifacts, Make targets, or candidate records surface, so maintainers must graduate the corresponding hold deliberately. File presence may be a placeholder rather than mature implementation; workflow findings must be inspected rather than interpreted as domain validation.

A successful held job proves only that its checked maturity assumptions still hold. It is not an EvidenceBundle, geoprivacy proof, stewardship decision, ReleaseManifest, legal determination, or publication authority.

The general `release-dry-run` workflow remains TODO-only. Green `echo TODO` jobs are not candidate assembly, promotion enforcement, rollback verification, or release proof.

[Back to top](#top)

---

## Review and release handoff

The accepted review chain should remain explicit and separate.

| Review concern | Required responsibility |
|---|---|
| Taxon and object-family meaning | Fauna domain steward |
| Artifact production and lifecycle state | Data/pipeline steward |
| Source admission and origin role | Source/registry steward |
| Rights, agreement, attribution, and stewardship | Rights/stewardship reviewer |
| Sensitivity and geoprivacy | Sensitivity/geoprivacy reviewer |
| Evidence and proof closure | Evidence/proof steward |
| Policy outcome and obligations | Policy steward |
| Deterministic validation | Test/validator steward |
| Public API/map/export/AI boundary | Public-surface steward |
| Promotion and manifest preparation | Release steward |
| Correction, withdrawal, supersession, and rollback | Release plus domain/data owners |

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes `/release/` review to `@bartytime4life`. That routing is not a StewardshipAssignment, rights-holder approval, independent review, PolicyDecision, release approval, or proof that review occurred.

### Handoff routes

| Record or action | Route | Candidate-lane boundary |
|---|---|---|
| Candidate dossier | This lane | Pre-publication review only |
| Release review | Accepted review lane | Review recommendation, not publication |
| Promotion decision | [`release/promotion_decisions/`](../../promotion_decisions/README.md) | May permit manifest preparation |
| Release manifest | [`release/manifests/`](../../manifests/README.md) or accepted successor | Release decision record, not payload |
| Correction notice | [`release/correction_notices/`](../../correction_notices/README.md) | Communication linked to governed correction |
| Rollback/review card | [`release/rollback_cards/`](../../rollback_cards/README.md) or accepted successor | Reversal/review aid; topology remains draft |
| Withdrawal notice | [`release/withdrawal_notices/`](../../withdrawal_notices/README.md) | Records governed withdrawal |
| Release history | [`release/changelog/`](../../changelog/README.md) | Narrative companion, not sovereign state |
| Published carrier | [`data/published/fauna/`](../../../data/published/fauna/README.md) | Downstream after governed release |

[Back to top](#top)

---

## Correction, withdrawal, and rollback

Fauna corrections must account for both truth defects and exposure defects.

### Correction triggers

- taxonomic identity or crosswalk changed;
- source was corrected, superseded, retired, or rights-restricted;
- occurrence validity or date changed;
- modeled/context material was misrepresented as observation;
- sensitivity or stewardship posture became more restrictive;
- a public derivative allowed re-identification;
- a field, tile, export, screenshot, search index, graph, cache, or AI surface leaked protected detail;
- evidence was withdrawn, stale, or contradicted;
- public carrier and manifest digest diverged;
- correction, withdrawal, or rollback references failed to resolve.

### Required response

1. Hold or disable affected public surfaces.
2. Preserve evidence and audit state without copying protected detail into public records.
3. Identify affected candidates, releases, catalogs, caches, indexes, tiles, exports, graph projections, and AI contexts.
4. Emit or link the governed correction, withdrawal, supersession, and rollback records.
5. Re-evaluate rights, sensitivity, geoprivacy, evidence, policy, validation, and review.
6. Restore a prior safe release or withdraw the public surface.
7. Verify cache invalidation and absence of protected canaries.
8. Preserve lineage and record why the state changed.

Rollback is a governed state transition, not a hidden file copy. The [`Fauna rollback runbook`](../../../docs/runbooks/fauna/ROLLBACK_RUNBOOK.md) is draft guidance; operational drill evidence remains `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Public API, map, export, and AI boundary

Public clients must consume governed interfaces and released, public-safe artifacts—not candidate, processed, restricted, registry, catalog, or proof stores directly.

### Public-surface rules

- No unreleased candidate may appear as current public truth.
- Exact or reverse-engineerable sensitive locations fail closed.
- Public layers and tiles use field allowlists and release-bound manifests.
- Range and density surfaces must not imply observed presence at every location.
- Uncertainty, taxonomy, time, source role, caveats, and correction state remain visible.
- Search, graph, embeddings, exports, screenshots, logs, and analytics preserve the same restrictions as maps and APIs.
- A missing public-safe representation produces `DENY`, `ABSTAIN`, or no render—not a guessed location.
- Public output must retain correction, supersession, withdrawal, and rollback status.

### Governed AI

AI is interpretive, not root truth. Preferred order:

1. resolve released candidate/release scope;
2. resolve `EvidenceRef` to admissible `EvidenceBundle`;
3. apply source-role, rights, stewardship, sensitivity, and geoprivacy policy;
4. verify current release and correction state; then
5. answer with citations and bounded detail, or `ABSTAIN`, `DENY`, or `ERROR`.

AI must not provide exact sensitive locations, reconstruction hints, collection or access advice, hunting/fishing/legal guidance, operational wildlife response, or emergency authority.

[Back to top](#top)

---

## Maintenance and definition of done

Update this README when:

- a child candidate is added, renamed, superseded, withdrawn, or removed;
- a candidate changes finite state;
- Fauna source-registry topology changes;
- sensitivity/geoprivacy policy becomes executable or changes materially;
- candidate schemas, validators, fixtures, proofs, tests, or CI mature;
- manifest, promotion, correction, withdrawal, or rollback topology changes;
- CODEOWNERS or stewardship assignments change;
- a public-surface leak or correction changes review requirements; or
- this document overstates repository maturity.

### Definition of done

This lane may graduate beyond draft only when:

- [ ] candidate inventory is generated or deterministically validated;
- [ ] every child exposes stable identity, version, status, decision, and immutable evidence snapshot;
- [ ] public dossiers are demonstrably free of protected detail and transform parameters;
- [ ] taxonomy, source role, rights, stewardship, sensitivity, geoprivacy, evidence, policy, validation, review, correction, and rollback fields are machine-checkable or explicitly governed;
- [ ] source-registry and validator topology conflicts are resolved;
- [ ] substantive public-safe positive and negative fixtures and tests exist;
- [ ] geoprivacy/no-leak checks cover structured and narrative surfaces;
- [ ] candidate validation and release dry-run commands are deterministic and no-network by default;
- [ ] CI invokes accepted commands and distinguishes placeholders from mature implementations;
- [ ] branch protection and required reviewers are verified;
- [ ] correction, withdrawal, cache-invalidation, and rollback drills have evidence; and
- [ ] public clients remain downstream of governed APIs and released artifacts.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior parent README, blob `360f8bdd…` | `CONFIRMED` | Existing Fauna candidate-lane purpose and generic fields | Did not record bounded inventory or current automation/policy maturity |
| [`release/candidates/README.md`](../README.md) | `CONFIRMED file / draft guidance` | Cross-domain candidate states and review fields | Does not prove Fauna completeness |
| Bounded Fauna candidate search | `CONFIRMED bounded search` | Surfaced parent README and no verified child dossier | Not a permanent recursive filesystem proof |
| [`RELEASE_INDEX.md`](../../../docs/domains/fauna/RELEASE_INDEX.md) | `CONFIRMED file / draft navigation` | Release-plane orientation, sensitivity posture, correction and rollback expectations | Identifiers and state vocabularies remain illustrative or conflicted |
| [`SENSITIVITY.md`](../../../docs/domains/fauna/SENSITIVITY.md) | `CONFIRMED doctrine-facing doc` | Deny-by-default, geoprivacy, safe representation, no-parameter public-doc posture | Binding policy implementation remains absent |
| Fauna policy READMEs | `CONFIRMED scaffolds` | Intended policy ownership | Do not establish executable admissibility |
| [`data/registry/sources/fauna/`](../../../data/registry/sources/fauna/README.md) | `CONFIRMED grounded README` | Source role, rights, sensitivity, cadence, and no-public-path controls | Source topology and concrete descriptor closure remain unresolved |
| [`data/proofs/fauna/`](../../../data/proofs/fauna/README.md) | `CONFIRMED file / PROPOSED proof lane` | EvidenceBundle, geoprivacy-proof, correction, and rollback support expectations | Concrete proof inventory and producer remain unverified |
| [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) and sampled modules | `CONFIRMED scaffold / placeholders sampled` | Intended domain test matrix | Executable suite and pass results not established |
| [`data/published/fauna/`](../../../data/published/fauna/README.md) | `CONFIRMED carrier guidance` | Released public-safe carrier boundary | Emitted release-linked instances remain unverified |
| [`domain-fauna`](../../../.github/workflows/domain-fauna.yml) | `CONFIRMED definition` | Read-only maturity checks and explicit holds | Held success/failure is not Fauna validation or release proof |
| General release dry run | `CONFIRMED TODO scaffold` | Existing workflow presence | Green echo jobs are not release governance |
| CODEOWNERS | `CONFIRMED routing` | Current GitHub review route | Not stewardship, independent approval, or branch-protection proof |

No external web research is required for this repository-state documentation update.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive child inventory under `release/candidates/fauna/`.
- [ ] Confirm candidate naming, identity, versioning, and artifact-manifest conventions.
- [ ] Confirm canonical taxon identity and crosswalk contracts.
- [ ] Confirm accepted object-family and source-role vocabularies.
- [ ] Resolve subtype-first versus domain-first source registry topology.
- [ ] Confirm admitted sources, rights, cadence, activation, stewardship, and source-head identity.
- [ ] Confirm EvidenceRef-to-EvidenceBundle and geoprivacy-proof contracts.
- [ ] Replace Fauna policy scaffolds with reviewed executable policy and safe reason codes.
- [ ] Confirm named geoprivacy profiles and receipt schemas without exposing parameters in public docs.
- [ ] Confirm public-safe fixture inventory and no-network enforcement.
- [ ] Confirm accepted validator ownership and distinguish placeholder files from mature implementations.
- [ ] Confirm candidate-to-review, PromotionDecision, and ReleaseManifest handoff.
- [ ] Resolve manifest, correction, withdrawal, rollback-card, and lifecycle rollback topology.
- [ ] Confirm correction consumers, cache invalidation, withdrawal/supersession behavior, and rollback drills.
- [ ] Confirm public API/map/tile/export/search/graph/AI no-leak tests.
- [ ] Confirm branch protection, required checks, immutable action pinning, and independent reviewer assignments.
- [ ] Confirm candidate inventory can be generated from machine-readable records without making generated output sovereign truth.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced generic Fauna candidate guidance with a repository-grounded, sensitivity-aware candidate index and pre-publication review contract.
- Recorded that no child candidate dossier or active candidate is established by bounded inspection.
- Preserved the exact workflow compatibility sentence and `publication-not_yet` marker.
- Added finite states and holds, admission and identity rules, source-role and object-family anti-collapse, taxonomic conflict posture, sensitivity/geoprivacy controls, release gates, a public-safe dossier contract, validation and automation maturity, review handoff, correction and rollback discipline, public-surface boundaries, evidence ledger, definition of done, and open verification.
- Added `CONTRACT_VERSION = "3.0.0"` and immutable evidence snapshot metadata.

### v1 — 2026-07-03

- Replaced the earlier greenfield stub with initial Fauna candidate-lane guidance.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
360f8bdd8b5474b0ef696a033ee8aefbd1dfdd61
```

No Fauna candidate, source, taxon, occurrence, sensitive site, evidence, policy, stewardship, review, release, public carrier, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
