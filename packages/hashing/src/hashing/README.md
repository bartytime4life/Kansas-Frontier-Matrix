<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-hashing-src-hashing-readme
title: packages/hashing/src/hashing/ — Import and API Boundary
type: readme
version: v1.2
status: draft; repository-grounded; bounded-implementation; inherited
owners:
  - "@bartytime4life — verified CODEOWNERS review route; package stewardship remains NEEDS VERIFICATION"
created: 2026-07-15
updated: 2026-08-25
policy_label: "repository-facing; import-boundary; deterministic-hashing; no-network; fail-closed; no-authority"
owning_root: packages/
inherited_parent: ../../README.md
responsibility: "Document only the current hashing import namespace, direct modules, explicit exports, input/output boundary, and API-local prohibitions."
truth_posture: "CONFIRMED explicit core and structural GeoJSON exports plus package CLI / inherits package maturity, compatibility, validation, distribution, and rollback status from ../../README.md / no semantic, schema, policy, evidence, release, or publication authority"
evidence_snapshot: "main@52d83c0233bef201587ec8a7b9d0c0a7a0c1493f; prior README 05a1320e395ad3b1e64ff72f16c844a5e43c3441; core a609eac44b1a5f24bd9ba449afedfeec7dd17e8e; GeoJSON 2db35caf8aa0bb8ff0c582e03c1a57b1caf8e358; CLI 860b7f04ad6b4ab2144ed61fb896100e1a8577bc; exports 676ddec2ede8dd3cba3b6eb73e647d876d5e1fe4; Directory Rules fd49a0b83e55cef52c1124281f093e263526898d"
related:
  - ../../README.md
  - ../README.md
  - __init__.py
  - core.py
  - geojson.py
  - cli.py
  - ../../../../contracts/common/spec_hash.md
  - ../../../../schemas/contracts/v1/common/spec_hash.schema.json
  - ../../../../tools/spec_hash/README.md
  - ../../../../tests/validators/test_validate_spec_hash.py
  - ../../../../tests/validators/test_validate_spec_hash_geojson.py
notes:
  - "This file does not repeat package-wide implementation, workflow, distribution, migration, or rollback status."
  - "Earlier proposed API sketches and reason-code inventories remain lineage in Git history, not current exports."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `packages/hashing/src/hashing/` — import and API boundary

> Current Python import namespace for the bounded hashing implementation. Package-wide status and compatibility posture are owned by [`packages/hashing/README.md`](../../README.md).

> [!WARNING]
> These helpers return integrity facts only. No result grants truth, evidence, policy, review, promotion, release, publication, or public-use authority.

## Inheritance and scope

This `LEAF_INHERITED` README documents only direct modules, explicit exports, admitted inputs and outputs, and API-local prohibitions. It does not define `spec_hash` meaning or shape and does not adopt ADR-0013's proposed `jcs:sha256:` grammar.

## Current direct modules

```text
packages/hashing/src/hashing/
├── README.md    # import/API boundary (this file)
├── __init__.py  # explicit public exports
├── cli.py       # compute, verify, and GeoJSON command handling
├── core.py      # bounded JSON admission, JCS, SHA-256, comparison
└── geojson.py   # structural GeoJSON feature digest profile
```

## Public exports

[`__init__.py`](__init__.py) currently exports:

- profile and algorithm constants;
- `SpecHashError`, input/canonicalization/format errors, and `VerificationResult`;
- `load_json_file`, `canonicalize_json`, `compute_spec_hash`, `is_valid_spec_hash`, and `verify_spec_hash`;
- structural GeoJSON constants, result/error types, normalization, geometry hashing, and feature-digest helpers.

Exports are deliberate but bounded. Their presence does not establish external software distribution, production support, or cross-language parity.

## Core API behavior

[`core.py`](core.py) implements:

- safe regular-file JSON admission with explicit byte, depth, node, duplicate-key, Unicode, and numeric controls;
- RFC 8785 JCS canonicalization through the pinned package dependency;
- SHA-256 scalar output using the current `sha256:<64 lowercase hex>` grammar;
- current-grammar validation; and
- constant-time stored-versus-recomputed comparison.

The generic API does not select object-family fields, exclusions, normalization, CRS, precision, rights, sensitivity, or policy.

## Structural GeoJSON profile

[`geojson.py`](geojson.py) implements `kfm-geojson-feature-digest-v1` with:

- explicit CRS and coordinate precision;
- bounded geometry nesting and coordinate counts;
- deterministic coordinate quantization;
- separate geometry and record subjects;
- sorted, explicit property exclusions; and
- optional feature-ID inclusion.

It deliberately preserves coordinate and collection order and does not reproject, repair topology, normalize ring direction, sort multipart geometries, establish spatial truth, or determine safe publication precision.

## CLI outcomes

[`cli.py`](cli.py) exposes `compute`, `verify`, and `geojson-feature`. Reports include a finite status, declared profile/algorithm, `authority: NONE`, and explicit non-effects. Invalid input, unsupported structure, canonicalization failure, malformed stored hashes, and structural GeoJSON failure return bounded non-success outcomes.

## API-local prohibitions

Code in this namespace must not:

- infer a missing hash domain or canonicalization profile;
- silently translate between current and proposed digest grammars;
- fetch remote content or resolve remote JSON-LD contexts;
- scan ambient directories or read hidden environment/credential state;
- echo full sensitive payloads in errors or logs;
- write lifecycle, evidence, receipt, proof, policy, review, correction, release, rollback, or publication records;
- map a match into an authority decision;
- add HMAC, signing, encryption, password hashing, key management, RDF canonicalization, Merkle, or run-ID behavior without an accepted bounded contract and tests.

## Validation and compatibility

Focused tests, fixture validation, workflow coverage, compatibility-significant changes, open holds, and rollback are documented once in the [package status owner](../../README.md).

When exports or module-local behavior change, update this file in the same dependency-closed slice. When only package maturity, workflow, distribution, or consumer posture changes, update the parent rather than duplicating status here.

<p align="right"><a href="#top">Back to top</a></p>
