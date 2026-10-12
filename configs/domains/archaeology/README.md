<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-archaeology-readme
title: configs/domains/archaeology/ — Governed Archaeology and Cultural Heritage Configuration Boundary
type: readme
version: v0.4.0
status: draft; repository-grounded; README-only; no-live-binding
owners: NEEDS VERIFICATION — configuration, archaeology, cultural/Tribal, rights, sensitivity, consumer, and validation stewardship
review_route: "@bartytime4life via /configs/ CODEOWNERS; routing is not cultural authority or independent approval"
created: 2026-07-13
updated: 2026-09-04
policy_label: public-doc; non-secret; exact-location-deny; sovereignty-aware; no-site-confirmation; no-release-authority
current_path: configs/domains/archaeology/README.md
owning_root: configs/
readme_profile: BOUNDARY_COMPACT
domain_slug: archaeology
truth_posture: CONFIRMED pinned tracked inventory and selected source inspection; PROPOSED future configuration; UNKNOWN consumer binding and runtime enforcement
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  authoring_base_commit: 700570cbcf191038aa20a030174c2dd08cf93675
  prior_readme_blob: e42316554e24777096611a5cc54fd3a61e2fa0be
  tracked_files_in_lane: 1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_decision: ADR-0029 accepted
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/archaeology/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/CODEOWNERS
  - ../../../schemas/contracts/v1/domains/archaeology/evidence_bundle.schema.json
  - ../../../tools/validators/validate_archaeology_evidence_bundle_projection.py
  - ../../../tests/validators/domains/archaeology/test_evidence_bundle_schema_convergence.py
  - ../../../.github/workflows/archaeology-evidence-bundle-convergence.yml
notes:
  - "Same-path documentation correction; no executable configuration or consumer is added."
  - "The exact tracked lane contains only README.md. Untracked, ignored, branch-only, and externally hosted state is not established."
  - "The former all-scaffold maturity summary is historical, not a current classification of every archaeology surface."
  - "The EvidenceBundle projection has executable source and focused tests; it is not this lane's configuration validator."
  - "All existing H2 navigation destinations and the document identity are retained. No cultural, rights, sensitivity, evidence, or release permission is created."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Archaeology and Cultural Heritage Domain Configuration

`configs/domains/archaeology/`

**Configuration can select already-governed behavior. It cannot confirm a site, supply cultural authority or consent, clear a protected location, or authorize publication.**

