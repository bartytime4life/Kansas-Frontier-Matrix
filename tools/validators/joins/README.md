<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-joins-readme
title: tools/validators/joins README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-join-steward-plus-architecture-steward-plus-domain-stewards-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; joins-validator-index; cross-domain-validator; source-role-aware; sensitivity-preserving; evidence-bound; release-gated; non-authoritative
owning_root: tools/
responsibility: shared parent index for named join validator lanes under tools/validators/joins; routes pair-specific join validators, generic cross-domain join invariants, source-role anti-collapse, sensitivity propagation, evidence/proof linkage, policy/review/release linkage, correction cascade, rollback support, and public-surface denial checks while deferring domain meaning, schemas, policy decisions, evidence records, receipts, lifecycle data, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../identity/README.md
  - agriculture-soil/README.md
  - person-parcel/README.md
  - ../../../docs/architecture/cross-domain/cross-lane-relations.md
  - ../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../docs/architecture/cross-domain/shared-kernel.md
  - ../../../docs/architecture/cross-domain/trust-membrane.md
  - ../../../contracts/crosswalks/
  - ../../../contracts/domains/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/registry/sources/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/joins/README.md. It does not confirm executable validator code."
  - "Pair-specific join lanes currently confirmed here include agriculture-soil/ and person-parcel/. Executable behavior remains NEEDS VERIFICATION."
  - "Generic cross-domain invariant checks remain documented at tools/validators/cross-domain-joins/. The cross-lane/ path is a compatibility bridge and should not duplicate logic."
  - "Join validators must preserve owning domain, source role, sensitivity posture, EvidenceBundle support, lifecycle state, policy posture, release references, correction paths, rollback targets, and public-surface limits."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, policy references, and release readiness. They do not define domain meaning, create EvidenceBundles, decide policy, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/joins

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-join--validator--index-informational)
![invariants](https://img.shields.io/badge/invariants-ownership%20%7C%20role%20%7C%20sensitivity%20%7C%20evidence-blueviolet)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/joins/` is the parent index for named pair-specific join validators. It keeps join validation visible without becoming domain meaning, schema, policy, evidence, receipt, lifecycle-data, release, graph, map, API, or AI authority.

---

## Purpose

`tools/validators/joins/` exists to organize pair-specific join validator lanes under the durable `tools/validators/` surface.

The durable KFM question for this parent index is:

> Which named join validators exist, and do they preserve owning domain, object identity, source role, sensitivity posture, evidence support, lifecycle state, policy/review state, release linkage, correction lineage, rollback target, and public-surface limits before joined candidates reach catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create domain truth, relation truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, graph truth, map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/joins/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| `tools/validators/joins/agriculture-soil/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Shared Agriculture × Soil join validator routing lane for MUKEY/COKEY/CHKEY continuity, Soil-owned evidence consumption, Agriculture-owned derivatives, source-role discipline, support-type separation, release readiness, correction cascade, rollback support, and public-surface denial. |
| `tools/validators/joins/person-parcel/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Shared person-parcel join validator routing lane with fail-closed defaults for living-person, consent, privacy, title-sensitive, parcel-sensitive, DNA/genealogy-derived, and public-surface risks. |
| `tools/validators/cross-domain-joins/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Generic cross-domain join invariant lane for ownership, source-role, sensitivity, and EvidenceBundle support. |
| `tools/validators/cross-lane/README.md` | **CONFIRMED compatibility bridge** | Points maintainers to `cross-domain-joins/` and should not duplicate validator authority. |
| Executables, registry wiring, fixtures, schema bindings, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a runnable validator, test suite, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| [`agriculture-soil/`](agriculture-soil/README.md) | Does an Agriculture × Soil candidate consume Soil-owned objects through governed EvidenceRefs, preserve MUKEY/COKEY/CHKEY identity, preserve Soil support type and source role, produce only Agriculture-owned derivatives, and include evidence/policy/release/correction/rollback support? | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`person-parcel/`](person-parcel/README.md) | Does a person-parcel candidate preserve person assertion evidence, living-person and consent posture, land-instrument and parcel source roles, ownership interval uncertainty, assessor/tax administrative context, parcel-geometry caveats, title-sensitive boundaries, privacy policy, release linkage, correction lineage, rollback target, and public-surface denial? | **CONFIRMED README / executable NEEDS VERIFICATION** |

Future child lanes should be added only when the join has distinct boundary rules, sensitivity posture, source-role risk, schema/report needs, or release implications. Avoid creating a child lane for every possible domain pair unless there is a real validator distinction.

Possible future children remain **PROPOSED** until created and verified:

- `hydrology-soil/` for watershed/reach/soil identity, hydrologic soil group, support-type separation, and evidence posture;
- `hydrology-hazards/` if maintainers choose to mirror the existing top-level lane under `joins/` rather than keep it at `tools/validators/hydrology-hazards/`;
- `flora-habitat/` for habitat/species/source-role/sensitivity joins;
- `fauna-habitat/` for species-location and habitat joins with geoprivacy controls;
- `infrastructure-hazards/` for hazard exposure joins that must avoid life-safety or infrastructure leakage;
- `people-genealogy/` only if consent, sensitivity, living-person, DNA, and public-surface boundaries are explicitly scoped and reviewed.

[Back to top](#top)

---

## Relationship to nearby validator lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Pair-specific join validator index | `tools/validators/joins/` | This parent README and named child lanes. |
| Generic cross-domain join invariants | `tools/validators/cross-domain-joins/` | Full generic validator boundary for ownership, source role, sensitivity, and evidence support. |
| Cross-lane naming bridge | `tools/validators/cross-lane/` | Compatibility pointer; should not duplicate validator logic. |
| Shared validator plumbing | `tools/validators/_common/` | Common runner/helper code if accepted. |
| Identity checks | `tools/validators/identity/` | Identity-token, spec-hash, canonicalization, and public-safe ID checks. |
| Domain-specific validators | `tools/validators/domains/<domain>/` and accepted domain validator lanes | Domain-specific checks stay with owning domain lanes. |
| Domain meaning | each owning domain's `docs/domains/` and `contracts/domains/` lanes | Validators check conformance; docs/contracts define meaning. |
| Crosswalk/relation meaning | `contracts/crosswalks/` or accepted cross-domain contract homes | Relation meaning belongs in contracts, not validator folders. |
| Machine shape | `schemas/contracts/v1/` or accepted schema homes | Schemas define shape; this folder does not. |
| Policy and release posture | `policy/`, `release/` | Validators report gaps; they do not decide policy or release. |
| Evidence/proof support | `data/proofs/` | Validators check references; they do not create proof authority. |
| Receipts | `data/receipts/` | Receipts remain separate from validator docs. |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/published/` | Lifecycle authority stays in `data/`. |

[Back to top](#top)

---

## Parent join invariants

Every child lane under `tools/validators/joins/` must preserve the generic KFM cross-domain invariants and any stricter pair-specific rules.

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Ownership preserved | Each joined side keeps its owning domain and object identity. | Join silently rebinds one side into the other domain. |
| Source role preserved | Each side carries observed, regulatory, modeled, administrative, aggregate, candidate, synthetic, or public-safe role as applicable. | Join collapses or drops source role labels. |
| Sensitivity preserved | Joined output inherits the most restrictive applicable posture. | Join downgrades sensitivity or treats aggregation as automatic public release. |
| Evidence support resolved | Consequential sides resolve to evidence support before public exposure. | EvidenceRef is missing, unresolved, or only resolves on one side. |
| Lifecycle state respected | Joined output cannot bypass RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED gates. | Validator output becomes a file move or publication shortcut. |
| Policy/review state visible | Applicable PolicyDecision, review state, consent state, rights posture, and release gate are visible where required. | Join proceeds with missing, stale, ambiguous, or contradicted policy/review support. |
| Correction and rollback preserved | Correction, withdrawal, revocation, stale-state, source-rights change, or evidence invalidation propagates to joined derivatives. | Downstream derivative remains current after a blocking change. |
| Public surface denied unless safe | Map, tile, popup, export, search, graph, Focus Mode, screenshot, embedding, or AI output is withheld unless public-safe and release-supported. | Joined content leaks sensitive, unsupported, unreviewed, or overclaiming context. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Shared joins parent index | `tools/validators/joins/` |
| Pair-specific join validator lanes | `tools/validators/joins/<join-name>/` |
| Generic cross-domain invariant validator | `tools/validators/cross-domain-joins/` |
| Cross-lane naming bridge | `tools/validators/cross-lane/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Domain-specific validator lanes | `tools/validators/domains/`, `tools/validators/<domain>/`, or accepted validator homes |
| Domain meaning | `docs/domains/`, `contracts/domains/` |
| Crosswalk/relation contracts | `contracts/crosswalks/` or accepted relation contract homes |
| Machine schemas | `schemas/contracts/v1/` or accepted schema homes |
| Policy rules and release gates | `policy/`, `release/` |
| Source descriptors | `data/registry/sources/` and accepted source registry homes |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/joins/`, `tests/validators/cross-domain-joins/`, `fixtures/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists, and child README lanes currently confirmed in this index are `agriculture-soil/` and `person-parcel/`.
- **PROPOSED:** validator code may live here or in child lanes when it checks declared join invariants and delegates meaning, schemas, policy, evidence, receipts, lifecycle data, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source descriptors, fixture shape, policy bundles, consent resolvers where relevant, report destinations, receipt emission, runtime behavior, release integration, and CI wiring.
- **DENY:** using this folder as domain doctrine, relation doctrine, schema home, policy home, consent authority, source registry, evidence store, lifecycle data store, proof store, receipt store, release record store, graph authority, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/joins/` include:

- this parent README;
- named child README lanes for join families with distinct boundary rules;
- lightweight validator adapters that delegate to shared plumbing, domain validators, schema validators, policy validators, evidence validators, and release checks;
- deterministic checks for ownership preservation, source-role preservation, sensitivity propagation, evidence closure, lifecycle posture, policy/review state, release references, correction cascades, rollback targets, and public-surface denial;
- routing notes that prevent orphan join validators and naming drift;
- generated validation report guidance only when report destinations are accepted and verified.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/joins/` | Correct home |
|---|---|
| Domain doctrine or contracts | `docs/domains/`, `contracts/domains/` |
| Crosswalk/relation semantic contracts | `contracts/crosswalks/` or accepted relation contract homes |
| Schemas, DTOs, enums, or join machine shape | `schemas/contracts/v1/...` |
| Policy rules, consent rules, sensitivity rules, release gates, steward decisions, or hidden thresholds | `policy/...`, `release/` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, decisions, rollback cards, corrections, withdrawals | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, screenshot, embedding, or AI runtime code | governed application/runtime roots |
| Sensitive exact locations, private person links, private parcel links, protected species locations, infrastructure exposure, archaeological locations, DNA/genomic details, or reconstruction hints | denied here; keep out of repository-facing validator documentation |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `JOIN_VALIDATOR_PASS` | Candidate passed configured join checks. |
| `JOIN_VALIDATOR_FAIL` | Candidate failed one or more configured join checks. |
| `JOIN_VALIDATOR_DENY` | Candidate is denied because risk, evidence, rights, policy, consent, review, release, or public-surface support cannot be resolved. |
| `JOIN_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `JOIN_VALIDATOR_ABSTAIN` | Candidate lacks enough evidence or policy support to assert the join. |
| `ROUTE_TO_PAIR_JOIN_VALIDATOR` | Candidate should be handled by a named child lane under `tools/validators/joins/`. |
| `ROUTE_TO_CROSS_DOMAIN_JOIN_VALIDATOR` | Candidate should be handled by `tools/validators/cross-domain-joins/`. |
| `ROUTE_TO_DOMAIN_VALIDATOR` | Candidate needs one or more domain-side validators before join evaluation. |
| `OWNERSHIP_COLLAPSE` | Join collapses owning-domain identity or authority. |
| `SOURCE_ROLE_COLLAPSE` | Join hides, rewrites, or conflates source roles. |
| `SENSITIVITY_DOWNGRADE_DENIED` | Join weakens the most restrictive applicable sensitivity posture. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `POLICY_OR_REVIEW_GAP` | Required PolicyDecision, review state, consent state, rights posture, or release policy support is absent. |
| `LIFECYCLE_BYPASS_DENIED` | Join is used to skip governed lifecycle state transitions. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, rollback target, or withdrawal path is absent. |
| `CORRECTION_CASCADE_MISSING` | Correction, revocation, withdrawal, stale state, rights change, or evidence invalidation did not propagate. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Map, tile, popup, export, search, graph, Focus Mode, screenshot, embedding, or AI surface exposes unsafe joined context. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/joins/
├── README.md
├── agriculture-soil/
│   └── README.md
├── person-parcel/
│   └── README.md
├── validate_join.py                     # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If `validate_join.py` is added, it should act as a dispatcher or adapter that routes to accepted child lanes, `cross-domain-joins/`, domain validators, schemas, policy, evidence, receipt, and release checks. It should not redefine domain meaning, copy schemas, copy policy, store fixtures, write lifecycle data, approve release, publish public outputs, or generate AI truth.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/joins/README.md`.
- [x] It marks this path as a shared join validator parent index, not domain, schema, policy, evidence, consent, release, graph, public runtime, or AI authority.
- [x] It lists confirmed child lanes for `agriculture-soil/` and `person-parcel/`.
- [x] It points generic cross-domain invariants to `tools/validators/cross-domain-joins/` and treats `cross-lane/` as a compatibility bridge.
- [x] It preserves ownership, source-role, sensitivity, evidence, lifecycle, policy, release, correction, rollback, and public-surface denial posture.
- [x] It routes machine shape, policy, fixtures, evidence, receipts, release, lifecycle data, tests, and domain meaning to their owning roots.
- [x] It marks executable behavior, registry wiring, schema bindings, policy bundles, fixture files, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to `joins/` are searched and classified.
- [ ] Accepted schema homes, policy homes, fixture homes, test paths, and report destinations are verified.
- [ ] Tests exercise valid and invalid generic join cases and pair-specific child lane cases.
- [ ] CI invokes the relevant join validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with shared joins validator parent index. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
