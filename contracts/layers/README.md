<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-layers-readme
title: contracts/layers — Layer Semantic Contract Compatibility README
type: readme
version: v0.2
status: draft; repository-grounded; compatibility-orientation; mixed-maturity; non-publisher
owners: OWNER_TBD — Layer steward · Contract steward · Data steward · UI steward · Evidence steward · Policy steward · Release steward · Docs steward · Directory Rules reviewer
created: 2026-06-24
updated: 2026-09-07
policy_label: public-with-gates; contracts; layers; compatibility; map-first; renderer-boundary; release-gated; family-routing-unresolved
owning_root: contracts/
current_path: contracts/layers/README.md
responsibility: Orient maintainers to existing layer semantics, paired schemas, candidate validation, and fixture-only admission without creating a second writable object-contract authority.
truth_posture: cite-or-abstain; document presence, implemented checks, approval, release, and public use remain separate
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@6087d07b49362540e437dc666d1cbaa6eb6b82c3
prior_blob: b340d48ba17b7d303b0863f1574bbacbad2c17ea
authority_basis: Accepted ADR-0029; docs/doctrine/directory-rules.md blob fd49a0b83e55cef52c1124281f093e263526898d; DIR-AUTHROOT-001 and DIR-AUTHROOT-002
supersedes: v0.1 of this README only; no object contract, schema, policy, runtime, or release state
related:
  - ../README.md
  - ../data/layer_manifest.md
  - ../data/layer_descriptor.md
  - ../data/layer_catalog_item.md
  - ../runtime/layer_manifest_admission.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/architecture/ui/LAYERING.md
  - ../../schemas/contracts/v1/layers/README.md
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../tools/validators/data/validate_layer_manifest.py
  - ../../tests/validators/test_validate_layer_manifest.py
  - ../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts
  - ../../data/registry/layers/README.md
tags: [kfm, contracts, layers, layer-manifest, layer-descriptor, layer-catalog-item, maplibre, evidence, policy, release, rollback, compatibility]
notes:
  - "Same-path documentation reconciliation; contracts/layers/ contains only this README at the pinned snapshot."
  - "The adopted root split and default schemas/contracts/v1/<family>/ route are established; the data-versus-layers family migration is not settled here."
  - "The data LayerManifest has a dual-profile schema and deterministic validator; parallel layers schemas remain permissive PROPOSED scaffolds."
  - "The runtime admission evaluator is a separate fixture-only projection, not a live resolver, registry writer, loader, or release decision."
  - "No source, dependency, renderer, policy, public data, release, or deployment is activated by this update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/layers

> Find the existing layer contracts and their actual validation boundaries without creating a second contract home. Layers, legends, styles, tiles, screenshots, exports, and AI summaries remain downstream carriers of governed evidence, not truth or publication authority.

**Status:** repository-grounded draft; compatibility/orientation only. **Owning root:** `contracts/`. **Stewardship:** `OWNER_TBD`; this update assigns no reviewer or approval authority.

**Evidence snapshot:** `main@6087d07b49362540e437dc666d1cbaa6eb6b82c3`. Current-state statements below are bounded to that snapshot, not a claim that every referenced capability has been executed or released.

## Quick jumps

[Scope](#scope) · [Repo fit](#repo-fit) · [Current contract surface](#current-contract-surface) · [Object family meanings](#object-family-meanings) · [Anti-collapse rules](#anti-collapse-rules) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Layer trust rules](#layer-trust-rules) · [Validation](#validation) · [Migration checklist](#migration-checklist) · [Open verification](#open-verification) · [Evidence basis](#evidence-basis) · [Rollback](#rollback)

## Scope

`contracts/layers/` remains a compatibility and orientation lane. Its only tracked child at the evidence snapshot is this README. The object-level meanings of `LayerManifest`, `LayerDescriptor`, and `LayerCatalogItem` remain in `contracts/data/`; do not duplicate them here.

Two different placement questions must stay separate:

1. **Root responsibility is established.** Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules](../../docs/doctrine/directory-rules.md). Section 9.3 separates semantic meaning in `contracts/`, machine shape in `schemas/`, and admissibility in `policy/`. `DIR-AUTHROOT-001` already defaults machine schemas to `schemas/contracts/v1/<family>/`; `DIR-AUTHROOT-002` permits semantic Markdown here.
2. **Layer-family convergence remains unresolved.** Paired data-family schemas and parallel `schemas/contracts/v1/layers/` scaffolds both exist. [ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) remains proposed for routing, compatibility, migration, and enforcement. This README does not accept that ADR, choose a new family home, or authorize a move.

