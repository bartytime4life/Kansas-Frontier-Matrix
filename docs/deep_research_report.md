<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-deep-research-report
title: Deep Research Report — Kansas Frontier Matrix Build Reference
type: synthesis_report
version: v0.3
status: draft
owners: <PLACEHOLDER — Docs steward · Architecture steward · Evidence/governance reviewer>
created: 2026-05-26
updated: 2026-06-12
policy_label: public
authority_class: synthesis / orientation; NOT canonical doctrine
placement:
  requested_path: docs/deep_research_report.md
  owning_root: docs/
  directory_rules_basis: docs/ is the responsibility root for human-facing doctrine, architecture, standards, reports, and implementation guidance.
truth_posture: cite-or-abstain with explicit truth labels
implementation_boundary: current live repository state, workflows, dashboards, deployments, package versions, and runtime behavior remain NEEDS VERIFICATION unless checked in the current implementation session.
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/contract-schema-policy-split.md
  - docs/architecture/repository-structure-guiding-document.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - docs/registers/DRIFT_REGISTER.md
tags:
  - kfm
  - deep-research
  - architecture
  - doctrine
  - evidence
  - governance
  - maplibre
  - governed-ai
  - publication
  - rollback
notes:
  - "v0.3 — optimized into a maintainable repository-facing synthesis with clearer truth labels, path posture, open questions, and implementation boundaries."
  - "This document is a reading aid and build reference. It does not supersede accepted doctrine, ADRs, contracts, schemas, policy, release manifests, or verified repo evidence."
] -->

# Deep Research Report — Kansas Frontier Matrix Build Reference

> **Status:** Draft synthesis / orientation
> **Authority:** Not canonical doctrine
> **Use:** Build reference, onboarding map, verification guide, and architecture alignment aid
> **Truth posture:** Cite-or-abstain · evidence-first · implementation-bounded
> **Requested path:** `docs/deep_research_report.md`

---

## Reader note

This document connects the major Kansas Frontier Matrix ideas into one implementation-facing reference.

It is intentionally **not** a replacement for canonical doctrine, accepted ADRs, contracts, schemas, policies, source descriptors, release manifests, or generated proof artifacts. It is a synthesis that explains how those pieces fit together and what must be verified before any claim is treated as implemented.

Where this report says **CONFIRMED**, it means confirmed from available doctrine or supplied artifacts for this synthesis. It does **not** automatically mean the live repository, CI, runtime, dashboard, deployment, route, or package behavior currently does that thing.

---

## Quick status

| Area                        | Status                 | Meaning                                                                                                                                                             |
| --------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KFM purpose                 | **CONFIRMED**          | KFM is a Kansas-first, map-first, time-aware, evidence-first, governed spatial knowledge and publication system.                                                    |
| Core lifecycle              | **CONFIRMED**          | `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` is the governing lifecycle invariant.                                                         |
| Directory placement law     | **CONFIRMED**          | File location encodes responsibility, lifecycle, and governance. Topic alone does not justify a root folder.                                                        |
| Public trust membrane       | **CONFIRMED**          | Public clients must use governed APIs and released artifacts, not RAW/WORK/QUARANTINE or direct internal stores.                                                    |
| AI role                     | **CONFIRMED**          | AI is interpretive and downstream of evidence, policy, review, and release state.                                                                                   |
| Current live implementation | **NEEDS VERIFICATION** | Repo state, route names, workflows, package versions, tests, dashboards, and deployment behavior must be verified in a mounted/current repo session.                |
| This file path              | **PROPOSED**           | `docs/deep_research_report.md` is a reasonable docs-root synthesis location, but exact placement should be checked against current repo conventions and docs index. |

---

## Mini table of contents

