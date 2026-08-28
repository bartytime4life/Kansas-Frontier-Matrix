<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/root-artifacts-readme
title: artifacts/ — Transitional Generated-Output Compatibility Root
type: readme
subtype: compatibility-root-landing-page
version: v0.4
prior_version: v0.3
status: draft; repository-grounded; compatibility; transitional; non-authoritative; conformance-hold
owner: "NEEDS VERIFICATION — CODEOWNERS routes repository review to @bartytime4life; no accepted artifacts steward, independent review requirement, retention owner, or migration authority was verified"
created: 2026-05-10
updated: 2026-08-08
policy_label: public
current_path: artifacts/README.md
owning_root: artifacts/
responsibility: define the temporary generated-output compatibility boundary, expose current conformance drift, and route durable or trust-bearing objects to their canonical responsibility roots
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION]
authority_class: compatibility root landing page
authority_rank: non-authoritative generated-output boundary subordinate to accepted Directory Rules, canonical responsibility roots, lifecycle records, evidence, policy, review, and release records
canonical_relationship: same-path update; no sibling authority created
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: d20c341149d43057c6540c499b9222bc4ac11460
  root_tree: 28f01907bb89386a6be3c515f3e24e33d032f5ea
  artifacts_tree_pre_edit: 39505667873ae68e6553aa2a47c270ffd2e10842
  target_prior_blob: 7b2acc0c296daadb430370cdc803b487933487ae
  target_prior_bytes: 33109
  tracked_files_pre_edit: 44
  tracked_child_bytes: 714240
  tracked_total_bytes_pre_edit: 747349
  build_tree: 35dd905857279c9397cad07baf7c37ef94429088
  docs_tree: a2e9b255d7cb095fa7dc9c0973ef860140fc8443
  qa_tree: c1fcc314b959b7bb14980bc627a28fa41d51c3f8
  release_tree: bd3923652bfabf1bafbef7fd6453e8f81c689cd3
  temporary_tree: 38baa602791bf34848b604096b7ee24f44a3416d
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption: ADR-0029; accepted
  root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
  drift_register_blob: 5c5078b93c467e66f4cc8b86a7a696dbce5ae7e0
  maplibre_perf_workflow_blob: 7608953fac56d2ac3e077a4e501f9d0521d6187e
  maplibre_proof_builder_blob: 8396c912a75c803baf8a92abe7a2f8cad582ba41
related:
  - ../README.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/architecture/directory-rules.md
  - ../control_plane/root_registry.yaml
  - ../docs/registers/DRIFT_REGISTER.md
  - build/README.md
  - docs/README.md
  - qa/README.md
  - release/README.md
  - temporary/README.md
  - ../data/receipts/
  - ../data/proofs/
  - ../data/catalog/
  - ../data/published/
  - ../release/
tags: [kfm, artifacts, compatibility-root, transitional, generated-output, trust-boundary, drift, retention, rollback]
notes:
  - "v0.4 replaces the obsolete Directory Rules identity-conflict posture with accepted ADR-0029 and the canonical doctrine path."
  - "v0.4 repins the exact tracked tree, corrects the stale byte inventory, and distinguishes current hosted-workflow behavior from manually invokable scripts that still target artifacts/perf/."
  - "The root remains on conformance HOLD because tracked artifacts/release/ violates the adopted direct-child allowlist and dormant/manual scripts can still create trust-shaped staging beneath artifacts/perf/."
  - "This update changes documentation only; it does not migrate, delete, generate, upload, release, promote, deploy, or publish any artifact."
[/KFM_META_BLOCK_V2] -->

<!-- KFM-DOC-GRAPH-HINT
This README is parseable. Keep the metadata, current-tree inventory, root-registry
projection, drift record, validation claims, and rollback instructions synchronized
whenever this compatibility boundary changes materially.
-->

<a id="top"></a>

<div align="center">

# `artifacts/`

