<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people-dna-land/land-ownership/readme
name: People DNA Land Land Ownership Raw README
path: data/raw/people-dna-land/land-ownership/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <land-records-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <privacy-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: people-dna-land
sublane: land-ownership
artifact_family: immutable-land-ownership-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; not-title-opinion; assessor-not-title; parcel-geometry-not-boundary-proof; private-person-parcel-joins-fail-closed; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/people-dna-land/land-ownership/README.md
  - ../../../quarantine/people-dna-land/README.md
  - ../../../processed/people-dna-land/README.md
  - ../../../catalog/domain/people-dna-land/README.md
  - ../../../published/layers/people-dna-land/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../../../docs/domains/people-dna-land/sublanes/land_ownership.md
  - ../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../../docs/domains/people-dna-land/SOURCE_LEDGER.md
  - ../../../../contracts/domains/people-dna-land/LandInstrument.md
  - ../../../../contracts/domains/people-dna-land/land-ownership/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - people-dna-land
  - land-ownership
  - land-instrument
  - chain-of-title
  - ownership-interval
  - deed
  - patent
  - probate
  - assessor
  - tax-record
  - parcel-version
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/people-dna-land/land-ownership/README.md`."
  - "Parent `data/raw/people-dna-land/README.md` is currently a greenfield stub."
  - "KFM land ownership records are evidence-bound source captures and assertions, not title opinions or legal abstracts."
  - "Assessor/tax records are administrative and never satisfy title claims; parcel geometry is not title-boundary proof."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, title-review workflows, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land — Land Ownership RAW Lane

RAW source-family lane for immutable land-ownership source captures and source-admission sidecars in the People/DNA/Land domain candidate.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-6f42c1">
  <img alt="Sublane: land ownership" src="https://img.shields.io/badge/sublane-land%20ownership-8a2be2">
  <img alt="Boundary: not title opinion" src="https://img.shields.io/badge/boundary-not%20title%20opinion-critical">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Land source posture](#land-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/people-dna-land/land-ownership/` is a RAW source-capture lane. It is not a title opinion, legal abstract, processed truth, catalog truth, proof, receipt authority, policy authority, release authority, public UI/API material, person-parcel truth, parcel-boundary proof, or generated-answer authority.

---

## Scope

This directory is for immutable land-ownership source captures and RAW-local sidecars in the People/DNA/Land domain candidate.

KFM records land evidence and ownership assertions from sources such as patents, deeds, mortgages, liens, easements, leases, mineral/water/access instruments, probate records, assessor/tax records, parcel versions, legal descriptions, and chain-of-title working references. It does not certify marketable title, issue title opinions, adjudicate legal boundaries, or treat administrative/tax records as title.

RAW records what was captured, where it came from, what source role it carried, and which recording authority, book/page or instrument number, legal description, parcel version, party names, dates, rights notes, citations, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/people-dna-land/land-ownership/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain candidate | `people-dna-land` |
| Sublane | `land-ownership` |
| Lane role | RAW source-capture lane for land instruments, administrative land records, parcel-version references, and ownership-assertion source support |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Explicitly admitted land-record source material only |
| Downstream | `data/work/people-dna-land/` or `data/quarantine/people-dna-land/land-ownership/` after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, legal-description support, recording authority, parcel-version lineage, person-join sensitivity, citation, validation, review state, correction, rollback, or release support is insufficient |

---

