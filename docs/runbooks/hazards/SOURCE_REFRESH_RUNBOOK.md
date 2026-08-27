<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hazards-source-refresh
title: Hazards Source Refresh Runbook
type: operational-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; LIVE_SOURCE_REFRESH_HELD; BOUNDED_SYNTHETIC_VALIDATION_ONLY; NON_RELEASE; NON_PUBLICATION
owners: "@bartytime4life — verified CODEOWNERS route; accountable Hazards, source, rights, sensitivity, operations, review, and release stewardship NEEDS VERIFICATION"
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; hazards; source-refresh; fail-closed; not-for-life-safety; non-publisher
owning_root: docs/
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
authority_effect: none
source_activation_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ca8a81a9f7728347ce19843b7a681d5c9fe19ba0
  target_path: docs/runbooks/hazards/SOURCE_REFRESH_RUNBOOK.md
  target_prior_blob: f2a5a8ddb57be9ff336ac9cb00de4b30a35a3d82
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  hazards_source_registry_readme_blob: bed3a870b83afce8a461a152e782c7a1e1897be6
  dotted_storm_events_descriptor_blob: db7d6c2c1e261e9687d74497498761f228bedd4b
  alternate_storm_events_descriptor_blob: 902da1bd0e7164d26f70bf4f2835fb1b48b8d69a
  storm_events_underscore_connector_readme_blob: 8e7dac6e913e9276c719e674c56719770bd65c43
  storm_events_hyphen_connector_readme_blob: a47e3eaf0e67c67b2126fd0c6a35249c11b4f1e9
  storm_events_watcher_readme_blob: e36c8e8213a51fc00290623dff5ca518881910af
  storm_events_pipeline_spec_blob: 74aad5c7ebbbc7e8c6dc0c848e3449c9dde0fcab
  domain_workflow_blob: 9d48f97ff33fedd4f2acf3a6aed2b6753d0caaea
  hazards_smoke_test_blob: af8550b8e22c7022e30cc11e5c77a951898cf1f0
  usdm_materiality_test_blob: dc71faa0667b8817abe070a7fef08361c9ddc743
  usdm_materiality_validator_blob: dac5f56560f40e725c4d8924d8d20138ae5708fd
  open_pull_requests_touching_target: 0
source_lineage:
  - title: kfm_hazards_extended_pro_pdf_only_blueprint.pdf
    source_class: PLANNING_LINEAGE
    use: not-for-life-safety, source-role, temporal, evidence, and offline-first design context only
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and draft-pull-request delivery
related:
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../README.md
  - ../../domains/hazards/README.md
  - ../../domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../domains/hazards/SOURCE_REGISTRY.md
  - ../../domains/hazards/SOURCE_ROLE_MATRIX.md
  - NO_NETWORK_TEST_RUNBOOK.md
  - PROMOTION_RUNBOOK.md
  - ROLLBACK_RUNBOOK.md
  - ROLLBACK_DRILL.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/hazards/README.md
  - ../../../data/registry/sources/hazards/noaa.storm_events.yaml
  - ../../../data/registry/hazards/sources/noaa_storm_events.yaml
  - ../../../connectors/noaa_storm_events/README.md
  - ../../../connectors/noaa-storm-events/README.md
  - ../../../pipeline_specs/hazards/noaa_storm_events.yaml
  - ../../../tools/ingest/storm_events_watch/README.md
  - ../../../policy/domains/hazards/README.md
  - ../../../release/candidates/hazards/README.md
  - ../../../.github/workflows/domain-hazards.yml
  - ../../../tests/domains/hazards/test_hazards_smoke.py
  - ../../../tests/domains/hazards/test_validate_usdm_materiality.py
  - ../../../tools/validators/domains/hazards/validate_usdm_materiality.py
notes:
  - The current repository has bounded, no-network drought fixture and USDM materiality validation; it does not have a verified operational Hazards source-refresh executor.
  - The only Hazards NOAA Storm Events registry records are proposal/TBD placeholders, the source-authority register is empty and projection-only, connector topology is conflicted and README-only, and the pipeline spec is a placeholder.
  - A passing synthetic materiality result can create a review candidate only inside its fixture profile; it cannot activate a source, authorize live retrieval, admit data, build proof, release, promote, deploy, or publish.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Source Refresh Runbook

> **One-line purpose.** Determine whether a Hazards source refresh is ready for accountable implementation, run the repository's current no-network validation, and produce a truthful handoff without activating a source, fetching live data, changing lifecycle state, or implying release or publication.

