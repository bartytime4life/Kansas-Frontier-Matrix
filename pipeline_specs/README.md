<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-readme
title: pipeline_specs/ — Declarative Pipeline Specification Authority
type: readme
version: v1.0
status: governed; proposed-inactive-corpus; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-05-02
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-secrets; no-live-activation
owning_root: pipeline_specs/
responsibility: canonical declarative pipeline specification authority; executable behavior remains under pipelines/
truth_posture: CONFIRMED placement and inactive corpus / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: ROOT_FULL
current_path: pipeline_specs/README.md
related:
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Declarative Pipeline Specification Authority

`pipeline_specs/` is the canonical repository root for declarative descriptions of
**what a pipeline may run**: candidate stages, inputs, outputs, source and contract
references, resource or execution envelopes, schedules when established, and required
governance gates. Executable code belongs under [`pipelines/`](../pipelines/README.md).

Directory placement, parsing success, a valid hash, or a passing workflow never activates
a source or pipeline. Every YAML declaration currently in this root is
`PROPOSED_INACTIVE` and denies live network access, source activation, lifecycle writes,
promotion, release, and publication.

## Authority, adoption, and conformance

- **Root class:** canonical implementation-and-operations support root; declarative only.
- **Authority owner:** repository maintainers with pipeline, domain, evidence, policy,
  validation, and release review.
