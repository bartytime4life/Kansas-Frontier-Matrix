<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-archaeology-readme
title: contracts/archaeology/ — Archaeology Semantic Contracts
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Archaeology steward · Contract steward · Schema steward · Sensitivity reviewer · Cultural/sovereignty reviewer · Rights-holder representative · Evidence steward · Validator steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-09-07
policy_label: public; contracts; archaeology; cultural-heritage; compatibility-path; sensitive-domain; deny-by-default; candidate-not-site; exact-location-denial; release-gates
related:
  - ../README.md
  - ../domains/archaeology/README.md
  - ../domains/archaeology/OBJECT_MAP.md
  - ../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../docs/domains/archaeology/ARCHITECTURE.md
  - ../../docs/domains/archaeology/SENSITIVITY.md
  - ../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../docs/domains/archaeology/VALIDATORS.md
  - ../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../schemas/contracts/v1/domains/archaeology/
  - ../../policy/domains/archaeology/
  - ../../policy/sensitivity/archaeology/
  - ../../fixtures/domains/archaeology/
  - ../../tests/domains/archaeology/
  - ../../tools/validators/
  - ../../data/receipts/archaeology/
  - ../../release/
tags: [kfm, contracts, archaeology, cultural-heritage, semantic-contracts, compatibility-path, sensitive-domain, deny-by-default, candidate-not-site, redaction, sovereignty, care, exact-location-denial, release-gates, governance]
notes:
  - "This is a compatibility/lineage README. Current Directory-Rules-aligned semantic contracts live under contracts/domains/archaeology/."
  - "Repository evidence shows mixed maturity: most domain schemas and policy files are PROPOSED scaffolds, several focused fixture validators are executable, and pipeline/package/API implementation remains incomplete or placeholder-only."
  - "No contract, schema, policy, validator, receipt, review, release, API, UI, or public-surface authority is created by this README."
  - "Google Drive archaeology and Atlas material is lineage-only; GitHub repository evidence controls current paths, statuses, and implementation claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Semantic Contracts

> Compatibility and lineage README for Archaeology / Cultural Heritage semantic contracts. This directory records object meaning and trust boundaries; it does not define machine shape, policy execution, source truth, cultural authority, exact-location release, API behavior, UI behavior, or publication permission.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: compatibility" src="https://img.shields.io/badge/path-compatibility%20%2F%20lineage-lightgrey">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-brown">
  <img alt="Sensitivity: deny by default" src="https://img.shields.io/badge/sensitivity-deny--by--default-critical">
  <img alt="Authority: non-authoritative" src="https://img.shields.io/badge/authority-non--authoritative-blue">
</p>

