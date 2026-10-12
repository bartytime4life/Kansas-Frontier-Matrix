<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/quarantine/people/dna/readme
name: People DNA Quarantine Compatibility README
path: data/quarantine/people/dna/README.md
type: data-quarantine-lane-readme; compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <dna-sublane-steward>
  - <data-steward>
  - <consent-reviewer>
  - <privacy-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: quarantine
responsibility_root: data/
requested_path_segment: people/dna
canonical_domain_candidate: people-dna-land
artifact_family: held-dna-genomic-material
sensitivity_posture: T4-default; fail-closed; no-public-path; raw-genotype-never-public; consent-required; revocation-required; release-blocked
related:
  - ../../README.md
  - ../../../README.md
  - ../../people-dna-land/README.md
  - ../../people-dna-land/land-ownership/README.md
  - ../../../../docs/domains/people-dna-land/CANONICAL_PATHS.md
  - ../../../../docs/domains/people-dna-land/DNA_HANDLING.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/people-dna-land/sublanes/dna.md
  - ../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - quarantine
  - people
  - dna
  - people-dna-land
  - compatibility-path
  - genomic
  - consent
  - revocation
  - privacy
  - deny-by-default
  - evidence-first
notes:
  - "This README documents the requested `data/quarantine/people/dna/` path as a compatibility quarantine lane, not canonical domain authority."
  - "Visible canonical-path doctrine uses `people-dna-land` as the confirmed domain segment; alternate `people` path forms are conflict/compatibility material unless an ADR says otherwise."
  - "DNA/genomic material is highest-sensitivity material in the domain: raw genotype is never public, kit/vendor identifiers must not leak, and consent/revocation checks fail closed."
  - "Quarantine is a hold state, not a shortcut to processed, catalog, triplet, published, reports, layers, PMTiles, stories, graph/vector indexes, generated answers, or public UI."
  - "Actual payload presence, parent `people/` README presence, policy automation, validator wiring, CI enforcement, review completion, and ADR resolution remain UNKNOWN unless verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People / DNA Quarantine Compatibility Lane

Compatibility hold lane for DNA, genomic, genetic-genealogy, consent, revocation, and DNA-derived evidence material associated with the People/DNA/Land domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: quarantine" src="https://img.shields.io/badge/lifecycle-quarantine-critical">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Canonical candidate: people-dna-land" src="https://img.shields.io/badge/canonical%20candidate-people--dna--land-6f42c1">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4%20default-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Canonical path warning](#canonical-path-warning) · [Scope](#scope) · [Repo fit](#repo-fit) · [Held material](#held-material) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/quarantine/people/dna/` is a no-public-path compatibility hold lane. Material here is not public, not processed truth, not catalog truth, not proof, not release authority, not policy authority, not consent authority, not person identity truth, not relationship truth, not DNA/genomic truth, not genealogy truth, and not generated-answer authority. Nothing in this subtree may be consumed by public clients or normal UI surfaces until a governed exit transition leaves inspectable evidence and the path question is resolved or explicitly bridged.

---

## Canonical path warning

Visible People/DNA/Land canonical-path doctrine identifies the confirmed domain segment as:

```text
people-dna-land
```

The nested path requested here is:

```text
data/quarantine/people/dna/
```

Treat this path as **compatibility / conflict-holding documentation** unless an accepted ADR or migration note explicitly authorizes `people/dna` as a lifecycle path. Do not create parallel schema, contract, policy, registry, proof, release, public-layer, graph, vector-index, or generated-answer authority from this nested compatibility path.

---

## Scope

This directory may hold DNA-related quarantine material only when the repository intentionally preserves the `people/dna` path as a compatibility bridge. It is governed by the stricter People/DNA/Land DNA handling rules.

Typical reasons for quarantine include:

