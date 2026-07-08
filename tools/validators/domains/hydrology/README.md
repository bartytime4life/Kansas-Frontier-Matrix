<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-hydrology-readme
title: tools/validators/domains/hydrology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-flood-boundary-reviewer-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; hydrology; huc; reach; gauge; nfhl; source-role-aware; not-flood-warning; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Hydrology validator index for Watershed, HUCUnit, HydroFeature, ReachIdentity, GaugeSite, GroundwaterWell, FlowObservation, WaterLevelObservation, WaterQualityObservation, AquiferObservation, Hydrograph, NFHLZone, UpstreamTrace, WaterUseLink, DroughtLink, IrrigationLink, source-role separation, HUC/COMID/reach identity, freshness/time posture, not-flood-warning boundaries, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Hydrology meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../atmosphere_hydrology/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/hydrology/ARCHITECTURE.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../../docs/domains/hydrology/INDEX.md
  - ../../../../docs/domains/hydrology/EXPANSION_BACKLOG.md
  - ../../../../docs/domains/hazards/README.md
  - ../../../../docs/domains/atmosphere/README.md
  - ../../../../data/proofs/hydrology/README.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/release/hydrology/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "No broad tools/validators/hydrology/README.md was found during this task, so this path currently serves as the inspected per-domain Hydrology validator index."
  - "Hydrology owns watersheds, HUC units, reaches, gauges, observations, hydrographs, regulatory flood context, and upstream traces. It does not own emergency alerts, life-safety warnings, soil truth, agriculture truth, geology truth, infrastructure truth, or hazards alert authority."
  - "NFHL and similar flood layers are regulatory context only; validators must deny treating them as observed inundation, forecast flood extent, or emergency instruction."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Hydrology meaning, create EvidenceBundles, issue flood warnings, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/hydrology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydrology--validators-informational)
