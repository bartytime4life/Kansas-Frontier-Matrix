<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-habitat-readme
title: tools/validators/domains/habitat README
type: README
version: v0.2
status: draft
owner: TODO-tooling-qa-owner-plus-habitat-steward-plus-ecology-steward-plus-geoprivacy-reviewer-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-08-28
policy_label: repository-facing; per-domain-validator-index; habitat; ecology; suitability; connectivity; geoprivacy; fail-closed; non-authoritative
owning_root: tools/
responsibility: per-domain Habitat validator index for habitat patches, classes, suitability, connectivity, corridors, restoration opportunity, stewardship zones, land-cover/ecoregion inputs, source-role separation, sensitive joins, geoprivacy, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Habitat meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../biodiversity/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/API_CONTRACTS.md
  - ../../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../../docs/domains/habitat/CANONICAL_PATHS.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/sublanes/ecoregions.md
  - ../../../../data/quarantine/habitat/over_precise_geometry/README.md
  - ../../../../data/registry/sources/habitat/README.md
  - ../../../../contracts/domains/habitat/
  - ../../../../schemas/contracts/v1/domains/habitat/
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "v0.2 reconciles this index with current repository executables, focused tests and fixtures, and CI wiring without changing validator behavior or maturity."
  - "No broad tools/validators/habitat/README.md was found during this task, so this path currently serves as the inspected per-domain Habitat validator index."
  - "Habitat owns landscape, patches, suitability, connectivity, restoration opportunity, and stewardship-zone products. It does not own Fauna occurrence truth, Flora taxon/specimen truth, Hydrology water truth, Soil substrate truth, or regulatory hazard truth."
  - "Habitat sensitivity is often join-induced. Outputs that reveal sensitive Fauna, Flora, archaeology, stewardship, private-land, infrastructure, or other restricted context must fail closed unless public-safe geoprivacy, review, policy, evidence, release, correction, and rollback support exists."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Habitat meaning, create EvidenceBundles, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/habitat

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-habitat--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-fail--closed-red)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/habitat/` is the per-domain Habitat validator index for habitat patches, classes, suitability, connectivity, corridors, restoration opportunity, stewardship zones, land-cover/ecoregion inputs, source-role separation, sensitive joins, geoprivacy, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/habitat/` exists to organize Habitat validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Habitat candidates preserve landscape identity, source-role posture, model/observation/regulatory separation, species-record non-ownership, sensitive-join geoprivacy, evidence closure, review state, policy decisions, release readiness, correction paths, rollback support, and public-surface denial boundaries before they reach any governed output?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create Habitat truth, species occurrence truth, rare-plant truth, critical-habitat legal truth, stewardship decisions, EvidenceBundles, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/habitat/README.md` | **CONFIRMED index / draft** | This file records current executable and placeholder posture without granting authority. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/habitat/README.md` | **ABSENT** | This path is the current per-domain Habitat validator index; no parallel broad Habitat validator home is established. |
| Habitat domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/habitat/README.md` defines Habitat as landscape/suitability/connectivity lane, not species-record ownership, with source-role anti-collapse and lifecycle boundaries. |
| Over-precise geometry quarantine | **CONFIRMED in repo evidence / draft** | `data/quarantine/habitat/over_precise_geometry/README.md` defines fail-closed hold posture for Habitat geometry that is too precise for sensitivity, source-role, evidence, review, release, or public-surface posture. |
| Subdirectories | **NONE** | Current validator implementations are direct children of this directory. |
| Substantive executables | **FOUR CONFIRMED** | Cover-class crosswalk, land-cover materiality, model-run receipt, and critical-habitat source-role validators are implemented with focused tests. |
| Placeholder executables | **SIX CONFIRMED** | Catalog matrix, EvidenceBundle, HabitatPatch, schema, source descriptor, and suitability-model files remain inert placeholders and must not be cited as enforcement. |
| Focused CI | **CONFIRMED / bounded** | Three focused workflows cover crosswalk, materiality, and model-run receipt; `domain-habitat` runs the materiality slice and explicit proof/release holds. Critical-habitat source-role tests have no dedicated focused workflow. |

[Back to top](#top)

---

## Executable inventory

Current main establishes four substantive direct-child validators:

| Validator | Bounded responsibility | Test / fixture evidence | Focused workflow |
|---|---|---|---|
| `validate_cover_class_crosswalk_profile.py` | Fixture-only ontology version, directionality, coverage, and lossiness checks. | `tests/domains/habitat/land_cover/crosswalk/test_cover_class_crosswalk_profile.py`; `fixtures/domains/habitat/land_cover/crosswalk/profile_cases.json` | `cover-class-crosswalk-profile.yml` |
| `validate_land_cover_materiality.py` | Deterministic material-change classification for the inactive land-cover profile. | `tests/validators/domains/habitat/test_land_cover_materiality.py`; `fixtures/domains/habitat/land_cover/materiality/` | `habitat-land-cover-materiality.yml`; also exercised by `domain-habitat.yml` |
| `validate_model_run_receipt.py` | Fixture-only model-run receipt shape, identity, temporal, digest, uncertainty, and authority-boundary checks. | `tests/validators/domains/habitat/test_validate_model_run_receipt.py`; `fixtures/contracts/v1/domains/habitat/model_run_receipt/` | `habitat-model-run-receipt.yml` |
| `validate_critical_habitat_source_role.py` | Synthetic source-role anti-collapse for regulatory critical habitat and modeled habitat, including species-presence denial. | `tests/domains/habitat/test_critical_habitat_source_role.py` | **No dedicated focused workflow**; local execution is confirmed. |

The following direct-child files remain placeholders: `validate_catalog_matrix.py`, `validate_evidence_bundle.py`, `validate_habitat_patch.py`, `validate_schema.py`, `validate_source_descriptor.py`, and `validate_suitability_model.py`. Their existence proves no validation behavior.

Habitat EvidenceBundle projection validation is implemented at the schema-declared top-level entry point `tools/validators/validate_habitat_evidence_bundle_projection.py`, with focused workflow `habitat-evidence-bundle-convergence.yml`. The inert same-named domain placeholder does not replace or mirror that authority.

No child directory is established below this index. Add one only when a distinct validator specialty has accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics; do not create a parallel authority home for an already-established direct-child or schema-declared entry point.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Habitat validator index | `tools/validators/domains/habitat/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain ecology/biodiversity validator context | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/` |
| Habitat domain meaning | `docs/domains/habitat/`, `contracts/domains/habitat/` |
| Habitat schemas | `schemas/contracts/v1/domains/habitat/` or ADR-selected homes |
| Habitat policy rules | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/habitat/` or accepted source registry home |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Lifecycle data and quarantine holds | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/`, `data/catalog/...`, `data/published/...` |
| Tests and fixtures | `tests/validators/domains/habitat/`, `tests/domains/habitat/`, `fixtures/domains/habitat/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **CONFIRMED:** the four substantive direct-child validators, their cited focused tests/fixtures, and the cited workflow files exist on the reviewed repository state.
- **BOUNDED:** passing fixtures prove only the declared validator behavior; they do not establish source truth, rights, sensitivity clearance, evidence closure, policy approval, human review, lifecycle promotion, release, deployment, or publication.
- **NEEDS VERIFICATION:** placeholder behavior, policy bundle execution, live source descriptors, production report destinations, operational receipts, runtime behavior, and any uncited CI coupling.
- **DENY:** using this folder as habitat doctrine, species-record authority, regulatory-designation authority, contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/habitat/` include:

- this parent/index README;
- child README lanes for narrow Habitat validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check source-role discipline, habitat object-family separation, land-cover/ecoregion lineage, suitability model posture, connectivity/corridor generalization, sensitive-join handling, public-safe geometry, evidence closure, review state, policy decisions, release references, correction cascade, and rollback support;
- validators that check cross-lane joins preserve Fauna, Flora, Hydrology, Soil, Agriculture, Hazards, Archaeology, Infrastructure, People/Land, and other neighboring-domain authority boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Habitat doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/habitat/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Habitat domain docs | `docs/domains/habitat/` |
| Habitat contracts | `contracts/domains/habitat/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and sensitivity rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, RedactionReceipts, AggregationReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, legal/regulatory advice, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Habitat validator posture

