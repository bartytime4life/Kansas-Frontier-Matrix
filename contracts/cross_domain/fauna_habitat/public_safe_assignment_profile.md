<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/cross-domain/fauna-habitat/public-safe-assignment-profile
title: Fauna–Habitat Public-Safe Assignment Candidate Profile
type: contract; cross-domain assessment profile
version: v0.2.0
status: proposed; repository-grounded; fixture-first; no-network; non-authoritative
owners: NEEDS VERIFICATION — Fauna, Habitat, cross-domain, evidence, sensitivity, and validation stewards
created: 2026-08-14
updated: 2026-09-08
policy_label: repository-facing; public-safe; sensitivity-aware; non-publisher
owning_root: contracts/
current_path: contracts/cross_domain/fauna_habitat/public_safe_assignment_profile.md
responsibility: Define pair-specific meaning and finite outcomes for a synthetic Fauna-to-Habitat assignment candidate without creating relationship truth, policy approval, release, or publication authority.
truth_posture: cite-or-abstain; source inspection is not runtime, review, or publication evidence
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@03138e81f19b801cf6d16d767a4c0e01ab36d717
prior_blob: 6e1e977da9086ef35d5ce3ba04865e0f8bb12215
related:
  - ../../joins/cross_lane_join_assessment.md
  - ../../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json
  - ../../../tools/joins/join_candidates.py
  - ../../../tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py
  - ../../../fixtures/contracts/v1/joins/fauna_habitat_public_safe_assignment/cases.json
  - ../../../tests/cross_domain/fauna_habitat/test_public_safe_assignment.py
  - ../../../.github/workflows/fauna-habitat-public-safe-assignment.yml
  - ../../../control_plane/domain_lane_register.yaml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-habitat-fauna-thin-slice.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "v0.2.0 reconciles existing behavior and repairs relative references; the machine schema, validator, fixtures, source-role rules, and authority boundaries are unchanged."
  - "Pair PASS/FAIL validates a report; decision.validator_outcome preserves ALLOW/DENY/ABSTAIN/ERROR inside that report. Neither axis creates public-use authority."
  - "No coordinate or geometry bytes, live source, lifecycle write, EvidenceBundle creation, policy decision, review decision, release decision, public route, or publication is in scope."
[/KFM_META_BLOCK_V2] -->

# Fauna–Habitat Public-Safe Assignment Candidate Profile

## Status and purpose

**CONFIRMED source implementation / PROPOSED profile.** The repository contains a
pair-specific validator, a ten-case synthetic fixture matrix, seven focused test
functions, and a dedicated workflow. The earlier statement that the pair
validator was absent is superseded by this bounded inventory. Their presence is
not proof that this revision's tests ran or that the full Habitat–Fauna thin slice
is operational.

The profile checks whether a synthetic Fauna occurrence reference and a synthetic
Habitat patch reference can form a **review candidate**, using declarations of
public safety, generalization, evidence, source role, cell identity, and time.
It does not establish an occurrence, actual habitat assignment, ecological
relationship, EvidenceBundle, policy permission, review approval, release, or
public claim. `PUBLIC_SAFE` and `GENERALIZED` are input declarations, not the
results of a geoprivacy transform or an independent sensitivity assessment.

### Current implementation bindings

| Responsibility | Inspected surface | Boundary |
|---|---|---|
| Generic semantics | [CrossLaneJoinAssessment](../../joins/cross_lane_join_assessment.md) | Shared identity, source-role preservation, finite decisions, and non-publisher rules. |
| Machine shape | [Shared schema](../../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json) | Closed generic assessment; no second pair schema is introduced. |
| Generic evaluation | [Join helper](../../../tools/joins/join_candidates.py) | Recomputes identity and decisions over synthetic metadata. |
| Pair evaluation | [Pair validator](../../../tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py) | Runs generic validation first, then the rules below. |
| Synthetic examples | [Pair fixture matrix](../../../fixtures/contracts/v1/joins/fauna_habitat_public_safe_assignment/cases.json) | Ten declared cases; not released occurrence or habitat records. |
| Regression evidence | [Focused tests](../../../tests/cross_domain/fauna_habitat/test_public_safe_assignment.py) | Seven source-defined tests; execution must be reported separately. |
| Orchestration | [Dedicated workflow](../../../.github/workflows/fauna-habitat-public-safe-assignment.yml) | Generic and pair checks plus historical/current receipt integrity, not approval. |

## Source provenance

The original proposal lineage is retained below. Its individual source locators
are historical attribution, not a claim that every original document was
re-audited for this edition:

