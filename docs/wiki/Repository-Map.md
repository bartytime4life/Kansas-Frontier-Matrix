<!--
KFM_WIKI_SOURCE
page_id: Repository-Map
title: Repository Map
version: v0.2.0
status: PROPOSED wiki source; review required
created: 2026-08-07
updated: 2026-08-15
authority: orientation-only; canonical repository evidence, adopted KFM doctrine, accepted ADRs, owning root contracts, and reviewed machine projections outrank this page
source_path: docs/wiki/Repository-Map.md
owning_root: docs/
responsibility: public orientation to KFM responsibility roots, root classes, path selection, lifecycle placement, scope segments, compatibility, and migration boundaries
evidence_snapshot: main@2d7f3014d52cc51556f1ecb1660f8998e8654035
prior_blob: e0772a42f11a61eb150c0c15cc45803145470417
root_tree: d2ca3c5c24cea63f1b30f92cb69019c736d39275
root_registry_blob: 024f668b5f0a9239bafa4f8b09e2afd86300ff8c
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
publication_effect: none until separately synchronized to the native GitHub Wiki
-->

<a id="top"></a>

<p align="center">
  <img src="https://raw.githubusercontent.com/bartytime4life/Kansas-Frontier-Matrix/main/docs/brand/logo/The-Kansas-Frontier-Matrix-Seal-transparent-cropped.png" alt="Kansas Frontier Matrix seal" width="150" />
</p>

# Repository Map

<p align="center"><strong>Responsibility first · Scope second · Evidence over convention · Reversible change</strong></p>

KFM is a **responsibility-root monorepo**. A top-level path says which kind of authority may own an artifact. Domain, source, geography, Focus Mode, cross-domain seam, and object-family segments narrow that responsibility only after the root is selected.

> [!IMPORTANT]
> **A path is an authority claim, not proof of truth or release.** Correct placement does not grant source authority, rights clearance, sensitivity approval, review, promotion, deployment, publication, or public access.

> [!NOTE]
> **Evidence checkpoint:** reviewed against [`main@2d7f3014d52cc51556f1ecb1660f8998e8654035`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/2d7f3014d52cc51556f1ecb1660f8998e8654035), its exact top-level tree, accepted [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), the adopted [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md), and [`control_plane/root_registry.yaml`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/control_plane/root_registry.yaml). The registry is a machine projection; it does not create or amend authority.

## At a glance

| Question | Bounded answer |
|---|---|
| What governs placement? | KFM invariants, accepted ADRs, adopted Directory Rules, non-conflicting root contracts, then current repository evidence |
| How many top-level directory roots are visible? | **25** at the evidence snapshot |
| How are they classified? | **22 canonical-or-platform roots**, plus `artifacts/` compatibility, `catalog/` deprecated, and `src/` conditional |
| What separates meaning, shape, and admissibility? | `contracts/` defines meaning, `schemas/` defines machine shape, and `policy/` decides allow/deny/hold/restrict/abstain |
| Where do lifecycle and accountability instances live? | The correct governed lane under `data/` |
| Where do release and rollback decisions live? | `release/`; published-looking paths do not authorize a release |
| Where does a domain belong? | As a lane inside each owning responsibility root—not as a new root merely because the topic matters |
| What happens when no unique safe home is proven? | `HOLD` or `DENY`, not “probably here” |
| What is this page? | An orientation projection under `docs/wiki/`, not placement authority |

