<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-land-cover-layer-manifest-readme
title: Habitat Land-Cover Layer-Manifest Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Layer steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; land-cover; layer-manifest; no-network; artifact-integrity-aware; source-role-aware; evidence-bound; release-gated; public-safe-layer
tags: [kfm, tests, habitat, land_cover, layer_manifest, LayerManifest, DomainLayerDescriptor, layer-registry, artifact-digest, freshness, source-role, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, MapLibre, EvidenceDrawer, FocusMode, ABSTAIN, DENY]
related:
  - ../../../../README.md
  - ../../../../../fixtures/domains/habitat/land_cover/layer_manifest/README.md
  - ../../../../../contracts/data/layer_manifest.md
  - ../../../../../contracts/data/layer_descriptor.md
  - ../../../../../contracts/data/layer_catalog_item.md
  - ../../../../../contracts/domains/habitat/domain_layer_descriptor.md
  - ../../../../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../../../../schemas/contracts/v1/domains/habitat/domain_layer_descriptor.schema.json
  - ../../../../../data/registry/layers/habitat/README.md
  - ../../../../../data/published/layers/habitat/land_cover/README.md
  - ../../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../../docs/domains/habitat/MAP_UI_CONTRACTS.md
  - ../../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../../../contracts/domains/habitat/land_cover/class_scheme.md
  - ../../../../../contracts/domains/habitat/land_cover/crosswalk.md
  - ../../../../../contracts/domains/habitat/land_cover/change_summary.md
  - ../../../../../pipelines/domains/habitat/land_cover/
  - ../../../../../pipeline_specs/habitat/land_cover/
  - ../../../../../policy/domains/habitat/
  - ../../../../../policy/sensitivity/habitat/
  - ../../../../../release/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/land_cover/layer_manifest/README.md."
  - "This is a test-lane README only. It does not define Habitat land-cover doctrine, layer contracts, schemas, source descriptors, layer registry records, fixtures, lifecycle records, evidence bundles, receipts, proofs, policy rules, release decisions, renderer code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that LayerManifest/DomainLayerDescriptor-style land-cover layer support must bind layer identity, artifact refs, artifact digests, source roles, evidence refs, integrity checks, freshness, rights, policy, review, release relationship, correction state, supersession, and rollback context without becoming source truth, evidence closure, policy approval, release approval, renderer implementation, public tile truth, or AI truth."
  - "The default posture is deterministic and no-network. Live source checks, credentials, real source exports, real layer payloads, public tiles, and sensitive occurrence joins do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat land-cover layer-manifest tests

> Deterministic, no-network test documentation for proving that Habitat land-cover layer manifests and descriptors preserve layer identity, artifact integrity, source-role badges, evidence posture, freshness, policy/review/release state, correction, supersession, and rollback without turning renderer output, tiles, popups, catalogs, or AI text into source truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: LayerManifest" src="https://img.shields.io/badge/object-LayerManifest-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: manifest not release" src="https://img.shields.io/badge/boundary-manifest__not__release-success">
</p>

**Path:** `tests/domains/habitat/land_cover/layer_manifest/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `land_cover/layer_manifest`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED the paired fixture README defines layer-manifest fixtures as toy layer-version metadata, artifact pointers, source-role badges, evidence pointers, integrity checks, freshness state, release-facing checks, correction state, and rollback posture for viewing products · CONFIRMED `LayerManifest` is a governed layer-version manifest and not raw data, renderer implementation, proof closure, policy approval, or release approval · CONFIRMED Habitat `DomainLayerDescriptor` is layer-support semantics and not a `LayerManifest`, release manifest, EvidenceBundle, PolicyDecision, source registry, public tile, renderer style, or AI answer · NEEDS VERIFICATION for executable test modules, fixture payload inventory, schema enforcement, validator paths, layer-registry records, policy runtime, release integration, public route/UI behavior, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/land_cover/layer_manifest/` is the intended home for tests that prove Habitat land-cover layer manifests, layer descriptors, and layer-registry pointers stay inside their governed meaning.

