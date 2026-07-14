<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-atmosphere-readme
title: configs/domains/atmosphere/ — Atmosphere Configuration Boundary
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Atmosphere steward · Consumer owner · Validation steward
created: 2026-07-13
updated: 2026-07-13
policy_label: public; config-sublane; atmosphere; non-alert; temporal; source-role-aware; non-secret; non-authoritative; no-live-binding
current_path: configs/domains/atmosphere/README.md
truth_posture: CONFIRMED canonical atmosphere slug, repository-present parent config contract, repository-present Atmosphere doctrine, non-alert boundary, source-role separation rules, and documentation-only lane / PROPOSED future consumer-bound templates / UNKNOWN consumers, precedence, loader behavior, and enforcement / NEEDS VERIFICATION owners, executable validation, source rights, freshness thresholds, slug resolution, and runtime binding
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../docs/registers/DOMAIN_LANE.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/security/SECRETS.md
notes:
  - "This lane contains documentation only. It does not create, load, activate, alert from, or publish an Atmosphere configuration payload."
  - "v0.2 expands the Atmosphere-specific temporal, source-role, stale-state, advisory, validation, correction, and rollback contract without creating a new policy, schema, registry, alert, or release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Domain Configuration

`configs/domains/atmosphere/`

> Safe-to-commit, Atmosphere-specific configuration documentation and future consumer-bound templates. This lane does not own weather, climate, air-quality, advisory, source, evidence, alert, release, or publication truth.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Scope](#scope) · [Inputs](#inputs) · [Outputs](#outputs) · [Configuration contract](#minimum-configuration-contract) · [Temporal and source-role safety](#temporal-source-role-and-public-safety-boundaries) · [Validation](#validation) · [Failure behavior](#failure-behavior) · [Maintenance](#maintenance) · [Related](#related-folders) · [ADRs](#adrs) · [Rollback](#rollback-and-correction)

> [!IMPORTANT]
> **Document lifecycle:** draft `v0.2`  
> **Component maturity:** documentation boundary only  
> **Authority:** implementation-supporting configuration sublane; non-authoritative for truth and governance  
> **Runtime posture:** no Atmosphere payload, loader, consumer binding, source activation, alerting, or public exposure is established by this README

> [!CAUTION]
> KFM Atmosphere is not an emergency alert or life-safety system. Directory presence, a future configuration file, or a parsed value must never activate live sources, issue warnings, suppress official-source redirection, relabel modeled data as observations, accept stale data silently, promote lifecycle state, authorize release, or create KFM publication.

---

## Purpose

This directory defines the safe-to-commit configuration boundary for the canonical Atmosphere / Air / Climate lane.

It may eventually hold small defaults, templates, examples, or review-oriented settings for a **named and verified consumer**. Those files may describe how that consumer should behave, but they cannot decide what an observation proves, whether a model output is current truth, whether an advisory is authoritative, whether stale data may be shown without warning, or whether an artifact may be released.

This README is intended for:

- Atmosphere domain stewards;
- configuration and developer-experience maintainers;
- temporal, source-role, validation, rights, policy, security, and release reviewers;
- package, pipeline, app, runtime, test, and tooling owners that may consume Atmosphere configuration;
- reviewers checking Directory Rules placement, public-safety boundaries, and trust-membrane integrity.

[Back to top](#top)

---

## Authority level

**Configuration-supporting and non-authoritative.**

| Concern | Authority in this lane |
|---|---|
| Atmosphere domain meaning | **None.** Domain doctrine remains in [`docs/domains/atmosphere/`](../../../docs/domains/atmosphere/README.md). |
| Observation, forecast, model, advisory, or climatology truth | **None.** Configuration cannot establish evidentiary status or convert one source role into another. |
| Source identity, role, rights, cadence, and activation | **None.** These require the applicable source registry, connector, policy, rights, and review surfaces. |
| Schema or contract shape | **None.** Configuration may reference a verified schema or contract but must not duplicate or redefine it. |
| Policy, freshness, caveat, or display decision | **None.** A value may select an already-governed profile; it cannot create or weaken policy. |
| Emergency or life-safety authority | **None.** Official issuing authorities and the Hazards lane govern emergency and life-safety direction. |
| Evidence or claim truth | **None.** Configuration cannot create an `EvidenceBundle`, validate a claim, or make generated interpretation sovereign truth. |
| Release or publication | **None.** Configuration cannot authorize promotion, release, public display, or KFM publication. |
| Consumer behavior | **Supporting only.** A verified consumer may read a validated file under an explicit binding and precedence rule. |

A configuration value may point to an authority surface. It does not become authority by repetition, proximity, successful parsing, or use by a UI.

[Back to top](#top)

---

## Status

| Item | State | Safe conclusion |
|---|---:|---|
| Canonical domain slug | **CONFIRMED** | `atmosphere` is present as a canonical human-facing domain lane. |
| Parent configuration contract | **CONFIRMED** | [`configs/domains/README.md`](../README.md) defines this directory as a non-secret, non-authoritative configuration sublane. |
| Atmosphere doctrine | **CONFIRMED repository-present** | [`docs/domains/atmosphere/README.md`](../../../docs/domains/atmosphere/README.md) defines the lane's purpose and source-role boundaries. |
| Current payload inventory | **README ONLY** | This lane establishes documentation, not executable configuration. |
| Consumer binding | **UNKNOWN** | No loader, package, pipeline, app, runtime, or deployment binding is established here. |
| Precedence and merge behavior | **UNKNOWN** | No overlay order, inheritance, environment precedence, or unknown-key behavior is established here. |
| Schema/contract slug | **CONFLICTED** | Repository doctrine identifies `air` versus `atmosphere` path drift. Configuration must not resolve this conflict by creating a parallel authority. |
| Validation enforcement | **NEEDS VERIFICATION** | Executable schema, semantic, freshness, source-role, and rights checks are not proven by this README. |
| Source rights and endpoint behavior | **NEEDS VERIFICATION** | Rights, quotas, cadence, terms, and outage behavior require source-specific evidence. |
| Runtime, alerting, release, and publication | **NOT ESTABLISHED** | Nothing in this lane authorizes operational use, alerts, release, or publication. |

Directory presence must not trigger discovery, network access, source activation, alerting, or publication.

[Back to top](#top)

---

## Scope

### What belongs here

Only small, safe-to-commit configuration material for a named or explicitly proposed Atmosphere consumer belongs here.

- this configuration-boundary README;
- non-secret `*.template.*` files for a verified consumer;
- tiny synthetic examples with clearly fictional stations, timestamps, values, and advisory identifiers;
- conservative review, hold, caveat, stale-state, and official-source-redirect defaults;
- public-safe display profile selectors that reference governed policy rather than embedding policy;
- config migration notes tied to a real key, consumer, version, deprecation path, and rollback target.

### What does not belong here

- real weather, climate, air-quality, smoke, AOD, sensor, model, forecast, advisory, or alert payloads;
- credentials, tokens, private endpoints, workstation paths, internal network details, or live deployment bindings;
- settings that present AQI as pollutant concentration;
- settings that present AOD as PM2.5;
- settings that present model fields, forecasts, normals, or anomalies as current observations;
- settings that remove low-cost sensor correction, confidence, caveat, or limitations requirements;
- emergency or life-safety instructions, alert authority, or suppression of official-source redirection;
- silent stale-data fallback or values that hide missing, delayed, partial, or failed source state;
- policy, registry, schema, contract, receipt, proof, release, correction, or publication authority;
- duplicate `air` or `atmosphere` authority paths created to bypass the unresolved slug conflict.

### Explicit non-ownership

This configuration lane does not own:

- emergency and hazard event truth, which belongs to the Hazards lane and official issuing authorities;
- crop, yield, or field truth, which belongs to Agriculture;
- streamflow, flood, or water-body truth, which belongs to Hydrology;
- ecological occurrence or sensitive-location truth, which belongs to the applicable biodiversity lane;
- built-environment, road, or infrastructure truth;
- source registration, evidence resolution, policy decisions, review decisions, release decisions, or public publication state.

[Back to top](#top)

---

## Inputs

Any future configuration payload requires all of the following before it can be treated as consumer-ready:

1. a named consumer and owning component;
2. an explicit file format and format version;
3. a verified contract or schema reference where one exists;
4. an explicit source-role model covering observed, regulatory, modeled, forecast, climatological, advisory, and aggregate data;
5. declared temporal semantics, including observation time, issue time, valid time, ingestion time, and freshness window where applicable;
6. a verified source-rights, terms, attribution, cadence, and outage posture;
7. synthetic or public-safe placeholders only;
8. a declared load path, precedence rule, unknown-key behavior, and fail-safe default;
9. no-network fixtures and deterministic validation;
10. a correction, deactivation, and rollback path.

A proposed file that lacks any required binding remains documentation or an unactivated template.

[Back to top](#top)

---

## Outputs

This lane currently outputs documentation only.

A future configuration file may support a verified consumer by selecting conservative defaults, named display profiles, temporal windows, caveat behavior, or review routing. It cannot:

- activate a live source;
- issue or suppress an alert;
- convert AQI into concentration;
- convert AOD into PM2.5;
- convert forecasts, model fields, normals, or anomalies into observations;
- hide stale, missing, delayed, partial, or failed source state;
- create evidence, approve policy, release an artifact, or establish KFM publication.

[Back to top](#top)

---

## Minimum configuration contract

Every future non-README file in this directory should document or be accompanied by the following information.

| Field | Requirement |
|---|---|
| Consumer | Exact package, pipeline, app, runtime, test, or tool that reads the file. |
| Purpose | One bounded behavior the file configures. |
| Format and version | File format plus schema or contract version when verified. |
| Activation posture | Inactive by default unless an explicit, reviewed binding says otherwise. |
| Load path | Exact mechanism by which the named consumer locates the file. |
| Precedence | Order relative to defaults, environment, deployment, and local overrides. |
| Unknown keys | Reject or hold by default unless the verified consumer defines another safe behavior. |
| Source roles | Observed, regulatory, modeled, forecast, climatological, advisory, and aggregate roles remain distinct. |
| Temporal semantics | Observation, issue, valid, ingestion, expiry, and freshness meanings are explicit where applicable. |
| Stale-state behavior | Stale or delayed inputs remain visibly stale and cannot silently fall back to apparently current truth. |
| Rights and attribution | Verified source-specific terms and required attribution references. |
| Public-safety behavior | No emergency authority; official-source redirect and Hazards handoff remain intact. |
| Validation | Parse, schema, semantic, temporal, source-role, rights, secret, and sensitivity checks. |
| Fixtures | Synthetic, deterministic, no-network examples covering valid and invalid cases. |
| Correction and rollback | Owner, deactivation method, prior known-good state, and transparent correction path. |

Do not add a payload merely to satisfy directory completeness. A file is justified only by a verified consumer and an enforceable contract.

[Back to top](#top)

---

## Temporal, source-role, and public-safety boundaries

### Source-role separation

The following categories must remain distinguishable in configuration, validation, display, and downstream evidence:

| Role | Configuration must not imply |
|---|---|
| Observation | That a forecast, model, climatology, advisory, or aggregate is directly observed. |
| Regulatory record | That every sensor or estimate has regulatory authority. |
| Low-cost sensor observation | That correction, confidence, calibration, caveat, and limitations review can be disabled. |
| Model field | That the field is an observation or guaranteed forecast outcome. |
| Forecast | That the value is current observed state. |
| Climate normal | That the normal is a current measurement. |
| Climate anomaly | That an anomaly is an absolute observation without its baseline and period. |
| AQI | That the index value is pollutant concentration. |
| AOD | That aerosol optical depth is equivalent to surface PM2.5. |
| Advisory context | That KFM is the issuing authority or may replace the official source. |
| Aggregate or derived product | That the derivative outranks its evidence, validation, caveats, and release lineage. |

### Time handling

A consumer-bound file must not collapse distinct time meanings. Where relevant, it must preserve:

- observation time;
- source issue time;
- forecast valid time or interval;
- model initialization time;
- ingestion and processing time;
- climatology baseline period;
- expiry or stale-after threshold;
- correction or supersession time.

Missing or ambiguous time fields must result in a hold, abstention, explicit stale state, or error according to the verified consumer contract. They must not produce apparently current truth.

### Advisory and alert boundary

Configuration may select a presentation profile that links to an official advisory source. It cannot:

- originate or modify an official advisory;
- claim that KFM is the issuing authority;
- suppress source identity, issue time, expiry, or official redirect;
- transform advisory context into emergency instructions;
- bypass the Hazards lane for emergency and life-safety interpretation.

### Slug conflict

The repository-present Atmosphere doctrine records a conflict between `air` and `atmosphere` contract or schema paths. This directory uses the canonical human-facing slug `atmosphere`, but it must not create compatibility files, alternate schema homes, duplicate contracts, or automatic path aliases to resolve that conflict. Resolution requires the appropriate ADR and drift-register update.

[Back to top](#top)

---

## Validation

### Documentation validation

For README-only changes:

- Markdown headings, anchors, links, tables, callouts, and final newline resolve;
- the KFM Meta Block remains structurally consistent with adjacent files;
- no credentials, private endpoints, live bindings, real payloads, or life-safety instructions are introduced;
- no wording implies current runtime, CI, source activation, alerting, release, or publication behavior without evidence;
- AQI, concentration, AOD, PM2.5, model, forecast, climatology, advisory, and observation roles remain distinct;
- the `air` versus `atmosphere` conflict remains visible and unresolved by configuration.

### Future executable configuration validation

Before the first non-README payload is activated, validation should cover:

1. parse and format validation;
2. schema or contract validation against a verified canonical path;
3. consumer binding and load-path verification;
4. precedence, override, and unknown-key behavior;
5. temporal semantics and freshness-window validation;
6. source-role non-collapse checks;
7. AQI-versus-concentration and AOD-versus-PM2.5 denials;
8. model, forecast, normal, anomaly, advisory, and observation distinction;
9. stale, missing, delayed, partial, outage, and recovery behavior;
10. source rights, terms, attribution, and redistribution checks;
11. no-secret and no-live-binding checks;
12. deterministic no-network fixture tests;
13. correction, deactivation, and rollback rehearsal.

Executable config validation remains **NOT APPLICABLE** while this directory contains only this README.

[Back to top](#top)

---

## Failure behavior

A verified consumer should use finite, inspectable outcomes rather than silent fallback.

| Condition | Minimum safe outcome |
|---|---|
| File missing and optional | Use a documented conservative default and record that no domain override loaded. |
| File missing and required | `ERROR` or `HOLD`; do not continue with guessed values. |
| Parse or schema failure | `ERROR`; reject the file. |
| Unknown key | Reject or `HOLD` unless the verified contract explicitly permits it. |
| Ambiguous source role | `HOLD` or `ABSTAIN`; do not relabel the value. |
| Missing or ambiguous time | `HOLD`, explicit stale state, or `ABSTAIN`; do not present as current. |
| Stale source | Preserve stale status and caveat; do not silently substitute apparently current truth. |
| Source outage | Report outage or unavailable state; do not fabricate continuity. |
| Rights or attribution unresolved | `DENY` or `HOLD` for release-facing use. |
| AQI/concentration or AOD/PM2.5 collapse | `ERROR` or `DENY`. |
| Model or forecast presented as observation | `ERROR` or `DENY`. |
| Advisory lacks official-source redirect | `HOLD` or `DENY` for public display. |
| Requested emergency or life-safety action | Redirect to the official authority and applicable Hazards workflow; KFM does not originate the instruction. |
| Slug conflict affects canonical binding | `HOLD` pending ADR-backed resolution. |
| Release state unresolved | `DENY`; configuration cannot authorize release. |

A warning log alone is insufficient when the unsafe value would still be consumed or displayed as authoritative.

[Back to top](#top)

---

## Review burden

README changes require configuration/docs and Atmosphere review.

Any future payload also requires review from the named consumer owner and the applicable:

- validation steward;
- temporal and source-role reviewer;
- source, rights, and attribution reviewer;
- policy and public-safety reviewer;
- security reviewer;
- release reviewer;
- ADR or architecture owner when the `air` versus `atmosphere` conflict is implicated.

A configuration review does not substitute for source admission, evidence review, policy review, release review, or official alert authority.

[Back to top](#top)

---

## Maintenance

### Definition of done for a future payload

- [ ] A named consumer and owner are recorded.
- [ ] The format, version, schema or contract reference, and canonical slug are verified.
- [ ] Load path, precedence, override, and unknown-key behavior are tested.
- [ ] Source roles remain distinct.
- [ ] Temporal meanings and stale-state behavior are explicit.
- [ ] AQI, AOD, model, forecast, climatology, advisory, and observation denials are tested.
- [ ] Rights, terms, attribution, cadence, and outage behavior are verified.
- [ ] Synthetic no-network fixtures cover valid, invalid, stale, denied, held, and error cases.
- [ ] No secrets, private endpoints, real source payloads, or live deployment bindings are present.
- [ ] Public-safety and official-source redirect behavior is reviewed.
- [ ] Correction, deactivation, and rollback are rehearsed.
- [ ] The file does not claim release or publication authority.

### Change discipline

- preserve the documentation-only default until a consumer is verified;
- keep examples synthetic and unmistakably non-production;
- treat key renames and path moves as migrations with compatibility and rollback analysis;
- do not create a second schema, contract, registry, policy, receipt, proof, release, or documentation authority;
- record unresolved placement or slug drift in the canonical drift register;
- re-run relevant validation after any substantive change.

[Back to top](#top)

---

## Related folders

- [`../README.md`](../README.md) — parent domain-configuration contract.
- [`../../README.md`](../../README.md) — repository-wide configuration boundary.
- [`../../../docs/domains/atmosphere/README.md`](../../../docs/domains/atmosphere/README.md) — Atmosphere doctrine and domain boundary.
- [`../../../docs/registers/DOMAIN_LANE.md`](../../../docs/registers/DOMAIN_LANE.md) — canonical lane register.
- [`../../../docs/registers/DRIFT_REGISTER.md`](../../../docs/registers/DRIFT_REGISTER.md) — unresolved path, terminology, and authority drift.
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — placement law and responsibility-root rules.
- [`../../../docs/security/SECRETS.md`](../../../docs/security/SECRETS.md) — secret-handling posture.

These links identify related authority surfaces. Their presence does not prove that a consumer, schema, validator, source, CI check, runtime binding, or release path is active.

[Back to top](#top)

---

## ADRs

No ADR is introduced by this README.

The following changes require separate governance rather than a configuration-only edit:

- resolving the `air` versus `atmosphere` schema or contract slug conflict;
- changing the canonical domain set;
- changing source-role semantics or temporal truth rules;
- creating alert, emergency, or life-safety authority;
- weakening AQI, AOD, model, forecast, climatology, low-cost sensor, advisory, stale-state, or official-source redirect boundaries;
- introducing universal domain-config discovery, precedence, or activation behavior;
- creating a new schema, contract, policy, registry, receipt, proof, release, or publication authority.

[Back to top](#top)

---

## Rollback and correction

Before merge, rollback means leaving the draft pull request unmerged or reverting the scoped branch commit.

After merge:

1. create a transparent revert commit or revert pull request;
2. restore the prior known-good configuration documentation or payload;
3. re-run applicable documentation, schema, temporal, source-role, rights, public-safety, and consumer checks;
4. record any correction or supersession required by repository doctrine;
5. verify that no stale, relabeled, alert-like, release, or publication behavior remains active.

Do not reset or force-push shared history. Configuration rollback does not retract an already released artifact; release correction requires the governing release and correction workflow.

[Back to top](#top)

---

## Last reviewed

**2026-07-13**, against the repository-present parent contract and Atmosphere doctrine available on `main` during this revision. Review again before the first non-README payload, consumer binding, source activation, or slug-resolution change.
