<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-hydro-fixtures-readme
title: tools/validators/hydro/fixtures README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-fixture-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; validator-fixture-routing; hydrology; hydro-alias; synthetic-only; not-flood-warning; non-authoritative
owning_root: tools/
responsibility: validator-local fixture routing README for the scaffolded hydro validator lane; documents what fixture references may support Hydrology validator development while deferring canonical fixture storage, Hydrology meaning, schemas, policy, evidence, receipts, proofs, lifecycle data, and release decisions to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../_common/README.md
  - ../../domains/hydrology/README.md
  - ../../atmosphere_hydrology/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../hazards/README.md
  - ../../domains/hazards/README.md
  - ../../../../fixtures/domains/hydrology/
  - ../../../../fixtures/validators/hydrology/
  - ../../../../tests/validators/hydro/
  - ../../../../tests/validators/domains/hydrology/
  - ../../../../tests/domains/hydrology/
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/hydrology/ARCHITECTURE.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/domains/hydrology/GLOSSARY.md
  - ../../../../docs/domains/hydrology/INDEX.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/release/hydrology/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../data/proofs/hydrology/README.md
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file at tools/validators/hydro/fixtures/README.md. It does not confirm fixture files, executable validator code, tests, or CI wiring."
  - "Directory Rules identify root fixtures/ as the home for golden, valid, or invalid sample data for tests. This tools-local fixtures path is therefore a routing/index surface unless an accepted convention says otherwise."
  - "tools/validators/hydro/README.md is a scaffold sourced from planned/missing files and says fixtures belong in fixtures/ unless an accepted ADR says otherwise."
  - "tools/validators/domains/hydrology/README.md remains the richer per-domain Hydrology validator index."
  - "No real gauge readings, restricted wells, private property context, exact sensitive infrastructure locations, operational warnings, emergency instructions, or release-authoritative objects belong here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/hydro/fixtures

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydro--validator--fixtures-informational)
![fixture](https://img.shields.io/badge/fixtures-synthetic--routing-lightgrey)
![boundary](https://img.shields.io/badge/not--flood--warning-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/hydro/fixtures/` documents validator-local fixture expectations for the scaffolded `hydro` validator lane, while canonical golden, valid, and invalid fixture data should live under accepted `fixtures/` roots unless an ADR or validator convention says otherwise.

---

## Purpose

`tools/validators/hydro/fixtures/` exists to keep Hydrology validator fixture expectations inspectable without turning a validator folder into a data, proof, receipt, schema, policy, release, or domain-truth store.

The durable KFM question for this README is:

> What synthetic or non-authoritative fixture shapes should Hydrology validators use to test source-role separation, HUC/reach/gauge identity, observation-vs-model-vs-regulatory boundaries, time/freshness posture, not-flood-warning posture, evidence references, policy decisions, release references, correction paths, rollback targets, and public-surface denial without storing real lifecycle data or official hydrology truth in a validator folder?

The answer should be routing guidance for future fixture authors and validator maintainers. This folder should not store authoritative Hydrology data, real EvidenceBundles, proof packs, receipts, release decisions, public map outputs, emergency instructions, flood warnings, regulatory determinations, or AI-facing truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/hydro/fixtures/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| `tools/validators/hydro/README.md` | **CONFIRMED scaffold** | Parent `hydro` path is a proposed scaffold and says fixtures belong in `fixtures/` unless an accepted ADR says otherwise. |
| `tools/validators/domains/hydrology/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Richer per-domain Hydrology validator index; current implementation behavior remains unverified. |
| Canonical root fixture storage | **PROPOSED / NEEDS VERIFICATION** | Candidate homes include `fixtures/domains/hydrology/` and `fixtures/validators/hydrology/`; existence and accepted convention need verification before use. |
| Local fixture files in this folder | **NOT CLAIMED** | No JSON, YAML, GeoJSON, parquet, CSV, raster, tile, report, proof, or receipt fixtures are claimed by this README. |
| Executables, schema bindings, test harnesses, policy bundles, receipt emission, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

Directory Rules make the responsibility split explicit:

| Responsibility | Preferred root |
|---|---|
| Repo-wide validator, generator, builder, checker | `tools/` |
| Golden, valid, or invalid sample data for tests | `fixtures/` |
| Tests that prove a rule is enforceable | `tests/` |
| Object meaning | `contracts/` |
| Machine shape | `schemas/` |
| Allow/deny/restrict/abstain rules | `policy/` |
| Lifecycle data | `data/` |
| Release decision, manifest, rollback, correction | `release/` |

Therefore this path should normally be a **fixture guide**, not the canonical fixture data store. If a validator needs local fixture snippets for developer ergonomics, keep them tiny, synthetic, non-sensitive, and clearly marked as non-authoritative. Prefer canonical fixture roots for reusable samples.

[Back to top](#top)

---

## Relationship to Hydrology validator lanes

| Path | Role | Boundary |
|---|---|---|
| `tools/validators/hydro/` | Scaffolded shorthand Hydrology validator lane. | Existing parent is a proposed scaffold, not full Hydrology authority. |
| `tools/validators/hydro/fixtures/` | This validator-local fixture routing surface. | Describes fixture expectations; should not store real hydrology data or proofs. |
| `tools/validators/domains/hydrology/` | Per-domain Hydrology validator index. | Richer Hydrology validator boundary for object families, identities, source roles, time posture, evidence, policy, release, correction, rollback, and public-surface denial. |
| `tools/validators/atmosphere_hydrology/` | Cross-domain Atmosphere/Hydrology overlap lane. | Weather, atmosphere, drought, precipitation, runoff, smoke/water interactions, and neighboring-domain boundaries. |
| `tools/validators/cross-domain-joins/` | Shared cross-domain join checks. | Prevents ownership, source-role, policy, and sensitivity collapse. |
| `fixtures/domains/hydrology/` | Candidate canonical domain fixture home. | **NEEDS VERIFICATION** before use. |
| `fixtures/validators/hydrology/` | Candidate validator fixture home. | **NEEDS VERIFICATION** before use. |

[Back to top](#top)

---

## Fixture classes

Future fixtures should be small, deterministic, synthetic, and designed to exercise one validator invariant at a time.

| Fixture class | Purpose | Example invariant |
|---|---|---|
| `valid_minimal_hydro_observation` | Minimal observation carrier with source role, units, timestamp, and EvidenceRef placeholder. | Observation keeps gauge/site identity and unit posture. |
| `invalid_missing_evidence_ref` | Candidate lacks required evidence pointer. | Validator returns `EVIDENCE_REF_MISSING`. |
| `invalid_source_role_collapse` | Regulatory, modeled, observed, and public-map roles are conflated. | Validator returns `SOURCE_ROLE_COLLAPSE`. |
| `invalid_nfhl_as_observed_flood` | NFHL/regulatory context is presented as observed inundation or forecast. | Validator denies regulatory/observed/future collapse. |
| `invalid_model_as_observation` | Modeled hydrograph or reconstructed flow is treated as a measured gauge reading. | Validator denies model-as-observation. |
| `invalid_stale_context_current` | Expired or superseded hydrologic context is represented as current. | Validator returns stale/freshness failure. |
| `invalid_flood_warning_authority` | Candidate presents KFM as a flood-warning, evacuation, or emergency-instruction authority. | Validator denies life-safety authority overclaim. |
| `invalid_cross_domain_policy_leak` | Hydrology join weakens Hazards, Infrastructure, Agriculture, People/Land, Habitat, or other neighboring-domain policy. | Validator propagates most-restrictive policy. |
| `invalid_release_gap` | Candidate lacks ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target. | Validator fails release readiness. |
| `invalid_public_surface_leakage` | Map, tile, popup, export, search, embedding, graph, Focus Mode, screenshot, or AI text overclaims or leaks unsupported hydrology context. | Validator denies public-surface leakage. |

[Back to top](#top)

---

## Minimal fixture metadata shape

Future fixture descriptors may use a lightweight manifest shape like this. This is **PROPOSED**, not a confirmed schema.

```yaml
fixture_id: hydro-fixture-example-001
status: synthetic
validator_lane: tools/validators/hydro
canonical_fixture_home: fixtures/validators/hydrology
case_type: invalid_missing_evidence_ref
expected_outcome: EVIDENCE_REF_MISSING
contains_real_source_data: false
contains_exact_sensitive_location: false
contains_operational_warning: false
contains_private_property_detail: false
requires_policy_bundle: policy/domains/hydrology
requires_schema_home: schemas/contracts/v1/domains/hydrology
notes: Synthetic fixture descriptor only; not an EvidenceBundle, receipt, release record, or official hydrology fact.
```

Do not treat this manifest sketch as a schema until a schema file, validator registry entry, and test harness are verified.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| This fixture README and local fixture guidance | `tools/validators/hydro/fixtures/` |
| Hydro validator scaffold | `tools/validators/hydro/` |
| Per-domain Hydrology validator index | `tools/validators/domains/hydrology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Canonical reusable fixture data | `fixtures/domains/hydrology/`, `fixtures/validators/hydrology/`, or accepted fixture home |
| Tests | `tests/validators/hydro/`, `tests/validators/domains/hydrology/`, `tests/domains/hydrology/`, or accepted test home |
| Hydrology domain meaning | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` or ADR-selected homes |
| Hydrology policy rules | `policy/domains/hydrology/`, `policy/release/hydrology/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/hydrology/` or accepted source registry home |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Lifecycle data | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, `data/catalog/...`, `data/published/...` |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** fixture descriptors may be referenced here if they remain synthetic, small, non-authoritative, and point to canonical fixture roots.
- **NEEDS VERIFICATION:** whether root-level `fixtures/` homes, test harnesses, schema bindings, validator registry entries, policy bundle digests, report destinations, receipt emission, runtime behavior, and CI wiring exist.
- **DENY:** using this folder as Hydrology doctrine, flood-warning authority, emergency-instruction surface, regulatory-determination authority, schema home, policy home, source registry, lifecycle data store, proof store, receipt store, release record store, or public map product surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/hydro/fixtures/` include:

- this README;
- tiny synthetic fixture descriptors used only to explain validator expectations;
- pointers to canonical fixture homes under `fixtures/`;
- fixture naming conventions and expected validator outcomes;
- notes for test authors on valid/invalid case families;
- non-sensitive examples that cannot be mistaken for real gauge readings, well locations, flood warnings, official observations, or release records.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/hydro/fixtures/` | Correct home |
|---|---|
| Real hydrology source extracts | `data/raw/hydrology/` through governed lifecycle roots |
| Work-in-progress or quarantined hydrology data | `data/work/hydrology/`, `data/quarantine/hydrology/` |
| Processed, cataloged, triplet, or published hydrology data | accepted `data/` lifecycle roots |
| EvidenceBundles, proof packs, receipts, validation reports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, rollback cards, correction notices | `release/` |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` |
| Hydrology policy rules | `policy/domains/hydrology/`, `policy/release/hydrology/` |
| Source descriptors | `data/registry/sources/hydrology/` |
| Authoritative domain docs or contracts | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Tests | `tests/validators/...`, `tests/domains/...` |
| Canonical reusable fixtures | root `fixtures/` homes once accepted and verified |
| Public API, UI, map, tile, search, graph, Focus Mode, export, screenshot, or AI runtime output | governed application/runtime roots |
| Current flood warnings, evacuation advice, dam-safety instructions, navigation safety advice, or regulatory determinations | official agencies and governed source systems, not KFM fixture docs |

[Back to top](#top)

---

## Fixture safety rules

Fixture authors should keep every sample:

- synthetic or fully scrubbed;
- small enough for review in a pull request;
- deterministic across machines;
- free of real private well locations, private property details, critical infrastructure exposure, emergency operations details, restricted water-system information, and current operational warning text;
- explicit about expected validator outcome;
- explicit about whether the fixture is valid or invalid;
- bounded to one or two invariants per fixture;
- linked to the validator lane, schema home, policy home, and test path it is meant to exercise;
- unable to be mistaken for EvidenceBundle, Proof, Receipt, ReleaseManifest, official warning, regulatory determination, or public map product.

[Back to top](#top)

---

## Standard fixture outcomes

| Outcome | Meaning |
|---|---|
| `FIXTURE_VALID_SYNTHETIC` | Fixture is synthetic, minimal, and safe to use for validator tests. |
| `FIXTURE_INVALID_BY_DESIGN` | Fixture intentionally violates a named invariant. |
| `FIXTURE_REAL_DATA_DENIED` | Fixture appears to contain real source data or lifecycle data. |
| `FIXTURE_SENSITIVE_LOCATION_DENIED` | Fixture includes exact or reverse-engineerable sensitive location context. |
| `FIXTURE_OPERATIONAL_WARNING_DENIED` | Fixture includes current or official warning/advisory text that could be mistaken for life-safety guidance. |
| `FIXTURE_SCHEMA_HOME_MISSING` | Fixture references an unverified or missing schema home. |
| `FIXTURE_POLICY_HOME_MISSING` | Fixture references an unverified or missing policy home. |
| `FIXTURE_EXPECTED_OUTCOME_MISSING` | Fixture does not declare the expected validator outcome. |
| `FIXTURE_EVIDENCE_AUTHORITY_COLLAPSE` | Fixture is presented as EvidenceBundle, proof, receipt, or release record. |
| `FIXTURE_PUBLIC_SURFACE_LEAKAGE` | Fixture can leak into map, tile, export, graph, search, Focus Mode, screenshot, embedding, or AI surfaces as apparent truth. |

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/hydro/fixtures/README.md`.
- [x] It marks this path as validator-local fixture guidance, not canonical fixture data storage.
- [x] It points canonical reusable fixtures toward accepted `fixtures/` roots.
- [x] It links the scaffolded `hydro` lane to the richer per-domain `hydrology` validator index.
- [x] It preserves not-flood-warning, source-role, identity, freshness, evidence, policy, release, correction, rollback, and public-surface denial boundaries.
- [x] It marks executable behavior, fixture files, test harnesses, schema bindings, policy bundles, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Accepted fixture homes are verified.
- [ ] Fixture file names, manifest shape, and schema bindings are accepted.
- [ ] Tests exercise valid and invalid Hydrology fixture families.
- [ ] CI invokes the relevant Hydrology validator fixture tests in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with Hydrology validator fixture routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
