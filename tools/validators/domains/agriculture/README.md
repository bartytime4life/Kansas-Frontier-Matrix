<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-agriculture-readme
title: tools/validators/domains/agriculture README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-agriculture-steward-plus-cross-domain-steward-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; agriculture; cross-lane; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Agriculture validator index for edge-specific and cross-lane Agriculture validators under tools/validators/domains/agriculture while deferring broad Agriculture validator scope to tools/validators/agriculture and domain meaning to docs/contracts
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../agriculture/README.md
  - ./soil-join/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../../docs/domains/agriculture/README.md
  - ../../../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../../../docs/domains/agriculture/OBJECTS.md
  - ../../../../../docs/domains/agriculture/POLICY.md
  - ../../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../../../contracts/domains/agriculture/
  - ../../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../../policy/domains/agriculture/
  - ../../../../../data/proofs/evidence_bundle/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "Broad Agriculture-domain validator scope is already documented at tools/validators/agriculture/. This subtree is for narrower per-domain edge/cross-lane validators, not a competing Agriculture authority."
  - "Child README lanes currently confirmed here include soil-join/. Executable behavior remains NEEDS VERIFICATION unless verified separately."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/agriculture

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-agriculture--edge--validators-informational)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/agriculture/` is the proposed per-domain index for Agriculture edge-specific validators under `tools/validators/domains/`, including Agriculture × Soil joins and future Agriculture cross-lane checks.

---

## Purpose

`tools/validators/domains/agriculture/` exists to organize Agriculture validators that are too specific for shared `_common/` tooling and too edge-specific for the broad `tools/validators/agriculture/` parent lane.

The durable KFM question for this index is:

> Which Agriculture-specific edge validators live under the per-domain validator tree, and how do they preserve Agriculture authority, neighboring-domain authority, source-role discipline, sensitivity posture, evidence closure, release readiness, correction paths, and rollback support?

The answer should be a navigable validator index and deterministic validation outputs from child lanes. This folder should not create Agriculture truth, neighboring-domain truth, EvidenceBundles, policy decisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/agriculture/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Broad Agriculture validator parent | **CONFIRMED in repo evidence / draft** | `tools/validators/agriculture/README.md` documents broad Agriculture schema, source-rights, aggregation, sensitivity, evidence, lifecycle, and release-reference checks. |
| Child README lanes | **CONFIRMED README child / executable proposed** | `soil-join/` README exists for Agriculture × Soil join validation. |
| Agriculture cross-lane doctrine | **CONFIRMED in repo evidence / draft** | `docs/domains/agriculture/CROSS_LANE.md` defines Agriculture edge categories, source-role discipline, correction cascade, and Agriculture × Soil join posture. |
| Executables, schemas, fixtures, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Relationship to `tools/validators/agriculture/`

Use this split:

| Validator concern | Preferred lane |
|---|---|
| Broad Agriculture-domain validation | `tools/validators/agriculture/` |
| Agriculture schema/source-rights/sensitivity/aggregation/release readiness | `tools/validators/agriculture/` |
| Agriculture cross-lane or edge-specific validators | `tools/validators/domains/agriculture/<edge>/` |
| Agriculture × Soil MUKEY join validation | `tools/validators/domains/agriculture/soil-join/` |
| Cross-domain generic invariants | `tools/validators/cross-domain-joins/` |

This README does not move or rename the broad Agriculture validator lane. It makes the `domains/agriculture/` subtree inspectable so future edge-specific validators do not become orphan stubs.

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| `soil-join/` | Does an Agriculture candidate consume Soil-owned objects through governed EvidenceRefs, preserve MUKEY/COKEY/CHKEY identity, preserve source roles, produce only Agriculture-owned derivatives, and include evidence/policy/release/correction support? | README confirmed; executable proposed. |

Future child lanes should be added only when they represent a distinct Agriculture edge or cross-lane invariant with contracts, schemas, policy posture, fixtures, and report semantics. Avoid creating a child lane for every object family unless the validator has distinct boundary rules.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Agriculture edge-validator index | `tools/validators/domains/agriculture/` |
| Broad Agriculture validator lane | `tools/validators/agriculture/` |
| Agriculture × Soil validator | `tools/validators/domains/agriculture/soil-join/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Agriculture edge doctrine | `docs/domains/agriculture/CROSS_LANE.md` |
| Agriculture domain meaning | `docs/domains/agriculture/`, `contracts/domains/agriculture/` |
| Neighboring-domain meaning | owning neighboring-domain docs/contracts lanes |
| Schemas | `schemas/contracts/v1/domains/...` or ADR-selected homes |
| Policy rules | `policy/domains/...` or accepted policy homes |
| Source descriptors | `data/registry/sources/...` or accepted source registry homes |
| EvidenceBundles and proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/agriculture/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** edge-specific validator code may live below this folder when it checks declared Agriculture edge invariants and delegates meaning to owning domains.
- **NEEDS VERIFICATION:** exact executable names, schema homes, source descriptors, fixtures, policy bundles, report destinations, receipts, and CI wiring.
- **DENY:** using this folder as an Agriculture contract home, neighboring-domain contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, public runtime surface, field-level publication surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/agriculture/` include:

- this parent/index README;
- child README lanes for Agriculture cross-lane validators;
- optional parent runner code that delegates to child validators without redefining their rules;
- edge-specific validators that preserve owning-domain authority, source-role discipline, sensitivity posture, EvidenceRef/EvidenceBundle support, release references, correction cascade, and rollback support;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative domain doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/agriculture/` | Correct home |
|---|---|
| Broad Agriculture validator contract | `tools/validators/agriculture/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Agriculture domain docs | `docs/domains/agriculture/` |
| Agriculture or neighboring-domain contracts | `contracts/domains/...` |
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

## Edge-validator posture

Agriculture edge validators must fail closed, deny, abstain, or route to review when a candidate:

- consumes another domain's objects without preserving owning-domain identity;
- drops or relabels source role;
- turns aggregate or modeled records into observed truth;
- exposes field-level/operator-adjacent outputs without aggregation/redaction/review support;
- publishes or maps Agriculture derivatives without EvidenceBundle, policy, review, release, correction, and rollback support;
- bypasses lifecycle boundaries;
- treats validator output as release approval, proof closure, policy approval, or public authority.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `AG_DOMAIN_VALIDATORS_PASS` | Configured child validators passed. |
| `AG_DOMAIN_VALIDATORS_FAIL` | One or more configured child validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Agriculture child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `EDGE_PROFILE_MISSING` | Required Agriculture edge profile is absent. |
| `EDGE_PROFILE_CONFLICT` | Edge profiles disagree about owner, source role, sensitivity, evidence, or release posture. |
| `AUTHORITY_COLLAPSE` | Validator output or candidate collapses Agriculture and neighboring-domain authority. |
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
tests/validators/domains/agriculture/
├── README.md
├── test_agriculture_domain_validator_parent.py
└── fixtures/
    ├── valid_child_validator_bundle/
    ├── missing_child_validator/
    ├── conflicting_edge_profile/
    ├── authority_collapse/
    ├── invalid_report_destination/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/agriculture
```

```bash
python tools/validators/domains/agriculture/run_agriculture_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_agriculture_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Broad Agriculture validation remains in `tools/validators/agriculture/`.
- [ ] Child edge validators preserve owning-domain authority and source-role discipline.
- [ ] Field-level/public outputs require aggregation/redaction/review support.
- [ ] EvidenceBundle, policy, review, release, rollback, and correction support are checked where required.
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
| Review state | Draft README replacement for greenfield stub and parent index for Agriculture edge validators. |
| Next smallest safe change | Verify parent runner, child validator scripts, accepted edge profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, correction-cascade behavior, and CI wiring before promoting this lane beyond draft. |