> [!IMPORTANT]
> A manifest can carry evidence, rights, sensitivity, policy, review, release, correction, and rollback references without proving that any reference resolves or that any operation is authorized. Schema validity and a layer toggle are not publication.

## Repo fit

| Responsibility | Inspected surface | Boundary |
|---|---|---|
| Semantic root | [Contracts README](../README.md) | Meaning and interface promises, not machine shape or permission. |
| Layer object meaning | [Manifest](../data/layer_manifest.md), [descriptor](../data/layer_descriptor.md), [catalog item](../data/layer_catalog_item.md) | Existing object contracts under `contracts/data/`; all three were opened for this update. |
| Paired candidate shape | [Data LayerManifest schema](../../schemas/contracts/v1/data/layer_manifest.schema.json) | Legacy permissive profile plus strict inactive fixture profile. |
| Parallel layer shapes | [Layer schema family](../../schemas/contracts/v1/layers/README.md) | Existing proposal scaffolds, not an adopted replacement for the paired data schemas. |
| Candidate validation | [LayerManifest validator](../../tools/validators/data/validate_layer_manifest.py) and [tests](../../tests/validators/test_validate_layer_manifest.py) | Local schema and deterministic checks; not reference resolution or release. |
| Admission projection meaning | [Runtime admission contract](../runtime/layer_manifest_admission.md) | Separate fixture-only eligibility/denial boundary. |
| Admission implementation | [Explorer evaluator](../../apps/explorer-web/src/features/map_runtime/layer_manifest_admission.ts) | Returns finite results with no registry mutation or MapLibre source creation. |
| Layer registry | [Registry README](../../data/registry/layers/README.md) | Identity/routing/control records; this review does not establish append-only enforcement or a live registry resolver. |
| Architecture | [UI layering reference](../../docs/architecture/ui/LAYERING.md) | Explanatory lineage; its older whole-runtime checkpoint must not substitute for current code or runtime evidence. |

Policy rules remain under `policy/`; lifecycle instances, receipts, proofs, catalog projections, and released data carriers remain under their governed `data/` lanes; release decisions and rollback records remain under `release/`. Runtime implementation remains outside this contract lane. These are responsibility boundaries, not claims that those systems are operational.

## Current contract surface

| Object/profile | Evidence and maturity | What a consumer may conclude |
|---|---|---|
| `LayerManifest` semantic contract | **CONFIRMED / DRAFT:** existing data-family contract, v0.3. | Defines a versioned representation and distinct source/evidence/policy/review/release/artifact/time/exposure/lineage references. |
| Data `LayerManifest` strict profile | **CONFIRMED / IMPLEMENTED, bounded:** schema and validator for `PROPOSED_INACTIVE` / `FIXTURE_ONLY` candidates. | Applicable shape and local deterministic rules can be checked; no public use follows. |
| Data `LayerManifest` legacy profile | **CONFIRMED / IMPLEMENTED, permissive:** no `object_type`; `id` required; extra properties allowed. | Backward compatibility only; strict semantic checks are intentionally not applied. |
| `LayerDescriptor` | **CONFIRMED / DRAFT:** [paired data schema](../../schemas/contracts/v1/data/layer_descriptor.schema.json) requires only `id`, with optional string `version` and `spec_hash` and extra properties allowed. | Renderer-facing meaning exists; the placeholder shape does not enforce full trust semantics. |
| `LayerCatalogItem` | **CONFIRMED / DRAFT:** [paired data schema](../../schemas/contracts/v1/data/layer_catalog_item.schema.json) has the same minimal shape. | Discovery/list meaning exists; listing does not authorize loading or exposure. |
| Parallel `layers/` schemas | **CONFIRMED / DRAFT:** [manifest](../../schemas/contracts/v1/layers/layer_manifest.schema.json), [descriptor](../../schemas/contracts/v1/layers/layer_descriptor.schema.json), and [catalog item](../../schemas/contracts/v1/layers/layer_catalog_item.schema.json) each have `properties: {}`, `additionalProperties: true`, no required fields, and `contract_doc: null`. | Even an empty object can satisfy these scaffolds; do not present their validation as substantive layer validation. |
| Runtime admission projection | **CONFIRMED / IMPLEMENTED, bounded:** separate synthetic evaluator, including selection-to-layer matching. | Eligibility or refusal within that fixture profile only; never real registration, reference authentication, or publication. |

