<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-catalog-readme
title: tools/validators/catalog README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-catalog-steward-plus-evidence-steward-plus-release-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; catalog-validator-lane; discovery-not-truth; release-gated
owning_root: tools/
responsibility: proposed catalog validator lane for STAC, DCAT, PROV, domain catalog, catalog index, release-reference, evidence-reference, source-descriptor, policy-posture, correction, and lifecycle-boundary checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../data/catalog/README.md
  - ../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../contracts/data/catalog_matrix.md
  - ../../../contracts/data/validation_report.md
  - ../../../data/catalog/
  - ../../../data/triplets/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../data/registry/
  - ../../../data/published/
  - ../../../release/
  - ../../../schemas/
  - ../../../policy/
  - ../../../tests/
notes:
  - "This README documents a proposed catalog validator lane. It does not confirm executable files."
  - "Catalog records are discovery and interchange carriers. They are not receipts, proof records, release decisions, or publication by themselves."
  - "Validators enforce declared catalog contracts, schemas, policy, release links, and evidence references. They do not create catalog authority, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/catalog

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-catalog--validators-informational)
![boundary](https://img.shields.io/badge/boundary-discovery--not--truth-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/catalog/` is the proposed validator lane for catalog records and catalog indexes: STAC, DCAT, PROV, domain catalog entries, release references, source-descriptor links, evidence/proof links, policy posture, correction lineage, and lifecycle-boundary checks.

---

## Purpose

`tools/validators/catalog/` exists to hold catalog-specific validator entrypoints and helpers under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a catalog candidate describe governed data accurately without becoming source truth, proof support, release approval, or publication?

The answer should be a deterministic validation result. It should not create source truth, EvidenceBundles, receipts, release decisions, public artifacts, or catalog records by itself.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/catalog/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Catalog validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| `data/catalog/` boundary | **CONFIRMED in repo evidence / draft** | Catalog records are discovery/provenance projections, not truth, proof, receipts, or release authority. |
| Artifact-family separation | **CONFIRMED in repo evidence / proposed ADR** | ADR-0011 separates receipts, proofs, catalog, and manifests/publication. |
| Catalog schemas and fixtures | **NEEDS VERIFICATION** | STAC, DCAT, PROV, and domain catalog schema paths must be checked before implementation claims. |
| Release/public exposure wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove release gates, public API behavior, or CI wiring. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Catalog validator entrypoints | `tools/validators/catalog/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Catalog records and indexes | `data/catalog/` |
| Graph/triplet projection | `data/triplets/` |
| EvidenceBundle and proof support | `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Source descriptors | `data/registry/` or accepted source registry roots |
| Release decisions, release manifests, rollback, corrections | `release/` |
| Published public-safe artifacts | `data/published/` |
| Catalog contracts and schemas | `contracts/`, `schemas/` |
| Policy rules | `policy/` |
| Tests and fixtures | `tests/` and accepted fixture conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** catalog validator code may live here when it validates declared catalog contracts, schemas, policy, release references, and evidence pointers.
- **NEEDS VERIFICATION:** exact executable names, schema homes, fixture paths, STAC/DCAT/PROV conventions, source registry shape, and CI wiring.
- **DENY:** using this folder as catalog storage, source registry, proof storage, receipt storage, release record storage, published artifact storage, contract home, schema home, policy home, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/catalog/` include checks that:

- validate STAC catalog records against accepted KFM catalog requirements;
- validate DCAT catalog records against accepted KFM catalog requirements;
- validate PROV catalog records against accepted KFM catalog requirements;
- validate domain catalog entries and indexes;
- require source descriptor references where catalog records describe source-derived data;
- require EvidenceRef, EvidenceBundle, ProofPack, CatalogMatrix, or validation-report references where material;
- require release-state references before public exposure;
- check sensitivity, rights, source-role, and policy posture fields;
- check correction, supersession, withdrawal, and rollback references;
- ensure catalog records do not substitute for proof, release, or publication authority.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/catalog/` | Correct home |
|---|---|
| Catalog records and indexes | `data/catalog/` |
| Graph/triplet records | `data/triplets/` |
| EvidenceBundles, ProofPacks, CatalogMatrix instances | `data/proofs/` |
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

## Catalog validation posture

Catalog validators should preserve the family split:

```text
receipt != proof != catalog != publication
```

They should fail closed, abstain, or route to review when a catalog candidate:

- lacks required source descriptor references;
- lacks evidence/proof support for claims that need it;
- lacks release-state references for public exposure;
- treats a catalog record as proof or publication approval;
- omits sensitivity, rights, source-role, or policy posture where material;
- points at RAW, WORK, QUARANTINE, or unresolved candidate data from a public-facing catalog;
- lacks correction, supersession, withdrawal, or rollback references where required.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `CATALOG_VALIDATION_PASS` | Configured catalog checks passed. |
| `CATALOG_VALIDATION_FAIL` | Configured catalog checks failed. |
| `CATALOG_SCHEMA_MISSING` | Required catalog schema could not be resolved. |
| `SOURCE_DESCRIPTOR_MISSING` | Required source descriptor reference is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `PROOF_REFERENCE_MISSING` | Required proof support pointer is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release-state pointer is absent. |
| `POLICY_POSTURE_MISSING` | Required policy/sensitivity/rights/source-role posture is absent. |
| `FAMILY_COLLAPSE` | Candidate treats catalog as receipt, proof, release, or publication. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed catalog exposure as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/catalog/
├── README.md
├── test_catalog_validators.py
└── fixtures/
    ├── valid_stac_record/
    ├── valid_dcat_record/
    ├── valid_prov_record/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── missing_release_ref/
    ├── family_collapse_catalog_as_proof/
    └── public_catalog_to_unreleased_candidate_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/catalog
```

```bash
python tools/validators/catalog/validate_catalog_candidate.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_catalog_candidate.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared catalog contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] Catalog records are kept separate from receipts, proofs, release records, and published artifacts.
- [ ] SourceDescriptor, EvidenceBundle, proof, validation report, policy, and release references are checked where required.
- [ ] Public-bound catalog entries do not point at RAW, WORK, QUARANTINE, or unresolved candidates.
- [ ] Correction, supersession, withdrawal, and rollback references are checked where required.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify catalog schemas, STAC/DCAT/PROV conventions, fixtures, source descriptor references, validator entrypoints, and CI wiring before promoting this lane beyond draft. |
