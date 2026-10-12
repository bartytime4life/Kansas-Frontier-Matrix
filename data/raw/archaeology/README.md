<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/archaeology/readme
title: Archaeology Raw README
path: data/raw/archaeology/README.md
type: data-raw-domain-index-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <archaeology-domain-steward>
  - <archaeology-source-steward>
  - <data-steward>
  - <cultural-review-liaison>
  - <rights-holder-representative>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Archaeology RAW compatibility and reference index and its fail-closed sensitivity, cultural-review, and sovereignty protections without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
domain: archaeology
artifact_family: archaeology-raw-compatibility-reference-index
sensitivity_posture: T4-default; fail-closed; no-public-path; exact-location-deny; cultural-review-required; sovereignty-inheritance-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../quarantine/archaeology/README.md
  - ../../quarantine/archaeology/exact_geometry/README.md
  - ../../processed/archaeology/README.md
  - ../../catalog/domain/archaeology/README.md
  - ../../published/layers/archaeology/README.md
  - ../../proofs/archaeology/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/archaeology/DATA_LIFECYCLE.md
  - ../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../docs/domains/archaeology/SOURCES.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../connectors/archaeology/README.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - archaeology
  - cultural-heritage
  - source-capture
  - exact-location-deny
  - sacred-sites
  - burial-sites
  - human-remains
  - cultural-review
  - sovereignty
  - consent
  - redaction
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README replaces the greenfield stub and documents the Archaeology-facing RAW compatibility/reference index."
  - "No Archaeology RAW child source README lanes were confirmed during this edit; source-family classes are routing guidance only."
  - "RAW is immutable source-first capture and source-admission context; this domain index is not a physical capture home and is not Archaeology truth, processed truth, catalog truth, proof, receipt authority, release authority, public API/UI output, or generated-answer authority."
  - "Archaeology doctrine applies deny-by-default controls for exact site locations, human remains, burials, sacred sites, unresolved cultural sensitivity, collection-security details, private landowner details, and looting-risk exposure."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, validator wiring, CI enforcement, review completion, cultural-review state, sovereignty labels, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "Archaeology deny-by-default, exact-location-deny, cultural-review, sovereignty-inheritance, and consent controls travel with any source-first capture that supports Archaeology, wherever it is placed; unresolved placement never relaxes them."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology RAW

Compatibility and reference index for legacy Archaeology and cultural-heritage RAW documentation; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4%20default-critical">
  <img alt="Exact location: deny" src="https://img.shields.io/badge/exact%20location-DENY-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source lanes](#confirmed-source-lanes) · [Proposed source families](#proposed-source-families) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/archaeology/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this domain subtree and any children are not default physical capture homes and must not receive duplicate RAW payloads. Every Archaeology sensitivity, cultural-review, sovereignty, consent, and exact-location protection below still applies to any source-first capture that supports Archaeology. Material here is not public, not processed archaeology truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not site truth, not artifact truth, not cultural-review authority, not sovereignty authority, not release authority, and not generated-answer authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory indexes tracked Archaeology-facing source documentation and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture preserves the source references, source-head snapshots, field/source packet snapshots, manifest snapshots, checksums, and minimal source-admission context that Archaeology use depends on.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a source can publish, whether a site or feature is real, whether a cultural review is complete, whether a sensitivity transform is adequate, or whether a downstream claim is true.

Archaeology is a deny-by-default sensitivity lane. Exact site coordinates, human remains, burials, sacred sites, unresolved cultural sensitivity, collection-security details, private landowner details, looting-risk exposure, oral-history/cultural-knowledge material, sovereignty-labeled content, and consent-bound material must fail closed until the appropriate reviewer and policy records exist. These controls bind the source-first capture and every reference to it, regardless of physical placement; an unresolved placement is itself a reason to fail closed, never a reason to relax them.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/archaeology/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `archaeology` |
| Artifact role | Compatibility/reference index for Archaeology-facing source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Archaeology WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, cultural review, sovereignty label, consent, sensitivity, geometry precision, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source lanes

No `data/raw/archaeology/` child source-lane README paths were confirmed during this edit or at `main@9e8bf3e6`. This index is confirmed as authored. Any future child README would be compatibility/reference documentation only, never a payload destination or source-first capture home.

| Child lane | Status | Notes |
|---|---|---|
| `<none confirmed>` | **UNKNOWN** | Do not infer payloads, SourceDescriptors, connector activation, validators, fixtures, release gates, or CI coverage from this parent README. |

