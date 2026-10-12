<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/hazards/sources/readme
name: Hazards Source Registry README
path: data/registry/hazards/sources/README.md
type: data-registry-hazards-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <hazards-domain-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: hazards-source-descriptor-records
domain: hazards
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-hazards; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; not-an-alert-system; freshness-bound; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/hazards/
  - ../../datasets/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/hazards/README.md
  - ../../../work/hazards/
  - ../../../quarantine/hazards/
  - ../../../processed/hazards/
  - ../../../catalog/domain/hazards/
  - ../../../receipts/
  - ../../../proofs/
  - ../../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hazards/SOURCES.md
  - ../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../../docs/domains/hazards/CONTINUITY_INVENTORY.md
  - ../../../../contracts/domains/hazards/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/hazards/
  - ../../../../policy/domains/hazards/
  - ../../../../policy/sensitivity/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - hazards
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - freshness
  - operational-context
  - regulatory-context
  - remote-sensing
  - modeled-hazard
  - administrative
  - not-an-alert-system
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README expands the thin README at `data/registry/hazards/sources/README.md`."
  - "Hazards source registry records are admission and authority-control records. They do not store source payloads, prove hazard claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The inspected Hazards source-registry doctrine names `data/registry/sources/hazards/` as the machine-readable registry lane. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled."
  - "Hazards is not an alert system. Time-bound source context may be admitted only with source time, retrieval time, freshness posture, and release blockers preserved."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Source Registry

Domain-first registry lane for Hazards source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: not an alert system" src="https://img.shields.io/badge/boundary-not%20an%20alert%20system-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Hazards source boundary](#hazards-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/hazards/sources/` is a source-registry lane for Hazards admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, current operational guidance, or generated-answer authority.

---

## Scope

This directory documents and may hold Hazards source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, supersession references, and registry-local indexes for sources that may feed the Hazards lane.

Hazards source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, and terms posture;
- sensitivity, public-boundary, and release-boundary posture;
- cadence, source head, retrieval window, source time, retrieval time, freshness posture, source vintage, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required redaction, quarantine, validation, proof, catalog, release, correction, stale-state, and rollback requirements.

