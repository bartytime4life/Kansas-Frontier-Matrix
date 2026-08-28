<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-flora-watchers-readme
title: pipeline_specs/flora/watchers/ — Governed Flora Watcher Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; direct-sublane-readme-only; external-placeholders-present; no-active-watcher-spec-established; sensitive-domain
owners: OWNER_TBD — Pipeline-spec steward · Flora steward · Watcher steward · Plant taxonomy/herbarium steward · Source and rights steward · Cultural/stewardship reviewer · Sensitivity/geoprivacy reviewer · Temporal/freshness steward · Validation steward · Evidence steward · Policy steward · Release steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public; pipeline-specs; flora; watchers; declarative-only; metadata-first; taxonomy-aware; specimen-aware; cultural-rights-aware; rare-plant-deny-default; no-secrets; no-live-activation; no-direct-fetch; no-direct-admission; no-direct-raw; no-direct-release; source-role-preserving; rights-aware; stale-state-aware; review-gated
current_path: pipeline_specs/flora/watchers/README.md
truth_posture: CONFIRMED current target, README-only direct watcher-spec sublane, two seven-line PROPOSED plants-drift placeholders outside this sublane, draft shared/domain executable watcher READMEs with unresolved ownership, README-only Flora config lane, draft source registry with unresolved topology, draft receipt lane with unresolved subtype layout, conflicted sensitivity docs, scaffold binding policy lanes, README-backed tests with unknown executable coverage, populated synthetic fixture lanes with unverified payload/consumer alignment, TODO-only Flora workflow, and placeholder CODEOWNERS / PROPOSED minimum active watcher-spec contract, canonical placement reconciliation, deterministic consumer binding, metadata-first comparison, taxonomy/specimen/occurrence role preservation, cultural-rights and sensitive-diff controls, finite outcomes, activation/deactivation, correction, and rollback / UNKNOWN accepted schema, parser, registry, discovery, scheduler, active sources, executable consumer, substantive CI, emitted receipts, production review integration, and runtime use / NEEDS VERIFICATION owners, source-registry topology, admitted SourceDescriptors, rights/source-role/cultural-authority vocabularies, taxonomy authorities, source terms, cadence budgets, report/receipt schemas, fixture payloads, executable tests, validators, policy implementation, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6a6abd1cfadf181c093f21d0eb36a38f7ca3ed8b
  prior_blob: e70461b62fca264f476fb739ea4eb9168709371a
  direct_sublane_files:
    - pipeline_specs/flora/watchers/README.md
  external_placeholders:
    - pipeline_specs/flora/plants_drift_watcher.yaml
    - pipeline_specs/watchers/plants_drift.yaml
  candidate_executable_lanes:
    - pipelines/domains/flora/watchers/README.md
    - pipelines/watchers/plants/README.md
  workflow_posture: domain-flora is pull-request-triggered TODO scaffolding
related:
  - ../../README.md
  - ../README.md
  - ../../watchers/README.md
  - ../plants_drift_watcher.yaml
  - ../../watchers/plants_drift.yaml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/flora/SENSITIVITY.md
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/SOURCE_ROLES.md
  - ../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../pipelines/watchers/README.md
  - ../../../pipelines/domains/flora/watchers/README.md
  - ../../../pipelines/watchers/plants/README.md
  - ../../../configs/domains/flora/README.md
  - ../../../data/registry/sources/flora/README.md
  - ../../../data/receipts/flora/README.md
  - ../../../policy/domains/flora/README.md
  - ../../../policy/sensitivity/flora/README.md
  - ../../../tests/domains/flora/README.md
  - ../../../fixtures/domains/flora/README.md
  - ../../../fixtures/domains/flora/plants_drift/README.md
  - ../../../release/candidates/flora/README.md
  - ../../../.github/workflows/domain-flora.yml
  - ../../../.github/CODEOWNERS
notes:
  - "v0.2 replaces a planning-only profile tree with commit-pinned evidence, classifies this direct sublane as README-only, and surfaces external plants-drift placeholders and ownership conflicts."
  - "Watcher specs are declarative intent only. They do not fetch payloads, activate sources, admit RAW, emit evidence, update catalogs, or release public artifacts."
  - "Rare, protected, culturally sensitive, medicinal, restoration-sensitive, and steward-controlled plant locations and knowledge fail closed. No exposure parameters or protected details appear here."
  - "No executable profile, source record, connector, pipeline, schema, contract, policy rule, fixture, test, validator, workflow, lifecycle object, receipt instance, proof, release object, runtime behavior, or public artifact is created or modified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Flora Watcher Specification Boundary