- **Placement authority:** accepted
  [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the
  adopted [`Directory Rules v2`](../docs/doctrine/directory-rules.md).
- **Semantic authority:**
  [`contracts/pipeline_spec_declaration.md`](../contracts/pipeline_spec_declaration.md).
- **Machine shape:**
  [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../schemas/contracts/v1/pipeline_spec_declaration.schema.json).
- **Current conformance:** all 110 YAML declarations use the common closed contract. The
  nine JSON profiles retain their narrower established contracts, schemas, fixtures,
  validators, and workflows; this README does not collapse those object families.

The historical architecture copy at `docs/architecture/directory-rules.md` is a read-only
compatibility tombstone. It is not the current doctrine authority.

## What belongs

- inactive stage-boundary declarations;
- inactive source-specific or derived pipeline candidates;
- explicit compatibility aliases with one canonical target and no write authority;
- reviewed references to admitted source descriptors, semantic contracts, schemas,
  implementations, fixtures, tests, and workflows;
- candidate lifecycle edges and required gate names;
- deterministic declaration identities, versions, hashes, and rollback posture.

## What is prohibited

- executable pipeline logic, connector code, or embedded scripts;
- credentials, tokens, private endpoints, or secret-bearing configuration;
- unreviewed source activation, schedules, or live-network permission;
- direct writes to `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `PUBLISHED`,
  proof, or release surfaces;
- evidence closure, policy approval, promotion, release, deployment, or publication;
- a second writable authority under `pipelines/specs/` or a compatibility lane;
- inferred activation from discovery, filename, directory membership, or parse success.

## Inputs, outputs, and writers

Inputs are reviewable references and candidate lifecycle states. Outputs are inert
declarations consumed by validators and, only after separate accepted decisions, by an
approved orchestrator. The current declarations write no lifecycle targets.

Permitted writers are reviewed repository changes. Runtime processes and source
connectors may read an accepted declaration only after a separate activation mechanism is
established; no such root-wide activation registry is created here.

The conceptual lifecycle remains:

```text
RAW → WORK or QUARANTINE → PROCESSED → CATALOG or TRIPLET → PUBLISHED
```

Candidate edges in a declaration describe possible placement only. They do not prove an
artifact exists or authorize a transition.

## Exposure and sensitivity

The declaration files are public repository metadata and must contain no secrets or
sensitive payloads. Domain data may still be restricted. Archaeological sites, individual
or genetic identity, exact land ownership or residence, vulnerable species, critical
habitat, private operators, and safety-sensitive infrastructure fail closed unless their
own policy and release families explicitly permit a safer representation.

KFM is not an emergency-alerting, engineering, navigation, regulatory-determination, or
life-safety authority. A pipeline declaration must not imply otherwise.

## Mutation, retention, generation, and storage

- YAML and JSON declarations are reviewed source artifacts retained in Git history.
- `spec_hash` binds canonical declaration content; it is not evidence or a release digest.
- YAML declarations are hand-reviewed or deterministically migrated, never runtime output.
- Generated payloads, caches, receipts, proofs, and releases stay in their owning roots.
- Correction or rollback reverts the declaration change and leaves prior history visible.
- Source data bytes and long-lived external storage do not belong in this root.

## Current inventory

| Object family | Count | Posture |
|---|---:|---|
| `KfmPipelineSpecDeclaration` YAML | 110 | 65 stage boundaries, 39 candidates, 6 compatibility aliases; all inactive |
| Schema-backed JSON profiles | 9 | `PROPOSED_INACTIVE`; governed by their established domain or watcher bundles |
| Boundary READMEs | 23 | One root boundary and 22 lane or sub-lane boundaries; each local contract owns its profile |
| `.gitkeep` markers | 0 | Removed where a boundary README already materializes the lane |

Exactly one YAML candidate, Hydrology WBD HUC12, is
`IMPLEMENTED_FIXTURE_FIRST`. It remains `FIXTURE_ONLY`, no-network, non-writing, and
inactive. The other 109 YAML declarations are `NOT_IMPLEMENTED`.

Compatibility YAML is limited to the five Archaeology `*.spec.yaml` aliases and
`hydrology/ingest_wbd.yaml`. The documentation-only compatibility lanes `air/`,
`people/`, and `settlement/` remain non-writable navigation boundaries.

## Direct-child map

Verified against repository contents on 2026-08-30. Only direct children are shown;
each child README owns deeper detail.

```text
pipeline_specs/
├── agriculture/                 # Agriculture declarations
├── air/                         # Proposed compatibility boundary; target unresolved
├── archaeology/                 # Archaeology declarations and compatibility aliases
├── atmosphere/                  # Atmosphere declarations
├── fauna/                       # Fauna declarations and local watcher boundary
├── flora/                       # Flora declarations and source-readiness profile
├── geology/                     # Geology declarations
├── habitat/                     # Habitat declarations and object-family boundaries
├── hazards/                     # Hazards declarations
├── hydrology/                   # Hydrology declarations and fixture-first WBD binding
├── people/                      # Proposed compatibility boundary; target unregistered
├── people-dna-land/             # Sensitive human, identity, and land declarations
├── roads-rail-trade/            # Transportation and trade declarations
├── settlement/                  # Proposed compatibility boundary; target unresolved
├── settlements-infrastructure/ # Settlement and infrastructure declarations
├── soil/                        # Soil declarations and domain-specific JSON profiles
└── watchers/                    # Shared inactive watcher declarations and profiles
```

## Validation and negative checks

Run the bounded, no-network validator and fixture suite:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python tools/validators/validate_pipeline_spec_declarations.py --fixtures
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q --strict-config --strict-markers
```

The dedicated
[`pipeline-spec-declarations`](../.github/workflows/pipeline-spec-declarations.yml)
workflow checks all material surfaces. Validation rejects malformed or multi-document
YAML, duplicate keys, aliases, non-finite values, symlinks, unknown fields, hash drift,
path mismatch, missing references, duplicate identities, alias chains, and any relaxed
execution or write posture.

A pass proves only declaration shape, reference existence, deterministic identity, and
the explicit inactive safety envelope. It proves no external truth, freshness, evidence
closure, policy decision, lifecycle transition, or release state.

## Owners, reviewers, and escalation

`OWNER_TBD` remains explicit until CODEOWNERS and domain-steward assignments are verified.
Changes require repository-maintainer review plus the affected domain and validation
reviewers. Source, rights, sensitivity, evidence, or release changes also require the
corresponding specialist reviewer. Escalate authority conflicts through an ADR; do not
resolve them by adding a parallel path.

## Governing decisions, aliases, and migration

- ADR-0029 adopts Directory Rules v2 as placement law.
- `pipeline_specs/` owns declarations; `pipelines/` owns executable behavior.
- `air/`, `people/`, and `settlement/` are bounded documentation-only proposed
  compatibility lanes. Their target mappings remain unresolved or pending accepted
  registration; none is a second writable authority.
- Archaeology legacy `*.spec.yaml` files are explicit one-hop aliases.
- `hydrology/ingest_wbd.yaml` is an explicit one-hop alias to the fixture-first WBD HUC12
  declaration.
- Flora watcher and NHDPlus naming/placement overlaps remain `HOLD` with
  `PLACEMENT_REVIEW_REQUIRED`; this migration does not invent a canonical target.

Rollback is a normal Git revert of the bounded declaration or documentation commit.
Rollback does not restore source activation, runtime state, or published data because this
root has authority over none of those effects.

## Last evidence review and triggers

Last evidence review: 2026-08-30 against the then-current `main` tree, accepted ADR-0029,
the adopted Directory Rules, established domain contracts and workflows, and the
repository-backed declaration inventory.

Re-review this root when authority, root class, writer, consumer, exposure, sensitivity,
storage, schema, validator, CODEOWNERS coverage, compatibility target, or activation model
changes; when an ADR is accepted or superseded; or when drift, security, correction,
withdrawal, rollback, or release behavior changes.

Open verification items:

- assign and verify human owners and CODEOWNERS coverage;
- decide the flora/shared-watcher and Hydrology NHDPlus placement holds;
- define a separate activation registry only through an accepted authority decision;
- bind the 109 unimplemented declarations only with source, contract, policy, fixture,
  test, workflow, evidence, and release review.
