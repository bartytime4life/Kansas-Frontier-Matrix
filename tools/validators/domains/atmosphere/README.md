<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-atmosphere-readme
title: tools/validators/domains/atmosphere README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-atmosphere-steward-plus-cross-domain-steward-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator-index; atmosphere; cross-lane; source-role-aware; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Atmosphere validator index for edge-specific and specialty Atmosphere validators under tools/validators/domains/atmosphere while deferring domain meaning to docs/contracts and broader cross-domain invariants to their existing validator lanes
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ./smoke/README.md
  - ../../air-hazards/README.md
  - ../../atmosphere_agriculture/README.md
  - ../../atmosphere_biodiversity/README.md
  - ../../atmosphere_hazards/README.md
  - ../../atmosphere_hydrology/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../../docs/domains/atmosphere/README.md
  - ../../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../../../docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - ../../../../../docs/domains/atmosphere/POLICY.md
  - ../../../../../docs/domains/atmosphere/SOURCES.md
  - ../../../../../docs/domains/atmosphere/PIPELINE.md
  - ../../../../../contracts/domains/atmosphere/
  - ../../../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../../../policy/domains/atmosphere/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "Existing cross-domain Atmosphere validator lanes include atmosphere_hydrology, atmosphere_agriculture, atmosphere_biodiversity, atmosphere_hazards, and air-hazards. This subtree is for narrower per-domain child or specialty validators, not a competing Atmosphere authority."
  - "Child README lanes currently confirmed here include smoke/. Executable behavior remains NEEDS VERIFICATION unless verified separately."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/atmosphere

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-atmosphere--child--validators-informational)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/atmosphere/` is the proposed per-domain index for narrow Atmosphere child, edge, and specialty validators under `tools/validators/domains/`, including the `smoke/` validator lane.

---

## Purpose

`tools/validators/domains/atmosphere/` exists to organize Atmosphere validators that are too specific for shared `_common/` tooling and too specialized for the existing cross-domain Atmosphere validator lanes.

The durable KFM question for this index is:

> Which Atmosphere-specific child validators live under the per-domain validator tree, and how do they preserve Atmosphere authority, neighboring-domain authority, source-role discipline, freshness posture, sensitivity posture, evidence closure, release readiness, correction paths, rollback support, and public-surface denial boundaries?

The answer should be a navigable validator index and deterministic validation outputs from child lanes. This folder should not create Atmosphere truth, neighboring-domain truth, advisory authority, alert authority, EvidenceBundles, policy decisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/atmosphere/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps its own boundary explicit. |
| Child README lanes | **CONFIRMED README child / executable proposed** | `smoke/` README exists for Atmosphere smoke validation. |
| Existing cross-domain Atmosphere validator lanes | **CONFIRMED README siblings / executable proposed** | README lanes exist for `air-hazards/`, `atmosphere_agriculture/`, `atmosphere_biodiversity/`, `atmosphere_hazards/`, and `atmosphere_hydrology/`; executable behavior remains unverified. |
| Atmosphere smoke lane | **CONFIRMED in repo evidence / draft** | `smoke/README.md` defines `SmokeContext`, `AODRaster`, source-role, freshness, Hazards seam, sensitive-join, release, and public-surface checks. |
| Executables, schemas, fixtures, policy bundles, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Relationship to existing Atmosphere validator lanes

Use this split:

| Validator concern | Preferred lane |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Hazards smoke, fire, and alert-authority seam checks | `tools/validators/air-hazards/`, `tools/validators/atmosphere_hazards/`, and `tools/validators/domains/atmosphere/smoke/` depending on scope |
| Atmosphere/Hydrology precipitation, drought, and flood-weather forcing checks | `tools/validators/atmosphere_hydrology/` |
| Atmosphere/Agriculture weather, heat, smoke, vegetation-stress context checks | `tools/validators/atmosphere_agriculture/` |
| Atmosphere/Biodiversity or ecology context checks | `tools/validators/atmosphere_biodiversity/` |
| Narrow Atmosphere child or specialty validators | `tools/validators/domains/atmosphere/<child>/` |
| Generic cross-domain invariants | `tools/validators/cross-domain-joins/` |

This README does not move or rename any existing Atmosphere cross-domain validator lane. It makes the `domains/atmosphere/` subtree inspectable so future child validators do not become orphan greenfield stubs.

[Back to top](#top)

---

## Child lanes

| Child lane | Validator question | Status |
|---|---|---|
| `smoke/` | Does an Atmosphere smoke candidate preserve source role, product type, time/freshness, uncertainty, rights, sensitivity, Hazards seam boundaries, evidence support, policy posture, release readiness, correction paths, and rollback support before it reaches a governed surface? | README confirmed; executable proposed. |

Future child lanes should be added only when they represent a distinct Atmosphere specialty, edge, fixture family, or public-surface invariant with accepted contracts, schemas, policy posture, fixtures, receipts, and report semantics. Avoid creating a child lane for every object family unless the validator has distinct boundary rules.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Atmosphere child-validator index | `tools/validators/domains/atmosphere/` |
| Atmosphere smoke validator | `tools/validators/domains/atmosphere/smoke/` |
| Existing cross-domain Atmosphere validator lanes | `tools/validators/air-hazards/`, `tools/validators/atmosphere_*`, accepted validator lanes |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Atmosphere domain meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Neighboring-domain meaning | owning neighboring-domain docs/contracts lanes |
| Schemas | `schemas/contracts/v1/domains/atmosphere/` or ADR-selected homes |
| Policy rules | `policy/domains/atmosphere/` or accepted policy homes |
| Source descriptors | `data/registry/sources/atmosphere/` or accepted source registry homes |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/atmosphere/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** child validator code may live below this folder when it checks declared Atmosphere invariants and delegates meaning, source roles, policy, evidence, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, source descriptors, fixtures, policy bundles, report destinations, receipts, runtime behavior, and CI wiring.
- **DENY:** using this folder as Atmosphere contract home, neighboring-domain contract home, schema home, policy home, source registry, evidence store, lifecycle data store, receipt store, release record store, public runtime surface, alert surface, health/safety surface, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/atmosphere/` include:

