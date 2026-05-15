<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-readme
title: docs/adr — Architecture Decision Records
type: standard
version: v1.1
status: draft
owners: Architecture steward, Docs steward
created: 2026-05-09
updated: 2026-05-15
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/authority-ladder.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/truth-posture.md
  - docs/architecture/contract-schema-policy-split.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, governance, adr, doctrine]
notes:
  - Repository was not mounted when this README was authored or revised; every per-ADR presence claim is PROPOSED / NEEDS VERIFICATION until repo inspection.
  - ADR-0001 (schema home) is referenced by directory-rules.md as the schema-home convention; its actual authored state and acceptance status must be verified against the mounted repo.
  - 2026-05-15 revision strengthened README contract, verification, and index-refresh guidance without claiming implementation state.
[/KFM_META_BLOCK_V2] -->

# `docs/adr/` — Architecture Decision Records

> The audit trail of architectural reasoning for the Kansas Frontier Matrix. One file per consequential decision. Append-only history. Supersession over deletion.

![authority](https://img.shields.io/badge/authority-canonical-1f6feb)
![class](https://img.shields.io/badge/class-governance-6f42c1)
![status](https://img.shields.io/badge/status-draft-d4a72c)
![review](https://img.shields.io/badge/review-NEEDS%20VERIFICATION-d4a72c)
![repo](https://img.shields.io/badge/repo-unverified-6e7781)
![supersession](https://img.shields.io/badge/policy-never%20delete-cf222e)

**Owners:** Architecture steward · Docs steward  
**Reviewers required:** Architecture steward + at least one subsystem owner  
**Target path:** `docs/adr/README.md`  
**Last reviewed:** `<TODO: YYYY-MM-DD on first repo-verified PR>`

> [!IMPORTANT]
> This README is doctrine-grounded but **not** repo-verified. The KFM repository was not mounted during authoring or this revision. Every claim about which ADRs currently exist on disk is **PROPOSED / NEEDS VERIFICATION** until checked against repo evidence such as `git ls-tree`, file contents, ADR metadata, and validator output. The placement rule for `docs/adr/` is CONFIRMED by Directory Rules doctrine; individual file presence is not.

---

## Quick jump

[Purpose](#purpose) · [README contract](#readme-contract) · [Authority](#authority-level) · [Lifecycle](#adr-lifecycle) · [What belongs here](#what-belongs-here) · [What does not](#what-does-not-belong-here) · [Inputs & outputs](#inputs--outputs) · [Naming](#naming-convention) · [Template](#adr-template) · [Authoring quickstart](#authoring-quickstart) · [Status & supersession](#status--supersession) · [Index](#index-of-adrs) · [Validation](#validation) · [Repo refresh](#first-repo-verification-pass) · [Review burden](#review-burden) · [Related](#related-folders--doctrine) · [Maintenance](#maintenance-checklist) · [FAQ](#faq)

---

## Purpose

`docs/adr/` is the **canonical home** for KFM Architecture Decision Records: short, dated, append-only documents that capture *what* was decided, *why*, *what was rejected*, and *what follows*. ADRs are the answer to *"why is this done this way?"* when the rationale is no longer obvious from the code, the schema, or the policy alone.

ADRs are **not** designed to *make* decisions inside their own files. A merged ADR is the trace of a decision that was already reached through review — it captures rationale and consequences in a form future maintainers can search, cite, and supersede.

> [!NOTE]
> ADRs explain decisions; they do not enforce them. Enforcement lives in `schemas/`, `policy/`, `tests/`, validators in `tools/`, and CI workflows. An ADR without enforcement is doctrine; an enforcer without an ADR is an unrecorded decision. KFM aims for both.

---

## README contract

| Item | Value |
|---|---|
| **Owning root** | `docs/` — canonical documentation and governance memory |
| **Target path** | `docs/adr/README.md` |
| **Document role** | Directory README and operating standard for Architecture Decision Records |
| **Audience** | Architecture steward, docs steward, subsystem owners, reviewers, implementation agents |
| **Primary inputs** | Proposed ADRs, drift-register escalations, doctrine amendments, backfill decisions, repo-inspection findings |
| **Primary outputs** | ADR files, index updates, supersession links, downstream references to schemas/contracts/policy/tests/release artifacts |
| **Truth posture** | CONFIRMED doctrine / PROPOSED file inventory / UNKNOWN implementation depth until mounted-repo evidence is inspected |
| **Public-safety posture** | Public doc; never place sensitive source details, secrets, private data, or restricted exact-location decisions here |

This README is a **routing and governance surface**. It tells maintainers where ADRs belong, how to author them, how to keep them append-only, and how to verify the index. It does not turn the starter ADR list into current repo truth.

---

## Authority level

| Property | Value |
|---|---|
| **Authority class** | Canonical — governance-bearing README for the ADR root |
| **Status of this README** | Draft / NEEDS REPO VERIFICATION |
| **Status of `docs/adr/` as a home** | CONFIRMED doctrine via Directory Rules |
| **Status of any specific ADR file's presence** | PROPOSED / NEEDS VERIFICATION (repo not mounted) |
| **Authority order** | Core invariants and accepted ADRs that explicitly amend Directory Rules outrank Directory Rules. This README refines the ADR root and cannot contradict doctrine. |
| **Append-only** | Yes — accepted ADR bodies are stable; superseded and rejected ADRs are retained with links. ADRs are **never deleted**. |
| **Change discipline** | An ADR is required for §2.4-class changes: canonical roots, schema-home rule, lifecycle phase changes, parallel-home creation, or invariant-bending. |

A draft or proposed ADR carries argument, not authority. An accepted ADR carries authority only for the decision it actually records, and only to the extent it does not silently weaken KFM core invariants.

---

## ADR lifecycle

````mermaid
flowchart LR
    A[Need recognized] --> B[Draft ADR<br/>status: proposed]
    B --> C{Architecture review}
    C -->|approved| D[Merge<br/>status: accepted]
    C -->|rejected| E[Merge<br/>status: rejected]
    C -->|needs work| B
    D --> F{Decision still holds?}
    F -->|yes| D
    F -->|no| G[Author successor ADR<br/>status: proposed]
    G --> H{Review}
    H -->|approved| I[Merge successor<br/>status: accepted<br/>+ link forward from old ADR<br/>old status: superseded]
    H -->|rejected| F

    classDef accepted fill:#dafbe1,stroke:#2da44e,color:#1a7f37
    classDef proposed fill:#fff8c5,stroke:#bf8700,color:#7d4e00
    classDef rejected fill:#ffebe9,stroke:#cf222e,color:#82071e
    classDef review fill:#ddf4ff,stroke:#0969da,color:#0550ae

    class D,I accepted
    class B,G proposed
    class E rejected
    class F,H review
````

**Statuses (per [Directory Rules §2.4](../doctrine/directory-rules.md#24-changes-that-require-an-adr)):** `proposed` · `accepted` · `superseded` · `rejected`. Superseded and rejected ADRs MUST be retained — they are part of the audit trail.

---

## What belongs here

ADR files, and only ADR files. Specifically:

- **Cross-cutting architectural decisions** — schema home, ID derivation, finite-outcome envelope vocabulary, watcher-as-non-publisher invariant, STAC profile, release manifest envelope, crypto stack, MapLibre adapter boundary, public-trust-path boundary, etc.
- **Domain-scoped architectural decisions** that affect more than one component or are non-obvious from code — e.g., a domain's source-role separation, a domain's geometry-sensitivity policy.
- **Supersession ADRs** that replace earlier decisions, written as new files with new IDs and forward/back links.
- **Rejected proposals** that were considered seriously enough to be worth preserving as a "we considered this and chose not to" record.

A useful threshold: *if the choice affects more than one component, or could be re-litigated by a future maintainer reading only the code, write an ADR.*

---

## What does NOT belong here

> [!WARNING]
> Putting the wrong artifact under `docs/adr/` weakens the trail and confuses readers. Use the table below to redirect.

| If the artifact is… | …it belongs in |
|---|---|
| Object-family **meaning** (semantic Markdown) | [`contracts/`](../../contracts/) |
| Object **shape** (JSON Schema, JSON-LD context) | [`schemas/contracts/v1/…`](../../schemas/) |
| Allow / deny / restrict / abstain rules | [`policy/`](../../policy/) |
| Release manifests, promotion decisions, rollback cards, correction notices | [`release/`](../../release/) |
| Run, validation, ingest, AI, release **receipts** | `data/receipts/` |
| Evidence bundles, proof packs, validation reports | `data/proofs/` |
| Operational procedures, runbooks, drills | `docs/runbooks/` |
| Doctrine, principles, invariants | `docs/doctrine/` |
| Architecture explainers (system context, deployment topology, governed-API description) | `docs/architecture/` |
| Drift, contradiction, deprecation, verification backlog records | `docs/registers/` and `control_plane/` |
| Domain-overview README, data-model walk-through, lineage | `docs/domains/<domain>/` |
| Build outputs, generated docs, QA reports | `artifacts/` (compatibility root, tightly scoped) |

ADRs **MUST NOT** be used as a substitute for any of the above. An ADR can *cite* a contract, *reference* a schema, *direct* a policy, but it does not *replace* them.

---

## Inputs & outputs

### Inputs

ADRs are produced from:

- **Architecture proposals** during PR review when a §2.4-class change is on the table.
- **Backfill drives** that record previously-undocumented decisions discovered during inspection.
- **Drift-register entries** in [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) that escalate into named decisions.
- **Open questions** from `docs/registers/VERIFICATION_BACKLOG.md` and per-domain `OPEN_QUESTIONS.md` that mature into decisions.
- **Doctrine evolution** — when `docs/doctrine/*.md` is amended in ways that demand a recorded rationale.

### Outputs

Merging an ADR can trigger downstream changes (which are tracked, but live elsewhere):

- Updates to `docs/doctrine/directory-rules.md` if §2.4 applies.
- New or revised entries in `schemas/`, `contracts/`, `policy/`, `tests/`, `tools/validators/`.
- `migrations/<kind>/` plans when the decision implies a path or schema migration.
- `control_plane/deprecation_register.yaml` entries when an ADR deprecates a path or rule.
- Forward-links from any prior ADR(s) being superseded.
- `release/correction_notices/` when the decision invalidates a previously-released claim.

---

## Naming convention

The canonical filename pattern is:

````
ADR-NNNN-<kebab-case-slug>.md
````

- `NNNN` — a four-digit, zero-padded, **monotonically increasing** integer. Once assigned, an ADR's number is permanent.
- `<kebab-case-slug>` — short, descriptive, stable. Avoid version numbers in the slug (use a successor ADR instead).

> [!TIP]
> Reserve the next number at the start of authoring so two PRs do not collide on `0007`. The drift-register or a `RESERVATIONS.md` register is a reasonable parking lot if collisions become frequent. **NEEDS VERIFICATION** whether KFM has adopted such a register.

**Examples** (starter cross-cutting examples only; file presence and acceptance status remain NEEDS VERIFICATION — see [Index](#index-of-adrs)):

````
ADR-0001-schema-home.md
ADR-0002-source-ledger-authority.md
ADR-0003-evidencebundle-contract.md
````

**Domain-scoped ADRs** appear in the corpus with a slug-only form (e.g., `ADR-archaeology-schema-home.md`, `ADR-habitat-fauna-source-role-split.md`) and sometimes with a per-domain numeric prefix (e.g., `docs/domains/atmosphere/ADR-0001-atmosphere-lane.md`).

> [!NOTE]
> **NEEDS VERIFICATION:** whether KFM standardizes on (a) one global number series under `docs/adr/`, (b) a global series plus per-domain series under `docs/domains/<domain>/`, or (c) slug-only domain ADRs. The default this README assumes — pending an ADR to clarify it — is: **global numeric series under `docs/adr/`** for cross-cutting decisions, and per-domain ADRs under `docs/domains/<domain>/` using either slug-only names or a per-domain numeric series, with a forward-link from the domain ADR into any cross-cutting ADR it depends on. This convention is **PROPOSED** until ratified.

---

## ADR template

Copy the block below into a new file. Field names and statuses follow [Directory Rules §2.4](../doctrine/directory-rules.md#24-changes-that-require-an-adr) and the J.3 ADR pattern in the project corpus. Do not omit fields; if a field is genuinely empty, write `n/a` and explain why.

````markdown
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/NNNN
title: ADR-NNNN — <Short title>
type: adr
version: v1
status: proposed
owners: <names or roles>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related:
  - <kfm:// or repo path>
tags: [kfm, adr]
notes: []
[/KFM_META_BLOCK_V2] -->

# ADR-NNNN — <Short title>

| Field | Value |
|---|---|
| **ID** | adr-NNNN |
| **Status** | proposed \| accepted \| superseded \| rejected |
| **Date** | YYYY-MM-DD |
| **Deciders** | <names or roles> |
| **Supersedes** | adr-MMMM (or `none`) |
| **Superseded by** | adr-MMMM (or `none`) |
| **Related** | <ADRs, ADR-amended doctrine, contracts, schemas, policies, tests> |
| **Affects** | <repo paths or subsystems> |

## Context

The forces in play. The problem statement. The constraints. What evidence motivated revisiting this. What KFM invariants are touched. What is currently confusing, conflicting, or unenforced.

## Evidence basis

List the repo files, doctrine sections, schemas, contracts, policies, tests, source descriptors, release artifacts, drift entries, or external standards that support the decision. Mark any implementation-dependent claim as `NEEDS VERIFICATION` unless checked in the mounted repo.

## Decision

The choice made. State it as an imperative single sentence first, then expand. Pin concrete details (paths, names, versions, parameters, thresholds) rather than gesturing at them.

## Consequences

- **Positive:** what this enables, simplifies, or removes ambiguity from.
- **Negative / costs:** what this constrains, breaks, requires migration for, or makes harder.
- **Operational:** validators, CI, fixtures, runbooks, dashboards, or release-gate changes implied.
- **Policy / sensitivity:** rights, sensitivity, public-access, source-role, or release-state consequences. Write `n/a` only when genuinely irrelevant.

## Alternatives considered

For each meaningful alternative: a one-paragraph description, why it was attractive, why it was rejected. **Do not omit this section.** A decision without alternatives looks foregone; recording the considered-and-rejected paths is the point of an ADR.

## Migration & rollback

- **Migration plan:** files, paths, schemas, policies, tests touched. Reference any plan under `migrations/`.
- **Rollback plan:** how to reverse if the decision proves wrong. Reference any rollback card under `release/rollback_cards/` if the decision touches released artifacts.
- **Sunset of mirrors / compatibility shims:** if the decision creates one, name the sunset criterion.

## Open questions

Things this ADR does not resolve and should be tracked elsewhere (link to `docs/registers/VERIFICATION_BACKLOG.md` or a successor ADR).

## References

Links to: doctrine sections, prior ADRs, schemas, contracts, policies, tests, dossiers, external standards, drift entries, release/correction artifacts, and verification backlog entries.
````

---

## Authoring quickstart

1. **Confirm an ADR is needed.** If the change matches [Directory Rules §2.4](../doctrine/directory-rules.md#24-changes-that-require-an-adr), it is. If it affects more than one component or is non-obvious from code, it almost certainly is. When in doubt, open one — it is cheaper than re-litigating later.
2. **Reserve a number.** Look at the index in this README, the file listing in `docs/adr/`, and any repo-approved reservation register if one exists. Take the next free `NNNN`. Note any companion domain ADR you also need (`docs/domains/<domain>/ADR-…`).
3. **Copy the [template](#adr-template)** into `docs/adr/ADR-NNNN-<slug>.md`. Fill the meta block. Do not skip fields.
4. **Draft with `status: proposed`.** Cite evidence — schemas, contracts, prior ADRs, dossiers, drift entries. Do not draft as a fait accompli; the alternatives section is doctrinally required.
5. **Open a PR.** Title format: `ADR-NNNN: <short title> [proposed]`. Tag the architecture steward and the affected subsystem owners.
6. **Run validation locally** if validators exist (see [Validation](#validation)). **NEEDS VERIFICATION** which validators are wired.
7. **Iterate through review.** If reviewers ask for fundamental changes, those edits stay in the same file while status remains `proposed`. The ADR is rewritable until it is merged.
8. **On merge, set `status: accepted`** in the meta block and the index table — and freeze the file body. Substantive changes happen via a successor ADR, not by rewriting accepted history.
9. **If superseding a prior ADR:** add `Supersedes: adr-MMMM` to the new ADR, and in the same PR update the old ADR's `status` to `superseded` plus its `Superseded by:` field. Both files ship together.
10. **Link forward and back.** Update [the index in this README](#index-of-adrs) and any per-root README that referenced the prior decision.

> [!TIP]
> An ADR is most useful when it is short and evidence-heavy. Aim for one tight page of context, one paragraph of decision, three bullets of consequence, two paragraphs of alternatives. Long ADRs become unread ADRs.

---

## Status & supersession

| Status | Meaning | Edits allowed? |
|---|---|---|
| `proposed` | Drafted, under review, not yet authoritative | Yes — until merged |
| `accepted` | Merged. Authoritative. | **No.** Use a successor ADR. |
| `superseded` | Replaced by a later ADR. Retained for audit. | Only the meta block / `superseded_by` field. |
| `rejected` | Considered, decided against. Retained for audit. | **No.** |

**Hard rules:**

- ADRs are **never deleted**. A wrong-headed ADR is superseded or rejected, not removed.
- An `accepted` ADR is **immutable** in body. Typos and dead-link fixes are permissible; substantive change requires a successor.
- A `superseded` ADR **MUST** carry a forward link to its replacement. The replacement **MUST** carry a back link.
- A `rejected` ADR is preserved so future readers see the path was considered.

---

## Index of ADRs

> [!NOTE]
> The list below is the **PROPOSED starter set** drawn from the project corpus (see [References](#references)). The repository was not mounted during authoring, so each row's *file presence* is **NEEDS VERIFICATION**. ADR-0001 is referenced by Directory Rules as the schema-home convention; whether it exists on disk and whether it is accepted remain separate repo-verification questions.
>
> When this README is next updated against a mounted repo, mark each row's status accurately, replace **NEEDS VERIFICATION** with **CONFIRMED** where appropriate, and add any ADRs not in this starter set.

| ID | Title | Topic | Status (file) | Status (decision) |
|---|---|---|---|---|
| `ADR-0001` | [`schema-home`](./ADR-0001-schema-home.md) | Resolve `schemas/contracts/v1/` vs `contracts/` as machine-schema authority | NEEDS VERIFICATION | PROPOSED / NEEDS VERIFICATION — referenced by Directory Rules as the schema-home convention |
| `ADR-0002` | `source-ledger-authority` | Source ledger update, supersession, and append-only rules | NEEDS VERIFICATION | PROPOSED |
| `ADR-0003` | `evidencebundle-contract` | `EvidenceRef` → `EvidenceBundle` resolution and closure contract | NEEDS VERIFICATION | PROPOSED |
| `ADR-0004` | `promotion-gate` | Promotion as governed state transition (not a file move) | NEEDS VERIFICATION | PROPOSED |
| `ADR-0005` | `maplibre-layer-manifest` | Public-safe `LayerManifest` rules for the map shell | NEEDS VERIFICATION | PROPOSED |
| `ADR-0006` | `governed-ai-runtime-envelope` | Finite-outcome envelope: `ANSWER \| ABSTAIN \| DENY \| ERROR` | NEEDS VERIFICATION | PROPOSED |
| `ADR-0007` | `domain-lane-template` | Standard lane files, schemas, validators, tests per domain | NEEDS VERIFICATION | PROPOSED |
| `ADR-0008` | `sensitive-location-policy` | Fail-closed treatment for sensitive exact locations | NEEDS VERIFICATION | PROPOSED |
| `ADR-0009` | `local-exposure-security` | VPN / reverse proxy / firewall / auth / audit posture | NEEDS VERIFICATION | PROPOSED |
| `ADR-0010` | `catalog-proof-release-separation` | Separate receipts, proofs, catalogs, releases, reviews, corrections | NEEDS VERIFICATION | PROPOSED |

**Domain-scoped ADRs** are tracked in the per-domain trees and SHOULD link back to the relevant cross-cutting ADR. Examples seen in the corpus (all PROPOSED, status NEEDS VERIFICATION):

- `docs/domains/atmosphere/ADR-0001-atmosphere-lane.md`
- `docs/domains/agriculture/ADR-0001-agriculture-domain-boundary.md`
- `docs/adr/ADR-archaeology-schema-home.md` (or its `docs/domains/archaeology/` equivalent — placement NEEDS VERIFICATION)
- `docs/adr/ADR-hydrology-schema-home.md` and three siblings
- `docs/adr/ADR-habitat-fauna-schema-home.md` and two siblings

> [!CAUTION]
> Two competing starter lists appear in the corpus — one in *Pipeline Living Implementation Manual v0.3* (`schema-home`, `source-ledger`, `evidencebundle`, `promotion-gate`, `maplibre-layer-manifest`, `governed-ai-runtime-envelope`, …) and one in *Pass 12 Idea Index* (`spec-normalization`, `finite-decision-outcomes`, `watcher-non-publisher`, `stac-profile`, `releasemanifest`, `crypto-stack`). The first list is used in this index because it aligns with Directory Rules' schema-home reference and the pipeline-manual starter set. **NEEDS VERIFICATION** whether the second list's topics are folded into later ADR numbers, written as separate ADRs, or absorbed into doctrine. An early housekeeping ADR to reconcile the two is recommended.

---

## Validation

> [!WARNING]
> The validators and CI checks listed below are **PROPOSED**. Their existence in the current repo is **NEEDS VERIFICATION**. Do not assume an absent check is a passing check.

PROPOSED gates for `docs/adr/` PRs:

- **Filename pattern check** — `ADR-\d{4}-[a-z0-9-]+\.md` for files in `docs/adr/`; domain-pattern alternative for `docs/domains/<domain>/ADR-…`.
- **Number-uniqueness check** — no two ADRs share `NNNN` in the same series.
- **Required-fields check** — meta block + table fields complete; `status` ∈ {`proposed`, `accepted`, `superseded`, `rejected`}.
- **Supersession-link check** — every `superseded` ADR has a valid forward link, every successor has a valid back link.
- **Append-only check** — substantive edits to `accepted` ADRs are flagged; only meta-block tweaks and dead-link fixes are auto-allowed.
- **Cross-link check** — links from `docs/doctrine/`, `contracts/`, `schemas/`, `policy/` to ADRs by ID resolve.
- **Index-coherence check** — the table in this README contains every ADR in `docs/adr/` and vice versa.
- **`docs/adr/README.md` "Last reviewed" freshness check** — flag if older than six months (per [Directory Rules §15](../doctrine/directory-rules.md#15-required-readme-contract)).

PROPOSED tooling homes:

- `tools/validators/adr/` (validators)
- `.github/workflows/adr-checks.yml` (CI)
- `tests/governance/adr/` (validator tests + golden ADRs)

These paths are PROPOSED. Confirmation against the mounted repo is required before any of them is treated as canonical.

---

## First repo verification pass

Run this pass before promoting this README from `draft` or replacing `NEEDS VERIFICATION` in the ADR index.

> [!CAUTION]
> These commands are read-only discovery commands. They should be run from the mounted KFM checkout, not from an artifact workspace.

```bash
pwd
git status --short
git branch --show-current
git ls-tree -r --name-only HEAD docs/adr docs/doctrine docs/registers schemas contracts policy release data/receipts data/proofs 2>/dev/null | sort
find docs/adr -maxdepth 1 -type f -name 'ADR-*.md' | sort
```

Verification outcomes to record in the PR:

- [ ] `docs/adr/README.md` exists at the expected path or is created there.
- [ ] Every ADR file in `docs/adr/` appears in the index above.
- [ ] Every index row with a linked file resolves to an actual file or remains `NEEDS VERIFICATION`.
- [ ] Every ADR meta block has `status` in `proposed | accepted | superseded | rejected`.
- [ ] Every `superseded` ADR has a forward link and every successor has a back link.
- [ ] Directory Rules links resolve, especially authority order and §2.4 ADR triggers.
- [ ] Any domain-scoped ADR location conflict is entered in `docs/registers/DRIFT_REGISTER.md` or resolved by an ADR.
- [ ] Validation tooling homes are confirmed or left explicitly `PROPOSED`.

Do not use a green validation run to imply the listed starter ADRs exist. File presence, decision status, and enforcement status are separate facts.

---

## Review burden

| Change | Reviewers required |
|---|---|
| New `proposed` ADR | Architecture steward + at least one affected subsystem owner |
| Move `proposed` → `accepted` | Architecture steward + the subsystem owners listed in the ADR's `Affects` row |
| Move `accepted` → `superseded` (paired with successor) | Same as the successor ADR's review |
| Move `proposed` → `rejected` | Architecture steward |
| Edits to this README | Docs steward + Architecture steward |
| Reorganization of `docs/adr/` itself (e.g., adding a per-domain subtree) | **A new ADR is required** per Directory Rules §2.4 |

`CODEOWNERS` reference: **TODO** — populate once the file exists in the mounted repo. Until then, route PRs via the PR template's reviewer list.

---

## Related folders & doctrine

**Doctrine (in `docs/doctrine/`)**

- [`directory-rules.md`](../doctrine/directory-rules.md) — placement law; pins ADR conventions and §2.4 triggers
- [`authority-ladder.md`](../doctrine/authority-ladder.md) — where ADRs sit in the authority order
- [`lifecycle-law.md`](../doctrine/lifecycle-law.md) — the invariant ADRs must respect
- [`trust-membrane.md`](../doctrine/trust-membrane.md) — boundary ADRs cannot weaken without explicit `Consequences`
- [`truth-posture.md`](../doctrine/truth-posture.md) — cite-or-abstain default

**Architecture (in `docs/architecture/`)**

- [`contract-schema-policy-split.md`](../architecture/contract-schema-policy-split.md) — context for ADR-0001
- `system-context.md`, `deployment-topology.md`, `governed-api.md`, `map-shell.md` — frequent ADR neighbors

**Registers (in `docs/registers/`)**

- [`DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) — drift entries that frequently mature into ADRs
- [`VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) — open questions, often ADR seeds
- [`CANONICAL_LINEAGE_EXPLORATORY.md`](../registers/CANONICAL_LINEAGE_EXPLORATORY.md) — classifies what is canon vs lineage

**Machine-readable governance (in `control_plane/`)**

- `deprecation_register.yaml` — receives entries when an ADR deprecates a path or rule
- `contradiction_register.yaml` — surfaces conflicts that may need an ADR

---

## Maintenance checklist

Use this checklist when editing this README or reviewing an ADR PR.

- [ ] Preserve this README's H1, meta block `doc_id`, and existing section anchors unless a migration note explains the break.
- [ ] Update `updated:` in the meta block and `Last reviewed` when a repo-verified review occurs.
- [ ] Keep implementation claims labeled: `CONFIRMED`, `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.
- [ ] Update the ADR index and supersession links in the same PR that adds, accepts, rejects, or supersedes an ADR.
- [ ] Keep ADRs out of schemas, policies, release manifests, receipts, proof packs, and runbooks; route those artifacts to their responsibility roots.
- [ ] Add or update drift/backlog entries when repo reality and this README disagree.
- [ ] Avoid broad rewrites of accepted ADR bodies. Use successor ADRs for material changes.

---

## FAQ

<details>
<summary><strong>Should every architectural decision get an ADR?</strong></summary>

No. Trivial choices, local refactors, and decisions fully expressed in a schema or contract typically don't. The threshold from the corpus: *if the choice affects more than one component, or is non-obvious from code, write one*. When in doubt, write one — they are cheap, and the cost of an unrecorded decision compounds.
</details>

<details>
<summary><strong>What if a decision was made years ago and never recorded?</strong></summary>

Backfill it. Author it as `proposed`, mark the `Date` as the original decision date if known (or "backfill: YYYY-MM-DD" if not), and note in `Context` that this is a retroactive ADR. Move to `accepted` once the rationale and consequences are agreed by current stewards.
</details>

<details>
<summary><strong>Can I edit an accepted ADR?</strong></summary>

Only for typos, broken links, and meta-block hygiene. Anything substantive — including changes to `Decision`, `Consequences`, or `Alternatives` — requires a successor ADR. The whole point of ADRs is that the record is stable enough to cite.
</details>

<details>
<summary><strong>Where do domain ADRs live — here or under <code>docs/domains/&lt;domain&gt;/</code>?</strong></summary>

**NEEDS VERIFICATION.** The corpus shows both patterns. The PROPOSED working rule (until an ADR ratifies it): cross-cutting decisions live in `docs/adr/` with a global numeric ID; domain-scoped decisions live under `docs/domains/<domain>/` with either a per-domain number or a slug-only filename, and link forward to any cross-cutting ADR they depend on. Do not duplicate.
</details>

<details>
<summary><strong>What happens if an ADR conflicts with Directory Rules?</strong></summary>

An accepted ADR that explicitly amends Directory Rules wins (per [authority order §2.1](../doctrine/directory-rules.md#21-authority-order)). The ADR itself MUST cite the Rules section it amends, and the Rules document SHOULD be updated in the same PR (or a follow-up PR with a forward link from §0).
</details>

<details>
<summary><strong>How do ADRs relate to <code>CHANGELOG.md</code>?</strong></summary>

`CHANGELOG.md` records *what changed* in releases. ADRs record *why an architectural choice was made*. They are complementary: a release entry might say *"Adopted `schemas/contracts/v1/` as the schema home"* and link to `ADR-0001`. The ADR carries the rationale; the changelog carries the timing and surface impact.
</details>

<details>
<summary><strong>Can an ADR be marked <code>accepted</code> if its enforcement isn't built yet?</strong></summary>

Yes — but the `Consequences` section MUST list the enforcement work as a deferred operational consequence, and the corresponding entry SHOULD land in `docs/registers/VERIFICATION_BACKLOG.md`. An accepted-but-unenforced ADR is still authoritative; it is not yet *executable*.
</details>

<details>
<summary><strong>Are ADRs the right place to record source rights, sensitivity decisions, or release decisions?</strong></summary>

No.
- Source rights / sensitivity → `policy/sensitivity/`, `policy/rights/`, `data/registry/<domain>/sources.yaml`.
- Release decisions → `release/manifests/`, `release/promotion_decisions/`, `release/correction_notices/`.

An ADR can establish the *framework* for these decisions (e.g., ADR-0008 sets the fail-closed exact-location rule); the per-instance decisions live in policy and release artifacts.
</details>

---

## Last reviewed

`<TODO: YYYY-MM-DD on first repo-verified PR>` — flag for review if older than six months, per [Directory Rules §15](../doctrine/directory-rules.md#15-required-readme-contract).

---

### References

- `docs/doctrine/directory-rules.md` — §0 Authority, §2.1 Authority order, §2.4 Changes that require an ADR, §6.1 `docs/`, §7.4 schema-home convention, §15 Required README contract.
- *Kansas Frontier Matrix Pipeline Living Implementation Manual v0.3* — §28 Decision register / ADR index (PROPOSED starter set ADR-0001 through ADR-0010).
- *KFM Pass 12 Part 2 — Idea Index, Category Atlas, and Expansion Dossier* — J.3 ADR pattern; §9.2 alternative starter set.
- *KFM Components Pass 11 — Idea Index, Category Atlas, and Expansion Dossier* — J.4.1 ADRs for every consequential architectural choice.
- *KFM Whole-UI / Governed AI Expansion Report* — file-home and trust-boundary ADR examples.
- Domain dossiers (Archaeology, Agriculture, Atmosphere, Habitat/Fauna, Hydrology, Roads/Rail/Trade, Settlements/Infrastructure, Geology) — domain-scoped ADR examples.

[Back to top](#docsadr--architecture-decision-records)
