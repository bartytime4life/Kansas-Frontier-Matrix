<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-hazards-readme
title: tools/validators/hazards README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-steward-plus-release-steward-plus-policy-steward-plus-evidence-steward-plus-ui-boundary-reviewer-plus-source-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; hazards-validator-routing-index; not-for-life-safety; alert-authority-deny; freshness-aware; official-source-attribution; release-gated; non-authoritative
owning_root: tools/
responsibility: broad Hazards validator routing index for Hazards-specific validator lanes under tools/validators/hazards, including warning/advisory context, freshness and expiry, official-source attribution, not-for-life-safety boundaries, public-surface disclaimers, cross-domain hazard joins, evidence/proof linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring per-domain Hazards validator authority, Hazards meaning, policy decisions, evidence records, receipts, proofs, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/hazards/README.md
  - ../air-hazards/README.md
  - ../atmosphere_hazards/README.md
  - ../atmosphere_hydrology/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/BLUEPRINT.md
  - ../../../docs/domains/hazards/CANONICAL_PATHS.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/RELEASE_INDEX.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../contracts/domains/hazards/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hazards/
  - ../../../data/registry/sources/hazards/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/hazards/README.md. It does not confirm executable validator code."
  - "tools/validators/domains/hazards/ remains the per-domain Hazards validator index. This README is a broad routing index for Hazards-specific validator lanes that intentionally sit outside the per-domain tree."
  - "KFM Hazards is not an emergency alert system, life-safety instruction surface, official warning authority, evacuation instruction surface, or regulatory determination authority."
  - "Warning, advisory, watch, declaration, forecast, model, and operational-context products may be represented only as evidence-bound context with visible source role, validity, expiry, disclaimer, official-source redirect, release state, correction path, and rollback support."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, freshness, and policy. They do not define Hazards meaning, create EvidenceBundles, issue alerts, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/hazards

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hazards--validator--routing-informational)
![boundary](https://img.shields.io/badge/not--for--life--safety-critical)
![authority](https://img.shields.io/badge/authority-routing--index-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/hazards/` is the broad Hazards validator routing index for Hazards-specific validator lanes that sit outside the per-domain tree, while the main per-domain Hazards validator index remains `tools/validators/domains/hazards/`.

---

## Purpose

`tools/validators/hazards/` exists to route Hazards validation concerns under the durable `tools/validators/` surface without moving Hazards doctrine, contracts, schemas, policy, evidence, receipts, release decisions, or lifecycle data into a validator folder.

The durable KFM question for this index is:

> Do Hazards validator lanes preserve object-family identity, source-role posture, official-source attribution, freshness and expiry, not-for-life-safety boundaries, release posture, correction lineage, rollback target, and public-surface denial before Hazards candidates reach catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a navigable validator routing index and deterministic validation outputs from configured child lanes. This folder should not create Hazards truth, official warning authority, emergency instructions, regulatory determinations, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/hazards/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| Per-domain Hazards validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/hazards/README.md` remains the per-domain Hazards validator index. |
| Cross-domain air/hazards validator lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/air-hazards/README.md` exists for air/hazard overlap. |
| Cross-domain atmosphere/hazards validator lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/atmosphere_hazards/README.md` exists for atmosphere/hazard overlap. |
| Hazards domain doctrine | **CONFIRMED repo evidence / draft** | Hazards docs define the domain as evidence-bound context, not a life-safety alerting authority. |
| Executables, schemas, fixtures, policy bundles, receipts, report paths, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, registry entry, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Index relationship

KFM currently has multiple Hazards-related validator surfaces with different responsibilities:

| Path | Role | Boundary |
|---|---|---|
| `tools/validators/domains/hazards/` | Per-domain Hazards validator index. | Primary home for domain-scoped Hazards validator routing under the per-domain validator tree. |
| `tools/validators/hazards/` | Broad Hazards validator routing index. | Convenience parent for Hazards-specific child lanes that sit outside the per-domain tree. |
| `tools/validators/air-hazards/` | Air/Hazards overlap lane. | Air-quality, smoke, hazard-context, and public-surface overlap checks. |
| `tools/validators/atmosphere_hazards/` | Atmosphere/Hazards overlap lane. | Weather, smoke, atmospheric model, stale-state, and hazard-context overlap checks. |
| `tools/validators/cross-domain-joins/` | Shared cross-domain join checks. | Keeps joins from collapsing ownership, source role, sensitivity, or policy. |
| `tools/validators/cross-lane/` | Shared cross-lane invariant checks. | General cross-lane routing and invariant support. |

Do not duplicate authority between these paths. If a validator is domain-scoped and fits the per-domain tree, prefer `tools/validators/domains/hazards/`. If a validator is a broad reusable Hazards helper or adapter that intentionally sits outside the domain tree, document the reason here and link back to the per-domain index.

[Back to top](#top)

---

## Child lanes

No child README lanes under `tools/validators/hazards/` are confirmed by this edit.

Possible future child lanes remain **PROPOSED** until created and verified:

- `warning-context/` for warnings, watches, advisories, expiry, not-for-life-safety posture, official-source redirects, and stale-state denial;
- `flood-context/` for NFHL, FEMA, floodplain, observed-inundation, forecast, and Hydrology ownership-boundary checks;
- `wildfire-smoke/` for wildfire detection, perimeter caveats, thermal detections, smoke context, and Atmosphere ownership boundaries;
- `drought-indicator/` for drought time series, cadence, aggregate/model posture, stale state, and supersession checks;
- `earthquake-heat-cold/` for event identity, magnitude/type, uncertainty, advisory context, and public-surface boundaries;
- `exposure-summary/` for aggregate exposure/resilience rollups without critical-infrastructure, private-detail, or emergency-instruction leakage;
- `freshness-expiry/` for current-sensitive hazard context, stale warnings, supersession, correction, and rollback checks;
- `release-readiness/` for release-reference, disclaimer, official-source redirect, correction, rollback, and public-surface readiness checks.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad Hazards validator routing index | `tools/validators/hazards/` |
| Per-domain Hazards validator index | `tools/validators/domains/hazards/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Hazards and Atmosphere/Air validator context | `tools/validators/air-hazards/`, `tools/validators/atmosphere_hazards/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Hazards domain meaning | `docs/domains/hazards/`, `contracts/domains/hazards/` |
| Publication and not-for-life-safety doctrine | `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`, `docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md` |
| Hazards schemas | `schemas/contracts/v1/domains/hazards/` or ADR-selected homes |
| Hazards policy rules | `policy/domains/hazards/`, `policy/release/hazards/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/hazards/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections, withdrawal | `release/` |
| Lifecycle data | `data/raw/hazards/`, `data/work/hazards/`, `data/quarantine/hazards/`, `data/processed/hazards/`, `data/catalog/...`, `data/published/...` |
| Tests and fixtures | `tests/validators/hazards/`, `tests/validators/domains/hazards/`, `tests/domains/hazards/`, `fixtures/domains/hazards/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared broad Hazards validation invariants and writes reports or receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, child lane inventory, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as Hazards doctrine, emergency-alert authority, life-safety surface, regulatory-determination authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/hazards/` include:

- this broad Hazards validator routing README;
- child lanes that intentionally sit outside `tools/validators/domains/hazards/` and have a clear reason to do so;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check official-source attribution, validity windows, expiry, supersession, freshness, warning-context boundaries, not-for-life-safety disclaimers, public-surface redirects, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Hydrology, Atmosphere/Air, Settlements/Infrastructure, Roads/Rail/Trade, Geology, Habitat, Agriculture, People/Land, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Hazards doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/hazards/` | Correct home |
|---|---|
| Hazards domain docs | `docs/domains/hazards/` |
| Hazards contracts | `contracts/domains/hazards/` |
| Schemas and enums | `schemas/contracts/v1/...` |
| Policy and release-gate rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, emergency alert, life-safety instruction, legal/regulatory determination, or AI runtime code | governed application/runtime roots |
| Current emergency instructions, evacuation advice, sheltering advice, route safety advice, or official warning replacement text | official public agencies and source systems, not KFM validator docs |

[Back to top](#top)

---

## Broad Hazards validator posture

Hazards validators under this broad index must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source role, official-source attribution, validity/expiry, rights, or object-family support;
- collapses HazardEvent, HazardObservation, WarningContext, AdvisoryContext, DisasterDeclaration, FloodContext, WildfireDetection, SmokeContext, DroughtIndicator, EarthquakeEvent, HeatColdEvent, ExposureSummary, ResilienceSummary, HazardTimeline, or ImpactArea into another role;
- presents KFM as an emergency alert system, current warning authority, life-safety instruction surface, evacuation surface, route-safety authority, or regulatory determination authority;
- displays an expired, superseded, or stale warning, advisory, watch, declaration, model output, or operational context as current;
- treats NFHL/FEMA regulatory context as observed flood extent, forecast, insurance advice, or legal determination;
- treats FIRMS, thermal detection, satellite detection, or perimeter context as legal fire status, ground-truth perimeter, official evacuation condition, or emergency instruction;
- treats smoke, aerosol, atmospheric model, or remote-sensing context as health advice, AQI/PM2.5 ground truth, emergency guidance, or exposure certainty without owning-domain support and release posture;
- joins hazards records to critical infrastructure, private property, people/land, roads, rail, facilities, agriculture, habitat, archaeology, or other sensitive context without preserving the most restrictive policy and ownership posture;
- lacks a not-for-life-safety disclaimer, official-source redirect, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, screenshots, or answers with Hazards content beyond the approved public-safe derivative;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `HAZARDS_VALIDATORS_PASS` | Configured Hazards validators passed. |
| `HAZARDS_VALIDATORS_FAIL` | One or more configured Hazards validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Hazards child validator lane, registry entry, or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `ROUTE_TO_DOMAIN_HAZARDS_VALIDATOR` | Candidate should be checked by `tools/validators/domains/hazards/`. |
| `ROUTE_TO_AIR_HAZARDS_VALIDATOR` | Candidate should be checked by `tools/validators/air-hazards/`. |
| `ROUTE_TO_ATMOSPHERE_HAZARDS_VALIDATOR` | Candidate should be checked by `tools/validators/atmosphere_hazards/`. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `OFFICIAL_SOURCE_ATTRIBUTION_MISSING` | Official or source-system attribution is absent where required. |
| `FRESHNESS_OR_EXPIRY_MISSING` | Candidate lacks valid time, observed time, source time, retrieval time, release time, correction time, expiry, or stale-state posture where material. |
| `STALE_WARNING_DENIED` | Expired or superseded warning/advisory/watch context is presented as current. |
| `ALERT_AUTHORITY_DENIED` | Candidate presents KFM as an alerting, evacuation, life-safety, or emergency-instruction authority. |
| `REGULATORY_DETERMINATION_DENIED` | Candidate presents KFM as legal/regulatory hazard determination authority. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Map, tile, popup, export, search, graph, embedding, Focus Mode, screenshot, or AI surface exposes unsupported, stale, or unsafe hazard context. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/hazards/
├── README.md
├── validate_hazards.py                  # PROPOSED; not confirmed
├── freshness-expiry/                    # PROPOSED child lane
│   └── README.md
└── warning-context/                     # PROPOSED child lane
    └── README.md
```

The executable, if added, should delegate to child validators and shared validator homes rather than copy policy rules locally. The repo-wide validator orchestrator should remain the entry point if registry wiring is adopted.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at the requested path.
- [x] It states the relationship between `tools/validators/hazards/` and `tools/validators/domains/hazards/`.
- [x] It marks the parent as a routing index, not domain authority, policy authority, evidence authority, or release authority.
- [x] It preserves cite-or-abstain, not-for-life-safety, official-source attribution, freshness/expiry, evidence, policy, release, correction, and rollback boundaries.
- [x] It marks executable behavior, CI wiring, policy bundle paths, schema bindings, fixtures, receipt emission, and runtime behavior as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry wiring is verified.
- [ ] Exact executable names and interfaces are accepted.
- [ ] Valid and invalid fixtures cover missing evidence, stale warnings, missing official-source attribution, alert-authority overclaim, regulatory-determination overclaim, cross-domain policy propagation, release gaps, and public-surface leakage.
- [ ] CI or `tools/validate_all.py` invokes the relevant Hazards validators in deterministic order.
- [ ] Validation outputs write reports or receipts only to accepted roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with broad Hazards validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