The schema family's `layer_descriptor.fauna-profile.example.json` is an example carrier, not another schema or a released fauna layer. Domain profiles and adjacent `LegendDescriptor`, `StyleManifest`, `TileArtifactManifest`, and `MapReleaseManifest` families are outside this subtree's inventory. Their repository-wide maturity is **NOT INSPECTED** here; this README neither declares them absent nor commissions duplicate definitions.

### Candidate validation is not runtime admission

The strict data manifest remains `lifecycle_state: CANDIDATE`. Its validator checks content-derived identity, reference ordering/uniqueness and role separation, floating-reference denial, representation/zoom/bounds consistency, temporal ordering, declared exposure constraints, and false-valued governance flags. See the existing [contract](../data/layer_manifest.md) for field-level meaning instead of copying its schema here.

Its `PUBLIC` audience and `APPROVED` rights fields are candidate declarations. A passing fixture does not establish actual rights clearance, public-safe geometry, authenticated review, or an issued release. Artifact references are not artifact-byte verification; budgets are not measured performance; drawer/Focus flags are not implemented or authorized user interactions.

The separate admission evaluator holds legacy and inactive profiles and candidate lifecycle state. Its positive case uses a **synthetic released-runtime projection**, not a way to promote the strict candidate by changing labels. Even on `PASS`, the result fixes `authority: "NONE"`, `registryMutated: false`, `maplibreSourceCreated: false`, and retains `RUNTIME_REGISTRATION_NOT_EXECUTED`. Selection admission additionally rejects a projection for a different selected layer. Neither evaluator resolves real evidence or authenticates its carried release assertions.

## Object family meanings

| Meaning | Object or boundary | Must not become |
|---|---|---|
| Catalog discovery | `LayerCatalogItem` describes what can be listed and what trust state must be visible. | Payload, renderer command, or permission to load. |
| Renderer handoff | `LayerDescriptor` describes a representation-facing reference and its trust context. | Source truth, evidence resolution, or a renderer implementation. |
| Layer manifesting | `LayerManifest` binds an exact representation/version and its supporting references. | Release approval, policy execution, or verified artifact bytes. |
| Admission projection | The runtime contract describes fixture-only eligibility and finite denial. | A registry writer, live loader, or authenticated release decision. |
| Legend, style, and asset interpretation | Existing owner contracts must explain classes, ramps, units, scale, transforms, and integrity claims. | A new writable family under this compatibility lane. |
| Feature interaction | A selection supplies context for governed evidence, export, or Focus handling. | Evidence inferred from rendered geometry or untrusted feature properties. |

## Anti-collapse rules

| Keep separate from layer metadata | Why |
|---|---|
| Source data and `SourceDescriptor` | A derived representation neither captures RAW source bytes nor admits source identity, rights, cadence, or authority. |
| `EvidenceRef` and `EvidenceBundle` | A carried locator must resolve to admissible support; neither a layer nor a catalog hit supplies evidence closure. |
| `PolicyDecision` and review | A field, boolean, fixture assertion, or successful check does not execute policy or authenticate independent approval. |
| Release and promotion decisions | A manifest, commit, PR, or successful render is not a governed transition to `PUBLISHED`. |
| Receipts and proofs | A record of an action does not establish all of the action's evidentiary or release preconditions. |
| Renderer and published artifacts | Style JSON, PMTiles, COG, GeoParquet, MVT, scenes, and screenshots are carriers, not semantic or domain truth. |
| Domain meanings and AI answers | Domain owners retain object meaning; generated explanations remain subordinate to admissible evidence. |

