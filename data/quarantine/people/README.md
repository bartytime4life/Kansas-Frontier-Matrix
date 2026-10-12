<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/quarantine/people/readme
name: People Quarantine Compatibility README
path: data/quarantine/people/README.md
type: data-quarantine-index-readme; compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <people-dna-land-domain-steward>
  - <people-compatibility-steward>
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
requested_path_segment: people
canonical_domain_candidate: people-dna-land
artifact_family: held-people-compatibility-material
sensitivity_posture: T4-default; fail-closed; no-public-path; living-person-deny-default; DNA-deny-default; consent-required; release-blocked
related:
  - dna/README.md
  - ../README.md
  - ../../README.md
  - ../people-dna-land/README.md
  - ../people-dna-land/land-ownership/README.md
  - ../../../docs/domains/people-dna-land/CANONICAL_PATHS.md
  - ../../../docs/domains/people-dna-land/DNA_HANDLING.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../docs/domains/people-dna-land/sublanes/dna.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - quarantine
  - people
  - people-dna-land
  - compatibility-path
  - living-person
  - dna
  - genealogy
  - consent
  - privacy
  - deny-by-default
  - evidence-first
notes:
  - "This README documents the requested `data/quarantine/people/` path as a compatibility quarantine index, not canonical domain authority."
  - "Visible canonical-path doctrine uses `people-dna-land` as the confirmed domain segment; alternate `people` path forms are conflict/compatibility material unless an ADR says otherwise."
  - "Confirmed child README lane in this path during this edit: `dna/`."
  - "People/DNA/Land material is high-sensitivity: living-person, DNA/genomic, consent, genealogy, private person-parcel, and land-ownership exposure fail closed by default."
  - "Actual payload presence, policy automation, validator wiring, CI enforcement, review completion, and ADR resolution remain UNKNOWN unless verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People Quarantine Compatibility Index

Compatibility parent index for held people-related material that appears under `data/quarantine/people/` while the canonical People/DNA/Land domain segment remains `people-dna-land`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: quarantine" src="https://img.shields.io/badge/lifecycle-quarantine-critical">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Canonical candidate: people-dna-land" src="https://img.shields.io/badge/canonical%20candidate-people--dna--land-6f42c1">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4%20default-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Canonical path warning](#canonical-path-warning) · [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Proposed compatibility classes](#proposed-compatibility-classes) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Forbidden shortcuts](#forbidden-shortcuts) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/quarantine/people/` is a no-public-path compatibility hold lane. Material here is not public, not processed truth, not catalog truth, not proof, not release authority, not policy authority, not consent authority, not person identity truth, not living-person truth, not DNA/genomic truth, not genealogy truth, not land/title truth, and not generated-answer authority. Nothing in this subtree may be consumed by public clients or normal UI surfaces until a governed exit transition leaves inspectable evidence and the path question is resolved or explicitly bridged.

---

## Canonical path warning

Visible People/DNA/Land canonical-path doctrine identifies the confirmed domain segment as:

```text
people-dna-land
```

The nested path requested here is:

```text
data/quarantine/people/
```

Treat this path as **compatibility / conflict-holding documentation** unless an accepted ADR or migration note explicitly authorizes `people` as a lifecycle domain segment. Do not create parallel schema, contract, policy, registry, proof, release, public-layer, graph, vector-index, or generated-answer authority from this compatibility path.

---

## Scope

This directory may hold people-related quarantine material only when the repository intentionally preserves the `people/` path as a compatibility bridge.

Typical reasons for quarantine include:

- a people, identity, genealogy, DNA, consent, revocation, privacy, land-ownership, or person-parcel artifact arrived under the alternate `people/` segment rather than the canonical `people-dna-land/` segment;
- living-person status, consent, revocation, privacy, source role, source rights, evidence support, sensitivity, validation, review, release state, correction path, or rollback target is unresolved;
- person identity candidates, relationship hypotheses, DNA evidence, land/title evidence, or private person-parcel joins are being collapsed into public truth;
- a report, story, map, graph edge, search index, vector index, API payload, or generated answer could expose restricted person, DNA, genealogy, consent, land, residence, or relationship context;
- the path itself is being used to bypass People/DNA/Land controls.

