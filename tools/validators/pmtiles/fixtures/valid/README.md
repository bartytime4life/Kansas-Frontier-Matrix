<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-pmtiles-fixtures-valid-readme
title: tools/validators/pmtiles/fixtures/valid README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-pmtiles-steward-plus-fixture-steward-plus-publication-steward-plus-policy-steward-plus-release-steward-plus-evidence-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; pmtiles-validator-fixtures; valid-fixtures; positive-fixtures; synthetic-only; public-safe; attestation; derived-artifacts-only; no-production-payloads; release-gated; non-authoritative
owning_root: tools/
responsibility: valid fixture routing README for PMTiles validator positive cases under tools/validators/pmtiles; documents public-safe synthetic fixture classes for complete artifact sets, reconciled spec_hash, valid header metadata, valid PMIDX sidecar, valid range proof, valid PMSIG signature bundle, matching RunReceipt, policy-ready posture, release-reference posture, correction/rollback linkage, and MapLibre/public-surface readiness checks while deferring real fixture bytes, schemas, policy decisions, evidence records, receipts, lifecycle data, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../invalid/README.md
  - ../../../README.md
  - ../../../_common/README.md
  - ../../../maplibre/README.md
  - ../../../lifecycle/README.md
  - ../../../evidence/README.md
  - ../../../geo_manifest/README.md
  - ../../../../../docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md
  - ../../../../../docs/standards/pmtiles/PMIDX_SPEC_V1.md
  - ../../../../../docs/architecture/publication/GEO_MANIFEST.md
  - ../../../../../contracts/release/release_manifest.md
  - ../../../../../contracts/data/validation_report.md
  - ../../../../../contracts/common/spec_hash.md
  - ../../../../../schemas/contracts/v1/
  - ../../../../../policy/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
  - ../../../../../fixtures/
  - ../../../../../tests/
