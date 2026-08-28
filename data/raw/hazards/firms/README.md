<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hazards/firms/readme
name: Hazards FIRMS Raw README
path: data/raw/hazards/firms/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <hazards-domain-steward>
  - <hazards-source-steward>
  - <firms-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: hazards
source_family: firms
source_role: candidate-observed-sensor
artifact_family: immutable-hazards-firms-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; detection-not-confirmed-event; freshness-bound; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../quarantine/hazards/README.md
  - ../../../processed/hazards/README.md
  - ../../../catalog/domain/hazards/README.md
  - ../../../published/layers/hazards/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hazards/SOURCES.md
  - ../../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../../docs/architecture/smoke-atmosphere-hazards.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hazards
  - firms
  - nasa
  - active-fire
  - remote-sensing-detection
  - candidate
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/hazards/firms/README.md`."
  - "Parent `data/raw/hazards/README.md` is currently a greenfield stub."
  - "FIRMS material is treated as remote-sensing detection source capture. Detection is not confirmed fire-event truth by itself."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards FIRMS RAW Lane

RAW source-family lane for immutable NASA FIRMS active-fire detection captures and source-admission sidecars in the Hazards domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Source family: FIRMS" src="https://img.shields.io/badge/source-FIRMS-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/hazards/firms/` is a RAW source-capture lane. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, confirmed event truth, or generated-answer authority.

---

## Scope

This directory is for immutable NASA FIRMS source captures and RAW-local sidecars in the Hazards domain.

KFM treats FIRMS as remote-sensing detection material. A hotspot or active-fire pixel is candidate evidence and/or sensor-observed detection context, not confirmed fire-event truth by itself. Downstream confirmation, rejection, aggregation, or publication requires SourceDescriptor role handling, validation, evidence closure, review, and release state.

RAW records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, sensor/product fields, confidence/quality fields, geometry/support metadata, checksums, freshness notes, and caveats must travel downstream.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hazards/firms/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hazards` |
| Source family | `firms` |
| Source role | `candidate` and/or `observed` sensor detection; exact role set by SourceDescriptor |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | `data/work/hazards/` or `data/quarantine/hazards/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, sensor/product identity, confidence fields, citation, freshness, validation, or release support is insufficient |

---

## FIRMS source posture

| FIRMS source condition | RAW handling | Boundary |
|---|---|---|
| Active-fire / hotspot detection | Capture as remote-sensing detection when admitted. | Detection is not confirmed fire-event truth by itself. |
| Sensor/product variant | Preserve sensor, product, source time, retrieval time, quality/confidence fields, and citation. | Product variants must not be flattened into one generic source. |
| Candidate disposition pending | Keep in RAW/WORK/QUARANTINE until reviewed. | Candidate records are not published event edges without governed promotion. |
| Smoke-event composition | Preserve FIRMS as one cited input only. | FIRMS alone does not prove smoke at a place/time. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

- source-reference manifests;
- FIRMS dataset references, API/service references, sensor/product references, active-fire record references, or raw payload references;
- source family, provider record ID, sensor/product identity, detection time, retrieval time, geometry/support metadata, confidence/quality fields, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that do not become proof, catalog, registry, policy, release, public artifact, event truth, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| FIRMS/source-family doctrine | `docs/sources/catalog/` or `docs/domains/hazards/` |
| Connector code or connector decisions | `connectors/nasa/` or other connector authority roots |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Rights, terms, review, sensitivity, freshness, or release policy | `policy/` and governed review lanes |
| Quarantine notes | `data/quarantine/hazards/` |
| Normalized working material | `data/work/hazards/` |
| Validated Hazards objects | `data/processed/hazards/` |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests and rollback records | `release/` |
| Public artifacts | `data/published/` only after release gates close |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hazards/firms/
├── README.md
├── <product_or_sensor>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── product_ref.json
│       ├── detection_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was captured, but no downstream decision has been made. |
| Quarantine | Source role, rights, product identity, confidence/quality fields, citation, schema, freshness, or source activation is unresolved. |
| Move to work | SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/hazards/firms/
→ data/processed/hazards/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hazards lane and the FIRMS source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, product/sensor identity, rights, cadence, citation, freshness posture, and hash posture.
- [ ] Confirm active-fire detections are not treated as confirmed fire events by themselves.
- [ ] Confirm sensor/product identity, source time, retrieval time, confidence/quality fields, and geometry support are preserved.
- [ ] Confirm candidate disposition is tracked before any downstream event use.
- [ ] Confirm smoke-event or hazard-event composition keeps FIRMS as a cited input, not sole truth.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/hazards/firms/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/hazards/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| Hazards source-registry doctrine lists NASA FIRMS active fire as remote-sensing detection with candidate / observed-sensor handling and says detection is not confirmed fire. | **CONFIRMED by GitHub contents API during this edit** |
| Smoke seam architecture identifies FIRMS / VIIRS hotspot detection as candidate fire evidence, not proof of smoke at a place/time. | **CONFIRMED by GitHub contents API during this edit** |
| Actual FIRMS RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, confirmed-event truth, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../quarantine/hazards/README.md`](../../../quarantine/hazards/README.md)
- [`../../../processed/hazards/README.md`](../../../processed/hazards/README.md)
- [`../../../catalog/domain/hazards/README.md`](../../../catalog/domain/hazards/README.md)
- [`../../../published/layers/hazards/README.md`](../../../published/layers/hazards/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/domains/hazards/SOURCE_REGISTRY.md`](../../../../docs/domains/hazards/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`](../../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md)
- [`../../../../docs/domains/hazards/SOURCES.md`](../../../../docs/domains/hazards/SOURCES.md)
- [`../../../../docs/domains/hazards/DATA_LIFECYCLE.md`](../../../../docs/domains/hazards/DATA_LIFECYCLE.md)
- [`../../../../docs/architecture/smoke-atmosphere-hazards.md`](../../../../docs/architecture/smoke-atmosphere-hazards.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a Hazards FIRMS RAW source-family lane for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, confirmed-event truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
