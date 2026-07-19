<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/air
title: Air Domain Policy Compatibility Guardrail README
type: readme; directory-readme; domain-policy-compatibility-lane; slug-conflict-guardrail; non-authoritative
version: v0.2
status: draft; repository-grounded; compatibility-only; direct-lane-readme-only; preferred-atmosphere-lane-confirmed; executable-policy-unestablished; slug-adr-open; not-for-life-safety
owners: OWNER_TBD — Atmosphere/Air steward · Policy steward · Directory-governance steward · Sensitivity and rights steward · Source steward · Contract/schema steward · Validator/test steward · Runtime steward · Release steward · Security reviewer · Docs steward
created: 2026-06-15
updated: 2026-07-19
supersedes: v0.1 Air policy slug-conflict guide
policy_label: restricted-review; policy; air; atmosphere; compatibility-only; slug-drift; redirect-to-atmosphere; no-active-policy-here; no-public-authority; not-emergency-alerting
current_path: policy/domains/air/README.md
owning_root: policy/
responsibility: >
  Compatibility and migration guardrail for the unresolved `air` policy segment. It records the
  current repository evidence, redirects new Atmosphere/Air policy work toward the preferred
  `policy/domains/atmosphere/` lane, prevents parallel policy authority and duplicate bundle
  selection, defines finite compatibility outcomes and obligations, and preserves evidence, rights,
  sensitivity, release, correction, and rollback boundaries without activating this path.
truth_posture: >
  CONFIRMED target v0.1 README; canonical singular policy root; bounded direct-lane search surfaced
  only this README under policy/domains/air; policy/domains/atmosphere/README.md exists as a
  33-line PROPOSED greenfield scaffold; Atmosphere canonical-path doctrine prefers `atmosphere` for
  new work and treats `air` as an ADR-class drift candidate; contracts/air, tests/domains/air, and
  pipeline_specs/air are documented compatibility lanes; Atmosphere policy and sensitivity doctrine
  define anti-collapse, rights, freshness, caveat, generalization, and official-authority
  redirection requirements; tests/domains/atmosphere is a scaffolded preferred test lane; the
  domain-atmosphere workflow emits readiness holds and evaluates no policy; the shared policy
  runtime remains a comment-only placeholder; the shared PolicyDecision schema currently permits
  ANSWER, ABSTAIN, DENY, and ERROR only /
  PROPOSED this lane remain documentation-only, redirect all new executable policy work to the
  preferred Atmosphere lane pending ADR, define compatibility decision normalization, reason-code
  and obligation families, alias/migration invariants, validation checks, review burden, and a
  reversible resolution sequence /
  CONFLICTED repository presence of both air and atmosphere segments across policy, contracts,
  pipeline specifications, executable-pipeline documentation, tests, and schemas while current
  placement doctrine prefers atmosphere; the atmosphere policy README calls itself canonical while
  also incorrectly allowing non-policy materials; documentation-level REDIRECT/HOLD/RESTRICT
  vocabulary versus the shared PolicyDecision schema's ANSWER/ABSTAIN/DENY/ERROR vocabulary /
  UNKNOWN accepted slug ADR, active policy source files, bundle manifest, evaluator, selector,
  deployment binding, executable Atmosphere policy tests, dedicated policy validators, direct
  runtime consumers, active public route aliases, branch-protection significance, release mapping,
  and production enforcement /
  NEEDS VERIFICATION owners and CODEOWNERS, exhaustive air/atmosphere inventory, accepted canonical
  slug and alias lifetime, migration/deprecation record, package namespaces, bundle identity,
  source-specific rights rules, stale-state profile, low-cost-sensor caveat profile, exact-station
  generalization profile, deterministic fixtures, no-network tests, API/UI/map/AI redirect handling,
  correction propagation, and rollback drill.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 0c0fc543a82123ea4b2216df7a4b41df0c1c82ae
  prior_blob: 1531b955ebc8474dae384e896117d0e265405e76
  policy_root_blob: 09cd966ab188d5e831960869117522a98274cb7f
  air_policy_guardrail_blob: 1531b955ebc8474dae384e896117d0e265405e76
  atmosphere_policy_readme_blob: d897f4f67458f9d12e0ef2b2e7146eeba935df4b
  atmosphere_canonical_paths_blob: 97296d516792ad3bc2bc1f18d03e2518e367d28a
  atmosphere_policy_doctrine_blob: 53480f8a9e7db4d863ed15cc96c708f0e8d40ef4
  atmosphere_sensitivity_doctrine_blob: 900dbc36d8eac280abd44531691273a6fd07c90f
  contracts_air_readme_blob: 47c6425000418602a3a351e116a4507a51de67e7
  tests_air_readme_blob: 57a1df863d1dfb25cfc9c902bf3ec81bb9795bed
  tests_atmosphere_readme_blob: 6474cc33c3bdd668fd8713e06e94f7dacda97b6b
  pipeline_specs_air_readme_blob: 16a5096d5edcad9bbba51c87ef5f5d5521c2a0d6
  domain_atmosphere_workflow_blob: 9d38e1b292d4907e9d910b7a96f1bef9a00f6c84
  policy_runtime_core_blob: e7e14cf39ae6919fbbc80f1b471de6b907292edb
  policy_decision_schema_blob: 1472d26a42c73f17545b4464a275412ffa1d098e
related:
  - ../README.md
  - ../../README.md
  - ../atmosphere/README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../docs/domains/atmosphere/POLICY.md
  - ../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../contracts/air/README.md
  - ../../../contracts/domains/atmosphere/README.md
  - ../../../schemas/contracts/v1/domains/atmosphere/README.md
  - ../../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../../tests/domains/air/README.md
  - ../../../tests/domains/atmosphere/README.md
  - ../../../tests/domains/atmosphere/policy-deny/README.md
  - ../../../fixtures/domains/atmosphere/
  - ../../../pipeline_specs/air/README.md
  - ../../../pipeline_specs/atmosphere/README.md
  - ../../../pipelines/domains/air/README.md
  - ../../../pipelines/domains/atmosphere/README.md
  - ../../../packages/policy-runtime/README.md
  - ../../../policy/bundles/README.md
  - ../../../data/registry/sources/atmosphere/README.md
  - ../../../data/proofs/atmosphere/README.md
  - ../../../release/candidates/atmosphere/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/doctrine/ai-build-operating-contract.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../.github/workflows/domain-atmosphere.yml
tags:
  - kfm
  - policy
  - air
  - atmosphere
  - compatibility
  - slug-drift
  - alias
  - redirect
  - migration
  - anti-collapse
  - source-role
  - rights
  - sensitivity
  - stale-state
  - low-cost-sensor
  - exact-station-generalization
  - official-authority-redirect
  - finite-outcomes
  - no-network
  - release-gated
  - correction
  - rollback
notes:
  - "This revision changes only policy/domains/air/README.md plus the required AI-generated provenance receipt."
  - "No Rego/YAML rule, policy value, bundle, evaluator, schema, contract, fixture, test, validator, workflow, source record, lifecycle object, receipt/proof instance, release artifact, deployment, route alias, or public behavior is created or modified."
  - "This README does not resolve the air/atmosphere ADR; it preserves the current preference for atmosphere while preventing silent parallel authority."
  - "KFM is not an AQI, medical, regulatory, emergency-alerting, or life-safety issuing authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/domains/air/` — Air Policy Compatibility Guardrail

