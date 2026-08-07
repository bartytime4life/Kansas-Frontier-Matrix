<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-catalog-readme
title: tools/validators/catalog/ — Catalog Record Validator Boundary
type: README; validator-lane; catalog-record-validation; stac; dcat; prov; non-authoritative
version: v0.3
status: draft; PROPOSED implementation; fixture-first; catalog-health-executable; no-network-by-default; release-gated; fail-closed
owners: OWNER_TBD — Catalog · STAC · DCAT · PROV/PAV · Validator · Schema · Contract · Source · Evidence · Rights/Sensitivity · Policy · Release · Security · CI · Docs stewards
created: 2026-07-07
updated: 2026-08-07
supersedes: v0.2 README-only boundary
policy_label: repository-facing; catalog; discovery; interchange; evidence-aware; rights-aware; sensitivity-aware; release-gated; fail-closed; discovery-not-truth
owning_root: tools/
current_path: tools/validators/catalog/README.md
responsibility: Validate individual catalog discovery/interchange records and bounded indexes; delegate cross-record closure, evidence, policy, release, storage, construction, and public serving to their owning lanes.
truth_posture: >
  CONFIRMED at main@14b9608addcf6cac80adaa0a836182f7a6e47806: this lane contained a detailed README and a placeholder evidence-closure file but no catalog-health executable, dedicated catalog-health fixtures/tests, report schema, or focused workflow. PROPOSED in this change: one narrow STAC Item health profile with deterministic local-byte verification, provenance-link checks, embargoed-access metadata, remote HOLD behavior, optional allowlisted HTTPS HEAD probes, a strict report schema, synthetic fixtures, tests, and focused CI. UNKNOWN: production consumers, accepted repository-wide STAC profile, required-check status, deployment, and public serving.
related:
  - ../README.md
  - ../_common/README.md
  - ../catalog_closure/README.md
  - ./catalog_health_core.py
  - ./catalog_health_rules.py
  - ./validate_catalog_health.py
  - ../../../contracts/data/catalog_health_report.md
  - ../../../contracts/data/catalog_closure_packet.md
  - ../../../schemas/contracts/v1/data/catalog_health_report.schema.json
  - ../../../fixtures/data/catalog_health/README.md
  - ../../../tests/validators/test_validate_catalog_health.py
  - ../../../data/catalog/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/workflows/catalog-health.yml
tags: [kfm, tools, validators, catalog, stac, catalog-health, provenance, assets, no-network, fail-closed]
notes:
  - "A catalog-health PASS is bounded record-local validation evidence only."
  - "STAC/DCAT/PROV cross-record agreement remains under tools/validators/catalog_closure/."
  - "No source, evidence, policy, review, release, publication, or public-use authority is created here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Catalog Record Validator Boundary

`tools/validators/catalog/`

> Validate individual catalog discovery/interchange records without turning catalog metadata into truth, proof, policy, release approval, or publication.