## Accepted inputs

This existing README may be maintained in place. Short compatibility, migration, and backlink notes may document a separately governed change, but must identify their scope, authority, consumers, and rollback. They must not silently become new object contracts or parallel registries.

New authoritative layer contracts here require an explicit family-routing decision or governed migration with dependency closure. That condition does **not** freeze safe same-path corrections to the existing data contracts, their paired schemas, tests, or this orientation guide.

## Exclusions

| Excluded material | Owning responsibility |
|---|---|
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, or PUBLISHED instances | Governed lifecycle lanes under `data/`, not semantic Markdown. |
| Machine schemas or duplicated executable shapes | `schemas/`; retain the existing paired family until an authorized change. |
| Executable policy, access rules, or sensitivity decisions | Policy rule source under `policy/`; decision records with their governed process or release. |
| Fixtures, validators, test code | Existing fixture, validator, and test roots; examples do not become authority. |
| Tiles, raster/vector assets, sprites, glyphs, or style JSON | Governed data/artifact and runtime owners, not this directory. |
| Release-instance manifests, correction notices, withdrawal or rollback records | `release/` or the accepted instance family; their semantic definitions remain contracts. |
| Map UI, adapters, SDKs, pipeline code, or model clients | Existing implementation roots, not the contract compatibility lane. |

## Layer trust rules

The lifecycle remains `RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED`. Promotion is a governed transition, not a file move, schema pass, or layer toggle.

Public clients consume governed APIs or released public-safe artifacts, never RAW, WORK, QUARANTINE, unpublished internal stores, or direct model output. Consequential claims resolve `EvidenceRef -> EvidenceBundle`; insufficient support must remain visible rather than be replaced by plausible prose or renderer properties.

Before exposure, preserve source role, geographic and temporal scope, attribution, rights, sensitivity, evidence, policy, review, release, correction, and rollback context. Observation time, source-update time, evaluation time, and release time must not silently substitute for each other. Unknown coverage is not zero; stale or superseded support is not current support.

> [!WARNING]
> **Style is not access control.** Hiding a layer, lowering opacity, filtering features, suppressing a popup, or restricting zoom does not protect data already delivered to a browser. Sensitive fields and geometry require policy-directed withholding, redaction, generalization, aggregation, staged access, or denial before delivery, with transform reasons and lineage preserved.

Feature clicks route through governed evidence handling. Exports, comparison views, cached vectors, legends, and AI summaries must preserve applicable restrictions and correction lineage. A correction or withdrawal requires governed propagation; this README does not implement cache invalidation or rollback execution.

### Finite outcomes stay local to their contract

| Surface | Vocabulary | Meaning and limit |
|---|---|---|
| Data manifest validator | `PASS` / `FAIL` / `ERROR` | Applicable local checks pass, conformance fails, or evaluation cannot safely complete. Not policy or release outcomes. |
| Fixture runtime admission | `PASS` / `HOLD` / `DENY` / `ERROR` | Synthetic eligibility or a finite refusal. No side effect or authority is created. |
| Governed answer design | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | User-facing interpretation must follow its own governing contract; not an automatic translation of validator output. |

Candidate trust states such as `CANDIDATE`, `DEGRADED`, `STALE`, and `HELD` are metadata, not the same enum as validator results, release states, or answer outcomes. Apply the specific consumer and policy rules; do not invent a universal status conversion in this README.

## Validation

For changes to the paired data manifest, the inspected validator and test entrypoints are:

```bash
python -m unittest tests.validators.test_validate_layer_manifest --verbose
python tools/validators/data/validate_layer_manifest.py --fixtures
```