> **One-line purpose.** Preserve an inspectable compatibility boundary for the unresolved `air` policy segment, redirect new Atmosphere/Air policy work to [`policy/domains/atmosphere/`](../atmosphere/README.md), and prevent alias paths from becoming duplicate policy, bundle, evidence, release, or public authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: policy" src="https://img.shields.io/badge/root-policy%2F-blue">
  <img alt="Authority: compatibility only" src="https://img.shields.io/badge/authority-compatibility__only-orange">
  <img alt="Preferred lane: atmosphere" src="https://img.shields.io/badge/preferred-policy%2Fdomains%2Fatmosphere%2F-success">
  <img alt="Inventory: README only" src="https://img.shields.io/badge/inventory-README__only-lightgrey">
  <img alt="ADR: required" src="https://img.shields.io/badge/slug__ADR-required-critical">
  <img alt="Emergency authority: official issuer" src="https://img.shields.io/badge/emergency__authority-official__issuer-red">
</p>

> [!IMPORTANT]
> **This directory is a compatibility guardrail, not a second Atmosphere policy package.** Path presence, README completeness, import aliases, or a green workflow must not activate `air` as a canonical domain segment. Until an accepted ADR or governing lane register resolves the name, new executable Atmosphere policy belongs under `policy/domains/atmosphere/`.

> [!CAUTION]
> **The preferred Atmosphere lane is not implementation proof.** Its current README is a short `PROPOSED` greenfield scaffold and incorrectly suggests that docs, contracts, schemas, fixtures, tests, packages, pipelines, registries, and lifecycle data may live under a policy directory. This Air guardrail must not inherit or repeat that over-broad placement claim.

> [!WARNING]
> **KFM is not an air-quality, medical, regulatory, emergency-alerting, or life-safety issuing authority.** Policy may preserve source roles, caveats, stale-state labels, evidence requirements, and official-authority redirects. It must not produce protective-action instructions or imply that KFM replaces AirNow, regulatory agencies, emergency management, health authorities, or other official issuers.

