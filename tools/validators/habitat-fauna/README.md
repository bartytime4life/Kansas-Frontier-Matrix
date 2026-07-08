<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-habitat-fauna-readme
title: tools/validators/habitat-fauna README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-habitat-steward-plus-fauna-steward-plus-geoprivacy-reviewer-plus-biodiversity-steward-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; habitat-fauna-validator; cross-domain-validator; biodiversity; sensitive-join; habitat-suitability; fauna-occurrence; source-role-aware; geoprivacy-routed; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed broad Habitat-Fauna validator lane for checking cross-domain Habitat and Fauna joins, Habitat suitability/patch/corridor products derived from Fauna context, species-record non-ownership, model/observation/regulatory separation, source-role and source-family separation, sensitive-join routing, geoprivacy handoff, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring Habitat meaning, Fauna meaning, geoprivacy policy parameters, source registry authority, evidence records, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../biodiversity/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../domains/habitat/README.md
  - ../domains/fauna/README.md
  - ../fauna/README.md
  - ../geoprivacy/README.md
  - ../geoprivacy/habitat-fauna/README.md
  - ../geometry/README.md
  - ../geoprivacy_transform/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../evidence_bundle/README.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../docs/domains/habitat/HABITAT_DOMAIN_MODEL.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/domains/habitat/sublanes/critical-habitat.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/CROSS_LANE_RELATIONS.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../contracts/domains/habitat/
  - ../../../contracts/domains/fauna/
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../schemas/contracts/v1/domains/fauna/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/domains/habitat/
  - ../../../policy/domains/fauna/
  - ../../../policy/sensitivity/habitat/
  - ../../../policy/sensitivity/fauna/
  - ../../../policy/geoprivacy/
  - ../../../data/registry/sources/habitat/
  - ../../../data/registry/sources/fauna/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "This broad Habitat-Fauna lane is not the geoprivacy-specific lane. Sensitive-location and public-safe-geometry details route to tools/validators/geoprivacy/habitat-fauna/."
  - "Habitat validator evidence says Habitat owns landscape, patches, suitability, connectivity, restoration opportunity, and stewardship-zone products, but not Fauna occurrence truth."
  - "Fauna validator evidence says sensitive occurrences, nests, dens, roosts, hibernacula, spawning/breeding/aggregation sites, telemetry detail, steward-controlled records, and reverse-engineerable derivatives are deny-by-default without governed support."
  - "Habitat-Fauna geoprivacy evidence says Habitat outputs joined to, derived from, or capable of reconstructing sensitive Fauna locations fail closed unless a public-safe geoprivacy path is fully supported."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, and policy. They do not define Habitat meaning, Fauna meaning, create EvidenceBundles, decide policy, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/habitat-fauna

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-habitat--fauna--validator-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-sensitive--joins--fail--closed-critical)
![handoff](https://img.shields.io/badge/geoprivacy-routed-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/habitat-fauna/` is the proposed broad cross-domain validator lane for Habitat × Fauna joins, models, summaries, map layers, graph projections, exports, and AI-facing outputs, while sensitive-location handling routes to `tools/validators/geoprivacy/habitat-fauna/`.

---

## Purpose

`tools/validators/habitat-fauna/` exists for cross-domain Habitat × Fauna validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a Habitat × Fauna candidate preserve Habitat/Fauna ownership boundaries, source-role separation, species-record non-ownership, model/observation/regulatory separation, sensitive-join routing, geoprivacy handoff, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Habitat truth, Fauna occurrence truth, taxonomic authority, Habitat suitability truth, sensitive-location transforms, RedactionReceipts, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/habitat-fauna/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Habitat validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Habitat index says Habitat owns landscape, patches, suitability, connectivity, restoration opportunity, and stewardship-zone products, but not Fauna occurrence truth. |
| Fauna validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Fauna index says broad Fauna validation preserves source role, sensitive-species geoprivacy, occurrence restrictions, evidence, policy, release, correction, rollback, and public-surface denial. |
| Habitat-Fauna geoprivacy lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/habitat-fauna/README.md` handles sensitive-location and public-safe geometry concerns for Habitat × Fauna products. |
| Executables, schemas, fixtures, policy bundles, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Broad Habitat-Fauna cross-domain validation | `tools/validators/habitat-fauna/` |
| Habitat-Fauna geoprivacy and sensitive-location validation | `tools/validators/geoprivacy/habitat-fauna/` |
| Shared geoprivacy routing | `tools/validators/geoprivacy/` |
| Shared geoprivacy-transform validation | `tools/validators/geoprivacy_transform/` |
| Shared geometry carrier validation | `tools/validators/geometry/` |
| Habitat validator index | `tools/validators/domains/habitat/` |
| Fauna validator indexes | `tools/validators/fauna/`, `tools/validators/domains/fauna/` |
| Biodiversity and cross-domain validation | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Habitat/Fauna domain meaning | `docs/domains/habitat/`, `docs/domains/fauna/`, `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Source descriptors | `data/registry/sources/habitat/`, `data/registry/sources/fauna/` |
| Policy, proofs, receipts, release | `policy/`, `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where broad Habitat × Fauna validation may be documented or implemented after verification.

[Back to top](#top)

---

## Geoprivacy handoff

This lane may detect that a Habitat × Fauna candidate has sensitive-location implications, but it must not decide the transform or public geometry locally.

| If the issue is... | Route to... | Reason |
|---|---|---|
| Habitat output joined to sensitive Fauna occurrence/site | `tools/validators/geoprivacy/habitat-fauna/` | Sensitive-location exposure requires geoprivacy-specific checks. |
| Public-safe geometry, redaction, generalization, aggregation, gridding, buffering, or suppression | `tools/validators/geoprivacy_transform/` and `tools/validators/geometry/` | Transform readiness and geometry carrier checks are shared validator concerns. |
| Taxon/source-role/source-family posture | `tools/validators/fauna/` and `tools/validators/fauna/source_role/` | Fauna source-role authority must remain visible. |
| Habitat suitability, connectivity, corridor, restoration, land-cover, or ecoregion posture | `tools/validators/domains/habitat/` | Habitat owns landscape/model product semantics. |
| Evidence, proof, policy, release, correction, rollback | `tools/validators/evidence/`, `tools/validators/evidence_bundle/`, policy roots, `release/` | Validator output is not proof or release approval. |

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and policy bundle bindings are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Domain boundary | Does Habitat remain landscape/model context while Fauna retains occurrence/species-event meaning? | A merged Habitat-Fauna truth object. |
| Source role | Are Habitat context sources and Fauna occurrence/regulatory/model/aggregate sources kept distinct? | Interchangeable evidence. |
| Species-record non-ownership | Does a Habitat output avoid claiming Fauna occurrence truth or taxonomic authority? | Species record by implication. |
| Suitability/model posture | Are habitat suitability, corridor, density, and connectivity products labeled as models/derivatives with caveats? | Observed occurrence or habitat guarantee. |
| Sensitive join | Does any join to rare/sensitive Fauna material route to geoprivacy checks? | Safe cross-domain context. |
| Most-restrictive policy | Does the strongest Habitat/Fauna/source/surface policy propagate? | Averaged or weakened policy. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, ReviewRecords, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |
| Public surface | Can map popups, tiles, graph edges, exports, search, Focus Mode, embeddings, or AI text overclaim or reconstruct sensitive details? | UI-only wording. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad Habitat-Fauna validator lane | `tools/validators/habitat-fauna/` |
| Habitat-Fauna geoprivacy validator lane | `tools/validators/geoprivacy/habitat-fauna/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Habitat validator index | `tools/validators/domains/habitat/` |
| Fauna validator indexes | `tools/validators/fauna/`, `tools/validators/domains/fauna/` |
| Shared biodiversity/cross-domain validation | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Habitat/Fauna doctrine and contracts | `docs/domains/habitat/`, `docs/domains/fauna/`, `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Source descriptors | `data/registry/sources/habitat/`, `data/registry/sources/fauna/` |
| Geoprivacy and sensitivity policy | `policy/geoprivacy/`, `policy/sensitivity/habitat/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/habitat-fauna/`, `tests/domains/habitat/`, `tests/domains/fauna/`, `fixtures/domains/habitat/`, `fixtures/domains/fauna/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Habitat-Fauna boundary, source-role, sensitive-join, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source registry topology, fixture shape, policy bundles, report destinations, receipt emission, release integration, tile/search/graph/vector/AI leakage checks, runtime behavior, and CI wiring.
- **DENY:** using this folder as Habitat doctrine, Fauna doctrine, occurrence truth, taxonomic authority, geoprivacy threshold store, exact-location storage, source registry, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/habitat-fauna/` include checks that:

- verify Habitat products do not claim Fauna occurrence, taxonomic, population, nesting, breeding, migration, or monitoring truth;
- verify Fauna occurrence/status/context is not converted into Habitat suitability or restoration truth without model/evidence/policy support;
- verify source-role, source-family, model/observation/regulatory/aggregate, and claim-scope boundaries remain visible;
- detect sensitive joins and route them to geoprivacy validation;
- verify public summaries, catalog records, graph edges, map labels, export rows, Evidence Drawer text, and AI answers do not strengthen Habitat or Fauna claims;
- verify EvidenceRef/EvidenceBundle, policy, release, correction, rollback, and public-surface denial links exist where required;
- emit deterministic findings for downstream review without storing source payloads, exact locations, proof artifacts, receipts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/habitat-fauna/` | Correct home |
|---|---|
| Habitat or Fauna doctrine and object meaning | `docs/domains/habitat/`, `docs/domains/fauna/`, `contracts/domains/` |
| Exact occurrence, nest, den, roost, hibernacula, spawning, breeding/aggregation, telemetry, steward-withheld, or training locations | restricted lifecycle lanes only; never this README or public outputs |
| Geoprivacy thresholds, grid sizes, radii, geohash precisions, or reconstruction parameters | steward-gated `policy/` bundles |
| Redaction/generalization/aggregation implementation and transform validation | `tools/validators/geoprivacy_transform/`, `packages/`, `pipelines/`, or accepted implementation roots |
| RedactionReceipts, AggregationReceipts, validation reports, proofs, EvidenceBundles | `data/receipts/`, `data/proofs/` |
| SourceDescriptor or source registry records | `data/registry/sources/habitat/`, `data/registry/sources/fauna/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Habitat-Fauna validator posture

Habitat-Fauna validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, claim scope, domain ownership, model/observation/regulatory posture, sensitivity tier, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- treats Habitat suitability, connectivity, corridor, ecoregion, land-cover, restoration, or density products as Fauna occurrence truth;
- treats Fauna occurrences, nests, dens, roosts, hibernacula, spawning/breeding/aggregation sites, telemetry, or sensitive records as public-safe Habitat context;
- collapses Habitat model outputs, Fauna observations, regulatory critical-habitat context, species status, source aggregates, or AI summaries into one untyped claim;
- detects sensitive-location exposure but does not route to `tools/validators/geoprivacy/habitat-fauna/` and public-safe transform checks;
- allows map labels, popups, tiles, screenshots, search results, graph edges, exports, embeddings, Focus Mode cards, or AI answers to overclaim or narrow protected locations;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure;
- treats Habitat-Fauna validation as SourceDescriptor creation, EvidenceBundle creation, RedactionReceipt creation, PolicyDecision creation, release approval, publication, public API behavior, stewardship approval, taxonomic authority, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `HABITAT_FAUNA_PASS` | Configured Habitat-Fauna checks passed. |
| `HABITAT_FAUNA_FAIL` | One or more configured Habitat-Fauna checks failed. |
| `HABITAT_FAUNA_SOURCE_DESCRIPTOR_MISSING` | Required Habitat/Fauna SourceDescriptor or source-registry pointer is absent. |
| `HABITAT_FAUNA_SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `DOMAIN_OWNERSHIP_COLLAPSE` | Habitat and Fauna meaning or ownership boundaries are collapsed. |
| `SPECIES_RECORD_OWNERSHIP_OVERCLAIM` | Habitat candidate claims or implies Fauna occurrence/taxon truth. |
| `SUITABILITY_AS_OCCURRENCE_DENIED` | Suitability/model output is treated as observed Fauna occurrence. |
| `OCCURRENCE_AS_HABITAT_TRUTH_DENIED` | Fauna occurrence is treated as Habitat suitability/restoration truth without support. |
| `SENSITIVE_JOIN_DETECTED` | Candidate joins to or derives from sensitive Fauna material. |
| `GEOPRIVACY_HANDOFF_MISSING` | Sensitive join does not route to geoprivacy validation. |
| `SURFACE_OVERCLAIM_RISK` | Public summary, map label, graph edge, export, or AI answer strengthens the claim. |
| `SURFACE_RECONSTRUCTION_RISK` | Public surface can narrow a protected location. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, geoprivacy handoff, evidence closure, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/habitat-fauna/
├── README.md
├── test_habitat_fauna_validator.py
└── fixtures/
    ├── valid_public_habitat_fauna_context/
    ├── missing_source_descriptor/
    ├── domain_ownership_collapse/
    ├── suitability_as_occurrence_denied/
    ├── occurrence_as_habitat_truth_denied/
    ├── sensitive_join_detected/
    ├── geoprivacy_handoff_missing/
    ├── surface_overclaim_risk/
    ├── surface_reconstruction_risk/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/habitat-fauna
```

```bash
python tools/validators/habitat-fauna/validate_habitat_fauna.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_habitat_fauna.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Habitat and Fauna contracts, schemas, source descriptors, source-role rules, sensitivity rules, policy, evidence records, release records, and correction/rollback records rather than defining meaning locally.
- [ ] Habitat landscape/model products do not become Fauna occurrence truth.
- [ ] Fauna occurrence/status/context does not become Habitat suitability/restoration truth without explicit model/evidence/policy support.
- [ ] Sensitive joins route to geoprivacy-specific validation.
- [ ] Produced geometry and downstream surfaces are evaluated when sensitive-location risk exists.
- [ ] Public summaries, catalog projections, graph edges, map labels, export rows, Evidence Drawer text, and AI answers do not strengthen or collapse claims.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy approval, release, publication, source admission, taxonomic authority, stewardship approval, public API behavior, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures and do not encode exact sensitive coordinates or reconstruction thresholds.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Habitat-Fauna validator file. |
| Next smallest safe change | Verify actual Habitat-Fauna validator script path, accepted Habitat/Fauna/source schemas, fixture safety, report destination, geoprivacy handoff behavior, policy enforcement, release linkage, public summary/AI wording behavior, and CI/runtime wiring before promoting this lane beyond draft. |
