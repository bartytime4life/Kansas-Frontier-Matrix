<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geoprivacy-transform-readme
title: tools/validators/geoprivacy_transform README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geoprivacy-steward-plus-redaction-steward-plus-geometry-steward-plus-sensitivity-reviewer-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geoprivacy-transform-validator; public-safe-geometry; redaction; generalization; aggregation; buffering; gridding; suppression; transform-receipt-aware; fail-closed; deny-by-default; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Geoprivacy Transform validator lane for checking whether a sensitive-location candidate has a policy-authorized public-safe transform, non-reversible geometry posture, transform receipt linkage, no threshold leakage, produced-geometry inspection, most-restrictive-policy propagation, EvidenceRef/EvidenceBundle linkage, policy/review/release linkage, correction and rollback linkage, finite negative outcomes, and public-surface denial checks while deferring geoprivacy policy parameters, redaction/generalization/aggregation implementation, exact-location storage, evidence records, proof records, receipt creation, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../geoprivacy/README.md
  - ../geoprivacy/habitat-fauna/README.md
  - ../geometry/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../evidence/README.md
  - ../citation/README.md
  - ../evidence_bundle/README.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../contracts/common/spatial_geometry.md
  - ../../../schemas/contracts/v1/common/spatial_geometry.schema.json
  - ../../../schemas/contracts/v1/receipts/
  - ../../../policy/geoprivacy/
  - ../../../policy/sensitivity/
  - ../../../policy/domains/
  - ../../../data/receipts/README.md
  - ../../../data/receipts/fauna/redaction/README.md
  - ../../../data/receipts/flora/redaction/README.md
  - ../../../data/proofs/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Geoprivacy parent evidence says geoprivacy validators prevent exact, sensitive, restricted, or reverse-engineerable location exposure and must not create policy thresholds, perform transforms, create RedactionReceipts, decide policy, approve release, or publish outputs."
  - "Habitat geoprivacy evidence says exact generalization radii, grid sizes, geohash precisions, and precision thresholds are steward-gated policy values; placing them in public docs would itself be a sensitivity leak."
  - "Habitat geoprivacy evidence says validators evaluate produced geometry, not just inputs; sensitive joins fail closed, and most-restrictive disposition applies."
  - "Receipt evidence says receipts live under data/receipts/ as process memory and do not prove truth, approve publication, replace evidence, close catalog, or become public artifacts by themselves."
  - "This validator lane may check that a transform receipt is required, present, linked, and routed to an accepted root; it must not create the receipt locally or expose transform parameters."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geoprivacy_transform

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-geoprivacy--transform--validator-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-thresholds--withheld-critical)
![posture](https://img.shields.io/badge/posture-receipt--aware-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geoprivacy_transform/` is the proposed validator lane for checking that a sensitive-location transform is policy-authorized, non-reversible, receipted, review-linked, release-linked, and safe for the requested governed surface.

---

## Purpose

`tools/validators/geoprivacy_transform/` exists for geoprivacy transform readiness checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Has a sensitive-location candidate been transformed into a public-safe derivative using an allowed transform class, without leaking policy thresholds or exact locations, with produced-geometry inspection, transform receipt linkage, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before use by catalog, proof, release, map, API, graph, tile, search, export, Focus Mode, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result. This folder should not perform redaction, generalization, aggregation, buffering, gridding, suppression, geohashing, or masking; store exact locations; define transform thresholds; create RedactionReceipts or AggregationReceipts; create EvidenceBundles; store proofs; store receipts; decide policy; approve release; publish map layers; expose public API payloads; or authorize AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geoprivacy_transform/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Geoprivacy parent index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/README.md` is the broad routing index for sensitive-location, public-safe geometry, reverse-engineerable derivative, and most-restrictive-policy checks. |
| Habitat-Fauna geoprivacy child lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/habitat-fauna/README.md` checks one domain-specific join/derivative geoprivacy case. |
| Habitat geoprivacy transform doctrine | **CONFIRMED in repo evidence / draft** | Habitat geoprivacy docs describe transform mechanics but keep radii, grid sizes, geohash precision, and thresholds in steward-gated policy bundles. |
| Receipt root boundary | **CONFIRMED in repo evidence / draft** | `data/receipts/README.md` says receipts are process memory and are not proof, not catalog, not release, and not public artifacts by themselves. |
| Geoprivacy-transform executable, schemas, fixtures, policy bundles, transform receipt shapes, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, threshold binding, transform implementation, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Geoprivacy-transform validator lane | `tools/validators/geoprivacy_transform/` |
| Broad geoprivacy routing index | `tools/validators/geoprivacy/` |
| Domain-specific geoprivacy child lanes | `tools/validators/geoprivacy/*/` |
| Shared geometry carrier checks | `tools/validators/geometry/` |
| Cross-domain join validation | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Geoprivacy and sensitivity policy parameters | `policy/geoprivacy/`, `policy/sensitivity/`, `policy/domains/`, or accepted policy homes |
| Transform receipt instances | `data/receipts/` and accepted receipt subtype lanes |
| Evidence/proof support | `data/proofs/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Domain meaning | `docs/domains/`, `contracts/domains/` |
| Common geometry meaning | `contracts/common/spatial_geometry.md` |

This README does not move, replace, or override those roots. It only defines where geoprivacy-transform readiness validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and policy bundle bindings are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Transform class | Is the candidate using an allowed transform class such as redaction, generalization, aggregation, buffering, gridding, masking, suppression, withholding, or abstention? | Permission to publish. |
| Threshold confidentiality | Are radii, grid sizes, geohash precisions, and reconstruction thresholds omitted from public docs, public fixtures, and public outputs? | Documentation detail. |
| Produced geometry | Does the produced geometry actually prevent reconstruction, not just rename the source layer? | Input-only validation. |
| Non-reversibility posture | Could the transform be reversed by tiles, screenshots, graph edges, search results, exports, embeddings, Focus Mode, or AI text? | Safe because exact coordinates were removed. |
| Transform receipt | Is a RedactionReceipt, AggregationReceipt, or equivalent governed receipt linked where required? | The transform itself or proof of truth. |
| Policy linkage | Is the transform class authorized by the applicable policy bundle and most-restrictive disposition? | A local validator decision. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, ReviewRecords, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |
| Output destination | Are reports and receipts routed to accepted roots and not mixed with source payloads, proofs, releases, or public artifacts? | Convenience path selection. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Geoprivacy-transform validator lane | `tools/validators/geoprivacy_transform/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Broad geoprivacy validator routing | `tools/validators/geoprivacy/` |
| Shared geometry validation | `tools/validators/geometry/` |
| Domain-specific validators | `tools/validators/<domain>/`, `tools/validators/domains/<domain>/`, or accepted domain validator homes |
| Domain doctrine and contracts | `docs/domains/`, `contracts/domains/` |
| Common geometry contract | `contracts/common/spatial_geometry.md` |
| Geoprivacy/sensitivity policy and transform parameters | `policy/geoprivacy/`, `policy/sensitivity/`, `policy/domains/`, `policy/` |
| Redaction/Aggregation/Validation receipts | `data/receipts/` |
| Evidence/proof support | `data/proofs/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geoprivacy_transform/`, `tests/validators/geoprivacy/`, `fixtures/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared transform class, threshold confidentiality, produced-geometry, non-reversibility, receipt-linkage, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, policy bundle binding, transform-class vocabulary, receipt schema, fixture shape, report destinations, receipt emission, release integration, tile/search/graph/vector/AI leakage checks, runtime behavior, and CI wiring.
- **DENY:** using this folder as geoprivacy policy threshold store, exact-location store, redaction/generalization/aggregation implementation, schema home, source registry, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geoprivacy_transform/` include checks that:

- verify a candidate has an allowed transform class for the sensitivity tier, surface, audience, source terms, and domain context;
- verify public docs and fixtures do not disclose thresholds, grid sizes, radii, geohash precision, or reconstruction-sensitive parameters;
- verify produced geometry is public-safe for the requested surface and cannot reconstruct sensitive locations through downstream derivatives;
- verify transform receipts are required, present, linkable, and stored under accepted receipt roots;
- verify most-restrictive policy, steward review, EvidenceRef/EvidenceBundle, release, correction, and rollback links exist where required;
- verify finite negative outcomes appear when transform evidence is incomplete;
- emit deterministic findings for downstream review without storing exact locations, running transforms, creating receipts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geoprivacy_transform/` | Correct home |
|---|---|
| Exact coordinates, precise geometries, site IDs, restricted source IDs, or identifiers that reveal location | restricted lifecycle lanes only; never public docs or public outputs |
| Generalization radii, grid sizes, geohash precisions, precision thresholds, reconstruction thresholds, or policy parameters | steward-gated `policy/` bundles |
| Redaction, generalization, aggregation, buffering, gridding, masking, or suppression implementation | `packages/`, `pipelines/`, or accepted implementation roots |
| RedactionReceipts, AggregationReceipts, validation reports, proofs, EvidenceBundles | `data/receipts/`, `data/proofs/` |
| Domain object meaning | `docs/domains/`, `contracts/domains/` |
| SourceDescriptor or source registry records | `data/registry/sources/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures with exact sensitive locations or transform thresholds | public-safe synthetic fixtures under accepted test roots |

[Back to top](#top)

---

## Geoprivacy-transform validator posture

Geoprivacy-transform validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks sensitivity classification, geoprivacy status, transform class, geometry role, public-safe transform posture, transform receipt, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- exposes or stores exact sensitive locations, restricted identifiers, transform thresholds, grid sizes, radii, geohash precisions, or reconstruction parameters in public docs, fixtures, reports, or outputs;
- uses a transform that is reversible, too precise, unreceipted, unreviewed, policy-incompatible, stale, superseded, withdrawn, or not authorized for the requested audience/surface;
- applies a weaker policy than the most restrictive applicable input, join, derivative, audience, or surface requires;
- hides reconstruction risk in tiles, screenshots, graph edges, search results, exports, embeddings, Focus Mode cards, or AI answers;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure;
- treats transform validation as SourceDescriptor creation, EvidenceBundle creation, RedactionReceipt creation, PolicyDecision creation, release approval, publication, public API behavior, steward approval, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `GEOPRIVACY_TRANSFORM_PASS` | Configured geoprivacy-transform checks passed. |
| `GEOPRIVACY_TRANSFORM_FAIL` | One or more configured geoprivacy-transform checks failed. |
| `TRANSFORM_CLASS_MISSING` | Required transform class is absent. |
| `TRANSFORM_CLASS_UNSUPPORTED` | Transform class is not accepted for the requested use. |
| `TRANSFORM_THRESHOLD_LEAK` | Public docs, fixtures, reports, or outputs expose thresholds, radii, grids, geohash precision, or reconstruction parameters. |
| `PRODUCED_GEOMETRY_UNSAFE` | Produced geometry can reveal or reconstruct sensitive location detail. |
| `NON_REVERSIBILITY_GAP` | Transform is reversible or lacks non-reversibility support. |
| `GEOPRIVACY_TRANSFORM_RECEIPT_MISSING` | Required transform receipt is absent or unresolved. |
| `TRANSFORM_RECEIPT_DESTINATION_INVALID` | Transform receipt is stored outside an accepted receipt root. |
| `TRANSFORM_POLICY_GAP` | Policy bundle, most-restrictive disposition, steward review, or allowed transform class is unresolved. |
| `SURFACE_RECONSTRUCTION_RISK` | Map/tile/search/graph/export/screenshot/vector/AI surface can narrow a protected location. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, public-safe transform, receipt linkage, evidence closure, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/geoprivacy_transform/
├── README.md
├── test_geoprivacy_transform_validator.py
└── fixtures/
    ├── valid_public_safe_transform/
    ├── missing_transform_class/
    ├── unsupported_transform_class/
    ├── transform_threshold_leak/
    ├── produced_geometry_unsafe/
    ├── non_reversibility_gap/
    ├── missing_transform_receipt/
    ├── invalid_receipt_destination/
    ├── surface_reconstruction_risk/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geoprivacy_transform
```

```bash
python tools/validators/geoprivacy_transform/validate_geoprivacy_transform.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_geoprivacy_transform.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts, schemas, geoprivacy policy, sensitivity policy, receipt records, evidence records, release records, and correction/rollback records rather than defining meaning locally.
- [ ] No exact coordinates, restricted identifiers, geoprivacy thresholds, grid sizes, radii, geohash precisions, or reconstruction parameters are added to public docs, fixtures, reports, or outputs.
- [ ] Produced geometry and downstream surfaces are evaluated, not just source inputs.
- [ ] Most-restrictive policy propagation is preserved across sources, joins, derivatives, audience, and surface.
- [ ] Public-safe geometry, transform receipt, steward review, policy decision, release manifest, correction path, and rollback target are present before public use.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, restricted exact/range material, direct internal stores, stale source descriptors, direct model outputs, unreceipted transforms, or incomplete proof closure.
- [ ] Reports and receipt references point only to accepted roots.
- [ ] Validator output is not described as truth, geoprivacy threshold authority, transform implementation, transform receipt creation, policy approval, release, publication, source admission, steward approval, public API behavior, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures and do not encode sensitive locations or reconstruction thresholds.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Geoprivacy Transform validator file. |
| Next smallest safe change | Verify actual geoprivacy-transform validator script path, policy bundle binding, accepted schemas, transform-class vocabulary, transform receipt shapes, fixture safety, report destination, receipt lookup, policy enforcement, release linkage, tile/search/graph/vector/AI leakage behavior, and CI/runtime wiring before promoting this lane beyond draft. |
