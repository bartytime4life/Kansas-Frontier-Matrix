<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/crosswalks/geography-crosswalk
title: GeographyCrosswalk Candidate Contract
type: semantic-contract
version: v0.2.0
status: proposed; inactive; fixture-only; review-required; repository-grounded
owners: OWNER_TBD - Geography steward; Crosswalk steward; Contract steward; Evidence steward; Validation steward
created: 2026-08-10
updated: 2026-09-08
policy_label: internal; crosswalk; geography; no-network
owning_root: contracts/
responsibility: Define a version-pinned, direction-specific geography mapping declaration without resolving geography, executing joins, upgrading source roles, or changing release state.
truth_posture: CONFIRMED current repository binding and static semantics / PROPOSED inactive profile / NEEDS VERIFICATION steward adoption, exact-head hosted execution, and any real-data admission
related:
  - ./README.md
  - ../../schemas/contracts/v1/crosswalks/geography_crosswalk.schema.json
  - ../../fixtures/contracts/v1/crosswalks/geography_crosswalk/cases.json
  - ../../tools/validators/validate_geography_crosswalk.py
  - ../../tests/validators/test_validate_geography_crosswalk.py
  - ../../.github/workflows/geography-crosswalk.yml
  - ../../data/receipts/generated/genrec-pass20-geography-crosswalk-20260810.json
  - ../../docs/intake/exploratory/pass-20-geography-crosswalk-source-map.md
  - ../common/geography_version.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, crosswalk, geography, version, deterministic, fixture-only]
notes:
  - "Implements the separately reviewed crosswalk dependency required by GeographyVersion and Pass 20 KFM-IDX-APP-008."
  - "A validated declaration is not a boundary comparison, identity equivalence, executed join, evidence resolution, review approval, release record, or publication authority."
  - "v0.2.0 documents the schema, fixture, validator, test, workflow, receipt, and governance boundary present at main@2bddc4b4e453a7396d654d5f988911e9ee3af1ef; it changes no executable behavior."
[/KFM_META_BLOCK_V2] -->

# GeographyCrosswalk Candidate

`GeographyCrosswalk` is a proposed, fixture-only declaration of how digest-identified features from one pinned `GeographyVersion` may map forward to another. It preserves cross-version ambiguity and makes mapping intent reproducible without executing a spatial overlay or asserting that the mapping is true.

This contract describes the repository profile as it exists. It does not admit a geography source, carry boundary geometry, resolve references, perform a join, approve evidence, or authorize public use.

## 1. Authority and scope

The object has one bounded authority: **representation of a forward, version-pinned mapping declaration**.

It may represent:

- a distinct source and target `GeographyVersion` pair;
- a digest-bound method profile and declared validity interval;
- source and target feature identities as SHA-256 digests only;
- `EXACT`, `SPLIT`, `MERGE`, `PARTIAL_OVERLAP`, and `UNMAPPED` relations;
- integer-millionth allocation weights;
- opaque evidence references and unresolved governance posture; and
- deterministic content identity for fixture replay.

It must not be interpreted as:

- a geography dataset, boundary artifact, coordinate reference system, geometry, or feature-name catalog;
- proof that either geography version, feature, method, mapping, weight, or evidence object exists or is correct;
- identity equivalence outside the declared source-to-target direction and version pair;
- permission to infer a reverse mapping, execute a join, or transfer source authority;
- evidence, rights, sensitivity, policy, review, promotion, release, or publication approval; or
- a public API, released artifact, deployment state, or publication record.

An explicit `UNMAPPED` row is a supported fail-closed result. Missing support must not be converted into an apparent match merely to complete a crosswalk.

## 2. Repository binding

This documentation revision is frozen to repository `main` at commit `2bddc4b4e453a7396d654d5f988911e9ee3af1ef`.

