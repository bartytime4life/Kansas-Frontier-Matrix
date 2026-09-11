<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/analytical-view-manifest
title: AnalyticalViewManifestCandidate Contract
type: semantic-contract
version: v1.1.0
status: proposed-inactive; repository-grounded; fixture-only; no-network; human-review-hold; non-authoritative
owners: OWNER_TBD — Data contract steward · Analytics steward · Database steward · Validation steward
created: 2026-08-11
updated: 2026-09-08
owning_root: contracts/
policy_label: internal; data; analytics; database-view; materialized-view; manifest; declaration-only
responsibility: Define fixture-only analytical-view identity, definition, upstream, semantic-dependency, validation, materialization, mutation-guard, disclosure, correction, and rollback declarations without creating a view, executing SQL, mutating data, or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED repository bindings and bounded executable behavior / PROPOSED inactive manifest profile / UNKNOWN database portability, accepted dialect and registry policy, runtime consumers, and live enforcement / NEEDS VERIFICATION owners, human review, source and evidence resolution, policy, release, deployment, publication, and public use"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d58c91b5ca5efb915bb21bf8d6945c46faa41e47
  target_blob_before_revision: b4764242ee8e9048dc1ea20e9646c11823010ebc
  inspected_on: 2026-09-08
related:
  - ./README.md
  - ./layer_manifest.md
  - ../governance/query_run_record.md
  - ../ui/view_registry_profile.md
  - ../../schemas/contracts/v1/data/analytical_view_manifest.schema.json
  - ../../fixtures/contracts/v1/data/analytical_view_manifest/cases.json
  - ../../tools/validators/data/validate_analytical_view_manifest.py
  - ../../tests/validators/data/test_validate_analytical_view_manifest.py
  - ../../.github/workflows/analytical-view-manifest.yml
  - ../../data/receipts/generated/genrec-pass18-analytical-view-manifest-20260811.json
  - ../../docs/intake/exploratory/pass-18-analytical-view-manifest-source-map.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, data, analytics, database-view, materialized-view, check-option, deterministic, fixture-only, no-network]
notes:
  - "Implements a dependency-closed adaptation of supplied Pass 18 cards KFM-P18-INV-107 and KFM-P18-INV-311."
  - "v1.1.0 reconciles the semantic documentation with the existing closed schema, 20-case fixture manifest, validator, 10-test module, workflow, source map, and generated receipt on current main."
  - "A passing manifest never creates or updates a database view and never grants query, mutation, refresh, evidence, policy, review, release, deployment, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AnalyticalViewManifestCandidate

> Fixture-only semantic contract for making one database view, materialized view, or equivalent derived view inspectable without executing it or granting it authority.

<p>
  <img alt="Status: proposed inactive" src="https://img.shields.io/badge/status-proposed__inactive-orange">
  <img alt="Profile: fixture only" src="https://img.shields.io/badge/profile-fixture__only-blue">
  <img alt="Network: denied" src="https://img.shields.io/badge/network-denied-red">
  <img alt="Database effects: none" src="https://img.shields.io/badge/database%20effects-none-red">
  <img alt="Review: pending" src="https://img.shields.io/badge/review-pending-yellow">
</p>

## Quick jumps

