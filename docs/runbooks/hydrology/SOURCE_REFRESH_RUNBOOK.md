<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-hydrology-source-refresh-v1
title: Hydrology — Source Refresh Runbook
type: runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; LIVE_SOURCE_REFRESH_HELD; CAPTURED_INPUT_AND_FIXTURE_VALIDATION_AVAILABLE; NON_RELEASE; NON_PUBLICATION; NOT_FOR_LIFE_SAFETY
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Hydrology, source, rights, sensitivity, evidence, policy, release, and operations assignments"
created: 2026-05-12
updated: 2026-08-27
policy_label: repository-facing; source-admission-sensitive; fail-closed
current_path: docs/runbooks/hydrology/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
responsibility: Human preflight, bounded offline validation, and review-handoff procedure for Hydrology source-refresh work without performing live retrieval, source activation, lifecycle writes, promotion, release, or publication.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source descriptors, activation decisions, rights and sensitivity policy, evidence, review, lifecycle, release, correction, rollback, and official authorities
current_disposition: LIVE_SOURCE_REFRESH_HOLD / BOUNDED_CAPTURED_INPUT_AND_FIXTURE_VALIDATION_AVAILABLE
reason_codes:
  - HYD_REFRESH_SOURCE_AUTHORITY_REGISTER_EMPTY
  - HYD_REFRESH_SOURCE_DESCRIPTORS_PLACEHOLDER
  - HYD_REFRESH_REGISTRY_TOPOLOGY_UNRESOLVED
  - HYD_REFRESH_LIVE_TRANSPORT_ABSENT
  - HYD_REFRESH_INGEST_PIPELINE_DOCS_ONLY
  - HYD_REFRESH_PIPELINE_SPEC_ABSENT_OR_PLACEHOLDER
  - HYD_REFRESH_RIGHTS_AND_ACTIVATION_UNRESOLVED
  - HYD_REFRESH_LIFECYCLE_WRITE_UNBOUND
  - HYD_REFRESH_EVIDENCE_POLICY_REVIEW_RELEASE_UNBOUND
  - HYD_REFRESH_PUBLICATION_HELD
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 314e851b2831d16a75ec5e8a35fed257ca12c82c
  target_prior_blob: 3405a9f66813525c85b574cbb7cea9aef26ac8dd
  lane_readme_prior_blob: 67ac2ebd8208b2720c5765336aa9ac8af32fc11e
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  hydrology_source_registry_readme_blob: dc9b445b6a5c71e5a079d6db50b8838a2eda0d8c
  usgs_nwis_descriptor_blob: 456f64974526ae55107f507878f85cf73292dd51
  nwis_capture_helper_blob: 21255cd17ebaf163e06583603f3717a8abb3a344
  nwis_capture_contract_blob: 8cd9ec2ed4d62d83109fe280d997ae21515ac41d
  nwis_capture_tests_blob: d53a5ffde295eb822f6f80b72b88e1f21cc33a5f
  nwis_capture_workflow_blob: 3d324c7732b372e45bf6dd32ca67366b3550037d
  usgs_cutover_contract_blob: 4ee942e32a0fdaaeee8d816d6da6b4a9dae2a95b
  usgs_cutover_workflow_blob: 33d2091cf2f9d954adbff5e785361bcc196f0c93
  wbd_material_change_contract_blob: 17dab94f35e519f11e850156a296821ff8178a47
  wbd_material_change_workflow_blob: e3edd2c98b708c170df84cef10d883d2c42b2b61
  usgs_ingest_pipeline_readme_blob: 7f97df612cb22038075eff3e6daf356ff0166ea4
source_lineage:
  - "KFM_Hydrology_Extended_Pro_PDF_Only_Reference_Report_2026-04-21.pdf — Google Drive planning lineage; no longer implementation authority"
  - "KFM Evidence, Documentation & Ideas Atlas — 2026-08-24 — Notion coordination evidence; current repository remains implementation authority"
  - "KFM Markdown Update & Modernization Agent v1.0 — attached editing and delivery guidance"
related:
  - docs/runbooks/hydrology/README.md
  - docs/runbooks/hydrology/VALIDATION.md
  - docs/runbooks/hydrology/PROMOTION_RUNBOOK.md
  - docs/runbooks/hydrology/ROLLBACK_RUNBOOK.md
  - docs/domains/hydrology/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - control_plane/source_authority_register.yaml
  - data/registry/sources/hydrology/README.md
  - connectors/usgs/water_data/README.md
  - connectors/usgs/water_data/nwis_county_capture.py
  - contracts/domains/hydrology/nwis_county_capture.md
  - contracts/domains/hydrology/usgs_water_api_cutover.md
  - contracts/domains/hydrology/wbd_huc12_material_change_assessment.md
  - pipelines/domains/hydrology/ingest_usgs_water/README.md
  - .github/workflows/hydrology-nwis-county-capture.yml
  - .github/workflows/hydrology-usgs-water-api-cutover.yml
  - .github/workflows/hydrology-wbd-huc12-material-change.yml