`pipeline_specs/flora/watchers/`

> Declarative run-intent boundary for Flora source-change watchers. A reviewed profile may state **what safe source-head or metadata signals a verified watcher should compare**, against which admitted source descriptors, at what cadence, and which bounded no-op, candidate, quarantine, or review handoff is expected. It does not fetch or admit payloads, decide botanical truth, lower sensitivity, create evidence, update catalogs, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__watcher__spec-green)
![inventory](https://img.shields.io/badge/direct__inventory-README__only-lightgrey)
![placement](https://img.shields.io/badge/plants__drift__placement-NEEDS__VERIFICATION-orange)
![sensitivity](https://img.shields.io/badge/rare__plant__locations-deny__by__default-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-evidence-and-maturity) · [Placement](#repository-fit-and-inventory) · [Scope](#flora-watcher-scope) · [Contract](#minimum-active-watcher-specification-contract) · [Example](#illustrative-inactive-yaml) · [Materiality](#materiality-and-finite-outcomes) · [Sensitivity](#sensitivity-cultural-rights-and-no-leak-boundary) · [Validation](#validation-review-and-activation) · [Rollback](#correction-deactivation-and-rollback) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@6a6abd1cfadf181c093f21d0eb36a38f7ca3ed8b`  
> **Prior target blob:** `e70461b62fca264f476fb739ea4eb9168709371a`  
> **Direct sublane:** this README only  
> **Elsewhere:** two seven-line `PROPOSED` plants-drift placeholders  
> **Activation:** file presence, merge state, schedule text, syntax validity, fixture success, or a dry run activates nothing

> [!CAUTION]
> A changed ETag, checksum, timestamp, version, manifest, taxonomy list, or source descriptor does **not** establish source admission, material botanical change, current occurrence, taxonomic identity, rights clearance, sensitivity safety, or release readiness. Exact rare/protected/culturally sensitive locations, herbarium locality detail, restoration-sensitive sites, small-cell clues, and steward-controlled or culturally restricted information must not enter watcher logs, reports, receipts, notifications, issue text, or generated summaries.

---

## Purpose

This directory is the Flora-specific declarative watcher sublane under the `pipeline_specs/` responsibility root.

A future active profile may bind:

- stable identity, immutable version/digest, owner, status, and supersession lineage;
- one accepted parser and one verified executable consumer;
- admitted Flora `SourceDescriptor` references;
- source role, rights, attribution, cultural authority, stewardship, sensitivity, cadence, and activation state;
- taxonomy/nomenclature authority and specimen-versus-occurrence knowledge character;
- metadata-first checks and prior comparison state;
- retry, outage, stale-state, correction, and no-op behavior;
- material-change classes and finite reason codes;
- bounded candidate, quarantine, and review handoffs;
- watcher-run and material-change receipt requirements;
- deterministic no-network fixtures and replay;
- explicit no-fetch, no-admission, no-RAW, no-evidence, no-catalog, and no-release constraints;
- deactivation, correction, withdrawal, and rollback targets.

This README is not a watcher schema, parser, registry, scheduler, executable watcher, source activation decision, source data record, taxonomy authority, cultural permission, policy decision, receipt, evidence object, release record, or public notification system.

[Back to top](#top)

---

## Authority and anti-collapse

```text
pipeline_specs/  = declarative intent: WHAT may be checked and under which gates
pipelines/       = executable behavior: HOW comparisons and handoffs occur
connectors/      = upstream access and payload retrieval authority
data/registry/   = source identity, role, rights, sensitivity, cadence, admission
contracts/       = Flora object meaning
schemas/         = machine-checkable shape
policy/          = rights, sensitivity, admissibility, and release decisions
data/            = lifecycle records, receipts, proofs, catalogs, published artifacts
release/         = promotion, correction, withdrawal, supersession, rollback
apps/            = governed released serving surfaces
```

A watcher spec may require a gate. Naming the gate does not satisfy it.

### Disallowed collapses

```text
watcher spec                 -> executable watcher or source activation
source list                  -> source authority
schedule                     -> proof of freshness
ETag/checksum change         -> botanical material change
source-head match            -> rights or sensitivity approval
taxonomy drift               -> accepted taxonomic revision
specimen metadata change     -> current occurrence
range/model change           -> observed occurrence
watcher report               -> EvidenceBundle
fixture pass                 -> implementation proof
watcher success              -> catalog or release approval
```

Specimen evidence, field occurrence, community-science report, survey, range, model, aggregate, habitat context, vegetation classification, restoration record, phenology record, and candidate inference remain distinct. Source role, taxonomy, rights, cultural authority, sensitivity, freshness, evidence, and release remain independent gates. Watcher outputs remain bounded candidates, process memory, quarantine, or review handoffs.

[Back to top](#top)

---

## Current evidence and maturity

| Surface | Inspected status | What it does **not** prove |
|---|---|---|
| Direct `pipeline_specs/flora/watchers/` sublane | README only in bounded search | No concrete profile, accepted schema, parser, schedule, activation, or consumer. |
| `pipeline_specs/flora/plants_drift_watcher.yaml` | Seven-line `PROPOSED` inventory placeholder | Not active or consumer-bound. |
| `pipeline_specs/watchers/plants_drift.yaml` | Seven-line `PROPOSED` inventory placeholder | Not canonical, active, or reconciled. |
| Flora executable watcher README | Detailed draft documentation under `pipelines/domains/flora/watchers/` | No verified code, source activation, schedule, runtime, or CI enforcement. |
| Shared plants watcher README | Detailed draft documentation under `pipelines/watchers/plants/` | No settled ownership or verified implementation. |
| Flora config lane | README-only | No loader, precedence, consumer, source activation, or runtime binding. |
| Flora source registry | Draft, with subtype-first/domain-first topology conflict | No canonical active descriptor inventory or production admission proof. |
| Flora receipt lane | Draft parent; redaction child documented | No emitted receipt instances, final subtype layout, signing, or enforcement. |
| Flora sensitivity documentation | Detailed but overlapping/conflicted documents | No binding policy implementation by prose. |
| Flora policy lanes | `PROPOSED` scaffolds | No executable rights, cultural-authority, geoprivacy, or release policy. |
| Flora tests | README coverage map; executable completeness unknown | No spec-specific test pass or enforcement proof. |
| Flora fixtures | Populated README lanes, including `plants_drift/` | No verified payload inventory or consumer alignment by README alone. |
| Domain Flora workflow | Three `echo TODO` jobs | No Flora watcher validation, proof build, or publish dry run. |
| CODEOWNERS | Placeholder | No enforced Flora watcher review ownership. |
| Runtime/public use | Not established | No production or public-surface behavior. |

**Current status:** documentation and planning artifacts exist; no active Flora watcher specification is established.

[Back to top](#top)

---

## Repository fit and inventory

### Direct sublane

```text
pipeline_specs/flora/watchers/
└── README.md
```

### External watcher-shaped placeholders

```text
pipeline_specs/flora/plants_drift_watcher.yaml
pipeline_specs/watchers/plants_drift.yaml
```

Both are seven-line `PROPOSED` placeholders created from documentation inventory. Neither is an accepted active specification.

Three possible declarative homes now appear: this domain watcher sublane, the parent Flora spec lane, and the shared watcher lane. Two possible executable homes appear: `pipelines/domains/flora/watchers/` and `pipelines/watchers/plants/`. This README does not select one by assertion. Before an active profile is added, canonical placement and delegation require a governed decision or migration note. Duplicate active specifications are prohibited.

The verified Flora receipt parent is `data/receipts/flora/`. Final watcher receipt subtype layout remains **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Flora watcher scope

| Profile family | Allowed observation intent | Required distinction |
|---|---|---|
| Plant taxonomy/nomenclature | Version, accepted-name, synonym, authority-list, or crosswalk drift | Drift is not accepted taxonomy. |
| Herbarium/specimen | Dataset/package/manifest/schema/terms drift | Specimen locality is not current occurrence and may be sensitive. |
| Occurrence/community science | Source-head, schema, metadata, terms, or controlled update notice | Reported observation is not verified occurrence. |
| Rare/protected plants | Public-safe metadata or reviewed source-state changes only | Never copy exact locality or reconstructive detail. |
| Vegetation communities | Classification, legend, schema, version, or source-package drift | Community polygon is not taxon occurrence. |
| Invasive plants | Listing/status/schema/source update signals | Status and occurrence remain separate. |
| Phenology | Method, station, schema, season, and source-version drift | Observation, valid, and retrieval time remain distinct. |
| Restoration | Plan/version/status metadata under rights and stewardship controls | Planned planting is not established occurrence. |
| Remote-sensing vegetation | Product version, collection, algorithm, manifest, or model-card drift | Modeled signal is not field observation. |
| Public indicators | Source and methodology drift | Changes do not directly refresh public products. |
| Source descriptors | Identity, role, rights, cadence, sensitivity, endpoint, or correction drift | Registry review precedes watcher action. |

Watcher specs must not contain credentials, private endpoints, live payloads, protected localities, cultural knowledge, or operational geoprivacy parameters; grant source admission; retrieve full payloads as connector authority; write lifecycle data; decide taxonomy, rights, sensitivity, evidence, policy, or release; or notify the public as an official authority.

[Back to top](#top)

---

## Minimum active watcher specification contract

A future active profile must be machine-validated and include accepted equivalents for:

1. **Identity:** schema version, stable ID, immutable version/digest, finite status, owner, effective/retired time, supersession, correction, and rollback references.
2. **Binding:** accepted parser, registry/discovery reference, exactly one executable consumer or delegation chain, precedence, conflict behavior, and separate activation record.
3. **Sources:** admitted `SourceDescriptor` refs, role, claim limits, rights, terms, attribution, cultural authority, stewardship, sensitivity, permitted checks, cadence, correction, and withdrawal refs.
4. **Taxonomy/knowledge character:** controlling nomenclatural authority, identifier namespace, crosswalk version, and explicit specimen/occurrence/survey/range/model/aggregate/vegetation/invasive/phenology/restoration/context role.
5. **Checks:** metadata-first strategy, prior baseline and digest, allowed checks, retry/backoff, timeout, outage, stale state, idempotency, log allowlist, and payload-capture prohibition.
6. **Outcomes:** finite outcomes, materiality classes, reason codes, candidate/quarantine/review handoffs, no-op/run/change receipts, hashes, lineage, and no-direct-admission/no-direct-release assertions.
7. **Safety:** sensitive-detail deny rules, cultural/stewardship restrictions, secret/private-endpoint prohibition, field allowlists, correction, suspension, withdrawal, invalidation, and rollback procedure.

[Back to top](#top)

---

## Illustrative inactive YAML

> [!WARNING]
> Incomplete, non-canonical, unregistered, inactive, and unsafe for production. It activates no source or watcher.

```yaml
schema_version: kfm.pipeline_spec.flora.watcher.PROPOSED
spec_id: flora.watchers.example
version: 0.0.0-example
status: draft
activation: disabled
owner: OWNER_TBD
implementation:
  target: NEEDS_VERIFICATION
sources:
  - source_descriptor_ref: NEEDS_VERIFICATION
    expected_role: NEEDS_VERIFICATION
    rights_ref: NEEDS_VERIFICATION
    sensitivity_ref: NEEDS_VERIFICATION
    cultural_authority_ref: NEEDS_VERIFICATION
watch:
  mode: metadata_only
  cadence: manual
  checks: [source_version, manifest_digest, source_vintage]
  payload_capture: false
prior_state:
  baseline_ref: NEEDS_VERIFICATION
materiality:
  classes: [no_material_change, metadata_change, taxonomy_change, schema_change, rights_or_terms_change, sensitivity_or_stewardship_change, unknown_change]
outputs:
  admit_to_raw: false
  publish: false
  candidate_report: true
  review_required: true
receipts:
  watcher_run_required: true
  material_change_required: true
security:
  log_sensitive_values: false
rollback:
  kill_switch: NEEDS_VERIFICATION
```

[Back to top](#top)

---

## Materiality and finite outcomes

| Class | Meaning | Default handoff |
|---|---|---|
| `NO_MATERIAL_CHANGE` | Compared metadata is equivalent. | No-op receipt. |
| `AVAILABILITY_CHANGE` | Availability or endpoint state changed. | Candidate/review; no blind fetch. |
| `METADATA_CHANGE` | Non-payload metadata changed. | Candidate/review. |
| `PAYLOAD_DIGEST_CHANGE` | Reviewed digest or manifest changed. | Intake review; not admission. |
| `SCHEMA_OR_FORMAT_CHANGE` | Shape, field, encoding, package, or manifest format changed. | Hold/quarantine review. |
| `TAXONOMY_CHANGE` | Taxonomy/nomenclature/crosswalk signal changed. | Taxonomy steward review. |
| `RIGHTS_OR_TERMS_CHANGE` | License, terms, access, attribution, or redistribution changed. | Suspend and rights review. |
| `SENSITIVITY_OR_STEWARDSHIP_CHANGE` | Sensitivity, cultural authority, stewardship, embargo, or consent changed. | Suspend; fail closed. |
| `CORRECTION_OR_WITHDRAWAL` | Correction, withdrawal, or supersession notice found. | Suspend downstream use and review. |
| `UNKNOWN_CHANGE` | Change cannot be safely classified. | Hold/quarantine. |

Finite outcomes should include `NO_OP`, `CANDIDATE_CHANGE`, `NEEDS_REVIEW`, `HOLD`, `QUARANTINE`, `ABSTAIN`, `DENY`, `SOURCE_STALE`, `SOURCE_UNAVAILABLE`, `SUSPENDED`, or `ERROR`. Empty results must not silently replace negative states.

The same spec digest, source state, baseline, and comparison result should produce the same logical outcome and idempotency key. Duplicate notifications should be linked or suppressed, and rapid upstream churn should trigger debounce/rate controls and review.

[Back to top](#top)

---

## Sensitivity, cultural rights, and no-leak boundary

The following must not appear at exact or reconstructable detail in watcher artifacts:

- rare, protected, threatened, medicinal, ceremonial, culturally significant, or stewardship-controlled plant locations;
- herbarium locality descriptions, collection notes, collector/landowner identities, accession details, or revealing timestamps;
- restoration planting sites, seed-source locations, private parcels, monitoring plots, or rehabilitation locations;
- precise phenology observations or repeated timing that reveals a vulnerable population;
- small counts, cells, screenshots, file names, paths, URLs, query strings, source identifiers, or diffs that enable reconstruction;
- cultural or traditional ecological knowledge, consent restrictions, embargoes, private reviewer notes, or stewardship contacts;
- transform parameters, seeds, grid sizes, radii, masking rules, credentials, tokens, request headers, or signed URLs.

Watcher artifacts should contain only stable governed references, allowlisted non-sensitive metadata, digests, bounded change classes/reason codes, public-safe source-role labels, handoff refs, outcomes, and audit timestamps.

Even public inputs can become sensitive when joined. Hold rather than summarize when a source change could combine with parcel, habitat, soil, hydrology, archaeology, road, settlement, land-management, phenology, specimen, or restoration data to reveal protected locations or knowledge.

AI may draft a bounded review summary only from policy-safe fields. Generated language cannot decide source role, taxonomy authority, cultural consent, sensitivity, materiality, admission, evidence closure, or release.

[Back to top](#top)

---

## Validation, review, and activation

| Gate | Positive case | Required negative cases |
|---|---|---|
| Shape/placement | Accepted schema and one canonical path resolve. | Unknown fields, unsupported version, duplicate active profile, ambiguous precedence. |
| Consumer | Parser and executable target resolve. | Missing consumer, version mismatch, multiple writers. |
| Source | Admitted descriptor and role resolve. | Missing/inactive source, role mismatch, registry conflict. |
| Rights/cultural authority | Terms, attribution, stewardship, and consent are current. | Unknown/expired terms, restricted redistribution, unresolved authority. |
| Taxonomy | Authority/version/crosswalk resolve. | Collision, unknown namespace, stale authority, synonym ambiguity. |
| Time/freshness | Cadence, vintage, stale state, and outage rules are deterministic. | Missing baseline, clock ambiguity, stale source, future timestamps. |
| Checks/materiality | Allowed metadata checks map to one finite outcome. | Forbidden payload fetch, excessive metadata, unknown/conflicting class. |
| Sensitivity | Logs and outputs contain no protected or reconstructable detail. | Rare-plant locality, herbarium clue, cultural knowledge, small-cell/join leak. |
| Receipts | Run/no-op/change/abort lineage and hashes emit. | Missing receipt/ref, inconsistent digest, receipt write failure. |
| No-network | Fixtures replay without live services. | Network access, credentials, production endpoint dependency. |
| Correction/rollback | Correction suspends use and prior state restores deterministically. | Stale baseline retained, candidates continue, unsafe derivative remains. |

`fixtures/domains/flora/plants_drift/` documents synthetic dry-run scenarios, but payload inventory and consumer alignment remain unverified and tests/validators were not run. Before reliance, inspect payloads, prove they are synthetic/public-safe, bind them to named validators, pair stable expected outputs, and prove no-network/no-leak behavior.

An active profile requires pipeline-spec/executable owner, Flora steward, taxonomy/herbarium steward, source-rights/cultural-stewardship reviewer, sensitivity reviewer, temporal/validation reviewer, evidence/policy/release reviewer, and security review where endpoints/logging/notifications change.

Activation must record profile ID/version/digest, authoritative path, parser/consumer versions, source refs, fixture/test evidence, reviewers, effective time, schedule, baseline, monitoring owner, kill switch, prior active version, and rollback target.

[Back to top](#top)

---

## Correction, deactivation, and rollback

### This README change

Before merge, close the draft PR and abandon the branch. After merge, use a transparent revert restoring v0.1 and removing the generated receipt. No runtime rollback is expected because no active profile or runtime changes.

### Future active profile

1. suspend discovery and scheduling;
2. preserve profile/version/digest/activation/run lineage;
3. stop new checks and hold pending candidates;
4. restore a reviewed prior profile and baseline, or remain disabled;
5. re-evaluate source role, rights, cultural authority, taxonomy, sensitivity, freshness, and correction state;
6. inventory affected records, receipts, caches, issues, notifications, indexes, exports, tiles, search, embeddings, and generated summaries;
7. issue correction, withdrawal, supersession, or rollback records;
8. invalidate unsafe/stale derivatives and verify no protected detail remains exposed;
9. record reviewer decisions and rollback outcome.

A source correction, rights change, cultural/stewardship revocation, taxonomy revision, sensitivity reclassification, or discovered leak must suspend affected profiles until impact is reviewed.

[Back to top](#top)

---

## Definition of done

A profile is not active-ready until canonical placement, identity, immutable version/digest, parser, consumer, activation record, source/rights/cultural/taxonomy/sensitivity/cadence/baseline refs, metadata-minimizing checks, deterministic outcomes, receipts, no-network/no-leak/no-admission/correction/rollback tests, substantive CI, CODEOWNERS, separation of duties, monitoring, correction, deactivation, rollback, and generated-work provenance all resolve. Only candidate/quarantine/review/receipt handoffs may be possible.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---:|
| `PIPE-SPEC-FLORA-WATCH-001` | Which schema, parser, state vocabulary, and validation entrypoint are canonical? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-002` | Should canonical specs live here, at `pipeline_specs/flora/`, or under shared `pipeline_specs/watchers/`? | `NEEDS VERIFICATION / ADR` |
| `PIPE-SPEC-FLORA-WATCH-003` | Should either plants-drift placeholder migrate, become a pointer, or retire? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-004` | Is executable ownership domain-specific, shared-plants, or delegated? | `NEEDS VERIFICATION / ADR` |
| `PIPE-SPEC-FLORA-WATCH-005` | Which registry/discovery/precedence/scheduler binds profiles? | `UNKNOWN` |
| `PIPE-SPEC-FLORA-WATCH-006` | Which Flora SourceDescriptors are admitted and active? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-007` | Which roles, rights, terms, cultural-authority, stewardship, and attribution rules are current? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-008` | Which taxonomy/nomenclatural authorities control each profile? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-009` | Which metadata checks and cadence/freshness budgets are allowed per source? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-010` | Which materiality and watcher report/receipt schemas are canonical? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-011` | Where is baseline/state stored, versioned, and restored? | `UNKNOWN` |
| `PIPE-SPEC-FLORA-WATCH-012` | Which rare-plant, locality, cultural-knowledge, restoration-site, count, and join-risk rules are binding? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-013` | Which `plants_drift/` payloads and consumers actually exist? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-014` | Which executable tests and substantive CI prove no-network, no-admission, no-leak, and rollback? | `NEEDS VERIFICATION`; workflow is TODO-only |
| `PIPE-SPEC-FLORA-WATCH-015` | Which CODEOWNERS and separation-of-duties rules govern activation? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-016` | How are taxonomy, rights, cultural authority, sensitivity, role, and schema corrections propagated? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-017` | Which caches, notifications, indexes, embeddings, and summaries invalidate after correction or leakage? | `NEEDS VERIFICATION` |
| `PIPE-SPEC-FLORA-WATCH-018` | Has a Flora watcher deactivation or rollback drill run? | `UNKNOWN` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Blob / status | Relevance |
|---|---|---|
| `pipeline_specs/flora/watchers/README.md` | `e70461b6...` | Prior target. |
| `pipeline_specs/flora/README.md` | `857f1cf4...` | Parent Flora spec boundary. |
| `pipeline_specs/watchers/README.md` | `4a1f642d...` | Shared watcher-spec boundary. |
| `pipeline_specs/flora/plants_drift_watcher.yaml` | `efc75e02...` | Flora placeholder. |
| `pipeline_specs/watchers/plants_drift.yaml` | `fa8ab22f...` | Shared placeholder. |
| `pipelines/domains/flora/watchers/README.md` | `ca41b4fc...` | Flora watcher documentation; implementation unverified. |
| `pipelines/watchers/plants/README.md` | `fc523e15...` | Shared plants watcher; ownership unresolved. |
| `configs/domains/flora/README.md` | `3215a5ee...` | README-only config lane. |
| `data/registry/sources/flora/README.md` | `356cd29c...` | Source controls and topology conflict. |
| `data/receipts/flora/README.md` | `c28c454b...` | Receipt parent/process-memory boundary. |
| `docs/domains/flora/SENSITIVITY.md` | `5143fe3b...` | Deny-by-default doctrine and doc conflict. |
| `policy/domains/flora/README.md` | `b040bff1...` | Broad scaffold. |
| `policy/sensitivity/flora/README.md` | `4c65abec...` | Sensitivity scaffold. |
| `tests/domains/flora/README.md` | `40411105...` | Coverage map; executable coverage unknown. |
| `fixtures/domains/flora/README.md` | `c7c3d770...` | Fixture index. |
| `fixtures/domains/flora/plants_drift/README.md` | `f2e79efa...` | Synthetic scenarios; tests not run. |
| `.github/workflows/domain-flora.yml` | `c7737001...` | Three TODO-only jobs. |
| `.github/CODEOWNERS` | `6adabefc...` | Placeholder ownership. |
| generated-receipt schema | `fba21ed2...` | AI provenance contract. |
| Directory Rules | `2affb080...` | Placement/lifecycle governance. |

Searches found no concrete profile in the requested sublane, no accepted Flora watcher schema, and no spec-specific executable tests. The two external watcher-shaped files were opened and confirmed as seven-line `PROPOSED` placeholders. This was a bounded repository inspection; deployed runtime state, secret-manager state, current upstream terms, branch protection, and off-repository configuration were not proven.

[Back to top](#top)

---

## Changelog

### v0.2 — 2026-07-15

- Replaced the planning-only profile tree with commit-pinned evidence.
- Classified the direct sublane as README-only and inactive.
- Surfaced two external plants-drift placeholders and unresolved declarative/executable ownership.
- Added taxonomy, specimen/occurrence, cultural-rights, sensitivity, metadata-first, finite-outcome, validation, activation, correction, and rollback controls.
- Corrected receipt guidance to `data/receipts/flora/` without selecting a final subtype layout.
- Preserved v0.1 watcher families, non-publication, lifecycle, receipt, review, fixture, test, and open-question concerns.

### v0.1 — 2026-06-13

- Established the initial Flora watcher-spec README and WHAT-versus-HOW boundary.

---

## Maintainer note

Keep this directory declarative, inactive by default, metadata-minimizing, and fail-closed. Do not add executable code, connectors, credentials, source payloads, source descriptors, protected localities, cultural knowledge, restoration-sensitive sites, operational geoprivacy parameters, lifecycle records, receipt instances, EvidenceBundles, catalog records, release decisions, public API/UI code, notifications, or generated source summaries here. Reference governed records by stable identifier and preserve auditable correction and rollback.
