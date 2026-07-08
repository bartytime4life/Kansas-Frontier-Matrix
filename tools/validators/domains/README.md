<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-readme
title: tools/validators/domains README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-domain-stewards-plus-validator-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; per-domain-validator-index; fail-closed; evidence-aware; policy-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: parent index for per-domain validator README lanes under tools/validators/domains, preserving responsibility-root boundaries, domain-segment placement, child-lane routing, fail-closed posture, evidence closure, policy checks, release references, correction paths, rollback targets, public-surface denial, and executable-claim verification while deferring domain meaning, schemas, source registries, policy decisions, proofs, receipts, release authority, and public outputs to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../catalog/README.md
  - ../catalog_closure/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - agriculture/README.md
  - archaeology/README.md
  - atmosphere/README.md
  - fauna/README.md
  - flora/README.md
  - geology/README.md
  - habitat/README.md
  - hazards/README.md
  - hydrology/README.md
  - people-dna-land/README.md
  - roads-rail-trade/README.md
  - settlements-infrastructure/README.md
  - soil/README.md
  - ../../../docs/domains/
  - ../../../contracts/domains/
  - ../../../schemas/contracts/v1/domains/
  - ../../../policy/domains/
  - ../../../data/registry/sources/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces the prior one-line parent stub. It does not confirm executable files."
  - "Per-domain validators are fail-closed checkers under tools/validators/. They do not define domain meaning, create schemas, admit sources, create EvidenceBundles, decide policy, approve release, or publish public outputs."
  - "Confirmed top-level child README lanes in current repo evidence/search: agriculture, archaeology, atmosphere, fauna, flora, geology, habitat, hazards, hydrology, people-dna-land, roads-rail-trade, settlements-infrastructure, and soil. Executable behavior remains NEEDS VERIFICATION."
  - "Domain validators must preserve KFM responsibility-root boundaries: docs/contracts/schemas/policy/source registry/evidence/proofs/receipts/release/public runtime remain separate roots."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-per--domain--validators-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/` is the parent index for KFM per-domain validator lanes: domain-segment checkers that enforce declared contracts, schemas, evidence closure, policy posture, release references, correction paths, rollback targets, public-surface denial, and cross-domain authority boundaries without becoming domain doctrine or publication authority.

---

## Purpose

`tools/validators/domains/` exists to organize validators that are specific to one KFM domain segment.

The durable KFM question for this parent lane is:

> Do domain-specific candidates preserve their owning domain's object-family identity, source-role posture, evidence support, policy posture, sensitivity posture, release linkage, correction lineage, rollback target, cross-domain boundaries, and public-surface constraints before they are used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a navigable index and deterministic validation outputs from configured domain child lanes. This folder should not create domain truth, schemas, source descriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/README.md` | **CONFIRMED** | This README replaces the previous one-line parent stub. |
| Parent validators README | **CONFIRMED stub** | `tools/validators/README.md` currently says validators are fail-closed checkers, cross-cutting plus per-domain. |
| Top-level domain README children | **CONFIRMED in current repo evidence/search** | Agriculture, Archaeology, Atmosphere, Fauna, Flora, Geology, Habitat, Hazards, Hydrology, People/DNA/Land, Roads/Rail/Trade, Settlements/Infrastructure, and Soil README lanes have been verified or found in current task context. |
| Nested domain validator README children | **PARTIAL / CONFIRMED by recent edits** | Examples include Agriculture `soil-join/`, Atmosphere `smoke/`, and Soil `catalog_closure/`, `dual_hash/`, `horizon_depth/`, `lineage/`, `moisture/`, and `support_type/`. |
| Executables, schemas, fixtures, policy bundles, report destinations, receipts, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This index does not claim that validators are implemented, wired to CI, or emitting reports/receipts. |

