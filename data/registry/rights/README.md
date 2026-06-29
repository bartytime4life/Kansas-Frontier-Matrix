<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/rights/readme
name: Rights Registry README
path: data/registry/rights/README.md
type: data-registry-rights-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <rights-steward>
  - <policy-steward>
  - <domain-stewards>
  - <source-steward>
  - <sensitivity-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: rights-registry-records
path_posture: existing-parent-stub-replaced; subtype-first-rights-registry-parent-confirmed; flora-child-readme-confirmed; canonical-record-shape-needs-verification; concrete-records-unknown
sensitivity_posture: registry-internal; no-public-path; rights-unknown-fail-closed; rights-do-not-override-sensitivity; attribution-and-redistribution-preserved; source-role-preserving; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - flora/README.md
  - ../../raw/
  - ../../work/
  - ../../quarantine/
  - ../../processed/
  - ../../catalog/
  - ../../published/
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../../docs/domains/flora/SENSITIVITY.md
  - ../../../contracts/
  - ../../../schemas/contracts/v1/
  - ../../../policy/rights/
  - ../../../policy/domains/
  - ../../../policy/sensitivity/
  - ../../../policy/geoprivacy/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - rights
  - source-rights
  - dataset-rights
  - derivative-rights
  - license
  - attribution
  - redistribution
  - rights-holder
  - steward-obligation
  - terms-review
  - source-role
  - sensitivity
  - evidence
  - provenance
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/rights/README.md`."
  - "Rights registry records are registry/control records. They do not store source payloads, prove domain claims, define contracts, enforce schemas, hold policy, issue licenses, close catalogs, or publish artifacts."
  - "Confirmed child README lane during this sequence: flora. Concrete rights registry payloads, canonical schemas, validators, fixtures, CI, runtime rights resolution, and public API behavior remain UNKNOWN or NEEDS VERIFICATION."
  - "Rights state and sensitivity state are separate fail-closed gates. A rights registry record can block release, but it does not by itself authorize public exposure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Rights Registry

Parent registry lane for rights-review state, attribution obligations, redistribution posture, source-terms pointers, rights blockers, and release-readiness control records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: rights" src="https://img.shields.io/badge/lane-rights-blue">
  <img alt="Topology: subtype-first" src="https://img.shields.io/badge/topology-subtype--first-informational">
  <img alt="Boundary: not policy" src="https://img.shields.io/badge/boundary-not%20policy-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Rights registry boundary](#rights-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested registry shape](#suggested-registry-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/rights/` is a registry/control lane for reviewed rights posture and rights-readiness pointers. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, legal advice, license authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/rights/` is the subtype-first parent for rights registry records:

```text
data/registry/rights/<domain-or-scope>/
```

A rights registry record makes rights posture inspectable before source activation, downstream processing, catalog closure, export, public display, or release. It may point to source descriptors, dataset registry records, derivative records, layer registry records, terms-review evidence, policy outcomes, validation receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

This parent README exists to prevent rights state from collapsing into adjacent authorities. It should help maintainers distinguish:

- rights registry records from source descriptors and dataset records;
- rights registry records from contracts, schemas, policy, receipts, proofs, catalog records, release records, and published artifacts;
- reviewed rights posture from legal interpretation, source license authority, or permission to publish;
- release-readiness pointers from actual release decisions.

A rights registry record does **not** make a source usable, a derivative publishable, a claim true, a layer public, a catalog closed, or a license valid. It records a governed review state and points to the evidence/policy/release chain needed to act on that state.

---

## Path posture

The confirmed parent lane is:

```text
data/registry/rights/
```

This path uses a subtype-first pattern, matching the broader registry style used by other registry families:

```text
data/registry/sources/<domain>/
data/registry/datasets/<domain>/
data/registry/domains/<domain>/
data/registry/crosswalks/<domain-or-scope>/
data/registry/layers/<domain>/
data/registry/rights/<domain-or-scope>/
```

The parent existed as a greenfield stub before this edit. A Flora child README now exists, but the canonical rights-registry object schema, emitted records, validators, fixtures, CI checks, runtime rights resolver, governed API behavior, and release integration remain **NEEDS VERIFICATION** or **UNKNOWN** unless separately verified.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Rights registry parent | `data/registry/rights/` | Rights-state routing, rights-review pointers, rights blockers, and registry-local indexes. |
| Domain rights registry lanes | `data/registry/rights/<domain-or-scope>/` | Domain-specific rights review records and release-readiness pointers. |
| Source descriptors | `data/registry/sources/<domain>/` and reconciled source registry lanes | Source identity/admission; rights posture may be pinned there and referenced here. |
| Dataset registry records | `data/registry/datasets/<domain>/` | Dataset identity and dataset-state; not rights policy or release authority. |
| Domain registry records | `data/registry/domains/<domain>/` | Domain-state records; not rights review records. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, vocabularies, units, fields, classes, and domain lanes. |
| Layer registry records | `data/registry/layers/<domain>/` | Layer identity and release-readiness pointers; rights refs may be attached but not duplicated. |
| Source/lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/` | Actual source and processed data; not rights registry control records. |
| Catalog projections | `data/catalog/`, `data/triplets/` | Discovery, catalog closure, and graph/triplet projections. |
| Published artifacts | `data/published/` | Released public-safe artifacts and direct release sidecars. |
| Semantic contracts | `contracts/` | Object meaning and invariants; not registry storage. |
| Machine schemas | `schemas/contracts/v1/...` | Machine-checkable shape; rights-registry schema remains NEEDS VERIFICATION. |
| Policy and sensitivity | `policy/` | Rights, access, sensitivity, geoprivacy, redaction, public-safety, and release-policy decisions. |
| Receipts | `data/receipts/` | Validation, transform, redaction, aggregation, model, policy, review, and terms-review process memory. |
| Proofs | `data/proofs/` | EvidenceBundle/proof support and citation closure. |
| Release authority | `release/` | Promotion decisions, ReleaseManifests, correction notices, rollback cards, withdrawal, and supersession. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. |