notes:
  - "This README replaces a short stub that said valid fixtures should be minimal, synthetic, public-safe, and reconstructable from committed inputs. It does not confirm any fixture files exist."
  - "Valid fixtures are positive test inputs. They are not production artifacts, source data, release artifacts, EvidenceBundles, receipts, proofs, or public map layers."
  - "A valid fixture may prove that a validator can recognize a well-formed PMTiles attestation chain; it does not prove that a real-world tile artifact is true, admissible, policy-approved, released, or safe for public use."
  - "PMTiles archives are derived publication artifacts, not canonical truth. Public clients may consume only released artifacts and governed APIs."
  - "Positive PMTiles fixtures must be synthetic, minimized, public-safe, deterministic, reconstructable from committed inputs, and free of sensitive exact locations, private source data, production payloads, credentials, secret keys, restricted geometry, and reconstruction hints."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/pmtiles/fixtures/valid

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-pmtiles--valid--fixtures-informational)
![posture](https://img.shields.io/badge/posture-positive--fixtures-success)
![payloads](https://img.shields.io/badge/payloads-synthetic--only-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/pmtiles/fixtures/valid/` documents positive PMTiles attestation fixture classes for validator acceptance behavior; it does not store truth, release artifacts, source data, sensitive geometry, proof authority, or publication authority.

---

## Purpose

`tools/validators/pmtiles/fixtures/valid/` exists to make PMTiles positive fixture expectations inspectable for maintainers who test publication-gate validators.

The durable KFM question for this fixture lane is:

> Which intentionally valid, synthetic, public-safe PMTiles, PMIDX, PMSIG, RunReceipt, policy, release-reference, correction, rollback, and public-surface cases should pass validator checks before a derived tile artifact can be considered eligible for later governed release review?

The answer should be a small, deterministic set of positive fixture classes and expected acceptance outcomes. This folder should not create PMTiles truth, tile truth, source truth, release truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, production tile archives, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/pmtiles/fixtures/valid/README.md` | **CONFIRMED README** | This README replaces a short stub about minimal synthetic valid fixtures. |
| `tools/validators/pmtiles/fixtures/invalid/README.md` | **CONFIRMED sibling README / fixture files NEEDS VERIFICATION** | Negative fixture lane documents fail-closed cases and forbids sensitive or production payloads. |
| `tools/validators/pmtiles/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Parent README describes fail-closed PMTiles validation helpers and expected artifact inputs. |
| `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines required artifact set, `spec_hash` reconciliation, publication gate, and fail-closed conditions. |
| Valid fixture files | **NOT CLAIMED** | File names below are fixture classes/examples, not proof that matching files exist. |
| Executable tests, schema bindings, policy bundles, report destinations, receipt emission, release integration, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Fixture safety rules

Valid PMTiles fixtures must be:

- synthetic or minimized;
- public-safe;
- deterministic;
- reconstructable from committed inputs;
- small enough for repository review, unless an accepted fixture policy says otherwise;
- free of real sensitive coordinates, protected locations, private source payloads, private parcel/person links, infrastructure exposure, archaeology locations, rare-species locations, DNA/genomic data, credentials, private keys, tokens, and reconstruction hints;
- explicitly tied to a positive validator outcome;
- unable to be mistaken for a production or release artifact;
- excluded from public artifacts, release manifests, catalog truth, and map runtime loading unless separately promoted through governed release.

A fixture can be **valid for a validator** while still not being **published**, **production-grade**, **source-authoritative**, or **claim-authoritative**.

[Back to top](#top)

---

## Valid fixture classes

| Fixture class | Example name | Expected outcome | Validator concern |
|---|---|---|---|
| Complete attestation chain | `complete_minimal.pmtiles` plus sidecars | `PMTILES_ATTESTATION_PASS` | PMTiles, PMIDX, PMSIG, RunReceipt, and release-reference stubs reconcile. |
| Reconciled spec hash | `reconciled_spec_hash.pmtiles` | `PMTILES_SPEC_HASH_RECONCILED` | Same canonical `spec_hash` appears in metadata, PMIDX, PMSIG, RunReceipt, and release/promotion reference. |
| Valid header metadata | `valid_header.pmtiles` | `PMTILES_HEADER_VALID` | Header values satisfy required metadata, bounds, zoom, and policy posture. |
| Valid PMIDX sidecar | `valid_sidecar.pmtiles.pmidx` | `PMIDX_VALID` | Sidecar schema, archive digest reference, Merkle root, and metadata reconcile. |
| Valid range proof | `valid_range_proof.pmtiles.pmidx` | `PMIDX_RANGE_PROOF_VALID` | Tile/range proof path verifies for selected deterministic sample ranges. |
| Valid signature bundle | `valid_signature.pmtiles.pmsig` | `PMSIG_VALID` | Signature verifies over archive digest, sidecar root, and `spec_hash` using fixture-safe public test keys. |
| Valid signer fixture | `valid_fixture_signer.pmtiles.pmsig` | `PMSIG_SIGNER_ALLOWED_FOR_FIXTURE` | Signer is allowed only for fixture/testing scope, not production release authority. |
| Matching RunReceipt | `matching_receipt.runreceipt.json` | `RUNRECEIPT_MATCH` | Builder identity, source refs, toolchain, spec hash, and output digest reconcile. |
| Policy-ready stub | `policy_ready.fixture-policy.json` | `POLICY_REFERENCE_PRESENT` | Rights/sensitivity/source-role posture is present for fixture scope; not a real PolicyDecision. |
| Release-reference stub | `release_reference.fixture-release.json` | `RELEASE_REFERENCE_PRESENT` | Release/correction/rollback references are shaped for tests; not real release approval. |
| MapLibre-safe descriptor | `maplibre_safe_descriptor.json` | `MAPLIBRE_DESCRIPTOR_PUBLIC_SAFE` | Descriptor points only to fixture-safe released-test artifact references. |
| Correction-ready fixture | `correction_ready.pmtiles` | `CORRECTION_REFERENCE_PRESENT` | Candidate carries a correction lineage placeholder usable by tests. |
| Rollback-ready fixture | `rollback_ready.pmtiles` | `ROLLBACK_REFERENCE_PRESENT` | Candidate carries rollback target placeholder usable by tests. |
| Minimal fixture index | `fixture_index.json` | `FIXTURE_INDEX_VALID` | Fixture index maps each positive fixture to expected validator outcomes and checksums. |

[Back to top](#top)

---

## Expected positive posture

Every valid fixture in this folder should produce one of these finite outcomes or a stricter accepted equivalent:

| Outcome | Meaning |
|---|---|
| `PMTILES_VALID_FIXTURE_EXPECTED_PASS` | Fixture is intentionally valid and should pass the configured positive validator path. |
| `PMTILES_ATTESTATION_PASS` | Required PMTiles artifact set and attestation chain reconcile for fixture scope. |
| `PMTILES_SPEC_HASH_RECONCILED` | `spec_hash` reconciles across metadata, PMIDX, PMSIG, RunReceipt, and release/promotion reference. |
| `PMTILES_HEADER_VALID` | Header metadata satisfies accepted validator expectations. |
| `PMTILES_BOUNDS_ZOOM_POLICY_READY` | Bounds/zoom/header values satisfy fixture policy posture. |
| `PMTILES_DIGEST_RECONCILED` | PMTiles byte digest matches signed subject and RunReceipt. |
| `PMIDX_VALID` | PMIDX sidecar validates and reconciles with archive digest and Merkle root. |
| `PMIDX_RANGE_PROOF_VALID` | Tile/range proof path verifies for deterministic test samples. |
| `PMSIG_VALID` | Signature verifies for fixture scope. |
| `PMSIG_SIGNER_ALLOWED_FOR_FIXTURE` | Signer is allowed for fixture/test scope only. |
| `RUNRECEIPT_MATCH` | RunReceipt matches source refs, toolchain, spec hash, and output digest. |
| `POLICY_REFERENCE_PRESENT` | Policy reference is present for fixture scope. |
| `RELEASE_REFERENCE_PRESENT` | Release/correction/rollback reference shape is present for fixture scope. |
| `MAPLIBRE_DESCRIPTOR_PUBLIC_SAFE` | Descriptor is safe for test renderer-boundary validation. |
| `FIXTURE_INDEX_VALID` | Fixture index is shaped and reconciles expected outcomes/checksums. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not evaluate the fixture because the fixture or test harness is misconfigured. |

A test harness should treat unexpected `DENY`, silent skip, network fetch, production artifact dependency, or public artifact emission as a failure of the positive fixture suite.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| This valid PMTiles fixture README | `tools/validators/pmtiles/fixtures/valid/` |
| Invalid PMTiles fixture guidance | `tools/validators/pmtiles/fixtures/invalid/` |
| PMTiles validator docs and possible helper scripts | `tools/validators/pmtiles/` |
| Shared validator plumbing | `tools/validators/_common/` |
| MapLibre renderer-boundary validation | `tools/validators/maplibre/` |
| Lifecycle gate validation | `tools/validators/lifecycle/` |
| Evidence and Geo Manifest validation | `tools/validators/evidence/`, `tools/validators/geo_manifest/` |
| PMTiles attestation standard | `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` |
| PMIDX sidecar standard | `docs/standards/pmtiles/PMIDX_SPEC_V1.md` |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/contracts/v1/` |
| Policy rules and release gates | `policy/` |
| Real lifecycle data and artifacts | governed `data/` lifecycle roots |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Canonical fixtures and tests, if later promoted | `fixtures/`, `tests/`, or an accepted ADR-selected fixture/test home |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** valid fixture files may live here only if they are synthetic, minimized, public-safe, reconstructable, reviewable, and tied to deterministic positive outcomes.
- **NEEDS VERIFICATION:** exact fixture files, schemas, policy bundles, validator scripts, test paths, report destinations, receipt emission, release integration, and CI wiring.
- **DENY:** using this folder as a PMTiles artifact store, release artifact store, source payload store, lifecycle data store, proof store, receipt store, policy home, schema home, public runtime surface, map tile service, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/pmtiles/fixtures/valid/` include:

- README documentation for intentionally valid fixture classes;
- tiny synthetic PMTiles-like payloads designed to pass header/digest/spec-hash checks;
- synthetic PMIDX sidecars with valid schema, Merkle root, and range-proof examples;
- synthetic PMSIG bundles using fixture-only test keys and clearly non-production signer identity;
- synthetic RunReceipt/policy/release-reference stubs that exercise positive reconciliation outcomes;
- notes mapping each positive fixture to an expected finite validator outcome;
- checksum notes for synthetic fixtures, if accepted by the test harness;
- reconstruction instructions that prove the fixture can be regenerated from committed inputs.

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
| Schemas, DTOs, enums, or PMTiles/PMIDX/PMSIG machine shape | `schemas/contracts/v1/...` |
| Semantic contracts | `contracts/` |
| Policy rules, release gates, steward decisions, sensitivity thresholds | `policy/`, `release/` |
| Secrets, production signing keys, real credentials, private source content, sensitive exact locations, or reconstruction hints | denied here; keep out of repository-facing fixtures |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/pmtiles/fixtures/valid/
├── README.md
├── complete_minimal.pmtiles              # PROPOSED; not confirmed
├── complete_minimal.pmtiles.pmidx        # PROPOSED; not confirmed
├── complete_minimal.pmtiles.pmsig        # PROPOSED; not confirmed
├── complete_minimal.runreceipt.json      # PROPOSED; not confirmed
├── complete_minimal.fixture-release.json # PROPOSED; not confirmed
├── maplibre_safe_descriptor.json         # PROPOSED; not confirmed
└── fixture_index.json                    # PROPOSED; maps fixture -> expected outcome/checksum
```

Do not add a positive fixture unless the expected validator outcome is documented and a test can prove the fixture passes for the intended reason without granting publication authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the short stub at `tools/validators/pmtiles/fixtures/valid/README.md`.
- [x] It marks this path as valid PMTiles fixture guidance, not artifact, proof, receipt, policy, release, public runtime, or AI authority.
- [x] It preserves PMTiles attestation positive posture for header, `spec_hash`, PMIDX, PMSIG, RunReceipt, policy reference, release reference, correction, rollback, and MapLibre/public-surface cases.
- [x] It forbids sensitive, unreleased, production-derived, credential-bearing, private, or reconstruction-capable payloads.
- [x] It distinguishes validator-positive fixture status from publication approval.
- [x] It marks fixture files, executable tests, schema bindings, policy bundles, receipt emission, release integration, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to valid PMTiles fixtures are searched and classified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads.
- [ ] Each fixture has an expected finite outcome in a fixture index or test parameterization.
- [ ] Tests prove valid fixtures pass for the intended reason and never emit public artifacts.
- [ ] CI invokes the relevant PMTiles positive fixture tests in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced short valid-fixture stub with governed PMTiles valid fixture README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
