<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people/dna/readme
name: People DNA Raw Compatibility README
path: data/raw/people/dna/README.md
type: data-raw-lane-readme; compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <dna-sublane-steward>
  - <data-steward>
  - <consent-reviewer>
  - <privacy-reviewer>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
requested_path_segment: people/dna
canonical_domain_candidate: people-dna-land
artifact_family: immutable-dna-genomic-source-capture
sensitivity_posture: T4-default; fail-closed; no-public-path; encrypted-access-scoped; raw-genotype-never-public; consent-required; revocation-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/people/dna/README.md
  - ../../../quarantine/people-dna-land/README.md
  - ../../../processed/people-dna-land/README.md
  - ../../../catalog/domain/people-dna-land/README.md
  - ../../../published/layers/people-dna-land/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/domains/people-dna-land/DNA_HANDLING.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/people-dna-land/sublanes/dna.md
  - ../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - people
  - dna
  - people-dna-land
  - compatibility-path
  - genomic
  - genetic-genealogy
  - consent
  - revocation
  - privacy
  - deny-by-default
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/people/dna/README.md`."
  - "Parent `data/raw/people/README.md` currently contains placeholder content only."
  - "Visible People/DNA/Land doctrine treats DNA/genomic material as highest-sensitivity, deny-by-default material; raw genotype is never public."
  - "The requested `people/dna` path is documented as a compatibility RAW lane, not a new canonical domain authority root."
  - "Payload presence, encryption/storage implementation, ConsentGrant records, RevocationReceipt records, SourceDescriptor records, policy automation, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People / DNA RAW Compatibility Lane

Compatibility RAW lifecycle lane for DNA, genomic, genetic-genealogy, consent, revocation, and DNA-derived evidence source captures associated with the People/DNA/Land domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4%20default-critical">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Canonical path warning](#canonical-path-warning) · [Scope](#scope) · [Repo fit](#repo-fit) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/people/dna/` is a no-public-path compatibility RAW lane. It is not processed truth, catalog truth, proof, receipt authority, consent authority, policy authority, release authority, person identity truth, relationship truth, DNA/genomic truth, public UI/API material, graph/vector-index authority, or generated-answer authority.

---

## Canonical path warning

Directory Rules state that file placement encodes ownership, governance, and lifecycle, and topic alone does not justify a root folder. Visible People/DNA/Land doctrine uses `people-dna-land` as the current domain candidate, while this requested path uses nested `people/dna`.

Treat this path as a **compatibility RAW lane** unless an accepted ADR or migration note explicitly authorizes `people/dna` as a canonical lifecycle path. Do not create parallel schema, contract, policy, registry, proof, release, public-layer, graph, vector-index, or generated-answer authority from this nested compatibility path.

---

## Scope

This directory may hold DNA-related RAW source-capture material only when the repository intentionally preserves the `people/dna` path as a compatibility bridge. It is governed by the stricter People/DNA/Land DNA handling rules.

In scope as RAW source capture, subject to consent, rights, storage, access, and review controls:

- direct-to-consumer DNA/genomic exports or references;
- DNA match evidence and DNA segment evidence or references;
- DNAKitToken sidecars or tokenized references, never public vendor identifiers;
- consent, revocation, retention, audience, redaction-profile, and rights sidecars;
- source-admission records needed to decide whether material stays RAW, moves to WORK, moves to QUARANTINE, or is rejected.

RAW records what was captured, where it came from, who may govern it, what consent scope applies, which revocation state applies, what identifiers were tokenized, and what caveats must travel downstream. RAW does not prove identity, relationship, ancestry, title, ownership, person status, or publication readiness.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/people/dna/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Requested segment | `people/dna` |
| Canonical domain candidate | `people-dna-land` |
| Lane type | Compatibility RAW lane for DNA/genomic source capture |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Explicitly admitted source material only |
| Downstream | `data/work/people-dna-land/` or `data/quarantine/people/dna/` / `data/quarantine/people-dna-land/` after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Consent/policy authority | `policy/consent/people/` and sensitivity/policy roots, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Default failure posture | `DENY`, `QUARANTINE`, `HOLD`, or `ABSTAIN` when consent, revocation, living-person status, rights, source role, path authority, storage posture, tokenization, evidence, review, correction, rollback, or release support is insufficient |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Deny by default | DNA/genomic material is treated as highest-sensitivity unless a stricter policy says otherwise. |
| Raw genotype is never public | Raw DNA/genomic material cannot become public artifact material. |
| Consent is required | Consent scope, audience, expiry, retention, and revocation state must travel with the material. |
| Revocation is first-class | Revoked, expired, unreachable, or unresolved consent fails closed. |
| Tokenization is mandatory before broader use | Raw kit/vendor identifiers must not appear outside approved RAW handling. |
| DNA is evidence, not identity truth | DNA match evidence may support a reviewed hypothesis; it does not prove identity or relationship by itself. |
| Aggregates require proof | Aggregate or k-anonymized DNA-derived outputs need aggregation/de-identification proof and review before release. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW lane directly. |

---

## Accepted material

