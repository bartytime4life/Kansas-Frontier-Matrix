<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-hashing-readme
title: packages/hashing/ — Deterministic Hashing Package Boundary
type: readme
version: v1.2
status: draft; repository-grounded; bounded-implementation; non-authoritative; unpublished
owners:
  - "@bartytime4life — verified CODEOWNERS review route; package stewardship remains NEEDS VERIFICATION"
created: 2026-07-15
updated: 2026-08-25
policy_label: "repository-facing; package-boundary; deterministic-hashing; no-network; fail-closed; no-authority; no-publication"
owning_root: packages/
responsibility: "Own current package maturity, distribution posture, public import surface, and compatibility boundary for the reusable KFM hashing implementation."
truth_posture: "CONFIRMED bounded RFC 8785 JCS plus SHA-256 implementation, current sha256:<hex> grammar, structural GeoJSON digest profile, package metadata, explicit exports, thin tool wrapper, validator, focused tests, and workflow / PROPOSED ADR-0013 grammar and future profiles / UNKNOWN external consumers, software distribution, cross-language parity, deployed use, and independent stewardship / no evidence, policy, review, promotion, release, publication, or public-use authority"
evidence_snapshot: "main@52d83c0233bef201587ec8a7b9d0c0a7a0c1493f; prior README 3d3174974668623117c1f90bcbc6918262d1b6af; package metadata 0466047f5a738aae1d51e78f579a057a869f1900; core a609eac44b1a5f24bd9ba449afedfeec7dd17e8e; GeoJSON 2db35caf8aa0bb8ff0c582e03c1a57b1caf8e358; CLI 860b7f04ad6b4ab2144ed61fb896100e1a8577bc; exports 676ddec2ede8dd3cba3b6eb73e647d876d5e1fe4; tool wrapper 1145aa6b9c55f7e18ab5e386d9d424755963e544; validator e83a8707548c35411d1fc61911f499ac7ca6d517; core tests ce981cede288facfa449026e422acfe60a6e4d5d; GeoJSON tests 9d8d044422afbe83868035484aff73e15b025d45; workflow 1da612211bf0d2e0bf339561bc06f336111d614e; contract cd20f45a900948fca1eba54dfb7ee128d2c15a11; Directory Rules fd49a0b83e55cef52c1124281f093e263526898d"
related:
  - ../README.md
  - src/README.md
  - src/hashing/README.md
  - pyproject.toml
  - ../../contracts/common/spec_hash.md
  - ../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../docs/architecture/identity-and-spec-hash.md
  - ../../docs/standards/CANONICALIZATION.md
  - ../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md
  - ../../tools/spec_hash/README.md
  - ../../tools/validators/validate_spec_hash.py
  - ../../tests/validators/test_validate_spec_hash.py
  - ../../tests/validators/test_validate_spec_hash_geojson.py
  - ../../.github/workflows/spec-hash.yml
notes:
  - "This package README is the single current implementation-status owner for packages/hashing/. Child READMEs inherit status and document only their local placement or API boundary."
  - "Earlier greenfield API, migration, and verification-register proposals remain available in Git history; this compact current-state contract does not adopt them."
  - "A digest match proves equality only under the declared input domain and profile."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `packages/hashing/` — deterministic hashing package boundary

> Reusable, no-network helpers for bounded JSON admission, RFC 8785 JCS canonicalization, SHA-256 content identity, and one structural GeoJSON digest profile.

> [!IMPORTANT]
> This README is the package's **current implementation-status owner**. [`src/README.md`](src/README.md) inherits this status and governs source placement. [`src/hashing/README.md`](src/hashing/README.md) inherits it and governs the import/API boundary. Neither child is a parallel maturity, contract, schema, policy, or release authority.

> [!WARNING]
> A matching digest proves only equality under the same admitted value, hash domain, profile, and algorithm. It does not prove truth, source authority, evidence sufficiency, rights, sensitivity clearance, policy approval, review, promotion, release, publication, or fitness for public use.

## Purpose and authority

