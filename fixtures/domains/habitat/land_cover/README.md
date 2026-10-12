<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-domains-habitat-land-cover-readme
title: Habitat Land-Cover Fixtures README
type: directory-readme
version: v0.1
status: draft; CONFIRMED directory and child-lane index; fixture payloads and executable coverage UNKNOWN
owners:
  - "@kfm/maintainers"
created: 2026-07-16
updated: 2026-07-16
policy_label: public-doc; fixtures; habitat; land-cover; synthetic; no-network; non-authoritative
owning_root: fixtures/
base_commit: 975291ccc1342f323bb23ce723e7f5e4b1f44ddc
truth_posture: "CONFIRMED parent directory, eight child lanes, child README files, and placeholder-only payload state at the pinned base; PROPOSED fixture responsibilities; UNKNOWN executable fixture coverage, consumers, validation results, and promotion readiness"
related:
  - ../README.md
  - ../../../README.md
  - ../../../../tests/domains/habitat/land_cover/README.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/README.md
  - ../../../../contracts/domains/habitat/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/CODEOWNERS
notes:
  - "This README documents the existing parent fixture lane without adding or claiming fixture payloads."
  - "At the pinned base, each of the eight child lanes contains README.md and .gitkeep only."
  - "No contracts/domains/habitat/land_cover/README.md exists at the pinned base; this file links the confirmed Habitat contract parent and individual contract files instead."
[/KFM_META_BLOCK_V2] -->

# Habitat Land-Cover Fixtures

## Purpose

`fixtures/domains/habitat/land_cover/` is the canonical fixture lane for small,
deterministic Habitat land-cover examples grouped by object or checking role. It
indexes synthetic inputs and expected outputs that may support contract, schema,
runtime, renderer, and test work after a consumer is implemented.

This directory is a fixture home, not a truth home. Its presence confirms only
the repository structure described below; it does not confirm real fixture
payloads, executable validation, source admission, evidence closure, policy
approval, release readiness, or published behavior.

## Authority level

**Canonical** for Habitat land-cover fixture placement under the canonical
`fixtures/` responsibility root defined by Directory Rules.

That placement authority is deliberately narrow. Files here are
**non-authoritative examples**: they do not define semantic meaning, machine
shape, source identity, policy, lifecycle state, proof, review, release, or
public truth. The corresponding `contracts/`, `schemas/`, `data/`, `policy/`,
`tests/`, and `release/` roots retain those responsibilities.

## Status

**CONFIRMED directory and index; DRAFT documentation; fixture payloads and
executable coverage UNKNOWN.** The parent directory and all eight child lanes
exist at base commit `975291ccc1342f323bb23ce723e7f5e4b1f44ddc`.

Each child currently contains only its `README.md` plus `.gitkeep`. Therefore,
the intended responsibility documented by each child README is **PROPOSED** and
there is no substantive payload inventory to validate.

| Child lane | Intended fixture family | Confirmed direct files | Payload / execution posture |
|---|---|---|---|
| [`change_summary/`](change_summary/README.md) | `LandCoverChangeSummary` examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |
| [`class_scheme/`](class_scheme/README.md) | `ClassSchemeProfile` examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |
| [`crosswalk/`](crosswalk/README.md) | `CoverClassCrosswalk` examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |
| [`layer_manifest/`](layer_manifest/README.md) | Land-cover layer-manifest examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |
| [`model_run/`](model_run/README.md) | Model-run and receipt-shaped examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |
| [`observation/`](observation/README.md) | `LandCoverObservation` examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |
| [`uncertainty/`](uncertainty/README.md) | Land-cover `UncertaintySurface` examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |
| [`watcher/`](watcher/README.md) | Source-drift, checkpoint, no-op, and proposed-work examples | `README.md`, `.gitkeep` | No payload; execution UNKNOWN |

## What belongs here

- This parent index and the eight object- or behavior-specific child lanes.
- Small synthetic `*.json`, `*.geojson`, `*.jsonl`, `*.yaml`, `*.yml`, or
  `*.svg` payloads when a confirmed consumer and expected posture are recorded.