---

## Confirmed child lanes

This confirms README/path evidence only. It does not prove live rights registry payloads, schema enforcement, validators, fixtures, CI, release integration, API behavior, UI behavior, or public-safe summaries.

| Child lane | Status | Rights registry posture |
|---|---:|---|
| [`flora/`](flora/README.md) | CONFIRMED README | Rights-unknown fails closed; attribution/redistribution/steward obligations are preserved; rights do not override Flora sensitivity gates. |

Future child lanes should follow the same boundary pattern and should not be added as proof of implementation maturity.

---

## Rights registry boundary

| Rule | Handling |
|---|---|
| Registry record is control state | It records or points to rights review posture; it does not grant a license or decide policy. |
| Rights are distinct from sensitivity | Passing rights does not relax sensitivity. Passing sensitivity does not clear rights. Both must close before public release. |
| Unknown terms fail closed | Unknown license, attribution, redistribution, endpoint terms, steward obligations, access terms, or rights-holder constraints block activation/release until reviewed. |
| SourceDescriptor remains upstream anchor | Source identity, source role, source terms, cadence, rights posture, and source head should remain anchored in source registry records. |
| Rights travel downstream | License, attribution, rights-holder, dataset identity, terms-review refs, and obligation refs must remain attached through derivatives and published artifacts. |
| No rights claim without evidence | A registry record should not assert a specific license, permission, rights holder, or redistribution allowance unless supported by source evidence and review state. |
| Restricted means denied by default | Restricted or steward-controlled source material should route to authorized/reviewed surfaces only; public exposure requires explicit release support. |
| Redaction does not erase rights | Generalization, aggregation, withholding, or redaction may reduce sensitivity exposure, but rights obligations and attribution still travel. |
| Registry is not legal advice | Legal interpretation and formal agreements remain outside this registry lane; this lane records reviewed posture and pointers. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog records and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |
| Unknown implementation stays unknown | A README path is not proof of emitted records, schemas, validators, tests, runtime behavior, or public availability. |