This lane should test that layer-facing records cannot silently become:

- source records or lifecycle data;
- EvidenceBundles or proof closure;
- PolicyDecisions or review approvals;
- ReleaseManifests or promotion decisions;
- public API material, public map material, public tiles, or published artifacts;
- renderer styles, UI legends, popups, graph projections, or AI answers;
- Habitat truth or land-cover observation truth by themselves.

A passing test here should **not** mean that a real layer exists, a public tile is published, a public route is wired, or a release manifest is accepted. It should mean only that layer-manifest guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat land-cover layer-manifest tests | `tests/domains/habitat/land_cover/layer_manifest/` | This directory. |
| Synthetic layer-manifest fixtures | `fixtures/domains/habitat/land_cover/layer_manifest/` | Preferred toy inputs and expected outcomes. |
| Generic layer-manifest meaning | `contracts/data/layer_manifest.md` | Referenced contract; tests do not redefine it. |
| Habitat layer-support meaning | `contracts/domains/habitat/domain_layer_descriptor.md` | Referenced contract; tests do not redefine it. |
| Machine schemas | `schemas/contracts/v1/data/layer_manifest.schema.json`, `schemas/contracts/v1/domains/habitat/domain_layer_descriptor.schema.json` | Referenced by tests; scaffold/conflict posture must be respected. |
| Layer registry | `data/registry/layers/habitat/` | Registry/control records; tests do not create registry authority. |
| Published layer artifacts | `data/published/layers/habitat/land_cover/` | Released artifacts only after governed promotion. |
| Land-cover source contracts | `contracts/domains/habitat/land_cover/` | Source classes, crosswalks, observations, summaries, and uncertainty remain separate. |
| Policy and sensitivity homes | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Pipeline logic and specs | `pipelines/domains/habitat/land_cover/`, `pipeline_specs/habitat/land_cover/` | Systems under test where accepted; not duplicated here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, supersession, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Layer manifest is a governed carrier, not release authority.** Land-cover layer manifests and descriptors may bind layer identity, product lineage, evidence posture, integrity references, valid time, freshness, source roles, rights, sensitivity, policy posture, review state, release relationship, correction, supersession, and rollback. They must not become raw data, renderer implementation, proof closure, policy approval, release approval, public tile truth, or AI truth.

For this test lane, the invariant decomposes into ten checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Layer identity | Layer ID, layer key, version, object family, product family, and digest basis are explicit. | validation failure / `ERROR`. |
| Artifact integrity | Artifact refs, artifact digests, schema/digest algorithms, and payload family are explicit. | validation failure / review required. |
| Source-role badges | Observed, modeled, regulatory, derivative, aggregate, administrative, candidate, synthetic, or context badges are preserved. | `DENY` / validation failure. |
| Evidence posture | Displayed claims resolve `EvidenceRef -> EvidenceBundle` or produce a finite non-answer. | `ABSTAIN`. |
| Rights and sensitivity | Rights, attribution, geoprivacy, redaction, aggregation, restricted-view, or deny posture is explicit where material. | `DENY` / `RESTRICT`. |
| Freshness and time | Valid time, source time, retrieval time, release time, correction time, stale state, and supersession state remain distinct. | validation failure / stale marker required. |
| Registry relationship | Layer registry pointers are control metadata, not layer bytes or release authority. | validation failure. |
| Release relationship | Manifest/descriptor points to release state but does not create release. | promotion-blocking failure. |
| UI boundary | Renderer styles, popups, legends, tiles, Evidence Drawer, Focus Mode, and AI answers remain downstream carriers. | `ABSTAIN` / validation failure. |
| Rollback readiness | Public-facing candidates preserve correction, supersession, withdrawal, and rollback target. | promotion-blocking failure. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- required layer ID, layer version, product family, object family, and artifact refs;
- rejection of missing artifact digest or mismatched artifact digest;
- preservation of source-role badges through layer-manifest, registry, descriptor, API, renderer, Evidence Drawer, and Focus Mode examples;
- non-answer behavior when displayed claims lack EvidenceBundle support;
- denial/restriction when sensitive habitat, occurrence-linked context, rare species, rare plants, stewardship zones, or private-context detail could leak through layer metadata or artifacts;
- failure when a descriptor, manifest, registry record, tile, style, popup, or AI answer is treated as release approval or source truth;
- freshness, stale, superseded, withdrawn, corrected, degraded, restricted, and rollback-ready state handling;
- public-carrier failure when policy, review, release, correction, or rollback posture is missing.

