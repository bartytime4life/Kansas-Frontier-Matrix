<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/dashboards-domain-atmosphere
title: Atmosphere / Air Dashboard Specification
type: standard
version: v0.2
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: Atmosphere steward + UI steward + evidence steward
created: 2026-05-26
updated: 2026-08-21
policy_label: public
owning_root: docs/
responsibility: Dashboard specification and repository-state reporting only; not domain, policy, runtime, release, or publication authority.
truth_posture: CONFIRMED repository evidence; PROPOSED or UNKNOWN implementation claims; cite or abstain.
related:
  - ./README.md
  - ../DASHBOARD_CATALOG.md
  - ../../domains/atmosphere/README.md
  - ../../../apps/explorer-web/src/features/domains/atmosphere/README.md
  - ../../../contracts/domains/atmosphere/pm_sensor_trust_profile.md
  - ../../../schemas/contracts/v1/domains/atmosphere/pm_sensor_trust_profile.schema.json
  - ../../../policy/domains/atmosphere/README.md
  - ../../../tests/validators/domains/atmosphere/test_pm_sensor_trust_profile.py
tags: [kfm, dashboards, domain, atmosphere, air, evidence, governed-ai, specification]
notes:
  - This is a dashboard specification, not a running dashboard, policy decision, release record, or publication surface.
  - Current repository evidence confirms bounded Atmosphere contracts, schemas, policies, fixtures, validators, tests, and one Explorer Evidence Drawer convergence seam; a complete dashboard and telemetry binding remain unverified.
  - The deleted domain/air PM Sensor Calibration Review specification is not restored. Its surviving fixture-only trust-profile packet is referenced directly.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere / Air Dashboard Specification

> A repository-grounded specification for reporting Atmosphere/Air evidence, validation, model-versus-observation, correction, and governed-AI posture without becoming source, policy, alert, release, or publication authority.

> [!IMPORTANT]
> **Truth posture:** this file and the repository surfaces linked below are `CONFIRMED` at the pinned repository snapshot. Dashboard routes, telemetry feeds, metric thresholds, stewardship assignments, and public runtime behavior remain `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION` as labeled.

> [!CAUTION]
> KFM Atmosphere surfaces provide evidence-backed context only. They do not issue emergency instructions, replace an official advisory source, treat AQI as concentration, treat AOD as PM2.5, treat model output as an observation, or promote a low-cost sensor to reference-grade authority.

## Contents