**Transitional compatibility root for disposable generated output—never a truth, evidence, receipt, proof, catalog, release, or publication authority.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: compatibility](https://img.shields.io/badge/authority-compatibility-d97706?style=flat-square)](#authority-level)
[![Directory Rules: ADR-0029 accepted](https://img.shields.io/badge/directory%20rules-ADR--0029%20accepted-2da44e?style=flat-square)](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
[![Allowed lanes: four](https://img.shields.io/badge/allowed%20lanes-4-0969da?style=flat-square)](#what-belongs-here)
[![Trust payloads: denied](https://img.shields.io/badge/trust%20payloads-denied-b42318?style=flat-square)](#what-does-not-belong-here)
[![Conformance: HOLD](https://img.shields.io/badge/conformance-HOLD-b42318?style=flat-square)](#status)
[![Tracked files: 44](https://img.shields.io/badge/tracked%20files-44-6e7781?style=flat-square)](#tracked-tree-inventory)
[![Exposure: internal](https://img.shields.io/badge/exposure-internal-6e7781?style=flat-square)](#public-exposure-and-sensitivity)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Tree](#direct-child-directory-map) · [Drift](#current-drift-and-migration-state) · [Rollback](#correction-and-rollback)

</div>

> [!IMPORTANT]
> `artifacts/` is a **compatibility root** for generated build output, documentation previews, QA output, and temporary working files. It does not own KFM truth, semantic meaning, machine shape, policy, lifecycle state, evidence, receipts, proofs, catalog records, release decisions, or published carriers.

> [!CAUTION]
> The tracked tree remains on **conformance HOLD**. `artifacts/release/` is a fifth direct child outside the adopted four-lane allowlist. Repository-owned MapLibre scripts can also create an untracked `artifacts/perf/` lane containing trust-shaped filenames when invoked manually. Neither location acquires authority from its name, generator, signature, or test result.

> [!NOTE]
> ADR-0029 is accepted. [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) is the sole writable human Directory Rules authority. The architecture-path copy is a read-only compatibility dependency pending its governed tombstone migration; it is not a second editable authority.

---

## Purpose

`artifacts/` isolates **derived, regenerable, non-authoritative output** from canonical source, lifecycle, evidence, policy, and release roots.

Its bounded purposes are:

- stage compiled output and replaceable distributables;
- stage generated documentation previews;
- retain small QA, lint, coverage, validation, and render-inspection outputs when repository tracking is intentional;
- hold ephemeral working files that are safe to delete or regenerate;
- support a controlled transition toward external CI artifact storage without creating another authority plane.

A generated file that becomes durable, trust-bearing, release-bearing, or consumed by standard clients must leave this compatibility root and enter its canonical family through a reviewed migration or governed producer change.

### Terms used here

| Term | Meaning |
|---|---|
| **Generated output** | Rebuildable output derived from declared source inputs and a named generator. |
| **Compatibility root** | A noncanonical path retained for a bounded transition or verified downstream need. |
| **Trust-bearing object** | Evidence, receipt, proof, catalog, policy, review, release, correction, rollback, or published object on which a consequential decision depends. |
| **Staging** | Disposable intermediate output whose path does not grant authority. |
| **Promotion** | A governed state transition supported by evidence, policy, review, release, correction, and rollback—not a copy, commit, merge, upload, or filename. |
| **External CI artifact** | A run-scoped hosted artifact governed by CI retention/access policy; still not KFM publication. |

## Authority level

**Compatibility / transitional / generated / internal / non-authoritative.**

The accepted Directory Rules and their machine projection establish the following boundary:

| Attribute | Current posture | Evidence-bounded effect |
|---|---|---|
| Root class | `compatibility` | No independent authority and no expansion by README alone |
| Allowed artifact kind | `generated_output` | Source-of-record and trust-bearing objects are excluded |
| Canonical transition target | `external://ci-artifacts` | A projected long-term direction, not migration authority |
| Exposure | `internal` | No standard public-client path |
| Mutation | `generated` | Outputs should come from declared generators, not hand edits |
| Retention | `temporary_or_ci_policy` | Durable/audit-bound objects must graduate elsewhere |
| Validation profiles | `no_independent_writes`, `no_trust_payloads` | Direct authority and trust payloads fail closed |
| Exit condition | `zero_trust_payloads_and_external_ci_storage_ready` | Retirement or cutover still requires reviewed evidence |

The machine Root Registry is a projection of accepted doctrine. Editing it or this README cannot authorize a migration, release, publication, root retirement, or destructive cleanup.

### Explicit non-authorities

| Question | Answer |
|---|---|
| Defines object meaning? | No—`contracts/` owns semantic meaning. |
| Defines machine shape? | No—`schemas/` owns machine-checkable shape. |
| Decides allow, deny, hold, restrict, or abstain? | No—`policy/` owns normative rules. |
| Holds lifecycle or registry truth? | No—`data/` owns governed instances. |
| Owns receipts, proofs, catalogs, or published artifacts? | No—canonical `data/` lanes own them. |
| Approves release, correction, withdrawal, or rollback? | No—`release/` owns decision records. |
| Serves standard public clients? | No—clients use governed APIs and released public-safe carriers. |
| Becomes authoritative when signed or uploaded? | No—authority follows object family, review, and lifecycle closure. |

## Status

**CONFIRMED tracked root / active compatibility projection / mixed child maturity / conformance `HOLD`.**

This edition is pinned to `main@d20c341149d43057c6540c499b9222bc4ac11460` and the pre-edit artifacts tree `39505667873ae68e6553aa2a47c270ffd2e10842`. It describes tracked repository state and directly inspected source definitions. It does not establish ignored or untracked runtime contents, CI artifact retention, deployment, hosted previews, public consumers, or production operation.

### Current conformance matrix

| Surface | Truth | Current state | Disposition |
|---|---|---|---|
| Root README | CONFIRMED | Same-path compatibility contract | Update in place |
| `build/` | CONFIRMED | Permitted lane with README-heavy, mixed-maturity scaffolding | Retain within generated-output boundary |
| `docs/` | CONFIRMED | Permitted lane; direct tracked content is README + `.gitkeep` | Retain as preview boundary |
| `qa/` | CONFIRMED | Permitted lane with tracked small QA samples and extensive README scaffolding | Retain; outputs remain non-authoritative |
| `temporary/` | CONFIRMED | Permitted lane; direct tracked content is README + `.gitkeep` | Retain as ephemeral boundary |
| `release/` | CONFIRMED | Tracked fifth child; nonconforming even as placeholder/scratch | Freeze authority claims; migrate or retire only through accepted decision and verified plan |
| `perf/` | CONFIRMED candidate output path; not tracked | Manual scripts can create trust-shaped staging; current hosted workflow does not emit it | Treat as dormant/disposable drift; do not cite as canonical |
| External CI storage | PROPOSED projection | Root Registry target only | Verify retention, access, producer, and cutover before use |
| Public/deployed use | UNKNOWN | No admissible runtime evidence inspected | Verify separately; default deny |

### Hosted workflow correction

The current `MapLibre Perf Governance` workflow performs syntax checks, deterministic negative-path tests, and readiness inspection. Its declared outputs are GitHub job state, logs, annotations, and step summary only. It does **not** currently upload screenshots, receipts, proofs, release records, correction objects, rollback objects, or other generated artifacts.

Separate repository-owned scripts still name `artifacts/perf/` outputs and can write objects named `ProofPack`, `ReleaseManifest`, receipt, correction, or rollback when invoked outside that hosted workflow. Those scripts are candidate writers, not proof that the lane exists at runtime or that any emitted file is canonical.

### Tracked-tree inventory

The current pre-edit tree has **44 tracked files and 747,349 bytes**. The child trees total **714,240 bytes**; this README is **33,109 bytes** before v0.4.

| Tracked lane | Files | Bytes | Conformance | Current evidence |
|---|---:|---:|---|---|
| Root `README.md` | 1 | 33,109 pre-edit | Allowed | Same-path parent contract |
| `build/` | 8 | 164,397 | Allowed lane | README/ignore files plus incomplete environment scaffolds; no tracked compiled payload |
| `docs/` | 2 | 47,721 | Allowed lane | README + `.gitkeep`; no tracked generated site |
| `qa/` | 26 | 410,757 | Allowed lane, mixed maturity | README scaffolds plus small lint/coverage/validation samples |
| `release/` | 5 | 78,114 | **Nonconforming** | README scaffolds plus `people-dna-land/release_manifest.json` placeholder |
| `temporary/` | 2 | 13,251 | Allowed lane | README + `.gitkeep` |
| **Total** | **44** | **747,349 pre-edit** | **HOLD** | Ignored, untracked, hosted, and external outputs are outside this inventory |

> [!NOTE]
> The root README byte count changes in this candidate revision. The child counts and bytes are pinned to immutable child-tree SHAs; the final candidate README digest and size belong in the pull-request validation record rather than being self-referential metadata.

## What belongs here

Only derived, regenerable, non-authoritative output belongs here.

| Allowed lane | Accepted contents | Required posture |
|---|---|---|
| `build/` | Compiled output, distributables, package residue, build-context snapshots | Rebuildable; no canonical data or release authority |
| `docs/` | Generated documentation previews or renderer output | Canonical authored source stays in `docs/`; preview is not publication |
| `qa/` | Lint, coverage, validation, JUnit, accessibility, render-smoke, and visual-diff reports | Review support only; never proof or approval by itself |
| `temporary/` | Scratch files, intermediate transforms, local run debris | Ephemeral, safe to prune, excluded from trust decisions |

A file may remain here only while all of these are true:

1. it is generated rather than hand-authored as a source of record;
2. it is reproducible or safely disposable;
3. no evidence, policy, review, release, correction, or rollback decision depends on this copy;
4. it does not create a parallel writable home;
5. its producer, source inputs, retention, cleanup, and sensitivity posture are explicit;
6. it is not a standard input to a public or semi-public client;
7. any hosted copy remains a run artifact rather than a published KFM carrier.

### Permitted target shape

```text
artifacts/
├── README.md       # compatibility-root contract
├── build/          # compiled and package output
├── docs/           # generated documentation previews
├── qa/             # QA, lint, coverage, validation, and render reports
└── temporary/      # ephemeral working files
```

The tree above is the **adopted allowed shape**, not the current conformance claim. The current tracked tree also contains nonconforming `release/`.

## What does NOT belong here

Trust-bearing, canonical, durable, sensitive, or standard-client material is prohibited.

| Forbidden content | Canonical owner | Why |
|---|---|---|
| EvidenceBundles, evidence sidecars, proof packs, integrity bundles | `data/proofs/` | Consequential claim support |
| Run, transform, AI, validation, promotion, or release receipts | `data/receipts/` | Durable process memory |
| STAC, DCAT, PROV, domain catalog, or triplet closure records | `data/catalog/`, `data/triplets/` | Catalog and relation instances |
| ReleaseManifest, PromotionDecision, signatures, attestations | `release/` | Release decision plane |
| RollbackCard, correction, withdrawal, supersession notices | `release/` | Governed correction and rollback state |
| PMTiles, MVT, COG, GeoParquet, styles, reports, or stories released for consumers | `data/published/` | Released public-safe carriers |
| SourceDescriptor, activation decision, rights/sensitivity registry | `data/registry/`, `policy/` | Source and admissibility authority |
| Contracts, schemas, policy, validators, reusable code, pipelines | `contracts/`, `schemas/`, `policy/`, `tools/`, `packages/`, `pipelines/` | Canonical meaning, shape, rule, and implementation |
| Authored doctrine, ADRs, runbooks, architecture | `docs/` | Human source of record |
| Secrets, credentials, private endpoints, signing keys | Approved secret system | Ordinary Git output is not a secret boundary |
| Protected geometry, restricted source bytes, living-person/genomic details | Governed restricted store or quarantine | Compatibility output is not an access-control boundary |

### Observed held paths

| Path | Current evidence | Boundary problem | Safe posture |
|---|---|---|---|
| `artifacts/release/` | Tracked tree | Parallel release-shaped child prohibited by Directory Rules §15.2 | No new trust content or authority claims; migration/retirement requires accepted decision and rollback |
| `artifacts/release/people-dna-land/release_manifest.json` | Tracked 268-byte placeholder | Sensitive-domain release-shaped object in a noncanonical root | Treat as proposal/fixture lineage only; never as release state |
| `artifacts/perf/` | Named by scripts and workflow path filters; absent from tracked tree | Manual writers use trust-shaped names in an unapproved direct child | Do not invoke as a publication path; rehome or retire writers through reviewed work |
| Trust-shaped hosted artifacts | No current workflow output verified | Run artifact could be mistaken for KFM proof/release | Require explicit naming, retention, access, and canonical handoff rules |

## Inputs

Inputs remain in their owning roots. `artifacts/` receives projections, never authority.

| Input | Owning root | Permitted use |
|---|---|---|
| Application/package/tool source | `apps/`, `packages/`, `tools/`, `scripts/` | Produce replaceable build or QA output |
| Authored documentation | `docs/` | Produce non-authoritative preview output |
| Tests and fixtures | `tests/`, `fixtures/` | Produce QA results |
| Validators | `tools/validators/` | Produce inspection reports; canonical validation logic stays outside |
| Non-secret configuration | `configs/` | Parameterize generation |
| Workflow definitions | `.github/workflows/` | Orchestrate bounded generation/upload with least privilege |
| Pipeline implementation/specification | `pipelines/`, `pipeline_specs/` | Use temporary staging only when no trust decision depends on it |
| Released carriers | `data/published/` | May be copied into local QA inspection only; canonical bytes remain in the published family |

No input may smuggle raw, quarantined, restricted, unreleased, or canonical-internal state into a public path.

### Permitted writers

| Writer class | Permission | Boundary |
|---|---|---|
| Repository-owned generator or build tool | May create output in an allowed lane | Must declare inputs, generator/version, digest, retention, cleanup, and failure state |
| Pull-request workflow | May create run-local output with read-only repository permission | No secrets, OIDC, deployment, publication, or canonical write |
| Trusted post-merge workflow | May upload bounded CI artifacts when separately configured | Upload is not KFM release; retention/access remain explicit |
| Human contributor | May edit README, ignore policy, or an intentionally retained tiny QA fixture | Must not hand-author generated payload as source-of-record |
| Public client or normal UI | **DENY** | Uses governed API/released artifacts, never this root |
| Release/promotion process | **DENY canonical writes here** | Writes decision records and published carriers to canonical homes |
| External untrusted source | **DENY direct writes** | Enters through source admission and lifecycle controls |

## Outputs

| Output class | Allowed use | Required routing after graduation |
|---|---|---|
| Build output | Local/CI inspection, packaging, reproducibility comparison | Package registry or reviewed deployment target |
| Docs preview | Renderer, link, search, accessibility, and visual review | Authored source remains `docs/`; released reports use governed publication |
| QA report | Debugging, reviewer support, bounded CI evidence | Durable validation receipt/proof moves to canonical data family |
| Temporary output | Intermediate local or CI processing | Delete after use |
| Hosted CI artifact | Run-scoped review support | Govern retention/access; never public truth by default |
| Trust-bearing candidate | None as authority while here | Route to canonical receipt/proof/catalog/release/published owner after gates |
| Failure bundle | Debugging only | Sensitive content redacted; durable incident/audit record goes to governed owner |

Nothing under `artifacts/` is a standard data source for [`apps/governed-api/`](../apps/governed-api/) or [`apps/explorer-web/`](../apps/explorer-web/).

## Public exposure and sensitivity

The root is **internal by default**. A generated preview or QA report may describe public-safe material, but the copy under `artifacts/` is not the released carrier and is not a supported public endpoint.

| Concern | Required posture |
|---|---|
| Public routing | No governed API, browser client, CDN, or reverse proxy reads this root as truth |
| Access | Repository/CI access only unless a separately governed review surface is approved |
| Sensitive content | Deny secrets, protected geometry, restricted evidence, living-person/genomic detail, and source material with unclear rights |
| Redaction/generalization | Apply before output generation; styling or hidden UI state is not protection |
| Logs/reports | Record bounded identifiers and safe diagnostics; avoid raw payloads, prompts, tokens, or private paths |
| Hosted artifacts | Treat as run-scoped review material with explicit retention/access policy |
| Publication handoff | Requires canonical object family, evidence/policy/review/release closure, correction, and rollback |

When sensitivity, rights, source terms, or exposure are unresolved, the output belongs in a governed restricted/quarantine path or must not be generated.

## Mutability, retention, generation, and physical storage

| Dimension | Root contract |
|---|---|
| Mutability | Generated or ephemeral; direct hand editing is limited to boundary documentation and intentionally retained tiny fixtures |
| Retention | Temporary, CI-policy-bound, or review-window-bound; never the only copy of an audit/release object |
| Generation | Declare `generated_from`, generator identity/version, content digest, and edit policy |
| Physical storage | Git only for boundary docs, ignore rules, and reviewed small fixtures; bulk output should prefer CI/package/object storage |
| Reproducibility | Mirrors and previews are one-way and reproducible; a failed rebuild blocks reliance on the copy |
| Cleanup | Producers define pruning and failure-safe cleanup without deleting canonical source |
| Identity | Generated path names do not become stable object IDs unless a canonical contract says so |
| Correction | Correct source/canonical objects first, then regenerate; do not patch a derived copy as the sole fix |

The long-term Directory Rules target is no tracked generated payload beyond the boundary README, ignore rules, and intentionally retained small QA fixtures.

## Validation

Validation must distinguish four questions:

1. **Does the source definition exist?**
2. **Did a generator execute successfully?**
3. **Does an output satisfy its local QA contract?**
4. **Does any governed process authorize reliance, release, or publication?**

A positive answer to the first three never implies the fourth.

### Required negative checks

A material change to this root should fail when it:

- adds a direct child outside `build/`, `docs/`, `qa/`, or `temporary/`;
- places a receipt, proof, catalog record, release decision, correction, rollback object, or published carrier under `artifacts/`;
- introduces a standard public-client read from `artifacts/`;
- tracks a cache, dependency installation, virtual environment, or uncontrolled bulk generated payload;
- commits a secret, credential, protected geometry, raw evidence, or restricted source material;
- permits manual edits to a generated mirror;
- lacks declared `generated_from`, generator identity/version, digest, edit policy, retention, or cleanup;
- changes a producer path without a migration and rollback plan;
- treats a green workflow, uploaded file, or signature as human review or publication authority.

### Current repository-native surfaces

| Surface | Current verified role | Bounded conclusion |
|---|---|---|
| `control_plane/root_registry.yaml` | Projects compatibility class, internal exposure, generated mutation, temporary/CI retention, and no-trust profiles | Projection confirms intended boundary; does not execute migration |
| `MapLibre Perf Governance` | Static syntax, negative tests, and readiness HOLD; no artifact upload | Green means the reviewed hold is intact, not runtime/release readiness |
| MapLibre performance scripts | Manually invokable candidate generators targeting `artifacts/perf/` | Writer drift exists even without hosted execution |
| `make validate` and related commands | Repository-wide validation entrypoints exist | Command presence is not a current run result |
| Child `.gitignore` files | Bound some build/QA output | Complete ignored/untracked hygiene remains unverified |
| No dedicated artifacts allowlist validator verified | Enforcement gap | Manual review remains required until an executable negative gate exists |

### README checks

For this file, require:

- exactly one H1 and one balanced KFM meta block;
- stable H2 anchors retained for existing inbound links;
- balanced fences and HTML;
- repository-relative links resolved;
- direct-child map limited to direct children;
- current inventory tied to immutable tree/blob evidence;
- no stale Directory Rules conflict claim;
- no claim that workflow, script, receipt, signature, or path grants authority;
- exact changed-path comparison and remote blob parity.

## Review burden

| Change | Required concerns |
|---|---|
| README-only correction | Evidence accuracy, stable anchors, root contract, no-loss, rollback |
| New or changed generated output | Producer, reproducibility, inputs, retention, cleanup, secrets, sensitivity |
| New direct child | Directory Rules, accepted ADR, parallel-authority risk, migration, rollback |
| Trust-shaped output | Canonical object family, schema/contract, policy, evidence, review, release, correction |
| Workflow or uploader | Least privilege, untrusted code, network, retention, access, naming, public exposure |
| Retirement or externalization | Complete producer/consumer inventory, compatibility window, zero-write proof, rollback drill |

`@bartytime4life` is the verified repository review route. CODEOWNERS routing is not an artifacts-steward assignment, independent approval, ReviewRecord, separation-of-duty proof, release authority, or evidence that review occurred.

### Escalation

Escalate rather than normalize silently when:

- a producer needs a trust-bearing output;
- an external consumer requires a legacy path;
- rights, sensitivity, retention, or access is unresolved;
- a path move changes object identity or breaks replay;
- a proposed exception would permit public reads or parallel writes;
- root retirement or release-lane migration is requested.

## Related folders

| Folder | Relationship |
|---|---|
| [`build/`](build/README.md) | Generated build staging; mixed-maturity scaffolds |
| [`docs/`](docs/README.md) | Generated documentation preview boundary |
| [`qa/`](qa/README.md) | QA output scaffold |
| [`temporary/`](temporary/README.md) | Ephemeral working-file boundary |
| [`release/`](release/README.md) | **Nonconforming child**; documentation does not legalize placement |
| [`data/receipts/`](../data/receipts/) | Canonical process-memory records |
| [`data/proofs/`](../data/proofs/) | EvidenceBundles, proof packs, integrity support |
| [`data/catalog/`](../data/catalog/) | Catalog and provenance instances |
| [`data/published/`](../data/published/) | Released public-safe carrier bytes |
| [`release/`](../release/) | Release, promotion, correction, withdrawal, signature, rollback decisions |
| [`docs/`](../docs/) | Authored human source of record |
| [`tests/`](../tests/) and [`fixtures/`](../fixtures/) | Conformance code and reusable test inputs |
| [`tools/validators/`](../tools/validators/) | Repository validator implementation |
| [`apps/governed-api/`](../apps/governed-api/) | Public trust membrane; no artifact-root truth reads |
| [`apps/explorer-web/`](../apps/explorer-web/) | Public/semi-public client; governed interfaces only |
| [`control_plane/root_registry.yaml`](../control_plane/root_registry.yaml) | Non-authoritative machine projection of the adopted root class |
| [`docs/registers/DRIFT_REGISTER.md`](../docs/registers/DRIFT_REGISTER.md) | Historical/open drift record |

> [!WARNING]
> Child README freshness is uneven. In particular, `artifacts/release/README.md` still labels its tracked path as proposed/unmounted and carries placeholder ownership and older rule references. Treat child prose as local lineage until separately reconciled against ADR-0029, current trees, and current workflows.

## ADRs

| Decision or rule | Current status | Effect on this root |
|---|---|---|
| [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **Accepted** | Adopts Directory Rules v2 and the sole writable doctrine path |
| Directory Rules §15.1 | Adopted through ADR-0029 | Defines generated-output classes and canonical routing |
| Directory Rules §15.2 | Adopted through ADR-0029 | Allows only `build/`, `docs/`, `qa/`, `temporary/`; denies release/proof equivalents |
| Directory Rules §§16–18 | Adopted through ADR-0029 | Defines ROOT_FULL README, compatibility, migration, correction, rollback |
| Root Registry projection | Active machine projection | Records compatibility target/exit conditions without creating authority |
| Artifacts/release disposition | **OPEN / NEEDS DECISION** | No accepted migration or retirement decision verified |
| Prior [`ADR-0011`](../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | Proposed lineage | Supports object-family separation but is not needed to establish the adopted artifacts boundary |

This README documents the accepted boundary and current drift. It does not accept the open artifacts/release disposition or authorize deletion.

## Last reviewed

**2026-08-08**, against `main@d20c341149d43057c6540c499b9222bc4ac11460`, root tree `28f01907bb89386a6be3c515f3e24e33d032f5ea`, and pre-edit artifacts tree `39505667873ae68e6553aa2a47c270ffd2e10842`.

Re-review after any of the following:

- an accepted artifacts-disposition, release-placement, or root-retirement decision;
- a move, deletion, or new direct child under `artifacts/`;
- a producer, consumer, retention, upload, cleanup, or external-storage change;
- a workflow begins emitting or uploading artifacts from this root;
- a public/deployed consumer is discovered;
- a trust-content or direct-child allowlist validator becomes executable;
- a correction, withdrawal, security event, or rollback affects this root;
- the evidence snapshot or accepted Directory Rules identity changes.

## Direct-child directory map

The map below shows the current direct children only, as required by Directory Rules.

```text
artifacts/
├── README.md       # this compatibility-root contract
├── build/          # allowed generated build staging
├── docs/           # allowed generated documentation previews
├── qa/             # allowed QA and validation output
├── release/        # NONCONFORMING release-shaped compatibility child
└── temporary/      # allowed ephemeral working files
```

`artifacts/perf/` is not tracked at the evidence snapshot; it is a candidate runtime output path named by repository scripts and workflow filters.

## Current drift and migration state

| Drift | Status | Current evidence | Required closure |
|---|---|---|---|
| Tracked `artifacts/release/` | CONFIRMED / HOLD | Fifth direct child plus release-shaped placeholder | Accepted disposition, complete producer/consumer inventory, migration manifest, link/identity checks, rollback |
| Manual `artifacts/perf/` writers | CONFIRMED source definitions / HOLD | Repository scripts create trust-shaped filenames; hosted workflow does not emit them | Rehome/retire writers or constrain them to pure QA with tests and canonical handoff |
| Direct-child allowlist not verified as executable | NEEDS VERIFICATION | No dedicated artifacts validator confirmed in this review | Add negative fixtures and a repository-owned gate through separate reviewed scope |
| Child README freshness | NEEDS VERIFICATION | Several child docs are pinned to older bases; release README is materially stale | Separate same-path child documentation updates |
| Ignored/untracked output inventory | UNKNOWN | GitHub tree cannot show local ignored/untracked contents | Clean checkout, generator dry-runs, `git status --ignored`, output manifests |
| External CI retention/access | UNKNOWN | Root Registry projects external CI target but no operational policy inspected | Settings, workflow artifacts, retention/access evidence, security review |
| Stewardship/separation of duties | NEEDS VERIFICATION | CODEOWNERS route only | Accepted roles, required review controls, review records |

### Disposition alternatives

<details>
<summary><strong>Retain <code>artifacts/</code> as a bounded compatibility root</strong></summary>

A retain decision should:

1. preserve the four-child allowlist;
2. migrate or retire `release/` and reconcile every `perf/` writer;
3. add executable direct-child and no-trust-payload validation;
4. define producer, retention, access, cleanup, and external-CI handoff policy;
5. keep standard clients and governed release flows on canonical homes;
6. maintain a tested rollback for every producer-path change.

</details>

<details>
<summary><strong>Retire <code>artifacts/</code> after externalization</strong></summary>

A retirement decision should:

1. inventory tracked, ignored, untracked, hosted, uploaded, and externally consumed output;
2. route build/docs/QA output to reviewed CI, package, documentation, or object-storage targets;
3. route every trust-bearing object to its canonical `data/` or `release/` owner;
4. update generators, workflows, links, ignores, retention rules, and consumers in a governed migration;
5. prove zero writers and zero consumers;
6. retain a tombstone or alias only for a verified compatibility window;
7. perform and record rollback before physical deletion.

</details>

Neither alternative is selected by this README.

### Migration law

Any rehome or retirement must:

1. freeze the governing rules, tree, producers, consumers, identities, and digests;
2. classify each file by object family rather than filename;
3. accept the authority decision before structural implementation;
4. add the canonical destination and negative write guard;
5. record old-to-new identity/content mappings;
6. cut producers to canonical single-write;
7. provide bounded dual-read only for verified consumers;
8. validate links, imports, schema, policy, tests, release, correction, and rollback;
9. prove zero writers and zero consumers before removing the old path;
10. preserve decision and Git history without force-push or silent deletion.

## Safe change pattern

1. Pin current `main`, the target blob, artifacts tree, adopted Directory Rules, Root Registry, drift record, producers, consumers, and open PRs.
2. Classify the proposed output using the responsibility signature: authority owner, lifecycle, execution role, exposure, mutability, retention, and physical storage.
3. Return a finite result: `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, or `DENY`.
4. Keep disposable output inside the four allowed lanes; route durable or trust-bearing output to its canonical owner.
5. Declare deterministic source inputs, generator identity/version, output digest, edit policy, retention, cleanup, and sensitivity posture.
6. Add positive and negative tests appropriate to the writer and destination.
7. Validate no public-client read, no parallel authority, no secrets/protected content, and a reversible migration path.
8. Deliver through a scoped branch and reviewable PR. Do not infer release, deployment, promotion, or publication.

## Version history and no-loss ledger

| Version | Date | Material change | Authority effect |
|---|---|---|---|
| v0.2 | 2026-07-22 | Established compatibility boundary, exact inventory, release/perf drift, migration alternatives | Documentation + drift record only |
| v0.3 | 2026-07-23 | Refreshed evidence, ownership language, prior Directory Rules conflict, validation limits, rollback | Documentation + generated provenance only |
| v0.4 | 2026-08-08 | Reconciles accepted ADR-0029, Root Registry projection, current tree/bytes, hosted workflow behavior, manual script drift, child-doc staleness, and v2 README/migration law | Documentation only |

### Preserved from v0.3

- compatibility/transitional/non-authoritative classification;
- strict four-lane allowlist;
- trust-content prohibition and canonical destination map;
- 44-file tracked inventory and child-lane evidence;
- `artifacts/release/` and `artifacts/perf/` drift;
- input/output/validation/review guidance;
- retain-versus-retire and migration discipline;
- correction and rollback posture;
- stable target path and prior Git lineage.

### Corrected in v0.4

- Directory Rules are no longer described as two unresolved writable authorities;
- ADR-0029 is recorded as accepted;
- the pre-edit byte total is corrected from 734,530 to 747,349;
- current MapLibre hosted workflow output is distinguished from manually invokable script output;
- the Root Registry projection and its non-effects are made explicit;
- stale child documentation is surfaced instead of inherited as current authority.

## Correction and rollback

### Documentation correction

When a claim becomes stale:

1. pin the correcting evidence;
2. update the truth label and claim at this same path;
3. preserve prior text in Git history;
4. update any affected drift or verification record;
5. do not change structure merely to make prose appear correct.

### Before-merge rollback

Close the draft PR or transparently revert the branch commit. The exact pre-edit README blob is:

```text
7b2acc0c296daadb430370cdc803b487933487ae
```

### After-merge rollback

Use a normal revert of the authorized merge commit or a forward documentation correction that restores the prior blob. Re-run the same documentation and boundary checks. Never rewrite shared history.

This documentation rollback has no generator, lifecycle, evidence, release, deployment, or publication effect because this update modifies none of those surfaces.

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Current ignored/untracked contents | UNKNOWN | Clean checkout, `git status --ignored`, safe generator runs, output manifests |
| Complete producer-to-output map | NEEDS VERIFICATION | Static path analysis plus bounded dry-runs |
| `artifacts/release/` consumers and writers | NEEDS VERIFICATION | Recursive references, workflow/script analysis, runtime/config inspection |
| Manual `artifacts/perf/` invocation in practice | UNKNOWN | Run history, operator scripts, CI logs, retained outputs |
| External CI artifact target and cutover readiness | PROPOSED / NEEDS VERIFICATION | Retention/access settings, threat review, producer changes, rollback |
| Direct-child and trust-payload enforcement | NEEDS VERIFICATION | Validator, valid/invalid fixtures, CI invocation, exact-head result |
| Child README freshness | NEEDS VERIFICATION | Same-path reviews against current trees and adopted rules |
| Public/deployed consumers | UNKNOWN | App/deployment config, CDN/proxy settings, logs, runtime traces |
| Accepted release-lane disposition | UNKNOWN / OPEN | Accepted ADR or bounded exception, migration manifest, review, rollback proof |
| Independent reviewer and steward enforcement | NEEDS VERIFICATION | Rulesets, branch protection, stewardship assignments, ReviewRecords |

---

> **Current conclusion:** `artifacts/` is an active transitional compatibility root for disposable generated output. Its adopted direct-child contract is `build/`, `docs/`, `qa/`, and `temporary/`. The tracked `release/` child and manually invokable `perf/` writers remain held drift. Keep this root internal, generated, temporary, non-public, and outside the trust membrane; route every durable or trust-bearing object to its canonical owner.

<p align="right"><a href="#top">Back to top</a></p>
