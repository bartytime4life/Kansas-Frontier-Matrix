<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-facilities-readme
title: tools/validators/facilities README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-facilities-steward-plus-settlements-infrastructure-steward-plus-roads-rail-trade-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; facilities-validator; cross-domain; infrastructure; transport-facility; critical-asset; source-role-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed cross-domain Facilities validator lane for facility-like assets, public facilities, service points, depots, stations, yards, terminals, transport-facility roles, infrastructure facilities, service-area links, operator links, condition/dependency claims, critical-asset exposure, source-role separation, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring facility meaning, schemas, source registry authority, evidence records, policy decisions, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/settlements-infrastructure/README.md
  - ../domains/roads-rail-trade/README.md
  - ../cross-domain-joins/README.md
  - ../../../schemas/contracts/v1/facilities/README.md
  - ../../../schemas/contracts/v1/domains/settlements-infrastructure/README.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/README.md
  - ../../../contracts/domains/settlements-infrastructure/
  - ../../../contracts/domains/roads-rail-trade/transport_facility.md
  - ../../../contracts/domains/roads-rail-trade/depot.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../docs/domains/roads-rail-trade/README.md
  - ../../../docs/architecture/critical-asset-exposure.md
  - ../../../policy/domains/settlements-infrastructure/
  - ../../../policy/domains/roads-rail-trade/
  - ../../../policy/sensitivity/infrastructure/
  - ../../../data/registry/sources/settlements-infrastructure/
  - ../../../data/registry/sources/roads-rail-trade/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces a stray one-character file. It does not confirm executable files."
  - "Facilities are cross-domain and boundary-sensitive. The facilities schema-family README is a proposed/empty family index and does not prove that facilities are already a first-class schema family."
  - "Settlements/Infrastructure validator evidence already treats facility identity, public-safe geometry, operator separation, condition, dependency, critical-infrastructure sensitivity, evidence, policy, release, correction, and rollback as validator concerns."
  - "Critical-asset exposure doctrine/architecture requires default-deny for critical detail and release only the safest representation that still answers the legitimate question."
  - "This validator lane must not certify canonical place identity, property title, structural condition, active service, legal access, public access, operator authority, security posture, publication approval, or public-safe exposure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/facilities

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-facilities--validator-informational)
![boundary](https://img.shields.io/badge/boundary-cross--domain-critical)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/facilities/` is the proposed cross-domain validator lane for facility-like assets and facility-role claims, checking identity, role, operator, condition, dependency, exposure, evidence, policy, release, correction, rollback, and public-surface posture without becoming facility doctrine or infrastructure authority.

---

## Purpose

`tools/validators/facilities/` exists for facility validation concerns that are broader than one domain but narrower than all cross-domain joins.

The durable KFM question for this lane is:

> Does a facility-like candidate preserve facility role, domain ownership, source role, geometry posture, operator posture, service/condition/dependency caveats, evidence support, rights/sensitivity posture, review state, policy decision, release linkage, correction lineage, rollback target, and public-surface denial before it is used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create facility truth, canonical place identity, property title, operator authority, condition authority, service authority, legal-access truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/facilities/README.md` | **CONFIRMED** | This README replaces a stray one-character file. |
| Settlements/Infrastructure validator lane | **CONFIRMED README / executable NEEDS VERIFICATION** | The per-domain validator index includes facility, service-area, operator-condition, network/dependency, critical-infrastructure, and cross-domain-exposure concerns. |
| Facilities schema-family index | **CONFIRMED README / proposed empty family** | `schemas/contracts/v1/facilities/README.md` says facilities are cross-domain and boundary-sensitive, with no schema files found beyond that README during its check. |
| Critical-asset exposure architecture | **CONFIRMED in repo evidence / draft** | `docs/architecture/critical-asset-exposure.md` states default-deny for critical detail and release only the safest representation that still answers the legitimate question. |
| Executables, accepted facility schemas, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator implementation, schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Facilities validator index / optional runner | `tools/validators/facilities/` |
| Domain-specific facility validation | `tools/validators/domains/settlements-infrastructure/`, `tools/validators/domains/roads-rail-trade/`, or accepted domain lane |
| Cross-domain joins involving facilities | `tools/validators/cross-domain-joins/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Facility-like schema shape if accepted | `schemas/contracts/v1/facilities/` or domain schema lanes |
| Settlement/infrastructure facility meaning | `docs/domains/settlements-infrastructure/`, `contracts/domains/settlements-infrastructure/` |
| Transport-facility role meaning | `docs/domains/roads-rail-trade/`, `contracts/domains/roads-rail-trade/` |
| Critical-asset exposure architecture | `docs/architecture/critical-asset-exposure.md` |
| Facility/infrastructure policy and sensitivity | `policy/domains/settlements-infrastructure/`, `policy/domains/roads-rail-trade/`, `policy/sensitivity/infrastructure/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/settlements-infrastructure/`, `data/registry/sources/roads-rail-trade/`, or accepted registry homes |
| Proofs, receipts, release | `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where a cross-domain facilities validator may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until accepted schemas and executable behavior are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Facility role | Is the candidate a facility, facility-like asset, transport-facility role, public facility, service point, terminal, depot, station, yard, or accepted equivalent? | Canonical place truth by itself. |
| Domain ownership | Does the candidate belong to Settlements/Infrastructure, Roads/Rail/Trade, or another domain lane? | A reason to collapse domain authority. |
| Geometry posture | Is geometry exact, generalized, hidden, aggregated, denied, or public-safe? | Public-safe exposure by default. |
| Operator/service posture | Are operator, service, access, active/inactive, condition, and dependency claims scoped and cited? | Active service, legal access, safety, or operator authority. |
| Critical-asset posture | Does the candidate expose critical infrastructure, vulnerability, dependency, or reverse-engineerable detail? | Public release without policy/review/receipts. |
| Evidence and release posture | Are EvidenceRefs, EvidenceBundles, source descriptors, review, policy, release, correction, and rollback links present? | Release approval by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Facilities validator lane | `tools/validators/facilities/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Settlements/Infrastructure validator lane | `tools/validators/domains/settlements-infrastructure/` |
| Roads/Rail/Trade validator lane | `tools/validators/domains/roads-rail-trade/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Facility schemas if accepted | `schemas/contracts/v1/facilities/` or domain schema homes |
| Domain meaning and contracts | `docs/domains/`, `contracts/domains/` |
| Policy and sensitivity | `policy/` |
| Source descriptors | `data/registry/sources/` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/facilities/`, `tests/domains/settlements-infrastructure/`, `tests/domains/roads-rail-trade/`, `fixtures/domains/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared facility-role, exposure, evidence, policy, and release-reference rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, fixture shape, policy bundles, report destinations, receipt emission, release integration, domain-routing behavior, runtime behavior, and CI wiring.
- **DENY:** using this folder as facility doctrine, schema home, source registry, proof storage, receipt storage, policy home, release record store, public runtime surface, security authority, condition authority, legal-access authority, operator authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/facilities/` include checks that:

- verify facility-like records route to the correct domain authority or accepted cross-domain schema family;
- verify facility role, facility type, source role, source descriptor, EvidenceRef/EvidenceBundle support, and time scope are present where required;
- verify exact facility geometry, sensitive dependency links, operator-sensitive attributes, condition/vulnerability claims, and continuity-critical details fail closed unless public-safe transform support exists;
- verify RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, and rollback target are present where required;
- verify transport-facility role claims do not become canonical settlement/infrastructure truth without support;
- verify facility claims do not imply active service, legal access, right-of-way, safety, structural condition, operator status, emergency routing, or regulatory status without owning authority;
- emit deterministic findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/facilities/` | Correct home |
|---|---|
| Facility doctrine or meaning | `docs/domains/`, `contracts/domains/`, or accepted contract homes |
| Facility schemas/enums | `schemas/contracts/v1/facilities/`, domain schema homes, or ADR-selected homes |
| Source descriptors or source registry records | `data/registry/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, RedactionReceipts, AggregationReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| Pipeline execution logic or source parsers | `pipelines/`, `packages/`, or accepted implementation roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, emergency instruction, legal determination, operational route guidance, security posture, or publication output | governed application/runtime roots |

[Back to top](#top)

---

## Facilities validator posture

Facilities validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor, source role, domain owner, facility role/type, time scope, geometry posture, EvidenceRef, EvidenceBundle/proof reference, validation report, policy posture, release reference, correction path, or rollback target required for its use;
- collapses canonical place identity, facility role, operator status, public access, legal access, service status, condition observation, dependency edge, security posture, and publication authority into one object;
- exposes exact critical-infrastructure location, sensitive dependency, vulnerability, continuity-critical detail, operator-sensitive detail, or reverse-engineerable derivative without approved public-safe transform and receipt support;
- treats a transport depot/station/yard/terminal role as canonical settlement/infrastructure identity without evidence and domain routing;
- treats a public facility label as proof of active service, legal access, open status, emergency suitability, structural condition, safety, or operator authority;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on unvalidated or over-exposed facility candidates;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, or incomplete proof closure;
- treats facilities validation as EvidenceBundle creation, PolicyDecision creation, release approval, publication, security clearance, emergency instruction, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `FACILITIES_VALIDATOR_PASS` | Configured facilities checks passed. |
| `FACILITIES_VALIDATOR_FAIL` | One or more configured facilities checks failed. |
| `FACILITY_DOMAIN_OWNER_MISSING` | Candidate does not identify the owning domain or accepted cross-domain lane. |
| `FACILITY_ROLE_MISSING` | Required facility role/type is absent. |
| `FACILITY_SCHEMA_UNRESOLVED` | Candidate cannot be mapped to an accepted schema or abstain path. |
| `FACILITY_EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `FACILITY_SOURCE_DESCRIPTOR_MISSING` | Required source descriptor pointer is absent. |
| `FACILITY_GEOMETRY_EXPOSURE_DENIED` | Geometry is too exact or reverse-engineerable for the requested surface. |
| `CRITICAL_ASSET_EXPOSURE_DENIED` | Candidate exposes critical-asset detail without public-safe transform support. |
| `OPERATOR_OR_CONDITION_AUTHORITY_COLLAPSE` | Operator, service, condition, access, safety, or dependency claims exceed authority. |
| `TRANSPORT_FACILITY_ROLE_COLLAPSE` | Transport-facility role is treated as canonical facility/place truth without support. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, closure, or quarantine before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/facilities/
├── README.md
├── test_facilities_validator.py
└── fixtures/
    ├── valid_public_safe_facility/
    ├── missing_domain_owner/
    ├── missing_facility_role/
    ├── unresolved_schema/
    ├── missing_evidence_ref/
    ├── exact_critical_asset_location_denied/
    ├── missing_redaction_receipt/
    ├── operator_condition_authority_collapse/
    ├── transport_facility_role_collapse/
    └── public_surface_leak_risk/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/facilities
```

```bash
python tools/validators/facilities/validate_facilities.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_facilities.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator routes facility-like candidates to the correct domain or accepted cross-domain schema family.
- [ ] Validator reads declared contracts, schemas, source descriptors, source-role rules, and policy rather than defining meaning locally.
- [ ] Facility role, canonical identity, operator, service, condition, dependency, access, and exposure posture remain distinct.
- [ ] Critical-asset details fail closed unless public-safe transform, receipt, review, policy, release, correction, and rollback support exists.
- [ ] Cross-domain joins preserve Settlements/Infrastructure, Roads/Rail/Trade, Hazards, Hydrology, People/Land, Archaeology, Geology, Agriculture, and Habitat boundaries.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source authority, facility authority, legal access, condition authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for stray one-character Facilities validator file. |
| Next smallest safe change | Verify actual facilities validator script path, accepted schemas, fixtures, domain-routing behavior, report destination, receipt emission, policy enforcement, release linkage, critical-asset exposure behavior, and CI/runtime wiring before promoting this lane beyond draft. |