---

## Accepted material

Accepted content is limited to rights registry records and registry-local support files:

- parent README and domain/scope child README files;
- domain/scope child lane indexes and local manifests;
- rights review records for sources, datasets, derivatives, layers, catalog items, release candidates, and published artifacts;
- references to SourceDescriptor, DatasetRegistry, LayerRegistry, CatalogItem, ReleaseCandidate, and ReleaseManifest objects;
- license, rights-holder, attribution, redistribution, terms-of-use, endpoint terms, access, steward-obligation, embargo, expiration, and recheck references;
- rights status, reviewer refs, review dates, source-terms review refs, contradiction notes, withdrawal notes, and blocker notes;
- policy, sensitivity, geoprivacy, redaction, aggregation, access, caveat, freshness, and public-exposure posture references;
- validation, transform, model, aggregation, redaction, review, policy, and terms-review receipt references;
- EvidenceRef/EvidenceBundle/proof references;
- catalog, triplet, and graph projection references;
- release candidate, release manifest, promotion decision, correction notice, withdrawal, supersession, and rollback references;
- registry-local index files that point outward without becoming catalog, proof, policy, release, or artifact authority.

Keep records compact and pointer-based. Do not embed full source payloads, sensitive content, proof packs, policy decisions, catalog records, release manifests, or domain claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, processed domain objects, rasters, shapefiles, GeoParquet, COG, PMTiles, source-native tables, remote-sensing scenes, scans, or model outputs | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, or `data/published/` depending on lifecycle/release state |
| Source descriptor/admission records | `data/registry/sources/<domain>/` and reconciled source registry lanes |
| Dataset identity records | `data/registry/datasets/<domain>/` |
| Domain-state records | `data/registry/domains/<domain>/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Layer identity/release-readiness records | `data/registry/layers/<domain>/` |
| Semantic object contracts | `contracts/` |
| JSON Schema | `schemas/contracts/v1/...` |
| Rights policy, sensitivity policy, geoprivacy policy, access-control logic, redaction policy, or release rules | `policy/` |
| Validation, transform, model, aggregation, redaction, terms-review, policy, review, or run receipts | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Public UI code, MapLibre runtime code, APIs, pipelines, validators, fixtures, tests, or CI workflows | `apps/`, `packages/`, `tools/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Legal advice, full license texts as authority, private agreements, secrets, credentials, or access tokens | governed legal/rights-holder systems, restricted storage, or external source-of-record systems |
| Generated-answer carriers or AI summaries | governed response/output lanes after evidence, policy, review, and release checks |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance. Confirmed README child lanes are marked; other domains are examples until created and verified.

```text
data/registry/rights/
├── README.md
├── flora/                # CONFIRMED README
│   └── README.md
├── agriculture/          # PROPOSED
│   └── README.md
├── atmosphere/           # PROPOSED
│   └── README.md
├── fauna/                # PROPOSED
│   └── README.md
├── geology/              # PROPOSED
│   └── README.md
├── habitat/              # PROPOSED
│   └── README.md
├── hazards/              # PROPOSED
│   └── README.md
├── hydrology/            # PROPOSED
│   └── README.md
├── people-dna-land/      # PROPOSED; likely restricted-review
│   └── README.md
├── soil/                 # PROPOSED
│   └── README.md
└── index.local.json      # PROPOSED local index, not catalog/release/policy authority
```

Do not create or populate child registry payloads until rights subject, source descriptor refs, rights evidence refs, policy refs, review state, release refs, and rollback path are known.

---

## Suggested registry shape

The exact rights-registry schema remains **NEEDS VERIFICATION**. A rights registry record should be structured enough for audit, release readiness, correction, and rollback.

