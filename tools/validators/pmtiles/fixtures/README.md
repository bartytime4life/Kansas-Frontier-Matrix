<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-pmtiles-fixtures-readme
title: tools/validators/pmtiles/fixtures README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-pmtiles-steward-plus-fixture-steward-plus-publication-steward-plus-policy-steward-plus-release-steward-plus-evidence-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; pmtiles-validator-fixtures-index; synthetic-only; public-safe; attestation; positive-and-negative-fixtures; no-production-payloads; no-sensitive-payloads; release-gated; non-authoritative
owning_root: tools/
responsibility: parent fixture routing README for PMTiles validator fixture lanes under tools/validators/pmtiles; indexes valid and invalid fixture guidance, fixture safety rules, expected attestation coverage, positive and negative outcome posture, synthetic/public-safe payload constraints, and verification gaps while deferring real fixture bytes, schemas, policy decisions, evidence records, receipts, lifecycle data, tests, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - valid/README.md
  - invalid/README.md
  - ../../README.md
  - ../../_common/README.md
  - ../../maplibre/README.md
  - ../../lifecycle/README.md
  - ../../evidence/README.md
  - ../../geo_manifest/README.md
  - ../../../../docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md
  - ../../../../docs/standards/pmtiles/PMIDX_SPEC_V1.md
  - ../../../../docs/architecture/publication/GEO_MANIFEST.md
  - ../../../../contracts/release/release_manifest.md
  - ../../../../contracts/data/validation_report.md
  - ../../../../contracts/common/spec_hash.md
  - ../../../../schemas/contracts/v1/
  - ../../../../policy/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
  - ../../../../fixtures/
  - ../../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/pmtiles/fixtures/README.md."
  - "Child fixture guidance currently exists for valid/ and invalid/. Both are documentation lanes; they do not confirm actual fixture files."
  - "PMTiles fixtures are test inputs only. They are not production artifacts, source data, release artifacts, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, or AI sources."
  - "Fixture payloads must be synthetic, minimized, public-safe, deterministic, and free of sensitive exact locations, private source data, production payloads, credentials, secret keys, restricted geometry, and reconstruction hints."
  - "A validator-positive fixture is not publication approval; a validator-negative fixture is not a release artifact; both remain subordinate to evidence, policy, review, release, correction, rollback, and lifecycle gates."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/pmtiles/fixtures

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-pmtiles--fixtures--index-informational)
![payloads](https://img.shields.io/badge/payloads-synthetic--only-blueviolet)
![posture](https://img.shields.io/badge/posture-positive%20%2B%20negative-success)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/pmtiles/fixtures/` indexes PMTiles validator fixture guidance for positive and negative attestation cases while keeping fixture bytes synthetic, public-safe, minimized, non-authoritative, and separate from production artifacts, proof, receipts, policy, release, and publication authority.

---

## Purpose

`tools/validators/pmtiles/fixtures/` exists to make PMTiles fixture expectations navigable for maintainers who test publication-gate validators.

The durable KFM question for this parent fixture lane is:

> Which synthetic PMTiles, PMIDX, PMSIG, RunReceipt, policy-reference, release-reference, correction, rollback, and public-surface fixture classes should pass or fail PMTiles validators deterministically without becoming production tile artifacts, source data, EvidenceBundles, receipts, release records, public map layers, or publication approval?

The answer should be a small, deterministic fixture index with explicit valid and invalid lanes. This folder should not create PMTiles truth, tile truth, source truth, release truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, production tile archives, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/pmtiles/fixtures/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/pmtiles/fixtures/valid/README.md` | **CONFIRMED README / fixture files NEEDS VERIFICATION** | Positive fixture guidance for synthetic valid attestation chains; valid fixture status is not publication approval. |
| `tools/validators/pmtiles/fixtures/invalid/README.md` | **CONFIRMED README / fixture files NEEDS VERIFICATION** | Negative fixture guidance for fail-closed attestation, policy, release, rollback, stale-state, and public-surface cases. |
| `tools/validators/pmtiles/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Parent PMTiles validator README describes fail-closed helpers and expected artifact inputs. |
| `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines required artifact set, `spec_hash` reconciliation, publication gate, and fail-closed conditions. |
| Fixture files | **NOT CLAIMED** | File names in child READMEs are fixture classes/examples, not proof that matching files exist. |
| Executable tests, schema bindings, policy bundles, report destinations, receipt emission, release integration, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Child lanes

| Lane | Purpose | Status |
|---|---|---|
| [`valid/`](valid/README.md) | Documents positive PMTiles attestation fixture classes: complete artifact sets, reconciled `spec_hash`, valid headers, PMIDX sidecars, range proofs, PMSIG signatures, RunReceipts, policy-reference stubs, release-reference stubs, correction/rollback linkage, and MapLibre-safe descriptors. | **CONFIRMED README / fixture files NEEDS VERIFICATION** |
| [`invalid/`](invalid/README.md) | Documents negative PMTiles attestation fixture classes: missing/malformed `spec_hash`, header mismatch, digest mismatch, PMIDX/Merkle failure, invalid range proof, bad signature, signer denial, RunReceipt mismatch, policy gaps, release gaps, stale/superseded artifacts, rollback mismatch, and public-surface bypass. | **CONFIRMED README / fixture files NEEDS VERIFICATION** |

Do not add another child lane unless it has a distinct fixture policy, payload class, validator route, or risk boundary. Broad fixture metadata should live here; positive and negative fixture specifics should stay in `valid/` and `invalid/`.

[Back to top](#top)

---

## Fixture-set invariant

Valid and invalid PMTiles fixture lanes must preserve the same KFM boundaries:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A fixture may exercise publication-gate validators, but it is not publication. Fixture acceptance does not prove source truth, evidence closure, policy approval, release approval, public safety, or real-world correctness. Fixture rejection does not itself write quarantine state, proof records, receipts, rollback records, or release decisions.

[Back to top](#top)

---

## Fixture safety rules

Every fixture described under this tree must be:

- synthetic or minimized;
- public-safe;
- deterministic;
- reviewable in repository context;
- tied to a documented expected outcome;
- unable to be mistaken for production or released artifacts;
- free of sensitive exact locations, protected locations, private source payloads, private parcel/person links, infrastructure exposure, archaeology locations, rare-species locations, DNA/genomic data, credentials, private keys, tokens, and reconstruction hints;
- excluded from public artifacts, release manifests, catalog truth, and map runtime loading unless separately promoted through governed release.

Invalid fixtures should fail for the intended reason. Valid fixtures should pass for the intended reason. Any fixture that unexpectedly passes, unexpectedly fails, requires a network fetch, depends on production artifacts, emits a public artifact, or exposes sensitive information should be treated as a fixture defect or validator defect.

[Back to top](#top)

---

## Coverage matrix

| Fixture concern | Positive lane | Negative lane | Boundary |
|---|---|---|---|
| Artifact set | Complete PMTiles + PMIDX + PMSIG + RunReceipt + release-reference stubs | Missing or incomplete artifact set | Fixture set is not a release artifact. |
| `spec_hash` | Reconciled across metadata, sidecar, signature, receipt, and release/promotion reference | Missing, malformed, or mismatched | Hash integrity is not truth or release approval. |
| PMTiles header | Valid metadata, bounds, zoom, digest posture | Altered header, policy-violating bounds/zoom, malformed metadata | Header is not source truth. |
| PMIDX sidecar | Valid schema, archive digest, Merkle root, range proof | Schema invalid, Merkle mismatch, range proof invalid | Sidecar is integrity support, not release. |
| PMSIG signature | Fixture-safe test signer and valid subject | Missing, invalid, expired, forged, denied signer | Test signer is not production release authority. |
| RunReceipt | Matching source refs, toolchain, spec hash, output digest | Missing or mismatched builder/source/toolchain/output | Receipt support is not policy or release approval. |
| Policy/reference posture | Fixture-scope policy/reference stubs present | Rights/sensitivity/source-role/review unresolved | Policy stubs are not real PolicyDecisions. |
| Release/correction/rollback | Fixture-scope release/correction/rollback reference shape present | Missing release, stale artifact, rollback mismatch, correction gap | Reference shape is not a ReleaseManifest. |
| MapLibre/public surface | Descriptor points only to fixture-safe test artifact refs | Browser/public-surface bypass | Public runtime remains governed and release-gated. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| PMTiles fixture parent index | `tools/validators/pmtiles/fixtures/` |
| Positive PMTiles fixture guidance | `tools/validators/pmtiles/fixtures/valid/` |
| Negative PMTiles fixture guidance | `tools/validators/pmtiles/fixtures/invalid/` |
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

- **CONFIRMED:** this README exists, and child README lanes exist for `valid/` and `invalid/`.
- **PROPOSED:** fixture files may live below child lanes only if they are synthetic, minimized, public-safe, deterministic, reviewable, and tied to documented outcomes.
- **NEEDS VERIFICATION:** exact fixture files, schemas, policy bundles, validator scripts, test paths, report destinations, receipt emission, release integration, and CI wiring.
- **DENY:** using this folder as a PMTiles artifact store, release artifact store, source payload store, lifecycle data store, proof store, receipt store, policy home, schema home, public runtime surface, map tile service, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/pmtiles/fixtures/` include:

- this parent fixture README;
- child README lanes for `valid/` and `invalid/`;
- small fixture indexes that map fixture names to expected outcomes, checksums, and validator routes, if accepted;
- synthetic/minimized payloads only in child lanes and only when tied to deterministic tests;
- notes about fixture reconstruction, review expectations, and safety constraints;
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
tools/validators/pmtiles/fixtures/
├── README.md
├── valid/
│   ├── README.md
│   └── fixture_index.json                # PROPOSED; not confirmed
└── invalid/
    ├── README.md
    └── fixture_index.json                # PROPOSED; not confirmed
```

Do not add fixture payloads unless the expected validator outcome is documented, the fixture is synthetic/public-safe, and a test can prove the fixture passes or fails for the intended reason without granting publication authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/pmtiles/fixtures/README.md`.
- [x] It indexes the confirmed `valid/` and `invalid/` fixture guidance lanes.
- [x] It marks this path as PMTiles fixture guidance, not artifact, proof, receipt, policy, release, public runtime, or AI authority.
- [x] It preserves PMTiles attestation fixture posture for header, `spec_hash`, PMIDX, PMSIG, RunReceipt, policy reference, release reference, correction, rollback, stale-state, and MapLibre/public-surface cases.
- [x] It forbids sensitive, unreleased, production-derived, credential-bearing, private, or reconstruction-capable payloads.
- [x] It distinguishes validator fixture status from publication approval.
- [x] It marks fixture files, executable tests, schema bindings, policy bundles, receipt emission, release integration, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to PMTiles fixtures are searched and classified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads.
- [ ] Each fixture has an expected finite outcome in a fixture index or test parameterization.
- [ ] Tests prove valid fixtures pass and invalid fixtures fail for the intended reason.
- [ ] CI invokes the relevant PMTiles fixture tests in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with PMTiles fixture parent index. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
