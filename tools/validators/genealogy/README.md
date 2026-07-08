<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-genealogy-readme
title: tools/validators/genealogy README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-people-dna-land-steward-plus-genealogy-steward-plus-consent-steward-plus-sensitivity-reviewer-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; genealogy-validator; people-dna-land; assertion-first; living-person; DNA-adjacent; consent-aware; source-role-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed shared Genealogy validator lane for checking assertion-first person and relationship claims, FamilySearch/GEDCOM/vital-record source-role posture, candidate-vs-observed anti-collapse, living-person and DNA-adjacent deny-by-default posture, consent/revocation linkage, EvidenceRef/EvidenceBundle linkage, source registry linkage, policy/review/release linkage, correction and rollback linkage, public-safe overlay posture, and public-surface denial checks while deferring People/DNA/Land meaning, source registry authority, consent decisions, evidence records, policy decisions, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../citation/README.md
  - ../evidence/README.md
  - ../evidence_bundle/README.md
  - ../domains/people-dna-land/README.md
  - ../cross-domain-joins/README.md
  - ../../../docs/domains/people-dna-land/sublanes/genealogy.md
  - ../../../docs/domains/people-dna-land/README.md
  - ../../../docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../../docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md
  - ../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - ../../../docs/sources/catalog/familysearch/family-tree.md
  - ../../../docs/sources/catalog/familysearch/historical-record-images.md
  - ../../../docs/sources/catalog/familysearch/README.md
  - ../../../contracts/domains/people-dna-land/
  - ../../../contracts/domains/people-dna-land/people/README.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/domains/people-dna-land/
  - ../../../policy/sensitivity/people-dna-land/
  - ../../../policy/consent/people-dna-land/
  - ../../../data/registry/sources/people-dna-land/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Genealogy sublane evidence says genealogy governs assertion-first lineage evidence and that every relationship is an assertion with evidence and confidence, never a sovereign fact."
  - "Genealogy evidence says living-person and DNA-derived outputs are denied or restricted by default and require explicit, scoped, revocable consent."
  - "FamilySearch Family Tree evidence says community-contributed tree nodes and person records are candidate hypotheses, not observations; publication is forbidden until merged and corroborated by an observation-role source."
  - "This validator lane must not define person identity, create genealogy truth, create SourceDescriptors, create EvidenceBundles, decide consent, decide policy, approve release, expose living-person/DNA/private-family graph detail, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/genealogy

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-genealogy--validator-informational)
![posture](https://img.shields.io/badge/posture-assertion--first-success)
![sensitivity](https://img.shields.io/badge/sensitivity-living%20%2B%20DNA%20deny--default-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/genealogy/` is the proposed shared validator lane for checking genealogy claims as evidence-bound assertions, not sovereign person, relationship, lineage, DNA, land, or living-person truth.

---

## Purpose

`tools/validators/genealogy/` exists for genealogy validation concerns under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a genealogy candidate preserve assertion-first person identity, relationship hypothesis posture, source-role separation, FamilySearch/GEDCOM/vital-record provenance, living-person and DNA-adjacent sensitivity, consent and revocation state, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create person truth, relationship truth, lineage truth, DNA truth, consent validity, title truth, SourceDescriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public graph layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/genealogy/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Per-domain People/DNA/Land validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The domain validator index names person assertions, genealogy relationships, consent, revocation, DNA, land, source-role separation, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Genealogy sublane doctrine | **CONFIRMED in repo evidence / draft** | The sublane doc says genealogy is assertion-first, evidence-bound, privacy-aware, and default-deny for living persons and DNA-derived inference. It also records an unresolved sublane-placement ADR question. |
| FamilySearch Family Tree source posture | **CONFIRMED in repo evidence / draft** | The source page says Family Tree records are community-contributed candidate hypotheses, not observations, and publication is forbidden until merged and corroborated by an observation-role source. |
| Genealogy executable, schemas, fixtures, consent bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, consent-registry integration, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Shared genealogy validator lane | `tools/validators/genealogy/` |
| Per-domain People/DNA/Land validator index | `tools/validators/domains/people-dna-land/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Citation/evidence validation | `tools/validators/citation/`, `tools/validators/evidence/`, `tools/validators/evidence_bundle/` |
| Cross-domain joins | `tools/validators/cross-domain-joins/` |
| Genealogy doctrine / sublane docs | `docs/domains/people-dna-land/sublanes/genealogy.md` |
| People/DNA/Land domain meaning | `docs/domains/people-dna-land/`, `contracts/domains/people-dna-land/` |
| FamilySearch source catalog posture | `docs/sources/catalog/familysearch/`, `data/registry/sources/people-dna-land/` |
| SourceDescriptor machine shape | `schemas/contracts/v1/source/` |
| People/DNA/Land schemas | `schemas/contracts/v1/domains/people-dna-land/` or ADR-selected schema home |
| Consent, sensitivity, and publication policy | `policy/consent/people-dna-land/`, `policy/sensitivity/people-dna-land/`, `policy/domains/people-dna-land/` |
| Proofs, receipts, release | `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where shared genealogy validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Assertion-first identity | Is every person, relationship, life event, family group, or lineage claim marked as an assertion with source, evidence, confidence, and review posture? | Sovereign person or relationship truth. |
| Source-role separation | Are candidate, observed, regulatory/administrative, aggregate, modeled, and synthetic roles distinct? | A family tree as observed event history. |
| FamilySearch Family Tree posture | Are community-contributed tree nodes treated as candidate hypotheses until merged and corroborated? | Observation-role evidence by default. |
| GEDCOM posture | Is GEDCOM treated as RAW/input evidence carrier only? | Public graph, canonical identity, or direct map/API payload. |
| Living-person sensitivity | Are living-person names, relationships, residences, contact info, family graph edges, and identifiers denied or consent/review-gated? | Public historical fact by default. |
| DNA-adjacent posture | Are DNA-derived hypotheses, match links, haplogroups, segment references, and triangulation hints restricted or denied unless consent/policy gates close? | Genealogy proof or public identity evidence. |
| Consent and revocation | Are consent scope, duration, delegation, withdrawal, tombstone/embargo, cache invalidation, graph/search/vector/AI withdrawal, correction, and rollback visible where required? | Permanent permission. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, review records, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Genealogy validator lane | `tools/validators/genealogy/` |
| Shared validator plumbing | `tools/validators/_common/` |
| People/DNA/Land validator index | `tools/validators/domains/people-dna-land/` |
| Genealogy and People/DNA/Land doctrine | `docs/domains/people-dna-land/` |
| Domain contracts | `contracts/domains/people-dna-land/` or accepted contract home |
| Source descriptors | `data/registry/sources/people-dna-land/` or accepted source registry home |
| Schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/people-dna-land/`, or ADR-selected schema homes |
| Consent and sensitivity policy | `policy/consent/people-dna-land/`, `policy/sensitivity/people-dna-land/`, `policy/domains/people-dna-land/` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/genealogy/`, `tests/domains/people-dna-land/`, `fixtures/domains/people-dna-land/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared genealogy, source-role, consent, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source registry topology, consent registry behavior, fixture shape, policy bundles, report destinations, receipt emission, release integration, graph/search/vector/AI withdrawal behavior, runtime behavior, and CI wiring.
- **DENY:** using this folder as genealogy doctrine, person identity authority, relationship truth authority, DNA authority, consent authority, source registry, source payload storage, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/genealogy/` include checks that:

- verify genealogy candidates are represented as assertions with evidence, confidence, source-role, review, and caveat posture;
- verify FamilySearch Family Tree records remain candidate hypotheses until disposition and corroboration gates close;
- verify GEDCOM and tree-upload inputs are treated as RAW/input carriers, not public identities or direct graph/map payloads;
- verify vital, census, cemetery, church, school, military, court, probate, obituary, directory, and similar records keep source-role and evidence boundaries visible;
- verify living-person data and DNA-adjacent claims fail closed unless scoped consent, review, policy, release, correction, and rollback support exist;
- verify revocation cascades can affect downstream cache, graph, search, vector, AI, overlay, correction, and rollback surfaces where applicable;
- emit deterministic findings for downstream review without storing proof artifacts or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/genealogy/` | Correct home |
|---|---|
| Genealogy doctrine or People/DNA/Land meaning | `docs/domains/people-dna-land/`, `contracts/domains/people-dna-land/` |
| Person, relationship, life-event, family-group, DNA, or land schemas | `schemas/contracts/v1/domains/people-dna-land/` or accepted schema homes |
| SourceDescriptor records or source registry records | `data/registry/sources/people-dna-land/` |
| Genealogy source payloads, GEDCOMs, FamilySearch responses, private tree exports | dedicated `data/` lifecycle roots with quarantine/review as needed |
| Consent records, revocation records, consent receipts | accepted consent/policy/receipt roots |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Policy rules and sensitivity/admissibility decisions | `policy/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, or public family-tree output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Genealogy validator posture

Genealogy validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, assertion ID, claim scope, confidence/review posture, EvidenceRef, EvidenceBundle/proof reference, consent posture, sensitivity posture, policy posture, release reference, correction path, or rollback target required for its use;
- treats a family tree, GEDCOM, community-contributed node, merged profile, or stable upstream identifier as sovereign person or relationship truth;
- treats candidate genealogy claims as observed event evidence without corroborating observation-role sources;
- exposes living-person names, relationships, residences, contact data, identifiers, family graph edges, private notes, or private tree metadata without consent/review/policy/release support;
- exposes DNA-derived relationship hypotheses, raw DNA, segment data, triangulation hints, haplogroup/match links, or genomic-adjacent inference without explicit, scoped, revocable consent and public-safe transform support;
- collapses genealogy with land/title truth, parcel-boundary truth, archaeology/burial sensitivity, tribal/cultural sensitivity, or DNA authority;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on unvalidated or unsupported genealogy assertions;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, revoked consent, or incomplete proof closure;
- treats genealogy validation as SourceDescriptor creation, EvidenceBundle creation, consent approval, PolicyDecision creation, release approval, publication, public API behavior, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `GENEALOGY_VALIDATOR_PASS` | Configured genealogy checks passed. |
| `GENEALOGY_VALIDATOR_FAIL` | One or more configured genealogy checks failed. |
| `GENEALOGY_ASSERTION_MISSING` | Required assertion identity, scope, or claim wrapper is absent. |
| `GENEALOGY_SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source-registry pointer is absent. |
| `GENEALOGY_SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `GENEALOGY_CANDIDATE_AS_OBSERVED_DENIED` | Candidate tree/profile data is treated as observed event evidence. |
| `GENEALOGY_CORROBORATION_MISSING` | Candidate or merged relationship lacks required corroborating observation-role evidence. |
| `GEDCOM_AS_PUBLIC_PAYLOAD_DENIED` | GEDCOM or private tree export is exposed as a public payload. |
| `LIVING_PERSON_CONSENT_GAP` | Living-person data lacks required consent, review, policy, release, correction, or rollback support. |
| `DNA_ADJACENT_DENIED` | DNA-derived or genomic-adjacent inference is unsafe for the requested surface. |
| `REVOCATION_STATE_GAP` | Consent revocation, tombstone, embargo, invalidation, correction, or rollback posture is incomplete. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `GENEALOGY_AUTHORITY_COLLAPSE` | Person, relationship, DNA, land, title, parcel, cultural, or burial authority is collapsed. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, source admission, consent closure, evidence closure, or quarantine before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/genealogy/
├── README.md
├── test_genealogy_validator.py
└── fixtures/
    ├── valid_public_historical_assertion/
    ├── candidate_as_observed_denied/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── missing_corroboration/
    ├── gedcom_as_public_payload_denied/
    ├── living_person_consent_gap/
    ├── dna_adjacent_denied/
    ├── revocation_state_gap/
    └── public_surface_leak_risk/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/genealogy
```

```bash
python tools/validators/genealogy/validate_genealogy.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_genealogy.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared People/DNA/Land contracts, schemas, source descriptors, source-role rules, consent policy, sensitivity policy, and evidence records rather than defining meaning locally.
- [ ] Genealogy claims remain assertion-first and evidence-bound.
- [ ] Candidate family-tree records do not become observation-role evidence without corroboration.
- [ ] GEDCOM and private tree exports are not exposed as public payloads.
- [ ] Living-person and DNA-adjacent outputs fail closed unless explicit, scoped, revocable consent and public-safe transform support exists.
- [ ] Revocation propagates to downstream cleanup, tombstone/embargo, cache invalidation, graph/search/vector/AI withdrawal, correction, and rollback targets where applicable.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, revoked consent, unsupported relationship hypotheses, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source admission, consent authority, genealogy authority, DNA authority, title authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Genealogy validator file. |
| Next smallest safe change | Verify actual genealogy validator script path, accepted People/DNA/Land schemas, FamilySearch/GEDCOM source descriptor shapes, consent and revocation integration, fixtures, report destination, receipt emission, policy enforcement, release linkage, graph/search/vector/AI withdrawal behavior, and CI/runtime wiring before promoting this lane beyond draft. |