- this parent/index README;
- child README lanes for narrow Atmosphere validator families;
- optional parent runner code that delegates to child validators without redefining their rules;
- specialty validators that preserve source-role discipline, knowledge-character separation, freshness windows, sensitivity posture, cross-lane authority, EvidenceRef/EvidenceBundle support, release references, correction cascade, and rollback support;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Atmosphere doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/atmosphere/` | Correct home |
|---|---|
| Shared validator plumbing | `tools/validators/_common/` |
| General cross-domain Atmosphere validator logic already covered elsewhere | existing `tools/validators/atmosphere_*` lanes |
| Atmosphere domain docs | `docs/domains/atmosphere/` |
| Atmosphere or neighboring-domain contracts | `contracts/domains/...` |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, or receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Public API, UI, map, export, tile, alert, health/safety, or AI runtime code | governed application/runtime roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Atmosphere child-validator posture

Atmosphere child validators must fail closed, deny, abstain, or route to review when a candidate:

- lacks source role, knowledge-character label, product lineage, or time/freshness posture;
- collapses observation, model field, remote-sensing mask, advisory context, regulatory archive, or public report into another role;
- claims KFM issues, confirms, or replaces an emergency alert or life-safety source;
- offers unsupported health, exposure, impact, evacuation, emergency-action, or regulatory advice;
- joins Atmosphere context to sensitive places, assets, people/land, habitat, infrastructure, archaeology, or rare-species surfaces without policy/review/release support;
- maps, exports, tiles, summarizes, or answers with Atmosphere context without EvidenceBundle, policy, review, release, correction, and rollback support;
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
| `ATMO_DOMAIN_VALIDATORS_PASS` | Configured child validators passed. |
| `ATMO_DOMAIN_VALIDATORS_FAIL` | One or more configured child validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Atmosphere child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `SOURCE_ROLE_MISSING` | Required source-role or knowledge-character label is absent. |
| `ROLE_COLLAPSE` | Observation, model, mask, advisory, regulatory, or public-report role is collapsed. |
| `FRESHNESS_WINDOW_EXPIRED` | Source, model, advisory, or report is stale for the claimed use. |
| `ALERT_AUTHORITY_DENIED` | Candidate presents KFM as alert authority or life-safety source. |
| `SENSITIVE_JOIN_DENIED` | Sensitive Atmosphere join is unsafe without review/release controls. |
| `EVIDENCE_OR_RELEASE_GAP` | Required evidence, review, release, correction, or rollback reference is absent. |
| `AUTHORITY_COLLAPSE` | Validator output or candidate collapses Atmosphere and neighboring-domain authority. |
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
tests/validators/domains/atmosphere/
├── README.md
├── test_atmosphere_domain_validator_parent.py
└── fixtures/
    ├── valid_child_validator_bundle/
    ├── missing_child_validator/
    ├── source_role_missing/
    ├── role_collapse/
    ├── stale_context_denied/
    ├── alert_authority_denied/
    ├── sensitive_join_denied/
    ├── evidence_or_release_gap/
    ├── authority_collapse/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/atmosphere
```

```bash
python tools/validators/domains/atmosphere/run_atmosphere_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_atmosphere_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Existing cross-domain Atmosphere validator lanes remain intact.
- [ ] Child validators preserve Atmosphere meaning, neighboring-domain meaning, source roles, and policy authority boundaries.
- [ ] Observation, model, mask, advisory, regulatory, and public-report roles remain distinct.
- [ ] Freshness windows and source times are visible for current-sensitive claims.
- [ ] KFM is never presented as alert authority or life-safety source.
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
| Review state | Draft README replacement for greenfield stub and parent index for Atmosphere child validators. |
| Next smallest safe change | Verify parent runner, child validator scripts, accepted specialty profiles, schemas, source descriptors, policy bundles, fixtures, report destinations, receipts, freshness thresholds, sensitive-join behavior, and CI wiring before promoting this lane beyond draft. |