`packages/hashing/` owns reusable, independently testable hashing implementation and its package-local API/build/test boundary. This is a `BOUNDARY_COMPACT` package under Directory Rules §16.

Other responsibilities remain separate:

| Responsibility | Owner |
|---|---|
| Semantic meaning of `spec_hash` | [`contracts/common/spec_hash.md`](../../contracts/common/spec_hash.md) |
| Machine-valid shape | [`schemas/contracts/v1/common/spec_hash.schema.json`](../../schemas/contracts/v1/common/spec_hash.schema.json) |
| Cross-root architecture and current grammar | [`docs/architecture/identity-and-spec-hash.md`](../../docs/architecture/identity-and-spec-hash.md) |
| Canonicalization guidance | [`docs/standards/CANONICALIZATION.md`](../../docs/standards/CANONICALIZATION.md) |
| Proposed future identity grammar | [`ADR-0013`](../../docs/adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md), still proposed |
| Repository CLI | [`tools/spec_hash/`](../../tools/spec_hash/README.md), a thin adapter |
| Validator of record | [`tools/validators/validate_spec_hash.py`](../../tools/validators/validate_spec_hash.py) |
| Evidence, policy, review, promotion, release, correction, and publication | Their existing owning roots and governed processes |

## Current bounded status

| Surface | Current repository evidence | Bounded conclusion |
|---|---|---|
| Package metadata | `kfm-hashing` `0.1.0`; Python `>=3.11`; Hatchling; `rfc8785==0.1.4`; `kfm-spec-hash` entry point | Installable package configuration is present; no external publication was verified or authorized. |
| Generic JSON hashing | [`core.py`](src/hashing/core.py) | Bounded loader, RFC 8785 JCS bytes, `sha256:<64 lowercase hex>`, validation, and constant-time comparison are implemented. |
| Structural GeoJSON digests | [`geojson.py`](src/hashing/geojson.py) | `kfm-geojson-feature-digest-v1` produces separate geometry and record digests with declared CRS and precision. It does not prove topological or spatial equivalence. |
| Public imports | [`__init__.py`](src/hashing/__init__.py) | Explicit core and GeoJSON exports are implemented. |
| Package CLI | [`cli.py`](src/hashing/cli.py) | Compute, verify, and `geojson-feature` commands return finite, non-authoritative results. |
| Tool delegation | [`tools/spec_hash/spec_hash.py`](../../tools/spec_hash/spec_hash.py) | Thin wrapper imports the package; it does not fork canonicalization. |
| Validation | [`validate_spec_hash.py`](../../tools/validators/validate_spec_hash.py) | Schema validation and optional recomputation are implemented with `PASS`, `DENY`, and `ERROR`. |
| Focused tests | [`test_validate_spec_hash.py`](../../tests/validators/test_validate_spec_hash.py) and [`test_validate_spec_hash_geojson.py`](../../tests/validators/test_validate_spec_hash_geojson.py) | Thirteen test methods cover canonicalization, fixture polarity, recomputation, unsafe input, deterministic CLI behavior, and GeoJSON profile boundaries. |
| Workflow | [`.github/workflows/spec-hash.yml`](../../.github/workflows/spec-hash.yml) | Path-filtered pull-request/main validation is checked in; a file's presence is not proof of a particular run. |
| Current executable grammar | `sha256:<64 lowercase hex>` | Implemented across package, schema, validator, and focused tests. |
| Candidate grammar | `jcs:sha256:<hex>` | Proposed by ADR-0013; not current write behavior. |
| Distribution, deployment, and external consumers | Not established by this evidence scope | `UNKNOWN`; no publishing or operational-use claim. |

## Current package map

```text
packages/hashing/
├── README.md       # current package status and boundary (this file)
├── pyproject.toml  # build, runtime, dependency, and CLI metadata
└── src/            # inherited source envelope
```

Deeper implementation detail belongs to the child README, not this map.

## Implemented behavior

The generic JSON path:

