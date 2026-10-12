<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-archaeology-readme
title: tools/validators/domains/archaeology README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-archaeology-steward-plus-sensitivity-reviewer-plus-policy-steward-plus-evidence-steward-plus-cultural-review-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; archaeology; sensitive-domain; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Archaeology validator index for narrow archaeology edge, child, and specialty validators under tools/validators/domains/archaeology while deferring broad archaeology validator scope to tools/validators/archaeology and archaeology meaning, sensitivity, cultural review, policy, evidence, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../archaeology/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../../docs/domains/archaeology/VALIDATORS.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../../docs/domains/archaeology/OBJECT_FAMILIES.md
  - ../../../../../docs/domains/archaeology/IDENTITY_MODEL.md
  - ../../../../../contracts/archaeology/
  - ../../../../../contracts/domains/archaeology/
  - ../../../../../policy/domains/archaeology/
  - ../../../../../policy/sensitivity/archaeology/
  - ../../../../../schemas/contracts/v1/
  - ../../../../../data/proofs/archaeology/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "Broad Archaeology-domain validator scope is already documented at tools/validators/archaeology/. This subtree is for narrower per-domain child or edge validators, not a competing Archaeology authority."
  - "Archaeology is a sensitive-domain lane. Child validators must fail closed when evidence, sensitivity, rights, cultural review, redaction, release, correction, rollback, or AI-location handling is incomplete."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/archaeology

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-archaeology--child--validators-informational)
![posture](https://img.shields.io/badge/posture-fail--closed-red)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/archaeology/` is the proposed per-domain index for narrow Archaeology child, edge, and specialty validators under `tools/validators/domains/`, while broad Archaeology validation remains documented at `tools/validators/archaeology/`.

---

## Purpose

`tools/validators/domains/archaeology/` exists to organize narrow archaeology validators that are too specific for shared `_common/` tooling and too specialized for the broad `tools/validators/archaeology/` parent lane.

The durable KFM question for this index is:

> Which archaeology-specific child validators live under the per-domain validator tree, and how do they preserve archaeology authority, sensitivity posture, rights and cultural review, evidence closure, redaction discipline, release readiness, correction paths, rollback support, and AI/public-surface denial boundaries?

The answer should be a navigable validator index and deterministic validation outputs from child lanes. This folder should not create archaeology truth, cultural authority, sensitivity policy, EvidenceBundles, redaction receipts, policy decisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/archaeology/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad Archaeology validator parent | **CONFIRMED in repo evidence / draft** | `tools/validators/archaeology/README.md` documents broad archaeology evidence, candidate/site separation, public no-leak, cultural review, sensitivity denial, catalog closure, AI denial, replay, and receipt checks. |
| Archaeology validator doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/archaeology/VALIDATORS.md` names seven canonical validator families, finite outcomes, receipt emission, fixture discipline, policy parity, replay, `spec_hash`, and `validate_all.py` as intended reference points. |
| Archaeology sensitivity doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/archaeology/SENSITIVITY.md` sets the lane to deny-by-default for sensitive archaeology materials and requires named redaction profiles and RedactionReceipt support for public-safe transformations. |
| Child README lanes | **NONE CONFIRMED IN THIS TASK** | No child archaeology validator README was verified while writing this index. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundle digests, receipts, runtime parity, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Relationship to `tools/validators/archaeology/`

Use this split:

| Validator concern | Preferred lane |
|---|---|
| Broad Archaeology-domain validation | `tools/validators/archaeology/` |
| EvidenceBundle-required, candidate-not-site, public no-leak, rights/cultural review, sensitive-geometry denial, catalog closure, AI exact-location denial | `tools/validators/archaeology/` |
| Narrow child or edge-specific archaeology validators | `tools/validators/domains/archaeology/<child>/` |
| Cross-domain generic invariants | `tools/validators/cross-domain-joins/` |
| Shared validator plumbing | `tools/validators/_common/` |

This README does not move or rename the broad Archaeology validator lane. It makes the `domains/archaeology/` subtree inspectable so future child validators do not become orphan greenfield stubs.

[Back to top](#top)

---

## Child lanes

No child README lanes were confirmed during this edit.

Future child lanes should be added only when they represent a distinct archaeology specialty, edge, fixture family, or public-surface invariant with accepted contracts, policy posture, fixtures, receipts, and report semantics. Examples may include a sovereignty-review child, redaction-profile child, catalog-closure child, AI-denial child, or cross-domain archaeology touch edge, but those examples remain **PROPOSED** until verified and approved.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Archaeology child-validator index | `tools/validators/domains/archaeology/` |
| Broad Archaeology validator lane | `tools/validators/archaeology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Archaeology validator doctrine | `docs/domains/archaeology/VALIDATORS.md` |
| Archaeology sensitivity doctrine | `docs/domains/archaeology/SENSITIVITY.md` |
| Archaeology cultural review and publication doctrine | `docs/domains/archaeology/` |
| Archaeology object meaning | `docs/domains/archaeology/OBJECT_FAMILIES.md`, accepted contracts |
| Archaeology contracts | `contracts/archaeology/`, `contracts/domains/archaeology/`, or accepted contract home |
| Archaeology policy rules | `policy/domains/archaeology/`, `policy/sensitivity/archaeology/`, or accepted policy homes |
| Machine schemas | `schemas/contracts/v1/` or accepted schema home |
| Evidence/proof support | `data/proofs/archaeology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/archaeology/`, `tests/domains/archaeology/`, `fixtures/domains/archaeology/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** child validator code may live below this folder when it checks declared archaeology invariants and delegates meaning, sensitivity, policy, cultural review, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, policy bundle digests, source descriptors, fixtures, report destinations, receipts, replay/golden-hash behavior, and CI/runtime parity.
- **DENY:** using this folder as cultural authority, archaeology contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public runtime surface, public map product surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/archaeology/` include:

- this parent/index README;
- child README lanes for narrow archaeology validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- specialty validators that preserve EvidenceBundle support, candidate/site separation, sensitivity posture, rights and cultural review, redaction profiles, AI/public-surface denial, release references, correction cascade, and rollback support;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative archaeology doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/archaeology/` | Correct home |
|---|---|
| Broad Archaeology validator contract | `tools/validators/archaeology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Archaeology domain docs | `docs/domains/archaeology/` |
| Archaeology contracts | `contracts/archaeology/`, `contracts/domains/archaeology/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and sensitivity rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, RedactionReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, export, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Sensitive-domain validator posture

Archaeology child validators must fail closed, deny, abstain, or route to steward review when a candidate:

- lacks required EvidenceBundle or EvidenceRef support;
- treats a candidate record as a confirmed site;
- lacks rights, cultural review, sovereignty, consent, embargo, or revocation posture where required;
- lacks a named redaction profile or RedactionReceipt for public-safe transformation;
- exposes restricted archaeology detail through public map, API, export, graph, narrative, or AI surface;
- allows exact restricted location inference from context;
- publishes catalog, graph, map, Focus Mode, export, or AI narrative without review, release, correction, and rollback support;
- bypasses lifecycle gates or treats validator output as release approval.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `ARCH_DOMAIN_VALIDATORS_PASS` | Configured child validators passed. |
| `ARCH_DOMAIN_VALIDATORS_FAIL` | One or more configured child validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Archaeology child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `SENSITIVE_DOMAIN_DENY` | Candidate is denied under sensitive-domain posture. |
| `CULTURAL_REVIEW_REQUIRED` | Candidate requires steward/cultural review before promotion or public use. |
| `REDACTION_PROFILE_MISSING` | Required named redaction profile is absent. |
| `REDACTION_RECEIPT_MISSING` | Required RedactionReceipt or equivalent transform receipt is absent. |
| `EVIDENCE_OR_RELEASE_GAP` | Required evidence, review, release, correction, or rollback reference is absent. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `AUTHORITY_COLLAPSE` | Validator output or candidate collapses archaeology, cultural, policy, evidence, or release authority. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/archaeology/
├── README.md
├── test_archaeology_domain_validator_parent.py
└── fixtures/
    ├── valid_child_validator_bundle/
    ├── missing_child_validator/
    ├── sensitive_domain_deny/
    ├── cultural_review_required/
    ├── redaction_profile_missing/
    ├── redaction_receipt_missing/
    ├── evidence_or_release_gap/
    ├── public_surface_leak_risk/
    ├── authority_collapse/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/archaeology
```

```bash
python tools/validators/domains/archaeology/run_archaeology_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_archaeology_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Broad Archaeology validation remains in `tools/validators/archaeology/`.
- [ ] Child validators preserve archaeology meaning, cultural authority, sensitivity posture, and policy authority boundaries.
- [ ] EvidenceBundle, rights, cultural review, release, rollback, and correction support are checked where required.
- [ ] Public-facing outputs require named redaction profiles and receipts where transformed.
- [ ] AI, map, graph, export, and narrative surfaces are denied when restricted-detail leakage is possible.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for greenfield stub and parent index for Archaeology child validators. |
| Next smallest safe change | Verify parent runner, child validator scripts, accepted specialty profiles, schemas, policy bundles, fixtures, report destinations, receipts, replay/golden-hash behavior, and CI/runtime parity before promoting this lane beyond draft. |
