<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-hydro-policy-readme
title: tools/validators/hydro/policy README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-hydrology-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; validator-policy-routing; hydrology; hydro-alias; not-policy-authority; not-flood-warning; release-gated; non-authoritative
owning_root: tools/
responsibility: validator-local policy routing README for the scaffolded hydro validator lane; documents how Hydrology validators should discover, reference, and report policy bindings while deferring Hydrology policy rules, allow/deny decisions, release policy, evidence, receipts, proofs, lifecycle data, schemas, and release decisions to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../fixtures/README.md
  - ../../README.md
  - ../../_common/README.md
  - ../../domains/hydrology/README.md
  - ../../atmosphere_hydrology/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../hazards/README.md
  - ../../domains/hazards/README.md
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/release/hydrology/
  - ../../../../policy/
  - ../../../../docs/domains/hydrology/README.md
  - ../../../../docs/domains/hydrology/ARCHITECTURE.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../docs/domains/hydrology/source-role-matrix.md
  - ../../../../docs/domains/hydrology/RELEASE_INDEX.md
  - ../../../../docs/runbooks/hydrology/PROMOTION_RUNBOOK.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../data/registry/sources/hydrology/
  - ../../../../data/proofs/hydrology/README.md
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file at tools/validators/hydro/policy/README.md. It does not confirm policy bundle files, executable validator code, tests, or CI wiring."
  - "Directory Rules identify policy/ as the root that decides allow, deny, restrict, or abstain. This tools-local policy folder is therefore a routing/index surface, not a policy authority."
  - "tools/validators/hydro/README.md is a scaffold and explicitly says policy belongs in policy/ unless an accepted ADR says otherwise."
  - "tools/validators/domains/hydrology/README.md remains the richer per-domain Hydrology validator index and routes Hydrology policy rules to policy/domains/hydrology/ and policy/release/hydrology/."
  - "No flood-warning authority, emergency instructions, legal/regulatory determination rules, hidden thresholds, release approvals, source data, evidence records, receipts, or policy decisions belong here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/hydro/policy

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-hydro--validator--policy--routing-informational)
![policy](https://img.shields.io/badge/policy-authority--elsewhere-lightgrey)
![boundary](https://img.shields.io/badge/not--flood--warning-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/hydro/policy/` documents policy lookup and reporting expectations for the scaffolded `hydro` validator lane; actual Hydrology allow/deny/restrict/abstain rules belong in `policy/`, not inside a validator folder.

---

## Purpose

`tools/validators/hydro/policy/` exists to keep Hydrology validator policy dependencies inspectable without turning `tools/validators/` into a policy root.

The durable KFM question for this README is:

> How should Hydrology validators discover, reference, pin, and report policy inputs for source-role separation, HUC/reach/gauge identity, observation-vs-model-vs-regulatory boundaries, time/freshness posture, not-flood-warning posture, public-safe geometry, evidence closure, release readiness, correction paths, rollback targets, and public-surface denial without storing policy decisions or release authority locally?

The answer should be routing guidance for validator maintainers. This folder should not define Hydrology policy, emergency-warning behavior, regulatory determinations, EvidenceBundles, receipts, release decisions, public map outputs, or AI-facing truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/hydro/policy/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| `tools/validators/hydro/README.md` | **CONFIRMED scaffold** | Parent `hydro` path is a proposed scaffold and says policy belongs in `policy/` unless an accepted ADR says otherwise. |
| `tools/validators/domains/hydrology/README.md` | **CONFIRMED README / executable NEEDS VERIFICATION** | Richer per-domain Hydrology validator index; current implementation behavior remains unverified. |
| Canonical Hydrology policy roots | **PROPOSED / NEEDS VERIFICATION** | Candidate homes include `policy/domains/hydrology/` and `policy/release/hydrology/`; existence, contents, and accepted bundle format need verification before use. |
| Local policy files in this folder | **NOT CLAIMED / DISCOURAGED** | No YAML, JSON, Rego, TOML, policy bundle, threshold file, review rule, release gate, or steward decision is claimed here. |
| Executables, schema bindings, test harnesses, policy bundle digests, receipt emission, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Placement decision

Directory Rules split responsibilities by authority:

| Responsibility | Preferred root |
|---|---|
| Repo-wide validator, generator, builder, checker | `tools/` |
| Allow, deny, restrict, or abstain rules | `policy/` |
| Tests that prove a rule is enforceable | `tests/` |
| Golden, valid, or invalid sample data for tests | `fixtures/` |
| Object meaning | `contracts/` |
| Machine shape | `schemas/` |
| Lifecycle data | `data/` |
| Release decision, manifest, rollback, correction | `release/` |

Therefore this path should normally be a **policy routing guide**, not a policy bundle store. Validators may read or pin policy bundle identifiers, but they must not become the source of policy truth.

[Back to top](#top)

---

## Policy routing relationship

| Concern | Preferred home | Validator responsibility |
|---|---|---|
| Hydrology domain allow/deny/restrict/abstain rules | `policy/domains/hydrology/` | Read the accepted policy bundle and report the bundle id/digest used. |
| Hydrology release gates | `policy/release/hydrology/` | Verify release-readiness policy was applied before public use. |
| Cross-domain policy propagation | `policy/` plus cross-domain validator lanes | Preserve most-restrictive policy across Hazards, Atmosphere, Agriculture, Soil, Geology, Infrastructure, Habitat, People/Land, and other joins. |
| Source-role policy | source registry, Hydrology docs, contracts, and policy roots | Verify observed, modeled, regulatory, aggregate, and public-map roles remain separated. |
| Freshness/expiry policy | policy roots plus source descriptors | Verify current-sensitive records do not bypass stale-state or expiry rules. |
| Public-surface denial | policy roots plus release manifests | Prevent unsupported Hydrology content from reaching maps, tiles, exports, search, graph, Focus Mode, screenshots, embeddings, or AI answers. |
| Release decision | `release/` | Report missing or mismatched ReleaseManifest, correction path, or rollback target; do not approve release. |
| Evidence and receipts | `data/proofs/`, `data/receipts/` | Verify references and emit/read accepted reports only where convention allows. |

[Back to top](#top)

---

## Relationship to Hydrology validator lanes

| Path | Role | Boundary |
|---|---|---|
| `tools/validators/hydro/` | Scaffolded shorthand Hydrology validator lane. | Existing parent is a proposed scaffold, not full Hydrology authority. |
| `tools/validators/hydro/policy/` | This validator-local policy routing surface. | Describes policy dependencies and lookup/reporting expectations; does not define policy. |
| `tools/validators/hydro/fixtures/` | Validator-local fixture routing surface. | Documents synthetic fixture expectations; not canonical fixture data storage. |
| `tools/validators/domains/hydrology/` | Per-domain Hydrology validator index. | Richer Hydrology validator boundary for object families, identities, source roles, time posture, evidence, policy, release, correction, rollback, and public-surface denial. |
| `tools/validators/atmosphere_hydrology/` | Cross-domain Atmosphere/Hydrology overlap lane. | Weather, atmosphere, drought, precipitation, runoff, smoke/water interactions, and neighboring-domain boundaries. |
| `tools/validators/cross-domain-joins/` | Shared cross-domain join checks. | Prevents ownership, source-role, policy, sensitivity, and release collapse. |

[Back to top](#top)

---

## Policy input classes

Future validators may need to resolve policy inputs such as:

| Policy input class | Validator question | Failure if absent |
|---|---|---|
| `domain_policy_bundle` | Which Hydrology domain policy bundle was used? | `POLICY_BUNDLE_MISSING` |
| `release_policy_bundle` | Which release gate applies before public output? | `RELEASE_POLICY_MISSING` |
| `source_role_policy` | Are observed, modeled, regulatory, aggregate, and public-map source roles separated? | `SOURCE_ROLE_POLICY_MISSING` |
| `freshness_policy` | Are valid time, observed time, source time, retrieved time, release time, correction time, expiry, and stale-state rules applied? | `FRESHNESS_POLICY_MISSING` |
| `not_flood_warning_policy` | Does the candidate deny KFM flood-warning, evacuation, emergency, dam-safety, navigation, engineering, or regulatory-decision authority? | `FLOOD_WARNING_AUTHORITY_DENIED` |
| `cross_domain_policy` | Does the most restrictive neighboring-domain policy propagate across joins? | `MOST_RESTRICTIVE_POLICY_MISSING` |
| `public_surface_policy` | Are map, tile, popup, export, search, graph, Focus Mode, screenshot, embedding, and AI surfaces governed? | `PUBLIC_SURFACE_POLICY_MISSING` |
| `release_reference_policy` | Are ReleaseManifest, correction path, rollback target, withdrawal path, and review state present where required? | `RELEASE_REFERENCE_MISSING` |

[Back to top](#top)

---

## Minimal policy binding manifest

Future validator runs may record policy binding metadata in a report or receipt. This sketch is **PROPOSED**, not a confirmed schema.

```yaml
validator_lane: tools/validators/hydro
policy_binding_id: hydro-policy-binding-example-001
policy_bundle_home: policy/domains/hydrology
release_policy_home: policy/release/hydrology
policy_bundle_digest: NEEDS_VERIFICATION
release_policy_digest: NEEDS_VERIFICATION
source_registry_home: data/registry/sources/hydrology
schema_home: schemas/contracts/v1/domains/hydrology
expected_policy_outcome: REVIEW_OR_POLICY_GAP
validator_may_decide_policy: false
validator_may_approve_release: false
notes: Metadata sketch only; not a policy bundle, EvidenceBundle, receipt, ReleaseManifest, or official hydrology decision.
```

Do not treat this manifest sketch as a schema until a schema file, validator registry entry, report destination, and test harness are verified.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| This policy README and validator policy-routing guidance | `tools/validators/hydro/policy/` |
| Hydro validator scaffold | `tools/validators/hydro/` |
| Per-domain Hydrology validator index | `tools/validators/domains/hydrology/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Hydrology policy rules | `policy/domains/hydrology/`, `policy/release/hydrology/`, or accepted policy homes |
| Tests | `tests/validators/hydro/`, `tests/validators/domains/hydrology/`, `tests/domains/hydrology/`, or accepted test home |
| Fixtures | `fixtures/domains/hydrology/`, `fixtures/validators/hydrology/`, or accepted fixture home |
| Hydrology domain meaning | `docs/domains/hydrology/`, `contracts/domains/hydrology/` |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` or ADR-selected homes |
| Source descriptors | `data/registry/sources/hydrology/` or accepted source registry home |
| Evidence/proof support | `data/proofs/hydrology/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Lifecycle data | `data/raw/hydrology/`, `data/work/hydrology/`, `data/quarantine/hydrology/`, `data/processed/hydrology/`, `data/catalog/...`, `data/published/...` |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator policy binding metadata may be documented here if it points to accepted `policy/` roots and does not become policy authority.
- **NEEDS VERIFICATION:** whether policy homes, policy bundle formats, digests, registry entries, schemas, fixtures, report destinations, receipt emission, runtime behavior, and CI wiring exist.
- **DENY:** using this folder as Hydrology doctrine, policy authority, emergency-warning authority, flood-warning authority, regulatory-determination authority, schema home, source registry, lifecycle data store, proof store, receipt store, release record store, or public map product surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/hydro/policy/` include:

- this README;
- notes on how a Hydrology validator should locate accepted policy bundles;
- policy binding metadata examples that are clearly marked **PROPOSED**;
- expected policy-related validator outcomes;
- links to canonical `policy/`, `release/`, `data/proofs/`, `data/receipts/`, `schemas/`, `contracts/`, `tests/`, and `fixtures/` homes;
- reminders that validators report policy gaps but do not decide policy or approve release.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/hydro/policy/` | Correct home |
|---|---|
| Hydrology allow/deny/restrict/abstain rules | `policy/domains/hydrology/` or accepted policy home |
| Release-gate rules | `policy/release/hydrology/`, `release/`, or accepted release-policy home |
| Policy bundles, steward decisions, hidden thresholds, or sensitive parameters | accepted `policy/` homes with review controls |
| Hydrology contracts or doctrine | `contracts/domains/hydrology/`, `docs/domains/hydrology/` |
| Hydrology schemas | `schemas/contracts/v1/domains/hydrology/` |
| Source descriptors | `data/registry/sources/hydrology/` |
| EvidenceBundles, proof packs, receipts, validation reports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, rollback cards, correction notices | `release/` |
| Tests and fixtures | `tests/`, `fixtures/` |
| Real source extracts or lifecycle data | governed `data/` lifecycle roots |
| Public API, UI, map, tile, search, graph, Focus Mode, export, screenshot, or AI runtime output | governed application/runtime roots |
| Current flood warnings, evacuation advice, dam-safety instructions, navigation safety advice, engineering decisions, or regulatory determinations | official agencies and governed source systems, not KFM validator docs |

[Back to top](#top)

---

## Policy safety rules

Hydrology policy-routing notes must:

- identify the policy home rather than copy policy rules locally;
- preserve source-role separation for observed, modeled, regulatory, aggregate, and public-map records;
- preserve not-flood-warning and not-emergency-instruction boundaries;
- preserve most-restrictive policy propagation across cross-domain joins;
- require policy bundle id or digest when validators claim a policy was applied;
- require explicit failure when policy is missing, ambiguous, stale, superseded, or unreviewed;
- require release, correction, and rollback references before public surfaces are treated as safe;
- avoid hidden thresholds, exact sensitive locations, real operational instructions, or current warning text;
- never convert validator pass into publication approval.

[Back to top](#top)

---

## Standard policy outcomes

| Outcome | Meaning |
|---|---|
| `POLICY_BINDING_PRESENT` | Validator found an accepted policy binding reference. |
| `POLICY_BUNDLE_MISSING` | Required Hydrology domain policy bundle is absent or unresolved. |
| `POLICY_BUNDLE_DIGEST_MISSING` | Policy bundle is referenced without digest, version, or review identity. |
| `POLICY_BUNDLE_STALE` | Referenced policy bundle is superseded, expired, or not current for the candidate surface. |
| `RELEASE_POLICY_MISSING` | Candidate lacks required release-policy gate reference. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `SOURCE_ROLE_POLICY_MISSING` | Candidate cannot prove observed/model/regulatory/aggregate/public-map source-role separation. |
| `FRESHNESS_POLICY_MISSING` | Candidate lacks freshness, expiry, stale-state, or correction policy support. |
| `FLOOD_WARNING_AUTHORITY_DENIED` | Candidate presents KFM as flood-warning, evacuation, emergency-instruction, engineering, or regulatory authority. |
| `MOST_RESTRICTIVE_POLICY_MISSING` | Cross-domain join fails to carry the strongest applicable policy. |
| `PUBLIC_SURFACE_POLICY_MISSING` | Candidate lacks policy support for map, tile, export, search, graph, Focus Mode, screenshot, embedding, or AI surface. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, rollback target, or withdrawal path is absent. |
| `VALIDATOR_POLICY_SYSTEM_ERROR` | Validator could not resolve policy because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/hydro/policy/README.md`.
- [x] It marks this path as validator-local policy-routing guidance, not policy authority.
- [x] It points Hydrology policy rules to `policy/domains/hydrology/` and release policy to `policy/release/hydrology/` or accepted policy homes.
- [x] It links the scaffolded `hydro` lane to the richer per-domain `hydrology` validator index.
- [x] It preserves not-flood-warning, source-role, identity, freshness, evidence, policy, release, correction, rollback, and public-surface denial boundaries.
- [x] It marks executable behavior, policy bundle files, policy digests, tests, schemas, fixtures, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Accepted policy homes and bundle formats are verified.
- [ ] Policy binding metadata shape is accepted or replaced by a real schema.
- [ ] Tests exercise present, missing, stale, superseded, and conflicting policy bindings.
- [ ] CI invokes the relevant Hydrology policy validation checks in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with Hydrology validator policy-routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
