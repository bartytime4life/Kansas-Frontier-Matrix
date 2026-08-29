<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/roads-rail-trade/source-refresh
title: Roads, Rail, and Trade Routes — Source Refresh Runbook
type: runbook
version: v1.0.0
prior_version: v0.1
prior_state: proposal-era live-refresh procedure with placeholder owners, unverified source authority, invented gate and validator commands, proposed receipt behavior, and unsupported promotion language
status: draft; repository-grounded hold boundary; bounded synthetic CorridorRoute validation available; live source refresh unavailable; non-release; non-deployment; non-publication
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Roads/Rail/Trade, source, transport, rights, sensitivity, Indigenous/Tribal stewardship, evidence, policy, security, operations, release, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; infrastructure-sensitive; historic-and-cultural-corridor-sensitive; no-network; fail-closed; non-release; non-publication
current_path: docs/runbooks/roads-rail-trade/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
responsibility: explain the current source-refresh hold, provide a repository-only readiness review, and route maintainers to the exact bounded synthetic CorridorRoute validation procedure
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, source registry and activation records, contracts, schemas, policy, evidence, review, lifecycle, proof, release, correction, and rollback authorities
canonical_relationship: same-path replacement of proposal-era instructions; prior detail remains in Git history and is not current operational authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 011bebd5ab51d22d4355eb754b5a921fb45243a0
  prior_blob: 2b403f3a6ca9bad993a30a0c8c609e712f3e4029
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  domain_readme_blob: f2d1250dad3eefd2f148483ddcc388e66d2a2186
  source_registry_readme_blob: e5ada8f7dc9eee48ed758bd4ec5c08bc4be15c0a
  subtype_source_registry_readme_blob: 54087e02e329b98c595807e4c9041c97972c0179
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  domain_connector_readme_blob: 20b94a2fa27844ae32da758c38f8570d016634ee
  corridor_route_contract_blob: 2bef2e964b8afa855ca7e72c86ca72dad2b63f52
  corridor_route_schema_blob: 663afd8aa09c52a2626d84cfbc6c76965df79942
  corridor_route_validator_blob: 9b75fd5d15d348ec788057fa1e1371f82e685415
  corridor_route_tests_blob: 4df9495c441810e5ad196d88ad67f64e00426136
  domain_workflow_blob: 391fead3fdd0d7ecead6464be7946cbaf68247e0
  proof_lane_readme_blob: 91c109d463c45c925f1d104d4cd8aaf742cd28af
  candidate_lane_readme_blob: c989bf2bed10472bc46a168231b2269f17bbda48
  proposal_descriptor_count: 5
  bounded_test_count: 14
  valid_fixture_count: 2
  invalid_fixture_count: 8
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../domains/roads-rail-trade/README.md
  - ../../domains/roads-rail-trade/DATA_LIFECYCLE.md
  - ../../domains/roads-rail-trade/SENSITIVITY.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../data/registry/roads-rail-trade/sources/README.md
  - ../../../data/registry/sources/roads-rail-trade/README.md
  - ../../../connectors/domains/roads-rail-trade/README.md
  - ../../../contracts/domains/roads-rail-trade/corridor_route.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
  - ../../../fixtures/domains/roads-rail-trade/corridor_route/
  - ../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py
  - ../../../tests/schemas/test_corridor_route_contract.py
  - ../../../.github/workflows/domain-roads-rail-trade.yml
notes:
  - "v1.0.0 retires proposal-era live-fetch, watcher, gate, receipt, lifecycle-write, and promotion instructions that current repository evidence does not implement."
  - "Five domain-first source YAML files exist, but each is explicitly a PROPOSED greenfield template with unresolved role, authority, rights, cadence, sensitivity, and access fields."
  - "The domain connector lane contains documentation and a placeholder only; no source-refresh implementation is established there."
  - "The only executable domain slice verified for this update is synthetic, no-network CorridorRoute validation."
  - "This runbook does not admit or activate a source, fetch data, emit a receipt, write a lifecycle lane, approve policy, promote, release, deploy, or publish."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Roads, Rail, and Trade Routes — Source Refresh Runbook

