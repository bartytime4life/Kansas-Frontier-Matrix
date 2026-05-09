<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0003-policy-singular-is-canonical
title: ADR-0003 — `policy/` is the canonical singular root; `policies/` is a compatibility mirror
type: standard
version: v1
status: draft
owners: <docs-steward> + <policy/ root owner — TODO>
created: 2026-05-09
updated: 2026-05-09
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0001-schema-home.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - control_plane/deprecation_register.yaml
tags: [kfm, adr, doctrine, policy, directory-rules]
notes:
  - "Resolves Directory Rules §18 open question — `policies/` vs `policy/` canonicality."
  - "ADR number 0003 is provisional — see Numbering note."
[/KFM_META_BLOCK_V2] -->

# ADR-0003 — `policy/` is the canonical singular root; `policies/` is a compatibility mirror

> **Decision (proposed).** `policy/` (singular) is the canonical repo-root home for admissibility, release, sensitivity, rights, runtime-gate, promotion-gate, and per-domain policy. If `policies/` (plural) exists, it is a **compatibility root** of class `mirror` or `legacy` and **MUST NOT** evolve independently.

| Field | Value |
|---|---|
| **Authors** | `<docs-steward>` *(placeholder — TODO)* |
| **Reviewers required** | Docs steward + `policy/` root owner *(per Directory Rules §17)* |
| **Supersedes** | — |
| **Superseded by** | — |
| **Related** | [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) §6.5, §8.1, §13.5, §18 · [`ADR-0001-schema-home`](./ADR-0001-schema-home.md) |
| **ADR §2.4 trigger** | #2 — *"Promoting a compatibility root to canonical, or deprecating a canonical root."* |

## Quick jumps

