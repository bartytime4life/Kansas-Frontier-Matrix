<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION-ADR-agriculture-schema-home
title: ADR-agriculture-schema-home
type: standard
version: v1
status: draft
owners: OWNER_TBD_NEEDS_VERIFICATION
created: 2026-05-08
updated: 2026-05-08
policy_label: NEEDS_VERIFICATION
related: [./README.md, ./ADR-0001-schema-home.md, ./ADR-0002-responsibility-root-monorepo.md, ../domains/agriculture/README.md, ../domains/agriculture/governance/STATE_OF_LANE.md, ../domains/agriculture/governance/VALIDATION_PLAN.md, ../domains/agriculture/architecture/DATA_CONTRACTS.md, ../domains/agriculture/architecture/EVIDENCE_AND_PROVENANCE.md, ../../schemas/README.md, ../../contracts/README.md, ../../policy/README.md]
tags: [kfm, adr, agriculture, schema-home, contracts, schemas, source-role, validation, evidence, rollback]
notes: [Replaces the thin backlog placeholder with an evidence-bounded proposed Agriculture schema-home decision. Target file exists in the GitHub main branch. Owners, CODEOWNERS, policy label, exact machine schema subpath enforcement, validator commands, CI workflow evidence, release artifacts, and runtime behavior remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-agriculture-schema-home

Proposed placement rule for Agriculture lane machine schemas, semantic contract companions, and validation-linked schema consumers.

<p align="center">
  <img alt="ADR status: proposed" src="https://img.shields.io/badge/ADR-proposed-lightgrey">
  <img alt="scope: agriculture schema home" src="https://img.shields.io/badge/scope-agriculture%20schema%20home-6f42c1">
  <img alt="machine schema home: proposed" src="https://img.shields.io/badge/machine%20schema%20home-PROPOSED-yellow">
  <img alt="contracts: meaning" src="https://img.shields.io/badge/contracts-meaning-5319e7">
  <img alt="policy: fail closed" src="https://img.shields.io/badge/policy-fail--closed-b60205">
  <img alt="enforcement: needs verification" src="https://img.shields.io/badge/enforcement-NEEDS%20VERIFICATION-ffb000">
</p>

<p align="center">
  <a href="#decision-summary">Decision</a> ·
  <a href="#evidence-boundary">Evidence</a> ·
  <a href="#problem">Problem</a> ·
  <a href="#options-considered">Options</a> ·
  <a href="#placement-rules">Placement</a> ·
  <a href="#schema-family-scope">Schema families</a> ·
  <a href="#validation-plan">Validation</a> ·
  <a href="#acceptance-criteria">Acceptance</a> ·
  <a href="#rollback-and-supersession">Rollback</a>
</p>

> [!IMPORTANT]
> **Decision status:** `PROPOSED`.
>
> **Preferred Agriculture machine-schema home:** `schemas/contracts/v1/domains/agriculture/`.
>
> This ADR must not be treated as accepted or enforced until the global schema-home decision is accepted or superseded, the active checkout inventory is verified, conflicting Agriculture schema homes are reconciled, owners/reviewers are confirmed, and fixture/validator/CI evidence proves the rule.

> [!NOTE]
> This file revises a backlog placeholder. It records an evidence-bounded proposed decision; it does **not** claim that Agriculture schemas, validators, policy bundles, fixtures, workflow gates, API routes, MapLibre layers, Evidence Drawer payloads, Focus Mode payloads, ReleaseManifests, proof packs, or rollback cards already exist or are enforced.

---

## Decision summary

| Field | Determination |
|---|---|
| ADR | `docs/adr/ADR-agriculture-schema-home.md` |
| Status | `proposed` |
| Scope | Agriculture lane machine schemas and adjacent contract/schema/policy/test placement |
| Preferred machine-schema home | `schemas/contracts/v1/domains/agriculture/` |
| Global dependency | [`ADR-0001-schema-home.md`](./ADR-0001-schema-home.md) |
| Root-layout dependency | [`ADR-0002-responsibility-root-monorepo.md`](./ADR-0002-responsibility-root-monorepo.md) |
| Semantic contract companion | `contracts/domains/agriculture/` or repo-confirmed contract convention; existing [`../domains/agriculture/architecture/DATA_CONTRACTS.md`](../domains/agriculture/architecture/DATA_CONTRACTS.md) remains architecture guidance, not machine-schema authority |
| Policy surface | `policy/domains/agriculture/` or repo-confirmed policy convention |
| Source registry surface | `data/registry/agriculture/` or repo-confirmed registry convention |
| Fixture/test surface | `fixtures/domains/agriculture/` and `tests/domains/agriculture/`, or repo-confirmed fixture/test conventions |
| Enforcement maturity | `NEEDS VERIFICATION` |
| Fail-safe rule | Ambiguous Agriculture schema resolution must fail closed. |

### Proposed decision rule

KFM should place Agriculture lane machine-checkable contract schemas under:

```text
schemas/contracts/v1/domains/agriculture/
```

This path is proposed because it combines:

1. the global machine-schema root proposed in `ADR-0001-schema-home.md`;
2. the responsibility-root and domain-subpath discipline accepted in `ADR-0002-responsibility-root-monorepo.md`;
3. Agriculture documentation that already treats exact machine schema subpath as unresolved and warns against parallel `contracts/` versus `schemas/` authority.

### Authority sentence

> `contracts/` defines meaning, `schemas/contracts/v1/` defines machine-checkable shape, `policy/` decides admissibility, and fixtures/tests/validators prove the split. Agriculture should inherit that split without creating a domain-specific exception by inertia.

[Back to top](#top)

---

## Evidence boundary

This ADR is based on current GitHub connector evidence, adjacent repository documentation, and the supplied KFM doctrine corpus. A local mounted checkout was not available in this workspace, so branch dirty state, local test output, workflow logs, dashboards, runtime traces, and emitted release/proof objects remain `UNKNOWN`.

| Evidence item | Status | Supports | Does not prove |
|---|---:|---|---|
| Existing target file | `CONFIRMED` | `docs/adr/ADR-agriculture-schema-home.md` exists as a thin proposed placeholder and needs replacement with evidence-linked decision language. | Acceptance, enforcement, or schema presence. |
| ADR index | `CONFIRMED` | ADRs belong in `docs/adr/` as human-facing decision records; ADR status and enforcement status stay separate. | Complete ADR coverage or CI enforcement. |
| ADR template | `CONFIRMED` | KFM ADRs should expose evidence, impact, policy risk, validation, rollback, and supersession. | That this specific ADR is accepted. |
| Global schema-home ADR | `CONFIRMED / PROPOSED` | `schemas/contracts/v1/` is the proposed canonical machine-contract schema root; `contracts/` remains semantic meaning; `policy/` remains admissibility. | Final acceptance or enforcement of that global rule. |
| Responsibility-root ADR | `CONFIRMED / ACCEPTED decision` | Domain names should not become root folders; domain work belongs under responsibility roots such as `docs/domains/`, `schemas/contracts/v1/domains/`, `policy/domains/`, and `tests/domains/`. | Every subpath convention or current implementation file. |
| Agriculture README | `CONFIRMED docs` | Agriculture has a structured in-repo documentation package; implementation surfaces remain `NEEDS VERIFICATION`. | Live source activation, schemas, validators, runtime, or release objects. |
| Agriculture state snapshot | `CONFIRMED docs` | Agriculture documentation control plane is confirmed; enforcement remains `NEEDS VERIFICATION`; machine schema home is `NEEDS VERIFICATION / CONFLICTED`. | Current CI, runtime, proof, or release behavior. |
| Agriculture data contracts | `CONFIRMED docs` | Agriculture contract map lists exact schema-home ambiguity, source-role discipline, shared trust objects, and proposed Agriculture object families. | Machine schema files or accepted subpath. |
| Agriculture validation plan | `CONFIRMED docs` | Agriculture validation is fixture-first and fail-closed; public claims must resolve released artifacts, governed APIs, and `EvidenceBundle` support. | Runnable validator commands or workflow success. |
| `schemas/README.md` | `CONFIRMED docs` | `schemas/contracts/v1/` is a visible machine-file scaffold, but canonical authority is still unresolved until ADR and enforcement evidence settle it. | Agriculture subpath or accepted schema-home law. |
| `contracts/README.md` | `CONFIRMED docs` | `contracts/` owns object meaning and compatibility, not silent machine-schema authority. | Agriculture semantic contract files or schema enforcement. |
| `policy/README.md` | `CONFIRMED docs` | Policy decides rights, sensitivity, review, release, correction, and runtime admissibility after validation. | Agriculture-specific policy bundles. |
| Local workspace scan | `CONFIRMED` | The local visible workspace was not a mounted Git checkout. | Absence of the repository; GitHub connector access confirms repository evidence is available. |

### Truth labels

| Label | Meaning in this ADR |
|---|---|
| `CONFIRMED` | Verified from current repository connector evidence, current workspace inspection, or supplied KFM doctrine. |
| `PROPOSED` | Recommended placement, rule, schema family, validator, test, or migration path not yet proven as active implementation. |
| `UNKNOWN` | Not verified strongly enough in this session. |
| `NEEDS VERIFICATION` | A concrete repository, workflow, owner, source, rights, schema, test, or runtime check can retire the uncertainty. |
| `CONFLICTED` | Multiple plausible authority signals exist and cannot be collapsed silently. |
| `LINEAGE` | Prior reports or scaffolds preserve design pressure but do not prove current repository implementation. |

[Back to top](#top)

---

## Problem

The Agriculture lane needs machine schemas for source descriptors, observations, aggregate statistics, gridded products, derived indicators, layer manifests, Evidence Drawer payloads, Focus Mode payloads, release objects, and validation reports.

The current problem is not simply “where should a file go?” It is an authority problem.

Agriculture materials currently point to multiple possible homes:

| Candidate home | Current posture | Risk |
|---|---:|---|
| `schemas/contracts/v1/domains/agriculture/` | `PROPOSED` | Best aligned with responsibility-root domain placement, but exact current repo convention must be verified. |
| `schemas/contracts/v1/agriculture/` | `PROPOSED / NEEDS VERIFICATION` | Shorter path, but less aligned with the domain-subpath pattern in the responsibility-root ADR. |
| `contracts/agriculture/*.schema.json` | `LINEAGE / CONFLICTED` | Prior scaffold-style path; risks making semantic contracts and machine schemas compete. |
| `contracts/domains/agriculture/` | `PROPOSED semantic companion` | Useful for meaning/compatibility, but not proposed as active machine-schema authority. |
| Do nothing / keep placeholder | `REJECTED` | Leaves Agriculture schema-home drift unresolved and weakens validators, fixtures, policy, release, and runtime consumers. |

A weak decision here would let the lane grow schemas, fixtures, validators, policies, and runtime DTOs under different assumptions. That would directly weaken KFM’s cite-or-abstain, fail-closed, release, correction, and rollback posture.

[Back to top](#top)

---

## Requirements and constraints

### KFM invariants checked

| Invariant | Agriculture schema-home implication | Status |
|---|---|---:|
| `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` | Schemas must support lifecycle-safe validation before artifacts become catalog or public release candidates. | `CONFIRMED doctrine` |
| Public clients use governed interfaces | Public DTO/layer schemas must not allow RAW, WORK, QUARANTINE, unpublished candidate, internal receipt, or direct model paths. | `CONFIRMED doctrine / PROPOSED validation` |
| `EvidenceRef -> EvidenceBundle` before consequential claims | Agriculture public claims, layers, Evidence Drawer payloads, and Focus Mode responses must reference resolvable evidence support. | `CONFIRMED doctrine / PROPOSED schema burden` |
| Promotion is a governed state transition | Release-related Agriculture schemas must support `PromotionDecision`, `ReleaseManifest`, proof refs, correction, and rollback. | `CONFIRMED doctrine / PROPOSED schema burden` |
| Source role is part of meaning | Aggregate, station, grid, remote-sensing, derived, and authority sources must not share unsafe claim affordances. | `CONFIRMED Agriculture docs` |
| Unknown rights/sensitivity fail closed | Source and release schemas must carry rights, sensitivity, policy labels, and obligations sufficient to block public release. | `CONFIRMED policy posture / PROPOSED validation` |
| AI is interpretive only | Agriculture Focus Mode schemas must require released evidence context and finite outcomes; generated language is not root truth. | `CONFIRMED doctrine / PROPOSED schema burden` |
| Derived surfaces stay derived | PMTiles, summaries, tiles, dashboards, embeddings, scenes, and layer manifests are rebuildable carriers, not sovereign truth. | `CONFIRMED Agriculture docs` |

### Non-goals

This ADR does **not** decide:

- the full schema versioning policy beyond the Agriculture `v1` placement rule;
- the full JSON Schema contents for each Agriculture object;
- OpenAPI route names, API framework, UI component paths, or runtime DTO implementations;
- policy-as-code package names or Rego module paths;
- source activation for SSURGO/SDA, gSSURGO/gNATSGO, Kansas Mesonet, SCAN, USCRN, SMAP, HLS/HLS-VI, NASS, or CDL;
- live source terms, quotas, licenses, API keys, or automation permissions;
- branch protection, CI runner behavior, dashboards, logs, release state, or deployment posture.

[Back to top](#top)

---

## Options considered

| Option | Description | Benefits | Risks / costs | Outcome |
|---|---|---|---|---|
| A | `schemas/contracts/v1/domains/agriculture/` | Aligns with global `schemas/contracts/v1/` proposal and domain-under-responsibility-root discipline. | Exact active repo convention still needs verification. | **Preferred / PROPOSED** |
| B | `schemas/contracts/v1/agriculture/` | Shorter and already appears in Agriculture planning as a candidate. | Less aligned with `domains/<domain>` placement; could become a domain exception by convenience. | Deferred unless repo evidence proves this convention is stronger. |
| C | `contracts/agriculture/*.schema.json` | Preserves older scaffold lineage. | Conflates semantic contract home with machine-schema authority; conflicts with ADR-0001 direction. | Rejected for active machine schemas; retain only as lineage/migration input. |
| D | `contracts/domains/agriculture/` | Good semantic companion path under responsibility-root discipline. | Not a machine-schema home. | Accepted only as semantic/narrative companion after repo convention verification. |
| E | Keep placeholder only | Minimal change. | Leaves schema-home ambiguity unresolved and unusable for implementation review. | Rejected. |

[Back to top](#top)

---

## Decision

### Chosen option

This ADR proposes:

```text
schemas/contracts/v1/domains/agriculture/
```

as the Agriculture lane’s canonical machine-schema home after acceptance.

### Decision details

1. Agriculture machine-checkable schemas should live under `schemas/contracts/v1/domains/agriculture/` once this ADR and its global dependency are accepted.
2. Agriculture semantic contract explanations should live under `contracts/domains/agriculture/` or a repo-confirmed semantic contract convention. Existing Agriculture documentation under `docs/domains/agriculture/architecture/` remains architecture guidance unless moved or superseded through a reviewed change.
3. Agriculture policies should live under `policy/domains/agriculture/` or a repo-confirmed policy convention; policy paths remain `NEEDS VERIFICATION`.
4. Agriculture source descriptors should live under `data/registry/agriculture/` or a repo-confirmed source registry convention.
5. Agriculture fixtures and tests should live under responsibility-root fixture/test paths such as `fixtures/domains/agriculture/` and `tests/domains/agriculture/`, or repo-confirmed equivalents.
6. Existing or discovered Agriculture schemas outside the chosen home must be mapped as `PRESERVE`, `MIGRATE`, `ALIAS`, `SUPERSEDE`, `ARCHIVE`, or `REMOVE WITH SUCCESSOR`. They must not remain parallel active schemas.
7. Any ambiguity in schema resolution must return `ERROR`, `DENY`, or review hold rather than choosing a path by convenience.

### Relationship to global schema-home ADR

This domain ADR is subordinate to `ADR-0001-schema-home.md`.

If ADR-0001 is accepted with `schemas/contracts/v1/` as the canonical machine-contract root, this Agriculture ADR can be accepted after it proves the domain subpath and migration/validation plan.

If ADR-0001 is superseded or chooses another canonical machine-schema root, this ADR must be revised or superseded before Agriculture machine schemas are landed.

[Back to top](#top)

---

## Placement rules

| Artifact | Proposed home | Status | Rule |
|---|---|---:|---|
| Agriculture JSON Schemas | `schemas/contracts/v1/domains/agriculture/*.schema.json` | `PROPOSED` | Machine-checkable shape only after acceptance. |
| Agriculture schema index | `schemas/contracts/v1/domains/agriculture/README.md` | `PROPOSED` | Should list schema family, version, shared dependencies, fixtures, validators, and migration notes. |
| Agriculture semantic contracts | `contracts/domains/agriculture/` or repo-confirmed contract convention | `NEEDS VERIFICATION` | Meaning and compatibility, not machine-schema authority. |
| Agriculture architecture docs | `docs/domains/agriculture/architecture/` | `CONFIRMED docs` | Guidance and evidence posture, not executable schema authority. |
| Agriculture source descriptors | `data/registry/agriculture/` or repo-confirmed registry convention | `NEEDS VERIFICATION` | Source identity, role, rights, sensitivity, stable keys, activation state. |
| Agriculture policy | `policy/domains/agriculture/` or repo-confirmed policy convention | `NEEDS VERIFICATION` | Rights, sensitivity, source-role, public-precision, release, correction, and runtime admissibility. |
| Agriculture validators | `tools/validators/...` or repo-confirmed tooling convention | `NEEDS VERIFICATION` | Deterministic checks; do not define schema meaning. |
| Agriculture fixtures | `fixtures/domains/agriculture/` or repo-confirmed fixture convention | `NEEDS VERIFICATION` | Valid/invalid examples; negative fixtures must fail closed. |
| Agriculture tests | `tests/domains/agriculture/` or repo-confirmed test convention | `NEEDS VERIFICATION` | No-network checks before live source activation. |
| Agriculture lifecycle data | `data/raw/agriculture/`, `data/work/agriculture/`, `data/quarantine/agriculture/`, `data/processed/agriculture/`, `data/catalog/.../agriculture/`, `data/published/agriculture/` or repo-confirmed equivalents | `NEEDS VERIFICATION` | Lifecycle objects are instances, not schema definitions. |
| Agriculture release objects | `release/.../agriculture/` or repo-confirmed release convention | `NEEDS VERIFICATION` | Release manifests, promotion decisions, rollback cards. |
| API/UI/Focus payload implementations | `apps/`, `packages/`, `ui/`, `web/`, or repo-confirmed runtime convention | `UNKNOWN` | Must consume governed schemas/contracts; must not become hidden schema authority. |

### Explicitly prohibited

Do not land new active Agriculture machine schemas in:

```text
contracts/agriculture/*.schema.json
contracts/domains/agriculture/*.schema.json
docs/domains/agriculture/**/*.schema.json
policy/**/agriculture/*.schema.json
apps/**/agriculture/*.schema.json
packages/**/agriculture/*.schema.json
```

unless a successor ADR or migration note explicitly marks them as generated, illustrative, deprecated, compatibility aliases, or non-canonical examples.

[Back to top](#top)

---

## Schema family scope

Agriculture schemas should reuse shared KFM trust-object schemas before creating domain forks.

### Shared schema dependencies

| Shared object | Agriculture use | Rule |
|---|---|---|
| `SourceDescriptor` | Source identity, role, rights, sensitivity, cadence, stable keys, activation state. | Reuse shared schema unless Agriculture needs a documented profile. |
| `EvidenceRef` | Pointer from claim/layer/observation/artifact to evidence. | Reuse shared schema. |
| `EvidenceBundle` | Resolved support package for claims, layers, Evidence Drawer, Focus Mode, and release review. | Reuse shared schema or define Agriculture profile only when justified. |
| `ValidationReport` | Schema, source-role, rights/sensitivity, temporal, unit/depth, geospatial, catalog, and public-path validation. | Reuse shared schema or profile. |
| `DatasetVersion` | Dataset/product snapshot identity. | Reuse shared schema. |
| `DecisionEnvelope` | Finite outcome: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`. | Reuse shared schema; no Agriculture fork by default. |
| `PromotionDecision` | Release-gate decision with validation, policy, catalog, review, and rollback state. | Reuse shared schema. |
| `ReleaseManifest` | Release identity, artifacts, digests, policy label, proof refs, rollback target. | Reuse shared schema. |
| `CatalogMatrix` | STAC/DCAT/PROV/release digest closure. | Reuse shared schema or profile. |
| `CorrectionNotice` | Correction, supersession, withdrawal, public lineage. | Reuse shared schema. |
| `RollbackCard` | Reversible release target and instructions. | Reuse shared schema. |

### Agriculture-specific candidate schemas

These are candidate families, not implemented claims.

| Candidate schema | Purpose | Notes |
|---|---|---|
| `agriculture_observation.schema.json` | Generic observation profile when a more specific schema is not available. | Avoid overuse; specific schemas should preserve source role. |
| `soil_moisture_station.schema.json` | Station metadata, depth availability, variables, provider status. | Station point is not surface truth. |
| `soil_moisture_reading.schema.json` | Station/depth/time soil-moisture reading with unit/QC normalization. | Requires unit, depth, timestamp, QC, source ref. |
| `soil_moisture_anomaly.schema.json` | Derived anomaly/outage/stress event from readings or grid context. | Derived, not observed truth. |
| `ssurgo_mukey_properties.schema.json` | MUKEY-level soil property context consumed from Soil support. | Must not fork Soil-lane authority. |
| `ssurgo_component.schema.json` | SSURGO component/horizon support and component percentage validation. | Requires tolerance validation. |
| `agriculture_aggregate_stat.schema.json` | Aggregate official statistic by geography, time, commodity, statistic, and unit. | Must block field, parcel, operator, or point-level claim affordance. |
| `crop_progress_observation.schema.json` | Crop Progress / phenology aggregate by geography and week/year. | Aggregate-only. |
| `agriculture_grid_product.schema.json` | SMAP, CDL, HLS, or other grid/product slice. | Requires product version, grid/asset refs, CRS, masks/QA, time window. |
| `vegetation_index_observation.schema.json` | HLS/NDVI/VI observation or derived change. | Must preserve STAC/asset/mask/time-window support. |
| `agriculture_derived_indicator.schema.json` | Stress, anomaly, suitability, condition, change, or fused indicator. | Requires inputs, algorithm/spec version, receipt, uncertainty, limitations. |
| `agriculture_layer_manifest.schema.json` | Public map/API layer contract. | Requires release ref, artifact digests, EvidenceBundle refs, policy, correction, rollback. |
| `agriculture_evidence_drawer_payload.schema.json` | UI trust payload for selected feature/layer/claim. | Must expose support class without leaking internal paths. |
| `agriculture_focus_payload.schema.json` | Focus Mode request/response context. | Must require released evidence context and finite outcomes. |

> [!CAUTION]
> Agriculture-specific schemas should extend or profile shared KFM trust objects only when shared schemas are insufficient. Do not create `agriculture_evidence_bundle.schema.json`, `agriculture_decision_envelope.schema.json`, or `agriculture_release_manifest.schema.json` merely because the Agriculture lane needs to reference those objects.

[Back to top](#top)

---

## Source-role guardrails

Agriculture schema placement must preserve source-role meaning. Placement alone cannot make a source authoritative outside its support scope.

| Source family | Source role pressure | Schema implication |
|---|---|---|
| SSURGO / SDA | Authoritative vector/tabular soil survey context. | Preserve MUKEY, component/horizon keys, source version, table/query identity, and Soil-lane boundary. |
| gSSURGO / gNATSGO | Gridded/derived soil companion. | Label as grid/derived companion; do not silently replace SSURGO/SDA provenance. |
| Kansas Mesonet / SCAN / USCRN | Station observations. | Preserve station, depth, variable, unit, timestamp, QC, freshness; block station-as-surface truth without transform. |
| SMAP | Satellite/grid soil-moisture context. | Preserve grid, product/version, granule/time window, QA/mask, support class; block field-level wording. |
| HLS / HLS-VI | Remote-sensing reflectance, vegetation-index, and derived context. | Preserve STAC item/asset, mask/cloud, index formula, time window, product version. |
| NASS QuickStats / Crop Progress | Official aggregate statistics. | Preserve geography/version, commodity, period, statistic, unit; block field/parcel/operator truth. |
| CDL | Annual classified raster context. | Preserve product year, class code, raster/grid, accuracy/caveat metadata. |
| Private/proprietary farm data | Restricted future class. | Block public release by default until a restricted-data lane, consent/authorization, steward review, retention, and revocation policy exist. |

[Back to top](#top)

---

## Validation plan

Validation must prove the placement rule and the Agriculture trust semantics together.

### Placement validation

| Check | Expected behavior |
|---|---|
| Canonical path check | Active Agriculture machine schemas live under the accepted schema home. |
| Duplicate active schema check | No active Agriculture schema is maintained in both `contracts/` and `schemas/`. |
| Alias check | Any legacy or compatibility schema path has explicit target, status, owner, review date, tests, and retirement rule. |
| Fixture mapping check | Valid and invalid Agriculture fixtures map to the accepted schema path or explicit alias. |
| Docs sync check | This ADR, ADR index, Agriculture README, `DATA_CONTRACTS.md`, `VALIDATION_PLAN.md`, `schemas/README.md`, and `contracts/README.md` agree. |
| Future-version check | No `schemas/contracts/v2/.../agriculture` path appears without successor ADR or migration decision. |

### Agriculture semantic validation

| Gate | Required negative case |
|---|---|
| Source-role validation | Aggregate used as field truth fails. |
| Rights/sensitivity validation | Missing rights or missing sensitivity fails. |
| Temporal validation | Missing observed/source/retrieved/release time fails or returns stale/abstain outcome. |
| Unit/depth validation | Soil-moisture reading without depth or unit fails. |
| Geospatial validation | Public exact geometry fails when policy requires generalization. |
| Remote-sensing lineage validation | HLS/SMAP/CDL object without product version, mask/QA, grid/asset, or time window fails. |
| Derived indicator validation | Derived stress/anomaly/suitability result without input refs, algorithm/spec version, receipt, uncertainty, and limitations fails. |
| Catalog closure validation | Mismatched STAC/DCAT/PROV/release digests fail. |
| Evidence closure validation | Public claim without resolved `EvidenceBundle` returns `ABSTAIN`, `DENY`, or `ERROR`. |
| Public path validation | API/layer/Drawer/Focus payload with RAW, WORK, QUARANTINE, unpublished candidate, internal receipt, or direct model path fails. |
| Rollback validation | Release candidate without rollback target fails. |

### Illustrative inventory commands

Run from repository root before accepting this ADR or landing Agriculture schemas.

```bash
git status --short
git branch --show-current
git rev-parse --show-toplevel

find docs/adr docs/domains/agriculture contracts schemas policy tests fixtures tools data release \
  -maxdepth 6 -type f 2>/dev/null \
  | grep -Ei 'agriculture|agri|crop|nass|mesonet|ssurgo|sda|soil_moisture|smap|hls|EvidenceBundle|DecisionEnvelope|PromotionDecision|ReleaseManifest|CatalogMatrix|SourceDescriptor' \
  | sort

git grep -nE 'agriculture schema home|schemas/contracts/v1/(domains/)?agriculture|contracts/(domains/)?agriculture|schema-home|SourceDescriptor|EvidenceBundle|DecisionEnvelope' -- \
  docs contracts schemas policy tests fixtures tools data release .github 2>/dev/null || true
```

> [!WARNING]
> The command block is a review aid, not enforcement proof. Acceptance requires repo-native validators, fixture mapping, CI evidence or reviewer-approved local validation output, and rollback/supersession planning.

[Back to top](#top)

---

## Impact map

| Area | Required action before acceptance | Status |
|---|---|---:|
| `docs/adr/README.md` | Add or update entry for this ADR and status. | `NEEDS VERIFICATION` |
| `docs/adr/ADR-0001-schema-home.md` | Confirm acceptance or successor path. | `NEEDS VERIFICATION` |
| `docs/domains/agriculture/README.md` | Link this ADR as the lane-specific schema-home decision. | `PROPOSED` |
| `docs/domains/agriculture/governance/STATE_OF_LANE.md` | Replace generic schema-home blocker with this ADR’s status when accepted. | `PROPOSED` |
| `docs/domains/agriculture/architecture/DATA_CONTRACTS.md` | Collapse candidate subpaths into the accepted path, or preserve unresolved status if not accepted. | `PROPOSED` |
| `docs/domains/agriculture/governance/VALIDATION_PLAN.md` | Add placement validation and negative fixture targets. | `PROPOSED` |
| `schemas/README.md` | Ensure parent schema lane and domain subpath language agree. | `NEEDS VERIFICATION` |
| `schemas/contracts/v1/` | Add `domains/agriculture/` only after acceptance and inventory. | `PROPOSED` |
| `contracts/README.md` | Ensure semantic contract lane does not claim machine-schema authority. | `NEEDS VERIFICATION` |
| `contracts/domains/agriculture/` | Add only if semantic contract convention is verified. | `PROPOSED` |
| `policy/` | Add or verify Agriculture policy subpath after policy convention is checked. | `NEEDS VERIFICATION` |
| `fixtures/` and `tests/` | Add valid/invalid fixtures and placement tests under repo-confirmed convention. | `PROPOSED` |
| `tools/validators/` | Add schema-home, source-role, public-path, catalog, and rollback checks under repo-confirmed convention. | `PROPOSED` |
| `data/registry/agriculture/` | Source descriptors must reference accepted schemas or shared schema IDs. | `PROPOSED` |
| `release/` | ReleaseManifest and RollbackCard checks must reference accepted schemas. | `PROPOSED` |
| `apps/` / `packages/` / UI surfaces | API, layer, Evidence Drawer, and Focus Mode consumers must reference accepted schemas or shared trust-object schemas. | `UNKNOWN` |

[Back to top](#top)

---

## Acceptance criteria

This ADR can move from `proposed` to `accepted` only when the following are complete or explicitly waived with a documented reason.

- [ ] `ADR-0001-schema-home.md` is accepted or superseded with a compatible global machine-schema root.
- [ ] `ADR-0002-responsibility-root-monorepo.md` remains accepted or a successor confirms domain-under-responsibility-root placement.
- [ ] Active checkout inventory confirms whether any Agriculture machine schemas already exist.
- [ ] Any existing `contracts/agriculture`, `contracts/domains/agriculture`, `schemas/contracts/v1/agriculture`, or other Agriculture machine-schema path is classified as `canonical`, `alias`, `deprecated`, `generated`, `example`, `archive`, or `remove-with-successor`.
- [ ] Owners, CODEOWNERS, and reviewer roles are verified or recorded as explicit unresolved blockers.
- [ ] `schemas/contracts/v1/domains/agriculture/` or the accepted successor path has an index/README before multiple schema files are added.
- [ ] Shared trust-object schemas are inventoried before Agriculture-specific forks are proposed.
- [ ] Valid and invalid fixtures cover the schema-home rule.
- [ ] Negative Agriculture semantics fail closed: missing rights, missing sensitivity, aggregate-as-field, station-as-surface, grid-as-ground-truth, derived-without-inputs, unresolved EvidenceBundle, public internal path leak, and missing rollback target.
- [ ] Validator output, CI run evidence, or reviewer-approved local validation evidence is captured.
- [ ] Agriculture README, state snapshot, data contracts, validation plan, schema docs, contract docs, and ADR index are synchronized.
- [ ] Rollback and supersession strategy is documented for any existing schema files or compatibility aliases.

[Back to top](#top)

---

## Rollback and supersession

### Rollback triggers

| Trigger | Required action |
|---|---|
| Global schema-home ADR chooses a different root | Mark this ADR superseded and migrate Agriculture path language to successor. |
| Active checkout reveals an established Agriculture schema convention incompatible with this ADR | Pause acceptance; classify existing files; decide migration or successor ADR. |
| Validators point to a different path than this ADR | Treat as `CONFLICTED`; do not land more schemas until paths are reconciled. |
| Public runtime or release artifacts reference a legacy schema path | Add compatibility alias or migration plan; do not silently repoint. |
| Agriculture-specific schema duplicates shared trust-object schemas | Prefer shared schema; deprecate Agriculture fork unless an extension is justified and tested. |

### Supersession rule

A successor ADR must:

1. link back to this ADR;
2. name the new canonical Agriculture schema path;
3. classify existing schema files and aliases;
4. preserve migration lineage;
5. update affected docs, schemas, fixtures, validators, policies, source descriptors, release artifacts, and runtime consumers;
6. include rollback evidence or a rollback test plan.

### Compatibility alias rule

Aliases are migration tools, not second authorities.

Every alias must declare:

- alias path;
- canonical target path or schema ID;
- status;
- reason;
- owner;
- created date;
- review/retirement date;
- tests proving resolution and failure behavior;
- rollback note.

[Back to top](#top)

---

## Open verification backlog

| Item | Status | Why it matters |
|---|---:|---|
| Owner / CODEOWNERS for this ADR | `NEEDS VERIFICATION` | Acceptance needs accountable review. |
| Policy label | `NEEDS VERIFICATION` | Public/restricted classification should not be inferred. |
| Global schema-home acceptance | `NEEDS VERIFICATION` | Domain ADR depends on ADR-0001 or successor. |
| Exact Agriculture schema subpath | `NEEDS VERIFICATION` | This ADR proposes `domains/agriculture`, but active checkout and global ADR must confirm. |
| Existing Agriculture machine schemas | `UNKNOWN` | Must be inventoried before migration or acceptance. |
| Shared trust-object schemas | `NEEDS VERIFICATION` | Avoid unnecessary Agriculture forks of EvidenceBundle, DecisionEnvelope, ReleaseManifest, and related objects. |
| Agriculture source descriptor path | `NEEDS VERIFICATION` | Registry convention affects schema refs and source validation. |
| Agriculture policy path | `NEEDS VERIFICATION` | Prior lineage mentions multiple policy path styles. |
| Agriculture fixture/test path | `NEEDS VERIFICATION` | Tests may use `tests/agriculture`, `tests/domains/agriculture`, or another repo-native convention. |
| Validator commands and CI workflow names | `UNKNOWN` | Enforcement cannot be claimed without command/workflow evidence. |
| ReleaseManifest / proof pack / rollback artifacts | `UNKNOWN` | Public release readiness is not proven. |
| Governed API, MapLibre, Evidence Drawer, Focus Mode consumers | `UNKNOWN` | Runtime/UI schema consumption remains unverified. |
| Source rights and automation terms | `NEEDS VERIFICATION` | Live source activation remains blocked until source terms are verified. |

[Back to top](#top)

---

## Review checklist

<details>
<summary>Pre-acceptance checklist</summary>

- [ ] This ADR is listed in the ADR index.
- [ ] ADR-0001 status is checked.
- [ ] ADR-0002 status is checked.
- [ ] Active repo inventory has been run.
- [ ] Any existing Agriculture schema file is classified.
- [ ] Shared schemas are reused where possible.
- [ ] No active Agriculture machine schema remains in `contracts/` unless explicitly marked alias/generated/example/deprecated.
- [ ] Agriculture docs agree on one schema-home posture.
- [ ] Source-role guardrails are preserved.
- [ ] Public path safety is tested.
- [ ] Negative fixtures fail closed.
- [ ] Rollback and supersession path is documented.
- [ ] Owners and policy label are confirmed or visibly unresolved.
- [ ] No public release, source activation, or runtime enforcement is claimed without direct evidence.

</details>

---

## Maintainer note

This ADR’s goal is to make the Agriculture lane easier to build safely, not to make the tree look tidy.

A tidy tree that hides duplicate schema authority is worse than an untidy tree with explicit lineage, review state, and rollback. Choose the placement that keeps evidence, validation, policy, release, and correction inspectable.

[Back to top](#top)
