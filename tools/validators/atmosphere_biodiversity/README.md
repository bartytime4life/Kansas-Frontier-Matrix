<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-atmosphere-biodiversity-readme
title: tools/validators/atmosphere_biodiversity README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-atmosphere-steward-plus-fauna-steward-plus-flora-steward-plus-habitat-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; cross-domain-validator; atmosphere-biodiversity
owning_root: tools/
responsibility: proposed cross-domain validator lane for Atmosphere/Air evidence cited by Fauna, Flora, and Habitat biodiversity claims, including ownership, source-role, evidence, sensitivity, freshness, lifecycle, and release-boundary checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../docs/domains/atmosphere/CROSS_LANE_RELATIONS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/architecture/ecology-cross-domain.md
  - ../../../docs/domains/fauna/
  - ../../../docs/domains/flora/
  - ../../../docs/domains/habitat/
  - ../../../contracts/domains/atmosphere/
  - ../../../contracts/domains/fauna/
  - ../../../contracts/domains/flora/
  - ../../../contracts/domains/habitat/
  - ../../../policy/domains/atmosphere/
  - ../../../policy/domains/fauna/
  - ../../../policy/domains/flora/
  - ../../../policy/domains/habitat/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed cross-domain validator lane. It does not confirm executable files."
  - "Atmosphere/Air owns atmospheric context. Fauna, Flora, and Habitat own biodiversity atoms and interpretations. Validators must not collapse those responsibilities."
  - "Ecology is cross-domain composition in KFM, not a separate domain root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/atmosphere_biodiversity

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-atmosphere--biodiversity--validators-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/atmosphere_biodiversity/` is the proposed cross-domain validator lane for biodiversity-facing products that cite Atmosphere/Air evidence: phenology, smoke, fire-weather, drought stress, climate context, habitat suitability, range context, occurrence context, evidence support, source-role separation, and public-release boundaries.

---

## Purpose

`tools/validators/atmosphere_biodiversity/` exists for validator logic that is genuinely cross-domain between Atmosphere/Air and the biodiversity-owning lanes: Fauna, Flora, and Habitat.

The durable KFM question for this lane is:

> Does a biodiversity-facing candidate cite Atmosphere/Air evidence without re-owning atmospheric truth, collapsing source roles, or skipping evidence, lifecycle, correction, policy, and release gates?

The answer should be a deterministic validation result. It should not create atmospheric observations, taxon records, occurrence records, habitat objects, EvidenceBundles, policy decisions, release decisions, or map/API products.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/atmosphere_biodiversity/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Atmosphere/Biodiversity edge | **CONFIRMED in repo evidence / draft** | Atmosphere cross-lane docs list biodiversity domains as consumers of phenology, smoke, fire, and drought-stress context while preserving ownership, source role, sensitivity, and EvidenceBundle support. |
| Ecology/biodiversity placement | **CONFIRMED in repo evidence / draft** | Ecology is documented as cross-domain composition, not a separate KFM domain root. |
| Contract/schema paths | **PROPOSED / NEEDS VERIFICATION** | Domain-specific schema and contract homes require path verification before implementation claims. |
| Policy and release wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove policy bundles, source descriptors, release gates, or CI are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Cross-domain Atmosphere/Biodiversity validator entrypoints | `tools/validators/atmosphere_biodiversity/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Air domain meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Fauna domain meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Flora domain meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| Habitat domain meaning | `docs/domains/habitat/`, `contracts/domains/habitat/` |
| Ecology cross-domain doctrine | `docs/architecture/ecology-cross-domain.md` |
| Domain schemas | `schemas/contracts/v1/domains/<domain>/` or accepted schema homes |
| Domain policy rules | `policy/domains/<domain>/` or accepted policy homes |
| EvidenceBundles and receipts | `data/proofs/evidence_bundle/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/validators/atmosphere_biodiversity/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it validates a cross-lane invariant and reads declared contracts, schemas, policy, and source descriptors.
- **NEEDS VERIFICATION:** exact executable names, schema homes, fixtures, policy bundles, source descriptors, and CI wiring.
- **DENY:** using this folder as a domain contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, biodiversity domain root, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/atmosphere_biodiversity/` include checks that:

- preserve Atmosphere/Air ownership of weather, smoke, AOD, climate, forecast, and advisory context evidence;
- preserve Fauna ownership of animal taxon, occurrence, range, movement, mortality, and disease records;
- preserve Flora ownership of plant taxon, plant occurrence, specimen, and vegetation-community records;
- preserve Habitat ownership of habitat patch, ecological system, restoration, quality, and connectivity records;
- prevent modeled or aggregate atmospheric context from being presented as observed biodiversity fact;
- require SourceDescriptor role, authority, rights, sensitivity, cadence, and freshness posture for cited Atmosphere/Air evidence;
- require EvidenceRef or EvidenceBundle support for public-bound biodiversity claims;
- require appropriate review or transformation support where biodiversity sensitivity is material;
- propagate Atmosphere/Air correction or stale-state signals into dependent biodiversity products;
- keep ecology/biodiversity composition from becoming a new domain root.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/atmosphere_biodiversity/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere, Fauna, Flora, or Habitat contracts | `contracts/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| Lifecycle data | dedicated `data/` lifecycle roots |
| EvidenceBundles or receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Connectors or pipelines | `connectors/`, `pipelines/` |
| Ecology or biodiversity as a new domain root | not allowed without ADR; ecology is cross-domain composition |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `ATM_BIO_VALIDATION_PASS` | Configured Atmosphere/Biodiversity checks passed. |
| `ATM_BIO_VALIDATION_FAIL` | Configured checks failed. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses modeled, observed, aggregate, regulatory, candidate, or synthetic roles. |
| `ATMOSPHERE_OWNERSHIP_CONFLICT` | Biodiversity candidate appears to redefine or re-own Atmosphere/Air evidence. |
| `BIODIVERSITY_OWNERSHIP_CONFLICT` | Atmospheric context is being used to claim unsupported Fauna, Flora, or Habitat truth. |
| `ECOLOGY_DOMAIN_COLLAPSE` | Candidate treats ecology/biodiversity composition as a new domain root. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SENSITIVITY_REVIEW_REQUIRED` | Public-bound output requires review or transformation support. |
| `FRESHNESS_OR_CORRECTION_REQUIRED` | Stale, superseded, corrected, or unversioned atmospheric evidence requires action. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/atmosphere_biodiversity/
├── README.md
├── test_atmosphere_biodiversity_validators.py
└── fixtures/
    ├── valid_generalized_phenology_context/
    ├── modeled_smoke_as_species_impact_denied/
    ├── climate_normal_as_occurrence_truth_denied/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── sensitive_biodiversity_without_review_denied/
    ├── stale_atmosphere_source_abstain/
    └── ecology_domain_root_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/atmosphere_biodiversity
```

> [!NOTE]
> This is a proposed interface, not proof that the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] Atmosphere/Air, Fauna, Flora, and Habitat ownership boundaries are preserved.
- [ ] Source-role and knowledge-character fields are explicit.
- [ ] Modeled, observed, aggregate, regulatory, candidate, and synthetic records remain distinct.
- [ ] Public-bound biodiversity products require EvidenceRef or EvidenceBundle support.
- [ ] Sensitive biodiversity outputs route through review, transformation, or denial where required.
- [ ] Corrections and stale-state signals propagate to dependent biodiversity products.
- [ ] Ecology is kept as cross-domain composition, not a new domain root.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify contracts, schemas, policy bundles, source descriptors, fixtures, validator entrypoints, and CI wiring before promoting this lane beyond draft. |
