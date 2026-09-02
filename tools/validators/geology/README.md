<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geology-readme
title: tools/validators/geology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geology-steward-plus-natural-resources-steward-plus-sensitivity-reviewer-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geology-validator-parent; broad-geology-routing-index; natural-resources; subsurface; resource-class; public-safe-geometry; borehole-rights; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: broad Geology validator routing index for shared Geology validator lanes under tools/validators/geology, including borehole-rights, public-safe-geometry, resource-class anti-collapse, source-role separation, exact-location sensitivity, rights/sensitivity posture, evidence/proof linkage, policy/review/release linkage, correction and rollback linkage, and public-surface denial checks while deferring the per-domain Geology validator index, Geology meaning, source registry authority, sensitivity registry authority, evidence records, policy decisions, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/geology/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../facilities/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../evidence_bundle/README.md
  - borehole_rights/README.md
  - public_safe_geometry/README.md
  - resource_class/README.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/geology/POLICY.md
  - ../../../docs/domains/geology/SENSITIVITY.md
  - ../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../contracts/domains/geology/MineralOccurrence.md
  - ../../../contracts/domains/geology/ResourceDeposit.md
  - ../../../contracts/domains/geology/ResourceEstimate.md
  - ../../../contracts/domains/geology/BoreholeReference.md
  - ../../../contracts/domains/geology/WellLogReference.md
  - ../../../packages/domains/geology/geometry/README.md
  - ../../../data/registry/sources/geology/
  - ../../../data/registry/sensitivity/geology/README.md
  - ../../../data/proofs/geology/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../tests/domains/geology/claim-class/README.md
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "The per-domain Geology validator authority remains tools/validators/domains/geology/README.md. This broad tools/validators/geology/ README is a routing/convenience index for Geology validator lanes that sit outside the per-domain folder shape."
  - "Confirmed child README lanes at this path: borehole_rights/, public_safe_geometry/, and resource_class/. Executable behavior remains NEEDS VERIFICATION."
  - "Geology validator evidence says exact borehole, core, well-log, private-well, sample, and extraction-targetable resource locations are sensitive by default and require public-safe transforms, review, evidence, policy, release, correction, and rollback support before public exposure."
  - "Resource-class evidence says MineralOccurrence, ResourceDeposit, ResourceEstimate, permit, production, reserve, extraction, reclamation, ownership, lease, title, and hazard claims must not collapse."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, and policy. They do not define Geology meaning, create SourceDescriptors, create EvidenceBundles, decide policy, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-geology--validator--routing-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-exact--subsurface--deny--default-critical)