They do **not** record hazard truth. A source descriptor can authorize or deny admission conditions, but every Hazards claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/hazards/sources/
```

This is a domain-first registry path. Current Hazards source-registry doctrine names the subtype-first pattern as the machine-readable source registry home:

```text
data/registry/sources/hazards/
```

Because both patterns are visible in repo evidence, this README preserves the requested path while marking final topology as **NEEDS VERIFICATION**. Until registry layout is reconciled by accepted directory or ADR guidance, do not silently duplicate source descriptor instances across both lanes. Prefer one canonical descriptor record with compatibility pointers, migration notes, and rollback history.

The domain-first parent exists but is currently a stub:

```text
data/registry/hazards/README.md
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Hazards source descriptor/admission records | `data/registry/hazards/sources/` and/or `data/registry/sources/hazards/` after topology reconciliation | Source identity, role, rights, terms, cadence, freshness, activation, supersession, and authority limits. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Human-facing Hazards source orientation | `docs/domains/hazards/SOURCE_REGISTRY.md`, `SOURCES.md`, `SOURCE_ROLE_MATRIX.md`, `CONTINUITY_INVENTORY.md` | Explains source families, admission posture, source-role discipline, knowledge-character labels, and boundaries; not machine descriptor storage. |
| Hazards source payloads | `data/raw/hazards/`, `data/work/hazards/`, `data/quarantine/hazards/`, `data/processed/hazards/` | Actual data belongs in lifecycle lanes, not registry records. |
| Hazards domain/dataset/crosswalk registry records | `data/registry/domains/`, `data/registry/datasets/`, `data/registry/crosswalks/` | Adjacent registry state; not source descriptor authority. |
| Hazards semantic meaning | `contracts/domains/hazards/` | Object-family meaning and invariants. |
| Hazards machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/hazards/`, or ADR-selected schema lane | Schema enforcement; path form remains NEEDS VERIFICATION until ADR/repo evidence resolves it. |
| Hazards policy and sensitivity | `policy/domains/hazards/`, `policy/sensitivity/`, `policy/rights/` | Exposure, rights, source-role, sensitivity, freshness, and admissibility rules. |
| Hazards validation receipts | `data/receipts/validation/hazards/` if/when accepted | Process memory for validation checks. |
| Hazards proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Hazards catalog projections | `data/catalog/domain/hazards/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Hazards release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Hazards source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Not an alert system | Hazards registry state must not become public operational guidance or alert authority. |
| Source role is fixed at admission | The canonical role must not be upgraded by processing, aggregation, cataloging, release review, map rendering, or generated explanation. |
| Time-bound context expires | Time-bound context must carry source time, retrieval time, freshness posture, stale-state handling, and public-use blockers. |
| Regulatory is not observed | Regulatory flood, fire, seismic, disaster, or planning context must not be reframed as observed event truth. |
| Detection is not confirmation | Remote-sensing detections, reports, and candidates require disposition and evidence review before being treated as confirmed event claims. |
| Administrative is not event truth | Declarations, rosters, programs, and accounting records are administrative context unless independently supported. |
| Models are not observations | Forecast, risk, exposure, scenario, susceptibility, or modeled hazard surfaces require model identity, run receipts, uncertainty, and source-role preservation. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to Hazards source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, sensitivity, cadence, steward, endpoint, access, attribution, redistribution, freshness, and authority-scope metadata;
- source time, retrieval time, freshness posture, product vintage, model version, event/candidate status, and source-head metadata summaries;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed large payloads, time-bound public guidance, proof packs, policy decisions, catalog records, release manifests, source-native dumps, or hazard claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Hazards source payloads, regulatory flood packages, remote-sensing detection packages, administrative extracts, time-bound feed captures, modeled risk surfaces, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/hazards/`, `data/work/hazards/`, `data/quarantine/hazards/`, or `data/processed/hazards/` depending on lifecycle state |
| Current public guidance, official-source substitution, sensitive infrastructure exposure, private identifiers, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/hazards/`, `docs/sources/`, or source catalog docs |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/hazards/` |
| JSON Schema | `schemas/contracts/v1/source/`, `schemas/contracts/v1/hazards/`, or ADR-selected schema lane |
| Policy rules, sensitivity rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Hazards layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/hazards/sources/
├── README.md
├── fema/
│   ├── README.md
│   └── index.local.json
├── noaa_nws/
│   ├── README.md
│   └── index.local.json
├── usgs/
│   ├── README.md
│   └── index.local.json
├── firms/
│   ├── README.md
│   └── index.local.json
├── nfhl/
│   ├── README.md
│   └── index.local.json
├── modeled_risk/
│   ├── README.md
│   └── index.local.json
├── administrative_context/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/hazards/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain two divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A Hazards source registry record should be structured enough for audit, admission, validation, correction, stale-state handling, and rollback.

```json
{
  "id": "kfm-source:hazards:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "hazards",
  "source_family": "regulatory_context | time_bound_context | remote_sensing | modeled_risk | administrative | event_candidate | historical_observation | context_layer | other",
  "source_name": "Human-readable source name",
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "knowledge_character": "historical | regulatory | modeled | time_bound_context | administrative | candidate | other",
  "authority_scope": "What this source may and may not support",
  "rights_posture": "open | attribution-required | restricted | stewarded | unknown | denied",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "freshness_posture": "static | source-vintage | time-bound | expires | unknown",
  "cadence": "one-time | periodic | event-driven | unknown",
  "source_head_refs": [],
  "retrieval_refs": [],
  "activation_refs": [],
  "intake_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "stale_state_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm whether `data/registry/hazards/sources/` or `data/registry/sources/hazards/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, source time, retrieval time, freshness posture, stale-state behavior, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
- [ ] Confirm regulatory context, time-bound context, remote-sensing detection, modeled risk, administrative action, historical observation, and candidate material are not collapsed.
- [ ] Confirm Hazards is not presented as an alerting or current-guidance surface.
- [ ] Confirm sensitive infrastructure, private, restricted, or operationally risky details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or time-bound Hazards source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/hazards/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/hazards/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Hazards source-registry doctrine names `data/registry/sources/hazards/` as the machine-readable registry lane. | CONFIRMED by GitHub contents API during this edit |
| Hazards continuity inventory states Hazards is not an alert system and frames Hazards as historical, regulatory, modeled, and time-bound context information. | CONFIRMED by GitHub contents API during this edit |
| Hazards RAW README keeps RAW source capture separate from registry, proof, receipt, policy, release, public, and alert authority. | CONFIRMED by GitHub contents API during this edit |
| Concrete Hazards source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between `data/registry/hazards/sources/` and `data/registry/sources/hazards/` is resolved. | NEEDS VERIFICATION |
| A canonical Hazards source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates Hazards source registry records. | UNKNOWN |
| This README grants public access to Hazards source registry internals. | DENY |

---

## Maintainer note

Hazards source registry records are useful because they make source identity, source role, rights, sensitivity, freshness, activation, correction, stale-state, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, release decisions, or current-guidance authority. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> RAW admission -> lifecycle processing -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public Hazards truth
```