---

## Proposed source families

Archaeology source docs name the families below. They are source-routing guidance, not proof that RAW folders, payloads, SourceDescriptors, connectors, fixtures, or validators exist, and not authorization to create Archaeology-scoped RAW folders for them.

| Source family | Typical posture | Status |
|---|---|---|
| State site inventory / SHPO-equivalent records | Authority source; exact location and steward control fail closed | **PROPOSED / NEEDS VERIFICATION** |
| Public NRHP-like listings | Public listing context; still sensitivity-reviewed before joins or map surfaces | **PROPOSED / NEEDS VERIFICATION** |
| Field survey forms | Observation/source packet; coordinates and landowner details are restricted by default | **PROPOSED / NEEDS VERIFICATION** |
| Excavation records and provenience packets | Provenience and context evidence; exact geometry and collection-security controls apply | **PROPOSED / NEEDS VERIFICATION** |
| Artifact / collection / repository records | Repository/collection evidence; collection-security and rights review required | **PROPOSED / NEEDS VERIFICATION** |
| Lab reports | Analysis evidence; source role, chain of custody, sample context, and rights must be preserved | **PROPOSED / NEEDS VERIFICATION** |
| Historic maps / plats / land records / newspapers | Context evidence; not site confirmation by itself | **PROPOSED / NEEDS VERIFICATION** |
| Oral history and cultural knowledge | Authority/consent-bound material; cultural review, sovereignty, consent, and revocation controls required | **PROPOSED / NEEDS VERIFICATION** |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support Archaeology without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/archaeology/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| Sensitivity travels with the capture | T4-default, exact-location-deny, human-remains, burial, sacred-site, collection-security, looting-risk, landowner, cultural-review, sovereignty-inheritance, consent, and revocation controls apply to the source-first capture and every reference to it, wherever it is placed. |
| Unresolved placement fails closed | If the accepted source-first home, its access tier, or its restriction controls are unclear, route to QUARANTINE / HOLD rather than staging restricted material here. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, cultural-review, sovereignty, consent, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape and the reference itself exposes no restricted detail;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, access tier, and non-authoritative role are accepted.

The source-first capture or its governed (restricted) reference must carry, where material: source-reference manifests; source packet snapshots and stable source references; raw payloads or restricted raw payload references; field-survey, inventory, collection, lab, map, oral-history, remote-sensing, 3D, or repository packet references with digest closure; and source-head records, retrieval/admission timestamps, source vintage notes, provenance notes, access notes, and checksums. Any README or index sidecar must help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, review, sovereignty, consent, or public authority.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Archaeology. Exact physical placement and legacy migration remain **HOLD**.

Do not place exact site coordinates, human-remains details, sacred-site details, looting-sensitive collection details, private landowner details, raw oral-history text, consent tokens, revocation tokens, or culturally restricted text into this README.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision, with Archaeology access-tier and restriction controls intact; exact path remains **NEEDS VERIFICATION** |
| Archaeology source-family doctrine | `docs/domains/archaeology/` |
| Connector code or connector decisions | `connectors/archaeology/` or accepted connector home |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` or accepted source-registry lane |
| Rights, terms, sensitivity, sovereignty, consent, redaction, or policy rules | `policy/` |
| Cultural review, steward review, release review, and reviewer authority | Governance/review lanes, not RAW source capture |
| Quarantine holds and remediation notes | `data/quarantine/archaeology/` |
| Normalized working material | `data/work/archaeology/` |
| Validated processed Archaeology objects | `data/processed/archaeology/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, cultural-review, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Site truth, artifact truth, chronology truth, cultural authority, landowner truth, or public interpretation | Governed downstream lanes after evidence/review closure; never RAW alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/archaeology/
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source or run directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

The earlier per-run layout (a source-family or source-ID directory, then a run-ID directory holding `source_reference.json`, `payload_ref.json`, `manifest.json`, `checksums.sha256`, and a `README.md`) is retained only as a proposed shape for a future accepted source-first home, not this subtree; that home must enforce the Archaeology access tier and restriction controls above.

