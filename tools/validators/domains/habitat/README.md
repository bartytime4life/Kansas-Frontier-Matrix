<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-habitat-readme
title: tools/validators/domains/habitat README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-habitat-steward-plus-ecology-steward-plus-geoprivacy-reviewer-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; habitat; ecology; suitability; connectivity; geoprivacy; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Habitat validator index for habitat patches, classes, suitability, connectivity, corridors, restoration opportunity, stewardship zones, land-cover/ecoregion inputs, source-role separation, sensitive joins, geoprivacy, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Habitat meaning, policy decisions, proof records, and release authority to their owning roots
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
  - "This README replaces a greenfield stub. It does not confirm executable files."
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

> **One-line purpose.** `tools/validators/domains/habitat/` is the proposed per-domain Habitat validator index for habitat patches, classes, suitability, connectivity, corridors, restoration opportunity, stewardship zones, land-cover/ecoregion inputs, source-role separation, sensitive joins, geoprivacy, evidence, policy, release, correction, rollback, and public-surface denial checks.

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
| `tools/validators/domains/habitat/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad `tools/validators/habitat/README.md` | **NOT FOUND in this task** | This path currently serves as the inspected Habitat validator index. |
| Habitat domain doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/habitat/README.md` defines Habitat as landscape/suitability/connectivity lane, not species-record ownership, with source-role anti-collapse and lifecycle boundaries. |
| Over-precise geometry quarantine | **CONFIRMED in repo evidence / draft** | `data/quarantine/habitat/over_precise_geometry/README.md` defines fail-closed hold posture for Habitat geometry that is too precise for sensitivity, source-role, evidence, review, release, or public-surface posture. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child Habitat validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct Habitat validator specialty, fixture family, edge, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics.

Possible future children remain **PROPOSED** until verified:

- `land-cover/` for NLCD, remote-sensing land-cover, ecological-system, and classification-role checks;
- `ecoregions/` for ecoregion/habitat-class lineage, source vintage, and boundary provenance;
- `suitability/` for habitat suitability model outputs, model cards, uncertainty, and non-occurrence posture;
- `connectivity/` for corridors, graph/connectivity products, and public-safe generalization;
- `critical-habitat/` for regulatory critical-habitat context without legal-advice or species-occurrence collapse;
- `sensitive-join/` for Fauna, Flora, archaeology, stewardship, private-land, infrastructure, or other restricted joins;
- `over-precise-geometry/` for precision, redaction, aggregation, and quarantine-exit checks.

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
- **PROPOSED:** validator code may live below this folder when it checks declared Habitat invariants and delegates meaning, sensitivity, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, runtime behavior, and CI wiring.
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

Suggested future test surface:

```text
tests/validators/domains/habitat/
├── README.md
├── test_habitat_domain_validator_parent.py
└── fixtures/
    ├── valid_public_safe_habitat_derivative/
    ├── missing_evidence_ref/
    ├── source_role_collapse/
    ├── model_as_observation_denied/
    ├── habitat_species_authority_collapse/
    ├── over_precise_geometry_denied/
    ├── sensitive_join_denied/
    ├── public_safe_geometry_missing/
    ├── review_or_policy_gap/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/habitat
```

```bash
python tools/validators/domains/habitat/run_habitat_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_habitat_domain_validators.py` or the test path exists.

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
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub and current parent index for Habitat validators. |
| Next smallest safe change | Verify child validator scripts, accepted profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, geoprivacy behavior, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
