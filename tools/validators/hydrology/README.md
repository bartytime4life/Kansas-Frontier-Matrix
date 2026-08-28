<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-hydrology-readme
title: tools/validators/hydrology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-flood-boundary-reviewer-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward-plus-ui-boundary-reviewer
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; hydrology-validator-routing-index; hydrology; huc; reach; gauge; nfhl; source-role-aware; not-flood-warning; release-gated; non-authoritative
owning_root: tools/
responsibility: broad full-name Hydrology validator routing index under tools/validators/hydrology; routes Hydrology validator entry points, shorthand hydro compatibility, cross-domain hydrology-hazards checks, flood-context checks, atmosphere-hydrology checks, schemas, policy, fixtures, evidence, receipts, lifecycle data, tests, and release decisions to their owning roots while preserving the per-domain Hydrology validator index at tools/validators/domains/hydrology
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/hydrology/README.md
  - ../hydro/README.md
  - ../hydro/fixtures/README.md
  - ../hydro/policy/README.md
  - ../hydro/schemas/README.md
  - ../hydrology-hazards/README.md
  - ../flood-context/README.md
  - ../atmosphere_hydrology/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../hazards/README.md
  - ../domains/hazards/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/ARCHITECTURE.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../docs/domains/hydrology/INDEX.md
  - ../../../docs/domains/hydrology/source-role-matrix.md
  - ../../../docs/domains/hydrology/RELEASE_INDEX.md
  - ../../../docs/runbooks/hydrology/PROMOTION_RUNBOOK.md
  - ../../../contracts/domains/hydrology/
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../schemas/contracts/v1/joins/hydrology_hazards/README.md
  - ../../../schemas/contracts/v1/joins/hydrology_soil/README.md
  - ../../../schemas/contracts/v1/joins/hydrology_agriculture/README.md
  - ../../../schemas/contracts/v1/joins/hydrology_settlements/README.md
  - ../../../schemas/contracts/v1/cross/atmosphere_hydrology/README.md
  - ../../../policy/domains/hydrology/
  - ../../../policy/release/hydrology/
  - ../../../data/registry/sources/hydrology/
  - ../../../data/proofs/hydrology/README.md
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/hydrology/README.md. It does not confirm executable validator code."
  - "tools/validators/domains/hydrology/ remains the richer per-domain Hydrology validator index. This full-name parent is a broad routing/index lane under tools/validators/."
  - "tools/validators/hydro/ is a shorthand/routing lane and should not become a competing Hydrology authority."
  - "Hydrology owns watersheds, HUC units, reaches, gauges, wells, observations, hydrographs, regulatory flood context, and upstream traces. It does not own emergency alerts, life-safety warnings, Hazards alert authority, soil truth, agriculture truth, geology truth, infrastructure truth, or release authority."
  - "NFHL and similar flood layers are regulatory context only; validators must deny treating them as observed inundation, forecast flood extent, flood-warning authority, emergency instruction, insurance advice, engineering decision, or legal/regulatory determination."
  - "Validators enforce declared contracts, schemas, policy references, evidence posture, and release readiness. They do not define Hydrology meaning, create EvidenceBundles, issue flood warnings, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/hydrology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydrology--validator--routing-informational)
