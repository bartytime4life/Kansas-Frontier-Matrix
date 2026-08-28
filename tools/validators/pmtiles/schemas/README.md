<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-pmtiles-schemas-readme
title: tools/validators/pmtiles/schemas README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-pmtiles-steward-plus-schema-steward-plus-publication-steward-plus-policy-steward-plus-release-steward-plus-evidence-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; pmtiles-validator-schema-routing; schema-binding; pmidx; pmsig; runreceipt; spec-hash; attestation; derived-artifacts-only; release-gated; non-authoritative
owning_root: tools/
responsibility: schema-routing README for PMTiles validators under tools/validators/pmtiles; documents schema-binding expectations for PMTiles metadata, PMTiles build spec, PMIDX sidecar, PMSIG signature bundle, RunReceipt, release/rollback references, validation reports, fixture indexes, and MapLibre/public-surface descriptor checks while deferring machine schema authority, policy decisions, evidence records, receipts, lifecycle data, tests, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../fixtures/README.md
  - ../fixtures/valid/README.md
  - ../fixtures/invalid/README.md
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
  - "This README replaces an empty placeholder at tools/validators/pmtiles/schemas/README.md. It does not confirm local schema files exist."
  - "Machine schema authority should live under accepted schemas/contracts/v1/ homes unless an accepted ADR or migration note explicitly permits local validator-owned schemas."
  - "PMIDX_SPEC_V1.md references tools/validators/pmtiles/schemas/pmidx.schema.json. That local-schema reference is treated here as NEEDS VERIFICATION / compatibility, not confirmed schema authority."
  - "PMTiles validator schema bindings should verify shape and schema identity; they do not prove truth, evidence closure, policy approval, release approval, or public safety."
  - "PMTiles archives are derived publication artifacts, not canonical truth. Public clients may consume only released artifacts and governed APIs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/pmtiles/schemas

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-pmtiles--schema--routing-informational)
![authority](https://img.shields.io/badge/authority-routing--not--schema--home-lightgrey)
![posture](https://img.shields.io/badge/posture-release--gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/pmtiles/schemas/` documents schema-binding expectations for PMTiles validators while keeping schema authority in accepted `schemas/` homes unless an accepted ADR says otherwise.

---

## Purpose

`tools/validators/pmtiles/schemas/` exists to make PMTiles validator schema expectations inspectable without turning a validator folder into a parallel schema authority.

The durable KFM question for this lane is:

> Which schema identifiers, versions, digests, canonicalization rules, and binding checks must PMTiles validators use when evaluating PMTiles metadata, build specs, PMIDX sidecars, PMSIG bundles, RunReceipts, fixture indexes, release/rollback references, validation reports, and MapLibre/public-surface descriptors?

The answer should be a deterministic schema-routing and binding posture. This folder should not create machine schema authority, PMTiles truth, tile truth, source truth, release truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, production tile archives, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/pmtiles/schemas/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/pmtiles/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Parent README describes fail-closed helpers for header validation, PMIDX schema/digest/Merkle checks, and expected artifact inputs. |
| `docs/standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md` | **CONFIRMED standard / implementation NEEDS VERIFICATION** | Defines required artifact set, `spec_hash` reconciliation, publication gate, fail-closed conditions, and definition-of-done schema checks. |
| `docs/standards/pmtiles/PMIDX_SPEC_V1.md` | **CONFIRMED standard / local schema home NEEDS VERIFICATION** | Defines PMIDX required fields and verifier rejection conditions; references a local schema path that requires placement review. |
| Local schema files under `tools/validators/pmtiles/schemas/` | **NOT CLAIMED** | This README does not confirm `pmidx.schema.json`, PMSIG schema, build-spec schema, fixture-index schema, or any other local schema file exists. |
| Accepted canonical schema homes | **NEEDS VERIFICATION** | Use accepted `schemas/contracts/v1/` homes or ADR-selected schema homes once confirmed. |
| Executable tests, schema digests, policy bundles, report destinations, receipt emission, release integration, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

`tools/validators/pmtiles/schemas/` is treated as a **validator-local schema routing and compatibility lane**, not as canonical machine-shape authority.

| Question | Answer |
|---|---|
| Can this folder document schema bindings used by PMTiles validators? | **Yes.** |
| Can this folder contain temporary compatibility schema copies? | **PROPOSED / NEEDS VERIFICATION** — only with an accepted ADR, migration note, or explicit test-scoped exception. |
| Can this folder become the canonical schema home for PMTiles, PMIDX, PMSIG, RunReceipt, or ReleaseManifest shape? | **No, unless an accepted ADR changes schema placement.** |
| Where should canonical machine shape live by default? | `schemas/contracts/v1/` or another accepted schema home. |
| Where should semantic meaning live? | `contracts/` and standards/docs, not validator-local schema files. |
| Where should policy and release decisions live? | `policy/` and `release/`, not schema files or validators. |

The reference from `PMIDX_SPEC_V1.md` to `tools/validators/pmtiles/schemas/pmidx.schema.json` is recorded as **NEEDS VERIFICATION**. If that file exists later, maintainers should decide whether it is a temporary validator test schema, a generated mirror from `schemas/`, or drift requiring migration.

[Back to top](#top)

---

## Schema-binding expectations

PMTiles validators should bind to schemas or schema-equivalent contracts for the following object families:

| Object family | Binding expectation | Authority posture |
|---|---|---|
| PMTiles metadata | Metadata must expose required build/spec identity, artifact digest, bounds/zoom, and policy-relevant fields. | PMTiles metadata is not truth or release. |
| PMTiles build spec | Build spec must canonicalize deterministically and produce a reproducible `spec_hash`. | `spec_hash` is integrity/reference posture, not evidence closure. |
| PMIDX sidecar | Sidecar shape must include schema version, `spec_hash`, PMTiles digest, Merkle metadata, root, leaves, and optional range commitments as required. | PMIDX is sidecar integrity support, not publication. |
| PMSIG bundle | Signature bundle shape must bind archive digest, sidecar root, `spec_hash`, signer, validity interval, and algorithm as required by accepted policy. | Signature validates subject integrity; it is not policy approval. |
| RunReceipt | Receipt shape must bind builder identity, source refs, toolchain, build spec, output digest, run timing, and replay context. | Receipt is provenance support, not release approval. |
| Release/rollback reference | Candidate must point to release, correction, rollback, or withdrawal references required for its intended use. | Reference shape is not a ReleaseManifest by itself. |
| ValidationReport | Validator output should follow accepted validation report shape and finite outcome vocabulary. | Validation report is not proof closure or release approval. |
| Fixture index | Fixture index should map fixture id, path, checksum, intended validator, expected outcome, and safety classification. | Fixture index is test support, not artifact truth. |
| MapLibre descriptor | Public-surface descriptor checks should bind to accepted layer/source/style/tile descriptor schemas. | Renderer descriptor is downstream carrier only. |

[Back to top](#top)

---

## Required reconciliation checks

PMTiles schema-bound validation should verify that:

- the declared schema id and version are present where required;
- schema ids are from accepted schema homes or explicitly documented test/compatibility homes;
- `spec_hash` uses accepted canonicalization and digest syntax;
- the same `spec_hash` reconciles across PMTiles metadata, PMIDX sidecar, PMSIG signed payload, RunReceipt, and release/promotion reference where applicable;
- PMTiles archive digest reconciles with PMIDX, PMSIG, RunReceipt, and release/reference metadata;
- PMIDX fields are present, correctly typed, and internally consistent;
- PMSIG fields are present, correctly typed, and do not imply production trust when fixture-only keys are used;
- RunReceipt fields reconcile builder, source refs, toolchain, build spec, output digest, and replay context;
- policy/release references are present where required without treating schema validity as policy approval;
- invalid fixtures fail for the intended schema/binding reason;
- valid fixtures pass for the intended schema/binding reason;
- validation reports write finite outcomes without publishing artifacts.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| PMTiles validator schema-routing README | `tools/validators/pmtiles/schemas/` |
| PMTiles validator docs and possible helper scripts | `tools/validators/pmtiles/` |
| PMTiles fixture guidance | `tools/validators/pmtiles/fixtures/` |
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

- **CONFIRMED:** this README exists.
- **PROPOSED:** local schema files may live here only as compatibility/test-scoped bindings or generated mirrors if an accepted ADR or migration note permits that placement.
- **NEEDS VERIFICATION:** exact schema files, canonical schema homes, schema ids, schema digests, validator scripts, fixture files, policy bundles, test paths, report destinations, receipt emission, release integration, and CI wiring.
- **DENY:** using this folder as canonical schema authority, PMTiles artifact store, release artifact store, source payload store, lifecycle data store, proof store, receipt store, policy home, public runtime surface, map tile service, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/pmtiles/schemas/` include:

- this schema-routing README;
- schema binding notes for PMTiles validator inputs and outputs;
- compatibility notes for legacy/local schema references that are being migrated to `schemas/`;
- generated schema mirrors only if an accepted ADR or migration note permits them;
- test-only schema stubs only if they are clearly labeled and cannot be mistaken for canonical schema authority;
- notes mapping schema validation failures to finite validator outcomes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Canonical JSON Schemas, DTOs, enums, or machine shape unless ADR-approved | `schemas/contracts/v1/...` or accepted schema homes |
| Semantic contracts | `contracts/` |
| PMTiles, COGs, GeoParquet, MVT/MLT bundles, sprites, glyphs, screenshots, or exports | governed lifecycle/release artifact homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Source descriptors or source registries | `data/registry/`, `data/registry/sources/` |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| Policy rules, release gates, steward decisions, sensitivity thresholds | `policy/`, `release/` |
| Secrets, production signing keys, real credentials, private source content, sensitive exact locations, or reconstruction hints | denied here; keep out of repository-facing docs and fixtures |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `PMTILES_SCHEMA_BINDING_PASS` | Candidate passed configured schema-binding checks. |
| `PMTILES_SCHEMA_BINDING_FAIL` | Candidate failed one or more configured schema-binding checks. |
| `PMTILES_SCHEMA_HOME_UNVERIFIED` | Candidate references a schema path not confirmed as accepted. |
| `PMTILES_SCHEMA_ID_MISSING` | Required schema id or schema version is absent. |
| `PMTILES_SCHEMA_DIGEST_MISSING` | Required schema digest or spec-hash binding is absent. |
| `PMTILES_SCHEMA_INVALID` | Candidate fails accepted machine-shape validation. |
| `PMIDX_SCHEMA_INVALID` | PMIDX sidecar fails accepted schema checks. |
| `PMSIG_SCHEMA_INVALID` | PMSIG bundle fails accepted schema checks. |
| `RUNRECEIPT_SCHEMA_INVALID` | RunReceipt fails accepted schema checks. |
| `FIXTURE_INDEX_SCHEMA_INVALID` | Fixture index fails accepted schema checks. |
| `SPEC_HASH_CANONICALIZATION_MISSING` | Candidate lacks accepted canonicalization posture for spec hash. |
| `SPEC_HASH_RECONCILIATION_FAILED` | `spec_hash` does not reconcile across required attestation artifacts. |
| `SCHEMA_VALIDITY_OVERCLAIM` | Candidate treats schema validity as evidence closure, policy approval, release approval, or public safety. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, rollback, or withdrawal reference is absent. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsafe or unreleased content to MapLibre, public clients, exports, screenshots, Focus Mode, graph, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/pmtiles/schemas/
├── README.md
├── pmidx.schema.json                    # PROPOSED compatibility/test mirror; not confirmed
├── pmsig.schema.json                    # PROPOSED compatibility/test mirror; not confirmed
├── pmtiles-build-spec.schema.json       # PROPOSED compatibility/test mirror; not confirmed
└── fixture-index.schema.json            # PROPOSED compatibility/test mirror; not confirmed
```

Do not add local schema files unless the placement decision is documented and the canonical schema relationship is explicit. A generated local mirror should identify its canonical source, generation command, spec hash, and update rule.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/pmtiles/schemas/README.md`.
- [x] It marks this path as PMTiles schema-routing guidance, not canonical schema, artifact, proof, receipt, policy, release, public runtime, or AI authority.
- [x] It records the local-schema reference in `PMIDX_SPEC_V1.md` as **NEEDS VERIFICATION / compatibility**, not confirmed schema authority.
- [x] It routes canonical machine shape to accepted `schemas/contracts/v1/` homes or ADR-selected schema homes.
- [x] It preserves PMTiles attestation schema-binding posture for PMTiles metadata, build spec, PMIDX, PMSIG, RunReceipt, fixture index, validation report, release references, correction, rollback, and MapLibre/public-surface descriptors.
- [x] It distinguishes schema validity from truth, evidence closure, policy approval, release approval, and public safety.
- [x] It marks schema files, schema ids, schema digests, executable tests, policy bundles, receipt emission, release integration, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Canonical schema homes for PMTiles metadata, PMIDX, PMSIG, RunReceipt, fixture index, and PMTiles build spec are verified.
- [ ] Any local compatibility schema files are either migrated, generated from canonical schemas, or ADR-approved.
- [ ] Validator registry or CLI references to PMTiles schema validation are searched and classified.
- [ ] Tests prove schema-valid and schema-invalid fixtures pass/fail for the intended reason.
- [ ] CI invokes the relevant PMTiles schema-binding tests in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with PMTiles schema-routing README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
