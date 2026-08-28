<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-cross-domain-joins-readme
title: tools/validators/cross-domain-joins/ — Generic Cross-Domain Join Validator Boundary
type: readme; validator-lane; cross-domain-join-validation; relation-claim-validation; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only; direct-executable-unestablished; direct-tests-unestablished; dedicated-workflow-unestablished; aggregate-registration-absent; four-invariants-confirmed; pair-specific-routing-confirmed; contract-and-schema-placement-conflicted; no-network-by-default; fail-closed; release-gated
owners: OWNER_TBD — Cross-domain architecture · Join · Contract · Schema · Validator · Identity · Geometry · Temporal · Source · Evidence · Rights/Sensitivity · Policy · Domain · Release · Security · CI · Docs stewards
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1
policy_label: repository-facing; cross-domain; joins; relations; crosswalks; ownership-preserving; source-role-preserving; sensitivity-monotonic; evidence-bound; time-aware; spatially-bounded; correction-aware; deterministic; fail-closed
owning_root: tools/
current_path: tools/validators/cross-domain-joins/README.md
responsibility: Validate generic mechanics and doctrine invariants for binary or n-ary relationship candidates spanning two or more independently governed domains, while delegating domain meaning, pair-specific rules, schemas, policy, proof, release, and public delivery to their owning roots.
truth_posture: >
  CONFIRMED target v0.1 and prior blob; direct lane README-only in bounded search; representative executable, dedicated test,
  fixture and workflow paths absent; shared five-entry aggregate excludes this lane; cross-lane is a compatibility bridge;
  joins is the pair-specific parent; Agriculture-Soil and Person-Parcel child READMEs and a top-level Habitat-Fauna lane exist;
  four invariants are doctrine; joins/crosswalk contract homes and joins/relations schema homes overlap; one permissive
  Habitat-Fauna join schema exists; tests/cross_domain is placement-conflicted and README-oriented / PROPOSED immutable packet,
  deterministic report, XDJ reason codes, fixtures, CI, migration and rollback / UNKNOWN runtime consumers and pass results
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: "ebdf9332c096facff23ff4379b576b6ae01c72b4"
  prior_blob: b85f6871a12173c83da6f4bbe410abb1ab8a9905
  cross_lane_relations_blob: 15ca8eb8c7790d2962b710097196ed9b1eea0f79
  multi_domain_placement_blob: 12ba496e89b1a2bb5e1009080e4d611c7fb369d0
  source_role_anti_collapse_blob: b8509017b0175fdd01da3fc47db9acca10ee0bc9
  shared_kernel_blob: 4b6e37b446c7f63bee02a966c8c0a0c8d9d05a37
  trust_membrane_blob: 968ee79eef37138148eab9fe505e9491dbe8ccd4
  joins_validator_index_blob: c67c66136b3c16857f1957f5d72ff61f6235372d
  cross_lane_bridge_blob: f6763f2dbb436c05e6ab40cc1bd3f79f614683e1
  joins_contract_index_blob: e31c295b48b41a4da3e861d4536a07f2bbe1660e
  crosswalk_contract_index_blob: 7dd131c6b6b5339eb6e433940d7ace169a350dbc
  joins_schema_index_blob: 6b8ff3f4c82a7ab256b86d31c33c27d0cf0cf959
  relations_schema_index_blob: 28678976c1cdaa215fc824627baa476d17dd3bbf
  habitat_fauna_schema_blob: 5db6f1b09b2ebafbeb788ab177a8a77b8a31ba6b
  cross_domain_tests_blob: cdf514e6a972be821f5f10d27d504aa3a5d03131
  aggregate_runner_blob: 3375cce172631dc3675cf2e46bb7788d273ff425
  validator_suite_blob: 7651f0571ba8f879819b197155d160c08f9fe7ac