- Explicitly named positive, negative, invalid, and expected-output examples,
  such as `*.valid.json`, `*.invalid.json`, and `*.expected.json`.
- Toy observation, class-scheme, crosswalk, change-summary, model-run,
  uncertainty, layer-manifest, and watcher states.
- Toy IDs, timestamps, source roles, evidence references, policy references,
  correction references, rollback references, geometries, hashes, and digests.
- Deterministic generation notes or scripts only when the repository's accepted
  fixture-generation convention and owning implementation root are identified.

Every future payload must be compact, reviewable, reproducible, public-safe,
synthetic by default, and usable without network access. Its filename or nearby
documentation must distinguish input, expected output, and expected failure.

## What does NOT belong here

- Real source exports, live endpoint responses, credentials, private material,
  sensitive exact geometry, or records that can be mistaken for real Habitat
  observations.
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED lifecycle
  data; actual SourceDescriptors; EvidenceBundles; ProofPacks; receipts; review
  records; release manifests; correction notices; or rollback cards.
- Contract prose, JSON Schema authority, validator or pipeline implementation,
  policy rules, test modules, application code, public API responses, map tiles,
  renderer output, or generated CI artifacts.
- Fixtures that require a live network call, depend on an unpinned clock or
  random seed, silently reuse real data, or lack a declared expected posture.
- Any claim that a fixture, a schema-shaped example, or a passing check is
  source truth, habitat proof, policy approval, release approval, or publication.

## Inputs

Future fixture payloads may be manually authored synthetic examples or
deterministically generated examples with a pinned recipe, seed, and input
digest. Design inputs may include the confirmed Habitat semantic contracts,
schema scaffolds, child fixture READMEs, land-cover test-lane README, and Habitat
doctrine.

These references guide example construction; they are not payload sources and
must not be copied here as authority. Default fixture creation and validation is
**no-network**. A real upstream response must first enter the governed data
lifecycle and must not be converted into a repository fixture without explicit
rights, sensitivity, provenance, review, and public-safety decisions.

At the pinned base, this lane has no fixture payload inputs beyond the eight
child documentation files and their `.gitkeep` placeholders.

## Outputs

When implemented, this lane may supply bounded synthetic inputs and deterministic
expected outputs to Habitat land-cover schema checks, validators, test suites,
runtime dry-runs, renderer checks, and documentation examples.

No such consumer relationship is confirmed by file presence alone. This lane
does not emit source records, evidence closure, policy decisions, proofs,
receipts, release state, public layers, tiles, API responses, or AI answers.

## Validation

Current validation posture is intentionally explicit:

| Surface | Confirmed repository state | What it proves |
|---|---|---|
| Eight fixture child lanes | Each contains only `README.md` and `.gitkeep`. | Structure and documentation only; no payload validity. |
| [`tests/domains/habitat/land_cover/`](../../../../tests/domains/habitat/land_cover/README.md) | Parent plus eight child READMEs and `.gitkeep` files; no executable test module in the subtree. | Intended test boundaries only; executable coverage UNKNOWN. |
| [`tests/domains/habitat/test_habitat_smoke.py`](../../../../tests/domains/habitat/test_habitat_smoke.py) | Contains one executable placeholder assertion. | Pytest wiring only; it does not consume or validate this lane. |
| [`tools/validators/domains/habitat/`](../../../../tools/validators/domains/habitat/README.md) | Named validator files exist, but the inspected schema/evidence/catalog/source validators raise `NotImplementedError` and the other files are placeholder docstrings. | Validator-path presence only; no land-cover fixture enforcement. |
| [`schemas/contracts/v1/domains/habitat/land_cover/`](../../../../schemas/contracts/v1/domains/habitat/land_cover/README.md) | Five land-cover schemas exist with empty `properties`, no required fields, and `additionalProperties: true`. | Scaffold shape only; not substantive payload validation. |
| [Habitat workflow](../../../../.github/workflows/domain-habitat.yml) | The three jobs execute TODO echo commands. | Workflow presence only; not fixture or domain validation. |

