<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/people/dna/readme
title: People DNA Raw Compatibility README
path: data/raw/people/dna/README.md
type: data-raw-lane-readme
secondary_type: compatibility-lane-readme
version: v0.2.0
prior_version: v0.1.0
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
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked People/DNA RAW compatibility and reference documentation, including its deny-by-default consent and privacy rules, without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
requested_path_segment: people/dna
canonical_domain_candidate: people-dna-land
artifact_family: dna-genomic-raw-compatibility-reference
sensitivity_posture: T4-default; fail-closed; no-public-path; encrypted-access-scoped; raw-genotype-never-public; consent-required; revocation-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../people-dna-land/README.md
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
  - compatibility-reference
  - source-first
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/people/dna/README.md`."
  - "At the v0.1.0 edit, parent `data/raw/people/README.md` contained placeholder content only; it now carries a People compatibility/reference index."
  - "Visible People/DNA/Land doctrine treats DNA/genomic material as highest-sensitivity, deny-by-default material; raw genotype is never public."
  - "The requested `people/dna` path is documented as a compatibility RAW lane, not a new canonical domain authority root."
  - "Payload presence, encryption/storage implementation, ConsentGrant records, RevocationReceipt records, SourceDescriptor records, policy automation, validators, fixtures, CI checks, review controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People / DNA RAW Compatibility Lane

Compatibility and reference lane for legacy DNA-, genomic-, genetic-genealogy-, consent-, revocation-, and DNA-derived-evidence-facing RAW documentation associated with the People/DNA/Land domain; not a physical source-capture home.

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
> `data/raw/people/dna/` is a no-public-path, deny-by-default compatibility/reference lane inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this subtree is not a default physical capture home and must not receive duplicate RAW payloads, DNA/genomic exports, raw kit/vendor identifiers, or capture sidecars. It is not processed truth, catalog truth, proof, receipt authority, consent authority, policy authority, release authority, person identity truth, relationship truth, DNA/genomic truth, public UI/API material, graph/vector-index authority, or generated-answer authority.

---

## Canonical path warning

Directory Rules state that file placement encodes ownership, governance, and lifecycle, and topic alone does not justify a root folder. Visible People/DNA/Land doctrine uses `people-dna-land` as the current domain candidate, while this requested path uses nested `people/dna`.

Treat this path as a **compatibility/reference lane** unless an accepted ADR or migration note explicitly authorizes `people/dna` as a canonical lifecycle path. Even then, accepted Directory Rules rule `DIR-SOURCE-001` keeps capture identity source-first; a domain path name does not establish physical RAW placement. Do not create parallel schema, contract, policy, registry, proof, release, public-layer, graph, vector-index, or generated-answer authority from this nested compatibility path.

---

## Scope

This directory documents DNA-related RAW handling and legacy domain-scoped topology only when the repository intentionally preserves the `people/dna` path as a compatibility bridge. It may reference one governed source-first capture, but it does not establish where that capture is stored. It is governed by the stricter People/DNA/Land DNA handling rules, and those rules apply in full to any source-first capture it references.

The sibling [`data/raw/people-dna-land/`](../../people-dna-land/README.md) index documents the same People/DNA/Land domain candidate. Both lanes must reference the same single source-first capture for any shared upstream source, never two copies.

In scope for the governed source-first capture (and for the references this lane may document), subject to consent, rights, storage, access, and review controls:

- direct-to-consumer DNA/genomic exports or references;
- DNA match evidence and DNA segment evidence or references;
- DNAKitToken sidecars or tokenized references, never public vendor identifiers;
- consent, revocation, retention, audience, redaction-profile, and rights sidecars;
- source-admission records needed to decide whether material remains at the source-first RAW home, moves to WORK, moves to QUARANTINE, or is rejected.

The governed source-first capture records what was captured, where it came from, who may govern it, what consent scope applies, which revocation state applies, what identifiers were tokenized, and what caveats must travel downstream. RAW does not prove identity, relationship, ancestry, title, ownership, person status, or publication readiness.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/people/dna/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Requested segment | `people/dna` |
| Canonical domain candidate | `people-dna-land` |
| Lane type | Compatibility RAW lane for DNA/genomic documentation |
| Artifact role | Compatibility/reference lane for DNA-facing documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed People/DNA/Land WORK (`data/work/people-dna-land/`) or QUARANTINE (`data/quarantine/people/dna/` / `data/quarantine/people-dna-land/`) procedures consume references or approved handoffs, not assumed domain-local copies, after governed triage |
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
| Capture identity is source-first | Register one `source_id` and preserve one immutable, access-scoped capture identity; domain references may support People/DNA/Land without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/people/dna/` as the capture home. Use only an accepted writer/path contract; none is established by this README. |
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

