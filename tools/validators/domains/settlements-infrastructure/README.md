<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-settlements-infrastructure-readme
title: tools/validators/domains/settlements-infrastructure README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-settlements-infrastructure-steward-plus-infrastructure-sensitivity-reviewer-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; settlements-infrastructure; facilities; networks; dependencies; critical-infrastructure; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Settlements/Infrastructure validator index for Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, InfrastructureAsset, NetworkNode, NetworkSegment, Facility, ServiceArea, Operator, ConditionObservation, Dependency, source-role separation, sensitive infrastructure posture, cross-domain ownership, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring domain meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../docs/domains/settlements-infrastructure/README.md
  - ../../../../docs/domains/settlements-infrastructure/IDENTITY_MODEL.md
  - ../../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../../docs/domains/settlements-infrastructure/CONTINUITY_INVENTORY.md
  - ../../../../docs/runbooks/settlements-infrastructure/PROMOTION_RUNBOOK.md
  - ../../../../docs/runbooks/settlements-infrastructure/ROLLBACK_RUNBOOK.md
  - ../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../contracts/domains/settlements-infrastructure/
  - ../../../../schemas/contracts/v1/domains/settlements-infrastructure/
  - ../../../../policy/domains/settlements-infrastructure/
  - ../../../../policy/sensitivity/settlements-infrastructure/
  - ../../../../data/registry/sources/settlements-infrastructure/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "No broad tools/validators/settlements-infrastructure/README.md was found during this task, so this path currently serves as the inspected per-domain Settlements/Infrastructure validator index."
  - "Settlements/Infrastructure exact facility, dependency, operator-sensitive, condition, vulnerability, and continuity-critical network details are restricted or denied by default unless public-safe aggregation, review, policy, evidence, release, correction, and rollback support exists."
  - "Validators enforce declared contracts, schemas, and policy. They do not define settlement truth, infrastructure truth, operator authority, facility condition truth, EvidenceBundle content, policy decisions, release decisions, or public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/settlements-infrastructure

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-settlements--infrastructure--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-restricted%2Freview-important)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/settlements-infrastructure/` is the proposed per-domain Settlements/Infrastructure validator index for settlements, municipalities, census places, historic townsites, forts, missions, reservation communities, infrastructure assets, networks, facilities, service areas, operators, condition observations, dependencies, source-role separation, sensitive-infrastructure posture, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/settlements-infrastructure/` exists to organize Settlements/Infrastructure validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Settlements/Infrastructure candidates preserve place, facility, network, operator, condition, and dependency identity; source-role posture; temporal scope; infrastructure sensitivity; neighboring-domain ownership; evidence closure; review state; policy decisions; release readiness; correction paths; rollback support; and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create settlement truth, facility truth, operator truth, condition truth, dependency truth, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/settlements-infrastructure/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/settlements-infrastructure/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected Settlements/Infrastructure validator index. |
| Settlements/Infrastructure domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/settlements-infrastructure/README.md` defines scope, object families, sensitivity default, non-ownership boundaries, and responsibility-root split. |
| Sensitive infrastructure doctrine | **CONFIRMED in repo evidence / draft** | ADR-0010 draft includes critical infrastructure among deny-by-default sensitivity classes and requires fail-closed policy gates for exact or identifying release when support is incomplete. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child Settlements/Infrastructure validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Settlements/Infrastructure validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `settlement-identity/` for settlements, municipalities, census places, townsites, ghost towns, forts, missions, and reservation-community identity;
- `facility/` for facility identity, type, source role, public-safe geometry, and operator separation;
- `network/` for network nodes, network segments, dependencies, and graph-derived topology;
- `service-area/` for service-area provenance, modeled/administrative/observed separation, and public-safe aggregation;
- `operator-condition/` for operator assertions, condition observations, time scope, and sensitivity posture;
- `critical-infrastructure/` for sensitive facility, dependency, continuity-critical, and reverse-engineerable public-surface checks;
- `cross-domain-exposure/` for Hazards, Roads/Rail/Trade, Hydrology, People/Land, Archaeology, Geology, Agriculture, and Habitat joins.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Settlements/Infrastructure validator index | `tools/validators/domains/settlements-infrastructure/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Settlements/Infrastructure domain meaning | `docs/domains/settlements-infrastructure/`, `contracts/domains/settlements-infrastructure/` |
| Settlements/Infrastructure schemas | `schemas/contracts/v1/domains/settlements-infrastructure/` or ADR-selected homes |
| Policy rules | `policy/domains/settlements-infrastructure/`, `policy/sensitivity/settlements-infrastructure/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/settlements-infrastructure/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/settlements-infrastructure/`, `tests/domains/settlements-infrastructure/`, `fixtures/domains/settlements-infrastructure/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live below this folder when it checks declared Settlements/Infrastructure invariants and delegates meaning, source roles, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as settlements doctrine, infrastructure doctrine, facility authority, operator authority, condition authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/settlements-infrastructure/` include:

