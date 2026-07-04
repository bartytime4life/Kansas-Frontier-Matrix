# `schemas/contracts/v1/domains/` — Domain Schema Lanes Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-readme
title: schemas/contracts/v1/domains/ — Domain Schema Lanes Index
type: readme; schema-index; domain-lane-index; governance-boundary
authority_class: schema-lane-index
version: v0.1
status: draft; domain-schema-index; remaining-stubs-present; path-conflicts-visible; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Domain stewards
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — placeholder existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; domains; domain-schema-lanes; machine-shape; source-role-aware; lifecycle-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, domains, json-schema, schema-home, domain-lanes, machine-shape, contracts-pairing, policy-separation, validation, adr-0001]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../contracts/domains/README.md
  - ../../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/registers/DRIFT_REGISTER.md
  - ../../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../../fixtures/domains/
  - ../../../../tests/domains/
  - ../../../../policy/domains/
  - ../../../../release/candidates/
notes:
  - "Expanded from a two-line placeholder at schemas/contracts/v1/domains/README.md."
  - "This file indexes domain schema lanes; it does not define field-level schema content."
  - "ADR-0001 is proposed and names schemas/contracts/v1/domains/<domain>/ as the default home for domain-specific machine-checkable schemas."
  - "schemas/contracts/v1/README.md currently identifies domains/* as remaining stubs, so individual domain schema maturity must stay NEEDS VERIFICATION unless proven by schema contents, fixtures, validators, registry entries, and CI evidence."
  - "Known slug and path conflicts, including transport vs roads-rail-trade, must remain visible until ADR or migration closure."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-domains-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![maturity](https://img.shields.io/badge/maturity-NEEDS__VERIFICATION-orange)
![publication](https://img.shields.io/badge/publication-release--gated-critical)

> **Purpose.** `schemas/contracts/v1/domains/` is the parent index for KFM domain-specific machine-checkable schemas.
>
> **One-line boundary.** This folder organizes domain schema lanes. It does not define semantic meaning, make policy decisions, admit sources, store evidence, publish public layers, or approve AI answers.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Domain lane inventory](#domain-lane-inventory) · [Known path conflicts](#known-path-conflicts) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-lane rules](#schema-lane-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this parent README exist? | Yes: `schemas/contracts/v1/domains/README.md`. It was a two-line placeholder before this expansion. | **CONFIRMED** |
| What does this folder own? | Domain-specific machine-checkable schema lanes under `schemas/contracts/v1/domains/<domain>/`. | **PROPOSED / ADR-0001-aligned** |
| Are all domain schemas mature? | No. The parent `schemas/contracts/v1/README.md` currently marks `domains/*` as remaining stubs. | **CONFIRMED / NEEDS VERIFICATION** |
| Does this README prove schema completeness? | No. It is an index and governance boundary only. | **CONFIRMED** |
| Can this README settle domain slug conflicts? | No. Slug/path conflicts require ADR, migration notes, and drift closure. | **CONFIRMED governance posture** |
| Does this README validate data or release public artifacts? | No. Validators, fixtures, policy, release, receipts, proofs, catalog records, and runtime behavior live elsewhere. | **CONFIRMED** |

> [!IMPORTANT]
> Treat this file as a map of the schema-lane boundary, not as a claim that every domain schema is complete, accepted, tested, wired into CI, or safe for publication.

---

## Authority and placement

ADR-0001 currently states the proposed repo-wide schema-home rule:

```text
schemas/contracts/v1/<family>/...
schemas/contracts/v1/domains/<domain>/...
```

Under that rule:

- `schemas/` owns machine-checkable shape.
- `contracts/` owns human-readable object meaning.
- `policy/` owns allow / deny / restrict / abstain behavior.
- `fixtures/` and `tests/` prove valid and invalid behavior.
- `data/` owns lifecycle payloads, registries, receipts, proofs, catalog, triplets, and published artifacts.
- `release/` owns promotion, release manifests, correction notices, and rollback cards.

This folder is therefore a **schema index**, not a domain root and not a substitute for any other responsibility root.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md                       # v1 schema-family status
        ├── common/                         # reusable/common schema families
        ├── evidence/                       # evidence schema families
        ├── governance/                     # governance schema families
        ├── policy/                         # policy-decision schema families
        ├── runtime/                        # runtime/API envelope schema families
        ├── source/                         # source descriptor/intake schema families
        └── domains/
            ├── README.md                   # this file
            └── <domain>/                   # domain-specific schema lane
                ├── README.md               # domain schema index
                └── *.schema.json           # machine-checkable domain shapes
```

Adjacent responsibility roots:

```text
contracts/domains/<domain>/                  # semantic meaning; not machine shape
docs/domains/<domain>/                       # doctrine and explanation
policy/domains/<domain>/                     # policy controls
fixtures/domains/<domain>/                   # valid/invalid examples
tests/domains/<domain>/                      # behavioral proof
data/<phase>/<domain>/                       # lifecycle data
release/candidates/<domain>/                 # promotion/release/correction/rollback surfaces
```

---

## Domain lane inventory

Current GitHub search surfaced the following domain schema-lane README paths or schema files. This is a **search-derived working index**, not an exhaustive file-tree proof. Regenerate it from a mounted checkout before promotion.

| Domain schema lane | Evidence surfaced | Posture |
|---|---|---|
| `agriculture/` | README and schema files surfaced. | **NEEDS VERIFICATION** |
| `air/` | README surfaced; overlaps with `atmosphere/` require review. | **NEEDS VERIFICATION / possible alias** |
| `archaeology/` | README and schema files surfaced. | **NEEDS VERIFICATION / sensitivity-heavy** |
| `atmosphere/` | README, registry README, and observation/registry schema files surfaced. | **NEEDS VERIFICATION** |
| `fauna/` | README and schema files surfaced. | **NEEDS VERIFICATION / geoprivacy-sensitive** |
| `flora/` | README and schema files surfaced. | **NEEDS VERIFICATION / geoprivacy-sensitive** |
| `geology/` | README, sublane READMEs, and schema files surfaced. | **NEEDS VERIFICATION** |
| `habitat/` | README, child-lane README, geoprivacy receipt schema, and other schema files surfaced. | **NEEDS VERIFICATION** |
| `hazards/` | README, receipts README, and schema files surfaced. | **NEEDS VERIFICATION / public-safety-sensitive** |
| `hydrology/` | README and schema files surfaced. | **NEEDS VERIFICATION** |
| `people/` | README surfaced. | **NEEDS VERIFICATION / living-person-sensitive** |
| `people-dna-land/` | README, genealogy/people/land-ownership child READMEs, and schema files surfaced. | **NEEDS VERIFICATION / deny-by-default-sensitive** |
| `roads/` | README surfaced; relationship to `roads-rail-trade/` requires review. | **NEEDS VERIFICATION / possible drift** |
| `roads-rail-trade/` | README and schema files surfaced. | **NEEDS VERIFICATION** |
| `settlement/` | README surfaced; relationship to `settlements-infrastructure/` requires review. | **NEEDS VERIFICATION / possible alias or drift** |
| `settlements-infrastructure/` | runtime README and schema files surfaced. | **NEEDS VERIFICATION** |
| `soil/` | README and schema files surfaced. | **NEEDS VERIFICATION** |
| `transport/` | README and `road-segment.schema.json` surfaced; path is conflict-indexed. | **PATH-CONFLICTED / NEEDS VERIFICATION** |

> [!NOTE]
> The inventory above should be normalized by an ADR-backed domain-slug registry or schema registry. This README should not silently merge, rename, or deprecate lanes.

---

## Known path conflicts

| Conflict | Evidence signal | Required handling |
|---|---|---|
| `transport/` vs `roads-rail-trade/` | Roads/Rail/Trade canonical-path doc records a two-axis conflict: `domains/` segment and slug choice. | Keep both visible; do not add new authority to the hybrid path without ADR. |
| `roads/` vs `roads-rail-trade/` | Search surfaced a `roads/README.md` as well as `roads-rail-trade/README.md`. | Treat as **NEEDS VERIFICATION** until a steward decides alias, migration, or deprecation. |
| `air/` vs `atmosphere/` | Search surfaced both lane names. | Treat as **NEEDS VERIFICATION** until domain-lane registry resolves alias/drift. |
| `settlement/` vs `settlements-infrastructure/` | Search surfaced both lane names. | Treat as **NEEDS VERIFICATION** until steward/ADR resolution. |
| `people/` vs `people-dna-land/` | Search surfaced both lanes plus child lanes. | Preserve sensitivity boundaries; do not collapse living-person, genealogy, DNA, and land ownership schemas without policy review. |
| Flat atlas-era schema paths vs `domains/<domain>/` paths | ADR-0001 discusses migration discipline and forbids divergent parallel authorities. | Use ADR/migration notes, mirror notices, or deprecation records; do not create duplicate canonical schemas. |

---

## What belongs here

- This parent README.
- Domain-lane README files under `schemas/contracts/v1/domains/<domain>/`.
- Domain-specific JSON Schema files.
- Domain schema-family child-lane READMEs.
- Migration notes, mirror notices, and deprecation notes for domain schema placement.
- Index pointers to paired contracts, fixtures, validators, schema registry records, source registry records, policy references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Semantic contract prose.
- Policy rules or sensitivity decisions.
- Validator implementation code.
- Runtime code, generated SDKs, or domain packages.
- Pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs or EvidenceBundles as data.
- Catalog records or triplets.
- Release records, release manifests, promotion decisions, correction notices, or rollback cards as records.
- Public tiles, map/UI behavior, dashboards, screenshots, story nodes, Focus Mode answers, or generated summaries.
- Claims that a schema is complete without fixtures, validators, registry records, policy checks, review state, release state, and steward review support.

---

## Schema-lane rules

| Rule | Requirement |
|---|---|
| Stable identity | Every schema should have a stable `$id` under the accepted schema-home namespace or an ADR-approved namespace. |
| Dialect | Use JSON Schema draft 2020-12 unless an ADR says otherwise. |
| Contract pairing | Each domain schema should link to a paired semantic contract or explicitly state why it profiles a common/shared schema. |
| Source-role preservation | Observation, interpretation, derived summary, model output, public artifact, and review/release records must not collapse. |
| Temporal explicitness | Preserve valid, observed, source, retrieval, release, and correction time where material. |
| Evidence closure | Schemas may shape EvidenceRef / EvidenceBundle references, but this folder must not store evidence bundles or proof instances. |
| Policy separation | Schemas may define decision-envelope fields, but policy decisions belong in `policy/` and release surfaces. |
| Release separation | Release-related schemas define shape only; authoritative release records live under `release/`. |
| Sensitive-domain default | Archaeology, living-person, DNA, land ownership, rare species, sensitive habitat, infrastructure, hazards, and precise locations require deny-by-default review where applicable. |
| No parallel authority | Do not create duplicate schema homes for the same object family without ADR, migration note, mirror notice, or deprecation plan. |

---

## Promotion checklist

A domain schema should not advance beyond `STUB` / `PROPOSED` unless:

- [ ] Accepted path home is clear or path conflict is marked `PATH-CONFLICTED` / `TRANSITIONAL`.
- [ ] Schema has stable `$id` and JSON Schema dialect.
- [ ] Paired semantic contract is linked.
- [ ] Schema registry entry is linked or explicitly marked **NEEDS VERIFICATION**.
- [ ] Valid fixtures are linked.
- [ ] Invalid fixtures are linked.
- [ ] Validator path is linked.
- [ ] CI/schema-test support is linked.
- [ ] Source-role, temporal, evidence, policy, sensitivity, release, correction, and rollback fields are explicit where material.
- [ ] Adjacent-domain boundaries are preserved.
- [ ] Public API, MapLibre, Evidence Drawer, and Focus Mode consumers are version-aware if they use the schema.
- [ ] Migration and rollback path are documented for breaking changes.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect parent and child domain schema lanes.
find schemas/contracts/v1/domains -maxdepth 2 -type f | sort

# Detect likely duplicated or conflicted schema lanes.
find schemas/contracts/v1 -maxdepth 4 -type f \
  | grep -Ei 'transport|roads-rail-trade|roads|air|atmosphere|settlement|settlements-infrastructure|people-dna-land|people' \
  | sort

# Validate JSON syntax for all domain schema files.
find schemas/contracts/v1/domains -name '*.schema.json' -print0 \
  | xargs -0 -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/domains || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/domains/README.md`.

Rollback for domain schemas requires more care:

1. Revert or migrate the schema file.
2. Revert or update paired semantic contracts.
3. Revert or update fixtures and validators.
4. Revert or update schema registry entries.
5. Revert or update producers, consumers, public API payloads, MapLibre layer descriptors, Evidence Drawer payloads, and Focus Mode fixtures.
6. Update release candidates, correction notices, and rollback cards if a schema reached release workflow.
7. Preserve drift and migration notes so reviewers can reconstruct the path decision.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Which domain lanes are canonical, aliases, mirrors, transitional, or drift? | **NEEDS VERIFICATION** | Schema steward + docs steward |
| Should a machine-readable schema registry be generated from this tree? | **PROPOSED** | Schema steward |
| Which `domains/*` schemas are still empty stubs, and which can advance to `DRAFT_SCHEMA`? | **NEEDS VERIFICATION** | Domain stewards + validation steward |
| How should transport / roads-rail-trade path conflict be resolved? | **ADR REQUIRED** | Roads/Rail/Trade steward + schema steward |
| How should air/atmosphere, roads/roads-rail-trade, settlement/settlements-infrastructure, and people/people-dna-land aliases be handled? | **NEEDS VERIFICATION / ADR-sensitive** | Docs steward + affected domain stewards |
| Which domain schema files are consumed by governed API, MapLibre, Evidence Drawer, Focus Mode, release candidates, or validators today? | **NEEDS VERIFICATION** | API/UI + release + validation stewards |

---

## Maintainer notes

- Keep this README as the parent index for domain schema lanes.
- Do not turn this folder into a cross-domain schema dumping ground; common reusable shapes belong under the appropriate shared family.
- Do not use schema existence as evidence that a claim can be published.
- Preserve the KFM lifecycle: `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`.
- Preserve cite-or-abstain: public truth requires evidence, source role, policy, review, release, correction lineage, and rollback support, not merely a valid JSON shape.
