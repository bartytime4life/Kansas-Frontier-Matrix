<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-joins-person-parcel-readme
title: tools/validators/joins/person-parcel README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-join-steward-plus-people-dna-land-steward-plus-land-ownership-steward-plus-privacy-steward-plus-consent-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: restricted-review; joins-validator; person-parcel; people-dna-land; land-ownership; living-person-deny-default; private-person-parcel-deny-default; consent-aware; title-sensitive; parcel-sensitive; release-gated; non-authoritative
owning_root: tools/
responsibility: shared Person-Parcel join validator routing lane under tools/validators/joins for checking person-to-parcel and person-to-land assertions, living-person status, consent posture, privacy posture, title sensitivity, assessor/tax/parcel source-role boundaries, parcel geometry caveats, land-instrument evidence references, person assertion evidence references, ownership interval posture, public-surface leakage, policy/review/release linkage, correction cascade, rollback support, and finite validation outcomes while deferring People/DNA/Land meaning, schemas, policy decisions, consent authority, evidence records, receipts, lifecycle data, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../_common/README.md
  - ../../identity/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../genealogy/README.md
  - ../../../../docs/domains/people-dna-land/README.md
  - ../../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../../../docs/domains/people-dna-land/sublanes/land_ownership.md
  - ../../../../contracts/domains/people-dna-land/README.md
  - ../../../../contracts/domains/people-dna-land/people/README.md
  - ../../../../contracts/domains/people-dna-land/land-ownership/README.md
  - ../../../../schemas/contracts/v1/domains/people-dna-land/README.md
  - ../../../../policy/domains/people-dna-land/
  - ../../../../policy/consent/people-dna-land/
  - ../../../../policy/sensitivity/people-dna-land/
  - ../../../../data/registry/sources/people-dna-land/README.md
  - ../../../../data/registry/sources/people-dna-land/land-ownership/README.md
  - ../../../../data/quarantine/people-dna-land/land-ownership/README.md
  - ../../../../data/catalog/domain/people-dna-land/land-ownership/README.md
  - ../../../../data/published/layers/people-dna-land/land-ownership/README.md
  - ../../../../data/proofs/
  - ../../../../data/receipts/people-dna-land/README.md
  - ../../../../data/receipts/
  - ../../../../release/people-dna-land/
  - ../../../../release/
