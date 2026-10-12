<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-pmtiles-fixtures-invalid-readme
title: tools/validators/pmtiles/fixtures/invalid README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-pmtiles-steward-plus-fixture-steward-plus-publication-steward-plus-policy-steward-plus-release-steward-plus-evidence-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; pmtiles-validator-fixtures; invalid-fixtures; fail-closed; attestation; derived-artifacts-only; no-sensitive-payloads; no-production-payloads; release-gated; non-authoritative
owning_root: tools/
responsibility: invalid fixture routing README for PMTiles validator negative cases under tools/validators/pmtiles; documents fail-closed fixture classes for missing/malformed spec_hash, header mismatch, PMIDX Merkle mismatch, invalid range proof, bad signature, signer denial, RunReceipt mismatch, policy gap, release gap, rollback/correction gap, stale/superseded artifact, and public-surface bypass while deferring real fixture bytes, schemas, policy decisions, evidence records, receipts, lifecycle data, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../README.md
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
  - "This README replaces a short stub that listed example invalid PMTiles attestation fixtures. It does not confirm any fixture files exist."
  - "Invalid fixtures are negative test inputs. They must not be used as production artifacts, source data, release artifacts, evidence records, receipts, proofs, or public map layers."
  - "PMTiles archives are derived publication artifacts, not canonical truth. Public clients may consume only released artifacts and governed APIs."
  - "Negative PMTiles fixtures must be synthetic, minimized, public-safe, and free of sensitive exact locations, private source data, production payloads, credentials, secret keys, restricted geometry, and reconstruction hints."
  - "A fixture that passes by accident is a validator defect or fixture defect and must be corrected before relying on the suite."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/pmtiles/fixtures/invalid

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-pmtiles--invalid--fixtures-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![payloads](https://img.shields.io/badge/payloads-synthetic--only-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/pmtiles/fixtures/invalid/` documents negative PMTiles attestation fixture classes for fail-closed validator behavior; it does not store truth, release artifacts, source data, sensitive geometry, proof authority, or publication authority.

---

## Purpose

`tools/validators/pmtiles/fixtures/invalid/` exists to make PMTiles negative fixture expectations inspectable for maintainers who test publication-gate validators.

The durable KFM question for this fixture lane is:

> Which intentionally invalid PMTiles, PMIDX, PMSIG, RunReceipt, policy, release, correction, rollback, and public-surface cases must fail closed before a derived tile artifact can approach MapLibre, governed APIs, public clients, exports, screenshots, Focus Mode, graph surfaces, or AI responses?

The answer should be a small, synthetic, deterministic set of invalid fixture classes and expected failure outcomes. This folder should not create PMTiles truth, tile truth, source truth, release truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, production tile archives, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/pmtiles/fixtures/invalid/README.md` | **CONFIRMED README** | This README replaces a short stub listing negative fixture examples. |
| `tools/validators/pmtiles/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Parent README describes fail-closed PMTiles validation helpers and expected artifact inputs. |
| `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines required artifact set, spec-hash reconciliation, publication gate, and fail-closed conditions. |
| `tools/validators/pmtiles/fixtures/README.md` | **NOT FOUND in this edit** | No parent fixtures README was found during this edit; this invalid README stands alone until a parent fixture index is added. |
| Invalid fixture files | **NOT CLAIMED** | File names below are fixture classes/examples, not proof that matching files exist. |
| Executable tests, schema bindings, policy bundles, report destinations, receipt emission, release integration, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Fixture safety rules

Invalid PMTiles fixtures must be:

- synthetic or minimized;
- public-safe;
- deterministic;
- small enough for repository review, unless an accepted fixture policy says otherwise;
- free of real sensitive coordinates, protected locations, private source payloads, private parcel/person links, infrastructure exposure, archaeology locations, rare-species locations, DNA/genomic data, credentials, private keys, tokens, and reconstruction hints;
- explicitly tied to a negative validator outcome;
- unable to pass publication gates by accident;
- excluded from public artifacts, release manifests, catalog truth, and map runtime loading.

Invalid fixtures should not be copied from production tile archives unless repository policy explicitly permits a minimized, scrubbed, public-safe derivative with review and receipt support.

[Back to top](#top)

---

## Invalid fixture classes

| Fixture class | Example name | Expected outcome | Validator concern |
|---|---|---|---|
| Missing spec hash | `missing_spec_hash.pmtiles` | `PMTILES_SPEC_HASH_MISSING` | Header/metadata lacks required build-spec digest. |
| Malformed spec hash | `malformed_spec_hash.pmtiles` | `PMTILES_SPEC_HASH_MALFORMED` | Digest format, namespace, or canonicalization marker is invalid. |
| Spec hash mismatch | `spec_hash_mismatch.pmtiles` | `PMTILES_SPEC_HASH_MISMATCH` | PMTiles metadata, PMIDX, PMSIG, RunReceipt, or release record disagree. |
| Altered header | `altered_header.pmtiles` | `PMTILES_HEADER_MISMATCH` | Header values changed after signing or after build receipt. |
| Bounds/zoom policy violation | `bounds_zoom_policy_violation.pmtiles` | `PMTILES_BOUNDS_ZOOM_DENIED` | Bounds or zoom exceed policy, sensitivity, or public-safe constraints. |
| Digest mismatch | `digest_mismatch.pmtiles` | `PMTILES_DIGEST_MISMATCH` | PMTiles byte digest does not match signed or receipt-pinned subject. |
| Wrong Merkle root | `wrong_merkle_root.pmtiles.pmidx` | `PMIDX_MERKLE_ROOT_MISMATCH` | Sidecar Merkle commitment does not reconcile. |
| Invalid PMIDX schema | `invalid_schema.pmtiles.pmidx` | `PMIDX_SCHEMA_INVALID` | Sidecar machine shape is invalid or unresolved. |
| Malformed range proof | `malformed_range_proof.pmtiles.pmidx` | `PMIDX_RANGE_PROOF_INVALID` | Tile/range proof path is malformed or invalid. |
| Missing signature | `missing_signature.pmtiles.pmsig` | `PMSIG_MISSING` | Required signature bundle is absent. |
| Expired signature | `expired_signature.pmtiles.pmsig` | `PMSIG_EXPIRED` | Signature is expired, not yet valid, or outside accepted time window. |
| Forged signer | `forged_signer.pmtiles.pmsig` | `PMSIG_SIGNER_DENIED` | Signer is not in allowed key set or does not match release policy. |
| Invalid signature | `invalid_signature.pmtiles.pmsig` | `PMSIG_INVALID` | Signature does not verify over required subject. |
| Mismatched RunReceipt | `mismatched_receipt.runreceipt.json` | `RUNRECEIPT_MISMATCH` | Builder, source refs, spec hash, toolchain, or output digest disagree. |
| Unpublished source receipt | `unpublished_source_receipt.runreceipt.json` | `SOURCE_NOT_RELEASED_DENIED` | Input source or upstream artifact lacks allowed lifecycle/release posture. |
| Policy gap | `rights_sensitivity_unresolved.policy.json` | `POLICY_OR_REVIEW_GAP` | Rights, sensitivity, source-role, review, or obligations are unresolved. |
| Missing release reference | `missing_release_manifest.pmtiles` | `RELEASE_REFERENCE_MISSING` | ReleaseManifest, PromotionDecision, correction path, rollback target, or withdrawal path is absent. |
| Rollback mismatch | `rollback_mismatch.pmtiles` | `ROLLBACK_REFERENCE_MISMATCH` | Rollback/correction reference does not match published artifact lineage. |
| Stale artifact | `stale_superseded.pmtiles` | `STALE_OR_SUPERSEDED_ARTIFACT_DENIED` | Artifact is stale, superseded, withdrawn, revoked, or correction-pending. |
| Tampered tile range | `tampered_tile_range.pmtiles` | `PMTILES_TILE_RANGE_TAMPERED` | A byte range or tile payload has changed after attestation. |
| Public-surface bypass | `browser_direct_source_bypass.json` | `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate tries to load unreleased or unsafe data directly into MapLibre/public client. |

[Back to top](#top)

---

## Expected fail-closed posture

Every invalid fixture in this folder should produce one of these finite outcomes or a stricter domain-specific equivalent:

| Outcome | Meaning |
|---|---|
| `PMTILES_INVALID_FIXTURE_EXPECTED_FAIL` | Fixture is intentionally invalid and should fail the configured validator. |
| `PMTILES_SPEC_HASH_MISSING` | Required `spec_hash` is absent. |
| `PMTILES_SPEC_HASH_MALFORMED` | `spec_hash` exists but is not valid for the accepted canonicalization/digest rule. |
| `PMTILES_SPEC_HASH_MISMATCH` | Required `spec_hash` values do not reconcile across metadata, PMIDX, PMSIG, receipt, and release records. |
| `PMTILES_HEADER_MISMATCH` | Header metadata differs from the attested or receipt-pinned expectation. |
| `PMTILES_BOUNDS_ZOOM_DENIED` | Bounds/zoom/header values violate declared policy, sensitivity, or public-safe posture. |
| `PMTILES_DIGEST_MISMATCH` | PMTiles byte digest does not match signed subject or run receipt. |
| `PMIDX_SCHEMA_INVALID` | PMIDX sidecar fails accepted machine-shape checks. |
| `PMIDX_MERKLE_ROOT_MISMATCH` | Merkle root does not reconcile with PMTiles bytes or signed metadata. |
| `PMIDX_RANGE_PROOF_INVALID` | Tile/range proof path is malformed or invalid. |
| `PMSIG_MISSING` | Required PMSIG signature bundle is absent. |
| `PMSIG_INVALID` | Signature cannot be verified. |
| `PMSIG_EXPIRED` | Signature is expired, not yet valid, or outside accepted validity window. |
| `PMSIG_SIGNER_DENIED` | Signer is not allowlisted or does not match policy. |
| `RUNRECEIPT_MISSING` | Required run receipt is absent. |
| `RUNRECEIPT_MISMATCH` | Run receipt does not match source refs, toolchain, spec hash, or output digest. |
| `POLICY_OR_REVIEW_GAP` | Rights, sensitivity, source-role, review, or policy posture is unresolved. |
| `SOURCE_NOT_RELEASED_DENIED` | Upstream source or artifact is not eligible for publication. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, rollback, or withdrawal reference is absent. |
| `ROLLBACK_REFERENCE_MISMATCH` | Rollback/correction target does not match artifact lineage. |
| `STALE_OR_SUPERSEDED_ARTIFACT_DENIED` | Artifact is stale, superseded, withdrawn, revoked, or correction-pending. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsafe or unreleased content to MapLibre, public clients, exports, screenshots, Focus Mode, graph, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator cannot evaluate the fixture because the fixture is malformed beyond the intended negative case or the test harness is misconfigured. |

A test harness should treat unexpected `PASS`, silent skip, network fetch, or public artifact emission as a failure of the validator suite.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| This invalid PMTiles fixture README | `tools/validators/pmtiles/fixtures/invalid/` |
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
- **PROPOSED:** invalid fixture files may live here only if they are synthetic, minimized, public-safe, reviewable, and tied to deterministic negative outcomes.
- **NEEDS VERIFICATION:** exact fixture files, schemas, policy bundles, validator scripts, test paths, report destinations, receipt emission, release integration, and CI wiring.
- **DENY:** using this folder as a PMTiles artifact store, release artifact store, source payload store, lifecycle data store, proof store, receipt store, policy home, schema home, public runtime surface, map tile service, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/pmtiles/fixtures/invalid/` include:

- README documentation for intentionally invalid fixture classes;
- tiny synthetic PMTiles-like payloads designed to fail header/digest/spec-hash checks;
- synthetic PMIDX sidecars with controlled schema, Merkle, or range-proof failures;
- synthetic PMSIG bundles with controlled signer, expiry, subject, or signature failures;
- synthetic RunReceipt/policy/release-reference stubs that exercise mismatch and missing-reference outcomes;
- notes mapping each negative fixture to an expected finite validator outcome;
- checksum notes for synthetic fixtures, if accepted by the test harness.

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
| Secrets, signing keys, real credentials, private source content, sensitive exact locations, or reconstruction hints | denied here; keep out of repository-facing fixtures |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/pmtiles/fixtures/invalid/
├── README.md
├── missing_spec_hash.pmtiles              # PROPOSED; not confirmed
├── altered_header.pmtiles                 # PROPOSED; not confirmed
├── wrong_merkle_root.pmtiles.pmidx        # PROPOSED; not confirmed
├── expired_signature.pmtiles.pmsig        # PROPOSED; not confirmed
├── forged_signer.pmtiles.pmsig            # PROPOSED; not confirmed
├── mismatched_receipt.runreceipt.json     # PROPOSED; not confirmed
└── fixture_index.json                     # PROPOSED; maps fixture -> expected outcome
```

Do not add a negative fixture unless the expected validator outcome is documented and a test can prove the fixture fails for the intended reason.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the short stub at `tools/validators/pmtiles/fixtures/invalid/README.md`.
- [x] It marks this path as invalid PMTiles fixture guidance, not artifact, proof, receipt, policy, release, public runtime, or AI authority.
- [x] It preserves PMTiles attestation fail-closed posture for header, `spec_hash`, PMIDX, PMSIG, RunReceipt, policy, release, correction, rollback, stale-state, and public-surface cases.
- [x] It forbids sensitive, unreleased, production-derived, credential-bearing, private, or reconstruction-capable payloads.
- [x] It marks fixture files, executable tests, schema bindings, policy bundles, receipt emission, release integration, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to invalid PMTiles fixtures are searched and classified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads.
- [ ] Each fixture has an expected finite outcome in a fixture index or test parameterization.
- [ ] Tests prove invalid fixtures fail for the intended reason and never emit public artifacts.
- [ ] CI invokes the relevant PMTiles negative fixture tests in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced short invalid-fixture stub with governed PMTiles invalid fixture README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