Accepted content in this subtree is limited to documentation and governed references that do not duplicate source-first captures:

- this README;
- links to canonical SourceDescriptor, source-admission, consent, revocation, rights, sensitivity, and policy authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape, never raw genotype, raw kit/vendor identifiers, or DNA payloads themselves;
- migration or correction notes that label legacy topology without moving or copying payloads;
- local README documentation that helps a steward understand capture state without becoming proof, consent authority, catalog, registry, policy, release, public artifact, or answer authority.

The governed source-first capture or reference (never a duplicate in this subtree) must carry, subject to consent, encryption/access scope, and review:

- source-reference manifests;
- raw payload references or encrypted/access-scoped raw payload pointers;
- admission-ticket references and SourceDescriptor references;
- ConsentGrant, consent-scope, retention, audience, revocation, redaction-profile, and rights references;
- tokenization sidecars for kit/vendor identifiers;
- source identity, source role, source time, retrieval time, vendor/source family, citation, attribution, rights posture, review notes, digest sidecars, and caveats.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support People/DNA. This includes DNA/genomic exports, match or segment files, raw kit/vendor identifiers, consent or revocation records, and tokenization sidecars. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a source directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

The earlier sketch of `intake/<source_or_run_id>/` (`source_reference.json`, `consent_ref.json`, `revocation_ref.json`, `rights_ref.json`, `checksums.sha256`, `README.md`) and `tokenized-references/<source_or_run_id>/` (`source_reference.json`, `tokenization_ref.json`, `consent_scope_ref.json`, `checksums.sha256`, `README.md`) is a proposed shape for a future accepted source-first home, not this subtree; any such home remains encrypted/access-scoped, consent- and revocation-bound, and deny-by-default. An optional RAW-local index there would be RAW-local only. It would not be a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This lane may retain a governed reference only. |
| Quarantine | Consent, revocation, rights, living-person status, source role, tokenization, storage posture, path authority, physical placement, or review state is unresolved. |
| Reject / erase | Consent is absent, revoked, expired, out of scope, or source retention is not permitted; rejection or erasure occurs through the owning source-first or quarantine procedure and must reach every reference. |
| Move to work | A governed reference or approved handoff may enter People/DNA/Land WORK only when consent, revocation, rights, source role, tokenization, storage/access posture, citation, hash, and review support are sufficient. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with inspectable evidence, consent/revocation checks, aggregation or redaction proof where applicable, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/people-dna-land/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence. Raw genotype material does not cross the publication boundary.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second People/DNA-scoped copy.
- [ ] Treat this README as compatibility/reference documentation only, not a new canonical authority root; do not create a child directory as a payload destination.
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
| Parent `data/raw/people/README.md` contained placeholder content only at the v0.1.0 edit. | **CONFIRMED by GitHub contents API during the v0.1.0 edit; superseded — the parent now carries a People compatibility/reference index** |
| Directory Rules say placement encodes ownership, governance, and lifecycle; topic alone does not justify a root folder. | **CONFIRMED by GitHub contents API during this edit** |
| People/DNA/Land doctrine says raw genotype is never republished and only aggregate or k-anonymized derived data may cross the publication boundary under documented consent and review. | **CONFIRMED by GitHub contents API during this edit** |
| DNA sublane doctrine says raw kit/vendor identifiers and raw genotype data never cross the publication boundary, and DNA evidence does not become relationship authority by itself. | **CONFIRMED by GitHub contents API during this edit** |
| Actual DNA RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction** — no payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| `data/raw/people-dna-land/` documents the same domain candidate; both lanes must reference one source-first capture, never two copies. | **CONFIRMED sibling README at `main@9e8bf3e6`** |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| Encryption/storage implementation, ConsentGrant records, RevocationReceipt records, SourceDescriptor records, policy automation, validators, fixtures, CI checks, review controls, and release readiness are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, consent authority, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, person identity truth, relationship truth, DNA/genomic truth, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../people-dna-land/README.md`](../../people-dna-land/README.md)
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

KFM rule: this directory is a People/DNA-facing compatibility/reference lane under deny-by-default consent, revocation, and privacy rules. One governed source-first capture may support People/DNA/Land without duplicated RAW bytes; this subtree does not establish physical placement. It is not canonical domain authority, source-family doctrine, registry authority, consent authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, person identity truth, relationship truth, DNA/genomic truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