- `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, Part II, `KFM-IDX-APP-002` — start with a synthetic non-sensitive occurrence and a sensitive occurrence; exact sensitive geometry must fail closed.
- `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, `KFM-P1-IDEA-0071` — test sensitivity, habitat assignment, source roles, evidence presentation, and redacted output without live-source activation.
- `kfm_encyclopedia.pdf`, page 11 — relate one non-sensitive occurrence to one habitat patch while retaining generalized public geometry and documented redaction behavior.
- `KFM_Living_Compass_Working_Edition_1.0`, Trail 13 Mission 3 and Trails 5/20 — prefer a small complete, synthetic, no-network proof and leave release/publication outside the implementation slice.

The Google Drive *KFM Habitat + Fauna Thin-Slice Extended Pro Blueprint*
(`1KU3Z_KkqbKAkv3E7oyulTAQlN4f1Gz5w`, 2026-04-21, pp. 4–6) describes a broader
proposed point-to-raster assignment and governed delivery path. The current
metadata-only profile does **not** implement that raster sampling or end-to-end
publication path. The Notion *KFM Hourly Fauna Domain Builder v1.0*
(`3caa9202-1bf6-811b-8926-dc0010d67672`, sections 5–8) preserves the distinction
between habitat assignment and Fauna truth and treats generalized geometry as
insufficient for release. These sources are lineage and coordination; pinned
GitHub implementation governs current behavior.

The [unassigned Habitat–Fauna ADR](../../../docs/adr/ADR-habitat-fauna-thin-slice.md)
remains effectively **proposed**, not accepted. Its older implementation snapshot
does not negate the files above, and this update does not adopt its broader
proof, stewardship, or release design.

## Directory Rules basis

Accepted [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../../docs/doctrine/directory-rules.md).
This is a same-path update inside the established neutral cross-domain seam:
`contracts/` owns meaning; `schemas/` owns machine shape; `tools/` owns validation;
`tests/` and `fixtures/` own tests and synthetic inputs. Neither participating
domain gains ownership of the other's truth.

The existing `.github/` workflow owns orchestration only. New authoring provenance
uses the existing `data/receipts/generated/` lane. There is no new root, duplicate
schema, policy, registry, proof, release, or canonical relationship home. The
profile remains proposed; placement does not establish production acceptance.

## Required endpoint roles

| Side | Required domain | Permitted fixture meaning |
|---|---|---|
| Left | `fauna` | A synthetic occurrence **reference**, not occurrence truth. |
| Right | `habitat` | A synthetic habitat-patch **reference**, not habitat truth. |
| Output | `CANDIDATE_RELATION` | Reviewable candidate only; never a canonical join. |

Each endpoint carries its own `source_descriptor_ref`, `source_role`,
`evidence_ref`, `sensitivity`, `geometry_precision`, `living_person`, and
`valid_from`/`valid_to`. The validator checks the supplied assessment; it does not
rewrite either endpoint or resolve its source. The fixture's `OBSERVED` labels
are simulated role declarations, not evidence of actual observations.

### Profile and identity carriage

The assessment retains generic `object_type: CrossLaneJoinAssessment`,
`schema_version: 0.1.0`, and
`profile: kfm.joins.cross-lane-assessment.fixture.v1`. Pair selection uses
`request.relation_profile_ref`, not a replacement root schema or profile.
The outer fixture matrix's
`kfm.joins.fauna-habitat-public-safe-assignment.fixture.v1` label is a different
surface and must not be copied into an assessment's `profile` field.

The generic helper computes `decision.candidate_id` from `request` and
`endpoints`, and `spec_hash` from the full assessment excluding only
`assessment_id` and `spec_hash`. Both use the shared RFC 8785/SHA-256 helper;
`assessment_id` carries the latter digest with its generic prefix. A candidate ID
also exists in a correctly derived negative report. Identity is not permission.
Changing `evaluated_at` can change assessment identity without changing the
request/endpoint candidate identity.

## Pair-specific rules

Generic shape, identity, endpoint-side, interval, evaluation-time, and exact
recomputed-decision checks run first. A generic finding returns pair `FAIL`
immediately; pair-only findings are not added in that case.