**Quick links:** [Purpose](#purpose) · [Current evidence](#current-evidence-and-maturity) · [Authority](#authority-and-directory-rules-basis) · [Slug contract](#slug-conflict-and-compatibility-contract) · [Belongs](#what-belongs-here) · [Does not](#what-does-not-belong-here) · [Preferred lane](#preferred-atmosphere-policy-lane) · [Policy spine](#atmosphereair-policy-spine) · [Inputs](#minimum-compatibility-input-contract) · [Outcomes](#finite-outcomes-and-normalization) · [Reasons](#reason-codes-and-obligations) · [Public surfaces](#public-surface-contract) · [Validation](#validation-tests-and-ci) · [Review](#review-burden-and-separation-of-duties) · [Migration](#adr-migration-correction-and-rollback) · [Related](#related-folders) · [Conflicts](#conflict-register) · [Sequence](#smallest-sound-resolution-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [Changelog](#changelog)

---

## Purpose

`policy/domains/air/` exists because the repository contains a historical or proposed `air` domain segment while current Directory Rules and Atmosphere placement documentation prefer `atmosphere` for new domain lanes.

Its durable question is:

> Can KFM preserve the `air` alias as an inspectable compatibility surface without allowing it to create duplicate policy source, bundle selection, object meaning, schema shape, source identity, evidence behavior, release semantics, public routes, or life-safety claims?

This path should support only these functions:

1. document the unresolved `air` versus `atmosphere` naming conflict;
2. redirect contributors and policy discovery toward the preferred Atmosphere lane;
3. define invariants a future migration or explicit alias strategy must satisfy;
4. prevent duplicate rule evaluation and divergent policy outcomes across both slugs;
5. preserve historical references long enough for reviewed migration, correction, or deprecation;
6. keep evidence, rights, sensitivity, release, correction, and rollback semantics unchanged by slug choice;
7. expose bounded compatibility decisions without inventing a new machine enum;
8. remain non-authoritative until a governed decision explicitly changes that posture.

It is not a place to implement Atmosphere policy while governance remains unresolved.

[Back to top](#top)

---

## Current evidence and maturity

### Safe conclusion

At `main@0c0fc543a82123ea4b2216df7a4b41df0c1c82ae`:

- `policy/domains/air/` is established only as a README-backed compatibility guardrail in bounded search.
- `policy/domains/atmosphere/` exists and is the documentation-preferred domain-policy segment, but its current README is still a 33-line greenfield scaffold.
- Atmosphere canonical-path doctrine explicitly says new work should use `atmosphere/` and treats `air/` as an ADR-class drift candidate.
- `contracts/air/`, `tests/domains/air/`, and `pipeline_specs/air/` also document compatibility or unresolved alias roles.
- the preferred Atmosphere test, schema, contract, pipeline, source-registry, proof, and release lanes exist as documentation surfaces of varying maturity;
- no active Air policy bundle, evaluator, selector, runtime binding, or public alias is established by the inspected evidence;
- the `domain-atmosphere` workflow is a readiness-hold workflow that performs no policy evaluation, proof production, release assembly, or publication;
- the policy runtime core remains a one-line placeholder;
- the shared `PolicyDecision` schema is concrete enough to require `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`, but it does not define `REDIRECT`, `HOLD`, `RESTRICT`, or slug-migration semantics.

### Maturity matrix

| Surface | Inspected status | Safe conclusion |
|---|---|---|
| `policy/domains/air/` | **CONFIRMED README-only in bounded search** | Compatibility documentation exists; no direct policy source surfaced. |
| `policy/domains/atmosphere/` | **CONFIRMED 33-line PROPOSED scaffold** | Preferred lane exists, but no executable policy inventory or safe folder contract is established. |
| Canonical-path doctrine | **CONFIRMED draft registry** | Uses `atmosphere` for new paths and treats `air` as ADR-class drift. |
| Atmosphere policy doctrine | **CONFIRMED draft doctrine** | Defines fail-closed anti-collapse, rights, stale-state, caveat, and advisory boundaries. |
| Atmosphere sensitivity doctrine | **CONFIRMED draft doctrine** | Defines T0/T1 defaults, exact-station generalization, rights holds, and official-authority denial. |
| `contracts/air/` | **CONFIRMED compatibility folder** | Semantic-contract slug conflict remains open. |
| `tests/domains/air/` | **CONFIRMED README-only compatibility lane** | New executable tests should use `tests/domains/atmosphere/`. |
| `tests/domains/atmosphere/` | **CONFIRMED preferred parent README / scaffold** | Child responsibilities are documented; executable coverage remains unestablished. |
| `pipeline_specs/air/` | **CONFIRMED compatibility guardrail** | No active Air specification established. |
| Atmosphere policy-deny child READMEs | **CONFIRMED documentation** | AQI/concentration, AOD/PM2.5, model/observed, and low-cost-sensor boundaries are described; execution remains verification-bound. |
| `domain-atmosphere` workflow | **CONFIRMED readiness holds** | No policy, validation, proof, release, alerting, or publication authority. |
| Policy runtime core | **CONFIRMED comment-only placeholder** | No accepted evaluator implementation. |
| Shared PolicyDecision schema | **CONFIRMED PROPOSED concrete shape** | Outcomes are limited to `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. |
| Canonical slug decision | **CONFLICTED / NEEDS VERIFICATION** | No accepted ADR or lane-register decision was verified. |
| Active public alias or runtime selector | **UNKNOWN** | No active route, loader, bundle selector, or deployment binding is claimed here. |

### Evidence boundary

This README can state repository presence and inspected content. It cannot establish:

- a byte-complete inventory of every `air` or `atmosphere` path;
- accepted ADR status;
- production policy execution;
- active bundle selection;
- deployment configuration;
- complete policy coverage;
- policy-test pass rates;
- public route alias behavior;
- release mapping;
- branch-protection requirements;
- monitoring or alerting behavior;
- medical, regulatory, emergency, or life-safety correctness.

Those remain `UNKNOWN` or `NEEDS VERIFICATION` until current implementation evidence proves them.

[Back to top](#top)

---

## Authority and Directory Rules basis

**Compatibility documentation only / no policy authority.**

Directory Rules make `policy/` the canonical responsibility root for allow, deny, restrict, abstain, redaction, sensitivity, promotion, and release-adjacent decisions. The conflict here is the domain segment—not the responsibility root.

| Concern | Authority home | This lane's role |
|---|---|---|
| Policy source rules | Accepted policy lanes under singular `policy/` | Pointer and migration guard only. |
| Atmosphere policy intent | [`docs/domains/atmosphere/POLICY.md`](../../../docs/domains/atmosphere/POLICY.md) | Cites intent; does not enforce it. |
| Sensitivity and tiering | [`docs/domains/atmosphere/SENSITIVITY.md`](../../../docs/domains/atmosphere/SENSITIVITY.md) plus accepted policy lanes | Preserves the most restrictive applicable posture. |
| Object meaning | Accepted contract home | Does not define semantic contracts. |
| Machine shape | Accepted schema home | Does not define JSON Schema. |
| Source identity and rights facts | Governed source registry and review records | Requires explicit context; cannot invent facts. |
| Evidence | EvidenceRef/EvidenceBundle and proof families | Requires evidence; cannot create closure. |
| Policy execution | Accepted evaluator and immutable bundle | Cannot execute or select policy. |
| Tests and validators | `tests/`, `tools/validators/` | Must prove redirect and anti-duplication behavior. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | May be referenced; never stored here. |
| Release, correction, rollback | `release/` | Cannot approve a state transition. |
| Public API, UI, map, export, AI | Governed applications and released artifacts | Must consume normalized outcomes; cannot select aliases ad hoc. |
| CI | `.github/workflows/` | May guard drift; cannot activate policy by green status. |

### Governing order

When Air/Atmosphere path sources conflict, apply this order:

1. KFM core invariants and operating law.
2. accepted ADRs that explicitly resolve the segment or compatibility strategy;
3. Directory Rules and the domain-placement law;
4. accepted domain registry or lane-register decision;
5. Atmosphere policy and sensitivity doctrine;
6. source-specific rights, license, confidentiality, cadence, and official-authority requirements;
7. accepted contracts, schemas, policy bundles, and evaluator profiles;
8. this compatibility README;
9. current greenfield scaffolds and examples.

A lower-ranked compatibility artifact must not weaken a higher-ranked denial, restriction, evidence, rights, review, release, correction, or rollback obligation.

[Back to top](#top)

---

## Slug conflict and compatibility contract

### Current naming conflict

| Source or surface | Segment | Current posture |
|---|---|---|
| Directory Rules domain enumeration | `atmosphere` | Doctrine-preferred segment. |
| Atmosphere canonical-path registry | `atmosphere` | Use for new work pending ADR. |
| Atlas crosswalk and historical paths | `air` in some roots | Drift/compatibility candidate. |
| Current policy compatibility path | `policy/domains/air/` | README-only guardrail. |
| Preferred policy path | `policy/domains/atmosphere/` | Repository-present scaffold; implementation unproved. |
| Contracts compatibility path | `contracts/air/` | Conflict documented. |
| Preferred domain contracts | `contracts/domains/atmosphere/` | Repository-present family, though inventory/path duplication exists. |
| Test compatibility path | `tests/domains/air/` | README-only redirect lane. |
| Preferred tests | `tests/domains/atmosphere/` | Parent/child documentation lane. |
| Pipeline-spec compatibility path | `pipeline_specs/air/` | README-only guardrail. |
| Preferred pipeline specs | `pipeline_specs/atmosphere/` | Documentation-preferred lane. |

### Compatibility invariants

Until governance resolves the slug, this lane must preserve all of the following:

1. **One active policy source.** At most one slug may supply the evaluated rule set.
2. **One bundle identity.** Equivalent rules under both paths must not produce independent bundle IDs or digests.
3. **One decision.** Alias resolution must not evaluate both paths and merge or race results.
4. **One reason/obligation meaning.** Slug choice cannot change decision semantics.
5. **No path-based activation.** Directory or file presence does not make a lane active.
6. **No silent fallback.** Missing preferred policy cannot fall back to an unreviewed compatibility source.
7. **No public alias bypass.** Public callers cannot choose `air` to evade `atmosphere` policy.
8. **No lifecycle bypass.** Alias resolution cannot move candidate data between lifecycle states.
9. **No release bypass.** Alias resolution cannot grant publication or restore withdrawn content.
10. **No evidence rewrite.** EvidenceRef, SourceDescriptor, receipt, proof, release, correction, and rollback identities survive migration.
11. **No semantic collapse.** AQI, concentration, AOD, PM2.5, model, observation, low-cost sensor, advisory, and official warning remain distinct.
12. **No official-authority impersonation.** Compatibility cannot make KFM an alert or life-safety issuer.

### Forbidden shortcut

```text
policy/domains/air/
  -> discovered by path
  -> treated as active bundle
  -> evaluated by public caller
  -> rendered as policy-authorized Atmosphere truth
```

This is forbidden without an accepted slug decision, immutable bundle identity, evaluator binding, tests, review, release mapping, and rollback support.

[Back to top](#top)

---

## What belongs here

While the slug remains unresolved, accepted content is deliberately narrow:

- this directory README;
- a compatibility/deprecation marker that contains no policy values;
- an ADR pointer;
- an alias manifest or redirect record only after its schema, owner, and activation semantics are accepted;
- migration inventories and checksums;
- a tombstone or supersession note after migration;
- safe reason-code and obligation documentation for compatibility handling;
- reviewer instructions for discovering the preferred Atmosphere lane;
- rollback instructions for reversing a migration;
- links to drift, correction, or deprecation records.

Any added file must state:

- whether it is documentation, redirect metadata, migration state, or a tombstone;
- that it is non-authoritative unless an accepted decision says otherwise;
- the preferred target;
- its activation prohibition;
- its owner and review state;
- its correction and rollback path;
- whether public clients can ever read it directly—the default answer is no.

[Back to top](#top)

---

## What does not belong here

| Material | Correct authority home |
|---|---|
| Atmosphere Rego or equivalent policy source | [`policy/domains/atmosphere/`](../atmosphere/README.md) pending accepted ADR/placement review |
| Active policy bundle or manifest | `policy/bundles/` or accepted bundle lane |
| Policy runtime/evaluator code | accepted runtime/package boundary |
| Policy inputs or decision instances | governed request/receipt/audit surfaces, not this directory |
| Policy schemas and semantic contracts | `schemas/` and `contracts/` |
| Source descriptors and rights records | governed `data/registry/` lanes |
| Source payloads or lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, catalog/triplet, and published roots |
| Fixtures and executable tests | `fixtures/domains/atmosphere/`, `tests/domains/atmosphere/` |
| Validator implementation | accepted `tools/validators/` lane |
| Pipeline specs or executable transforms | `pipeline_specs/atmosphere/`, `pipelines/domains/atmosphere/`, or accepted homes |
| Receipts and proofs | `data/receipts/`, `data/proofs/` |
| Release manifests, corrections, withdrawals, rollback cards | `release/` |
| Public API, UI, MapLibre, report, export, or AI behavior | governed application/runtime roots |
| AQI, medical, regulatory, emergency, or life-safety instructions | official issuing authorities; KFM may only redirect with bounded context |
| A second copy of any Atmosphere policy for convenience | forbidden until an accepted migration/alias decision authorizes it |

Adding executable policy here before ADR resolution would create parallel policy authority and must be rejected.

[Back to top](#top)

---

## Preferred Atmosphere policy lane

The current preferred policy lane is:

```text
policy/domains/atmosphere/
```

Its presence does not yet establish a production policy implementation.

### Confirmed current limitation

The inspected sibling README:

- is only 33 lines;
- labels the lane `PROPOSED (greenfield scaffold)`;
- calls itself canonical;
- provides no inventory of Rego/YAML policy files;
- provides no bundle ID, manifest, digest, selector, evaluator, input contract, reason-code registry, obligation registry, fixtures, tests, or runtime evidence;
- incorrectly states that docs, contracts, schemas, fixtures, tests, packages, pipelines, registries, and lifecycle data may belong under the policy lane.

### Required hardening before executable Atmosphere policy lands

The preferred lane should be updated to:

1. narrow itself to Atmosphere policy source and policy-lane documentation only;
2. enumerate current direct files and truth-label each one;
3. bind to accepted `PolicyInputBundle` and `PolicyDecision` contracts;
4. define or link one package namespace and entrypoint convention;
5. define fail-closed default semantics;
6. separate engine-native results from canonical public/runtime outcomes;
7. define reason-code and obligation registries;
8. identify bundle/manifest/evaluator/selector expectations;
9. require deterministic no-network fixtures and negative tests;
10. preserve source-role, knowledge-character, rights, sensitivity, stale-state, caveat, evidence, review, release, correction, and rollback context;
11. deny emergency/life-safety authority;
12. document how the `air` compatibility lane is ignored, redirected, deprecated, or migrated.

This Air README does not perform that sibling update. It records the prerequisite.

[Back to top](#top)

---

## Atmosphere/Air policy spine

Any future accepted Atmosphere policy—regardless of slug—must preserve the domain's knowledge-character and trust boundaries.

### Anti-collapse rules

| Boundary | Required policy posture |
|---|---|
| AQI versus concentration | Deny presenting an AQI/report object as a pollutant concentration observation. |
| AOD versus PM2.5 | Deny presenting an aerosol optical depth raster or smoke mask as a PM2.5 measurement. |
| Model versus observation | Deny presenting forecast/model context as observed measurement. |
| Low-cost sensor versus regulatory monitor | Require correction, caveat, confidence, limitations, and source-role display; never silently upgrade authority. |
| Advisory context versus official warning | Deny KFM-issued life-safety instructions; redirect to official issuer. |
| Context versus canonical claim | Atmosphere context may support Hazards, Agriculture, Hydrology, Habitat, or Settlement analysis without owning those domains' canonical claims. |
| Stale versus current | Require explicit valid-time/freshness state; stale data cannot be rendered as current without restriction. |
| Aggregate versus station-specific | Aggregation cannot be re-expanded into exact station, property, infrastructure, or person-linked detail. |
| Calibration versus observation | Calibration metadata supports interpretation; it does not become an observation itself. |
| Map layer versus truth | Tiles, rasters, contours, legends, and map styling are carriers, not evidence authority. |

### Rights and sensitivity rules

- unresolved source terms, license, attribution, redistribution, or written-permission status fail closed;
- exact station siting may require generalization where private land or sensitive infrastructure exposure is plausible;
- rights-restricted feeds remain denied or restricted even when technically accessible;
- sensitive cross-lane joins inherit the most restrictive row;
- transform receipts and review records are required for public-facing generalization/redaction when policy requires them;
- a tier or audience upgrade cannot be inferred from a generalized geometry alone;
- rollback, correction, or source withdrawal can make a previously released derivative unsafe or stale;
- public clients never receive hidden source credentials, raw payloads, internal policy detail, or restricted geometry.

### Freshness and operational boundary

Atmosphere policy must explicitly distinguish:

- observed time;
- valid time;
- issue time;
- retrieval time;
- processing time;
- source cadence;
- stale-after threshold or source-specific freshness state;
- current versus historical versus model/forecast context.

A policy decision may require stale-state badges, disclaimers, restriction, abstention, or denial. It must not assert current operational conditions from stale or time-ambiguous data.

### Official-authority redirection

When a request asks for emergency action, health protection, official AQI guidance, regulatory compliance status, or other consequential direction, KFM should:

1. preserve the requested scope safely;
2. identify that KFM is not the issuing authority;
3. return a bounded `ABSTAIN` or `DENY` where policy support is absent;
4. point the caller toward an official authority through the governed public interface when an approved link/reference exists;
5. avoid reproducing restricted, stale, or unverified instructions;
6. record the policy reason and obligations without leaking protected detail.

[Back to top](#top)

---

## Minimum compatibility input contract

A compatibility decision must not be made from a path string alone.

### Required inputs

| Input family | Minimum fields or posture |
|---|---|
| Requested path | Exact repository or logical path the caller attempted to use. |
| Requested operation | Discover, load, evaluate, validate, migrate, deprecate, render, export, release, or rollback. |
| Domain identity | Requested slug plus canonical/compatibility status from an accepted register or explicit unresolved marker. |
| Preferred target | Exact Atmosphere target path or `UNKNOWN`; never guessed silently. |
| ADR/migration context | Decision record, migration ID, deprecation state, effective date, rollback target, and review state where available. |
| Policy bundle context | Bundle ID/version/digest, selector identity, evaluator profile, and activation state when policy execution is requested. |
| Audience | Public, reviewer, restricted, internal, release steward, or another accepted audience. |
| Source/evidence context | Source role, rights state, EvidenceRef/EvidenceBundle status, validation state, and time/freshness fields where claim-bearing behavior is involved. |
| Sensitivity context | Exact siting, private-land/infrastructure, low-cost-sensor caveat, sensitive join, advisory, or other applicable restrictions. |
| Release context | Candidate/released/superseded/withdrawn state, ReleaseManifest ref, correction state, and rollback ref. |
| Caller identity | Governed caller/service identity and allowed capabilities where access-controlled behavior is involved. |
| Trace context | Correlation ID, request ID, or audit reference that does not expose secrets or sensitive data. |

### Missing-input posture

| Missing or unresolved input | Safe disposition |
|---|---|
| Canonical slug decision | `ABSTAIN` with redirect obligation, or `DENY` for activation. |
| Preferred target | `ERROR` or `ABSTAIN`; no guessed fallback. |
| Bundle identity or digest | `DENY` policy execution. |
| Evaluator profile | `ERROR`; do not evaluate with an arbitrary engine. |
| Rights or sensitivity context | `DENY` or `ABSTAIN` depending on requested operation. |
| Evidence support for claim-bearing output | `ABSTAIN` or `DENY`. |
| Release state | `DENY` public serving. |
| Correction/rollback context for migration | `HOLD` in review workflow; normalize to `ABSTAIN` or `ERROR` at public runtime. |

Input assembly must be deterministic, documented, sensitivity-minimized, and free of hidden network fetches.

[Back to top](#top)

---

## Finite outcomes and normalization

### Canonical shared outcome surface

The inspected shared `PolicyDecision` schema currently permits:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

This compatibility README must not silently create additional machine enums.

### Documentation and workflow dispositions

Reviewers and migration tooling may need richer internal dispositions:

```text
REDIRECT | HOLD | RESTRICT | DEPRECATE | SUPERSEDE | MIGRATE
```

These are **PROPOSED orchestration dispositions**, not confirmed shared `PolicyDecision.outcome` values.

### Required normalization

| Compatibility disposition | Canonical runtime outcome | Typical obligation |
|---|---|---|
| Preferred `atmosphere` policy resolved and accepted | `ANSWER` | Preserve selected bundle/version and normal obligations. |
| `air` path requested; safe target known | `ABSTAIN` or bounded `ANSWER` containing redirect metadata, per accepted contract | `redirect_required`; no policy evaluation from compatibility path. |
| Slug unresolved | `ABSTAIN` | `adr_review_required`; `redirect_required` where safe. |
| Attempt to activate compatibility policy | `DENY` | `canonical_policy_required`; `security_review_required`. |
| Duplicate active bundles | `DENY` | `duplicate_authority_blocked`; `incident_review_required`. |
| Alias resolver malfunction | `ERROR` | `fail_closed`; `operator_review_required`. |
| Sensitive or rights-unclear request | `DENY` or `ABSTAIN` | `rights_review_required`; `sensitivity_review_required`. |
| Emergency/life-safety request | `DENY` or `ABSTAIN` | `official_authority_redirect_required`. |
| Migration prerequisites incomplete | `ABSTAIN` in runtime; internal workflow hold | `migration_review_required`; `rollback_target_required`. |

A public caller must never receive `ANSWER` solely because the compatibility target exists.

[Back to top](#top)

---

## Reason codes and obligations

The following names are **PROPOSED vocabulary** until an accepted contract or registry makes them normative.

### Reason-code families

| Family | Candidate examples |
|---|---|
| Slug authority | `air_slug_not_canonical`, `canonical_slug_unresolved`, `alias_not_accepted` |
| Duplicate authority | `parallel_policy_home_detected`, `duplicate_bundle_detected`, `multiple_active_selectors` |
| Migration | `migration_record_missing`, `deprecation_state_unresolved`, `rollback_target_missing` |
| Bundle/evaluator | `bundle_identity_missing`, `bundle_digest_mismatch`, `evaluator_profile_missing`, `selector_unapproved` |
| Evidence/source role | `source_role_missing`, `evidence_unresolved`, `knowledge_character_missing` |
| Rights/sensitivity | `rights_unresolved`, `exact_station_restricted`, `sensitive_join_unresolved`, `low_cost_sensor_caveat_missing` |
| Time/freshness | `valid_time_missing`, `source_stale`, `cadence_unknown` |
| Anti-collapse | `aqi_as_concentration`, `aod_as_pm25`, `model_as_observation`, `advisory_as_alert` |
| Release | `release_state_missing`, `candidate_not_released`, `withdrawn_artifact`, `rollback_blocked` |
| System | `alias_resolution_error`, `policy_runtime_unavailable`, `invalid_policy_input` |

Reason text exposed publicly must remain bounded and must not reveal private coordinates, source restrictions, credentials, internal network details, protected policy logic, or sensitive joins.

### Obligation families

| Obligation | Required effect |
|---|---|
| `redirect_required` | Use the accepted Atmosphere path; do not evaluate `air` policy. |
| `adr_review_required` | Route naming decision to governed architecture review. |
| `drift_record_required` | Record the existing alias/path in the drift register. |
| `migration_record_required` | Bind source and target paths, identities, hashes, owners, review state, and rollback target. |
| `canonical_policy_required` | Refuse compatibility-path activation. |
| `duplicate_authority_blocked` | Disable or reject simultaneous policy sources/selectors. |
| `source_role_required` | Preserve observed/model/report/mask/advisory character. |
| `rights_review_required` | Do not use or expose until source rights are resolved. |
| `sensitivity_review_required` | Apply most restrictive relevant row. |
| `generalization_required` | Reduce exact station/private-land/infrastructure precision through an accepted transform. |
| `caveat_required` | Carry low-cost-sensor/model/mask limitations. |
| `stale_state_required` | Display or encode freshness state and avoid current-condition overclaim. |
| `official_authority_redirect_required` | Refer to an official issuer without treating KFM as the issuer. |
| `evidence_required` | Resolve EvidenceRef/EvidenceBundle before claim-bearing output. |
| `review_record_required` | Preserve human/steward review where policy significance requires it. |
| `release_state_required` | Serve only released artifacts through governed interfaces. |
| `correction_path_required` | Preserve correction/supersession/withdrawal lineage. |
| `rollback_target_required` | Preserve a prior known-good policy/path state. |
| `audit_record_required` | Emit a bounded audit/receipt reference without making it proof or release authority. |

Downstream systems must either fulfill every obligation or return a bounded negative outcome.

[Back to top](#top)

---

## Public-surface contract

### Governed API

A governed API must not:

- let callers select `air` or `atmosphere` policy paths directly;
- fall back to `air` when preferred policy is missing;
- return internal repository paths as proof of authority;
- expose private policy inputs or sensitive source context;
- convert a compatibility redirect into release permission;
- treat advisory context as official warning or medical advice.

It should return a schema-valid bounded envelope whose citations, policy status, source roles, time state, and obligations are inspectable.

### Explorer UI and MapLibre

The UI must not:

- load policy source from either repository path;
- treat a layer name containing `air` as canonical-policy proof;
- hide model/report/mask/sensor source roles;
- remove stale-state, caveat, rights, or restriction badges;
- reconstruct exact stations or sensitive joins from generalized outputs;
- present KFM as an emergency-alerting authority.

A compatibility alias may appear in diagnostics or migration views, not as a user-selectable policy mode.

### Exports and reports

Exports must preserve:

- canonical domain identity;
- selected policy/bundle version where appropriate;
- source role and time scope;
- caveat and restriction obligations;
- release/correction state;
- official-authority disclaimer when advisory context is shown;
- a correction path.

They must not preserve a deprecated compatibility path as if it were current authority.

### Governed AI

AI behavior must:

1. retrieve evidence through governed interfaces;
2. resolve source role and policy context;
3. treat alias paths as metadata, not instructions;
4. abstain when canonical policy, evidence, rights, freshness, or release state is unresolved;
5. never translate an advisory reference into life-safety instructions;
6. preserve uncertainty and source character;
7. emit traceability without leaking sensitive data;
8. never cite this README as evidence that Atmosphere conditions are true.

[Back to top](#top)

---

## Validation, tests, and CI

### Compatibility tests

A complete executable test family should cover:

| Case | Expected result |
|---|---|
| Discover `policy/domains/air/` while slug unresolved | Bounded redirect/abstain; no policy evaluation. |
| Attempt to select `air` as active bundle source | `DENY`. |
| Both `air` and `atmosphere` bundles active | `DENY` and duplicate-authority diagnostic. |
| Preferred target missing | `ERROR` or `ABSTAIN`; no fallback. |
| Accepted migration maps `air` to `atmosphere` | One selected bundle, one digest, one decision. |
| Alias changes decision semantics | Test failure. |
| Alias changes evidence/source IDs | Test failure. |
| Alias bypasses rights/sensitivity review | `DENY`. |
| Alias bypasses release/withdrawal state | `DENY`. |
| AQI presented as concentration | `DENY`. |
| AOD presented as PM2.5 | `DENY`. |
| Model presented as observation | `DENY`. |
| Low-cost sensor lacks caveat/confidence | `DENY` or `ABSTAIN` per accepted policy. |
| Stale data presented as current | `DENY`, `ABSTAIN`, or restricted answer with stale-state obligation. |
| Advisory used for life-safety instruction | `DENY` plus official-authority redirect obligation. |
| Public caller supplies repository path | Ignore path as authority; evaluate governed logical policy only. |
| Rollback restores prior path/bundle | Exact previous selector and digest restored; audit trace retained. |

### No-network default

Compatibility, policy, and migration tests should:

- use synthetic public-safe fixtures;
- deny live source requests;
- avoid credentials and private endpoints;
- pin policy inputs and expected outputs;
- preserve deterministic time and freshness fixtures;
- avoid depending on current AirNow/AQS/forecast state;
- fail if hidden network access occurs;
- keep diagnostic output free of sensitive coordinates, source payloads, or restricted terms.

### Current workflow boundary

The inspected `domain-atmosphere` workflow:

- checks repository maturity;
- confirms there are no collected Atmosphere test functions;
- confirms no validator implementation is established in several candidate lanes;
- emits explicit `WORKFLOW_HOLD` / `WORKFLOW_SKIPPED_EXPLICIT` states;
- performs no live source requests;
- emits no PolicyDecision, EvidenceBundle, ProofPack, release, alert, deployment, or publication.

A green readiness hold is evidence of the documented scaffold state only.

### Minimum validation commands after implementation

The exact commands remain `NEEDS VERIFICATION`, but a mature lane should provide repository-native equivalents of:

```bash
# inventory and drift
find policy/domains/air policy/domains/atmosphere -maxdepth 5 -type f | sort
find contracts schemas tests fixtures pipeline_specs pipelines data release -maxdepth 6 -type f \
  | grep -E '/(air|atmosphere)/' \
  | sort

# policy source and tests
opa fmt --fail policy/
opa check --strict policy/
opa test policy/ -v

# deterministic domain tests
python -m pytest tests/domains/atmosphere -q --strict-config --strict-markers

# path/alias guards
python -m pytest tests/policy tests/architecture -q -k 'air or atmosphere or alias or slug'
```

Commands must not be called implemented until the repository actually supplies them and current runs pass.

[Back to top](#top)

---

## Review burden and separation of duties

Changes to this compatibility lane are governance-significant because they can affect policy discovery and public-serving behavior even when they look like path cleanup.

### Required review roles

| Change | Minimum reviewers |
|---|---|
| README clarification only | Policy steward + Atmosphere/Air steward + docs steward |
| Alias/redirect metadata | Policy steward + directory-governance steward + runtime owner |
| Canonical slug decision | Architecture steward + policy steward + domain steward + owners of affected roots |
| Policy source migration | Policy steward + security reviewer + contract/schema/test owners |
| Bundle/selector change | Policy runtime steward + security reviewer + policy steward |
| Public route or export alias | Governed API/UI owner + policy steward + release steward |
| Rights/sensitivity behavior | Rights/sensitivity reviewer + source steward |
| Advisory/official-authority behavior | Atmosphere steward + Hazards/life-safety reviewer + security reviewer |
| Release/correction/rollback mapping | Release steward + independent reviewer |

### Separation rules

- the migration author must not be the sole approver;
- bundle/selector activation is separate from source migration;
- passing tests are separate from policy acceptance;
- policy acceptance is separate from release approval;
- release approval is separate from publication;
- correction and rollback remain independently executable;
- an alias cannot be activated through documentation merge alone.

### Review checklist

- [ ] Direct inventories for both slugs are current.
- [ ] No executable policy was added under `air`.
- [ ] Preferred Atmosphere lane remains the only active candidate.
- [ ] Package namespace and entrypoint are unambiguous.
- [ ] Bundle ID/digest/selector are deterministic.
- [ ] Alias handling cannot evaluate both paths.
- [ ] Canonical decision normalization is tested.
- [ ] Evidence, rights, sensitivity, freshness, review, release, correction, and rollback are preserved.
- [ ] Public API/UI/map/export/AI cannot choose repository paths.
- [ ] Official-authority redirection is bounded and tested.
- [ ] Logs and errors do not expose sensitive details.
- [ ] Revert and rollback steps are documented and realistic.
- [ ] Drift and ADR records are linked.
- [ ] Generated receipts remain provenance, not approval.

[Back to top](#top)

---

## ADR, migration, correction, and rollback

### ADR requirement

Resolving `air` versus `atmosphere` across policy, contracts, schemas, tests, pipeline specs, pipelines, data, and release paths changes an authority-bearing namespace and therefore requires an accepted ADR or equivalent governing decision.

The decision should specify:

- canonical segment;
- whether aliases are allowed;
- which roots are in scope;
- package and object namespaces;
- bundle/selector behavior;
- compatibility duration;
- deprecation milestones;
- migration identity mapping;
- public route behavior;
- release/correction/rollback mapping;
- ownership and review duties.

### Migration record

A migration should bind:

| Field | Requirement |
|---|---|
| `migration_id` | Stable identity. |
| `decision_ref` | Accepted ADR or governing record. |
| `source_paths` | Exact `air` paths and blob/digest identities. |
| `target_paths` | Exact `atmosphere` paths and expected identities. |
| `policy_bundle_before` | Bundle ID/version/digest/selector before migration. |
| `policy_bundle_after` | Bundle ID/version/digest/selector after migration. |
| `identity_map` | Package, object, route, fixture, and release reference mapping. |
| `review_state` | Named reviewers and approvals. |
| `effective_at` | Activation time. |
| `rollback_target` | Exact prior known-good state. |
| `correction_refs` | Follow-up corrections/supersessions. |
| `validation_refs` | Tests, reports, receipts, and run IDs. |
| `public_impact` | Whether any API/UI/export/report reference changes. |

### Correction triggers

Issue a correction or rollback review when:

- both paths become active;
- a selector chooses the wrong path;
- policy decisions differ by slug;
- evidence/source/release identities change unexpectedly;
- a public route exposes the compatibility slug as authority;
- stale or withdrawn policy remains selected;
- advisory behavior implies life-safety authority;
- logs disclose protected policy inputs;
- migration breaks rollback;
- an ADR is superseded.

### Rollback

Rollback should:

1. disable the new selector or alias;
2. restore the prior bundle ID/digest and target path;
3. restore prior API/UI/export behavior if affected;
4. invalidate policy decisions emitted under the faulty mapping where required;
5. preserve audit records rather than deleting history;
6. issue correction/withdrawal records for affected public artifacts;
7. verify the compatibility lane remains non-authoritative;
8. rerun deterministic path, policy, and public-surface tests.

For this README-only revision, rollback is a Git revert to prior blob `1531b955ebc8474dae384e896117d0e265405e76` plus removal of the paired generated receipt. No policy, runtime, data, release, or public state requires restoration.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Parent domain-policy boundary. |
| [`../atmosphere/README.md`](../atmosphere/README.md) | Preferred Atmosphere policy lane; currently a greenfield scaffold requiring hardening. |
| [`../../../docs/domains/atmosphere/CANONICAL_PATHS.md`](../../../docs/domains/atmosphere/CANONICAL_PATHS.md) | Naming conflict and preferred `atmosphere` placement. |
| [`../../../docs/domains/atmosphere/POLICY.md`](../../../docs/domains/atmosphere/POLICY.md) | Human-facing fail-closed policy doctrine. |
| [`../../../docs/domains/atmosphere/SENSITIVITY.md`](../../../docs/domains/atmosphere/SENSITIVITY.md) | Tiering, generalization, rights, advisory, and cross-lane posture. |
| [`../../../contracts/air/README.md`](../../../contracts/air/README.md) | Air contract compatibility folder and semantic-path conflict. |
| [`../../../contracts/domains/atmosphere/README.md`](../../../contracts/domains/atmosphere/README.md) | Preferred Atmosphere semantic-contract lane. |
| [`../../../schemas/contracts/v1/domains/atmosphere/README.md`](../../../schemas/contracts/v1/domains/atmosphere/README.md) | Preferred Atmosphere schema lane. |
| [`../../../tests/domains/air/README.md`](../../../tests/domains/air/README.md) | Air test compatibility guardrail. |
| [`../../../tests/domains/atmosphere/README.md`](../../../tests/domains/atmosphere/README.md) | Preferred Atmosphere test parent. |
| [`../../../pipeline_specs/air/README.md`](../../../pipeline_specs/air/README.md) | Air pipeline-spec compatibility guardrail. |
| [`../../../pipeline_specs/atmosphere/README.md`](../../../pipeline_specs/atmosphere/README.md) | Preferred Atmosphere declarative-spec lane. |
| [`../../../pipelines/domains/air/README.md`](../../../pipelines/domains/air/README.md) | Air executable-lane alias candidate. |
| [`../../../pipelines/domains/atmosphere/README.md`](../../../pipelines/domains/atmosphere/README.md) | Preferred Atmosphere executable lane. |
| [`../../../packages/policy-runtime/README.md`](../../../packages/policy-runtime/README.md) | Proposed evaluator/runtime boundary; implementation remains unproved. |
| [`../../../policy/bundles/README.md`](../../../policy/bundles/README.md) | Policy bundle and manifest boundary. |
| [`../../../schemas/contracts/v1/policy/policy_decision.schema.json`](../../../schemas/contracts/v1/policy/policy_decision.schema.json) | Current shared finite outcome shape. |
| [`../../../data/registry/sources/atmosphere/README.md`](../../../data/registry/sources/atmosphere/README.md) | Source identity, role, rights, cadence, and activation context. |
| [`../../../data/proofs/atmosphere/README.md`](../../../data/proofs/atmosphere/README.md) | Evidence/proof support; not policy authority. |
| [`../../../release/candidates/atmosphere/README.md`](../../../release/candidates/atmosphere/README.md) | Candidate release boundary. |
| [`../../../.github/workflows/domain-atmosphere.yml`](../../../.github/workflows/domain-atmosphere.yml) | Current explicit readiness-hold workflow. |
| [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) | Required home for recorded path drift. |

[Back to top](#top)

---

## Conflict register

| Conflict | Current evidence | Required resolution |
|---|---|---|
| `air` versus `atmosphere` segment | Both appear across multiple roots; doctrine prefers Atmosphere for new work. | Accepted ADR or lane-register decision. |
| Air policy guardrail versus Atmosphere policy scaffold | Air is compatibility-only; Atmosphere claims canonical but remains over-broad and unimplemented. | Harden preferred lane and keep Air non-authoritative. |
| Contract homes | `contracts/air/` and `contracts/domains/atmosphere/` both exist. | Inventory, identity map, migration decision. |
| Schema homes | Air and Atmosphere variants are referenced and/or present. | One accepted schema namespace and compatibility plan. |
| Test homes | `tests/domains/air/` and `tests/domains/atmosphere/` exist. | Keep Air redirect-only; execute tests in Atmosphere lane. |
| Pipeline-spec homes | Both slugs exist. | One active spec lane and no duplicate discovery. |
| Executable pipeline homes | Both slugs have documentation. | One active package/module namespace. |
| Compatibility dispositions | `REDIRECT`, `HOLD`, `RESTRICT` useful internally. | Normalize into accepted canonical PolicyDecision outcomes. |
| Policy source maturity | Preferred Atmosphere lane contains only README scaffold. | Implement reviewed source, bundle, evaluator, fixtures, tests, validators, and CI. |
| Life-safety boundary | Atmosphere docs require official-authority redirect; no runtime proof. | Contract, policy, fixtures, public-surface tests, and review. |

No conflict in this table is resolved by this README alone.

[Back to top](#top)

---

## Smallest sound resolution sequence

1. **Freeze expansion under `air`.** Add no executable policy, contracts, schemas, fixtures, tests, specs, pipelines, data, or release artifacts there.
2. **Build a byte-complete inventory.** Enumerate every tracked `air` and `atmosphere` path, package namespace, route, bundle reference, schema `$id`, fixture pointer, source record, release record, and consumer.
3. **Record drift.** Add/update the drift register with current paths and evidence.
4. **Decide the canonical segment.** Accept an ADR with compatibility duration, affected roots, identity mapping, and rollback.
5. **Harden the preferred Atmosphere policy README.** Remove over-broad placement language and add a repository-grounded inventory.
6. **Define policy contracts.** Accept policy input, decision, reason-code, obligation, bundle-manifest, selector, and evaluation-receipt contracts.
7. **Implement one policy source lane.** Use one package namespace and fail-closed default.
8. **Create deterministic fixtures.** Cover source roles, rights, freshness, exact siting, low-cost sensors, anti-collapse, advisories, release, correction, and alias behavior.
9. **Implement validators and tests.** Prove policy and migration behavior no-network.
10. **Build immutable bundle and selector.** Bind exact source, dependencies, evaluator, version, digest, and review state.
11. **Integrate governed callers.** API/UI/map/export/AI consume normalized outcomes and obligations without path selection.
12. **Run migration dry-run.** Compare decisions under old/new references and prove identity/evidence/release continuity.
13. **Activate with rollback target.** Separate approval, activation, release, and publication duties.
14. **Deprecate or tombstone Air path.** Preserve redirect/audit metadata only for the approved compatibility period.
15. **Close drift after evidence.** Record validation, review, correction, and rollback results.

Each step should be independently reviewable and reversible.

[Back to top](#top)

---

## Definition of done

This compatibility lane is complete only when:

- [ ] owners and CODEOWNERS are confirmed;
- [ ] an accepted ADR or lane-register decision resolves the canonical segment;
- [ ] a complete `air`/`atmosphere` inventory exists across all responsibility roots;
- [ ] the preferred Atmosphere policy README is repository-grounded and policy-only;
- [ ] no executable policy source remains under `policy/domains/air/`;
- [ ] one policy package namespace and entrypoint are accepted;
- [ ] one immutable bundle/manifest/evaluator/selector path is accepted;
- [ ] shared policy input and decision contracts cover the required Atmosphere context;
- [ ] compatibility dispositions are normalized without inventing public outcomes;
- [ ] reason-code and obligation registries are accepted;
- [ ] deterministic no-network fixtures and executable tests cover alias, anti-collapse, rights, freshness, caveat, advisory, release, correction, and rollback behavior;
- [ ] validators and CI invoke repository-native commands and fail closed;
- [ ] public API/UI/map/export/AI cannot select or expose compatibility policy as authority;
- [ ] official-authority redirection is implemented and tested;
- [ ] release/correction/withdrawal/rollback references use the accepted slug;
- [ ] rollback has been exercised;
- [ ] drift records are closed with evidence;
- [ ] generated receipts and review records are complete;
- [ ] no sensitive, restricted, medical, regulatory, or life-safety claim is introduced.

Until then, the lane remains `draft`, compatibility-only, and non-authoritative.

[Back to top](#top)

---

## Open verification register

| Item | Why it matters |
|---|---|
| Accepted `air` versus `atmosphere` ADR | Determines canonical authority. |
| Complete tracked-file inventory | Prevents hidden duplicate sources and consumers. |
| Current CODEOWNERS and steward assignments | Required for accountable review. |
| Policy package namespace and entrypoint | Prevents evaluator ambiguity. |
| Preferred Atmosphere policy source inventory | Required before claiming implementation. |
| Bundle/manifest/evaluator/selector identity | Required for deterministic execution and replay. |
| Shared policy input completeness | Required for rights, evidence, sensitivity, freshness, and release decisions. |
| Reason-code and obligation registries | Prevents incompatible downstream behavior. |
| Exact-station generalization profile | Required for public-safe coordinates where applicable. |
| Low-cost-sensor caveat/correction profile | Required to prevent authority overclaim. |
| Source-specific rights matrix | Required for legally and contractually safe use. |
| Stale-state thresholds per source | Required to avoid current-condition overclaim. |
| Advisory/official-authority redirect contract | Required to prevent life-safety impersonation. |
| Executable Atmosphere policy tests | Required before enforcement claims. |
| Dedicated policy validators | Required for bundle/input/decision integrity. |
| Public API/UI/map/export/AI behavior | Required to prove compatibility cannot bypass policy. |
| Release and rollback mapping | Required before any public-impacting migration. |
| Branch protection and required checks | Required to know whether CI signals are enforced. |
| Production consumers and deployment state | Required before operational claims. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Supports | Limit |
|---|---|---|
| Prior `policy/domains/air/README.md` | Existing guardrail intent and path. | v0.1 lacked current repository inventory and cross-root evidence. |
| `policy/README.md` | Singular policy root owns allow/deny/restrict/abstain behavior. | Root README remains short and `PROPOSED`. |
| `policy/domains/atmosphere/README.md` | Preferred policy lane exists. | It is a 33-line greenfield scaffold and over-broad. |
| `docs/domains/atmosphere/CANONICAL_PATHS.md` | Prefers `atmosphere`; treats `air` as ADR-class drift. | Draft navigation document; accepted ADR still absent. |
| `docs/domains/atmosphere/POLICY.md` | Anti-collapse, rights, caveat, stale-state, and advisory policy intent. | Draft doctrine; paths/enforcement proposed. |
| `docs/domains/atmosphere/SENSITIVITY.md` | T0/T1 posture, exact-siting generalization, rights holds, official-authority denial. | Per-object implementation remains proposed. |
| `contracts/air/README.md` | Contract slug conflict and compatibility posture. | Does not settle canonical contract home. |
| `tests/domains/air/README.md` | Air test lane is compatibility-only. | No direct executable tests established. |
| `tests/domains/atmosphere/README.md` | Preferred test parent and required proof families. | Executable depth remains unverified. |
| `pipeline_specs/air/README.md` | Air spec lane is a compatibility guardrail. | No active spec established. |
| `.github/workflows/domain-atmosphere.yml` | Current repository maturity is guarded by explicit holds. | Performs no substantive domain policy/validation/proof/release work. |
| `packages/policy-runtime/src/policy_runtime/core.py` | Runtime core is a comment-only placeholder. | No evaluator implementation. |
| `schemas/contracts/v1/policy/policy_decision.schema.json` | Shared outcome enum and required decision fields. | Status is `PROPOSED`; compatibility dispositions not included. |
| Directory Rules | Responsibility-root and parallel-authority controls. | Does not itself prove current implementation. |
| AI Build Operating Contract | Truth labels, cite-or-abstain, trust membrane, fail-safe policy, review and receipt discipline. | Doctrine; runtime proof still required. |

---

## Changelog

| Date | Version | Change | Status |
|---|---|---|---|
| 2026-06-15 | v0.1 | Expanded an empty placeholder into an Air/Atmosphere slug-conflict guardrail. | Documentation only; repository depth largely unverified. |
| 2026-07-19 | v0.2 | Replaced the generic guardrail with a pinned repository-grounded compatibility boundary; confirmed the preferred Atmosphere lane and current scaffolds; added cross-root drift evidence, alias invariants, decision normalization, reason/obligation families, public-surface rules, validation matrix, review duties, ADR/migration/rollback contract, implementation sequence, definition of done, open verification, and evidence ledger. | Documentation and provenance receipt only; no policy enforcement changed. |

---

KFM rule: `policy/domains/air/` is a compatibility and migration guardrail only. It must not become an active policy source, bundle selector, public alias, emergency authority, or parallel truth path while the `air` versus `atmosphere` decision remains unresolved.

<p align="right"><a href="#top">Back to top</a></p>
