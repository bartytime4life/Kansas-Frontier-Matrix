<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/rollback
title: Fauna Rollback Runbook
type: operational-runbook
version: v2.0.1
status: DRAFT_REPOSITORY_GROUNDED; REVIEW_HANDOFF_ONLY; SHARED_SYNTHETIC_REHEARSAL_AVAILABLE; FAUNA_TABLETOP_AVAILABLE; FAUNA_INTEGRATED_REHEARSAL_ABSENT; OPERATIONAL_ROLLBACK_HELD; SENSITIVE_LOCATION_FAIL_CLOSED; NON_RELEASE; NON_PUBLICATION; NOT_FOR_LIFE_SAFETY
owners: "@bartytime4life — verified CODEOWNERS route only; accountable Fauna, taxonomy, source, rights, sensitivity, geoprivacy, evidence, policy, review, correction, rollback, release, operations, security, and public-recovery assignments NEEDS VERIFICATION"
created: 2026-05-13
updated: 2026-08-28
policy_label: repository-facing; fauna; rollback; withdrawal; correction-aware; sensitive-location; synthetic-proof-bounded; fail-closed; non-publisher
current_path: docs/runbooks/fauna/ROLLBACK_RUNBOOK.md
owning_root: docs/
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
responsibility: Classify a defective Fauna release-facing surface and prepare a bounded rollback, withdrawal, hold, error, or forward-correction review handoff without performing an operational or public mutation.
truth_posture: cite-or-abstain
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
  base_commit: 6e02ced04834c8f9f2210da8c655cdef626a3b08
  target_prior_blob: d8d7d3bb9c40d3de50d484e6d13640bee5baaa58
  lane_readme_prior_blob: 5989e996d317cace6d63c0fc6b22c2cdf9f0c207
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  rollback_drill_blob: 78a0c3663ef30e5edb9260c0c5ab58d6e7f860fb
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  synthetic_rehearsal_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  rollback_drill_workflow_blob: 2d0c39fc6ff8e44bd9cf753ce546475079e8ffd5
  fauna_schema_stub_blob: 08b82778b3654ab7643a12770bdcb976eb12e9ff
  fauna_test_lane_blob: 28853dc37d00981a405613f43b1860d5500db6bb
source_lineage:
  - "KFM_Fauna_Architecture_PDF_Only_Report.pdf | PLANNING_LINEAGE | Preserve Fauna source-role, sensitivity, geoprivacy, evidence, correction, and rollback framing only; its no-repository assumptions do not describe current implementation."
  - "KFM Evidence, Documentation & Ideas Atlas — 2026-08-24 | NOTION_COORDINATION_ONLY | Keep implementation, review, merge, authorization, execution, release, deployment, promotion, and publication separate."
  - "KFM Markdown Update & Modernization Agent v1.0 | CURRENT_TASK_GUIDANCE | Apply same-path repository-grounded Markdown modernization and focused draft-pull-request delivery."
related:
  - docs/runbooks/fauna/README.md
  - docs/runbooks/fauna/ROLLBACK_DRILL.md
  - docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - docs/runbooks/fauna/PUBLICATION_GATE_DRY_RUN.md
  - docs/runbooks/fauna/SENSITIVE_OCCURRENCE_REVIEW.md
  - docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md
  - docs/domains/fauna/README.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/POLICY.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - contracts/release/rollback_card.md
  - schemas/contracts/v1/release/rollback_card.schema.json
  - schemas/contracts/v1/domains/fauna/rollback_card.schema.json
  - tools/validators/release/validate_rollback_card.py
  - tools/release/rollback_apply.py
  - tests/validators/test_validate_rollback_card.py
  - tests/release/test_synthetic_rollback_rehearsal.py
  - tests/domains/fauna/release/rollback/README.md
  - .github/workflows/rollback-drill.yml
notes:
  - Shared RollbackCard validation and marker-protected synthetic rollback/withdrawal mechanics are executable and fixture-first.
  - The shared profile proves candidate shape and local consistency only; governance flags remain false and release_ref remains null.
  - The Fauna rollback drill adds a public-safe tabletop, but direct Fauna fixtures, tests, an executor, a safe target, and operational authority remain absent.
  - The Fauna-specific rollback-card schema is a permissive id-only greenfield stub and is not operational proof.
  - The helper's optional report path is caller-controlled and not confined to the synthetic workspace.
  - Scenario-derived correction and invalidation paths can replace existing files on collision; append-only synthetic history is not established.
  - This runbook prepares classification and review evidence only and performs no containment, rollback, withdrawal, correction, alias mutation, invalidation, release, deployment, promotion, or publication.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Rollback Runbook