**Quick navigation:** [Mental model](#how-to-read-a-path) · [Root tree](#current-root-tree) · [Root atlas](#responsibility-root-atlas) · [Authority split](#meaning-shape-policy-and-enforcement) · [Data](#data-lifecycle-and-accountability) · [Scope](#scope-comes-after-responsibility) · [Placement](#placement-protocol) · [Examples](#worked-examples) · [Transitions](#compatibility-and-migration) · [Checklist](#contributor-checklist)

---

## How to read a path

```text
responsibility root
  -> lifecycle or execution role
  -> domain / source / geography / seam / object family
  -> stable artifact identity
```

For example, `schemas/contracts/v1/domains/hydrology/` means:

1. `schemas/` owns machine-checkable shape;
2. `contracts/v1/` narrows the schema family and version;
3. `domains/hydrology/` narrows scope;
4. the path does **not** make hydrology a root or prove an object valid, safe, released, or public.

Before naming a path, classify the artifact by kind, authority owner, lifecycle, execution role, scope, exposure, mutability, and retention. If two independent authorities would edit one artifact, the correct result is usually `SPLIT`.

[Back to top](#top)

---

## Current root tree

```text
Kansas-Frontier-Matrix/
├── .github/         [platform]
├── apps/            [canonical]
├── artifacts/       [compatibility]
├── catalog/         [deprecated]
├── configs/         [canonical]
├── connectors/      [canonical]
├── contracts/       [canonical]
├── control_plane/   [canonical]
├── data/            [canonical]
├── docs/            [canonical]
├── examples/        [canonical]
├── fixtures/        [canonical]
├── infra/           [canonical]
├── migrations/      [canonical]
├── packages/        [canonical]
├── pipeline_specs/  [canonical]
├── pipelines/       [canonical]
├── policy/          [canonical]
├── release/         [canonical]
├── runtime/         [canonical]
├── schemas/         [canonical]
├── scripts/         [canonical]
├── src/             [conditional]
├── tests/           [canonical]
└── tools/           [canonical]
```

A path may exist and still be noncanonical. Presence is implementation evidence, not permission to repeat drift.

| Class | Meaning |
|---|---|
| `platform` | Required host integration that must not become KFM truth authority |
| `canonical` | Active responsibility root with one defined authority class |
| `compatibility` | Transitional or consumer-bound surface; derived output only, no independent authority |
| `deprecated` | Frozen legacy containment with a known target; no new producers or direct writes |
| `conditional` | Proposed or unresolved root profile that cannot broaden without an accepted decision |

Current transition posture: keep trust objects out of `artifacts/`; add no new writes to top-level `catalog/`; prefer `packages/` over expanding `src/` unless accepted authority says otherwise.

[Back to top](#top)

---

## Responsibility-root atlas

| Root family | Owns |
|---|---|
| `docs/` | Human doctrine, ADRs, architecture, runbooks, standards, domain guidance, and orientation |
| `control_plane/` | Machine projections and indexes of adopted governance; projections do not become decisions |
| `contracts/` | Semantic meaning, invariants, interface promises, and shared language |
| `schemas/` | Machine-checkable shapes, contexts, versions, and declared type authority |
| `policy/` | Normative allow, deny, hold, restrict, redact, generalize, delay, and abstain rules |
| `apps/` | Deployable applications, UIs, APIs, workers, and service boundaries |
| `packages/` | Reusable, independently testable, non-deployable implementation |
| `connectors/` | Source-specific fetch, capture, and admission implementation |
| `pipelines/` | Executable transformations and lifecycle orchestration |
| `pipeline_specs/` | Declarative schedules, inputs, outputs, run graphs, and resource envelopes |
| `runtime/` | Bounded provider harnesses, deterministic mocks, local adapters, and runtime composition |
| `tools/` | Repository-wide validators, generators, builders, inspectors, and operators |
| `scripts/` | Thin wrappers around governed tools and routine maintenance |
| `configs/` | Non-secret profiles, templates, defaults, and environment-neutral configuration |
| `infra/` | Deployment, networking, exposure, provisioning, and hardening implementation |
| `migrations/` | Versioned migration logic, mappings, compatibility windows, and rollback definitions |
| `fixtures/` | Reusable synthetic valid, invalid, denied, and golden inputs and expected outputs |
| `tests/` | Executable conformance, boundary, negative, integration, and end-to-end evidence |
| `examples/` | Runnable public-safe demonstrations of supported use |
| `data/` | Governed lifecycle, registry, receipt, proof, catalog, rollback, and released-carrier instances |
| `release/` | Promotion, release, correction, withdrawal, rollback, and signature decisions |
| `.github/` | Workflows, templates, CODEOWNERS routing, and repository-platform integration |

No root owns everything about an object merely because it produces or consumes it.

[Back to top](#top)

---

## Meaning, shape, policy, and enforcement

| Question | Owner | Example |
|---|---|---|
| What does the object mean? | `contracts/` | Define `EvidenceBundle` and its invariants |
| What fields and constraints exist? | `schemas/` | Require IDs, evidence references, versions, and finite enums |
| May it be used or exposed? | `policy/` | Deny protected coordinates or hold unresolved rights |
| Can the rule be enforced? | `fixtures/`, `tests/`, and usually `tools/` | Positive, invalid, denied, stale, correction, and rollback cases |

A contract is not a schema. A schema is not policy. A passing test is not human review. None is a release decision.

[Back to top](#top)

---

## Data lifecycle and accountability

```text
Pre-RAW -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

| Lane | Purpose |
|---|---|
| `data/raw/` | Source-native capture or immutable source reference after governed admission |
| `data/work/` | Candidate normalization, transformation, analysis, or review |
| `data/quarantine/` | Unsafe, invalid, conflicted, unclear, or under-supported material held fail-closed |
| `data/processed/` | Validated products that are not automatically public |
| `data/catalog/` | Governed discovery and catalog instances |
| `data/triplets/` | Relationship projections under the adopted grammar |
| `data/published/` | Released public-safe carriers; path presence alone is not release authority |
| `data/registry/` | Source, dataset, layer, identity, rights, and sensitivity registry instances |
| `data/receipts/` | Process and authoring provenance records |
| `data/proofs/` | Proof objects and integrity evidence |
| `data/rollback/` | Rollback-related instances and materializations |

Promotion, release, correction, withdrawal, rollback, and signature **decisions** stay under `release/`.

> [!WARNING]
> The current `data/` tree contains inherited naming and containment drift, including multiple triplet variants. Existing siblings are not templates for new work. Check [`data/README.md`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/data/README.md), adopted rules, registries, and active migration decisions before creating a deeper path.

Read [Data Lifecycle](Data-Lifecycle.md) for the stage-by-stage trust model.

[Back to top](#top)

---

## Scope comes after responsibility

A domain, source, geography, Focus Mode, cross-domain seam, or object family narrows scope. It does not select the root.

```text
docs/domains/hydrology/
contracts/domains/hydrology/
schemas/contracts/v1/domains/hydrology/
policy/domains/hydrology/
tests/domains/hydrology/
data/raw/hydrology/
data/quarantine/hydrology/
data/processed/hydrology/
data/catalog/hydrology/
data/published/hydrology/
```

These lines illustrate the pattern; they do not claim every leaf exists or is ready for new writes. Verify the owning README, registered slug, aliases, current lane, and accepted decisions first.

A source belongs under source-acquisition or registry responsibilities, not a new agency root. A county, watershed, or Focus Mode is compositional scope, not a root. Cross-domain work requires explicit seams rather than one lane absorbing another.

Read [Domains](Domains.md) for bounded contexts and seam governance.

[Back to top](#top)

---

## Placement protocol

Before creating, moving, renaming, mirroring, or deleting a path:

1. classify the artifact and exactly one authority owner;
2. choose the candidate root from adopted authority;
3. reject roots that prohibit its lifecycle, execution role, exposure, mutability, or retention;
4. separate app, package, connector, pipeline, spec, tool, script, runtime, and infrastructure roles;
5. select the correct `data/` lane for instances or `release/` for decisions;
6. add registered scope only after the root is fixed;
7. search canonical, compatibility, generated, deprecated, and legacy homes plus open work;
8. check dependency direction;
9. record one finite outcome.

| Outcome | Meaning |
|---|---|
| `PLACE` | Exactly one canonical home satisfies the rules |
| `SPLIT` | The artifact contains more than one authority owner |
| `MIGRATE` | An existing artifact has a known canonical target |
| `MIRROR` | A verified consumer requires a derived one-way copy |
| `HOLD` | Ownership, identity, sensitivity, target, or authority remains unresolved |
| `DENY` | Placement would violate an invariant, expose protected state, or create parallel authority |

“Probably here” is not a governed outcome.

[Back to top](#top)

---

## Worked examples

| Artifact | Owning home |
|---|---|
| This public repository orientation page | `docs/wiki/Repository-Map.md` |
| Human definition of `EvidenceBundle` | `contracts/` family |
| JSON Schema for `EvidenceBundle` | `schemas/` family |
| Rule denying protected coordinates | `policy/` family |
| Valid and denied samples | `fixtures/` |
| Executable conformance check | `tests/` |
| Repository-wide validator | `tools/` |
| Thin command wrapper | `scripts/` |
| Source-specific fetcher | `connectors/` |
| Reusable geometry library | `packages/` |
| Governed API service | `apps/governed-api/` |
| Explorer Web component | `apps/explorer-web/` |
| Executable normalization flow | `pipelines/` |
| Declarative run graph | `pipeline_specs/` |
| Unsafe candidate | `data/quarantine/<scope>/` |
| Generated authoring receipt | `data/receipts/generated/` |
| Catalog record | `data/catalog/` |
| Public-safe released carrier | `data/published/`, with a separate release decision |
| Promotion, correction, withdrawal, or rollback decision | `release/` |

Exact leaf names and versions remain subject to owning READMEs, accepted ADRs, registries, and current repository evidence.

[Back to top](#top)

---

## Compatibility and migration

A compatibility mirror is derived one-way from canonical source and is not hand-edited. A deprecated path remains frozen until producer, consumer, reference, history, rollback, and retirement evidence support removal.

A safe migration identifies the source, canonical target, object family, writers, readers, links, imports, generators, compatibility window, validation, correction path, and rollback target. Root creation, retirement, promotion, split, or merge normally requires an accepted ADR followed by a separate implementation change.

> [!CAUTION]
> Do not delete merely because a canonical target is known, and do not let a proposed document authorize its own dependent structural change.

[Back to top](#top)

---

## Repository anti-patterns

- creating roots for domains, sources, counties, or features;
- putting semantic prose, JSON shape, policy, and instances in one folder;
- writing new catalog material under deprecated top-level `catalog/`;
- storing receipts, proofs, or release records under `artifacts/`;
- letting `src/` become a second package or domain authority;
- treating `data/published/`, a test, a receipt, a merge, or a wiki edit as release;
- hand-editing mirrors or generated files;
- letting public clients read RAW, WORK, QUARANTINE, or canonical stores directly;
- copying drift because it already exists;
- deleting before proving consumer closure and rollback.

[Back to top](#top)

---

## Contributor checklist

- [ ] Read the complete target and nearest owning README.
- [ ] Pin the base commit and exact target bytes.
- [ ] Read adopted Directory Rules and applicable accepted ADRs.
- [ ] Treat `root_registry.yaml` as a projection, not authority.
- [ ] Search history, references, issues, and open pull requests for competing homes.
- [ ] Write the artifact's responsibility signature and finite placement outcome.
- [ ] Preserve lifecycle, evidence, policy, review, release, correction, and rollback boundaries.
- [ ] Update direct contracts, schemas, policy, fixtures, tests, registries, navigation, generators, and docs when required.
- [ ] Run changed-area and repository-native validation.
- [ ] Separate inherited failures from introduced failures.
- [ ] Keep generated-receipt and human-review state accurate.
- [ ] State rollback and do not confuse PR, merge, wiki sync, release, deployment, promotion, or publication.

Continue with [Development and Validation](Development-and-Validation.md) and [Contributing](Contributing.md).

[Back to top](#top)

---

## Authority references

- [ADR-0029 — Adopt Directory Governance Standard v2](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules v2](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md)
- [Machine root registry](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/control_plane/root_registry.yaml)
- [Root README repository map](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/README.md#repository-map)
- [CONTRIBUTING placement guidance](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/CONTRIBUTING.md#choose-the-owning-responsibility-root)

Reader routes: [Architecture](Architecture.md) · [Data Lifecycle](Data-Lifecycle.md) · [Domains](Domains.md) · [Governance and Evidence](Governance-and-Evidence.md) · [Project Status](Project-Status.md) · [Wiki Maintenance](Wiki-Maintenance.md)

> [!IMPORTANT]
> When this page and a current canonical source disagree, use the canonical source, record the drift, and correct this page.

[Back to top](#top)
