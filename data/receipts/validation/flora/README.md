<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/receipts/validation/flora/readme
name: Flora Validation Receipts README
path: data/receipts/validation/flora/README.md
type: data-receipts-validation-domain-readme
version: v0.1.0
status: draft
owners:
  - <receipt-steward>
  - <validation-steward>
  - <flora-domain-steward>
  - <sensitivity-reviewer>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: flora-validation-receipts
receipt_scope: flora-validation-process-memory
domain: flora
path_posture: requested-validation-domain-receipt-lane; existing-target-blank-placeholder-replaced; exact-receipt-layout-needs-verification
sensitivity_posture: receipt-internal; no-public-path; process-memory-not-proof; validation-not-release; exact-location-deny-default; redaction-and-review-required; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../flora/README.md
  - ../../redaction/flora/README.md
  - ../../../proofs/citation_validation/flora/README.md
  - ../../../raw/flora/README.md
  - ../../../work/flora/README.md
  - ../../../quarantine/flora/README.md
  - ../../../processed/flora/README.md
  - ../../../../contracts/domains/flora/domain_validation_report.md
  - ../../../../contracts/domains/flora/flora_occurrence.md
  - ../../../../contracts/domains/flora/rare_plant_record.md
  - ../../../../contracts/domains/flora/redaction_receipt.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../../docs/domains/flora/PUBLICATION_AND_ROLLBACK.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../../../docs/standards/RUN_RECEIPT.md
  - ../../../../docs/architecture/directory-rules.md
tags:
  - kfm
  - data
  - receipts
  - validation
  - flora
  - domain-validation-report
  - rare-plant
  - geoprivacy
  - sensitivity
  - policy-preflight
  - review-record
  - no-public-path
  - evidence-first
notes:
  - "This README replaces a blank placeholder at `data/receipts/validation/flora/README.md`."
  - "Validation receipts record validator process memory and review support. They do not create Flora truth, approve public release, or replace proofs, catalogs, policy decisions, review records, or release manifests."
  - "Flora sensitivity doctrine denies exact rare, protected, or culturally sensitive plant locations on public surfaces by default and requires steward review, generalized or withheld geometry, and RedactionReceipt for public release."
  - "The Flora DomainValidationReport contract is draft/PROPOSED and records validation evidence and decision support; validator behavior and emitted reports remain NEEDS VERIFICATION unless proven by tests or run artifacts."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Validation Receipts

Validation receipt lane for Flora domain process-memory records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: receipts" src="https://img.shields.io/badge/family-receipts-purple">
  <img alt="Lane: validation" src="https://img.shields.io/badge/lane-validation-blue">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Boundary: not release authority" src="https://img.shields.io/badge/boundary-not%20release%20authority-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Receipt boundary](#receipt-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested receipt shape](#suggested-receipt-shape) · [Directory map](#directory-map) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/receipts/validation/flora/` is for Flora validation receipt process memory only. It is not Flora source truth, rare-plant authority, exact-location authority, sensitivity policy, proof, catalog closure, release approval, public artifact authority, public UI/API material, or generated-answer authority.

---

## Scope

This directory stores receipts and receipt-local sidecars emitted by bounded Flora validation work. A receipt in this lane records what a validator, dry run, fixture check, policy preflight, schema check, release-candidate check, correction check, or rollback check observed about Flora material at a specific run boundary.

Flora validation receipts may support review over:

- `FloraOccurrence`, `RarePlantRecord`, `RangePolygon`, `VegetationCommunity`, `PhenologyObservation`, `BotanicalSurvey`, `RestorationPlanting`, and related Flora object families;
- taxon/crosswalk integrity;
- source-role preservation and anti-collapse checks;
- EvidenceRef to EvidenceBundle closure checks;
- geometry validity, uncertainty, precision, redaction, and public-safe generalization checks;
- rare-plant, steward-controlled, private-land, culturally sensitive, and source-restricted material;
- rights, source terms, attribution, redistribution, and access-posture preflight checks;
- release-candidate readiness, correction posture, stale-state handling, and rollback readiness.

Receipts do **not** prove the Flora observation, authorize public exposure, approve exact geometry, or replace `EvidenceBundle`, `ProofPack`, `CatalogMatrix`, `PolicyDecision`, `ReviewRecord`, `RedactionReceipt`, `ReleaseManifest`, `CorrectionNotice`, or `RollbackCard` objects.

---

## Path posture

`data/receipts/` is the receipt family root for process memory. The requested validation/domain lane is:

```text
data/receipts/validation/flora/
```

This README documents the requested lane without claiming final receipt-layout authority. The Flora parent receipt lane is also present at:

```text
data/receipts/flora/
```

The redaction-specific Flora receipt lane is present at:

```text
data/receipts/redaction/flora/
```

