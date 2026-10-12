<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-geology-borehole-rights-readme
title: tools/validators/geology/borehole_rights README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-geology-steward-plus-source-steward-plus-rights-steward-plus-sensitivity-reviewer-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; geology-validator; borehole-rights; well-log-rights; subsurface; exact-location-sensitive; resource-sensitive; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Geology borehole-rights validator lane for checking borehole, core, well-log, sample, private-well, geophysics, geochemistry, and subsurface source rights posture, source-role and authority limits, exact-location sensitivity, resource-targeting exposure, ownership/lease/permit/title anti-collapse, redaction/generalization receipt posture, EvidenceRef/EvidenceBundle linkage, source registry linkage, policy/review/release linkage, correction and rollback linkage, and public-surface denial checks while deferring Geology meaning, source registry authority, rights decisions, policy decisions, evidence records, proof records, receipts, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../../domains/geology/README.md
  - ../../cross-domain-joins/README.md
  - ../../facilities/README.md
  - ../../evidence/README.md
  - ../../citation/README.md
  - ../../evidence_bundle/README.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/geology/SENSITIVITY.md
  - ../../../../docs/domains/geology/SOURCE_LEDGER.md
  - ../../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../../docs/domains/geology/sublanes/natural_resources.md
  - ../../../../docs/runbooks/geology/SOURCE_REFRESH_RUNBOOK.md
  - ../../../../contracts/domains/geology/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/domains/geology/
  - ../../../../policy/sensitivity/geology/
  - ../../../../data/registry/sources/geology/
  - ../../../../data/registry/sensitivity/geology/
  - ../../../../data/proofs/geology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Geology validator evidence says exact borehole, core, well-log, private-well, sample, and extraction-targetable resource locations are sensitive by default and require public-safe transforms, review, evidence, policy, release, correction, and rollback support before public exposure."
  - "Geology policy evidence says exact borehole, sample, sensitive-resource, well-log, and private-well locations default to restricted or generalized public geometry, and unclear rights/source role/evidence/sensitivity/release blocks public promotion."
  - "Geology source-registry evidence says source admission records who may say what about Geology, in which role, under which rights, and at which sensitivity tier before connectors or watchers activate."
  - "This validator lane must not decide rights, certify ownership, title, lease, permit, reserve, production, resource value, extraction feasibility, public safety, or publication approval."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/geology/borehole_rights

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-borehole--rights--validator-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-exact--subsurface--deny--default-critical)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/geology/borehole_rights/` is the proposed validator lane for checking borehole, well-log, core, sample, private-well, and subsurface-source rights and exposure posture before any governed Geology use.

---

## Purpose

`tools/validators/geology/borehole_rights/` exists for Geology borehole/well-log/source-rights checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a borehole, core, well-log, private-well, sample, geophysical, geochemical, or subsurface-source candidate preserve source rights, source role, authority limits, exact-location sensitivity, resource-targeting exposure posture, ownership/lease/permit/title distinctions, EvidenceRef/EvidenceBundle support, policy/review state, release linkage, correction lineage, rollback target, and public-surface denial before it reaches catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Geology truth, source rights decisions, property/title truth, mineral-rights truth, lease truth, permit truth, reserve estimates, production truth, extraction guidance, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/geology/borehole_rights/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Per-domain Geology validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | The Geology validator index names boreholes, well logs, cores, subsurface observations, resource sensitivity, source-role posture, evidence, policy, release, correction, rollback, and public-surface denial as validator concerns. |
| Geology policy posture | **CONFIRMED in repo evidence / draft** | `docs/domains/geology/POLICY.md` states mixed-tier posture; exact borehole, sample, sensitive-resource, well-log, and private-well locations default to restricted/generalized public geometry and require transform/review/policy gates. |
| Geology source registry posture | **CONFIRMED in repo evidence / draft** | `docs/domains/geology/SOURCE_REGISTRY.md` is an admission/authority-control surface for who may say what about Geology, in which source role, under which rights and sensitivity tier, before connectors/watchers/layers activate. |
| Borehole-rights executable, accepted schemas, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a validator script, schema, fixture set, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home |
|---|---|
| Borehole-rights validator lane | `tools/validators/geology/borehole_rights/` |
| Per-domain Geology validator index | `tools/validators/domains/geology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Evidence and citation validation | `tools/validators/evidence/`, `tools/validators/evidence_bundle/`, `tools/validators/citation/` |
| Cross-domain joins | `tools/validators/cross-domain-joins/` |
| Geology meaning and contracts | `docs/domains/geology/`, `contracts/domains/geology/` |
| Geology source admission and rights posture | `docs/domains/geology/SOURCE_REGISTRY.md`, `data/registry/sources/geology/` |
| Geology sensitivity posture | `docs/domains/geology/POLICY.md`, `data/registry/sensitivity/geology/`, `policy/sensitivity/geology/` |
| Geology and source schemas | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/source/` |
| Policy/admissibility | `policy/domains/geology/`, `policy/sensitivity/geology/`, or accepted policy homes |
| Proofs, receipts, release | `data/proofs/geology/`, `data/proofs/`, `data/receipts/`, `release/` |

This README does not move, replace, or override those roots. It only defines where borehole-rights validation may be documented or implemented after verification.

[Back to top](#top)

---

## Proposed validation focus

Until executable behavior and field-level schemas are verified, this README treats the following as proposed validation concepts:

| Concept | Validator question | Must not be treated as |
|---|---|---|
| Source rights | Are license, access, redistribution, attribution, confidentiality, owner/operator restrictions, and derivative-use limits visible? | Public-use permission by default. |
| Source role | Is the source role and authority limit explicit for borehole, well-log, core, sample, geophysics, geochemistry, or private-well material? | Claim truth or publication approval. |
| Exact-location sensitivity | Is exact subsurface geometry restricted, generalized, redacted, aggregated, denied, or review-gated as required? | Public-safe geometry by default. |
| Well-log and borehole content | Are logs, depths, lithology, formations, sample intervals, and geophysical/geochemical readings rights- and sensitivity-scoped? | Engineering advice, drilling guidance, or resource certification. |
| Resource-targeting exposure | Could a point, interval, attribute, or derived layer enable extraction-targeting harm? | Public release without transform/review/policy gates. |
| Ownership/title/lease/permit boundary | Are property, mineral rights, lease, permit, production, reserve, and ownership claims kept distinct? | Title truth, mineral-rights truth, or legal determination. |
| Transform receipts | Are redaction, generalization, aggregation, or geometry suppression receipts present when public-bound? | A hidden untracked edit. |
| Evidence/release posture | Are EvidenceRefs, EvidenceBundles, review records, PolicyDecisions, ReleaseManifests, correction paths, and rollback targets present before public use? | Publication by validation alone. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Borehole-rights validator lane | `tools/validators/geology/borehole_rights/` |
| Geology validator index | `tools/validators/domains/geology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Geology doctrine and policy posture | `docs/domains/geology/` |
| Geology contracts | `contracts/domains/geology/` |
| Source descriptors and source admission records | `data/registry/sources/geology/` or accepted source-registry home |
| Sensitivity registry and policy | `data/registry/sensitivity/geology/`, `policy/domains/geology/`, `policy/sensitivity/geology/` |
| Source and geology schemas | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/geology/` |
| Evidence/proof support | `data/proofs/geology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/geology/borehole_rights/`, `tests/domains/geology/`, `fixtures/domains/geology/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared borehole-rights, source-role, rights, sensitivity, transform, evidence, policy, release, correction, and public-surface rules and writes reports/receipts only to accepted roots.
- **NEEDS VERIFICATION:** exact executable names, accepted schemas, source registry topology, rights vocabulary, sensitivity-tier binding, fixture shape, policy bundles, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Geology doctrine, rights authority, source registry, source payload storage, schema home, proof storage, receipt storage, policy home, release record store, mineral-rights authority, title authority, lease authority, permit authority, engineering authority, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/geology/borehole_rights/` include checks that:

- verify borehole, core, well-log, sample, private-well, geophysical, geochemical, and related subsurface candidates have source descriptors and rights posture before use;
- verify exact borehole/sample/private-well/resource-targetable coordinates fail closed unless public-safe transform, review, policy, release, correction, and rollback support exists;
- verify source-role and authority limits are visible and do not turn a source into ownership, lease, permit, reserve, production, or extraction authority;
- verify well-log content, depths, intervals, lithology, geochemistry, and geophysics do not expose restricted or proprietary detail beyond allowed use;
- verify redaction/generalization/aggregation receipts exist for public-bound derived geometry or summaries;
- verify occurrence, deposit, estimate, permit, production, reserve, reclamation, ownership, lease, and title claims remain distinct;
- emit deterministic findings for downstream review without storing source payloads, proof artifacts, or approving release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/geology/borehole_rights/` | Correct home |
|---|---|
| Geology doctrine, object-family meaning, or policy prose | `docs/domains/geology/`, `contracts/domains/geology/` |
| SourceDescriptor records or source registry records | `data/registry/sources/geology/` |
| Borehole, well-log, core, private-well, sample, geophysics, or geochemistry payloads | dedicated `data/` lifecycle roots with quarantine/review as needed |
| Rights decisions, sensitivity decisions, policy bundles | `policy/`, `data/registry/sensitivity/geology/`, or accepted policy/sensitivity homes |
| Schemas and controlled vocabularies | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/geology/` |
| EvidenceBundles, proofs, receipts, validation reports, redaction receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, correction notices, rollback cards, withdrawals | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Connectors, parsers, ETL, source refreshers, or model runners | `connectors/`, `pipelines/`, `packages/`, or accepted implementation roots |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime output, extraction guidance, legal/title/lease/permit determinations, engineering recommendations, or publication output | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Borehole-rights validator posture

Borehole-rights validators must fail closed, deny, abstain, hold, or route to review when a candidate:

- lacks source descriptor linkage, source role, source family, rights posture, sensitivity tier, location posture, EvidenceRef, EvidenceBundle/proof reference, policy posture, review state, release reference, correction path, or rollback target required for its use;
- exposes exact borehole, core, sample, well-log, private-well, sensitive-resource, or extraction-targetable location without approved public-safe transform and receipt support;
- lacks rights clearance for copying, deriving, summarizing, redistributing, displaying, exporting, embedding, or using well-log/subsurface material;
- treats source admission, public availability, agency publication, stable identifier, or successful ingestion as rights clearance, evidence closure, or release approval;
- collapses occurrence, deposit, estimate, permit, production, reserve, reclamation, lease, title, ownership, and parcel claims;
- treats borehole or well-log validation as drilling guidance, engineering advice, mineral-rights confirmation, lease determination, title determination, resource certification, reserve estimate, production estimate, or extraction recommendation;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on rights-incomplete or sensitivity-incomplete borehole candidates;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, restricted well-log payloads, or incomplete proof closure;
- treats borehole-rights validation as SourceDescriptor creation, EvidenceBundle creation, rights approval, PolicyDecision creation, release approval, publication, public API behavior, or AI answer authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `BOREHOLE_RIGHTS_PASS` | Configured borehole-rights checks passed. |
| `BOREHOLE_RIGHTS_FAIL` | One or more configured borehole-rights checks failed. |
| `BOREHOLE_SOURCE_DESCRIPTOR_MISSING` | Required SourceDescriptor or source-registry pointer is absent. |
| `BOREHOLE_SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `BOREHOLE_RIGHTS_GAP` | Rights, license, attribution, redistribution, access, or derivative-use posture is incomplete. |
| `BOREHOLE_SENSITIVITY_TIER_MISSING` | Sensitivity tier or public-use posture is absent. |
| `BOREHOLE_EXACT_LOCATION_DENIED` | Exact borehole/core/sample/well/private-well/resource-targetable geometry is unsafe for the requested surface. |
| `BOREHOLE_REDACTION_RECEIPT_MISSING` | Required redaction, generalization, aggregation, or geometry-suppression receipt is absent. |
| `BOREHOLE_RESTRICTED_CONTENT_DENIED` | Restricted or proprietary well-log/subsurface content is unsafe for the requested surface. |
| `BOREHOLE_RESOURCE_TARGETING_RISK` | Candidate could enable extraction-targeting harm or sensitive resource exploitation. |
| `GEOLOGY_CLAIM_CLASS_COLLAPSE` | Occurrence, deposit, estimate, permit, production, reserve, reclamation, ownership, lease, title, or parcel claims are collapsed. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `DENY` | Candidate is explicitly disallowed for the requested use. |
| `HOLD` | Candidate requires steward review, rights clearance, source admission, evidence closure, quarantine, or release closure before use. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/geology/borehole_rights/
├── README.md
├── test_borehole_rights_validator.py
└── fixtures/
    ├── valid_generalized_public_borehole_summary/
    ├── missing_source_descriptor/
    ├── missing_rights_posture/
    ├── missing_sensitivity_tier/
    ├── exact_location_denied/
    ├── missing_redaction_receipt/
    ├── restricted_well_log_content_denied/
    ├── resource_targeting_risk/
    ├── claim_class_collapse/
    └── policy_or_release_gap/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/geology/borehole_rights
