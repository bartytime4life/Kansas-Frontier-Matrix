<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/pad-us/readme
name: Habitat PAD-US Raw README
path: data/raw/habitat/pad-us/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: habitat
source_family: pad-us
source_role: administrative-context
artifact_family: immutable-habitat-pad-us-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../quarantine/habitat/README.md
  - ../../../processed/habitat/README.md
  - ../../../catalog/domain/habitat/README.md
  - ../../../published/layers/habitat/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/SOURCES.md
  - ../../../../docs/domains/habitat/POLICY.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - pad-us
  - usgs
  - stewardship
  - source-capture
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/habitat/pad-us/README.md`."
  - "Parent `data/raw/habitat/README.md` is currently a greenfield stub."
  - "This lane is source capture only; implementation wiring and payload presence remain unverified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat PAD-US RAW Lane

RAW source-family lane for PAD-US Habitat source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Source family: PAD-US" src="https://img.shields.io/badge/source-PAD--US-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/habitat/pad-us/` is a RAW source-capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, or generated-answer authority.

---

## Scope

This directory is for immutable PAD-US source captures and RAW-local sidecars in the Habitat domain.

KFM treats PAD-US as administrative context for stewardship-zone work. The Habitat docs identify PAD-US as a USGS source family and say it needs version, GAP-status fields, boundary-diff strategy, rights, and source URI recorded by SourceDescriptor.

RAW records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, version fields, hashes, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/pad-us/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `habitat` |
| Source family | `pad-us` |
| Source role | `administrative`; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, version, citation, validation, or release support is insufficient |

---

## Source posture

| Source condition | RAW handling | Boundary |
|---|---|---|
| PAD-US versioned release | Capture as administrative context when admitted. | A new version must not overwrite a prior capture in place. |
| GAP-status fields | Preserve native fields and version. | Crosswalks are advisory until downstream proof/release closure. |
| Boundary-diff strategy | Preserve method and comparison basis. | Diff output requires downstream validation before publication. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |
| Mixed package | Split by SourceDescriptor or quarantine. | One descriptor carries one role. |

---

## Accepted material

- source-reference manifests;
- PAD-US release references, source URI references, GAP-status references, boundary-diff references, or raw payload references;
- release version, source URI, source time, retrieval time, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/pad-us/
├── README.md
├── <release_or_run_id>/
│   ├── source_reference.json
│   ├── release_ref.json
│   ├── gap_status_ref.json
│   ├── boundary_diff_ref.json
│   ├── checksums.sha256
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, version, citation, schema, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/habitat/pad-us/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and the PAD-US source family.
- [ ] Confirm a SourceDescriptor or admission ticket records source ID, source role, rights, citation, review posture, and hash posture.
- [ ] Confirm release version, GAP-status fields, source URI, and boundary-diff strategy are recorded.
- [ ] Confirm a new release is stored as a new capture and does not overwrite a prior capture in place.
- [ ] Confirm GAP-status crosswalks remain advisory until downstream proof/release closure.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/habitat/pad-us/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/habitat/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat docs identify PAD-US as USGS Protected Areas Database stewardship context. | **CONFIRMED by GitHub contents API during this edit** |
| Habitat docs say PAD-US source role is administrative and requires version, GAP-status fields, boundary-diff strategy, rights, and source URI. | **CONFIRMED by GitHub contents API during this edit** |
| Actual PAD-US RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../quarantine/habitat/README.md`](../../../quarantine/habitat/README.md)
- [`../../../processed/habitat/README.md`](../../../processed/habitat/README.md)
- [`../../../catalog/domain/habitat/README.md`](../../../catalog/domain/habitat/README.md)
- [`../../../published/layers/habitat/README.md`](../../../published/layers/habitat/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/habitat/SOURCE_REGISTRY.md`](../../../../docs/domains/habitat/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/habitat/SOURCE_FAMILIES.md`](../../../../docs/domains/habitat/SOURCE_FAMILIES.md)
- [`../../../../docs/domains/habitat/SOURCES.md`](../../../../docs/domains/habitat/SOURCES.md)
- [`../../../../docs/domains/habitat/POLICY.md`](../../../../docs/domains/habitat/POLICY.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat PAD-US RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