```json
{
  "id": "kfm-rights:<domain-or-scope>:<stable-rights-id>",
  "record_type": "rights_registry_record",
  "domain": "<domain-or-scope>",
  "rights_family": "source_terms | attribution | redistribution | steward_obligations | derivative_rights | release_readiness | embargo | withdrawal | other",
  "subject_ref": "source | dataset | derivative | layer | catalog_item | release_candidate | published_artifact",
  "source_registry_refs": [],
  "dataset_registry_refs": [],
  "layer_registry_refs": [],
  "catalog_refs": [],
  "release_refs": [],
  "rights_status": "allowed | attribution-required | restricted | unknown | denied | expired | conflicting | needs-review",
  "license_refs": [],
  "rights_holder_refs": [],
  "attribution_refs": [],
  "redistribution_refs": [],
  "terms_review_refs": [],
  "steward_obligation_refs": [],
  "policy_refs": [],
  "sensitivity_refs": [],
  "receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "review_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | permissioned | restricted | denied",
  "blockers": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, release workflows, governed API behavior, and UI behavior are verified.

---

## Required checks before use

- [ ] Confirm the record belongs in `data/registry/rights/<domain-or-scope>/`, not `data/registry/sources/`, `data/registry/datasets/`, `data/registry/domains/`, `data/registry/crosswalks/`, `data/registry/layers/`, `contracts/`, `schemas/`, `policy/`, `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/published/`, or `release/`.
- [ ] Confirm the subject of the rights review is identified: source, dataset, derivative, layer, catalog item, release candidate, published artifact, or other reviewed object.
- [ ] Confirm source descriptor, dataset registry, layer registry, catalog, policy, receipt, proof, and release refs are pointer-based and not duplicated.
- [ ] Confirm license, attribution, redistribution, rights-holder, source terms, endpoint terms, steward obligations, access posture, review date, and recheck date are recorded or explicitly blocked.
- [ ] Confirm rights evidence exists before asserting any specific license, rights holder, redistribution permission, or public-release eligibility.
- [ ] Confirm unknown, restricted, expired, conflicting, or missing rights state fails closed.
- [ ] Confirm rights state does not override sensitivity, privacy, geoprivacy, public-safety, sovereignty, living-person, rare-species, archaeology, infrastructure, evidence closure, catalog closure, or release state.
- [ ] Confirm rights obligations travel to derivatives, catalog records, published artifacts, exports, API payloads, reports, attribution panels, and correction notices.
- [ ] Confirm validation receipts, redaction receipts, aggregation receipts, transform receipts, model receipts, terms-review receipts, policy outcomes, and review records exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential rights use.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from rights state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for changed source terms, rights errors, attribution defects, expired permission, or release withdrawal.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth or permission.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/rights/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/rights/flora/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| Directory Rules state that file location encodes responsibility root, lifecycle phase, and governance posture, and that responsibility, not topic, determines root placement. | CONFIRMED by GitHub contents API during this edit |
| Flora rights registry README says rights records are control records, not policy, license authority, source payloads, proofs, catalog closure, release decisions, or public output. | CONFIRMED by GitHub contents API during this edit |
| Flora rights/sensitivity docs state rights and sensitivity are distinct fail-closed gates before public release. | CONFIRMED by GitHub contents API in this sequence |
| Concrete rights registry payloads exist under this parent lane. | UNKNOWN |
| A canonical rights-registry schema is enforced. | NEEDS VERIFICATION |
| CI validates rights registry records. | UNKNOWN |
| Runtime rights resolution or governed API behavior reads this registry lane. | UNKNOWN |
| This README grants public access to rights registry internals. | DENY |

---

## Maintainer note

Rights registry records are useful because they make source terms, rights-holder obligations, attribution, redistribution, steward obligations, release readiness, correction, and rollback inspectable before a source or derivative reaches public surfaces. They become dangerous when treated as policy, legal advice, source payloads, proof closure, catalog closure, release decisions, or permission.

Keep the safe chain explicit:

```text
rights registry record -> source/dataset/layer refs -> terms/evidence review -> policy/review outcome -> lifecycle payload -> validation/redaction/terms receipt -> proof/catalog -> release -> governed public surface
```

Never collapse it into:

```text
rights registry record -> public permission
```