- this parent/index README;
- child README lanes for narrow Settlements/Infrastructure validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check settlement, municipality, census place, townsite, ghost town, fort, mission, reservation community, infrastructure asset, network node, network segment, facility, service area, operator, condition observation, and dependency posture;
- validators that check source-role discipline, temporal scope, public-safe geometry, sensitive-infrastructure posture, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Roads/Rail/Trade, Hydrology, Hazards, People/DNA/Land, Archaeology, Agriculture, Geology, Habitat, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Settlements/Infrastructure doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/settlements-infrastructure/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Settlements/Infrastructure domain docs | `docs/domains/settlements-infrastructure/` |
| Domain contracts | `contracts/domains/settlements-infrastructure/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and sensitivity rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, RedactionReceipts, AggregationReceipts, ValidationReports | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, asset-security, condition-authority, dependency-authority, operator-authority, emergency, safety, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Settlements/Infrastructure validator posture

Settlements/Infrastructure validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, rights, time, geometry lineage, operator, condition, dependency, or object-family support;
- collapses Settlement, Municipality, CensusPlace, Townsite, GhostTown, Fort, Mission, ReservationCommunity, InfrastructureAsset, NetworkNode, NetworkSegment, Facility, ServiceArea, Operator, ConditionObservation, or Dependency into another role;
- treats an administrative boundary, census place, facility point, service area, dependency edge, or condition observation as an operational, legal, safety, security, or regulatory determination without owning authority and release support;
- exposes restricted facility details, operator-sensitive details, exact dependency relationships, condition/vulnerability context, continuity-critical network details, or reverse-engineerable derivatives without public-safe transform and review support;
- imports Roads/Rail route truth, Hydrology water truth, Hazards event/warning truth, People/Land ownership truth, Archaeology location truth, Geology/Soil truth, or Agriculture operational truth without preserving ownership, source role, sensitivity, and EvidenceBundle support;
- lacks a named redaction/generalization/aggregation transform, RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Settlements/Infrastructure content beyond the approved public-safe derivative;
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
| `SETTLE_INFRA_DOMAIN_VALIDATORS_PASS` | Configured Settlements/Infrastructure validators passed. |
| `SETTLE_INFRA_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Settlements/Infrastructure child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `SETTLEMENT_IDENTITY_UNRESOLVED` | Place, settlement, municipality, census place, or historic settlement identity is unresolved. |
| `INFRASTRUCTURE_IDENTITY_UNRESOLVED` | Facility, asset, node, segment, network, service area, operator, condition, or dependency identity is unresolved. |
| `CRITICAL_INFRASTRUCTURE_DENIED` | Candidate exposes restricted infrastructure detail without approved public-safe support. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required generalized/redacted/aggregated geometry or profile is absent. |
| `CONDITION_OR_DEPENDENCY_AUTHORITY_COLLAPSE` | Condition, dependency, or service information is presented beyond its evidence and authority. |
| `SENSITIVE_JOIN_DENIED` | Settlement/infrastructure join reveals or infers restricted neighboring-domain context. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Settlements/Infrastructure without preserving boundaries. |
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
tests/validators/domains/settlements-infrastructure/
├── README.md
├── test_settlements_infrastructure_domain_validator_parent.py
└── fixtures/
    ├── valid_public_safe_settlement_bundle/
    ├── missing_evidence_ref/
    ├── source_role_collapse/
    ├── settlement_identity_unresolved/
    ├── infrastructure_identity_unresolved/
    ├── critical_infrastructure_denied/
    ├── public_safe_geometry_missing/
    ├── condition_or_dependency_authority_collapse/
    ├── sensitive_join_denied/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/settlements-infrastructure
```

```bash
python tools/validators/domains/settlements-infrastructure/run_settlements_infrastructure_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_settlements_infrastructure_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared Settlements/Infrastructure contracts, schemas, and policy rather than defining meaning locally.
- [ ] Settlement, municipality, census place, townsite, ghost town, fort, mission, reservation community, facility, network, operator, condition, and dependency object families remain distinct.
- [ ] Source role, temporal scope, geometry lineage, public-safe geometry, and sensitivity posture remain visible.
- [ ] Critical infrastructure details fail closed unless approved public-safe transform support exists.
- [ ] KFM is never presented as operator, security, condition, dependency, emergency, safety, engineering, legal, or regulatory authority.
- [ ] Cross-domain joins preserve ownership, source role, sensitivity, and EvidenceBundle support.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces do not reveal restricted details or reverse-engineerable derivatives.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, infrastructure authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub and current parent index for Settlements/Infrastructure validators. |
| Next smallest safe change | Verify child validator scripts, accepted profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, public-safe geometry behavior, infrastructure-sensitivity behavior, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