[Back to top](#top)

---

## Confirmed top-level domain lanes

| Domain lane | Validator focus | Status |
|---|---|---|
| [`agriculture/`](agriculture/README.md) | Agriculture-specific validation and cross-lane soil/crop suitability posture. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`archaeology/`](archaeology/README.md) | Archaeology sensitivity, exact-location denial, review, policy, release, and public-surface boundaries. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`atmosphere/`](atmosphere/README.md) | Atmosphere observations and smoke/air/hazards/hydrology boundary posture. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`fauna/`](fauna/README.md) | Fauna occurrence, sensitive-site, taxon/status/range/migration/disease/invasive, geoprivacy, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`flora/`](flora/README.md) | Plant taxon, occurrence/specimen, rare/protected/culturally sensitive flora, geoprivacy, vegetation, invasive, phenology, restoration, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`geology/`](geology/README.md) | Geologic maps, stratigraphy, lithology, subsurface, boreholes/well logs, resource/deposit/permit/production anti-collapse, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`habitat/`](habitat/README.md) | Habitat patches/classes/suitability/connectivity/corridors/restoration/stewardship zones, sensitive joins, geoprivacy, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`hazards/`](hazards/README.md) | Hazard events, observations, warning/advisory context, freshness/expiry, not-for-life-safety boundaries, official-source redirects, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`hydrology/`](hydrology/README.md) | Watersheds, HUC units, reaches, gauges, wells, observations, hydrographs, NFHL/regulatory context, upstream traces, evidence, and not-flood-warning boundaries. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`people-dna-land/`](people-dna-land/README.md) | Person assertions, restricted DNA evidence, consent, revocation, land instruments, person-parcel joins, T4 deny-by-default posture, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`roads-rail-trade/`](roads-rail-trade/README.md) | Road/rail/route/crossing/bridge/ferry/freight/access/network/story boundaries, live-closure and legal-access denial, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | Settlements, facilities, networks, service areas, operators, condition, dependencies, critical-infrastructure sensitivity, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`soil/`](soil/README.md) | Soil catalog closure, dual-hash posture, horizon-depth integrity, lineage, moisture, support-type separation, source-role discipline, evidence, and release checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |

[Back to top](#top)

---

## Nested lanes currently known

These nested lanes are confirmed as README surfaces from recent current-session edits or current repo evidence. They are not executable claims.

| Parent | Nested lane | Use |
|---|---|---|
| `agriculture/` | `soil-join/` | Agriculture × Soil join validation, suitability posture, and cross-domain evidence boundaries. |
| `atmosphere/` | `smoke/` | Smoke context validation with Atmosphere/Hazards boundary checks and not-life-safety posture. |
| `soil/` | `catalog_closure/` | Soil-specific catalog-closure readiness. |
| `soil/` | `dual_hash/` | Soil-specific content/provenance hash posture. |
| `soil/` | `horizon_depth/` | Soil horizon top/bottom depth and component-horizon checks. |
| `soil/` | `lineage/` | Soil source/provenance lineage and MUKEY/COKEY/CHKEY continuity. |
| `soil/` | `moisture/` | SoilMoistureObservation unit/depth/QC/cadence/stale-state checks. |
| `soil/` | `support_type/` | Soil static survey / gridded derivative / station / satellite / pedon-profile / interpretation anti-collapse checks. |

Future nested lanes should be added only when a domain-specific validator specialty is narrow enough to justify its own child folder and has clear relationship to contracts, schemas, policy, fixtures, reports, receipts, release, correction, and rollback.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain validator index | `tools/validators/domains/` |
| Per-domain validator child lanes | `tools/validators/domains/<domain>/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` or accepted cross-lane validator homes |
| Broad catalog validation / catalog closure | `tools/validators/catalog/`, `tools/validators/catalog_closure/` |
| Domain meaning and doctrine | `docs/domains/<domain>/`, `contracts/domains/<domain>/`, or ADR-selected contract homes |
| Domain schemas | `schemas/contracts/v1/domains/<domain>/` or ADR-selected schema homes |
| Domain policy rules | `policy/domains/<domain>/` or accepted policy homes |
| Source descriptors and source registry | `data/registry/sources/<domain>/` or accepted source registry homes |
| Domain catalog records | `data/catalog/domain/<domain>/` or accepted catalog homes |
| EvidenceBundle and proof support | `data/proofs/` and domain proof lanes |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/<domain>/`, `tests/domains/<domain>/`, `fixtures/domains/<domain>/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists and the table lists current README lanes verified or found in current task context.
- **PROPOSED:** validator code may live in this folder tree when it checks declared domain invariants and delegates meaning, source roles, schemas, policy, evidence, proof, receipt, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, field names, schemas, source mappings, fixture shapes, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as a domain doctrine home, source registry, source payload store, contract home, schema home, policy home, catalog store, proof store, receipt store, lifecycle data store, release record store, published artifact store, public runtime surface, operational-advice surface, AI truth source, or publication authority.

[Back to top](#top)

---

## Placement rules for new domain validator lanes

Use this decision pattern before adding a new child under `tools/validators/domains/`:

1. **Is the check domain-specific?** If not, use a cross-cutting validator lane such as `tools/validators/cross-domain-joins/`, `tools/validators/catalog_closure/`, or another accepted shared validator home.
2. **Does the path duplicate an existing child?** If yes, extend the existing child README or runner rather than creating a parallel authority.
3. **Does the validator depend on domain meaning?** Link to `docs/domains/<domain>/` and contracts. Do not define meaning locally.
4. **Does the validator depend on machine shape?** Link to schemas. Do not define schemas locally.
5. **Does the validator depend on allow/deny/restrict/abstain behavior?** Link to policy. Do not decide policy locally.
6. **Does the validator depend on source authority?** Link to source registry. Do not admit sources locally.
7. **Does the validator emit or require proof/receipt/release support?** Link to proof, receipt, and release roots. Do not store those records here.
8. **Does the validator touch public, sensitive, or policy-significant material?** Default to fail closed, deny, abstain, quarantine, redaction/generalization/aggregation, review, or staged access until release support exists.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/` include:

- this parent/index README;
- domain-specific README children;
- optional parent runner code that discovers/delegates to domain child validators without redefining their rules;
- narrow domain validator lanes that check declared contract/schema/policy/evidence/release invariants;
- route tables, ignore-rule guidance, and report-shape guidance for validator execution;
- synthetic fixture references and test-surface guidance;
- docs that explain validator scope without becoming authoritative domain doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/` | Correct home |
|---|---|
| Domain doctrine and meaning | `docs/domains/`, `contracts/domains/`, or accepted contract homes |
| Schemas and enums | `schemas/contracts/v1/` or accepted schema homes |
| Policy and sensitivity rules | `policy/` |
| Source descriptors and source mappings | `data/registry/sources/` or accepted registry homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, release decisions, rollback, corrections, withdrawals | `release/` |
| Pipeline execution logic, ETL, connectors, or source parsers | `pipelines/`, `packages/`, `connectors/`, or accepted implementation roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, operational advice, legal determination, emergency instruction, or publication output | governed application/runtime roots |

[Back to top](#top)

---

## Parent validator posture

This parent lane and its children must fail closed, deny, abstain, or route to review when a candidate:

- lacks required source descriptor, source role, evidence, validation report, policy posture, review state, release reference, correction path, or rollback target;
- collapses object families, support types, source roles, lifecycle states, policy states, evidence/proof state, receipt state, or release state;
- absorbs another domain's truth without preserving ownership, source role, sensitivity, EvidenceBundle support, and release posture;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct canonical/internal stores, direct model outputs, stale source descriptors, or incomplete proof closure;
- treats validator output as source admission, domain truth, schema validation proof unless that is the configured validator, EvidenceBundle creation, PolicyDecision creation, release approval, publication, public API behavior, operational advice, emergency instruction, legal determination, or AI answer authority.

The validator tree must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `DOMAIN_VALIDATORS_PASS` | Configured per-domain validators passed. |
| `DOMAIN_VALIDATORS_FAIL` | One or more configured per-domain validators failed. |
| `DOMAIN_VALIDATOR_MISSING` | Expected domain validator lane or runner is absent. |
| `DOMAIN_CHILD_FAILED` | A child validator reported one or more findings. |
| `DOMAIN_SCOPE_UNKNOWN` | Requested validator scope does not map cleanly to a domain or shared validator lane. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor or source registry pointer is absent. |
| `SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/
├── README.md
├── test_domain_validator_parent.py
├── agriculture/
├── archaeology/
├── atmosphere/
├── fauna/
├── flora/
├── geology/
├── habitat/
├── hazards/
├── hydrology/
├── people-dna-land/
├── roads-rail-trade/
├── settlements-infrastructure/
├── soil/
└── fixtures/
    ├── valid_domain_validator_bundle/
    ├── missing_domain_child/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── policy_or_release_gap/
    ├── cross_domain_authority_collapse/
    └── public_surface_leak_risk/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains
```

```bash
python tools/validators/domains/run_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to domain children instead of redefining their rules.
- [ ] Validators read declared contracts, schemas, source descriptors, source-role rules, and policy rather than defining meaning locally.
- [ ] Domain-specific lanes do not duplicate shared validator homes.
- [ ] Cross-domain joins preserve domain ownership, source role, sensitivity, and EvidenceBundle support.
- [ ] Sensitive lanes fail closed by default and require policy/review/release/correction/rollback support before public use.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for one-line per-domain validators parent stub. |
| Next smallest safe change | Verify actual parent runner, child scripts, schemas, source mappings, source descriptors, fixture shapes, policy bundles, report destinations, receipts, release linkage, cross-domain behavior, and CI/runtime wiring before promoting this lane beyond draft. |
