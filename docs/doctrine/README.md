# `docs/doctrine/`

> **The small, stable layer of invariants that govern every other surface in the Kansas Frontier Matrix repository.**
> Doctrine encodes *how* KFM is allowed to know, decide, publish, and correct. It is the highest layer in the
> authority ladder. Every other root operationalizes it; none of them overrules it.

<!--
Repo placement: docs/doctrine/README.md
Authority root: docs/ (Canonical) — see ../README.md and ../../README.md
Owning doctrine: directory-rules.md §6.1
This README is a directory landing page. The numbered, prose-heavy doctrine documents
are the substantive sources of truth; this file orients readers to them.
-->

[![authority: doctrine](https://img.shields.io/badge/authority-doctrine-1f6feb)](./directory-rules.md)
[![conformance: RFC 2119](https://img.shields.io/badge/conformance-RFC%202119-555)](./directory-rules.md#22-conformance-language-rfc-2119-style)
[![change: ADR required](https://img.shields.io/badge/change-ADR%20required-orange)](../adr/)
[![status: active](https://img.shields.io/badge/status-active-2ea043)](#status)
[![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92WORK%2FQ%E2%86%92PROCESSED%E2%86%92CATALOG%2FTRIPLET%E2%86%92PUBLISHED-555)](./lifecycle-law.md)

> **Badge targets are placeholders** until the relevant docs and CI signals are live. Do not treat them as
> proof of enforcement. See [Validation](#validation) and [Open questions](#open-questions--needs-verification).

---

## Quick navigation

[Scope](#scope) ·
[Authority](#authority-level) ·
[Status](#status) ·
[Documents](#documents-in-this-folder) ·
[What belongs here](#what-belongs-here) ·
[What does NOT belong here](#what-does-not-belong-here) ·
[Doctrine map](#doctrine-map) ·
[Inputs](#inputs) ·
[Outputs](#outputs) ·
[Validation](#validation) ·
[Change discipline](#change-discipline) ·
[Review burden](#review-burden) ·
[Related folders](#related-folders) ·
[ADRs](#adrs) ·
[Open questions](#open-questions--needs-verification) ·
[Glossary](#mini-glossary) ·
[Last reviewed](#last-reviewed)

---

## Scope

This folder is the **doctrinal layer** of the human-facing control plane. It contains the
small, stable set of documents that define KFM's non-negotiable invariants — the things that
must remain true across every domain, every release, every contributor, and every iteration
of the implementation.

Doctrine answers questions like:

- *What ranks above what when sources disagree?* → [`authority-ladder.md`](./authority-ladder.md)
- *What does it mean for KFM to "know" something?* → [`truth-posture.md`](./truth-posture.md)
- *Who is allowed to publish, and how?* → [`trust-membrane.md`](./trust-membrane.md)
- *What lifecycle must data move through before it is public?* → [`lifecycle-law.md`](./lifecycle-law.md)
- *Where do new files belong?* → [`directory-rules.md`](./directory-rules.md)

Doctrine **does not** decide individual cases. Per-case decisions are made by `contracts/` (meaning),
`schemas/` (shape), `policy/` (admissibility), `tests/` (proof), ADRs (architecture decisions), and
`release/` (release decisions). Doctrine is the frame those layers are required to honour.

> [!IMPORTANT]
> A `docs/` page is **not** the source of a canonical decision on its own. Documentation explains;
> ADRs decide; contracts, schemas, policy, and tests enforce. Doctrine is special only in that it
> sets the frame *all* of those operate within. Changing doctrine therefore requires an ADR.
> See [`directory-rules.md` §13.5 (Documentation as truth anti-pattern)](./directory-rules.md#135-additional-anti-patterns)
> and [§17 (Document change discipline)](./directory-rules.md#17-document-change-discipline).

[↑ Back to top](#docsdoctrine)

---

## Authority level

| Field | Value |
|---|---|
| **Authority class** | Canonical · doctrinal |
| **Position in authority order** | Layer 1 — top of the ladder per [`directory-rules.md` §2.1](./directory-rules.md#21-authority-order) |
| **Conformance language** | RFC 2119-style: MUST / MUST NOT / SHOULD / SHOULD NOT / MAY |
| **Change governs** | ADR required for any change that bends an invariant ([`directory-rules.md` §2.4](./directory-rules.md#24-changes-that-require-an-adr)) |
| **What overrules doctrine** | Only an accepted ADR that explicitly amends doctrine, with supersession discipline |
| **What does *not* overrule doctrine** | Per-root READMEs, domain dossiers, prior architecture reports, current repo convention, generated artifacts, model output |

**CONFIRMED** — the *role* of `docs/doctrine/` and the listed authority order are doctrine, captured in
[`directory-rules.md` §2.1, §2.4, §6.1](./directory-rules.md).

**NEEDS VERIFICATION** — whether the live repository currently contains every file enumerated below
(see [Open questions](#open-questions--needs-verification)).

[↑ Back to top](#docsdoctrine)

---

## Status

| Field | Value |
|---|---|
| **Folder status** | active |
| **Per-file status** | mixed — see [Documents](#documents-in-this-folder) |
| **Overall doctrine maturity** | CONFIRMED as doctrine; PROPOSED as a complete authored set in any specific repo until each file is verified present |
| **Owners** | Docs steward · KFM architecture council (placeholder until `CODEOWNERS` is verified) |
| **Last reviewed** | `YYYY-MM-DD` (placeholder — set on first merge; see [Last reviewed](#last-reviewed)) |

[↑ Back to top](#docsdoctrine)

---

## Documents in this folder

The doctrinal set listed in [`directory-rules.md` §6.1](./directory-rules.md#61-docs--the-human-facing-control-plane).

| File | Encodes | Status (in this corpus) | Notes |
|---|---|---|---|
| [`README.md`](./README.md) | This orientation document. | CONFIRMED (this file) | Directory landing page. Not itself a source of doctrine — it points to the docs that are. |
| [`authority-ladder.md`](./authority-ladder.md) | The order in which sources, documents, and runtime evidence are ranked when they disagree. | PROPOSED | A standalone authored doc is listed in §6.1 but not yet verified present. The *ladder itself* is CONFIRMED doctrine and partially encoded in [`directory-rules.md` §2.1](./directory-rules.md#21-authority-order). |
| [`truth-posture.md`](./truth-posture.md) | **Cite-or-abstain.** Every consequential claim either resolves to an `EvidenceBundle` or returns `ABSTAIN` / `DENY` / `ERROR`. Fluent text never substitutes for evidence. | PROPOSED | The posture is CONFIRMED doctrine across the corpus; the standalone file is not yet verified present. |
| [`trust-membrane.md`](./trust-membrane.md) | Public clients consume **governed APIs and released artifacts only**. RAW / WORK / QUARANTINE / candidate / direct-model paths are non-public. | PROPOSED | The boundary is CONFIRMED doctrine; the operational form is `apps/governed-api/`. |
| [`lifecycle-law.md`](./lifecycle-law.md) | **RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED.** Promotion is a governed state transition, not a file move. | PROPOSED | The invariant is CONFIRMED doctrine; the standalone file is not yet verified present. |
| [`directory-rules.md`](./directory-rules.md) | Where files belong. Responsibility roots, lifecycle phases, domain-as-segment, compatibility roots, anti-patterns, migration discipline. | CONFIRMED — present in this corpus | The canonical placement-rules document. |

> [!NOTE]
> One named invariant — **watcher-as-non-publisher** ("workers emit receipts and candidate decisions only;
> they do not publish, mutate canonical records, or bypass review") is invoked in
> [`directory-rules.md` §2.1](./directory-rules.md#21-authority-order) but does not have its own listed file
> in §6.1. It is currently expressed inside `trust-membrane.md` (PROPOSED) and the canonical-tree commentary.
> Whether to split it into a sixth doctrine doc is an [open question](#open-questions--needs-verification).

[↑ Back to top](#docsdoctrine)

---

## What belongs here

Only documents that:

1. State a KFM-wide **invariant** that constrains every domain, app, package, pipeline, and release.
2. Are written for **humans** (Markdown prose, RFC 2119-style conformance language, examples).
3. Are **stable enough to require an ADR to change** — not workshopped material.
4. Sit at the **top of the authority ladder** and define the frame for `contracts/` / `schemas/` / `policy/` / `tests/`.

If a document does not satisfy all four, it does not belong in `docs/doctrine/`.

## What does NOT belong here

| Content | Belongs in | Why not here |
|---|---|---|
| Architecture decisions (one decision, with context / consequences / alternatives) | [`docs/adr/`](../adr/) | ADRs *amend* doctrine; doctrine is the frame ADRs operate within. |
| System-context, deployment, governed-API, map-shell, contract/schema/policy split docs | [`docs/architecture/`](../architecture/) | Architecture explains how the system *implements* doctrine. Different layer. |
| Domain-specific architecture, dossiers, source registries | [`docs/domains/<domain>/`](../domains/) | Domains are lanes inside responsibility roots — never doctrine. |
| Operational procedures, rollback drills, validation runs | [`docs/runbooks/`](../runbooks/) | Operations apply doctrine; they don't define it. |
| Threat model, exposure posture, incident response | [`docs/security/`](../security/) | Security operationalizes the trust membrane; it's not the doctrine itself. |
| Roles, review burden, separation of duties | [`docs/governance/`](../governance/) | Governance procedures live in their own lane. |
| Authority / lineage / drift / verification *registers* (machine-readable) | [`control_plane/`](../../control_plane/) (machine) · [`docs/registers/`](../registers/) (human-readable index) | Registers index "what governs what"; doctrine *defines* what governs. Different layer. |
| External standards KFM conforms to (STAC, DCAT, PROV, JSON-LD, etc.) | [`docs/standards/`](../standards/) | External standards are referenced, not authored as doctrine. |
| Source-descriptor standards, source families | [`docs/sources/`](../sources/) | Source identity is its own concern. |
| Idea intake, exploratory packets, archived lineage | [`docs/intake/`](../intake/) · [`docs/archive/`](../archive/) | Exploratory by definition; not doctrine. |
| Generated review / release reports | [`docs/reports/`](../reports/) | Read-only outputs of governed runs. |
| Object-family **meaning** (what an object means) | [`contracts/`](../../contracts/) | Different layer of the same governance function. |
| Object **shape** (machine-checkable) | [`schemas/`](../../schemas/) | Default home: `schemas/contracts/v1/...` per ADR-0001. |
| **Admissibility / release** decisions (allow / deny / restrict / abstain) | [`policy/`](../../policy/) · [`release/`](../../release/) | Doctrine sets the frame; policy decides individual cases. |
| Proof that doctrine is enforceable | [`tests/`](../../tests/) · [`fixtures/`](../../fixtures/) | Tests prove the rules; doctrine states them. |

> [!CAUTION]
> **Documentation-as-truth is an anti-pattern.** A `docs/` page MUST NOT be cited as the source of a canonical
> decision. Promote canonical decisions to an ADR or to a `control_plane/` register.
> See [`directory-rules.md` §13.5](./directory-rules.md#135-additional-anti-patterns).

[↑ Back to top](#docsdoctrine)

---

## Doctrine map

How `docs/doctrine/` relates to the rest of the repository:

```mermaid
flowchart TD
  classDef doctrine fill:#e8f0ff,stroke:#1f6feb,color:#0b3d91,stroke-width:2px;
  classDef adr fill:#fff7e6,stroke:#bf8700,color:#5a3d00;
  classDef govern fill:#f0fff4,stroke:#1a7f37,color:#0a4a1f;
  classDef impl fill:#f6f8fa,stroke:#57606a,color:#24292f;
  classDef public fill:#fff5f5,stroke:#cf222e,color:#82071e;

  D["docs/doctrine/<br/><b>Invariants</b><br/>authority-ladder · truth-posture<br/>trust-membrane · lifecycle-law<br/>directory-rules"]:::doctrine

  ADR["docs/adr/<br/>Architecture decisions<br/>(amend doctrine via ADR)"]:::adr
  ARCH["docs/architecture/<br/>System context, governed-API,<br/>contract/schema/policy split"]:::govern
  CP["control_plane/<br/>Machine-readable registers<br/>(authority · drift · lineage)"]:::govern
  C["contracts/<br/>Object meaning"]:::govern
  S["schemas/<br/>Machine-checkable shape"]:::govern
  P["policy/<br/>Admissibility · allow/deny/restrict/abstain"]:::govern
  T["tests/ + fixtures/<br/>Enforceability proof"]:::govern

  PIPE["pipelines/ · connectors/ · packages/<br/>data/ lifecycle (RAW → … → PUBLISHED)"]:::impl
  REL["release/<br/>Decisions · manifests · rollback · correction"]:::impl
  API["apps/governed-api/<br/><b>Trust membrane</b> in executable form"]:::public
  UI["apps/explorer-web/ · review-console<br/>Public &amp; semi-public clients"]:::public

  D -- "frames"      --> ARCH
  D -- "frames"      --> C
  D -- "frames"      --> S
  D -- "frames"      --> P
  D -- "frames"      --> T
  D -- "indexed by"  --> CP
  ADR -- "amends with discipline" --> D

  ARCH --> API
  C --> S
  S --> P
  P --> PIPE
  PIPE --> REL
  REL --> API
  API --> UI

  UI -. "MUST NOT bypass" .-> PIPE
  UI -. "MUST NOT read" .-> D
```

**Reading the diagram.** Doctrine sits above architecture. Architecture explains how doctrine is realized.
Contracts / schemas / policy / tests operationalize doctrine for individual object families and decisions.
The `control_plane/` indexes doctrine and its consequences in machine-readable form. ADRs are the *only*
mechanism that may amend doctrine, and they do so with supersession discipline. Public clients reach data
exclusively through the governed API — never around the lifecycle, never directly through documentation.

[↑ Back to top](#docsdoctrine)

---

## Inputs

Doctrine is authored, not generated. Inputs to this folder are:

- **Lessons surfaced from prior reports and dossiers** in `docs/archive/lineage/`, `docs/archive/exploratory/`, and the
  PDF corpus underpinning the redesign — once promoted from exploratory to invariant.
- **Accepted ADRs** that explicitly amend or supersede a doctrine claim.
- **Editorial PRs** by the Docs steward with subsystem-owner sign-off.

Doctrine MUST NOT be authored from generated text, model output, or unreviewed external material.
The governed-AI rule applies: AI is interpretive, not the root truth source.

## Outputs

Doctrine emits *constraints*, not artifacts. Concretely, it constrains:

- **`docs/architecture/`** — architecture must be consistent with the trust membrane and lifecycle law.
- **`contracts/`** — object meanings must respect the authority ladder and cite-or-abstain posture.
- **`schemas/contracts/v1/...`** — machine shapes must reflect contract meaning, not invent it.
- **`policy/`** — allow / deny / restrict / abstain decisions must implement the truth posture.
- **`tests/`** and **`fixtures/`** — must prove every doctrinal invariant is enforceable.
- **`release/`** — release manifests, rollback cards, and correction notices must satisfy the publication gate.
- **`apps/governed-api/`** — the executable form of the trust membrane.
- **`docs/registers/`** and **`control_plane/`** — register the authority order, drift, and lineage relative to doctrine.

[↑ Back to top](#docsdoctrine)

---

## Validation

Doctrine is enforced *operationally*, not by the doctrine documents themselves. The intended enforcement
surfaces (per [`directory-rules.md` §16](./directory-rules.md#16-path-validation-checklist-for-reviewers) and the
attached implementation reports) are:

| Doctrine claim | Enforcement surface |
|---|---|
| Authority ladder | Reviewer checklist; `docs/registers/AUTHORITY_LADDER.md`; PR description must cite the rule |
| Cite-or-abstain | `RuntimeResponseEnvelope` finite outcomes (ANSWER · ABSTAIN · DENY · ERROR); citation-validation tests |
| Trust membrane | `apps/governed-api/` route discipline; no-public-raw-route tests; CI workflow gate |
| Lifecycle law | Lifecycle layout validator; promotion-gate policy; `release/manifests/`; rollback cards |
| Directory rules | Path-validation checklist; per-root README contract; drift-register scan |
| Watcher-as-non-publisher | Worker access controls; receipt-only emission tests |

**PROPOSED** — every specific tool, workflow, validator, or test name above is proposed until verified
against a mounted repository. The *enforcement model* is doctrine; the *enforcement code* is implementation.

[↑ Back to top](#docsdoctrine)

---

## Change discipline

Per [`directory-rules.md` §17](./directory-rules.md#17-document-change-discipline), changes to doctrine follow
the same rules they impose:

| Change | What's required |
|---|---|
| Typo, clarification, dead-link fix | Routine PR. |
| New example, anti-pattern, or non-normative note | PR + reviewer sign-off. |
| **Adding, removing, or renaming an invariant** | **ADR required.** Supersession notice for any superseded text. Drift-register entry while the change is in flight. |
| **Reversing a previously stated rule** | ADR + supersession notice + drift-register entry. |
| Major restructure of a doctrine document | ADR + migration plan + transition window. |

All changes MUST preserve link stability where reasonably possible: stable anchors, stable filenames,
preserved ToC ordering. When stability cannot be preserved, the PR MUST note the breakage and update
inbound links.

## Review burden

| Role | Responsibility |
|---|---|
| **Docs steward** | First reviewer for any change in this folder. Mandatory. |
| **Subsystem owner** | At least one — chosen by the doctrine claim being touched. Mandatory. |
| **Architecture council** | Required for any change touching trust-membrane, lifecycle-law, authority-ladder, or directory-rules. |
| **CODEOWNERS** | The repo's `CODEOWNERS` file (or `.github/CODEOWNERS`) MUST list this folder explicitly. **NEEDS VERIFICATION** in the live repo. |

[↑ Back to top](#docsdoctrine)

---

## Related folders

| Path | Relationship |
|---|---|
| [`../README.md`](../README.md) | Top-level `docs/` landing page. Names doctrine as the first-class layer of the human-facing control plane. |
| [`../adr/`](../adr/) | Architecture Decision Records — the only mechanism that may amend doctrine. |
| [`../architecture/`](../architecture/) | Explains *how* doctrine is implemented. Includes `contract-schema-policy-split.md`, the architectural counterpart to `directory-rules.md`. |
| [`../registers/`](../registers/) | Human-readable indexes (`AUTHORITY_LADDER.md`, `CANONICAL_LINEAGE_EXPLORATORY.md`, `DRIFT_REGISTER.md`, `VERIFICATION_BACKLOG.md`). Reference doctrine; do not redefine it. |
| [`../governance/`](../governance/) | Roles, review burden, separation-of-duties procedure. Operationalizes doctrine. |
| [`../../control_plane/`](../../control_plane/) | Machine-readable registers (`document_registry.yaml`, `policy_gate_register.yaml`, etc.) that index what doctrine governs. |
| [`../../contracts/`](../../contracts/) | Object meaning. Doctrine constrains the meanings; contracts state them. |
| [`../../schemas/`](../../schemas/) | Machine-checkable shape (default: `schemas/contracts/v1/...` per ADR-0001). |
| [`../../policy/`](../../policy/) | Admissibility / release. Implements truth posture and trust membrane in executable policy. |
| [`../../tests/`](../../tests/) · [`../../fixtures/`](../../fixtures/) | Proof that doctrine is enforceable. |
| [`../../release/`](../../release/) | Release decisions, manifests, rollback cards, correction notices — the operational form of the publication gate. |
| [`../../apps/governed-api/`](../../apps/governed-api/) | The trust membrane in executable form. |

[↑ Back to top](#docsdoctrine)

---

## ADRs

| ADR | Subject | Doctrine link |
|---|---|---|
| **ADR-0001** | Schema-home rule: `schemas/contracts/v1/...` is the canonical machine-schema home. | Cited by [`directory-rules.md` §0 and §7.4](./directory-rules.md). PROPOSED-as-present until the live repo is verified. |
| *(none yet specifically governing other doctrine docs)* | — | A doctrine-amending ADR template SHOULD include: `id`, `title`, `status`, `date`, `context`, `decision`, `consequences`, `alternatives`, plus *which doctrine claim is amended* and the supersession path. See [`directory-rules.md` §2.4](./directory-rules.md#24-changes-that-require-an-adr). |

[↑ Back to top](#docsdoctrine)

---

## Open questions / NEEDS VERIFICATION

These items are **not** resolved by this README. They should be tracked in
[`../registers/VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) and resolved via ADR or
per-root README:

- **NEEDS VERIFICATION** — whether the mounted repo currently contains
  `authority-ladder.md`, `truth-posture.md`, `trust-membrane.md`, `lifecycle-law.md` as standalone authored files.
  Until verified, these are PROPOSED.
- **NEEDS VERIFICATION** — whether `CODEOWNERS` lists `docs/doctrine/` explicitly with the right reviewers.
- **NEEDS VERIFICATION** — whether any CI workflow currently fails a PR that violates a §16 path-validation
  checklist item, or whether the checklist is review-only at present.
- **OPEN** — whether **watcher-as-non-publisher** should be split into its own doctrine document or remain
  inside `trust-membrane.md`. (It is currently invoked in `directory-rules.md` §2.1 as a top-level invariant.)
- **OPEN** — whether `docs/doctrine/` should also host a single-page `INVARIANTS.md` that lists every
  KFM-wide MUST in one place, with backlinks to the document that authors each one.
- **OPEN** — whether the `docs/registers/AUTHORITY_LADDER.md` register and the doctrinal `authority-ladder.md`
  should be merged, kept distinct (register = machine-friendly index; doctrine doc = prose), or generated
  one from the other.

[↑ Back to top](#docsdoctrine)

---

## Mini-glossary

Short, placement-relevant definitions. Full definitions live in the doctrine documents and `contracts/`.

<details>
<summary><b>Expand glossary</b> — invariant · authority root · compatibility root · lane · lifecycle · trust membrane · cite-or-abstain · watcher-as-non-publisher · ADR · drift</summary>

| Term | Short definition |
|---|---|
| **Invariant** | A KFM-wide MUST or MUST NOT that holds across every domain, app, and release. |
| **Authority root** | A repo-root folder that carries one of the §3 responsibilities (governs truth · contains deployable systems · stores lifecycle data · supports validation/runtime · genuinely cross-domain). |
| **Compatibility root** | A root that exists for legacy, mirror, deprecated, external-export, or transitional reasons. README must declare class. |
| **Lane** | A domain or topic segment *inside* a responsibility root (e.g. `data/processed/hydrology/`). Domains are lanes, never roots. |
| **Lifecycle invariant** | RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED. Promotion is a governed state transition, not a file move. |
| **Trust membrane** | The boundary that prevents raw / unreviewed / model-generated / internal state from becoming public truth. Operational form: `apps/governed-api/`. |
| **Cite-or-abstain** | Every consequential claim either resolves an `EvidenceRef` to an `EvidenceBundle` or returns ABSTAIN / DENY / ERROR. Fluent text never substitutes for evidence. |
| **Watcher-as-non-publisher** | Workers and watchers emit receipts and candidate decisions only. They do not publish, mutate canonical records, or bypass review. |
| **ADR** | Architecture Decision Record. The only mechanism that may amend doctrine. Statuses: proposed · accepted · superseded · rejected. |
| **Drift** | A divergence between doctrine, repo state, source authority, or runtime evidence. Logged in `docs/registers/DRIFT_REGISTER.md`; not promoted to authority. |

</details>

[↑ Back to top](#docsdoctrine)

---

## Last reviewed

`YYYY-MM-DD` · *placeholder — set on first merge; update on every substantive change to this folder.*
Older than 6 months → flag for review per [`directory-rules.md` §15](./directory-rules.md#15-required-readme-contract).

---

<sub>This file is a directory landing page. It does **not** itself encode doctrine — the documents it points to do.
If this README and a doctrine document conflict, the doctrine document wins; open a PR to fix this README.</sub>