Live source downloads, real layer payloads, real source exports, public tile generation, real sensitive occurrence joins, and provider credentials are out of scope for the default suite.

---

## Fixture posture

Use `fixtures/domains/habitat/land_cover/layer_manifest/` when possible.

Fixture requirements:

- synthetic and public-safe;
- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit layer identity, layer version, artifact refs, artifact digests, payload family, source role, evidence refs, policy/review/release posture, freshness state, correction state, and rollback posture where material;
- no real source exports, real layer payloads, real public tiles, real sensitive occurrence records, rare-species/rare-plant locations, owner/land detail, or published artifacts.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Valid toy layer manifest | `fixtures/domains/habitat/land_cover/layer_manifest/` | accepted as layer-version metadata only. |
| Missing layer ID or version | same | validation failure / `ERROR`. |
| Missing artifact digest | same or invalid lane | validation failure / review required. |
| Evidence missing for displayed claim | same or invalid lane | `ABSTAIN`. |
| Descriptor treated as release approval | same or invalid lane | validation failure. |
| Tile/style treated as source truth | same or invalid lane | validation failure / `ABSTAIN`. |
| Missing correction/rollback posture | same or invalid lane | review required / promotion block. |
| Sensitive join exposed through layer metadata | same or invalid lane | `DENY` / `RESTRICT`. |

---

## Assertions

A useful land-cover layer-manifest test should make the carrier boundary obvious.

### Positive path

- layer identity and version are stable;
- artifact references and artifact digests are explicit;
- source-role badge, evidence posture, rights posture, and sensitivity posture are preserved;
- policy, review, release relationship, correction, supersession, and rollback references are linkable where material;
- freshness/stale state is visible;
- UI-facing examples point back to governed manifest/descriptor/evidence rather than becoming authority.

### Negative path

- missing layer ID, version, artifact refs, or artifact digest fails closed;
- registry record cannot become layer bytes;
- descriptor or manifest cannot approve release;
- tile, renderer style, popup, legend, graph edge, Focus Mode answer, or AI text cannot become source truth;
- missing EvidenceBundle support produces `ABSTAIN`;
- missing policy/review/release/correction/rollback posture blocks public carrier promotion;
- sensitive joins cannot leak through public layer metadata or fixture artifacts.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Valid synthetic layer manifest with identity, artifact digest, evidence, policy, review, release relationship, correction, and rollback context | accepted carrier support / downstream carrier allowed only if separately release-admitted. |
| Missing layer ID, version, or artifact ref | validation failure / `ERROR`. |
| Missing or mismatched artifact digest | validation failure / review required. |
| Displayed claim lacks EvidenceBundle support | `ABSTAIN`. |
| Descriptor/manifest/registry record treated as release approval | validation failure. |
| Tile/style/popup/AI answer treated as truth | `ABSTAIN` / validation failure. |
| Sensitive context would be exposed | `DENY` / `RESTRICT`. |
| Missing correction, supersession, or rollback posture for public-facing candidate | promotion-blocking failure. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real source exports, real source rasters, real lifecycle data, real layer payloads, or real public tiles;
- store real sensitive occurrence joins, rare-species/rare-plant locations, owner/land data, or exact protected-resource geometry;
- store public PMTiles, MVT, COG, GeoParquet, release artifacts, or generated public layers;
- redefine layer contracts, Habitat land-cover doctrine, schemas, source descriptors, fixtures, policy rules, receipts, proofs, layer registry authority, release decisions, renderer code, or production code;
- bypass `EvidenceRef -> EvidenceBundle` resolution;
- bypass artifact integrity, source-role, freshness, policy, sensitivity, correction, supersession, or rollback checks with a fixture flag;
- infer release state from file existence, layer name, registry presence, map rendering, tile availability, or AI wording;
- publish, promote, or release anything.

