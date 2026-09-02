<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-habitat-readme
title: tools/validators/habitat README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-habitat-steward-plus-ecology-steward-plus-geoprivacy-reviewer-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; habitat-validator-routing-index; habitat; ecology; geoprivacy; sensitive-join; public-safe-geometry; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: broad Habitat validator routing index for Habitat-specific validator lanes under tools/validators/habitat, including Habitat-facing geoprivacy adapters, public-safe geometry checks, suitability and connectivity derivative checks, source-role boundaries, evidence/proof linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring per-domain Habitat validator authority, Habitat meaning, geoprivacy policy parameters, evidence records, receipts, proofs, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/habitat/README.md
  - ../domains/fauna/README.md
  - ../fauna/README.md
  - ../geoprivacy/README.md
  - ../geoprivacy/habitat-fauna/README.md
  - ../geometry/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../biodiversity/README.md
  - fauna-geoprivacy/README.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../contracts/domains/habitat/
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../policy/geoprivacy/
  - ../../../data/quarantine/habitat/over_precise_geometry/README.md
  - ../../../data/registry/sources/habitat/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/habitat/README.md. It does not confirm executable validator code."
  - "tools/validators/domains/habitat/ remains the per-domain Habitat validator index. This README is a broad routing index for Habitat-specific validator lanes that intentionally sit outside the per-domain tree."
  - "Confirmed child README lane at this path: fauna-geoprivacy/. Executable behavior remains NEEDS VERIFICATION."
  - "Habitat sensitivity is often join-induced or derivation-induced. Outputs that reveal sensitive Fauna, Flora, archaeology, stewardship, private-land, infrastructure, or other restricted context must fail closed unless public-safe geoprivacy, review, policy, evidence, release, correction, and rollback support exists."
  - "This README does not include exact coordinates, restricted identifiers, geoprivacy thresholds, grid sizes, generalization radii, geohash precisions, or other reverse-engineering hints."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/habitat

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-habitat--validator--routing-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)
![authority](https://img.shields.io/badge/authority-routing--index-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/habitat/` is the broad Habitat validator routing index for Habitat-specific validator lanes that sit outside the per-domain tree, while the main per-domain Habitat validator index remains `tools/validators/domains/habitat/`.

---

## Purpose

`tools/validators/habitat/` exists to route Habitat validation concerns under the durable `tools/validators/` surface without moving Habitat doctrine, contracts, schemas, policy, evidence, receipts, release decisions, or lifecycle data into a validator folder.

The durable KFM question for this index is:

> Do Habitat validator lanes preserve habitat object-family boundaries, source-role posture, sensitive-join geoprivacy, public-safe geometry, produced-geometry checks, evidence/proof linkage, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before Habitat candidates reach catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a navigable validator routing index and deterministic validation outputs from configured child lanes. This folder should not create Habitat truth, species occurrence truth, ecological-system authority, suitability-model authority, geoprivacy thresholds, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/habitat/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| Per-domain Habitat validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/habitat/README.md` remains the per-domain Habitat validator index. |
| Child lane `fauna-geoprivacy/` | **CONFIRMED README / executable NEEDS VERIFICATION** | Habitat-facing route for Fauna geoprivacy checks; should not duplicate the shared geoprivacy validator lane. |
| Shared geoprivacy parent | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/README.md` is the broad routing index for sensitive-location and public-safe-geometry checks. |
| Shared Habitat-Fauna geoprivacy lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/habitat-fauna/README.md` is the preferred shared cross-domain rule lane. |
| Executables, schemas, fixtures, policy bundles, receipts, report paths, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, registry entry, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Index relationship

KFM currently has multiple Habitat-related validator surfaces with different responsibilities:

| Path | Role | Boundary |
|---|---|---|
| `tools/validators/domains/habitat/` | Per-domain Habitat validator index. | Primary home for domain-scoped Habitat validator routing under the per-domain validator tree. |
| `tools/validators/habitat/` | Broad Habitat validator routing index. | Convenience parent for Habitat-specific child lanes that sit outside the per-domain tree. |
| `tools/validators/habitat/fauna-geoprivacy/` | Habitat-facing Fauna geoprivacy route. | Adapter/routing lane; must not duplicate shared policy or cross-domain geoprivacy authority. |
| `tools/validators/geoprivacy/habitat-fauna/` | Shared Habitat × Fauna geoprivacy lane. | Preferred shared rule lane for sensitive joins, derivation-induced exposure, most-restrictive policy propagation, public-safe geometry, transform receipts, and public-surface leakage checks. |

Do not duplicate authority between these paths. If a validator is domain-scoped and fits the per-domain tree, prefer `tools/validators/domains/habitat/`. If a validator is a broad reusable Habitat helper or adapter that intentionally sits outside the domain tree, document the reason here and link back to the per-domain index.

[Back to top](#top)

---

## Child lanes

| Child lane | Purpose | Status |
|---|---|---|
| [`fauna-geoprivacy/`](fauna-geoprivacy/README.md) | Habitat-facing routing for Fauna geoprivacy checks: sensitive Fauna joins, derivation-induced exposure, public-safe geometry, transform receipt linkage, EvidenceRef/EvidenceBundle closure, release linkage, correction/rollback posture, and public-surface denial. | **CONFIRMED README / executable NEEDS VERIFICATION** |

Possible future child lanes remain **PROPOSED** until created and verified:

- `public-safe-geometry/` for Habitat public-geometry profile checks that are not specific to one neighboring domain;
- `suitability-derivatives/` for suitability, model, uncertainty, training-location reconstruction, and model-as-observation denial checks;
- `connectivity-corridors/` for corridor, endpoint, graph, and connectivity-surface public-safe generalization checks;
- `stewardship-zone/` for stewardship, restoration, private-land, or restricted-management context exposure checks;
- `tile-surface/` for Habitat map tiles, screenshots, labels, popups, and scale/zoom leakage checks;
- `release-readiness/` for release-reference, correction, rollback, and public-surface readiness checks.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad Habitat validator routing index | `tools/validators/habitat/` |
| Habitat child validator lanes outside per-domain tree | `tools/validators/habitat/*/` |
| Per-domain Habitat validator index | `tools/validators/domains/habitat/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Shared geometry validation | `tools/validators/geometry/` |
| Geoprivacy validation | `tools/validators/geoprivacy/` and child lanes |
| Biodiversity / cross-domain validator context | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Habitat domain meaning | `docs/domains/habitat/`, `contracts/domains/habitat/` |
| Habitat schemas | `schemas/contracts/v1/domains/habitat/` or ADR-selected homes |
| Habitat policy rules | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, `policy/geoprivacy/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/habitat/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections, withdrawal | `release/` |
| Lifecycle data and quarantine holds | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/`, `data/catalog/...`, `data/published/...` |
| Tests and fixtures | `tests/validators/habitat/`, `tests/validators/domains/habitat/`, `tests/domains/habitat/`, `fixtures/domains/habitat/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists and the `fauna-geoprivacy/` child README exists.
- **PROPOSED:** validator code may live here when it checks declared broad Habitat validation invariants and writes reports or receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, child lane inventory, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as Habitat doctrine, species-record authority, legal/regulatory authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/habitat/` include:

- this broad Habitat validator routing README;
- child lanes that intentionally sit outside `tools/validators/domains/habitat/` and have a clear reason to do so;
- Habitat-facing adapter checks that delegate shared concerns to `tools/validators/geoprivacy/`, `tools/validators/geometry/`, `tools/validators/cross-domain-joins/`, or other accepted validator homes;
- optional parent runner code that delegates to child validators without redefining their rules;
- checks for source-role discipline, object-family separation, public-safe geometry, sensitive joins, derivative reconstruction risk, release linkage, correction and rollback posture, and public-surface denial;
- synthetic fixture references and test-surface guidance;
- docs that explain broad Habitat validator scope without becoming authoritative Habitat doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/habitat/` | Correct home |
|---|---|
| Habitat domain doctrine and meaning | `docs/domains/habitat/`, `contracts/domains/habitat/` |
| Habitat schemas and enums | `schemas/contracts/v1/domains/habitat/`, accepted schema homes |
| Policy, sensitivity rules, geoprivacy thresholds, grid sizes, radii, or restricted parameters | `policy/...` and steward-gated policy bundles |
| Source descriptors | `data/registry/sources/habitat/` |
| Habitat source payloads or lifecycle data | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/` |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts, aggregation receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices | `release/` |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, stewardship decisions, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Broad Habitat validator posture

Habitat validators under this broad index must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, evidence support, sensitivity posture, rights posture, review state, PolicyDecision, release reference, correction path, or rollback target required for its use;
- collapses habitat patch, habitat class, suitability raster, corridor, connectivity graph, restoration opportunity, stewardship zone, land-cover class, ecological system, regulatory critical-habitat context, or species occurrence into another role;
- treats a modeled suitability surface as a Fauna or Flora occurrence;
- presents a regulatory critical-habitat layer as KFM legal advice or species-presence proof;
- exposes over-precise geometry or reverse-engineerable derivatives tied to sensitive Fauna, Flora, archaeology, stewardship, private-land, infrastructure, or other restricted context;
- lacks a named generalization, redaction, aggregation, suppression, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, screenshots, or answers with Habitat content beyond the approved public-safe derivative;
- imports another domain's truth into a Habitat artifact without preserving ownership, source role, sensitivity, and EvidenceBundle support;
- offers legal, regulatory, emergency, operational wildlife, conservation-compliance, or land-use guidance outside an accepted governed authority path;
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
| `HABITAT_VALIDATORS_PASS` | Configured Habitat validators passed. |
| `HABITAT_VALIDATORS_FAIL` | One or more configured Habitat validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Habitat child validator lane, registry entry, or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `ROUTE_TO_DOMAIN_HABITAT_VALIDATOR` | Candidate should be checked by `tools/validators/domains/habitat/`. |
| `ROUTE_TO_GEOPRIVACY_VALIDATOR` | Candidate should be checked by `tools/validators/geoprivacy/` or a child lane. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `HABITAT_SPECIES_AUTHORITY_COLLAPSE` | Candidate treats Habitat output as Fauna/Flora occurrence or species truth. |
| `MODEL_AS_OBSERVATION_DENIED` | Suitability or model output is presented as observation or species fact. |
| `OVER_PRECISE_GEOMETRY_DENIED` | Geometry is too precise for the sensitivity, evidence, or public tier. |
| `SENSITIVE_JOIN_DENIED` | Habitat join reveals or infers restricted neighboring-domain context. |
| `DERIVATIVE_RECONSTRUCTION_DENIED` | Derivative product can reconstruct a restricted or sensitive location. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required generalized, redacted, aggregated, suppressed, or withheld geometry is absent. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent or unresolved. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Map, tile, popup, export, search, graph, embedding, Focus Mode, screenshot, or AI surface leaks protected context. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/habitat/
├── README.md
├── fauna-geoprivacy/
│   └── README.md
├── validate_habitat.py                  # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

The executable, if added, should delegate to child validators and shared validator homes rather than copy policy rules locally. The repo-wide validator orchestrator should remain the entry point if registry wiring is adopted.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at the requested path.
- [x] It states the relationship between `tools/validators/habitat/`, `tools/validators/domains/habitat/`, and `tools/validators/geoprivacy/habitat-fauna/`.
- [x] It marks the parent as a routing index, not domain authority, policy authority, evidence authority, or release authority.
- [x] It lists the confirmed `fauna-geoprivacy/` child README and keeps executable behavior as **NEEDS VERIFICATION**.
- [x] It preserves cite-or-abstain, fail-closed, deny-by-default, public-safe geometry, EvidenceBundle, receipt, release, correction, and rollback boundaries.
- [x] It avoids exact coordinates, restricted identifiers, policy thresholds, grid sizes, generalization radii, geohash precisions, and reconstruction hints.

Future implementation is not complete until:

- [ ] Validator registry wiring is verified.
- [ ] Exact executable names and interfaces are accepted.
- [ ] Valid and invalid fixtures cover missing evidence, source-role collapse, over-precise geometry, sensitive joins, derivative reconstruction, missing receipts, release gaps, and public-surface leakage.
- [ ] CI or `tools/validate_all.py` invokes the relevant Habitat validators in deterministic order.
- [ ] Validation outputs write reports or receipts only to accepted roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with broad Habitat validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
