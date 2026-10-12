<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people-dna-land/land-ownership/readme
title: People DNA Land Land Ownership Raw README
path: data/raw/people-dna-land/land-ownership/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <land-records-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <privacy-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked People/DNA/Land land-ownership RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: people-dna-land
sublane: land-ownership
artifact_family: people-dna-land-land-ownership-raw-compatibility-reference
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
  - compatibility-reference
  - source-first
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/people-dna-land/land-ownership/README.md`."
  - "At the v0.1.0 edit, parent `data/raw/people-dna-land/README.md` was a greenfield stub; it now carries a People/DNA/Land compatibility/reference index."
  - "KFM land ownership records are evidence-bound source captures (held at one source-first RAW home, not this lane) and assertions, not title opinions or legal abstracts."
  - "Assessor/tax records are administrative and never satisfy title claims; parcel geometry is not title-boundary proof."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, title-review workflows, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People/DNA/Land — Land Ownership RAW Lane

Compatibility and reference lane for legacy land-ownership-facing RAW documentation in the People/DNA/Land domain candidate; not a physical source-capture home.

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
> `data/raw/people-dna-land/land-ownership/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this subtree is not a default physical capture home and must not receive duplicate RAW payloads. It is not a title opinion, legal abstract, processed truth, catalog truth, proof, receipt authority, policy authority, release authority, public UI/API material, person-parcel truth, parcel-boundary proof, or generated-answer authority.

---

## Scope

This directory documents land-ownership source handling and legacy domain-scoped RAW topology in the People/DNA/Land domain candidate. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM records land evidence and ownership assertions from sources such as patents, deeds, mortgages, liens, easements, leases, mineral/water/access instruments, probate records, assessor/tax records, parcel versions, legal descriptions, and chain-of-title working references. It does not certify marketable title, issue title opinions, adjudicate legal boundaries, or treat administrative/tax records as title.

A governed source-first capture records what was captured, where it came from, what source role it carried, and which recording authority, book/page or instrument number, legal description, parcel version, party names, dates, rights notes, citations, checksums, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/people-dna-land/land-ownership/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain candidate | `people-dna-land` |
| Sublane | `land-ownership` |
| Lane role | Compatibility/reference lane for land-instrument, administrative land-record, parcel-version, and ownership-assertion source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed People/DNA/Land WORK (`data/work/people-dna-land/`) or QUARANTINE (`data/quarantine/people-dna-land/land-ownership/`) procedures consume references or approved handoffs, not assumed domain-local copies, after governed triage |
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
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity. | Domain references may support land-ownership work without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/people-dna-land/land-ownership/` as the capture home. | Use only an accepted writer/path contract; none is established by this README. |
| Land patent / deed / probate / mortgage / lien / easement / lease | Capture as recorded instrument source material when admitted. | The record evidences its own recording and contents; downstream ownership claims remain assertions requiring review. |
| Assessor / tax roll | Capture as administrative source material when admitted. | Administrative tax records are not title truth and do not prove conveyance. |
| Parcel geometry / parcel version | Capture as spatial or administrative context when admitted. | Parcel geometry is not title-boundary proof and must cite Spatial Foundation or parcel-version lineage where applicable. |
| Legal description | Preserve original text and normalized form where present. | Normalization does not replace the original recorded description. |
| Ownership interval candidate | Hold as candidate or work support until backed by instruments and review. | Candidate chains do not become public ownership edges without governed promotion. |
| Person-parcel join | Treat as sensitive until reviewed and released. | Private person-parcel joins fail closed when consent, living-person, rights, source role, or release state is unresolved. |
| Public derivative proposal | Hold until proof, review, policy, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content in this subtree is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, title-review, and policy authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads.

The governed source-first capture or reference (never a duplicate in this subtree) must carry:

- source-reference manifests;
- scanned-instrument references, record-book references, recorder index references, patent references, probate references, assessor/tax references, parcel-version references, legal-description references, or raw payload references;
- recording authority, book/page or instrument number, instrument type, party names as recorded, legal description, parcel-version reference, recording date, effective date where present, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, page counts, geometry counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, title opinion, parcel-boundary proof, person-join authority, or answer authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support land ownership. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

The earlier sketch of `instruments/`, `assessor-tax/`, `parcel-version-context/`, and `ownership-assertion-candidates/` folders, each holding `<source_or_run_id>/` runs with `source_reference.json`, a family-specific reference (`instrument_ref.json` + `legal_description_ref.json`; `administrative_record_ref.json` + `cycle_ref.json`; `parcel_version_ref.json` + `geometry_lineage_ref.json`; `assertion_candidate_ref.json` + `evidence_gap_ref.json`), `checksums.sha256`, and `README.md`, is a proposed shape for a future accepted source-first home, not this subtree. An optional RAW-local index there would be RAW-local only. It would not be a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, recording authority, legal-description support, parcel-version lineage, person-join sensitivity, citation, schema, physical placement, or review state is unresolved. |
| Move to work | A governed reference or approved handoff may enter People/DNA/Land WORK only when SourceDescriptor, rights posture, source role, citation, hash, recording metadata, legal-description support, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence, review state, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/people-dna-land/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second land-ownership-scoped copy.
- [ ] Treat this README as compatibility/reference documentation only; do not create a child directory as a payload destination.
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
| Parent `data/raw/people-dna-land/README.md` was a greenfield stub at the v0.1.0 edit. | **CONFIRMED by GitHub contents API during the v0.1.0 edit; superseded — the parent now carries a People/DNA/Land compatibility/reference index** |
| Land-ownership doctrine says KFM records and reasons about ownership evidence but is not a title opinion or title-search substitute. | **CONFIRMED by GitHub contents API during this edit** |
| Land-ownership doctrine says assessor/tax records are administrative and never satisfy title claims; parcel geometry is not a title boundary. | **CONFIRMED by GitHub contents API during this edit** |
| Land source-role doctrine preserves observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles through promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Actual land-ownership RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction** — no payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
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

KFM rule: this directory is a People/DNA/Land land-ownership-facing compatibility/reference lane. One governed source-first capture may support land-ownership work without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, title opinion, legal abstract, parcel-boundary proof, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