- raw DNA/genomic data, kit/vendor identifiers, segment data, match evidence, or DNA-derived relationship support is present outside an approved encrypted/access-scoped lane;
- ConsentGrant, consent scope, retention term, audience, revocation state, or RevocationReceipt is missing, expired, contradicted, unreachable, or unresolved;
- DNA evidence is being treated as identity truth, relationship truth, title/ownership truth, or source authority rather than evidence;
- a relationship hypothesis, triangulation result, or genetic-genealogy inference is being presented as a confirmed person/genealogy claim without independent review;
- an aggregate or derived DNA statistic lacks aggregation/de-identification proof, review state, policy decision, correction path, or rollback target;
- a report, story, map, graph edge, search index, vector index, or generated answer could expose raw genotype, kit/vendor identifiers, segment detail, individual match evidence, living-person identity, or consent-restricted context;
- the path itself is being used to bypass the canonical `people-dna-land` lane.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/quarantine/people/dna/` |
| Responsibility root | `data/` |
| Lifecycle phase | `quarantine/` |
| Requested segment | `people/dna` |
| Working canonical candidate | `people-dna-land` |
| Segment status | **Compatibility / NEEDS ADR OR MIGRATION DECISION** |
| Artifact role | Held DNA/genomic and DNA-derived review material plus quarantine-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Exit posture | Only by explicit consent/privacy/source-role/evidence/policy/review closure and ADR-aware path handling |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/` and `data/receipts/`, not this directory |
| Catalog authority | `data/catalog/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Consent authority | `policy/consent/` or accepted consent-control lane, not this directory |
| Default failure posture | `HOLD`, `DENY`, `RESTRICT`, or `ABSTAIN` when consent, revocation, privacy, source role, rights, evidence, sensitivity, path authority, review, correction, rollback, or release support is insufficient |

---

## Held material

| Held family | Why it is held |
|---|---|
| Raw DNA/genomic packets | Raw genotype never crosses the publication boundary and must not become public or normal UI material. |
| Kit/vendor identifier packets | Vendor IDs, kit identifiers, and raw match identifiers must not leak outside governed restricted handling. |
| DNA match evidence | Match evidence supports hypotheses; it is not identity, relationship, or title truth. |
| Segment/triangulation candidates | Segment-level evidence is high sensitivity and requires consent, review, and strict access scoping. |
| Consent or revocation defects | Consent is required, scoped, current, and revocable; failed revocation checks fail closed. |
| DNA-derived relationship hypotheses | Hypotheses must not be collapsed into confirmed genealogy or person identity. |
| Aggregate derived candidates | Aggregates require documented privacy protection, review, release, correction, and rollback support before any public-safe use. |
| Generated or indexed carriers | Reports, stories, graph/vector/search indexes, and generated answers must not leak DNA or consent-restricted context. |

---

## Inputs

Accepted content is limited to held review material and quarantine-local sidecars: source references, consent notes, revocation notes, privacy notes, source-role notes, evidence notes, sensitivity notes, policy-decision drafts, receipt-closure checklists, digest sidecars, correction notes, rollback notes, and local README/index files.

Do not place raw genotype values, kit/vendor identifiers, segment coordinates, individual match details, or living-person genomic details in this README.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Canonical People/DNA/Land quarantine index | `data/quarantine/people-dna-land/` |
| Clean RAW DNA source material | Approved RAW/restricted/encrypted lane only; not public documentation |
| Ordinary WORK material that is safe to process | `data/work/people-dna-land/` or ADR-approved equivalent |
| Validated processed People/DNA/Land objects | `data/processed/people-dna-land/` only after quarantine resolution |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, triplet lanes, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Consent, revocation, redaction, aggregation, validation, or release receipts | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, or signatures | `release/` |
| Source descriptors, activation records, source registries, or registry truth | `data/registry/` |
| Public layers, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close and only for allowed public-safe derivatives |
| Person identity truth, genealogy truth, land/title truth, or property-rights truth | Owning People/DNA/Land sublane/root, not this compatibility path |
| Contracts, schemas, validators, policy rules, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `policy/`, `apps/`, or UI roots |

---

## Directory map

```text
data/quarantine/people/dna/
├── README.md
├── <hold_id>/
│   ├── quarantine_reason.md
│   ├── consent_review.notes.md
│   ├── revocation_review.notes.md
│   ├── privacy_review.notes.md
│   ├── source_role_review.notes.md
│   ├── policy_decision.draft.json
│   ├── receipt_closure.checklist.md
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain quarantine-local. It is not a public index, catalog record, release manifest, registry, graph edge source, layer/story/report pointer, search index, vector index, map source, person index, DNA index, genealogy authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay held | Any unresolved consent, revocation, privacy, source role, rights, sensitivity, evidence, validation, review, policy, correction, rollback, release, or path-authority question remains. |
| Deny | PolicyDecision says `DENY`; public/UI/generated-answer surfaces abstain or deny. |
| Restrict | PolicyDecision and ReviewRecord identify allowed audience, purpose, terms, consent state, revocation state, correction path, and rollback target. |
| Return to work | Hold reason is resolved, but normal validation, attribution, consent review, privacy review, source-role review, or EvidenceBundle work still remains. |
| Promote downstream | Only after required receipts, consent/revocation closure, source descriptors, validation closure, evidence closure, policy/review closure, correction path, rollback target, release support, and ADR-aware path decision exist. |

