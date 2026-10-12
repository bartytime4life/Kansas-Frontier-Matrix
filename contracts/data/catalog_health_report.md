<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/catalog-health-report
title: CatalogHealthReport Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED; fixture-first
owners: OWNER_TBD — Catalog steward · STAC steward · Validation steward · Security reviewer
created: 2026-08-07
updated: 2026-08-07
policy_label: public; contracts; data; catalog-health; no-network-by-default; non-authoritative
owning_root: contracts/
responsibility: Define the non-authoritative semantic meaning and trust boundary of CatalogHealthReport.
truth_posture: PROPOSED implementation; CONFIRMED local validation; UNKNOWN production adoption.
related:
  - ../../schemas/contracts/v1/data/catalog_health_report.schema.json
  - ../../tools/validators/catalog/catalog_health_core.py
  - ../../tools/validators/catalog/catalog_health_rules.py
  - ../../tools/validators/catalog/validate_catalog_health.py
  - ../../fixtures/data/catalog_health/
  - ../../tests/validators/test_validate_catalog_health.py
  - ./catalog_closure_packet.md
  - ../../docs/doctrine/directory-rules.md
notes:
  - "A PASS is bounded catalog-record health evidence, never evidence truth, policy permission, review approval, promotion, release, publication, or public-use authority."
  - "This first profile validates one STAC Item and its declared assets; STAC/DCAT/PROV cross-record agreement remains the CatalogClosurePacket lane."
[/KFM_META_BLOCK_V2] -->

# `CatalogHealthReport`

> A deterministic, public-safe report describing whether one STAC Item satisfies the proposed KFM record-health profile and whether its declared local assets match their recorded byte size and SHA-256 digest.

## Purpose and boundary

`CatalogHealthReport` turns the attached catalog-health checklist into an enforceable first slice while reinforcing existing KFM catalog, provenance, no-network, finite-outcome, and fail-closed rules.

The report covers only:

- STAC Item identity, geometry/bbox, time, assets, links, license, providers, and created/updated metadata;
- the proposed provenance-link rels `derived_from`, `checksum`, `commit`, and `manifest_uri`;
- asset `href`, media type, roles, title, `file:checksum`, and `file:size`;
- deterministic local byte-size and SHA-256 verification;
- explicitly embargoed assets with a `via` access/request link; and
- optional HTTPS `HEAD` reachability checks when the operator enables network access and supplies an exact host allowlist.

It does **not** validate every STAC extension, establish DCAT/PROV agreement, create an `EvidenceBundle`, prove source truth, decide rights or sensitivity, approve policy or review, close a release, publish an artifact, or authorize public use. Cross-record STAC/DCAT/PROV readiness remains under `CatalogClosurePacket` and its validator.

## Directory Rules basis

The semantic meaning belongs under `contracts/data/`; machine shape under `schemas/contracts/v1/data/`; the executable under `tools/validators/catalog/`; synthetic bytes and records under `fixtures/data/catalog_health/`; enforceability under `tests/validators/`; and hosted orchestration under `.github/workflows/`.

No new root or parallel catalog, proof, receipt, policy, release, or publication authority is introduced.

## Profile

The initial profile identifier is:

```text
kfm.catalog-health.stac-item.v1
```

It is intentionally narrow and fixture-first. It does not claim to be the repository's complete STAC profile.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The configured record-local checks passed. All non-embargoed local assets were byte-verified, or explicitly enabled/allowlisted remote assets were reachable with matching declared size. |
| `HOLD` | No blocking defect was found, but one or more non-embargoed remote assets were not probed because network access or the host allowlist was absent. |
| `FAIL` | The record, provenance links, asset descriptors, local bytes, remote probe result, or resource boundary violated the profile. |
| `ERROR` | The validator could not safely parse or evaluate the input. |

`PASS` is admissible as a `validation_report_ref` input to a later closure review. It never implies release readiness by itself.

## Network contract

Network mode is `DENY` unless all of the following are true:

1. the operator passes `--network-head`;
2. `KFM_NO_NETWORK` is not `1`;
3. each remote host is supplied through `--allow-host`; and
4. each remote URL is HTTPS, contains no credentials, and is not localhost, local-only, private, reserved, link-local, multicast, or unspecified as a literal address.

Redirects are not followed. Network mode verifies reachability and declared `Content-Length` only; it does not download remote bytes or cryptographically verify a remote checksum.

## Determinism and diagnostics

- Target JSON is parsed as UTF-8 with duplicate-key and non-finite-number rejection.
- Record and local-asset sizes, JSON depth/node count, asset count, and link count are bounded.
- The target record digest is canonical sorted-key JSON plus SHA-256.
- Findings contain stable codes and JSON-pointer-like fields only; untrusted values are not echoed.
- Finding order and serialized report bytes are deterministic for the same inputs and mode.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_catalog_health.py' \
  --verbose

KFM_NO_NETWORK=1 \
python tools/validators/catalog/validate_catalog_health.py --fixtures
```

Optional bounded probe:

```bash
python tools/validators/catalog/validate_catalog_health.py \
  --asset-root path/to/catalog-package \
  --network-head \
  --allow-host data.example.gov \
  path/to/item.json
```

## Rollback

This slice is additive except for updating the catalog-validator README from README-only status. Rollback removes the contract, schema, fixture family, executable, tests, workflow, generated authoring receipt, and the README implementation note. No catalog record, evidence/proof object, policy decision, release object, or published artifact requires restoration.
