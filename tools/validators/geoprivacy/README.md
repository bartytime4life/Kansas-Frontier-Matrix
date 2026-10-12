<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geoprivacy-readme
title: tools/validators/geoprivacy README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geoprivacy-steward-plus-sensitivity-reviewer-plus-redaction-steward-plus-domain-stewards-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geoprivacy-validator-parent; sensitive-location; public-safe-geometry; RedactionReceipt; AggregationReceipt; rare-species; archaeology; infrastructure; people-dna-land; fail-closed; deny-by-default; release-gated; non-authoritative
owning_root: tools/
responsibility: broad Geoprivacy validator routing index for shared sensitive-location and public-safe-geometry validator lanes under tools/validators/geoprivacy, including Habitat-Fauna sensitive joins, rare-species exact-location denial, produced-geometry inspection, reverse-engineerable derivative checks, most-restrictive-policy propagation, redaction/generalization/aggregation receipt linkage, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring domain meaning, geoprivacy policy parameters, redaction implementation, evidence records, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../geometry/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../biodiversity/README.md
  - ../fauna/README.md
  - ../domains/fauna/README.md
  - ../domains/habitat/README.md
  - habitat-fauna/README.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../contracts/common/spatial_geometry.md
  - ../../../contracts/domains/habitat/
  - ../../../contracts/domains/fauna/
  - ../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../schemas/contracts/v1/receipts/
  - ../../../policy/geoprivacy/
  - ../../../policy/sensitivity/
  - ../../../policy/domains/
  - ../../../data/quarantine/habitat/over_precise_geometry/README.md
  - ../../../data/registry/sources/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Confirmed child README lane at this path: habitat-fauna/. Executable behavior remains NEEDS VERIFICATION."
  - "Habitat geoprivacy evidence says Habitat exposure can be join-induced or derivation-induced; a produced Habitat output becomes sensitive when it reveals or can reconstruct a sensitive Fauna occurrence or steward-withheld place."
  - "Habitat geoprivacy evidence says validators evaluate the produced geometry, not only the input records; sensitive joins fail closed and most-restrictive disposition applies."
  - "ADR-0010 evidence says rare-species exact locations are deny-by-default and public derivatives require generalization, redaction, buffering, gridding, aggregation, transform receipts, and steward review."
  - "This index must not include exact coordinates, identifiers, restricted-source-derived fields, generalization radii, grid sizes, geohash precisions, reconstruction thresholds, or other values that could help reverse-engineer sensitive locations."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, and policy. They do not define geoprivacy thresholds, create RedactionReceipts, decide policy, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geoprivacy

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-geoprivacy--validator--routing-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-deny--by--default-critical)
![posture](https://img.shields.io/badge/posture-most--restrictive--wins-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geoprivacy/` is the broad validator routing index for sensitive-location, public-safe geometry, geoprivacy transform, reverse-engineerable derivative, and most-restrictive-policy checks.

---

## Purpose

`tools/validators/geoprivacy/` exists to route shared geoprivacy validation concerns under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do geoprivacy validator lanes prevent exact, sensitive, restricted, or reverse-engineerable location exposure before candidates reach catalog, proof, release, map, API, graph, tile, search, export, Focus Mode, screenshot, embedding, or AI surfaces?

The answer should be a navigable validator routing index and deterministic validation outputs from configured child lanes. This folder should not create geoprivacy policy thresholds, perform redaction transforms, store exact locations, create RedactionReceipts, create EvidenceBundles, store proofs, store receipts, decide policy, approve release, publish map layers, expose public API payloads, or authorize AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geoprivacy/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Child lane `habitat-fauna/` | **CONFIRMED README / executable NEEDS VERIFICATION** | Checks Habitat × Fauna sensitive joins, derivation-induced exposure, most-restrictive policy propagation, public-safe geometry, transform receipts, release linkage, and public-surface denial. |
| Habitat geoprivacy doctrine | **CONFIRMED in repo evidence / draft** | Habitat geoprivacy doctrine says exposure can be join-induced and derivation-induced, protects places rather than rows, and omits exact threshold values because those are steward-gated policy values. |
| Deny-by-default ADR | **CONFIRMED in repo evidence / draft** | ADR-0010 states rare-species exact locations are deny-by-default and public derivatives require public-safe transforms, receipts, and steward review. |
| Shared geometry validator | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geometry/README.md` documents common geometry-carrier checks and defers domain-specific public-safe exposure decisions. |
| Executables, schemas, fixtures, policy bundles, transform receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, geoprivacy threshold, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Child lanes

| Child lane | Purpose | Status |
|---|---|---|
| [`habitat-fauna/`](habitat-fauna/README.md) | Habitat × Fauna geoprivacy checks for sensitive joins, derivation-induced exposure, rare-species exact-location denial, public-safe geometry, transform receipt linkage, release linkage, and surface reconstruction risk. | **CONFIRMED README / executable NEEDS VERIFICATION** |

Possible future child lanes remain **PROPOSED** until created and verified:

- `flora-habitat/` for rare-plant, collectable-species, habitat, suitability, and restoration-output exposure checks;
- `archaeology-public/` for exact site, burial, sacred/culturally sensitive, collection-storage, and looting-risk exposure checks;
- `infrastructure-public/` for critical facility, dependency, operational condition, vulnerability, and continuity network exposure checks;
- `people-dna-land/` for living-person, family graph, DNA-adjacent, parcel-level, and revocation-sensitive exposure checks;
- `tile-surface/` for map tiles, screenshots, cached tiles, exports, and scale/zoom reconstruction risks;
- `graph-search-vector/` for graph edges, search results, embeddings, vector retrieval, and AI reconstruction risks;
- `redaction-receipt/` for transform receipt presence and destination checks without creating receipts locally.

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Broad geoprivacy validator index | `tools/validators/geoprivacy/` |
| Habitat-Fauna geoprivacy child lane | `tools/validators/geoprivacy/habitat-fauna/` |
| Shared geometry carrier checks | `tools/validators/geometry/` |
| Cross-domain join validation | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Biodiversity/Fauna/Habitat context | `tools/validators/biodiversity/`, `tools/validators/fauna/`, `tools/validators/domains/fauna/`, `tools/validators/domains/habitat/` |
| Domain meaning | `docs/domains/`, `contracts/domains/` |
| Common geometry meaning | `contracts/common/spatial_geometry.md` |
| Geoprivacy and sensitivity policy | `policy/geoprivacy/`, `policy/sensitivity/`, `policy/domains/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/` |
| Proofs, receipts, release | `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where shared geoprivacy validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and policy bundle bindings are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Sensitive-location class | Does the candidate involve rare species, archaeology, critical infrastructure, living-person/DNA, private-land, restricted-source, or other sensitive-location material? | Public-safe content by default. |
| Produced geometry | Does the produced output reveal more than the source input appears to reveal? | Input-only validation. |
| Reverse-engineerable derivative | Can tiles, screenshots, graph edges, exports, search, embeddings, Focus Mode, or AI text reconstruct a sensitive location? | Safe because exact coordinates are absent. |
| Most-restrictive propagation | Does the strongest applicable policy travel through joins, derivatives, caches, indexes, summaries, and public surfaces? | Averaged or weakened policy. |
| Public-safe transform | Is geometry generalized, redacted, buffered, gridded, aggregated, suppressed, or denied according to policy? | Local validator decision. |
| Transform receipt | Is a RedactionReceipt, AggregationReceipt, or equivalent governed receipt linked where required? | Hidden cartographic simplification. |
| Steward review | Is required sensitivity, cultural, species, infrastructure, consent, or domain review present? | Optional sign-off. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, PolicyDecisions, ReviewRecords, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Geoprivacy validator routing index | `tools/validators/geoprivacy/` |
| Geoprivacy child lanes | `tools/validators/geoprivacy/*/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Shared geometry validation | `tools/validators/geometry/` |
| Domain-specific validators | `tools/validators/<domain>/`, `tools/validators/domains/<domain>/`, or accepted domain validator homes |
| Domain doctrine and contracts | `docs/domains/`, `contracts/domains/` |
| Common geometry contract | `contracts/common/spatial_geometry.md` |
| Source descriptors | `data/registry/sources/` |
| Sensitivity and geoprivacy policy | `policy/geoprivacy/`, `policy/sensitivity/`, `policy/domains/`, `policy/` |
| Redaction/Aggregation/Validation receipts | `data/receipts/` |
| Evidence/proof support | `data/proofs/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geoprivacy/`, `tests/domains/`, `fixtures/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists and the `habitat-fauna/` child README exists.
- **PROPOSED:** validator code may live here when it checks declared geoprivacy, public-safe geometry, most-restrictive-policy, receipt, evidence, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, policy bundles, threshold vocabulary, transform receipt shapes, fixture shape, report destinations, receipt emission, release integration, tile/search/graph/vector/AI leakage checks, runtime behavior, and CI wiring.
- **DENY:** using this folder as geoprivacy policy threshold store, exact-location store, redaction implementation, schema home, source registry, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geoprivacy/` include:

- this broad geoprivacy validator routing README;
- child lanes that check cross-domain sensitive-location exposure without storing sensitive details;
- parent runners that delegate to child validators without redefining policy thresholds;
- checks that public-bound geometry, tiles, screenshots, graph edges, search results, exports, embeddings, Focus Mode cards, and AI answers cannot reverse-engineer sensitive locations;
- checks that required transform receipts, steward reviews, policy decisions, release manifests, correction paths, and rollback targets are linked;
- synthetic fixture references and test-surface guidance that do not encode exact sensitive locations or reconstruction thresholds.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geoprivacy/` | Correct home |
|---|---|
| Exact coordinates, precise geometries, site IDs, restricted source IDs, or identifiers that reveal location | restricted lifecycle lanes only; never public docs or public outputs |
| Geoprivacy thresholds, grid sizes, radii, geohash precisions, or reconstruction parameters | steward-gated `policy/` bundles |
| Redaction/generalization/aggregation implementation | `packages/`, `pipelines/`, or accepted implementation roots |
| RedactionReceipts, AggregationReceipts, validation reports, proofs, EvidenceBundles | `data/receipts/`, `data/proofs/` |
| Domain object meaning | `docs/domains/`, `contracts/domains/` |
| SourceDescriptor or source registry records | `data/registry/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Geoprivacy validator posture

Geoprivacy validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks sensitivity classification, geoprivacy status, geometry role, public-safe transform posture, transform receipt, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- exposes exact or reverse-engineerable rare-species, archaeology, critical-infrastructure, living-person/DNA, private-land, steward-withheld, or restricted-source location detail;
- hides reconstruction risk in tiles, screenshots, graph edges, search results, exports, embeddings, Focus Mode cards, or AI answers;
- applies a weaker policy than the most restrictive applicable input, join, derivative, audience, or surface requires;
- uses public-safe geometry without a governed transform receipt and review chain;
- stores exact sensitive locations, thresholds, or reconstruction parameters in this folder or in public fixtures/docs;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure;
- treats geoprivacy validation as SourceDescriptor creation, EvidenceBundle creation, RedactionReceipt creation, PolicyDecision creation, release approval, publication, public API behavior, steward approval, or AI answer authority.

The validator tree must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `GEOPRIVACY_VALIDATORS_PASS` | Configured geoprivacy validators passed. |
| `GEOPRIVACY_VALIDATORS_FAIL` | One or more configured geoprivacy validators failed. |
| `GEOPRIVACY_CHILD_VALIDATOR_MISSING` | Expected child validator lane or runner is absent. |
| `GEOPRIVACY_CHILD_VALIDATOR_FAILED` | A child validator reported one or more findings. |
| `SENSITIVE_LOCATION_CLASS_MISSING` | Required sensitive-location class or tier is absent. |
| `GEOPRIVACY_STATUS_MISSING` | Required geoprivacy status is absent. |
| `MOST_RESTRICTIVE_POLICY_GAP` | Candidate does not propagate the most restrictive applicable policy. |
| `EXACT_LOCATION_DENIED` | Exact sensitive location is unsafe for the requested surface. |
| `REVERSE_ENGINEERABLE_DERIVATIVE_DENIED` | Candidate can reconstruct sensitive location despite absent exact coordinates. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required public-safe geometry role or transform is absent. |
| `GEOPRIVACY_TRANSFORM_RECEIPT_MISSING` | Required redaction, generalization, aggregation, buffering, gridding, or suppression receipt is absent. |
| `STEWARDSHIP_REVIEW_GAP` | Required steward, cultural, species, infrastructure, consent, or sensitivity review is absent. |
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
tests/validators/geoprivacy/
├── README.md
├── test_geoprivacy_validator_parent.py
├── habitat-fauna/
└── fixtures/
    ├── valid_public_safe_derivative/
    ├── missing_sensitivity_class/
    ├── exact_location_denied/
    ├── reverse_engineerable_derivative_denied/
    ├── missing_public_safe_geometry/
    ├── missing_transform_receipt/
    ├── most_restrictive_policy_gap/
    ├── stewardship_review_gap/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geoprivacy
```

```bash
python tools/validators/geoprivacy/run_geoprivacy_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_geoprivacy_validators.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining policy thresholds.
- [ ] No exact coordinates, restricted identifiers, geoprivacy thresholds, grid sizes, radii, geohash precisions, or reconstruction parameters are added to public docs or fixtures.
- [ ] Produced geometry and downstream surfaces are evaluated, not just source inputs.
- [ ] Most-restrictive policy propagation is preserved across sources, joins, derivatives, audience, and surface.
- [ ] Public-safe geometry, transform receipt, steward review, policy decision, release manifest, correction path, and rollback target are present before public use.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, geoprivacy threshold authority, transform receipt, policy approval, release, publication, source admission, steward approval, public API behavior, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures and do not encode sensitive locations or reconstruction thresholds.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Geoprivacy validator parent file. |
| Next smallest safe change | Verify actual parent runner path, child lane inventory, geoprivacy policy bundle binding, accepted schemas, transform receipt shapes, fixtures, report destination, receipt emission, policy enforcement, release linkage, tile/search/graph/vector/AI leakage behavior, and CI/runtime wiring before promoting this lane beyond draft. |