The exact choice between subtype-first lanes such as `data/receipts/validation/<domain>/` and domain-first lanes such as `data/receipts/<domain>/validation/` remains **NEEDS VERIFICATION** until accepted receipt-layout governance or ADR review confirms the pattern.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/receipts/validation/flora/` |
| Responsibility root | `data/` |
| Artifact family | receipts |
| Receipt subtype | validation process memory |
| Domain lane | flora |
| Related semantic contract | `contracts/domains/flora/domain_validation_report.md` |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Lifecycle payload authority | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, and `data/processed/flora/`, not this lane |
| Redaction receipt authority | `data/receipts/redaction/flora/` or accepted redaction receipt lane, not this validation lane |
| Proof authority | `data/proofs/`, not this lane |
| Citation-validation proof support | `data/proofs/citation_validation/flora/`, not this lane |
| Catalog authority | `data/catalog/`, not this lane |
| Release authority | `release/`, not this lane |
| Published artifacts | `data/published/`, not this lane |
| Policy authority | `policy/`, `policy/sensitivity/flora/`, and `policy/geoprivacy/`, not this lane |
| Default failure posture | `FAIL`, `DENY`, `ABSTAIN`, `HOLD`, `NEEDS_REVIEW`, `QUARANTINE`, or `ERROR` when evidence, source role, rights, sensitivity, redaction, review, validation, correction, rollback, or release state is unresolved |

---

## Receipt boundary

| Rule | Handling |
|---|---|
| Receipt is process memory | It records validation behavior and observed results; it is not Flora truth. |
| Validation is not release | A validation receipt can support review and promotion decisions; it cannot approve publication. |
| Sensitivity fails closed | Rare, protected, culturally sensitive, steward-controlled, private-land, or join-sensitive plant material remains blocked unless sensitivity, rights, redaction, review, and release support resolve. |
| Exact geometry stays protected | README and local indexes must not expose exact rare-plant coordinates, protected location details, restricted identifiers, generalization radii, fuzzing parameters, transform seeds, consent tokens, revocation tokens, or restricted steward notes. |
| Policy remains separate | Binding rights, sensitivity, geoprivacy, source-role, and release rules live in governed policy roots, not this receipt lane. |
| Review remains separate | Steward review, sensitivity review, rights-holder review, and release authority must remain visible and cannot collapse into validation output. |
| Proof remains separate | EvidenceBundle, ProofPack, CatalogMatrix, citation validation, and integrity proof belong in `data/proofs/`. |
| Catalog remains separate | STAC/DCAT/PROV and discovery records belong in `data/catalog/`. |
| Release remains separate | ReleaseManifest, promotion decision, CorrectionNotice, RollbackCard, withdrawal notice, signatures, and release changelog belong in `release/`. |
| Public clients never read receipts directly | Public outputs consume governed APIs and released artifacts, not receipt lanes. |

---

## Accepted material

Accepted content is limited to Flora validation receipt instances and receipt-local sidecars:

- `DomainValidationReport`, `ValidationReport`, validation-run receipts, fixture-check receipts, schema-check receipts, contract-check receipts, policy-preflight receipts, sensitivity-check receipts, correction-check receipts, rollback-check receipts, and release-candidate-check receipts;
- run IDs, validator refs, validator versions, ruleset refs, schema refs, policy refs, source refs, object refs, evidence refs, redaction receipt refs, review refs, release-candidate refs, correction refs, rollback refs, timestamps, actor/runner identity, finite outcomes, reason codes, blocker status, severity counts, input/output hashes, and signatures;
- public-safe validation summaries with sensitive details removed;
- receipt manifests, checksums, signing sidecars, and reproducibility notes where applicable;
- README files and local indexes that help stewards inspect validation receipt state without becoming proof, catalog, policy, release, public output, Flora truth, location authority, sensitivity policy, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora source payloads, exact sensitive coordinates, source-native files, private-land joins, or restricted identifiers | `data/raw/flora/` or governed restricted storage as applicable |
| Work/candidate outputs, scratch transforms, and unresolved validation experiments | `data/work/flora/` |
| Quarantined Flora material and unresolved sensitive records | `data/quarantine/flora/` |
| Processed Flora payloads or generalized public-safe layers | `data/processed/flora/` after gates; `data/published/` only after release |
| Redaction/generalization/suppression process memory | `data/receipts/redaction/flora/` or accepted redaction receipt lane |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation closure, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, or domain discovery records | `data/catalog/` |
| SourceDescriptor records or source activation decisions | `data/registry/sources/flora/` |
| ReleaseManifest, promotion decision, correction notice, rollback card, withdrawal notice, signature, or release changelog | `release/` |
| Sensitivity, geoprivacy, rights, sovereignty, CARE, consent, revocation, source-role, publication, or release policy | `policy/` and governed policy roots |
| Semantic contracts and schemas | `contracts/` and `schemas/` |
| Validator code, fixtures, package code, tests, or CI workflows | `tools/`, `fixtures/`, `packages/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, species pages, graph edges, vector-index content, or generated answer text | governed public outputs only after evidence, policy, validation, review, release, correction, and rollback gates close |