> **Purpose.** Classify a suspected Fauna release defect, assess whether rollback or withdrawal is supportable, and prepare a public-safe accountable-review handoff. Stop before any operational or public mutation.

> [!WARNING]
> KFM is not an official wildlife, law-enforcement, hunting, veterinary, regulatory, disease-response, emergency, or life-safety authority. Direct current determinations and operational instructions to the responsible agency or steward.

> [!IMPORTANT]
> **Current disposition:** `SHARED_SYNTHETIC_REHEARSAL_AVAILABLE / FAUNA_TABLETOP_AVAILABLE / FAUNA_INTEGRATED_REHEARSAL_ABSENT / OPERATIONAL_FAUNA_ROLLBACK_HOLD`.

The highest successful output from this procedure is:

```text
REVIEW_HANDOFF_READY
```

That state is not rollback approval, rollback execution, recovery, release, deployment, promotion, or publication.

**Navigation:** [Scope](#scope) · [Authority](#authority) · [Evidence](#current-evidence) · [Safety](#safety-and-source-role) · [Decision](#decision-model) · [Preflight](#preflight) · [Validation](#candidate-and-rehearsal-validation) · [Target](#prior-target-safety) · [Invalidation](#invalidation-and-cross-lane-impact) · [Handoff](#review-handoff) · [Graduation](#operational-graduation) · [Maintenance](#maintenance-and-document-rollback)

---

<a id="scope"></a>

## Scope

Use this runbook when a released or release-facing Fauna carrier may be defective and maintainers need to determine whether to prepare:

- a forward correction;
- `ROLLBACK_CANDIDATE`;
- `WITHDRAWAL_CANDIDATE`;
- `HOLD`;
- `ERROR`; or
- `NO_ACTION` when rollback is not the appropriate mechanism.

This procedure may pin evidence, classify the defect, validate a candidate, run shared synthetic checks, inventory consumers, and prepare a review packet. It must not activate or withdraw a source, retrieve wildlife data, process protected location detail, mutate lifecycle state, alter a public alias, invalidate a real consumer, issue a correction notice, release, deploy, promote, or publish.

[Back to top](#top)

---

<a id="authority"></a>

## Authority

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). Human procedures live under `docs/runbooks/`; meaning under `contracts/`; machine shape under `schemas/`; policy under `policy/`; executable mechanics under `tools/` and `pipelines/`; behavioral evidence under `tests/`; lifecycle/proof/receipt artifacts under `data/`; and release decisions under `release/`.

| Surface | Current role | Limit |
|---|---|---|
| This runbook | Classification, preflight, commands, interpretation, handoff | Documentation only |
| [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | Fauna tabletop plus shared rehearsal | No public mutation |
| [`RollbackCard` contract](../../../contracts/release/rollback_card.md) | Candidate meaning | No authority flags |
| [Shared schema](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Closed candidate shape | Not target safety or approval |
| [Fauna schema stub](../../../schemas/contracts/v1/domains/fauna/rollback_card.schema.json) | Greenfield placeholder | Do not use operationally |
| [Shared validator](../../../tools/validators/release/validate_rollback_card.py) | Fixture or explicit-candidate validation | Local consistency only |
| [Shared helper](../../../tools/release/rollback_apply.py) | Marker-protected synthetic plan/apply | Never a production operator |
| [Generic rehearsal tests](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Eight shared tests | Not Fauna integration |
| [Fauna test lane](../../../tests/domains/fauna/release/rollback/README.md) | Guidance/scaffold | Direct executable proof absent |

[Back to top](#top)

---

<a id="current-evidence"></a>

## Current evidence

At `main@6e02ced04834c8f9f2210da8c655cdef626a3b08`:

- the prior runbook was proposal-era, named unverified paths/actors, and linked an absent `VALIDATION_RUNBOOK.md`;
- the shared RollbackCard contract, closed schema, three valid fixtures, six invalid fixtures, expected findings, validator, and validator tests exist;
- the shared helper requires an exact synthetic marker, safe relative paths, digest/target checks, and all nine invalidation classes;
- eight generic rollback/withdrawal tests exist;
- the hosted rollback workflow runs the shared profile and a Hazards extension, not an integrated Fauna rehearsal;
- the Fauna rollback drill is repository-grounded as a tabletop and handoff procedure;
- direct Fauna rollback fixtures/tests are absent;
- the Fauna-specific rollback schema remains permissive and id-only;
- candidate, rollback, proof, receipt, data-plane rollback, and pipeline roots are documentation/placeholder-oriented rather than an accepted Fauna rollback instance;
- tracked Fauna delivery lanes do not prove deployment, current public state, or a safe prior target; and
- `@bartytime4life` is a verified GitHub route, not authenticated specialist or rollback authority.

> [!NOTE]
> Repository-tracked absence does not prove that no external, deployed, or cached Fauna state exists. Operational inventory and independent read-back remain separate requirements.

[Back to top](#top)

---

<a id="safety-and-source-role"></a>

## Safety and source role

Fauna rollback can reintroduce an older sensitivity, rights, taxonomy, or source-role defect. Preserve these boundaries:

- taxonomy mapping is not occurrence, legal status, range, abundance, habitat, or release authority;
- occurrence is not range, absence, population, habitat suitability, disease conclusion, mortality cause, or regulatory determination;
- public and restricted occurrence families remain distinct;
- exact or reverse-engineerable nests, dens, roosts, hibernacula, breeding/aggregation sites, telemetry paths, observer-linked records, private-land joins, steward-controlled detail, and transform parameters fail closed;
- style filters and client-only hiding are not geoprivacy transforms;
- direct observation, checklist/event data, specimen/collection record, agency/legal record, model/derived surface, and context retain distinct source roles;
- a public endpoint does not establish redistribution rights; and
- maps, tiles, indexes, tests, receipts, and AI output are not evidence or release authority.

When containment appears necessary, route a public-safe request to the accountable operational or official authority. Record containment as `REQUESTED`, `UNKNOWN`, or `HOLD` until execution is proved.

[Back to top](#top)

---

<a id="decision-model"></a>

## Decision model

| Condition | Classification | Next step |
|---|---|---|
| A corrected successor can use the normal governed path while current state is safely held | Forward correction | Use promotion/correction; preserve rollback readiness |
| A distinct prior release is immutable, digest-verifiable, currently admissible, evidence-supported, taxonomy-compatible, rights-cleared, sensitivity-safe, reviewable, and consumer-compatible | `ROLLBACK_CANDIDATE` | Prepare and validate the exact candidate; stop before execution |
| Current carrier must leave public use and no safe prior target exists | `WITHDRAWAL_CANDIDATE` | Prepare withdrawal/correction review and expected public non-answer |
| Evidence, target, rights, sensitivity, taxonomy, policy, review, executor, alias, invalidation, or read-back is unresolved | `HOLD` | Name each blocker and preserve history |
| Input is malformed, contradictory, unsafe to inspect, or cannot produce a valid evaluation | `ERROR` | Record a public-safe reason and no state change |
| Signal is stale-only, already corrected, outside Fauna ownership, or affects no public state | `NO_ACTION` or route elsewhere | Record why rollback is not the mechanism |

Keep vocabularies separate:

| Vocabulary | Finite values |
|---|---|
| `RollbackCard.disposition` | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` |
| Work state | `REVIEW_HANDOFF_READY`, `HOLD`, `BLOCKED`, `NO_ACTION` |
| Validator result | `PASS`, `FAIL` |
| Runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Drill result | `DRILL_HANDOFF_READY`, `HOLD`, `ERROR` |

[Back to top](#top)

---

<a id="preflight"></a>

## Preflight

Freeze one exact affected release and repository revision.

- [ ] Affected release reference, immutable manifest identity, and artifact digests.
- [ ] Public-safe defect summary, detection time, and authority source.
- [ ] Affected claims, object families, source roles, time/geography, public carriers, caches, indexes, exports, and cross-lane derivatives.
- [ ] Current evidence resolution and limitations.
- [ ] Current source/product identity, taxonomy snapshot, native IDs, rights, approved purpose, attribution, sensitivity, geoprivacy, and public/restricted treatment.
- [ ] Applicable policy bundle, correction/public-notice requirements, accountable roles, and separation of duties.
- [ ] Distinct prior target or explicit withdrawal/hold posture.
- [ ] Current target safety, consumer compatibility, invalidation classes, executor, alias profile, receipt, and read-back path—or explicit blockers.

Missing prerequisites produce `HOLD`; do not invent an owner, path, source role, transform, or prior release.

[Back to top](#top)

---

<a id="candidate-and-rehearsal-validation"></a>

## Candidate and rehearsal validation

Prepare the actual candidate against the shared RollbackCard contract and closed schema. Do not use the Fauna schema stub.

A candidate must use one finite disposition, name the exact affected release, use a distinct prior target only for rollback, keep evidence/policy/review/invalidation references sorted and unique, require restored-target validation, link a correction notice when required, preserve time order, and keep all governance flags false with `release_ref: null`.

Run both the fixture profile and the actual candidate:

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python tools/validators/release/validate_rollback_card.py \
  <path-to-actual-candidate.json>

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

Then run the generic synthetic mechanics check:

```bash
python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal
```

Expected current generic result: eight tests. The hosted workflow currently adds Hazards-specific tests; neither result proves Fauna integration.

Shared helper limits:

- `--report` accepts a caller-selected path outside the synthetic workspace;
- correction and invalidation records use atomic replacement, so colliding scenario IDs can replace synthetic files;
- the report's append-only flag does not prove collision-safe append-only history; and
- the helper does not resolve evidence, execute policy, authenticate reviewers, verify signatures, contact external systems, mutate production aliases, invalidate real consumers, or read back recovery.

[Back to top](#top)

---

<a id="prior-target-safety"></a>

## Prior target safety

A prior release is a candidate, not a trusted backup. Recheck:

- immutable distinct identity and digests;
- current EvidenceRef-to-EvidenceBundle support;
- source role, product version, taxonomy, native identity, and ambiguity;
- rights, approved purpose, attribution, and access class;
- sensitivity, public/restricted separation, and geoprivacy transform support;
- observation/source/retrieval/release/correction time and geography bindings;
- current policy and accountable review;
- API, map, Evidence Drawer, Focus Mode, export, cache, index, graph, and downstream compatibility;
- correction/public notice; and
- independent governed read-back.

Any unresolved item yields `HOLD` or withdrawal. Never restore exact or reconstructable sensitive detail merely because it existed in an older release.

[Back to top](#top)

---

<a id="invalidation-and-cross-lane-impact"></a>

## Invalidation and cross-lane impact

Inventory all shared invalidation classes without executing them:

```text
API_CACHE
CDN
TILES
CATALOG
TRIPLETS
SEARCH_INDEX
VECTOR_INDEX
AI_CACHE
DOWNSTREAM_DERIVATIVES
```

For each class, identify the implementation, expected action, verification/read-back, failure posture, and owner role. Include species pages, Evidence Drawer, Focus Mode, exports/offline bundles, Habitat–Fauna derivatives, and any sibling domain that inherited the affected support. Each sibling lane requires its own accountable decision.

A hidden layer, popup change, client filter, or prompt change is not containment when sensitive bytes remain in a public carrier.

[Back to top](#top)

---

<a id="review-handoff"></a>

## Review handoff

An illustrative packet—not a schema or authority object—should include:

```yaml
fauna_rollback_handoff:
  repository_ref: <exact-commit>
  affected_release_ref: <exact-release-ref-or-UNKNOWN>
  affected_manifest_digest: <sha256-or-UNKNOWN>
  public_safe_defect_summary: <no-sensitive-detail>
  work_state: <REVIEW_HANDOFF_READY|HOLD|ERROR|NO_ACTION>
  proposed_path: <FORWARD_CORRECTION|ROLLBACK_CANDIDATE|WITHDRAWAL_CANDIDATE|HOLD|ERROR>
  rollback_card:
    path: <candidate-path-or-NOT_APPLICABLE>
    digest: <sha256-or-UNKNOWN>
    disposition: <ROLLBACK_CANDIDATE|WITHDRAWAL_CANDIDATE|HOLD|ERROR|NOT_APPLICABLE>
  target_checks:
    evidence: <PASS|FAIL|NOT_RUN>
    rights: <PASS|FAIL|NOT_RUN>
    sensitivity: <PASS|FAIL|NOT_RUN>
    taxonomy: <PASS|FAIL|NOT_RUN>
    policy: <PASS|FAIL|NOT_RUN>
    review: <PASS|FAIL|NOT_RUN>
  commands_run: []
  results: []
  invalidations: []
  cross_lane_impacts: []
  blockers: []
  requested_review_roles: []
  non_effects:
    containment_executed: false
    source_activated_or_withdrawn: false
    lifecycle_written: false
    rollback_executed: false
    public_state_mutated: false
    release_authorized: false
    deployment_authorized: false
    promotion_authorized: false
    publication_authorized: false
```

Protected locations, private review text, credentials, secret URLs, vulnerable-source details, or unreviewed source excerpts do not belong in the packet.

[Back to top](#top)

---

<a id="operational-graduation"></a>

## Operational graduation

Operational Fauna rollback remains held until one exact affected release has:

- accepted affected/target release, manifest, alias, correction, rollback, receipt, and read-back contracts;
- authenticated Fauna, taxonomy, source-rights, sensitivity/geoprivacy, evidence, policy, correction, release, operations, security, and independent-review roles;
- current evidence, source role, rights, taxonomy, time, geography, sensitivity, policy, review, and target safety;
- public-safe synthetic Fauna positive and negative fixtures and direct executable tests;
- an accepted production plan/apply operator with no-write planning, safe paths, target/digest checks, policy/review verification, idempotency, concurrency control, collision-safe persistence, confined outputs, recovery, and negative tests;
- least-privilege invalidation adapters, execution receipt, monitoring, and correction behavior; and
- independent governed API, map, Evidence Drawer, Focus Mode, export, cache, catalog, search, vector, and cross-lane read-back.

No score, deadline, green workflow, or feature value compensates for a missing non-compensable gate.

The smallest useful next implementation is a public-safe no-network Fauna integrated rehearsal that reuses the shared candidate profile/helper and adds domain-specific target, taxonomy, sensitivity, and downstream-consumer assertions.

[Back to top](#top)

---

<a id="maintenance-and-document-rollback"></a>

## Maintenance and document rollback

Update this runbook when the shared RollbackCard profile, helper, write boundary, tests, hosted workflow, Fauna test/candidate/release/proof/receipt/policy/sensitivity/taxonomy lanes, operational executor, invalidation, monitoring, or read-back maturity changes.

For a documentation change:

1. freeze target bytes, current `main`, and same-path work;
2. review the complete diff for unsupported claims or sensitive-detail leakage;
3. check metadata, one H1, anchors, fences, tables, links, and final newline;
4. verify every named path and command;
5. run candidate, fixture, validator, generic rehearsal, metadata, document-graph, link, and domain checks when available;
6. classify hosted checks at the exact head; and
7. keep review, merge, rollback authorization, execution, release, deployment, promotion, and publication separate.

If abandoned before merge, close the draft and remove only its task-owned branch. After an authorized merge, use a reviewed revert or smaller forward correction. Documentation rollback does not reverse source, evidence, policy, deployed, public, or wildlife-management state.

## Related surfaces

- [Fauna runbook index](README.md)
- [Fauna rollback drill](ROLLBACK_DRILL.md)
- [Fauna sensitive-occurrence review](SENSITIVE_OCCURRENCE_REVIEW.md)
- [Fauna domain boundary](../../domains/fauna/README.md)
- [Fauna sensitivity doctrine](../../domains/fauna/SENSITIVITY.md)
- [Fauna policy documentation](../../domains/fauna/POLICY.md)
- [Shared rollback rehearsal](../rollback-rehearsal.md)
- [`RollbackCard` contract](../../../contracts/release/rollback_card.md)
- [`RollbackCard` schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Shared validator](../../../tools/validators/release/validate_rollback_card.py)
- [Shared helper](../../../tools/release/rollback_apply.py)
- [Generic rehearsal tests](../../../tests/release/test_synthetic_rollback_rehearsal.py)
- [Hosted rollback workflow](../../../.github/workflows/rollback-drill.yml)
- [Fauna rollback decision lane](../../../release/rollback/fauna/README.md)
- [Fauna data-plane rollback lane](../../../data/rollback/fauna/README.md)
- [Fauna rollback test lane](../../../tests/domains/fauna/release/rollback/README.md)

[Back to top](#top)