related:
  - ../README.md
  - ../_common/README.md
  - ../joins/README.md
  - ../cross-lane/README.md
  - ../identity/README.md
  - ../geometry/README.md
  - ../evidence/README.md
  - ../evidence_bundle/README.md
  - ../joins/agriculture-soil/README.md
  - ../joins/person-parcel/README.md
  - ../habitat-fauna/README.md
  - ../../../docs/architecture/cross-domain/cross-lane-relations.md
  - ../../../docs/architecture/cross-domain/multi-domain-placement.md
  - ../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../docs/architecture/cross-domain/shared-kernel.md
  - ../../../docs/architecture/cross-domain/trust-membrane.md
  - ../../../contracts/joins/README.md
  - ../../../contracts/crosswalks/README.md
  - ../../../schemas/contracts/v1/joins/README.md
  - ../../../schemas/contracts/v1/relations/README.md
  - ../../../schemas/contracts/v1/joins/habitat-fauna-join.schema.json
  - ../../../tests/cross_domain/README.md
  - ../../../.github/workflows/validator-suite.yml
notes:
  - Documentation-only update paired with a generated provenance receipt.
  - No executable, schema, contract, policy, fixture, test, workflow, data, proof, release record, route, or public artifact behavior changes.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Generic Cross-Domain Join Validator Boundary

`tools/validators/cross-domain-joins/`

> Validate relationship claims spanning independently governed domains without merging their authority, laundering sensitivity, collapsing source roles, treating proximity as identity, or turning a successful join into truth, proof, permission, release approval, or publication.

> [!IMPORTANT]
> No working direct executable, dedicated test lane, fixture lane, or dedicated workflow was established for this directory. The only concrete join schema inspected is an empty permissive scaffold, and current contract/schema/test placement remains conflicted.

