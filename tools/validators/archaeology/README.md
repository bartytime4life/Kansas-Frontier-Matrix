<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-archaeology-readme
title: tools/validators/archaeology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-archaeology-steward-plus-sensitivity-reviewer-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; archaeology-validator-lane; sensitive-domain; fail-closed
owning_root: tools/
responsibility: proposed archaeology-domain validator lane for evidence closure, candidate/site separation, public no-leak checks, cultural review, sensitivity denial, catalog closure, AI location denial, replay, and receipt discipline
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../docs/domains/archaeology/VALIDATORS.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../docs/domains/archaeology/IDENTITY_MODEL.md
  - ../../../contracts/archaeology/
  - ../../../contracts/domains/archaeology/
  - ../../../policy/domains/archaeology/
  - ../../../policy/sensitivity/archaeology/
  - ../../../schemas/contracts/v1/
  - ../../../fixtures/domains/archaeology/
  - ../../../tests/domains/archaeology/
  - ../../../data/receipts/
  - ../../../data/proofs/archaeology/
  - ../../../release/
notes:
  - "This README documents a proposed archaeology-domain validator implementation lane. It does not confirm executable files."
  - "Archaeology is a sensitive-domain lane. Validators must fail closed when evidence, sensitivity, cultural review, rights, sovereignty, redaction, catalog closure, release state, or AI-location handling is incomplete."
  - "Validators enforce declared contracts, schemas, and policy. They do not define archaeology meaning, cultural authority, sensitivity policy, proof records, release decisions, or public products."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/archaeology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-archaeology--validators-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-red)
