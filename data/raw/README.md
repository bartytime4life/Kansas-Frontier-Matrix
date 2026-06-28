<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/readme
name: Data Raw Root README
path: data/raw/README.md
type: data-raw-root-readme
version: v0.1.0
status: draft
owners:
  - <data-steward>
  - <source-steward>
  - <domain-stewards>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
artifact_family: immutable-source-capture-root-index
sensitivity_posture: raw-internal; no-public-path; source-role-preserving; rights-needs-verification; release-blocked
related:
  - ../README.md
  - agriculture/README.md
  - archaeology/README.md
  - atmosphere/README.md
  - fauna/README.md
  - flora/README.md
  - geology/README.md
  - habitat/README.md
  - hazards/README.md
  - hydrology/README.md
  - people/README.md
  - people-dna-land/README.md
  - roads-rail-trade/README.md
  - settlement/README.md
  - settlements-infrastructure/README.md
  - soil/README.md
  - usda-nass/README.md
  - ../quarantine/README.md
  - ../processed/README.md
  - ../catalog/README.md
  - ../published/README.md
  - ../registry/sources/README.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/architecture/source-roles.md
  - ../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - source-capture
  - source-role
  - lifecycle
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/README.md`."
  - "Directory Rules state that placement encodes ownership, governance, and lifecycle; topic alone does not justify a root folder."
  - "This root is a lifecycle root for RAW source capture only; it is not proof, catalog, registry, policy, release, public artifact, or generated-answer authority."
  - "README/path presence confirms documentation or path evidence only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Data RAW

Lifecycle root for immutable KFM source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Root contract](#root-contract) · [Confirmed RAW lanes](#confirmed-raw-lanes) · [RAW handling rules](#raw-handling-rules) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/` is a no-public-path lifecycle root. It is not processed truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, graph/vector-index authority, or generated-answer authority.

---

## Scope

`data/raw/` holds immutable source captures, source references, source-head snapshots, source-admission sidecars, checksums, and RAW-local indexes before any governed normalization or publication decision.

RAW exists for preservation, replay, and audit. It records what was captured, where it came from, what source role it carried, which source family and domain lane own it, and what rights, sensitivity, version, time, citation, hash, and review caveats must travel downstream.

RAW does **not** decide what a source means, whether a claim is true, whether rights permit reuse, whether sensitivity is resolved, whether a source can publish, whether a model or aggregate may answer a question, or whether a public artifact may be generated.

---

## Root contract

