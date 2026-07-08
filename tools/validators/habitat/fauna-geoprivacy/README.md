<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-habitat-fauna-geoprivacy-readme
title: tools/validators/habitat/fauna-geoprivacy README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-habitat-steward-plus-fauna-steward-plus-geoprivacy-steward-plus-sensitive-species-reviewer-plus-redaction-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; habitat-facing-validator-shim; fauna-geoprivacy; rare-species; sensitive-join; public-safe-geometry; RedactionReceipt; fail-closed; deny-by-default; release-gated; non-authoritative
owning_root: tools/
responsibility: Habitat-facing routing README for Fauna geoprivacy validation under tools/validators/habitat/fauna-geoprivacy; points maintainers toward the shared Habitat-Fauna geoprivacy lane and documents how Habitat outputs must fail closed when they reveal or can reconstruct sensitive Fauna places; defers Habitat meaning, Fauna occurrence meaning, geoprivacy policy parameters, redaction implementation, EvidenceBundles, receipts, proofs, release decisions, correction records, and rollback authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../geoprivacy/README.md
  - ../../geoprivacy/habitat-fauna/README.md
  - ../../domains/habitat/README.md
  - ../../domains/fauna/README.md
  - ../../fauna/README.md
  - ../../geometry/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../biodiversity/README.md
  - ../../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../contracts/domains/habitat/
  - ../../../../contracts/domains/fauna/
  - ../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../schemas/contracts/v1/receipts/
  - ../../../../policy/geoprivacy/
  - ../../../../policy/sensitivity/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/domains/fauna/
  - ../../../../data/quarantine/habitat/over_precise_geometry/README.md
  - ../../../../data/registry/sources/habitat/
  - ../../../../data/registry/sources/fauna/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file at the requested path. It does not confirm executable validator code."
  - "The preferred shared cross-domain Habitat-Fauna geoprivacy lane is tools/validators/geoprivacy/habitat-fauna/; this path is a Habitat-facing routing shim and must not become a competing authority."
  - "No tools/validators/habitat/README.md parent was confirmed during this edit; parent-lane placement remains NEEDS VERIFICATION."
  - "Habitat geoprivacy exposure can be join-induced or derivation-induced. A Habitat product becomes sensitive when it reveals or can reconstruct sensitive Fauna occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation places, telemetry detail, steward-withheld records, or other restricted places."
  - "Validators evaluate produced geometry and downstream surfaces, not only input records. Sensitive joins fail closed and the most restrictive applicable disposition wins."
  - "This README intentionally contains no exact coordinates, restricted identifiers, generalization radii, grid sizes, geohash precisions, reconstruction thresholds, or other values that could help reverse-engineer sensitive places."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/habitat/fauna-geoprivacy

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-habitat--fauna--geoprivacy-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-rare--species--deny--default-critical)
![posture](https://img.shields.io/badge/posture-fail--closed-red)
![authority](https://img.shields.io/badge/authority-routing--shim-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/habitat/fauna-geoprivacy/` is a Habitat-facing routing README for Fauna geoprivacy checks: it explains how Habitat products must fail closed when they reveal, narrow, or reconstruct sensitive Fauna places, while delegating the shared cross-domain validator lane to `tools/validators/geoprivacy/habitat-fauna/`.

---

## Purpose

This folder exists because Habitat products often become sensitive through **Fauna context**, not because the Habitat layer is inherently restricted.

The durable KFM question for this lane is:

> Does a Habitat candidate that uses, joins, models, summarizes, maps, tiles, exports, indexes, graph-projects, or answers from Fauna context preserve sensitive-species geoprivacy, most-restrictive policy propagation, public-safe geometry, redaction or aggregation receipt linkage, EvidenceRef/EvidenceBundle closure, review state, release linkage, correction path, rollback target, and public-surface denial before any public or semi-public exposure?

The answer should be a deterministic validation result or a clear routing decision to the shared geoprivacy lane. This folder must not create Habitat truth, Fauna occurrence truth, taxonomic authority, geoprivacy thresholds, redaction transforms, RedactionReceipts, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/habitat/fauna-geoprivacy/README.md` | **CONFIRMED README** | This README replaces the empty file at the requested path. |
| Executable validator in this folder | **NEEDS VERIFICATION** | No script, package, registry entry, fixture set, CI job, policy bundle, or runtime behavior is claimed here. |
| Parent Habitat validator folder `tools/validators/habitat/` | **NEEDS VERIFICATION** | No parent `README.md` was confirmed during this edit. Keep this file narrow until that parent is documented. |
| Shared geoprivacy parent | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/README.md` is the broad routing index for sensitive-location and public-safe-geometry checks. |
| Shared Habitat-Fauna geoprivacy lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/habitat-fauna/README.md` is the preferred cross-domain lane for the core Habitat × Fauna geoprivacy rule set. |
| Habitat geoprivacy doctrine | **CONFIRMED repo evidence / draft** | `docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md` states that Habitat exposure can be join-induced or derivation-induced and that produced geometry must be inspected. |
| Rare-species deny-by-default ADR | **CONFIRMED repo evidence / draft** | ADR-0010 says rare species exact locations are deny-by-default and public derivatives require public-safe transforms, receipts, review, and release support. |

[Back to top](#top)

---

## Placement and authority note

This README is intentionally a **routing shim**, not a new authority source.

| Concern | Preferred home |
|---|---|
| Shared Habitat × Fauna geoprivacy validation | `tools/validators/geoprivacy/habitat-fauna/` |
| Habitat-facing routing or adapter notes | `tools/validators/habitat/fauna-geoprivacy/` |
| Per-domain Habitat validator index | `tools/validators/domains/habitat/` |
| Per-domain Fauna validator index | `tools/validators/domains/fauna/` |
| Broad Fauna validator routing | `tools/validators/fauna/` |
| Shared geometry carrier checks | `tools/validators/geometry/` |
| Cross-domain join checks | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Geoprivacy policy parameters | `policy/geoprivacy/`, `policy/sensitivity/`, `policy/domains/` |
| Evidence/proof support | `data/proofs/` |
| Transform and validation receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |

Safe interpretation:

- **CONFIRMED:** this README exists at the requested path.
- **PROPOSED:** this path may host Habitat-facing wrapper code only if it delegates shared rules to the accepted geoprivacy validator lane and does not duplicate policy or domain authority.
- **NEEDS VERIFICATION:** parent folder convention, executable names, validator registry wiring, fixture paths, schema bindings, policy bundle paths, receipt emission, CI wiring, and release integration.
- **DENY:** using this folder as a policy-parameter store, exact-location store, redaction implementation, source registry, schema home, proof store, receipt store, release store, public API/UI surface, map-layer publisher, AI answer authority, or domain-meaning authority.

[Back to top](#top)

---

## Validation focus

Until executable behavior is verified, the following are the proposed validation concepts for this Habitat-facing lane:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Sensitive Fauna join | Does the Habitat product use, join, train on, summarize, or expose sensitive Fauna places? | Safe just because the output is labeled Habitat. |
| Derivation-induced exposure | Could a suitability surface, corridor, density map, graph edge, tile, index, export, or AI answer reconstruct source or training locations? | Public-safe derivative by default. |
| Produced geometry | Does the produced geometry narrow a sensitive site more than allowed by policy? | Input-only validation. |
| Most-restrictive propagation | Does the strongest policy posture from Habitat, Fauna, source terms, joined context, and release state travel through the derivative? | Averaged or weakened policy. |
| Public-safe geometry | Is the public geometry generalized, redacted, buffered, gridded, aggregated, suppressed, or denied according to policy? | Exact geometry with nicer styling. |
| Transform receipt | Is a RedactionReceipt, AggregationReceipt, or equivalent governed receipt linked when a public-safe derivative exists? | Hidden cartographic simplification. |
| Steward review | Is required species, sensitivity, habitat, source, or release review present before public exposure? | Optional sign-off. |
| Public-surface leakage | Could popups, tiles, screenshots, exports, search, graph, embeddings, Focus Mode, or AI text reverse-engineer a sensitive Fauna place? | UI-only concern. |
| Evidence and release posture | Are EvidenceRefs, EvidenceBundles, PolicyDecisions, ReviewRecords, ReleaseManifests, correction paths, and rollback targets present? | Publication by passing validation. |

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/habitat/fauna-geoprivacy/` include:

- this Habitat-facing README;
- a small wrapper that routes Habitat products to `tools/validators/geoprivacy/habitat-fauna/` without copying its rule set;
- thin adapter checks for Habitat candidate payload shapes before forwarding to the shared geoprivacy validator;
- references to valid and invalid Habitat × Fauna fixture families;
- reason-code documentation specific to Habitat-side failure messages;
- maintainer notes that explain how Habitat outputs should interpret shared geoprivacy results;
- no-network examples that demonstrate fail-closed handling without exposing sensitive coordinates or thresholds.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/habitat/fauna-geoprivacy/` | Correct home |
|---|---|
| Habitat domain meaning or Habitat contracts | `docs/domains/habitat/`, `contracts/domains/habitat/` |
| Fauna occurrence meaning, taxon authority, or Fauna contracts | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Geoprivacy thresholds, grid sizes, geohash precision, buffers, or policy values | `policy/geoprivacy/`, `policy/sensitivity/`, accepted restricted policy bundles |
| Redaction, generalization, aggregation, or masking implementation that changes data | accepted transformer/pipeline/package roots, with policy and receipts |
| Source descriptors | `data/registry/sources/habitat/`, `data/registry/sources/fauna/` |
| Schemas and enums | `schemas/contracts/v1/...` |
| EvidenceBundles, proof packs, validation reports, transform receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, graph, search, export, Focus Mode, screenshot, or AI runtime code | governed application/runtime roots |
| Exact coordinates, restricted identifiers, or reverse-engineering hints | nowhere in public repository-facing docs |

[Back to top](#top)

---

## Required input posture for future validator code

A future executable validator under this lane should accept only no-network local fixture or candidate paths and should treat missing context as fail-closed.

Minimum expected inputs remain **PROPOSED** until schemas and registry wiring are verified:

| Input | Required posture |
|---|---|
| Habitat candidate reference | Must identify the candidate artifact, layer, feature set, model output, tile build, API payload, or derived product being checked. |
| Fauna context reference | Must identify whether the candidate uses occurrence, sensitive-site, range, telemetry, steward-controlled, modeled, aggregate, or public-safe Fauna support. |
| EvidenceRef list | Must resolve to EvidenceBundle before consequential claims or public artifacts are accepted. |
| PolicyDecision or sensitivity evaluation | Must include geoprivacy, source-rights, steward-review, and most-restrictive propagation posture. |
| Geometry posture | Must distinguish exact, public-safe, generalized, gridded, buffered, aggregated, suppressed, and withheld geometry. |
| Transform receipt reference | Required when geometry was changed or suppressed for public safety. |
| Release reference | Required before any public-safe derivative can be treated as released. |
| Surface inventory | Must name downstream surfaces checked: map, tile, popup, screenshot, export, search, graph, embedding, Focus Mode, AI, catalog, proof, or release. |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `HABITAT_FAUNA_GEOPRIVACY_PASS` | Candidate passed configured Habitat-facing Fauna geoprivacy checks. |
| `HABITAT_FAUNA_GEOPRIVACY_FAIL` | One or more configured checks failed. |
| `ROUTE_TO_SHARED_GEOPRIVACY_VALIDATOR` | Candidate should be checked by `tools/validators/geoprivacy/habitat-fauna/`. |
| `SHARED_GEOPRIVACY_VALIDATOR_MISSING` | Required shared validator lane, registry entry, or runner was expected but not found. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses Habitat product role, Fauna support role, model role, observation role, or public derivative role. |
| `SENSITIVE_FAUNA_JOIN_DENIED` | Habitat product joins to or reveals sensitive Fauna location context without an allow path. |
| `DERIVATIVE_RECONSTRUCTION_DENIED` | Suitability, corridor, density, graph, tile, search, embedding, export, or AI output can reconstruct a sensitive place. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required generalized, redacted, buffered, gridded, aggregated, suppressed, or withheld public-safe geometry is absent. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent or unresolved. |
| `GEOPRIVACY_POLICY_UNRESOLVED` | Applicable geoprivacy or sensitivity policy could not be resolved. |
| `REVIEW_OR_POLICY_GAP` | Required steward review, PolicyDecision, or sensitivity decision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | A public surface could disclose exact or reverse-engineerable sensitive location detail. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Public-surface denial checks

This lane should treat these downstream surfaces as disclosure surfaces, not presentation details:

- MapLibre layers, tiles, PMTiles, screenshots, and thumbnails;
- feature popups, Evidence Drawer previews, hover cards, labels, and legends;
- GeoJSON, GeoParquet, CSV, image, report, and notebook exports;
- graph edges, graph projections, search results, vector indexes, and embeddings;
- Focus Mode prompts, AI answers, summaries, story nodes, and generated captions;
- catalog previews, release notes, QA reports, and documentation snippets.

A candidate fails when any of those surfaces can reveal, narrow, or reconstruct a sensitive Fauna place beyond the approved public-safe derivative.

[Back to top](#top)

---

## Minimal future implementation sketch

A future code lane should remain small and reversible:

```text
tools/validators/habitat/fauna-geoprivacy/
├── README.md
├── validate_habitat_fauna_geoprivacy.py        # PROPOSED; not confirmed
└── fixtures.md                                 # PROPOSED; documentation index only
```

The executable, if added, should call shared validation helpers rather than copy policy rules locally. The repo-wide validator orchestrator should remain the entry point if registry wiring is adopted.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at the requested path.
- [x] It states that this path is a Habitat-facing routing shim, not a competing authority.
- [x] It points to the shared `tools/validators/geoprivacy/habitat-fauna/` lane.
- [x] It preserves cite-or-abstain, fail-closed, deny-by-default, public-safe-geometry, receipt, evidence, release, correction, and rollback boundaries.
- [x] It avoids exact coordinates, restricted identifiers, policy thresholds, grid sizes, geohash precisions, and reconstruction hints.
- [x] It marks executable behavior, CI wiring, policy bundle paths, schema bindings, fixtures, receipt emission, and runtime behavior as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Parent `tools/validators/habitat/README.md` is created or the parent-lane convention is explicitly recorded elsewhere.
- [ ] The shared Habitat-Fauna geoprivacy validator has an accepted executable or registry entry.
- [ ] Valid and invalid fixtures cover sensitive joins, missing EvidenceRef, unresolved policy, missing transform receipt, reverse-engineerable derivative, public-surface leakage, and release gaps.
- [ ] CI or `tools/validate_all.py` invokes the validator in deterministic order.
- [ ] Validation outputs write reports or receipts only to accepted roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with Habitat-facing Fauna geoprivacy routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
