<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/published-language-review-source-map
title: PublishedLanguageReview source map
type: exploratory-source-map
version: 1.0.0
status: proposed
owning_root: docs/
truth_posture: source-derived proposal; current repository behavior verified separately
related:
  - ../../../contracts/governance/published_language_review.md
  - ../../../control_plane/cross_domain_seam_register.yaml
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# PublishedLanguageReview source map

## Goal

Translate the bounded-context and published-language recommendations in the supplied KFM idea atlases into one deterministic, no-network, fixture-only review profile.

## Source-derived requirement

The supplied Pass 20 synthesis proposes that KFM domain lanes operate as bounded contexts with explicit published language, source-role registries, and anticorruption boundaries. Pass 18 separately proposes context maps for cross-lane dependency governance and a public vocabulary boundary that stabilizes outward API terms while insulating internal context vocabulary.

Those sources support a **review candidate**, not adopted vocabulary. The repository already contains a partial cross-domain seam projection; this packet references that concept rather than creating a second context-map authority.

## Repository evidence and gap

At the implementation base:

- `control_plane/cross_domain_seam_register.yaml` already records a partial context-map projection for high-risk seams;
- multiple domain documentation lanes contain ubiquitous-language material; and
- no fixture-backed `published_language_review` schema, validator, or workflow was found.

The smallest dependency-closed increment is therefore a held, fixture-only review object rather than a context-map rewrite or API migration.

## Non-effects

This packet does not:

- adopt or deprecate a public term;
- amend `control_plane/cross_domain_seam_register.yaml`;
- change a schema or API consumer;
- assign a steward;
- activate a source or resolve evidence;
- evaluate policy or human review;
- promote, release, deploy, publish, or authorize public use.

## Directory Rules basis

Accepted ADR-0029 makes `docs/doctrine/directory-rules.md` the placement authority. The implementation uses existing responsibility roots for semantic meaning, machine shape, examples, validators, tests, orchestration, and generated accountability. No new root or parallel contract, schema, policy, registry, evidence, release, or publication home is created.