Run these from a complete repository checkout with its declared dependencies. The fixture runner checks expected outcomes and finding codes as well as fixture inventory; negative fixtures must retain their expected failure polarity. Do not run the permissive parallel `layers/` schemas instead and call that equivalent validation.

This README update was checked as documentation against connector-read, commit-pinned evidence. It does not report these repository-native commands, hosted CI, browser tests, or end-to-end source/release checks as passed. The accompanying authoring receipt records executed checks and unrun coverage separately.

## Migration checklist

Before changing family routing or making `contracts/layers/` an object-contract authority:

- [ ] Record the exact accepted decision or governed migration scope, owners, source and destination paths, and rollback.
- [ ] Decide independently whether each semantic contract stays under `contracts/data/` and how each parallel schema is retained, profiled, redirected, or retired.
- [ ] Inventory consumers, schema `$id` and `$ref` relationships, contract metadata, registries, fixtures, validator bindings, tests, and inbound documentation links.
- [ ] Preserve the legacy profile deliberately or provide explicit breaking-change impact, migration, compatibility tests, and rollback; do not silently apply strict rules to old instances.
- [ ] Preserve the candidate-validation versus runtime-admission distinction and selection-to-layer binding, including deterministic negative fixtures.
- [ ] Update affected references atomically, retaining compatibility pointers and established document IDs/anchors where required.
- [ ] Keep data instances, executable policy, released artifacts, release decisions, and runtime code outside contract prose; verify applicable public-path and correction behavior before any later activation.

No migration is performed or accepted by this update.

## Open verification

Family convergence, descriptor/catalog field completeness and operative validation, live source/evidence resolution, rights and sensitivity enforcement, release authentication, artifact/signature verification, public loading, and correction/rollback execution require their own current evidence. The existence of a metadata-declared validator path is not implementation proof.

The wider Explorer and MapLibre runtime are **NOT INSPECTED** for readiness in this documentation slice. Do not copy older architecture claims that the renderer is absent, or interpret fixture admission as proof that all present runtime consumers are governed. Independent review and hosted exact-head validation remain separate handoff checks.

## Evidence basis

Repository links above are interpreted at the pinned commit, not as floating evidence of future state. Implementation findings come from the actual schemas and evaluators; accepted placement comes from ADR-0029 and its exact adopted Directory Rules bytes. Older architecture and object-contract checkpoints are lineage where current code differs.

| External workspace source inspected | Role and limit |
|---|---|
| Google Drive: *Direct plan for building KFM*, document `1xykJzHwdYevZPdk2R1keDtPjKssAUgwxmDhm5pbOO0A`, modified 2026-05-03 | Planning lineage for released-layer → governed API → EvidenceBundle → Evidence Drawer and bounded Focus. Its historical path and stack proposals do not override accepted decisions or current code. |
| Notion: *Close governed MapLibre runtime probe matrix*, page `3c9a9202-1bf6-8146-ab6a-ca4e03139382` | Coordination evidence that configuration/fixture progress and runtime-probe readiness are separate. Its PR and CI summaries are not re-certified here as current GitHub state. |

The original `Directory Rules.pdf` was not located in the bounded Drive search. Placement is based on the accepted, exact-byte repository adoption, not an inferred PDF revision. Drive was read-only; this README does not turn Notion coordination or source plans into repository authority.

## Rollback

Restore this README from **blob `b340d48ba17b7d303b0863f1574bbacbad2c17ea`**, as recorded at the evidence snapshot, or revert the scoped update through review. Retain the generated-work receipt as historical accountability; do not rewrite it as approval or erase the authoring trail.

The former stub blob `5a9510af8c9a4386a5d738788c63697627ad0ee5` remains v0.1 lineage, not the rollback target for v0.2. Restore the complete previous README rather than discarding its intervening content.

This documentation change has no schema, data, registry, policy, runtime, release, deployment, or publication state to roll back. A later functional migration must supply its own rollback and correction evidence.

[Back to top](#top)