[Status](#status) · [Scope](#scope) · [Repository binding](#repository-binding) · [Manifest model](#manifest-model) · [View and refresh semantics](#view-and-refresh-semantics) · [Mutation guard](#mutation-and-predicate-guard) · [Outcomes](#finite-outcomes) · [Executable coverage](#executable-coverage) · [Integration](#adjacent-contract-boundaries) · [Gaps](#known-gaps) · [Evidence](#evidence-and-coordination-lineage) · [Validation](#validation) · [Rollback](#acceptance-and-rollback)

---

## Status

| Dimension | Current posture |
|---|---|
| Semantic contract | `PROPOSED_INACTIVE`; documentation profile v1.1.0 |
| Packet schema | `CONFIRMED` repository-present Draft 2020-12 schema; packet `schema_version` is `1.0.0` |
| Fixtures and validator | `CONFIRMED` fixture-only, deterministic, no-network profile |
| Database integration | `ABSENT` from this slice |
| Runtime consumers | `UNKNOWN`; none is established by this contract family |
| Human review | pending |
| Authority | none |

The profile was introduced by [PR #2597](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2597), merged on 2026-08-12. Current repository presence confirms that the profile and companions exist; it does not convert the proposal into an active database contract or prove consumer adoption.

## Scope

`AnalyticalViewManifestCandidate` is an additive carrier for one derived analytical view. It makes these declarations inspectable:

- stable view identity, kind, purpose, and definition digest;
- a dialect-profile reference without raw SQL;
- canonical upstream dataset references and optional lineage;
- separate join, filter, aggregate, deduplication, and window-semantics references;
- validation state and opaque validation/fixture references;
- query-time or materialized refresh posture;
- read-only, governed-updatable, direct-mutation-prohibited, or unresolved mutation posture;
- predicate-preservation intent for governed write-through use;
- intended use, review references, correction policy, and rollback target; and
- deterministic profile identity and fixed-false authority claims.

The manifest is declaration-only. It does not parse SQL, connect to a database, inspect a catalog, create or replace a view, run a query, refresh a materialization, mutate data, resolve an opaque reference, or authorize any lifecycle transition.

Raw SQL, SQL parameters, database endpoints, connection strings, credentials, table paths, and unrestricted runtime configuration are excluded. The schema is closed, so unknown fields fail validation.

## Repository binding

The current implementation slice is dependency-bound across existing responsibility roots:

| Role | Path | Verified posture |
|---|---|---|
| Semantic meaning | This contract | Proposed inactive profile; no runtime effect. |
| Machine shape | [`analytical_view_manifest.schema.json`](../../schemas/contracts/v1/data/analytical_view_manifest.schema.json) | Closed Draft 2020-12 schema for `AnalyticalViewManifestCandidate`. |
| Synthetic examples | [`cases.json`](../../fixtures/contracts/v1/data/analytical_view_manifest/cases.json) | One base candidate and 20 reviewed outcome cases. |
| Validator | [`validate_analytical_view_manifest.py`](../../tools/validators/data/validate_analytical_view_manifest.py) | Local schema, identity, coherence, and outcome checks only. |
| Focused tests | [`test_validate_analytical_view_manifest.py`](../../tests/validators/data/test_validate_analytical_view_manifest.py) | Ten deterministic tests, including explicit no-network replay. |
| Dedicated CI | [`analytical-view-manifest.yml`](../../.github/workflows/analytical-view-manifest.yml) | Path-scoped Python 3.11 validation and generated-receipt integrity. |
| Source reconciliation | [`pass-18-analytical-view-manifest-source-map.md`](../../docs/intake/exploratory/pass-18-analytical-view-manifest-source-map.md) | Proposal-card and adjacent-contract lineage; not implementation authority. |
| Authoring receipt | [`genrec-pass18-analytical-view-manifest-20260811.json`](../../data/receipts/generated/genrec-pass18-analytical-view-manifest-20260811.json) | Hash-binds seven artifacts; human review remains pending. |

The generated receipt includes this contract in its `artifact_paths`. Any contract-byte change must refresh the recorded contract digest and validate the receipt at the same proposed head. Schema, fixture, validator, test, workflow, and source-map bytes need not change when their behavior is unchanged.

## Manifest model

The closed envelope requires 18 top-level members:

| Concern | Required members | Meaning |
|---|---|---|
| Profile identity | `object_type`, `schema_version`, `profile`, `profile_spec_hash`, `source_cards` | Pins the candidate to `AnalyticalViewManifestCandidate`, schema `1.0.0`, profile `kfm.data.analytical-view-manifest.fixture.v1`, and the two Pass 18 cards. |
| Assessment | `assessed_at` | Offset-aware timestamp; the validator requires a UTC `Z` value. |
| View identity | `view_id`, `view_kind`, `purpose` | Stable opaque reference, finite kind, and bounded single-line purpose. |
| Definition | `definition` | SHA-256 definition digest, optional dialect-profile reference, and `raw_sql_stored: false`. |
| Upstream | `upstream` | One to 64 unique dataset references plus optional lineage reference. |
| Hidden semantics | `semantic_dependencies` | Separate join, filter, aggregate, deduplication, and window-disclosure references. |
| Validation | `validation` | Finite validation state plus report and fixture-receipt references. |
| Materialization | `materialization` | Refresh mode and optional freshness-profile reference. |
| Mutation | `mutation` | Posture, predicate reference, check-option mode, and policy reference. |
| Disclosure and recovery | `disclosure` | Intended use, summary, review references, correction policy, and rollback target. |
| Non-effects | `limitations`, `authority_claims` | Fixed declaration-only limits and 12 fixed-false authority flags. |

`profile_spec_hash` is computed over the complete candidate except the hash field itself through the shared hashing package. It binds definition, dependencies, validation, refresh, mutation guard, disclosure, limits, and authority claims. It detects candidate drift; it is not a signature, source checksum, database catalog digest, evidence proof, or release digest.

## View and refresh semantics

| View kind | Required refresh posture | Result boundary |
|---|---|---|
| `DATABASE_VIEW` | `ON_QUERY`; no freshness-profile reference | Describes query-time evaluation intent only. It does not prove that a database view exists. |
| `MATERIALIZED_VIEW` | `SCHEDULED`, `EVENT_DRIVEN`, or `MANUAL`; freshness-profile reference required | Describes refresh intent only. It does not schedule or perform a refresh. |
| `EQUIVALENT_DERIVED_VIEW` | Shape-valid declared posture; no database/materialization equivalence is proven | Holds a non-database derived-view proposal without inventing execution semantics. |
| `UNRESOLVED` | Visible abstention | Prevents an unknown kind from being treated as resolved. |

Database and materialized-view candidates require a dialect-profile reference. The validator does not resolve that reference, parse the underlying definition, compare dialect behavior, inspect indexes, estimate query cost, or verify freshness.

Validation states remain separate from execution and release:

- `VALIDATED` requires at least one validation-report reference and a fixture-receipt reference;
- `PARTIAL` returns `ABSTAIN`;
- `NOT_VALIDATED` returns `ABSTAIN` and must not carry validation references;
- `ERROR` returns `ERROR`; and
- no state authenticates the referenced reports or receipt.

## Mutation and predicate guard

| Mutation posture | Coherence rule | Effect |
|---|---|---|
| `READ_ONLY` | No predicate or mutation-policy reference; check option is `NOT_APPLICABLE`. | Declaration only; no database permission is changed. |
| `DIRECT_MUTATION_PROHIBITED` | Mutation-policy reference required; no predicate; check option is `NOT_APPLICABLE`. | Records an intended prohibition; does not enforce one. |
| `UPDATABLE_GOVERNED` | Predicate and mutation-policy references required; check option is `LOCAL`, `CASCADED`, or `EQUIVALENT_GUARD`; mutation predicate must equal the declared filter predicate. | Internal-only candidate posture; no write-through execution or database guard is created. |
| `UNRESOLVED` | Predicate and policy are null; guard is `UNRESOLVED`. | Returns `ABSTAIN`. |

The v1 profile denies `UPDATABLE_GOVERNED` when `intended_use` is `PUBLIC_CANDIDATE`. A public candidate also requires at least one review-record reference, but an opaque review reference is not authenticated and does not prove approval.

The check-option field records intended predicate preservation. It does not prove database support for `WITH CHECK OPTION`, trigger enforcement, row-level security, a policy engine, transactional behavior, or equivalent runtime protection.

## Finite outcomes

Outcome precedence is fail-closed:

| Outcome | When returned | What it proves |
|---|---|---|
| `ERROR` | Schema/canonicalization/input failure or recorded validation error. | The candidate could not be safely treated as a coherent manifest. |
| `DENY` | One or more non-abstention semantic findings remain. | The local candidate is contradictory, unsafe for its declared posture, noncanonical, unguarded, or hash-invalid. |
| `ABSTAIN` | Only reviewed unresolved/partial/not-validated findings remain. | The profile cannot reach a supported local determination. |
| `PASS` | Schema, deterministic identity, and implemented coherence rules all pass. | Only local fixture-profile coherence at those bytes. |

No outcome proves the view exists, the definition is correct, data is current, referenced evidence is resolved, policy ran, a reviewer approved, or release/publication is authorized.

## Executable coverage

### Fixture matrix

The manifest contains 20 synthetic cases:

| Outcome | Count | Covered situations |
|---|---:|---|
| `PASS` | 4 | Read-only database view; mutation-prohibited materialized view; internal governed-updatable view with guard; public read-only candidate with review reference. |
| `ABSTAIN` | 4 | Unresolved view kind; partial validation; not validated; unresolved mutation posture. |
| `DENY` | 10 | Database-view refresh mismatch; missing materialized freshness; missing validation evidence; incoherent read-only mutation fields; missing or drifted write guard; public write-through candidate; missing public review; noncanonical upstream refs; profile-hash tamper. |
| `ERROR` | 2 | Recorded validation error; schema-invalid unknown field. |

### Focused tests

The ten-test module verifies:

- Draft 2020-12 schema validity;
- unique fixture names and coverage of all four finite outcomes;
- exact replay of all 20 cases;
- the four positive posture boundaries;
- exact abstention and denial codes;
- hash binding across definition and mutation guard;
- denial of noncanonical semantic references after rehashing;
- finite canonicalization failure for an unpaired surrogate; and
- deterministic replay while socket creation and network connections are denied.

The validator also canonicalizes selected reference arrays, checks UTC assessment time, caps schema findings at 100, and returns sorted finding codes. It does not dereference any carried identity.

## Adjacent contract boundaries

| Contract | Owns | Does not become |
|---|---|---|
| [`LayerManifest`](./layer_manifest.md) | One governed map-layer representation and its catalog, artifact, policy, evidence, review, runtime, and release references. | A database/materialized-view definition or predicate-guard contract. |
| [`QueryRunRecord`](../governance/query_run_record.md) | One fixture-only governed query iteration, evidence-resolution projection, finite result, and candidate proposal references. | A stable reusable view definition, refresh declaration, or mutation policy. |
| [`ViewRegistryProfile`](../ui/view_registry_profile.md) | Inactive route-to-delivery resolution for future UI views. | Embedded SQL, a database endpoint, live route activation, or analytical-view execution. |

A future consumer may reference all three families while preserving their ownership: analytical definition, query-run history, layer delivery, UI resolution, evidence, policy, review, and release must not collapse into one manifest.

## Directory Rules basis

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../docs/doctrine/directory-rules.md) responsibility-root model. The analytical-view manifest describes semantic meaning for a derived data contract, so this document belongs in `contracts/data/`.

Machine shape, fixtures, validation, tests, CI, source reconciliation, and authoring accountability remain under `schemas/`, `fixtures/`, `tools/validators/`, `tests/`, `.github/workflows/`, `docs/intake/`, and `data/receipts/`. No SQL registry, database runtime, policy lane, lifecycle store, release path, or new authority root is created.

## Known gaps

The current profile does not establish or enforce:

- accepted SQL dialect profiles, a canonical analytical-view registry, or database portability rules;
- database catalog discovery, schema/table existence, dependency reachability, or definition-digest provenance;
- SQL parsing, deterministic query semantics, query plans, indexes, performance, cost, or resource limits;
- live creation, replacement, deletion, refresh, invalidation, concurrency, transactions, or rollback of a view;
- runtime verification of `WITH CHECK OPTION`, triggers, row-level security, mutation policy, or equivalent guards;
- reference resolution or authentication for datasets, lineage, semantic assessments, validation reports, fixture receipts, policies, reviews, corrections, or rollback targets;
- source admission, evidence closure, rights, sensitivity, lifecycle, review, promotion, release, deployment, publication, or public-use decisions;
- an accepted policy permitting any public write-through analytical view; v1 denies that posture;
- a runtime consumer or binding into `ViewRegistryProfile`, `LayerManifest`, `QueryRunRecord`, Explorer, APIs, or reports; or
- confirmed owners and operational rollback responsibility.

These are explicit holds, not implied future behavior. Any executable expansion requires a dependency-complete change across semantic contract, schema, fixtures, validator, tests, workflow, receipt, policy, runtime integration, and rollback evidence as applicable.

## Evidence and coordination lineage

| Source | Status | Supports | Limit |
|---|---|---|---|
| GitHub `main@d58c91b5ca5efb915bb21bf8d6945c46faa41e47`, current companion paths, and [merged PR #2597](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/2597) | `CONFIRMED` repository evidence | Current bytes, original dependency-closed introduction, and merge history. | Presence, merge, and CI do not activate a database view or grant review/release authority. |
| [Pass 18 source map](../../docs/intake/exploratory/pass-18-analytical-view-manifest-source-map.md) and [Drive Pass 18 dossier](https://drive.google.com/file/d/1ww-h3abQkxXeBvSxO5YV6_yvsZ9Wn1P5/view) | `CONFIRMED` source transcription; Drive file metadata/content available | `KFM-P18-INV-107` pressures documented view definition/purpose/validation, and `KFM-P18-INV-311` pressures check-option-style predicate preservation. | The source map records a supplied-PDF hash; byte identity with the Drive copy was not asserted. Proposal lineage is not implementation authority. |
| [Drive: Living Atlas interface and default-view design](https://docs.google.com/document/d/1aivNyfMjQ8urQO6vjt4YvkT1ltF1t7fxCahEcnGV4Dw/edit) | read-only proposed design | A useful view is a question, geography, layer stack, dates, legend, evidence path, and report outcome; future user-loadable views require resolved released public-safe artifacts. | Design guidance does not prove source admission, runtime binding, deployment, or release. |
| [Notion: Living Atlas design summary](https://app.notion.com/p/3d2a92021bf681d68e6dfad0564d8687) | unverified coordination summary | Preserves the same question/geography/layer/time/evidence/report distinction and directs implementation to re-pin current main. | Coordination context is not a second specification or implementation evidence. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `CONFIRMED` adopted placement governance | Responsibility-root and lifecycle separation. | Placement governance does not approve an analytical definition or consumer. |

GitHub remains implementation authority. Drive provides proposal/design lineage, and Notion provides coordination context. Conflicts resolve to current repository evidence and accepted governance; unresolved database, source, evidence, policy, and release facts remain visible and fail closed.

## Validation

From repository root, the dedicated profile runs:

```bash
python -m py_compile \
  tools/validators/data/validate_analytical_view_manifest.py \
  tests/validators/data/test_validate_analytical_view_manifest.py

python -m unittest \
  tests.validators.data.test_validate_analytical_view_manifest \
  --verbose

python tools/validators/data/validate_analytical_view_manifest.py --fixtures

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-pass18-analytical-view-manifest-20260811.json \
  --repo-root .
```

The dedicated workflow is triggered by this contract and receipt path. Reviewers should also verify:

- the pull request changes only this semantic contract and its bound receipt;
- the receipt's contract digest equals the exact proposed contract bytes;
- all repository-relative links resolve at the exact head;
- schema, fixture, validator, test, workflow, and source-map bytes are unchanged;
- exact-head hosted checks are recorded without converting inherited failures into waivers; and
- human review remains distinct from authorship, automated checks, and merge state.

## Definition of done

- [x] The existing schema, 20-case fixture manifest, validator, 10-test module, workflow, source map, and authoring receipt are linked.
- [x] Finite outcome precedence and exact fixture polarity are documented.
- [x] Database-view, materialized-view, equivalent-derived-view, validation, mutation, predicate-guard, disclosure, and non-authority semantics are explicit.
- [x] Adjacent LayerManifest, QueryRunRecord, and ViewRegistryProfile responsibilities remain separate.
- [ ] Owners and independent human reviewers are confirmed.
- [ ] Accepted dialect, registry, source/evidence, policy, and runtime-consumer boundaries are adopted.
- [ ] Live database behavior and rollback are separately implemented and proven, if authorized.
- [ ] Any release or public use has independent policy, review, evidence, and release records.

## Acceptance and rollback

Accept this documentation revision only if:

- repository readback matches the proposed bytes;
- the generated receipt validates at the same head;
- the executable profile and non-authority boundary are unchanged;
- exact-head CI is reconciled against the pinned base; and
- independent review occurs through the repository's normal review route.

Before merge, rollback is closing the pull request and abandoning its task branch. After an authorized merge, rollback is a normal revert of the contract and receipt refresh together. The pre-change contract is blob `b4764242ee8e9048dc1ea20e9646c11823010ebc` on `main@d58c91b5ca5efb915bb21bf8d6945c46faa41e47`.

No database object, data row, refresh job, query route, lifecycle record, cache, release, deployment, or public artifact requires restoration because this profile remains inactive and declaration-only.

---

`AnalyticalViewManifestCandidate` makes an analytical-view proposal inspectable. It does not make the proposal true, executable, current, reviewed, released, deployed, or public.

<p align="right"><a href="#top">Back to top</a></p>
