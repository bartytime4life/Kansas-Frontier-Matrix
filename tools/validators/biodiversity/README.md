<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-biodiversity-readme
title: tools/validators/biodiversity README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-fauna-steward-plus-flora-steward-plus-habitat-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; biodiversity-validator-parent; cross-domain-composition; geoprivacy-aware
owning_root: tools/
responsibility: proposed parent boundary and index for validators that check biodiversity/ecology-style cross-domain composition across Fauna, Flora, Habitat, and cited supporting lanes without creating a new biodiversity or ecology authority root
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../atmosphere_biodiversity/README.md
  - ../../../docs/architecture/ecology-cross-domain.md
  - ../../../docs/domains/fauna/
  - ../../../docs/domains/flora/
  - ../../../docs/domains/habitat/
  - ../../../docs/domains/atmosphere/
  - ../../../docs/domains/hydrology/
  - ../../../docs/domains/soil/
  - ../../../contracts/domains/fauna/
  - ../../../contracts/domains/flora/
  - ../../../contracts/domains/habitat/
  - ../../../policy/domains/fauna/
  - ../../../policy/domains/flora/
  - ../../../policy/domains/habitat/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed biodiversity validator parent lane. It does not confirm executable files."
  - "KFM ecology/biodiversity composition is cross-domain. Fauna, Flora, and Habitat retain atomic ownership; validators must not create a new biodiversity or ecology domain root."
  - "Validators enforce declared contracts, schemas, and policy. They do not define taxonomic authority, create EvidenceBundles, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/biodiversity

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-biodiversity--validators-informational)
![composition](https://img.shields.io/badge/composition-cross--domain-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/biodiversity/` is the proposed parent validator lane for biodiversity/ecology-style cross-domain composition checks across Fauna, Flora, Habitat, and cited supporting lanes. It is not a new biodiversity domain root.

---

## Purpose

`tools/validators/biodiversity/` exists to hold parent-level validator guidance for biodiversity products that compose evidence from multiple owning domains.

The durable KFM question for this lane is:

> Does a biodiversity-facing candidate preserve atomic ownership, evidence support, sensitivity posture, source-role separation, lifecycle boundaries, and release readiness across all contributing lanes?

The answer should be a deterministic validation result. It should not create taxon truth, occurrence truth, habitat truth, EvidenceBundles, policy decisions, release decisions, or map/API products.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/biodiversity/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Biodiversity validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Ecology/biodiversity placement | **CONFIRMED in repo evidence / draft** | Ecology is documented as cross-domain composition, not a separate KFM domain root. |
| Atomic ownership | **CONFIRMED in repo evidence / draft** | Fauna, Flora, Habitat, and other contributing lanes retain ownership of their atoms. |
| Child validator lanes | **PARTIAL / NEEDS VERIFICATION** | `atmosphere_biodiversity/` is documented; other cross-lane validators may be added later. |
| Policy and release wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove policy bundles, source descriptors, release gates, or CI are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Biodiversity validator parent/index | `tools/validators/biodiversity/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Biodiversity validator | `tools/validators/atmosphere_biodiversity/` |
| Ecology cross-domain doctrine | `docs/architecture/ecology-cross-domain.md` |
| Fauna domain meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Flora domain meaning | `docs/domains/flora/`, `contracts/domains/flora/` |
| Habitat domain meaning | `docs/domains/habitat/`, `contracts/domains/habitat/` |
| Supporting-domain meaning | owning docs/contracts lanes, such as Atmosphere, Hydrology, Soil, Hazards, Agriculture, and Geology |
| Domain schemas | `schemas/contracts/v1/domains/<domain>/` or accepted schema homes |
| Domain policy rules | `policy/domains/<domain>/` or accepted policy homes |
| EvidenceBundles and receipts | `data/proofs/evidence_bundle/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/validators/biodiversity/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** parent/index validator code may live here only when it checks cross-domain composition invariants and delegates domain-specific truth to owning lanes.
- **NEEDS VERIFICATION:** exact executable names, child lanes, schema homes, fixtures, policy bundles, source descriptors, and CI wiring.
- **DENY:** using this folder as a biodiversity domain root, ecology domain root, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, or public runtime surface.

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| `../atmosphere_biodiversity/` | Do biodiversity-facing products cite Atmosphere/Air evidence without collapsing ownership, source role, evidence, sensitivity, freshness, or release boundaries? | README confirmed; executable proposed. |

Future child lanes should be named for cross-domain invariants, not for a new biodiversity domain. Examples may include Fauna × Habitat, Flora × Habitat, Flora × Soil, Fauna × Hydrology, or Habitat × Hazards if supported by doctrine and fixtures.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/biodiversity/` include checks that:

- preserve Fauna, Flora, and Habitat atomic ownership;
- reject creation of a separate ecology or biodiversity domain root;
- require EvidenceRef or EvidenceBundle support for derived biodiversity products;
- require SourceDescriptor references for contributing sources;
- preserve source-role and knowledge-character fields across joins;
- require appropriate review or transformation support where biodiversity sensitivity is material;
- check that derived richness, suitability, connectivity, invasive-monitoring, or habitat-quality products trace back to contributing owning lanes;
- check release-readiness references, rollback support, and correction propagation for public-bound products;
- enforce `ABSTAIN`, `DENY`, `NARROWED`, or `BOUNDED` behavior for governed-AI surfaces when evidence or policy is insufficient.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/biodiversity/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Fauna, Flora, or Habitat contracts | `contracts/domains/<domain>/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| Lifecycle data | dedicated `data/` lifecycle roots |
| EvidenceBundles or receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Connectors or pipelines | `connectors/`, `pipelines/` |
| New `ecology` or `biodiversity` domain data roots | not allowed without ADR; ecology is cross-domain composition |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `BIODIVERSITY_VALIDATION_PASS` | Configured biodiversity composition checks passed. |
| `BIODIVERSITY_VALIDATION_FAIL` | Configured checks failed. |
| `OWNERSHIP_COLLAPSE` | Candidate collapses Fauna, Flora, Habitat, or supporting-domain ownership. |
| `ECOLOGY_DOMAIN_COLLAPSE` | Candidate treats ecology/biodiversity composition as a new domain root. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source roles across joined evidence. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SENSITIVITY_REVIEW_REQUIRED` | Public-bound output requires review or transformation support. |
| `REDACTION_RECEIPT_MISSING` | Required transformation support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release support pointer is absent. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/biodiversity/
├── README.md
├── test_biodiversity_validator_index.py
└── fixtures/
    ├── valid_species_richness_composition/
    ├── missing_evidence_ref/
    ├── ownership_collapse/
    ├── ecology_domain_root_denied/
    ├── source_role_collapse/
    └── missing_release_reference/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/biodiversity
```

> [!NOTE]
> This is a proposed validation surface, not proof that `tests/validators/biodiversity/` exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator preserves Fauna, Flora, and Habitat ownership boundaries.
- [ ] Validator keeps ecology/biodiversity as cross-domain composition, not a new domain root.
- [ ] Validator reads declared contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] EvidenceRef or EvidenceBundle support is required for public-bound claims.
- [ ] Sensitivity, transformation, release, rollback, and correction support are checked where required.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify child lanes, contracts, schemas, policy bundles, source descriptors, fixtures, validator entrypoints, and CI wiring before promoting this parent lane beyond draft. |