![boundary](https://img.shields.io/badge/not--flood--warning-critical)
![authority](https://img.shields.io/badge/authority-routing--index-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/hydrology/` is the broad full-name Hydrology validator routing index. The richer per-domain Hydrology validator index remains `tools/validators/domains/hydrology/`; the shorthand compatibility lane remains `tools/validators/hydro/`.

---

## Purpose

`tools/validators/hydrology/` exists to give maintainers a full-name Hydrology validator entry point under the durable `tools/validators/` surface without turning this folder into Hydrology doctrine, schema authority, policy authority, evidence storage, fixture storage, release authority, lifecycle data, or public-output code.

The durable KFM question for this routing index is:

> Do Hydrology validator lanes preserve watershed/reach/site identity, source-role posture, observed-vs-regulatory-vs-modeled separation, HUC/COMID/reach lineage, units, time/freshness posture, not-flood-warning boundaries, neighboring-domain ownership, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial before Hydrology candidates reach catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation route and report. This folder should not create Hydrology truth, official flood-warning authority, emergency instructions, engineering decisions, regulatory determinations, EvidenceBundles, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/hydrology/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| `tools/validators/domains/hydrology/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Richer per-domain Hydrology validator index and current primary Hydrology validator boundary. |
| `tools/validators/hydro/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Shorthand/routing lane; should not become competing Hydrology authority. |
| `tools/validators/hydrology-hazards/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Cross-domain Hydrology × Hazards validator lane. |
| `tools/validators/flood-context/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Shared flood-context lane for NFHL/FEMA/regulatory context and anti-collapse checks. |
| `tools/validators/atmosphere_hydrology/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Cross-domain Atmosphere/Hydrology lane. |
| Executables, registry wiring, report destinations, fixtures, schema bindings, policy bundle digests, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a runnable validator, test suite, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Path | Role | Boundary |
|---|---|---|
| `tools/validators/hydrology/` | Full-name Hydrology validator routing parent. | Broad navigational index; not Hydrology doctrine or release authority. |
| `tools/validators/domains/hydrology/` | Per-domain Hydrology validator index. | Richer Hydrology validator boundary for object families, identities, source roles, time posture, evidence, policy, release, correction, rollback, and public-surface denial. |
| `tools/validators/hydro/` | Shorthand/routing Hydrology lane. | Compatibility or convenience entry point; routes schemas, policy, fixtures, proofs, receipts, data, and release elsewhere. |
| `tools/validators/hydrology-hazards/` | Hydrology × Hazards validator lane. | Cross-domain join and boundary checks, while flood-context specifics route to `flood-context/`. |
| `tools/validators/flood-context/` | Shared flood-context validator lane. | NFHL/FEMA/regulatory flood context, source-role preservation, anti-warning/anti-instruction checks. |
| `tools/validators/atmosphere_hydrology/` | Atmosphere/Hydrology overlap lane. | Precipitation, drought, runoff, weather, smoke/water interactions, freshness, and neighboring-domain boundaries. |
| `tools/validators/cross-domain-joins/` | Shared cross-domain join checks. | Prevents ownership, source-role, policy, sensitivity, evidence, and release collapse. |
| `tools/validators/cross-lane/` | Shared cross-lane invariant checks. | Keeps multi-lane validation behavior consistent. |

If new Hydrology validation work is domain-scoped, prefer `tools/validators/domains/hydrology/`. If a full-name entry point is useful for maintainers or registry routing, keep it here and route to the per-domain, shorthand, flood-context, or cross-domain lanes as appropriate.

[Back to top](#top)

---

## Child and adjacent lanes

No child directories under `tools/validators/hydrology/` are confirmed by this edit.

Use adjacent lanes instead of duplicating them:

| Concern | Preferred lane |
|---|---|
| Schema lookup/binding guidance | `tools/validators/hydro/schemas/` and canonical `schemas/` roots |
| Policy lookup/binding guidance | `tools/validators/hydro/policy/` and canonical `policy/` roots |
| Fixture guidance | `tools/validators/hydro/fixtures/` and accepted `fixtures/` roots |
| Hydrology-Hazards joins | `tools/validators/hydrology-hazards/` |
| NFHL/FEMA/flood regulatory context | `tools/validators/flood-context/` |
| Atmosphere-Hydrology joins | `tools/validators/atmosphere_hydrology/` |
| Generic cross-domain joins | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |

Possible future child lanes remain **PROPOSED** until created and verified:

- `huc-reach-identity/` for WBD/HUC, NHD/NHDPlus, COMID, reach identity, and topology checks;
- `gauge-observation/` for gauge/site identity, flow/water-level/water-quality observations, units, timestamps, and source-role posture;
- `groundwater-aquifer/` for groundwater wells, aquifer observations, well/privacy boundaries, and public-safe geometry;
- `nfhl-flood-context/` only if maintainers choose a Hydrology-specific child instead of the shared `flood-context/` lane;
- `hydrograph-model/` for modeled hydrographs, model-run receipts, uncertainty, and model-as-observation denial;
- `upstream-trace/` for upstream/downstream trace topology and evidence support;
- `water-use-drought-irrigation/` for Agriculture/Hazards/Atmosphere joins without absorbing neighboring-domain truth;
- `release-readiness/` for release-reference, public-surface, correction, rollback, and withdrawal readiness checks.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Full-name Hydrology validator routing index | `tools/validators/hydrology/` |
| Per-domain Hydrology validator index | `tools/validators/domains/hydrology/` |
| Shorthand Hydrology validator routing lane | `tools/validators/hydro/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Hydrology validator context | `tools/validators/atmosphere_hydrology/` |
| Hydrology/Hazards validator context | `tools/validators/hydrology-hazards/` |
| Flood-context validator lane | `tools/validators/flood-context/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Hydrology domain meaning | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` or accepted schema homes |
| Hydrology join/cross schemas | `schemas/contracts/v1/joins/`, `schemas/contracts/v1/cross/`, or accepted schema homes |
| Hydrology policy rules | `policy/domains/hydrology/`, `policy/release/hydrology/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/hydrology/` or accepted source registry home |
| Canonical reusable fixtures | `fixtures/domains/hydrology/`, `fixtures/validators/hydrology/`, or accepted fixture home |
| Tests | `tests/validators/hydrology/`, `tests/validators/domains/hydrology/`, `tests/domains/hydrology/`, or accepted test home |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections, withdrawal | `release/` |
| Lifecycle data | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, `data/catalog/...`, `data/published/...` |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here only as a routing adapter or runner that delegates meaning, schema, policy, evidence, fixtures, receipts, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, accepted validator registry entries, schema ids, policy bundle digests, fixture homes, test paths, report destinations, receipt emission, runtime behavior, and CI wiring.
- **DENY:** using this folder as Hydrology doctrine, schema authority, policy authority, source registry, evidence store, lifecycle data store, proof store, receipt store, release record store, flood-warning authority, emergency-instruction surface, regulatory-determination authority, public map product surface, or AI answer authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/hydrology/` include:

- this full-name routing README;
- lightweight validator entry points that delegate to `tools/validators/domains/hydrology/` or shared validator utilities;
- routing notes that point Hydrology work to `hydro/`, `hydrology-hazards/`, `flood-context/`, `atmosphere_hydrology/`, `cross-domain-joins/`, or `cross-lane/`;
- deterministic checks for source-role separation, object-family identity, HUC/reach/gauge identity, time/freshness posture, not-flood-warning posture, evidence references, policy references, release references, correction paths, rollback targets, and public-surface denial;
- compatibility notes for full-name `hydrology` naming;
- generated validation report guidance only when report destinations are accepted and verified.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/hydrology/` | Correct home |
|---|---|
| Hydrology doctrine or contracts | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Hydrology schemas, enums, DTOs, or machine shape | `schemas/contracts/v1/domains/hydrology/` or accepted schema homes |
| Hydrology policy rules, thresholds, release gates, or steward decisions | `policy/domains/hydrology/`, `policy/release/hydrology/`, accepted policy homes |
| Source descriptors | `data/registry/sources/hydrology/` |
| Real source extracts, lifecycle data, or public data products | governed `data/` lifecycle roots |
| EvidenceBundles, proof packs, receipts, validation reports, ModelRunReceipts | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, rollback cards, correction notices, withdrawal notices | `release/` |
| Canonical fixtures | accepted root `fixtures/` homes |
| Tests | `tests/validators/...`, `tests/domains/...` |
| Public API, UI, map, tile, search, graph, Focus Mode, export, screenshot, embedding, or AI runtime output | governed application/runtime roots |
| Flood warnings, evacuation advice, dam-safety instructions, navigation safety advice, engineering decisions, insurance advice, or regulatory determinations | official agencies and governed source systems, not KFM validator docs |

[Back to top](#top)

---

## Hydrology validator posture

Hydrology validators routed through this full-name lane must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source role, official-source attribution, identity lineage, units, timestamps, rights, schema binding, policy binding, release reference, correction path, or rollback target required for its use;
- collapses Watershed, HUCUnit, HydroFeature, ReachIdentity, GaugeSite, GroundwaterWell, FlowObservation, WaterLevelObservation, WaterQualityObservation, AquiferObservation, Hydrograph, NFHLZone, UpstreamTrace, WaterUseLink, DroughtLink, or IrrigationLink into another role;
- treats NFHL, FEMA, or other regulatory flood context as observed inundation, forecast flood extent, hydraulic model output, insurance advice, emergency instruction, or legal/regulatory determination;
- treats modeled hydrographs, reconstructed flows, downscaled products, or derived surfaces as observed readings without model-run receipts and modeled posture;
- displays stale, superseded, or expired flood, drought, warning, advisory, model, or operational hydrologic context as current;
- presents KFM as a flood-warning, evacuation, dam-safety, navigation, engineering, insurance, legal, emergency, or regulatory-decision authority;
- joins hydrology records to infrastructure, private property, people/land, agriculture, geology, soil, hazards, habitat, archaeology, or other sensitive context without preserving the most restrictive policy and ownership posture;
- maps, tiles, exports, searches, embeds, graphs, summarizes, screenshots, or answers with Hydrology content beyond the approved public-safe derivative;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard routing outcomes

| Outcome | Meaning |
|---|---|
| `HYDROLOGY_ROUTE_READY` | Candidate can be routed to configured Hydrology validators. |
| `HYDROLOGY_VALIDATORS_PASS` | Configured Hydrology validators passed. |
| `HYDROLOGY_VALIDATORS_FAIL` | One or more configured Hydrology validators failed. |
| `ROUTE_TO_DOMAIN_HYDROLOGY_VALIDATOR` | Candidate should be checked by `tools/validators/domains/hydrology/`. |
| `ROUTE_TO_HYDRO_SHORTHAND_VALIDATOR` | Candidate should be checked by `tools/validators/hydro/` or its child guidance lanes. |
| `ROUTE_TO_FLOOD_CONTEXT_VALIDATOR` | Candidate should be checked by `tools/validators/flood-context/`. |
| `ROUTE_TO_HYDROLOGY_HAZARDS_VALIDATOR` | Candidate should be checked by `tools/validators/hydrology-hazards/`. |
| `ROUTE_TO_ATMOSPHERE_HYDROLOGY_VALIDATOR` | Candidate should be checked by `tools/validators/atmosphere_hydrology/`. |
| `SCHEMA_BINDING_MISSING` | Candidate lacks accepted Hydrology schema id, version, digest, or home. |
| `POLICY_BINDING_MISSING` | Candidate lacks accepted Hydrology policy or release-policy binding. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses observed/model/regulatory/aggregate/public-map source-role posture. |
| `OBJECT_FAMILY_COLLAPSE` | Candidate collapses Hydrology object family into another domain or role. |
| `NFHL_AS_OBSERVED_FLOOD_DENIED` | Regulatory flood context is presented as observed inundation or forecast. |
| `MODEL_AS_OBSERVATION_DENIED` | Modeled or derived hydrology is presented as measured observation. |
| `FLOOD_WARNING_AUTHORITY_DENIED` | Candidate presents KFM as flood-warning, evacuation, emergency-instruction, engineering, insurance, or regulatory authority. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Map, tile, popup, export, search, graph, embedding, Focus Mode, screenshot, or AI surface exposes unsupported or unsafe Hydrology context. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, rollback target, or withdrawal path is absent. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/hydrology/
├── README.md
├── validate_hydrology.py                # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If `validate_hydrology.py` is added, it should act as an adapter or runner that delegates to accepted Hydrology, schema, policy, fixture, evidence, and release validators. It should not redefine domain meaning, copy schemas, copy policy, store fixtures, write lifecycle data, approve release, or publish public outputs.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/hydrology/README.md`.
- [x] It marks `hydrology` as a full-name routing lane, not canonical Hydrology authority.
- [x] It points the richer Hydrology validator boundary to `tools/validators/domains/hydrology/`.
- [x] It distinguishes the shorthand `tools/validators/hydro/` lane from this full-name parent.
- [x] It routes machine shape, policy, fixtures, evidence, receipts, release, lifecycle data, tests, and domain meaning to their owning roots.
- [x] It preserves not-flood-warning, source-role, identity, freshness, evidence, policy, release, correction, rollback, and public-surface denial boundaries.
- [x] It marks executable behavior, registry wiring, schema bindings, policy bundles, fixture files, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to `hydrology` are searched and classified.
- [ ] Accepted schema homes, policy homes, fixture homes, test paths, and report destinations are verified.
- [ ] Tests exercise valid and invalid Hydrology fixture families.
- [ ] CI invokes the relevant Hydrology validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with full-name Hydrology validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