1. opens a regular, non-symlink file without following symlinks;
2. reads at most 1,000,000 bytes;
3. decodes UTF-8 and rejects duplicate keys, non-standard numeric constants, non-finite values, excessive integer text, excessive depth, and excessive document nodes;
4. canonicalizes the admitted value with RFC 8785 JCS;
5. hashes the canonical bytes with SHA-256; and
6. formats or compares the current scalar `sha256:<hex>` value.

The structural GeoJSON profile additionally requires a declared CRS, binds coordinate precision, separates geometry and record hash domains, and makes property exclusions and optional feature-ID inclusion explicit. It deliberately does not reproject, repair topology, reorder geometries, or decide sensitivity/public-safe precision.

## Inputs, outputs, and non-effects

Allowed inputs are explicit parsed JSON values, bounded local JSON files, stored current-grammar hash records, and GeoJSON Features with declared profile parameters.

Outputs are canonical bytes, scalar digests, verification results, structural GeoJSON digest reports, and finite CLI/validator outcomes. Outputs carry `authority: NONE` where reports expose authority posture.

The package must not:

- fetch sources or use network access;
- read credentials, lifecycle stores, policy state, or model output;
- choose an object-family field projection, evidence rule, rights decision, or sensitivity transform;
- write receipts, proofs, release records, corrections, rollback records, or published artifacts;
- silently emit ADR-0013's proposed profile-tagged grammar;
- represent structural GeoJSON equality as topological, semantic, evidentiary, or public-safe equality.

## Public API boundary

The current explicit exports are the constants, error/result types, bounded loader, canonicalization and spec-hash helpers, and structural GeoJSON helpers listed by [`src/hashing/__init__.py`](src/hashing/__init__.py).

Compatibility-significant changes include the wire grammar, canonicalization dependency/profile, admitted numeric domain, loader bounds, GeoJSON profile/precision rules, public exports, distribution/import names, and CLI outcomes. Such changes require synchronized contracts/schemas where applicable, focused tests, consumer analysis, correction/rollback review, and an accepted decision when authority or compatibility changes.

## Validation

Focused repository commands are:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_spec_hash*.py' \
  --verbose

python tools/validators/validate_spec_hash.py --fixtures
```

Documentation changes also require the repository's changed-Markdown link check and relevant repository guardrails. A passing test proves only the tested profile and revision.

## Security and sensitive material

The package uses bounded parsing and sanitized finite outcomes, but callers remain responsible for minimizing inputs and excluding secrets, private source records, culturally controlled material, living-person or genomic information, precise archaeology/rare-species locations, infrastructure-sensitive detail, and other restricted content from fixtures and logs.

Hashing sensitive bytes does not make the bytes safe to publish. Digest values can also be correlatable and remain subject to the owning data and access controls.

## Open holds

- ADR-0013 remains proposed; no `sha256:` to `jcs:sha256:` migration is authorized.
- Complete producer/consumer inventory and cross-language parity remain `UNKNOWN`.
- External package publication, deployed use, service health, and independent stewardship remain `UNKNOWN` or `NEEDS VERIFICATION`.
- The separate canonicalization-document case collision remains governed by its existing hold and is not changed here.
- New hash families, RDF canonicalization, signatures, HMAC, encryption, password hashing, key management, Merkle profiles, or run-ID grammar require their own accepted scope and tests.

## Correction and rollback

Historical digests and receipts are immutable evidence of their original producer/profile. Correct a defective result through the owning correction or supersession process; do not rewrite prior records or silently reinterpret a prefix.

For a documentation-only correction, revert the documentation commit or restore the prior blobs. No data migration, package publication rollback, source shutdown, deployment rollback, or release withdrawal is implied.

## Documentation inheritance

- This file owns package maturity, package metadata/distribution posture, and the package-wide current-status summary.
- [`src/README.md`](src/README.md) owns only source placement and dependency direction.
- [`src/hashing/README.md`](src/hashing/README.md) owns only the namespace's direct modules, explicit exports, and API-local prohibitions.
- Proposal-era API sketches, migration sequences, and verification registers from v1.1 remain historical lineage in Git, not current parallel authority.

<p align="right"><a href="#top">Back to top</a></p>
