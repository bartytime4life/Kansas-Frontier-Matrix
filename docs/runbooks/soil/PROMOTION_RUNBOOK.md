<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/soil/promotion
title: Soil - Promotion Preflight Runbook
type: runbook
version: v2.0
prior_version: v0.1
prior_state: proposal-era promotion procedure with unverified live commands, automatic gate behavior, signing, policy, proof, registry, lifecycle-write, and publication claims
status: draft; repository-grounded; PROMOTION_EXECUTION_HELD; BOUNDED_SOIL_FIXTURE_VALIDATION; BOUNDED_SSURGO_DRIFT_COMPARISON; PROOF_HELD; RELEASE_DRY_RUN_HELD; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life - verified GitHub review route"
  - "NEEDS VERIFICATION - accountable Soil, source, scientific, evidence, rights, sensitivity, policy, release, correction, rollback, public-surface, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-30
policy_label: repository-facing; soil and land context; potentially precision-sensitive; consequential-use-sensitive; fail-closed
current_path: docs/runbooks/soil/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: human promotion-readiness assessment and accountable release-review handoff for the Soil lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source-admission records, evidence, policy, review, lifecycle state, receipts, proofs, release records, correction, rollback, and competent official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ba5b47bfe081d97ecd5d927a861be40716e68019
  target_before_update_blob: ace5df133481918157faa902a9450b0f7f9cace8
  local_runbook_boundary_blob: 5d39da512018afc842182d3e59aaddeb831f67f8
  domain_workflow_blob: e009e00d5743d907461289c1c6571cab69ea2672
  candidate_readme_blob: f0f5a002ef3085790a0fcc991fc61788c9e04c4f
  release_index_blob: 19994f0faafb6a7858eae7e59c10049fd2ff5425
  source_registry_readme_blob: ee56b4950dd131c12db28f3ca88798d313cdbe1a
  inspected_ssurgo_placeholder_blob: 85fab71af52928888bc8bafb937063952a853552
  proof_readme_blob: 1d67e180326b283e33b04cbdee283520ef3b2fad
  published_readme_blob: c70312dacedf4e367d8db2607a780b088677e30d
  proposed_agri_soil_manifest_blob: 20717b51bc9f7c791f2d6bd2b0aeef5d337c9d67
  soil_map_unit_schema_blob: 41190e62cf8e90533cb66f42acd236f158bd4c1f
  soil_release_manifest_schema_blob: 14feb0ecffad32f2bf11ef943d757dbaaea41e22
  soil_promotion_decision_schema_blob: c0806cb2ff764a2e06883bd81d5dc7a1657d2f6c
  public_safe_validator_blob: a2c82caf9522e7557ba8fbf009dd296f4a965940
  public_safe_tests_blob: 348e00757d198ec77cc9af0cc75355807ccfb123
  station_moisture_tests_blob: 9388fbcca647b4d5daf32dc62a05b8aba5ae136e
  smap_l4_tests_blob: eaabd01221e8fde8ad1d6a280d8d82c2490dd40c
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  planning_report_sha256: 7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea
  soil_candidate_records_observed: 0
  soil_proof_artifacts_observed: 0
  soil_published_payloads_observed: 0
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ../../domains/soil/README.md
  - ../../domains/soil/RELEASE_INDEX.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-soil.yml
  - ../../../contracts/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/README.md
  - ../../../schemas/contracts/v1/domains/soil/soil_map_unit.schema.json
  - ../../../schemas/contracts/v1/domains/soil/release_manifest.schema.json
  - ../../../schemas/contracts/v1/domains/soil/promotion_decision.schema.json
  - ../../../policy/domains/soil/README.md
  - ../../../data/registry/sources/soil/README.md
  - ../../../data/proofs/soil/README.md
  - ../../../data/published/soil/README.md
  - ../../../data/published/layers/soil/README.md
  - ../../../release/candidates/soil/README.md
  - ../../../release/manifests/README.md
  - ../../../release/manifests/agri-soil-crop-suitability-v1-001.json
  - ../../../tests/domains/soil/README.md
  - ../../../tools/validators/domains/soil/README.md
