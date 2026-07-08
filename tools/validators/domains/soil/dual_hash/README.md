<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-soil-dual-hash-readme
title: tools/validators/domains/soil/dual_hash README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-identity-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator; soil; dual-hash; spec-hash; provenance-hash; deterministic-identity; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed Soil-specific dual-hash validator lane for comparing canonical Soil record content hashes and provenance/source-lineage hashes across Soil catalog, proof, receipt, release, and derived-public-safe artifacts while deferring generic spec_hash computation to tools/spec_hash and Soil meaning, evidence, policy, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../_common/README.md
  - ../../../../spec_hash/README.md
  - ../catalog_closure/README.md
  - ../../../catalog_closure/README.md
  - ../../../cross-domain-joins/README.md
  - ../../../../../docs/architecture/identity-and-spec-hash.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../../docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/ROLLBACK_RUNBOOK.md
  - ../../../../../data/registry/sources/soil/
  - ../../../../../data/catalog/domain/soil/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Generic spec_hash computation remains tools/spec_hash/. This child lane is only for Soil-specific dual-hash validation policy and report posture."
  - "Dual-hash is PROPOSED here as a Soil validator pattern: compare canonical record/content hash with provenance/source-lineage hash or equivalent accepted pair. The exact field names, schema, algorithm pairing, and report envelope need verification before implementation claims."
  - "Soil dual-hash validation is not EvidenceBundle creation, receipt storage, proof storage, policy decision, release approval, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/soil/dual_hash

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--dual--hash-informational)
![hash](https://img.shields.io/badge/hash-spec--hash%20delegated-blueviolet)
![authority](https://img.shields.io/badge/authority-validator--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/soil/dual_hash/` is the proposed Soil-specific validator lane for checking paired content/provenance hash posture on Soil records, catalog entries, proof references, receipts, release candidates, and public-safe derivatives without replacing `tools/spec_hash/` or any evidence, policy, proof, receipt, or release authority.

---

## Purpose

`tools/validators/domains/soil/dual_hash/` exists for Soil-specific dual-hash checks that are narrower than the generic deterministic hashing helper at `tools/spec_hash/`.

The durable KFM question for this lane is:

> Does a Soil candidate carry a reproducible hash pair that proves both the canonical Soil record bytes and the declared source/provenance lineage have not drifted across catalog, proof, receipt, release, correction, rollback, and derived-public-safe surfaces?

The answer should be a deterministic validation result. This folder should not create Soil truth, source truth, identity truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/soil/dual_hash/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent `tools/validators/domains/soil/README.md` | **CONFIRMED stub** | Parent file currently says only `# validators :: soil`; this README keeps its own boundary explicit. |
| Generic spec-hash helper | **CONFIRMED in repo evidence / draft** | `tools/spec_hash/README.md` defines the generic helper lane for JCS canonicalization, SHA-256 digesting, stored-vs-recomputed comparison, and mismatch reporting. |
| Identity and spec-hash doctrine | **CONFIRMED in repo evidence / draft** | `docs/architecture/identity-and-spec-hash.md` defines `spec_hash` as RFC 8785 JCS plus SHA-256 and says mismatches fail closed at governance boundaries. |
| Soil lifecycle and canonical-path docs | **CONFIRMED in repo evidence / draft** | `docs/domains/soil/DATA_LIFECYCLE.md` and `CANONICAL_PATHS.md` provide the current inspected Soil lane evidence for lifecycle, object families, source families, placement, and verification posture. |
| Dual-hash schema, field names, algorithm pair, fixtures, and CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not claim that a dual-hash schema, executable, test fixture, receipt field, CI check, or runtime integration exists. |

[Back to top](#top)

---

## Relationship to `tools/spec_hash/`

Use this split:

| Concern | Preferred lane |
|---|---|
| Generic JCS canonicalization, SHA-256 digest computation, `jcs:sha256:<hex>` formatting, and stored-vs-recomputed hash comparison | `tools/spec_hash/` |
| Validator-of-record outcomes, policy-aware report posture, and fail-closed findings | `tools/validators/` and child lanes |
| Soil-specific paired hash checks over Soil record bytes and Soil source/provenance lineage | `tools/validators/domains/soil/dual_hash/` |
| Soil catalog closure that also checks evidence/policy/release completeness | `tools/validators/domains/soil/catalog_closure/` |
| Cross-domain hash checks across Soil × Agriculture, Soil × Hydrology, or Soil × Geology joins | `tools/validators/cross-domain-joins/` or an accepted cross-lane validator lane |

This README does not move, replace, or override `tools/spec_hash/`. A future validator here should call or conform to the accepted hash helper rather than reimplementing canonicalization silently.

[Back to top](#top)

---

## Proposed dual-hash meaning

Until a schema or ADR confirms exact field names, this README uses **dual-hash** as a proposed validation pattern, not a confirmed contract.

| Hash side | Proposed meaning | Must not be treated as |
|---|---|---|
| `content_hash` / `record_hash` | Digest of the canonical Soil record body, such as a SoilMapUnit, SoilComponent, Horizon, SoilProperty, derived Soil raster descriptor, catalog row, or release-candidate descriptor. | EvidenceBundle, receipt, release approval, or truth by itself. |
| `provenance_hash` / `lineage_hash` | Digest of the canonical source/provenance closure record, such as source descriptor IDs, source vintage, retrieval/run references, transform identifiers, source-role labels, and upstream EvidenceRef links. | Source authority, rights clearance, policy approval, or proof closure by itself. |

A future implementation may choose different names. The invariant is the pair: **one hash for canonical content, one hash for source/provenance closure**, with both recomputed and compared under accepted canonicalization rules.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Soil-specific dual-hash validator entrypoints | `tools/validators/domains/soil/dual_hash/` |
| Generic hash computation and comparison helpers | `tools/spec_hash/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Soil validator parent index | `tools/validators/domains/soil/` |
| Soil catalog closure validator | `tools/validators/domains/soil/catalog_closure/` |
| Soil domain meaning and doctrine | `docs/domains/soil/`, `contracts/domains/soil/`, `contracts/soil/`, or ADR-selected contract home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| Soil source descriptors | `data/registry/sources/soil/` or accepted source registry home |
| Soil catalog records | `data/catalog/domain/soil/` or accepted catalog home |
| EvidenceBundle and proof support | `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/soil/dual_hash/`, `tests/spec_hash/`, `tests/domains/soil/`, `fixtures/domains/soil/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Soil dual-hash and source-lineage rules using accepted canonicalization.
- **NEEDS VERIFICATION:** exact executable names, field names, schema homes, source registry shape, fixture shape, policy bundles, report destinations, receipts, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as hash-helper authority, catalog storage, proof storage, receipt storage, source registry, lifecycle data store, release record store, published artifact store, contract home, schema home, policy home, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/soil/dual_hash/` include checks that:

- verify the canonical Soil record hash matches the stored or declared content hash;
- verify the canonical Soil source/provenance closure hash matches the stored or declared lineage hash;
- detect when Soil record bytes changed but source/provenance closure did not update;
- detect when Soil source descriptors, retrieval receipts, transform identifiers, source vintages, or upstream EvidenceRefs changed but derived Soil records did not update;
- validate paired hash posture for SoilMapUnit, SoilComponent, Horizon, SoilProperty, HydrologicSoilGroup, SoilMoistureObservation, ErosionRisk, SuitabilityRating, Pedon / SoilProfileView, ComponentHorizonJoin, SoilTimeCaveat, and configured Soil derivatives;
- preserve SSURGO/SDA/gSSURGO/gNATSGO/Mesonet/SCAN/USCRN/SMAP source-family distinctions where configured;
- require fail-closed findings when either hash side is missing, malformed, stale, mismatched, or computed with an unaccepted canonicalization rule;
- emit deterministic validation reports without creating receipts, proofs, release manifests, or public artifacts.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/soil/dual_hash/` | Correct home |
|---|---|
| Generic spec_hash helper implementation | `tools/spec_hash/` |
| Canonicalization standards | `docs/standards/CANONICALIZATION.md` or accepted standards docs |
| Soil source descriptors | `data/registry/sources/soil/` |
| Soil domain docs | `docs/domains/soil/` |
| Soil contracts | `contracts/domains/soil/`, `contracts/soil/`, or ADR-selected home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Soil dual-hash validator posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks either side of the accepted hash pair;
- uses an unknown, unsupported, or undocumented canonicalization rule;
- has malformed `jcs:sha256:<hex>` values where that format is required;
- has a recomputed content hash that does not match the stored content hash;
- has a recomputed provenance/source-lineage hash that does not match the stored lineage hash;
- changes source descriptors, retrieval/run receipts, transform profiles, source vintages, or upstream EvidenceRefs without updating dependent Soil content;
- changes Soil record bytes without updating dependent catalog, proof, receipt, release, correction, or rollback references;
- treats a hash match as evidence closure, policy approval, rights clearance, release approval, or public-surface safety;
- allows public-bound Soil artifacts to depend on RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, or stale provenance closure;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_DUAL_HASH_PASS` | Configured Soil dual-hash checks passed. |
| `SOIL_DUAL_HASH_FAIL` | One or more configured checks failed. |
| `SOIL_CONTENT_HASH_MISSING` | Required content/record hash is absent. |
| `SOIL_LINEAGE_HASH_MISSING` | Required provenance/source-lineage hash is absent. |
| `SOIL_CONTENT_HASH_MISMATCH` | Recomputed Soil content hash differs from stored value. |
| `SOIL_LINEAGE_HASH_MISMATCH` | Recomputed Soil lineage/provenance hash differs from stored value. |
| `SOIL_HASH_FORMAT_INVALID` | Stored hash does not match accepted format. |
| `SOIL_HASH_ALGORITHM_UNSUPPORTED` | Hash algorithm or canonicalization rule is unsupported. |
| `SOIL_PROVENANCE_STALE` | Source/provenance closure changed without dependent Soil update. |
| `SOIL_CONTENT_STALE` | Soil content changed without dependent catalog/proof/release update. |
| `SOIL_SOURCE_ROLE_COLLAPSE` | Hash package hides source-role or object-family distinction. |
| `SOIL_CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Soil without preserving boundaries. |
| `HASH_AS_TRUTH_DENIED` | Candidate treats hash match as truth, evidence closure, policy approval, or release approval. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/soil/dual_hash/
├── README.md
├── test_soil_dual_hash.py
└── fixtures/
    ├── valid_soil_dual_hash_bundle/
    ├── missing_content_hash/
    ├── missing_lineage_hash/
    ├── content_hash_mismatch/
    ├── lineage_hash_mismatch/
    ├── invalid_hash_format/
    ├── unsupported_algorithm/
    ├── provenance_stale/
    ├── content_stale/
    └── hash_as_truth_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/soil/dual_hash
```

```bash
python tools/validators/domains/soil/dual_hash/validate_soil_dual_hash.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_soil_dual_hash.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator delegates canonicalization and generic hash computation to the accepted spec-hash helper or exactly matches its documented behavior.
- [ ] Dual-hash fields, algorithms, and report shape are backed by schema/contract evidence before implementation claims are made.
- [ ] Soil object families and source families remain distinct.
- [ ] SSURGO/SDA/gSSURGO/gNATSGO and configured Soil identity keys remain traceable.
- [ ] Hash checks do not replace EvidenceBundle, proof, receipt, PolicyDecision, ReleaseManifest, correction, or rollback records.
- [ ] Cross-domain joins preserve Agriculture, Hydrology, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, or direct internal stores.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty Soil dual-hash validator file. |
| Next smallest safe change | Verify actual Soil dual-hash scripts, accepted field names, schemas, canonicalization rules, source descriptors, fixtures, report destinations, receipts, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
