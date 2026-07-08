<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-pmtiles-readme
title: tools/validators/pmtiles README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-pmtiles-steward-plus-publication-steward-plus-schema-steward-plus-fixture-steward-plus-policy-steward-plus-release-steward-plus-evidence-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; pmtiles-validator-index; fail-closed; attestation; spec-hash; pmidx; pmsig; runreceipt; derived-artifacts-only; release-gated; public-surface-deny-by-default; non-authoritative
owning_root: tools/
responsibility: parent PMTiles validator routing README under tools/validators; indexes fail-closed validation helpers, schema routing, fixture routing, PMTiles metadata/header checks, spec_hash reconciliation, PMIDX sidecar and Merkle checks, PMSIG/signature posture, RunReceipt reconciliation, policy/review posture, release/correction/rollback references, MapLibre/public-surface denial, and verification gaps while deferring artifact bytes, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, tests, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../maplibre/README.md
  - ../lifecycle/README.md
  - ../evidence/README.md
  - ../geo_manifest/README.md
  - fixtures/README.md
  - fixtures/valid/README.md
  - fixtures/invalid/README.md
  - schemas/README.md
  - ../../../docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md
  - ../../../docs/standards/pmtiles/PMIDX_SPEC_V1.md
  - ../../../docs/architecture/publication/GEO_MANIFEST.md
  - ../../../contracts/common/spec_hash.md
  - ../../../contracts/data/validation_report.md
  - ../../../contracts/release/release_manifest.md
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces a short parent README that listed validate_header.py and verify_merkle.py. It does not confirm those scripts currently exist or run."
  - "PMTiles archives are derived publication artifacts, not canonical truth. Public clients may consume only released artifacts and governed APIs."
  - "A PMTiles artifact is not trusted merely because it exists; the archive, metadata, build specification, PMIDX sidecar, PMSIG signature bundle, RunReceipt, policy posture, and release/rollback references must reconcile before publication eligibility."
  - "The fixture and schema sublanes are documentation/routing lanes; they do not confirm fixture files, local schema files, tests, CI wiring, release artifacts, or publication readiness."
  - "Validators enforce declared contracts, schemas, evidence posture, policy references, release readiness, correction paths, rollback targets, and public-surface limits. They do not define tile truth, approve release, publish public outputs, or authorize AI/map claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/pmtiles

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-pmtiles--validator--index-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![artifact](https://img.shields.io/badge/artifact-derived--not--truth-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/pmtiles/` is the PMTiles validator routing index for fail-closed attestation checks over PMTiles archives, PMIDX sidecars, PMSIG signatures, RunReceipts, `spec_hash` reconciliation, fixtures, schema bindings, release references, correction/rollback posture, and public-surface denial.

---

## Purpose

`tools/validators/pmtiles/` exists to organize PMTiles publication-gate validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a PMTiles-bound candidate prove enough attestation readiness — through header/metadata checks, deterministic build-spec `spec_hash`, PMIDX sidecar commitments, PMSIG signature posture, RunReceipt reconciliation, policy/review state, release/correction/rollback references, fixture coverage, and MapLibre/public-surface denial checks — to be considered eligible for later governed release review?

The answer should be a deterministic validation result or routing decision. This folder should not create PMTiles truth, tile truth, source truth, release truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, production tile archives, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/pmtiles/README.md` | **CONFIRMED README** | This README replaces the prior short validator note. |
| `validate_header.py` | **NEEDS VERIFICATION** | Prior README listed this helper for PMTiles header/metadata and required `spec_hash`; this edit does not confirm the script file exists or runs. |
| `verify_merkle.py` | **NEEDS VERIFICATION** | Prior README listed this helper for PMIDX schema, PMTiles digest, and Merkle root checks; this edit does not confirm the script file exists or runs. |
| `fixtures/README.md` | **CONFIRMED README / fixture files NEEDS VERIFICATION** | Parent fixture index for valid and invalid PMTiles fixture lanes. |
| `fixtures/valid/README.md` | **CONFIRMED README / fixture files NEEDS VERIFICATION** | Positive fixture guidance; validator-positive fixture status is not publication approval. |
| `fixtures/invalid/README.md` | **CONFIRMED README / fixture files NEEDS VERIFICATION** | Negative fixture guidance for fail-closed cases. |
| `schemas/README.md` | **CONFIRMED README / schema files NEEDS VERIFICATION** | Schema-routing guidance; local schema files are not confirmed and canonical schema homes remain NEEDS VERIFICATION. |
| `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines required artifact set, `spec_hash` reconciliation, publication gate, fail-closed conditions, and no-public-publication-before-promotion posture. |
| Executable tests, validator registry wiring, schema bindings, policy bundles, report destinations, receipt emission, release integration, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Required attestation set

PMTiles validation is not a single-file check. The expected PMTiles publication-gate candidate includes:

| Artifact | Validator concern | Boundary |
|---|---|---|
| `tiles.pmtiles` | Archive header, metadata, byte digest, bounds/zoom, source/layer posture, `spec_hash`. | Derived tile artifact, not truth. |
| `tiles.pmtiles.pmidx` | Sidecar schema, PMTiles digest, Merkle root, leaves, optional range/tile commitments. | Integrity sidecar, not release. |
| `tiles.pmtiles.pmsig` | Signature subject, signer identity, validity interval, algorithm, archive digest, sidecar root, `spec_hash`. | Signature support, not policy approval. |
| `tiles.pmtiles.runreceipt.json` | Builder identity, source refs, toolchain, build spec, output digest, replay context. | Provenance support, not release approval. |
| Release/correction/rollback reference | Promotion/release linkage, rollback target, correction path, withdrawal posture. | Required publication context, not created here. |
| Policy/review reference | Rights, sensitivity, source-role, freshness, steward review, obligations. | Policy support remains in `policy/` and release governance. |
| Evidence/manifest references | EvidenceRef, EvidenceBundle, KFM Geo Manifest, ValidationReport, digest/spec-hash references where required. | Evidence and proof support stay outside validators. |

A candidate missing a required artifact or required reference should fail closed, abstain, deny, or route to steward review depending on the configured validator and policy posture.

[Back to top](#top)

---

## Relationship to child lanes

| Lane | Purpose | Status |
|---|---|---|
| [`fixtures/`](fixtures/README.md) | Parent index for PMTiles positive and negative fixture guidance. | **CONFIRMED README / fixture files NEEDS VERIFICATION** |
| [`fixtures/valid/`](fixtures/valid/README.md) | Positive fixture classes for complete attestation chains, reconciled `spec_hash`, valid headers, PMIDX, range proofs, PMSIG, RunReceipt, policy/reference stubs, release references, correction/rollback, and MapLibre-safe descriptors. | **CONFIRMED README / fixture files NEEDS VERIFICATION** |
| [`fixtures/invalid/`](fixtures/invalid/README.md) | Negative fixture classes for missing/malformed `spec_hash`, header mismatch, digest mismatch, PMIDX/Merkle failure, invalid range proof, bad signature, signer denial, RunReceipt mismatch, policy gaps, release gaps, rollback mismatch, stale-state, and public-surface bypass. | **CONFIRMED README / fixture files NEEDS VERIFICATION** |
| [`schemas/`](schemas/README.md) | Schema-binding expectations and routing for PMTiles metadata, build spec, PMIDX, PMSIG, RunReceipt, release/rollback references, fixture indexes, validation reports, and MapLibre descriptors. | **CONFIRMED README / local schema files NEEDS VERIFICATION** |

Future sublanes should be added only when they have distinct validator behavior, artifact class, fixture policy, schema-binding posture, or release/public-surface risk. Avoid creating local schema or artifact homes that compete with `schemas/`, `data/`, `release/`, `fixtures/`, or `tests/` without an accepted ADR or migration note.

[Back to top](#top)

---

## Validator responsibilities

PMTiles validators routed through this folder should check:

- PMTiles archive existence, readability, declared metadata, and header posture;
- deterministic build-spec `spec_hash` syntax, canonicalization, and reconciliation;
- PMIDX sidecar schema, PMTiles archive digest, Merkle root, leaves, and range/tile proof posture;
- PMSIG signature subject, signer posture, validity interval, algorithm, and signed payload reconciliation;
- RunReceipt builder identity, source refs, toolchain, build spec, output digest, and replay context;
- policy/review references for rights, sensitivity, source role, freshness, obligations, and restrictions;
- release, correction, rollback, withdrawal, and supersession references required for intended use;
- EvidenceRef, EvidenceBundle, KFM Geo Manifest, ValidationReport, digest, and manifest references where required;
- valid fixtures pass for intended reasons and invalid fixtures fail for intended reasons;
- MapLibre/public surfaces receive only governed released/public-safe artifacts through governed APIs or released artifact routes;
- non-zero or finite negative results are returned for unknown, malformed, missing, unresolved, stale, denied, or unsafe values.

[Back to top](#top)

---

## Fail-closed conditions

A PMTiles candidate should fail closed, deny, abstain, or route to steward review when:

- PMTiles archive bytes are missing, unreadable, altered, stale, superseded, withdrawn, revoked, or correction-pending;
- header or metadata is missing, malformed, contradicted, or violates bounds/zoom/public-safe policy;
- `spec_hash` is missing, malformed, not reproducible from canonical JSON, or does not reconcile across required artifacts;
- PMTiles digest does not match PMIDX, PMSIG, RunReceipt, manifest, or release reference;
- PMIDX schema is invalid, required fields are absent, Merkle root does not recompute, range proof is invalid, or sidecar subject mismatches the archive;
- PMSIG is missing, invalid, expired, not-yet-valid, signed over the wrong subject, or signed by a denied/unapproved signer;
- RunReceipt is missing, builder identity is not approved, source refs or toolchain do not match the build spec, or output digest differs;
- policy, rights, sensitivity, source-role, review, release, correction, rollback, or withdrawal posture is missing or unresolved;
- fixture payloads are production-derived, sensitive, credential-bearing, reconstruction-capable, or not tied to deterministic expected outcomes;
- browser/MapLibre/public-surface logic attempts to load RAW, WORK, QUARANTINE, unpublished, canonical/internal, connector, source-system, or direct model output data;
- schema validity, fixture pass status, digest match, signature validity, or validator success is treated as evidence closure, policy approval, release approval, source truth, or public safety.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| PMTiles validator parent index | `tools/validators/pmtiles/` |
| PMTiles validator fixture guidance | `tools/validators/pmtiles/fixtures/` |
| PMTiles validator schema-routing guidance | `tools/validators/pmtiles/schemas/` |
| Shared validator plumbing | `tools/validators/_common/` |
| MapLibre renderer-boundary validation | `tools/validators/maplibre/` |
| Lifecycle gate validation | `tools/validators/lifecycle/` |
| Evidence and Geo Manifest validation | `tools/validators/evidence/`, `tools/validators/geo_manifest/` |
| PMTiles attestation standard | `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` |
| PMIDX sidecar standard | `docs/standards/pmtiles/PMIDX_SPEC_V1.md` |
| Semantic contracts | `contracts/` |
| Canonical machine schemas | `schemas/contracts/v1/` or accepted ADR-selected schema homes |
| Policy rules and release gates | `policy/` |
| Real lifecycle data and artifacts | governed `data/` lifecycle roots |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Canonical fixtures and tests, if later promoted | `fixtures/`, `tests/`, or an accepted ADR-selected fixture/test home |

Safe interpretation:

- **CONFIRMED:** this README exists, and child README lanes exist for `fixtures/`, `fixtures/valid/`, `fixtures/invalid/`, and `schemas/`.
- **PROPOSED:** validator code may live here when it checks declared PMTiles attestation invariants and delegates meaning, schemas, policy, evidence, receipts, lifecycle data, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, schemas, schema ids, schema digests, fixture files, policy bundles, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as PMTiles artifact store, release artifact store, source payload store, lifecycle data store, proof store, receipt store, policy home, canonical schema home, public runtime surface, map tile service, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/pmtiles/` include:

- this parent README;
- small PMTiles validator scripts or adapters, if verified and kept fail-closed;
- references to fixture and schema-routing lanes;
- deterministic checks for PMTiles metadata, `spec_hash`, PMIDX, PMSIG, RunReceipt, policy references, release references, correction/rollback references, and public-surface denial;
- finite validation outcome vocabulary and routing notes;
- test planning notes that route generated reports to accepted report/proof/receipt/artifact roots.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Production PMTiles, COGs, GeoParquet, MVT/MLT bundles, sprites, glyphs, screenshots, or exports | governed lifecycle/release artifact homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Source descriptors or source registries | `data/registry/`, `data/registry/sources/` |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| Canonical schemas, DTOs, enums, or PMTiles/PMIDX/PMSIG machine shape | `schemas/contracts/v1/...` or accepted schema homes |
| Semantic contracts | `contracts/` |
| Policy rules, release gates, steward decisions, sensitivity thresholds | `policy/`, `release/` |
| Secrets, production signing keys, real credentials, private source content, sensitive exact locations, or reconstruction hints | denied here; keep out of repository-facing docs and fixtures |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `PMTILES_VALIDATOR_PASS` | Candidate passed configured PMTiles attestation checks. |
| `PMTILES_VALIDATOR_FAIL` | Candidate failed one or more configured checks. |
| `PMTILES_VALIDATOR_DENY` | Candidate is denied because evidence, rights, policy, release, correction, rollback, sensitivity, integrity, or public-surface support cannot be resolved. |
| `PMTILES_VALIDATOR_ABSTAIN` | Candidate lacks enough evidence or policy support to evaluate safely. |
| `PMTILES_HEADER_INVALID` | Header or metadata fails required checks. |
| `PMTILES_SPEC_HASH_MISSING` | Required `spec_hash` is absent. |
| `PMTILES_SPEC_HASH_MALFORMED` | `spec_hash` exists but is malformed or uses unsupported canonicalization posture. |
| `PMTILES_SPEC_HASH_MISMATCH` | `spec_hash` does not reconcile across required artifacts. |
| `PMTILES_DIGEST_MISMATCH` | PMTiles byte digest does not match sidecar/signature/receipt/release reference. |
| `PMIDX_SCHEMA_INVALID` | PMIDX sidecar fails accepted schema checks. |
| `PMIDX_MERKLE_ROOT_MISMATCH` | PMIDX Merkle root does not reconcile. |
| `PMIDX_RANGE_PROOF_INVALID` | Tile/range proof path is malformed or invalid. |
| `PMSIG_MISSING` | Required signature bundle is absent. |
| `PMSIG_INVALID` | Signature cannot be verified. |
| `PMSIG_SIGNER_DENIED` | Signer is not allowed for the target release or fixture scope. |
| `RUNRECEIPT_MISSING` | Required run receipt is absent. |
| `RUNRECEIPT_MISMATCH` | Run receipt does not match source refs, toolchain, spec hash, or output digest. |
| `POLICY_OR_REVIEW_GAP` | Rights, sensitivity, source-role, review, or policy posture is unresolved. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, rollback, or withdrawal reference is absent. |
| `STALE_OR_SUPERSEDED_ARTIFACT_DENIED` | Artifact is stale, superseded, withdrawn, revoked, or correction-pending. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsafe or unreleased content to MapLibre, public clients, exports, screenshots, Focus Mode, graph, embedding, or AI surfaces. |
| `SCHEMA_VALIDITY_OVERCLAIM` | Schema validity is treated as evidence closure, policy approval, release approval, or public safety. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/pmtiles/
├── README.md
├── validate_header.py                   # NEEDS VERIFICATION; listed by prior README
├── verify_merkle.py                     # NEEDS VERIFICATION; listed by prior README
├── fixtures/
│   ├── README.md
│   ├── valid/
│   │   └── README.md
│   └── invalid/
│       └── README.md
└── schemas/
    └── README.md
```

Do not add executable validators, fixture payloads, or local schema files unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting publication authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the short parent README at `tools/validators/pmtiles/README.md`.
- [x] It marks this path as PMTiles validator routing, not artifact, proof, receipt, policy, schema, release, public runtime, or AI authority.
- [x] It indexes `fixtures/`, `fixtures/valid/`, `fixtures/invalid/`, and `schemas/`.
- [x] It preserves PMTiles attestation posture for PMTiles metadata/header, `spec_hash`, PMIDX, PMSIG, RunReceipt, policy, release, correction, rollback, stale-state, and MapLibre/public-surface cases.
- [x] It distinguishes validator success, schema validity, fixture pass status, digest match, and signature validity from truth, evidence closure, policy approval, release approval, and public safety.
- [x] It marks executable scripts, registry wiring, schema files, schema ids, fixtures, tests, policy bundles, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to PMTiles validators are searched and classified.
- [ ] `validate_header.py`, `verify_merkle.py`, and any additional validator scripts are verified or corrected.
- [ ] Canonical schema homes for PMTiles metadata, PMIDX, PMSIG, RunReceipt, fixture index, and PMTiles build spec are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive and negative PMTiles cases pass/fail for the intended reason.
- [ ] CI invokes the relevant PMTiles validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Expanded short PMTiles validator README into governed parent validator index. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