![sensitivity](https://img.shields.io/badge/sensitivity-T4--default-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/archaeology/` is the proposed validator lane for archaeology-domain checks: EvidenceBundle-required, candidate-not-site, public no-leak, rights and cultural review, exact sensitive geometry denial, catalog closure, and AI exact-location denial.

---

## Purpose

`tools/validators/archaeology/` exists to hold archaeology-specific validator entrypoints and helpers under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does an archaeology candidate satisfy declared evidence, sensitivity, rights, cultural-review, redaction, catalog, release, AI-surface, and replay requirements without exposing restricted cultural or site-location information?

The answer should be a deterministic validation result and a `ValidationReport` where the governed workflow requires it. It should not become archaeology truth, cultural authority, policy authority, proof closure, release approval, or publication.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/archaeology/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Archaeology validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Canonical archaeology validator reference | **CONFIRMED in repo evidence / draft** | Domain validator doc names seven canonical validators, finite outcomes, receipt emission, fixtures, CI binding, policy parity, replay, `spec_hash`, and `validate_all.py` as the intended entrypoint. |
| Archaeology sensitivity posture | **CONFIRMED in repo evidence / draft** | Sensitivity doc sets archaeology default tier to T4 DENY for site location, human remains, sacred sites, collection security, and looting-risk exposure. |
| Policy bundles and fixtures | **PROPOSED / NEEDS VERIFICATION** | Paths exist in docs as proposed; implementation must be checked before CI claims. |
| Release and cultural-review wiring | **PROPOSED / NEEDS VERIFICATION** | Requires current repo evidence for actual release, review, and approval artifacts. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Archaeology validator entrypoints | `tools/validators/archaeology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Archaeology validator doctrine | `docs/domains/archaeology/VALIDATORS.md` |
| Archaeology sensitivity doctrine | `docs/domains/archaeology/SENSITIVITY.md` |
| Archaeology meaning and contracts | `contracts/archaeology/`, `contracts/domains/archaeology/`, or accepted contract home |
| Archaeology policy rules | `policy/domains/archaeology/`, `policy/sensitivity/archaeology/`, or accepted policy home |
| Machine schemas | `schemas/contracts/v1/` or accepted schema home |
| Fixtures and tests | `fixtures/domains/archaeology/`, `tests/domains/archaeology/`, or accepted conventions |
| Receipts and proof records | `data/receipts/`, `data/proofs/archaeology/` |
| Release records | `release/` |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it enforces declared contracts, schemas, policy, sensitivity, and release gates.
- **NEEDS VERIFICATION:** exact executable names, policy bundle digests, fixtures, schema paths, CI wiring, and runtime parity.
- **DENY:** using this folder as cultural authority, source registry, schema home, policy home, proof store, release record store, data store, public API, or public map product surface.

[Back to top](#top)

---

## Canonical validator set

The archaeology domain validator reference names seven validator families. This implementation lane should map to them without redefining their meaning.

| Validator family | Core check | Status |
|---|---|---|
| `EvidenceBundle-required` | Public or promotable claim resolves to required evidence support. | PROPOSED implementation |
| `Candidate-not-site` | Candidate records are not presented as confirmed sites. | PROPOSED implementation |
| `Public no-leak` | Public-bound artifacts do not expose restricted site/location/cultural details. | PROPOSED implementation |
| `Rights and cultural review` | Rights, sovereignty, CARE/cultural review, consent, and embargo requirements are represented. | PROPOSED implementation |
| `Exact sensitive geometry denial` | Restricted exact geometry is denied or transformed per accepted profile. | PROPOSED implementation |
| `Catalog closure` | Catalog/proof/release pointers are complete before promotion. | PROPOSED implementation |
| `AI exact-location denial` | AI surfaces cannot reveal exact restricted locations or infer them from context. | PROPOSED implementation |

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/archaeology/` include validators that check:

- EvidenceBundle or EvidenceRef presence for archaeology claims;
- candidate record vs confirmed site separation;
- public no-leak constraints for exact location, site identity, collection security, sacred/cultural details, and looting-risk exposure;
- rights, cultural review, sovereignty label, CARE label, consent, revocation, and embargo references;
- named redaction profile and `RedactionReceipt` presence for public-safe transformations;
- exact sensitive geometry denial or accepted generalization path;
- catalog, proof, release, rollback, and correction support before publication;
- AI prompt/response denial for exact restricted location requests;
- deterministic `spec_hash` and replay/golden-hash checks where configured;
- receipt emission discipline for validator invocations.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/archaeology/` | Correct home |
|---|---|
| Shared schema registry helpers | `tools/validators/_common/` |
| Archaeology contracts | `contracts/archaeology/` or accepted contract home |
| Archaeology schemas | `schemas/contracts/v1/...` |
| Archaeology policy rules | `policy/domains/archaeology/`, `policy/sensitivity/archaeology/` |
| Source descriptors | `data/registry/sources/archaeology/` |
| Lifecycle data | dedicated `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, and `data/published` roots |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release records | `release/` |
| Connectors or pipelines | `connectors/`, `pipelines/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

[Back to top](#top)

---

## Archaeology validation posture

Archaeology validators must be fail-closed. Missing support should return `DENY`, `ABSTAIN`, `ERROR`, or `NEEDS_REVIEW` according to the declared contract rather than guessing a safe result.

Validators should fail closed or route to review when:

- exact site geometry is public-bound;
- human remains, sacred sites, culturally sensitive records, or collection-security details are present;
- redaction/generalization support is absent;
- cultural review, sovereignty labels, rights, consent, revocation, or embargo state is incomplete;
- a candidate record is presented as a confirmed site;
- an AI answer could reveal or triangulate restricted location information;
- catalog/proof/release/rollback/correction support is missing;
- CI/runtime policy bundle parity cannot be proven.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `ARCH_VALIDATION_PASS` | Configured archaeology checks passed. |
| `ARCH_VALIDATION_FAIL` | Configured archaeology checks failed. |
| `EVIDENCE_BUNDLE_REQUIRED` | Required evidence support is absent or unresolved. |
| `CANDIDATE_SITE_COLLAPSE` | Candidate is presented as confirmed site. |
| `PUBLIC_LEAK_DENIED` | Public-bound payload exposes restricted archaeology information. |
| `CULTURAL_REVIEW_REQUIRED` | Rights, sovereignty, CARE, consent, embargo, or cultural review is incomplete. |
| `SENSITIVE_GEOMETRY_DENIED` | Exact or unsafe geometry is present without accepted transformation. |
| `REDACTION_RECEIPT_MISSING` | Required redaction/generalization receipt is absent. |
| `CATALOG_CLOSURE_MISSING` | Required catalog/proof/release closure support is absent. |
| `AI_LOCATION_DENIED` | AI-facing request or output seeks or reveals restricted exact location. |
| `POLICY_PARITY_UNVERIFIED` | CI/runtime policy bundle parity cannot be verified. |
| `NEEDS_REVIEW` | Human steward or rights-holder review is required. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/domains/archaeology/
├── README.md
├── test_archaeology_validators.py
└── fixtures/
    ├── valid_public_safe_summary/
    ├── missing_evidence_bundle/
    ├── candidate_presented_as_site/
    ├── public_exact_geometry_denied/
    ├── missing_cultural_review/
    ├── missing_redaction_receipt/
    ├── catalog_closure_missing/
    └── ai_exact_location_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/domains/archaeology
```

```bash
python tools/validators/archaeology/validate_all.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_all.py` or `tests/domains/archaeology/` exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy and sensitivity posture rather than defining policy locally.
- [ ] Exact sensitive geometry is denied or transformed only through accepted profiles.
- [ ] Candidate-not-site distinction is enforced.
- [ ] Public no-leak checks cover location, cultural sensitivity, collection security, and looting-risk exposure.
- [ ] Rights, sovereignty, CARE, consent, revocation, and embargo references are checked where required.
- [ ] RedactionReceipt, ValidationReport, EvidenceBundle, catalog, release, correction, and rollback support are checked where relevant.
- [ ] AI exact-location denial is tested.
- [ ] Tests use public-safe or synthetic fixtures only.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify actual validator entrypoints, policy bundle digests, fixtures, schemas, receipt outputs, and CI/runtime parity before wiring CI. |
