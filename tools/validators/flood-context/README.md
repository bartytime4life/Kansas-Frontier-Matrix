<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-flood-context-readme
title: tools/validators/flood-context README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-hazards-steward-plus-fema-source-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward-plus-ui-boundary-reviewer
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; flood-context-validator; hydrology; hazards; NFHL; FEMA; regulatory-context; not-flood-warning; not-life-safety; source-role-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed shared Flood Context validator lane for checking NFHL/FEMA/regulatory flood context, flood-context source-role separation, regulatory-vs-observed-vs-forecast-vs-warning anti-collapse, NFHL attribute preservation, effective-date/version posture, source registry linkage, evidence/proof linkage, policy/review/release linkage, correction and rollback linkage, official-source redirects, and public-surface denial checks while deferring Hydrology meaning, Hazards meaning, source registry authority, evidence records, policy decisions, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/hydrology/README.md
  - ../domains/hazards/README.md
  - ../atmosphere_hydrology/README.md
  - ../cross-domain-joins/README.md
  - ../../../docs/sources/catalog/fema/nfhl-flood-hazard.md
  - ../../../docs/sources/catalog/fema/map-service-center.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../contracts/domains/hydrology/
  - ../../../contracts/domains/hazards/
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../policy/domains/hydrology/
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hydrology/
  - ../../../policy/release/hazards/
  - ../../../data/registry/sources/hydrology/
  - ../../../data/registry/sources/hazards/
  - ../../../data/proofs/hydrology/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Hydrology validator evidence says NFHL and similar flood layers are regulatory context only, and validators must deny treating them as observed inundation, forecast flood extent, or emergency instruction."
  - "Hazards validator evidence says KFM is not an emergency alert system, life-safety instruction surface, or regulatory determination authority. Warning/advisory products may only be evidence-bound context with official-source redirect and finite validity posture."
  - "FEMA NFHL source evidence says NFHL is regulatory context, not observed inundation; public surfaces displaying NFHL must redirect life-safety action to official FEMA, NWS, state, and local emergency channels."
  - "This validator lane must not issue flood warnings, make insurance determinations, make engineering/legal/regulatory determinations, approve release, create EvidenceBundles, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/flood-context

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-flood--context--validator-informational)
![boundary](https://img.shields.io/badge/not--flood--warning-critical)
![source](https://img.shields.io/badge/source--role-regulatory-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/flood-context/` is the proposed shared validator lane for checking that FEMA/NFHL and flood-context candidates remain regulatory or contextual evidence, not observed inundation, forecast flood extent, emergency instruction, insurance determination, engineering determination, legal determination, or public alert authority.

---

## Purpose

`tools/validators/flood-context/` exists for flood-context checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a flood-context candidate preserve source role, NFHL/FEMA regulatory posture, version/effective-date lineage, required regulatory attributes, observed-vs-regulatory-vs-modeled-vs-warning separation, Hydrology/Hazards domain boundaries, evidence support, policy/review state, release linkage, correction lineage, rollback target, official-source redirects, and public-surface denial before it is used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Hydrology truth, Hazards truth, official flood-warning authority, emergency instructions, regulatory determinations, insurance determinations, engineering determinations, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/flood-context/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Hydrology validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Hydrology validator index names NFHL/regulatory flood context, not-flood-warning boundaries, source-role separation, freshness/time posture, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Hazards validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Hazards validator index includes FloodContext and states KFM is not an emergency alert system, life-safety instruction surface, or regulatory determination authority. |
| FEMA NFHL source descriptor doc | **CONFIRMED in repo evidence / draft** | The NFHL source page says NFHL is regulatory context, not observed inundation; public surfaces must redirect life-safety action to official FEMA/NWS/state/local channels. |
| Exact flood-context executable, schemas, fixtures, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Shared flood-context validator lane | `tools/validators/flood-context/` |
| Hydrology domain validator index | `tools/validators/domains/hydrology/` |
| Hazards domain validator index | `tools/validators/domains/hazards/` |
| Atmosphere/Hydrology context | `tools/validators/atmosphere_hydrology/` |
| Cross-domain joins | `tools/validators/cross-domain-joins/` |
| Hydrology meaning and contracts | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Hazards meaning and contracts | `docs/domains/hazards/`, `contracts/domains/hazards/` |
| FEMA/NFHL source catalog posture | `docs/sources/catalog/fema/`, `data/registry/sources/` |
| Machine shape | `schemas/contracts/v1/domains/hydrology/`, `schemas/contracts/v1/domains/hazards/`, or accepted schema homes |
| Policy and release posture | `policy/domains/hydrology/`, `policy/domains/hazards/`, `policy/release/`, or accepted policy homes |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |

This README does not move, replace, or override those roots. It only defines where shared flood-context validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Source role | Is the flood-context source marked as regulatory, observed, modeled, aggregate, or another accepted role with clear limits? | Role-free flood truth. |
| NFHL regulatory posture | Are NFHL/FEMA candidates preserved as effective regulatory context? | Observed inundation, forecast, warning, or emergency instruction. |
| Required NFHL attributes | Are `DFIRM_ID`, `VERSION_ID`, `EFFECTIVE_DATE`, zone designation, BFE/datum where present, FIS/study refs, and LOMR/LOMA refs preserved when required? | A normalized summary that drops regulatory meaning. |
| Time/version posture | Are effective dates, source times, revision times, version IDs, and stale-state caveats visible? | Current flood condition or real-time risk. |
| Domain boundary | Does Hydrology own NFHLZone/regulatory context while Hazards owns warning/advisory/event context? | A collapsed flood mega-object. |
| Official-source redirect | Do public outputs direct life-safety action to official FEMA/NWS/state/local channels? | KFM as alert authority. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, policy, review, release, correction, and rollback links present where required? | Publication by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Flood-context validator lane | `tools/validators/flood-context/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Hydrology validator index | `tools/validators/domains/hydrology/` |
| Hazards validator index | `tools/validators/domains/hazards/` |
| Hydrology/Hazards meaning | `docs/domains/hydrology/`, `docs/domains/hazards/`, `contracts/domains/hydrology/`, `contracts/domains/hazards/` |
| Source registry and FEMA source posture | `data/registry/sources/`, `docs/sources/catalog/fema/` |
| Schemas | `schemas/contracts/v1/domains/hydrology/`, `schemas/contracts/v1/domains/hazards/`, or accepted schema homes |
| Policy and release gates | `policy/`, `release/` |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Tests and fixtures | `tests/validators/flood-context/`, `tests/domains/hydrology/`, `tests/domains/hazards/`, `fixtures/domains/hydrology/`, `fixtures/domains/hazards/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared flood-context, NFHL/FEMA, source-role, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, fixture shape, policy bundles, report destinations, receipt emission, release integration, official-source redirect behavior, runtime behavior, and CI wiring.
- **DENY:** using this folder as Hydrology doctrine, Hazards doctrine, FEMA source registry, schema home, source payload storage, proof storage, receipt storage, policy home, release record store, public runtime surface, emergency alert authority, insurance authority, regulatory determination authority, engineering authority, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/flood-context/` include checks that:

- verify NFHL/FEMA flood-context candidates preserve regulatory source role and required source metadata;
- verify NFHL attributes that carry regulatory meaning are preserved verbatim or transformed only with source-preserving receipts;
- detect when NFHL/FEMA regulatory context is treated as observed inundation, forecast extent, real-time water condition, warning, watch, advisory, or emergency instruction;
- verify public-bound flood-context surfaces include official-source redirects and not-for-life-safety posture;
- verify Hydrology and Hazards domain ownership boundaries are visible before cross-domain output;
- verify source descriptors, EvidenceRefs, EvidenceBundles, review records, policy decisions, release references, correction paths, rollback targets, and stale-state caveats are present where required;
- emit deterministic findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/flood-context/` | Correct home |
|---|---|
| Hydrology or Hazards doctrine and meaning | `docs/domains/hydrology/`, `docs/domains/hazards/`, `contracts/domains/` |
| FEMA/NFHL source descriptor records | `data/registry/sources/` or accepted source registry home |
| FEMA/NFHL source catalog prose | `docs/sources/catalog/fema/` |
| Hydrology/Hazards schemas and enums | `schemas/contracts/v1/domains/hydrology/`, `schemas/contracts/v1/domains/hazards/`, or accepted schema homes |
| Policy rules, warning/exposure rules, sensitivity, and release rules | `policy/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| FEMA connectors, parsers, pipelines, or source download code | `connectors/`, `pipelines/`, `packages/`, or accepted implementation roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, emergency instruction, insurance determination, legal/regulatory determination, engineering recommendation, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Flood-context validator posture

Flood-context validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, source family, regulatory/effective-date posture, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- drops or rewrites required NFHL regulatory attributes without original-value preservation and transform receipt support;
- treats NFHL/FEMA regulatory polygons as observed inundation, forecast flood extent, current flood condition, warning/watch/advisory, evacuation guidance, emergency route guidance, insurance determination, engineering determination, legal determination, or regulatory determination by KFM;
- treats NWS/hazard warning context as Hydrology truth or treats Hydrology regulatory context as Hazards alert authority;
- lacks freshness/expiry/effective-date caveats for current-sensitive or public-bound flood context;
- lacks official-source redirect and not-for-life-safety posture for public-bound surfaces;
- exposes critical infrastructure, private parcels, person-level risk, or reverse-engineerable sensitive details through a flood-context join without policy/review/release support;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on flood-context-collapsed records;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, or incomplete proof closure;
- treats flood-context validation as EvidenceBundle creation, PolicyDecision creation, release approval, publication, official-source status, emergency instruction, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `FLOOD_CONTEXT_PASS` | Configured flood-context checks passed. |
| `FLOOD_CONTEXT_FAIL` | One or more configured flood-context checks failed. |
| `FLOOD_SOURCE_DESCRIPTOR_MISSING` | Required source descriptor or source-registry pointer is absent. |
| `FLOOD_SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `FLOOD_REGULATORY_OBSERVED_COLLAPSE` | Regulatory flood context is treated as observed inundation. |
| `FLOOD_REGULATORY_FORECAST_COLLAPSE` | Regulatory flood context is treated as forecast flood extent or current flood condition. |
| `FLOOD_WARNING_AUTHORITY_DENIED` | Candidate treats KFM as warning, watch, advisory, evacuation, or emergency-instruction authority. |
| `NFHL_REQUIRED_ATTRIBUTE_MISSING` | Required NFHL/FEMA regulatory attribute is missing or not preserved. |
| `FLOOD_EFFECTIVE_DATE_OR_VERSION_GAP` | Effective date, version, source time, revision, or stale-state posture is incomplete. |
| `FLOOD_BFE_DATUM_GAP` | BFE/elevation claim lacks datum, unit, or source support. |
| `OFFICIAL_SOURCE_REDIRECT_MISSING` | Public-bound surface lacks official-source redirect where required. |
| `FLOOD_CONTEXT_DOMAIN_COLLAPSE` | Hydrology, Hazards, Infrastructure, People/Land, or other domain authority is collapsed. |
| `FLOOD_SENSITIVE_JOIN_RISK` | Candidate exposes critical infrastructure, private/person-level, parcel-level, or sensitive join detail without approval. |
| `FLOOD_POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `FLOOD_PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, closure, quarantine, or source-admission work before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/flood-context/
├── README.md
├── test_flood_context_validator.py
└── fixtures/
    ├── valid_nfhl_regulatory_context/
    ├── missing_source_descriptor/
    ├── missing_nfhl_required_attribute/
    ├── regulatory_as_observed_denied/
    ├── regulatory_as_forecast_denied/
    ├── warning_authority_denied/
    ├── missing_official_source_redirect/
    ├── bfe_datum_gap/
    ├── sensitive_join_risk/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/flood-context
```

```bash
python tools/validators/flood-context/validate_flood_context.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_flood_context.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Hydrology/Hazards contracts, schemas, source descriptors, FEMA/NFHL source docs, and policy rather than defining meaning locally.
- [ ] NFHL/regulatory context is not treated as observed inundation, forecast, warning, emergency instruction, insurance determination, engineering determination, legal determination, or KFM regulatory authority.
- [ ] Required regulatory attributes remain visible and original values are preserved before EvidenceBundle or release use.
- [ ] Hydrology and Hazards ownership boundaries remain distinct.
- [ ] Public-bound outputs include official-source redirect and not-for-life-safety posture where required.
- [ ] Sensitive joins involving infrastructure, parcels, people, critical assets, or reverse-engineerable details fail closed unless policy/review/release/correction/rollback support exists.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, source-role-collapsed candidates, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source admission, emergency authority, regulatory authority, engineering authority, insurance authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Flood Context validator file. |
| Next smallest safe change | Verify actual flood-context validator script path, accepted Hydrology/Hazards schemas, NFHL source descriptor shape, fixtures, report destination, receipt emission, policy enforcement, official-source redirect behavior, release linkage, and CI/runtime wiring before promoting this lane beyond draft. |