Accepted content is limited to RAW source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payload references or encrypted/access-scoped raw payload pointers;
- admission-ticket references and SourceDescriptor references;
- ConsentGrant, consent-scope, retention, audience, revocation, redaction-profile, and rights references;
- tokenization sidecars for kit/vendor identifiers;
- source identity, source role, source time, retrieval time, vendor/source family, citation, attribution, rights posture, review notes, digest sidecars, and caveats;
- local README or index sidecars that help a steward understand capture state without becoming proof, consent authority, catalog, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| People/DNA/Land doctrine | `docs/domains/people-dna-land/` |
| Source-family doctrine | `docs/domains/people-dna-land/SOURCE_REGISTRY.md` and source catalog docs |
| Authoritative SourceDescriptor records | `data/registry/sources/` |
| Consent policy, revocation policy, sensitivity policy, or render gates | `policy/consent/people/`, `policy/sensitivity/people/`, and governed policy roots |
| Quarantine holds and remediation notes | `data/quarantine/people/dna/` or `data/quarantine/people-dna-land/` |
| Normalized working material | `data/work/people-dna-land/` if that path is confirmed, otherwise hold/quarantine until ADR resolution |
| Processed DNA-derived candidates | `data/processed/people-dna-land/` only after gates close |
| Catalog, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, reports, stories, API payloads, downloads, PMTiles, graph edges, vector indexes, or generated answers | `data/published/` only after release gates close; raw DNA never public |
| Person identity truth, relationship truth, genealogy truth, ancestry truth, title/ownership truth, or generated-answer truth | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/people/dna/
├── README.md
├── intake/
│   └── <source_or_run_id>/
│       ├── source_reference.json
│       ├── consent_ref.json
│       ├── revocation_ref.json
│       ├── rights_ref.json
│       ├── checksums.sha256
│       └── README.md
├── tokenized-references/
│   └── <source_or_run_id>/
│       ├── source_reference.json
│       ├── tokenization_ref.json
│       ├── consent_scope_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and RAW-local only. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Consent, revocation, rights, living-person status, source role, tokenization, storage posture, path authority, or review state is unresolved. |
| Reject / erase | Consent is absent, revoked, expired, out of scope, or source retention is not permitted. |
| Move to work | Consent, revocation, rights, source role, tokenization, storage/access posture, citation, hash, and review support are sufficient. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with inspectable evidence, consent/revocation checks, aggregation or redaction proof where applicable, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/people/dna/
→ data/processed/people-dna-land/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence. Raw genotype material does not cross the publication boundary.

---

## Required checks before use

- [ ] Confirm the path is being used as a compatibility RAW lane, not a new canonical authority root.
- [ ] Confirm consent exists, is machine-readable, unexpired, unrevoked, and scoped to the requested use.
- [ ] Confirm revocation handling and cache/render invalidation requirements are known before any downstream exposure.
- [ ] Confirm raw kit/vendor identifiers are absent outside approved RAW handling and tokenization sidecars are present where needed.
- [ ] Confirm DNA evidence is not treated as person identity truth, relationship truth, genealogy truth, ancestry truth, title truth, or ownership truth.
- [ ] Confirm source role, rights, vendor/source-family terms, citation, retention, storage posture, and review state are recorded or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm aggregate or k-anonymized derivatives have aggregation/de-identification proof before any release proposal.
- [ ] Confirm raw payloads are immutable or hash-bound and access-scoped.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW DNA material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/people/dna/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/people/README.md` currently contains placeholder content only. | **CONFIRMED by GitHub contents API during this edit** |
| Directory Rules say placement encodes ownership, governance, and lifecycle; topic alone does not justify a root folder. | **CONFIRMED by GitHub contents API during this edit** |
| People/DNA/Land doctrine says raw genotype is never republished and only aggregate or k-anonymized derived data may cross the publication boundary under documented consent and review. | **CONFIRMED by GitHub contents API during this edit** |
| DNA sublane doctrine says raw kit/vendor identifiers and raw genotype data never cross the publication boundary, and DNA evidence does not become relationship authority by itself. | **CONFIRMED by GitHub contents API during this edit** |
| Actual DNA RAW payloads exist under this subtree. | **UNKNOWN** |
| Encryption/storage implementation, ConsentGrant records, RevocationReceipt records, SourceDescriptor records, policy automation, validators, fixtures, CI checks, review controls, and release readiness are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, consent authority, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, person identity truth, relationship truth, DNA/genomic truth, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/people/dna/README.md`](../../../quarantine/people/dna/README.md)
- [`../../../quarantine/people-dna-land/README.md`](../../../quarantine/people-dna-land/README.md)
- [`../../../processed/people-dna-land/README.md`](../../../processed/people-dna-land/README.md)
- [`../../../catalog/domain/people-dna-land/README.md`](../../../catalog/domain/people-dna-land/README.md)
- [`../../../published/layers/people-dna-land/README.md`](../../../published/layers/people-dna-land/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/architecture/directory-rules.md`](../../../../docs/architecture/directory-rules.md)
- [`../../../../docs/domains/people-dna-land/DNA_HANDLING.md`](../../../../docs/domains/people-dna-land/DNA_HANDLING.md)
- [`../../../../docs/domains/people-dna-land/SENSITIVITY.md`](../../../../docs/domains/people-dna-land/SENSITIVITY.md)
- [`../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md`](../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md)
- [`../../../../docs/domains/people-dna-land/sublanes/dna.md`](../../../../docs/domains/people-dna-land/sublanes/dna.md)
- [`../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md`](../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a People/DNA compatibility RAW lane for source capture only. It is not canonical domain authority, source-family doctrine, registry authority, consent authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, person identity truth, relationship truth, DNA/genomic truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