[Parent configuration lane](../README.md) · [Archaeology documentation](../../../docs/domains/archaeology/README.md) · [Current evidence](#status) · [Validation](#validation) · [Location protection](#exact-location-reconstruction-and-looting-risk) · [First payload](#definition-of-done-for-the-first-payload)

> [!IMPORTANT]
> **Current lane: README-only at the pinned revision.** No configuration payload is tracked here. No loader, precedence rule, runtime binding, source activation, map layer, or publication behavior is established by this document. The surrounding archaeology implementation is mixed, not uniformly scaffold-only.

> [!CAUTION]
> Exact or reconstructable archaeological locations, burial and human-remains information, sacred places, restricted cultural knowledge, collection-security details, private-land context, and looting-risk clues remain fail-closed. A public repository, a passing shape check, a reviewed example, or a hidden map marker is not clearance to expose them.

## Purpose

This README maintains the archaeology boundary within the [shared configuration root](../../README.md). It helps a contributor decide whether a proposed setting is commit-safe, which consumer owns it, which authorities constrain it, and what evidence is required before use.

The lane currently provides documentation only. Future genuinely shared defaults or templates may belong here after consumer and placement review. Under [adopted Directory Rules](../../../docs/doctrine/directory-rules.md) §10.4, configuration for one app follows that app; declarative pipeline runs belong to `pipeline_specs/`, deployment configuration to `infra/`, and executable admissibility rules to `policy/`. Domain naming alone does not justify moving them into this directory.

## Authority level

The owning responsibility root is **`configs/`**, not an independent archaeology authority. The local profile is `BOUNDARY_COMPACT`, inheriting the parent configuration contract.

[ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) accepts the exact Directory Rules v2 bytes. The rules' internal draft-era label is retained in those adopted bytes; it does not undo that acceptance. This update changes no adopted decision or responsibility boundary.

Configuration owns none of the following: archaeological meaning, site identity, cultural authority, consent, custody, source admission, machine-shape authority, policy, evidence, review approval, release, or publication. A setting may reference an authority but cannot create it. `configs/` is a canonical configuration root; the frozen top-level `catalog/` correction mechanism is not a placement rule for this lane.

## Status

### Repository snapshot

The current evidence review is pinned to `main@bb3eb695e6068b38453ca3ded8f1394a8fdebc20`. The incoming README is blob `e42316554e24777096611a5cc54fd3a61e2fa0be`, version `v0.3`, dated 2026-07-14.

A direct, exact-ref directory listing returned one file and no child directories. The complete **tracked lane** is therefore:

```text
configs/domains/archaeology/
└── README.md  # configuration boundary; no executable payload
```

This is not an inventory of local ignored files, other branches, external storage, or deployment state. A bounded indexed path search found only this README, but its index snapshot lagged the review pin; it is not an exhaustive proof of zero consumers.

### Current evidence matrix

| Surface | Current bounded finding | What it does not establish |
|---|---|---|
| This configuration lane | **CONFIRMED / README-only:** one tracked file. | A parser, payload, loader, precedence rule, or deployment binding. |
| Parent and root READMEs | **CONFIRMED documents:** domain parent `v0.6`; configuration root `v0.5`. | Execution or policy enforcement. Their dated inventories remain their own snapshots. |
| Archaeology domain README | **CONFIRMED document:** `v2.2.3` describes mixed implementation and bounded convergence work. | A fresh audit of every domain component or live service. |
| Archaeology EvidenceBundle schema | **CONFIRMED / PROPOSED projection:** delegates shape by `$ref` to the shared schema; denies independent fields and declares no public-release authority. | Accepted independent semantics, cultural approval, or configuration validation. |
| Projection validator and convergence tests | **CONFIRMED executable source:** shared runner wrapper and three substantive test methods. | A test result in this session, consumer binding, or sensitive-data permission. |
| Legacy domain EvidenceBundle validator | **CONFIRMED placeholder:** `main()` raises `NotImplementedError`. | A substitute for the separately named projection validator. |
| Focused convergence workflow | **CONFIRMED source:** compilation, startup-guard assertion, unittest, and fixture validation commands exist. | Exact-head hosted success, required-check enforcement, or runner-wide no-egress. |
| Runtime, sources, public access, cultural and specialist review | **UNKNOWN / NEEDS VERIFICATION.** | No activation, release, or operational maturity is inferred. |

### Critical scaffold warning

The July edition's blanket scaffold summary is superseded by the bounded matrix above. It must not be generalized to every present-day schema, validator, or workflow. Conversely, one implemented projection does not make the whole domain operational.

For each future consumer, inspect the exact code and referenced profile. An empty schema, `NotImplementedError`, TODO job, or unbound policy default is not effective protection. Absence of a deny result is never permission. The current projection validator is **not a configuration validator** and establishes no loading or activation binding to this directory.

### Current conflict register

This revision does not re-adjudicate every historical naming, schema, source-registry, or policy-layer question. `Site` versus `ArchaeologicalSite`, collapsed versus decomposed names, transform/receipt terminology, consent-record authority, and alternate registry layouts remain matters to resolve against their current owning contracts and decisions before dependent use. Do not assert they are settled—or still identical to the July snapshot—without reinspection.

## What belongs here

The retained README belongs here now. Future small, non-secret shared defaults, inert templates, or config-facing migration notes require a concrete consumer and a responsibility-root basis; directory symmetry is not sufficient.

Examples must be unmistakably synthetic and non-operational. Do not include real or plausibly identifying sites, communities, accessions, people, parcels, routes, coordinates, oral-history content, collection records, credentials, or access details. A label saying “example” does not make sensitive content safe.

## What does not belong here

Do not store source records, archaeological observations, site or candidate geometry, raw scans, restricted knowledge, custody determinations, consent or review records, policy rules, schemas, proofs, receipts, catalog instances, release decisions, or published products in this lane. They retain their own responsibility and access controls.

Secret values, signed URLs, private endpoints, deployment-only paths, reviewer rosters, and live source bindings are also excluded. Restricted material must not be moved into public Git merely because its logical home is a `data/` lane.

No threshold, flag, alias, or fallback may confirm a candidate, waive review, lower sensitivity, turn a placeholder into an active source, or enable direct public access to internal stores.

## Inputs

A future configuration proposal needs an exact consumer, intended use and audience, format/version, field-meaning owner, schema/profile reference, explicit binding, precedence and merge semantics, missing/unknown-key behavior, and a correction/rollback plan.

For consequential use, references must resolve to the applicable current source, rights, cultural-authority, consent/revocation, sensitivity, evidence, policy, review, and release controls. Unresolved dependencies remain visible and block the dependent use; they need not block safe, inert, synthetic authoring.

## Outputs

Today, the output is configuration guidance. A future validated setting may select an already-governed candidate label, uncertainty display, review route, denial state, or approved representation profile for its named consumer.

It cannot emit a site confirmation, supply consent, establish custody or affiliation, activate a source, close an EvidenceBundle, or grant release permission. Public clients consume governed interfaces and released public-safe carriers, not this directory or internal registries directly.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Configuration supports a consumer within that lifecycle. It does not advance the lifecycle; promotion remains a governed transition, not a file move, configuration toggle, successful job, or merge.

## Validation

### Configuration-review outcomes

`PASS`, `HOLD`, `DENY`, and `ERROR` below are review descriptions, **not a new machine enum**. A check passing establishes only that check. Missing support keeps the affected behavior inactive; an error must never become permission. Runtime `ANSWER`/`ABSTAIN`/`DENY`/`ERROR` mappings remain owned by their contracts.

For this README, check identity and preserved anchors, metadata, relative links, table/fence structure, safe examples, final newline, whitespace, and evidence attribution. The generated-work receipt is validated separately and retains pending human review.

For a future payload, require meaningful shape validation, explicit consumer selection, deterministic precedence, safe fallback, no implicit network or publication effects, and targeted positive and negative tests. Unknown risk-bearing keys, type coercion, missing references, stale permissions, and invalid profiles must not weaken the boundary.

**Existing implementation is adjacent evidence, not a shortcut:**

- [Projection validator](../../../tools/validators/validate_archaeology_evidence_bundle_projection.py) selects the archaeology EvidenceBundle schema and shared fixtures through the common runner.
- [Convergence tests](../../../tests/validators/domains/archaeology/test_evidence_bundle_schema_convergence.py) check delegation, shared closed shape, and acceptance/rejection of shared fixtures.
- [Focused workflow](../../../.github/workflows/archaeology-evidence-bundle-convergence.yml) defines real commands. Its `pull_request.paths` list does **not** include this README; this documentation edit alone does not select that workflow. No manual dispatch is implied.

These sources were inspected, not executed by this documentation review. They do not validate hypothetical configuration, authenticate review, prove cultural permission, or establish system-wide no-network enforcement.

## Review burden

### Minimum review posture

[CODEOWNERS](../../../.github/CODEOWNERS) routes `/configs/` to `@bartytime4life`. This is a repository review route, not a verified archaeology, Tribal, cultural, rights-holder, or human-remains authority assignment. Specialist stewardship, independent review, and effective approval enforcement remain `NEEDS VERIFICATION`.

Review should match the effect: documentation accuracy for this update; consumer/schema/validation review for a payload; cultural, rights, sensitivity, security, and release review for any change affecting protected representation or exposure. Source-role, identity, chronology, and alias changes also involve the relevant meaning and source owners.

### Separation of duties

An author must not choose the rightful cultural authority, approve its own consent or release claim, define and approve a sensitive transform, or treat its own generated receipt as approval. Draft authoring, human review, integration, source activation, release, and publication remain separate.

## Related folders

| Responsibility | Owning family or entry point | Boundary |
|---|---|---|
| Shared configuration | [Parent lane](../README.md), [root contract](../../README.md) | Non-secret inputs for named consumers. |
| Domain explanation | [Archaeology documentation](../../../docs/domains/archaeology/README.md) | Scope, language, sensitivity, and verification context. |
| Meaning and machine shape | `contracts/`, `schemas/` | Refer to current owning definitions; do not copy them into config. |
| Admissibility | `policy/` | Executable rights, sensitivity, and access rules, not settings that grant permission. |
| Source identity | `data/registry/` | Resolve the accepted family/lane before adding a descriptor or alternate topology. |
| Evidence and process memory | `data/proofs/`, `data/receipts/` | EvidenceBundle/proof support and process records remain distinct. |
| Catalog and public carriers | `data/catalog/`, `data/published/` | Discovery projections and released public-safe bytes are not evidence authority. |
| Release and correction | `release/` | Release, withdrawal, correction, and rollback decisions. |
| Implementation and tests | Consumer-owning code and test roots | Configuration does not implement the consumer or prove behavior. |

This table routes responsibilities, not a claim that every possible archaeology child path is active or populated. In particular, a catalog pointer to an EvidenceBundle does not move the bundle's authority into a catalog lane.

## ADRs and drift triggers

### Repository-present Archaeology ADRs

The domain's [current documentation entry point](../../../docs/domains/archaeology/README.md) provides its decision context. This configuration update does not accept a domain ADR or reclassify a proposal as adopted. The July source-role and exact-location descriptions are historical evidence, not current decision-status proof.

### Decisions not enacted here

No new configuration schema, source-role enum, canonical object alias, cultural-review record home, source-registry topology, public geometry floor, loader order, or policy/runtime binding is established.

### ADR or migration triggers

A new authority home, conflicting alias, canonical identity change, policy or consent semantic change, source-registry reorganization, public-access change, or retirement requires the applicable decision and migration review before dependent use. Routine same-path explanatory maintenance does not itself adopt those changes.

## Last reviewed

**2026-09-04**, against `bb3eb695e6068b38453ca3ded8f1394a8fdebc20`. Selected sources and limits are listed in the [evidence ledger](#evidence-ledger). Before authoring, main advanced to `700570cbcf191038aa20a030174c2dd08cf93675`; the exact comparison changed only `catalog/triplet/README.md`, leaving the inspected inputs unchanged. The authoring branch starts from that newer base.

Re-review when a payload or consumer is proposed; a contract, schema, ADR, policy, reviewer route, or sensitivity obligation changes; a source is admitted; a public consumer is connected; or an incident, correction, revocation, or rollback changes the evidence. Review is event- and risk-based, not an unsupported blanket six-month freshness claim.

## Scope and bounded context

The configuration scope may support surveys and transects, site/component candidates, artifacts and provenience, excavation and stratigraphy, chronology, remote sensing and geophysics, three-dimensional documentation, collections, and review-oriented representations. It owns none of those records or meanings.

A consumer must declare which families it supports. A broad “archaeology” selector is not permission to process all domain material. Location, culture, community authority, consent, custody, and method uncertainty remain attached to the relevant evidence and use.

## Configuration classes

The retained vocabulary—`template`, `example`, `dev-default`, `test-default`, `review-default`, `public-safe-template`, and `compatibility`—is a **PROPOSED authoring taxonomy**, not an accepted parser contract.

Development and test material stays synthetic and network-disabled by default. Review defaults cannot approve review; public-safe templates only reference reviewed profiles. Compatibility requires a bounded migration, one writable authority, expiry/exit criteria, and rollback. `production-binding` remains forbidden here.

## Minimum configuration contract

The following is a **PROPOSED design checklist**, not an executable payload or schema. Names must be reconciled with the actual consumer before implementation.

| Candidate fields | Required meaning |
|---|---|
| `domain_slug`, `config_class` | Explicit archaeology scope and authoring class; no activation by filename. |
| `intended_consumer`, `consumer_version`, `format` | Exact consumer, supported version, parser, and format version. |
| `authority_refs`, `validation_ref` | Current owning contracts/profiles and executable validation; a name or placeholder is not a resolved reference. |
| `object_families`, `source_roles`, `candidate_behavior` | Preserve family and use-specific role; no automatic candidate confirmation or alias adoption. |
| `cultural_authority_ref`, `consent_revocation_ref` | Governed authority and scoped, current consent/revocation references where required; never manufactured permission. |
| `sensitivity_floor`, `geometry_behavior`, `burial_sacred_behavior` | References to governing restrictions and reviewed transforms; no embedded sensitive geometry or invented universal floor. |
| `collection_security_behavior`, `chronology_behavior` | Preserve custody/access limits, methods, ranges, and uncertainty. |
| `network_behavior`, `side_effects` | No network, model, indexing, release, or publication effects during parsing/validation by default. |
| `unknown_key_behavior`, `missing_ref_behavior`, `logging_posture` | Reject unsafe ambiguity; remain inactive or return the governing finite failure outcome without disclosing protected values. |
| `rollback`, `owner`, `reviewed_at` | Named responsibility when verified, versioned correction/invalidation path, and review timestamp; unknowns remain explicit. |

Merely satisfying this checklist does not authorize use. A future configuration contract belongs with its proper meaning/shape owners, not as parallel authority inside this README.

## Consumer binding, precedence, and discovery

### Explicit binding

Consumers must select an exact path or stable identifier. Do not recursively activate files because they are present here. No consumer or loader was established by the current bounded search.

### No implicit precedence

The consumer must define merge versus replace, domain/environment/deployment/CLI ordering, unknown keys, coercion, missing files, stale values, and safe fallback. This README does not prescribe an unimplemented overlay order.

### Fail-safe behavior

A failure cannot trigger live fetching, choose an unreviewed “latest” release, ignore revocation, retain unsafe caches, promote a candidate, switch to permissive policy, or reveal guessed geometry. Report safe reason codes and preserve a protected audit reference when appropriate.

## Archaeology object-family boundaries

Keep source vocabulary and uncertainty intact until an owning contract and reviewed crosswalk support a mapping. Neither close spelling nor a familiar noun creates equivalence.

In particular: `Site` is not automatically `ArchaeologicalSite`; `CandidateFeature`, `LiDARCandidate`, and `RemoteSensingAnomaly` are not site confirmations; `ArtifactRecord` is not ownership; `CulturalReview` is not consent; `StewardReview` is not release approval; and `SensitivityTransform`, `PublicationTransformReceipt`, and a cross-cutting redaction receipt must not be substituted for one another without their contracts.

Validation, policy allowance, review, evidence closure, and publication are separate facts. A configuration alias must not collapse them.

## Identity, alias, and candidate promotion

### `Site` versus `ArchaeologicalSite`

The earlier README recorded overlapping names and compatibility paths. Their complete current reconciliation was not audited here. Preserve that uncertainty and resolve the current contract before selecting an alias; a config file cannot arbitrate canonical identity.

### Candidate promotion

An anomaly, score, model output, contextual source, or survey record remains what its evidence supports. Promotion to a reviewed site identity requires evidence and decisions outside this lane. Configuration can preserve a label or route to review, not approve promotion.

### Stable identity

Preserve governed source-native, project/transect, provenience/context, collection/accession, candidate/model/run, and correction identifiers where permitted. Do not expose them in public configuration merely because they are stable. Digests of sensitive geometry can also reveal or confirm location.

Do not merge records by proximity, geometry overlap, similar names, historic labels, route/parcel association, image resemblance, or embedding similarity alone.

## Source role and knowledge character

Observation, official designation, candidate, context, model/inference, community-controlled oral history, restricted material, synthetic examples, and legacy records are different knowledge characters. This is explanatory vocabulary, not a newly adopted role enum.

A source may be authoritative for one assertion and contextual for another. Do not upcast a role based on publisher name. Preserve source vintage, claim scope, method, rights, uncertainty, and restrictions; validate against the owning source-role contract before use.

## Cultural authority, sovereignty, consent, and revocation

Defer community-controlled knowledge and its permitted uses to the relevant named authority. Geography, government records, dataset ownership, organizational names, and convenience do not establish that authority. Multiple communities or authorities must not be flattened into one presumed representative.

A governed reference may carry scoped obligations for attribution, retention, benefit, access, and permitted use. Configuration cannot create `authority_to_control`, infer consent from silence, turn one-time consent into perpetual or secondary-use permission, or normalize restricted cultural meaning without authority.

Missing, limited, expired, superseded, revoked, or out-of-scope consent blocks the affected use. Resolve current revocation state rather than indefinitely caching permission. Invalidation obligations follow every affected representation and retrieval surface.

## Exact location, reconstruction, and looting risk

### Direct geometry channels

Protection covers coordinates, UTM/survey grids, bearings and distances, polygons, centroids, bounding boxes, revealing buffers, elevation profiles, and find-spot references—not just a latitude/longitude column.

### Indirect reconstruction channels

Review tile/H3/geohash/grid/raster/zoom identifiers; extents and query windows; filenames, URLs, IDs, hashes, and cache keys; dates, counts, accessions, narratives, photographs and metadata; parcel, route, river, settlement and environmental joins; cross-layer differencing; model saliency, embeddings and nearest-neighbor results; and logs, errors, telemetry, previews, or test snapshots.

### Required behavior

Unresolved reconstruction risk means inactive, `DENY`, `HOLD`, or `ABSTAIN` as the governing process requires—not guessed geometry, intermediate centroids, public risk maps, or best-effort disclosure. Client-only blurring or hiding a marker is not protection when the underlying bytes remain accessible.

County/region generalization is not a universal safe floor or a permission to publish. Cultural, burial, sacred-site, rights, collection-security, and looting-risk controls can require stronger generalization or complete denial. No transform is selected or approved by this update.

## Burial, human remains, sacred, and funerary material

No ordinary configuration switch may authorize exact or generalized locations; human-remains inventory or disposition; sacred/ceremonial identification; culturally restricted affiliation; excavation, storage, access, handling, imaging, analysis or transfer details; or legal/repatriation conclusions.

The most restrictive applicable policy and named-authority decision controls. Missing context is not clearance. Tests must use deliberately non-real synthetic fixtures without identifying locations, communities, or restricted knowledge.

## Collections, custody, repatriation, and security

Configuration cannot determine title, ownership, lawful custody, accession legitimacy, repository authority, consultation/repatriation status, legal eligibility, access permission, storage location, insurance/valuation, security arrangements, movement, or vulnerability.

Collection identifiers, repository names, photographs, accession numbers, and descriptions can themselves be sensitive or reconstructive. A released public-safe profile is a reference for its specified use, not permission to expose the underlying collection record.

## Chronology, time, and uncertainty

Keep source creation/vintage, observation/excavation, collection/acquisition, valid/effective time, interpretation/model time, retrieval, cultural review, consent/revocation, policy decision, release, and correction/withdrawal time distinct where material.

A display profile must not turn a range into an exact date, suppress calibration or method uncertainty, establish cultural affiliation, equate terms across communities, present a legacy interpretation as current, or erase contested chronology. Preserve limitations and correction lineage alongside the time representation.

## Remote sensing, LiDAR, geophysics, and three-dimensional documentation

Preserve sensor/product/source identity, acquisition time, permitted geometry context, resolution, processing chain, model/run/version, relevant parameters, method limitations, uncertainty/false positives, candidate state, and evidence/review linkage in the owning records—not as sensitive payloads in config.

An anomaly score or plausible reconstruction does not confirm a site. Public imagery availability is not rights or sensitivity clearance. Three-dimensional documentation does not grant reproduction, access, or distribution rights. Do not expose precise candidate geometry, saliency layers, or intermediate derivatives that undo location controls.

## Cross-domain context and anti-confirmation

Roads and historical routes, people/DNA/land and parcel records, geology, hazards, settlements/infrastructure, hydrology, habitat/flora/fauna, atmosphere, and agriculture may supply governed context. They do not confirm archaeology, grant land access, establish ownership or affiliation, or authorize intervention or disclosure.

Joins retain the strongest applicable sensitivity and named-authority obligations. A harmless-looking pair of public layers can still require reconstruction-risk review before an archaeology-facing derivative is exposed.

## Logging, telemetry, caches, and derived indexes

Do not dump configuration, protected identifiers, coordinates, extents, geometry hashes, cultural/review/consent substance, oral histories, collection/access details, private endpoints, raw prompts, or revealing denial context into public logs or indexes.

Prefer bounded safe reason codes and protected audit references; even counts and coarse categories require review when they identify a place or person. Corrections, revocations, withdrawals, and increased restrictions must propagate to affected app/CDN/tile caches, search/vector indexes, embeddings, graph projections, reports/exports, controlled previews/bookmarks, AI retrieval, and generated summaries.

Invalidation must be verified where controlled. Reverting a file does not recover copies already disclosed to others.

## Failure behavior

| Condition | Required safe disposition before dependent use |
|---|---|
| Missing/invalid config, unknown risk-bearing key, coercion, unresolved reference | Reject, remain inactive, or return the contract's error/hold; never silently widen access. |
| Empty schema, placeholder validator, unbound or permissive policy | Do not activate or describe the consumer as protected. |
| Authority, consent, rights, custody, or source role unresolved | Hold/deny/abstain as applicable; missing evidence is not permission. |
| Candidate presented as site or unreviewed alias substituted | Reject/relabel under the owning contract and route to review. |
| Exact-location, reconstruction, sacred, burial, or collection risk | Deny/hold under the most restrictive applicable rule. |
| Evidence, review, transform, release, correction, or rollback support missing | No public rendering, export, indexing, AI answer, or promotion. |
| Source/consumer unavailable or permission stale/revoked | Fail closed; do not conceal stale state or retain unsafe public derivatives. |
| Invalidation incomplete | Keep affected delivery withdrawn or restricted; do not claim restoration is safe. |

Errors must not reveal the rejected value or enough context to reconstruct it.

## Governed AI and generated language

AI is interpretive, never root truth. It must not confirm sites from imagery or model scores, infer authority/consent/affiliation/custody/legal status, reconstruct protected locations, rank vulnerable targets, provide access directions, or reveal restricted knowledge.

The intended sequence remains: scope the question and audience; resolve permitted released `EvidenceRef` to `EvidenceBundle`; apply cultural authority, consent/revocation, rights, sensitivity, policy, review and release checks; then answer with citations and bounded limitations or abstain/deny. A citation is not permission to disclose its underlying restricted content.

Ordinary public AI must not read RAW, WORK, QUARANTINE, private registries, candidate stores, or unreleased records. AI receipts, retrieval indexes, and controlled generated outputs remain subject to correction and invalidation.

## Migration and anti-bypass posture

When unsafe or misplaced material is discovered, stop affected activation/exposure, identify consumers and the disclosure window, preserve a protected audit trail, and handle secrets or sensitive bytes through the appropriate incident process. Do not copy protected contents into public issues or “cleanup” commits.

Classify by responsibility before any migration. Preserve source and object identity, versions, digests where safe, aliases, review decisions, consumer cutover, correction, and rollback. Migration must not create two writable authorities or be inferred from `git mv` alone.

### Anti-bypass matrix

Reject config that treats a source placeholder as admission, an empty schema as meaningful validation, a validator filename as a passing run, a published-path file as release, a candidate threshold as confirmation, a cached consent flag as perpetual permission, or direct UI/store access as governed delivery. Require current owning evidence and negative tests for the actual consumer.

## Rollback, correction, withdrawal, and invalidation

### Rollback triggers

Sensitive disclosure, misrepresented authority/consent, candidate confirmation, unsafe aliasing, scaffold reliance, reconstruction, ignored revocation, broken release mediation, or incomplete correction propagation requires safer handling of the affected consumer.

### Required response

Enter a safer state; stop affected public/API/UI/search/export/AI delivery; preserve protected audit evidence; identify releases and derivatives; restore a known-safe configuration or built-in denial; record correction/withdrawal/rollback decisions; invalidate controlled derivatives; and revalidate before restoration.

For this **documentation-only change**, the prior README blob is `e42316554e24777096611a5cc54fd3a61e2fa0be`. Keep the branch unintegrated or use a reviewed non-force revert/forward correction. Preserve the generated-work receipt as provenance for the bytes it recorded; do not silently repurpose it as a receipt for different content. No runtime rollback, source change, or data migration is performed here.

## Definition of done for the first payload

**Inert authoring:** identify the exact consumer and placement basis; keep values synthetic/non-secret; label proposed fields and unresolved dependencies; specify parser, version, binding, precedence, unknown/missing behavior, tests, and rollback. Do not add empty symmetry scaffolds or imply activation.

**Before activation:** verify the consumer and owner; resolve applicable contracts and meaningful schemas; run executable positive/negative tests; demonstrate fail-closed policy integration, authority/consent/revocation handling, candidate/identity boundaries, source-role and chronology preservation, no-network parse/validation, and safe observability. Sensitive behavior requires cultural/rights/security review and reconstruction, burial/sacred/human-remains, collection-security, and cross-domain denial cases.

**Before public use:** close evidence, rights, sensitivity, transforms, review, integrity, receipts/proofs, release, correction, and rollback. Verify invalidation across the actual map, cache, search, vector, graph, export, and AI consumers. Neither an inert template nor this checklist grants that transition.

## Verification backlog

| Item | Current posture and next evidence |
|---|---|
| Tracked configuration inventory | **CONFIRMED** at the pin: README only. Recheck on a payload or tree change. |
| Consumer, loader, discovery, precedence | **UNKNOWN.** Exact source binding and focused tests required. |
| Configuration schema and validator | **NEEDS VERIFICATION.** Do not substitute the EvidenceBundle projection. |
| Other archaeology packages, pipelines, schemas, policies, registries, UI and API | **NOT INSPECTED comprehensively in this review.** Classify each selected consumer rather than reuse the old blanket scaffold matrix. |
| Domain decision, alias, object-family and registry reconciliation | **NEEDS VERIFICATION** before dependent implementation. |
| Cultural/Tribal/rights-holder and specialist authority | **NEEDS VERIFICATION.** Repository routing is not assignment or consent. |
| Review enforcement and hosted exact-head results | **NEEDS VERIFICATION.** No approval or required-check claim. |
| Consent/revocation, location transforms, collection security, chronology and invalidation | **NEEDS VERIFICATION** for the actual consuming path; active/public use stays held without support. |
| External storage, live sources and deployed public behavior | **UNKNOWN.** This documentation change does not probe or activate them. |

## Safe language rules

Say “one tracked README at the pinned revision,” not “nothing exists anywhere.” Say “executable projection source inspected,” not “archaeology validation passed.” Say “the named legacy entrypoint is a placeholder,” not “all validators are placeholders.” Say “workflow commands exist,” not “CI enforces all archaeology controls.”

Say “candidate/anomaly under a method and uncertainty,” not “LiDAR found a confirmed site.” Say “current scoped authority and consent records support this use,” not “the community approved everything.” Say “reviewed upstream controls protect permitted representations,” not “the UI hides it” or “county generalization makes it safe.”

Use the core truth labels separately from implementation maturity, review state, and release state. Unknowns are not negative findings and code presence is not operation.

## Evidence ledger

All repository observations below refer to **`bb3eb695e6068b38453ca3ded8f1394a8fdebc20`** unless explicitly marked historical. Relative links are navigation; the pin and blob identities make the review reproducible.

| Evidence | Identity | Bounded support |
|---|---|---|
| Incoming target README | `e42316554e24777096611a5cc54fd3a61e2fa0be` | July `v0.3` source and safeguards retained; its broad maturity claims are not reused as current proof. |
| Exact configuration directory listing | One README, no child directories | Closed tracked-lane inventory only. |
| Parent / root configuration READMEs | `c497e41466f3aaf934aeca4b9976a2fa8516ff21` / `a800983eac7582a84e9dd82bc7d4baf04f552ad8` | Inherited responsibility and no-live-binding boundary. |
| Directory Rules / accepted ADR-0029 | `fd49a0b83e55cef52c1124281f093e263526898d` / `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Adopted placement; consumer-owned config; responsibility/lifecycle separation. |
| CODEOWNERS | `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | Repository review routing only. |
| Archaeology domain README | `c128be25ea31227cf03fc756dcd74b2a5e82bb06` | Domain framing and reported mixed maturity; not a substitute for code inspection. |
| [EvidenceBundle projection](../../../schemas/contracts/v1/domains/archaeology/evidence_bundle.schema.json) | `6bf74442d485f346c2412a2e07564161d80d1900` | Shared-shape delegation, proposed status, no independent fields/public release authority. |
| Projection validator / convergence tests | `28cceef5f1446fd492c6e520f3c7ed64698a4ee7` / `79e712f5ada05eae3596134f23c1281121b9f544` | Runnable source and substantive tests; not executed in this review. |
| Legacy domain validator | `5eb3a70d78c1074ba64071b16f591032b629b8c5` | Separate `NotImplementedError` entrypoint; not the projection implementation. |
| Focused convergence workflow | `259d61c5e339d693e964ca7297cff60a0ada5d80` | Source-level commands and selected paths; no README trigger or hosted result claim. |

The earlier July evidence inventory remains available in the prior Git blob. Google Drive's *Directory Rules* is lineage; the Notion archaeology builder page is coordination with an older repository checkpoint. Neither overrides the adopted repository rules or proves a scheduler, runtime, review, or release state.

## Status summary

**README-only configuration lane; selected adjacent validation is implemented in source; active configuration and public-use closure are unproved.** This revision corrects currentness, narrows unsupported maturity claims, preserves the document identity and H2 navigation, and retains cultural authority, consent/revocation, exact-location, candidate, collection, chronology, source-role, AI, correction, and rollback safeguards.

Only this README and its required AI-generated-work receipt participate in the change. No configuration payload, consumer, dependency, schema, policy, source record, domain data, workflow, permission, release decision, or deployment is changed. Human review remains separate and pending.

[Back to top](#top)
