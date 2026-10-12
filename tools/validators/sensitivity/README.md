<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-sensitivity-readme
title: tools/validators/sensitivity README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-sensitivity-steward-plus-policy-steward-plus-rights-steward-plus-evidence-steward-plus-release-steward-plus-redaction-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; sensitivity-validator-index; T0-T4-aware; deny-by-default; most-restrictive-wins; rights-aware; geoprivacy-aware; redaction-aware; review-required; release-gated; fail-closed; non-authoritative
owning_root: tools/
responsibility: parent sensitivity validator routing README under tools/validators; documents validation expectations for sensitivity classification, tier posture, source and derivative sensitivity propagation, most-restrictive composition, rights/sensitivity interaction, public-safe transform requirements, policy decision and reason-code support, review and receipt linkage, lifecycle quarantine routing, release/correction/rollback posture, AI/map/tile/export/search/graph public-surface denial, schema/fixture/test routing, and finite outcomes while deferring sensitivity policy rules, tier authority, policy decisions, redaction parameters, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../policy/README.md
  - ../rights/README.md
  - ../sensitive_geometry/README.md
  - ../sensitive_location_allow/README.md
  - ../geoprivacy/README.md
  - ../geoprivacy_transform/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../maplibre/README.md
  - ../pmtiles/README.md
  - ../../../docs/architecture/sensitivity-tiers.md
  - ../../../docs/architecture/sensitive-domain-fail-closed.md
  - ../../../docs/registers/POLICY_GATE.md
  - ../../../docs/standards/REDACTION_PROFILES.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../policy/sensitivity/README.md
  - ../../../policy/decision/README.md
  - ../../../policy/geoprivacy/
  - ../../../policy/redaction/
  - ../../../policy/rights/
  - ../../../schemas/contracts/v1/policy/
  - ../../../schemas/contracts/v1/receipts/
  - ../../../data/quarantine/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/sensitivity/README.md. It does not confirm executable sensitivity validators, registry wiring, policy bundles, transform implementation, receipt emission, or CI behavior."
  - "Sensitivity validation is a checking/routing lane. It must not define tier authority, set policy rules, downgrade sensitivity, write PolicyDecisions, create receipts, approve release, publish artifacts, or authorize public surfaces."
  - "T0 is not the default. Public-safe openness must be proven through governed evidence, rights, sensitivity, policy, review, release, correction, and rollback support."
  - "Most-restrictive wins across joins, derivatives, maps, tiles, graphs, screenshots, search, embeddings, Focus Mode, AI answers, and public clients."
  - "No exact coordinates, restricted identifiers, redaction radii, grid sizes, geohash precision, reconstruction thresholds, hidden policy values, or other reverse-engineering hints belong in this README or in repository-facing validator documentation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/sensitivity

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-sensitivity--validator--index-informational)
![default](https://img.shields.io/badge/default-deny--by--default-critical)
![posture](https://img.shields.io/badge/posture-most--restrictive--wins-red)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/sensitivity/` is the sensitivity validator routing index for checking tier posture, deny-by-default handling, rights/sensitivity interaction, most-restrictive propagation, policy/review/receipt/release support, and public-surface denial without becoming sensitivity policy authority or release authority.

---

## Purpose

`tools/validators/sensitivity/` exists to organize sensitivity-facing validation under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a candidate source, derivative, catalog record, triplet, join, layer, tile, export, graph edge, search result, screenshot, Focus Mode surface, embedding, AI answer, or release candidate carry a resolved sensitivity posture, rights posture, policy decision, review state, transform receipt, evidence support, lifecycle state, release reference, correction path, rollback target, and public-surface limit appropriate for the requested use?

The answer should be a deterministic validation result or routing decision. This folder should not define sensitivity policy, assign authoritative tiers, downgrade sensitivity, define hidden thresholds, perform redaction transforms as authority, create receipts, create EvidenceBundles, store proofs, store lifecycle data, decide policy, approve release, publish artifacts, expose public API payloads, or authorize AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/sensitivity/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `docs/architecture/sensitivity-tiers.md` | **CONFIRMED draft architecture doc / implementation NEEDS VERIFICATION** | Defines T0–T4 as a proposed tier scheme and states default-deny applies when rights, sovereignty, sensitivity, or release-state evidence is missing. |
| `docs/registers/POLICY_GATE.md` | **CONFIRMED register / implementation NEEDS VERIFICATION** | Describes the validator-class gate ladder and places source role, rights, cadence, and sensitivity checks before policy, lifecycle, receipt, and release gates. |
| `docs/architecture/sensitive-domain-fail-closed.md` | **CONFIRMED architecture doc / implementation NEEDS VERIFICATION** | Sensitive lanes fail closed by default; no silent allow, no style-as-policy, and no carrier-as-evidence. |
| `tools/validators/sensitive_geometry/README.md` | **CONFIRMED sibling README / executable behavior NEEDS VERIFICATION** | Sensitive-geometry lane handles exact-location/public-safe geometry, reverse-engineering risk, receipts, release, and public-surface denial. |
| `policy/sensitivity/README.md` | **CONFIRMED stub / policy implementation NEEDS VERIFICATION** | Existing policy sensitivity root is a greenfield bundle stub; active policy rules and bundle digests are not confirmed here. |
| Executable sensitivity validator scripts, registry wiring, schema bindings, policy bundles, redaction profiles, fixture coverage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

`tools/validators/sensitivity/` is a **validator routing index**, not the sensitivity policy root.

| Responsibility | Preferred home | Validator relationship |
|---|---|---|
| Sensitivity validation adapters | `tools/validators/sensitivity/` | Check sensitivity readiness and emit deterministic findings. |
| Sensitivity policy rules and bundles | `policy/sensitivity/`, `policy/geoprivacy/`, `policy/redaction/`, accepted policy homes | Validators reference accepted policy bundle ids/digests; they do not decide policy. |
| Policy decision vocabulary and finite outcomes | `policy/decision/`, policy contracts/schemas | Validators check presence, shape, reason codes, and obligations. |
| Sensitivity architecture and doctrine | `docs/architecture/sensitivity-tiers.md`, `docs/architecture/sensitive-domain-fail-closed.md`, domain sensitivity docs | Human-facing standards; validators check conformance. |
| Sensitive-geometry and geoprivacy checks | `tools/validators/sensitive_geometry/`, `tools/validators/geoprivacy/` | Specialized geometry/location checks route there. |
| Rights checks | `tools/validators/rights/` | Rights and sensitivity must close together where rights limit publication. |
| Release/promotion checks | `tools/validators/release/`, `tools/validators/promotion_gate/` | Validator success is not release approval. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Validators check refs and may emit reports only to accepted homes. |
| Quarantine/lifecycle data | `data/quarantine/` and other `data/` lifecycle roots | Validators route held material; they do not store lifecycle payloads. |
| Fixtures and tests | `fixtures/`, `tests/`, accepted fixture/test homes | Synthetic examples and tests prove behavior; they are not sensitivity authority. |

Validators may fail closed when sensitivity support is absent, stale, contradictory, unsupported, unreviewed, non-transferable, inherited from a stricter upstream object, or unresolved. They must not silently substitute source popularity, public web visibility, generated text, map display, tile presence, schema validity, citation availability, or file location for sensitivity permission.

[Back to top](#top)

---

## Sensitivity validation packet

A sensitivity candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Candidate identity | Candidate id, source refs, domain/lane, object refs, artifact refs, lifecycle state, requested audience, requested operation, and requested public surface. | Permission by naming convention. |
| Sensitivity posture | Tier/class, sensitivity reason codes, domain-specific sensitivity flags, composition/join sensitivity, and most-restrictive upstream posture. | Sensitivity decision by validator alone. |
| Rights and sovereignty posture | License, rights, consent, stewardship, cultural/tribal authority, source terms, revocation, and downstream obligations. | Public visibility as permission. |
| Evidence support | EvidenceRef resolves to EvidenceBundle/proof support required for sensitivity and release-visible claims. | Generated prose, map display, or tile presence as evidence. |
| Policy decision | Finite policy outcome, policy bundle id/version/digest, reason codes, obligations, scope, audience, expiry/reevaluation, and required next actions. | Local validator as policy authority. |
| Review support | Sensitivity reviewer, domain steward, rights reviewer, cultural/tribal reviewer, release reviewer, or other required review bindings. | Hidden approval or default allow. |
| Transform receipt | RedactionReceipt, AggregationReceipt, RunReceipt, ValidationReport, or equivalent receipt references resolve and match input/output lineage where transforms matter. | Transform performed by this validator. |
| Release support | ReleaseManifest, promotion decision, correction path, withdrawal posture, rollback target, and supersession state exist where required. | Publication by validator success. |
| Public-surface envelope | API/map/tile/export/screenshot/graph/search/Focus Mode/embedding/AI surfaces are limited to the approved derivative and obligations. | Unbounded reuse across all surfaces. |

[Back to top](#top)

---

## Sensitivity invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| T0 is not default | Public-safe openness must be proven; missing evidence starts at deny/hold/restrict/abstain. | Candidate assumes open because no sensitivity was recorded. |
| Most restrictive wins | Joins and derivatives inherit the strictest upstream sensitivity, rights, consent, and release posture. | Candidate weakens or drops upstream restriction. |
| Sensitivity can arise by composition | A join, aggregation, graph edge, search result, tile, screenshot, label, or AI answer may become sensitive even if inputs look open. | Validator checks inputs only and ignores produced output. |
| Allow is explicit | ALLOW requires policy decision, review where required, receipts where transforms matter, evidence support, release support, correction, and rollback. | Silent allow, default allow, or UI allow. |
| Downgrades are easy and upgrades are gated | Motion toward less-public tiers can happen on correction; motion toward more-public tiers requires transform and review support. | Candidate upgrades without receipt/review. |
| Carriers are not evidence | Tiles, maps, screenshots, exports, popups, graphs, embeddings, and AI prose are downstream carriers. | Carrier becomes evidence, policy, or release authority. |
| Style is not policy | Public surfaces receive public-safe derivatives, not restricted payloads hidden by style, zoom, filters, or opacity. | Renderer or UI hides sensitive payload client-side. |
| Corrections propagate | Rights changes, sensitivity changes, revocations, corrections, withdrawals, and rollbacks invalidate downstream carriers. | Public artifacts remain active after a blocking change. |

[Back to top](#top)

---

## Fail-closed conditions

A sensitivity candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- sensitivity tier/class, source role, rights posture, sovereignty posture, consent state, or domain sensitivity flag is missing or unresolved;
- candidate includes archaeology, cultural heritage, sensitive fauna, rare flora, critical infrastructure, living-person, DNA/genomic, private person/parcel, hazards-as-authority, restricted source terms, exact coordinates, or sensitive-by-composition context without explicit review and policy support;
- a derivative, join, tile, layer, graph, search index, embedding, export, screenshot, Focus Mode card, story, or AI answer weakens inherited sensitivity obligations;
- required EvidenceRef, EvidenceBundle, policy decision, reason codes, obligations, review binding, release reference, correction path, rollback target, or transform receipt is missing;
- redaction, generalization, aggregation, suppression, or public-safe transform is required but absent or unsupported;
- candidate tries to move toward a more-public tier without transform receipt and review support;
- public rendering relies on zoom thresholds, opacity, filters, style layers, hidden columns, or client-side controls instead of upstream public-safe derivatives;
- public surfaces would expose sensitive, unreleased, unreviewed, rights-limited, revoked, stale, or unsupported content.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Sensitivity validator routing | `tools/validators/sensitivity/` |
| Sensitivity policy rules and bundles | `policy/sensitivity/`, `policy/geoprivacy/`, `policy/redaction/`, accepted policy homes |
| Policy decision vocabulary | `policy/decision/` and accepted policy object homes |
| Sensitive-domain and tier doctrine | `docs/architecture/sensitivity-tiers.md`, `docs/architecture/sensitive-domain-fail-closed.md`, domain docs |
| Sensitive-geometry/geoprivacy validation | `tools/validators/sensitive_geometry/`, `tools/validators/geoprivacy/`, `tools/validators/sensitive_location_allow/` |
| Rights validation | `tools/validators/rights/` |
| Release and promotion validation | `tools/validators/release/`, `tools/validators/promotion_gate/` |
| Map/tile public-surface validation | `tools/validators/maplibre/`, `tools/validators/pmtiles/` |
| Schemas | `schemas/contracts/v1/policy/`, `schemas/contracts/v1/receipts/`, accepted schema homes |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle/quarantine data | `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared sensitivity invariants and delegates policy decisions, tier authority, transform parameters, schemas, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, sensitivity policy bundle homes, policy bundle digests, tier vocabulary authority, schema ids, fixture files, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as sensitivity policy authority, sensitivity tier authority, allowlist authority, exact-location storage, redaction implementation authority, receipt store, proof store, release record store, canonical schema home, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/sensitivity/` include:

- this README;
- small validation adapters that check sensitivity packets, tier posture, most-restrictive propagation, and public-surface denial;
- checks that rights, consent, stewardship, sensitivity, policy, review, receipts, release, correction, and rollback support close for the requested use;
- checks that joins, tiles, maps, graphs, searches, screenshots, embeddings, Focus Mode surfaces, and AI answers do not weaken inherited sensitivity;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Sensitivity policy rules, tier assignments as authority, allowlists, denylists, steward decisions, thresholds, redaction parameters | `policy/`, steward review homes, release governance homes |
| Exact coordinates, restricted ids, source geometry payloads, public geometry payloads, tile payloads, screenshots, exports, embeddings, or map artifacts | governed lifecycle/release/runtime homes after policy and release review |
| RedactionReceipts, AggregationReceipts, RunReceipts, ValidationReports, proof packs, EvidenceBundles | `data/receipts/`, `data/proofs/`, accepted report lanes |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawals | `release/` |
| Canonical schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/...` or accepted schema homes |
| Semantic contracts | `contracts/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Secrets, source credentials, private source content, sensitive exact locations, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SENSITIVITY_VALIDATOR_PASS` | Candidate passed configured sensitivity checks. |
| `SENSITIVITY_VALIDATOR_FAIL` | Candidate failed one or more configured sensitivity checks. |
| `SENSITIVITY_VALIDATOR_DENY` | Candidate must not proceed because sensitivity, policy, evidence, receipt, rights, review, release, rollback, or public-surface support cannot be resolved. |
| `SENSITIVITY_VALIDATOR_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SENSITIVITY_VALIDATOR_HOLD` | Candidate must remain held pending sensitivity, rights, consent, stewardship, evidence, or policy review. |
| `SENSITIVITY_VALIDATOR_ABSTAIN` | Candidate lacks enough support for a sensitivity assertion. |
| `SENSITIVITY_TIER_MISSING` | Required tier/classification is absent. |
| `SENSITIVITY_TIER_UNRESOLVED` | Sensitivity class is stale, conflicted, unknown, or unsupported. |
| `T0_OVERCLAIM_DENIED` | Candidate claims open/public-safe status without proof. |
| `MOST_RESTRICTIVE_POLICY_NOT_PRESERVED` | Join or derivative weakens upstream restrictions. |
| `SENSITIVE_BY_COMPOSITION_REVIEW_REQUIRED` | Produced output becomes sensitive by join, aggregation, context, graph, search, tile, or AI inference. |
| `POLICY_DECISION_MISSING` | Required policy decision or policy bundle reference is absent. |
| `POLICY_DECISION_NOT_ALLOW` | Policy outcome does not allow the requested scope. |
| `REVIEW_BINDING_MISSING` | Required reviewer, steward, ticket, or separation-of-duties binding is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `RIGHTS_OR_CONSENT_GAP` | Required rights, consent, stewardship, or revocation posture is unresolved. |
| `REDACTION_RECEIPT_MISSING` | Required redaction/generalization/aggregation/suppression receipt is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `STYLE_AS_POLICY_DENIED` | Candidate relies on styling, zoom, opacity, filters, or UI hiding instead of upstream policy-safe outputs. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose sensitive content to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/sensitivity/
├── README.md
├── validate_sensitivity_packet.py       # PROPOSED; not confirmed
├── validate_tier_transition.py          # PROPOSED; not confirmed
├── validate_most_restrictive.py         # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, allowlists, redaction profiles, local schema files, sensitive payloads, public geometry payloads, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting public-surface or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/sensitivity/README.md`.
- [x] It marks this path as sensitivity validator routing, not sensitivity policy authority, tier authority, allowlist authority, redaction implementation authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves fail-closed posture for missing tier/classification, unresolved sensitivity, T0 overclaiming, missing policy/review/evidence/rights/release support, most-restrictive failures, sensitive-by-composition outputs, and style-as-policy shortcuts.
- [x] It routes policy to `policy/`, doctrine to `docs/`, machine shape to `schemas/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It avoids exact coordinates, restricted identifiers, redaction radii, grid sizes, geohash precision, reconstruction thresholds, and hidden policy values.
- [x] It marks executable scripts, registry wiring, sensitivity policy bundle homes, policy bundles, schema files, fixtures, tests, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to sensitivity validators are searched and classified.
- [ ] Accepted sensitivity/geoprivacy/redaction policy bundle homes, tier vocabulary authority, profile ids, and digest rules are verified.
- [ ] Receipt schemas and policy decision schemas are verified against actual validators and fixtures.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes and no reconstruction hints.
- [ ] Tests prove positive, negative, deny, restrict, hold, abstain, T0-overclaim, sensitive-by-composition, review-missing, receipt-missing, most-restrictive-failed, style-as-policy, and public-surface-blocked cases.
- [ ] CI invokes sensitivity validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with sensitivity validator parent README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
