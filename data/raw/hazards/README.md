<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/hazards/readme
name: Hazards Raw README
path: data/raw/hazards/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <hazards-domain-steward>
  - <hazards-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: hazards
artifact_family: immutable-hazards-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; not-an-alert-system; freshness-bound; rights-needs-verification; release-blocked
related:
  - fema/README.md
  - firms/README.md
  - nfhl/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/hazards/README.md
  - ../../processed/hazards/README.md
  - ../../catalog/domain/hazards/README.md
  - ../../published/layers/hazards/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/hazards/SOURCE_REGISTRY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/SOURCES.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - hazards
  - source-capture
  - source-role
  - source-family-index
  - freshness
  - not-an-alert-system
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/hazards/README.md`."
  - "Confirmed child README lanes during this edit: `fema/`, `firms/`, and `nfhl/`."
  - "README presence confirms documentation lanes only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, review controls, or release readiness."
  - "Hazards RAW records remain source captures until governed downstream lifecycle transitions close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards RAW

Parent RAW lifecycle index for immutable Hazards source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-c62828">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Boundary: not an alert system" src="https://img.shields.io/badge/boundary-not%20an%20alert%20system-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source-family lanes](#confirmed-source-family-lanes) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/hazards/` is a no-public-path RAW lifecycle lane. It is not processed Hazards truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, live alert material, emergency guidance, or generated-answer authority.

---

## Scope

This directory indexes immutable RAW source captures and source-admission sidecars for the Hazards domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, versions, times, rights notes, citations, geometry/support metadata, source-head metadata, freshness posture, hashes, review notes, and caveats must travel downstream.

RAW does not decide what a hazard means, whether a detection is confirmed, whether a regulatory layer describes observed conditions, whether an operational product is current, whether rights permit reuse, whether a downstream claim can publish, or whether an answer may be generated.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/hazards/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `hazards` |
| Artifact role | Parent RAW domain index for Hazards source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/hazards/` or `data/quarantine/hazards/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, citation, geometry/support, freshness, classification, review state, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source-family lanes

The child lanes below are README paths confirmed by current-session GitHub fetches. This table confirms README presence only; it does **not** prove payloads, SourceDescriptors, connectors, validators, fixtures, receipts, CI checks, review controls, or release readiness.

| Source-family lane | Status | Parent boundary |
|---|---|---|
| [`fema/`](fema/README.md) | **CONFIRMED README** | FEMA requires per-product role handling: administrative declarations and regulatory flood context are separate. |
| [`firms/`](firms/README.md) | **CONFIRMED README** | FIRMS is remote-sensing detection source capture; detection is not confirmed event truth by itself. |
| [`nfhl/`](nfhl/README.md) | **CONFIRMED README** | NFHL is regulatory flood-hazard context; not observed inundation, not model output, and not release authority by itself. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Candidate remains candidate | Remote-sensing detections, unmerged reports, and preliminary materials require disposition before publication. |
| Regulatory is not observed | FEMA NFHL / MSC flood context must not be reframed as observed inundation or modeled flood output. |
| Administrative is not event truth | FEMA disaster declarations and similar administrative actions must not be used as observed event timelines by themselves. |
| Freshness gates matter | Operational and near-real-time context must carry source time, retrieval time, expiry/freshness posture, and stale-state handling where applicable. |
| Watchers do not publish | Watchers may emit intake candidates; they do not admit, promote, publish, or answer public claims. |
| Public use requires governed release | Public layers, PMTiles, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, source time, retrieval time, product version/vintage, source-head metadata, geometry/support metadata, citation, attribution, rights posture, freshness posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, alert authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Hazards domain doctrine | `docs/domains/hazards/` |
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/hazards/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, sensitivity, freshness, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/hazards/` |
| Normalized working material | `data/work/hazards/` |
| Validated Hazards objects | `data/processed/hazards/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, review, source-role, freshness, model, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Emergency alerting, life-safety guidance, observed-event truth, regulatory truth, model truth, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/hazards/
├── README.md
├── fema/
│   └── README.md
├── firms/
│   └── README.md
├── nfhl/
│   └── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, source family, product/version identity, citation, geometry/support, schema, freshness, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization/model/freshness receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/hazards/
→ data/processed/hazards/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Hazards lane and a documented source-family subfolder.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, product identity, rights, cadence, citation, freshness posture, and hash posture.
- [ ] Confirm source roles are not collapsed across observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic products.
- [ ] Confirm candidate detections are not treated as confirmed event truth.
- [ ] Confirm regulatory context is not treated as observed or modeled condition truth.
- [ ] Confirm administrative records are not treated as observed event timelines by themselves.
- [ ] Confirm current/near-real-time context has source time, retrieval time, freshness/expiry posture, and stale-state handling where applicable.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior captures in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/hazards/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child README lanes confirmed during this edit: fema, firms, and nfhl. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, receipts, review controls, or release readiness. | **DENY** |
| Hazards source-registry doctrine lists source roles and marks live descriptor activation as needing verification. | **CONFIRMED by GitHub contents API during this edit** |
| Hazards source-role doctrine says role is first-class, set at admission, and preserved through promotion. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Hazards RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, alert authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`fema/README.md`](fema/README.md)
- [`firms/README.md`](firms/README.md)
- [`nfhl/README.md`](nfhl/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/hazards/README.md`](../../quarantine/hazards/README.md)
- [`../../processed/hazards/README.md`](../../processed/hazards/README.md)
- [`../../catalog/domain/hazards/README.md`](../../catalog/domain/hazards/README.md)
- [`../../published/layers/hazards/README.md`](../../published/layers/hazards/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/hazards/SOURCE_REGISTRY.md`](../../../docs/domains/hazards/SOURCE_REGISTRY.md)
- [`../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md)
- [`../../../docs/domains/hazards/SOURCES.md`](../../../docs/domains/hazards/SOURCES.md)
- [`../../../docs/domains/hazards/DATA_LIFECYCLE.md`](../../../docs/domains/hazards/DATA_LIFECYCLE.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Hazards RAW domain index for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, alert authority, observed-event truth, regulatory truth, model truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
