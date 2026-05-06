<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-UUID-docs-doctrine-readme
title: Doctrine
type: standard
version: v1
status: draft
owners: OWNER_TBD_NEEDS_VERIFICATION
created: CREATED_DATE_TBD_FROM_GIT_OR_DOC_REGISTRY
updated: 2026-05-06
policy_label: NEEDS_VERIFICATION
related: [../../README.md, ../README.md, ../adr/README.md, ../adr/ADR-0014-truth-path.md, ../registers/README.md, ../runbooks/README.md]
tags: [kfm, doctrine, evidence, governance, truth-posture, trust-membrane, lifecycle, publication]
notes: [Replaces the inspected docs/doctrine/README.md scaffold stub with a repo-ready doctrine directory landing page, doc UUID owner created date and policy label remain verification placeholders, sibling doctrine files are listed as proposed backlog until confirmed in the active checkout]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Doctrine

Human-facing doctrine for Kansas Frontier Matrix: the operating law that keeps evidence, policy, publication, correction, rollback, maps, and AI inside the trust boundary.

<div align="left">

![status](https://img.shields.io/badge/status-experimental-orange)
![owners](https://img.shields.io/badge/owners-NEEDS%20VERIFICATION-lightgrey)
![path](https://img.shields.io/badge/path-docs%2Fdoctrine-0b7285)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-informational)
![lifecycle](https://img.shields.io/badge/lifecycle-governed-2ea44f)
![rollback](https://img.shields.io/badge/rollback-visible-6f42c1)

</div>

> [!IMPORTANT]
> **Status:** `experimental`  
> **Owners:** `OWNER_TBD_NEEDS_VERIFICATION`  
> **Path:** `docs/doctrine/README.md`  
> **Current revision role:** replaces an inspected scaffold stub with a navigable doctrine landing page.  
> **Trust rule:** doctrine can govern intent, language, and review burden; implementation enforcement still requires repo evidence such as schemas, policies, validators, fixtures, tests, workflows, receipts, proofs, release manifests, runtime traces, or reviewed artifacts.

## Quick jumps

| Start here | Stewardship | Review gates |
|---|---|---|
| [Scope](#scope) | [Doctrine map](#doctrine-map) | [Definition of done](#definition-of-done) |
| [Repo fit](#repo-fit) | [Directory tree](#directory-tree) | [Open verification](#open-verification) |
| [Accepted inputs](#accepted-inputs) | [Usage](#usage) | [Appendix](#appendix) |
| [Exclusions](#exclusions) | [Diagram](#diagram) | [FAQ](#faq) |

---

## Scope

`docs/doctrine/` is the home for KFM’s durable operating law: the short, reviewable human rules that explain how the project preserves evidence-first, map-first, time-aware, policy-aware, auditable, and reversible behavior.

Doctrine documents should answer questions like:

1. What counts as admissible support for a public or semi-public claim?
2. Which source classes outrank others?
3. How does evidence move through the lifecycle?
4. Where is the public trust membrane?
5. When must KFM `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`?
6. What must be visible for publication, correction, rollback, and supersession?

KFM doctrine is not decorative prose. It is the human-readable control layer that downstream ADRs, contracts, schemas, policies, validators, fixtures, APIs, map layers, review consoles, release manifests, and governed AI surfaces should obey.

> [!NOTE]
> KFM’s durable public unit is the **inspectable claim**: a public or semi-public statement whose evidence, source role, spatial scope, temporal scope, policy posture, review state, release state, and correction lineage can be inspected.

[Back to top](#top)

---

## Repo fit

**Target path:** `docs/doctrine/README.md`

`docs/doctrine/` belongs under `docs/` because doctrine is a human-facing governance surface. It should explain rules and boundaries; it should not become a machine-schema home, policy engine, source-data store, proof archive, release directory, or domain-specific root.

### Upstream surfaces

| Surface | Relationship | Status |
|---|---|---:|
| [`../../README.md`](../../README.md) | Repository-level orientation, KFM identity, trust law, responsibility roots, and public-client posture. | `CONFIRMED` |
| [`../README.md`](../README.md) | Documentation root landing page; currently lightweight and should eventually route into doctrine, ADRs, registers, runbooks, domains, and standards. | `CONFIRMED / THIN` |
| [`../adr/README.md`](../adr/README.md) | Decision ledger for architecture-significant choices that operationalize doctrine. | `CONFIRMED` |
| [`../adr/ADR-0014-truth-path.md`](../adr/ADR-0014-truth-path.md) | Current truth-path and public trust membrane ADR draft. | `CONFIRMED / DRAFT` |
| [`../registers/README.md`](../registers/README.md) | Register landing page for authority, canon, drift, source ledger, and verification backlog surfaces. | `CONFIRMED` |
| [`../runbooks/README.md`](../runbooks/README.md) | Operational runbooks that should execute doctrine without bypassing validation, release, correction, or rollback. | `CONFIRMED` |

### Downstream consumers

| Consumer | How it should use doctrine | Enforcement status |
|---|---|---:|
| `docs/adr/` | Turns doctrine into reviewed architecture decisions with alternatives, validation, rollback, and supersession. | `PARTIAL / NEEDS VERIFICATION` |
| `contracts/` | Defines semantic meaning for evidence, source, runtime, release, correction, rollback, and domain objects. | `NEEDS VERIFICATION` |
| `schemas/` | Defines machine-checkable shape for doctrine-backed object families. | `NEEDS VERIFICATION` |
| `policy/` | Converts doctrine into admissibility, deny, restrict, abstain, release, and obligation rules. | `NEEDS VERIFICATION` |
| `tests/` and `fixtures/` | Proves doctrine with positive and negative examples. | `NEEDS VERIFICATION` |
| `apps/`, `packages/`, `tools/` | Implements governed APIs, validators, Evidence Drawer payloads, Focus Mode envelopes, and review helpers. | `UNKNOWN / NEEDS VERIFICATION` |
| `data/`, `release/`, `runtime/` | Stores lifecycle data, emitted receipts/proofs, release candidates, manifests, rollback cards, and runtime support. | `NEEDS VERIFICATION` |

> [!WARNING]
> Do not use doctrine placement to imply implementation maturity. A doctrine rule becomes active system behavior only when the matching contracts, schemas, policy, validators, tests, workflows, runtime behavior, and release artifacts are verified.

[Back to top](#top)

---

## Accepted inputs

Use `docs/doctrine/` for stable, project-wide KFM rules that should outlive a single domain lane or implementation sprint.

| Accepted input | Belongs here when... | Typical companion surface |
|---|---|---|
| Authority rules | A source, document, repo artifact, or external reference needs an explicit order of precedence. | `docs/registers/AUTHORITY_LADDER.md` |
| Truth posture rules | Maintainers need shared language for `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`, `DENY`, `ABSTAIN`, and `ERROR`. | `docs/registers/VERIFICATION_BACKLOG.md` |
| Lifecycle law | A public claim depends on how material moves from source edge to published state. | `release/`, `data/receipts/`, `data/proofs/` |
| Trust membrane rules | Public clients, map layers, APIs, exports, dashboards, or AI surfaces need a boundary from internal stores. | `docs/adr/`, `policy/`, `tests/` |
| Evidence closure rules | Claims, features, layers, or answers must resolve through `EvidenceRef` to `EvidenceBundle`. | `contracts/evidence/`, `schemas/contracts/v1/` |
| Publication and correction doctrine | Promotion, rollback, withdrawal, correction, and supersession need durable language. | `docs/runbooks/`, `release/` |
| Governed AI doctrine | Model runtimes, Focus Mode, citations, and AI receipts need bounded behavior. | `contracts/runtime/`, `apps/`, `packages/` |
| Sensitivity defaults | Rare species, archaeology, living persons, DNA, infrastructure, cultural stewardship, and precise locations require fail-closed defaults. | `policy/`, `docs/domains/` |

[Back to top](#top)

---

## Exclusions

`docs/doctrine/` should stay authoritative, concise, and reviewable. It should not become a catch-all.

| Do not put here | Put it here instead | Why |
|---|---|---|
| JSON Schemas | `schemas/` | Doctrine states rules; schemas validate shape. |
| Semantic contract files | `contracts/` | Contracts define object meaning and compatibility. |
| Policy-as-code | `policy/` | Policy needs executable or policy-owned enforcement. |
| Source descriptors and registries | `data/registry/`, `control_plane/`, or the verified source registry home | Source authority requires structured fields, rights, cadence, and steward posture. |
| Receipts, proof packs, release manifests, rollback cards | `data/receipts/`, `data/proofs/`, `release/` | Emitted trust objects are audit artifacts, not doctrine pages. |
| Domain-specific architecture manuals | `docs/domains/<domain>/` | Domain lanes should inherit doctrine without turning domain names into root authority. |
| Exploratory packets and idea inventories | `docs/intake/`, `docs/reports/`, or a verified archive home | Exploratory material must not become accidental canon. |
| Runtime logs or dashboard exports | `runtime/`, `artifacts/`, or verified observability homes | Logs are implementation evidence, not doctrine. |
| Private chain-of-thought | Do not store as KFM truth material | Generated reasoning is not a governed evidence object. |

[Back to top](#top)

---

## Directory tree

Current sibling inventory must be rechecked on the branch where this file lands. The only doctrine file directly inspected for this revision was `docs/doctrine/README.md`.

```text
docs/doctrine/
├── README.md                    # CONFIRMED target path; this file
├── authority-ladder.md          # PROPOSED / NEEDS VERIFICATION
├── truth-posture.md             # PROPOSED / NEEDS VERIFICATION
├── trust-membrane.md            # PROPOSED / NEEDS VERIFICATION
├── lifecycle-law.md             # PROPOSED / NEEDS VERIFICATION
├── publication-law.md           # PROPOSED / NEEDS VERIFICATION
├── correction-rollback-law.md   # PROPOSED / NEEDS VERIFICATION
├── governed-ai-law.md           # PROPOSED / NEEDS VERIFICATION
└── sensitivity-defaults.md      # PROPOSED / NEEDS VERIFICATION
```

> [!TIP]
> Keep future doctrine pages short. When a rule needs alternatives, tradeoffs, and acceptance state, write or update an ADR. When a rule needs executable enforcement, write or update policy, schemas, validators, and tests.

[Back to top](#top)

---

## Doctrine map

| Doctrine surface | Purpose | Current disposition |
|---|---|---:|
| `README.md` | Directory orientation, scope, repo fit, accepted inputs, exclusions, and review burden. | `THIS REVISION` |
| `authority-ladder.md` | Source and evidence precedence across attached doctrine, repo evidence, generated artifacts, external standards, and runtime proof. | `PROPOSED` |
| `truth-posture.md` | Shared truth labels and system outcomes. | `PROPOSED` |
| `trust-membrane.md` | Boundary between internal lifecycle/canonical stores and public governed surfaces. | `PROPOSED` |
| `lifecycle-law.md` | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. | `PROPOSED` |
| `publication-law.md` | Promotion as governed state transition, not file movement. | `PROPOSED` |
| `correction-rollback-law.md` | Correction, withdrawal, supersession, rollback target, and public trust repair. | `PROPOSED` |
| `governed-ai-law.md` | AI as interpretive, evidence-subordinate, citation-validated runtime surface. | `PROPOSED` |
| `sensitivity-defaults.md` | Fail-closed handling for rights uncertainty, sovereignty, cultural sensitivity, living-person data, DNA/genomic material, rare species, archaeology, infrastructure, and precise locations. | `PROPOSED` |

[Back to top](#top)

---

## Operating law

KFM doctrine should preserve these rules unless an accepted ADR explicitly narrows or supersedes them.

| Rule | Meaning | Default failure outcome |
|---|---|---|
| Evidence first | Consequential claims resolve evidence before authority. | `ABSTAIN` when support is insufficient. |
| Map first | Place is the primary operating surface, but maps are not truth authorities. | Hide or downgrade layers lacking release/evidence support. |
| Time aware | Valid time, observed time, source time, retrieval time, release time, and correction time stay distinct where material. | Mark stale, abstain, or block publication. |
| Cite or abstain | Unsupported factual public claims do not get polished into authority. | `ABSTAIN`. |
| Policy-aware | Rights, sensitivity, access role, source terms, review state, and release state must be readable by gates. | `DENY` or `ERROR`. |
| Public-safe by default | Public clients consume governed APIs and released artifacts only. | `DENY` direct internal-stage access. |
| Publication is governed | Promotion requires validation, evidence closure, policy, review, release, correction path, and rollback target. | Block release candidate. |
| Derived products stay derived | Tiles, maps, graphs, indexes, scenes, dashboards, summaries, reports, exports, and AI answers are carriers. | Do not treat derivative as root proof. |
| AI is subordinate | Model output may interpret released evidence; it cannot decide truth, rights, sensitivity, review, or release. | `DENY` direct model authority; `ABSTAIN` uncited output. |
| Corrections are visible | Published material keeps correction, withdrawal, supersession, and rollback lineage. | `ERROR` if correction path is missing. |

[Back to top](#top)

---

## Usage

### 1. Start from doctrine, then choose the right authority surface

Use doctrine to decide the rule. Use ADRs to record durable architecture choices. Use contracts and schemas to define and validate object shape. Use policy to enforce admissibility. Use tests and fixtures to prove negative paths. Use release artifacts to publish, correct, and roll back.

```text
Doctrine rule
  -> ADR decision when architecture-significant
  -> Contract meaning
  -> Schema shape
  -> Policy admissibility
  -> Fixture and validator proof
  -> Release / correction / rollback evidence
```

### 2. Keep doctrine and implementation evidence separate

A doctrine page may say “public clients must not read RAW.” That does not prove the app enforces it. Enforcement needs inspected routes, tests, policies, validators, workflow evidence, or runtime proof.

### 3. Prefer short doctrine pages over sprawling manuals

If a doctrine page grows too large, split it by responsibility:

- stable rule stays in `docs/doctrine/`;
- decision history moves to `docs/adr/`;
- operational steps move to `docs/runbooks/`;
- source classification moves to `docs/registers/` or source registries;
- machine validation moves to `schemas/`, `policy/`, `tests/`, or `tools/`.

### 4. Record uncertainty where maintainers will see it

Use `UNKNOWN` or `NEEDS VERIFICATION` in the document body when uncertainty materially affects review, publication, public exposure, or implementation claims.

[Back to top](#top)

---

## Diagram

```mermaid
flowchart TD
  D[docs/doctrine<br/>operating law] --> A[docs/adr<br/>decisions + tradeoffs]
  D --> R[docs/registers<br/>authority + canon + drift + backlog]
  D --> B[docs/runbooks<br/>safe operations]

  A --> C[contracts<br/>semantic meaning]
  C --> S[schemas<br/>machine-checkable shape]
  D --> P[policy<br/>admissibility + fail-closed rules]
  S --> T[tests + fixtures<br/>positive and negative proof]
  P --> T

  T --> E[EvidenceRef -> EvidenceBundle<br/>claim support]
  E --> G[Proof / review / release<br/>manifest + correction + rollback]
  G --> U[Governed API / tiles / exports]
  U --> M[Map shell<br/>Evidence Drawer<br/>Focus Mode]

  X[RAW / WORK / QUARANTINE<br/>internal lifecycle states] -. denied .-> M
  Y[Direct model output] -. denied .-> M
  Z[Maps / tiles / graphs / indexes] -. carriers, not sovereign truth .-> E
```

This diagram shows responsibility boundaries, not implementation proof. Each arrow requires matching repository evidence before enforcement can be claimed.

[Back to top](#top)

---

## Quickstart

Run these from the repository root before treating this directory as complete.

```bash
# Confirm repository context.
git rev-parse --show-toplevel
git status --short
git branch --show-current

# Inspect doctrine files.
find docs/doctrine -maxdepth 1 -type f | sort

# Look for unresolved placeholders and truth labels.
rg -n 'TODO|TBD|NEEDS VERIFICATION|UNKNOWN|PROPOSED|CONFLICTED' docs/doctrine docs/adr docs/registers docs/runbooks || true

# Check Markdown link health with the repo-native tool, if present.
# Replace this with the verified project command before claiming link checks passed.
```

> [!CAUTION]
> Do not report these checks as passing unless they ran on the active checkout.

[Back to top](#top)

---

## Definition of done

This README is ready to be treated as active doctrine navigation only when:

- [ ] `doc_id` is replaced with a verified document registry ID or accepted placeholder policy.
- [ ] `owners` is verified against CODEOWNERS, maintainer records, or project governance.
- [ ] `created` is filled from Git history or the document registry.
- [ ] `policy_label` is confirmed.
- [ ] Parent navigation from `docs/README.md` points here.
- [ ] Sibling doctrine files are either created, removed from the tree, or left clearly marked `PROPOSED`.
- [ ] Links to ADRs, registers, and runbooks are checked.
- [ ] Any doctrine rule with enforcement language has corresponding backlog, policy, validator, fixture, test, or ADR linkage.
- [ ] No implementation, CI, runtime, API, dashboard, or release claim is made without current repo evidence.
- [ ] Reviewers can identify rollback impact if this directory is reorganized.

[Back to top](#top)

---

## Open verification

| Item | Status | Required evidence |
|---|---:|---|
| Document UUID / registry ID | `NEEDS VERIFICATION` | `control_plane/document_registry.yaml`, docs register, or accepted ID policy. |
| Owner / steward | `NEEDS VERIFICATION` | CODEOWNERS, maintainer assignment, governance register, or reviewed owner field. |
| Created date | `NEEDS VERIFICATION` | Git history or document registry. |
| Policy label | `NEEDS VERIFICATION` | Policy classification or docs governance register. |
| Sibling doctrine files | `NEEDS VERIFICATION` | Active checkout inventory for `docs/doctrine/*.md`. |
| Parent docs navigation | `NEEDS VERIFICATION` | `docs/README.md` update or accepted navigation decision. |
| Link checks | `NEEDS VERIFICATION` | Repo-native Markdown/link validation output. |
| Enforcement maturity | `UNKNOWN` | Verified schemas, policies, validators, tests, workflows, runtime behavior, proof objects, and release artifacts. |
| ADR alignment | `NEEDS VERIFICATION` | ADR index and successor/supersession mapping. |
| Meta block enforcement | `NEEDS VERIFICATION` | Metadata linter or promotion-gate evidence. |

[Back to top](#top)

---

## FAQ

### Is doctrine the same as an ADR?

No. Doctrine states stable operating law. ADRs record decisions, alternatives, tradeoffs, consequences, validation plans, rollback paths, and supersession.

### Is doctrine implementation proof?

No. Doctrine can be governing text, but enforcement requires current repo evidence.

### Can this directory include proposed future files?

Yes, when the status is explicit. Proposed doctrine surfaces should not be active links unless the files exist or link checking allows placeholders by policy.

### Why are public clients mentioned in a docs directory?

Because KFM treats public exposure as a trust boundary. Documentation that weakens the trust membrane can lead directly to unsafe implementation, so the boundary belongs in doctrine.

### What should happen when doctrine and implementation conflict?

Record the conflict, cite the evidence, and choose the safer behavior until an ADR, fix, or rollback resolves it. Do not hide the conflict with confident prose.

[Back to top](#top)

---

## Appendix

<details>
<summary>Truth labels used by doctrine</summary>

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository evidence, attached doctrine, current-session evidence, generated artifacts, tests, workflows, logs, manifests, or other inspected proof. |
| `INFERRED` | Strongly grounded by evidence but not directly verified as implementation. |
| `PROPOSED` | Recommended design, file, path, behavior, or rule not yet verified as implemented. |
| `UNKNOWN` | Not verified strongly enough to state as fact. |
| `NEEDS VERIFICATION` | Checkable, but not checked strongly enough to promote. |
| `CONFLICTED` | Sources, paths, authority, terms, or implementation evidence materially disagree or remain unresolved. |
| `LINEAGE` | Historically useful material that should be preserved but not treated as current implementation proof. |
| `SUPERSEDED` | Replaced by a stronger source, successor decision, or verified implementation. |
| `DENY` | Policy or trust boundary blocks the requested action. |
| `ABSTAIN` | KFM lacks enough support to answer or publish. |
| `ERROR` | A contract, validation, runtime, release, or system failure prevents safe handling. |

</details>

<details>
<summary>Doctrine entry template</summary>

```markdown
# <Doctrine title>

One-line rule statement.

> [!IMPORTANT]
> **Status:** draft | active | stable | deprecated  
> **Owners:** OWNER_TBD_NEEDS_VERIFICATION  
> **Path:** `docs/doctrine/<file>.md`  
> **Rule:** <one sentence>  
> **Implementation proof:** UNKNOWN until verified.

## Scope

## Rule

## Accepted inputs

## Exclusions

## Evidence and authority

## Downstream surfaces

## Validation / negative paths

## Rollback and supersession

## Open verification
```

</details>

<details>
<summary>Pre-publish checklist</summary>

- [ ] One H1 only.
- [ ] One-line purpose directly below the H1.
- [ ] Meta block preserved.
- [ ] Status, owners, badges, and quick jumps present.
- [ ] Repo fit includes path plus upstream and downstream surfaces.
- [ ] Accepted inputs and exclusions are explicit.
- [ ] Directory tree is truth-labeled.
- [ ] Mermaid diagram explains a real KFM responsibility boundary.
- [ ] Code fences are language-tagged.
- [ ] Long appendix content is collapsed.
- [ ] Links are verified or uncertainty is visible.
- [ ] No unsupported implementation, CI, runtime, route, release, or dashboard claims.
- [ ] Rollback and supersession implications are visible.

</details>

[Back to top](#top)
