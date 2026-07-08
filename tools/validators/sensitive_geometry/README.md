<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-sensitive-geometry-readme
title: tools/validators/sensitive_geometry README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-sensitive-geometry-steward-plus-geoprivacy-steward-plus-redaction-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; sensitive-geometry-validator-index; exact-location-deny-default; geoprivacy-aware; redaction-aware; generalization-aware; aggregation-aware; receipt-aware; most-restrictive-wins; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: parent sensitive-geometry validator routing README under tools/validators; documents validation expectations for exact/internal geometry separation, sensitive-location denial, public-safe geometry posture, redaction/generalization/aggregation receipt linkage, geometry carrier checks, CRS/precision/role posture, reverse-engineerable derivative checks, side-channel exposure checks, most-restrictive policy propagation, EvidenceRef and EvidenceBundle linkage, policy/review/release posture, correction/rollback propagation, schema/fixture/test routing, and finite outcomes while deferring geometry semantics, domain meaning, geoprivacy policy parameters, redaction transforms, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../geometry/README.md
  - ../geoprivacy/README.md
  - ../geoprivacy_transform/README.md
  - ../policy/README.md
  - ../rights/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../maplibre/README.md
  - ../pmtiles/README.md
  - ../geology/public_safe_geometry/README.md
  - ../../../docs/architecture/sensitive-domain-fail-closed.md
  - ../../../docs/standards/REDACTION_PROFILES.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../contracts/common/spatial_geometry.md
  - ../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../schemas/contracts/v1/receipts/
  - ../../../policy/geoprivacy/
  - ../../../policy/sensitivity/
  - ../../../policy/redaction/
  - ../../../data/quarantine/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/sensitive_geometry/README.md. It does not confirm executable sensitive-geometry validators, registry wiring, policy bundles, transform implementation, receipt emission, or CI behavior."
  - "Sensitive geometry validation is a routing/checking lane. It must not store exact geometry, publish public geometry, define redaction parameters, create receipts, decide policy, approve release, or authorize public surfaces."
  - "No exact coordinates, restricted identifiers, redaction radii, grid sizes, geohash precision, reconstruction thresholds, hidden policy values, or other reverse-engineering hints belong in this README or in repository-facing validator documentation."
  - "Public-safe geometry must be produced upstream by governed transforms and supported by receipts, policy, review, evidence, release, correction, and rollback posture before public use."
  - "Style-only hiding is forbidden: public renderers must receive public-safe geometry, not exact/internal geometry hidden by zoom, opacity, layer filters, styling, or UI affordances."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/sensitive_geometry

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-sensitive--geometry--validator-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-exact--location--deny--default-critical)
![posture](https://img.shields.io/badge/posture-most--restrictive--wins-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/sensitive_geometry/` is the sensitive-geometry validator routing index for checking exact-location denial, public-safe geometry posture, geoprivacy/redaction/aggregation receipt linkage, reverse-engineering risk, policy/review/release support, correction/rollback propagation, and public-surface denial without storing sensitive geometry or becoming policy/release authority.

---

## Purpose

`tools/validators/sensitive_geometry/` exists to organize sensitive-geometry validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a geometry-bearing candidate preserve exact/internal geometry separation, public-safe geometry role, geoprivacy and sensitivity posture, redaction/generalization/aggregation receipt linkage, EvidenceRef and EvidenceBundle support, policy/review/release state, correction and rollback paths, and public-surface denial before it reaches catalog, proof, release, map, API, graph, tile, search, export, Focus Mode, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result or routing decision. This folder should not define geometry semantics, store geometry payloads, perform redaction transforms as authority, define geoprivacy policy parameters, create RedactionReceipts, create AggregationReceipts, create EvidenceBundles, store proofs, store receipts, decide policy, approve release, publish map layers, expose public API payloads, or authorize AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/sensitive_geometry/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/geoprivacy/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Broad geoprivacy validator routing index for sensitive-location, public-safe geometry, reverse-engineerable derivative, most-restrictive-policy, receipt, evidence, policy, release, correction, rollback, and public-surface denial checks. |
| `tools/validators/geometry/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Shared geometry-carrier validator lane for common geometry shape, CRS, precision bucket, geometry role, validity/topology, sensitivity/geoprivacy, evidence, policy, release, correction, rollback, and public-surface denial. |
| `docs/standards/REDACTION_PROFILES.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Redaction profiles are named, versioned, deterministic, receipt-bearing policy artifacts; missing profiles fail closed. |
| `docs/architecture/sensitive-domain-fail-closed.md` | **CONFIRMED architecture doc / implementation NEEDS VERIFICATION** | Sensitive lanes fail closed by default; public derivatives require explicit, evidenced, receipted, reviewed, and policy-allowed transforms. |
| `tools/validators/geology/public_safe_geometry/README.md` | **CONFIRMED domain example / executable behavior NEEDS VERIFICATION** | Domain-specific public-safe geometry lane that separates exact/internal geometry from public-safe geometry and defers policy/release authority. |
| Executable sensitive-geometry scripts, registry wiring, schema bindings, policy bundles, redaction profiles, fixture coverage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Sensitive-geometry validator routing | `tools/validators/sensitive_geometry/` | Umbrella route for exact-location exposure, public-safe geometry, side-channel, and sensitive-geometry release checks. |
| Broad geoprivacy routing | `tools/validators/geoprivacy/` | Geoprivacy-specific validator index and child lanes. |
| Shared geometry carrier checks | `tools/validators/geometry/` | Common shape/CRS/precision/role checks, not public exposure authority. |
| Geoprivacy transform validation | `tools/validators/geoprivacy_transform/` | Transform-specific validation, when verified. |
| Domain public-safe geometry | Domain-specific lanes such as `tools/validators/geology/public_safe_geometry/` | Domain meaning and domain sensitivity rules remain domain-owned. |
| Map/tile public surfaces | `tools/validators/maplibre/`, `tools/validators/pmtiles/` | Renderer and tile artifacts consume only release-supported public-safe geometry. |
| Redaction profile standard and policy | `docs/standards/REDACTION_PROFILES.md`, `policy/redaction/`, `policy/geoprivacy/`, `policy/sensitivity/` | Policy parameters and redaction profile authority do not belong in validators. |
| Geometry contract and schema | `contracts/common/spatial_geometry.md`, `schemas/contracts/v1/common/spatial_geometry.schema.json` | Contracts/schemas define meaning and shape. |
| Evidence/proofs/receipts/release | `data/proofs/`, `data/receipts/`, `release/` | Validators check references; they do not create authority records. |

[Back to top](#top)

---

## Sensitive geometry scope

Sensitive geometry includes any coordinate, geometry, topology, extent, tile, graph relation, join result, label placement, search result, screenshot, cached derivative, or generated description that could reveal, narrow, reconstruct, infer, or operationalize a restricted place.

Common sensitive-geometry families include:

- exact rare fauna or flora occurrences, nests, dens, roosts, hibernacula, spawning places, collection sites, or protected habitats;
- archaeology, burial, sacred, cultural heritage, collection-storage, looting-risk, or steward-controlled places;
- critical infrastructure, dependencies, vulnerabilities, operational condition, continuity routes, or asset-level exposure;
- living-person, DNA/genomic, private parcel/person, residence, family graph, land-interest, or consent-revocation-sensitive locations;
- sensitive geology or resource-targeting points, boreholes, private wells, samples, restricted subsurface details, or private operator/parcel joins;
- hazards, security, medical, legal, title, engineering, or operational contexts where precise location could be misconstrued as official guidance or expose risk;
- any join, derivative, aggregation, tile pyramid, map screenshot, label, search result, vector index, graph edge, or AI answer that can reconstruct one of the above.

Do not add exact coordinates, redaction parameters, grid values, threshold values, or reconstruction recipes to this README.

[Back to top](#top)

---

## Validation focus

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Exact/internal geometry | Is exact geometry denied from public surfaces and kept separate from public-safe geometry? | Public display geometry. |
| Public-safe geometry role | Is the candidate explicitly marked generalized, redacted, aggregated, suppressed, public-safe, or denied according to accepted policy? | Proof that publication is allowed. |
| Geometry carrier | Does the candidate satisfy common geometry shape, CRS, precision, geometry role, topology, uncertainty, and scale posture? | Domain meaning or release readiness by itself. |
| Sensitivity/geoprivacy | Does the candidate preserve most-restrictive sensitivity posture and route policy decisions to policy roots? | Local validator discretion. |
| Redaction/generalization/aggregation receipts | Are transform receipts present, resolvable, and tied to the correct input/output lineage where required? | Redaction performed by this README. |
| Reverse-engineering risk | Could the output, join, tile, label, screenshot, search result, graph edge, export, embedding, or AI answer reconstruct restricted geometry? | A visual-only concern. |
| Side-channel risk | Do style rules, zoom levels, feature counts, extents, bounds, labels, hover states, logs, cache keys, ids, or errors leak sensitive geometry? | Cosmetic UI bug. |
| Public-surface readiness | Are evidence, policy, review, release, correction, rollback, and rights/sensitivity obligations closed before exposure? | Map/tile/API existence as approval. |

[Back to top](#top)

---

## Invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Exact geometry is denied by default | Exact/internal sensitive geometry remains unavailable to public clients and normal UI surfaces. | Public surface can access exact/internal geometry or source geometry. |
| Public-safe geometry is a derivative | Public geometry is produced upstream by governed transforms and supported by receipts, evidence, policy, review, release, correction, and rollback posture. | Candidate treats exact geometry as public with style-only hiding. |
| Most restrictive wins | Joins and derivatives inherit the strictest upstream sensitivity, rights, consent, and release posture. | A derivative weakens or drops upstream restrictions. |
| Receipts are required where transforms matter | Redaction, generalization, aggregation, suppression, tiling, or public-safe projection is receipt-backed where material. | Transform exists without resolvable receipt, profile id, reason, or lineage. |
| No hidden parameter leakage | Public docs and validator outputs do not expose exact coordinates, restricted ids, sensitive thresholds, or reconstruction hints. | README, report, fixture, log, or error message leaks unsafe detail. |
| Carriers are not evidence | Tiles, maps, screenshots, exports, graphs, labels, popups, embeddings, and AI answers are downstream carriers. | Carrier is treated as source truth, evidence closure, or policy approval. |
| Correction and rollback propagate | Rights changes, sensitivity changes, revocations, corrections, withdrawals, and rollbacks invalidate downstream geometry carriers. | Public artifacts remain active after a blocking change. |

[Back to top](#top)

---

## Fail-closed conditions

A sensitive-geometry candidate should fail closed, deny, restrict, abstain, or route to steward review when:

- exact/internal/source geometry is present in a public-bound payload;
- geometry role, CRS, precision/exposure posture, sensitivity tier, rights posture, or source role is missing or unresolved;
- required redaction, generalization, aggregation, suppression, or public-safe transform receipt is absent or unresolved;
- required policy bundle, PolicyDecision, ReviewRecord, steward review, release reference, correction path, rollback target, or withdrawal posture is absent;
- geometry is sensitive because of a join, derivative, label, tile extent, screenshot, search result, vector embedding, graph edge, or AI answer even when the source input was not obviously sensitive;
- output geometry, feature counts, bounds, tiles, labels, hover state, cache key, id, filename, log, or error message can reconstruct restricted geometry;
- public rendering relies on zoom thresholds, opacity, filters, style layers, hidden columns, or client-side controls instead of upstream public-safe derivatives;
- source rights, consent, stewardship, or sensitivity posture conflicts with the intended geometry use;
- the candidate attempts to publish, export, screenshot, index, tile, embed, summarize, or answer from unreleased or rights/sensitivity-restricted geometry.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Sensitive-geometry validator routing | `tools/validators/sensitive_geometry/` |
| Shared geoprivacy routing | `tools/validators/geoprivacy/` |
| Shared geometry carrier validation | `tools/validators/geometry/` |
| Domain-specific public-safe geometry gates | domain validator lanes under `tools/validators/` |
| Geometry semantics | `contracts/common/spatial_geometry.md`, domain contracts, and domain docs |
| Machine schemas | `schemas/contracts/v1/common/`, `schemas/contracts/v1/receipts/`, domain schema homes |
| Redaction/geoprivacy/sensitivity policy | `policy/redaction/`, `policy/geoprivacy/`, `policy/sensitivity/`, accepted policy homes |
| Redaction/profile standards | `docs/standards/REDACTION_PROFILES.md` and related standards |
| Sensitive-domain doctrine | `docs/architecture/sensitive-domain-fail-closed.md` and domain docs |
| Lifecycle and quarantine data | `data/quarantine/` and other `data/` lifecycle roots |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release records | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared sensitive-geometry invariants and delegates policy, transform parameters, geometry semantics, schemas, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, redaction profile homes, policy bundle homes, schema ids, fixture files, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as exact-geometry storage, public geometry store, redaction implementation authority, geoprivacy policy home, sensitivity policy home, receipt store, proof store, release record store, canonical schema home, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/sensitive_geometry/` include:

- this README;
- small validation adapters that check sensitive-geometry readiness and public-surface denial;
- checks for exact/internal vs public-safe geometry separation;
- checks for redaction/generalization/aggregation/suppression receipt linkage;
- checks for reverse-engineerable derivatives, side-channel exposure, and most-restrictive propagation;
- routing notes for geoprivacy, geometry, redaction, MapLibre, PMTiles, policy, rights, release, and domain-specific validators;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of geometry, receipt, proof, policy, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Exact coordinates, restricted-source-derived fields, source geometry payloads, public geometry payloads, tile payloads, screenshots, exports, embeddings, or map artifacts | governed `data/`, `release/`, artifact, or runtime homes after policy/release review |
| Redaction profile parameters, thresholds, radii, grid sizes, geohash precision, hidden policy values, or reconstruction recipes | `policy/` and steward-gated standards, never repository-facing validator docs |
| RedactionReceipts, AggregationReceipts, RunReceipts, ValidationReports, proof packs, EvidenceBundles | `data/receipts/`, `data/proofs/`, accepted report lanes |
| Policy rules, allow/deny/restrict/abstain decisions, sensitivity tier decisions, steward approvals | `policy/`, `release/`, steward review homes |
| Canonical schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/...` or accepted schema homes |
| Semantic contracts | `contracts/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SENSITIVE_GEOMETRY_VALIDATOR_PASS` | Candidate passed configured sensitive-geometry checks. |
| `SENSITIVE_GEOMETRY_VALIDATOR_FAIL` | Candidate failed one or more configured checks. |
| `SENSITIVE_GEOMETRY_VALIDATOR_DENY` | Candidate must not proceed because sensitive-geometry, policy, evidence, receipt, release, correction, rollback, rights, or public-surface support cannot be resolved. |
| `SENSITIVE_GEOMETRY_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SENSITIVE_GEOMETRY_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a safe geometry assertion. |
| `EXACT_GEOMETRY_PUBLIC_DENIED` | Exact/internal sensitive geometry appears in a public-bound surface. |
| `GEOMETRY_ROLE_MISSING` | Required geometry role is absent or unresolved. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Public-safe derivative geometry is required but absent. |
| `REDACTION_RECEIPT_MISSING` | Required redaction/generalization/aggregation/suppression receipt is absent. |
| `REDACTION_PROFILE_UNRESOLVED` | Required redaction profile reference is absent, revoked, stale, or unsupported. |
| `SENSITIVITY_POSTURE_UNRESOLVED` | Sensitivity/geoprivacy posture is missing or conflicted. |
| `MOST_RESTRICTIVE_POLICY_NOT_PRESERVED` | Join or derivative weakens upstream restrictions. |
| `RECONSTRUCTION_RISK_DENIED` | Candidate can reconstruct or narrow sensitive geometry through derivative or side-channel exposure. |
| `STYLE_AS_POLICY_DENIED` | Candidate relies on styling, zoom, opacity, filter, or UI hiding instead of public-safe geometry. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `POLICY_OR_REVIEW_GAP` | Required policy decision, review state, rights posture, sensitivity posture, or obligation support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose sensitive geometry to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/sensitive_geometry/
├── README.md
├── validate_sensitive_geometry.py       # PROPOSED; not confirmed
├── validate_public_safe_geometry.py     # PROPOSED; not confirmed
├── validate_reconstruction_risk.py      # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, redaction profiles, local schema files, sensitive geometry payloads, public geometry payloads, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting public-surface or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/sensitive_geometry/README.md`.
- [x] It marks this path as sensitive-geometry validator routing, not exact-geometry storage, redaction implementation authority, geoprivacy policy authority, sensitivity policy authority, proof/receipt storage, release records, public runtime, or AI authority.
- [x] It preserves fail-closed posture for exact/internal geometry, missing public-safe derivatives, missing receipts, unresolved policy/review/release support, reverse-engineering risk, and style-as-policy shortcuts.
- [x] It routes geometry meaning to `contracts/`, machine shape to `schemas/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It avoids exact coordinates, restricted identifiers, redaction radii, grid sizes, geohash precision, reconstruction thresholds, and hidden policy values.
- [x] It marks executable scripts, registry wiring, redaction profile homes, policy bundles, schema files, fixtures, tests, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to sensitive-geometry validators are searched and classified.
- [ ] Accepted redaction/geoprivacy/sensitivity policy bundle homes, profile ids, and digest rules are verified.
- [ ] Receipt schemas and geometry schemas are verified against actual validators and fixtures.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes and no reconstruction hints.
- [ ] Tests prove positive, negative, deny, restrict, abstain, receipt-missing, exact-geometry-denied, reconstruction-risk, style-as-policy, and public-surface-blocked cases.
- [ ] CI invokes sensitive-geometry validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with sensitive-geometry validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