[![Status: live refresh held](https://img.shields.io/badge/status-live%20refresh%20held-b42318?style=flat-square)](#current-disposition)
[![Validation: bounded synthetic](https://img.shields.io/badge/validation-bounded%20synthetic-8250df?style=flat-square)](#repository-native-validation)
[![Life safety: no](https://img.shields.io/badge/life%20safety-not%20an%20alerting%20system-b42318?style=flat-square)](#not-for-life-safety-boundary)
[![Source activation: none](https://img.shields.io/badge/source%20activation-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)

<a id="not-for-life-safety-boundary"></a>

> [!CAUTION]
> **KFM Hazards is not an emergency-alerting system, incident-command system, regulatory authority, or substitute for official instructions.** This procedure must not issue, replace, delay, retract, summarize as actionable, or interpret a warning, evacuation order, shelter instruction, medical direction, all-clear, or other life-safety message. Current urgent needs belong with the appropriate official authority.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `LIVE_SOURCE_REFRESH_HOLD / BOUNDED_SYNTHETIC_VALIDATION_AVAILABLE`.** At the pinned repository snapshot, the source-authority register is empty and projection-only; the NOAA Storm Events source records are proposal or TBD placeholders; the competing connector paths are README-only; the Storm Events pipeline spec and watcher are proposed documentation boundaries; and no accepted live retrieval command, active source decision, or operational Hazards refresh pipeline is established. The repository can validate committed synthetic drought fixtures and deterministic USDM materiality semantics. It cannot truthfully claim a live source refresh.

```yaml
work_state: HOLD
available_evidence:
  - BOUNDED_SYNTHETIC_DROUGHT_SCHEMA_AND_FIXTURE_VALIDATION
  - BOUNDED_SYNTHETIC_USDM_MATERIALITY_VALIDATION
reason_codes:
  - HAZ_REFRESH_SOURCE_AUTHORITY_REGISTER_EMPTY
  - HAZ_REFRESH_SOURCE_DESCRIPTOR_PLACEHOLDER
  - HAZ_REFRESH_CONNECTOR_TOPOLOGY_CONFLICTED
  - HAZ_REFRESH_CONNECTOR_IMPLEMENTATION_UNVERIFIED
  - HAZ_REFRESH_PIPELINE_SPEC_PLACEHOLDER
  - HAZ_REFRESH_PROOF_AND_RELEASE_HELD
source_activation_effect: none
lifecycle_effect: none
release_effect: none
publication_effect: none
```

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-terminal-boundary) · [Evidence](#current-repository-evidence) · [States](#state-and-vocabulary-separation) · [Preconditions](#preconditions) · [Procedure](#procedure) · [Validation](#repository-native-validation) · [Interpretation](#interpret-the-bounded-results) · [Quarantine](#quarantine-stale-and-correction-handling) · [Handoff](#source-refresh-handoff-packet) · [Failures](#mandatory-stop-conditions) · [Acceptance](#acceptance-and-negative-cases) · [Maintenance](#maintenance-drift-and-verification-backlog)

---

<a id="goal-and-scope"></a>

## Goal and scope

Use this runbook when a maintainer needs to evaluate, prepare, or review a refresh of an **already proposed or admitted Hazards source** and must first determine what the repository can actually support.

The current safe operating circle is:

```text
exact repository and source identity
  -> source authority, role, rights, cadence, and connector preflight
  -> committed no-network fixture validation
  -> deterministic materiality assessment where implemented
  -> HOLD, ABSTAIN, DENY, ERROR, or review handoff
  -> no live fetch and no lifecycle mutation unless a separate governed path exists
```

### In scope

- freeze the exact repository SHA, source identity, descriptor path, connector path, pipeline-spec path, and reviewer route;
- determine whether the source descriptor and source-activation authority are real, current, and non-placeholder;
- distinguish connector, watcher, pipeline, validator, policy, evidence, proof, candidate, release, and publication responsibilities;
- run the current repository-owned no-network Hazards validation;
- interpret the USDM materiality profile without promoting its finite outcomes into source or release authority;
- record missing rights, sensitivity, cadence, source-role, connector, pipeline, fixture, proof, review, correction, or rollback support;
- prepare a reviewable source-refresh handoff; and
- mark dependent material stale or route unsupported input to quarantine through the owning lifecycle procedure.

### Out of scope

- live NOAA, NWS, FEMA, USGS, NASA, Kansas, local, or other external-source access;
- creating or accepting credentials, API keys, secrets, endpoints, rate-limit policy, or source terms;
- activating or admitting a `SourceDescriptor`;
- selecting a canonical connector path or resolving source-registry topology by documentation alone;
- writing to RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, receipt, proof, release, or PUBLISHED stores;
- assembling a Hazards release candidate;
- approving policy, review, release, deployment, promotion, or publication;
- validating current hazard conditions or operational warning freshness; and
- issuing or interpreting emergency guidance.

[Back to top](#top)

---

<a id="authority-and-terminal-boundary"></a>

## Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [Directory Rules v2](../../doctrine/directory-rules.md) place human operational procedures under `docs/runbooks/`. This is a same-path modernization of an established file, so it creates no new responsibility root or parallel contract, schema, policy, source, evidence, proof, release, or publication home.

| Responsibility | Owning surface | This runbook may do | This runbook must not do |
|---|---|---|---|
| Human procedure | `docs/runbooks/hazards/SOURCE_REFRESH_RUNBOOK.md` | Explain preflight, bounded validation, holds, and handoff | Grant source or release authority |
| Source identity and admission | `data/registry/sources/`, owning descriptor, and accepted activation decision | Require and inspect exact references | Activate, admit, or invent missing fields |
| Source-authority projection | `control_plane/source_authority_register.yaml` | Read current projection state | Treat an empty or proposed projection as authority |
| External acquisition | Ratified path under `connectors/` | Verify implementation, tests, and declared limits | Choose among conflicted paths or perform an unverified fetch |
| Watcher materiality signal | `tools/ingest/` or accepted watcher home | Consume a bounded report | Treat a watcher signal as source truth or publication |
| Pipeline behavior | Accepted `pipelines/` implementation plus `pipeline_specs/` | Verify exact command and stage limits | Infer implementation from a placeholder spec |
| Object meaning and shape | `contracts/` and `schemas/` | Require current references and run validation | Redefine semantics or treat shape validity as truth |
| Policy and review | `policy/` plus authenticated review records | Require finite results and obligations | Invent approval or reviewer authority |
| Lifecycle instances | Governed `data/` phases and accountability families | Describe expected transition evidence | Mutate lifecycle state from Markdown |
| Release and correction | `release/` plus linked evidence, review, correction, and rollback objects | Prepare a bounded handoff | Assemble, sign, approve, release, or publish |
| Public use | Governed API and released public-safe carriers | Preserve the no-direct-source rule | Serve registry, connector, watcher, RAW, or model output directly |

The highest result this runbook can establish today is one of:

```text
SOURCE_REFRESH_PREFLIGHT_COMPLETE
BOUNDED_SYNTHETIC_VALIDATION_PASS
READY_FOR_ACCOUNTABLE_SOURCE_REFRESH_IMPLEMENTATION_REVIEW
```

None means `SOURCE_ACTIVATED`, `SOURCE_REFRESHED`, `RAW_CAPTURED`, `EVIDENCE_RESOLVED`, `POLICY_APPROVED`, `REVIEWED`, `PROOF_COMPLETE`, `RELEASED`, `DEPLOYED`, `PROMOTED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

The observations below are pinned to `main@ca8a81a9f7728347ce19843b7a681d5c9fe19ba0`. Re-read the exact files when the base, source registry, connector, pipeline, workflow, tests, or policy lane changes.

| Surface | CONFIRMED repository evidence | Bounded conclusion |
|---|---|---|
| Runbook path | The target exists under `docs/runbooks/hazards/` | Same-path update is valid; no new path is needed |
| Pull-request overlap | No open pull request matching this target was found before branch creation | A focused branch can proceed; recheck before mutation |
| Source-authority register | `status: PROPOSED`, `authority_mode: projection_only`, `implementation_status: ABSENT`, `entries: []` | No Hazards source is activated by this register |
| Hazards source registry | The subtype-first lane contains a substantive README and `noaa.storm_events.yaml` | The lane exists; one file does not prove admission |
| Dotted Storm Events record | `status: PROPOSED`; the file is explicitly a documentation-inventory placeholder | Not an active or complete descriptor |
| Alternate Storm Events record | Authority, role, rights, cadence, access, and citation remain `TBD` | Not eligible for live retrieval |
| Registry topology | Subtype-first and domain-first source lanes coexist | Canonical descriptor placement remains conflicted |
| Storm Events connector | Underscore and hyphenated paths are README-only; no verified client, parser, product test, or accepted canonical path | No operational connector is established |
| Storm Events pipeline spec | `status: PROPOSED`; placeholder created from documentation inventory | Not an executable pipeline |
| Storm Events watcher | README defines a proposed review-signal boundary and names no executable | No watcher result can be produced from the documented lane |
| Hazards workflow | Runs no-network drought fixture and USDM materiality validation; proof and release jobs are explicit holds | Bounded synthetic validation only |
| Hazards policy | Policy source is draft/default-only and evaluator binding remains unverified | No operational policy decision can be inferred |
| Hazards release candidate lane | The promotion runbook records no current Hazards candidate | No candidate exists to advance |
| Planning lineage | The Drive Hazards blueprint preserves source-role, time, evidence, and not-for-life-safety doctrine but was authored without a mounted repository | Use as planning lineage, never as current implementation proof |

### Current executable evidence

The repository currently proves only this bounded path:

```text
committed drought-family JSON Schemas and fixtures
  -> exact valid/invalid fixture polarity
  -> in-process socket, DNS, and urllib denial checks
  -> deterministic synthetic USDM snapshot comparison
  -> UNCHANGED | SEMANTIC_NON_MATERIAL | MATERIAL | UNDETERMINED
  -> NON_EVENT | PROMOTION_CANDIDATE | HOLD
```

It does not retrieve a live source, resolve current rights, verify current conditions, create a raw capture, resolve EvidenceRef to EvidenceBundle, evaluate an active Hazards policy bundle, assemble proof, create a release candidate, or publish.

[Back to top](#top)

---

<a id="state-and-vocabulary-separation"></a>

## State and vocabulary separation

Keep these states independent.

| State or term | Meaning | Effect |
|---|---|---|
| `WATCHER_SIGNAL` | A watcher reports possible source, schema, correction, cadence, or materiality drift | Review work only; no source or lifecycle effect |
| `SOURCE_REFRESH_PREFLIGHT_COMPLETE` | Required repository and source-edge checks were performed and recorded | No live fetch or admission |
| `BOUNDED_SYNTHETIC_VALIDATION_PASS` | Current committed fixture profile passed | No statement about live source truth |
| `SOURCE_ACTIVATED` | A separate accepted source decision authorizes bounded intake | Outside this runbook |
| `RAW_CAPTURED` | An approved connector preserved an immutable source payload or reference with receipts | Not established by current Hazards implementation |
| `PROMOTION_CANDIDATE` | In the current USDM fixture profile, a deterministic materiality criterion fired | A review signal only; not source admission or release readiness |
| `READY_FOR_ACCOUNTABLE_SOURCE_REFRESH_IMPLEMENTATION_REVIEW` | The missing implementation/authority packet is complete enough for accountable review | Still not activation or execution |
| `PUBLISHED` | A separate governed release transition exposed a public-safe carrier | Outside this runbook |

Do not convert `PROPOSED`, `TBD`, `README-only`, `SKIPPED`, `NOT_RUN`, `PENDING`, `NO_RUN_FOUND`, or an explicit workflow hold into `PASS`.

[Back to top](#top)

---

<a id="preconditions"></a>

## Preconditions

A live source refresh remains **HOLD** unless every applicable condition is supported by immutable or versioned evidence.

| # | Required condition | Minimum evidence | Failure posture |
|---:|---|---|---|
| 1 | Exact repository and source identity | Forty-character repository SHA, source ID, native product/version, descriptor path and digest | `HOLD` or `ERROR` |
| 2 | Canonical descriptor authority | One non-placeholder descriptor in the accepted registry home | `HOLD` |
| 3 | Source activation | Accepted, current source-activation decision bound to the descriptor | `HOLD` or `DENY` |
| 4 | Source role | Canonical role plus role authority and anti-collapse obligations | `ABSTAIN` or `DENY` |
| 5 | Rights and terms | Current access, redistribution, attribution, retention, and citation basis | `HOLD` or `DENY` |
| 6 | Sensitivity and precision | Reviewed sensitivity class, public-use floor, minimization/generalization obligations | `HOLD` or `DENY` |
| 7 | Time and cadence | Source, publication, valid, retrieval, expiry, correction, and expected cadence where material | `ABSTAIN` or `DENY` |
| 8 | Canonical connector | One accepted connector path with implementation, bounded transport rules, tests, and rollback | `HOLD` |
| 9 | Executable pipeline | Accepted pipeline command/spec pair with stage boundaries and deterministic identity | `HOLD` |
| 10 | No-network fixture | Public-safe synthetic fixture that exercises the parser/transform path without live access | `HOLD` |
| 11 | Credentials and egress control | Approved secret ownership, least privilege, redaction, timeout, retry, redirect, size, and audit policy | `HOLD` or `DENY` |
| 12 | Quarantine path | Reason codes, immutable source reference, review route, and no-public-path enforcement | `HOLD` |
| 13 | Correction and rollback | Upstream correction handling, prior safe target, invalidation scope, and replay plan | `ABSTAIN` or `DENY` |
| 14 | Accountable review | Verified assignments and separation where materiality or sensitivity requires it | `HOLD` |
| 15 | Overlap check | No active branch, pull request, migration, or steward work owns the same source or path | `HOLD` |
| 16 | Separate execution authority | Current instruction or governed operation authorizes live external access | `HOLD` |

A green fixture run cannot compensate for a missing descriptor, rights record, canonical connector, active source decision, or separate execution authority.

[Back to top](#top)

---

<a id="procedure"></a>

## Procedure

### 1. Freeze the evaluation baseline

Record the exact repository and source-edge references before inspecting or running anything.

```bash
git rev-parse HEAD
git status --short
python --version
```

Record at least:

```yaml
repository_sha: "<40-character SHA>"
source_id: "<canonical source ID or UNKNOWN>"
descriptor_path: "<path or UNKNOWN>"
descriptor_digest: "<blob/content digest or UNKNOWN>"
activation_decision_ref: "<immutable ref or ABSENT>"
rights_ref: "<immutable ref or UNKNOWN>"
connector_path: "<accepted path or CONFLICTED>"
connector_revision: "<commit/blob or ABSENT>"
pipeline_spec_ref: "<commit/blob or PLACEHOLDER>"
requested_scope: "<source, vintage, geography, and time window>"
operator_or_requestor: "<authenticated identity>"
review_route: "<verified assignment or NEEDS VERIFICATION>"
```

Re-run the overlap check immediately before mutation. Preserve unrelated branches and pull requests.

### 2. Verify source authority before any fetch

Inspect the canonical descriptor and its activation decision. A filename, provider name, endpoint, README, or registry path is not enough.

For the currently tracked NOAA Storm Events surfaces:

- `data/registry/sources/hazards/noaa.storm_events.yaml` is a `PROPOSED` placeholder;
- `data/registry/hazards/sources/noaa_storm_events.yaml` retains `TBD` authority, rights, cadence, and access;
- `control_plane/source_authority_register.yaml` is empty and projection-only.

Therefore the current result is:

```text
HOLD: HAZ_REFRESH_SOURCE_AUTHORITY_UNRESOLVED
```

Do not live-fetch. Do not “complete” the missing fields from general knowledge, the upstream website, a planning PDF, or a second registry copy.

### 3. Verify connector, watcher, and pipeline implementation

Confirm one canonical connector path and inspect its code, tests, fixture profile, transport controls, and emitted object boundary.

Current NOAA Storm Events evidence produces these results:

| Check | Current result |
|---|---|
| Canonical connector path | `CONFLICTED` between underscore and hyphenated README-only lanes |
| Source client/parser | Not verified |
| Product-specific tests | Not verified |
| Source-specific fixture parser path | Not verified |
| Accepted live endpoint/configuration | Not verified |
| Pipeline spec | Proposal placeholder |
| Watcher executable | Not verified |
| Connector workflow enforcement | Not established as source-refresh proof |

Current result:

```text
HOLD: HAZ_REFRESH_CONNECTOR_AND_PIPELINE_UNVERIFIED
```

A watcher README may define future review signals. It cannot substitute for a connector, raw capture, activation decision, or pipeline.

### 4. Run the repository-native no-network checks

Run the bounded validation even when live refresh remains held. It detects regression in the implemented drought fixture lane and provides an exact handoff fact.

See [Repository-native validation](#repository-native-validation).

### 5. Classify the result without broadening it

Use [Interpret the bounded results](#interpret-the-bounded-results). A synthetic `MATERIAL / PROMOTION_CANDIDATE` result means the fixture's deterministic thresholds fired. It does not mean a source may be fetched, admitted, promoted, or published.

### 6. Decide the next state

| Condition | Result | Next action |
|---|---|---|
| Descriptor, activation, rights, canonical connector, or executable pipeline missing | `HOLD` | Produce the handoff packet; do not fetch |
| Evidence cannot establish role, time, or source identity | `ABSTAIN` | Narrow the request or obtain authoritative records |
| Rights, sensitivity, life-safety, public-path, or role boundary is violated | `DENY` | Stop; preserve evidence and escalate |
| Validator or required input cannot be evaluated safely | `ERROR` | Repair evaluator/input before retry |
| Bounded fixtures pass but live path remains incomplete | `SOURCE_REFRESH_PREFLIGHT_COMPLETE` | Route implementation/authority gaps for review |
| Every precondition is met under a separately authorized live-source operation | Outside current repository evidence | Follow the accepted connector's own reviewed command and receipt contract; this runbook intentionally supplies no unverified live command |

### 7. Preserve the lifecycle boundary when a future live path exists

A future accepted connector may emit only to controlled RAW or QUARANTINE intake. It must record:

- exact `SourceDescriptor` and activation-decision references;
- connector and pipeline revisions;
- source-native object identity and product/vintage;
- source, publication, valid, retrieval, expiry, and correction times where material;
- content digest or immutable source-object reference;
- rights, attribution, access, and sensitivity snapshots;
- fetch status, transport limits, retries, redirects, and size/decompression results;
- quarantine reason or raw-capture receipt;
- no claim of evidence closure, review, release, or publication.

The connector must not write directly to WORK, PROCESSED, CATALOG, TRIPLET, proof, release, or PUBLISHED lanes.

### 8. Hand off downstream work without collapsing states

After controlled intake exists, normalization, evidence resolution, policy, catalog, proof, candidate assembly, promotion, correction, and rollback remain separate operations. Use the [Hazards Promotion Runbook](./PROMOTION_RUNBOOK.md) only after a real candidate and its closure objects exist. Current proof and release jobs remain explicit holds.

[Back to top](#top)

---

<a id="repository-native-validation"></a>

## Repository-native validation

### Preconditions

1. Work from a clean checkout or isolated worktree at a recorded commit SHA.
2. Run from the repository root.
3. Use Python 3.11 for hosted-workflow parity unless the workflow pin changes.
4. Keep live-source credentials, endpoints, tokens, and production data out of the focused validation environment.
5. Install only the repository-declared, hash-locked validation profile.

Dependency bootstrap:

```bash
python tools/ci/install_python_ci.py project-runtime
```

The bootstrap may require an approved package cache or network before the focused test. Record dependency acquisition separately; it is not part of the no-live-source validation claim.

### Focused commands

```bash
python -m unittest -v tests.domains.hazards.test_hazards_smoke
make hazards-validate
```

Equivalent explicit USDM commands currently owned by the Make target are:

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
python -m unittest discover \
  --start-directory tests/domains/hazards \
  --pattern 'test_validate_usdm_materiality.py' \
  --verbose

KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
python tools/validators/domains/hazards/validate_usdm_materiality.py --fixtures
```

### What the checks cover

| Check | Covered behavior |
|---|---|
| Drought schema/fixture smoke | Three JSON Schema 2020-12 object families; exact valid/invalid inventories; duplicate-key, regular-file, symlink, UTF-8, and fixture-size protections |
| Process-level network guard | Selected socket connect, DNS resolution, and `urllib.request.urlopen` paths fail closed during the smoke test |
| USDM materiality tests | Four valid finite states, deterministic trigger criteria, exact invalid finding sets, and rejection of legal-declaration fields in an observation snapshot |
| USDM fixture validator | Fixture-only declaration, network forbidden, time ordering, geometry digest, severity hierarchy, thresholds, and explicit governance non-effects |

### What the checks do not cover

- operating-system firewall, namespace, proxy, DNS, or air-gap enforcement;
- live source availability, endpoint behavior, rate limits, credentials, terms, or current rights;
- live parser correctness or raw-capture integrity;
- current drought or hazard conditions;
- SourceDescriptor admission or source activation;
- EvidenceRef-to-EvidenceBundle resolution;
- Hazards policy evaluation or authenticated review;
- proof, candidate, release, deployment, promotion, or publication.

[Back to top](#top)

---

<a id="interpret-the-bounded-results"></a>

## Interpret the bounded results

The USDM validator has four deterministic assessment states.

| Assessment state | Validator outcome | Meaning inside the fixture profile | Forbidden inference |
|---|---|---|---|
| `UNCHANGED` | `NON_EVENT` | No tested metric or geometry change | The live source was checked |
| `SEMANTIC_NON_MATERIAL` | `NON_EVENT` | Change exists but no configured materiality criterion fired | The change is safe to publish |
| `MATERIAL` | `PROMOTION_CANDIDATE` | One or more deterministic fixture criteria fired | A source, candidate, release, or publication was authorized |
| `UNDETERMINED` | `HOLD` | Geometry changed without supporting metric change | The operator may resolve the ambiguity by assumption |

The validator also requires these governance flags to remain false:

```text
authority_created
source_activated
promotion_authorized
release_authorized
publication_authorized
```

Any attempt to set one true is a `GOVERNANCE_BOUNDARY_VIOLATION`.

Record:

- exact repository SHA;
- exact commands;
- exit codes;
- finite assessment and triggered criteria;
- validation findings;
- whether dependency bootstrap used external access;
- unresolved source/connector/pipeline conditions; and
- `live_fetch: NOT_RUN`.

[Back to top](#top)

---

<a id="quarantine-stale-and-correction-handling"></a>

## Quarantine, stale, and correction handling

### Quarantine

Quarantine is a governed hold, not a publishable staging area. Route a future intake to the owning quarantine path when any of these conditions applies:

- source identity or role is ambiguous;
- descriptor or activation reference is missing;
- rights, terms, attribution, access, or retention is unresolved;
- sensitivity or public precision is unsafe;
- content digest, archive, encoding, schema, geometry, or time checks fail;
- operational context is expired or cannot be bounded;
- the upstream correction/supersession relationship is unclear;
- evidence support cannot be resolved; or
- policy or review returns `DENY`, `ABSTAIN`, `ERROR`, or `HOLD`.

Do not invent a quarantine reason-code schema in this document. Use the accepted lifecycle contract when one is verified and preserve the original input reference, findings, actor, time, and review path.

### Stale is not wrong

- **Stale** means the declared freshness or review window elapsed, a source vintage was superseded, or required support is no longer current.
- **Wrong** means the claim or carrier is substantively incorrect.

A missed refresh does not justify silent replacement. Mark dependent claims or layers stale through their owning surfaces, preserve the prior release identity, and record what evidence is missing.

### Operational context expiry

An expired warning, watch, or advisory must not be presented as a current KFM warning state. It may remain historical/contextual evidence only when the source, issue time, expiry time, retrieval time, correction state, official-source referral, and not-for-life-safety boundary remain visible.

### Correction and rollback

When a future refresh reveals a defect in a released Hazards carrier:

1. contain or disable the affected KFM surface when rights, sensitivity, or life-safety risk requires immediate action;
2. preserve the failed release and evidence identity;
3. emit or reference the governed correction/withdrawal objects;
4. invalidate dependent catalog, map, export, Evidence Drawer, search, and AI derivatives;
5. use the [Rollback Runbook](./ROLLBACK_RUNBOOK.md) and [Rollback Drill](./ROLLBACK_DRILL.md) through accountable release authority; and
6. verify recovery without implying that KFM changed the official upstream source.

[Back to top](#top)

---

<a id="source-refresh-handoff-packet"></a>

## Source-refresh handoff packet

Use this documentation-only worksheet when the current result is `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or bounded preflight completion. It does not create a source, receipt, policy decision, review record, or release object.

```yaml
source_refresh_handoff:
  repository:
    base_sha: "<40-character SHA>"
    branch_or_pr: "<ref or NONE>"
    changed_paths: []
  request:
    source_id: "<canonical ID or UNKNOWN>"
    source_family: "<family>"
    native_product_and_version: "<value or UNKNOWN>"
    spatial_scope: "<value or UNKNOWN>"
    temporal_scope: "<value or UNKNOWN>"
  authority:
    descriptor_ref: "<immutable ref or PLACEHOLDER>"
    activation_decision_ref: "<immutable ref or ABSENT>"
    source_authority_register_entry: "<ref or ABSENT>"
    rights_ref: "<ref or UNKNOWN>"
    sensitivity_ref: "<ref or UNKNOWN>"
    review_assignments: "<refs or NEEDS VERIFICATION>"
  implementation:
    connector_path: "<accepted path or CONFLICTED>"
    connector_revision: "<ref or ABSENT>"
    pipeline_spec_ref: "<ref or PLACEHOLDER>"
    executable_command: "<reviewed command or ABSENT>"
    no_network_fixture_ref: "<ref>"
  validation:
    dependency_bootstrap: "<record>"
    smoke_test: "<PASS | FAIL | NOT_RUN>"
    materiality_test: "<PASS | FAIL | NOT_RUN>"
    assessment_state: "<UNCHANGED | SEMANTIC_NON_MATERIAL | MATERIAL | UNDETERMINED | NOT_APPLICABLE>"
    triggered_criteria: []
    limitations: []
  result:
    work_state: "<HOLD | ABSTAIN | DENY | ERROR | SOURCE_REFRESH_PREFLIGHT_COMPLETE>"
    reason_codes: []
    live_fetch: "NOT_RUN"
    lifecycle_effect: "NONE"
    release_effect: "NONE"
    publication_effect: "NONE"
  next_review:
    owner_route: "@bartytime4life"
    accountable_roles: "<NEEDS VERIFICATION>"
    requested_decision: "<bounded decision>"
```

Do not populate missing authority fields with plausible defaults. Preserve `UNKNOWN`, `ABSENT`, `PLACEHOLDER`, or `NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="mandatory-stop-conditions"></a>

## Mandatory stop conditions

Stop without live retrieval or lifecycle mutation when any of the following is true.

| Condition | Required result |
|---|---|
| Source-authority register has no accepted entry for the source | `HOLD` |
| Descriptor is a placeholder, incomplete, duplicated, or in a conflicted home | `HOLD` |
| Source role cannot be fixed without collapsing observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic meaning | `ABSTAIN` or `DENY` |
| Rights, attribution, redistribution, retention, or access terms are unresolved | `HOLD` or `DENY` |
| Sensitivity or public precision is unresolved | `HOLD` or `DENY` |
| Connector path is conflicted or implementation/tests are absent | `HOLD` |
| Pipeline spec is a placeholder or has no executable implementation | `HOLD` |
| Live command, credential owner, egress rules, or audit path is unverified | `HOLD` |
| No public-safe no-network fixture exists for the proposed parser/transform path | `HOLD` |
| Focused synthetic validation fails | `ERROR` or `DENY`, according to the finding |
| A watcher, connector, or test attempts to publish or authorize release | `DENY` |
| An operational product is framed as KFM life-safety guidance | `DENY` |
| A synthetic `PROMOTION_CANDIDATE` result is used as source or release approval | `DENY` |
| Evidence, policy, review, correction, or rollback closure is missing for a downstream candidate | `HOLD`, `ABSTAIN`, or `DENY` |
| Overlapping branch, pull request, migration, or steward work owns the same surface | `HOLD` |
| The requested action would release, deploy, promote, or publish under this runbook | `DENY` |

[Back to top](#top)

---

<a id="acceptance-and-negative-cases"></a>

## Acceptance and negative cases

### Runbook acceptance

This procedure is accurate for the pinned snapshot when:

1. it identifies the live source-refresh capability as held;
2. it names the current source-authority, descriptor, connector, pipeline, workflow, test, validator, policy, and release evidence without upgrading maturity;
3. the focused commands match the Makefile and workflow;
4. relative links resolve;
5. the not-for-life-safety boundary is visible;
6. synthetic validation, source activation, lifecycle mutation, proof, review, release, deployment, promotion, and publication remain separate; and
7. the diff changes only this runbook unless a direct documentation dependency is proven.

### Negative cases

| Case | Expected posture |
|---|---|
| Dotted placeholder descriptor is presented as admitted | Reject the documentation change |
| Alternate TBD descriptor is silently treated as canonical | Reject |
| One of the competing connector README paths is declared canonical without an accepted decision | Reject |
| A live endpoint or command is copied from planning material rather than verified implementation | Reject |
| `make hazards-validate` is described as current-conditions validation | Reject |
| `MATERIAL / PROMOTION_CANDIDATE` is described as release readiness | Reject |
| Expired warning context is presented as current instruction | Reject |
| Watcher output writes or implies PUBLISHED state | Reject |
| The procedure creates a source-activation, policy, review, release, or publication effect | Reject |
| Missing support is converted to a plausible default | Reject |

[Back to top](#top)

---

<a id="maintenance-drift-and-verification-backlog"></a>

## Maintenance, drift, and verification backlog

Reconcile this runbook whenever any of these surfaces changes:

- `control_plane/source_authority_register.yaml`;
- Hazards source descriptor schemas or accepted registry topology;
- `data/registry/sources/hazards/` or `data/registry/hazards/sources/`;
- NOAA Storm Events connector placement or implementation;
- the Storm Events watcher or pipeline spec;
- Hazards fixture schemas, tests, validator, Make target, or domain workflow;
- policy bundle/evaluator binding;
- proof or release-candidate implementation;
- source-rights, sensitivity, or reviewer assignments;
- correction and rollback contracts; or
- the not-for-life-safety boundary.

### Open verification backlog

- Settle the canonical Hazards source registry and descriptor identity without creating parallel writable authority.
- Resolve the NOAA Storm Events underscore/hyphen connector topology through an accepted ADR or migration note.
- Replace proposal/TBD descriptor records with one reviewed descriptor only after rights, cadence, source role, access, citation, and activation are supported.
- Populate the source-authority register through its owning governed process; do not edit it merely to satisfy this runbook.
- Implement and test a connector, fixture-first parser, raw/quarantine receipt boundary, and transport controls before any live fetch.
- Bind an executable pipeline spec to accepted code and deterministic identity.
- Add source-refresh-specific negative tests that prove the connector cannot write beyond RAW/QUARANTINE or act as a publisher.
- Establish policy evaluator binding, EvidenceRef-to-EvidenceBundle closure, proof production, candidate assembly, and release review separately.
- Assign accountable source, Hazards, rights, sensitivity, security, operations, review, correction, and release stewards.
- Reconcile the inherited duplicate at [`docs/domains/hazards/SOURCE_REFRESH_RUNBOOK.md`](../../domains/hazards/SOURCE_REFRESH_RUNBOOK.md), which points readers back to this canonical runbook path, without deleting or moving it until consumer and migration evidence exists.
- Reconcile the generic [`docs/runbooks/SOURCE_REFRESH_RUNBOOK.md`](../SOURCE_REFRESH_RUNBOOK.md) relationship and the one-byte local [`docs/runbooks/hazards/README.md`](./README.md) in separate, dependency-aware documentation work.

### Source posture

The Drive Hazards blueprint remains planning lineage. It contributes the not-for-life-safety, source-role, time, evidence, quarantine, and offline-first design posture. Its no-mounted-repository assumptions, proposed paths, and illustrative commands do not override the live repository.

The Notion runbook-inventory checkpoint confirms that the runbook lane is broad but does not prove child procedure validation, rehearsal, review, source admission, release, deployment, promotion, or publication. This runbook therefore remains tied to repository bytes and owning authority surfaces.

[Back to top](#top)

---

## Related repository surfaces

| Surface | Role |
|---|---|
| [Hazards No-Network Test Runbook](./NO_NETWORK_TEST_RUNBOOK.md) | Exact bounded synthetic validation procedure and limitations |
| [Hazards Promotion Runbook](./PROMOTION_RUNBOOK.md) | Candidate preflight and accountable release-review handoff; current promotion remains held |
| [Hazards Rollback Runbook](./ROLLBACK_RUNBOOK.md) | Release-side correction and rollback procedure |
| [Hazards Rollback Drill](./ROLLBACK_DRILL.md) | Recovery rehearsal boundary |
| [Hazards domain README](../../domains/hazards/README.md) | Domain mission, object families, source-role and public boundary |
| [Life-Safety Boundary](../../domains/hazards/LIFE_SAFETY_BOUNDARY.md) | Non-negotiable not-for-life-safety doctrine |
| [Publication and Boundary](../../domains/hazards/PUBLICATION_AND_BOUNDARY.md) | Public-use and alert-authority constraints |
| [Hazards Source Registry](../../../data/registry/sources/hazards/README.md) | Source admission and authority-control orientation |
| [Source Authority Register](../../../control_plane/source_authority_register.yaml) | Current projection-only source-authority index |
| [Storm Events connector boundary](../../../connectors/noaa_storm_events/README.md) | Current README-only, placement-conflicted source edge |
| [Storm Events watcher boundary](../../../tools/ingest/storm_events_watch/README.md) | Proposed review-signal tooling boundary |
| [Hazards domain workflow](../../../.github/workflows/domain-hazards.yml) | Bounded synthetic validation plus explicit proof/release holds |
| [Hazards policy boundary](../../../policy/domains/hazards/README.md) | Draft/default-only policy source and evaluator gap |
| [Hazards release candidates](../../../release/candidates/hazards/README.md) | Candidate boundary; no current candidate established |

---

## Runbook rollback

This is a Markdown-only, same-path modernization. Revert the documentation commit or restore prior blob `f2a5a8ddb57be9ff336ac9cb00de4b30a35a3d82` if the evidence snapshot, command mapping, or stated maturity is shown to be wrong. Reverting this file changes no source, connector, lifecycle object, policy, review, release, deployment, promotion, or publication state.

[Back to top](#top)