Any optional RAW-local index (previously sketched in this map as a local JSON index file) belongs to that proposed shape, not this subtree. If accepted, it is not a public index, catalog record, registry record, release manifest, review record, graph edge source, layer/story/report pointer, search index, vector index, map source, site-truth index, cultural-review index, sovereignty authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This index may retain a governed reference only, and that reference must not expose restricted detail. |
| Quarantine | Rights, source role, sensitivity, cultural review, sovereignty label, consent, geometry precision, citation, digest, schema, source activation, admission state, or physical placement is unresolved. |
| Return / reject | Admission decision, steward review, cultural review, or rights-holder direction says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Archaeology WORK only when SourceDescriptor, rights posture, source role, cultural/sensitivity posture, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, cultural review, redaction/generalization, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/archaeology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Archaeology-scoped copy.
- [ ] Treat this README (and any source-named child README) as compatibility/reference documentation only; do not create a child directory as a payload destination.
- [ ] Confirm the source-first capture home, wherever placed, enforces the Archaeology access tier, exact-location deny, cultural-review, sovereignty, and consent controls; if not verifiable, fail closed.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, authority, rights, sensitivity, cadence, citation, sovereignty posture, consent posture where applicable, and hash posture.
- [ ] Confirm exact site coordinates, human remains, sacred sites, collection security, looting risk, private landowner details, oral history, and cultural knowledge are not exposed beyond the approved access tier.
- [ ] Confirm source role is not being upgraded by promotion or convenience.
- [ ] Confirm rights, current terms, citation, cultural review, sovereignty inheritance, consent/revocation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm prompt-like content inside source payloads is treated as data and not instructions.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public layer, PMTiles, report, story, API payload, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/archaeology/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| No `data/raw/archaeology/` child source-lane README path was confirmed during this edit. | **CONFIRMED by GitHub search/fetch during this edit** |
| Archaeology lifecycle doctrine identifies `data/raw/archaeology/<source_id>/<run_id>/` as the raw data pattern. | **CONFIRMED by GitHub contents API during the original edit**; that domain-first pattern conflicts with accepted `DIR-SOURCE-001` and is not a physical placement decision — **HOLD / NEEDS VERIFICATION** pending reconciliation of the domain doctrine |
| Archaeology lifecycle doctrine says RAW is admitted source material, not public, and public clients, AI context, UI layers, and normalized records must not read RAW directly. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology sensitivity doctrine says exact site geometry, human remains, sacred sites, collection security, and looting-risk exposure are T4 deny/fail-closed. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology source docs say every source family carries rights/current terms NEEDS VERIFICATION, sensitive joins fail closed, and source role is fixed at admission. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Archaeology deny-by-default, exact-location-deny, cultural-review, sovereignty, and consent controls are relaxed by the source-first reclassification. | **DENY — they bind the source-first capture and every reference wherever placed** |
| Actual Archaeology RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, validators, fixtures, CI checks, cultural-review workflows, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, site truth, artifact truth, cultural-review authority, sovereignty authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/archaeology/README.md`](../../quarantine/archaeology/README.md)
- [`../../quarantine/archaeology/exact_geometry/README.md`](../../quarantine/archaeology/exact_geometry/README.md)
- [`../../processed/archaeology/README.md`](../../processed/archaeology/README.md)
- [`../../catalog/domain/archaeology/README.md`](../../catalog/domain/archaeology/README.md)
- [`../../published/layers/archaeology/README.md`](../../published/layers/archaeology/README.md)
- [`../../proofs/archaeology/README.md`](../../proofs/archaeology/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/archaeology/DATA_LIFECYCLE.md`](../../../docs/domains/archaeology/DATA_LIFECYCLE.md)
- [`../../../docs/domains/archaeology/SOURCE_REGISTRY.md`](../../../docs/domains/archaeology/SOURCE_REGISTRY.md)
- [`../../../docs/domains/archaeology/SOURCES.md`](../../../docs/domains/archaeology/SOURCES.md)
- [`../../../docs/domains/archaeology/SENSITIVITY.md`](../../../docs/domains/archaeology/SENSITIVITY.md)
- [`../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md`](../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md)
- [`../../../docs/domains/archaeology/CULTURAL_REVIEW.md`](../../../docs/domains/archaeology/CULTURAL_REVIEW.md)
- [`../../../connectors/archaeology/README.md`](../../../connectors/archaeology/README.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is an Archaeology-facing compatibility/reference index. One governed source-first capture may support Archaeology without duplicated RAW bytes; this subtree does not establish physical placement, and Archaeology sensitivity, cultural-review, sovereignty, consent, and exact-location protections travel with that capture wherever it lives. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, policy authority, cultural-review authority, sovereignty authority, proof authority, receipt authority, release authority, catalog authority, site truth, artifact truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