non_effects:
  - does_not_contact_live_sources
  - does_not_read_credentials
  - does_not_activate_source_descriptors
  - does_not_admit_source_bytes
  - does_not_write_raw_work_quarantine_processed_catalog_triplet_or_published_state
  - does_not_resolve_evidence
  - does_not_approve_policy_or_review
  - does_not_promote_release_deploy_or_publish
  - does_not_issue_life_safety_guidance
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology — Source Refresh Runbook

Repository-grounded procedure for deciding whether Hydrology refresh work may
proceed, running the exact bounded offline checks that exist today, and producing
a truthful handoff when live retrieval or a later lifecycle transition remains
held.

![status: repository grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-blue)
![live refresh: hold](https://img.shields.io/badge/live%20refresh-HOLD-red)
![bounded mode: available](https://img.shields.io/badge/captured--input%20%2B%20fixtures-available-green)
![network: denied](https://img.shields.io/badge/network-denied-orange)
![release: none](https://img.shields.io/badge/release-none-lightgrey)
![life safety: no](https://img.shields.io/badge/life%20safety-not%20an%20authority-red)

> [!WARNING]
> KFM is not a flood-warning, emergency-response, navigation, engineering,
> insurance, dam-operation, water-rights, legal, or regulatory authority. Use
> the responsible official source for current conditions and life-safety
> decisions. FEMA NFHL is regulatory flood-hazard context, not observed
> inundation. A gauge value, model result, map, fixture, or passing test is not
> an official warning.

> [!IMPORTANT]
> **Current disposition:** `LIVE_SOURCE_REFRESH_HOLD`. The repository contains
> one deterministic captured-input-only USGS Water Data county normalizer and
> two fixture-only assessments for USGS API cutover and WBD HUC12 material
> change. It does **not** establish live transport, source activation, rights
> acceptance, RAW or QUARANTINE writes, an executable USGS ingest pipeline,
> evidence closure, promotion, release, deployment, publication, or public-use
> authority.

**Quick navigation:** [Current evidence](#1-current-repository-evidence) ·
[Authority boundary](#2-authority-and-terminal-boundary) ·
[Truth classes](#3-hydrology-source-role-and-truth-class-rules) ·
[Readiness](#4-refresh-readiness-and-current-holds) ·
[Preflight](#5-authority-freeze-and-preflight) ·
[Bounded procedures](#6-current-bounded-procedures) ·
[Result handling](#7-result-classification-and-handoff) ·
[Failure matrix](#8-failure-and-stop-condition-matrix) ·
[Graduation](#9-live-refresh-graduation-gates) ·
[Validation](#10-documentation-and-change-validation) ·
[Maintenance](#11-maintenance-correction-and-rollback) ·
[Related surfaces](#12-related-repository-surfaces)

## 1. Current repository evidence

This section describes what is verified at the pinned repository revision. A
later revision may change the result; re-run the authority freeze before use.

| Surface | Verified current state | Operational consequence |
|---|---|---|
| [`control_plane/source_authority_register.yaml`](../../../control_plane/source_authority_register.yaml) | `PROPOSED`, `projection_only`, `implementation_status: ABSENT`, `completeness: empty`, and `entries: []` | No machine authority entry activates or admits a Hydrology source. Live refresh remains held. |
| [Hydrology source registry](../../../data/registry/sources/hydrology/README.md) | Draft admission-control orientation with `OWNER_TBD`; it records unresolved subtype-first versus domain-first topology | Treat registry prose as boundary guidance, not activation evidence. Do not create divergent descriptor copies. |
| [`usgs_nwis.yaml`](../../../data/registry/sources/hydrology/usgs_nwis.yaml) and peer Hydrology source files | `status: PROPOSED` placeholders created from documentation inventory | A placeholder is not a `SourceDescriptor`, rights decision, endpoint approval, or source activation. |
| [USGS Water Data connector lane](../../../connectors/usgs/water_data/README.md) | Draft connector boundary with one executable captured-input-only helper | Request planning and local normalization are available; transport and lifecycle writes are not. |
| [`nwis_county_capture.py`](../../../connectors/usgs/water_data/nwis_county_capture.py) | Builds credential-free modern API request plans and normalizes caller-supplied captured OGC API FeatureCollections; it performs no transport and emits JSON to stdout | May be used only for bounded offline validation of supplied bytes. Success is not proof that USGS was contacted or that data are current or authentic. |
| [NWIS county capture contract](../../../contracts/domains/hydrology/nwis_county_capture.md), [schema](../../../schemas/contracts/v1/domains/hydrology/nwis_county_capture_manifest.schema.json), [fixture](../../../fixtures/connectors/usgs/water_data/nwis_county_capture/valid_capture.json), [tests](../../../tests/connectors/usgs/water_data/test_nwis_county_capture.py), and [workflow](../../../.github/workflows/hydrology-nwis-county-capture.yml) | Deterministic captured-input shape, pagination, role/state preservation, digest, and no-network checks exist | Establishes a bounded profile only. It does not activate a source, write RAW, resolve evidence, or authorize public use. |
| [USGS Water API cutover contract](../../../contracts/domains/hydrology/usgs_water_api_cutover.md) and [workflow](../../../.github/workflows/hydrology-usgs-water-api-cutover.yml) | Fixture-only migration assessment with finite outcomes | `CUTOVER_CANDIDATE` is a fixture disposition, not production cutover or source activation. |
| [WBD HUC12 material-change contract](../../../contracts/domains/hydrology/wbd_huc12_material_change_assessment.md) and [workflow](../../../.github/workflows/hydrology-wbd-huc12-material-change.yml) | Fixture-only geometry/area fingerprinting and materiality assessment | `NO_CHANGE`, `MATERIAL_CHANGE`, `ADD`, and `REMOVE` classify supplied fixtures only; they are not live WBD results. |
| [USGS Water ingest pipeline lane](../../../pipelines/domains/hydrology/ingest_usgs_water/README.md) | Directory contains a README and `.gitkeep`; executable pipeline behavior remains proposed | No current pipeline consumes the captured manifest into governed lifecycle state. |
| Hydrology pipeline specifications | The expected `pipeline_specs/hydrology/ingest_usgs_water.yaml` is absent; WBD ingest specifications named by the domain workflow remain placeholders | Do not invent a refresh command, schedule, writer, or pipeline invocation. |
| Hydrology domain workflow | Executes bounded synthetic and fixture-polarity checks while explicitly denying live requests, admission, evidence/proof, release, and publication authority | A green workflow is limited to the named tests at the tested SHA. |

### 1.1 Current disposition and reason codes

The current live-refresh decision is `HOLD` for all source families.

| Reason code | Meaning | Clearing evidence required |
|---|---|---|
| `HYD_REFRESH_SOURCE_AUTHORITY_REGISTER_EMPTY` | The authority projection contains no entries | Reviewed owning source object plus reconciled projection; projection alone still does not activate the source |
| `HYD_REFRESH_SOURCE_DESCRIPTORS_PLACEHOLDER` | Hydrology YAML files are inventory placeholders | Schema-valid, reviewed descriptor with source role, rights, terms, endpoint, cadence, sensitivity, and steward state |
| `HYD_REFRESH_REGISTRY_TOPOLOGY_UNRESOLVED` | Multiple registry homes are documented | Accepted path decision or migration note with one writable authority and compatible pointers |
| `HYD_REFRESH_LIVE_TRANSPORT_ABSENT` | No verified connector performs live retrieval | Reviewed transport adapter, tests, no-network boundary, credential/rate-limit handling, and exact endpoint profile |
| `HYD_REFRESH_INGEST_PIPELINE_DOCS_ONLY` | USGS Water ingest lane has documentation but no executable implementation | Executable normalizer/handoff with contract, fixtures, tests, receipts, and lifecycle boundary |
| `HYD_REFRESH_PIPELINE_SPEC_ABSENT_OR_PLACEHOLDER` | Required declarative run specification is missing or still a placeholder | Accepted, validated pipeline specification bound to executable behavior |
| `HYD_REFRESH_RIGHTS_AND_ACTIVATION_UNRESOLVED` | Rights and source activation are not closed | Applicable rights/sensitivity decisions and a governed activation record |
| `HYD_REFRESH_LIFECYCLE_WRITE_UNBOUND` | No verified writer moves source material into RAW or QUARANTINE | Idempotent writer, destination contract, collision policy, receipt, negative tests, and rollback |
| `HYD_REFRESH_EVIDENCE_POLICY_REVIEW_RELEASE_UNBOUND` | Downstream trust objects and accountable review are not closed | EvidenceBundle resolution, policy decision, review record, proof/catalog closure, promotion decision, and release manifest |
| `HYD_REFRESH_PUBLICATION_HELD` | No public release is authorized | Separate governed release, correction, rollback, readback, and publication evidence |

[Back to top](#top)

## 2. Authority and terminal boundary

This runbook is an explanatory procedure under `docs/runbooks/`, consistent
with the accepted Directory Rules decision. It does not own semantic meaning,
machine shape, source activation, policy, lifecycle state, evidence, proof, or
release state.

| Concern | Owning surface | This runbook may do | This runbook must not do |
|---|---|---|---|
| Hydrology meaning | `contracts/domains/hydrology/` | Link and explain the active contract | Redefine contract fields or source roles |
| Machine shape | `schemas/` | Name the schema used by a bounded check | Treat Markdown examples as schema authority |
| Source admission | Governed source registry and activation objects | Verify whether the required objects exist and are resolved | Activate a source, infer approval from a placeholder, or select a convenient registry copy |
| Connector behavior | `connectors/` | Run exact offline helper/tests already implemented | Contact a live endpoint, add credentials, or claim transport occurred |
| Pipeline behavior | `pipelines/` and `pipeline_specs/` | Verify current implementation or absence | Invent a `kfm hydrology refresh` command or lifecycle writer |
| Lifecycle state | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` | Describe required handoff boundaries | Write or promote lifecycle artifacts from documentation |
| Evidence and proof | `data/proofs/`, evidence contracts, and resolvers | Require resolvable references before later claims | Treat a test, digest, receipt, map, or summary as an EvidenceBundle |
| Policy and review | `policy/` and accountable review records | Require the applicable decision and reviewer | Approve rights, sensitivity, public precision, or release |
| Release/correction/rollback | `release/` and governed runbooks | Produce a review handoff and stop | Promote, release, deploy, publish, withdraw, or republish |

### 2.1 Permitted terminal states

A run under this document may end only as one of the following:

- `PASS` — an exact bounded offline check passed at the recorded revision.
- `FAIL` — the bounded check ran and rejected the supplied input or expectation.
- `HOLD` — a prerequisite or later transition is incomplete.
- `ABSTAIN` — evidence is insufficient to make the requested hydrologic or
  operational claim.
- `DENY` — rights, sensitivity, source role, policy, or an authority boundary
  prohibits the requested action.
- `ERROR` — the procedure or environment could not produce a valid result.
- `ESCALATE` — accountable source, Hydrology, rights, sensitivity, evidence,
  policy, release, or official-authority review is required.

Always pair the result with a **scope**. `PASS` without scope is misleading.
A fixture pass is not a live-refresh pass.

[Back to top](#top)

## 3. Hydrology source-role and truth-class rules

Source refresh must preserve the source's role and the claim it can support.
Provider identity, file name, visual appearance, cadence, or location does not
change that role.

| Material | Required treatment | Prohibited substitution |
|---|---|---|
| Monitoring-location metadata | Administrative source material | Observation or current condition |
| Instantaneous readings | Observed values with timestamp, parameter, unit, qualifier, and approval state | Daily aggregate, forecast, warning, or operational directive |
| Daily values and annual statistics | Aggregates with statistic and period | Point-in-time observation |
| Provisional values | Distinct provisional lifecycle state | Approved value |
| WBD HUC boundaries | Boundary/aggregation context at a named vintage | Streamflow observation or watershed condition |
| NHDPlus/3DHP network and derivatives | Network identity or modeled/derived context according to product | Direct observation without method and lineage |
| FEMA NFHL/MSC | Regulatory flood-hazard context | Observed inundation, forecast, or warning |
| Terrain/3DEP-derived hydrology | Observed elevation source or modeled derivative according to product | Hydrologic observation without algorithm and run support |
| Historical flood evidence | Observed or candidate evidence according to review state | Current warning or unrestricted exact-location release |
| Watcher or model output | Candidate, modeled, or synthetic support | Source activation, evidence authority, or release approval |

The Hydrology registry documents a canonical source-role vocabulary for new
source descriptors. The captured NWIS profile uses contract-specific values
such as `ADMINISTRATIVE` and `AGGREGATE_DAILY`. Preserve each owning
contract's values; do not silently translate between vocabularies or normalize a
role by assumption.

### 3.1 Time and identity rules

Keep material times distinct when the source provides them:

- observation time or source-valid date;
- source publication or last-modified time;
- retrieval/capture time;
- processing time;
- approval or correction time;
- release and supersession time.

Preserve native source identifiers, parameter codes, statistic IDs, units,
datum, qualifier, site identity, HUC level, geometry vintage, and endpoint
family. A derived KFM identity may link these values; it must not erase them.

[Back to top](#top)

## 4. Refresh readiness and current holds

Use the highest level supported by current evidence. Do not jump over a held
level because a later-level fixture happens to pass.

| Level | Capability | Current state | Permitted action |
|---|---|---|---|
| 0 | Repository reconnaissance | `AVAILABLE` | Pin revision, inspect source/contract/workflow paths, and classify gaps |
| 1 | Captured-input and fixture validation | `AVAILABLE` for the three profiles in §6 | Run exact no-network helper, validators, and tests; record bounded results |
| 2 | Live source preflight | `HOLD` | Assess missing descriptor, activation, rights, endpoint, credential, and writer evidence; do not connect |
| 3 | Authorized retrieval into RAW or QUARANTINE | `HOLD` | No current execution permitted |
| 4 | Executable normalization into WORK/PROCESSED plus receipt and evidence handoff | `HOLD` | No current execution permitted |
| 5 | Catalog/proof/policy/review closure and promotion decision | `HOLD` | Assemble requirements only; do not transition |
| 6 | Release, deployment, publication, correction, and rollback | `HOLD` | Separate governed operation required |

The captured-input helper's request plans are **plans**, not network actions.
The WBD material-change result is a comparison of supplied fixture snapshots,
not a source probe. The API cutover result is a migration-readiness fixture,
not a production configuration change.

[Back to top](#top)

## 5. Authority freeze and preflight

Before any bounded validation or live-refresh proposal, freeze the exact
question and evidence. A missing mandatory item ends in `HOLD`, `ABSTAIN`,
`DENY`, or `ERROR`; it is not filled with a plausible default.

### 5.1 Freeze the repository revision

Run from a clean checkout:

```bash
git rev-parse --show-toplevel
git rev-parse HEAD
git status --short
```

Record:

- repository and exact commit;
- current branch;
- target source family and product;
- exact contract, schema, fixture, test, validator, workflow, descriptor, and
  pipeline paths consulted;
- open pull requests or branches that overlap those paths;
- the intended terminal state for this run.

Stop if the checkout is dirty in a way that can affect the result, the target
path changed after inspection, or overlapping work owns the same surface.

### 5.2 Live-refresh mandatory preflight

Every item below is required before a live source request. Current repository
evidence does not close the checklist.

- [ ] One authoritative, schema-valid source descriptor exists; it is not a
  placeholder or divergent copy.
- [ ] Source role, authority scope, native identifiers, endpoint family, source
  vintage, cadence, rights, terms, citation requirements, access class,
  sensitivity, and public-use limits are explicit.
- [ ] A governed activation decision authorizes the exact source/product and
  operating mode.
- [ ] Accountable source, Hydrology, rights, sensitivity, and operations roles
  are assigned and reviewable.
- [ ] The transport adapter, supported query profile, pagination behavior,
  timeout, retry, rate-limit, credential, secret-redaction, and failure behavior
  are implemented and tested.
- [ ] No-network tests prove that offline validation cannot make a request.
- [ ] The approved RAW/QUARANTINE writer is idempotent, collision-safe, receipt
  emitting, and rollback-aware.
- [ ] The pipeline spec and executable pipeline agree on inputs, outputs,
  schemas, source role, time, identity, units, and quarantine reasons.
- [ ] Rights or sensitivity uncertainty fails closed before content enters a
  public-capable lane.
- [ ] RunReceipt, validation, evidence, policy, review, catalog, proof,
  correction, rollback, and release object paths are known and validated.
- [ ] A separate approval exists for any later promotion, release, deployment,
  or publication transition.

Until every applicable item is supported by current evidence, set:

```text
disposition: HOLD
reason_code: HYD_REFRESH_LIVE_PREREQUISITES_INCOMPLETE
network_attempted: false
lifecycle_written: false
```

The three-line record is a handoff statement, not a schema instance.

[Back to top](#top)

## 6. Current bounded procedures

The following procedures are the only source-refresh-adjacent executable
surfaces verified for this revision. They are no-network and do not write KFM
lifecycle state.

### 6.1 Procedure A — USGS Water Data county captured-input normalization

**Use when:** validating already captured, caller-supplied modern USGS Water
Data OGC API FeatureCollections against the bounded county/daily profile.

**Do not use when:** the task requires live retrieval, source authentication,
currentness, rights acceptance, RAW admission, general NWIS coverage, or a
public hydrologic claim.

Run the focused tests:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m pytest \
  tests/connectors/usgs/water_data/test_nwis_county_capture.py \
  -q --strict-config --strict-markers
```

Run the helper on the repository fixture:

```bash
python connectors/usgs/water_data/nwis_county_capture.py \
  --input fixtures/connectors/usgs/water_data/nwis_county_capture/valid_capture.json \
  > /tmp/kfm-nwis-county-capture-manifest.json
```

The helper:

- constructs credential-free request plans for the modern OGC API;
- validates Kansas county scope and safe pagination links;
- rejects API keys embedded in pagination URLs;
- preserves site, parameter, statistic, date, unit, qualifier, last-modified,
  time-series, approval/provisional state, and source-role distinctions;
- binds supplied page bytes through canonical SHA-256 digests;
- emits normalized JSON to stdout only;
- does not perform transport, read credentials, activate a source, write RAW,
  resolve evidence, promote, release, or publish.

A successful command supports only this statement:

> At the recorded repository revision, the supplied captured bytes conform to
> the bounded `NwisCountyCaptureManifest` profile and its deterministic local
> checks.

It does not support “USGS was contacted,” “the source is current,” “the data are
approved for KFM,” or “the observations are safe for public use.”

### 6.2 Procedure B — fixture-only USGS Water API cutover assessment

**Use when:** testing the deterministic migration profile that distinguishes
modern Water Data endpoints from legacy WaterServices/NWISWeb dependencies.

Run the validator and focused tests:

```bash
python tools/validators/domains/hydrology/usgs_water_api_cutover/validate_usgs_water_api_cutover.py \
  fixtures/domains/hydrology/usgs_water_api_cutover/valid/cutover_candidate.json

KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m pytest \
  tests/validators/domains/hydrology/usgs_water_api_cutover/test_validate_usgs_water_api_cutover.py \
  -q --strict-config --strict-markers
```

Finite fixture outcomes include:

- `CUTOVER_CANDIDATE` — the fixture satisfies the contract's deterministic
  candidate rules;
- `HOLD` — migration evidence is incomplete but potentially remediable;
- `DENY` — legacy-only, denied, or conflicting state violates the profile;
- validator `ERROR` — shape or decision is internally inconsistent.

`CUTOVER_CANDIDATE` does not activate a descriptor, change a production client,
prove endpoint availability, or authorize live transport.

### 6.3 Procedure C — fixture-only WBD HUC12 material-change assessment

**Use when:** validating the deterministic geometry-plus-area comparison profile
and its treatment of metadata-only churn.

Run the validator and focused tests:

```bash
python tools/validators/domains/hydrology/wbd_huc12_material_change/validate_wbd_huc12_material_change.py \
  fixtures/domains/hydrology/wbd_huc12_material_change/valid/metadata_churn_no_change.json

KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m pytest \
  tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py \
  -q --strict-config --strict-markers
```

Finite fixture outcomes are:

| Outcome | Contract meaning |
|---|---|
| `NO_CHANGE` | No geometry or rounded-area change in the supplied snapshots |
| `MATERIAL_CHANGE` | `geometry_change`, `area_change`, or both |
| `ADD` | Feature was added |
| `REMOVE` | Feature was removed |

The validator excludes source metadata such as load/edit dates from the feature
fingerprint while retaining it for traceability. `NO_CHANGE` therefore means
“no material geometry-plus-area change in this fixture,” not HTTP `304`, not a
live WBD no-op, and not proof that the upstream source has not changed.

### 6.4 Combined focused validation

Use this command to verify all three bounded profiles together:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m pytest \
  tests/connectors/usgs/water_data/test_nwis_county_capture.py \
  tests/validators/domains/hydrology/usgs_water_api_cutover/test_validate_usgs_water_api_cutover.py \
  tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py \
  -q --strict-config --strict-markers
```

Do not replace repository dependency installation rules with an ad-hoc package
set. In CI, the relevant workflows use:

```bash
python tools/ci/install_python_ci.py project-test
```

A local environment that cannot reproduce the repository's declared test
dependencies ends in `ERROR` or `HOLD`, not an improvised dependency change.

[Back to top](#top)

## 7. Result classification and handoff

### 7.1 Result interpretation

| Observed result | Classification | Required handoff |
|---|---|---|
| Exact focused command passes | `PASS` with `scope: bounded_offline_profile` | Record commit, command, input path/digest where available, output location, and non-effects |
| Expected-negative fixture is accepted or a positive fixture is rejected | `FAIL` | Preserve logs, stop, and open a bounded repair issue/PR; do not weaken the validator |
| Live source operation is requested | `HOLD` | List missing descriptor, activation, rights, transport, writer, pipeline, evidence, policy, review, release, and rollback prerequisites |
| Current hydrologic condition is requested from a fixture or stale capture | `ABSTAIN` | Direct the user to the appropriate current official source |
| Rights, sensitivity, sovereignty, or harmful precision prohibits use | `DENY` | Record the policy/source reason without exposing protected content |
| Environment or command cannot produce a valid result | `ERROR` | Record exact failure and what was not run |
| Specialist or authority judgment is required | `ESCALATE` | Name the required role, not an unverified person |

### 7.2 Handoff packet

The following is an **illustrative review handoff**, not a schema or lifecycle
object:

```yaml
hydrology_source_refresh_handoff:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_ref: <exact-commit>
  source_family: <usgs_water_data|wbd_huc12|nhdplus_hr|fema_nfhl|other>
  mode: <captured_input_only|fixture_cutover_assessment|fixture_material_change_assessment|live_refresh_proposed>
  disposition: <PASS|FAIL|HOLD|ABSTAIN|DENY|ERROR|ESCALATE>
  scope: <exact-bounded-claim>
  commands_run:
    - <exact-command>
  inputs:
    - path: <repository-or-local-path>
      digest: <digest-or-NEEDS_VERIFICATION>
  outputs:
    - path: <temporary-or-review-artifact-path>
      authority: <non_authoritative|review_only>
  reason_codes:
    - <finite-or-bounded-reason>
  evidence_consulted:
    - <contract/schema/test/workflow/source-object>
  missing_prerequisites:
    - <specific-gap>
  non_effects:
    network_attempted: false
    source_activated: false
    lifecycle_written: false
    evidence_resolved: false
    promotion_authorized: false
    release_authorized: false
    publication_authorized: false
  next_review_role: <role-or-NONE>
```

Do not put credentials, secret-bearing URLs, restricted payloads, temporary
access tokens, sensitive coordinates, or unreviewed source excerpts in the
handoff, issue, pull request, or logs.

### 7.3 No-change and stale-state handling

The repository does not currently prove conditional HTTP retrieval, heartbeat
receipt emission, or a live no-change writer. Therefore:

- do not document or execute `HEAD`, `If-None-Match`, `If-Modified-Since`, or
  unconditional-fetch behavior as current KFM implementation;
- do not equate WBD fixture `NO_CHANGE` with an upstream HTTP no-change;
- do not create a catalog version, release record, or public artifact from a
  local digest comparison;
- mark a capture stale or insufficient when its source-valid, retrieval,
  publication, correction, or approval time cannot support the requested use;
- use `ABSTAIN` for a current-condition claim that cannot be supported by
  current admissible evidence.

A future live connector should preserve ETag, Last-Modified, source manifest or
content digest, query identity, response status, retrieval time, and endpoint
family where available. That future behavior requires its own contract, tests,
receipt, and review; it is not activated by this paragraph.

[Back to top](#top)

## 8. Failure and stop-condition matrix

| Condition | Required result | Do not do |
|---|---|---|
| Source YAML is a placeholder | `HOLD` | Treat filename or `status: PROPOSED` as admission |
| Authority register remains empty/projection-only | `HOLD` | Infer authority from documentation or provider reputation |
| Multiple registry copies differ | `HOLD` / `ESCALATE` | Pick the convenient copy or synchronize by assumption |
| Live network is attempted during a bounded run | `FAIL` / `ERROR` | Retry with weaker no-network controls |
| API key or credential appears in input, URL, log, or output | `DENY` / security escalation | Commit, quote, or redact incompletely |
| Pagination is incomplete, unsafe, cross-host, or credential-bearing | `FAIL` | Normalize partial pages as complete |
| County, site, parameter, statistic, time window, unit, or identifier drifts | `FAIL` or `QUARANTINE` in a future governed pipeline | Coerce values to fit the request |
| Provisional and approved values collapse | `FAIL` | Prefer the value that appears more useful |
| Administrative metadata becomes an observation | `FAIL` | Promote site records as measurements |
| Daily aggregate becomes instantaneous observation | `FAIL` | Remove statistic/time-basis fields |
| NFHL becomes observed inundation or warning | `DENY` | Publish or summarize it as current flooding |
| WBD metadata churn becomes material geometry change | `FAIL` | Key materiality only to load/edit dates |
| Pipeline spec or executable pipeline is absent | `HOLD` | Invent a command, output path, schedule, or writer |
| Rights, terms, sensitivity, sovereignty, or precision is unresolved | `HOLD` / `DENY` | Move content into a public-capable lane |
| EvidenceRef cannot resolve to admissible EvidenceBundle support | `ABSTAIN` / `HOLD` | Treat receipt, checksum, test, map, or prose as proof |
| Accountable review or release authority is absent | `HOLD` | Interpret merge or green CI as approval |
| Current conditions or life safety are requested | `ABSTAIN` and redirect | Use KFM fixture/capture output as the authority |

Stop rather than improvise whenever exact source identity, role, rights,
endpoint, time, units, datum, approval state, sensitivity, provenance, evidence,
review, correction, rollback, or release state cannot be established.

[Back to top](#top)

## 9. Live refresh graduation gates

A future change may replace `LIVE_SOURCE_REFRESH_HOLD` only after all applicable
gates are supported by current repository and operational evidence.

### 9.1 Source and authority

- one authoritative descriptor path and schema-valid descriptor;
- explicit source role and claim limits;
- verified rights, terms, attribution, cadence, and access conditions;
- sensitivity, sovereignty, harmful-precision, and public-use posture;
- accountable steward and reviewer assignments;
- governed activation decision for the exact product and mode.

### 9.2 Transport and source edge

- reviewed live transport adapter with endpoint-family pinning;
- bounded query profile and complete pagination rules;
- timeout, retry, backoff, rate-limit, and no-op behavior;
- secret injection outside source-controlled content;
- response-size, media-type, redirect, host, TLS, and decompression controls;
- conditional-retrieval and source-manifest behavior where supported;
- no-network tests and negative fixtures that fail closed;
- retrieval and failure receipts without secret leakage.

### 9.3 Lifecycle and processing

- deterministic RAW/QUARANTINE destination and collision policy;
- source-byte or immutable-reference capture with digest;
- executable pipeline and validated pipeline specification;
- role-, identity-, time-, unit-, datum-, geometry-, and approval-aware
  normalization;
- explicit quarantine reason codes and review path;
- idempotency, replay, correction, and rollback tests;
- receipts that record what ran without masquerading as proof.

### 9.4 Evidence, policy, review, and release

- resolvable EvidenceRef-to-EvidenceBundle support for consequential claims;
- validation and proof closure appropriate to significance;
- policy decisions for rights, sensitivity, public precision, and source use;
- accountable human review, with separation of duties where required;
- catalog/triplet closure without making the projection sovereign truth;
- promotion decision, release manifest, rollback target, and correction path;
- public-safe artifact generation and governed API readback;
- monitoring, stale-state, withdrawal, cache invalidation, and rollback drill;
- separately authorized release, deployment, promotion, and publication.

A passing fixture suite may satisfy part of a gate. It cannot compensate for a
missing non-compensable gate.

[Back to top](#top)

## 10. Documentation and change validation

For an update to this runbook:

1. inspect the complete diff for stale commands, unsupported maturity claims,
   accidental authority expansion, and unrelated formatting churn;
2. verify every changed repository path and relative link;
3. check one H1, heading order, explicit anchors, code-fence balance, tables,
   alerts, and line endings;
4. confirm the exact commands still match the connector, validator, test, and
   workflow paths at the reviewed revision;
5. run the combined focused validation in §6.4 when the environment has the
   repository's declared test dependencies;
6. classify unavailable or inherited checks separately from failures introduced
   by the documentation change;
7. verify the branch, changed paths, pull-request base/head, and draft state;
8. keep merge, source admission, release, deployment, promotion, and
   publication as separate transitions.

The former unimplemented Hydrology refresh CLI pattern must not reappear
unless a future repository-grounded implementation, contract, tests, and review
establish it. The old runbook's conditional-GET, lifecycle-writer, heartbeat,
catalog-closure, and publication instructions were planning concepts, not
verified current commands.

### 10.1 Documentation acceptance criteria

- [ ] Current implementation claims cite or link to repository evidence.
- [ ] Live source refresh is explicitly held.
- [ ] All executable commands are bounded, no-network, and present in the repo.
- [ ] Source roles and provisional/approved state remain distinct.
- [ ] No fixture outcome is described as live source truth.
- [ ] No Markdown step writes lifecycle, evidence, policy, release, or public
  state.
- [ ] Rights, sensitivity, correction, rollback, and accountable review remain
  visible.
- [ ] The Hydrology lane README maturity map was reviewed; any necessary index
  correction remains a separate same-path change.

[Back to top](#top)

## 11. Maintenance, correction, and rollback

Update this runbook when any of the following changes materially:

- source descriptor or registry authority;
- source activation state;
- connector transport or endpoint family;
- credential, rate-limit, or conditional-retrieval behavior;
- pipeline specification or executable pipeline;
- contract, schema, validator, fixture, or test paths;
- lifecycle writer or receipt behavior;
- evidence, policy, review, release, correction, or rollback controls;
- official-source role, terms, cadence, or deprecation posture.

When behavior changes, update the owning implementation and its tests first or
in the same dependency-closed change. Documentation must describe the reviewed
behavior; it must not be used to manufacture implementation maturity.

### 11.1 Correction path

If a runbook claim is found false or stale:

1. stop using the affected instruction;
2. identify the exact repository revision and text at issue;
3. classify the impact on prior handoffs or reviews;
4. open the smallest forward correction or revert;
5. record any resulting Hydrology lane README drift for a separate bounded
   correction;
6. preserve the prior document in Git history rather than silently rewriting
   operational lineage.

### 11.2 Documentation rollback

If the change is abandoned before merge, close the draft pull request and
delete only its task-owned feature branch. After an authorized merge, revert the
documentation commit or submit a reviewed forward correction. Documentation
rollback does not undo source activation, data retrieval, lifecycle writes,
evidence, policy, release, deployment, or publication; those require their own
governed rollback paths.

[Back to top](#top)

## 12. Related repository surfaces

### Hydrology procedure and domain boundaries

- [Hydrology runbook index](./README.md)
- [Hydrology bounded validation](./VALIDATION.md)
- [Hydrology promotion preflight](./PROMOTION_RUNBOOK.md)
- [Hydrology rollback handoff](./ROLLBACK_RUNBOOK.md)
- [Hydrology domain boundary](../../domains/hydrology/README.md)

### Governance and source admission

- [Accepted Directory Rules decision](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Source authority projection](../../../control_plane/source_authority_register.yaml)
- [Hydrology source registry](../../../data/registry/sources/hydrology/README.md)
- [USGS Water Data connector lane](../../../connectors/usgs/water_data/README.md)

### Contracts, validators, tests, and workflows

- [NWIS county captured-input contract](../../../contracts/domains/hydrology/nwis_county_capture.md)
- [USGS Water API cutover contract](../../../contracts/domains/hydrology/usgs_water_api_cutover.md)
- [WBD HUC12 material-change contract](../../../contracts/domains/hydrology/wbd_huc12_material_change_assessment.md)
- [NWIS county capture workflow](../../../.github/workflows/hydrology-nwis-county-capture.yml)
- [USGS Water API cutover workflow](../../../.github/workflows/hydrology-usgs-water-api-cutover.yml)
- [WBD HUC12 material-change workflow](../../../.github/workflows/hydrology-wbd-huc12-material-change.yml)
- [Hydrology domain workflow](../../../.github/workflows/domain-hydrology.yml)

### Pipeline, proof, and release boundaries

- [USGS Water ingest pipeline lane](../../../pipelines/domains/hydrology/ingest_usgs_water/README.md)
- [Hydrology pipeline-spec boundary](../../../pipeline_specs/hydrology/README.md)
- [Hydrology proof lane](../../../data/proofs/hydrology/README.md)
- [Hydrology release-candidate lane](../../../release/candidates/hydrology/README.md)

GitHub review is routed by [CODEOWNERS](../../../.github/CODEOWNERS) to
`@bartytime4life`. That route does not prove specialist assignment,
independent review, source admission, approval, release, deployment, or
publication.

[Back to top](#top)