Habitat validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks EvidenceRef, EvidenceBundle, source descriptor, source-role, rights, time, model, lineage, or object-family support;
- collapses habitat patch, habitat class, suitability raster, corridor, connectivity graph, restoration opportunity, stewardship zone, land-cover class, ecological system, regulatory critical-habitat context, or species occurrence into another role;
- treats a modeled suitability surface as a Fauna or Flora occurrence;
- presents a regulatory critical-habitat layer as KFM legal advice or species-presence proof;
- exposes over-precise geometry or reverse-engineerable derivatives tied to sensitive Fauna, Flora, archaeology, stewardship, private-land, infrastructure, or other restricted context;
- lacks a named generalization/redaction/aggregation transform, RedactionReceipt, AggregationReceipt, ReviewRecord, PolicyDecision, ReleaseManifest, correction path, or rollback target where required;
- maps, tiles, exports, searches, embeds, graphs, summarizes, or answers with Habitat content beyond the approved public-safe derivative;
- imports another domain's truth into a Habitat artifact without preserving ownership, source role, sensitivity, and EvidenceBundle support;
- offers legal, regulatory, emergency, operational wildlife, conservation-compliance, or land-use guidance outside an accepted governed authority path;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `HABITAT_DOMAIN_VALIDATORS_PASS` | Configured Habitat validators passed. |
| `HABITAT_DOMAIN_VALIDATORS_FAIL` | One or more configured validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Habitat child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `SOURCE_ROLE_COLLAPSE` | Candidate collapses source-role or object-family posture. |
| `HABITAT_SPECIES_AUTHORITY_COLLAPSE` | Candidate treats Habitat output as Fauna/Flora occurrence or species truth. |
| `MODEL_AS_OBSERVATION_DENIED` | Suitability/model output is presented as observed habitat or species fact. |
| `OVER_PRECISE_GEOMETRY_DENIED` | Geometry is too precise for the sensitivity, evidence, or public tier. |
| `SENSITIVE_JOIN_DENIED` | Habitat join reveals or infers restricted neighboring-domain context. |
| `PUBLIC_SAFE_GEOMETRY_MISSING` | Required generalized/redacted/aggregated geometry or profile is absent. |
| `REDACTION_OR_AGGREGATION_RECEIPT_MISSING` | Required transform receipt is absent. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Habitat without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Repository-confirmed focused commands:

