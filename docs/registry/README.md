<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registry/readme
title: docs/registry/ — Registry Documentation Boundary
type: readme
version: v1.1
status: provisional
owners:
  - "@bartytime4life"
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing
owning_root: docs/
responsibility: "Explain and navigate current registry families without becoming a registry, schema, policy, release, or publication authority."
truth_posture: "CONFIRMED current repository paths, accepted placement doctrine, and schema child routing boundary / PROPOSED deeper child documentation / NEEDS VERIFICATION child-lane ownership and intended fixture-validator dry-run scope"
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - control_plane/document_registry.yaml
  - control_plane/root_registry.yaml
  - data/registry/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/registry/` — Registry Documentation Boundary

This directory is a human-readable navigation and explanation surface for KFM
registry families. It is not a registry implementation or a second writable copy
of machine governance, governed data records, schemas, policy, or release state.

> [!IMPORTANT]
> The word “registry” describes several responsibilities in this repository. Use
> the owning path for the responsibility at hand; a document, generated index,
> passing validator, or pull request does not create authority or publication
> state.

## Choose the owning surface

| Need | Current owning surface | What that surface establishes |
|---|---|---|
| Explain or navigate registry families for people | `docs/registry/` | Documentation only |
| Project adopted governance for machines | [`control_plane/`](../../control_plane/README.md) | Machine-readable projections and indexes; projections do not create their own authority |
| Identify and route sources, datasets, domains, rights, sensitivity, layers, and crosswalks | [`data/registry/`](../../data/registry/README.md) | Governed registry records; not payload, policy, proof, release, or public-serving authority |
| Define semantic meaning and interface promises | [`contracts/`](../../contracts/README.md) | Semantic contract authority |
| Define machine-checkable shape | [`schemas/`](../../schemas/README.md) | Schema authority where declared |
| Decide allow, deny, hold, restrict, or abstain outcomes | [`policy/`](../../policy/README.md) | Normative policy authority |
| Validate or orchestrate registry checks | [`tools/`](../../tools/README.md), [`tests/`](../../tests/README.md), and [`.github/workflows/`](../../.github/workflows/) | Executable evidence and automation, not registry or release authority |

The accepted [Directory Rules v2](../doctrine/directory-rules.md), adopted by
[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md), separates
human documentation under `docs/` from machine governance projections under
`control_plane/`, governed instances under `data/`, and machine shapes under
`schemas/`.

## Current registry families

### Machine governance projections

| Projection | Current repository posture | Focused validation |
|---|---|---|
| [`control_plane/document_registry.yaml`](../../control_plane/document_registry.yaml) | `PROPOSED`, `projection_only`, `PARTIAL`; indexes document identity without accepting or superseding documents | [`control-plane-registry-packet.yml`](../../.github/workflows/control-plane-registry-packet.yml) |
| [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) | `ACTIVE`, `machine_projection_only`; projects adopted root classes without creating, activating, migrating, or retiring roots | [`directory-root-registry.yml`](../../.github/workflows/directory-root-registry.yml) |

Do not infer completeness from either projection. The document registry currently
records one conflicted, partial entry; the root registry limits its coverage to
top-level roots and adopted root classes.

### Governed data registries

[`data/registry/`](../../data/registry/README.md) contains the repository’s
governed identity and routing records. Its parent contract distinguishes source,
dataset, domain, crosswalk, rights, sensitivity, and layer records from source
captures, lifecycle payloads, semantic contracts, schemas, policy, proofs, and
release decisions.

Use the child indexes under `data/registry/` to find a specific record family.
Public clients must use a governed interface or released public-safe artifact,
not an internal registry path as a direct data service.

### Shapes, checks, and orchestration

Representative current implementation surfaces include:

- [`control_plane_registry.schema.json`](../../schemas/contracts/v1/governance/control_plane_registry.schema.json)
  and [`root_registry.schema.json`](../../schemas/contracts/v1/governance/root_registry.schema.json)
  for machine shape;
- [`validate_control_plane_registry_packet.py`](../../tools/validators/control_plane/validate_control_plane_registry_packet.py)
  and [`validate_root_registry.py`](../../tools/validators/directory_governance/validate_root_registry.py)
  for focused validation;
- [`test_validate_control_plane_registry_packet.py`](../../tests/validators/test_validate_control_plane_registry_packet.py)
  and [`test_validate_root_registry.py`](../../tests/validators/directory_governance/test_validate_root_registry.py)
  for executable regression evidence; and
- the registry-specific workflows linked above for hosted orchestration.

Schemas constrain shape, validators report findings, tests exercise known cases,
and workflows orchestrate checks. None of them independently admits a source,
resolves a governance conflict, approves policy, releases data, or publishes a
client-facing artifact.

## Reproduce the focused checks

From the repository root, use the commands exercised by the current workflows:

```bash
make control-plane-registry-packet

python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_root_registry.py' \
  --verbose
python tools/validators/directory_governance/validate_root_registry.py --fixtures
python tools/validators/directory_governance/validate_root_registry.py
```

Interpret a passing result narrowly: it confirms the exercised projection,
fixtures, and repository relationships at that revision. It does not establish
real-world truth, owner review, source admission, policy approval, release,
deployment, promotion, or publication.

## Child documentation status

[`schema/README.md`](schema/README.md) is now a substantive routing-and-hold
boundary. It directs readers to the established schema, fixture, validator, test,
policy, and package implementation roots without making `docs/registry/schema/`
an authority for those artifacts.

The deeper current paths remain placeholders, not substantive contracts:

- [`schema/fixture/README.md`](schema/fixture/README.md)
- [`schema/fixture/validator/README.md`](schema/fixture/validator/README.md)

The nested `schema/fixture/validator/policy/dry-run/` path contains only a
`.gitkeep` marker. Do not infer a fixture contract, validator policy, dry-run
capability, consumer, or accepted placement decision from these paths. Before
expanding a child README, identify the current owning implementation and keep
canonical schema, fixture, validator, and policy content in their established
authority roots.

## Maintenance and correction

Update this guide when a registry family, authority boundary, canonical path, or
focused validation entry point changes. Verify claims against current repository
files and accepted doctrine; treat external plans and generated prose as lineage
or proposals until repository evidence and governance establish otherwise.

If this guide conflicts with an owning artifact, preserve the owning artifact’s
state, label the conflict, and correct this documentation through review. Revert
the documentation commit to roll back this guide; that action does not roll back
any registry record, policy decision, release, deployment, or publication.

[Back to `docs/`](../README.md) · [Back to top](#top)