## Land source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| Land patent / deed / probate / mortgage / lien / easement / lease | Capture as recorded instrument source material when admitted. | The record evidences its own recording and contents; downstream ownership claims remain assertions requiring review. |
| Assessor / tax roll | Capture as administrative source material when admitted. | Administrative tax records are not title truth and do not prove conveyance. |
| Parcel geometry / parcel version | Capture as spatial or administrative context when admitted. | Parcel geometry is not title-boundary proof and must cite Spatial Foundation or parcel-version lineage where applicable. |
| Legal description | Preserve original text and normalized form where present. | Normalization does not replace the original recorded description. |
| Ownership interval candidate | Hold as candidate or work support until backed by instruments and review. | Candidate chains do not become public ownership edges without governed promotion. |
| Person-parcel join | Treat as sensitive until reviewed and released. | Private person-parcel joins fail closed when consent, living-person, rights, source role, or release state is unresolved. |
| Public derivative proposal | Hold until proof, review, policy, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- scanned-instrument references, record-book references, recorder index references, patent references, probate references, assessor/tax references, parcel-version references, legal-description references, or raw payload references;
- recording authority, book/page or instrument number, instrument type, party names as recorded, legal description, parcel-version reference, recording date, effective date where present, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, page counts, geometry counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, title opinion, parcel-boundary proof, person-join authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| People/DNA/Land land-ownership doctrine | `docs/domains/people-dna-land/LAND_OWNERSHIP.md` |
| Source-family doctrine | `docs/domains/people-dna-land/SOURCE_REGISTRY.md` and source catalog docs |
| Contract definitions | `contracts/domains/people-dna-land/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, sensitivity, person-join, title-review, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/people-dna-land/land-ownership/` |
| Normalized working material | `data/work/people-dna-land/` after governed triage |
| Validated People/DNA/Land objects | `data/processed/people-dna-land/` only after gates close |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, reports, stories, API payloads, downloads, PMTiles, graph edges, vector indexes, or generated answers | `data/published/` only after release gates close |
| Title opinion, legal abstract, marketable-title determination, parcel-boundary proof, private person-parcel truth, public artifact authority, or generated-answer truth | Owning governed downstream/proof/policy/release lanes, never this RAW directory alone |
| Schemas, validators, app/API/UI code | `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/people-dna-land/land-ownership/
├── README.md
├── instruments/
│   └── <source_or_run_id>/
│       ├── source_reference.json
│       ├── instrument_ref.json
│       ├── legal_description_ref.json
│       ├── checksums.sha256
│       └── README.md
├── assessor-tax/
│   └── <source_or_run_id>/
│       ├── source_reference.json
│       ├── administrative_record_ref.json
│       ├── cycle_ref.json
│       ├── checksums.sha256
│       └── README.md
├── parcel-version-context/
│   └── <source_or_run_id>/
│       ├── source_reference.json
│       ├── parcel_version_ref.json
│       ├── geometry_lineage_ref.json
│       ├── checksums.sha256
│       └── README.md
├── ownership-assertion-candidates/
│   └── <source_or_run_id>/
│       ├── source_reference.json
│       ├── assertion_candidate_ref.json
│       ├── evidence_gap_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, recording authority, legal-description support, parcel-version lineage, person-join sensitivity, citation, schema, or review state is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, citation, hash, recording metadata, legal-description support, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, review state, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/people-dna-land/land-ownership/
→ data/processed/people-dna-land/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the People/DNA/Land land-ownership lane.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, rights, recording authority, citation, retrieval time, and hash posture.
- [ ] Confirm assessor/tax material is not treated as title truth or conveyance evidence.
- [ ] Confirm parcel geometry is not treated as title-boundary proof.
- [ ] Confirm instrument identity, legal-description text, book/page or instrument number, parties, and recording authority are preserved where present.
- [ ] Confirm candidate owner matches and chain summaries remain candidate/work support until reviewed.
- [ ] Confirm private person-parcel joins are not released without sensitivity review, evidence support, correction path, rollback target, and release state.
- [ ] Confirm rights, redaction obligations, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW land-ownership material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/people-dna-land/land-ownership/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/people-dna-land/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Land-ownership doctrine says KFM records and reasons about ownership evidence but is not a title opinion or title-search substitute. | **CONFIRMED by GitHub contents API during this edit** |
| Land-ownership doctrine says assessor/tax records are administrative and never satisfy title claims; parcel geometry is not a title boundary. | **CONFIRMED by GitHub contents API during this edit** |
| Land source-role doctrine preserves observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles through promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Actual land-ownership RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, title-review workflows, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, title opinion, parcel-boundary proof, public artifact authority, person-parcel truth, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/people-dna-land/land-ownership/README.md`](../../../quarantine/people-dna-land/land-ownership/README.md)
- [`../../../quarantine/people-dna-land/README.md`](../../../quarantine/people-dna-land/README.md)
- [`../../../processed/people-dna-land/README.md`](../../../processed/people-dna-land/README.md)
- [`../../../catalog/domain/people-dna-land/README.md`](../../../catalog/domain/people-dna-land/README.md)
- [`../../../published/layers/people-dna-land/README.md`](../../../published/layers/people-dna-land/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)
- [`../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md`](../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md)
- [`../../../../docs/domains/people-dna-land/sublanes/land_ownership.md`](../../../../docs/domains/people-dna-land/sublanes/land_ownership.md)
- [`../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md`](../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/people-dna-land/SOURCE_LEDGER.md`](../../../../docs/domains/people-dna-land/SOURCE_LEDGER.md)
- [`../../../../contracts/domains/people-dna-land/LandInstrument.md`](../../../../contracts/domains/people-dna-land/LandInstrument.md)
- [`../../../../contracts/domains/people-dna-land/land-ownership/README.md`](../../../../contracts/domains/people-dna-land/land-ownership/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a People/DNA/Land land-ownership RAW source-capture lane only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, title opinion, legal abstract, parcel-boundary proof, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
