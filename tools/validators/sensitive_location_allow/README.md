<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-sensitive-location-allow-readme
title: tools/validators/sensitive_location_allow README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-sensitive-location-steward-plus-geoprivacy-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward-plus-redaction-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; sensitive-location-allow-validator; allow-exception-check; deny-by-default-preserved; geoprivacy-aware; redaction-receipt-aware; review-required; release-gated; rollback-required; public-safe-derivative-only; non-authoritative
owning_root: tools/
responsibility: validator routing README for sensitive-location allow-exception checks under tools/validators; documents how an otherwise denied sensitive-location candidate may be allowed only when exact/internal geometry is absent from public surfaces, public-safe derivative posture is explicit, EvidenceRef and EvidenceBundle support resolves, policy decision and reason codes approve the scoped use, redaction/generalization/aggregation receipts resolve, steward review and rights/sensitivity obligations close, release/correction/rollback references exist, and public-surface leakage checks pass while deferring policy decisions, geoprivacy parameters, redaction transforms, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../sensitive_geometry/README.md
  - ../geoprivacy/README.md
  - ../geometry/README.md
  - ../geoprivacy_transform/README.md
  - ../policy/README.md
  - ../rights/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../maplibre/README.md
  - ../pmtiles/README.md
  - ../habitat/fauna-geoprivacy/README.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../docs/architecture/sensitive-domain-fail-closed.md
  - ../../../docs/standards/REDACTION_PROFILES.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../policy/decision/README.md
  - ../../../policy/geoprivacy/
  - ../../../policy/sensitivity/
  - ../../../policy/redaction/
  - ../../../schemas/contracts/v1/policy/
  - ../../../schemas/contracts/v1/receipts/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../data/quarantine/
  - ../../../data/published/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/sensitive_location_allow/README.md. It does not confirm executable allow validators, registry wiring, policy bundles, transform implementation, receipt emission, or CI behavior."
  - "The word allow in this path means allow-exception validation after the deny-by-default baseline. It must never be read as default allow, silent allow, or policy bypass."
  - "Sensitive exact-location and identifying release remain denied by default. Public use requires explicit, evidenced, reviewed, receipted, scoped, policy-allowed, release-linked, and rollback-supported approval."
  - "This lane must not store exact coordinates, restricted identifiers, redaction radii, grid sizes, geohash precision, reconstruction thresholds, hidden policy values, or other reverse-engineering hints."
  - "Style-only hiding is forbidden: an allowed public surface must receive public-safe derivatives, not exact/internal geometry hidden by zoom, opacity, filters, layers, or UI affordances."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/sensitive_location_allow

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-sensitive--location--allow--validator-informational)
![default](https://img.shields.io/badge/default-deny--by--default-critical)
![allow](https://img.shields.io/badge/allow-explicit--exception--only-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/sensitive_location_allow/` is the validator routing lane for proving that a sensitive-location candidate has satisfied every allow-exception precondition before any public-safe derivative can be shown; it does not make policy decisions, publish geometry, or weaken deny-by-default posture.

---

## Purpose

`tools/validators/sensitive_location_allow/` exists to validate the **exception path** for sensitive-location exposure.

The durable KFM question for this lane is:

> Has this sensitive-location candidate satisfied the explicit allow path — public-safe derivative only, no exact/internal geometry in public payloads, resolved EvidenceRef and EvidenceBundle support, finite PolicyDecision with reason codes and obligations, required review, redaction/generalization/aggregation receipts, rights/sensitivity closure, ReleaseManifest or release reference, correction path, rollback target, and public-surface leakage checks — for the exact scoped use being requested?

The answer should be a deterministic validation result or routing decision. This folder should not decide policy, define allow rules, name hidden thresholds, set geoprivacy parameters, store exact geometry, perform redaction transforms as authority, create receipts, create EvidenceBundles, write release records, approve release, publish map layers, expose public API payloads, or authorize AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/sensitive_location_allow/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md` | **CONFIRMED draft ADR / implementation NEEDS VERIFICATION** | States exact-location or identifying release is denied by default and allow requires explicit, evidenced, reviewed, receipted, scoped, rollback-supported approval. |
| `policy/decision/README.md` | **CONFIRMED policy README / runtime enforcement NEEDS VERIFICATION** | Decision outcomes are not truth by themselves; `ALLOW` still depends on evidence, authority, rights, sensitivity, validation, review, release state, receipts, and rollback support. |
| `tools/validators/habitat/fauna-geoprivacy/README.md` | **CONFIRMED example README / executable behavior NEEDS VERIFICATION** | Shows sensitive joins fail closed and public-safe geometry, receipt linkage, evidence, policy, release, correction, rollback, and public-surface denial must be preserved. |
| `tools/validators/sensitive_geometry/README.md` | **CONFIRMED sibling README / executable behavior NEEDS VERIFICATION** | Umbrella sensitive-geometry lane; this allow lane is narrower and checks the affirmative exception packet. |
| Executable sensitive-location allow scripts, registry wiring, schema bindings, policy bundles, redaction profiles, fixture coverage, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Allow is an exception, not the default

This validator lane must preserve the following rule:

> Sensitive-location exposure starts at `DENY`. A public-safe derivative may be allowed only when the required evidence, policy, review, receipt, rights, release, correction, rollback, and public-surface gates close for a scoped use.

Safe interpretation:

- **ALLOW** means a finite policy/release posture supports the exact scoped use.
- **ALLOW** does not mean public access to exact/internal/source geometry.
- **ALLOW** does not mean a reusable global permission.
- **ALLOW** does not mean AI, UI, map, export, screenshot, graph, tile, search, or embedding surfaces may improvise beyond the approved envelope.
- **ALLOW** can be revoked, superseded, corrected, withdrawn, narrowed, or rolled back.

[Back to top](#top)

---

## Allow-exception packet

A sensitive-location candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Candidate identity | Candidate id, source refs, domain/lane, object refs, artifact refs, lifecycle state, requested audience, requested operation, and requested public surface. | Global permission by candidate id. |
| Sensitivity classification | Sensitivity class, geoprivacy posture, exact/internal/public-safe geometry role, and most-restrictive upstream classification. | Sensitivity downgrade by validator. |
| Public-safe derivative | Public-bound payload contains only redacted, generalized, aggregated, suppressed, or other approved public-safe derivative geometry. | Exact geometry with styling or filtering. |
| Evidence support | EvidenceRef resolves to EvidenceBundle/proof support required for release-visible claims and artifacts. | Generated prose, map display, or tile presence as evidence. |
| Policy decision | Finite policy outcome, policy bundle id/version/digest, reason codes, obligations, scope, audience, expiry/reevaluation posture, and required next actions. | Local validator as policy authority. |
| Review support | Steward, sensitivity reviewer, rights reviewer, tribal/cultural reviewer, domain reviewer, or other required review bindings. | Hidden approval or default allow. |
| Transform receipt | RedactionReceipt, AggregationReceipt, RunReceipt, ValidationReport, or equivalent receipt references resolve and match input/output lineage. | Transform performed by this validator. |
| Rights and consent | License, rights, stewardship, consent, revocation, partner terms, and downstream obligations close for the intended use. | Public visibility as permission. |
| Release support | ReleaseManifest, promotion decision, correction path, withdrawal posture, rollback target, and supersession state exist where required. | Publication by validator success. |
| Public-surface envelope | Map/API/tile/export/screenshot/graph/search/Focus Mode/embedding/AI surfaces are limited to the approved derivative and obligations. | Unbounded reuse across all surfaces. |

[Back to top](#top)

---

## Allow invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Deny remains baseline | Allow is proven case-by-case and scope-by-scope. | Candidate assumes default allow or silent allow. |
| Exact geometry stays internal | Public surfaces receive only public-safe derivatives. | Public payload contains exact/internal/source geometry or reverse-engineerable detail. |
| Policy is explicit | Policy decision, bundle id/version/digest, reason codes, obligations, scope, and expiry are visible. | Allow is inferred from context, file placement, schema validity, or UI state. |
| Receipts close transforms | Transform receipts resolve and match input/output lineage. | Public-safe geometry appears without receipt support. |
| Evidence supports claims | EvidenceRef and EvidenceBundle resolve for release-visible claims. | Map/tile/export/AI text is treated as evidence. |
| Review is accountable | Required reviewers and tickets are visible. | Approval is missing, hidden, stale, or not bound to the candidate. |
| Rights and consent propagate | Rights, consent, stewardship, revocation, and obligations travel to derivatives and public surfaces. | Candidate drops upstream restrictions. |
| Release gates remain authoritative | Release/promotion/correction/rollback support is present where public exposure is requested. | Validator success is treated as release approval. |
| Side channels are checked | Bounds, counts, labels, ids, filenames, cache keys, errors, screenshots, tiles, graph edges, and AI answers do not reconstruct restricted places. | Output leaks location through derivative context. |

[Back to top](#top)

---

## Deny, restrict, abstain, or review conditions

A sensitive-location allow candidate should fail closed, deny, restrict, abstain, or route to steward review when:

- sensitivity class is unknown, missing, stale, contradicted, or unresolved;
- exact/internal/source geometry is present in a public-bound payload;
- the public-safe derivative is missing, unsupported, too precise, or reverse-engineerable;
- required EvidenceRef, EvidenceBundle, proof support, citation-validation, or validation report is missing or unresolved;
- policy decision, policy bundle id/version/digest, reason codes, obligations, scope, expiry, or reevaluation rule is missing or unsupported;
- required steward/domain/sensitivity/rights/cultural/tribal review is absent or stale;
- RedactionReceipt, AggregationReceipt, RunReceipt, transform receipt, or lineage support is missing or mismatched;
- rights, license, consent, stewardship, revocation, partner terms, or downstream obligations are unresolved;
- ReleaseManifest, PromotionDecision, rollback target, correction path, withdrawal posture, or supersession state is missing where required;
- map, tile, export, screenshot, search, graph, embedding, story, Focus Mode, popup, Evidence Drawer, or AI answer output can reconstruct or narrow a restricted place;
- any allow is broader than the requested scope, audience, operation, surface, time window, or release envelope.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Sensitive-location allow-exception validation | `tools/validators/sensitive_location_allow/` |
| Sensitive-geometry umbrella validation | `tools/validators/sensitive_geometry/` |
| Geoprivacy validation | `tools/validators/geoprivacy/` and accepted child lanes |
| Geometry carrier validation | `tools/validators/geometry/` |
| Policy validation | `tools/validators/policy/` |
| Rights validation | `tools/validators/rights/` |
| Release and promotion validation | `tools/validators/release/`, `tools/validators/promotion_gate/` |
| Map/tile public-surface validation | `tools/validators/maplibre/`, `tools/validators/pmtiles/` |
| Policy decision vocabulary and bundles | `policy/decision/`, `policy/geoprivacy/`, `policy/sensitivity/`, `policy/redaction/`, accepted policy homes |
| Redaction and geoprivacy standards | `docs/standards/REDACTION_PROFILES.md`, sensitive-domain docs, domain docs |
| Receipts, proofs, and evidence | `data/receipts/`, `data/proofs/` |
| Lifecycle data and quarantine | `data/` lifecycle roots, especially `data/quarantine/` for unresolved cases |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared allow-exception invariants and delegates policy decisions, transform parameters, geometry semantics, schemas, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, redaction profile homes, policy bundle homes, schema ids, fixture files, test paths, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as allowlist authority, policy authority, exact-geometry storage, public geometry store, redaction implementation authority, receipt store, proof store, release record store, canonical schema home, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/sensitive_location_allow/` include:

- this README;
- small validation adapters that check sensitive-location allow-exception packets;
- checks that public-safe derivatives are supported by receipts and release references;
- checks that policy decisions are finite, scoped, reason-coded, obligation-bearing, and tied to accepted bundle identity;
- checks that exact/internal geometry and reverse-engineerable derivatives are absent from public-bound payloads;
- checks that public-surface envelopes do not exceed approved audience, operation, time window, domain, or release scope;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Allowlists, policy rules, steward approvals, sensitivity decisions, geoprivacy thresholds, redaction parameters | `policy/`, steward review homes, release governance homes |
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
| `SENSITIVE_LOCATION_ALLOW_PASS` | Candidate passed configured allow-exception checks for the scoped use. |
| `SENSITIVE_LOCATION_ALLOW_FAIL` | Candidate failed one or more configured allow-exception checks. |
| `SENSITIVE_LOCATION_ALLOW_DENY` | Candidate must not proceed because policy, evidence, receipt, rights, review, release, rollback, or public-surface support cannot be resolved. |
| `SENSITIVE_LOCATION_ALLOW_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `SENSITIVE_LOCATION_ALLOW_ABSTAIN` | Candidate lacks enough support for an allow assertion. |
| `ALLOW_SCOPE_MISSING` | Requested audience, operation, surface, duration, or release envelope is absent. |
| `ALLOW_SCOPE_OVERBROAD` | Requested or produced allow exceeds approved scope. |
| `SENSITIVITY_CLASS_UNRESOLVED` | Sensitivity class is missing, stale, conflicted, or unknown. |
| `EXACT_LOCATION_PUBLIC_DENIED` | Public-bound payload contains exact/internal/source location detail. |
| `PUBLIC_SAFE_DERIVATIVE_MISSING` | Required public-safe derivative is absent. |
| `REDACTION_RECEIPT_MISSING` | Required redaction/generalization/aggregation/suppression receipt is absent. |
| `POLICY_DECISION_MISSING` | Required policy decision or policy bundle reference is absent. |
| `POLICY_DECISION_NOT_ALLOW` | Policy outcome is deny, restrict, hold, abstain, review-needed, error, stale, or otherwise not allow for this scope. |
| `REVIEW_BINDING_MISSING` | Required reviewer, steward, ticket, or separation-of-duties binding is absent. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent or unresolved. |
| `RIGHTS_OR_CONSENT_GAP` | Required rights, consent, stewardship, or revocation posture is unresolved. |
| `RELEASE_REFERENCE_MISSING` | Required release, correction, withdrawal, reevaluation, or rollback reference is absent. |
| `RECONSTRUCTION_RISK_DENIED` | Candidate can reconstruct or narrow sensitive location through derivative or side-channel exposure. |
| `STYLE_AS_POLICY_DENIED` | Candidate relies on styling, zoom, opacity, filter, or UI hiding instead of public-safe geometry. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose sensitive location to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/sensitive_location_allow/
├── README.md
├── validate_sensitive_location_allow.py # PROPOSED; not confirmed
├── validate_allow_packet.py             # PROPOSED; not confirmed
├── validate_allow_surface_scope.py      # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, policy bundles, allowlists, redaction profiles, local schema files, sensitive geometry payloads, public geometry payloads, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting public-surface or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/sensitive_location_allow/README.md`.
- [x] It makes clear that allow is an explicit exception path under a deny-by-default baseline.
- [x] It marks this path as allow-exception validation, not policy authority, allowlist authority, exact-geometry storage, redaction implementation authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves fail-closed posture for missing public-safe derivatives, missing receipts, unresolved policy/review/evidence/rights/release support, overbroad scope, reverse-engineering risk, and style-as-policy shortcuts.
- [x] It routes policy to `policy/`, geometry/redaction meaning to `contracts/` and docs, machine shape to `schemas/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It avoids exact coordinates, restricted identifiers, redaction radii, grid sizes, geohash precision, reconstruction thresholds, and hidden policy values.
- [x] It marks executable scripts, registry wiring, redaction profile homes, policy bundles, schema files, fixtures, tests, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to sensitive-location allow validators are searched and classified.
- [ ] Accepted geoprivacy/sensitivity/redaction policy bundle homes, allow-scope vocabulary, profile ids, and digest rules are verified.
- [ ] Receipt schemas and policy decision schemas are verified against actual validators and fixtures.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes and no reconstruction hints.
- [ ] Tests prove positive, negative, deny, restrict, abstain, overbroad-scope, receipt-missing, exact-location-denied, reconstruction-risk, style-as-policy, and public-surface-blocked cases.
- [ ] CI invokes sensitive-location allow validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with sensitive-location allow validator README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