1. [Domain scope](#1-domain-scope)
2. [Indicator subset](#2-indicator-subset)
3. [Domain-specific indicators](#3-domain-specific-indicators-proposed)
4. [Ownership](#4-ownership)
5. [Implementation pointer](#5-implementation-pointer)
6. [Review cadence](#6-review-cadence)
7. [Open questions](#7-open-questions)
8. [Evidence basis and citations](#8-evidence-basis--citations)
9. [Finite outcomes and safety boundary](#9-finite-outcomes-and-safety-boundary)
10. [PM-sensor compatibility note](#10-pm-sensor-compatibility-note)
11. [Validation](#11-validation)
12. [Maintenance and rollback](#12-maintenance-and-rollback)

---

## 1. Domain scope

This specification describes a read-only review surface for Atmosphere/Air governance health. It may summarize evidence and validator results for air observations, weather observations, smoke and AOD context, climate products, atmospheric model context, and fixture-only PM-sensor trust declarations.

It does not own the underlying objects or their admissibility.

| Concern | Owning surface | Dashboard relationship |
|---|---|---|
| Domain meaning, source roles, sensitivity, and publication posture | [`docs/domains/atmosphere/`](../../domains/atmosphere/README.md) | Read and summarize; do not redefine. |
| Semantic object meaning | [`contracts/domains/atmosphere/`](../../../contracts/domains/atmosphere/README.md) | Link the contract version represented by a signal. |
| Machine shape | [`schemas/contracts/v1/domains/atmosphere/`](../../../schemas/contracts/v1/domains/atmosphere/README.md) | Validate payload shape before presentation. |
| Admissibility | [`policy/domains/atmosphere/`](../../../policy/domains/atmosphere/README.md) | Display finite policy outcomes; do not decide them in the UI. |
| Executable evidence | [`tools/validators/domains/atmosphere/`](../../../tools/validators/domains/atmosphere/) and [`tests/validators/domains/atmosphere/`](../../../tests/validators/domains/atmosphere/) | Report bounded results with their fixture or artifact identity. |
| UI composition | [`apps/explorer-web/`](../../../apps/explorer-web/README.md) and a future verified review surface | Render governed envelopes; do not read canonical/internal stores directly. |
| Release, correction, and rollback | [`release/`](../../../release/README.md) | Display released state only when a governing record exists. |

The lifecycle shorthand remains `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. A dashboard, green test, badge, screenshot, commit, or pull request does not perform a lifecycle promotion.

[Back to top](#top)

---

## 2. Indicator subset

Numeric service objectives and alert thresholds are not established by this document. Until a threshold has an adopted owner and evidence source, the dashboard should expose the measured value and its support state without inventing a healthy/unhealthy cutoff.

| Indicator family | Required presentation | Current evidence | Dashboard status |
|---|---|---|---|
| Evidence closure | Show whether each claim-bearing item resolves from `EvidenceRef` to `EvidenceBundle`, including validation and correction state. | Atmosphere EvidenceBundle schema, validator, fixtures, tests, and convergence workflow are present. | Signal binding `PROPOSED`; full route `UNKNOWN`. |
| Observation/model separation | Keep observed, modeled, remote-sensing, advisory, and derived-fusion roles visible and non-interchangeable. | Atmosphere contracts, schemas, policies, and focused negative tests are present. | Rules `CONFIRMED`; dashboard enforcement `NEEDS VERIFICATION`. |
| Source and time posture | Show source role, observed/valid/retrieved/released time as applicable, freshness, and limitations. | Domain documentation and object families are present. | Telemetry and thresholds `NEEDS VERIFICATION`. |
| Policy outcomes | Preserve `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` without coercing a negative state into a successful result. | Atmosphere policy files and finite-outcome tests are present. | Runtime binding `NEEDS VERIFICATION`. |
| Governed-AI posture | For generated summaries, show evidence handles, model/run context when relevant, and the AI receipt or an explicit absence state. | AIReceipt contract, schemas, validator, and fixtures exist outside this dashboard lane. | Atmosphere dashboard integration `PROPOSED`. |
| PM-sensor trust dimensions | Present accuracy, stability, responsiveness, consensus alignment, calibration context, reference-anchor state, and a finite assessment without a composite score. | Fixture-only PM trust contract, schema, fixtures, validator, and tests are present. | `CONFIRMED` synthetic packet; live evaluation and dashboard `DENY`/`UNKNOWN`. |
| Explorer evidence presentation | Surface governed evidence-drawer results while preserving finite states and source limits. | Atmosphere re-export, payload schema, focused convergence test, receipt, and workflow are present. | Bounded seam `CONFIRMED`; complete Atmosphere dashboard `UNKNOWN`. |

> [!NOTE]
> A passing fixture or convergence test proves only its declared contract. It does not admit a live source, establish scientific validity, authorize an alert, approve review, release an artifact, or publish a dashboard.

[Back to top](#top)

---

## 3. Domain-specific indicators (PROPOSED)

These are candidate dashboard views, not adopted thresholds or verified runtime panels.

| Candidate indicator | Question answered | Required evidence or negative state |
|---|---|---|
| Model-context completeness | Is a forecast/model item clearly labeled with its run, valid time, source role, limitations, and evidence support? | Supported context, otherwise `ABSTAIN` or `DENY`. |
| Observed/modeled separation | Has any modeled, remote-sensing, advisory, or derived item been presented as an observation? | Zero silent collapse; violations are `DENY`/`ERROR`. |
| PM trust-dimension resolution | Which fixture-only trust dimensions are measured or unresolved, and is the calibration/reference-anchor context internally consistent? | Preserve `QUALIFIED_CONTEXT`, `HOLD`, or `DENY`; never synthesize a composite score. |
| Evidence Drawer convergence | Does the Atmosphere payload resolve through the shared Evidence Drawer contract with deterministic finite outcomes? | Focused schema/test/workflow result plus exact payload identity. |
| Correction visibility | Does a displayed item expose correction, supersession, and rollback context when those records exist? | `CorrectionNotice`, release identity, or explicit not-applicable/unknown state. |
| Cite-or-abstain coverage | Does each generated Atmosphere summary carry resolvable evidence support or abstain? | Evidence handles and AI receipt, otherwise `ABSTAIN`; policy blocks remain `DENY`. |

[Back to top](#top)

---

## 4. Ownership

No repository evidence inspected for this update establishes named Atmosphere, dashboard, AI-surface, or evidence stewards for this path.

| Responsibility | Required decision | Current state |
|---|---|---|
| Atmosphere steward | Approves domain meaning and source-role interpretation. | `OWNER_TBD` / `NEEDS VERIFICATION` |
| UI or dashboard steward | Owns the implemented route, panels, accessibility, and operational maintenance. | `OWNER_TBD` / `NEEDS VERIFICATION` |
| Evidence/validation steward | Owns signal binding to exact validator, fixture, proof, and correction identities. | `OWNER_TBD` / `NEEDS VERIFICATION` |
| Policy/sensitivity reviewer | Reviews denial, rights, advisory, and harmful-precision boundaries. | Role required when applicable; identity `UNKNOWN` |

Documentation authorship and a generated receipt do not satisfy these review roles.

[Back to top](#top)

---

## 5. Implementation pointer

Current repository bytes support a partial implementation picture rather than a single running dashboard claim.

| Surface | Repository evidence | Status and limit |
|---|---|---|
| Atmosphere dashboard specification | [`atmosphere.md`](./atmosphere.md) | `CONFIRMED` document; implementation authority absent. |
| Explorer Atmosphere feature boundary | [`README.md`](../../../apps/explorer-web/src/features/domains/atmosphere/README.md) | `CONFIRMED` feature documentation; several claims in that README require repinning against current code. |
| Evidence Drawer seam | [`EvidenceDrawer.tsx`](../../../apps/explorer-web/src/features/domains/atmosphere/EvidenceDrawer.tsx), [payload schema](../../../schemas/contracts/v1/domains/atmosphere/evidence_drawer_payload.schema.json), [focused test](../../../tests/validators/domains/atmosphere/test_evidence_drawer_convergence.py), and [workflow](../../../.github/workflows/atmosphere-evidence-drawer-convergence.yml) | `CONFIRMED` bounded re-export and convergence packet; not a complete dashboard. |
| Atmosphere layers | [`layers.ts`](../../../apps/explorer-web/src/features/domains/atmosphere/layers.ts) | `CONFIRMED` placeholder only; no layer implementation claim. |
| Atmosphere Focus Flow | [`FocusFlow.tsx`](../../../apps/explorer-web/src/features/domains/atmosphere/FocusFlow.tsx) | `CONFIRMED` placeholder only; no governed-AI route claim. |
| Review Console | [`apps/review-console/`](../../../apps/review-console/README.md) | App exists, but no Atmosphere-specific file was found at the pinned snapshot; dashboard route `UNKNOWN`. |
| PM-sensor trust packet | [contract](../../../contracts/domains/atmosphere/pm_sensor_trust_profile.md), [schema](../../../schemas/contracts/v1/domains/atmosphere/pm_sensor_trust_profile.schema.json), [fixtures](../../../fixtures/contracts/v1/domains/atmosphere/pm_sensor_trust_profile/cases.json), [validator](../../../tools/validators/domains/atmosphere/validate_pm_sensor_trust_profile.py), and [tests](../../../tests/validators/domains/atmosphere/test_pm_sensor_trust_profile.py) | `CONFIRMED` proposed-inactive, fixture-only packet; no live sensor or public-health authority. |
| Telemetry | No `runtime/observability/` or Atmosphere dashboard telemetry path was found at the pinned snapshot. | `UNKNOWN`; do not infer absence across external systems. |

[Back to top](#top)

---

## 6. Review cadence

Review is event-driven until a steward adopts a periodic cadence.

| Trigger | Required review |
|---|---|
| Contract, schema, policy, fixture, validator, or finite-outcome change | Reconcile the affected indicator and its evidence link. |
| Atmosphere UI route, panel, layer, Focus Flow, or telemetry implementation | Replace the corresponding `UNKNOWN`/`PROPOSED` state with exact implementation and test evidence. |
| Source terms, rights, cadence, model family, correction method, or reference-anchor change | Reassess admissibility, limitations, stale-state handling, and public-safe presentation. |
| Correction, supersession, withdrawal, or rollback | Ensure every affected surface exposes the governing record and invalidates stale derivatives. |
| Alert-like or public-health presentation proposal | Require Atmosphere, Hazards, policy, and sensitivity review; fail closed until resolved. |
| Dashboard catalog change | Recompute file presence from a pinned tree and repair direct references. |

[Back to top](#top)

---

## 7. Open questions

- [ ] **OPEN-DASH-ATMOS-01** — Identify the Atmosphere, UI, evidence, and policy review roles for this specification.
- [ ] **OPEN-DASH-ATMOS-02** — Verify whether a review-console or Explorer route will own the operational dashboard; do not create two writable dashboard authorities.
- [ ] **OPEN-DASH-ATMOS-03** — Define telemetry contracts and policy-owned thresholds without moving metric authority into this document.
- [ ] **OPEN-DASH-ATMOS-04** — Define the governed-AI forecast/model summary boundary, including model/run context and AIReceipt visibility.
- [ ] **OPEN-DASH-ATMOS-05** — Decide whether the fixture-only PM trust packet should ever feed a review surface; live sensor evaluation, scientific thresholds, and reference-grade equivalence remain out of scope.
- [ ] **OPEN-DASH-ATMOS-06** — Reconcile the proposed `docs/dashboards/` lane with accepted Directory Rules before any structural migration.
- [ ] **OPEN-DASH-ATMOS-07** — Verify external source terms, rights, freshness, and redistribution constraints before presenting current source coverage.

[Back to top](#top)

---

<a id="8-evidence-basis--citations"></a>

## 8. Evidence basis & citations

| Evidence | What it supports | Limit |
|---|---|---|
| [Per-domain dashboard README](./README.md) | Current specification pattern and the proposed status of the dashboard documentation lane. | It is not runtime or indicator authority. |
| [Dashboard catalog](../DASHBOARD_CATALOG.md) | Current inventory relationship for this file. | Catalog presence does not prove implementation. |
| [Atmosphere domain README](../../domains/atmosphere/README.md) | Domain scope, object families, source-role and public-safety boundaries. | Several implementation and external-source items remain proposed or unverified. |
| [Accepted ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules](../../doctrine/directory-rules.md) | Responsibility-root separation and canonical human Directory Rules authority. | Same-path edits do not settle the proposed dashboard-lane placement question. |
| [Explorer Atmosphere files](../../../apps/explorer-web/src/features/domains/atmosphere/) | Exact current source state: one Evidence Drawer re-export and two placeholders. | No complete Atmosphere dashboard, route, telemetry, or deployment proof. |
| [Atmosphere contract/schema/policy/test roots](../../../contracts/domains/atmosphere/README.md) | Current bounded object and validator surfaces. | File presence is not source admission, scientific validity, release, or publication. |
| [PM Sensor Trust Profile candidate](../../../contracts/domains/atmosphere/pm_sensor_trust_profile.md) | Exact fixture-only trust dimensions and non-authority controls. | No live sensor, composite trust score, dashboard, or public-health claim. |

External manuscripts and source endpoints were not needed to establish this repository-state specification. External source currentness, rights, and scientific fitness remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## 9. Finite outcomes and safety boundary

| Outcome | Dashboard behavior |
|---|---|
| `ANSWER` | Present only released or otherwise authorized public-safe content with resolvable evidence and applicable caveats. |
| `ABSTAIN` | State that evidence, precision, model context, freshness, or support is insufficient. |
| `DENY` | Withhold content blocked by policy, rights, sensitivity, alert-authority, source-role, release-state, or anti-collapse rules. |
| `ERROR` | Report a bounded validation, resolver, contract, or availability failure without silently falling back to unsupported content. |

These outcomes are delivery states, not truth substitutes. The underlying `EvidenceBundle`, `PolicyDecision`, validation result, release record, correction record, and rollback target remain separate object families.

Public and ordinary UI paths must use governed APIs or released public-safe artifacts. Direct reads from RAW, WORK, QUARANTINE, canonical/internal, restricted, or unreleased candidate stores are denied.

[Back to top](#top)

---

## 10. PM-sensor compatibility note

The former `docs/dashboards/domain/air/PM_SENSOR_CALIBRATION_REVIEW.md` specification was deleted from current main. This update does not restore that alternate `air/` dashboard path.

The surviving bounded packet is the fixture-only [PM Sensor Trust Profile candidate](../../../contracts/domains/atmosphere/pm_sensor_trust_profile.md) with its schema, fixtures, validator, and tests. It declares four independent dimensions and finite `QUALIFIED_CONTEXT` / `HOLD` / `DENY` routing without producing a composite score. Its controls explicitly deny live evaluation, source admission, policy approval, review approval, promotion, release, publication, public-health authority, and reference-grade equivalence.

Active documentation should link this Atmosphere dashboard specification or the trust-profile packet directly. Historical generated receipts that cite the deleted path remain immutable provenance and are not rewritten.

[Back to top](#top)

---

## 11. Validation

Repository-hosted documentation checks should validate metadata, document-graph integrity, Markdown structure, and repository-relative links for the final branch head.

The PM trust packet exposes these focused no-network commands:

```bash
python -m unittest discover \
  --start-directory tests/validators/domains/atmosphere \
  --pattern 'test_pm_sensor_trust_profile.py' \
  --verbose

python tools/validators/domains/atmosphere/validate_pm_sensor_trust_profile.py --fixtures
```

Passing those commands proves only the candidate schema, evidence-reference closure, finite trust posture, deterministic identity, negative fixture polarity, and bounded input handling. It does not prove this dashboard exists or that any live sensor, source, policy, scientific threshold, release, deployment, or publication is approved.

Before changing an implementation status in this document, verify all of the following at one exact commit:

- route or component bytes;
- contract and schema versions;
- policy and finite-outcome behavior;
- deterministic positive and negative fixtures;
- evidence and correction binding;
- accessibility and no-sensitive-leak behavior;
- hosted checks for the exact head;
- rollback or abandonment path.

[Back to top](#top)

---

## 12. Maintenance and rollback

Maintain this file when its linked implementation, contract, schema, policy, fixture, validator, catalog entry, or ownership evidence changes. Preserve the document ID, `# Atmosphere / Air Dashboard Specification` heading, `#top` anchor, and numbered section anchors unless a reviewed compatibility change updates known inbound links.

For a documentation-only correction before merge, abandon or close the draft branch/PR. After merge, revert the merged change or submit a forward correction against current bytes. Do not recreate the deleted `domain/air/` specification as a second writable authority; if a future migration requires a compatibility path, it needs an accepted placement decision, one-way ownership, exit criteria, and reference repair.

No rollback of data, policy, runtime, release, deployment, or publication state is required for this documentation specification alone.

[Back to top](#top)