1. [Executive determination](#1-executive-determination)
2. [Evidence boundary and truth labels](#2-evidence-boundary-and-truth-labels)
3. [Directory and placement posture](#3-directory-and-placement-posture)
4. [KFM operating law](#4-kfm-operating-law)
5. [System architecture spine](#5-system-architecture-spine)
6. [Data lifecycle and object families](#6-data-lifecycle-and-object-families)
7. [Domain lane model](#7-domain-lane-model)
8. [Map, viewer, and MapLibre boundary](#8-map-viewer-and-maplibre-boundary)
9. [Governed AI boundary](#9-governed-ai-boundary)
10. [Security, policy, release, and rollback](#10-security-policy-release-and-rollback)
11. [Implementation roadmap](#11-implementation-roadmap)
12. [Validation checklist](#12-validation-checklist)
13. [Open questions](#13-open-questions)
14. [Citation key](#14-citation-key)
15. [Maintainer notes](#15-maintainer-notes)

---

## 1. Executive determination

**CONFIRMED — KFM is best understood as a governed evidence-to-publication system, not merely a map application.**

Kansas Frontier Matrix exists to govern how Kansas-relevant sources become claims that are traceable, reviewable, publishable, correctable, reversible, and useful across place, time, policy, and public consequence.

The system’s durable public unit of value is the **inspectable claim**. Maps, tiles, graphs, AI answers, dashboards, scenes, story nodes, exports, reports, and indexes are downstream carriers. They may help users understand evidence, but they do not become sovereign truth.

**CONFIRMED — The trust membrane is the center of the architecture.**

KFM’s public surfaces should expose only governed, released, policy-screened, evidence-resolved material. Public clients and ordinary UI surfaces must not directly read:

* `data/raw/`
* `data/work/`
* `data/quarantine/`
* unpublished candidate records
* canonical/internal stores
* direct model-provider outputs
* unreleased generated artifacts
* sensitive exact geometry that has not passed policy and review

**CONFIRMED — Publication is a state transition, not a file move.**

A record is not public merely because it appears in a public-looking folder, map layer, tile archive, generated page, or API response. Publication requires validation, policy, evidence closure, review, release manifest, proof/receipt trail, correction path, and rollback target.

**PROPOSED — This report should function as a contributor orientation and build-control reference.**

It should help builders answer:

* What is KFM trying to protect?
* Which artifacts are truth-bearing?
* Which artifacts are only carriers?
* Where do files belong?
* What must be verified before implementation claims are made?
* What must exist before public release?
* Which open questions block reliable build-out?

---

## 2. Evidence boundary and truth labels

### 2.1 Evidence boundary

This report is built from supplied KFM doctrine, architecture reports, domain-lane reports, pass atlases, MapLibre guidance, and implementation references.

It does **not** claim current live repository behavior unless that behavior is directly verified in the same implementation session where the claim is made.

The following remain **NEEDS VERIFICATION** before operational use:

* current repository tree
* current branch and commit
* package manager
* CI workflow behavior
* branch protection
* route names
* DTO shapes
* schema bodies
* policy bundle behavior
* validator behavior
* source descriptor inventory
* release manifest inventory
* dashboards
* runtime logs
* deployment posture
* external source currentness
* source rights and license terms

### 2.2 Truth label key

| Label                  | Meaning                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **CONFIRMED**          | Verified from supplied doctrine, current-session artifacts, generated artifacts, or directly inspected evidence.      |
| **PROPOSED**           | A recommended design, path, contract, schema, implementation step, or interpretation not yet verified as implemented. |
| **NEEDS VERIFICATION** | Checkable, but not checked strongly enough to rely on operationally.                                                  |
| **UNKNOWN**            | Not established from available evidence.                                                                              |
| **CONFLICTED**         | Two authorities or conventions disagree; do not silently smooth over the conflict.                                    |
| **DENY**               | Policy blocks exposure or action.                                                                                     |
| **ABSTAIN**            | Evidence is insufficient, inaccessible, unsafe, or outside the allowed scope.                                         |
| **ERROR**              | System, integrity, validation, runtime, or dependency failure.                                                        |

### 2.3 No-overclaim rule

A KFM document may describe a proposed file, schema, route, validator, policy, dashboard, or workflow. That does not prove it exists.

Before saying “KFM contains X” or “the system does Y,” verify at least one of the following:

* file existence
* schema body
* contract body
* policy rule
* test fixture
* validation output
* workflow run
* generated receipt
* release manifest
* proof pack
* runtime log
* deployment artifact
* reviewed source descriptor
* current repo commit evidence

---

## 3. Directory and placement posture

### 3.1 Requested path

**Requested path:** `docs/deep_research_report.md`

**Placement status:** **PROPOSED / reasonable**

The `docs/` root is the appropriate responsibility root for a human-facing synthesis and build-reference report. This file is not a schema, policy bundle, contract, source descriptor, release artifact, proof object, receipt, fixture, or runtime component.

### 3.2 Naming note

The requested filename uses underscores: `deep_research_report.md`.

That is acceptable if current repo convention permits it. If the repository standard prefers hyphenated Markdown filenames, the cleaner long-term path may be:

```text
docs/deep-research-report.md
```

Do not rename automatically without checking the current docs index, links, and any references in README files.

### 3.3 Directory Rules basis

KFM placement is governance. File location encodes:

* ownership
* responsibility root
* lifecycle phase
* authority class
* review expectations
* rollback/migration behavior

Topic alone does not justify a root folder. Domain and subject depth should live inside responsibility roots, not as new top-level convenience folders.

### 3.4 Drift handling

If this file conflicts with current repo placement convention:

1. Do not treat the current repo shape as canon by default.
2. Check Directory Rules and accepted ADRs.
3. Record the conflict in `docs/registers/DRIFT_REGISTER.md`.
4. Either migrate the file or open an ADR/migration note.
5. Preserve old links through redirects, index notes, or deprecation references where needed.

---

## 4. KFM operating law

### 4.1 Core invariant

```text
Pre-RAW
  → RAW
  → WORK / QUARANTINE
  → PROCESSED
  → CATALOG / TRIPLET
  → PUBLISHED
```

The only normal off-spine branch is quarantine. Promotion to published state is not a copy operation; it is a governed decision.

### 4.2 Public access rule

Public clients use governed interfaces and released artifacts.

They must not directly access:

* RAW data
* WORK data
* QUARANTINE data
* unpublished candidates
* source-native sensitive material
* internal canonical stores
* direct model output
* unreleased generated layers
* unreviewed artifacts

### 4.3 Evidence rule

EvidenceBundle outranks generated text.

When a public or semi-public claim depends on evidence, the claim should resolve through an EvidenceRef to an EvidenceBundle or should abstain.

### 4.4 AI rule

AI may summarize, compare, explain, narrow, and draft.

AI must not decide:

* truth
* source authority
* rights
* sensitivity
* review state
* release state
* rollback state
* public exposure

### 4.5 Publication rule

A public release needs support appropriate to consequence:

* identity
* source role
* rights
* sensitivity
* validation
* provenance
* integrity
* receipts
* proof objects
* policy decisions
* review records
* release manifest
* correction path
* rollback target

### 4.6 Sensitive-domain rule

When sensitivity is unclear, KFM should prefer:

* quarantine
* redaction
* generalization
* staged access
* delayed release
* denial
* abstention

This applies especially to:

* archaeology and cultural heritage
* burial and sacred sites
* tribal and sovereignty-sensitive material
* living-person data
* DNA/genomic data
* rare species locations
* critical infrastructure
* private-property-sensitive exposure
* public safety vulnerabilities
* military/security-sensitive details

---

## 5. System architecture spine

### 5.1 Responsibility roots

KFM should be understood as a responsibility-root monorepo.

Root folders are not topic buckets. They are authority boundaries.

A simplified responsibility map:

| Root              | Responsibility                                                                                       |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| `docs/`           | Human-readable doctrine, architecture, standards, runbooks, registers, and explanatory reports.      |
| `contracts/`      | Semantic meaning and object-family contracts.                                                        |
| `schemas/`        | Machine-checkable shapes, typically under `schemas/contracts/v1/...`.                                |
| `policy/`         | Policy-as-code, sensitivity logic, release logic, rights logic, runtime decisions.                   |
| `tests/`          | Validation and regression tests.                                                                     |
| `fixtures/`       | Controlled examples and negative cases.                                                              |
| `tools/`          | Developer and validation tooling.                                                                    |
| `scripts/`        | Operational scripts and glue where appropriate.                                                      |
| `apps/`           | Deployable applications such as governed API, explorer UI, admin, review console, workers, and CLI.  |
| `packages/`       | Shared implementation packages.                                                                      |
| `connectors/`     | Source connectors and watchers.                                                                      |
| `pipelines/`      | Pipeline implementations.                                                                            |
| `pipeline_specs/` | Pipeline specifications and declarative run plans.                                                   |
| `data/`           | Lifecycle data, registry material, catalog projections, receipts, proofs, tiles, and published data. |
| `release/`        | Release candidates, release decisions, manifests, rollback cards, and correction records.            |
| `runtime/`        | Runtime configuration and runtime envelopes.                                                         |
| `infra/`          | Infrastructure definitions.                                                                          |
| `configs/`        | Configuration defaults and environment-specific non-secret configuration.                            |
| `migrations/`     | Database/data migration scripts and notes.                                                           |

### 5.2 Contracts, schemas, and policy split

KFM should preserve a clear split:

| Layer             | Root         | Meaning                                                                          |
| ----------------- | ------------ | -------------------------------------------------------------------------------- |
| Semantic contract | `contracts/` | What the object means and why it exists.                                         |
| Machine schema    | `schemas/`   | What shape the object must satisfy.                                              |
| Policy            | `policy/`    | Whether the object/action/exposure is allowed, denied, restricted, or abstained. |
| Fixtures          | `fixtures/`  | Examples and counterexamples.                                                    |
| Tests             | `tests/`     | Proof that contracts, schemas, and policy are enforced.                          |

Do not create parallel homes for schemas, contracts, policy, sources, registries, releases, proofs, or receipts without an accepted ADR or migration note.

### 5.3 Canonical objects

KFM’s architecture repeatedly depends on the following object families:

| Object family              | Role                                                                                               |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| `SourceDescriptor`         | Declares source identity, role, rights, sensitivity, cadence, and admission posture.               |
| `EvidenceBundle`           | Evidence closure supporting claims.                                                                |
| `EvidenceRef`              | Public-safe reference to evidence closure.                                                         |
| `RunReceipt`               | Records tool or pipeline execution with inputs, outputs, versions, hashes, and policy context.     |
| `EventEnvelope`            | Pre-RAW source-change or watcher event envelope.                                                   |
| `EventRunReceipt`          | Admission-edge receipt for source-change events.                                                   |
| `TransformReceipt`         | Records transformation from one lifecycle phase to another.                                        |
| `RedactionReceipt`         | Records suppression, generalization, or removal for sensitivity/policy reasons.                    |
| `PolicyDecision`           | Records policy result and reason.                                                                  |
| `ValidationReport`         | Records schema, contract, data, or artifact validation result.                                     |
| `CitationValidationReport` | Records whether claims resolve to required evidence.                                               |
| `ReleaseManifest`          | Defines released assets, evidence, policy, review, integrity, correction, and rollback references. |
| `PromotionDecision`        | Records publication-gate decision.                                                                 |
| `RollbackCard`             | Defines how to reverse or repoint a release safely.                                                |
| `CorrectionNotice`         | Records public correction, supersession, or withdrawal.                                            |
| `LayerManifest`            | Describes a map layer and its evidence/release/policy bindings.                                    |
| `TileArtifactManifest`     | Describes tile artifacts, digests, provenance, and release state.                                  |
| `EvidenceDrawerPayload`    | UI-facing evidence explanation payload.                                                            |
| `RuntimeResponseEnvelope`  | Finite AI/API response envelope: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.                          |

---

## 6. Data lifecycle and object families

### 6.1 Pre-RAW

Pre-RAW handles source-change signals before data admission.

Typical artifacts:

* `EventEnvelope`
* `PrefilterOutput`
* `EventRunReceipt`
* source-head check
* source-cadence check
* rights/sensitivity precheck

Pre-RAW prevents watchers from becoming publishers.

### 6.2 RAW

RAW preserves source-native capture.

Rules:

* keep source-native material separate
* preserve hashes and source timestamps
* attach intake/admission receipts
* do not serve RAW to public clients
* do not treat RAW as publishable truth

### 6.3 WORK

WORK is for transformation, normalization, QA, reconciliation, staging, and review.

Rules:

* every transform should emit a receipt
* no public reads
* invalid or sensitive material may branch to quarantine
* candidate interpretation remains candidate until promotion

### 6.4 QUARANTINE

QUARANTINE holds unsafe, unclear, invalid, sensitive, disputed, or policy-blocked material.

Quarantine is not failure. It is a governed fail-closed state.

Reasons may include:

* rights unclear
* sensitivity unclear
* source identity weak
* schema failure
* integrity mismatch
* contradictory evidence
* exact sensitive geometry
* living-person exposure
* cultural/sovereignty concern
* public-safety concern

### 6.5 PROCESSED

PROCESSED contains normalized candidates.

Rules:

* schema-valid is not the same as publishable
* normalized data still needs evidence closure
* derived data must retain provenance
* public exposure is still denied unless released

### 6.6 CATALOG / TRIPLET

CATALOG and TRIPLET are evidence and discovery projections.

They should support:

* source discovery
* dataset discovery
* provenance graph
* claim-to-evidence resolution
* cross-domain joins
* graph/triplet projection
* STAC/DCAT/PROV-aligned publication surfaces

They are not substitutes for release approval.

### 6.7 PUBLISHED

PUBLISHED contains public-safe materialization.

A published object should have:

* release manifest
* policy decision
* evidence closure
* proof/receipt trail
* validation result
* review record
* correction path
* rollback target

---

## 7. Domain lane model

### 7.1 Domain placement law

Domains are lanes inside responsibility roots.

A domain should not become a root-level folder merely because it is large or important.

For example:

| Domain concern               | Good responsibility-root pattern             |
| ---------------------------- | -------------------------------------------- |
| Hydrology docs               | `docs/domains/hydrology/...`                 |
| Hydrology contracts          | `contracts/domains/hydrology/...`            |
| Hydrology schemas            | `schemas/contracts/v1/domains/hydrology/...` |
| Hydrology policy             | `policy/domains/hydrology/...`               |
| Hydrology fixtures           | `fixtures/domains/hydrology/...`             |
| Hydrology tests              | `tests/domains/hydrology/...`                |
| Hydrology processed data     | `data/processed/hydrology/...`               |
| Hydrology release candidates | `release/candidates/hydrology/...`           |

Exact homes remain subject to Directory Rules, accepted ADRs, and current repo conventions.

### 7.2 Domain lanes

KFM’s domain architecture includes, at minimum, the following lane families:

| Lane                                      | Primary concern                                                                     | Key publication caution                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Hydrology                                 | Water bodies, watersheds, streamflow, groundwater, flood context.                   | Do not collapse observed, modeled, regulatory, and historical water evidence.                   |
| Soil                                      | Soil map units, horizons, properties, capability, moisture context.                 | Preserve source and scale limits; avoid overclaiming field-level precision.                     |
| Habitat                                   | Habitat patches, suitability, connectivity, restoration context.                    | Avoid exposing sensitive habitat/rare-species locations.                                        |
| Fauna                                     | Species, occurrence evidence, range, monitoring, conservation context.              | Exact sensitive occurrences default to restriction/denial.                                      |
| Flora                                     | Plant taxonomy, specimens, rare plants, invasives, phenology.                       | Rare plants and sensitive locations require redaction/generalization.                           |
| Agriculture                               | Crop, field, CDL/NASS, irrigation, yield, land-use indicators.                      | Aggregates and field-level claims need source-role clarity.                                     |
| Geology / Natural resources               | Bedrock, surficial geology, minerals, aquifers, resources.                          | Do not substitute context layers for direct observed truth.                                     |
| Atmosphere / Air                          | Weather, climate, smoke, air quality, emissions, atmospheric hazards.               | Observed, modeled, regulatory, and fused products are not interchangeable.                      |
| Hazards                                   | Flood, fire, storm, drought, heat, seismic, resilience context.                     | KFM is not an emergency alert system unless separately governed.                                |
| Roads / Rail / Trade routes               | Transportation networks, corridors, routes, logistics, restrictions.                | Current operational restrictions and infrastructure details need sensitivity review.            |
| Settlements / Infrastructure              | Municipalities, historic settlements, assets, facilities, dependencies.             | Critical infrastructure and private-property exposure require public-safe generalization.       |
| Archaeology / Cultural heritage           | Sites, surveys, cultural resources, historic interpretation.                        | Exact site locations default to denial unless specifically reviewed and generalized.            |
| People / Genealogy / DNA / Land           | People assertions, genealogy evidence, DNA restrictions, land ownership assertions. | Living-person and DNA-derived data default to deny/restrict; assessor rows are not title truth. |
| Frontier Matrix                           | Cross-domain historical/spatial analytical layer.                                   | Derived matrix indicators must remain evidence-bound and time-aware.                            |
| Planetary / 3D / Digital twin / Synthetic | 3D, terrain, scene, simulation, planetary or synthetic views.                       | 3D scenes are high-exposure carriers, not source truth.                                         |

### 7.3 Source-role anti-collapse

KFM should preserve source-role distinctions.

Useful source roles include:

* observed
* regulatory
* modeled
* aggregate
* administrative
* candidate
* synthetic
* historical interpretation
* operational notice
* scientific interpretation
* monitoring reference

Promotion may improve review state, release state, or exposure posture. It should not silently upgrade the original source role.

---

## 8. Map, viewer, and MapLibre boundary

### 8.1 MapLibre role

MapLibre is a renderer and interaction runtime.

It is not:

* the truth store
* the source registry
* the policy engine
* the citation authority
* the review authority
* the publication authority
* the AI authority

### 8.2 Map shell rule

The map shell should only load layers that are:

* released or explicitly preview-scoped
* policy-screened
* backed by manifests
* validated
* tied to evidence references where claims are made
* safe for the requested user/exposure context

### 8.3 Evidence Drawer rule

Popups are not proof.

The Evidence Drawer should expose:

* claim summary
* EvidenceRef
* EvidenceBundle metadata
* source role
* source date/cadence
* confidence / uncertainty
* policy posture
* release state
* citation validation status
* correction/supersession state
* rollback or release reference where applicable

### 8.4 Tile and artifact governance

Tiles, PMTiles, MVT, COGs, rasters, vector layers, styles, screenshots, 3D scenes, and story exports are artifacts.

Before public use, map artifacts should have:

* artifact manifest
* digest/hash
* source ledger reference
* build receipt
* validation report
* release manifest reference
* policy decision
* rollback target

### 8.5 Anti-patterns

Avoid:

* hiding sensitive geometry only with style rules
* loading unreleased PMTiles directly in a public map
* using screenshots as proof
* treating rendered features as evidence closure
* giving map popups the authority of the Evidence Drawer
* allowing browser clients to call model providers directly
* using convenience layers to bypass release gates

---

## 9. Governed AI boundary

### 9.1 AI operating order

Governed AI should follow this order:

1. Define scope.
2. Retrieve released evidence.
3. Resolve EvidenceRef to EvidenceBundle.
4. Apply policy and sensitivity checks.
5. Validate citations.
6. Generate bounded response.
7. Emit finite outcome.
8. Record AIReceipt / RunReceipt where required.

### 9.2 Runtime outcomes

AI and governed runtime surfaces should use finite outcomes:

| Outcome   | Meaning                                                                           |
| --------- | --------------------------------------------------------------------------------- |
| `ANSWER`  | Evidence and policy support a bounded answer.                                     |
| `ABSTAIN` | Evidence is missing, insufficient, stale, inaccessible, or not safe to summarize. |
| `DENY`    | Policy blocks the request or exposure.                                            |
| `ERROR`   | System, validation, integrity, or runtime failure.                                |

### 9.3 AI cannot authorize

AI cannot authorize:

* source admission
* rights acceptance
* sensitivity downgrade
* release approval
* correction closure
* rollback decision
* reviewer separation bypass
* direct publication

### 9.4 Focus Mode

Focus Mode should be a governed API feature, not a direct model chat bolted onto the map.

A Focus Mode answer should carry:

* scope
* resolved evidence references
* cited claims
* uncertainty
* policy posture
* release state
* finite outcome
* refusal/abstention reason when applicable
* debug/receipt references for maintainers where appropriate

---

## 10. Security, policy, release, and rollback

### 10.1 Policy-as-code

Policy should decide:

* allow
* deny
* restrict
* redact
* generalize
* delay
* abstain
* require review
* quarantine

Policy outputs should become recorded objects where consequence requires auditability.

### 10.2 Release gate checklist

A release candidate should not become published until the following are present or deliberately waived with review:

| Gate            | Required support                            |
| --------------- | ------------------------------------------- |
| Source identity | SourceDescriptor / source ledger reference  |
| Rights          | rights review or source terms posture       |
| Sensitivity     | sensitivity profile and PolicyDecision      |
| Schema/contract | validation report                           |
| Evidence        | EvidenceBundle / EvidenceRef closure        |
| Citations       | citation validation                         |
| Integrity       | hashes, signatures, manifest checks         |
| Review          | reviewer record / separation where required |
| Release         | ReleaseManifest                             |
| Correction      | CorrectionNotice path                       |
| Rollback        | RollbackCard or rollback target             |

### 10.3 Rollback

Rollback is not deletion.

Rollback should preserve:

* what was released
* why it was released
* why it was withdrawn, superseded, or repointed
* what replaces it
* how public clients discover the current state
* how auditors reconstruct prior state

### 10.4 Correction

Corrections should be public enough for the exposure class.

A correction should identify:

* affected release
* affected claims or layers
* reason
* evidence change
* policy change if any
* replacement release if any
* effective time
* reviewer
* rollback or supersession link

---

## 11. Implementation roadmap

### 11.1 First build priority

**PROPOSED — Start with schema, fixture, policy, and validator foundations before UI polish.**

A safe first implementation slice should prove:

* one SourceDescriptor
* one EvidenceBundle
* one EvidenceRef
* one PolicyDecision
* one RuntimeResponseEnvelope
* one ReleaseManifest fixture
* one RollbackCard fixture
* one CitationValidationReport
* one valid case
* one abstain case
* one deny case
* one error case

### 11.2 Recommended thin slice

**PROPOSED — Hydrology or habitat/fauna remains the cleanest proof lane.**

A thin slice should avoid live sensitive data at first. Use controlled fixtures and public-safe geometry.

Minimum slice:

1. SourceDescriptor fixture.
2. RAW fixture.
3. TransformReceipt fixture.
4. PROCESSED fixture.
5. EvidenceBundle fixture.
6. PolicyDecision fixture.
7. LayerManifest fixture.
8. ReleaseManifest fixture.
9. EvidenceDrawerPayload fixture.
10. Governed API response fixture.
11. Map layer preview using only released/mock-safe data.
12. Tests proving deny/abstain/error outcomes.

### 11.3 Documentation workstream

Priority docs to maintain alongside implementation:

* `docs/doctrine/directory-rules.md`
* `docs/doctrine/trust-membrane.md`
* `docs/doctrine/lifecycle-law.md`
* `docs/doctrine/truth-posture.md`
* `docs/architecture/contract-schema-policy-split.md`
* `docs/architecture/repository-structure-guiding-document.md`
* `docs/registers/DRIFT_REGISTER.md`
* `docs/sources/catalog/README.md`
* `docs/domains/README.md`
* domain-lane READMEs
* release/correction/rollback runbooks

### 11.4 Build order

| Order | Workstream                         | Why                                                      |
| ----: | ---------------------------------- | -------------------------------------------------------- |
|     1 | Directory and ADR reconciliation   | Prevents path drift from becoming architecture.          |
|     2 | Object-family contracts            | Establishes semantic meaning.                            |
|     3 | Schemas and fixtures               | Makes validation testable.                               |
|     4 | Policy profiles                    | Makes allow/deny/restrict explicit.                      |
|     5 | Validators                         | Turns doctrine into enforceable checks.                  |
|     6 | Receipts and proof objects         | Makes transformations auditable.                         |
|     7 | Release manifest and rollback card | Makes publication reversible.                            |
|     8 | Governed API fixtures              | Defines public trust membrane.                           |
|     9 | Evidence Drawer payload            | Makes trust visible.                                     |
|    10 | Map shell integration              | Renders only released/policy-safe artifacts.             |
|    11 | Focus Mode                         | Adds AI interpretation after evidence/policy are stable. |

---

## 12. Validation checklist

### 12.1 Document validation

For this file:

* [ ] File path checked against Directory Rules and current repo docs index.
* [ ] KFM meta block present and valid.
* [ ] No unsupported implementation claims.
* [ ] Truth labels applied where needed.
* [ ] Current-session evidence boundary stated.
* [ ] Citation key present.
* [ ] Open questions preserved.
* [ ] No raw sensitive data included.
* [ ] No exact sensitive locations included.
* [ ] No direct model-output-as-truth language.
* [ ] No root-level domain folder proposals.
* [ ] No parallel schema/contract/policy/release/proof homes proposed without ADR note.

### 12.2 Repo validation

Before merging this file:

* [ ] Confirm `docs/deep_research_report.md` does not conflict with naming conventions.
* [ ] Check whether `docs/deep-research-report.md` already exists.
* [ ] Check whether this belongs under `docs/architecture/`, `docs/reports/`, or `docs/reference/` instead.
* [ ] Update any docs index or README that should link to it.
* [ ] Add a drift-register note if the repo lacks a clear home for synthesis reports.
* [ ] Run Markdown lint.
* [ ] Run link/reference checks.
* [ ] Confirm no generated citation tokens are broken.
* [ ] Confirm no stale “current repo” claims remain.

### 12.3 Architecture validation

Before implementing recommendations from this report:

* [ ] Verify accepted ADR list.
* [ ] Verify schema-home rule.
* [ ] Verify policy root convention.
* [ ] Verify source registry home.
* [ ] Verify release manifest home.
* [ ] Verify proof/receipt separation.
* [ ] Verify governed API route conventions.
* [ ] Verify MapLibre component homes.
* [ ] Verify current CI validation jobs.
* [ ] Verify package manager and test runner.
* [ ] Verify public-sensitive policy profiles.
* [ ] Verify correction and rollback runbooks.

---

## 13. Open questions

| ID         | Question                                                                                                                                                          | Status                                       | Resolution path                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------- |
| OQ-DRR-001 | Should this file remain at `docs/deep_research_report.md`, move to `docs/architecture/deep-research-report.md`, or become `docs/reports/deep-research-report.md`? | **NEEDS VERIFICATION**                       | Inspect current repo docs organization and Directory Rules.                 |
| OQ-DRR-002 | Is underscore naming accepted for Markdown files in `docs/`, or should this be hyphenated?                                                                        | **NEEDS VERIFICATION**                       | Inspect current repo naming conventions and references.                     |
| OQ-DRR-003 | What is the current accepted ADR inventory?                                                                                                                       | **NEEDS VERIFICATION**                       | Enumerate `docs/adr/` in mounted repo.                                      |
| OQ-DRR-004 | Is `policy/` singular fully canonical in the current repo, or do legacy `policies/` paths still exist?                                                            | **NEEDS VERIFICATION / POSSIBLY CONFLICTED** | Repo scan plus drift register entry if needed.                              |
| OQ-DRR-005 | Are `schemas/contracts/v1/...` paths implemented consistently?                                                                                                    | **NEEDS VERIFICATION**                       | Repo scan, ADR check, schema index check.                                   |
| OQ-DRR-006 | Which object-family contracts already exist?                                                                                                                      | **NEEDS VERIFICATION**                       | Inspect `contracts/`, `schemas/`, `fixtures/`, and `tests/`.                |
| OQ-DRR-007 | Which validators are merge-blocking?                                                                                                                              | **NEEDS VERIFICATION**                       | Inspect `.github/workflows/`, `Makefile`, CI logs, and test configs.        |
| OQ-DRR-008 | Are ReleaseManifest, PromotionDecision, RollbackCard, and CorrectionNotice implemented as schemas and fixtures?                                                   | **NEEDS VERIFICATION**                       | Inspect release contracts, schemas, fixtures, and tests.                    |
| OQ-DRR-009 | Is Focus Mode implemented, mocked, planned, or only documented?                                                                                                   | **NEEDS VERIFICATION**                       | Inspect `apps/governed-api/`, `apps/explorer-web/`, and UI/API docs.        |
| OQ-DRR-010 | Which domain lane is the current proof lane?                                                                                                                      | **NEEDS VERIFICATION**                       | Inspect current roadmap, issues, milestones, and release candidates.        |
| OQ-DRR-011 | Are MapLibre tile/layer manifests validated before public load?                                                                                                   | **NEEDS VERIFICATION**                       | Inspect map runtime, sidecar validators, layer registry, and release gates. |
| OQ-DRR-012 | Does the current repo have a source-role vocabulary ADR?                                                                                                          | **NEEDS VERIFICATION**                       | Inspect ADRs and source catalog docs.                                       |
| OQ-DRR-013 | Does the current repo have a sensitivity-tier ADR?                                                                                                                | **NEEDS VERIFICATION**                       | Inspect ADRs, policy profiles, and domain-lane docs.                        |
| OQ-DRR-014 | What is the canonical source registry home?                                                                                                                       | **NEEDS VERIFICATION**                       | Inspect Directory Rules, source catalog, data registry, and ADRs.           |
| OQ-DRR-015 | Are correction and rollback paths visible in public-facing documentation?                                                                                         | **NEEDS VERIFICATION**                       | Inspect release docs, public API docs, and Evidence Drawer payloads.        |

---

## 14. Citation key

This report uses short citation keys to avoid brittle generated citation tokens inside repository Markdown.

| Key                        | Source                                                       |
| -------------------------- | ------------------------------------------------------------ |
| `[DIRRULES]`               | Directory Rules / responsibility-root doctrine               |
| `[TRUTH]`                  | Truth posture doctrine                                       |
| `[TRUST]`                  | Trust membrane doctrine                                      |
| `[LIFECYCLE]`              | Lifecycle law doctrine                                       |
| `[CONTRACT-SCHEMA-POLICY]` | Contract/schema/policy split architecture                    |
| `[GREENFIELD]`             | Kansas Frontier Matrix Definitive Greenfield Building Plan   |
| `[PIPELINE]`               | Kansas Frontier Matrix Pipeline Living Implementation Manual |
| `[ENCY]`                   | KFM Encyclopedia / domain and capability encyclopedia        |
| `[IMPL-REF]`               | KFM Implementation Reference                                 |
| `[MAPLIBRE]`               | KFM MapLibre Operating Architecture / Master MapLibre atlas  |
| `[GAI]`                    | KFM Governed AI reports                                      |
| `[UIAI]`                   | KFM Whole UI + Governed AI Expansion report                  |
| `[PASS18]`                 | KFM Components Pass 18                                       |
| `[PASS19]`                 | KFM Components Pass 19 / retained lineage where available    |
| `[PASS20]`                 | KFM Components Pass 20 combined / Part 2 dossier             |
| `[DOM-HYD]`                | Hydrology domain report                                      |
| `[DOM-SOIL]`               | Soil domain report                                           |
| `[DOM-HAB]`                | Habitat domain report                                        |
| `[DOM-FAUNA]`              | Fauna domain report                                          |
| `[DOM-FLORA]`              | Flora domain report                                          |
| `[DOM-AG]`                 | Agriculture domain report                                    |
| `[DOM-GEO]`                | Geology / natural resources domain report                    |
| `[DOM-AIR]`                | Atmosphere / air domain report                               |
| `[DOM-HAZ]`                | Hazards domain report                                        |
| `[DOM-ROADS]`              | Roads / rail / trade routes domain report                    |
| `[DOM-SETTLE]`             | Settlements / infrastructure domain report                   |
| `[DOM-ARCH]`               | Archaeology domain report                                    |
| `[DOM-PEOPLE]`             | People / genealogy / DNA / land report                       |
| `[DDD]`                    | Domain-Driven Design reference                               |
| `[GIS-PRIMER]`             | GIS/cartography primer reference                             |
| `[TEMPORAL-SQL]`           | Time-oriented database reference                             |
| `[WEB-API]`                | Web API design reference                                     |

---

## 15. Maintainer notes

### 15.1 Why this report exists

KFM has enough doctrine, domain reports, pass atlases, and implementation plans that contributors need a compact orientation layer.

This file should answer “how the pieces fit” without pretending to be the pieces.

### 15.2 What this report must not become

This report must not become:

* a replacement for Directory Rules
* a replacement for ADRs
* a schema index
* a policy index
* a source registry
* a release manifest
* a proof pack
* an implementation-status dashboard
* a runtime behavior claim
* a shortcut around review

### 15.3 Update cadence

Update this report when:

* Directory Rules change
* a major ADR is accepted
* schema-home or policy-home decisions change
* a new proof lane becomes canonical
* public trust membrane behavior changes
* MapLibre architecture changes
* governed AI boundaries change
* release/correction/rollback process changes
* a major domain lane moves from proposal to implemented proof

### 15.4 Safe edit pattern

When updating:

1. Preserve the meta block.
2. Update the `updated:` date.
3. Keep truth labels current.
4. Move stale implementation claims to **NEEDS VERIFICATION**.
5. Add new open questions rather than guessing.
6. Keep source keys short and stable.
7. Do not paste raw sensitive data.
8. Do not add exact sensitive locations.
9. Do not add direct generated citations that will break outside the chat.
10. Record material changes in the changelog below.

---

## 16. Changelog

| Version |       Date | Change                                                                                                                                                                            |
| ------- | ---------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| v0.3    | 2026-06-12 | Optimized as a repository-ready synthesis with stronger path posture, truth-label discipline, implementation boundary, roadmap, validation checklist, and open-question register. |
| v0.2    | 2026-05-26 | Refreshed prior deep research/build synthesis with clearer doctrine and implementation boundaries.                                                                                |
| v0.1    | 2026-05-26 | Initial research-run synthesis.                                                                                                                                                   |

---

## 17. Footer

```yaml
kfm_footer:
  document: "Deep Research Report — Kansas Frontier Matrix Build Reference"
  requested_path: "docs/deep_research_report.md"
  version: "v0.3"
  status: "draft"
  authority_class: "synthesis / orientation; NOT canonical doctrine"
  applies_to_repo_state: "doctrine-level and planning-level only unless separately verified"
  truth_posture: "cite-or-abstain with explicit truth labels"
  next_review_triggers:
    - "Directory Rules update"
    - "ADR acceptance affecting roots, schemas, contracts, policy, release, or source roles"
    - "new implementation proof lane"
    - "governed API / MapLibre / Focus Mode boundary change"
    - "release/correction/rollback process change"
```

**Authority reminder:** This document is a synthesis and orientation aid. If it conflicts with accepted doctrine, accepted ADRs, contracts, schemas, policy, release manifests, proof objects, or current verified repo evidence, those sources win.