\`contracts/archaeology/\`

## Quick jumps

[Status](#status) · [Scope and authority](#scope-and-authority) · [Path posture](#path-posture) · [Current repository snapshot](#current-repository-snapshot) · [Object-family spine](#object-family-spine) · [Semantic rules](#semantic-rules) · [Sensitivity and publication](#sensitivity-and-publication) · [Lifecycle](#lifecycle) · [Validation maturity](#validation-maturity) · [Evidence basis](#evidence-basis) · [Open verification](#open-verification) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** \`draft\` / \`repository-grounded\` / \`mixed-maturity\`  
> **Path:** \`contracts/archaeology/\`  
> **Path posture:** \`COMPATIBILITY\` / \`LINEAGE\`; current Archaeology path guidance prefers \`contracts/domains/archaeology/\`.  
> **Truth posture:** the compatibility README, canonical semantic-contract lane, 32 semantic Markdown files, 40 domain schema files, mixed validator/test fixtures, and bounded Archaeology workflow surfaces are confirmed in the inspected repository tree. Full policy evaluation, source activation, pipeline execution, cultural-review authority, public release, API runtime behavior, and UI behavior remain independently unproven.

This README corrects the earlier directory snapshot. The target file was already populated; it was not a blank contract. The stale claims were the inventory, path, and rollback assertions—not the existence of this document.

---

## Scope and authority

This path describes semantic expectations for Archaeology and Cultural Heritage object families, including:

- what an object means and what it must not be confused with;
- identity, source role, temporal, provenance, and evidence expectations;
- candidate-versus-confirmed distinctions;
- sensitivity, rights, CARE, sovereignty, consent, embargo, and revocation posture;
- redaction/generalization, cultural/steward review, release, correction, and rollback expectations.

Authority is split across responsibility roots:

| Surface | Establishes | Does not establish |
|---|---|---|
| This compatibility README | Directory boundary, semantic intent, and lineage notes. | Canonical migration, machine shape, policy execution, review approval, release, or publication. |
| \`contracts/domains/archaeology/\` | Current Directory-Rules-aligned semantic contract home and object-family meaning. | JSON Schema, policy decisions, source admission, or release permission. |
| \`schemas/contracts/v1/domains/archaeology/\` | Machine-checkable shape where a schema is actually defined. | Evidence truth, cultural authority, policy execution, or public release. |
| \`docs/domains/archaeology/\` | Domain doctrine, path guidance, sensitivity, lifecycle, API/UI, validator, and publication guidance. | Runtime enforcement or approval. |
| \`policy/domains/archaeology/\` and \`policy/sensitivity/archaeology/\` | Policy rule candidates and sensitivity boundaries. | An active evaluator, cultural authority, or release decision unless independently wired and reviewed. |
| \`tests/\`, \`fixtures/\`, and \`tools/validators/\` | Bounded executable or fixture checks where implementation exists. | Archaeological truth, rights clearance, review approval, or publication authority. |
| \`data/\` and \`release/\` | Lifecycle artifacts, proofs, receipts, manifests, corrections, and rollback records when populated. | Automatic permission to promote or publish. |
| Governed API, Explorer, connectors, and pipelines | Runtime projections or processing only when executable and independently verified. | Domain doctrine or cultural/sovereignty authority. |

Never infer authority from a filename, a generated receipt, a green local fixture check, or the presence of a route/pipeline directory.

---

## Path posture

Current Archaeology path guidance reconciles the semantic and schema namespaces to the Directory Rules §12 form:

| Path | Current posture | Meaning |
|---|---|---|
| \`contracts/archaeology/\` | \`CONFIRMED\` compatibility path / lineage | Existing requested folder retained for compatibility and historical references. |
| \`contracts/domains/archaeology/\` | \`CONFIRMED\` current Directory-Rules-aligned semantic lane | Preferred home for Archaeology object-family meaning in current repository evidence. |
| \`schemas/contracts/v1/domains/archaeology/\` | \`CONFIRMED\` populated schema lane with mixed maturity | Preferred machine-shape namespace; individual schema status controls readiness. |
| \`schemas/contracts/v1/archaeology/\` | \`LINEAGE\` / compatibility shorthand | Existing namespace must not become a second schema authority. |
| \`docs/domains/archaeology/\` | \`CONFIRMED\` doctrine lane | Path, sensitivity, lifecycle, publication, API/UI, and validator guidance. |
| \`policy/domains/archaeology/\` | \`CONFIRMED\` policy responsibility root | Current direct Rego files are mostly proposed default-deny scaffolds, not an accepted runtime bundle. |

This README does not move, delete, redirect, or canonicalize files. Removing or formally redirecting the compatibility path requires an ADR or migration note and a repository-wide reference check.

---

## Current repository snapshot

The following counts are from the inspected current \`main\` tree at base commit \`afe3d353023e83eebb8937874312942fbf5bfaf4\`. They describe file presence, not production readiness.

| Surface | Observed state | Safe conclusion |
|---|---|---|
| \`contracts/domains/archaeology/\` | 32 Markdown files, including README/Object Map and object-family contracts. | A substantial semantic corpus exists under the preferred lane. Object-family convergence is not complete. |
| \`schemas/contracts/v1/domains/archaeology/\` | 40 JSON Schema files: 36 \`PROPOSED\`, 3 \`PROPOSED_INACTIVE\`, and 1 \`DRAFT_BOUNDED_PROJECTION\`. | The schema inventory exists, but most shapes remain proposed or permissive. |
| \`policy/domains/archaeology/\` and adjacent sensitivity lane | 18 policy/index files. | Policy source files exist; the policy README records mixed maturity and evaluator-unbound status. |
| Archaeology validators | 8 domain validator paths plus a shared EvidenceBundle projection runner. | CandidateFeature, 3D documentation/visibility, and volume-assessment fixture slices are substantive; several named validators remain placeholders. |
| Archaeology tests | 14 direct domain test modules plus 4 validator test modules and package initialization. | Candidate/no-network and focused validator tests are executable; many named direct domain tests remain one-line placeholders. |
| Archaeology fixtures | Candidate denial matrix, source/steward examples, EvidenceBundle projection, 3D, visibility, and volume-assessment cases. | Synthetic fixture coverage exists for bounded slices; it does not close source rights, cultural review, or public release. |
| Archaeology workflows | \`domain-archaeology.yml\` and \`archaeology-evidence-bundle-convergence.yml\`. | Bounded no-network fixture lanes exist; broad domain validation, release dry-run, and publication remain holds. |
| \`pipelines/domains/archaeology/\` | Seven named scripts, each currently greenfield placeholder-only. | Pipeline directory shape exists; no executable ingest-to-publish pipeline is established. |
| \`packages/domains/archaeology/src/archaeology/\` | Identity, layer, and observation modules are placeholder-only. | No reusable package implementation is established by these files. |
| \`apps/governed-api/routes/domains/archaeology/\` | Route-family README plus placeholder directory state. | Route contract guidance exists; handlers, DTOs, middleware, and runtime wiring are not proven. |
| \`data/receipts/generated/\` | Archaeology-related documentation/policy/workflow receipts exist. | Receipts record process lineage; they do not grant evidence, cultural, policy, release, or publication authority. |

The repository therefore contains a real archaeology contract and validation corpus, but it is not accurate to describe the domain as fully enforced or live.

---

## Object-family spine

The preferred semantic lane includes contracts for, among others:

- \`ArchaeologicalSite\`, \`SiteComponent\`, \`ChronologyAssertion\`, and \`ProvenienceContext\`;
- \`SurveyProject\`, \`SurveyTransect\`, \`ExcavationUnit\`, \`StratigraphicUnit\`, and \`TestUnit\`;
- \`ArtifactRecord\` and \`CollectionRepositoryRecord\`;
- \`RemoteSensingAnomaly\`, \`LidarCandidate\`, \`GeophysicsObservation\`, and \`CandidateFeature\`;
- \`ThreeDDocumentation\` and \`ThreeDVisibilityAssumptionDisclosure\`;
- \`CulturalReview\`, \`StewardReview\`, \`SensitivityTransform\`, and \`PublicationTransformReceipt\`;
- \`DomainFeatureIdentity\`, \`DomainLayerDescriptor\`, \`DomainObservation\`, and \`DomainValidationReport\`.

Two overlapping corpus lists are still preserved in the domain architecture and contract README: a collapsed Archaeology/Cultural Heritage vocabulary and a decomposed object-family spine. The terms are meaningful, but their single canonical realization and cross-family relationships remain an ADR/open-verification concern.

The following distinctions are non-negotiable:

- a \`CandidateFeature\` is not an \`ArchaeologicalSite\`;
- a LiDAR or remote-sensing anomaly is not a confirmed cultural feature;
- a 3D model or visibility analysis is documentation/paradata, not archaeological truth;
- source, observation, validation, retrieval, release, and correction times remain distinct where material;
- contextual layers from roads, geology, hazards, people/land, or other domains cannot confirm a site or bypass Archaeology sensitivity gates;
- a file move, UI label, validator PASS, or generated receipt cannot promote an object.

---

## Semantic rules

Every Archaeology semantic contract should state:

- object meaning, identity-bearing attributes, and non-equivalences;
- source family and source role, without collapsing source, observation, interpretation, review, and release;
- temporal fields and provenance lineage;
- \`EvidenceRef\` and \`EvidenceBundle\` expectations;
- rights, cultural authority, sovereignty/CARE, consent, embargo, and revocation posture;
- sensitivity tier/rank and permitted audience;
- candidate, confirmed, stale, superseded, corrected, and withdrawn states;
- redaction/generalization and transform-receipt requirements;
- cultural/steward review and policy decision expectations;
- lifecycle, correction, rollback, and release references.

Contracts are semantic documentation. They do not validate payloads, resolve evidence, execute policy, admit sources, create cultural authority, approve a release, or publish a map/API/AI result.

---

## Sensitivity and publication

Archaeology is a sensitive lane. The conservative public posture is deny-by-default for:

- exact or reverse-engineerable site geometry;
- burial or human-remains context;
- sacred-place or culturally restricted locations;
- collection-security detail;
- looting-risk detail;
- restricted oral history, sovereignty-bearing knowledge, or private sensitive records;
- derivatives that allow a withheld location to be reconstructed.

The domain documents identify T4/rank-5 defaults and a proposed sensitivity crosswalk; the crosswalk and named profiles still require the responsible stewards and rights-holder/cultural review authority. Until a less restrictive disposition is explicitly closed, the most restrictive applicable posture applies.

A public-safe transformation requires more than a schema-valid payload. Depending on the object and audience, it requires:

- a named redaction/generalization profile;
- a \`RedactionReceipt\` or \`PublicationTransformReceipt\`;
- resolved evidence and source/rights posture;
- cultural, steward, sovereignty, or rights-holder review where applicable;
- a \`PolicyDecision\`;
- an explicit \`ReleaseManifest\`/map release record;
- correction, withdrawal, stale-state, and rollback support.

Generalized or aggregate surfaces must not be reverse-joined to sensitive records. Public API, UI, export, graph, search, and AI surfaces must use governed projections and must cite or abstain. No document in this folder authorizes exact-location release.

---

## Lifecycle

The intended Archaeology lifecycle is:

~~~mermaid
flowchart TD
  A["Source admission and rights"] --> B["RAW / WORK / QUARANTINE"]
  B --> C["Validated object and EvidenceBundle"]
  C --> D["Catalog / triplet closure and review"]
  D --> E["Transform and release manifest"]
  E --> F["Published generalized surface"]
~~~

| Phase | Archaeology boundary |
|---|---|
| Admission | Source identity, rights, sensitivity, cultural authority, consent, and integrity are explicit or the material is quarantined/denied. |
| RAW | Admitted source material remains traceable; RAW is not public truth. |
| WORK / QUARANTINE | Transformations, conflicts, unresolved rights, sensitive content, and review holds remain distinguishable. |
| PROCESSED | Normalized objects are validated without collapsing candidate into confirmed or source into evidence. |
| CATALOG / TRIPLET | Evidence, identity, temporal, sensitivity, review, and source closure are recorded before release candidacy. |
| PUBLISHED | Only explicitly released, generalized/redacted, policy-safe, correction-aware projections may be public. |
| Correction / rollback | Corrections, revocation, embargo, withdrawal, stale-state propagation, and rollback must reach all derived public surfaces. |

The seven archaeology pipeline files currently contain placeholder comments, so this diagram is doctrine and target shape—not proof of execution.

---

## Validation maturity

### Bounded executable slices

| Surface | Current evidence | Boundary |
|---|---|---|
| \`tools/validators/archaeology/validate_candidate_feature.py\` | Deterministic, standard-library, no-network validator with \`--fixtures\`. | Validates a bounded candidate projection; it does not confirm sites, resolve evidence, evaluate cultural authority, or release data. |
| \`tests/domains/archaeology/test_candidate_not_site.py\` | Executable synthetic safety tests with a denial matrix. | Proves the tested candidate invariants only. |
| \`tools/validators/domains/archaeology/validate_three_d_documentation.py\` | Fixture-only validator with finite \`PASS\`, \`ABSTAIN\`, \`DENY\`, and \`ERROR\` outcomes. | Emits \`authority: NONE\`; does not read 3D assets, interpret archaeology, review culture/rights, release, or publish. |
| \`tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py\` | Fixture-only visibility-assumption validator with deterministic replay tests. | Records disclosed assumptions; it is not a visibility truth or publication decision. |
| \`tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py\` | Fixture-only volume/measurement validator with bounded integrity and coherence checks. | It does not establish archaeological interpretation or public-release safety. |
| \`tools/validators/validate_archaeology_evidence_bundle_projection.py\` | Shared-schema fixture projection runner. | A local projection check is not EvidenceBundle resolution or proof closure. |
| \`tests/domains/archaeology/test_no_network_fixtures.py\` | Verifies the tested fixture path and Python no-network startup guard. | Does not prove runner-wide, browser, process, or deployment isolation. |

### Placeholder and unbound surfaces

The following are present but not enforcement proof:

- \`validate_evidence_bundle.py\`, \`validate_schema.py\`, \`validate_source_descriptor.py\`, and \`validate_catalog_matrix.py\` are greenfield \`NotImplementedError\` placeholders;
- many direct domain tests are one-line \`PROPOSED\` placeholders, despite their names suggesting broader coverage;
- direct Archaeology Rego files generally declare \`PROPOSED\` scaffolds with \`default allow := false\`; the policy index records evaluator binding, accepted bundles, obligation handlers, and runtime consumers as unresolved;
- \`domain-archaeology.yml\` runs one bounded synthetic \`ThreeDDocumentation\` slice and explicit maturity assertions;
- \`archaeology-evidence-bundle-convergence.yml\` provides a no-network convergence lane, not a full source-to-public pipeline;
- governed API, connectors, pipelines, packages, Explorer behavior, data activation, and release behavior require separate implementation evidence.

A validator result of \`PASS\` means only that the bounded local assertion passed. It is not cultural approval, source admission, evidence truth, policy authorization, release approval, or publication authority.

### Suggested local checks

Run only from the repository root and preserve the no-network posture:

~~~bash
KFM_NO_NETWORK=1 python tools/validators/archaeology/validate_candidate_feature.py --fixtures
KFM_NO_NETWORK=1 python -m unittest tests.domains.archaeology.test_candidate_not_site -v
KFM_NO_NETWORK=1 python -m unittest tests.domains.archaeology.test_no_network_fixtures -v

KFM_NO_NETWORK=1 python tools/validators/domains/archaeology/validate_three_d_documentation.py --fixtures
KFM_NO_NETWORK=1 python tools/validators/domains/archaeology/validate_three_d_visibility_assumption_disclosure.py --fixtures
KFM_NO_NETWORK=1 python tools/validators/domains/archaeology/validate_archaeological_volume_measurement_assessment.py --fixtures

KFM_NO_NETWORK=1 python -m unittest \
  tests.validators.domains.archaeology.test_validate_three_d_documentation \
  tests.validators.domains.archaeology.test_validate_three_d_visibility_assumption_disclosure \
  tests.validators.domains.archaeology.test_validate_archaeological_volume_measurement_assessment -v

KFM_NO_NETWORK=1 python tools/validators/validate_archaeology_evidence_bundle_projection.py --fixtures
~~~

These commands document confirmed local entrypoints; this documentation-only update does not claim a hosted run or a full Archaeology suite pass.

---

## Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Existing \`contracts/archaeology/README.md\` | \`CONFIRMED\` but stale before this edit | Compatibility-folder purpose, sensitive-domain boundaries, and prior lineage. | Its former “blank file” and incomplete-inventory claims were incorrect. |
| \`contracts/domains/archaeology/README.md\` and \`OBJECT_MAP.md\` | \`CONFIRMED\` current semantic lane | Directory-Rules-aligned path, object-family spine, and semantic/authority split. | Object-family convergence and implementation maturity remain open. |
| \`docs/domains/archaeology/CANONICAL_PATHS.md\` | \`CONFIRMED\` path guidance | Reconciliation of \`contracts/domains/archaeology/\` and \`schemas/contracts/v1/domains/archaeology/\` as preferred namespaces. | A repository-wide migration still needs an ADR or migration note. |
| \`docs/domains/archaeology/ARCHITECTURE.md\` and \`OBJECT_FAMILIES.md\` | \`CONFIRMED\` doctrine / \`PROPOSED\` field realization | Candidate-not-site, source-role separation, 3D/documentation boundaries, and sensitive-lane posture. | Architecture prose is not runtime enforcement. |
| \`schemas/contracts/v1/domains/archaeology/\` | \`CONFIRMED\` file inventory; mixed maturity | 40 schema paths and their individual status labels. | 36 are \`PROPOSED\`; most are permissive scaffolds. |
| \`tools/validators/\`, \`tests/\`, \`fixtures/\`, and workflows | \`CONFIRMED\` bounded implementation slices | Candidate, 3D, volume, EvidenceBundle projection, and no-network fixture surfaces. | No full domain proof, policy parity, release dry-run, or public-surface authorization. |
| \`policy/domains/archaeology/README.md\` and direct Rego files | \`CONFIRMED\` policy lane / \`PROPOSED\` rule maturity | Named deny/abstain families and fail-closed intent. | Evaluator binding, accepted bundle, obligation handling, and runtime behavior are unresolved. |
| \`apps/governed-api/routes/domains/archaeology/README.md\` | \`CONFIRMED\` route-family documentation | Governed API trust boundary and minimum safe route intent. | No route handler, DTO, middleware, policy runtime, evidence resolver, or deployment behavior is proven. |
| \`pipelines/domains/archaeology/\` and \`packages/domains/archaeology/src/archaeology/\` | \`CONFIRMED\` placeholder paths | Intended ownership roots. | Current files are placeholder-only; no live processing/package behavior. |
| Google Drive: *Archaeological 3D GIS.pdf* | \`LINEAGE\` / general technical reference | Context for archaeological 3D GIS capture, visualization, spatial analysis, and knowledge-production use cases. | It does not define KFM contracts, rights, sensitivity, cultural authority, schemas, or implementation. |
| Google Drive: *KFM_Full_Atlas_seed_cards* | \`LINEAGE\` / proposed KFM doctrine | Evidence-first, EvidenceBundle/EvidenceRef, cite-or-abstain, finite outcomes, and sensitive-location fail-closed principles. | It does not override current GitHub paths, status labels, or runtime evidence. |

---

## Open verification

- [ ] Confirm named owners for semantics, schemas, source admission, cultural/sovereignty review, policy, validators, API, UI, release, and rollback.
- [ ] Record the compatibility-path migration or redirect in an ADR before removing or enforcing a single namespace.
- [ ] Reconcile the collapsed and decomposed Archaeology object-family lists and assign one canonical identity for each family.
- [ ] Replace or explicitly retain each permissive schema scaffold with a reviewed strict shape, including rights, sensitivity, evidence, review, release, correction, and rollback bindings.
- [ ] Bind policy bundles to an accepted evaluator and test policy/runtime parity; do not treat default-deny stubs as active enforcement.
- [ ] Implement the placeholder validators, domain tests, pipeline stages, and package helpers or keep their non-readiness visible.
- [ ] Verify source descriptors, rights, licenses, cultural authority, consent, embargo, revocation, and retrieval posture for each activated source.
- [ ] Establish EvidenceBundle/proof closure without treating a schema or validator PASS as proof.
- [ ] Implement and independently test governed API handlers, route middleware, safe logging/telemetry, and public UI projections.
- [ ] Verify release manifests, transform/redaction receipts, correction propagation, withdrawal, rollback, and stale-state handling.
- [ ] Keep exact sensitive locations and reverse-engineerable derivatives denied unless every applicable cultural, rights, policy, evidence, review, transform, and release gate is explicitly closed.

---

## Rollback

This update is documentation-only. Revert the single README commit to roll it back. No schema, policy, validator, test, fixture, source, pipeline, package, receipt, release, or runtime file was changed. No generated receipt specifically paired with this README was identified or updated.

---

## Definition of done

- [ ] Compatibility and canonical semantic paths are reconciled by an ADR or migration note.
- [ ] Owners and responsible cultural/rights-holder review roles are confirmed.
- [ ] Object-family vocabulary and contract/schema pairs are reconciled.
- [ ] Strict accepted schemas exist for the object families that can cross a governed boundary.
- [ ] Candidate, confirmed, source, evidence, review, policy, transform, release, correction, and rollback records remain distinct.
- [ ] Sensitive-location and reverse-engineering denial is tested across data, API, UI, export, graph, search, and AI surfaces.
- [ ] Policy rules are evaluator-bound, runtime-parity tested, and culturally reviewed.
- [ ] Validators, fixtures, tests, pipelines, connectors, packages, route handlers, and release records have verified maturity.
- [ ] EvidenceBundle closure, rights posture, cultural/steward review, redaction/transform receipts, and release manifests are required before public-safe output.
- [ ] Public surfaces consume only released governed projections; no raw, work, quarantine, candidate, exact-location, or unreleased material is exposed.
- [ ] Correction, revocation, embargo, withdrawal, and rollback drills are independently evidenced.

---

## Status summary

\`contracts/archaeology/\` remains a useful compatibility and lineage folder, but current repository guidance prefers \`contracts/domains/archaeology/\` for semantic meaning and \`schemas/contracts/v1/domains/archaeology/\` for machine shape. The Archaeology lane has substantial documented and bounded fixture/validator work, while most schemas and policy rules remain proposed, several test/validator/pipeline/package surfaces are placeholders, and live API, source activation, cultural-review authority, release, and publication remain unproven.

<p align="right"><a href="#top">Back to top</a></p>