| Responsibility | Current repository object | Binding at the frozen commit |
|---|---|---|
| Semantic meaning | This contract | Document profile `v0.2.0`; prior blob `683d22abb441edcc6b280f9a74950cc3363a42c5` |
| Machine shape | [`geography_crosswalk.schema.json`](../../schemas/contracts/v1/crosswalks/geography_crosswalk.schema.json) | JSON Schema Draft 2020-12; payload `schema_version` is exactly `1.0.0`; blob `cac2e5f8be37271f0b2cd043418d86422577b428` |
| Synthetic replay | [`cases.json`](../../fixtures/contracts/v1/crosswalks/geography_crosswalk/cases.json) | 25 cases: five `PASS` and 20 `DENY`; blob `62b7f04b4de55e236c0405986a3774096b32300a` |
| Validation | [`validate_geography_crosswalk.py`](../../tools/validators/validate_geography_crosswalk.py) | Local, deterministic, no-network validator; blob `1b4297aac85927aaafd4b5ac130802642c75a5ba` |
| Executable coverage | [`test_validate_geography_crosswalk.py`](../../tests/validators/test_validate_geography_crosswalk.py) | Nine unit tests; blob `cb95c6d46c16bfc20b50becd1bdfa85f1c421a78` |
| CI orchestration | [`geography-crosswalk.yml`](../../.github/workflows/geography-crosswalk.yml) | Path-scoped Python 3.11 workflow; blob `67639fe970b7b863f88e9e98f0714c1a83c434ec` |
| Authoring provenance | [`genrec-pass20-geography-crosswalk-20260810.json`](../../data/receipts/generated/genrec-pass20-geography-crosswalk-20260810.json) | Generated receipt; its contract digest must be refreshed with this documentation change |
| Source reconciliation | [`pass-20-geography-crosswalk-source-map.md`](../../docs/intake/exploratory/pass-20-geography-crosswalk-source-map.md) | Design-source and repository reconciliation; blob `d837c7e898efdc72e88dbc6646170d40511cdd8b` |
| Upstream dependency | [`geography_version.md`](../common/geography_version.md) | Separately versioned geography declaration; blob `35d2886a444af39d68326f6d3aa625b173321147` |
| Placement authority | [`ADR-0029`](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted decision adopting the pinned Directory Rules bytes; blob `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` |

The document version and payload schema version are separate. Updating this prose to `v0.2.0` does not change the payload profile `kfm.geography-crosswalk.fixture.v1` or its `1.0.0` machine shape.

## 3. Closed object envelope

The schema closes the root object and every nested object with `additionalProperties: false`.

| Field | Required value or constraint |
|---|---|
| `object_type` | Exactly `GeographyCrosswalk` |
| `schema_version` | Exactly `1.0.0` |
| `profile` | Exactly `kfm.geography-crosswalk.fixture.v1` |
| `crosswalk_id` | `kfm:geography-crosswalk:` plus the first 24 hexadecimal characters of the computed subject digest |
| `scope` | Version pair, direction, method profile, and validity interval |
| `mappings` | 1–128 mapping rows, lexically ordered by source digest |
| `support` | Source-role preservation plus unresolved evidence, rights, sensitivity, and review state |
| `disclosure` | The complete interpretation-limit set |
| `governance` | Fixture-only execution declaration and explicit non-authority values |
| `spec_hash` | `sha256:` plus 64 lowercase hexadecimal characters |

Digest-bound references use a constrained `kfm://...@sha256:<64 lowercase hex>` form. Feature identities use `sha256:<64 lowercase hex>` only. These shapes make references stable and opaque; they do not prove that a referenced object exists or has been admitted.

### 3.1 Scope

`scope` requires:

- different `source_geography_version_ref` and `target_geography_version_ref` values;
- `direction` exactly `SOURCE_TO_TARGET`;
- one digest-bound `method_profile_ref`;
- `valid_from` as an ISO calendar date; and
- `valid_to` as an ISO calendar date not earlier than `valid_from`, or null for an open interval.

The interval describes the declaration's stated applicability. It does not establish source-valid time, transaction time, publication time, or temporal compatibility with either referenced geography.

### 3.2 Mapping row

Every row requires `source_feature_id_digest`, `relation`, `targets`, and `reason_code`. A target requires `target_feature_id_digest` and `weight_millionths`; each weight is an integer from 1 through 1,000,000. A row can contain at most 16 targets.

| Relation | Required row shape | Interpretation limit |
|---|---|---|
| `EXACT` | One target; weight exactly `1000000`; `reason_code` null | Exact only within this declared direction and version pair |
| `SPLIT` | At least two targets; weights total exactly `1000000`; `reason_code` null | Allocation is declared, not measured by this validator |
| `MERGE` | One target; weight exactly `1000000`; the target is reused by at least two rows and every colliding row is `MERGE`; `reason_code` null | Shared target does not erase source identities |
| `PARTIAL_OVERLAP` | At least one target; positive total below `1000000`; `reason_code` null | Unallocated remainder is not inferred or described |
| `UNMAPPED` | No targets; `reason_code` exactly `NO_SUPPORTED_TARGET` | Absence of a supported target is preserved |

A target digest reused by multiple rows is invalid unless all involved rows form a `MERGE` group. A `MERGE` row that does not share its target with another row is also invalid.

## 4. Ordering, uniqueness, and identity

The validator requires deterministic authoring order:

- mapping rows sorted lexically by `source_feature_id_digest`;
- target entries within each row sorted lexically by `target_feature_id_digest`;
- `support.evidence_refs` sorted lexically; and
- `disclosure.interpretation_limits` sorted lexically.

Source digests must be unique across rows. Target digests must be unique within a row. Evidence references and interpretation limits are unique by schema.

For identity, the validator removes only top-level `crosswalk_id` and `spec_hash`, canonicalizes the remaining object with the repository hashing package's RFC 8785 JCS profile, and computes SHA-256:

```text
spec_hash    = SHA-256(JCS(identity subject))
crosswalk_id = kfm:geography-crosswalk:<first 24 digest hex>
```

The hash binds the declaration's representation. It is not a signature, source checksum, geometry digest, evidence proof, empirical quality score, release digest, or authority grant.

## 5. Evidence, disclosure, and governance boundary

`support` fixes the profile to an unresolved posture:

- `source_role_preserved` is true;
- `evidence_state` is `REFERENCED_NOT_RESOLVED`;
- `evidence_refs` contains 1–16 unique digest-bound references;
- `rights_state` is `REFERENCED_NOT_EVALUATED`;
- `sensitivity_state` is `REFERENCED_NOT_EVALUATED`; and
- `review_state` is `PENDING`.

`disclosure.interpretation_limits` must contain all five values:

- `NO_IDENTITY_EQUIVALENCE_INFERENCE`
- `NO_PUBLICATION_AUTHORITY`
- `NO_REVERSE_JOIN_INFERENCE`
- `SOURCE_ROLE_PRESERVED`
- `WEIGHTS_ARE_DECLARATIONS_NOT_MEASUREMENTS`

`governance.execution_mode` is exactly `FIXTURE_ONLY`. The schema requires `network_attempted`, `geographies_resolved`, `mapping_executed`, `evidence_resolved`, `rights_evaluated`, `sensitivity_evaluated`, `policy_evaluated`, `review_approved`, `promotion_authorized`, `release_authorized`, `public_use_allowed`, and `publication_authorized` all to be false.

A digest, evidence reference, passing validator, green workflow, pull request, review comment, merge, or repository path cannot override those explicit non-effects.

## 6. Validator behavior

The CLI has three outcome classes.

| Outcome | Meaning in this profile | Exit code |
|---|---|---|
| `PASS` | The object satisfies the bundled schema and current semantic checks | `0` |
| `DENY` | Schema or semantic findings exist | `1` |
| `ERROR` | The input cannot be safely read or parsed for validation | `2` |

### 6.1 Input safety

The reader:

- denies symlinks, missing or non-file paths, and files larger than 4 MiB;
- requires UTF-8 JSON with an object root;
- rejects duplicate object keys, non-finite numbers, invalid JSON, and read failures; and
- returns stable finding codes without reflecting candidate values in the serialized result.

### 6.2 Schema and semantic checks

Schema findings are emitted as `CROSSWALK_SCHEMA_INVALID` with JSON-pointer paths. After schema success, semantic checks cover:

- source/target version separation and interval ordering;
- row, target, evidence, and disclosure ordering;
- source and target uniqueness;
- exact relation shape and weight rules;
- coherent merge groups and cross-row target collisions;
- unmapped reason handling;
- the complete interpretation-limit set; and
- recomputed `spec_hash` and `crosswalk_id`.

The CLI serialization fixes `authority` to `NONE`, `execution_mode` to `FIXTURE_ONLY`, and reports the non-effects of no network, geography resolution, mapping execution, identity equivalence, evidence resolution, policy or review approval, promotion or release, public use, publication, or deployment.

## 7. Executable coverage

The fixture manifest defines 25 exact cases: five positive cases cover every finite relation, and 20 negative cases cover the principal semantic and schema boundaries.

| Coverage family | Included checks |
|---|---|
| Version and time | Same version pair; inverted validity interval |
| Determinism | Row, target, evidence, and disclosure ordering; duplicate source or target; hash and ID mismatch |
| Relation shape | Exact, split, merge, partial-overlap, and unmapped shape/weight failures |
| Collision control | Singleton merge and non-merge target collision |
| Disclosure and governance | Missing required limit; attempted release authorization |
| Input safety | Duplicate keys, non-finite numbers, symlink, oversize, malformed JSON, and parser determinism |
| Trust boundary | Digest-only identities, no geometry fields, no network access, and no payload-value reflection |

The nine-test module verifies Draft 2020-12 schema validity, exact fixture replay, relation coverage, digest-only/no-geometry posture, replay-stable identity, no-network source behavior, non-reflective output, deterministic CLI behavior, and input-safety failures.

The path-scoped workflow is configured to run the dedicated test module, the adjacent `GeographyVersion` test module, fixture replay, and generated-receipt integrity under Python 3.11 with `KFM_NO_NETWORK=1`. A future green exact-head run proves only those checks at that commit; it is not independent review or admission of real geography data.

## 8. Known enforcement gaps

The current profile does not:

- dereference either `GeographyVersion`, the method profile, evidence references, or feature identities;
- read coordinates, compare boundaries, calculate overlap, measure weights, or execute a forward or reverse join;
- prove mapping completeness, geographic coverage, conservation of unallocated partial weight, or crosswalk quality;
- check compatibility between the crosswalk interval and either geography's valid, retrieval, or publication times;
- establish source authority, source admission, identity equivalence, rights, sensitivity, evidence closure, or policy outcome;
- create review, promotion, release, public-use, publication, deployment, correction, or supersession authority; or
- provide a production resolver, registry entry, released artifact, public API, or UI behavior.

These are explicit limits, not implied capabilities. Executable expansion requires a dependency-closed change to the contract, schema, validator, positive and negative fixtures, tests, workflow paths, and generated receipt as applicable.

## 9. Directory Rules basis

ADR-0029 is the accepted decision that adopts the pinned Directory Rules bytes. Under its responsibility-first placement law:

| Responsibility | Existing owning path |
|---|---|
| Governed mapping meaning | `contracts/crosswalks/` |
| Machine shape | `schemas/contracts/v1/crosswalks/` |
| Synthetic replay | `fixtures/contracts/v1/crosswalks/` |
| Reusable validation | `tools/validators/` |
| Executable conformance | `tests/validators/` |
| Read-only CI orchestration | `.github/workflows/` |
| Source reconciliation | `docs/intake/exploratory/` |
| Generated authoring provenance | `data/receipts/generated/` |

This documentation revision changes no path. It creates no root, geography store, crosswalk registry, evidence store, policy home, runtime, public API, release lane, or publication path.

## 10. Validation and review

Run the changed-area checks from the repository root:

```bash
python -m unittest -v tests.validators.test_validate_geography_crosswalk
python -m unittest -v tests.validators.test_validate_geography_version
python tools/validators/validate_geography_crosswalk.py --fixtures
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-pass20-geography-crosswalk-20260810.json \
  --repo-root .
```

Reviewers should also confirm that every linked repository path resolves, the generated receipt binds the revised contract bytes, the target workflow is triggered for the exact pull-request head, and no overlapping pull request changes this object family.

Acceptance of this documentation revision requires:

- the semantic edit and its generated-receipt digest refresh remain dependency-closed;
- no schema, validator, fixture, workflow, or runtime behavior changes are implied;
- the non-authority boundary remains exact;
- hosted checks are attributed only to the exact pull-request head; and
- independent human review remains separate from automated checks and authoring.

## 11. Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the contract and paired receipt-digest refresh together. No source, geography, evidence, crosswalk registry, policy, lifecycle, deployment, release, or public state requires restoration.
