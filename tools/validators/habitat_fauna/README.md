<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-habitat-fauna-underscore-readme
title: tools/validators/habitat_fauna README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-habitat-steward-plus-fauna-steward-plus-geoprivacy-reviewer-plus-biodiversity-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; compatibility-routing-index; habitat-fauna; cross-domain-validator; underscore-alias; non-authoritative; fail-closed; release-gated
owning_root: tools/
responsibility: compatibility README for the underscore path tools/validators/habitat_fauna; routes maintainers to the preferred hyphenated Habitat-Fauna validator lane at tools/validators/habitat-fauna and the geoprivacy-specific lane at tools/validators/geoprivacy/habitat-fauna; prevents underscore and hyphen paths from becoming parallel validator authority
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../habitat-fauna/README.md
  - ../habitat/README.md
  - ../habitat/fauna-geoprivacy/README.md
  - ../geoprivacy/README.md
  - ../geoprivacy/habitat-fauna/README.md
  - ../domains/habitat/README.md
  - ../domains/fauna/README.md
  - ../fauna/README.md
  - ../biodiversity/README.md
  - ../cross-domain-joins/README.md
  - ../cross-lane/README.md
  - ../../../docs/domains/habitat/SENSITIVITY_AND_GEOPRIVACY.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../contracts/domains/habitat/
  - ../../../contracts/domains/fauna/
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../schemas/contracts/v1/domains/fauna/
  - ../../../policy/geoprivacy/
  - ../../../policy/sensitivity/habitat/
  - ../../../policy/sensitivity/fauna/
  - ../../../data/registry/sources/habitat/
  - ../../../data/registry/sources/fauna/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README replaces an empty file at tools/validators/habitat_fauna/README.md. It does not confirm executable validator code."
  - "The preferred broad cross-domain lane is tools/validators/habitat-fauna/. This underscore path is compatibility/routing only."
  - "Sensitive-location and public-safe-geometry concerns route to tools/validators/geoprivacy/habitat-fauna/."
  - "This path must not store policy parameters, schemas, receipts, proofs, lifecycle data, source descriptors, release decisions, exact coordinates, restricted identifiers, or reverse-engineering hints."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/habitat_fauna

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-habitat__fauna--compatibility-informational)
![authority](https://img.shields.io/badge/authority-routing--alias-lightgrey)
![canonical](https://img.shields.io/badge/preferred-habitat--fauna-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/habitat_fauna/` is a compatibility routing README for the underscore path. New broad Habitat × Fauna validator work should prefer `tools/validators/habitat-fauna/`; sensitive-location work should route to `tools/validators/geoprivacy/habitat-fauna/`.

---

## Purpose

This folder exists to prevent an empty underscore path from becoming an accidental parallel validator authority.

The durable KFM question for this README is:

> When a maintainer lands on `tools/validators/habitat_fauna/`, can they immediately tell which Habitat × Fauna validator lane is preferred, which geoprivacy lane owns sensitive-location checks, and which roots own doctrine, contracts, schemas, policy, evidence, receipts, release, correction, rollback, tests, and fixtures?

The answer should be a clear routing decision. This folder should not create Habitat truth, Fauna occurrence truth, taxonomic authority, Habitat suitability truth, geoprivacy thresholds, sensitive-location transforms, RedactionReceipts, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/habitat_fauna/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| Preferred broad Habitat-Fauna lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/habitat-fauna/README.md` is the preferred broad cross-domain validator lane. |
| Habitat-Fauna geoprivacy lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/geoprivacy/habitat-fauna/README.md` handles sensitive-location and public-safe geometry checks. |
| Habitat-facing Fauna geoprivacy shim | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/habitat/fauna-geoprivacy/README.md` is a Habitat-facing adapter/routing lane. |
| Executable code in this underscore folder | **NEEDS VERIFICATION / NOT CLAIMED** | No script, registry entry, fixture set, policy bundle, receipt path, runtime route, or CI job is claimed here. |

[Back to top](#top)

---

## Routing decision

Use this table before adding files below this underscore path.

| Work type | Preferred home | Why |
|---|---|---|
| Broad Habitat × Fauna validator logic | `tools/validators/habitat-fauna/` | Hyphenated path is already documented as the broad cross-domain lane. |
| Sensitive-location, public-safe geometry, redaction, aggregation, gridding, buffering, or reconstruction-risk checks | `tools/validators/geoprivacy/habitat-fauna/` | Geoprivacy-specific checks need the shared geoprivacy validator posture. |
| Habitat-facing adapter notes for Fauna geoprivacy | `tools/validators/habitat/fauna-geoprivacy/` | Habitat-specific routing belongs under the Habitat parent. |
| Per-domain Habitat checks | `tools/validators/domains/habitat/` | Domain-scoped Habitat validator index owns Habitat-side routing. |
| Per-domain Fauna checks | `tools/validators/domains/fauna/` or `tools/validators/fauna/` | Fauna occurrence/source-role posture stays visible. |
| Shared cross-domain join checks | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` | Cross-lane utilities should not be hidden in one paired lane. |
| Tests and fixtures | `tests/validators/...`, `tests/domains/...`, `fixtures/...` | Validator folders are not fixture or proof stores unless an accepted convention says otherwise. |

This folder should normally remain documentation-only. If code is ever added here, the PR should explain why the underscore path is required instead of the preferred hyphenated lane and should update the validator registry or drift register accordingly.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Compatibility routing for underscore path | `tools/validators/habitat_fauna/` |
| Preferred broad Habitat-Fauna validator lane | `tools/validators/habitat-fauna/` |
| Habitat-Fauna geoprivacy validator lane | `tools/validators/geoprivacy/habitat-fauna/` |
| Habitat-facing Fauna geoprivacy shim | `tools/validators/habitat/fauna-geoprivacy/` |
| Habitat validator routing | `tools/validators/habitat/`, `tools/validators/domains/habitat/` |
| Fauna validator routing | `tools/validators/fauna/`, `tools/validators/domains/fauna/` |
| Habitat/Fauna doctrine and contracts | `docs/domains/habitat/`, `docs/domains/fauna/`, `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Schemas | `schemas/contracts/v1/domains/habitat/`, `schemas/contracts/v1/domains/fauna/`, accepted schema homes |
| Policy and sensitivity | `policy/geoprivacy/`, `policy/sensitivity/habitat/`, `policy/sensitivity/fauna/`, accepted policy homes |
| Source descriptors | `data/registry/sources/habitat/`, `data/registry/sources/fauna/` |
| Evidence/proof support | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, correction, rollback, withdrawal | `release/` |

Safe interpretation:

- **CONFIRMED:** this README exists and provides routing guidance.
- **PROPOSED:** this path may remain as a compatibility alias while maintainers migrate to or prefer the hyphenated path.
- **NEEDS VERIFICATION:** whether any validator registry, CI job, package import, historical script, or external reference still expects the underscore path.
- **DENY:** using this folder as Habitat doctrine, Fauna doctrine, occurrence truth, taxonomic authority, geoprivacy threshold store, exact-location storage, source registry, schema home, proof storage, receipt storage, policy home, release record store, public runtime surface, AI answer authority, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/habitat_fauna/` include:

- this compatibility routing README;
- temporary migration notes that point from underscore to hyphenated validator lanes;
- a small import/routing shim only if an accepted validator registry or legacy caller still requires underscore naming;
- links to the preferred broad lane, geoprivacy lane, tests, fixtures, policy, schemas, and release roots;
- drift-register notes that explain whether the underscore path should be retained, mirrored, redirected, or deleted.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/habitat_fauna/` | Correct home |
|---|---|
| Broad Habitat-Fauna validator implementation | `tools/validators/habitat-fauna/` unless an ADR/registry requires otherwise |
| Geoprivacy policy parameters or transform logic | `policy/geoprivacy/`, accepted transformer/pipeline/package roots |
| Habitat or Fauna doctrine | `docs/domains/habitat/`, `docs/domains/fauna/` |
| Contracts | `contracts/domains/habitat/`, `contracts/domains/fauna/` |
| Schemas | `schemas/contracts/v1/...` |
| Source descriptors | `data/registry/sources/...` |
| EvidenceBundles, proof packs, validation reports, transform receipts | `data/proofs/`, `data/receipts/` |
| Release manifests, promotion decisions, rollback cards, correction notices | `release/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Public API, UI, map, tile, graph, search, export, Focus Mode, screenshot, or AI runtime code | governed application/runtime roots |
| Exact coordinates, restricted identifiers, thresholds, grid sizes, geohash precisions, or reverse-engineering hints | nowhere in public repository-facing docs |

[Back to top](#top)

---

## Standard routing outcomes

| Outcome | Meaning |
|---|---|
| `ROUTE_TO_HABITAT_FAUNA_HYPHEN` | Use `tools/validators/habitat-fauna/` for broad cross-domain validation. |
| `ROUTE_TO_HABITAT_FAUNA_GEOPRIVACY` | Use `tools/validators/geoprivacy/habitat-fauna/` for sensitive-location/public-safe geometry checks. |
| `ROUTE_TO_HABITAT_FAUNA_ADAPTER` | Use `tools/validators/habitat/fauna-geoprivacy/` for Habitat-facing adapter notes. |
| `UNDERSCORE_PATH_COMPATIBILITY_ONLY` | Keep this path as documentation or legacy shim only. |
| `UNDERSCORE_PATH_NEEDS_VERIFICATION` | Check registry, imports, CI, or historical references before deleting or adding code. |
| `PARALLEL_AUTHORITY_DENIED` | Do not define a competing Habitat-Fauna validator contract or policy here. |

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/habitat_fauna/README.md`.
- [x] It marks the underscore path as compatibility/routing only.
- [x] It points maintainers to `tools/validators/habitat-fauna/` for broad validation.
- [x] It points maintainers to `tools/validators/geoprivacy/habitat-fauna/` for sensitive-location and public-safe-geometry checks.
- [x] It avoids exact coordinates, restricted identifiers, policy thresholds, grid sizes, generalization radii, geohash precisions, and reconstruction hints.
- [x] It marks executable behavior, registry wiring, CI, fixtures, schemas, receipts, and release integration as **NEEDS VERIFICATION**.

Future cleanup remains open until:

- [ ] Validator registry or import references to `habitat_fauna` are searched and classified.
- [ ] Maintainers decide whether this path stays as compatibility, becomes a generated mirror, or is removed after migration.
- [ ] Any retained compatibility behavior is documented in the drift register or validator registry.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with underscore compatibility routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
