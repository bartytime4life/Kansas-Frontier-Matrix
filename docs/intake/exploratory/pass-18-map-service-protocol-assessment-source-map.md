<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-map-service-protocol-assessment
title: Pass 18 Map Service Protocol Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: draft; proposed-inactive; implementation-candidate
owners: OWNER_TBD — Intake steward · Source steward · Map steward · Rights reviewer
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; source-lineage; map-service; pmtiles; xyz; wmts; wms
responsibility: Preserve source and repository lineage for a bounded map-service protocol assessment without contacting services, activating sources, mutating caches or layers, or granting release or public-use authority.
truth_posture: "CONFIRMED attached-card transcription, visual review, and inspected-repository comparison; PROPOSED bounded KFM adaptation; UNKNOWN source adoption and reviewer ownership; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../../../contracts/source/map_service_protocol_assessment.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/source/source_rights_currentness_assessment.md
  - ../../../contracts/source/source_health_assessment.md
  - ../../../contracts/data/layer_manifest.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Map Service Protocol Assessment Source Map

## Evidence basis

| Evidence | Observation | Status |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, physical PDF pages 436-438 / printed pages 433-435 | Cards `KFM-P18-INV-073` and `KFM-P18-INV-180` call for explicit PMTiles/XYZ/WMTS/WMS protocol declarations with protocol-specific access, attribution, caching, freshness, validation, and fail-closed treatment of mutable or unverified external services. All three pages were rendered and visually inspected. | `CONFIRMED` |
| `schemas/contracts/v1/source/source_descriptor.schema.json` | `SourceDescriptor` models WMS and WMTS access methods plus general rights, attribution, cadence, and access posture, but does not declare a closed four-protocol validation matrix. | `CONFIRMED` adjacent responsibility |
| `schemas/contracts/v1/data/layer_manifest.schema.json` | The inactive strict `LayerManifest` supports PMTiles and XYZ representation declarations, but not protocol-specific WMTS/WMS capabilities evidence, cache, and health coherence. | `CONFIRMED` adjacent responsibility |
| `tools/validators/maplibre/validate_source_metadata.py` | The existing no-network validator checks generic renderer metadata and digest projection; its own boundary disclaims source, rights, evidence, policy, review, release, publication, and remote-byte authority. | `CONFIRMED` adjacent responsibility |
| Starting `main@bd59127604f3ab7578fe43f30caaeef089c0fffc` plus repository, code, branch, and PR searches | No exact card IDs, four-protocol assessment contract, schema, fixture family, validator, workflow, matching branch, or open matching PR was found before implementation. | `CONFIRMED` inspected snapshot |

The attached and Drive sources are design evidence, not permission to contact an
endpoint, accept terms, verify rights, activate a source, populate a cache, or
publish a map.

## Selected increment

| Source pressure | Bounded adaptation | Held boundary |
|---|---|---|
| Declare the actual map protocol. | Closed `PMTILES`, `XYZ`, `WMTS`, and `WMS` classes map to distinct access surfaces and local evidence kinds. | No endpoint parsing, tile request, capabilities request, or artifact-byte inspection. |
| Treat immutable packages differently from remote services. | PMTiles requires a non-placeholder artifact digest and immutable cache posture; remote protocols remain mutable `CONTEXT_ONLY` references. | No artifact verification, cache write, evidence admission, or source-role promotion. |
| Keep rights, attribution, freshness, and health visible. | Compose existing assessment responsibilities by opaque ref and fail closed on blocked rights, missing attribution, stale service state, and unresolved controls. | No reference resolution, rights decision, health probe, or policy inference. |
| Prevent a protocol declaration from becoming public authority. | Every activation, fetch, verification, cache, layer, release, publication, and public-use effect is fixed to `false`. | No registry, layer, release, deployment, or public state changes. |

## Directory Rules basis

| Artifact | Owning root and scope | Outcome |
|---|---|---|
| Source assessment meaning | `contracts/source/` owns source protocol semantics. | `PLACE` |
| Closed machine shape | `schemas/contracts/v1/source/` owns the Draft 2020-12 schema. | `PLACE` |
| Public-safe replay and validation | `fixtures/contracts/v1/source/`, `tools/validators/source/`, and `tests/validators/` own deterministic conformance. | `PLACE` |
| Source lineage and read-only CI | `docs/intake/exploratory/` and `.github/workflows/` retain their non-authoritative roles. | `PLACE` |

No new root, source registry entry, rights rule, service connector, capabilities
cache, tile cache, layer registration, release lane, or public path is created.

## Deferred questions

- Which source and map steward roles may adopt a protocol declaration for a real service?
- What concrete PMTiles header, XYZ template, and OGC capabilities assessment objects should satisfy the opaque evidence refs?
- How should authentication, rate limits, vendor terms, tile expiry, and service-version drift be governed at runtime?
- Whether WMTS or WMS should later become direct strict `LayerManifest` representations remains a separate design decision.

## Rollback

Rollback is a focused revert of the additive packet. No endpoint, artifact,
source, cache, layer, registry, release, deployment, or public artifact requires
restoration.
