<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-template
title: ADR Template — Architecture Decision Record
type: standard
version: v1.1
status: draft
owners: ["Docs steward", "Architecture steward"]
created: 2026-05-09
updated: 2026-05-15
policy_label: public
related:
  - "docs/doctrine/directory-rules.md"
  - "docs/adr/README.md"
  - "docs/registers/DRIFT_REGISTER.md"
  - "docs/registers/VERIFICATION_BACKLOG.md"
tags: [adr, template, kfm, governance, documentation, directory-rules]
notes:
  - "Template doc; copy to ADR-NNNN-kebab-case-slug.md and fill in."
  - "Updated to align with Directory Rules responsibility-root, schema-home, migration, and no-parallel-authority discipline."
  - "Owners, related links, badge targets, parser path, and mounted-repo ADR inventory remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

# ADR Template — Architecture Decision Record

> Copy this file to `docs/adr/ADR-NNNN-<kebab-case-slug>.md`, fill it in, and open a PR. ADRs are the audit trail of architectural reasoning in Kansas Frontier Matrix — they are versioned and never deleted.

[![Doc type](https://img.shields.io/badge/type-template-blue)](#)
[![Status](https://img.shields.io/badge/status-draft-yellow)](#)
[![Authority](https://img.shields.io/badge/authority-docs%2Fadr-success)](#)
[![Lifecycle](https://img.shields.io/badge/never--delete-superseded%20kept-important)](#)
[![Placement](https://img.shields.io/badge/placement-Directory%20Rules-informational)](#)
[![Convention](https://img.shields.io/badge/RFC--2119-MUST%20%7C%20SHOULD%20%7C%20MAY-informational)](#)
<!-- Badge targets are placeholders — NEEDS VERIFICATION against the repo's badge convention. -->

| Field | Value |
|---|---|
| **Document type** | Standard (template) |
| **Owners** | Docs steward · Architecture steward *(PROPOSED until verified)* |
| **Canonical ADR home** | `docs/adr/` *(Directory Rules default; repo presence NEEDS VERIFICATION)* |
| **Schema-home convention** | `schemas/contracts/v1/...` as the default machine-schema home per Directory Rules / ADR-0001 |
| **Authority** | CONFIRMED doctrine source: `docs/doctrine/directory-rules.md` §2.4, §14, §16, §17 |
| **Truth posture** | CONFIRMED template doctrine / PROPOSED repo placement until mounted-repo inspection |
| **Last revised** | 2026-05-15 |

**Quick jumps:** [Purpose](#1-purpose) · [When to write one](#2-when-you-need-an-adr) · [Lifecycle](#3-status-lifecycle) · [Naming](#4-naming-and-numbering) · [How to use](#5-how-to-use-this-template) · [The template](#6-the-template) · [Field reference](#7-field-reference) · [Pre-merge checklist](#8-pre-merge-checklist) · [References](#9-related-docs--references) · [Open questions](#10-open-questions--needs-verification)

---

## 1. Purpose

An **Architecture Decision Record (ADR)** captures **one** consequential architectural decision: the **context** that forced it, the **choice** that was made, the **consequences** that follow, and the **alternatives** that were rejected. ADRs are the institutional memory that prevents settled choices from being silently re-litigated.

This template is the **canonical scaffold** every new ADR copies from. It encodes:

- The **field set** required by Directory Rules §2.4: `id`, `title`, `status`, `date`, `context`, `decision`, `consequences`, `alternatives`.
- The **status vocabulary** used across ADRs: `proposed | accepted | superseded | rejected`.
- The **never-delete discipline**: superseded ADRs **MUST** be retained with a forward link to the replacing ADR.
- The **placement and migration discipline** that keeps KFM responsibility roots stable and prevents parallel schema, contract, policy, source, registry, release, proof, or receipt homes.
- The **meta block** convention so ADRs are queryable from `related[]` references in README meta blocks and from doc-graph tooling.

> [!NOTE]
> ADRs **explain and record a decision**. They do not, by themselves, **enact** the change. Schemas, contracts, policy, fixtures, tests, registries, release objects, migrations, and runbooks enact. ADRs are referenced by the things that enact.

> [!IMPORTANT]
> ADR paths and numbering are **PROPOSED until verified** against the mounted repo. Do not claim a number, existing ADR, owner, parser, badge target, or CI enforcement status without current repo evidence.

[Back to top](#adr-template--architecture-decision-record)

---

## 2. When You Need an ADR

A new ADR is **required** before any change in the categories below. Sources: `docs/doctrine/directory-rules.md` §2.4, §14.2, §14.3, and §17.

| Trigger | Example | Required because |
|---|---|---|
| Add, remove, or rename a **canonical root** | Renaming `policy/` → `policies/` | §2.4(1) |
| Promote a **compatibility root** to canonical, or deprecate a canonical root | Retiring `artifacts/` or making `jsonschema/` canonical | §2.4(2) |
| Change the **schema-home rule** | Moving machine schemas from `schemas/contracts/v1/...` to `contracts/` | §2.4(3) |
| Split or merge a **lifecycle phase** | Splitting `data/processed/` or merging `data/receipts/` with `data/proofs/` | §2.4(4) |
| Create a **parallel home** for schemas, contracts, policy, sources, registries, releases, proofs, or receipts | Adding a second `release/` or letting `artifacts/` hold release manifests | §2.4(5) |
| **Bend an invariant** from Directory Rules §3 | Allowing a public route to bypass the trust membrane | §2.4(6) |
| **Structural moves**: schema-home migration, root change, lifecycle split | Moving schema authority, renaming a root, splitting a lifecycle directory | §14.2; migration manifest required |
| **Object-identity rename**: a rename that changes what an object *means* | `Source` → `SourceDescriptor` with semantic delta | §14.3; schema bump and compatibility tests required |
| Major restructure of Directory Rules or reversal of a canonical rule | Changing root policy or lifecycle law | §17 |

ADRs are **also strongly recommended** when a choice (a) affects more than one component, (b) is non-obvious from the code alone, (c) creates a release/publication consequence, or (d) changes how evidence, policy, review, correction, rollback, or public clients behave.

Smaller routine changes — typos, dead-link fixes, lane-internal moves that do not create parallel authority — follow the routine PR path in Directory Rules §14.1.

> [!IMPORTANT]
> If a change qualifies under §2.4 and lands without an ADR, it is a **drift event**. Open an entry in `docs/registers/DRIFT_REGISTER.md` and propose a retroactive ADR. Do not normalize the drift as new authority merely because it exists in the repo.

[Back to top](#adr-template--architecture-decision-record)

---

## 3. Status Lifecycle

ADRs move through a small, finite set of statuses. **CONFIRMED** vocabulary per Directory Rules §2.4: `proposed | accepted | superseded | rejected`.

```mermaid
flowchart LR
  P([proposed]):::start --> A([accepted]):::ok
  P --> R([rejected]):::stop
  A --> S([superseded]):::sup
  S -.forward link.-> N([new ADR-MMMM]):::new

  classDef start fill:#fff8d6,stroke:#a07900,color:#333
  classDef ok fill:#d6f5d6,stroke:#2a7d2a,color:#1a4d1a
  classDef stop fill:#f5d6d6,stroke:#a02a2a,color:#5a1a1a
  classDef sup fill:#e0e0e0,stroke:#666,color:#333
  classDef new fill:#d6e6ff,stroke:#2a5dab,color:#1a3a6e
```

**Rules.**

- **`proposed`** — drafted; not yet binding. Reviewers may comment, request changes, or reject.
- **`accepted`** — merged with `accepted` status; the decision is now in force. The decision is referenced from artifacts it governs: contracts, schemas, policies, registries, READMEs, migrations, tests, release objects, and runbooks.
- **`superseded`** — replaced by a later ADR. The file is **kept**; `superseded_by` links to the replacement ADR; the replacement's `supersedes` lists this ADR.
- **`rejected`** — proposed and not adopted. The file is **kept** as a record of the path not taken.

> [!CAUTION]
> **Never delete an ADR.** A stale ADR with `accepted` status but undocumented replacement behavior is worse than a missing one. If reality has drifted from the ADR, write a new ADR that supersedes it, update both meta blocks, and record the drift.

> [!NOTE]
> Some earlier KFM material may use `deprecated` as a lifecycle term. For ADR status, prefer **`superseded`**. If `deprecated` already appears in accepted repo conventions, treat the vocabulary as **NEEDS VERIFICATION** and resolve through an ADR or register entry rather than silently mixing terms.

[Back to top](#adr-template--architecture-decision-record)

---

## 4. Naming and Numbering

| Aspect | Rule |
|---|---|
| **Filename** | `ADR-NNNN-<kebab-case-slug>.md` — zero-padded 4-digit number; lower-kebab slug. |
| **Directory** | `docs/adr/` — canonical ADR home per Directory Rules; repo presence **NEEDS VERIFICATION**. |
| **ID format** | `ADR-NNNN` in the visible header table; `kfm://adr/ADR-NNNN` in the meta block `doc_id`. |
| **Numbering** | Monotonic, repo-wide. The next number = 1 + the highest existing number under `docs/adr/`. |
| **Slugs** | Short, action-oriented, decision-flavored. Examples: `schema-home-v1`, `finite-decision-outcomes`, `release-manifest-envelope`. |
| **Domain ADRs** | A domain-scoped ADR **MAY** be filed as `ADR-NNNN-<domain>-<slug>.md` (for example, `ADR-0014-hydrology-schema-home.md`) to keep it grep-able by domain. The numeric prefix remains monotonic across the repo. |
| **Title (H1)** | `# ADR-NNNN: <Concise decision title>` — match the slug semantically; do not duplicate the ID elsewhere in the title. |

> [!TIP]
> When proposing an ADR, claim the next number in the PR body and include the filename. Reviewers check that no concurrent PR has claimed the same number; collisions are resolved by re-numbering the later PR before merge.

[Back to top](#adr-template--architecture-decision-record)

---

## 5. How to Use This Template

1. **Verify the target home.** Confirm `docs/adr/` exists and inspect the highest existing ADR number. If unavailable, label the path and number **PROPOSED / NEEDS VERIFICATION**.
2. **Copy** this file to `docs/adr/ADR-NNNN-<kebab-case-slug>.md`.
3. **Update** the meta block: `doc_id`, `title`, `owners`, `created`, `updated`, `tags`, `related`, `supersedes`, and `superseded_by` as applicable.
4. **Replace** every placeholder. Remove author-guidance HTML comments before requesting review.
5. **Set status** to `proposed` until the decision is accepted or rejected.
6. **Fill the required sections**: Context, Decision, Consequences, Alternatives Considered, Evidence and References, Migration Plan, Rollback Plan, Open Questions, Change History.
7. **Classify the Directory Rules trigger.** Use `n/a — non-§2.4 decision` only when the change truly does not fall under §2.4, §14.2, §14.3, or §17.
8. **Cross-link** the ADR from any README, register, contract, schema, policy, runbook, migration manifest, or doc whose `related[]` array should include it.
9. **Open a PR.** Cite the relevant Directory Rules section, affected paths, superseded ADRs, migration manifest, rollback card, and verification commands.
10. **On merge**, update status to `accepted` or `rejected` in the same PR or an immediate follow-up.
11. **If superseded later**, do **not** delete this ADR. Set status to `superseded`, fill `superseded_by`, and ensure the replacing ADR's `supersedes` includes this ID.

[Back to top](#adr-template--architecture-decision-record)

---

## 6. The Template

> Copy everything inside the fenced block below into your new file. Edit placeholders and remove guidance comments before publishing.

```markdown
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-NNNN
title: <Concise, action-oriented decision title>
type: adr
version: v1
status: proposed
owners: ["<decider or steward team>"]
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related:
  - "docs/doctrine/directory-rules.md"
  - "<other governing or affected docs>"
tags: [adr, kfm, "<domain or topic tags>"]
supersedes: []          # ADR ids this decision replaces, if any
superseded_by: []       # filled in only when this ADR is later superseded
notes:
  - "NEEDS VERIFICATION: replace placeholders with mounted-repo evidence before acceptance."
[/KFM_META_BLOCK_V2] -->

# ADR-NNNN: <Title>

<One-paragraph TL;DR. The reader should know the decision, the trigger, and the expected effect after this paragraph.>

| Field | Value |
|---|---|
| **ID** | ADR-NNNN |
| **Status** | proposed |
| **Date** | YYYY-MM-DD |
| **Deciders** | <names or roles> |
| **Consulted** | <names, teams, or stewards> |
| **Informed** | <downstream owners notified> |
| **Supersedes** | — *(or `ADR-MMMM`)* |
| **Superseded by** | — |
| **Directory Rules trigger** | §2.4(?) / §14.2 / §14.3 / §17 / `n/a — non-structural decision` |
| **Primary responsibility root** | `<docs|control_plane|contracts|schemas|policy|tests|fixtures|tools|scripts|apps|packages|connectors|pipelines|pipeline_specs|data|release|runtime|infra|configs|migrations|examples>` |
| **Migration required** | yes / no |
| **Rollback required** | yes / no |
| **Truth posture** | CONFIRMED / PROPOSED / NEEDS VERIFICATION / UNKNOWN |

---

## 1. Context

<State the problem and the forces that require a decision now. Reference repo evidence — paths, schemas, fixtures, tests, registers, prior ADRs — where possible. Avoid generic best-practice prose; write what is specifically true of KFM.>

### 1.1 Decision drivers (forces)

- **<Force / constraint / quality requirement 1>** — <one-line rationale>
- **<Force / constraint / quality requirement 2>** — <one-line rationale>
- **<Force / constraint / quality requirement 3>** — <one-line rationale>

### 1.2 Evidence boundary

- **CONFIRMED:** <what was verified from repo files, tests, logs, generated artifacts, or governing docs>
- **PROPOSED:** <what is design intent but not yet implemented>
- **UNKNOWN:** <what evidence is missing>
- **NEEDS VERIFICATION:** <specific check required before acceptance>

### 1.3 Out of scope

- <What this ADR explicitly does **not** decide>

---

## 2. Decision

> **Decision:** <The chosen option, in one or two sentences.>

### 2.1 Specifics

- <Concrete sub-rule, schema choice, parameter, threshold, or path>
- <Concrete sub-rule, schema choice, parameter, threshold, or path>

### 2.2 Placement basis

| Question | Answer |
|---|---|
| **Primary responsibility** | <human doc / object meaning / machine shape / policy / validator / data lifecycle / release decision / runtime / etc.> |
| **Owning root** | `<root>/` |
| **Domain segment** | `<domain>` or `n/a — cross-domain` |
| **Lifecycle phase** | `<raw|work|quarantine|processed|catalog|triplets|published|receipts|proofs|registry|rollback>` or `n/a` |
| **Directory Rules section cited** | §<section> |
| **Parallel authority risk** | none / mitigated by <ADR, migration manifest, mirror class, deprecation entry> |

### 2.3 Conformance language

- **MUST** — <non-negotiable element>
- **SHOULD** — <strong default; deviation requires justification>
- **MAY** — <permitted variation>

---

## 3. Consequences

### 3.1 Positive

- <Benefit, capability unlocked, or risk reduced>

### 3.2 Negative

- <Cost, complexity introduced, or capability foreclosed>

### 3.3 Accepted tradeoffs

- <Tradeoff knowingly accepted; explain why it is acceptable here>

### 3.4 Affected surfaces

| Surface | File / path | Impact |
|---|---|---|
| Contracts | `contracts/<...>` | <created · updated · superseded · not affected> |
| Schemas | `schemas/contracts/v1/<...>` | <created · updated · superseded · not affected> |
| Policy | `policy/<...>` | <created · updated · superseded · not affected> |
| Tests / fixtures | `tests/<...>` · `fixtures/<...>` | <created · updated · superseded · not affected> |
| Registries | `data/registry/<...>` · `control_plane/<...>` | <created · updated · superseded · not affected> |
| Data lifecycle | `data/<phase>/<domain>/...` | <created · updated · superseded · not affected> |
| Release | `release/<...>` | <manifest · promotion decision · rollback card · correction notice · not affected> |
| Docs | `docs/<...>` | <created · updated · superseded · not affected> |
| Apps / runtime | `apps/<...>` · `runtime/<...>` | <created · updated · superseded · not affected> |
| Pipelines / tools | `pipelines/<...>` · `tools/<...>` | <created · updated · superseded · not affected> |
| Migrations | `migrations/<schema|data|database|graph|rollback>/...` | <created · updated · not affected> |

---

## 4. Alternatives Considered

### 4.1 <Alternative A — name>

- **Summary:** <one or two sentences>
- **Why rejected:** <one or two sentences>

### 4.2 <Alternative B — name>

- **Summary:** <…>
- **Why rejected:** <…>

### 4.3 Status quo (do nothing)

- **Why rejected:** <what breaks, drifts, or remains unverifiable if no decision is made>

---

## 5. Evidence and References

<List the evidence that grounds the decision. Prefer relative repo paths and permalinks at specific commits when pinning matters. If evidence is absent or unverified, label it PROPOSED or NEEDS VERIFICATION.>

- Doctrine: `docs/doctrine/directory-rules.md` §<sec>
- Prior ADRs: `docs/adr/ADR-MMMM-<slug>.md`
- Contracts: `contracts/<...>`
- Schemas: `schemas/contracts/v1/<...>`
- Policies: `policy/<...>`
- Tests / fixtures: `tests/<...>` · `fixtures/<...>`
- Registries: `data/registry/<...>` · `control_plane/<...>`
- Data / release artifacts: `data/<phase>/<...>` · `release/<...>`
- Migrations: `migrations/<...>`
- External standards: <RFC, spec, or normative reference, with version pin>

---

## 6. Migration Plan

<Required for §2.4 structural changes, schema-home migration, lifecycle phase splits, root changes, parallel-home creation, invariant bends, and object-identity renames. For other ADRs, write: `Not applicable — non-structural decision.`>

- **Old → new mapping:** see `migrations/<schema|data|database|graph>/<adr-NNNN>/manifest.yaml`
- **Mirror window:** <duration; mark mirrors `mirror` per Directory Rules §8>
- **Deprecation entry:** `control_plane/deprecation_register.yaml` with sunset date <YYYY-MM-DD>
- **References to update:** code, docs, contracts, schemas, fixtures, tests, workflows, registries, release objects
- **Compatibility tests:** <old fixture parity / consumer compatibility checks>
- **Validators to run:** <list>
- **Drift register check:** confirm no new unresolved entries remain post-migration

---

## 7. Rollback Plan

<Required for §2.4 structural changes and recommended for implementation-significant decisions. A rollback plan must be runnable, not aspirational. For other ADRs, write: `Not applicable — non-structural decision.`>

- **Trigger conditions:** <what observable failure mode reverts this decision>
- **Rollback steps:**
  1. <Concrete step>
  2. <Concrete step>
- **Compatibility:** <whether old fixtures/consumers still work; for how long>
- **Dry-run rollback card:** `release/rollback_cards/ADR-NNNN-dry-run.md` *(if applicable)*
- **Verification:** <tests / validators / smoke checks that confirm rollback success>

---

## 8. Open Questions

- <Question that this ADR does not yet resolve>
- <Question deferred to a follow-up ADR or to a register entry>

---

## 9. Change History

| Date | Status | Change | PR |
|---|---|---|---|
| YYYY-MM-DD | proposed | Initial draft | #<num> |
| YYYY-MM-DD | accepted | Merged after review | #<num> |
| YYYY-MM-DD | superseded | Replaced by ADR-MMMM | #<num> |
```

[Back to top](#adr-template--architecture-decision-record)

---

## 7. Field Reference

<details>
<summary><strong>Meta block fields</strong></summary>

| Field | Required | Notes |
|---|---|---|
| `doc_id` | yes | `kfm://adr/ADR-NNNN`. Stable join key for doc-graph tooling. |
| `title` | yes | Match the H1; concise, action-oriented. |
| `type` | yes | `adr` for ADRs. |
| `version` | yes | Document version, not the decision version. Increment on substantive edits. |
| `status` | yes | `proposed` · `accepted` · `superseded` · `rejected`. |
| `owners` | yes | Decider names or steward team. Use placeholders only while `proposed`. |
| `created` / `updated` | yes | ISO `YYYY-MM-DD`. |
| `policy_label` | yes | Usually `public` for ADRs. Use `restricted` only with explicit cause. |
| `related` | recommended | Affected READMEs, contracts, schemas, policies, doctrine docs, prior ADRs, registries, migrations. |
| `tags` | recommended | Always include `adr` and `kfm`; add domain/topic tags. |
| `supersedes` | conditional | Array of ADR ids this replaces. Empty if none. |
| `superseded_by` | conditional | Filled when this ADR is later replaced. |
| `notes` | optional | Short notes for reviewers; do not duplicate body content. |

</details>

<details>
<summary><strong>Body sections</strong></summary>

| Section | Required | Purpose |
|---|---|---|
| **TL;DR paragraph** | yes | One paragraph; the decision is clear after this paragraph alone. |
| **Header table** | yes | ID, status, date, deciders, supersession, Directory Rules trigger, placement, migration/rollback posture. |
| **1. Context** | yes | The problem and forces. Reference repo evidence. |
| **1.1 Decision drivers** | yes | Bulleted forces / quality requirements. |
| **1.2 Evidence boundary** | yes | CONFIRMED / PROPOSED / UNKNOWN / NEEDS VERIFICATION split. |
| **1.3 Out of scope** | recommended | Prevents scope creep in review. |
| **2. Decision** | yes | The chosen option, with RFC 2119 conformance language where appropriate. |
| **2.2 Placement basis** | yes when path-bearing | Responsibility root, lifecycle phase, domain segment, rule citation, parallel-authority risk. |
| **3. Consequences** | yes | Positive, negative, accepted tradeoffs, affected surfaces. |
| **4. Alternatives Considered** | yes | At least one alternative + the status quo. |
| **5. Evidence and References** | yes | Repo paths, prior ADRs, external standards, fixtures, validators, release objects. |
| **6. Migration Plan** | conditional | Required for §2.4 structural changes and §14.2 moves; otherwise `Not applicable.` |
| **7. Rollback Plan** | conditional | Required for §2.4 structural changes and recommended for implementation-significant decisions. |
| **8. Open Questions** | recommended | Honest deferrals; do not pretend a question is closed. |
| **9. Change History** | yes | Append-only; never delete rows. |

</details>

[Back to top](#adr-template--architecture-decision-record)

---

## 8. Pre-Merge Checklist

Apply conditionally — do not fabricate to satisfy a box.

- [ ] **Filename** matches `ADR-NNNN-<kebab-case-slug>.md`; number is unique and monotonic.
- [ ] **Meta block** is present, parseable, and has `type: adr`, status `proposed | accepted | superseded | rejected`, and valid `doc_id`.
- [ ] **Header table** lists the Directory Rules trigger or explicit `n/a — non-§2.4 decision`.
- [ ] **Placement basis** identifies the responsibility root, lifecycle phase if data, domain segment if domain-specific, and the Directory Rules section cited.
- [ ] **No domain folder** is added at repo root; domain work lives inside responsibility roots.
- [ ] **No parallel authority** is created for schemas, contracts, policy, sources, registries, releases, proofs, or receipts without an ADR and migration plan.
- [ ] **Decision** is unambiguous and uses RFC 2119 keywords where conformance is implied.
- [ ] **Alternatives** section contains at least one alternative **plus** the status-quo case.
- [ ] **Consequences** section names affected surfaces with concrete repo paths.
- [ ] **Evidence** section cites real paths, schemas, fixtures, tests, registries, release objects, or external standards — not generic best practice.
- [ ] **Migration Plan** and **Rollback Plan** are filled in if §2.4, §14.2, §14.3, or §17 applies.
- [ ] **Migration manifest** exists under `migrations/<schema|data|database|graph>/...` when required.
- [ ] **Rollback card** exists or is explicitly not applicable; rollback is runnable, not aspirational.
- [ ] **Cross-references** added to README `related[]` arrays or register entries for affected lanes and object families.
- [ ] **Supersession links** are bidirectional: `supersedes` ↔ `superseded_by`, both meta blocks updated.
- [ ] **Drift register** checked; conflicts with Directory Rules are recorded in `docs/registers/DRIFT_REGISTER.md` rather than silently normalized.
- [ ] **Verification backlog** records unresolved repo, parser, owner, CI, or path checks.
- [ ] **Status** set to `accepted` or `rejected` in the same merge or an immediate follow-up.
- [ ] **No deletions** of prior ADR files; superseded ADRs remain on disk.
- [ ] **PR body** cites the Directory Rules section that justifies the decision.

[Back to top](#adr-template--architecture-decision-record)

---

## 9. Related Docs & References

- `docs/doctrine/directory-rules.md` — §2.4 (changes that require an ADR), §4 (placement protocol), §8 (compatibility roots), §14 (migration discipline), §16 (path-validation checklist), §17 (document change discipline).
- `docs/adr/README.md` — ADR index and process overview *(PROPOSED until verified in repo).*
- `docs/registers/DRIFT_REGISTER.md` — where to log conflicts between doctrine and the mounted repo *(PROPOSED until verified in repo).*
- `docs/registers/VERIFICATION_BACKLOG.md` — where to log open verification items *(PROPOSED until verified in repo).*
- `control_plane/deprecation_register.yaml` — sunset entries for migrations driven by ADRs *(PROPOSED until verified in repo).*
- `migrations/data/` · `migrations/schema/` · `migrations/database/` · `migrations/graph/` · `migrations/rollback/` — migration and rollback manifests pinned by structural ADRs *(PROPOSED until verified in repo).*
- `release/rollback_cards/` — rollback cards for release and structural decisions *(PROPOSED until verified in repo).*

**Starter ADR set referenced by the corpus** (illustrative; numbering follows monotonic order at the time the ADR is filed):

| ADR | Decision |
|---|---|
| ADR-0001 | Schema-home / spec normalization / hash and ID derivation v1, depending on the accepted repo ADR inventory. |
| ADR-0002 | Finite decision outcomes (`ANSWER` · `ABSTAIN` · `DENY` · `ERROR`). |
| ADR-0003 | Watcher non-publisher invariant. |
| ADR-0004 | KFM STAC profile v1. |
| ADR-0005 | ReleaseManifest as the publication envelope. |
| ADR-0006 | Crypto stack pin (BLAKE3 + BAO + DSSE + cosign + Rekor). |

> [!NOTE]
> The starter set above is illustrative. Whether each ADR exists, what number it uses, and what exact title it has is **NEEDS VERIFICATION** against `docs/adr/` in the mounted repo.

[Back to top](#adr-template--architecture-decision-record)

---

## 10. Open Questions / NEEDS VERIFICATION

These items are explicitly **not resolved** by this template and should be tracked in `docs/registers/VERIFICATION_BACKLOG.md`:

- **NEEDS VERIFICATION:** Whether `docs/adr/` exists in the mounted repo and what ADRs it already contains. Until verified, the canonical home and starter ADR set are PROPOSED.
- **NEEDS VERIFICATION:** Whether `docs/adr/README.md` exists and defines any repo-specific ADR workflow that should refine this template.
- **NEEDS VERIFICATION:** Whether a documentation linter / parser (`tools/docs/parse_meta_block.py` or equivalent) is wired in CI to validate ADR meta blocks.
- **NEEDS VERIFICATION:** Whether the `KFM_META_BLOCK_V2` schema is published and where it lives. Do not hard-code the path until repo inspection confirms it.
- **NEEDS VERIFICATION:** Whether ADR enforcement is **advisory** (PR reviewer discretion) or **hard** (CI denies §2.4 PRs without an ADR). Pin the cutover date and enforcement mechanism in a follow-up ADR.
- **NEEDS VERIFICATION:** Whether earlier accepted ADRs use `deprecated` as an ADR status. This template treats `superseded` as canonical for ADR status, but the repo inventory must confirm no accepted vocabulary conflict.
- **OPEN:** Whether every affected lane README **MUST** reference the ADR in `related[]`, or only lane READMEs materially changed by the ADR.
- **OPEN:** Whether `ADR-0001` is strictly schema-home, spec normalization, or both in the mounted repo. This template uses Directory Rules as the governing source until the ADR inventory is inspected.

[Back to top](#adr-template--architecture-decision-record)
