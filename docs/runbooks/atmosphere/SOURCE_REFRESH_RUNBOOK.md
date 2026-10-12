<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-atmosphere-source-refresh
title: Atmosphere Source Refresh Runbook
type: standard
subtype: operational-runbook
version: v1.0.0
prior_version: v0.1
status: draft; repository-grounded; documentation-only; live-source-execution-hold; not-for-life-safety; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
  - "NEEDS VERIFICATION — accountable Atmosphere, source, connector, rights, sensitivity, Hazards-seam, evidence, release, correction, operations, and independent-review assignments"
created: 2026-05-13
updated: 2026-08-24
policy_label: repository-facing; restricted-by-default; no-network-first; not-for-life-safety; non-release
current_path: docs/runbooks/atmosphere/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
responsibility: "Describe the governed operator procedure for refreshing an already-admitted Atmosphere source without granting source authority, activating a connector, issuing an alert, exposing restricted material, promoting a release, or publishing data."
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS_VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational procedure
authority_rank: subordinate to accepted doctrine and ADRs, source authority, contracts, schemas, policy, evidence, review, lifecycle, release, correction, and rollback records
canonical_relationship: same-path update; no sibling authority created
path_posture: PLACE
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  content_commit: 1012d9f6b605656d3e994801581ff3ccbe212556
  branch_base_commit: 991f9f99634ceeb31228b22e593b1111f9b0510b
  target_prior_blob: e96d7118a91bf68704ed14f679ba7e6bebb68991
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  source_admission_adr_blob: b5c0ac83be6f00897ee626c46df2bf64f15d82f5
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  atmosphere_source_registry_readme_blob: 6a50dd496225cd9e4c3165dead10cde3d0f23959
  atmosphere_source_placeholder_blob: 2899950fd4b9f4fa53df37b39cf8780e1503a5da
  atmosphere_connector_readme_blob: 4acc061f85248d8c98d85195ac5548bd384aed9d
  atmosphere_ingest_spec_blob: 4b0c610557a4c0b2d11a5376608565d138c78023
  atmosphere_ingest_placeholder_blob: ff71241bb9c783bbf22fc067b5b00602110b88f5
  source_descriptor_validator_blob: a0420731a1b80ce6d156f8e4cfd928a6b13699f4
  source_activation_validator_blob: 6e2bfceae3b58872d3f905f4d24003b80b7de422
  ingest_receipt_validator_blob: 6596685b04b7889355bf66ae6b25f1f83bacccaf
  atmosphere_workflow_blob: fccba4b6e2cdae561ec8a4904446ed5dbe6ec8ce
  atmosphere_validation_runbook_blob: ba3257f79cb4245d1c6de7e1271768910b42d9c8
inspection_boundary: >-
  Current-session GitHub reads of this target, accepted Directory Rules evidence,
  proposed source-admission ADR, source contracts, schemas, fixtures, validators,
  source authority register, Atmosphere source registry, connector lanes, pipeline
  specifications and placeholders, lifecycle roots, release-candidate boundary,
  Atmosphere workflows, tests, policy, and sibling runbooks. Repository-native
  commands were not executed in a mounted checkout during authoring. No live source
  was contacted and no credential, lifecycle, release, deployment, or publication
  state was changed.
related:
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../adr/ADR-0017-source-descriptor-admission-process.md
  - ../../domains/atmosphere/README.md
  - ../../domains/atmosphere/DATA_LIFECYCLE.md
  - ../../domains/atmosphere/OBSERVED_MODELED_SEPARATION.md
  - ../../domains/atmosphere/POLICY.md
  - ../../domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/atmosphere/README.md
  - ../../../connectors/atmosphere/README.md
  - ../../../connectors/airnow/README.md
  - ../../../pipeline_specs/atmosphere/README.md
  - ../../../pipelines/domains/atmosphere/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../fixtures/domains/atmosphere/README.md
  - ../../../tests/domains/atmosphere/README.md
  - ../../../tools/validators/domains/atmosphere/README.md
  - ../../../release/candidates/atmosphere/README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./VALIDATION_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./CORRECTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
tags: [kfm, runbook, atmosphere, air, source-refresh, source-admission, source-role, no-network, evidence, policy, correction, rollback, life-safety-denial]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Source Refresh Runbook

> **Repository-grounded procedure for refreshing an already-admitted Atmosphere source through bounded acquisition, immutable capture, normalization, validation, evidence closure, and review handoff—without treating source access, green CI, a receipt, a map, or generated language as truth or publication authority.**