```bash
python -m pytest -q tests/validators/domains/habitat/test_land_cover_materiality.py
python tools/validators/domains/habitat/validate_land_cover_materiality.py --fixtures
```

```bash
python -m pytest -q tests/validators/domains/habitat/test_validate_model_run_receipt.py
python tools/validators/domains/habitat/validate_model_run_receipt.py --fixtures
```

```bash
python -m unittest -v tests.domains.habitat.land_cover.crosswalk.test_cover_class_crosswalk_profile
python tools/validators/domains/habitat/validate_cover_class_crosswalk_profile.py --fixtures
```

```bash
python -m unittest -v tests.domains.habitat.test_critical_habitat_source_role
```

There is no confirmed `run_habitat_domain_validators.py` aggregate entry point. Do not substitute broad test discovery for the focused commands above without first classifying unrelated or placeholder lanes.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validator reads declared Habitat contracts, schemas, and policy rather than defining meaning locally.
- [ ] Habitat object families remain distinct from Fauna occurrence truth and Flora plant-record truth.
- [ ] Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain distinct.
- [ ] Suitability, connectivity, corridor, restoration, and stewardship products do not overclaim source role or legal authority.
- [ ] Sensitive joins and over-precise geometry fail closed unless approved public-safe transform support exists.
- [ ] EvidenceBundle, public-safe geometry, review, policy, release, rollback, and correction support are checked where required.
- [ ] Cross-domain joins preserve ownership, source role, sensitivity, and EvidenceBundle support.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces do not reveal restricted details or reverse-engineerable derivatives.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-28 against `main@bacb77cfbc04014a2c05da541f9cba8025629068` |
| Review state | Draft index reconciled to current executable, placeholder, test/fixture, and workflow evidence. |
| Next smallest safe change | Add dedicated hosted coverage for the critical-habitat source-role guard or implement one currently inert placeholder only with an accepted contract/schema boundary, synthetic negative fixtures, and a complete focused test/workflow seam. |