![boundary](https://img.shields.io/badge/not--flood--warning-critical)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/hydrology/` is the proposed per-domain Hydrology validator index for watersheds, HUC units, reaches, gauges, water observations, aquifer observations, hydrographs, NFHL/regulatory flood context, upstream traces, water-use/drought/irrigation links, source-role separation, HUC/COMID/reach identity, freshness/time posture, not-flood-warning boundaries, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/hydrology/` exists to organize Hydrology validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Hydrology candidates preserve watershed/reach/site identity, source-role posture, observed-vs-regulatory-vs-modeled separation, HUC/COMID/reach lineage, time/freshness posture, not-flood-warning boundaries, neighboring-domain ownership, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create Hydrology truth, official flood-warning authority, emergency instructions, regulatory determinations, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/hydrology/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/hydrology/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected Hydrology validator index. |
| Hydrology domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/hydrology/README.md` defines Hydrology as evidence-bound, time-aware water systems and names its not-flood-warning, NFHL, source-role, and lifecycle boundaries. |
| Hydrology proof lane | **CONFIRMED in repo evidence / draft** | `data/proofs/hydrology/README.md` defines proof support for hydrology evidence closure and requires source-role separation for observed water conditions, watershed units, regulatory flood context, terrain-derived context, models, and public map artifacts. |
| Existing related validator lanes | **CONFIRMED README siblings / executable proposed** | `atmosphere_hydrology/` and cross-domain lanes exist where scope overlaps; executable behavior remains unverified. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child Hydrology validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Hydrology validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `huc-reach-identity/` for WBD/HUC, NHD/NHDPlus, COMID, reach identity, and topology checks;
- `gauge-observation/` for gauge/site identity, flow/water-level/water-quality observations, units, timestamps, and source-role posture;
- `groundwater-aquifer/` for groundwater wells, aquifer observations, well/privacy boundaries, and public-safe geometry;
- `nfhl-flood-context/` for NFHL/FEMA/regulatory flood context without observed-inundation, forecast, or emergency-warning collapse;
- `hydrograph-model/` for modeled hydrographs, model-run receipts, uncertainty, and model-as-observation denial;
- `upstream-trace/` for upstream/downstream trace topology and evidence support;
- `water-use-drought-irrigation/` for Agriculture/Hazards/Atmosphere joins without absorbing neighboring-domain truth.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Hydrology validator index | `tools/validators/domains/hydrology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Hydrology validator context | `tools/validators/atmosphere_hydrology/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Hydrology domain meaning | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` or ADR-selected homes |
| Hydrology policy rules | `policy/domains/hydrology/`, `policy/release/hydrology/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/hydrology/` or accepted source registry home |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/hydrology/`, `tests/domains/hydrology/`, `fixtures/domains/hydrology/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared Hydrology invariants and delegates meaning, source roles, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as Hydrology doctrine, emergency-warning authority, flood-warning authority, regulatory-determination authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/hydrology/` include:

- this parent/index README;
- child README lanes for narrow Hydrology validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check WBD/HUC, NHD/NHDPlus, COMID, reach, gauge, well, observation, hydrograph, NFHL, upstream-trace, drought, water-use, and irrigation-link posture;
- validators that check source-role discipline, official-source attribution, time/freshness windows, validity, units, identity crosswalks, public-safe geometry, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Hazards, Atmosphere, Geology, Soil, Agriculture, Infrastructure, Roads/Rail/Trade, Habitat, People/Land, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Hydrology doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/hydrology/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Hydrology domain docs | `docs/domains/hydrology/` |
| Hydrology contracts | `contracts/domains/hydrology/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and release-gate rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, flood warning, emergency instruction, regulatory determination, engineering decision, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Hydrology validator posture

Hydrology validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, official-source attribution, identity lineage, units, timestamps, rights, or object-family support;
- collapses Watershed, HUCUnit, HydroFeature, ReachIdentity, GaugeSite, GroundwaterWell, FlowObservation, WaterLevelObservation, WaterQualityObservation, AquiferObservation, Hydrograph, NFHLZone, UpstreamTrace, WaterUseLink, DroughtLink, or IrrigationLink into another role;
- treats NFHL, FEMA, or other regulatory flood context as observed inundation, forecast flood extent, hydraulic model output, or emergency instruction;
- treats modeled hydrographs or reconstructed flows as observed readings without model-run receipts and modeled posture;
- displays stale, superseded, or expired flood/drought/warning/advisory/operational hydrologic context as current;
- presents KFM as a flood-warning, evacuation, dam-safety, navigation, engineering, or regulatory-decision authority;
- joins hydrology records to infrastructure, private property, people/land, agriculture, geology, soil, hazards, habitat, or other sensitive context without preserving the most restrictive policy and ownership posture;
- lacks a required ReviewRecord, PolicyDecision, ValidationReport, ModelRunReceipt, ReleaseManifest, correction path, or rollback target;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Hydrology content beyond the approved public-safe derivative;
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
| `HYDROLOGY_DOMAIN_VALIDATORS_PASS` | Configured Hydrology validators passed. |
| `HYDROLOGY_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Hydrology child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `HYDRO_IDENTITY_UNRESOLVED` | HUC, COMID, reach, gauge, well, or crosswalk identity is missing or unresolved. |
| `NFHL_AS_OBSERVED_FLOOD_DENIED` | Regulatory flood context is presented as observed inundation, forecast, or warning. |
| `MODEL_AS_OBSERVATION_DENIED` | Modeled or reconstructed hydrologic output is presented as observed fact. |
| `FLOOD_WARNING_AUTHORITY_DENIED` | Candidate presents KFM as flood-warning or life-safety authority. |
| `FRESHNESS_WINDOW_EXPIRED` | Observation, model, advisory, warning, or context is stale for the claimed use. |
| `SENSITIVE_JOIN_DENIED` | Hydrology join reveals or infers restricted neighboring-domain context. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Hydrology without preserving boundaries. |
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
tests/validators/domains/hydrology/
├── README.md
├── test_hydrology_domain_validator_parent.py
└── fixtures/
    ├── valid_huc_reach_gauge_bundle/
    ├── missing_evidence_ref/
    ├── unresolved_hydro_identity/
    ├── source_role_collapse/
    ├── nfhl_as_observed_flood_denied/
    ├── model_as_observation_denied/
    ├── flood_warning_authority_denied/
    ├── stale_context_denied/
    ├── sensitive_join_denied/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/hydrology
```

```bash
python tools/validators/domains/hydrology/run_hydrology_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_hydrology_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared Hydrology contracts, schemas, and policy rather than defining meaning locally.
- [ ] Watersheds, HUCs, reaches, gauges, wells, observations, hydrographs, NFHL zones, traces, and cross-domain links remain distinct.
- [ ] Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain distinct.
- [ ] NFHL and regulatory flood context are not treated as observed inundation, forecast, or warning.
- [ ] KFM is never presented as flood-warning, emergency, evacuation, dam-safety, navigation, engineering, or regulatory authority.
- [ ] Freshness windows, stale-state, supersession, correction, and rollback support are checked where required.
- [ ] Cross-domain joins preserve ownership, source role, sensitivity, and EvidenceBundle support.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces do not reveal restricted details or reverse-engineerable derivatives.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, emergency warning, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub and current parent index for Hydrology validators. |
| Next smallest safe change | Verify child validator scripts, accepted profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, identity-crosswalk behavior, freshness/expiry behavior, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
