<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-hydrology-hazards-readme
title: tools/validators/hydrology-hazards README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-hazards-steward-plus-flood-boundary-reviewer-plus-policy-steward-plus-evidence-steward-plus-release-steward-plus-ui-boundary-reviewer
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; hydrology-hazards-validator; cross-domain-validator; flood-context; source-role-aware; not-flood-warning; not-life-safety; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed cross-domain Hydrology-Hazards validator lane for checking Hydrology and Hazards joins, flood context, NFHL/regulatory flood posture, observed-vs-regulatory-vs-modeled-vs-warning separation, source-role boundaries, freshness/expiry, official-source attribution, evidence/proof linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring Hydrology meaning, Hazards meaning, schemas, policy decisions, evidence records, proofs, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../hydro/README.md
  - ../hydro/fixtures/README.md
  - ../hydro/policy/README.md
  - ../hydro/schemas/README.md
  - ../hazards/README.md
  - ../flood-context/README.md
  - ../domains/hydrology/README.md
  - ../domains/hazards/README.md
  - ../atmosphere_hydrology/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/ARCHITECTURE.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/source-role-matrix.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../contracts/domains/hydrology/
  - ../../../contracts/domains/hazards/
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../schemas/contracts/v1/joins/hydrology_hazards/README.md
  - ../../../policy/domains/hydrology/
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hydrology/
  - ../../../policy/release/hazards/
  - ../../../data/registry/sources/hydrology/
  - ../../../data/registry/sources/hazards/
  - ../../../data/proofs/hydrology/README.md
  - ../../../data/proofs/hazards/README.md
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/hydrology-hazards/README.md. It does not confirm executable validator code."
  - "Hydrology-specific validation remains routed through tools/validators/domains/hydrology/ and the shorthand hydro lane. Hazards-specific validation remains routed through tools/validators/domains/hazards/ and tools/validators/hazards/."
  - "Flood-context specifics route to tools/validators/flood-context/. This lane is broader: it covers Hydrology-Hazards joins and boundary preservation."
  - "KFM must not become a flood-warning, emergency-alert, evacuation, engineering, insurance, legal, regulatory, or life-safety instruction authority."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, freshness, policy references, and release readiness. They do not define Hydrology meaning, Hazards meaning, create EvidenceBundles, issue warnings, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/hydrology-hazards

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydrology--hazards--validator-informational)
![boundary](https://img.shields.io/badge/not--flood--warning-critical)
![life-safety](https://img.shields.io/badge/not--life--safety-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/hydrology-hazards/` is the proposed cross-domain validator lane for Hydrology × Hazards joins and boundary checks, while flood-context-specific checks route to `tools/validators/flood-context/`.

---

## Purpose

`tools/validators/hydrology-hazards/` exists for cross-domain validation where Hydrology records, models, or regulatory context interact with Hazards events, warnings, advisories, declarations, exposure summaries, or public hazard surfaces.

The durable KFM question for this lane is:

> Does a Hydrology × Hazards candidate preserve watershed/reach/site identity, hazard object-family identity, source-role posture, observed-vs-regulatory-vs-modeled-vs-warning separation, time/freshness/expiry posture, official-source attribution, not-flood-warning and not-life-safety boundaries, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Hydrology truth, Hazards truth, official warning authority, emergency instructions, engineering decisions, insurance determinations, legal/regulatory determinations, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/hydrology-hazards/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| Hydrology validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/hydrology/README.md` names NFHL/regulatory flood context, not-flood-warning boundaries, source-role separation, freshness/time posture, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Hazards validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/hazards/README.md` names warning/advisory context, freshness/expiry, not-for-life-safety boundaries, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Shared flood-context lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/flood-context/README.md` owns NFHL/FEMA/regulatory-flood-context specifics and anti-collapse checks. |
| Hydrology-Hazards join schema home | **CONFIRMED search result / content NEEDS VERIFICATION** | `schemas/contracts/v1/joins/hydrology_hazards/README.md` appears in repository search; field-level schema contents were not inspected in this edit. |
| Executables, fixtures, schema bindings, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, fixture set, schema maturity, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Broad Hydrology-Hazards cross-domain validation | `tools/validators/hydrology-hazards/` |
| Flood-context and NFHL/FEMA regulatory posture | `tools/validators/flood-context/` |
| Hydrology per-domain validation | `tools/validators/domains/hydrology/`, `tools/validators/hydro/` |
| Hazards per-domain validation | `tools/validators/domains/hazards/`, `tools/validators/hazards/` |
| Atmosphere/Hydrology overlap | `tools/validators/atmosphere_hydrology/` |
| Generic cross-domain join invariants | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Hydrology/Hazards join schema | `schemas/contracts/v1/joins/hydrology_hazards/` or accepted schema home |
| Hydrology/Hazards meaning | `docs/domains/hydrology/`, `docs/domains/hazards/`, `contracts/domains/hydrology/`, `contracts/domains/hazards/` |
| Policy and release posture | `policy/domains/hydrology/`, `policy/domains/hazards/`, `policy/release/hydrology/`, `policy/release/hazards/`, `release/` |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/hazards/`, `data/proofs/` |
| Receipts | `data/receipts/` |

This README does not move, replace, or override those roots. It only defines where broad Hydrology × Hazards validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Domain boundary | Does Hydrology retain water-system/regulatory/model/observation meaning while Hazards retains event/warning/advisory/impact meaning? | A collapsed flood mega-object. |
| Source role | Are observed, regulatory, modeled, forecast, warning, advisory, declaration, aggregate, and public-map source roles kept distinct? | Interchangeable flood truth. |
| Flood-context handoff | Do NFHL/FEMA/regulatory flood cases route to `tools/validators/flood-context/`? | Local duplicate flood-context authority. |
| Freshness and expiry | Are observed times, source times, valid times, warning/advisory expiry, retrieval time, release time, correction time, and stale-state posture visible? | Current condition by implication. |
| Official-source attribution | Are official sources and public redirects preserved where life-safety action could be inferred? | KFM as alert authority. |
| Not-flood-warning boundary | Does the candidate deny KFM flood-warning, evacuation, dam-safety, navigation, emergency, engineering, insurance, legal, or regulatory authority? | A public instruction surface. |
| Evidence and release posture | Are EvidenceRefs, EvidenceBundles, ReviewRecords, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present where required? | Publication by validation alone. |
| Public surface | Can maps, popups, tiles, graph edges, exports, search, Focus Mode, screenshots, embeddings, or AI text overclaim current risk or official guidance? | UI-only wording problem. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad Hydrology-Hazards validator lane | `tools/validators/hydrology-hazards/` |
| Flood-context validator lane | `tools/validators/flood-context/` |
| Hydrology validator index | `tools/validators/domains/hydrology/`, `tools/validators/hydro/` |
| Hazards validator index | `tools/validators/domains/hazards/`, `tools/validators/hazards/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Hydrology/Hazards domain meaning | `docs/domains/hydrology/`, `docs/domains/hazards/`, `contracts/domains/hydrology/`, `contracts/domains/hazards/` |
| Hydrology/Hazards schemas | `schemas/contracts/v1/domains/hydrology/`, `schemas/contracts/v1/domains/hazards/`, `schemas/contracts/v1/joins/hydrology_hazards/`, or accepted schema homes |
| Policy and release gates | `policy/domains/hydrology/`, `policy/domains/hazards/`, `policy/release/hydrology/`, `policy/release/hazards/`, `release/` |
| Source descriptors | `data/registry/sources/hydrology/`, `data/registry/sources/hazards/`, or accepted source registry homes |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/hazards/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/hydrology-hazards/`, `tests/domains/hydrology/`, `tests/domains/hazards/`, `fixtures/domains/hydrology/`, `fixtures/domains/hazards/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Hydrology-Hazards boundary, source-role, freshness, evidence, policy, release, correction, rollback, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source registry topology, fixture shape, policy bundles, report destinations, receipt emission, release integration, official-source redirect behavior, runtime behavior, and CI wiring.
- **DENY:** using this folder as Hydrology doctrine, Hazards doctrine, schema home, policy home, source registry, source payload storage, proof storage, receipt storage, release record store, public runtime surface, emergency alert authority, flood-warning authority, evacuation authority, insurance authority, regulatory determination authority, engineering authority, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/hydrology-hazards/` include checks that:

- verify Hydrology and Hazards candidates preserve separate object-family identity and source-role posture;
- detect when NFHL/regulatory flood context, gauge observations, modeled hydrographs, flood forecasts, warnings, advisories, declarations, or hazard summaries are collapsed into one unsupported object;
- route flood-context-specific cases to `tools/validators/flood-context/` without duplicating its authority;
- verify observed-vs-regulatory-vs-modeled-vs-warning separation;
- verify valid time, observed time, source time, retrieval time, release time, correction time, expiry, and stale-state posture;
- verify official-source attribution and not-for-life-safety redirect behavior before public surfaces;
- verify cross-domain joins preserve the most restrictive policy and owning-domain responsibility;
- verify source descriptors, EvidenceRefs, EvidenceBundles, review records, policy decisions, release references, correction paths, rollback targets, and stale-state caveats are present where required;
- emit deterministic findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/hydrology-hazards/` | Correct home |
|---|---|
| Hydrology or Hazards doctrine | `docs/domains/hydrology/`, `docs/domains/hazards/` |
| Hydrology or Hazards contracts | `contracts/domains/hydrology/`, `contracts/domains/hazards/` |
| Schemas, DTOs, enums, or join contract machine shape | `schemas/contracts/v1/...` |
| Policy rules, thresholds, release gates, or steward decisions | `policy/...`, `release/` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback cards, corrections, withdrawals | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, emergency alert, flood warning, life-safety instruction, legal/regulatory determination, engineering decision, insurance advice, or AI runtime code | governed application/runtime roots or official agencies, not validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `HYDROLOGY_HAZARDS_VALIDATOR_PASS` | Candidate passed configured Hydrology-Hazards checks. |
| `HYDROLOGY_HAZARDS_VALIDATOR_FAIL` | Candidate failed one or more configured checks. |
| `ROUTE_TO_FLOOD_CONTEXT_VALIDATOR` | Candidate should be checked by `tools/validators/flood-context/`. |
| `ROUTE_TO_HYDROLOGY_VALIDATOR` | Candidate should be checked by Hydrology validator lanes. |
| `ROUTE_TO_HAZARDS_VALIDATOR` | Candidate should be checked by Hazards validator lanes. |
| `JOIN_SCHEMA_MISSING` | Candidate lacks accepted Hydrology-Hazards join schema binding. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses observed, regulatory, modeled, forecast, warning, advisory, aggregate, or public-map roles. |
| `DOMAIN_OWNERSHIP_COLLAPSE` | Candidate collapses Hydrology and Hazards object-family ownership. |
| `NFHL_AS_OBSERVED_FLOOD_DENIED` | Regulatory flood context is presented as observed inundation or forecast. |
| `MODEL_AS_OBSERVATION_DENIED` | Modeled or derived hydrology is presented as measured observation. |
| `WARNING_AS_KFM_AUTHORITY_DENIED` | Warning/advisory/watch context presents KFM as alert authority. |
| `FRESHNESS_OR_EXPIRY_MISSING` | Candidate lacks required time, version, expiry, stale-state, or supersession posture. |
| `OFFICIAL_SOURCE_REDIRECT_MISSING` | Candidate lacks required redirect to official sources where life-safety action could be inferred. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Map, tile, popup, export, search, graph, Focus Mode, screenshot, embedding, or AI surface exposes unsupported or unsafe hazard/hydrology context. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, rollback target, or withdrawal path is absent. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/hydrology-hazards/
├── README.md
├── validate_hydrology_hazards.py        # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If `validate_hydrology_hazards.py` is added, it should act as an adapter or runner that delegates flood-context, Hydrology, Hazards, schema, policy, fixture, evidence, and release checks to accepted validator homes. It should not redefine domain meaning, copy schemas, copy policy, store fixtures, write lifecycle data, approve release, or publish public outputs.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/hydrology-hazards/README.md`.
- [x] It marks this path as a cross-domain validator lane, not Hydrology or Hazards authority.
- [x] It routes flood-context-specific checks to `tools/validators/flood-context/`.
- [x] It points Hydrology and Hazards meaning, schemas, policy, sources, evidence, receipts, release, tests, fixtures, and lifecycle data to owning roots.
- [x] It preserves not-flood-warning, not-life-safety, source-role, freshness/expiry, official-source attribution, evidence, policy, release, correction, rollback, and public-surface denial boundaries.
- [x] It marks executable behavior, schema bindings, policy bundles, fixture files, report destinations, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to `hydrology-hazards` are searched and classified.
- [ ] Accepted schema homes, policy homes, fixture homes, test paths, and report destinations are verified.
- [ ] Valid and invalid fixtures cover source-role collapse, flood-context handoff, stale warnings, NFHL-as-observed-flood, model-as-observation, missing official-source redirects, release gaps, and public-surface leakage.
- [ ] CI invokes the relevant Hydrology-Hazards validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with Hydrology-Hazards cross-domain validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