notes:
  - "This README replaces an empty file at tools/validators/joins/person-parcel/README.md. It does not confirm executable validator code."
  - "People/DNA/Land is T4 deny-by-default for living-person fields, raw DNA segment data, private person-parcel joins, and DNA-derived hypotheses."
  - "Person assertions are evidence, not facts; assessor and tax records are administrative context, not title truth; parcel geometry is not boundary or title proof."
  - "Private person-parcel joins that expose or narrow a living person's holdings, residence, family connection, or land interest must fail closed unless consent, privacy, evidence, policy, review, release, correction, and rollback gates are explicitly closed."
  - "Validators enforce declared contracts, schemas, source roles, evidence posture, consent posture, privacy posture, policy references, and release readiness. They do not define People/DNA/Land meaning, create EvidenceBundles, decide consent, issue legal/title opinions, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/joins/person-parcel

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-person--parcel--join-critical)
![sensitivity](https://img.shields.io/badge/sensitivity-T4%20deny--by--default-critical)
![consent](https://img.shields.io/badge/consent-revocable-blueviolet)
![authority](https://img.shields.io/badge/authority-routing--lane-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/joins/person-parcel/` is the shared validator routing lane for person-to-parcel and person-to-land joins, with fail-closed defaults for living-person, consent, privacy, title-sensitive, parcel-sensitive, DNA/genealogy-derived, and public-surface exposure risks.

---

## Purpose

`tools/validators/joins/person-parcel/` exists to make person-parcel join validation visible under the shared `tools/validators/joins/` surface without moving People/DNA/Land meaning, land-ownership meaning, schemas, policy, consent decisions, evidence, receipts, fixtures, lifecycle data, or release authority into a validator folder.

The durable KFM question for this lane is:

> Does a person-parcel candidate preserve person assertion evidence, living-person and consent posture, land-instrument and parcel source roles, ownership interval uncertainty, assessor/tax administrative context, parcel-geometry caveats, title-sensitive boundaries, privacy policy, review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, search, tile, screenshot, embedding, or AI surfaces?

The answer should be a deterministic validation result or routing decision. This folder should not create person truth, owner truth, title truth, parcel-boundary truth, residence truth, genealogy truth, DNA truth, EvidenceBundles, receipts, proofs, PolicyDecisions, consent decisions, ReleaseManifests, public map layers, API payloads, AI answers, legal advice, title opinions, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/joins/person-parcel/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| People/DNA/Land domain doctrine | **CONFIRMED repo evidence / draft** | Domain README marks living-person, DNA, private person-parcel joins, and DNA-derived outputs as deny/restrict by default and evidence-bound. |
| Land-ownership contract lane | **CONFIRMED README / implementation NEEDS VERIFICATION** | Land ownership contracts state land-ownership claims remain evidence-bound assertions; assessor/tax records and parcel geometry are not title truth. |
| Quarantine land-ownership lane | **CONFIRMED README / behavior NEEDS VERIFICATION** | Quarantine README marks private person-parcel joins as deny-default and no-public-path when unresolved. |
| Published land-ownership layer lane | **CONFIRMED README / release artifacts NEEDS VERIFICATION** | Published layer README limits output to privacy-reviewed, public-safe derivatives and denies living-person, DNA, title, and legal leakage. |
| Executables, registry wiring, fixtures, schema bindings, policy bundles, consent-resolution behavior, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a runnable validator, test suite, receipt path, runtime route, consent engine, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Shared person-parcel join validation | `tools/validators/joins/person-parcel/` | Shared validator routing lane; does not define domain meaning or consent decisions. |
| People/DNA/Land domain doctrine | `docs/domains/people-dna-land/` | Human-facing doctrine, sensitivity posture, and lane boundaries. |
| People and land semantic contracts | `contracts/domains/people-dna-land/`, `contracts/domains/people-dna-land/land-ownership/`, `contracts/domains/people-dna-land/people/` | Contracts define meaning; validators check conformance. |
| Machine shape | `schemas/contracts/v1/domains/people-dna-land/` or accepted schema homes | Schemas define shape; this folder does not. |
| Consent, sensitivity, and domain policy | `policy/domains/people-dna-land/`, `policy/consent/...`, `policy/sensitivity/...`, or accepted policy homes | Validator reports gaps; does not decide consent or policy. |
| Source descriptors | `data/registry/sources/people-dna-land/`, `data/registry/sources/people-dna-land/land-ownership/` | Source role, rights, cadence, and caveat authority. |
| Quarantine and lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/published/` | Lifecycle authority stays in `data/`. |
| Evidence/proof support | `data/proofs/` | Validator checks references; does not create proof authority. |
| Receipts | `data/receipts/`, `data/receipts/people-dna-land/` | Receipts remain separate from validator docs. |
| Release decisions, correction, rollback, withdrawal | `release/`, `release/people-dna-land/` | Validator pass is not release approval. |
| Shared identity checks | `tools/validators/identity/` | Person, parcel, release, evidence, and public-safe IDs may need identity checks. |
| Generic cross-domain join invariants | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` | Shared anti-collapse and routing invariants. |

[Back to top](#top)

---

## Join invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Person assertion remains evidence-bound | Person identity, name, relationship, residence, and ownership assertions cite evidence, source role, date, confidence, review state, and uncertainty. | Person string or generated summary is treated as canonical person truth. |
| Living-person status fails closed | Living-person, likely living-person, unknown-living-status, minor, protected, or private-person cases deny/restrict by default. | Candidate proceeds to public or semi-public output without living-person review and policy support. |
| Consent is explicit and revocable | Consent state is scoped, current, recorded, revocation-aware, and tied to the intended use. | Consent is absent, stale, inherited, implied, unscoped, contradicted, revoked, or not traceable. |
| Parcel geometry is contextual | Parcel geometry carries source, vintage, version, caveat, precision, and non-title-boundary posture. | Geometry is treated as legal boundary, title proof, residence proof, or ownership proof. |
| Assessor/tax records remain administrative | Assessor and tax records stay administrative context, not title, ownership, heirship, residence, or legal conclusion. | Assessor/tax row is presented as title truth or person-parcel proof by itself. |
| Land instrument evidence remains source-role aware | Deed, patent, probate, court, mortgage, lien, easement, lease, tax, plat, survey, OCR, and modeled records keep source role and caveats. | Instrument context is collapsed into an unsupported ownership conclusion. |
| Ownership is interval-valued and uncertain | Ownership intervals carry source dates, effective/recording dates, conflict posture, uncertainty, correction path, and rollback target. | Candidate emits a bare owner label or absolute ownership statement. |
| DNA/genealogy does not strengthen parcel claims without gates | DNA, genealogy, probate, family-tree, or heirship links require explicit evidence, sensitivity, consent, review, and policy closure before any land use. | DNA/genealogy-derived claim narrows ownership or residence without gates. |
| Public surface is public-safe only | Public output is generalized, allowlisted, release-manifested, and free of living-person, DNA, private-residence, private-land, and title-sensitive leakage. | Map, popup, export, graph, search, Focus Mode, screenshot, embedding, or AI answer exposes unsafe person-parcel context. |
| Correction cascade is mandatory | Correction, withdrawal, revocation, stale source, source-rights change, or evidence invalidation propagates to downstream catalog, graph, release, tile, search, export, and AI carriers. | Downstream person-parcel derivative stays active after a blocking change. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Shared person-parcel join validator routing | `tools/validators/joins/person-parcel/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Shared identity validator routing | `tools/validators/identity/` |
| People/DNA/Land doctrine | `docs/domains/people-dna-land/` |
| People/DNA/Land semantic contracts | `contracts/domains/people-dna-land/` |
| Land-ownership contract orientation | `contracts/domains/people-dna-land/land-ownership/` |
| People contracts | `contracts/domains/people-dna-land/people/` |
| Machine schemas | `schemas/contracts/v1/domains/people-dna-land/` or accepted schema homes |
| Consent, sensitivity, domain, and release policy | `policy/`, accepted `policy/domains/`, `policy/consent/`, `policy/sensitivity/`, and release-policy homes |
| Source descriptors | `data/registry/sources/people-dna-land/` and accepted source registry homes |
| Lifecycle data | `data/raw/people-dna-land/`, `data/work/people-dna-land/`, `data/quarantine/people-dna-land/`, `data/processed/people-dna-land/`, `data/catalog/...`, `data/published/...` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/`, `data/receipts/people-dna-land/` |
| Release decisions, correction, rollback, withdrawal | `release/`, `release/people-dna-land/` |
| Tests and fixtures | `tests/validators/joins/person-parcel/`, `tests/domains/people-dna-land/`, `fixtures/domains/people-dna-land/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared person-parcel join invariants and delegates meaning, schemas, consent, policy, evidence, receipts, lifecycle data, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source descriptors, fixture shape, policy bundles, consent-state resolver, report destinations, receipt emission, runtime behavior, release integration, and CI wiring.
- **DENY:** using this folder as People/DNA/Land doctrine, schema home, policy home, consent authority, source registry, evidence store, lifecycle data store, proof store, receipt store, release record store, public runtime surface, title authority, legal advice surface, living-person truth surface, residence exposure surface, genealogy truth surface, DNA truth surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/joins/person-parcel/` include checks that:

- verify person-to-parcel links cite accepted person, land, instrument, and parcel EvidenceRefs;
- verify living-person and unknown-living-status joins fail closed unless policy and consent gates are closed;
- verify consent is scoped to the intended use, current, revocation-aware, and tied to the release candidate;
- verify assessor/tax records remain administrative context and are not used as title proof;
- verify parcel geometry carries source/vintage/version/caveat posture and is not used as boundary proof;
- verify person names, relationships, residences, family-tree assertions, probate links, DNA/genealogy hints, and ownership intervals keep source role and uncertainty visible;
- verify public outputs use field allowlists, redaction/generalization receipts, release manifests, correction paths, and rollback targets;
- verify correction, revocation, withdrawal, stale-source, or rights changes propagate downstream;
- emit deterministic validation findings for steward review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/joins/person-parcel/` | Correct home |
|---|---|
| People/DNA/Land doctrine or contracts | `docs/domains/people-dna-land/`, `contracts/domains/people-dna-land/` |
| Land-ownership semantic contracts | `contracts/domains/people-dna-land/land-ownership/` |
| Schemas, DTOs, enums, or join machine shape | `schemas/contracts/v1/...` |
| Consent rules, sensitivity rules, release gates, steward decisions, or hidden thresholds | `policy/...`, `release/` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, decisions, rollback cards, corrections, withdrawals | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, field-level publication, private/residence exposure, legal/title opinion, or AI runtime code | governed application/runtime roots or official/legal channels, not validator docs |
| Real living-person identifiers, private addresses, raw DNA data, private parcel/holding links, or reconstruction hints | denied here; keep out of repository-facing validator documentation |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `PERSON_PARCEL_JOIN_PASS` | Candidate passed configured person-parcel checks. |
| `PERSON_PARCEL_JOIN_FAIL` | Candidate failed one or more configured checks. |
| `PERSON_PARCEL_JOIN_DENY` | Candidate is denied because privacy, consent, sensitivity, source-role, rights, evidence, review, release, or public-surface risk cannot be resolved. |
| `PERSON_PARCEL_JOIN_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `PERSON_PARCEL_JOIN_ABSTAIN` | Candidate lacks enough evidence or policy support to assert the join. |
| `LIVING_PERSON_REVIEW_MISSING` | Living-person or unknown-living-status review is absent. |
| `CONSENT_STATE_MISSING` | Required scoped consent state is absent or unresolved. |
| `CONSENT_REVOKED` | Consent was revoked; downstream cleanup and rollback are required. |
| `PRIVATE_PERSON_PARCEL_JOIN_DENIED` | Candidate exposes or narrows a living person's holdings, residence, family connection, or land interest. |
| `PERSON_ASSERTION_EVIDENCE_MISSING` | Person identity, name, relationship, residence, or ownership assertion lacks accepted evidence support. |
| `PARCEL_GEOMETRY_AS_TITLE_DENIED` | Parcel geometry is treated as legal boundary, title proof, or ownership proof. |
| `ASSESSOR_TAX_AS_TITLE_DENIED` | Assessor/tax row is treated as title truth. |
| `OWNERSHIP_INTERVAL_UNSUPPORTED` | Ownership interval lacks source dates, role, uncertainty, evidence, correction, or rollback support. |
| `DNA_GENEALOGY_LAND_LINK_DENIED` | DNA/genealogy-derived link strengthens parcel/ownership inference without consent, review, and evidence closure. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Map, tile, popup, export, search, graph, Focus Mode, screenshot, embedding, or AI surface exposes unsafe person-parcel context. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, rollback target, or withdrawal path is absent. |
| `CORRECTION_CASCADE_MISSING` | Correction, revocation, withdrawal, stale state, rights change, or evidence invalidation did not propagate. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/joins/person-parcel/
├── README.md
├── validate_person_parcel_join.py       # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If `validate_person_parcel_join.py` is added, it should delegate domain meaning, schemas, consent, policy, evidence, fixtures, receipts, and release checks to accepted People/DNA/Land, identity, cross-domain, and shared validator homes. It should not redefine domain meaning, copy schemas, copy policy, store fixtures, write lifecycle data, decide consent, approve release, publish public outputs, or generate legal/title conclusions.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/joins/person-parcel/README.md`.
- [x] It marks this path as a shared person-parcel join validator routing lane, not People/DNA/Land authority, consent authority, policy authority, title authority, or release authority.
- [x] It preserves living-person deny/default posture, private person-parcel deny/default posture, consent/revocation, person assertions as evidence, assessor/tax administrative context, parcel geometry caveats, title sensitivity, evidence, policy, release, correction, rollback, and public-surface denial posture.
- [x] It routes machine shape, policy, consent, fixtures, evidence, receipts, release, lifecycle data, tests, and domain meaning to their owning roots.
- [x] It marks executable behavior, registry wiring, schema bindings, policy bundles, consent-state resolution, fixture files, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to `joins/person-parcel` are searched and classified.
- [ ] Accepted schema homes, policy homes, consent homes, fixture homes, test paths, and report destinations are verified.
- [ ] Tests exercise valid and invalid person assertions, living-person states, consent states, parcel geometry caveats, assessor/tax/title boundaries, ownership intervals, DNA/genealogy links, release gaps, correction cascades, and public-surface leakage cases.
- [ ] CI invokes the relevant person-parcel validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with shared person-parcel join validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