[Context](#1-context) · [Decision](#2-decision) · [Consequences](#3-consequences) · [Alternatives considered](#4-alternatives-considered) · [Migration plan](#5-migration-plan) · [Rollback plan](#6-rollback-plan) · [Validation](#7-validation) · [Open items](#8-open-items) · [Numbering note](#numbering-note)

---

## 1. Context

### 1.1 The forces

KFM governance treats **a folder's location** as encoding **who owns it, what governance it answers to, and what lifecycle it belongs to** *(Directory Rules §0)*. Two parallel homes for the same authority is the **single most common drift pattern** in the repo *(Directory Rules §13)*.

Three doctrinal sources already converge on a singular `policy/`:

- **Directory Rules §6.5** — *"`policy/` is the **canonical** singular. If `policies/` exists, treat it as legacy / mirror / deprecated / external-export per §8."*
- **Directory Rules §8.1** — `policies/` → canonical home `policy/`, class default `mirror` or `legacy`, recommended action: *"Pick canonical `policy/`; freeze writes to `policies/` and migrate."*
- **Directory Rules §13.5** — names *"Schema mirror divergence — `schemas/` and `contracts/` (or `policies/` and `policy/`) evolve separately"* as an anti-pattern.

However, **Directory Rules §18 — Open Questions** explicitly leaves the live answer pending mounted-repo verification:

> **NEEDS VERIFICATION:** Whether `policies/` or `policy/` is canonical. Default is `policy/`; resolve by inspection.

This ADR resolves that open question by ratifying the doctrinal default. It is the **§2.4 #2** ADR that promotes the doctrinal default into an accepted decision and freezes `policies/`, where present, as compatibility.

### 1.2 What this ADR cannot assume

The repository was **not mounted** in the session that produced this ADR. The following are **NEEDS VERIFICATION** until inspected against `git ls-tree`-equivalent evidence:

- Whether `policies/` exists at the repo root.
- Whether `policy/` exists at the repo root.
- Which (if any) files currently live under `policies/`.
- Whether tooling, CI workflows, OPA bundle paths, or import statements reference `policies/` directly.

The **decision** in §2 is doctrinally stable regardless of repo state. The **migration plan** in §5 is conditional on what an inspection finds.

---

## 2. Decision

> **`policy/` (singular) is the canonical repo-root home** for admissibility, release, sensitivity, rights, runtime-gate, promotion-gate, and per-domain policy. **`policies/` (plural), if present, is a compatibility root** of class `mirror` or `legacy` per Directory Rules §8. New rules, fields, fixtures, and policy updates land in canonical `policy/` first; mirrors regenerate from canonical or migrate.

### 2.1 Conformance language *(RFC 2119-style)*

| Rule | Level |
|---|---|
| New policy files (bundles, fixtures, tests, runtime/promotion/release gates, sensitivity, rights, domain) are authored under `policy/`. | **MUST** |
| `policies/`, if present, evolves independently of `policy/`. | **MUST NOT** |
| If `policies/` exists in the mounted repo, it carries a `README.md` declaring its class (`mirror` \| `legacy` \| `deprecated` \| `external-export` \| `transitional`) per Directory Rules §8. | **MUST** |
| Tooling, CI, runtime, OPA bundles, and `apps/governed-api/` reference `policy/` paths. References to `policies/` paths are tracked in `docs/registers/DRIFT_REGISTER.md` until migrated. | **SHOULD** |
| Future ADRs further constrain policy placement. They silently broaden it. | **MAY** / **MUST NOT** |

### 2.2 Canonical contents of `policy/`

The substructure is unchanged from Directory Rules §6.5 — this ADR freezes the **root**, not the subtree.

```
policy/
├── README.md
├── bundles/         # Rego/OPA bundles or equivalents
├── fixtures/        # policy fixtures distinct from tests/fixtures/
├── tests/           # policy tests
├── runtime/         # runtime gate policy (Focus Mode, evidence resolution, abstain)
├── promotion/       # promotion gate policy
├── sensitivity/     # sensitivity classes, redaction rules
├── rights/          # rights status, license enforcement
├── domains/
│   ├── fauna/   archaeology/   people-dna-land/   …
└── release/         # release-gate policy
```

### 2.3 What `policies/` (if present) is

| Class | When it applies | Allowed contents |
|---|---|---|
| `mirror` | Regenerated from `policy/` for IDE convenience or downstream export | Generated copies; never hand-edited |
| `legacy` | Predates canonical `policy/` and is awaiting migration | Frozen content; new files **SHOULD NOT** land here |
| `deprecated` | Slated for removal | Migration plan referenced; sunset date in `control_plane/deprecation_register.yaml` |
| `external-export` | Exists for downstream consumers; canonical home is `policy/` | Read-only export bundle; consumer documentation |
| `transitional` | Mid-migration | ADR or migration note pinned |

The default class on first inspection is **`mirror` or `legacy`** per Directory Rules §8.1.

---

## 3. Consequences

### 3.1 Positive

- **Resolves Directory Rules §18** open item for `policies/` vs `policy/`.
- **Eliminates one of four named drift patterns** *(§13.5 mirror divergence applied to policy roots)*.
- **Aligns with the singular-root convention** already used by sibling responsibility roots (`data/`, `release/`, `runtime/`, `infra/`, `migrations/`), making the §4 placement protocol more predictable for reviewers.
- **Makes the §16 path-validation checklist actionable** — reviewers can answer *"canonical `policy/` or compatibility `policies/`?"* without ambiguity.
- **Pins the per-root README contract** *(§15)* against one canonical directory rather than splitting it across two roots.

### 3.2 Negative / costs

- **Migration cost** for any code, tooling, OPA bundle path, CI workflow, or import statement that currently points at `policies/`. Magnitude is **NEEDS VERIFICATION** — depends on inspection.
- **Mirror maintenance** if `policies/` is kept as a `mirror` for downstream-consumer compatibility: a regenerator must be built and CI-checked for divergence.
- **Reviewer cost** during the transition window — PRs touching policy paths require an extra canonical-vs-compatibility check until `policies/` is fully retired or fully classed.

### 3.3 Risks if **not** taken

- Two homes for the same authority continues *(the §13 most-common drift)*.
- Policy bundles diverge silently between `policy/` and `policies/`, undermining the cite-or-abstain truth posture and the trust membrane.
- The per-root README contract *(§15)* cannot be enforced against an undecided root.
- Future ADRs that depend on policy placement (sensitive-location, rights enforcement, sensitivity defaults) inherit the ambiguity.

---

## 4. Alternatives considered

### 4.1 Make `policies/` canonical, demote `policy/` to compatibility

**Rejected.** Contradicts the Directory Rules §6.5 default; breaks the singular-root convention shared with `data/`, `release/`, `runtime/`, `infra/`; and would force a coordinated rename across every doctrine document, ADR, and dossier already referencing `policy/`. The doctrinal default already favors singular.

### 4.2 Allow both as live, parallel authorities

**Rejected.** Directly violates Directory Rules §8.3 (*"Compatibility roots are not parallel authority"*) and §13.5 (mirror-divergence anti-pattern). This is the failure mode the ADR exists to prevent.

### 4.3 Split by class — e.g., `policy/` for runtime gates, `policies/` for promotion bundles

**Rejected.** Bifurcates policy authority along a non-doctrinal axis, makes the §4 placement protocol harder rather than easier, and introduces a new reviewer burden (*"which kind of policy is this?"*) that the per-root README contract is meant to remove.

### 4.4 Defer the decision; keep `policies/` as `PROPOSED / CONFLICTED`

**Rejected.** The §18 question has been open since the Rules were authored; deferral perpetuates drift. A `proposed` ADR is a lower bar than waiting for a fully planned `policies/` migration — the doctrinal pin can land first, the migration plan in §5 follows.

---

## 5. Migration plan

The plan follows Directory Rules §14, conditional on what a `git ls-tree`-equivalent inspection of the mounted repo finds.

### 5.1 Inspection (precondition)

Before any move:

- [ ] List the contents of `policy/` and `policies/` at the repo root.
- [ ] Grep for path strings `policies/`, `"policies/`, `'policies/`, and `policies\.` across `apps/`, `packages/`, `connectors/`, `pipelines/`, `runtime/`, `tools/`, `scripts/`, `tests/`, `fixtures/`, `configs/`, `infra/`, `.github/`, `docs/`, `examples/`, and `pipeline_specs/`.
- [ ] Record the inspection result in `docs/registers/DRIFT_REGISTER.md` with affected paths.

### 5.2 Case A — `policy/` exists, `policies/` does not

No migration. The decision is informational. Update Directory Rules §18 to mark the open item resolved, and add an entry to §0 referencing this ADR.

### 5.3 Case B — `policies/` exists, `policy/` does not

Structural move under Directory Rules §14.2.

1. Open this ADR for review and acceptance.
2. Add the migration manifest under `migrations/data/` (or `migrations/schema/` if schema-shaped) listing every old → new mapping with `git_sha_before` and `git_sha_after`.
3. `git mv policies policy` so history is preserved *(§14.1 step 1)*.
4. Update every reference — code, docs, CI workflows, OPA bundle config, `apps/governed-api/` runtime config, schema cross-references.
5. If downstream consumers depend on the old path, **temporarily** mirror `policy/` → `policies/` with a generator, and class `policies/` as `mirror` in its `README.md` per §8.
6. Add a deprecation entry in `control_plane/deprecation_register.yaml` with sunset date.
7. Verify rollback with a dry-run rollback card in `release/rollback_cards/`.
8. After the verification window, remove the `policies/` mirror.

### 5.4 Case C — Both `policy/` and `policies/` exist

The §13.5 drift case, materialized.

1. Open this ADR for review and acceptance.
2. Author a **content reconciliation report** as a drift-register entry: which file lives in which root, where they diverge, what authority each currently has in tooling.
3. Resolve divergence by canonicalizing into `policy/`. Where `policies/` content is the more correct version, the move is a *content change* into `policy/`, recorded with a `CorrectionNotice` in `release/correction_notices/` if anything had been published from the divergent state.
4. Reclassify `policies/` as `mirror` or `legacy` per §8 — declare the class in `policies/README.md`.
5. Continue with §5.3 steps 4 onward.

### 5.5 Case D — Neither exists yet (greenfield)

Create `policy/` per the §6.5 substructure as part of normal repo bring-up. Do not create `policies/` at all unless and until a downstream-export need justifies it; in that case it begins life as a compatibility `mirror`.

> [!IMPORTANT]
> Promotion in KFM is a **governed state transition, not a file move** *(Directory Rules §0, §9.1)*. A `git mv` in §5.3 / §5.4 changes only **placement**, not the meaning, identity, version, or release state of any policy object. If a move would also change object identity, follow §14.3 instead.

---

## 6. Rollback plan

ADR rollback is a **doctrinal action**, not a file move.

1. Open a successor ADR with `status: proposed` arguing for a different canonical root or for parallel authority.
2. The successor ADR addresses every consequence in §3 and every alternative in §4.
3. If accepted, mark this ADR `status: superseded` with a forward link to the successor *(per Directory Rules §2.4)*.
4. If a §5 migration had already retired `policies/`, the successor ADR's migration plan reverses the move using the manifests recorded under `migrations/`.
5. Issue `CorrectionNotice` records in `release/correction_notices/` for any released artifacts that referenced the old canonical placement.

If a §5 migration fails partway:

1. Halt — do not partially commit.
2. Restore from the verification-window mirror *(§5.3 step 5)*.
3. Open a drift entry; treat the partially-moved state as the new starting point for a revised plan.

---

## 7. Validation

The decision is **enforceable** only when these checks exist; until they do, the rule is governance-only.

- [ ] Per-root `README.md` in `policy/` declares it canonical *(per Directory Rules §15)*.
- [ ] Per-root `README.md` in `policies/`, **if it exists**, declares its compatibility class *(per Directory Rules §8)*.
- [ ] CI lint flags new files under `policies/` that are not generated mirrors.
- [ ] CI lint flags imports / path strings in `apps/`, `packages/`, `runtime/`, `pipelines/`, `connectors/`, `tools/`, and `tests/` that reference `policies/` outside the mirror generator.
- [ ] `docs/registers/DRIFT_REGISTER.md` carries an entry for any unresolved divergence.
- [ ] `control_plane/deprecation_register.yaml` carries a sunset entry if `policies/` is classed `legacy` or `deprecated`.
- [ ] Directory Rules §0 lists this ADR alongside ADR-0001 once accepted.
- [ ] Directory Rules §18 marks the `policies/` vs `policy/` open item resolved with a forward link to this ADR.

> [!NOTE]
> All of the above are **PROPOSED / NEEDS VERIFICATION** until checked against the mounted repo and against CI. This ADR does not assert that any check currently exists.

---

## 8. Open items

- **NEEDS VERIFICATION** — Existence and contents of `policy/` and `policies/` in the mounted repo.
- **NEEDS VERIFICATION** — Existence of any CI lint or import-path check that would enforce §7.
- **NEEDS VERIFICATION** — `CODEOWNERS` coverage for `policy/` and `policies/`.
- **NEEDS VERIFICATION** — Whether `apps/governed-api/`, `runtime/`, and OPA-bundle wiring already point at `policy/` or at `policies/`.
- **OPEN** — Whether `policies/` is retained at all in the long run, or fully retired in favor of canonical `policy/` plus an export bundle in `data/published/` or `artifacts/docs/` for downstream consumers.
- **OPEN** — Whether the Directory Rules §0 metadata block should also reference this ADR explicitly under a *"policy-home convention"* line, mirroring the existing *"Schema-home convention"* line.
- **OPEN** — Whether this ADR's filename should drop the parenthesized clarifier and use kebab-case only (e.g., `ADR-0003-policy-singular-canonical.md`) to match `ADR-0001-schema-home.md` convention.

---

## Numbering note

The ADR number **`0003`** is **provisional**. Two prior `Suggested Future Work` lists in the corpus reserve `ADR-0003` for different topics:

| Source | Reserved ADR-0003 topic | Status in source |
|---|---|---|
| `Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf` (Decision register / ADR index) | `ADR-0003-evidencebundle-contract` — Define `EvidenceRef` → `EvidenceBundle` closure contract | `PROPOSED` future-work |
| `KFM Pass 12 Part 2` §9.2 Writing | `ADR-0003 Watcher Non-Publisher Invariant` | Suggested future work |

Neither is recorded as **accepted** in any Directory-Rules-tracked register. The number `0003` is therefore available *as a draft proposal*, but reviewers **SHOULD** reconcile against the canonical ADR index before accepting this ADR. If a different topic has already been accepted as `ADR-0003`, this ADR's number **SHOULD** be advanced to the next free integer and its filename renamed accordingly.

The **doctrinal content of this ADR is independent of its number** and survives renumbering unchanged.

[↑ Back to top](#adr-0003--policy-is-the-canonical-singular-root-policies-is-a-compatibility-mirror)
