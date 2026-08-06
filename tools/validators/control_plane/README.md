<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools/validators/control-plane/object-family-register/v1
title: Object Family Register Validator
type: validator-readme
version: 1.0.0
status: PROPOSED
owners:
  - OWNER_TBD — Control-plane steward
  - OWNER_TBD — Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; control-plane; validator; no-network
related:
  - ../../../control_plane/object_family_register.yaml
  - ../../../docs/registers/OBJECT_FAMILY.md
  - ../../../schemas/contracts/v1/governance/object_family_register.schema.json
  - ../../../fixtures/contracts/v1/governance/object_family_register/README.md
notes:
  - "The register is a navigational index only and never creates family authority."
[/KFM_META_BLOCK_V2] -->

# Object family register validator

`validate_object_family_register.py` checks the machine-readable object-family index without network access.

The `.yaml` file intentionally uses the JSON-compatible subset of YAML. This keeps parsing deterministic and dependency-free while remaining valid YAML 1.2.

## Checks

- Draft 2020-12 schema shape;
- duplicate-key and non-finite-number rejection;
- canonical family and path ordering;
- unique family IDs;
- responsibility-root placement for each declared path role;
- declared-path existence in the tested checkout;
- deterministic `seed`, `partial`, `covered`, or `hardened` maturity classification;
- bounded diagnostics that never echo registry values.

## Commands

```bash
python tools/validators/control_plane/validate_object_family_register.py
python tools/validators/control_plane/validate_object_family_register.py --fixtures
```

A PASS means only that the index is internally consistent with observed repository paths. It does not add, rename, remove, approve, release, or publish an object family; it does not override contracts, schemas, policy, evidence, reviews, or release records.
