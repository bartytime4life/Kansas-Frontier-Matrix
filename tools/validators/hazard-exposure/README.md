<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-hazard-exposure-readme
title: tools/validators/hazard-exposure README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hazards-steward-plus-settlements-infrastructure-steward-plus-critical-asset-reviewer-plus-sensitivity-reviewer-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; hazard-exposure-validator; cross-domain; hazards; settlements-infrastructure; critical-asset; exposure-summary; resilience-summary; not-for-life-safety; default-deny; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed cross-domain Hazard Exposure validator lane for checking exposure summaries, resilience summaries, impact-area joins, Hazards x Settlements/Infrastructure joins, facility/critical-asset exposure posture, operational-context freshness, official-source attribution, not-for-life-safety disclaimers, critical-detail default-deny, public-safe geometry, redaction/generalization/suppression receipt linkage, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring Hazards meaning, facility/infrastructure meaning, sensitivity policy, exposure transforms, evidence records, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/hazards/README.md
  - ../domains/settlements-infrastructure/README.md
  - ../facilities/README.md
  - ../flood-context/README.md
  - ../freshness/README.md
  - ../geometry/README.md
  - ../geoprivacy/README.md
  - ../geoprivacy_transform/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../evidence_bundle/README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/PRESERVATION_MATRIX.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../docs/architecture/critical-asset-exposure.md
  - ../../../contracts/domains/hazards/
  - ../../../contracts/domains/settlements-infrastructure/
  - ../../../schemas/contracts/v1/domains/hazards/
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../policy/domains/hazards/
  - ../../../policy/release/hazards/
  - ../../../policy/sensitivity/infrastructure/
  - ../../../policy/sensitivity/
  - ../../../data/registry/sources/hazards/
  - ../../../data/registry/sources/settlements-infrastructure/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Hazards validator evidence says KFM Hazards is not an emergency alert system, life-safety instruction surface, or regulatory determination authority; KFM-as-alert-authority is T4 forever."
  - "Hazards validator evidence names ExposureSummary, ResilienceSummary, ImpactArea, freshness/expiry, not-for-life-safety disclaimers, official-source redirect, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns."
  - "Facilities validator evidence treats critical-asset exposure, facility/operator/condition/dependency posture, public-safe geometry, evidence, policy, release, correction, and rollback as cross-domain validator concerns."
  - "Critical-asset exposure architecture says default-deny for critical detail and release only the safest representation that still answers the legitimate question."
  - "This lane must not issue warnings, provide emergency instructions, certify risk, identify vulnerabilities, approve publication, decide policy, create receipts, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/hazard-exposure

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hazard--exposure--validator-informational)
![boundary](https://img.shields.io/badge/not--for--life--safety-critical)
![sensitivity](https://img.shields.io/badge/critical--detail--deny--default-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/hazard-exposure/` is the proposed cross-domain validator lane for checking hazard exposure and resilience summaries before they can reach public or governed surfaces, without becoming an alerting, emergency, risk-certification, vulnerability, engineering, insurance, or release authority.

---

## Purpose

`tools/validators/hazard-exposure/` exists for hazard exposure validation concerns that cross Hazards, Settlements/Infrastructure, Facilities, Roads/Rail/Trade, Hydrology, Atmosphere, and public-safe map/API surfaces.

The durable KFM question for this lane is:

> Does a hazard exposure candidate preserve hazard-context boundaries, not-for-life-safety posture, official-source attribution, valid/expiry/freshness state, facility and critical-asset sensitivity, public-safe geometry, aggregation/redaction/suppression receipt linkage, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Hazards truth, facility truth, critical-asset truth, current-warning authority, emergency instructions, evacuation advice, regulatory determinations, engineering determinations, insurance/risk determinations, vulnerability maps, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/hazard-exposure/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Hazards validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Hazards index names `ExposureSummary`, `ResilienceSummary`, `ImpactArea`, freshness/expiry, not-for-life-safety boundaries, official-source redirects, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Facilities validator lane | **CONFIRMED README / executable NEEDS VERIFICATION** | The Facilities lane names facility identity, public-safe geometry, operator/condition/dependency claims, critical-asset exposure, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Critical-asset exposure architecture | **CONFIRMED in repo evidence / draft** | `docs/architecture/critical-asset-exposure.md` states default-deny for critical detail and release only the safest representation that still answers the legitimate question. |
| Hazard-exposure executable, schemas, fixtures, policy bundles, transform receipt shapes, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Hazard Exposure validator lane | `tools/validators/hazard-exposure/` |
| Hazards per-domain validator index | `tools/validators/domains/hazards/` |
| Facilities / critical-asset validation | `tools/validators/facilities/` |
| Settlements/Infrastructure validator index | `tools/validators/domains/settlements-infrastructure/` |
| Flood context and regulatory flood posture | `tools/validators/flood-context/` |
| Freshness, expiry, stale-state checks | `tools/validators/freshness/` |
| Public-safe geometry and geoprivacy transform checks | `tools/validators/geometry/`, `tools/validators/geoprivacy/`, `tools/validators/geoprivacy_transform/` |
| Cross-domain joins | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Hazards and infrastructure meaning | `docs/domains/hazards/`, `contracts/domains/hazards/`, `docs/domains/settlements-infrastructure/`, `contracts/domains/settlements-infrastructure/` |
| Critical-asset exposure architecture | `docs/architecture/critical-asset-exposure.md` |
| Policy, proofs, receipts, release | `policy/`, `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where hazard-exposure validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and policy bundle bindings are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Exposure summary | Is the candidate an aggregate/contextual exposure statement with scoped hazard, asset class, geography, time, source, and caveats? | Risk certification or emergency instruction. |
| Not-for-life-safety posture | Are disclaimers, official-source redirects, validity/expiry/freshness, and no-alert-authority boundaries visible? | Current warning, watch, advisory, or emergency directive. |
| Critical-asset detail | Does the candidate expose exact facilities, dependencies, vulnerabilities, operations, conditions, or reverse-engineerable infrastructure detail? | Public-safe detail by default. |
| Geometry posture | Is geometry exact, generalized, redacted, aggregated, suppressed, or denied according to sensitivity and release posture? | Public map readiness by itself. |
| Transform receipt | Is a RedactionReceipt, AggregationReceipt, RepresentationReceipt, or equivalent governed receipt linked when detail is transformed? | Hidden cartographic simplification. |
| Cross-domain join | Do Hazards x Settlements/Infrastructure, Hydrology, Atmosphere, Roads/Rail/Trade, or Facilities joins propagate the most restrictive policy? | A weaker merged policy. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, ReviewRecords, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |
| Public surface leakage | Could map popups, tiles, search, graph edges, exports, screenshots, embeddings, Focus Mode, or AI text reveal critical detail or overstate exposure? | UI-only wording. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Hazard Exposure validator lane | `tools/validators/hazard-exposure/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Hazards validator index | `tools/validators/domains/hazards/` |
| Facilities and infrastructure validator lanes | `tools/validators/facilities/`, `tools/validators/domains/settlements-infrastructure/` |
| Hazards and infrastructure doctrine/contracts | `docs/domains/hazards/`, `contracts/domains/hazards/`, `docs/domains/settlements-infrastructure/`, `contracts/domains/settlements-infrastructure/` |
| Critical-asset exposure architecture | `docs/architecture/critical-asset-exposure.md` |
| Source descriptors | `data/registry/sources/hazards/`, `data/registry/sources/settlements-infrastructure/`, or accepted registry homes |
| Sensitivity and hazard policy | `policy/domains/hazards/`, `policy/release/hazards/`, `policy/sensitivity/infrastructure/`, `policy/sensitivity/`, or accepted policy homes |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/hazard-exposure/`, `tests/domains/hazards/`, `tests/domains/settlements-infrastructure/`, `fixtures/domains/hazards/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared exposure, critical-asset, freshness, geometry, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, hazard-exposure vocabulary, critical-asset tier binding, fixture shape, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Hazards doctrine, emergency alert authority, current-warning authority, life-safety instruction surface, regulatory authority, facility authority, critical-asset inventory, vulnerability map store, source registry, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/hazard-exposure/` include checks that:

- verify hazard exposure/resilience summaries are scoped, aggregated, caveated, source-linked, time-aware, and not framed as emergency guidance;
- verify official-source redirect, validity/expiry/freshness state, stale-state handling, correction lineage, and rollback targets are present where needed;
- verify critical-asset, facility, dependency, vulnerability, operations, condition, and service details fail closed unless public-safe transformation and policy gates support the requested surface;
- verify public-safe geometry and transform receipt linkage for exposure maps, tiles, reports, and summaries;
- verify cross-domain joins propagate the most restrictive policy across Hazards, Settlements/Infrastructure, Facilities, Roads/Rail/Trade, Hydrology, and Atmosphere;
- verify public summaries, catalog records, graph edges, map labels, export rows, Evidence Drawer text, and AI answers do not strengthen the exposure claim;
- emit deterministic findings for downstream review without storing source payloads, exact critical-asset detail, proof artifacts, receipts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/hazard-exposure/` | Correct home |
|---|---|
| Hazards or Settlements/Infrastructure doctrine and object meaning | `docs/domains/`, `contracts/domains/` |
| Emergency warnings, watches, advisories, evacuation instructions, life-safety instructions, or official alert feeds | official external systems and governed source/context lanes only |
| Exact critical facilities, dependencies, vulnerabilities, operations, condition, access, or security-sensitive details | restricted lifecycle lanes; never this README or public outputs |
| SourceDescriptor or source registry records | `data/registry/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Redaction/generalization/aggregation implementation | `packages/`, `pipelines/`, or accepted implementation roots |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, risk certification, insurance/engineering/legal determinations, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures with exact sensitive critical-asset details | public-safe synthetic fixtures under accepted test roots |

[Back to top](#top)

---

## Hazard-exposure validator posture

Hazard-exposure validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, hazard context, asset class, exposure scope, valid/expiry/freshness state, official-source redirect, not-for-life-safety posture, sensitivity tier, geometry role, transform receipt, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- treats exposure context as current warning, emergency instruction, evacuation guidance, risk certification, regulatory determination, insurance determination, or engineering determination;
- exposes exact critical-asset, facility, dependency, vulnerability, operational, service-condition, or security-sensitive detail to public-bound surfaces;
- uses generalized/redacted/aggregated/suppressed exposure outputs without receipt linkage and review support;
- applies a weaker policy than the most restrictive applicable hazard, asset, facility, source, audience, or surface requires;
- hides freshness/expiry/stale state, official-source limitations, uncertainty, model/observation/regulatory distinctions, or correction status;
- allows map popups, tiles, screenshots, search results, graph edges, exports, embeddings, Focus Mode cards, or AI answers to reveal critical detail or overstate exposure;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure;
- treats hazard-exposure validation as SourceDescriptor creation, EvidenceBundle creation, RedactionReceipt creation, PolicyDecision creation, release approval, publication, public API behavior, official alerting, emergency management authority, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `HAZARD_EXPOSURE_PASS` | Configured hazard-exposure checks passed. |
| `HAZARD_EXPOSURE_FAIL` | One or more configured hazard-exposure checks failed. |
| `HAZARD_EXPOSURE_SCOPE_MISSING` | Required hazard, asset, geography, time, or exposure scope is absent. |
| `OFFICIAL_SOURCE_REDIRECT_MISSING` | Required official-source attribution or redirect is absent. |
| `NOT_FOR_LIFE_SAFETY_GAP` | Required disclaimer, no-alert-authority posture, or emergency-boundary statement is absent. |
| `FRESHNESS_OR_EXPIRY_GAP` | Required validity, expiry, stale-state, source-time, retrieval-time, or correction-time posture is incomplete. |
| `CRITICAL_ASSET_EXPOSURE_DENIED` | Critical-asset detail is unsafe for the requested surface. |
| `VULNERABILITY_DETAIL_DENIED` | Dependency, vulnerability, operation, condition, service, or security-sensitive detail is unsafe. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required public-safe geometry role or transform is absent. |
| `EXPOSURE_TRANSFORM_RECEIPT_MISSING` | Required redaction, generalization, aggregation, suppression, or representation receipt is absent. |
| `MOST_RESTRICTIVE_POLICY_GAP` | Candidate does not apply the strongest applicable policy. |
| `SUMMARY_OVERCLAIM` | Public summary, label, graph edge, export, or AI answer strengthens the exposure claim. |
| `SURFACE_RECONSTRUCTION_RISK` | Public surface can narrow or reconstruct protected critical detail. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, exposure transform, evidence closure, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/hazard-exposure/
├── README.md
├── test_hazard_exposure_validator.py
└── fixtures/
    ├── valid_public_aggregate_exposure_summary/
    ├── missing_official_source_redirect/
    ├── not_for_life_safety_gap/
    ├── freshness_or_expiry_gap/
    ├── critical_asset_exposure_denied/
    ├── vulnerability_detail_denied/
    ├── missing_public_safe_geometry/
    ├── missing_exposure_transform_receipt/
    ├── summary_overclaim/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/hazard-exposure
```

```bash
python tools/validators/hazard-exposure/validate_hazard_exposure.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_hazard_exposure.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Hazards, Facilities, Settlements/Infrastructure, source, sensitivity, policy, evidence, release, and correction/rollback records rather than defining meaning locally.
- [ ] Exposure summaries remain contextual and not-for-life-safety.
- [ ] Official-source attribution, validity/expiry/freshness, stale-state, caveats, and correction status remain visible.
- [ ] Critical-asset detail is denied, generalized, redacted, aggregated, suppressed, or routed to review according to policy.
- [ ] Public-safe geometry and transform receipts are required before public-bound exposure outputs are accepted.
- [ ] Public summaries, catalog projections, graph edges, map labels, export rows, Evidence Drawer text, and AI answers do not strengthen the claim or expose critical detail.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, emergency authority, risk certification, policy approval, release, publication, source admission, public API behavior, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures and do not encode exact critical-asset detail or exploitable vulnerability detail.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Hazard Exposure validator file. |
| Next smallest safe change | Verify actual hazard-exposure validator script path, accepted Hazards/Facilities/Infrastructure schemas, critical-asset policy bundle binding, freshness/expiry vocabulary, transform receipt shapes, fixture safety, report destination, receipt lookup, policy enforcement, release linkage, tile/search/graph/vector/AI leakage behavior, and CI/runtime wiring before promoting this lane beyond draft. |