```

```bash
python tools/validators/geology/borehole_rights/validate_borehole_rights.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_borehole_rights.py` or the test path exists here.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Geology contracts, schemas, source descriptors, rights posture, sensitivity posture, policy, evidence records, release records, and correction/rollback records rather than defining meaning locally.
- [ ] Exact borehole, core, well-log, sample, private-well, and extraction-targetable geometry fails closed unless public-safe transform and receipt support exists.
- [ ] Rights posture is explicit before copying, deriving, summarizing, redistributing, displaying, exporting, embedding, or public use.
- [ ] Occurrence, deposit, estimate, permit, production, reserve, reclamation, lease, title, ownership, and parcel claims remain distinct.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, direct model outputs, stale source descriptors, restricted well-log payloads, rights-incomplete candidates, or incomplete proof closure.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, rights approval, policy approval, release, publication, source admission, mineral-rights authority, title authority, lease authority, permit authority, reserve estimate, engineering authority, extraction guidance, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Geology borehole-rights validator file. |
| Next smallest safe change | Verify actual borehole-rights validator script path, accepted Geology/source schemas, source registry topology, rights vocabulary, sensitivity-tier binding, fixtures, report destination, receipt emission, policy enforcement, release linkage, and CI/runtime wiring before promoting this lane beyond draft. |
