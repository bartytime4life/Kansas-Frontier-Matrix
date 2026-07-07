<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-catalog-closure-readme
title: tools/validators/catalog_closure README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-catalog-steward-plus-evidence-steward-plus-release-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; catalog-closure-validator-lane; proof-side-closure; release-gated
owning_root: tools/
responsibility: proposed validator lane for catalog-closure and CatalogMatrix-style proof-side readiness checks across source descriptors, catalog records, EvidenceBundles, policy posture, validation reports, release references, rollback/correction links, and lifecycle state
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../catalog/README.md
  - ../../../contracts/data/catalog_matrix.md
  - ../../../contracts/data/validation_report.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../data/catalog/
  - ../../../data/triplets/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../data/registry/
  - ../../../data/published/
  - ../../../release/
  - ../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../policy/data/
  - ../../../tests/
notes:
  - "This README documents a proposed catalog-closure validator lane. It does not confirm executable files."
  - "Catalog closure is proof-side/readiness validation. It is not the same as catalog discovery validation, receipt storage, release approval, or publication."
  - "Validators enforce declared contracts, schemas, policy, evidence references, release references, and correction links. They do not create EvidenceBundles, CatalogMatrix instances, ReleaseManifests, or public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/catalog_closure

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-catalog--closure--validators-informational)
![boundary](https://img.shields.io/badge/boundary-proof--side--readiness-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/catalog_closure/` is the proposed validator lane for catalog-closure readiness checks: CatalogMatrix-style coverage, source descriptors, catalog records, EvidenceBundles, validation reports, policy posture, review state, release references, correction lineage, rollback targets, and lifecycle-state consistency.

---

## Purpose

`tools/validators/catalog_closure/` exists for validators that answer whether a catalog-facing claim set is sufficiently closed for review, release consideration, or downstream governed use.

The durable KFM question for this lane is:

> Does a candidate catalog matrix or closure package prove that source, evidence, policy, review, release, correction, and lifecycle references are complete enough for the next governed state transition?

The answer should be a deterministic validation result. It should not create source truth, catalog truth, EvidenceBundles, CatalogMatrix instances, PolicyDecisions, ReleaseManifests, public artifacts, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/catalog_closure/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Catalog-closure validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| CatalogMatrix contract | **CONFIRMED in repo evidence / draft** | `CatalogMatrix` is a semantic descriptor for catalog/evidence/source relationships and release readiness; it is not proof closure by itself. |
| Artifact-family separation | **CONFIRMED in repo evidence / proposed ADR** | ADR-0011 separates receipts, proofs, catalog, and manifests/publication, and places `CatalogMatrix` on the proof-side closure boundary. |
| Paired schema | **CONFIRMED placeholder / NEEDS VERIFICATION** | `catalog_matrix.schema.json` is referenced as a placeholder; stronger semantics, fixtures, and validators need verification. |
| Release/public exposure wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove release gates, public API behavior, or CI wiring. |

[Back to top](#top)

---

## Relationship to `catalog/`

`tools/validators/catalog/` validates catalog records and discovery/interchange entries.

`tools/validators/catalog_closure/` validates closure readiness around those records: whether the matrix of catalog entries, source descriptors, evidence support, policy posture, validation reports, release references, rollback targets, and correction links is complete enough to proceed.

Both lanes must preserve the family split:

```text
receipt != proof != catalog != publication
```

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Catalog-closure validator entrypoints | `tools/validators/catalog_closure/` |
| Catalog-record validator entrypoints | `tools/validators/catalog/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Catalog records and indexes | `data/catalog/` |
| CatalogMatrix meaning | `contracts/data/catalog_matrix.md` |
| CatalogMatrix schema | `schemas/contracts/v1/data/catalog_matrix.schema.json` or ADR-selected schema home |
| EvidenceBundle and proof support | `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Source descriptors | `data/registry/` or accepted source registry roots |
| Release decisions, release manifests, rollback, corrections | `release/` |
| Published public-safe artifacts | `data/published/` |
| Policy rules | `policy/` |
| Tests and fixtures | `tests/` and accepted fixture conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared CatalogMatrix, closure, policy, evidence, and release-reference rules.
- **NEEDS VERIFICATION:** exact executable names, schema strength, fixtures, policy bundles, source registry shape, release integration, and CI wiring.
- **DENY:** using this folder as catalog storage, proof storage, receipt storage, source registry, release record storage, published artifact storage, contract home, schema home, policy home, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/catalog_closure/` include checks that:

- validate CatalogMatrix-style row, column, and cell completeness;
- require each consequential catalog entry to resolve to source descriptors and evidence/proof references;
- require validation reports for schema, policy, source-role, lifecycle, and sensitivity checks;
- require policy posture for release-bound or public-bound entries;
- require review-state, release-state, correction, supersession, withdrawal, and rollback references where material;
- confirm catalog closure does not point public surfaces at RAW, WORK, QUARANTINE, or unresolved candidates;
- confirm CatalogMatrix or closure summaries do not replace EvidenceBundles, ProofPacks, ReleaseManifests, or PolicyDecisions;
- detect drift between catalog records, triplets, proof bundles, and release references.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/catalog_closure/` | Correct home |
|---|---|
| Catalog records and indexes | `data/catalog/` |
| Catalog validator for simple discovery records | `tools/validators/catalog/` |
| CatalogMatrix instances | `data/proofs/catalog_matrix/` or accepted proof-side home |
| EvidenceBundles and ProofPacks | `data/proofs/` |
| Receipts | `data/receipts/` |
| Source descriptors | `data/registry/` |
| Release manifests or release decisions | `release/` |
| Public materialized artifacts | `data/published/` |
| Contracts | `contracts/` |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Tests and fixtures | `tests/` and fixture conventions |
| Catalog builder pipelines | `pipelines/` or accepted implementation root |

[Back to top](#top)

---

## Catalog-closure validation posture

Catalog-closure validators should fail closed, abstain, or route to review when a closure candidate:

- has catalog entries without source descriptors;
- has claim-bearing entries without evidence/proof support;
- has unresolved lifecycle state or skipped lifecycle stages;
- lacks validation reports for material schema/policy/evidence/source-role checks;
- lacks policy posture for rights, sensitivity, source-role, or public exposure;
- lacks review, release, correction, supersession, withdrawal, or rollback references where material;
- treats `CatalogMatrix` as proof closure by itself;
- treats catalog closure as release approval;
- exposes unreleased or unsafe candidates to public/governed clients.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `CATALOG_CLOSURE_PASS` | Configured catalog-closure checks passed. |
| `CATALOG_CLOSURE_FAIL` | Configured catalog-closure checks failed. |
| `MATRIX_SCHEMA_MISSING` | Required CatalogMatrix schema could not be resolved. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor reference is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `VALIDATION_REPORT_MISSING` | Required validation report is absent. |
| `POLICY_POSTURE_MISSING` | Required policy/sensitivity/rights/source-role posture is absent. |
| `REVIEW_STATE_MISSING` | Required review-state pointer is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release-state or ReleaseManifest pointer is absent. |
| `ROLLBACK_REFERENCE_MISSING` | Required rollback or correction path is absent. |
| `FAMILY_COLLAPSE` | Candidate treats catalog closure as receipt, proof, release, or publication. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed exposure as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/catalog_closure/
├── README.md
├── test_catalog_closure_validators.py
└── fixtures/
    ├── valid_catalog_matrix_closure/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── missing_validation_report/
    ├── missing_release_reference/
    ├── missing_rollback_reference/
    ├── family_collapse_matrix_as_release/
    └── public_closure_to_unreleased_candidate_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/catalog_closure
```

```bash
python tools/validators/catalog_closure/validate_catalog_closure.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_catalog_closure.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared CatalogMatrix contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] Catalog closure is kept separate from receipts, proofs, release records, and published artifacts.
- [ ] SourceDescriptor, EvidenceBundle, validation report, policy, review, release, correction, and rollback references are checked where required.
- [ ] Public-bound closure summaries do not point at RAW, WORK, QUARANTINE, or unresolved candidates.
- [ ] CatalogMatrix is treated as an inspectability aid, not proof closure or release approval by itself.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify CatalogMatrix schema strength, fixtures, policy bundles, source descriptor links, validator entrypoints, release references, and CI wiring before promoting this lane beyond draft. |
