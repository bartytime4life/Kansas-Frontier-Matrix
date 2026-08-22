<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/control-plane-registry-packet/v1
title: Normalized Control-Plane Registry Packet Contract
type: semantic-contract
version: v1.0.0
status: proposed; repository-grounded; schema-backed; implementation-partial; non-authoritative
owners:
  - UNKNOWN
created: 2026-08-22
updated: 2026-08-22
policy_label: internal-governance; projection-only; cite-or-abstain; fail-closed
owning_root: contracts/
responsibility: define one common semantic envelope for seven existing legacy control-plane registry projections without creating a parallel registry home inventing owners activating sources approving policy changing lifecycle or release state or publishing
truth_posture: CONFIRMED seven existing canonical registry paths one populated document index six empty bodies accepted Directory Rules and inherited metadata tests / PROPOSED this normalized common contract schema validator fixture test and workflow packet / UNKNOWN accountable field-level owners external consumers and production use / NEEDS VERIFICATION human review and hosted exact-head results
related:
  - ../../schemas/contracts/v1/governance/control_plane_registry.schema.json
  - ../../control_plane/document_registry.yaml
  - ../../control_plane/source_authority_register.yaml
  - ../../control_plane/policy_gate_register.yaml
  - ../../control_plane/release_state_register.yaml
  - ../../control_plane/verification_backlog.yaml
  - ../../control_plane/contradiction_register.yaml
  - ../../control_plane/deprecation_register.yaml
  - ../../tools/validators/control_plane/validate_control_plane_registry_packet.py
  - ../../fixtures/contracts/v1/governance/control_plane_registry/README.md
  - ../../tests/validators/test_validate_control_plane_registry_packet.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This packet implements MRTS-02 and preserves the existing seven canonical paths."
  - "UNKNOWN is an explicit evidence state and never a wildcard permission."
  - "An empty registry is ABSENT for population and cannot be read as proof that no objects or problems exist."
[/KFM_META_BLOCK_V2] -->

# Normalized Control-Plane Registry Packet Contract

## Purpose

This contract gives seven existing `control_plane/` registry projections one common, schema-backed envelope while preserving their canonical paths:

1. `document_registry.yaml`
2. `source_authority_register.yaml`
3. `policy_gate_register.yaml`
4. `release_state_register.yaml`
5. `verification_backlog.yaml`
6. `contradiction_register.yaml`
7. `deprecation_register.yaml`

The packet indexes repository relationships and observed state. It does not move the authority-bearing document, source, policy, evidence, verification, contradiction resolution, deprecation decision, release decision, correction, withdrawal, or rollback object into `control_plane/`.

## Authority boundary

| Registry | May index | Cannot decide |
| --- | --- | --- |
| Document registry | Stable document ID, path, digest, observed authority/implementation state | Doctrine or document authority |
| Source authority register | Source descriptor, rights, role, sensitivity, and activation references | Source identity, rights, admission, or activation |
| Policy gate register | Gate identity, policy decision reference, and observed outcome | Policy source, allow/deny/hold, or bypass |
| Release state register | Release, promotion, correction, withdrawal, and rollback references | Release approval or lifecycle mutation |
| Verification backlog | Unresolved claim, evidence needed, owner state, and review target | Verification closure |
| Contradiction register | Conflicting claims, evidence, affected subjects, and resolution route | Which claim wins |
| Deprecation register | Deprecated subject, replacement, consumers, decision, and exit state | Deprecation, retirement, migration, or deletion |

Every instance must declare `authority_mode: projection_only`. Schema or validator success proves only the bounded projection contract.

## Common envelope

Each registry keeps the legacy `meta` block required by current repository consumers and adds:

- `schema_version: 1.0.0`;
- stable `registry_id` matching the canonical filename;
- `status: PROPOSED`;
- `authority_mode: projection_only`;
- implementation and completeness state;
- exact implementation-base commit;
- evidence-backed `owner_role`, including literal `UNKNOWN`;
- sorted, unique non-effects;
- a canonically ordered entry array.

The shared schema is [`control_plane_registry.schema.json`](../../schemas/contracts/v1/governance/control_plane_registry.schema.json). One schema is used for all seven instances; no second register root or compatibility mirror is introduced.

## Population and truth states

Completeness and implementation are coupled:

| Completeness | Required implementation state | Entry count | Meaning |
| --- | --- | ---: | --- |
| `empty` | `ABSENT` | 0 | Canonical path exists, but no entry population is implemented. |
| `partial` | `PARTIAL`, `CONFLICTED`, or `DEPRECATED` | 1+ | Some bounded entries exist; global completeness is not claimed. |
| `complete` | `IMPLEMENTED` | 1+ | Allowed by the schema but requires separate evidence and review; no current instance claims it. |

An empty contradiction register does not prove that no contradictions exist. An empty verification backlog does not prove closure. The same rule applies to sources, policy gates, release state, and deprecations.

`UNKNOWN` is allowed only as an explicit evidence gap. It grants no permissions and cannot satisfy a material governing-reference or source-digest requirement.

## Entry contract

Every populated entry declares:

- stable `entry_id` and `subject_id`;
- bounded kind;
- canonical repository-relative subject path and SHA-256;
- separate authority and implementation states;
- owner role or `UNKNOWN`;
- sorted governing references and source digests;
- sorted reason codes;
- bounded notes.

Entries with `CONFIRMED` or `CONFLICTED` authority state are material and require at least one governing reference and source digest. Every path must remain inside the repository and resolve to a regular non-symlink file. Every pinned path digest is replayed.

## Current normalization result

The document registry retains its one historical entry but corrects an overclaim: the referenced `document_registry_doctrine_required.yaml` declares `PROPOSED`, while the prior index entry declared `CONFIRMED`. The normalized entry therefore records `authority_status: CONFLICTED`, exact bytes, and reason codes. The projection does not resolve the document's authority.

The other six registries remain empty and are now explicitly `ABSENT` for population. Their owners remain `UNKNOWN`; no identity is invented to make the packet appear complete.

## Deterministic validation

Run:

```bash
python tools/validators/control_plane/validate_control_plane_registry_packet.py
python tools/validators/control_plane/validate_control_plane_registry_packet.py --fixtures
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_control_plane_registry_packet.py' \
  --verbose
```

The profile checks:

- safe YAML parsing with duplicate-key and non-finite-number rejection;
- Draft 2020-12 shape and format constraints;
- exact canonical packet membership and registry/file identity;
- stable ID ordering and uniqueness;
- completeness/population consistency;
- `UNKNOWN` owner consistency;
- governing-reference and source-digest requirements for material claims;
- repository path containment, existence, regular-file status, and SHA-256 replay;
- required non-effects;
- exact fixture polarity.

After declared dependencies are installed, the profile performs no network calls.

## Failure and correction

Malformed input, duplicate IDs, unknown fields, self-authority, unresolved references, digest mismatch, incomplete material authority, noncanonical ordering, or packet-member omission fails closed.

Correction uses the same seven canonical paths. Preserve stable IDs and reason/evidence lineage. Before merge, close the draft change. After an authorized merge, apply a transparent revert or same-path forward fix with a new receipt. Do not create `control_plane/registers/` copies or compatibility mirrors to avoid correction.

## Non-effects

This packet does not:

- create document, source, policy, evidence, review, verification, contradiction-resolution, deprecation, release, correction, withdrawal, rollback, deployment, or publication authority;
- activate or admit a source;
- execute or bypass policy;
- mark verification complete;
- resolve or hide a contradiction;
- deprecate, retire, migrate, or delete a path;
- approve release, promotion, rollback, deployment, or publication;
- prove any external consumer or production behavior.