Any test that needs real layer bytes or public tile output belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/habitat/land_cover/layer_manifest/
├── README.md
├── test_layer_identity_required.py       # layer ID/version/object family/product family required
├── test_artifact_integrity.py            # artifact refs and digests required and stable
├── test_source_role_and_evidence.py      # source-role badges and EvidenceBundle support preserved
├── test_manifest_not_release.py          # descriptor/manifest/registry cannot approve release
├── test_renderer_not_truth.py            # tile/style/popup/AI cannot become source truth
└── test_correction_supersession_rollback.py # stale/corrected/superseded/rollback state required
```

Keep helpers local only when they are test-specific. Shared contracts, schemas, layer registries, source registries, policy behavior, evidence resolvers, fixtures, pipeline behavior, renderer behavior, or release behavior belong under their accepted responsibility roots.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/habitat/land_cover/layer_manifest
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing layer identity, missing artifact integrity, source-role collapse, unresolved evidence, missing policy, sensitive leakage, stale-state omission, registry/release collapse, renderer-as-truth, or missing correction/supersession/rollback posture;
- live-source or tile-generation checks: separate gated jobs only;
- release gate: land-cover layer-manifest failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/land_cover/layer_manifest/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; failures should block promotion. | Does not prove habitat/land_cover/layer_manifest modules or pass rate. |
| `fixtures/domains/habitat/land_cover/layer_manifest/README.md` | CONFIRMED | Fixture lane describes toy layer-version metadata, artifact pointers, source-role badges, evidence pointers, integrity checks, freshness state, release-facing checks, correction state, and rollback posture; fixtures are not source records, lifecycle data, EvidenceBundles, release state, public map material, public tiles, or published artifacts. | Does not prove payload inventory or consumer tests. |
| `contracts/data/layer_manifest.md` | CONFIRMED semantic contract / CONFLICTED schema home | `LayerManifest` is a governed manifest for a versioned layer payload and is not raw data, renderer implementation, proof closure, policy approval, or release approval. | Schema home is CONFLICTED / NEEDS VERIFICATION and validator path was not found in the contract session. |
| `contracts/domains/habitat/domain_layer_descriptor.md` | CONFIRMED semantic contract / PROPOSED implementation | Habitat layer descriptors describe public-safe layer support without turning tiles, render styles, popups, graph projections, or AI text into source truth; public descriptors must carry evidence, policy, sensitivity, correction, stale-state, and rollback context. | Paired schema is a scaffold and field-level enforcement remains NEEDS VERIFICATION. |
| `data/registry/layers/habitat/README.md` | CONFIRMED registry README / NEEDS VERIFICATION record shape | Habitat layer registry is for layer identity, meaning, constraints, sensitivity posture, and release-readiness pointers; it is not layer bytes, proof, policy, release authority, public API/UI material, or generated-answer authority. | Parent registry topology and concrete record shape remain NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for valid layer manifest, missing layer ID, missing version, missing artifact ref, missing artifact digest, mismatched digest, missing evidence for displayed claim, descriptor-as-release, tile/style-as-truth, sensitive-context exposure, stale state, supersession, correction, and rollback posture.
- [ ] LayerManifest schema home conflict is resolved or compatibility rule is accepted before enforcing schema-path-specific behavior.
- [ ] DomainLayerDescriptor schema path and field expectations are accepted beyond scaffold status.
- [ ] Layer registry record shape is accepted before enforcing registry assertions.
- [ ] SourceDescriptor/source-role behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] PolicyDecision and sensitivity behavior are available to tests or safely stubbed.
- [ ] ReleaseManifest, MapReleaseManifest, CorrectionNotice, SupersessionRecord, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat land-cover layer-manifest suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a source export store, layer payload store, lifecycle data store, fixture root, semantic-contract root, schema authority, layer-registry authority, policy authority, proof store, receipt store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