---

## Suggested receipt shape

The exact machine schema remains **NEEDS VERIFICATION** until accepted schema and validator evidence exists. A Flora validation receipt should remain structured enough to support audit, review, correction, and rollback.

```json
{
  "id": "kfm:receipt:validation:flora:<run-id>",
  "domain": "flora",
  "receipt_type": "validation",
  "report_type": "schema|contract|fixture|source_registry|evidence|policy_preflight|sensitivity|release_candidate|correction|rollback|composite",
  "run_ref": "<pipeline-or-ci-run-ref>",
  "validator_ref": "<validator-or-ruleset-ref>",
  "validator_version": "<version-or-hash>",
  "ruleset_refs": [],
  "schema_refs": [],
  "policy_refs": [],
  "subject_refs": [],
  "input_hashes": {},
  "outcome": "PASS|WARN|FAIL|ABSTAIN|DENY|ERROR",
  "promotion_blocking": true,
  "severity_counts": {
    "info": 0,
    "warn": 0,
    "fail": 0,
    "deny": 0,
    "error": 0
  },
  "evidence_resolution_summary": {},
  "source_role_summary": {},
  "sensitivity_summary": {},
  "geometry_summary": {},
  "taxon_summary": {},
  "temporal_summary": {},
  "rights_summary": {},
  "release_summary": {},
  "redaction_receipt_refs": [],
  "review_record_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_summary": "<sensitive-details-redacted>",
  "created_at": "<ISO-8601 timestamp>"
}
```

> [!NOTE]
> This example is documentation guidance, not a committed run receipt and not a schema contract. Store real receipts only when emitted by a governed validator, CI run, pipeline run, or documented manual smoke check.

---

## Directory map

```text
data/receipts/validation/flora/
├── README.md
├── <run_id>/
│   ├── validation_receipt.json
│   ├── domain_validation_report.json
│   ├── findings.jsonl
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

This map is a proposed receipt-lane shape for documentation. It does not prove emitted validation receipts, validators, fixtures, CI checks, signing, policy enforcement, review workflow, correction hooks, rollback hooks, release integration, or public-safe summaries exist.

`index.local.json` is optional and receipt-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, location authority, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the receipt belongs to the Flora domain and validation receipt lane.
- [ ] Confirm canonical validation/domain receipt naming against accepted receipt-layout governance before relying on this path as final layout authority.
- [ ] Confirm receipt ID, run ID, validator ref, ruleset refs, schema refs, policy refs, subject refs, evidence refs, input hashes, timestamps, actor/runner identity, outcome, blocker status, and signatures are present where applicable.
- [ ] Confirm rare-plant exact coordinates, protected or culturally sensitive plant locations, private-land joins, restricted identifiers, and steward-only notes are not exposed in README/index/public-summary text.
- [ ] Confirm validation did not silently upgrade source roles such as modeled, aggregate, candidate, synthetic, administrative, or inferred records into observed fact.
- [ ] Confirm EvidenceRef/EvidenceBundle resolution is reported for consequential claims.
- [ ] Confirm rights, sensitivity, geoprivacy, review, correction, rollback, and release states are recorded where the receipt supports a public-safe derivative or release candidate.
- [ ] Confirm RedactionReceipt and ReviewRecord references exist before any rare, protected, or culturally sensitive plant material moves toward a more-public tier.
- [ ] Confirm receipt presence is not treated as Flora truth, location authority, sensitivity policy, proof, catalog closure, release approval, or public artifact authority.
- [ ] Confirm no public artifact, graph edge, search index, vector index, API payload, species page, generated answer, or released layer uses this receipt lane as truth directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces a blank placeholder at `data/receipts/validation/flora/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a blank placeholder before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/receipts/flora/README.md` exists as the Flora domain parent receipt README. | CONFIRMED by GitHub contents API during this edit |
| `data/receipts/redaction/flora/README.md` exists as a Flora redaction receipt README. | CONFIRMED by GitHub contents API during this edit |
| `contracts/domains/flora/domain_validation_report.md` exists as a draft semantic contract for Flora validation reports. | CONFIRMED by GitHub contents API during this edit |
| Emitted Flora validation receipt payloads exist under this folder. | UNKNOWN |
| CI currently emits Flora validation receipts into this folder. | UNKNOWN |
| Field-level machine enforcement for `DomainValidationReport` is complete. | NEEDS VERIFICATION |
| This README grants public access to Flora validation internals. | DENY |

---

## Maintainer note

Validation receipts are useful because they make validator runs inspectable and correctable. They are dangerous if they are treated as truth, policy, release authority, or public-safe content. Keep the chain explicit:

```text
validation receipt -> review input -> policy/proof/catalog/release checks -> governed public surface
```

Never collapse it into:

```text
validation receipt -> public Flora truth
```