---

## Forbidden shortcuts

```text
data/quarantine/people/dna/
→ data/processed/people-dna-land/
→ data/catalog/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

is forbidden unless the appropriate governed transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the material belongs in this compatibility path rather than canonical `data/quarantine/people-dna-land/`.
- [ ] Confirm the path conflict or compatibility reason is recorded.
- [ ] Confirm consent, revocation, privacy, source role, rights, sensitivity, and evidence state.
- [ ] Confirm DNA evidence is not being treated as identity truth, relationship truth, title truth, or source authority.
- [ ] Confirm required receipts are present or explicitly marked missing.
- [ ] Confirm PolicyDecision, ReviewRecord where required, correction path, rollback target, and release-state handling before any exit.
- [ ] Confirm no public layer, report, story, API payload, graph edge, search index, vector index, or generated answer uses quarantined material.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested quarantine compatibility path boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| The parent `data/quarantine/people/README.md` was not found during this edit. | **CONFIRMED by GitHub contents API during this edit** |
| People/DNA/Land canonical-path doctrine identifies `people-dna-land` as the confirmed domain segment and treats alternate `people` forms as conflict/compatibility material. | **CONFIRMED by GitHub contents API during this edit** |
| DNA handling doctrine says raw genotype is never republished and only aggregate or k-anonymized derived data may cross the publication boundary under documented consent and review. | **CONFIRMED by GitHub contents API during this edit** |
| DNA sublane doctrine says DNA evidence is restricted by default, raw kit/vendor identifiers and raw genotype data never cross the publication boundary, and DNA evidence is not identity/relationship authority by itself. | **CONFIRMED by GitHub contents API during this edit** |
| Actual DNA quarantine payloads exist in this subtree. | **UNKNOWN** |
| Policy automation, validators, and CI checks enforce this exact compatibility lane. | **NEEDS VERIFICATION** |
| This README is proof, release, catalog, registry, policy, consent authority, person identity truth, relationship truth, DNA/genomic truth, genealogy truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../people-dna-land/README.md`](../../people-dna-land/README.md)
- [`../../people-dna-land/land-ownership/README.md`](../../people-dna-land/land-ownership/README.md)
- [`../../../../docs/domains/people-dna-land/CANONICAL_PATHS.md`](../../../../docs/domains/people-dna-land/CANONICAL_PATHS.md)
- [`../../../../docs/domains/people-dna-land/DNA_HANDLING.md`](../../../../docs/domains/people-dna-land/DNA_HANDLING.md)
- [`../../../../docs/domains/people-dna-land/SENSITIVITY.md`](../../../../docs/domains/people-dna-land/SENSITIVITY.md)
- [`../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md`](../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md)
- [`../../../../docs/domains/people-dna-land/sublanes/dna.md`](../../../../docs/domains/people-dna-land/sublanes/dna.md)
- [`../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md`](../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a People/DNA compatibility quarantine hold lane only. It is not source authority, proof authority, receipt authority, release authority, catalog authority, registry authority, policy authority, consent authority, person identity truth, relationship truth, DNA/genomic truth, genealogy truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