![status](https://img.shields.io/badge/status-draft-yellow)
![implementation](https://img.shields.io/badge/implementation-fixture--first-orange)
![profile](https://img.shields.io/badge/profile-STAC--Item--health-blue)
![network](https://img.shields.io/badge/network-deny--by--default-red)
![authority](https://img.shields.io/badge/authority-validator--only-lightgrey)

## Purpose

This lane owns **record-local** checks. It does not build catalog records, close a cross-record catalog package, create evidence, decide policy, approve review, release, publish, host, search, or serve public clients.

The first implemented profile is deliberately narrow:

```text
kfm.catalog-health.stac-item.v1
```

It turns a catalog-health checklist into deterministic validation for one STAC Item and its declared assets. The profile is `PROPOSED`; it is not the repository's complete or adopted STAC profile.

[Back to top](#top)

## Current implementation

| Surface | Status | Meaning |
|---|---|---|
| `catalog_health_core.py`, `catalog_health_rules.py`, `validate_catalog_health.py` | **PROPOSED executable** | Validates one STAC Item, governance metadata, provenance-link rels, asset descriptors, local asset bytes, embargoed access metadata, and bounded optional remote reachability. |
| `CatalogHealthReport` contract/schema | **PROPOSED** | Defines a strict deterministic report with `PASS`, `HOLD`, `FAIL`, or `ERROR`. |
| Synthetic fixture family | **PROPOSED** | Two PASS cases, one remote-unverified HOLD, and four exact-negative cases; no real source or sensitive data. |
| Focused tests | **PROPOSED** | Schema validity, fixture polarity, local SHA-256/size checks, network kill switch, exact allowlist, safe diagnostics, deterministic replay, and authority-overclaim rejection. |
| `catalog-health` workflow | **PROPOSED** | Read-only, no-network focused validation and generated-receipt integrity. |
| Production consumers / required-check status | **UNKNOWN** | This change does not claim deployment, branch-protection adoption, or runtime use. |

The pre-existing `validate_evidence_closure.py` placeholder is not promoted into authority by this slice.

[Back to top](#top)

## Directory Rules and authority

Directory Rules place executable validator logic under `tools/`; semantic meaning under `contracts/`; machine shape under `schemas/`; synthetic examples under `fixtures/`; enforceability under `tests/`; hosted orchestration under `.github/workflows/`; catalog records under `data/catalog/`; evidence/proofs under `data/proofs/`; receipts under `data/receipts/`; policy under `policy/`; and release decisions under `release/`.

This lane must not become a second catalog, proof, receipt, source registry, policy engine, release store, published-artifact store, or public API.

| Concern | Owning lane |
|---|---|
| Individual STAC/DCAT/PROV/domain record checks | `tools/validators/catalog/` |
| STAC↔DCAT↔PROV agreement and readiness closure | `tools/validators/catalog_closure/` |
| Domain-specific closure | `tools/validators/domains/<domain>/catalog_closure/` when verified |
| Catalog construction | `pipelines/catalog/` and accepted catalog packages |
| Catalog-stage records | `data/catalog/` |
| Release, correction, withdrawal, rollback | `release/` and accepted accountability homes |
| Public delivery | Governed APIs and released public-safe artifacts |

[Back to top](#top)

## Catalog-health profile

The first profile checks:

- STAC `Feature` type, `stac_version`, stable `id`, geometry/bbox, properties, time, nonempty assets and links;
- license, providers with names and roles, and created/updated timestamps;
- provenance-link rels `derived_from`, `checksum`, `commit`, and `manifest_uri`;
- asset `href`, media type, unique roles, title, `file:checksum`, and `file:size`;
- local path containment, symlink denial, file existence, resource limits, byte size, and SHA-256;
- embargoed assets only when an explicit `via` access/request link exists;
- remote public assets as `HOLD` when network is denied; and
- optional HTTPS `HEAD` probes only with an explicit operator switch and exact host allowlist.

The profile does not download remote assets, verify a remote checksum, validate every STAC extension, establish DCAT/PROV agreement, or decide whether the data may be released.

[Back to top](#top)

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Configured record-local checks passed. |
| `HOLD` | No blocking defect was found, but a public remote asset remains unverified because network access or host authorization was absent. |
| `FAIL` | A deterministic profile, integrity, URI, metadata, or resource rule failed. |
| `ERROR` | Input could not be safely parsed or evaluated. |

A `PASS` may be referenced by a later closure packet as validation evidence. It is never an `EvidenceBundle`, `PolicyDecision`, review approval, `PromotionReceipt`, `ReleaseManifest`, or publication authorization.

Stable reason-code families use the `CAT_*` prefix. Findings contain only codes, severities, and JSON-pointer-like fields; untrusted values are not echoed.

[Back to top](#top)

## Security and resource posture

- Network is denied by default and by `KFM_NO_NETWORK=1`.
- Optional probes require `--network-head` plus one or more exact `--allow-host` values.
- Only HTTPS remote assets are probeable; redirects and credential-bearing URLs are denied.
- Localhost, local-only names, and private/reserved/link-local/multicast/unspecified literal addresses are denied.
- Target bytes, asset bytes, JSON depth/nodes, assets, and links are bounded.
- Duplicate JSON keys, non-finite numbers, symlink inputs, path traversal, unsafe schemes, and unsafe diagnostics fail closed.
- Output order and canonical target digest are deterministic.

[Back to top](#top)

## Commands

Focused tests:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_catalog_health.py' \
  --verbose
```

Deterministic fixture replay:

```bash
KFM_NO_NETWORK=1 \
python tools/validators/catalog/validate_catalog_health.py --fixtures
```

Local package validation:

```bash
python tools/validators/catalog/validate_catalog_health.py \
  --asset-root path/to/catalog-package \
  path/to/catalog-package/item.json
```

Bounded remote reachability:

```bash
python tools/validators/catalog/validate_catalog_health.py \
  --asset-root path/to/catalog-package \
  --network-head \
  --allow-host data.example.gov \
  path/to/catalog-package/item.json
```

[Back to top](#top)

## CI and trust boundary

`.github/workflows/catalog-health.yml` runs only the focused tests, fixture replay, and generated authoring-receipt check. It sets `KFM_NO_NETWORK=1`. A green workflow proves only the declared synthetic profile at the tested commit.

The workflow does not activate a source, write catalog data, call a public endpoint, create evidence, approve policy or review, promote, release, publish, or change repository settings.

[Back to top](#top)

## Record versus closure separation

`validate_catalog_health.py` validates one STAC Item. `validate_catalog_closure.py` validates a bounded `CatalogClosurePacket` joining STAC, DCAT, PROV, evidence, validation, policy/review, correction, rollback, and release-candidate references. Neither validator owns the underlying records or decisions.

Do not merge the lanes merely because both use catalog metadata. Record health and cross-record closure are separate responsibilities and separate review boundaries.

[Back to top](#top)

## Remaining verification backlog

- Accepted repository-wide STAC profile and extension registry.
- Accepted SPDX/custom-license registry and attribution policy adapter.
- DCAT and PROV record-local profiles.
- Source/evidence/rights/sensitivity adapters.
- Production report destination and retention.
- Registration in any shared validator aggregate.
- Required-check / branch-protection significance.
- Real catalog consumers, public routes, metrics, and correction propagation.
- Disposition of the older `validate_evidence_closure.py` placeholder.
- Human owners and CODEOWNERS coverage.

These remain `NEEDS VERIFICATION` or `UNKNOWN`; this slice does not guess them.

[Back to top](#top)

## Correction and rollback

If the profile, source rights, sensitivity posture, asset digest, record identity, or release status changes, invalidate the report and rerun validation. Published correction, withdrawal, cache invalidation, and rollback remain responsibilities of their governing lanes.

Repository rollback removes the additive contract, schema, fixture family, executable, tests, workflow, generated receipt, and reverts this README to v0.2. No catalog record, proof, policy decision, release object, or published artifact is changed by that rollback.

## Changelog

- **v0.3 — 2026-08-07:** adds the proposed fixture-first STAC Item catalog-health executable, strict report contract/schema, synthetic fixtures, focused tests, no-network workflow, record/closure separation, and explicit trust boundary.
- **v0.2 — 2026-07-16:** repository-grounded README-only boundary and implementation backlog.
- **v0.1 — 2026-07-07:** initial proposed lane.
