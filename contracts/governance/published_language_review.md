<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/published-language-review/v1
title: PublishedLanguageReview candidate profile
type: semantic-contract
version: 1.0.0
status: proposed-inactive
owning_root: contracts/
responsibility: Define a fixture-only review record for stabilizing public vocabulary across KFM bounded contexts without adopting terminology or changing an API.
truth_posture: cite-or-abstain; review candidates are not adoption, release, or publication authority
related:
  - ../../schemas/contracts/v1/governance/published_language_review.schema.json
  - ../../fixtures/contracts/v1/governance/published_language_review/README.md
  - ../../tools/validators/governance/validate_published_language_review.py
  - ../../control_plane/cross_domain_seam_register.yaml
  - ../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# `PublishedLanguageReview` candidate profile

> **Status:** `PROPOSED_INACTIVE` · **Authority:** fixture-only review candidate · **Public-use authority:** none

## Purpose

`PublishedLanguageReview` records a bounded proposal to stabilize one public term across KFM bounded contexts. It makes the term, owning context, related contexts, object-family bindings, public API resource bindings, internal aliases, compatibility posture, and evidence support inspectable before adoption.

The profile operationalizes a source-derived recommendation that KFM use bounded contexts, context maps, and published language to prevent domain semantics from collapsing while keeping public API vocabulary stable. It does **not** declare a term canonical, amend a context map, change a schema or API, approve migration, activate a source, resolve evidence, authorize release, or publish anything.

## Directory Rules basis

The accepted Directory Governance Standard assigns:

- semantic meaning to `contracts/`;
- machine shape to `schemas/contracts/v1/`;
- examples to `fixtures/`;
- executable validation to `tools/validators/` and `tests/`;
- orchestration to `.github/workflows/`; and
- generated authoring accountability to `data/receipts/generated/`.

This profile stays within those existing responsibility roots and creates no parallel authority home.

## Required meaning

| Field | Meaning |
|---|---|
| `term_id` | Stable candidate identity for the vocabulary concept. |
| `public_term` | Exact outward spelling proposed for public contracts and documentation. |
| `definition` | Bounded definition that a consumer can inspect. |
| `owning_context` | The bounded context that owns the term's semantic meaning. |
| `related_contexts` | Other contexts that consume or translate the term without owning it. |
| `context_map_ref` | Reference to the context-map or seam projection used during review. |
| `object_family_refs` | Semantic object families the term names or constrains. |
| `public_api_resource_refs` | Public resource families whose language would be affected. |
| `internal_aliases` | Internal names that remain implementation details rather than public vocabulary. |
| `stability` | `PROVISIONAL`, `STABLE`, or `DEPRECATED`. |
| `change_kind` | `ADDITIVE`, `CLARIFICATION`, `BREAKING`, or `DEPRECATION`. |
| `migration_ref` / `compatibility_window` | Mandatory only for breaking or deprecation candidates. |
| `decision` | Fixed at `HOLD`; this profile cannot adopt itself. |

## Deterministic identity

The validator computes RFC 8785 JCS + SHA-256 over the complete candidate except `review_id` and `spec_hash`:

```text
spec_hash = sha256(JCS(identity_subject))
review_id = "published-language-review:" + first_24_hex(spec_hash)
```

Identity proves deterministic fixture binding only. It does not prove semantic correctness or approval.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The inactive candidate is internally coherent and retains all authority holds. |
| `DENY` | Semantic, compatibility, bounded-context, or authority invariants fail. |
| `ERROR` | Input, schema, hashing, deterministic identity, or fixture execution failed. |

## Mandatory invariants

- Reference arrays are sorted and unique.
- `related_contexts` cannot include `owning_context`.
- `internal_aliases` cannot collide with `public_term`, case-insensitively.
- `BREAKING` and `DEPRECATION` require a migration reference and a valid compatibility window.
- `ADDITIVE` and `CLARIFICATION` cannot carry migration authority or a compatibility window.
- `DEPRECATED` stability and `DEPRECATION` change kind must occur together.
- `decision` remains `HOLD`, `adoption_ref` remains `null`, `public_use_allowed` remains `false`, and every effect remains `false`.

## Trust boundary

A passing result proves only local candidate shape, canonical ordering, bounded-context separation, migration-field coherence, deterministic identity, and fixture polarity. Human/domain review, API compatibility approval, context-map amendment, schema change, policy evaluation, adoption, release, deployment, publication, and public use remain outside this profile.