notes:
  - "v2.0 replaces proposed live promotion instructions with a repository-grounded preflight that terminates at accountable release review or a finite fail-closed result."
  - "The active Soil workflow runs three bounded synthetic Soil fixture suites and one fixture-only SSURGO package-drift comparator; its proof and release-dry-run jobs remain explicit holds."
  - "The Soil candidate lane contains no candidate instance, the Soil release index is a greenfield placeholder, and the Soil proof and published lanes contain no payload beyond README and keep files at the pinned snapshot."
  - "The root agri-soil manifest-like JSON is explicitly PROPOSED and documentation-inventory-derived; it is not treated as a Soil release."
  - "The supplied Soil architecture report is planning lineage. It had no mounted repository and does not prove current paths, commands, admission, policy, proof, release, deployment, or publication."
  - "No source is contacted, admitted, activated, transformed, promoted, released, deployed, or published by this runbook."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="soil-promotion-runbook"></a>

# Soil - Promotion Preflight Runbook

Use this runbook to assess one immutable Soil release candidate, run the
bounded checks the repository actually provides, record missing gates, and
prepare an accountable release-review handoff. This procedure does **not**
execute promotion, release, deployment, or publication.

> [!WARNING]
> **Current repository result: `HOLD`.** No Soil candidate instance was found
> under `release/candidates/soil/`; the Soil release index is still a
> greenfield placeholder; Soil proof production and the Soil release dry run
> remain explicit workflow holds; and no candidate-bound release manifest,
> policy decision, proof pack, correction plan, or operational rollback target
> is available for promotion review.

> [!CAUTION]
> `release/manifests/agri-soil-crop-suitability-v1-001.json` is explicitly
> `PROPOSED` and says it was created from documentation inventory. Its filename
> is not release evidence, and it must not be used as a substitute Soil
> candidate or release manifest.

> [!IMPORTANT]
> KFM Soil material is not agronomic, engineering,
> conservation-compliance, land-value, title, regulatory, emergency, or
> safety advice. Route consequential decisions to the relevant qualified
> professional and official authority.