![authority](https://img.shields.io/badge/authority-routing--index-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geology/` is the broad Geology validator routing index for Geology-specific validator lanes that are useful outside the per-domain folder shape, while the main per-domain Geology validator index remains `tools/validators/domains/geology/`.

---

## Purpose

`tools/validators/geology/` exists to route broad Geology and Natural Resources validation concerns under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do broad Geology validator lanes preserve source-role posture, source-family boundaries, exact-location sensitivity, borehole and well-log rights posture, public-safe geometry posture, resource claim class, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before Geology candidates reach catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a navigable validator routing index and deterministic validation outputs from configured child lanes. This folder should not create Geology truth, resource truth, reserve truth, mineral-rights truth, title truth, lease truth, permit truth, extraction guidance, SourceDescriptors, EvidenceBundles, geometry transforms, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geology/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Per-domain Geology validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/geology/README.md` remains the per-domain validator index for geologic maps, stratigraphy, lithology, structures, subsurface observations, natural resources, evidence, policy, release, correction, rollback, and public-surface denial checks. |
| Broad child lane `borehole_rights/` | **CONFIRMED README / executable NEEDS VERIFICATION** | Checks borehole, well-log, core, sample, private-well, and subsurface-source rights and exposure posture. |
| Broad child lane `public_safe_geometry/` | **CONFIRMED README / executable NEEDS VERIFICATION** | Checks exact/internal geometry separation, public-safe geometry roles, transform receipts, sensitivity, evidence, policy, release, correction, and rollback posture. |
| Broad child lane `resource_class/` | **CONFIRMED README / executable NEEDS VERIFICATION** | Checks MineralOccurrence, ResourceDeposit, ResourceEstimate, permit, production, reserve, extraction, reclamation, ownership, lease, title, and hazard anti-collapse. |
| Executables, schemas, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator implementation, source-role enum enforcement, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Index relationship

KFM now has two Geology validator index surfaces with different jobs:

| Path | Role | Boundary |
|---|---|---|
| `tools/validators/domains/geology/` | Per-domain Geology validator index. | Primary home for domain-scoped Geology validator routing under the per-domain validator tree. |
| `tools/validators/geology/` | Broad Geology validator routing index. | Convenience parent for Geology validator lanes that are not placed directly under the per-domain tree, currently `borehole_rights/`, `public_safe_geometry/`, and `resource_class/`. |

Do not duplicate authority between these paths. If a validator is domain-scoped and fits the per-domain tree, prefer `tools/validators/domains/geology/`. If a validator is a broad reusable Geology helper lane that intentionally sits outside the domain tree, document the reason here and link back to the per-domain index.

[Back to top](#top)

---

## Child lanes

| Child lane | Purpose | Status |
|---|---|---|
| [`borehole_rights/`](borehole_rights/README.md) | Borehole, well-log, core, sample, private-well, geophysics, geochemistry, and subsurface-source rights posture, exact-location sensitivity, resource-targeting exposure, ownership/lease/permit/title anti-collapse, evidence, policy, release, correction, rollback, and public-surface denial checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`public_safe_geometry/`](public_safe_geometry/README.md) | Exact/internal geometry separation, public-safe geometry role checks, CRS/topology/uncertainty posture, redaction/generalization/aggregation receipt checks, sensitive subsurface/resource-location denial, evidence, policy, release, correction, rollback, and public-surface denial checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`resource_class/`](resource_class/README.md) | MineralOccurrence, ResourceDeposit, ResourceEstimate, permit, production, reserve, extraction-site, reclamation, ownership, lease, title, hazard, public summary, graph, map, export, and AI wording anti-collapse checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |

Possible future child lanes remain **PROPOSED** until created and verified:

- `source_role/` for Geology source-role/source-family/source-authority anti-collapse;
- `stratigraphy/` for stratigraphic unit identity, correlation, geologic age, and cross-section evidence posture;
- `geologic_map/` for bedrock/surficial map polygons, structure/fault layers, and public-safe cartographic release;
- `hydrostratigraphy/` for Geology ↔ Hydrology joins without re-owning water observation, groundwater, or regulatory flood truth;
- `geochemistry/` for sample/assay/geochemical observation source-role, units, sensitivity, and resource-targeting exposure checks;
- `geophysics/` for interpreted vs observed geophysical data, survey-line exposure, and model/observation anti-collapse.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad Geology validator routing index | `tools/validators/geology/` |
| Broad Geology child validator lanes | `tools/validators/geology/*/` |
| Per-domain Geology validator index | `tools/validators/domains/geology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain validator context | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Geology domain meaning | `docs/domains/geology/`, `contracts/domains/geology/` |
| Natural Resources doctrine | `docs/domains/geology/sublanes/natural_resources.md` |
| Geology source registry | `data/registry/sources/geology/` or accepted source-registry home |
| Geology sensitivity registry | `data/registry/sensitivity/geology/` or accepted sensitivity-registry home |
| Geology and source schemas | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/source/` |
| Geology policy and geoprivacy | `policy/domains/geology/`, `policy/sensitivity/geology/`, `policy/geoprivacy/`, or accepted policy homes |
| Evidence/proof support | `data/proofs/geology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geology/`, `tests/validators/domains/geology/`, `tests/domains/geology/`, `fixtures/domains/geology/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists and the `borehole_rights/`, `public_safe_geometry/`, and `resource_class/` child READMEs exist.
- **PROPOSED:** validator code may live here when it checks declared broad Geology validation invariants and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, child lane inventory, accepted schemas, source registry topology, sensitivity-tier binding, claim-class vocabulary, geometry-role vocabulary, fixture shape, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Geology doctrine, resource/reserve authority, source registry, source payload storage, schema home, proof storage, receipt storage, policy home, release record store, mineral-rights authority, title authority, lease authority, permit authority, production authority, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geology/` include:

- this broad Geology validator routing README;
- child lanes that intentionally sit outside `tools/validators/domains/geology/` and have a clear reason to do so;
- borehole-rights, public-safe-geometry, resource-class, source-role, stratigraphy, geochemistry, geophysics, hydrostratigraphy, or other broad Geology validator helpers that delegate domain meaning, source authority, sensitivity, policy, evidence, and release authority to owning roots;
- optional parent runner code that delegates to child validators without redefining their rules;
- synthetic fixture references and test-surface guidance;
- docs that explain broad Geology validator scope without becoming authoritative Geology doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geology/` | Correct home |
|---|---|
| Geology domain doctrine and meaning | `docs/domains/geology/`, `contracts/domains/geology/` |
| Resource/reserve classification schemes and schemas | `schemas/contracts/v1/domains/geology/`, contract docs, or accepted schema homes |
| SourceDescriptor records or source registry records | `data/registry/sources/geology/` |
| Sensitivity registry records or policy bundles | `data/registry/sensitivity/geology/`, `policy/` |
| Geology source payloads, exact geometry, well logs, private-well data, samples, geochemistry, geophysics, or resource datasets | dedicated `data/` lifecycle roots with quarantine/review as needed |
| Schemas and enums | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/receipts/` |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, extraction guidance, legal/title/lease/permit determinations, engineering recommendations, investment advice, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Broad Geology validator posture

Geology validators under this broad index must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, source family, authority limit, claim class, sensitivity tier, geometry role, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- exposes exact borehole, core, sample, well-log, private-well, geochemistry, sensitive-resource, extraction-targetable, or rights-restricted geometry/content without approved public-safe transform and receipt support;
- collapses MineralOccurrence, ResourceDeposit, ResourceEstimate, permit, production, reserve, extraction, reclamation, ownership, lease, title, or hazard claims;
- treats public display geometry as exact source geometry, reserve estimate, resource truth, drilling guidance, ownership/title truth, or proof of the underlying claim;
- treats source admission, stable identifiers, public availability, generalized map polygons, model outputs, summaries, graph edges, map labels, or AI answers as source evidence, policy approval, release approval, or Geology truth;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on rights-incomplete, sensitivity-incomplete, public-safe-geometry-incomplete, or claim-class-collapsed Geology candidates;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, direct model outputs, exact sensitive geometry, unsupported reserve language, or incomplete proof closure;
- treats validator output as SourceDescriptor creation, EvidenceBundle creation, PolicyDecision creation, RedactionReceipt creation, release approval, publication, public API behavior, or AI answer authority.

The validator tree must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `GEOLOGY_VALIDATORS_PASS` | Configured broad Geology validators passed. |
| `GEOLOGY_VALIDATORS_FAIL` | One or more configured broad Geology validators failed. |
| `GEOLOGY_CHILD_VALIDATOR_MISSING` | Expected broad Geology child validator lane or runner is absent. |
| `GEOLOGY_CHILD_VALIDATOR_FAILED` | A child validator reported one or more findings. |
| `GEOLOGY_SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source-registry pointer is absent. |
| `GEOLOGY_SOURCE_ROLE_GAP` | Required source-role or authority-limit posture is missing. |
| `GEOLOGY_SENSITIVITY_TIER_MISSING` | Required sensitivity tier or public-use posture is absent. |
| `GEOLOGY_EXACT_LOCATION_DENIED` | Exact sensitive subsurface/resource geometry is unsafe for the requested surface. |
| `GEOLOGY_PUBLIC_SAFE_GEOMETRY_GAP` | Required public-safe transform, geometry role, or transform receipt is absent. |
| `GEOLOGY_RESOURCE_CLASS_GAP` | Required resource claim class is missing or unsupported. |
| `GEOLOGY_RESOURCE_CLASS_COLLAPSE` | Resource claim classes are collapsed. |
| `GEOLOGY_RIGHTS_GAP` | Rights, license, attribution, redistribution, access, or derivative-use posture is incomplete. |
| `GEOLOGY_EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `GEOLOGY_POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `GEOLOGY_PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, source admission, evidence closure, transform receipt, classification review, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/geology/
├── README.md
├── test_geology_validator_parent.py
├── borehole_rights/
├── public_safe_geometry/
├── resource_class/
└── fixtures/
    ├── valid_public_safe_geology_bundle/
    ├── missing_source_descriptor/
    ├── exact_location_denied/
    ├── missing_transform_receipt/
    ├── resource_class_collapse/
    ├── unsupported_reserve_claim/
    ├── rights_gap/
    ├── policy_or_release_gap/
    └── public_surface_leak_risk/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geology
```

```bash
python tools/validators/geology/run_geology_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_geology_validators.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Broad parent delegates to child validators instead of redefining their rules.
- [ ] New Geology child lanes are placed here only when there is a clear reason not to place them under `tools/validators/domains/geology/`.
- [ ] Validators read declared Geology contracts, schemas, source descriptors, source-role rules, sensitivity registry records, and policy rather than defining meaning locally.
- [ ] Borehole/well-log rights, public-safe geometry, resource claim class, source role, sensitivity, rights, evidence, policy, release, correction, and rollback remain visible.
- [ ] Exact sensitive subsurface/resource geometry fails closed unless public-safe transform, receipt, review, policy, release, correction, and rollback support exists.
- [ ] Resource claim classes do not collapse in summaries, catalog records, graph edges, map labels, export rows, Evidence Drawer text, or AI answers.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, rights-incomplete candidates, exact sensitive geometry, source-role-collapsed candidates, direct model outputs, unsupported reserve language, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source admission, resource/reserve certification, geometry authority, mineral-rights authority, title authority, lease authority, permit authority, production authority, extraction guidance, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty broad Geology validator parent file. |
| Next smallest safe change | Verify actual broad Geology parent runner, child lane inventory, borehole-rights/public-safe-geometry/resource-class scripts, accepted schemas, source registry topology, sensitivity-tier binding, fixtures, report destination, receipt emission, policy enforcement, release linkage, public summary/AI wording behavior, and CI/runtime wiring before promoting this lane beyond draft. |
