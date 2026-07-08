<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-fauna-readme
title: tools/validators/fauna README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-fauna-steward-plus-sensitive-species-reviewer-plus-geoprivacy-reviewer-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; fauna-validator-parent; broad-fauna-routing-index; sensitive-species; geoprivacy; source-role-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: broad Fauna validator routing index for shared fauna validation concerns under tools/validators/fauna, including source-role child routing, sensitive occurrence denial, geoprivacy gate posture, source registry linkage, evidence/proof linkage, policy/review/release linkage, correction and rollback linkage, and public-surface denial checks while deferring the per-domain Fauna validator index, Fauna meaning, source-role doctrine, source registry authority, evidence records, policy decisions, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/fauna/README.md
  - ../biodiversity/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - source_role/README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/IDENTITY_MODEL.md
  - ../../../docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../contracts/domains/fauna/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/fauna/
  - ../../../policy/domains/fauna/
  - ../../../policy/sensitivity/fauna/
  - ../../../data/registry/sources/fauna/
  - ../../../data/proofs/fauna/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces a stray one-character file. It does not confirm executable files."
  - "The per-domain Fauna validator authority remains tools/validators/domains/fauna/README.md. This broad tools/validators/fauna/ README is a routing/convenience index for shared Fauna validator lanes that sit outside the per-domain folder shape."
  - "Confirmed child README lane at this path: source_role/. Executable behavior remains NEEDS VERIFICATION."
  - "Fauna sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry detail, steward-controlled records, and reverse-engineerable derivatives are deny-by-default unless geoprivacy, review, policy, evidence, release, correction, and rollback support authorize a public-safe derivative."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, and policy. They do not define Fauna meaning, create SourceDescriptors, create EvidenceBundles, make stewardship decisions, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/fauna

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-fauna--validator--routing-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-deny--by--default-red)
![authority](https://img.shields.io/badge/authority-routing--index-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/fauna/` is the broad Fauna validator routing index for Fauna-specific validator lanes that are useful outside the per-domain folder shape, while the main per-domain Fauna validator index remains `tools/validators/domains/fauna/`.

---

## Purpose

`tools/validators/fauna/` exists to route broad Fauna validation concerns under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do broad Fauna validator lanes preserve source-role posture, source-family boundaries, sensitive-species geoprivacy, occurrence restrictions, evidence/proof linkage, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before Fauna candidates reach catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a navigable validator routing index and deterministic validation outputs from configured child lanes. This folder should not create Fauna truth, taxonomic authority, source descriptors, source-role doctrine, source payloads, EvidenceBundles, geoprivacy transforms, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/fauna/README.md` | **CONFIRMED** | This README replaces a stray one-character file. |
| Per-domain Fauna validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/fauna/README.md` remains the per-domain validator index for occurrence, sensitive-site, geoprivacy, taxon/status, range, migration, mortality, disease, invasive-species, evidence, policy, release, correction, rollback, and public-surface denial checks. |
| Broad child lane `source_role/` | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/fauna/source_role/README.md` checks the proposed posture for canonical `SourceDescriptor.source_role` assignment and anti-collapse. |
| Fauna source registry lane | **CONFIRMED in repo evidence / draft** | `data/registry/sources/fauna/README.md` says Fauna source registry records carry source identity, source family, source role, rights, sensitivity, cadence, authority limits, and release references, but not animal truth. |
| Fauna source-role crosswalk | **CONFIRMED in repo evidence / draft** | `docs/domains/fauna/SOURCE_ROLES.md` maps informal shorthand to the canonical seven-class `source_role` and says SourceDescriptor assignment wins. |
| Executables, schemas, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator implementation, source-role enum enforcement, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Index relationship

KFM now has two Fauna validator index surfaces with different jobs:

| Path | Role | Boundary |
|---|---|---|
| `tools/validators/domains/fauna/` | Per-domain Fauna validator index. | Primary home for domain-scoped Fauna validator routing under the per-domain validator tree. |
| `tools/validators/fauna/` | Broad Fauna validator routing index. | Convenience parent for Fauna validator lanes that are not placed directly under the per-domain tree, currently `source_role/`. |

Do not duplicate authority between these paths. If a validator is domain-scoped and fits the per-domain tree, prefer `tools/validators/domains/fauna/`. If a validator is a broad reusable Fauna helper lane that intentionally sits outside the domain tree, document the reason here and link back to the per-domain index.

[Back to top](#top)

---

## Child lanes

| Child lane | Purpose | Status |
|---|---|---|
| [`source_role/`](source_role/README.md) | Fauna `SourceDescriptor.source_role` assignment, canonical seven-class enum posture, source-family separation, aggregator/context/model/observation anti-collapse, sensitive occurrence source-role handling, source registry, evidence/proof, policy/review/release, correction, rollback, and public-surface denial checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |

Possible future child lanes remain **PROPOSED** until created and verified:

- `geoprivacy/` for Fauna redaction, generalization, gridding, buffering, aggregation, and public-safe derivative checks;
- `sensitive_occurrence/` for exact occurrence, nest, den, roost, hibernacula, spawning, breeding/aggregation, telemetry, and steward-controlled record denial checks;
- `taxon_status/` for taxon identity, legal/conservation status, source-role, and public-surface caveat checks;
- `range_model/` for modeled range, seasonal range, migration, suitability, and model/observation anti-collapse checks;
- `mortality_disease/` for mortality, disease, carcass, outbreak, and sensitive disclosure checks.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad Fauna validator routing index | `tools/validators/fauna/` |
| Broad Fauna child validator lanes | `tools/validators/fauna/*/` |
| Per-domain Fauna validator index | `tools/validators/domains/fauna/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Biodiversity / cross-domain validator context | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/` |
| Fauna domain meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Fauna source-role doctrine/crosswalk | `docs/domains/fauna/SOURCE_ROLES.md`, `docs/domains/fauna/SOURCES.md`, `docs/domains/fauna/SOURCE_FAMILIES.md` |
| SourceDescriptor records | `data/registry/sources/fauna/` or accepted source-registry home |
| Source and Fauna schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/fauna/` |
| Fauna policy and geoprivacy | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| Evidence/proof support | `data/proofs/fauna/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/fauna/`, `tests/validators/domains/fauna/`, `tests/domains/fauna/`, `fixtures/domains/fauna/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists and the `source_role/` child README exists.
- **PROPOSED:** validator code may live here when it checks declared broad Fauna validation invariants and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, child lane inventory, accepted schemas, source registry topology, fixture shape, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Fauna doctrine, taxonomic authority, source-role enum authority, source registry, source payload storage, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, stewardship authority, geoprivacy authority, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/fauna/` include:

- this broad Fauna validator routing README;
- child lanes that intentionally sit outside `tools/validators/domains/fauna/` and have a clear reason to do so;
- source-role, geoprivacy, sensitive-occurrence, range-model, taxon-status, or other broad Fauna validator helpers that delegate domain meaning, source authority, policy, evidence, and release authority to owning roots;
- optional parent runner code that delegates to child validators without redefining their rules;
- synthetic fixture references and test-surface guidance;
- docs that explain broad Fauna validator scope without becoming authoritative Fauna doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/fauna/` | Correct home |
|---|---|
| Fauna domain doctrine and meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Source-role doctrine, enum definition, or crosswalk authority | `docs/domains/fauna/SOURCE_ROLES.md`, `docs/domains/fauna/SOURCES.md`, source schemas, or accepted doctrine/schema homes |
| SourceDescriptor records or admission sidecars | `data/registry/sources/fauna/` or accepted source-registry home |
| Fauna source payloads | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/` |
| Schemas and enums | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/fauna/` |
| Policy and geoprivacy rules | `policy/domains/fauna/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, stewardship decisions, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Broad Fauna validator posture

Fauna validators under this broad index must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, source family, claim family, authority limit, EvidenceRef, EvidenceBundle/proof reference, sensitivity posture, policy posture, review state, release reference, correction path, or rollback target required for its use;
- collapses regulatory, aggregate, observed, modeled, administrative, candidate, or synthetic source roles;
- treats context layers such as habitat, landcover, wetlands, hydrology, soils, infrastructure, ownership, or administrative units as Fauna truth instead of governed join context;
- treats aggregator records as if the aggregator itself decides the role for all underlying records;
- exposes sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry detail, steward-controlled records, or reverse-engineerable derivatives without geoprivacy, review, policy, release, correction, and rollback support;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on source-role-collapsed, geoprivacy-incomplete, evidence-incomplete, or policy-incomplete Fauna records;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, direct model outputs, or incomplete proof closure;
- treats validator output as SourceDescriptor creation, EvidenceBundle creation, PolicyDecision creation, release approval, publication, taxonomic authority, stewardship authority, geoprivacy authority, or public API behavior.

The validator tree must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `FAUNA_VALIDATORS_PASS` | Configured broad Fauna validators passed. |
| `FAUNA_VALIDATORS_FAIL` | One or more configured broad Fauna validators failed. |
| `FAUNA_CHILD_VALIDATOR_MISSING` | Expected broad Fauna child validator lane or runner is absent. |
| `FAUNA_CHILD_VALIDATOR_FAILED` | A child validator reported one or more findings. |
| `FAUNA_SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source-registry pointer is absent. |
| `FAUNA_SOURCE_ROLE_GAP` | Required source-role or authority-limit posture is missing. |
| `FAUNA_CONTEXT_AS_TRUTH_DENIED` | Context layer is treated as Fauna truth. |
| `FAUNA_SENSITIVE_OCCURRENCE_DENIED` | Sensitive occurrence/site detail is unsafe for the requested surface. |
| `FAUNA_GEOPRIVACY_GAP` | Required geoprivacy, redaction, aggregation, or review support is absent. |
| `FAUNA_EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `FAUNA_POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `FAUNA_PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
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
tests/validators/fauna/
├── README.md
├── test_fauna_validator_parent.py
├── source_role/
└── fixtures/
    ├── valid_fauna_validation_bundle/
    ├── missing_source_descriptor/
    ├── source_role_gap/
    ├── context_as_truth_denied/
    ├── sensitive_occurrence_denied/
    ├── geoprivacy_gap/
    ├── policy_or_release_gap/
    └── public_surface_leak_risk/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/fauna
```

```bash
python tools/validators/fauna/run_fauna_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_fauna_validators.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Broad parent delegates to child validators instead of redefining their rules.
- [ ] New Fauna child lanes are placed here only when there is a clear reason not to place them under `tools/validators/domains/fauna/`.
- [ ] Validators read declared SourceDescriptor/source-role schemas, Fauna source docs, source registry records, contracts, and policy rather than defining meaning locally.
- [ ] Source role, source family, claim family, authority limits, sensitivity, rights, evidence, policy, release, correction, and rollback remain visible.
- [ ] Context layers and aggregators do not become Fauna truth by accident.
- [ ] Sensitive occurrence/site detail fails closed unless geoprivacy, review, policy, release, correction, and rollback support exists.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, source-role-collapsed candidates, direct model outputs, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source admission, taxonomic authority, stewardship authority, geoprivacy authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for stray one-character broad Fauna validator parent file. |
| Next smallest safe change | Verify actual broad Fauna parent runner, child lane inventory, source-role script path, accepted schemas, source registry topology, fixtures, report destination, receipt emission, policy enforcement, release linkage, geoprivacy behavior, and CI/runtime wiring before promoting this lane beyond draft. |
