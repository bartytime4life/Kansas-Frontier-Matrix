<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/packages-hashing-src-readme
title: packages/hashing/src/ — Inherited Source Envelope
type: readme
version: v1.2
status: draft; repository-grounded; inherited
owners:
  - "@bartytime4life — verified CODEOWNERS review route; package stewardship remains NEEDS VERIFICATION"
created: 2026-07-15
updated: 2026-08-25
policy_label: "repository-facing; source-envelope; no-network; no-authority"
owning_root: packages/
inherited_parent: ../README.md
responsibility: "Document only source placement, direct-child structure, and dependency direction beneath packages/hashing/."
truth_posture: "CONFIRMED populated source envelope inheriting current package status from ../README.md / no independent contract, schema, policy, maturity, migration, release, or publication authority"
evidence_snapshot: "main@52d83c0233bef201587ec8a7b9d0c0a7a0c1493f; prior README e54dc45019f0df1761e03abf02bfa909a05621b5; parent prior README 3d3174974668623117c1f90bcbc6918262d1b6af; Directory Rules fd49a0b83e55cef52c1124281f093e263526898d"
related:
  - ../README.md
  - hashing/README.md
  - hashing/__init__.py
  - hashing/core.py
  - hashing/geojson.py
  - hashing/cli.py
notes:
  - "Package maturity, metadata, validation, workflow, compatibility, and distribution status are owned by ../README.md."
  - "The v1.1 proposal and migration detail remains available in Git history and is not repeated here."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `packages/hashing/src/` — inherited source envelope

> Source placement boundary for the reusable hashing package. Current implementation status is owned by the [package README](../README.md) and is not duplicated here.

## Purpose and inheritance

This directory inherits the package's authority, maturity, security, compatibility, validation, and rollback posture. It exists to keep the Python `src` layout and dependency direction explicit.

It is a `LEAF_INHERITED` directory under Directory Rules §16: it does not create an independent package, API, canonicalization standard, semantic contract, schema, policy, receipt, proof, release, or publication boundary.

## Current direct children

```text
packages/hashing/src/
├── README.md  # inherited source-placement boundary (this file)
└── hashing/   # import namespace and implementation modules
```

The child namespace README owns deeper module and export detail.

## Belongs here

- reusable, deterministic, package-internal Python implementation;
- explicit value/result types and fail-closed errors;
- bounded input admission, canonicalization, digest, comparison, and declared structural-profile helpers;
- package-local CLI implementation when exposed through reviewed package metadata;
- minimal explicit namespace exports.

## Prohibited here

- semantic contract or schema authority;
- policy, evidence, review, promotion, release, correction, rollback, or publication decisions;
- source acquisition, deployment handlers, UI/public endpoints, pipeline orchestration, or lifecycle persistence;
- hidden network, credential, environment, clock, randomness, filesystem-scan, telemetry, or model effects;
- a second implementation of behavior already owned by another module or tool;
- silent compatibility conversion or adoption of proposed ADR grammar.

## Dependency direction

Implementation modules may use the standard library and dependencies declared in [`pyproject.toml`](../pyproject.toml). Repository tools, validators, and governed consumers may import the package; package implementation must not import those orchestration or authority layers back into itself.

```text
contracts / schemas / accepted guidance
                  ↓ constrain
packages/hashing/src/hashing
                  ↓ reused by
tools / validators / governed consumers
```

The arrows do not transfer authority. Callers remain responsible for object-family projection, admissibility, evidence, rights, sensitivity, persistence, and release consequences.

## Validation and changes

Use the focused commands and compatibility rules in the [package README](../README.md). A source change must update the parent status summary and the namespace README only when its documented exports or local boundary change.

Rollback this documentation through a reviewed revert or forward correction. Historical proposal detail remains in Git history; no lifecycle or operational rollback is created by this file.

<p align="right"><a href="#top">Back to top</a></p>
