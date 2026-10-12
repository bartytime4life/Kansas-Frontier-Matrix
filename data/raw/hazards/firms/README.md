<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hazards/firms/readme
title: Hazards FIRMS Raw README
path: data/raw/hazards/firms/README.md
type: data-raw-source-family-lane-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <hazards-domain-steward>
  - <hazards-source-steward>
  - <firms-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Hazards FIRMS RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: hazards
source_family: firms
source_role: candidate-observed-sensor
artifact_family: hazards-firms-raw-compatibility-reference
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/hazards/firms/README.md`."
  - "Parent `data/raw/hazards/README.md` was a greenfield stub when this README was first authored on 2026-06-27; it is now a tracked compatibility/reference index."
  - "FIRMS material is treated as remote-sensing detection source capture. Detection is not confirmed fire-event truth by itself."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards FIRMS RAW Lane

Compatibility/reference documentation for Hazards-facing FIRMS RAW topology; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Source family: FIRMS" src="https://img.shields.io/badge/source-FIRMS-1f6feb">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/hazards/firms/` is a no-public-path compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this source-named subtree is not a default physical capture home and must not receive duplicate RAW payloads. It is not processed truth, catalog truth, proof, receipt authority, registry authority, policy authority, release authority, public UI/API material, confirmed event truth, or generated-answer authority.

---

## Scope

This directory documents Hazards-facing NASA FIRMS source handling and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

KFM treats FIRMS as remote-sensing detection material. A hotspot or active-fire pixel is candidate evidence and/or sensor-observed detection context, not confirmed fire-event truth by itself. Downstream confirmation, rejection, aggregation, or publication requires SourceDescriptor role handling, validation, evidence closure, review, and release state.

A governed source-first capture records what was captured, where it came from, what source role it carried, and which identifiers, times, rights notes, citations, sensor/product fields, confidence/quality fields, geometry/support metadata, checksums, freshness notes, and caveats must travel downstream.

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
| Artifact role | Compatibility/reference documentation for Hazards-facing FIRMS source handling and unresolved legacy RAW topology |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Governed Hazards WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, sensor/product identity, confidence fields, citation, freshness, validation, or release support is insufficient |

---

## FIRMS source posture

| FIRMS source condition | RAW handling | Boundary |
|---|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; references may support Hazards without duplicating RAW bytes. | A hazards-scoped copy is not a second capture identity. |
| Physical placement is held | Do not infer `data/raw/hazards/firms/` or any subfolder as the capture home. Use only an accepted writer/path contract; none is established by this README. | This lane may retain governed references only. |
| Active-fire / hotspot detection | Capture as remote-sensing detection when admitted. | Detection is not confirmed fire-event truth by itself. |
| Sensor/product variant | Preserve sensor, product, source time, retrieval time, quality/confidence fields, and citation. | Product variants must not be flattened into one generic source. |
| Candidate disposition pending | Keep in RAW/WORK/QUARANTINE until reviewed. | Candidate records are not published event edges without governed promotion. |
| Smoke-event composition | Preserve FIRMS as one cited input only. | FIRMS alone does not prove smoke at a place/time. |
| Public derivative proposal | Hold until policy, proof, release, correction, and rollback gates close. | RAW capture is not a public derivative. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, review, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads.

The governed source-first capture or reference that supports Hazards FIRMS use must carry, where applicable:

- source-reference manifests;
- FIRMS dataset references, API/service references, sensor/product references, active-fire record references, or raw payload references;
- source family, provider record ID, sensor/product identity, detection time, retrieval time, geometry/support metadata, confidence/quality fields, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

None of these, and no local README or index, becomes proof, catalog, registry, policy, release, public artifact, event truth, or answer authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Hazards. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source-run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

Earlier drafts sketched per-product or per-sensor run groupings carrying `source_reference.json`, `product_ref.json`, `detection_ref.json`, `checksums.sha256`, and a run README, plus an optional RAW-local index. That layout is a proposed shape for a future accepted source-first home, not this subtree.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was captured, but no downstream decision has been made. This lane may retain a governed reference only. |
| Quarantine | Source role, rights, product identity, confidence/quality fields, citation, schema, freshness, source activation, or physical placement is unresolved. |
| Return / reject | Admission or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Hazards WORK only when SourceDescriptor, rights posture, source role, source-family identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/hazards/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Hazards-scoped copy.
- [ ] Treat this source-named README as compatibility/reference documentation only; do not create a child directory as a payload destination.
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
| Parent `data/raw/hazards/README.md` was a greenfield stub when this README was first authored (2026-06-27). | **CONFIRMED historically; superseded — the parent is now a tracked compatibility/reference index reconciled on 2026-10-11** |
| Hazards source-registry doctrine lists NASA FIRMS active fire as remote-sensing detection with candidate / observed-sensor handling and says detection is not confirmed fire. | **CONFIRMED by GitHub contents API during this edit** |
| Smoke seam architecture identifies FIRMS / VIIRS hotspot detection as candidate fire evidence, not proof of smoke at a place/time. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual FIRMS RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
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

KFM rule: this directory is a Hazards-facing FIRMS compatibility/reference lane. One governed source-first capture may support Hazards without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, confirmed-event truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