This parent lane does not make held content authoritative. It routes compatibility material so stewards can review, deny, restrict, migrate to the canonical lane, return to work, or promote only through governed lifecycle transitions.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/quarantine/people/` |
| Responsibility root | `data/` |
| Lifecycle phase | `quarantine/` |
| Requested segment | `people` |
| Working canonical candidate | `people-dna-land` |
| Segment status | **Compatibility / NEEDS ADR OR MIGRATION DECISION** |
| Artifact role | Parent compatibility hold lane for people-related quarantine material and quarantine-local review sidecars |
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

## Confirmed child lanes

The child lane below is a README path confirmed by current-session GitHub fetches or edits. This table does **not** prove held payloads exist under that lane.

| Child lane | Held material | Boundary |
|---|---|---|
| [`dna/`](dna/README.md) | DNA, genomic, genetic-genealogy, consent, revocation, and DNA-derived evidence material | Compatibility-only; no public path until consent/privacy/source-role/evidence closure, receipts, review, release, correction, rollback, and path decision exist. |

---

## Proposed compatibility classes

| Class | Status | Typical handling |
|---|---|---|
| People segment conflict | **PROPOSED / NEEDS VERIFICATION** | Keep non-authoritative until ADR or migration note resolves `people` versus `people-dna-land`. |
| Living-person exposure | **PROPOSED / NEEDS VERIFICATION** | Hold when identity, residence, family relation, contactability, or land relation could expose a living person. |
| Consent unresolved | **PROPOSED / NEEDS VERIFICATION** | Hold until consent, revocation, audience, purpose, retention, and correction path are resolved. |
| DNA/genomic restriction | **PROPOSED / NEEDS VERIFICATION** | Hold raw DNA, kit tokens, segment data, match evidence, and DNA-derived support unless allowed by strict consent/review gates. |
| Relationship hypothesis collapse | **PROPOSED / NEEDS VERIFICATION** | Preserve hypothesis status; do not collapse evidence into confirmed person or genealogy truth. |
| Private person-parcel join | **PROPOSED / NEEDS VERIFICATION** | Deny/restrict by default; public-safe path requires redaction/generalization, review, and receipt closure. |
| Evidence open | **PROPOSED / NEEDS VERIFICATION** | Build EvidenceBundle support or deny/abstain. |
| Generated/indexed leakage | **PROPOSED / NEEDS VERIFICATION** | Deny graph, vector, search, story, report, map, API, or generated-answer use until release gates close. |

---

## Inputs

Accepted content is limited to held review material and quarantine-local sidecars: source references, consent notes, revocation notes, privacy notes, source-role notes, evidence notes, sensitivity notes, policy-decision drafts, receipt-closure checklists, digest sidecars, correction notes, rollback notes, path-migration notes, and local README/index files.

Do not place raw genotype values, kit/vendor identifiers, individual match details, contactable living-person details, private residence details, or private person-parcel details in this README.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Canonical People/DNA/Land quarantine index | `data/quarantine/people-dna-land/` |
| Clean RAW person/DNA/source material | Approved RAW/restricted lane only; not public documentation |
| Ordinary WORK material that is safe to process | `data/work/people-dna-land/` or ADR-approved equivalent |
| Validated processed People/DNA/Land objects | `data/processed/people-dna-land/` only after quarantine resolution |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, triplet lanes, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Consent, revocation, redaction, aggregation, validation, or release receipts | `data/receipts/` |
| Release manifests, promotion decisions, correction records, rollback records, signatures | `release/` |
| Source descriptors, activation records, source registries, registry truth | `data/registry/` |
| Public layers, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close and only for allowed public-safe derivatives |
| Person identity truth, genealogy truth, DNA/genomic truth, land/title truth, or property-rights truth | Owning People/DNA/Land lane, not this compatibility path |
| Contracts, schemas, validators, policy rules, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `policy/`, `apps/`, or UI roots |

---

## Directory map

```text
data/quarantine/people/
├── README.md
├── dna/
│   └── README.md
├── <future-compatibility-sublane>/
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
| Migrate to canonical lane | Path decision says material belongs under `people-dna-land/`; move only with receipt or migration note preserving provenance. |
| Return to work | Hold reason is resolved, but normal validation, attribution, consent review, privacy review, source-role review, or EvidenceBundle work still remains. |
| Promote downstream | Only after required receipts, consent/revocation closure, source descriptors, validation closure, evidence closure, policy/review closure, correction path, rollback target, release support, and ADR-aware path decision exist. |

---

## Forbidden shortcuts

```text
data/quarantine/people/
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
- [ ] Confirm people, DNA, genealogy, land/title, and person-parcel evidence is not being overclaimed as public truth.
- [ ] Confirm required receipts are present or explicitly marked missing.
- [ ] Confirm PolicyDecision, ReviewRecord where required, correction path, rollback target, and release-state handling before any exit.
- [ ] Confirm no public layer, report, story, API payload, graph edge, search index, vector index, or generated answer uses quarantined material.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested parent quarantine compatibility path boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `data/quarantine/people/dna/README.md` exists as a confirmed child compatibility lane. | **CONFIRMED by GitHub contents API during this edit** |
| People/DNA/Land canonical-path doctrine identifies `people-dna-land` as the confirmed domain segment and treats alternate `people` forms as conflict/compatibility material. | **CONFIRMED by GitHub contents API during this edit** |
| DNA handling doctrine says raw genotype is never republished and only aggregate or k-anonymized derived data may cross the publication boundary under documented consent and review. | **CONFIRMED by GitHub contents API during this edit** |
| Actual People quarantine payloads exist in this subtree. | **UNKNOWN** |
| Policy automation, validators, and CI checks enforce this exact compatibility lane. | **NEEDS VERIFICATION** |
| This README is proof, release, catalog, registry, policy, consent authority, person identity truth, living-person truth, DNA/genomic truth, genealogy truth, land/title truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`dna/README.md`](dna/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../people-dna-land/README.md`](../people-dna-land/README.md)
- [`../people-dna-land/land-ownership/README.md`](../people-dna-land/land-ownership/README.md)
- [`../../../docs/domains/people-dna-land/CANONICAL_PATHS.md`](../../../docs/domains/people-dna-land/CANONICAL_PATHS.md)
- [`../../../docs/domains/people-dna-land/DNA_HANDLING.md`](../../../docs/domains/people-dna-land/DNA_HANDLING.md)
- [`../../../docs/domains/people-dna-land/SENSITIVITY.md`](../../../docs/domains/people-dna-land/SENSITIVITY.md)
- [`../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md`](../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md)
- [`../../../docs/domains/people-dna-land/sublanes/dna.md`](../../../docs/domains/people-dna-land/sublanes/dna.md)
- [`../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md`](../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a People compatibility quarantine hold index only. It is not source authority, proof authority, receipt authority, release authority, catalog authority, registry authority, policy authority, consent authority, person identity truth, living-person truth, DNA/genomic truth, genealogy truth, land/title truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
