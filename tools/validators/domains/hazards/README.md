<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-hazards-readme
title: tools/validators/domains/hazards README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-steward-plus-release-steward-plus-policy-steward-plus-evidence-steward-plus-ui-boundary-reviewer
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; hazards; not-for-life-safety; alert-authority-deny; freshness-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Hazards validator index for HazardEvent, HazardObservation, WarningContext, AdvisoryContext, DisasterDeclaration, FloodContext, WildfireDetection, SmokeContext, DroughtIndicator, EarthquakeEvent, HeatColdEvent, ExposureSummary, ResilienceSummary, HazardTimeline, ImpactArea, source-role separation, freshness/expiry, not-for-life-safety boundaries, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Hazards meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../air-hazards/README.md
  - ../../atmosphere_hazards/README.md
  - ../../atmosphere_hydrology/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../docs/domains/hazards/README.md
  - ../../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../../docs/domains/hazards/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/hazards/MISSING_OR_PLANNED_FILES.md
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../docs/domains/settlements-infrastructure/README.md
  - ../../../../docs/domains/roads-rail-trade/README.md
  - ../../../../contracts/domains/hazards/
  - ../../../../schemas/contracts/v1/domains/hazards/
  - ../../../../policy/domains/hazards/
  - ../../../../policy/release/hazards/
  - ../../../../data/registry/sources/hazards/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "No broad tools/validators/hazards/README.md was found during this task, so this path currently serves as the inspected per-domain Hazards validator index."
  - "KFM Hazards is not an emergency alert system, life-safety instruction surface, or regulatory determination authority. KFM-as-alert-authority is treated as T4 forever; no transform releases it."
  - "Warning, advisory, watch, and operational-context products may be represented only as evidence-bound context with visible source role, validity, expiry, disclaimer, official-source redirect, release state, correction path, and rollback support."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Hazards meaning, create EvidenceBundles, issue alerts, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/hazards

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hazards--validators-informational)
![boundary](https://img.shields.io/badge/not--for--life--safety-critical)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/hazards/` is the proposed per-domain Hazards validator index for hazard events, observations, warning/advisory context, declarations, flood/wildfire/smoke/drought/earthquake/heat/cold context, exposure/resilience summaries, timelines, impact areas, source-role separation, freshness/expiry, not-for-life-safety boundaries, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/hazards/` exists to organize Hazards validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Hazards candidates preserve object-family identity, source-role posture, operational-context freshness, official-source attribution, not-for-life-safety disclaimers, neighboring-domain ownership, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create Hazards truth, official warning authority, emergency instructions, regulatory determinations, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/hazards/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/hazards/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected Hazards validator index. |
| Hazards domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/hazards/README.md` defines Hazards as historical, regulatory, observational, modeled, and operational-context information, explicitly not a life-safety alerting system. |
| Publication and boundary doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` defines what may be published and what KFM must never become, including the T4-forever alert-authority boundary. |
| Existing related validator lanes | **CONFIRMED README siblings / executable proposed** | `air-hazards/`, `atmosphere_hazards/`, and other cross-domain lanes exist where scope overlaps; executable behavior remains unverified. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child Hazards validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Hazards validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `warning-context/` for warnings, watches, advisories, expiry, not-for-life-safety posture, and official-source redirects;
- `flood-context/` for NFHL/FEMA/regulatory flood context without observed-inundation or forecast collapse;
- `wildfire-smoke/` for wildfire detection, smoke context, thermal detections, perimeter caveats, and Atmosphere ownership boundaries;
- `drought-indicator/` for drought time series, cadence, modeled/aggregate posture, and stale-state checks;
- `earthquake-heat-cold/` for event identity, magnitude/type, uncertainty, and operational-advisory boundaries;
- `exposure-summary/` for aggregate exposure/resilience rollups without critical-infrastructure or private-detail leakage;
- `freshness-expiry/` for current-sensitive hazard context, stale warnings, supersession, correction, and rollback checks.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Hazards validator index | `tools/validators/domains/hazards/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Hazards and Atmosphere/Hazards validator context | `tools/validators/air-hazards/`, `tools/validators/atmosphere_hazards/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Hazards domain meaning | `docs/domains/hazards/`, `contracts/domains/hazards/` |
| Publication and not-for-life-safety doctrine | `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` |
| Hazards schemas | `schemas/contracts/v1/domains/hazards/` or ADR-selected homes |
| Hazards policy rules | `policy/domains/hazards/`, `policy/release/hazards/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/hazards/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/hazards/`, `tests/domains/hazards/`, `fixtures/domains/hazards/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared Hazards invariants and delegates meaning, source roles, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as Hazards doctrine, emergency-alert authority, life-safety surface, regulatory-determination authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/hazards/` include:

- this parent/index README;
- child README lanes for narrow Hazards validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check object-family separation, source-role discipline, official-source attribution, freshness windows, expiry, supersession, warning-context boundaries, public-surface disclaimers, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Hydrology, Atmosphere/Air, Settlements/Infrastructure, Roads/Rail/Trade, Geology, Habitat, Agriculture, People/Land, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Hazards doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/hazards/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Hazards domain docs | `docs/domains/hazards/` |
| Hazards contracts | `contracts/domains/hazards/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and release-gate rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, emergency alert, life-safety instruction, legal/regulatory determination, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Hazards validator posture

Hazards validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, official-source attribution, validity/expiry, rights, or object-family support;
- collapses HazardEvent, HazardObservation, WarningContext, AdvisoryContext, DisasterDeclaration, FloodContext, WildfireDetection, SmokeContext, DroughtIndicator, EarthquakeEvent, HeatColdEvent, ExposureSummary, ResilienceSummary, HazardTimeline, or ImpactArea into another role;
- presents KFM as an emergency alert system, current warning authority, life-safety instruction surface, or regulatory determination authority;
- displays an expired, superseded, or stale warning/advisory/watch as current;
- treats NFHL/FEMA regulatory context as observed flood extent or forecast;
- treats FIRMS or thermal detection as legal fire status, ground-truth perimeter, or emergency instruction;
- treats smoke/AOD/model context as PM2.5, AQI, exposure, impact, or emergency guidance without owning-domain support and release posture;
- joins hazards records to critical infrastructure, private property, people/land, roads, rail, facilities, agriculture, habitat, archaeology, or other sensitive context without preserving the most restrictive policy and ownership posture;
- lacks a not-for-life-safety disclaimer, official-source redirect, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Hazards content beyond the approved public-safe derivative;
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
| `HAZARDS_DOMAIN_VALIDATORS_PASS` | Configured Hazards validators passed. |
| `HAZARDS_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Hazards child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `ALERT_AUTHORITY_DENIED` | Candidate presents KFM as alert authority or life-safety source. |
| `NOT_FOR_LIFE_SAFETY_POSTURE_MISSING` | Required disclaimer or official-source redirect is absent. |
| `FRESHNESS_WINDOW_EXPIRED` | Warning, advisory, watch, observation, model, report, or context is stale for the claimed use. |
| `REGULATORY_CONTEXT_COLLAPSE` | Regulatory context is presented as observed event, forecast, or instruction. |
| `SENSITIVE_JOIN_DENIED` | Hazards join reveals or infers restricted neighboring-domain context. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Hazards without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/hazards/
├── README.md
├── test_hazards_domain_validator_parent.py
└── fixtures/
    ├── valid_historical_hazard_event/
    ├── missing_evidence_ref/
    ├── source_role_collapse/
    ├── alert_authority_denied/
    ├── expired_warning_denied/
    ├── regulatory_context_collapse/
    ├── stale_model_context_denied/
    ├── sensitive_join_denied/
    ├── release_reference_missing/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/hazards
```

```bash
python tools/validators/domains/hazards/run_hazards_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_hazards_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared Hazards contracts, schemas, and policy rather than defining meaning locally.
- [ ] KFM is never presented as alert authority, emergency-warning issuer, life-safety source, or regulatory decision-maker.
- [ ] Historical, regulatory, observational, modeled, operational-context, exposure, resilience, and impact object families remain distinct.
- [ ] Warning/advisory/watch context carries source, validity, expiry, not-for-life-safety posture, and official-source redirect.
- [ ] Freshness windows, stale-state, supersession, correction, and rollback support are checked where required.
- [ ] Cross-domain joins preserve ownership, source role, sensitivity, and EvidenceBundle support.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces do not reveal restricted details or reverse-engineerable derivatives.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, emergency alerting, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub and current parent index for Hazards validators. |
| Next smallest safe change | Verify child validator scripts, accepted profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, freshness/expiry behavior, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
