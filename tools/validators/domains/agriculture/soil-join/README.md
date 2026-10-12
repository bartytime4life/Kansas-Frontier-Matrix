<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-agriculture-soil-join-readme
title: tools/validators/domains/agriculture/soil-join README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-agriculture-steward-plus-soil-steward-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; agriculture-soil-join-validator; cross-lane; MUKEY; source-role-aware; release-gated
owning_root: tools/
responsibility: proposed Agriculture x Soil join validator lane for MUKEY/COKEY/CHKEY preservation, Soil-owned evidence references, Agriculture-owned SoilCropSuitability derivatives, source-role anti-collapse, sensitivity posture, evidence closure, correction cascade, release readiness, and public-surface denial checks
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../../README.md
  - ../../../_common/README.md
  - ../../README.md
  - ../../../../agriculture/README.md
  - ../../../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../../../docs/domains/agriculture/OBJECTS.md
  - ../../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../../../docs/domains/agriculture/POLICY.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../contracts/domains/agriculture/
  - ../../../../../contracts/domains/soil/
  - ../../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../../schemas/contracts/v1/domains/soil/
  - ../../../../../policy/domains/agriculture/
  - ../../../../../policy/domains/soil/
  - ../../../../../data/proofs/evidence_bundle/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README documents a proposed Agriculture x Soil join validator lane. It does not confirm executable files."
  - "Agriculture consumes Soil-owned objects by EvidenceRef. Agriculture MUST NOT re-publish Soil objects as Agriculture canonical truth."
  - "The load-bearing Agriculture x Soil join key is MUKEY; unresolved MUKEY should produce ABSTAIN rather than fabricated suitability or snapped geometry."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Agriculture meaning, Soil meaning, EvidenceBundle content, policy rules, release decisions, or public products."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/agriculture/soil-join

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-agriculture--soil--join-informational)
![join](https://img.shields.io/badge/join-MUKEY-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/agriculture/soil-join/` is the proposed validator lane for Agriculture × Soil joins: MUKEY/COKEY/CHKEY preservation, Soil-owned evidence references, Agriculture-owned `SoilCropSuitability` derivatives, source-role preservation, sensitivity posture, evidence closure, correction cascade, release readiness, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/agriculture/soil-join/` exists for validator logic that checks the Agriculture × Soil edge without collapsing either side's authority.

The durable KFM question for this lane is:

> Does an Agriculture candidate consume Soil-owned objects through governed EvidenceRefs, preserve MUKEY/COKEY/CHKEY identity, preserve source roles, produce only Agriculture-owned derivatives, and include the evidence, policy, review, release, correction, and rollback support required for its intended surface?

The answer should be a deterministic validation result. It should not create Agriculture truth, Soil truth, SoilMapUnit truth, field-level truth, suitability truth, EvidenceBundles, policy decisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/agriculture/soil-join/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| `tools/validators/domains/README.md` | **CONFIRMED stub** | Parent file currently says only `# Per-domain validators`; this README is self-bounded. |
| Agriculture validator parent | **CONFIRMED in repo evidence / draft** | `tools/validators/agriculture/README.md` names `SoilCropSuitability` references to Soil-owned MUKEY semantics as a valid agriculture validator concern. |
| Agriculture × Soil edge doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/agriculture/CROSS_LANE.md` defines Agriculture × Soil as consume-from-owner, with MUKEY as the load-bearing join key. |
| Paired schemas, fixtures, and CI wiring | **NEEDS VERIFICATION** | Exact schema paths, fixture paths, validator names, policy bundles, and CI integration must be verified before implementation claims. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Agriculture × Soil join validator entrypoints | `tools/validators/domains/agriculture/soil-join/` |
| Agriculture validator parent lane | `tools/validators/agriculture/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Agriculture × Soil edge doctrine | `docs/domains/agriculture/CROSS_LANE.md` |
| Agriculture domain meaning | `docs/domains/agriculture/`, `contracts/domains/agriculture/` |
| Soil domain meaning and Soil-owned objects | `docs/domains/soil/`, `contracts/domains/soil/` |
| Agriculture and Soil schemas | `schemas/contracts/v1/domains/agriculture/`, `schemas/contracts/v1/domains/soil/`, or ADR-selected homes |
| Policy rules | `policy/domains/agriculture/`, `policy/domains/soil/`, or accepted policy homes |
| Source descriptors | `data/registry/sources/agriculture/`, `data/registry/sources/soil/`, or accepted source registry homes |
| EvidenceBundles and proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/agriculture/soil-join/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks Agriculture × Soil join invariants and delegates meaning to the owning domains.
- **NEEDS VERIFICATION:** exact executable names, schema homes, source descriptors, fixtures, policy bundles, report destinations, receipts, and CI wiring.
- **DENY:** using this folder as an Agriculture contract home, Soil contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, public runtime surface, field-level publication surface, or domain-meaning authority.

[Back to top](#top)

---

## Join invariants

| Invariant | Validator expectation | Fail condition |
|---|---|---|
| Soil ownership preserved | Soil objects remain Soil-owned and are cited by EvidenceRef. | SoilMapUnit, SoilComponent, Horizon, SoilProperty, Hydrologic Soil Group, Pedon, or SuitabilityRating is re-published as Agriculture canonical truth. |
| Agriculture derivative preserved | Agriculture may produce `SoilCropSuitability` as an Agriculture-owned derivative. | Suitability output is presented as raw Soil truth or as an unreviewed field-level public fact. |
| MUKEY resolves | MUKEY is preserved verbatim from Soil admission and resolves for the join. | MUKEY is missing, malformed, fabricated, snapped from geometry only, or unresolved. |
| Source role preserved | Soil `observed`, `regulatory`, `modeled`, `aggregate`, or candidate roles remain visible across the join. | Pedon observed data or SSURGO regulatory context is relabeled as generic Agriculture modeled truth without side-specific role support. |
| Sensitivity preserved | Public output stays aggregate/public-safe; field-level joins follow deny-default posture. | Field-level/operator/private joins are surfaced publicly without aggregation/redaction/review support. |
| Evidence and release support | Public-bound suitability output carries EvidenceBundle, policy, review, release, correction, and rollback references where required. | Output is published, mapped, exported, or summarized without required trust artifacts. |

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/agriculture/soil-join/` include checks that:

- validate MUKEY presence, shape, and resolvability for Agriculture × Soil joins;
- preserve COKEY and CHKEY where component/horizon joins are material;
- reject geometry-only joins that invent Soil identity without governed Soil evidence;
- require Agriculture candidates to cite Soil-owned EvidenceRefs instead of copying Soil objects into Agriculture authority;
- require `SoilCropSuitability` to remain an Agriculture-owned derivative with clear modeled/derived posture;
- preserve Soil source-role labels, especially observed Pedon data and regulatory Hydrologic Soil Group context;
- require AggregationReceipt or RedactionReceipt before field-level or sensitive joins reach public surfaces;
- downgrade or abstain when Soil-side CorrectionNotice, revocation, stale source, or unresolved EvidenceBundle invalidates the join;
- check release references, rollback targets, and correction propagation for public-bound suitability products.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/agriculture/soil-join/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| General Agriculture validator parent content | `tools/validators/agriculture/` |
| Agriculture contracts | `contracts/domains/agriculture/` |
| Soil contracts | `contracts/domains/soil/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, or receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, export, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Soil-join validation posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks MUKEY for a join that depends on Soil map-unit identity;
- derives Soil identity only from geometry overlap;
- re-publishes Soil objects as Agriculture canonical truth;
- hides Soil source role, source authority, or time posture;
- relabels observed or regulatory Soil evidence into generic Agriculture modeled output;
- creates public field-level or operator-adjacent outputs without aggregation/redaction/review support;
- maps or exports `SoilCropSuitability` without evidence, policy, review, release, correction, and rollback support;
- fails to propagate Soil-side corrections into Agriculture derivatives.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `AG_SOIL_JOIN_PASS` | Configured Agriculture × Soil join checks passed. |
| `AG_SOIL_JOIN_FAIL` | Configured checks failed. |
| `MUKEY_MISSING` | Required MUKEY is absent. |
| `MUKEY_MALFORMED` | MUKEY is present but invalid under the configured profile. |
| `MUKEY_UNRESOLVED` | MUKEY does not resolve to governed Soil support. |
| `GEOMETRY_ONLY_JOIN_DENIED` | Candidate uses spatial overlap as identity without Soil evidence. |
| `SOIL_OWNERSHIP_COLLAPSE` | Candidate re-publishes Soil-owned objects as Agriculture canonical truth. |
| `SOURCE_ROLE_COLLAPSE` | Candidate drops or relabels Soil source role. |
| `SENSITIVITY_DOWNGRADE` | Candidate lowers sensitivity or exposes field/operator-adjacent joins publicly. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `UPSTREAM_SOIL_REVOKED` | Soil-side correction or revocation invalidates the downstream Agriculture derivative. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, rollback target, or correction path is absent. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/agriculture/soil-join/
├── README.md
├── test_agriculture_soil_join.py
└── fixtures/
    ├── valid_mukey_join/
    ├── missing_mukey/
    ├── malformed_mukey/
    ├── unresolved_mukey/
    ├── geometry_only_join_denied/
    ├── soil_ownership_collapse/
    ├── source_role_collapse/
    ├── field_level_public_join_denied/
    ├── upstream_soil_revoked/
    └── missing_release_reference/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/agriculture/soil-join
```

```bash
python tools/validators/domains/agriculture/soil-join/validate_agriculture_soil_join.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_agriculture_soil_join.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Agriculture and Soil contracts rather than defining meaning locally.
- [ ] Validator reads declared schemas and policy rather than defining shape or policy locally.
- [ ] Soil objects remain Soil-owned and are consumed through EvidenceRefs.
- [ ] `SoilCropSuitability` remains an Agriculture-owned derivative.
- [ ] MUKEY resolves before the join is treated as usable.
- [ ] COKEY and CHKEY are preserved where component/horizon joins are material.
- [ ] Source-role and time posture are preserved across the join.
- [ ] Field-level/public outputs require aggregation/redaction/review support.
- [ ] EvidenceBundle, policy, review, release, rollback, and correction support are checked where required.
- [ ] Soil-side correction cascade causes downstream Agriculture derivatives to abstain or refresh.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify actual validator scripts, schema paths, Soil/Agriculture source descriptors, policy bundles, fixtures, receipts, report destinations, correction-cascade behavior, and CI wiring before promoting this lane beyond draft. |
