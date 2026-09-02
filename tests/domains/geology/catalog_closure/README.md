<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-catalog-closure-underscore-readme
title: Tests — Geology Catalog Closure Compatibility Alias
class: test-readme; compatibility-pointer
status: draft
truth_posture: CONFIRMED path / CONFIRMED sibling lane exists / PROPOSED naming decision / UNKNOWN enforcement completeness
owner: <geology-domain-steward> + <catalog-steward> + <evidence-steward> + <test-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - ../catalog-closure/README.md
  - ../README.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/runbooks/geology/PROMOTION_RUNBOOK.md
  - data/catalog/domain/geology/README.md
  - data/proofs/geology/README.md
  - fixtures/domains/geology/
tags:
  - kfm
  - tests
  - geology
  - natural-resources
  - catalog-closure
  - catalog_closure
  - compatibility
  - naming
  - evidence-bundle
  - fail-closed
notes:
  - "This README exists because the repository contains an underscore path at tests/domains/geology/catalog_closure/."
  - "A full catalog-closure lane README already exists at tests/domains/geology/catalog-closure/README.md."
  - "Until a repo-wide naming decision or ADR selects one path, this directory is a compatibility pointer and should not become a second test-authority home."
  - "Do not duplicate executable tests across both catalog-closure and catalog_closure; choose one home, document the decision, and retire or alias the other."
[/KFM_META_BLOCK_V2] -->

# Tests — Geology Catalog Closure Compatibility Alias

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fgeology%2Fcatalog__closure-blue?style=flat-square)
![type](https://img.shields.io/badge/type-compatibility__pointer-lightgrey?style=flat-square)
![primary](https://img.shields.io/badge/primary-see%20catalog--closure%2F-orange?style=flat-square)
![posture](https://img.shields.io/badge/posture-no__parallel__authority-critical?style=flat-square)

> **Purpose.** This README records the underscore naming variant `tests/domains/geology/catalog_closure/` and points maintainers to the current full catalog-closure test-lane contract at [`../catalog-closure/README.md`](../catalog-closure/README.md).

---

## 1. Status

| Question | Answer |
|---|---|
| This path | `tests/domains/geology/catalog_closure/` |
| Current role | Compatibility pointer / naming alias |
| Full lane contract | [`tests/domains/geology/catalog-closure/README.md`](../catalog-closure/README.md) |
| Gate under discussion | `PROCESSED -> CATALOG / TRIPLET` |
| Allowed contents here | This README only, unless an ADR or migration note chooses this as the active test home. |
| Enforcement status | `UNKNOWN` until executable tests, fixtures, validators, and CI wiring are verified. |

---

## 2. Why this is not a duplicate test lane

KFM Directory discipline avoids parallel authority homes. `catalog-closure/` and `catalog_closure/` name the same responsibility: Geology catalog-closure tests. Maintaining two independent README contracts or two duplicate test suites would create drift.

Therefore, until the repository chooses one naming convention:

- keep the full lane contract in one place;
- do not duplicate tests across both folders;
- do not split fixtures by punctuation style;
- do not let one folder become the docs home and the other become the executable home without recording that decision; and
- if this underscore path becomes preferred later, migrate the full lane contract here, update links, and retire or redirect the hyphen path in the same governed change.

---

## 3. Current full lane contract

Use [`../catalog-closure/README.md`](../catalog-closure/README.md) for the active catalog-closure test-lane contract. That README defines proposed coverage for:

- `EvidenceRef -> EvidenceBundle` resolution;
- `SourceDescriptor` linkage;
- `CatalogMatrix` entries;
- digest closure;
- STAC / DCAT / PROV projection alignment;
- graph / triplet support;
- source-role and resource-class anti-collapse;
- sensitivity and rights linkage;
- cross-lane ownership; and
- public-edge separation from the later release gate.

---

## 4. Migration rule

If maintainers decide `catalog_closure/` is the preferred path because Python module discovery commonly uses underscores, use this migration sequence:

1. Move or copy the full contract from `../catalog-closure/README.md` into this folder.
2. Move executable tests into this folder using underscore module names.
3. Update `tests/domains/geology/README.md`, fixtures, CI, validation commands, and docs links.
4. Leave a short redirect README in `catalog-closure/` or remove that folder in the same PR.
5. Record the naming decision in a PR note, drift register entry, or ADR if it affects more than this lane.

Do not silently maintain both homes as independent authorities.

---

## 5. Non-goals

This folder must not:

- become a second catalog-closure test authority without a migration decision;
- store duplicate tests that also exist under `catalog-closure/`;
- store catalog records, proofs, fixtures, schemas, policies, receipts, release manifests, or data artifacts;
- call live external Geology/Natural Resources services;
- publish public outputs; or
- weaken the catalog-closure gate by treating a naming alias as proof that enforcement exists.

---

## 6. Definition of done

This compatibility README is complete when it prevents ambiguity. The next implementation-backed step is not to expand this alias, but to choose one active path and wire executable catalog-closure tests, fixtures, validators, and CI to that path.