> [!CAUTION]
> **STOP — live Roads/Rail/Trade source refresh is not established by current
> repository evidence.** Do not execute the retired fetch, hashing, watcher,
> receipt, lifecycle-write, or promotion examples from this path. Use the
> repository-only review below and the bounded synthetic
> [no-network procedure](./NO_NETWORK_TEST_RUNBOOK.md) only.

This runbook is a fail-closed readiness and handoff procedure. It does not
contact KDOT, FHWA, FRA, Census, WZDx, OSM, GNIS, a railroad, a local
government, a Tribal or Indigenous steward, an archive, or any other source.
It does not make KFM a navigation, dispatch, traffic-control,
railroad-operating, bridge-safety, emergency-routing, legal-access,
right-of-way, regulatory, or current-closure authority.

**Use:** [current outcome](#current-outcome) ·
[authority](#authority-and-placement) ·
[repository review](#repository-only-readiness-review) ·
[synthetic validation](#bounded-synthetic-validation) ·
[live-refresh gates](#requirements-before-any-future-live-refresh) ·
[handoff](#review-handoff) ·
[rollback](#documentation-correction-and-rollback)

## Current outcome

| Surface | Current repository evidence | Result |
|---|---|---|
| Source authority | `data/registry/roads-rail-trade/sources/` contains five YAML files, each marked `PROPOSED — greenfield template` with `TBD` role, authority, rights, sensitivity, cadence, access, and citation fields. The subtype-first lane contains a README and placeholder. `control_plane/source_authority_register.yaml` is `PROPOSED`, `implementation_status: ABSENT`, and empty. | `HOLD` |
| Connector | `connectors/domains/roads-rail-trade/` contains a draft README and placeholder. Product-family lanes such as TIGER/Line and WZDx describe proposed boundaries; the inspected documentation says code, descriptors, endpoints, fixtures, tests, receipts, CI wiring, and runtime behavior remain unverified. | `HOLD` |
| Executable validation | The paired `CorridorRoute` contract and Draft 2020-12 schema, two valid fixtures, eight invalid fixtures, one validator, and fourteen focused tests are present. | `AVAILABLE` for synthetic validation only |
| No-network enforcement | The shared Python startup guard is available for explicit local activation. The domain workflow sets `KFM_NO_NETWORK=1` but does not add the guard directory to `PYTHONPATH` before Python starts. | local guarded command `AVAILABLE`; workflow-wide injection `HOLD` |
| Lifecycle write | No verified connector or source-refresh writer binds an admitted descriptor to RAW or QUARANTINE with an accepted receipt and collision policy. | `HOLD` |
| Proof and release | The domain workflow records explicit holds for proof production and release dry-run. The proof and candidate lanes contain no domain records beyond README/placeholder material. | `HOLD` |
| Live refresh, promotion, or publication | No complete source admission, transport, lifecycle, evidence, policy, review, proof, release, correction, and rollback chain is established. | `HOLD` |

A passing fixture suite changes none of these held states. It proves only the
bounded synthetic profile at the exact tested revision.

## Authority and placement

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md). The same-path
update remains under `docs/runbooks/` because this file is a human procedure.
It may explain other authorities but cannot replace them.

| Responsibility | Owning surface | This runbook may | This runbook must not |
|---|---|---|---|
| Source admission and role | Governed source registry and activation records | Inspect status and report gaps | Treat a template, filename, README, or source name as admission |
| Retrieval and admission code | `connectors/` | Require descriptor-gated, bounded behavior | Invent or activate an endpoint, credential, schedule, or writer |
| Semantic meaning | `contracts/` | Link the current contract | Redefine route meaning or source role |
| Machine shape | `schemas/` | Link the current schema | Make a documentation sketch executable |
| Policy and sensitivity | `policy/` and accountable review | Require decisions and reviewers | Approve rights, public precision, legal access, safety, or release |
| Lifecycle state | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, and `data/published` | Explain boundaries | Move, copy, or label material into a stronger state |
| Evidence and proof | Evidence contracts, resolvers, and `data/proofs/` | Require resolvable support | Treat a digest, test, receipt, map, graph, or summary as an EvidenceBundle |
| Release and rollback | `release/` and governed runbooks | Prepare a review handoff | Promote, release, deploy, publish, withdraw, or roll back production |

The repository currently has both domain-first and subtype-first
Roads/Rail/Trade source-registry lanes. Their READMEs record unresolved topology.
Do not create or update parallel descriptor sets until an accepted decision or
migration note selects the authoritative home.

## Source-role and truth rules

Source refresh must preserve what a source is qualified to support. Processing,
conflation, graph projection, map rendering, or generated explanation cannot
upgrade that role.

| Material | Permitted interpretation | Prohibited substitution |
|---|---|---|
| Official road, rail, crossing, or freight records | Time-, jurisdiction-, product-, and field-bounded administrative or regulatory assertions | Universal route truth, safe passage, legal access, or current condition |
| TIGER/Line and similar geometry | Administrative or observed geometry at a named vintage and scale | Legal right-of-way, ownership, cadastral truth, road openness, or name authority |
| WZDx or other operational event feeds | Time-bound source observations with update, expiry, and stale-state handling | Permanent network truth, traveler instruction, or emergency authority |
| OSM or other community material | Community observation or context with license and source-role limits | Legal status, official designation, jurisdiction, or safety authority |
| Archival maps and historic route records | Evidence for a claim with source vintage, method, uncertainty, and limitations | Surveyed alignment, exact continuous path, or present-day access |
| Indigenous, Tribal, oral-history, burial, sacred, or cultural-corridor material | Steward-controlled evidence under sovereignty, sensitivity, consent, and harmful-precision review | Unreviewed public geometry, inferred permission, or ownership by KFM |
| Modeled or inferred network output | Derived candidate with method, inputs, uncertainty, and evidence references | Source observation, official fact, or routable public graph edge |

Keep source time, observation or event time, valid/effective time, retrieval
time, record time, publication time, and supersession time distinct whenever
they apply. Geometry does not prove legal access; a route name does not prove
continuity; a mapped rail line does not prove active service.

## Repository-only readiness review

This is the only source-refresh review authorized by this document.

### 1. Freeze the evidence revision

Run from a clean checkout or dedicated worktree:

~~~bash
git remote get-url origin
git rev-parse HEAD
git status --short
~~~

Record the exact commit and any inherited changes. Do not attribute a result to
`main` without the commit SHA.

### 2. Inspect the authority surfaces

Confirm the current contents of:

~~~text
data/registry/roads-rail-trade/sources/
data/registry/sources/roads-rail-trade/
control_plane/source_authority_register.yaml
connectors/domains/roads-rail-trade/
contracts/domains/roads-rail-trade/corridor_route.md
schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json
fixtures/domains/roads-rail-trade/corridor_route/
tools/validators/domains/roads-rail-trade/validate_corridor_route.py
tests/schemas/test_corridor_route_contract.py
.github/workflows/domain-roads-rail-trade.yml
data/proofs/roads-rail-trade/
release/candidates/roads-rail-trade/
~~~

Use repository bytes, not this snapshot, if any path has changed.

### 3. Confirm descriptor and connector posture

The current five domain-first YAML files are proposals, not admitted sources.
Verify that status without interpreting their IDs as activation:

~~~bash
git grep -n 'status: PROPOSED — greenfield template' -- \
  data/registry/roads-rail-trade/sources/*.yaml
git grep -n 'TBD' -- data/registry/roads-rail-trade/sources/*.yaml
~~~

Also inspect directory contents. A README or placeholder does not establish
runtime code:

~~~bash
find connectors/domains/roads-rail-trade -maxdepth 2 -type f -print | sort
find data/registry/sources/roads-rail-trade -maxdepth 2 -type f -print | sort
find data/proofs/roads-rail-trade -maxdepth 2 -type f -print | sort
find release/candidates/roads-rail-trade -maxdepth 2 -type f -print | sort
~~~

If a real descriptor, connector module, receipt, proof, or candidate appears,
stop using this snapshot as current truth and review the new owning object
before changing the result.

### 4. Assign a finite review result

| Result | Meaning |
|---|---|
| `PASS` | The repository-only inventory or named synthetic check completed at the pinned revision. It says nothing about source freshness or live-refresh readiness. |
| `FAIL` | A bounded check ran and rejected its input or declared expectation. |
| `HOLD` | One or more dependencies for retrieval, admission, lifecycle write, evidence, policy, review, proof, release, correction, or rollback are incomplete. |
| `ABSTAIN` | Available evidence cannot support the requested transport or operational claim. |
| `DENY` | Rights, sensitivity, sovereignty, source role, harmful precision, security, or an authority boundary prohibits the request. |
| `ERROR` | The procedure or environment could not produce a valid result. |
| `ESCALATE` | An accountable source, rights, sensitivity, Indigenous/Tribal, transport, safety, policy, evidence, security, operations, release, or independent reviewer is required. |

Always pair `PASS` with its exact scope. The current live-refresh result remains
`HOLD`.

## Bounded synthetic validation

Use the sibling
[No-Network Test Runbook](./NO_NETWORK_TEST_RUNBOOK.md) as the canonical command
procedure. Its scope is the synthetic `CorridorRoute` contract, schema,
fixtures, validator, and focused tests.

Dependency bootstrap is a separate network and supply-chain boundary:

~~~bash
python tools/ci/install_python_ci.py project-test
~~~

After dependencies are available, enter the explicitly guarded Python window:

~~~bash
export KFM_NO_NETWORK=1
export PYTHONDONTWRITEBYTECODE=1
export PYTHONHASHSEED=0
export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD${PYTHONPATH:+:$PYTHONPATH}"

python -c 'import sitecustomize; assert sitecustomize.GUARD_ACTIVE'

python -m pytest -q -p no:cacheprovider \
  tests/schemas/test_corridor_route_contract.py

python tools/validators/domains/roads-rail-trade/validate_corridor_route.py \
  --fixtures
~~~

Expected bounded evidence:

- the startup assertion exits `0`;
- fourteen focused tests pass;
- two valid fixtures produce their declared `PASS` or `ABSTAIN` outcomes;
- eight invalid fixtures produce `DENY`; and
- fixture mode exits `0` only when every fixture matches its declared outcome.

The validator's finite outcomes are `PASS`, `ABSTAIN`, `DENY`, and `ERROR`.
It does not implement a live fetch, SourceDescriptor validation, activation
decision, RAW or QUARANTINE writer, receipt producer, EvidenceBundle resolver,
policy engine, review authenticator, proof producer, promotion executor,
release manifest, or publication path.

After validation, inspect `git status --short`. Do not claim that dependency
installation or the hosted workflow ran under the startup guard unless the
evidence proves that exact boundary.

## Requirements before any future live refresh

Live source access remains `HOLD` until current implementation authority closes
every applicable dependency below.

### Source and authority

- one authoritative registry topology and one schema-valid descriptor for the
  exact product, feed, archive, or steward-controlled collection;
- explicit source role, authority scope, native identifiers, product/vintage,
  cadence, endpoint or delivery form, rights, terms, attribution, access class,
  sensitivity, public-use limits, and steward;
- an authenticated activation decision for the exact source, mode, purpose,
  audience, and time window; and
- accountable owner and reviewer assignments without placeholder roles.

### Transport and source edge

- accepted connector placement and implementation, with explicit configuration,
  credential isolation, allowlisted egress, bounded retries, timeouts,
  rate-limit handling, size limits, and safe logs;
- conditional retrieval or immutable package comparison where the source
  supports it, without equating HTTP status to semantic no-change;
- deterministic digests, source-head identity, source-native time, retrieval
  time, and stale-state rules;
- minimized no-network fixtures and negative tests for changed, unchanged,
  malformed, unavailable, unauthorized, rate-limited, stale, superseded,
  rights-unknown, sensitive, and overprecise inputs; and
- finite outcomes that cannot publish or mutate stronger truth.

### Lifecycle, evidence, and policy

- idempotent, collision-safe RAW or QUARANTINE handoff with an accepted contract,
  schema, receipt binding, denial reasons, replay behavior, and rollback target;
- normalization that preserves source role, identity, time, geometry accuracy,
  uncertainty, rights, sensitivity, and correction lineage;
- EvidenceRef resolution to admissible EvidenceBundle support for consequential
  claims;
- active policy decisions for rights, sensitivity, sovereignty, harmful
  precision, infrastructure detail, legal-access implications, and public use;
  and
- accountable review that is distinct from authorship and CI.

### Proof, release, and public use

- proof and catalog/triplet closure without treating receipts, tests, maps,
  tiles, indexes, or graph projections as sovereign truth;
- a reviewable candidate with immutable artifact references and digests;
- promotion decision, release manifest, rollback target, correction and
  withdrawal paths, stale-state behavior, and readback evidence; and
- separate authorization for promotion, release, deployment, source activation,
  and publication.

Missing any item keeps live refresh at `HOLD`.

## No-change, stale, and supersession handling

The current repository does not establish a live source comparison, heartbeat
receipt, debounce scheduler, or refresh writer for this lane. Therefore:

- do not claim a live `304`, no-change result, source freshness, or emitted
  heartbeat from the synthetic profile;
- do not create a catalog version, graph edge, proof, candidate, or public
  artifact merely because bytes or a digest appear unchanged;
- preserve a stale or unknown state when accepted freshness evidence is absent;
- preserve prior identities and forward supersession or correction links rather
  than overwriting history; and
- require a reviewed source manifest, digest scope, semantic comparison rule,
  receipt contract, and retry policy before automating no-change behavior.

A future connector may preserve ETag, Last-Modified, package manifests, feed
sequence, source revision, or content digests when appropriate. This paragraph
does not activate that behavior.

## Mandatory stop conditions

| Condition | Result | Required action |
|---|---|---|
| Descriptor is `PROPOSED`, contains `TBD`, or lacks activation | `HOLD` | Resolve the owning source record and review; do not fetch |
| Registry topology remains ambiguous | `HOLD` | Avoid parallel descriptor mutation and request an accepted placement decision |
| Connector surface is README/placeholder only | `HOLD` | Do not invent a client, endpoint, credential, schedule, or writer |
| Shared no-network guard is not proven active for the process | `ERROR` | Stop the guarded procedure and correct the environment |
| Rights, terms, attribution, source role, cadence, or authority scope is unresolved | `HOLD` or `DENY` | Do not retrieve for a public-capable path |
| Sensitive infrastructure, private access, cultural corridor, burial, sacred, archaeological, or steward-controlled detail may be exposed | `DENY` or `ESCALATE` | Withhold; use the accountable policy and stewardship route |
| Historic geometry would be presented more precisely than evidence supports | `HOLD` or `DENY` | Preserve uncertainty and generalize or withhold only under reviewed policy |
| A current closure, safety, legal-access, operating, or emergency claim is requested | `ABSTAIN` | Direct the user to the applicable current official authority |
| A green workflow, test, digest, receipt, map, or graph is offered as proof of release | `DENY` implied authority | Narrow the claim to the exact bounded evidence |
| EvidenceRef does not resolve to admissible evidence | `ABSTAIN` or `HOLD` | Record the gap; do not strengthen the claim |
| Proof, candidate, promotion, rollback, or release dependencies are absent | `HOLD` | Stop at review handoff |
| A secret, token, restricted payload, private movement record, or harmful coordinate could enter Git, CI, logs, or a public artifact | `DENY` | Stop propagation and use the approved secure or quarantine process |

Unknown conditions never imply approval.

## Review handoff

Record only references and minimized, non-sensitive findings. The following is a
documentation checklist, not an accepted schema or release object:

~~~yaml
roads_rail_trade_source_refresh_review:
  repository: bartytime4life/Kansas-Frontier-Matrix
  revision: "<exact commit SHA>"
  source_family: "<named product, feed, archive, or steward collection>"
  mode: repository_only
  result: "<PASS|FAIL|HOLD|ABSTAIN|DENY|ERROR|ESCALATE>"
  scope: "<exact inventory or synthetic check>"
  descriptor:
    path: "<authoritative path or unresolved>"
    status: "<proposal|admitted|activated|denied|unknown>"
    activation_ref: "<reference or null>"
  connector:
    path: "<path or unresolved>"
    implementation_verified: false
    network_used: false
  validation:
    commands: []
    tested_revision: "<exact commit SHA>"
    introduced_failures: []
    inherited_failures: []
    pending_checks: []
  non_effects:
    source_retrieved: false
    lifecycle_written: false
    receipt_emitted: false
    evidence_closed: false
    policy_approved: false
    promotion_authorized: false
    released: false
    deployed: false
    published: false
  blockers: []
  accountable_reviewers_needed: []
~~~

Do not include credentials, endpoint tokens, restricted source excerpts,
sensitive coordinates, private access detail, movement histories, or
unreviewed cultural material.

## Proposal-lineage disposition

The prior v0.1 body is superseded at this path and retained in Git history. Its
proposed source inventory remains research lineage only. The following items
were not verified as a complete current implementation and must not be
reconstructed as operational authority:

- proposal-era watcher, fetcher, conditional-GET, debounce, and schedule
  behavior;
- invented gate job names and validator paths;
- proposed SourceDescriptor, receipt, proof, catalog, candidate, release, and
  lifecycle destinations;
- suggested live-source commands, signing behavior, kill switches, cache
  invalidation, heartbeat receipts, and watcher-created pull requests; and
- claims that a missing prerequisite permits writes through WORK, creates an
  `ABSTAIN` receipt, or otherwise authorizes partial live ingestion.

Connected Drive Roads/Rail/Trade documents remain doctrine, research, and
design lineage. Notion remains coordination. Current GitHub repository evidence
controls claims about implemented behavior.

## Documentation validation

For a documentation-only change to this file:

1. review the complete diff for accuracy and unrelated churn;
2. confirm one H1, logical headings, balanced fences/comments, and no trailing
   whitespace;
3. resolve every changed relative link and repository path at the pinned base;
4. reconcile commands with the current validator, tests, workflow, and
   no-network helper;
5. run the bounded synthetic profile when dependencies are available, or report
   it as not run rather than inferring a result;
6. classify hosted checks as introduced, inherited, skipped, pending, or not
   run and bind them to the exact head; and
7. keep source admission, merge, promotion, release, deployment, publication,
   and ready-for-review transitions separately authorized.

A documentation check or synthetic profile cannot prove source freshness,
rights clearance, activation, live retrieval, lifecycle mutation, evidence
closure, review, proof, promotion, release, deployment, publication,
correction, or rollback execution.

## Documentation correction and rollback

If this file becomes stale, compare the exact repository revision and correct
the same path through a focused review. Do not preserve a convenient command
after its owning implementation changes.

Before merge, close the draft pull request and delete only its task branch.
After a separately authorized merge, revert the focused documentation commit
or apply a reviewed forward correction.

Reverting this file does not undo or perform source retrieval, source admission,
lifecycle writes, policy decisions, proof production, promotion, release,
deployment, publication, correction, withdrawal, or operational rollback.

## Related repository surfaces

### Domain and procedure boundaries

- [Roads/Rail/Trade domain](../../domains/roads-rail-trade/README.md)
- [Data lifecycle](../../domains/roads-rail-trade/DATA_LIFECYCLE.md)
- [Sensitivity and public precision](../../domains/roads-rail-trade/SENSITIVITY.md)
- [No-network test procedure](./NO_NETWORK_TEST_RUNBOOK.md)
- [Promotion preflight](./PROMOTION_RUNBOOK.md)
- [Rollback readiness](./ROLLBACK_RUNBOOK.md)

### Governance and source admission

- [Accepted Directory Rules decision](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Lifecycle Law](../../doctrine/lifecycle-law.md)
- [Trust Membrane](../../doctrine/trust-membrane.md)
- [Domain-first source registry](../../../data/registry/roads-rail-trade/sources/README.md)
- [Subtype-first source registry](../../../data/registry/sources/roads-rail-trade/README.md)
- [Domain connector boundary](../../../connectors/domains/roads-rail-trade/README.md)

### Executable bounded profile

- [`CorridorRoute` semantic contract](../../../contracts/domains/roads-rail-trade/corridor_route.md)
- [`CorridorRoute` schema](../../../schemas/contracts/v1/domains/roads-rail-trade/corridor_route.schema.json)
- [Synthetic fixtures](../../../fixtures/domains/roads-rail-trade/corridor_route/)
- [Validator](../../../tools/validators/domains/roads-rail-trade/validate_corridor_route.py)
- [Focused tests](../../../tests/schemas/test_corridor_route_contract.py)
- [Domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml)
- [No-network helper](../../../tools/ci/kfm_no_network/README.md)

[Back to top](#top)