| Field | Value |
|---|---|
| Path | `data/raw/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Root role | Parent lifecycle root for source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Explicitly admitted connector/source-admission output only |
| Downstream | `data/work/<domain>/` or `data/quarantine/<domain>/` after governed triage |
| Release authority | `release/`, not this root |
| Proof authority | `data/proofs/`, not this root |
| Receipt authority | `data/receipts/`, not this root |
| Registry authority | `data/registry/`, not this root |
| Policy authority | `policy/`, not this root |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, sensitivity, path authority, source family, product identity, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed RAW lanes

The lanes below are confirmed by current-session GitHub fetches, search results, or recent file edits. This table confirms README/path evidence only; it does **not** prove payloads, SourceDescriptors, connectors, validators, receipts, fixtures, review controls, CI checks, or release readiness.

| Lane | Status | Boundary |
|---|---|---|
| [`agriculture/`](agriculture/README.md) | **CONFIRMED README** | Agriculture source capture; includes canonical `usda-nass/` child lane. |
| [`archaeology/`](archaeology/README.md) | **CONFIRMED README** | Archaeology/cultural-heritage source capture; no public RAW path. |
| [`atmosphere/`](atmosphere/README.md) | **CONFIRMED README** | Atmosphere source capture; observed, modeled, aggregate, and administrative roles stay distinct. |
| [`fauna/`](fauna/README.md) | **CONFIRMED README** | Fauna source capture; exact occurrence and sensitivity posture require governed handling. |
| [`flora/`](flora/README.md) | **CONFIRMED PATH / EMPTY OR PLACEHOLDER** | Flora RAW path exists but still needs a substantive README before it can serve as a documented parent lane. |
| [`geology/`](geology/README.md) | **CONFIRMED README** | Geology/natural-resources source capture; exact subsurface and rights-sensitive details stay gated. |
| [`habitat/`](habitat/README.md) | **CONFIRMED README** | Habitat source capture; class crosswalks, regulatory layers, and models are not interchangeable. |
| [`hazards/`](hazards/README.md) | **CONFIRMED README** | Hazards source capture; not a live alert, emergency guidance, or public warning surface. |
| [`hydrology/`](hydrology/README.md) | **CONFIRMED README** | Hydrology source capture with confirmed child lanes for FEMA NFHL, USGS 3DEP, NHDPlus HR, Water Data, and WBD. |
| [`people/`](people/README.md) | **CONFIRMED README / COMPATIBILITY** | Compatibility RAW index; does not create a canonical People authority root. |
| [`people-dna-land/`](people-dna-land/README.md) | **CONFIRMED README** | People/DNA/Land source capture; confirmed child lane `land-ownership/`; DNA is related compatibility context under `people/dna/`. |
| [`roads-rail-trade/`](roads-rail-trade/README.md) | **CONFIRMED README** | Roads/Rail/Trade source capture; route status, graph, and legal-designation claims require downstream proof/release. |
| [`settlement/`](settlement/README.md) | **CONFIRMED README / COMPATIBILITY** | Singular settlement compatibility path; canonical domain candidate is `settlements-infrastructure`. |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | **CONFIRMED README** | Canonical Settlements/Infrastructure RAW parent lane. |
| [`soil/`](soil/README.md) | **CONFIRMED README** | Soil source capture; support-type separation is required. |
| [`usda-nass/`](usda-nass/README.md) | **CONFIRMED README / COMPATIBILITY** | Root-level USDA NASS compatibility index; canonical lane is `agriculture/usda-nass/`. |

---

## RAW handling rules

| Rule | Handling |
|---|---|
| RAW is source capture | RAW holds source material and admission context only. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Paths encode authority | Domain material belongs under the responsibility-rooted lane, not a topic-root shortcut. |
| Compatibility lanes are not canonical roots | Compatibility paths must not create parallel schema, policy, registry, proof, release, public-layer, graph, or answer authority. |
| Time and version metadata travel | Source time, observation time, retrieval time, effective time, release time, correction time, version, vintage, and digest stay explicit where material. |
| Rights and sensitivity fail closed | Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks promotion. |
| Watchers and connectors do not publish | They may emit source captures, candidates, and receipts; they do not write public artifacts or final claims. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to RAW source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, product identity, source time, observed time, retrieval time, version/vintage, endpoint identity, geometry/support metadata, citation, attribution, rights posture, sensitivity posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, feature counts, raster metadata, series counts, station counts, topology counts, or package metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, graph authority, vector-index authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain doctrine and source-family doctrine | `docs/` |
| Connector code or connector decisions | `connectors/` |
| Pipeline code or pipeline decisions | `pipelines/` and `pipeline_specs/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, sensitivity, review, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/` |
| Normalized working material | `data/work/` |
| Validated processed domain objects | `data/processed/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, graph edges, vector indexes, or generated answers | `data/published/` only after release gates close |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/
├── README.md
├── agriculture/
├── archaeology/
├── atmosphere/
├── fauna/
├── flora/
├── geology/
├── habitat/
├── hazards/
├── hydrology/
├── people/                         # compatibility path
├── people-dna-land/
├── roads-rail-trade/
├── settlement/                     # compatibility path
├── settlements-infrastructure/
├── soil/
├── usda-nass/                      # compatibility path; canonical: agriculture/usda-nass/
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, source family, product identity, path authority, citation, schema, sensitivity, or activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG/TRIPLET, and RELEASE gates close with inspectable evidence, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/
→ data/processed/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs under `data/raw/` and a documented domain/source-family lane.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, rights, citation, product identity, retrieval time, and hash posture.
- [ ] Confirm compatibility paths are not treated as canonical roots unless an accepted ADR or migration note authorizes them.
- [ ] Confirm observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles are not collapsed.
- [ ] Confirm sensitive joins, exact protected locations, living-person data, DNA/genomic data, infrastructure-sensitive details, archaeology/cultural sensitivity, and private land/person joins fail closed where applicable.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior captures in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Directory Rules say placement encodes ownership, governance, and lifecycle; topic alone does not justify a root folder. | **CONFIRMED by GitHub contents API during this edit** |
| RAW lifecycle lanes listed here are documentation/path evidence, not proof of payloads or release maturity. | **CONFIRMED posture** |
| `flora/` currently has path evidence but still needs a substantive parent RAW README. | **NEEDS VERIFICATION / TODO** |
| Actual RAW payloads exist under every listed lane. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for every listed lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, graph authority, vector-index authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`agriculture/README.md`](agriculture/README.md)
- [`archaeology/README.md`](archaeology/README.md)
- [`atmosphere/README.md`](atmosphere/README.md)
- [`fauna/README.md`](fauna/README.md)
- [`flora/README.md`](flora/README.md)
- [`geology/README.md`](geology/README.md)
- [`habitat/README.md`](habitat/README.md)
- [`hazards/README.md`](hazards/README.md)
- [`hydrology/README.md`](hydrology/README.md)
- [`people/README.md`](people/README.md)
- [`people-dna-land/README.md`](people-dna-land/README.md)
- [`roads-rail-trade/README.md`](roads-rail-trade/README.md)
- [`settlement/README.md`](settlement/README.md)
- [`settlements-infrastructure/README.md`](settlements-infrastructure/README.md)
- [`soil/README.md`](soil/README.md)
- [`usda-nass/README.md`](usda-nass/README.md)
- [`../quarantine/README.md`](../quarantine/README.md)
- [`../processed/README.md`](../processed/README.md)
- [`../catalog/README.md`](../catalog/README.md)
- [`../published/README.md`](../published/README.md)
- [`../registry/sources/README.md`](../registry/sources/README.md)
- [`../../docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md)
- [`../../docs/architecture/source-roles.md`](../../docs/architecture/source-roles.md)
- [`../../release/manifests/README.md`](../../release/manifests/README.md)

---

KFM rule: `data/raw/` is the RAW lifecycle root for source capture only. It is not domain doctrine, source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
