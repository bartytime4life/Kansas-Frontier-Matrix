<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geoprivacy-habitat-fauna-readme
title: tools/validators/geoprivacy/habitat-fauna README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geoprivacy-steward-plus-habitat-steward-plus-fauna-steward-plus-sensitive-species-reviewer-plus-redaction-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geoprivacy-validator; habitat-fauna; sensitive-join; rare-species; public-safe-geometry; RedactionReceipt; fail-closed; deny-by-default; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Habitat-Fauna geoprivacy validator lane for checking join-induced and derivation-induced location exposure between Habitat outputs and Fauna sensitive occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry detail, steward-withheld records, suitability surfaces, corridors, density/hot-spot products, public-safe geometry, redaction/generalization/aggregation receipt posture, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, correction and rollback linkage, official sensitivity posture, finite negative outcomes, and public-surface denial checks while deferring Habitat meaning, Fauna meaning, geoprivacy policy parameters, redaction implementation, evidence records, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../../geometry/README.md
  - ../../fauna/README.md
  - ../../domains/fauna/README.md
  - ../../domains/habitat/README.md
  - ../../biodiversity/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../evidence/README.md
  - ../../citation/README.md
  - ../../evidence_bundle/README.md
  - ../../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../../docs/domains/habitat/SENSITIVITY_POLICY.md
  - ../../../../docs/domains/habitat/HABITAT_DOMAIN_MODEL.md
  - ../../../../docs/domains/habitat/sublanes/critical-habitat.md
  - ../../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../../docs/domains/fauna/CROSS_LANE_RELATIONS.md
  - ../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../contracts/domains/habitat/
  - ../../../../contracts/domains/fauna/
  - ../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/domains/fauna/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../policy/sensitivity/fauna/
  - ../../../../policy/geoprivacy/
  - ../../../../data/quarantine/habitat/over_precise_geometry/README.md
  - ../../../../data/processed/fauna/restricted/range_exact/README.md
  - ../../../../data/registry/sources/habitat/
  - ../../../../data/registry/sources/fauna/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "No parent tools/validators/geoprivacy/README.md was found during this task. A future parent geoprivacy index remains PROPOSED."
  - "Habitat geoprivacy evidence says Habitat exposure is often join-induced or derivation-induced; a Habitat output becomes sensitive when it reveals or can reconstruct a sensitive Fauna occurrence or steward-withheld place."
  - "Habitat geoprivacy evidence says validators evaluate the produced geometry, not just the inputs; sensitive joins fail closed and most-restrictive disposition applies."
  - "Fauna validator evidence says sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry detail, steward-controlled records, and reverse-engineerable derivatives are deny-by-default without geoprivacy, review, policy, evidence, release, correction, and rollback support."
  - "ADR-0010 evidence says rare species exact occurrence/site locations are deny-by-default and any public derivative must be generalized, redacted, buffered, gridded, or aggregated with transform receipts and steward review."
  - "This validator lane must not publish exact locations, define geoprivacy thresholds, create RedactionReceipts, decide policy, approve release, create EvidenceBundles, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geoprivacy/habitat-fauna

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-habitat--fauna--geoprivacy-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-rare--species--deny--default-critical)
![posture](https://img.shields.io/badge/posture-most--restrictive--wins-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geoprivacy/habitat-fauna/` is the proposed validator lane for checking that Habitat outputs joined to, derived from, or capable of reconstructing sensitive Fauna locations fail closed unless a public-safe geoprivacy path is fully supported.

---

## Purpose

`tools/validators/geoprivacy/habitat-fauna/` exists for Habitat × Fauna geoprivacy validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a Habitat output that uses, joins, models, summarizes, maps, tiles, graph-projects, exports, or answers from Fauna occurrence/context preserve sensitive-species location protection, most-restrictive policy propagation, public-safe geometry posture, redaction/generalization/aggregation receipt linkage, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Habitat truth, Fauna occurrence truth, taxonomic authority, geoprivacy thresholds, redaction transforms, RedactionReceipts, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geoprivacy/habitat-fauna/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent geoprivacy validator index | **NOT FOUND in this task** | `tools/validators/geoprivacy/README.md` was not found. A future parent geoprivacy routing index remains PROPOSED. |
| Habitat geoprivacy doctrine | **CONFIRMED in repo evidence / draft** | Habitat geoprivacy doctrine says exposure is join-induced and derivation-induced, protects places rather than rows, and contains no exact thresholds because those are steward-gated policy values. |
| Habitat validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Habitat validator index names sensitive joins, geoprivacy, over-precise geometry, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Fauna validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Fauna validator index says sensitive occurrences, nests, dens, roosts, hibernacula, spawning/breeding/aggregation sites, telemetry detail, steward-controlled records, and reverse-engineerable derivatives are deny-by-default without governed support. |
| Deny-by-default ADR | **CONFIRMED in repo evidence / draft** | ADR-0010 states rare species exact locations are deny-by-default and public derivatives require generalization/redaction/buffering/gridding/aggregation, transform receipts, and steward review. |
| Executables, schemas, fixtures, geoprivacy policy bundle, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, geoprivacy threshold, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Habitat-Fauna geoprivacy validator lane | `tools/validators/geoprivacy/habitat-fauna/` |
| Future parent geoprivacy index | `tools/validators/geoprivacy/README.md` **PROPOSED** |
| Shared geometry validator | `tools/validators/geometry/` |
| Habitat validator index | `tools/validators/domains/habitat/` |
| Fauna validator index | `tools/validators/fauna/`, `tools/validators/domains/fauna/` |
| Biodiversity / cross-domain validation | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Habitat geoprivacy doctrine | `docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md` |
| Habitat and Fauna domain meaning | `docs/domains/habitat/`, `docs/domains/fauna/`, `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Geoprivacy and sensitivity policy | `policy/geoprivacy/`, `policy/sensitivity/habitat/`, `policy/sensitivity/fauna/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/habitat/`, `data/registry/sources/fauna/` |
| Proofs, receipts, release | `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where Habitat × Fauna geoprivacy validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and policy bundle bindings are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Join-induced sensitivity | Does a Habitat output become sensitive because it joins to a Fauna occurrence or sensitive site? | Safe just because Habitat input was public. |
| Derivation-induced sensitivity | Could a suitability surface, corridor, density map, model, tile, graph edge, or AI answer reconstruct training or source locations? | Public-safe derivative by default. |
| Most-restrictive propagation | Does the output inherit the most restrictive applicable policy from Habitat, Fauna, source terms, and joined context? | An average or weaker policy. |
| Sensitive Fauna site categories | Are nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, telemetry detail, steward-controlled records, and exact occurrences denied unless gates close? | Public map context. |
| Public-safe geometry | Is geometry generalized, redacted, buffered, gridded, aggregated, suppressed, or denied according to policy? | Exact geometry or a reversible transform. |
| Transform receipt | Does the public-safe derivative have a RedactionReceipt, AggregationReceipt, or equivalent governed receipt? | Hidden cartographic simplification. |
| Surface-specific leakage | Could map popups, tiles, screenshots, exports, search, graph, embeddings, Focus Mode, or AI text reverse-engineer a sensitive location? | A UI-only concern. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, ReviewRecords, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Habitat-Fauna geoprivacy validator lane | `tools/validators/geoprivacy/habitat-fauna/` |
| Future geoprivacy validator parent | `tools/validators/geoprivacy/README.md` **PROPOSED** |
| Shared validator plumbing | `tools/validators/_common/` |
| Shared geometry validation | `tools/validators/geometry/` |
| Habitat validator index | `tools/validators/domains/habitat/` |
| Fauna validator index | `tools/validators/fauna/`, `tools/validators/domains/fauna/` |
| Habitat/Fauna doctrine and contracts | `docs/domains/habitat/`, `docs/domains/fauna/`, `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Geoprivacy, sensitivity, and domain policy | `policy/geoprivacy/`, `policy/sensitivity/habitat/`, `policy/sensitivity/fauna/`, `policy/domains/habitat/`, `policy/domains/fauna/` |
| Source descriptors | `data/registry/sources/habitat/`, `data/registry/sources/fauna/` |
| Over-precise or unsafe Habitat holds | `data/quarantine/habitat/over_precise_geometry/` or accepted quarantine lanes |
| Restricted Fauna exact/range material | restricted Fauna lifecycle lanes, not public outputs |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geoprivacy/habitat-fauna/`, `tests/domains/habitat/`, `tests/domains/fauna/`, `fixtures/domains/habitat/`, `fixtures/domains/fauna/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Habitat-Fauna geoprivacy, most-restrictive-policy, public-safe geometry, receipt, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, geoprivacy threshold vocabulary, public-safe geometry policy bundle, transform receipt shapes, fixture shape, report destinations, receipt emission, policy integration, release integration, tile/search/graph/vector/AI leakage checks, runtime behavior, and CI wiring.
- **DENY:** using this folder as Habitat doctrine, Fauna doctrine, geoprivacy policy parameter store, redaction implementation, exact-location storage, source registry, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geoprivacy/habitat-fauna/` include checks that:

- verify Habitat outputs that join to or derive from Fauna records inherit sensitive-site posture;
- verify outputs evaluate produced geometry and downstream surfaces rather than only input records;
- verify rare-species exact locations and reverse-engineerable derivatives fail closed;
- verify public-safe geometry has policy-approved transform posture and transform receipt linkage;
- verify the most restrictive applicable policy propagates across Habitat, Fauna, source terms, surface, audience, and release channel;
- verify map, tile, search, graph, screenshot, export, embedding, Focus Mode, and AI surfaces do not reconstruct sensitive locations;
- verify correction, withdrawal, supersession, and rollback targets exist for released public-safe derivatives;
- emit deterministic findings for downstream review without storing exact locations, proof artifacts, receipts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geoprivacy/habitat-fauna/` | Correct home |
|---|---|
| Habitat or Fauna doctrine and object meaning | `docs/domains/habitat/`, `docs/domains/fauna/`, `contracts/domains/` |
| Exact occurrence, nest, den, roost, hibernacula, spawning, breeding/aggregation, telemetry, steward-withheld, or training locations | restricted lifecycle lanes only; never this README or public outputs |
| Geoprivacy thresholds, grid sizes, radii, geohash precisions, or reconstruction parameters | steward-gated `policy/` bundles, not public docs |
| Redaction/generalization/aggregation implementation | `packages/`, `pipelines/`, or accepted implementation roots |
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

## Habitat-Fauna geoprivacy validator posture

Habitat-Fauna geoprivacy validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, sensitivity tier, geoprivacy status, geometry role, transform receipt, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- reveals or can reconstruct exact Fauna occurrence, nest, den, roost, hibernacula, spawning site, breeding/aggregation site, telemetry detail, steward-controlled record, rare-species site, or protected location;
- treats Habitat suitability, connectivity, corridor, density, hot-spot, ecoregion, land-cover, or restoration outputs as safe when they are trained on, joined to, or derived from sensitive Fauna records;
- publishes a Habitat product at finer resolution than the allowed generalized Fauna product;
- lacks public-safe geometry transform support, RedactionReceipt/AggregationReceipt linkage, steward review, policy decision, release manifest, correction path, or rollback target;
- allows map labels, popups, tiles, screenshots, search results, graph edges, exports, embeddings, Focus Mode cards, or AI answers to narrow a protected location;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure;
- treats geoprivacy validation as SourceDescriptor creation, EvidenceBundle creation, RedactionReceipt creation, PolicyDecision creation, release approval, publication, public API behavior, stewardship approval, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `HABITAT_FAUNA_GEOPRIVACY_PASS` | Configured Habitat-Fauna geoprivacy checks passed. |
| `HABITAT_FAUNA_GEOPRIVACY_FAIL` | One or more configured checks failed. |
| `SENSITIVE_JOIN_DETECTED` | Habitat output joins to or derives from sensitive Fauna material. |
| `JOIN_POLICY_UNRESOLVED` | Most-restrictive policy propagation cannot be resolved. |
| `FAUNA_EXACT_LOCATION_DENIED` | Exact or reverse-engineerable Fauna location is unsafe for the requested surface. |
| `HABITAT_DERIVATIVE_RECONSTRUCTION_RISK` | Habitat derivative can reconstruct sensitive Fauna locations. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required public-safe geometry role or transform is absent. |
| `GEOPRIVACY_TRANSFORM_RECEIPT_MISSING` | Required redaction, generalization, aggregation, buffering, gridding, or suppression receipt is absent. |
| `SURFACE_RECONSTRUCTION_RISK` | Map/tile/search/graph/export/screenshot/vector/AI surface can narrow a protected location. |
| `MOST_RESTRICTIVE_POLICY_GAP` | Candidate does not apply the most restrictive applicable policy. |
| `STEWARDSHIP_REVIEW_GAP` | Required steward or sensitivity review state is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, public-safe transform, evidence closure, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/geoprivacy/habitat-fauna/
├── README.md
├── test_habitat_fauna_geoprivacy_validator.py
└── fixtures/
    ├── valid_public_safe_habitat_fauna_derivative/
    ├── sensitive_join_detected/
    ├── exact_occurrence_denied/
    ├── habitat_derivative_reconstruction_risk/
    ├── missing_public_safe_geometry/
    ├── missing_transform_receipt/
    ├── missing_stewardship_review/
    ├── surface_reconstruction_risk/
    ├── most_restrictive_policy_gap/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geoprivacy/habitat-fauna
```

```bash
python tools/validators/geoprivacy/habitat-fauna/validate_habitat_fauna_geoprivacy.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_habitat_fauna_geoprivacy.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Habitat and Fauna contracts, schemas, source descriptors, sensitivity rules, geoprivacy policy, evidence records, release records, and correction/rollback records rather than defining meaning locally.
- [ ] Produced geometry and downstream surfaces are evaluated, not just source inputs.
- [ ] Most-restrictive policy propagation is preserved across Habitat, Fauna, source, audience, and surface.
- [ ] Rare species exact locations and reverse-engineerable derivatives fail closed.
- [ ] Public-safe geometry, transform receipt, steward review, policy decision, release manifest, correction path, and rollback target are present before public use.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, geoprivacy threshold authority, transform receipt, policy approval, release, publication, source admission, stewardship approval, public API behavior, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures and do not encode exact sensitive coordinates or reconstruction thresholds.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Habitat-Fauna geoprivacy validator file. |
| Next smallest safe change | Create or verify a parent `tools/validators/geoprivacy/README.md`, then verify actual Habitat-Fauna geoprivacy validator script path, accepted Habitat/Fauna/receipt schemas, geoprivacy policy bundle binding, transform receipt shapes, fixtures, report destination, receipt emission, policy enforcement, release linkage, tile/search/graph/vector/AI leakage behavior, and CI/runtime wiring before promoting this lane beyond draft. |