| Rule | Existing check | Pair finding on violation |
|---|---|---|
| Relation profile | `kfm:relation-profile:fauna-habitat-public-safe-assignment:v1` exactly | `RELATION_PROFILE_MISMATCH` |
| Predicate | `SPATIAL_TEMPORAL`, not `EXACT_KEY` | `PAIR_PREDICATE_MISMATCH` |
| Tolerance | `temporal_tolerance_seconds == 0` | `PAIR_TEMPORAL_TOLERANCE_MISMATCH` |
| Direction | Left is `fauna`; right is `habitat` | `ENDPOINT_DOMAIN_MISMATCH` at the affected side |
| Reference posture | Both endpoints' object, source-descriptor, non-null evidence, and spatial-cell references start with `kfm:fixture:` | `NON_FIXTURE_REF_DENIED` |
| Living-person state | Both values are explicitly `false` | `LIVING_PERSON_STATE_DENIED` |
| Accepted `ALLOW` | `JOIN_CANDIDATE`, `matched: true`; both endpoints `PUBLIC_SAFE`, `GENERALIZED`, and evidence-bearing | `ALLOW_CANDIDATE_STATE_INVALID`, `ALLOW_SENSITIVITY_NOT_PUBLIC_SAFE`, `ALLOW_GEOMETRY_NOT_GENERALIZED`, or `ALLOW_EVIDENCE_REF_MISSING` |
| Output boundary | `CANDIDATE_RELATION` and every effect false | `ALLOW_OUTPUT_ROLE_INVALID` or `ALLOW_EFFECTS_NOT_ALL_FALSE`; the generic schema also constrains these fields |

Reference-prefix checks cover the eight endpoint fields above; they are not a
resolver, suffix/type authentication, or a guarantee that arbitrary text is safe.
The pair validator does not apply that prefix test to `request_id` or `join_key`.
Do not place sensitive or real source identifiers inside supposedly synthetic
strings. Unknown extra geometry fields are rejected by the shared closed schema;
no geometry is inspected, generalized, or redacted by this validator.

A null `evidence_ref` is permitted to represent incomplete support. It normally
produces the generic missing-evidence abstention, but a higher-priority dependency
or privacy/sensitivity reason can take precedence. It never permits an accepted
`ALLOW`. Likewise, a coherent restricted/exact **metadata denial report** may
pass report validation without allowing the underlying join or any geometry.

### Spatial and temporal meaning

`SPATIAL_TEMPORAL` compares equal, non-null `spatial_cell_ref` strings and
explicit timezone-aware intervals. It does not compute a spatial intersection,
point-in-polygon relation, raster class, distance, or habitat suitability.
The fixed generic `sql_database: IN_MEMORY_SQLITE` declaration is not evidence
that this pair executes SQL; the helper's SQL branch belongs to `EXACT_KEY`.

Each interval must have `valid_from < valid_to`, and `evaluated_at` must be at or
after both interval ends. This is declared-time coherence, not a current-clock
or freshness check. The fixture's 2027 evaluation timestamp is synthetic.

At this pair's zero tolerance, genuine interval overlap may match. Intervals that
only touch at one endpoint produce `TEMPORAL_BOUNDARY_AMBIGUOUS` and
`ABSTAIN / NO_JOIN_CANDIDATE` when no higher-priority trust reason applies.
The profile does not invent closed-interval semantics. Different cells or
non-overlapping intervals produce `JOIN_PREDICATE_NOT_SATISFIED` under the same
precedence condition. Neither condition changes endpoint identity or time values.

### Source roles, sensitivity, and dependencies

The generic helper preserves both input roles and uses the strictest endpoint
sensitivity. **Every unequal source-role vector** requires compatibility review,
not only modeled-versus-observed inputs. Equal roles may continue to candidate
checks; equality does not turn modeled, aggregate, regulatory, administrative,
candidate, or synthetic support into observation truth.

The [domain-lane register](../../../control_plane/domain_lane_register.yaml) is a
conservative alias/dependency projection, not domain identity authority. A
missing or invalid projection produces generic `ERROR / VALIDATOR_SYSTEM_ERROR`.
For this correctly ordered distinct-domain pair, generic precedence is dependency
error, living-person or blocked sensitivity denial, missing-evidence abstention,
restricted-sensitivity review, then applicable alias/time/predicate/role review,
then `ALLOW`. Detailed generic rules remain in the shared contract. An input with
`living_person: true` also fails the pair's unconditional rule even when its
embedded generic denial is correct.

## Finite outcomes

**Two result axes must be read separately.** Pair `ValidationResult.status` is
`PASS` or `FAIL`. The embedded `decision.validator_outcome` is `ALLOW`, `DENY`,
`ABSTAIN`, or `ERROR`; `decision.status` explains that decision. Neither axis uses
`ANSWER` or `HOLD` in this profile.

| Pair result | Embedded decision | Meaning |
|---|---|---|
| `PASS`, no findings | `ALLOW / JOIN_CANDIDATE` | A coherent synthetic public-safe candidate for later human/evidence/policy review only. |
| `PASS`, no findings | `DENY`, `ABSTAIN`, or `ERROR` | The negative report is internally coherent and pair-conformant; the join is not allowed. |
| `FAIL` | Any stored value, including `ALLOW` | The report is invalid for this profile. Never trust its stored `ALLOW` as an accepted candidate. |