**Quick navigation:** [Purpose and authority](#purpose-and-authority-boundary) ·
[Current repository disposition](#current-repository-disposition) ·
[Outcomes](#finite-outcomes-and-precedence) ·
[Candidate requirements](#candidate-preconditions) ·
[Procedure](#promotion-preflight-procedure) ·
[Validation](#repository-native-validation) ·
[Handoff](#accountable-review-handoff) ·
[Rollback](#rollback-of-this-document)

## Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). Human
operational procedures belong under `docs/runbooks/`; release candidates and
release decisions remain under `release/`; lifecycle data remains under
`data/`; semantic meaning remains under `contracts/`; machine shape remains
under `schemas/`; and policy remains under `policy/`.

Promotion is a governed state transition. It is not:

- a file move into `data/published/`;
- a branch merge or pull-request state change;
- a green test or workflow;
- a change to a `current`, `latest`, catalog, map, or cache alias;
- a generated summary, screenshot, tile, report, or AI answer; or
- a decision this Markdown file can make.

| Concern | Owning surface | This runbook's limit |
|---|---|---|
| Human preflight and handoff | `docs/runbooks/soil/` | Explains bounded checks, finite outcomes, and stop conditions |
| Soil object meaning | [`contracts/domains/soil/`](../../../contracts/domains/soil/README.md) | Consumes accepted meaning; does not redefine it |
| Soil machine shape | [`schemas/contracts/v1/domains/soil/`](../../../schemas/contracts/v1/domains/soil/README.md) | Uses exact schema versions when accepted; does not create authority |
| Source identity and admission | [`data/registry/sources/soil/`](../../../data/registry/sources/soil/README.md) | Requires candidate-bound records; does not admit or activate a source |
| Lifecycle payloads | `data/raw|work|quarantine|processed|catalog|triplets|published/` | Inspects immutable pointers only; performs no lifecycle write |
| Evidence and proof | [`data/proofs/soil/`](../../../data/proofs/soil/README.md) and accepted evidence objects | Requires closure; does not create evidence or proof |
| Policy | [`policy/domains/soil/`](../../../policy/domains/soil/README.md) and accepted cross-cutting policy | Requires an exact evaluation; does not choose policy ad hoc |
| Candidate review | [`release/candidates/soil/`](../../../release/candidates/soil/README.md) | Requires one exact candidate; does not approve it |
| Release records | `release/manifests/`, correction, withdrawal, and rollback lanes | Requires accepted records; does not issue them |
| Public state | Governed resolvers and released public-safe carriers | No direct public mutation or unpublished read path is authorized |

Public clients and ordinary UI surfaces use governed APIs and released,
public-safe carriers. They do not read `RAW`, `WORK`, `QUARANTINE`, candidate,
source-registry, proof-store, or direct model state.

## Current repository disposition

The preflight is intentionally fail-closed. At the pinned repository snapshot:

| Surface | Confirmed repository state | Promotion consequence |
|---|---|---|
| Candidate inventory | `release/candidates/soil/` contains only `README.md` | `HOLD`: there is no immutable candidate identity to review |
| Soil release index | `docs/domains/soil/RELEASE_INDEX.md` says `Greenfield placeholder.` | `HOLD`: no authoritative Soil release inventory is established |
| Manifest-like Soil file | `release/manifests/agri-soil-crop-suitability-v1-001.json` is `PROPOSED` and inventory-derived | Do not treat it as a candidate-bound release record |
| Proof inventory | `data/proofs/soil/` contains only `README.md` and `.gitkeep` | `HOLD`: no Soil proof artifact or ProofPack is available |
| Published inventory | `data/published/soil/` contains only `README.md` and `.gitkeep` | No public Soil payload is established by the repository lane |
| Source registry | The canonical subtype-first Soil registry and source-family YAML files exist; the inspected `nrcs-ssurgo.yaml` is a `PROPOSED` placeholder | File presence does not prove admission, rights, currentness, or candidate use |
| Soil object schemas | Some fixture-first schemas are substantive and explicitly inactive; the Soil `release_manifest` and `promotion_decision` schemas remain permissive greenfield stubs | Candidate-bound schema and release-contract closure remain unproved |
| Soil policy | The policy index records one fixture-only watcher guard, five scaffolds, incompatible direct result shapes, and no accepted general Soil bundle/evaluator | `HOLD`: no candidate-bound policy decision can be inferred |
| Bounded validation | The active Soil workflow runs three deterministic synthetic Soil suites plus one fixture-only SSURGO drift comparator | Useful guardrail evidence only; not source, proof, policy, review, or release approval |
| Proof job | The workflow emits `WORKFLOW_HOLD: no accepted Soil proof producer or deterministic proof command` | Proof production remains held |
| Release dry run | The workflow emits `WORKFLOW_HOLD: no accepted Soil release dry-run command or candidate manifest contract` | Promotion, release, deployment, and publication remain held |
| Reviewer routing | CODEOWNERS routes review to `@bartytime4life` and explicitly says routing is not stewardship or approval | Accountable functional and independent review assignments remain unresolved |

The current finite result is:

```text
HOLD
```

with at least these reason codes:

```text
SOIL_CANDIDATE_ABSENT
SOIL_RELEASE_INDEX_PLACEHOLDER
SOIL_CANDIDATE_MANIFEST_UNESTABLISHED
SOIL_CANDIDATE_BOUND_SOURCE_AND_RIGHTS_UNVERIFIED
SOIL_CANDIDATE_BOUND_EVIDENCE_UNAVAILABLE
SOIL_POLICY_EVALUATOR_UNBOUND
SOIL_PROOF_PRODUCER_UNESTABLISHED
SOIL_RELEASE_DRY_RUN_UNESTABLISHED
SOIL_ACCOUNTABLE_REVIEW_AUTHORITY_UNVERIFIED
SOIL_OPERATIONAL_ROLLBACK_UNESTABLISHED
```

A later run must recompute this disposition from the exact candidate SHA and
current repository evidence. Do not carry a prior `PASS`, review, or hold
forward without revalidation.

## Finite outcomes and precedence

Check results, review states, and release states are separate.

| Outcome | Meaning in this runbook | Effect |
|---|---|---|
| `PASS` | One exact bounded check passed at the recorded SHA | Evidence for that check only |
| `FAIL` | One exact bounded check failed or an expected-negative case did not fail as specified | Repair or classify; do not promote |
| `HOLD` | A required candidate, authority, evidence, policy, proof, review, release, correction, or rollback gate is incomplete | Stop and preserve the gap |
| `ABSTAIN` | Available evidence cannot support the requested claim or readiness determination | Do not guess or upcast support |
| `DENY` | Rights, sensitivity, source-role, support-type, public-boundary, or other policy rules prohibit the action | Do not advance the candidate |
| `ERROR` | Inputs or tooling are malformed, inconsistent, unavailable, or nondeterministic | Repair before relying on a result |
| `ESCALATE` | The review can be classified but must move to a protected or competent-authority channel | No public detail or promotion |
| `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` | Every documented preflight input is complete enough for the owning release authority to review | Terminal state of this runbook; not approval or release |

When multiple outcomes apply, use the most restrictive supported result:

```text
ERROR > DENY > ESCALATE > ABSTAIN > HOLD > READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
```

`ESCALATE` does not override a concrete `ERROR` or `DENY`; it records the
required protected handoff. Runtime `ANSWER` is not a promotion outcome.

## Candidate preconditions

Do not begin substantive promotion review until one candidate record identifies
one immutable candidate. A filename, directory, branch, pull request, catalog
entry, or map layer is not enough.

### Minimum candidate identity

The candidate must bind:

- stable candidate ID and version;
- exact repository commit;
- immutable artifact URI or repository pointer;
- content digest and, where material, geometry or representation digest;
- object/profile/schema versions;
- lifecycle stage and prior state;
- proposed public carrier and audience;
- source and EvidenceBundle references;
- support-type and source-role mapping;
- correction, withdrawal, supersession, and rollback references; and
- candidate owner plus accountable review routes.

If any mutable alias is present, also record the immutable object it resolved to
at review time. Never validate only `current`, `latest`, a floating URL, or an
unversioned source response.

### No-op and materiality check

A changed retrieval timestamp, run ID, generated-at timestamp, or formatting
difference does not by itself justify promotion. A material candidate may be
triggered by a content, source version, schema, geometry, method, QC, policy, or
review-significant change, but that trigger creates review work only.

The supplied Soil planning report proposed a similar distinction on its page 17:
material source/content/schema/QC changes may create a promotion candidate,
while timestamp-only change, source unavailability, failed validation, unclear
rights, or incomplete catalog/proof must not promote. That report had no mounted
repository; this runbook treats the rule as planning lineage and requires current
candidate-bound evidence before use.

## Promotion gate matrix

Every row is non-compensable. A strong result in one row cannot offset a
failure in another.

| Gate | Required candidate-bound evidence | Fail-closed result |
|---|---|---|
| Identity | Stable ID, version, exact SHA, immutable pointers, digests, profile versions | `ERROR` or `HOLD` |
| Source admission | Exact SourceDescriptor/admission record, source role, permitted claims, snapshot/version, terms, rights, attribution, withdrawal posture | `HOLD`, `ABSTAIN`, or `DENY` |
| Lifecycle | Candidate points only to governed processed/catalog/proof inputs; no direct RAW/WORK/QUARANTINE-to-public path | `DENY` |
| Semantic contract | Exact accepted Soil meaning for every object family and cross-lane relation | `HOLD` or `ABSTAIN` |
| Machine shape | Closed accepted schemas and exact validation reports for the candidate, manifest, decision, and public envelope | `FAIL` or `HOLD` |
| Support type | Explicit accepted vocabulary/mapping; static survey, gridded/model derivative, station observation, satellite grid, pedon/profile, interpretation, and public-safe carrier remain distinct | `DENY` or `ABSTAIN` |
| Source role | Observation, survey, model, aggregate, classification, interpretation, regulatory, contextual, and synthetic roles are not upcast | `DENY` |
| Soil identity and lineage | Relevant MUKEY/COKEY/CHKEY, map-unit/component/horizon, station/depth, grid-cell, source-vintage, transform, and derivative lineage is intact | `FAIL` or `HOLD` |
| Time | Source, observation, valid, retrieval, release, correction, and transaction times remain distinct where material; staleness is explicit | `ABSTAIN` or `HOLD` |
| Measurement quality | Units, depth basis, method, QC, uncertainty, no-data semantics, resolution, aggregation, and limitations are recorded | `ABSTAIN` or `DENY` |
| Geometry and sensitivity | Public scale/precision is authorized; private field, parcel, station, cultural, Tribal, rare-location-adjacent, or operational detail is generalized, withheld, or denied before rendering | `DENY` or `ESCALATE` |
| Evidence | Every consequential claim resolves from EvidenceRef to admissible EvidenceBundle support with limitations and public-safe citations | `ABSTAIN` |
| Validation | Exact commands, fixtures, environment, SHA, outputs, expected-negative polarity, and introduced/inherited failure classification | `FAIL`, `ERROR`, or `HOLD` |
| Policy | Exact accepted bundle, evaluator, input, decision, reason codes, obligations, version, and consumer enforcement | `DENY` or `HOLD` |
| Proof and catalog | Candidate-bound proof objects plus required catalog/checksum/manifest closure; receipts remain distinct from proof | `HOLD` |
| Review | Accountable Soil, scientific, source, rights, sensitivity, evidence, policy, release, correction/rollback, and required independent review are recorded | `HOLD` |
| Correction and rollback | Exact correction path, withdrawal path, invalidation targets, prior safe release or withdrawal posture, rollback candidate, and testable recovery plan | `HOLD` |
| Release dry run | Accepted candidate-manifest contract and non-publishing dry-run command produce an exact candidate-bound report | `HOLD` |
| Public carrier | Governed resolver/API and released public-safe artifact are named; direct internal-store access is impossible | `DENY` or `HOLD` |

The planning report's page 16 distinction remains useful: receipt, proof,
catalog, and publication are different object families. A receipt records what
ran. It does not prove a Soil claim, close review, or authorize release.

## Promotion preflight procedure

### Step 0 - Freeze authority, base, and overlap

Record:

```text
repository:
base_sha:
candidate_id:
candidate_version:
candidate_artifact_digests:
target_release_id:
open_overlapping_prs:
reviewer_routes:
```

Confirm the target runbook, candidate, schemas, policy, proofs, release records,
and rollback surfaces have not changed since discovery. Stop on unresolved
same-path overlap or a moving candidate.

### Step 1 - Establish that the candidate exists

Inspect `release/candidates/soil/` and the candidate's immutable referenced
artifacts. Confirm the record is more than a README, keep file, example,
fixture, placeholder, or documentation-inventory projection.

Current result: `SOIL_CANDIDATE_ABSENT`.

Do not manufacture a candidate inside this procedure. Candidate creation has
its own contracts, schemas, evidence, and review boundary.

### Step 2 - Classify the candidate without collapsing support

Record the candidate's object families, source roles, support types, spatial
support, temporal support, depth basis, units, quality flags, uncertainty, and
intended claims.

Current fixture profiles use profile-local strings such as `static_survey`,
`station_observation`, `satellite_grid`, and `modeled_derivative`; other Soil
documents use longer planning labels. These strings are not made canonical by
this runbook. Require an accepted candidate-bound vocabulary or mapping.

Deny any candidate that treats:

- a survey map unit as a parcel, farm boundary, or current field condition;
- a component or horizon as a whole map unit;
- a station reading as area truth;
- a satellite or modeled grid as an in-situ observation;
- a pedon/profile as map-unit truth without a declared derivation;
- a gridded derivative as the source-of-record survey;
- a hydrologic soil group as a flood observation or forecast;
- an erosion or suitability interpretation as legal, engineering, regulatory,
  conservation, or crop-management advice; or
- an Agriculture, Hydrology, Geology, Habitat, Flora, Fauna, Hazards, or
  People/Land claim as Soil-owned truth.

### Step 3 - Verify source, rights, and acquisition posture

For every source:

1. resolve the exact admitted source record;
2. verify source role and permitted claim family;
3. pin source version, snapshot, query/extraction profile, and retrieval time;
4. record license, attribution, redistribution, endpoint terms, and access
   constraints;
5. record source corrections, withdrawals, caveats, and freshness; and
6. confirm no live request or temporary URL is being treated as an immutable
   release input.

The presence of a short YAML file under the source registry is not source
admission. Current `nrcs-ssurgo.yaml` is a `PROPOSED` placeholder.

### Step 4 - Verify lifecycle and immutable identity

Trace every input and output through:

```text
SOURCE EDGE
  -> RAW
  -> WORK or QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET / PROOF SUPPORT
  -> RELEASE REVIEW
  -> PUBLISHED PUBLIC-SAFE CARRIER
```

No stage may be inferred from a path name. Reject direct public dependence on
RAW, WORK, QUARANTINE, candidate, registry, or unpublished proof stores.

Recompute the candidate's deterministic hashes using the accepted profile.
Differentiate at least:

- source-content hash;
- transform/specification hash;
- output/content hash;
- geometry or representation hash when material; and
- release-manifest digest.

Timestamp-only changes do not create new truth or automatic promotion.

### Step 5 - Verify contract and schema closure

Pin the exact semantic contract and schema for every candidate object and
envelope. Confirm:

- schema IDs and versions;
- closed or intentionally bounded fields;
- required references;
- finite enums;
- deterministic identity rules;
- source-role and support-type constraints;
- time, units, depth, QC, uncertainty, and no-data semantics;
- public-use and release-state constraints; and
- fixture and validator pairing.

Current `soil_map_unit.schema.json` is a substantive, closed,
`PROPOSED_INACTIVE` fixture-candidate profile. Current Soil
`release_manifest.schema.json` and `promotion_decision.schema.json` remain
permissive greenfield stubs. None supplies candidate-bound release authority.

### Step 6 - Resolve evidence and limitations

Every consequential claim, field, layer, summary, export, report, or AI-facing
statement must resolve to admissible evidence. Record:

```text
claim_id -> evidence_refs -> EvidenceBundle -> source/admission records
         -> limitations -> public-safe citation projection
```

Use `ABSTAIN` when support is missing, indirect, stale, role-incompatible,
scale-incompatible, or insufficient for the intended claim. Generated wording,
map display, schema validity, and repeated source agreement do not replace
evidence closure.

### Step 7 - Run the current bounded repository checks

Run the four commands in [Repository-native validation](#repository-native-validation)
from a clean checkout at the exact candidate-review SHA. Record every command,
environment, exit code, and unexpected skip.

These checks exercise only synthetic, no-network profiles. They do not validate
a real candidate, live source, evidence resolver, policy engine, proof producer,
release dry run, public API, deployment, or publication path.

### Step 8 - Verify candidate-bound policy

Require:

- exact policy input;
- accepted policy bundle digest and version;
- accepted evaluator;
- normalized finite decision;
- public-safe reason codes;
- enforceable obligations;
- consumer acknowledgment/enforcement; and
- replay, correction, withdrawal, and rollback behavior.

The current Soil policy index does not establish an accepted general Soil
bundle/evaluator. Do not compose direct Rego files by filename or infer a
decision from their presence.

### Step 9 - Verify proof, catalog, and manifest closure

Confirm the candidate has candidate-bound proof and catalog support where
required. Verify digests across artifact manifests, evidence, catalog
projections, and release records.

Current `data/proofs/soil/` has no proof payload. The active workflow therefore
keeps proof production held.

Do not treat:

- a run receipt as proof;
- a catalog entry as evidence authority;
- a schema-valid manifest as release approval;
- a signature as proof of scientific truth; or
- a map/tile/export as the canonical Soil record.

### Step 10 - Verify correction, withdrawal, and rollback

Use [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) to assess the candidate's
recovery posture. Require exact:

- affected and target release identities;
- correction and withdrawal paths;
- public resolver and cache invalidation targets;
- derivative dependency inventory;
- rollback candidate and prior safe target or explicit withdrawal-only posture;
- validation and re-publication plan; and
- accountable operator and reviewer routes.

A release without a testable correction and rollback path remains `HOLD`.

### Step 11 - Require a non-publishing release dry run

A qualifying dry run must:

- consume the exact candidate and accepted manifest contract;
- resolve candidate-bound source, evidence, policy, proof, review, correction,
  and rollback references;
- produce no release, lifecycle, deployment, or public-state mutation;
- emit a deterministic report and receipt;
- fail closed on missing or conflicting inputs; and
- be reproducible at the exact SHA.

The current Soil workflow explicitly records that no accepted Soil release
dry-run command or candidate manifest contract is wired.

### Step 12 - Produce one minimized handoff

Return one finite outcome and the smallest public-safe evidence packet needed
for accountable review. Do not copy source payloads, private coordinates,
credentials, protected station details, restricted excerpts, or unnecessary
personal or land-context information into the handoff.

Stop at `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW`. The release authority may still
deny, abstain, hold, request correction, or require additional review.

## Repository-native validation

Run from the repository root at the exact SHA under review:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_smoke.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_moisture_qc.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_smap_l4_anti_collapse.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose
```

The active workflow currently binds these checks:

| Check | Confirmed bounded coverage | Explicit non-proof |
|---|---|---|
| Public-safe Soil fixture | Closed synthetic fields, support types, source/evidence refs, generalized county support, depth/measurement bounds, fixture-only governance, deterministic non-echoing results | No Soil truth, live source, evidence resolution, policy, proof, or release |
| Station moisture fixture | Identity, depth, units, canonical UTC plus source timezone, QC, dedupe, bounded values, public-safe geometry, parser bounds | No station freshness, source admission, area truth, scientific fitness, or release |
| SMAP L4 fixture | Surface/root-zone and NRT/standard-quality separation, model/grid/raw/station/field anti-collapse, QA, uncertainty, cadence, non-release governance | No live SMAP access, ground truth, canonical vocabulary, policy, or release |
| SSURGO drift comparator | Fixture-only package/schema/table/geometry/materiality/chronology comparison with finite review-only outcomes | No retrieval, admission, rights, currentness, candidate creation, promotion, or publication |

`KFM_NO_NETWORK=1` is posture metadata, not a firewall. The Python suites install
targeted test-level guards for specific networking APIs; they do not prove
runner-wide, operating-system, container, dependency-install, or non-Python
egress isolation.

The SSURGO comparator's `PROPOSED_WORK_RECORD` means review work may be needed.
Its report keeps `promotion_allowed=false` and `publication=false`. Do not map
that outcome to release readiness.

For rollback-candidate shape only, the current generic non-executing profile may
also be checked:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose

python tools/validators/release/validate_rollback_card.py --fixtures
```

These generic checks do not select a Soil rollback target or authorize
execution.

## Mandatory stop conditions

| Condition | Required result |
|---|---|
| No exact candidate record or immutable artifact digest | `HOLD` |
| Candidate is only a README, fixture, placeholder, inventory projection, branch, PR, or mutable alias | `HOLD` |
| Source identity, admission, rights, attribution, terms, version, or withdrawal posture is missing | `HOLD`, `ABSTAIN`, or `DENY` |
| Candidate crosses directly from RAW, WORK, QUARANTINE, registry, candidate, or proof support to a public surface | `DENY` |
| Source roles or support types collapse | `DENY` |
| MUKEY/COKEY/CHKEY, map-unit/component/horizon, station/depth, grid-cell, or source-vintage lineage is inconsistent | `FAIL` or `HOLD` |
| Time, units, depth, method, QC, uncertainty, no-data, scale, or resolution is missing for a consequential claim | `ABSTAIN` or `DENY` |
| Private field/parcel/station, cultural, Tribal, exact-location, or harmful operational detail may be exposed | `DENY` or `ESCALATE` |
| EvidenceRef does not resolve to admissible candidate-bound evidence | `ABSTAIN` |
| Candidate schemas, promotion decision, or release manifest are permissive, placeholder, incompatible, or unvalidated | `HOLD` |
| Required policy bundle, evaluator, decision, obligations, or consumer enforcement is absent | `HOLD` or `DENY` |
| Proof or catalog/manifest digest closure is absent | `HOLD` |
| Required reviewer identity, authority, independence, or decision record is absent | `HOLD` |
| Correction, withdrawal, invalidation, supersession, or rollback target is absent | `HOLD` |
| Release dry run is absent, mutating, nondeterministic, or not candidate-bound | `HOLD` or `ERROR` |
| A command would contact a live source, mutate lifecycle state, alter public aliases, deploy, release, or publish | Stop and use the separately authorized owning procedure |
| The requested conclusion is agronomic, engineering, legal, regulatory, conservation-compliance, emergency, or safety advice | `DENY` or `ESCALATE` |

## Accountable review handoff

Use a public-safe packet shaped like the following. This is an illustrative
review record, not an accepted schema:

```yaml
candidate:
  id: "<stable candidate ID>"
  version: "<version>"
  repository_sha: "<40-hex commit>"
  artifact_refs:
    - uri: "<immutable pointer>"
      sha256: "<64 lowercase hex>"
  proposed_release_id: "<stable release ID>"

scope:
  object_families: []
  source_roles: []
  support_types: []
  geography: "<public-safe description>"
  temporal_scope: "<valid/source/observation/retrieval scope>"
  depth_and_units: "<declared profile>"
  intended_claims: []
  prohibited_uses: []

closure:
  source_admission_refs: []
  rights_and_terms: "<PASS | HOLD | DENY>"
  evidence_bundle_refs: []
  evidence_status: "<PASS | ABSTAIN | HOLD>"
  schema_and_contract_refs: []
  validation_reports: []
  policy_decision_ref: null
  proof_refs: []
  catalog_and_manifest_refs: []
  correction_ref: null
  withdrawal_ref: null
  rollback_candidate_ref: null
  release_dry_run_ref: null

review:
  soil_steward: null
  scientific_reviewer: null
  source_and_rights_reviewer: null
  sensitivity_reviewer: null
  evidence_reviewer: null
  policy_reviewer: null
  release_reviewer: null
  correction_and_rollback_reviewer: null
  independent_reviewer: null

result:
  outcome: "HOLD"
  reason_codes:
    - "SOIL_CANDIDATE_ABSENT"
  limitations: []
  non_effects:
    source_contacted: false
    source_activated: false
    lifecycle_mutated: false
    released: false
    deployed: false
    published: false
```

### Reviewer questions

Before accepting even `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW`, confirm:

- Is every claim tied to the correct source role and support type?
- Can every public statement be reconstructed to candidate-bound evidence?
- Are source rights, attribution, redistribution, and withdrawal terms exact?
- Are scale, precision, private-land, station, cultural, and sovereignty risks
  handled before rendering or export?
- Are time, depth, units, QC, uncertainty, and limitations visible?
- Did expected-negative fixtures fail for the intended reason?
- Are test failures attributed to the exact base/head rather than merely called
  inherited?
- Is policy evaluated by an accepted bundle and evaluator?
- Are receipts, proofs, catalogs, manifests, and release decisions kept
  separate?
- Is accountable human review recorded, including required independence?
- Can the release be corrected, withdrawn, invalidated, and rolled back without
  hiding lineage?
- Does the public carrier use governed interfaces and released artifacts only?

## Promotion decision boundary

This runbook may produce only:

```text
READY_FOR_ACCOUNTABLE_RELEASE_REVIEW
HOLD
ABSTAIN
DENY
ERROR
ESCALATE
```

It must not produce or imply:

- `APPROVED`, `PROMOTED`, `RELEASED`, or `PUBLISHED`;
- a `PromotionDecision` or `ReleaseManifest`;
- source activation or admission;
- a lifecycle transition;
- a signature or attestation;
- public alias or resolver mutation;
- cache or tile invalidation;
- deployment;
- review approval; or
- an agronomic, engineering, legal, regulatory, conservation, or safety
  determination.

A future owning release procedure may consume the handoff only after its
contracts, schemas, policy, proof, review, dry-run, correction, and rollback
gates are independently established.

## Correction, supersession, and audit trail

If the preflight packet is wrong:

1. preserve the original packet and exact candidate identity;
2. record the defect and affected claims;
3. issue a corrected packet with a new immutable identity;
4. link supersession rather than silently rewriting history;
5. re-run candidate-bound validation and policy;
6. reassess every derivative, public carrier, and rollback target; and
7. keep the release result at `HOLD` until accountable review closes the
   correction.

Do not delete source evidence, receipts, failed reports, prior decisions, or
lineage merely to make a later candidate appear clean. Apply separate lawful
retention, privacy, or erasure controls when required.

## Maintenance triggers

Update this runbook when any of the following changes:

- an actual Soil candidate record is added;
- the Soil release index gains an authoritative entry;
- an accepted Soil candidate-manifest, PromotionDecision, or ReleaseManifest
  contract/schema replaces the current stubs;
- source registry records move from placeholders to admitted candidate-bound
  sources;
- an accepted Soil policy bundle/evaluator and native tests are wired;
- a Soil proof producer or catalog-closure command is accepted;
- the active Soil workflow command inventory or hold semantics changes;
- a non-publishing Soil release dry run becomes available;
- accountable steward or independent-review assignments change;
- a Soil public carrier, correction, withdrawal, invalidation, or rollback path
  becomes operational; or
- Directory Rules, lifecycle, public-boundary, or release doctrine changes.

Do not advance maturity from document length, path presence, green fixture
tests, or a manifest-like filename. Pin the exact evidence and preserve
unknowns until their owning surfaces establish otherwise.

## Source and planning lineage

This runbook was reconciled against current repository bytes first. The
*KFM Soil Architecture Extended Pro PDF-Only Planning Report* (2026-04-21,
SHA-256
`7c2d498212b9ad56f3ba37bf91f841e9f328794e8aa4940f8f665a4116c5aaea`)
was consulted as read-only lineage. Its useful preserved ideas include:

- support-type separation across survey, gridded, station, satellite/model, and
  interpretation surfaces;
- material-change versus timestamp-only-change distinction;
- finite fail-closed outcomes;
- receipt/proof/catalog/publication separation; and
- correction and rollback as promotion prerequisites.

The report explicitly had no mounted repository. Its proposed commands, paths,
validators, APIs, signing, policy, proof, and publication behavior are not
implementation evidence and were not copied forward as current procedure.

## Rollback of this document

Before merge, close the draft pull request and delete only its task branch.
After merge, use an ordinary reviewed revert or a corrective follow-up.

Documentation rollback does not contact a source, change source admission,
reverse lifecycle state, withdraw a release, restore a public alias, invalidate
a cache, redeploy a service, or undo a publication event.

[Back to top](#top)