**Quick links:** [Purpose](#purpose) · [Status](#status) · [Placement](#placement) · [Topology](#topology) · [Packet](#packet) · [Four invariants](#four-invariants) · [Relation validity](#relation-validity) · [Identity and cardinality](#identity) · [Time and space](#time-space) · [Sensitivity and evidence](#sensitivity-evidence) · [Policy and public surfaces](#policy-public) · [Conflict register](#conflicts) · [Report](#report) · [Outcomes](#outcomes) · [Security](#security) · [Tests and CI](#tests-ci) · [Implementation](#implementation) · [Definition of done](#done) · [Migration and rollback](#rollback) · [Open verification](#open) · [Evidence ledger](#ledger)

---

<a id="purpose"></a>

## Purpose

This lane answers:

> Does a declared binary or n-ary relation candidate preserve every participating domain's ownership, object identity, source role, sensitivity, evidence support, temporal and spatial scope, uncertainty, lifecycle posture, policy/review state, release linkage, correction lineage, and public-exposure limits under an accepted relation profile?

A `PASS` proves only the configured checks for the exact packet, profiles, dependency results, and hashes named in the report. It does not prove endpoint truth, relation truth, identity, policy permission, release, or public safety.

---

<a id="status"></a>

## Status and evidence boundary

**Snapshot:** `main@ebdf9332c096facff23ff4379b576b6ae01c72b4`
**Prior target blob:** `b85f6871a12173c83da6f4bbe410abb1ab8a9905`

| Surface | Status | Safe conclusion |
|---|---|---|
| Direct lane | **CONFIRMED README-only in bounded search** | Do not claim executable behavior. |
| Direct entrypoint | **Not established** | CLI, registry id, exits and report emission remain proposed. |
| Dedicated tests/fixtures/workflow | **Not established at tested paths** | No direct coverage or required check is claimed. |
| Shared aggregate | **Five entrypoints; this lane absent** | `make schemas` does not prove join validation. |
| Four invariants | **CONFIRMED doctrine spine** | Mandatory minimum for every cross-domain relation. |
| `cross-lane/` | **Compatibility bridge** | Must not duplicate logic. |
| `joins/` | **Pair-specific parent index** | Pair lanes strengthen but cannot weaken generic rules. |
| Contracts | **`joins/` and `crosswalks/` overlap** | Semantic authority must be profile-pinned. |
| Schemas | **`joins/` and `relations/` overlap** | Machine authority is unresolved. |
| Concrete join schema | **Permissive Habitat-Fauna scaffold** | Shape pass is not semantic validation. |
| `tests/cross_domain/` | **Surviving, placement-conflicted parent** | README presence does not establish executable proof. |
| Runtime use and pass results | **UNKNOWN** | No deployment or production claim. |

Bounded absence is not historical or exhaustive proof.

---

<a id="placement"></a>

## Directory Rules and authority

| Responsibility | Owning home |
|---|---|
| Generic cross-domain mechanics | `tools/validators/cross-domain-joins/` |
| Pair-specific routing and stricter checks | `tools/validators/joins/` and accepted named lanes |
| Naming compatibility | `tools/validators/cross-lane/` |
| Domain object meaning | Each domain's doctrine and contracts |
| Join/relation/crosswalk meaning | Accepted contract profile under `contracts/` |
| Machine shape | Accepted schema profile under `schemas/contracts/v1/` |
| Source identity/role | Source contracts and `data/registry/sources/` |
| Evidence/proof | `data/proofs/` |
| Receipts | `data/receipts/` |
| Policy/admissibility | `policy/` |
| Lifecycle data | Governed `data/` phase roots |
| Release/correction/rollback | `release/` |
| Tests and fixtures | `tests/` and `fixtures/` |
| Public delivery | Governed runtime/API/UI surfaces |

The Domain Placement Law keeps this generic validator under the lowest common responsibility root without assigning it to one participating domain. This lane must not become a merged-domain model, semantic contract home, schema home, mapping registry, proof store, policy engine, graph authority, release service, or public API.

---

<a id="topology"></a>

## Validator topology

```text
domain-owned endpoints + accepted relation profile
  -> generic cross-domain validator
       ownership / role / sensitivity / evidence
       identity / cardinality / time / space / uncertainty
       lifecycle / correction / public-boundary checks
  -> pair-specific validator
  -> identity / geometry / evidence / policy / release dependencies
  -> deterministic CrossDomainJoinValidationReport
  -> later promotion or runtime gate
```

Rules:

- Generic mechanics live once in this lane.
- Pair-specific lanes may add constraints but never weaken generic outcomes.
- `cross-lane/` remains a pointer unless an ADR or migration changes the canonical spelling.
- Equivalent top-level pair lanes and `joins/<pair>/` children require explicit routing or migration.
- Domain validators remain authoritative for endpoint semantics.

---

<a id="packet"></a>

## Proposed immutable validation packet

```yaml
packet_version: kfm.cross_domain_join_validation.v1
request_id: req_<stable-id>
join:
  join_id: join_<content-hash>
  relation_type: <accepted-profile-id>
  direction: <directed|symmetric|ordered-nary>
  profile_ref: <immutable-ref>
  profile_hash: <sha256>
endpoints:
  - endpoint_id: left
    domain: <domain-slug>
    object_type: <domain-owned-type>
    object_ref: <immutable-ref>
    object_digest: <sha256>
    source_role: <role>
    sensitivity: <posture>
    evidence_refs: []
relation_assertion:
  method: <identifier|crosswalk|temporal|spatial|derived|reviewed-manual>
  predicate: <controlled-predicate>
  relation_evidence_refs: []
  cardinality: <1:1|1:n|n:1|n:n>
  temporal_scope: <explicit-or-none>
  spatial_profile_ref: <explicit-or-none>
  uncertainty: <explicit>
requested_use:
  audience: <internal|reviewer|restricted|public>
  surface: <catalog|graph|map|api|export|focus|ai|release-review>
dependencies:
  policy_refs: []
  review_refs: []
  release_refs: []
  correction_refs: []
  rollback_refs: []
execution:
  validator_ref: <entrypoint-and-version>
  rule_hash: <sha256>
  network_mode: denied
  timeout_ms: <bounded>
  max_endpoints: <bounded>
```

Missing profile, audience, surface, relation method, predicate, endpoint identity, or required dependency produces a finite negative outcome rather than an inferred default.

---

<a id="four-invariants"></a>

## Four doctrine invariants

| Invariant | Required behavior | Blocking failure |
|---|---|---|
| Ownership preserved | Every endpoint retains its owning domain and identity. | Relation silently rebinds or copies authority. |
| Source role preserved | Each endpoint keeps its admitted role. | Role is dropped, upgraded, averaged, or synthesized. |
| Sensitivity preserved | Effective posture is at least the most restrictive input and may be stricter due to composition risk. | Join downgrades sensitivity or treats aggregation as permission. |
| EvidenceBundle support | Every consequential endpoint and the relation assertion resolve required evidence before public use. | Evidence missing, unresolved, one-sided, stale, or inconsistent. |

All four must pass. None substitutes for another.

---

<a id="relation-validity"></a>

## Endpoint validity is not relation validity

A validator must distinguish:

1. **Endpoint integrity** — each referenced domain object exists, is correctly identified, and preserves domain/source posture.
2. **Association method** — the join key, crosswalk, spatial predicate, temporal rule, or reviewed assertion is declared and allowed.
3. **Predicate support** — evidence supports the connecting claim, not merely the endpoint claims.
4. **Use fitness** — policy, release, correction, and public-surface requirements are satisfied.

A valid left endpoint plus a valid right endpoint does not establish a valid relationship.

Accepted relation methods are profile-controlled. Free-text predicates, implicit SQL joins, geometry proximity, name similarity, or model output do not acquire authority merely because they produce a match.

---

<a id="identity"></a>

## Identity, direction, and cardinality

- Use stable namespace-qualified references; do not copy domain-owned records into the join.
- Preserve direction for directed predicates and canonical endpoint ordering for symmetric predicates.
- Pin crosswalk authority, version, status, confidence, and evidence.
- Record cardinality and enforce pair-specific limits.
- Duplicate rows, self-joins, fan-out explosions, namespace collisions, or ambiguous crosswalks fail closed.
- Spatial coincidence is not identity.
- Similar names are not identity.
- Aggregate membership is not individual membership.
- A relation id is deterministic from accepted profile and canonicalized inputs; it is not proof that the relation is true.

---

<a id="time-space"></a>

## Temporal and spatial compatibility

Time checks must preserve source, observed, valid, retrieval, release, and correction time where material. The validator must not compare unlike time kinds as though equivalent. Non-overlapping validity windows, stale current-status endpoints, uncertain intervals, or missing temporal rules produce `FAIL`, `HOLD`, or `ABSTAIN` according to profile.

Spatial checks must pin CRS, axis order, units, geometry version, predicate, tolerance, resolution, boundary semantics, and transform provenance. Reprojection success does not prove semantic compatibility. Buffering, snapping, centroid use, raster sampling, and nearest-neighbor matching are derivations with explicit uncertainty—not identity operations.

---

<a id="sensitivity-evidence"></a>

## Sensitivity, evidence, rights, and consent

The effective posture is:

```text
most restrictive input
+ relation-specific composition risk
+ requested audience/surface policy
```

A public endpoint joined to a restricted endpoint does not produce a public join. Aggregation, generalization, suppression, or delay lowers exposure only when a governed transform, policy decision, review record, and release path support the result.

Validate separately:

- endpoint EvidenceRefs and EvidenceBundles;
- relation-evidence support;
- source roles and rights;
- consent and revocation where applicable;
- redaction/generalization receipts;
- review and policy decisions;
- release, correction, withdrawal, and rollback references.

Living-person, DNA, private land/title, rare-species, archaeology, cultural, sacred-site, and critical-infrastructure joins fail closed by default.

---

<a id="policy-public"></a>

## Policy, lifecycle, and public surfaces

The validator reports policy dependencies; it does not make policy or release decisions.

A public-bound join must not reference RAW, WORK, QUARANTINE, unresolved candidates, direct canonical stores, private URLs, internal ids, or unreleased proof material. Catalog, graph, map, tile, search, vector index, API, export, screenshot, Focus Mode, and AI outputs are downstream projections—not sovereign truth.

Policy/review/release outcomes are monotonic: a downstream validator may make a result more restrictive, never less restrictive.

Lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move or a validator side effect.

---

<a id="conflicts"></a>

## Conflict register

| Conflict | Current evidence | Safe default |
|---|---|---|
| `cross-domain-joins/` vs `cross-lane/` | Full lane plus compatibility bridge | Implement only in the full lane until migration/ADR. |
| Generic lane vs `joins/` | Generic mechanics plus pair index | Generic first; pair-specific constraints second. |
| Top-level pair lanes vs `joins/<pair>/` | Both patterns exist | Require explicit routing; do not duplicate logic. |
| `contracts/joins/` vs `contracts/crosswalks/` | Both can describe mapping/relationship meaning | Packet pins accepted semantic profile. |
| `schemas/.../joins/` vs `schemas/.../relations/` | Overlapping families | Packet pins accepted schema profile; no local invention. |
| Join schema maturity | Habitat-Fauna scaffold has empty properties and allows extras | Schema pass is insufficient. |
| Cross-domain tests | `tests/cross_domain/` survives, while doctrine prefers topic placement | Do not create another spelling without migration. |
| Outcomes | Doctrine and lanes use overlapping vocabularies | Use profile-pinned mapping; preserve restrictive result. |

This README records conflicts; it does not resolve them.

---

<a id="report"></a>

## Proposed deterministic report

```yaml
report_version: kfm.cross_domain_join_validation_report.v1
report_id: xdj_<content-hash>
join_id: <join-id>
profile_ref: <immutable-ref>
profile_hash: <sha256>
validator_ref: <entrypoint>
validator_version: <version>
rule_hash: <sha256>
input_hashes: {}
overall_outcome: <PASS|WARN|FAIL|HOLD|DENY|ABSTAIN|ERROR|REVIEW_REQUIRED>
findings:
  - finding_id: <stable-id>
    endpoint_ids: []
    outcome: <finite-outcome>
    reason_code: <XDJ_*>
    blocking: true
    dependency_refs: []
    public_safe_message: <bounded-text>
effective_sensitivity: <posture>
source_role_distribution: {}
dependency_results: []
limitations: []
correction_refs: []
rollback_refs: []
```

Identical canonical inputs, profiles, dependency results, rule hash, and validator version should produce byte-stable report content excluding operational timestamps.

Reports must not include secrets, restricted payloads, exact sensitive coordinates, private chain-of-thought, hidden thresholds, private URLs, or public stack traces.

---

<a id="outcomes"></a>

## Finite outcomes and reason codes

| Outcome | Meaning |
|---|---|
| `PASS` | Configured generic checks passed; later gates still apply. |
| `WARN` | Accepted non-blocking limitation. |
| `FAIL` | Deterministic validation defect. |
| `HOLD` | Dependency, placement, review, or profile unresolved. |
| `DENY` | Requested relation/use is disallowed or unsafe. |
| `ABSTAIN` | Support is insufficient to assert the relation. |
| `ERROR` | Validator or dependency failed. |
| `REVIEW_REQUIRED` | Human review is mandatory. |

Proposed reason-code families:

- `XDJ_PROFILE_*` — missing or mismatched profile/rules.
- `XDJ_ENDPOINT_*` — missing, invalid, stale, or wrong-owner endpoint.
- `XDJ_IDENTITY_*` — namespace collision, ambiguous key, fabricated identity.
- `XDJ_ROLE_*` — source-role missing or collapsed.
- `XDJ_SENSITIVITY_*` — downgrade or composition risk.
- `XDJ_EVIDENCE_*` — endpoint or relation evidence missing/unresolved.
- `XDJ_CARDINALITY_*` — duplicate, self-join, or fan-out violation.
- `XDJ_TIME_*` — incompatible time kind/window or stale state.
- `XDJ_SPATIAL_*` — CRS, tolerance, predicate, precision, or reconstruction risk.
- `XDJ_POLICY_*` — rights, consent, policy, review, or release gap.
- `XDJ_LIFECYCLE_*` — internal-stage public reference or gate bypass.
- `XDJ_CORRECTION_*` — stale report, revocation, withdrawal, or rollback gap.
- `XDJ_SECURITY_*` — path, URI, network, secret, or resource violation.
- `XDJ_INTERNAL_ERROR` — bounded operational failure.

Reason-code vocabulary remains proposed until accepted by contract/registry.

---

<a id="security"></a>

## Security and resource posture

- Network denied by default.
- No arbitrary URI dereference or remote crosswalk lookup.
- Treat relation packets, predicates, labels, and excerpts as untrusted input.
- Reject path traversal, symlink escape, credential-bearing URLs, private endpoints, and unsafe redirects.
- Do not execute source content, templates, macros, expressions, SQL, code, or prompt-like instructions.
- Bound endpoints, edges, fan-out, bytes, recursion, geometry complexity, regex work, and runtime.
- Do not log restricted endpoint values or exact sensitive geometry.
- Dependency failures and resource exhaustion never default to `PASS`.

---

<a id="tests-ci"></a>

## Tests, fixtures, and CI

No dedicated generic executable test lane or workflow was established. A future no-network corpus should include:

- valid binary and n-ary relations;
- missing/incorrect ownership;
- role collapse;
- sensitivity downgrade and composition risk;
- endpoint evidence present but relation evidence absent;
- unresolved evidence on one side;
- ambiguous crosswalk and namespace collision;
- cardinality/fan-out/self-join violations;
- temporal mismatch and stale endpoint;
- CRS/tolerance/precision errors;
- modeled/aggregate/proximity-as-truth failures;
- living-person, consent, rare-species, archaeology, land/title, and infrastructure denial;
- unreleased/public-boundary violations;
- correction, revocation, withdrawal, and rollback invalidation;
- deterministic reruns and resource-limit failures.

Anti-tautology controls require nonempty valid and invalid sets, intended failure reasons, pinned profiles, and explicit proof that permissive schema success is not semantic coverage.

A future CI check should execute generic and pair-specific profiles, preserve negative-outcome monotonicity, emit a safe structured report, fail on registry/profile drift, and remain separate from release approval. Workflow existence, green status, branch protection, and production enforcement are separate facts.

---

<a id="implementation"></a>

## Smallest sound implementation sequence

1. Settle generic spelling, join/relation/crosswalk taxonomy, schema homes, test placement, and outcomes by ADR or reviewed migration.
2. Define generic packet/report contracts and pair-specific profile registration.
3. Implement closed schemas and nonempty positive/negative fixtures.
4. Implement deterministic identity, time, geometry, evidence, policy, and release adapters.
5. Implement one generic entrypoint and registry id with no-network defaults.
6. Migrate pair-specific lanes to reuse generic checks.
7. Add dedicated CI and safe report artifacts.
8. Prove correction, withdrawal, consent revocation, and rollback.

Each step should be a small reversible PR.

---

<a id="done"></a>

## Definition of done

- [ ] Owners and CODEOWNERS accepted.
- [ ] Generic spelling and pair-routing model accepted.
- [ ] Join/relation/crosswalk contract and schema taxonomy accepted.
- [ ] Cross-domain test placement accepted.
- [ ] Generic packet/report contracts and closed schemas implemented.
- [ ] Pair-specific profile registry implemented.
- [ ] One executable entrypoint and registry id confirmed.
- [ ] Identity, time, geometry, evidence, policy, review, and release adapters tested.
- [ ] Valid and invalid fixtures are nonempty.
- [ ] Pair suites reuse generic invariants.
- [ ] No-network and resource controls enforced.
- [ ] Reports are deterministic and public-safe.
- [ ] CI significance is verified.
- [ ] Corrections, consent revocation, source withdrawal, and rollback invalidate joins.
- [ ] Duplicate paths have migration/deprecation notices.
- [ ] Rollback is exercised.
- [ ] Documentation matches behavior.

---

<a id="rollback"></a>

## Migration, correction, and rollback

Known drift includes lane spellings, pair-lane placement, contracts `joins/` versus `crosswalks/`, schemas `joins/` versus `relations/`, hyphen/underscore/order variants, and `tests/cross_domain/` versus topic placement.

Canonicalization requires an accepted ADR or migration note, explicit source/destination paths, no steady-state duplicate implementation, compatibility pointers where justified, shared-corpus comparison, correction and rollback targets, and retirement dates.

A validation report becomes stale when any endpoint identity/version, domain ownership, source role, sensitivity, rights, consent, evidence, relation profile, join key, crosswalk, method, geometry, time interval, policy, review, release, correction state, or validator rule changes.

Before merge, close the draft PR and abandon the branch. After merge, revert the README commit and revert or supersede the generated receipt. No runtime, schema, policy, relation, data, or release rollback is required for this documentation-only change.

---

<a id="open"></a>

## Open verification register

1. Owners and CODEOWNERS.
2. Canonical generic spelling and bridge lifetime.
3. Generic versus pair-specific registry contract.
4. Top-level pair lanes versus `joins/<pair>/`.
5. Join/relation/crosswalk definitions and canonical contract family.
6. Canonical schema family, slug convention, and endpoint order.
7. Cross-domain test and fixture placement.
8. Generic packet and report schemas/home.
9. Outcome and reason-code vocabulary.
10. Canonical executable and registry id.
11. Aggregate/CI integration and required-check significance.
12. Pair-specific profile inventory.
13. Identity/crosswalk authority resolver.
14. Geometry/tolerance and temporal profiles.
15. Evidence and relation-evidence rules.
16. Source-role and sensitivity policy bindings.
17. Consent, rights, cardinality, uncertainty, and conflict handling.
18. Public projection profile.
19. Correction dependency graph and revocation/withdrawal behavior.
20. Runtime consumers, metrics, budgets, and rollback drill.

Unresolved items remain `NEEDS VERIFICATION`, not implementation facts.

---

<a id="ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Target README v0.1 | CONFIRMED | Existing proposed lane | Runtime behavior |
| Cross-lane relation doctrine | CONFIRMED spine | Four invariants | Enforcement |
| Multi-domain placement | CONFIRMED spine | Lowest common root | Final topic naming |
| Source-role anti-collapse | CONFIRMED spine | Roles and deny patterns | Current policy |
| Shared kernel/trust membrane | CONFIRMED spine | Dependency and public boundaries | Deployment |
| `joins/` and pair READMEs | CONFIRMED docs | Pair routing and stricter risks | Executables |
| `cross-lane/` | CONFIRMED bridge | Current canonical pointer | Accepted final spelling |
| `contracts/joins/` and `crosswalks/` | CONFIRMED families | Semantic overlap | Canonical authority |
| `schemas/.../joins/` and `relations/` | CONFIRMED families | Shape overlap | Accepted field-complete schemas |
| Habitat-Fauna schema | CONFIRMED permissive scaffold | Schema immaturity | Semantic validity |
| `tests/cross_domain/` | CONFIRMED conflicted parent | Test-routing posture | Executable tests/CI |
| Shared aggregate and validator workflow | CONFIRMED | Generic lane absent | No other invocation |
| Directory Rules | CONFIRMED doctrine | Placement and authority | Implementation maturity |

---

## Changelog

### v0.2 — 2026-07-16

- Replaced planning language with a commit-pinned repository evidence boundary.
- Recorded the direct lane as README-only and absent from the shared aggregate.
- Clarified generic, pair-specific, and compatibility-bridge responsibilities.
- Exposed contract, schema, pair-lane, and test-placement conflicts.
- Added packet, relation validity, identity/cardinality, time/space, evidence/sensitivity, report, security, test, CI, migration, correction, and rollback contracts.
- Added generated-work provenance receipt requirement.

### v0.1 — 2026-07-07

- Replaced an empty file with the initial four-invariant guide.

<p align="right"><a href="#top">Back to top</a></p>