> [!IMPORTANT]
> **A source refresh is not source admission, truth certification, lifecycle promotion, release, deployment, or publication.** This procedure can produce a reviewable candidate only after the owning source, evidence, policy, and lifecycle controls resolve. It stops before promotion authority acts.

> [!WARNING]
> **KFM is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority.** Do not use this runbook to issue health guidance, declare safe or unsafe conditions, replace an agency alert, infer exposure, or certify a measurement. Official observations, forecasts, and advisories retain their source roles and issuer authority.

> [!CAUTION]
> **Live Atmosphere source execution is `HOLD` at the pinned repository state.** The source-authority projection is empty; the tracked Atmosphere source records are placeholders; connector lanes are README-only; the ingest specification has no stages; and the ingest implementation is a placeholder. The executable posture currently supported by evidence is bounded and no-network.

**Navigation:** [Purpose](#1-purpose-scope-and-non-goals) · [Evidence](#2-placement-authority-and-current-state) · [Outcomes](#3-truth-labels-and-finite-outcomes) · [Preflight](#4-roles-inputs-and-authority-freeze) · [Sources](#5-source-family-routing-inventory) · [Meaning](#6-atmosphere-meaning-time-and-cross-domain-guardrails) · [Lifecycle](#7-refresh-lifecycle-and-trust-boundary) · [Procedure](#8-governed-refresh-procedure) · [Validation](#9-current-no-network-validation) · [Graduation](#10-live-profile-graduation-sequence) · [Operations](#11-staleness-retries-security-and-safe-diagnostics) · [Correction](#12-correction-withdrawal-and-rollback) · [Handoff](#13-review-handoff-and-open-verification) · [References](#14-related-current-surfaces) · [Anti-patterns](#appendix-a-anti-patterns)

---

## 1. Purpose, scope, and non-goals

Use this runbook only to check or retrieve a new version of an **already-admitted** Atmosphere source. The operator must:

1. freeze the exact source, descriptor, decision, connector, prior state, and intended effects;
2. prove the affected boundary with no-network fixtures before any permitted live contact;
3. preserve source role, rights, sensitivity, access, time, units, spatial support, uncertainty, and caveats;
4. retrieve conditionally and with bounded effects;
5. capture immutable bytes or immutable source references into governed RAW or QUARANTINE;
6. normalize only in WORK and route unresolved records to QUARANTINE;
7. validate machine shape, Atmosphere meaning, integrity, policy, and evidence references;
8. prepare catalog/evidence candidates and a review handoff; then stop.

### In scope

- admitted observations, regulatory records, operational context, remote-sensing observations, model context, historical context, citation sources, and other explicitly classified Atmosphere products;
- source-head comparison, conditional retrieval, no-change, skip, rate-limit, error, quarantine, and denial outcomes;
- immutable capture, WORK normalization, source-specific validation, evidence/catalog candidate closure, and correction/rollback handoff.

### Out of scope

This runbook does not:

- admit, activate, credential, schedule, approve, release, deploy, or publish a source;
- define machine contracts or schemas in Markdown;
- certify calibration, regulatory equivalence, model skill, forecast accuracy, health impact, exposure, causality, or emergency significance;
- issue or repeat life-safety instructions as KFM authority;
- permit public clients, maps, dashboards, or AI to read RAW, WORK, QUARANTINE, candidate, or restricted stores;
- turn AQI into concentration, AOD into ground-level PM2.5, a model into an observation, a preliminary report into a certified record, or a low-cost sensor into regulatory evidence;
- treat a file move, pull request, merge, workflow, badge, receipt, or map layer as promotion.

Use the [Correction Runbook](./CORRECTION_RUNBOOK.md) and [Rollback Runbook](./ROLLBACK_RUNBOOK.md) when already released material is affected. Route emergency or life-safety communication to the official issuer and the Hazards boundary.

[Back to top](#top)

---

## 2. Placement, authority, and current state

### Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This is a same-path `PLACE` under the human-readable operational-procedure responsibility root:

```text
docs/runbooks/atmosphere/SOURCE_REFRESH_RUNBOOK.md
```

The update creates no parallel contract, schema, source registry, connector, policy, receipt, proof, release, or publication authority, and creates, moves, renames, or deletes no file.

### Responsibility boundary

| Responsibility | Owning surface | Runbook posture |
|---|---|---|
| Source admission and meaning | source doctrine, contracts, accepted decisions | Require resolution; never grant it |
| Machine shape | canonical schemas and validators | Invoke verified checks; never redefine fields |
| Source authority projection | `control_plane/` | Inspect status; an index is not authority by itself |
| Source records | `data/registry/sources/` | Resolve admitted records; never mint or upgrade them |
| Acquisition and transforms | `connectors/`, `pipeline_specs/`, `pipelines/` | Run only substantive, reviewed implementation |
| Lifecycle material | governed `data/` roots | Write only through the owning implementation and authorized transition |
| Policy, evidence, review | policy, evidence, proof, and review authorities | Require closure; keep object families distinct |
| Promotion and release | `release/` and authorized reviewers | Prepare a packet and stop |
| Public delivery | governed APIs and released public-safe carriers | Verify only after separate release authority |

### Confirmed repository evidence

The target remained at blob `e96d7118a91bf68704ed14f679ba7e6bebb68991` when re-read at branch base `main@991f9f99…`; intervening sibling-runbook merges did not modify it.

| Surface | Confirmed evidence | Safe conclusion |
|---|---|---|
| Existing target | v0.1 contains proposed commands, fixed cadences/thresholds, source claims, wire skeletons, and a direct promotion step | Replace it with bounded repository evidence |
| Source-admission ADR | ADR-0017 remains proposed | Operational source-admission authority is not established |
| Source authority register | `implementation_status: ABSENT`, `completeness: empty`, `entries: []`, projection-only | No Atmosphere authority resolves from it |
| Atmosphere source registry | README plus placeholder `aqs.source.json` and `knowledge_character.json` | Routing exists; complete admitted source records are not established |
| Shared validators | No-network validators exist for SourceDescriptor, SourceActivationDecision, and IngestReceipt | Candidate shape and local consistency only; no live refresh |
| Atmosphere/AirNow connectors | README plus `.gitkeep` | No executable connector verified |
| Ingest specification | `stages: []` | No executable sequence declared |
| Ingest implementation | one-line placeholder | No live implementation established |
| Atmosphere workflow | read-only, no-network, synthetic positive/negative profiles | Useful bounded proof; no source contact or release proof |
| Release candidates | README only | No Atmosphere release candidate established |

**Current result:** shared candidate validators and bounded Atmosphere fixture profiles are `CONFIRMED`; live refresh, source activation, credentials, external requests, lifecycle persistence, production policy, evidence/catalog closure, promotion, release, deployment, and publication remain `HOLD`. Accountable steward and independent-review assignments remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## 3. Truth labels and finite outcomes

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from pinned repository evidence, executable code, fixtures, workflows, or generated artifacts inspected in this session |
| `PROPOSED` | Future design or procedure not verified as accepted implementation |
| `UNKNOWN` | Evidence is insufficient |
| `NEEDS VERIFICATION` | A concrete check remains |
| `CONFLICTED` | Authority, naming, shape, or lifecycle evidence disagrees |
| `HOLD` | Do not advance; preserve the prior safe state |

Use these operator classifications without inventing machine enum values:

| Outcome | Meaning | Maximum effect |
|---|---|---|
| `READY_TO_FETCH` | All preconditions for the exact authorized request resolve | Permit that bounded request only |
| `ADMIT_TO_RAW` | Material may enter governed RAW under the resolved decision | RAW capture plus receipt |
| `QUARANTINE` | Material or operation requires controlled review | Governed QUARANTINE only |
| `DENY_INTAKE` | Source or operation is not permitted | No admitted lifecycle write |
| `HOLD` | Authority, rights, sensitivity, policy, evidence, review, or rollback is unresolved | No live operation or transition |
| `NO_CHANGE` | Accepted comparison proves unchanged content/version | Heartbeat or no-change record only |
| `SKIP` | Run intentionally not attempted under a documented rule | Safe reason and next eligibility only |
| `RATE_LIMITED` | Upstream/local policy requires backoff | Safe retry metadata only |
| `ERROR` | Attempt failed or integrity cannot close | No permissive fallback |

The current SourceActivationDecision contract owns `ADMIT_TO_RAW`, `QUARANTINE`, `DENY_INTAKE`, `HOLD`, and `ERROR`. Do not serialize other prose labels unless an accepted contract allows them.

[Back to top](#top)

---

## 4. Roles, inputs, and authority freeze

[CODEOWNERS](../../../.github/CODEOWNERS) routes GitHub review to `@bartytime4life`; that is not source, rights, policy, independent-review, release, or operational authority.

### Required role classes

- **Source steward:** identity, role, authority rank, terms, cadence, access, citation, source-head, and retirement posture.
- **Connector operator:** exact implementation, bounded request, secret hygiene, capture target, and safe diagnostics.
- **Atmosphere steward:** units, knowledge character, observation/model distinction, uncertainty, caveats, and domain ownership.
- **Rights/sensitivity reviewers:** permitted use, attribution, redistribution, credentials, precision, joins, restricted stations, infrastructure, and re-identification risk.
- **Hazards liaison:** official-issuer, advisory, warning, incident, and life-safety boundary.
- **Validation/evidence steward:** validator scope, integrity, evidence resolution, limitations, and replay.
- **Release/correction authority and independent reviewer:** separately governed review, release, correction, rollback, and duty separation where required.

### Minimum input packet

Before live work, resolve:

- exact repository commit and implementation identity;
- complete source descriptor reference, digest, registry state, and source role;
- operation-specific activation/re-admission decision, scope, obligations, and expiry;
- source authority and accountable steward;
- current terms, permitted use, attribution, redistribution, credentials, and rate limits;
- sensitivity floor, public precision, cross-domain join rules, and required transforms;
- exact connector/importer, configuration digest, timeouts, retries, size/content-type/redirect bounds;
- prior ETag, Last-Modified, immutable version, digest, or other accepted source-head basis;
- current no-network positive and negative proof;
- approved RAW/QUARANTINE and WORK targets;
- exact validation/policy/evidence profile;
- prior release, correction, withdrawal, and rollback references when public state could be affected;
- named next owner for every outcome.

### Authority freeze

Record all of the above before the first request or write. A change in descriptor, decision, endpoint, product, connector, scope, time window, terms, role, or policy requires a new or explicitly linked preflight.

Stop with `HOLD`, `DENY_INTAKE`, `QUARANTINE`, or `ERROR` when any applicable authority is absent, stale, placeholder-only, expired, conflicted, rights-unclear, role-ambiguous, sensitivity-unclear, implementation-incomplete, network-reaching during no-network proof, digest-mismatched, meaning-losing, or lacking a correction/rollback route.

[Back to top](#top)

---

## 5. Source-family routing inventory

The previous runbook named the following families. They are retained as **candidate lineage**, not proof of admission, rights, reachability, or connector support.

| Candidate family | Required source-role boundary | Current posture |
|---|---|---|
| EPA AQS / AirData | Product-specific regulatory record or observation; certification state explicit | AQS record is placeholder-only |
| EPA AirNow | Preliminary/operational context distinct from certified records and raw concentration | README-only connector |
| NOAA / NWS products | Observation, model/forecast, or official advisory classified per product | Source-specific descriptor and issuer routing required |
| Kansas Mesonet | In-situ observation with network, parameter, unit, time, attribution, and terms | Rights/access/cadence and connector unverified |
| PurpleAir or other low-cost networks | Low-cost/community observation with correction, drift, transferability, caveats, and reference relation | Synthetic caveat proof only; no live admission or accepted correction method |
| OpenAQ-like aggregators | Aggregator/discovery context; upstream authority and rights remain resolvable | Aggregation cannot upgrade authority |
| HRRR-Smoke, BlueSky, CAMS, or other models | Model/forecast context with run, valid time, method, uncertainty, and limits | Model cannot become observation |
| HMS or other analyst-derived products | Analyst/operational context appropriate to the product | Not direct measurement by default |
| GOES/ABI AOD, MAIAC, related aerosol products | Remote-sensing observation of represented quantity | No direct substitution for ground PM2.5 |
| VIIRS/MODIS FIRMS or related fire detections | Fire context only | Not smoke exposure, causality, or instruction |
| Climate normals/anomalies | Historical/statistical context with baseline, method, version, and release time | Descriptor-driven refresh only |
| KDHE or other official state communications | Official context with issuer identity, issue/expiry, and link-back | KFM does not originate instructions |
| Local, research, historical, or steward-controlled material | Explicit observation, archive, model, contextual, or restricted role | `HOLD` until identity, rights, sensitivity, provenance, review, and access resolve |

Fixed polling intervals and stale thresholds from v0.1 are removed as operating instructions. Binding cadence, retries, staleness, and source-health behavior must come from the admitted descriptor, source-native release semantics, terms, and accepted source profile.

[Back to top](#top)

---

## 6. Atmosphere meaning, time, and cross-domain guardrails

| Distinction | Required behavior | Fail-closed posture |
|---|---|---|
| AQI vs concentration | Preserve index, pollutant, averaging, method, category, and concentration as distinct meanings | Hold/quarantine collapsed candidates |
| AOD vs ground PM2.5 | Preserve AOD as its represented quantity; any bridge is a separately governed derived method | No direct relabeling |
| Model/forecast/reanalysis vs observation | Preserve model identity, initialization, valid time, method, uncertainty, and generated status | Model cannot fill observation authority |
| Preliminary vs certified/final | Preserve provisional, QC, certification, correction, and supersession state | No silent replacement |
| Low-cost vs reference/regulatory | Preserve sensor class, correction, reference relation, drift, transferability, and limits | Agreement does not mint regulatory authority |
| Smoke/fire/plume context vs exposure/cause | Preserve context and uncertainty | Abstain/deny or route to official health/Hazards authority |
| Advisory context vs instruction | Preserve official issuer, ID, issue/expiry, and link-back | Deny KFM-originated life-safety language |
| Grid/aggregate vs station/place | Preserve spatial support, scale, resolution, interpolation, aggregation, and uncertainty | No point-truth substitution |
| Atmosphere vs Hazards | Atmosphere owns bounded observations/context; official issuers and Hazards own warning/life-safety posture | Route and hold |
| Cross-domain joins | Each lane retains canonical observations and sensitivity | Derived joins remain downstream and reviewed |

Preserve observation time, source issue/publication time, model initialization, forecast valid time, retrieval time, effective/expiry time, certification/correction time, transaction time, and KFM release time as distinct fields where material.

Before a record leaves WORK, preserve source-native and normalized units with transform lineage; parameter identity; station/pixel/grid/polygon/vertical support; CRS/datum/resolution; detection limits and missing/censored values; quality/provisional flags; method and uncertainty; and any generalization or redaction receipt.

[Back to top](#top)

---

## 7. Refresh lifecycle and trust boundary

```text
ADMITTED SOURCE + VALID OPERATION DECISION
  -> bounded source-head check / conditional retrieval
  -> RAW capture or QUARANTINE
  -> WORK normalization
  -> validation + policy + evidence resolution
  -> PROCESSED candidate
  -> CATALOG / optional TRIPLET candidate
  -> promotion handoff
  -> STOP

Separate authority only:
  -> promotion decision
  -> release decision and manifest
  -> PUBLISHED public-safe carrier
  -> governed API / map / Evidence Drawer / bounded AI
  -> correction / withdrawal / rollback / recompile
```

Lifecycle rules:

- RAW preserves retrieved bytes or immutable source references and integrity evidence; it is not public truth.
- WORK is mutable transformation space and never a normal public path.
- QUARANTINE preserves unsafe, unclear, conflicted, malformed, or unauthorized material with safe reasons.
- PROCESSED requires validated shape and meaning; it is still not released.
- Catalogs, triplets, indexes, tiles, summaries, scenes, and AI text remain derived carriers.
- Promotion is a governed state transition, not a file move or merge.
- Public clients use governed APIs and released public-safe carriers only.
- EvidenceRef must resolve to EvidenceBundle before a consequential claim is authoritative; otherwise abstain or deny.

[Back to top](#top)

---

## 8. Governed refresh procedure

### Step 0 — Freeze authority and scope

Create a preflight record containing the repository revision, source and descriptor digests, decision identity, connector/config identity, prior source head, lifecycle targets, validators, policy/evidence references, prior release context, correction/rollback targets, and overlap check.

### Step 1 — Resolve source and operation decision

Validate the complete descriptor and exact operation decision. Confirm role, rights, sensitivity, access, timing, obligations, source-head convention, and digest lineage. A placeholder, README, or projection-only index cannot satisfy this step.

### Step 2 — Prove the boundary without network access

Run the shared source fixture validators and affected Atmosphere positive/negative profiles. Confirm denied network access, deterministic fixtures, exact expected polarity, bounded diagnostics, and no secret dependence. Any unexpected network call is a failure.

### Step 3 — Recheck source-native controls

Verify current official endpoint/product identity, terms, attribution, access limits, content types, redirect behavior, size limits, source schema/version, publication/correction behavior, sensitivity, and official-issuer boundary. Record the check without copying secrets or restricted payloads.

### Step 4 — Retrieve or import conditionally

Only after explicit authorization:

- use an accepted source-head mechanism where available;
- send the minimum request needed;
- enforce timeout, retry, redirect, media-type, decompression, and size bounds;
- do not follow unapproved hosts or accept silent schema/product substitution;
- do not log authorization headers, tokens, signed URLs, cookies, private endpoints, or raw restricted responses;
- stop on changed terms, identity, shape, or risk.

### Step 5 — Capture immutable RAW or QUARANTINE material

Write through the owning implementation only. Record source/descriptor/decision IDs, retrieval and represented times, request profile, status, headers allowed by policy, byte count, media type, digest, prior source head, storage reference, sensitivity floor, and failure classification. Verify persisted bytes or immutable reference before success. Never overwrite prior RAW.

### Step 6 — Normalize only in WORK

Preserve source role, identifiers, units, time kinds, spatial support, quality/provisional flags, uncertainty, method/version, rights, sensitivity, and provenance. Record every transform. Route ambiguity, mismatch, unsafe precision, malformed data, or unsupported semantics to QUARANTINE.

### Step 7 — Validate shape, meaning, integrity, and policy

Run, as applicable:

1. source descriptor, activation decision, and ingest receipt checks;
2. source-specific schema and semantic checks;
3. Atmosphere anti-collapse and observed/modeled separation checks;
4. cross-domain boundary and sensitivity checks;
5. digest, count, time, units, CRS, duplicate, and idempotency checks;
6. policy evaluation and EvidenceRef resolution.

A green machine check proves only its bounded assertion. Rights, scientific validity, independent review, release, deployment, and publication remain separate.

### Step 8 — Close evidence and catalog candidates

Create only contract-valid candidate objects. Evidence must identify supporting source material, scope, limits, transformations, and review state. Catalog/triplet projections must point back to governed evidence and must not become canonical truth.

### Step 9 — Prepare promotion handoff and stop

Provide exact input/output digests, source and decision references, validation and policy results, evidence/catalog closure, unresolved items, reviewer roles, correction/rollback targets, and public-safe read-back plan. Continue only under the [Promotion Runbook](./PROMOTION_RUNBOOK.md) and separate authority.

### Step 10 — Record every terminal outcome

Record success, no-change, skip, rate-limit, quarantine, denial, hold, and error with safe reason, exact scope, prior/new source head where applicable, artifact references, validator results, limitations, next owner, and retry/review timing. Do not silently drop failed or no-change runs.

[Back to top](#top)

---

## 9. Current no-network validation

### Shared source-candidate validators

```bash
python tools/validators/validate_source_descriptor.py --fixtures
python tools/validators/validate_source_activation_decision.py --fixtures
python tools/validators/validate_ingest_receipt.py --fixtures
```

These validate bounded fixture shape, routing, lineage, and local consistency only. They do not establish live source identity, terms, authority, activation, network behavior, credential safety, scientific validity, persistence, promotion, or publication.

### Atmosphere bounded profiles

The read-only domain workflow and repository-grounded [Validation Runbook](./VALIDATION_RUNBOOK.md) identify the current no-network checks:

```bash
python tests/domains/atmosphere/test_atmosphere_smoke.py --verbose
python tests/domains/atmosphere/test_knowledge_character_registry.py --verbose
python tests/domains/atmosphere/test_low_cost_sensor_caveat_required.py --verbose
python tests/domains/atmosphere/test_observed_modeled_separation.py --verbose
python tests/cross_domain/test_environmental_observation_boundaries.py --verbose

python -m pytest \
  tests/validators/domains/atmosphere/airnow_aqs_reconciliation/test_validate_reconciliation.py \
  tests/domains/atmosphere/test_prescribed_burn_quality_flag.py \
  tests/domains/atmosphere/test_pm25_trigger_candidate_assessment.py \
  -q --strict-config --strict-markers
```

Use the current Validation Runbook for exact polarity and proof limits. No accepted aggregate `make atmosphere-validate` target was verified at the pinned snapshot.

### Documentation-change checks

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/atmosphere/SOURCE_REFRESH_RUNBOOK.md

python -m unittest discover \
  --start-directory tests/validators/docs/link-check \
  --pattern 'test_*.py' \
  --verbose

make repository-topology
```

These commands are recorded for a real checkout. They were not run locally in this connector-only authoring session. Hosted CI is separate evidence and must be reported at the exact pull-request head.

[Back to top](#top)

---

## 10. Live-profile graduation sequence

A future live source must graduate through separate, reviewable stages:

1. complete source-specific descriptor under the accepted registry convention;
2. accepted operation decision bound to its exact digest and scope;
3. deterministic positive and negative source fixtures;
4. substantive no-network connector/importer with request, media, size, redirect, retry, secret, and failure controls;
5. immutable RAW/QUARANTINE writer with digest verification and idempotency;
6. source-specific parser/normalizer preserving role, time, units, support, uncertainty, rights, sensitivity, and caveats;
7. semantic, policy, evidence, correction, and rollback tests;
8. bounded count-only or metadata-only live checkpoint where terms permit;
9. externally deterministic payload/carrier proof where material;
10. repeatable replay and no-change/error/rate-limit proof;
11. human review and separation-of-duty checks;
12. separate promotion and release authorization;
13. public-safe governed read-back, correction, withdrawal, and rollback drill.

No stage may infer the next. A successful metadata probe does not admit geometry or payloads; an admitted source does not authorize a release; a merge does not publish.

[Back to top](#top)

---

## 11. Staleness, retries, security, and safe diagnostics

### No change and staleness

A `NO_CHANGE` record must state the comparison basis, prior/new source head, retrieval time, and limitations. A missed refresh does not automatically make prior data false; a recent retrieval does not prove represented conditions are current. Apply the admitted product's time semantics and the owning stale-state procedure.

### Retry and rate limits

- retry only transient failures classified by the accepted profile;
- use bounded attempts, exponential backoff, jitter, and upstream `Retry-After` where applicable;
- never retry rights denial, authentication misconfiguration, schema drift, digest mismatch, unsafe redirect, policy denial, or semantic mismatch as if transient;
- do not rotate credentials, hosts, or IPs to evade terms or rate limits;
- record next eligibility without exposing restricted headers or account details.

### Fail-closed rights and sensitivity

| Unresolved condition | Posture |
|---|---|
| Terms, attribution, redistribution, retention, or credentials | `HOLD` or `DENY_INTAKE` |
| Station precision, infrastructure implication, private-person relation, or harmful join | QUARANTINE, transform, staged access, or denial |
| Official advisory or emergency meaning | Preserve issuer and route to official/Hazards surface |
| Source-role ambiguity or unsupported scientific bridge | QUARANTINE or abstain |
| Restricted endpoint, token, signed URL, cookie, or account identity | Never log or publish |

Safe diagnostics may include stable source ID, public product family, descriptor/decision digest, run ID, status class, count/byte total, duration bucket, safe reason code, and content digest where policy permits. Do not log secrets, authorization data, private endpoints, full restricted payloads, exact sensitive coordinates, unsafe joins, or free-form upstream bodies.

Dependency installs, new network permissions, secrets, schedules, workflow permissions, or repository settings are outside this documentation slice and require separate review. Network access must remain deny-by-default until a source-specific profile proves otherwise.

[Back to top](#top)

---

## 12. Correction, withdrawal, and rollback

### Before promotion

Defective candidates remain in WORK or QUARANTINE. Preserve prior RAW, record the failed transform or validation, and create a new candidate or transparent forward fix. Do not silently rewrite evidence or history.

### Released material

Use the [Correction Runbook](./CORRECTION_RUNBOOK.md) and, when needed, the [Rollback Runbook](./ROLLBACK_RUNBOOK.md). Identify affected evidence, catalog/triplet projections, governed API responses, tiles, caches, exports, summaries, Focus Mode outputs, and downstream consumers. Preserve correction notice, supersession, withdrawal, cache invalidation, rollback target, review, and public read-back evidence.

A source refresh cannot itself revoke or republish a released artifact. Source retirement or suspension also requires explicit authority, effective time, reasons, successor posture, affected releases, and correction/rollback handling. Endpoint reachability neither proves authority nor reverses retirement.

[Back to top](#top)

---

## 13. Review handoff and open verification

### Handoff checklist

- [ ] Same-path placement and exact repository/head are recorded.
- [ ] Descriptor, operation decision, source role, rights, sensitivity, access, cadence, citation, and source head resolve.
- [ ] Connector and pipeline are substantive rather than placeholder-only.
- [ ] No-network positive/negative proof and exact command results are attached.
- [ ] Network, secret, redirect, timeout, retry, media, size, decompression, and log controls are explicit.
- [ ] RAW/QUARANTINE integrity, idempotency, and failure cleanup are demonstrated.
- [ ] Units, time kinds, spatial support, uncertainty, quality, and source-role distinctions survive normalization.
- [ ] AQI/concentration, AOD/PM2.5, model/observation, preliminary/certified, low-cost/regulatory, context/exposure, and advisory/instruction distinctions remain intact.
- [ ] Policy, EvidenceRef/EvidenceBundle, catalog, correction, and rollback state are visible.
- [ ] CI, human review, promotion, release, deployment, and publication are reported as separate states.
- [ ] A named owner and next action exist for every unresolved item.

### Current `HOLD` / verification backlog

1. accepted operational source-admission authority and complete source-authority projection;
2. complete Atmosphere SourceDescriptors and operation decisions;
3. executable, dependency-closed Atmosphere/AirNow connectors and non-empty ingest stages;
4. immutable lifecycle persistence and replay proof;
5. source-specific rights, access, cadence, schema, source-head, and attribution verification;
6. semantic profiles for each admitted source/product;
7. production policy evaluation and EvidenceBundle/catalog closure;
8. accountable Atmosphere, Hazards, source, rights, sensitivity, evidence, operations, release, correction, and independent reviewers;
9. source-health, stale-state, correction, withdrawal, rollback, and public read-back drill;
10. release, deployment, and publication authorization.

Until these resolve, live refresh remains `HOLD`; the bounded no-network profiles are the supported proof surface.

[Back to top](#top)

---

## 14. Related current surfaces

### Governance and domain doctrine

- [Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029 — Adopt Directory Governance Standard v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [ADR-0017 — Source Descriptor Admission Process](../../adr/ADR-0017-source-descriptor-admission-process.md)
- [Source Descriptor Standard](../../sources/SOURCE_DESCRIPTOR_STANDARD.md)
- [Atmosphere domain README](../../domains/atmosphere/README.md)
- [Atmosphere data lifecycle](../../domains/atmosphere/DATA_LIFECYCLE.md)
- [Observed-modeled separation](../../domains/atmosphere/OBSERVED_MODELED_SEPARATION.md)
- [Atmosphere policy doctrine](../../domains/atmosphere/POLICY.md)
- [Atmosphere publication posture](../../domains/atmosphere/PUBLICATION_POSTURE.md)

### Source, implementation, validation, and release

- [Source authority register](../../../control_plane/source_authority_register.yaml)
- [Atmosphere source registry README](../../../data/registry/sources/atmosphere/README.md)
- [Atmosphere connector README](../../../connectors/atmosphere/README.md)
- [AirNow connector README](../../../connectors/airnow/README.md)
- [Atmosphere pipeline specification README](../../../pipeline_specs/atmosphere/README.md)
- [Atmosphere pipeline implementation README](../../../pipelines/domains/atmosphere/README.md)
- [Atmosphere policy implementation README](../../../policy/domains/atmosphere/README.md)
- [Atmosphere fixtures README](../../../fixtures/domains/atmosphere/README.md)
- [Atmosphere tests README](../../../tests/domains/atmosphere/README.md)
- [Atmosphere validator README](../../../tools/validators/domains/atmosphere/README.md)
- [Atmosphere release-candidate README](../../../release/candidates/atmosphere/README.md)
- [Atmosphere domain workflow](../../../.github/workflows/domain-atmosphere.yml)
- [Runbooks index](../README.md)
- [No-Network Test Runbook](./NO_NETWORK_TEST_RUNBOOK.md)
- [Validation Runbook](./VALIDATION_RUNBOOK.md)
- [Promotion Runbook](./PROMOTION_RUNBOOK.md)
- [Correction Runbook](./CORRECTION_RUNBOOK.md)
- [Rollback Runbook](./ROLLBACK_RUNBOOK.md)

[Back to top](#top)

---

<a id="appendix-a-anti-patterns"></a>

## Appendix A — Anti-patterns

Do not:

- treat repository presence, a README, placeholder JSON, empty stage list, or comment-only module as source admission or executable capability;
- use illustrative commands, fixed cadences, thresholds, endpoint assumptions, or wire shapes from v0.1 as current implementation;
- let a watcher, connector, receipt, successful request, green workflow, map, dashboard, search index, graph projection, or generated explanation publish;
- fetch first and decide rights, role, sensitivity, or storage later;
- place secrets or restricted responses in commands, fixtures, issues, PRs, logs, receipts, catalogs, or evidence bundles;
- overwrite RAW, silently rewrite history, or discard failed/no-change runs;
- collapse AQI and concentration, AOD and PM2.5, model and observation, preliminary and certified, low-cost and regulatory, context and exposure, or advisory context and official instruction;
- infer exposure, causality, health impact, emergency status, or safe/unsafe conditions from proximity, correlation, model output, or map appearance;
- hide sensitive records with client-side styling rather than applying governed transforms before delivery;
- treat promotion as a file move, merge, release badge, or deployment;
- let AI decide source authority, rights, sensitivity, policy, review, release, correction, or life-safety meaning;
- continue when authority, evidence, or rollback is unresolved—use `HOLD`.

[Back to top](#top)
