<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/archaeology/readme
name: Archaeology Raw README
path: data/raw/archaeology/README.md
type: data-raw-domain-index-readme
version: v0.1.0
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
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: archaeology
artifact_family: immutable-archaeology-source-capture
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
notes:
  - "This README replaces the greenfield stub and documents the parent Archaeology RAW lifecycle lane."
  - "No Archaeology RAW child source README lanes were confirmed during this edit; source-family classes are routing guidance only."
  - "RAW is immutable source capture and source-admission context; it is not Archaeology truth, processed truth, catalog truth, proof, receipt authority, release authority, public API/UI output, or generated-answer authority."
  - "Archaeology doctrine applies deny-by-default controls for exact site locations, human remains, burials, sacred sites, unresolved cultural sensitivity, collection-security details, private landowner details, and looting-risk exposure."
  - "Source rights, current terms, payload presence, source descriptors, connector activation, validator wiring, CI enforcement, review completion, cultural-review state, sovereignty labels, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology RAW

Parent RAW lifecycle lane for immutable Archaeology and cultural-heritage source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-8a6d3b">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4%20default-critical">
  <img alt="Exact location: deny" src="https://img.shields.io/badge/exact%20location-DENY-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source lanes](#confirmed-source-lanes) · [Proposed source families](#proposed-source-families) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/archaeology/` is a no-public-path RAW source-capture lane. Material here is not public, not processed archaeology truth, not catalog truth, not proof, not receipt authority, not source registry authority, not rights authority, not sensitivity authority, not policy authority, not site truth, not artifact truth, not cultural-review authority, not sovereignty authority, not release authority, and not generated-answer authority. No public client or normal UI surface may read this lane directly.

---

## Scope

This directory holds immutable source captures, source references, source-head snapshots, field/source packet snapshots, manifest snapshots, checksums, and minimal source-admission sidecars for Archaeology source families.

RAW is for preservation, replay, and audit. It does not decide what a source means, whether rights permit use, whether a source can publish, whether a site or feature is real, whether a cultural review is complete, whether a sensitivity transform is adequate, or whether a downstream claim is true.

Archaeology is a deny-by-default sensitivity lane. Exact site coordinates, human remains, burials, sacred sites, unresolved cultural sensitivity, collection-security details, private landowner details, looting-risk exposure, oral-history/cultural-knowledge material, sovereignty-labeled content, and consent-bound material must fail closed until the appropriate reviewer and policy records exist.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/archaeology/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `archaeology` |
| Artifact role | Parent RAW lane for Archaeology source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/archaeology/` or `data/quarantine/archaeology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when rights, source role, cultural review, sovereignty label, consent, sensitivity, geometry precision, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source lanes

No `data/raw/archaeology/` child source-lane README paths were confirmed during this edit. This parent index is confirmed as authored, but child routing remains proposed until a child README path is created and verified.

| Child lane | Status | Notes |
|---|---|---|
| `<none confirmed>` | **UNKNOWN** | Do not infer payloads, SourceDescriptors, connector activation, validators, fixtures, release gates, or CI coverage from this parent README. |

---

## Proposed source families

Archaeology source docs name the families below. They are source-routing guidance, not proof that RAW folders, payloads, SourceDescriptors, connectors, fixtures, or validators exist.

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

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- source packet snapshots and stable source references;
- raw payloads or restricted raw payload references;
- field-survey, inventory, collection, lab, map, oral-history, remote-sensing, 3D, or repository packet references with digest closure;
- source-head records, retrieval/admission timestamps, source vintage notes, provenance notes, access notes, and checksums;
- minimal README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, review, sovereignty, consent, or public authority.

Do not place exact site coordinates, human-remains details, sacred-site details, looting-sensitive collection details, private landowner details, raw oral-history text, consent tokens, revocation tokens, or culturally restricted text into this README.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
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
├── README.md
├── <source_family_or_source_id>/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── payload_ref.json
│       ├── manifest.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, review record, graph edge source, layer/story/report pointer, search index, vector index, map source, site-truth index, cultural-review index, sovereignty authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Rights, source role, sensitivity, cultural review, sovereignty label, consent, geometry precision, citation, digest, schema, source activation, or admission state is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, cultural/sensitivity posture, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, cultural review, redaction/generalization, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcuts

```text
data/raw/archaeology/
→ data/processed/archaeology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Archaeology lane.
- [ ] Confirm the correct source family subfolder or create a documented source-lane README before adding payloads.
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
| Archaeology lifecycle doctrine identifies `data/raw/archaeology/<source_id>/<run_id>/` as the raw data pattern. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology lifecycle doctrine says RAW is admitted source material, not public, and public clients, AI context, UI layers, and normalized records must not read RAW directly. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology sensitivity doctrine says exact site geometry, human remains, sacred sites, collection security, and looting-risk exposure are T4 deny/fail-closed. | **CONFIRMED by GitHub contents API during this edit** |
| Archaeology source docs say every source family carries rights/current terms NEEDS VERIFICATION, sensitive joins fail closed, and source role is fixed at admission. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Archaeology RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, validators, fixtures, CI checks, cultural-review workflows, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
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

KFM rule: this directory is an Archaeology RAW source-capture index only. It is not source-family doctrine, source registry authority, rights authority, sensitivity authority, policy authority, cultural-review authority, sovereignty authority, proof authority, receipt authority, release authority, catalog authority, site truth, artifact truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