Until real payloads and consumers are added, validation for this parent README is
limited to repository path checks, relative-link resolution, Markdown review,
and whitespace checks. A future payload is not ready merely because it parses:
its paired contract, accepted schema, expected outcome, deterministic consumer,
negative case, no-network behavior, and review requirements must also be named.

## Review burden

The current [`CODEOWNERS`](../../../../.github/CODEOWNERS) file has no
fixture- or Habitat-specific override, so its repository-wide default assigns
changes here to `@kfm/maintainers`. Changes that also modify `contracts/` or
`schemas/` invoke the listed contract or schema steward ownership for those
counterparts.

Reviewers of this lane must verify that:

- every payload is synthetic or explicitly approved as public-safe and carries
  no real or reverse-engineerable sensitive material;
- the change is deterministic and no-network by default;
- object families remain separate and the expected outcome is explicit;
- contract, schema, test, validator, and consumer links resolve without claiming
  unimplemented behavior;
- fixture success is not described as evidence, policy, proof, release, or truth;
- added payloads include both useful positive and fail-closed coverage where the
  consumer contract requires them.

### Rollback

For this documentation-only addition, rollback is a normal revert of this
`README.md`; the eight existing child directories and their files remain
unchanged. For a future payload change, first detach the fixture from consumers,
then revert the payload and its expected-output pair together. Preserve the last
reviewed deterministic case when it is still needed for regression history.

If real, private, restricted, or overly precise material is discovered, stop
consumption immediately, follow the governed quarantine and correction path,
and assess whether history, caches, artifacts, or credentials also require
remediation. Do not treat deletion from this directory alone as completed
rollback.

## Related folders

- [Habitat fixture parent](../README.md)
- [Fixture root](../../../README.md)
- [Habitat land-cover tests](../../../../tests/domains/habitat/land_cover/README.md)
- [Habitat land-cover schema index](../../../../schemas/contracts/v1/domains/habitat/land_cover/README.md)
- [Habitat contract parent](../../../../contracts/domains/habitat/README.md)
- [Land-cover observation contract](../../../../contracts/domains/habitat/land_cover/observation.md)
- [Class-scheme contract](../../../../contracts/domains/habitat/land_cover/class_scheme.md)
- [Crosswalk contract](../../../../contracts/domains/habitat/land_cover/crosswalk.md)
- [Change-summary contract](../../../../contracts/domains/habitat/land_cover/change_summary.md)
- [Model-run receipt contract](../../../../contracts/domains/habitat/land_cover/model_run_receipt.md)
- [Uncertainty contract](../../../../contracts/domains/habitat/land_cover/uncertainty.md)
- [Habitat land-cover doctrine](../../../../docs/domains/habitat/sublanes/land_cover.md)
- [Habitat validator index](../../../../tools/validators/domains/habitat/README.md)
- [Directory Rules](../../../../docs/doctrine/directory-rules.md)
- [CODEOWNERS](../../../../.github/CODEOWNERS)

There is no `contracts/domains/habitat/land_cover/README.md` at the pinned base,
so this index deliberately links the confirmed Habitat contract parent and
individual land-cover contract files instead.

## ADRs

- [ADR-0001 — Schema Home](../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md)
  is `proposed` and separates contract meaning from machine-checkable schema
  shape; it does not make fixtures authoritative.
- [ADR-0002 — Contracts vs Schemas Split](../../../../docs/adr/ADR-0002-contracts-vs-schemas-split.md)
  is `draft` with a proposed decision and describes fixtures, tests, and
  validators as separate verification support.

No Habitat land-cover fixture-specific ADR was identified at the pinned base.
Any future change that creates a parallel fixture authority, moves this lane,
or changes responsibility-root meaning requires Directory Rules review and, if
the decision class demands it, an accepted ADR before migration.

## Last reviewed

2026-07-16 — reviewed against base commit
`975291ccc1342f323bb23ce723e7f5e4b1f44ddc`, Directory Rules §15, the Habitat
fixture parent, all eight child READMEs and direct file inventories, the Habitat
land-cover test README and subtree, the Habitat land-cover schema README and
schema files, the Habitat contract parent and individual land-cover contracts,
current Habitat validator files, the Habitat workflow, and CODEOWNERS.
