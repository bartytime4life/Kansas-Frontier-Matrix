<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-suitability-readme
title: tools/validators/suitability README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-suitability-steward-plus-domain-stewards-plus-model-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; suitability-validator-index; modeled-derivative-aware; source-role-aware; method-version-aware; evidence-bound; policy-bound; aggregation-aware; sensitivity-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: parent suitability validator routing README under tools/validators; indexes suitability-derivative validation concerns across domains including modeled/derived posture, source-role anti-collapse, method id/version, scoring scheme, units/class vocabulary, support geometry, temporal applicability, uncertainty, source inputs, cross-domain dependencies, aggregation/redaction receipt linkage, evidence/proof linkage, policy/review/release posture, correction cascade, rollback support, public-surface denial, and routing to narrower suitability validators such as soil-suitability while deferring domain meaning, model authority, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../soil-suitability/README.md
  - ../agriculture/README.md
  - ../domains/agriculture/soil-join/README.md
  - ../domains/soil/README.md
  - ../joins/agriculture-soil/README.md
  - ../source_role/README.md
  - ../policy/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../../../docs/domains/agriculture/OBJECTS.md
  - ../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../docs/domains/agriculture/POLICY.md
  - ../../../docs/domains/agriculture/SENSITIVITY.md
  - ../../../docs/domains/soil/README.md
  - ../../../contracts/domains/agriculture/
  - ../../../contracts/domains/soil/
  - ../../../schemas/contracts/v1/domains/agriculture/
  - ../../../schemas/contracts/v1/domains/soil/
  - ../../../policy/domains/agriculture/
  - ../../../policy/domains/soil/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/suitability/README.md. It does not confirm executable suitability validators, registry wiring, schemas, fixtures, model cards, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "This is the broad suitability parent lane. Soil-specific suitability validation belongs in tools/validators/soil-suitability/."
  - "Suitability outputs are derived, modeled, interpretive, or scored artifacts unless a domain contract says otherwise. They are not raw observation truth, regulatory determinations, operational commands, field-level management orders, or release approval by themselves."
  - "Source-role anti-collapse is mandatory: modeled suitability must not be presented as measured, observed, authoritative, regulatory, or field-verified truth."
  - "Any suitability output exposed to public surfaces must carry method/version posture, evidence support, policy/review/release support, correction path, rollback target, and sensitivity/rights posture appropriate to its domain."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/suitability

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-suitability--validator--index-informational)
![authority](https://img.shields.io/badge/authority-derived--not--truth-lightgrey)
![posture](https://img.shields.io/badge/posture-source--role--aware-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/suitability/` is the broad suitability validator routing index for modeled or derived suitability outputs, checking method/version posture, source-role preservation, evidence support, policy/review/release readiness, correction/rollback support, and public-surface denial without becoming model authority, domain truth, policy authority, evidence authority, or release authority.

---

## Purpose

`tools/validators/suitability/` exists to organize suitability-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a suitability candidate preserve the correct domain boundary, input source roles, method identity, model version, scoring scheme, units/class vocabulary, support geometry, temporal applicability, uncertainty, EvidenceRef and EvidenceBundle support, policy/review posture, rights/sensitivity posture, release reference, correction path, rollback target, and public-surface limits for the exact use being requested?

The answer should be a deterministic validation result or routing decision. This folder should not create suitability truth, raw observation truth, regulatory determinations, field-level advice, model authority, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/suitability/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `tools/validators/soil-suitability/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Soil-specific suitability derivative lane for `SoilCropSuitability`, MUKEY/COKEY/CHKEY continuity, Soil-owned EvidenceRefs, Agriculture-owned derivative boundaries, and correction cascade. |
| `docs/domains/agriculture/OBJECTS.md` | **CONFIRMED draft reference / realization NEEDS VERIFICATION** | Names `SoilCropSuitability` as a derived score/rating and states it is modeled, not measured. |
| `tools/validators/source_role/README.md` | **CONFIRMED README / executable behavior NEEDS VERIFICATION** | Source-role anti-collapse lane; suitability outputs must preserve modeled/derived posture. |
| `tools/validators/sensitivity/README.md` and `tools/validators/rights/README.md` | **CONFIRMED READMEs / executable behavior NEEDS VERIFICATION** | Suitability public surfaces must preserve rights, sensitivity, consent, and public-surface limits. |
| Executable suitability scripts, registry wiring, schemas, fixtures, model cards, policy bundles, method vocabularies, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Broad suitability routing | `tools/validators/suitability/` | Parent validator route for suitability-derived outputs. |
| Soil suitability derivatives | `tools/validators/soil-suitability/` | SoilCropSuitability, Soil-owned identity/evidence, Agriculture-owned scoring. |
| Source-role anti-collapse | `tools/validators/source_role/` | Prevents modeled suitability from becoming observed/authority truth. |
| Domain meaning | `docs/domains/`, `contracts/domains/` | Validators check conformance; they do not define domain meaning. |
| Machine shape | `schemas/contracts/v1/domains/` and accepted schema homes | Schemas define shape; this folder does not. |
| Model cards/specs/method registries | accepted model, method, or domain documentation homes when verified | This folder may check references; it does not own model authority. |
| Policy and release posture | `policy/`, `release/` | Validator reports gaps; it does not decide policy or release. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Validators check references; they do not create authority records. |
| Fixtures and tests | `fixtures/`, `tests/` | Synthetic examples and tests prove behavior; they are not suitability authority. |

[Back to top](#top)

---

## Suitability validation packet

A suitability candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Candidate identity | Candidate id, domain/lane, object refs, artifact refs, lifecycle state, requested audience, requested operation, and requested surface. | Permission by naming convention. |
| Domain boundary | Owning domain, borrowed/input domains, join boundaries, and derivative ownership are explicit. | Cross-domain truth transfer. |
| Source role posture | Input source roles and output role are visible, with modeled/derived/aggregate/candidate posture preserved. | Observed, authority, regulatory, or field-verified truth. |
| Suitability method | Method id, method version, scoring scheme, class/rating vocabulary, units, limitations, uncertainty, assumptions, and scale are explicit. | Universal or timeless suitability. |
| Inputs and evidence | Input object refs, EvidenceRefs, EvidenceBundle/proof support, source ids, spec hashes, and digest lineage are resolvable where required. | Generated score as evidence. |
| Temporal posture | Valid time, observed time, modeled time, effective time, refresh cadence, stale-state, and supersession posture are visible. | Current advice by default. |
| Sensitivity/rights posture | Private, operator-adjacent, exact-location, source-rights, consent, and public-surface limits are preserved. | Public release by derived status alone. |
| Receipts and validation | Model run receipt, aggregation/redaction receipt, validation report, or equivalent support resolves where material. | Receipt as truth or release approval. |
| Policy/review/release support | Policy decision, reason codes, obligations, reviewer binding, release reference, correction path, withdrawal posture, rollback target, and supersession state exist where required. | Publication by validator success. |
| Public-surface envelope | Map/API/tile/export/screenshot/graph/search/Focus Mode/embedding/AI surfaces are limited to approved public-safe derivatives and caveats. | Unbounded reuse across surfaces. |

[Back to top](#top)

---

## Suitability invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Suitability is interpretive | Suitability scores/ratings remain modeled, derived, or interpretive unless a verified domain contract says otherwise. | Candidate is presented as raw observation truth, official determination, or field instruction. |
| Source roles do not collapse | Modeled, aggregate, candidate, contextual, observed, authority, and regulatory roles remain distinct. | Suitability output upgrades input roles or hides modeled status. |
| Method is explicit | Method id/version, scoring scheme, class vocabulary, units, scale, limitations, and uncertainty are present. | Score/rating appears without method context. |
| Inputs remain traceable | Input objects, source ids, EvidenceRefs, proof refs, and spec hashes resolve where required. | Suitability is generated from untraceable inputs. |
| Cross-domain boundaries are preserved | Borrowed domain inputs remain owned by their domain and are consumed by reference. | Suitability domain republishes another domain's canonical truth. |
| Public use is gated | Rights, sensitivity, aggregation/redaction, policy, review, release, correction, and rollback support close before public exposure. | Public surface receives unsupported or private/operator-adjacent detail. |
| Corrections cascade | Input correction, method change, stale source, rights change, revocation, withdrawal, or rollback invalidates dependent suitability outputs. | Suitability remains active after upstream support changes. |
| Carriers are not authority | Maps, tiles, exports, graphs, screenshots, Focus Mode, embeddings, and AI answers are downstream carriers. | Carrier becomes evidence, policy, release, model, or suitability authority. |

[Back to top](#top)

---

## Fail-closed conditions

A suitability candidate should fail closed, deny, restrict, abstain, or route to steward review when:

- owning domain, borrowed input domain, derivative boundary, source refs, object refs, or lifecycle state is missing;
- source role, method id/version, scoring scheme, class/rating vocabulary, units, limitations, uncertainty, scale, or temporal applicability is missing;
- suitability is presented as measured, observed, regulatory, field-verified, official advice, or operational instruction without verified authority;
- input EvidenceRefs, EvidenceBundles, proof refs, source ids, spec hashes, run receipts, validation reports, or digest lineage are missing or unresolved;
- support types or source roles collapse across observed, regulatory, modeled, aggregate, candidate, contextual, public-safe derivative, or experimental records;
- private, operator-adjacent, parcel-linked, exact-location, rights-limited, consent-limited, or sensitive suitability output is public-bound without aggregation/redaction/review/release support;
- policy decision, review binding, rights posture, sensitivity posture, release reference, correction path, rollback target, or supersession posture is missing where required;
- map, tile, export, screenshot, search, graph, embedding, Focus Mode, popup, or AI answer output overclaims suitability, hides caveats, drops evidence, or exposes unsupported details.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Broad suitability validator routing | `tools/validators/suitability/` |
| Soil suitability validation | `tools/validators/soil-suitability/` |
| Source-role validation | `tools/validators/source_role/` |
| Domain validators | domain validator lanes under `tools/validators/` |
| Domain meaning | `docs/domains/`, `contracts/domains/` |
| Domain schemas | `schemas/contracts/v1/domains/` and accepted schema homes |
| Model/method documentation | accepted model, method, package, or domain documentation homes when verified |
| Policy | `policy/` and accepted domain policy homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared suitability invariants and delegates domain meaning, model authority, schema authority, policy decisions, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, suitability schema/contract homes, model/method vocabulary, model-card homes, fixture files, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as domain truth, model authority, suitability truth, field advice, regulatory authority, source registry, policy home, schema home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/suitability/` include:

- this README;
- parent routing notes for suitability-facing validators;
- small validation adapters that check suitability derivative packets;
- checks for method id/version, score/rating vocabulary, units, uncertainty, assumptions, limitations, temporal applicability, and scale caveats;
- checks for source-role preservation and anti-collapse;
- checks that borrowed domain truth is consumed by reference, not republished;
- checks that sensitive/private/operator-adjacent suitability requires aggregation/redaction/review/release support;
- checks that upstream corrections, stale sources, revocations, method changes, or rollbacks cascade into suitability outputs;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Domain semantic contracts | `contracts/domains/` |
| Domain schemas, model-output schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/domains/` and accepted schema homes |
| Policy rules, suitability allowlists, model thresholds, field-management rules, steward decisions | `policy/`, steward review homes, release governance homes |
| Source data, model outputs, suitability payloads, rasters, vectors, private/operator records | governed `data/` lifecycle roots |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SUITABILITY_VALIDATOR_PASS` | Candidate passed configured suitability checks. |
| `SUITABILITY_VALIDATOR_FAIL` | Candidate failed one or more configured suitability checks. |
| `SUITABILITY_VALIDATOR_DENY` | Candidate must not proceed because evidence, policy, review, rights, sensitivity, release, correction, rollback, model, or public-surface support cannot be resolved. |
| `SUITABILITY_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SUITABILITY_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a suitability assertion. |
| `SUITABILITY_METHOD_MISSING` | Method id/version, scoring scheme, vocabulary, units, limitations, uncertainty, or scale is absent. |
| `SUITABILITY_SOURCE_ROLE_COLLAPSE_DENIED` | Suitability output collapses or upgrades source roles. |
| `SUITABILITY_DOMAIN_BOUNDARY_MISSING` | Owning domain, borrowed input domain, or derivative boundary is missing. |
| `SUITABILITY_EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `SUITABILITY_RECEIPT_MISSING` | Required model run, aggregation, redaction, validation, or transformation receipt is absent. |
| `SUITABILITY_MODEL_OVERCLAIM` | Modeled/derived suitability is presented as observed truth, official determination, or field instruction. |
| `SUITABILITY_INPUT_TRACE_MISSING` | Required input object refs, source ids, spec hashes, or digest lineage are absent. |
| `SUITABILITY_SUPPORT_TYPE_COLLAPSE_DENIED` | Observed/regulatory/modeled/aggregate/candidate support types collapse. |
| `SUITABILITY_FIELD_LEVEL_PUBLIC_DENIED` | Field/operator/private parcel-adjacent suitability is public-bound without aggregation/redaction/review/release support. |
| `POLICY_OR_REVIEW_GAP` | Required policy decision, review state, rights posture, sensitivity posture, or obligation support is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `SUITABILITY_CORRECTION_CASCADE_MISSING` | Input correction, source stale state, method change, revocation, withdrawal, or rollback did not propagate to suitability output. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsupported or sensitive suitability content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/suitability/
├── README.md
├── validate_suitability_packet.py       # PROPOSED; not confirmed
├── validate_suitability_method.py       # PROPOSED; not confirmed
├── validate_suitability_cascade.py      # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, model cards, local schema files, source data, suitability payloads, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting suitability, public-surface, or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/suitability/README.md`.
- [x] It marks this path as broad suitability validator routing, not domain truth, model authority, suitability truth, field advice, regulatory authority, schema authority, policy authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It distinguishes this parent lane from `tools/validators/soil-suitability/`.
- [x] It preserves method/version posture, source-role anti-collapse, domain-boundary checks, evidence/proof linkage, policy/review/release posture, correction cascade, rollback, and public-surface denial.
- [x] It routes domain meaning to `contracts/` and `docs/`, machine shape to `schemas/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, schema homes, method vocabularies, model-card homes, policy bundles, fixtures, tests, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to broad suitability validators are searched and classified.
- [ ] Suitability contract/schema homes, method vocabulary, model-card homes, and domain-specific suitability lanes are verified.
- [ ] EvidenceRef, support type, source role, rating vocabulary, model run receipt, and release-reference schema bindings are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, abstain, method-missing, evidence-missing, source-role-collapse, support-type-collapse, model-overclaim, field-public-denied, correction-cascade-missing, and public-surface-blocked cases.
- [ ] CI invokes suitability validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with broad suitability validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