Examples of coherent negative decisions include missing evidence
(`EVIDENCE_REF_MISSING`), unequal roles (`SOURCE_ROLE_REVIEW_REQUIRED`, reason
`SOURCE_ROLE_CONFLICT`), restricted generalized metadata
(`SENSITIVITY_REVIEW_REQUIRED`), restricted exact metadata or prohibited
sensitivity (`GEOMETRY_PRECISION_BLOCKED`), and unavailable declared dependencies
(`VALIDATOR_SYSTEM_ERROR`). A literal `matched: true` is not permission: a
predicate match can coexist with a negative trust decision.

Findings are sorted by `(code, path)`. The same code at two endpoint paths remains
two findings; swapped domain order is not one collapsed finding. File-read
failures use pair `FAIL` with `INPUT_JSON_INVALID` or
`INPUT_OR_DEPENDENCY_ERROR`. Generic-schema and identity findings retain their
codes. Import-time dependency failures are not guaranteed to become a finite
report; this documentation does not claim a universal exception boundary.

## Non-effects

This profile does not activate or retrieve sources; ingest, transform, generalize,
or emit geometry; resolve EvidenceRef to EvidenceBundle; evaluate live policy;
record reviewer approval; or write RAW, WORK/QUARANTINE, PROCESSED,
CATALOG/TRIPLET, or PUBLISHED state.

The seven decision effects remain schema-fixed false: `lifecycle_write`,
`evidence_bundle_created`, `policy_decision_created`, `review_decision_created`,
`release_decision_created`, `publication`, and `public_use_authorized`.
The governance envelope remains fixture-only, dry-run, and no-network with its
identity, relationship-truth, policy, review, release, and publication authorities
false. A schema check or generated-work receipt does not replace any of those
independent decisions.

No proof pack, PromotionDecision, ReleaseManifest, correction notice, rollback
card, public route, MapLibre layer, Evidence Drawer response, Focus Mode answer,
export, deployment, or publication is authorized. Public consumers must still
use separately governed APIs or released public-safe artifacts, never internal
or unreleased candidate stores. A habitat association does not prove occurrence,
occupancy, habitat preference, suitability, or absence.

## Validation and coverage

The committed pair matrix declares five conforming reports (one `ALLOW`, one
`DENY`, three `ABSTAIN`) and five invalid reports. Its invalid cases cover exact
precision on an `ALLOW`, swapped domains, wrong relation profile, non-fixture
object reference, and a publication-effect overclaim. The seven focused tests
cover this matrix, identity repeatability, those boundaries, and source/fixture
scans. These are inventory statements, not current-run pass claims.

The ten cases are not exhaustive: they do not directly cover a generic `ERROR`,
nonzero pair tolerance, temporal boundary touch, or every source-role pair.
Generic regressions provide adjacent coverage; their presence must not be
misreported as execution of missing pair cases.

From a dependency-ready repository root:

```bash
python tools/joins/join_candidates.py --fixtures
python tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py --fixtures
python -m pytest tests/joins/test_join_candidates.py tests/joins/test_cross_lane_*.py tests/cross_domain/fauna_habitat/test_public_safe_assignment.py -q --strict-config --strict-markers
```

The fixture matrix contains `AUTO` identity placeholders and an unmaterialized
base decision. It is not a standalone assessment: use the fixture runner, which
rederives and seals cases before comparison. Report each case's declared
validation result, ordered finding codes, embedded outcome, and decision status.

The pair file CLI returns exit `0` for conforming reports, including coherent
negative decisions, and exit `1` for validation failure. Its output reports
validation findings, not an authorization result. Use file mode and `--fixtures`
separately: unlike the stricter generic CLI, the current pair CLI prioritizes
fixture mode when both are supplied. Do not infer that explicitly supplied files
were checked in that mixed invocation.

## Acceptance and rollback

Before integration, run the focused pair and generic suites, exact fixture
replay, current receipt integrity, and historical receipt replay in the supported
environment at the exact head; check affected links and workflow configuration.
Record unrun, failed, inherited, and hosted results separately. Independent
review is still required; green CI does not accept the proposed profile or
establish source, renderer, release, or publication readiness.

The workflow preserves the existing historical receipt and validates its six
artifact bindings at exact pre-edit snapshot
`03138e81f19b801cf6d16d767a4c0e01ab36d717`. A separate current receipt covers this
document and its workflow companion. This avoids rewriting past authorship to
follow successor bytes. The broader domain ADR and source-blueprint graduation
remain outside this revision.

Rollback of **this edition** is a reviewed revert of the contract-currentness,
workflow-replay, and new-receipt change only. Restore the prior contract blob
`6e1e977da9086ef35d5ce3ba04865e0f8bb12215` and prior workflow; preserve the existing
validator, schema, fixtures, tests, and historical receipt. No source, lifecycle,
public artifact, cache, or release state needs rollback from this change.
