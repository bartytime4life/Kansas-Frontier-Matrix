# Kansas Frontier Matrix

> A governed, evidence-first, map-first, time-aware spatial knowledge system for Kansas and the surrounding frontier.

[![Status: doctrine CONFIRMED · implementation PROPOSED](https://img.shields.io/badge/status-doctrine_confirmed_·_implementation_proposed-blue)](docs/doctrine/)
[![Lifecycle: RAW→PUBLISHED](https://img.shields.io/badge/lifecycle-RAW→WORK%2FQUARANTINE→PROCESSED→CATALOG%2FTRIPLET→PUBLISHED-1f6feb)](docs/doctrine/lifecycle-law.md)
[![Truth posture: cite-or-abstain](https://img.shields.io/badge/truth_posture-cite--or--abstain-2da44e)](docs/doctrine/truth-posture.md)
[![Public path: governed API only](https://img.shields.io/badge/public_path-governed_API_only-8957e5)](docs/architecture/governed-api.md)
[![Build: TODO](https://img.shields.io/badge/build-TODO-lightgrey)](#status-and-maturity)
[![License: TODO](https://img.shields.io/badge/license-TODO-lightgrey)](LICENSE)
[![Docs last updated: 2026-05-11](https://img.shields.io/badge/docs_updated-2026--05--11-informational)](#last-updated)

> [!NOTE]
> **Status & posture.** KFM doctrine, invariants, and governance contracts are **CONFIRMED** in attached project sources. **Implementation maturity is PROPOSED / NEEDS VERIFICATION** in this session: the repository was not mounted while drafting, so all per-path, per-route, per-test, and per-workflow claims below must be verified against actual repo state before treated as fact. Badge targets shown as `TODO` are placeholders awaiting first-pass verification.

| Field | Value |
|---|---|
| **Status** | doctrine CONFIRMED · implementation PROPOSED / NEEDS VERIFICATION |
| **Owners** | TODO — Repo steward · Docs steward · Subsystem owners (per `CODEOWNERS`) |
| **Last reviewed** | 2026-05-11 |
| **Authoritative placement rules** | [`docs/doctrine/directory-rules.md`](docs/doctrine/directory-rules.md) |
| **Lifecycle invariant** | RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED |
| **Truth posture** | Cite-or-abstain. EvidenceRef must resolve to EvidenceBundle before consequential claims. |
| **Public path** | Standard clients consume **governed APIs and released artifacts only.** No public access to RAW / WORK / QUARANTINE / candidate / internal stores / model runtimes. |

---

## Quick jump

- [What KFM is](#what-kfm-is)
- [Why it works this way](#why-it-works-this-way)
- [Core invariants](#core-invariants)
- [Repository layout](#repository-layout)
- [How a claim travels through KFM](#how-a-claim-travels-through-kfm)
- [Truth labels you'll see in this repo](#truth-labels-youll-see-in-this-repo)
- [Domains](#domains)
- [Public surfaces](#public-surfaces)
- [Getting oriented (no install yet)](#getting-oriented-no-install-yet)
- [Quickstart (when the repo is mounted)](#quickstart-when-the-repo-is-mounted)
- [Contributing](#contributing)
- [Status and maturity](#status-and-maturity)
- [FAQ](#faq)
- [Related docs](#related-docs)
- [Appendix: glossary](#appendix-glossary)

---

## What KFM is

The **Kansas Frontier Matrix (KFM)** is a governed spatiotemporal knowledge system whose outputs are designed to be **useful, inspectable, policy-conscious, traceable, correctable, and improvable.** Every consequential surface — a map popup, a public API answer, a Focus Mode response, a catalog entry, a release-supporting claim — is expected to resolve to admissible evidence, to carry visible governance state, and to be reversible if it turns out wrong.

KFM is **not**:

- not a generic GIS portal,
- not a model-of-the-week chatbot,
- not an emergency-alerting authority,
- not a flat data dump dressed up as a map.

KFM **is**:

- a **map-first** explorer whose renderer is a presentation surface, never a truth source;
- a **time-aware** evidence graph that distinguishes valid time, observed time, source/retrieval time, and release time;
- a **governed AI** runtime where generated language is interpretive and subordinate to resolved evidence;
- a **publication discipline** in which release, correction, and rollback are explicit, auditable acts.

CONFIRMED doctrine throughout the attached corpus.

---

## Why it works this way

Three commitments shape every other rule in the system.

1. **Evidence outranks fluent prose.** A claim that cannot resolve `EvidenceRef → EvidenceBundle` abstains — it does not improvise. This applies to API answers, Focus Mode replies, map popups, public layer explanations, catalog entries, and release-supporting claims.
2. **The public path is governed.** Public clients and ordinary UI surfaces consume only governed APIs, released artifacts, catalog records, tile services, EvidenceBundles, release manifests, and safe envelopes. **RAW / WORK / QUARANTINE / candidate / direct internal-store / direct model-runtime access is denied by default.**
3. **Promotion is a state transition, not a file move.** Material moves up the lifecycle only when validation, policy, citation closure, release manifest, review state, correction path, and rollback target are all in place.

> [!IMPORTANT]
> If a map, a tile, a graph index, a generated answer, or a polished report ever appears to be the **source** of truth rather than a **carrier** of resolved evidence, that is a bug in the trust membrane, not a feature.

---

## Core invariants

The system holds these invariants by default. A change that bends one requires an explicit tradeoff and (where §2.4 of Directory Rules applies) an ADR.

| # | Invariant | Operational meaning |
|---|---|---|
| 1 | **Lifecycle law** | `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a **governed state transition**, not a file move. |
| 2 | **Public path governance** | Public surfaces use governed interfaces; canonical/internal stores are not directly readable from the browser. |
| 3 | **Cite-or-abstain** | EvidenceRef must resolve to EvidenceBundle before claims; otherwise the surface returns `ABSTAIN`. |
| 4 | **Policy-aware fail-safe defaults** | Sensitive lanes (rare species, archaeology, infrastructure, living-person, DNA, exact location) **default to DENY** unless rights, sensitivity, validation, and review explicitly allow. |
| 5 | **Deterministic identity** | Object identity is stable across time and representations; mistaken identity is treated as data corruption. |
| 6 | **Governed promotion** | Validation, policy decision, proof or citation closure, release manifest, review state, correction path, rollback target, and receipt trail are all required. |
| 7 | **Auditable governance trail** | Provenance, receipts, reviews, corrections, and rollback targets remain inspectable after the fact. |
| 8 | **AI is interpretive, not sovereign** | Generated text never substitutes for evidence, policy, review state, source authority, or release state. |
| 9 | **Separation of duties** | Policy-significant release duties are separated from authoring when materiality justifies it. |

Primary doctrine: [`docs/doctrine/lifecycle-law.md`](docs/doctrine/lifecycle-law.md), [`docs/doctrine/trust-membrane.md`](docs/doctrine/trust-membrane.md), [`docs/doctrine/truth-posture.md`](docs/doctrine/truth-posture.md), [`docs/doctrine/authority-ladder.md`](docs/doctrine/authority-ladder.md). All paths PROPOSED until mounted-repo inspection confirms.

---

## Repository layout

KFM uses **responsibility roots**, not topic roots. A file's location encodes who owns it, what governance it answers to, and what lifecycle it belongs to. Domains live as **lanes inside responsibility roots**, never as new top-level folders.

```text
Kansas-Frontier-Matrix/
├── README.md                    # this file
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── CODEOWNERS                   # may live in .github/CODEOWNERS instead
├── .github/                     # workflows, issue/PR templates, governance hooks
├── docs/                        # human-facing control plane (doctrine, ADRs, architecture, runbooks)
├── control_plane/               # machine-readable governance maps & registers
├── contracts/                   # object-family MEANING (what an object is)
├── schemas/                     # machine-checkable SHAPE (default: schemas/contracts/v1/<…>)
├── policy/                      # admissibility, sensitivity, release policy (allow / deny / restrict / abstain)
├── tests/                       # enforceability proof
├── fixtures/                    # golden / valid / invalid test inputs
├── tools/                       # repo-wide validators, generators, builders
├── scripts/                     # small operational helpers
├── apps/                        # deployable applications (governed-api, explorer-web)
├── packages/                    # shared libraries (ui, maplibre, evidence-resolver, …)
├── connectors/                  # source-specific fetchers / admitters
├── pipelines/                   # executable pipeline logic
├── pipeline_specs/              # declarative pipeline configuration
├── data/                        # lifecycle data and emitted proof
│   ├── raw/  work/  quarantine/  processed/  catalog/  triplets/
│   ├── receipts/  proofs/  published/  registry/  rollback/
├── release/                     # release decisions, manifests, rollback cards, correction notices
├── runtime/                     # local runtime adapters / harnesses
├── infra/                       # deployment, host, network, exposure posture
├── configs/                     # non-secret config defaults / templates
├── migrations/                  # database / schema / graph migrations
├── examples/                    # worked, runnable examples
└── artifacts/                   # OPTIONAL compatibility; build / docs / qa scratch only
```

> [!WARNING]
> **Status of this tree:** the **rules** that produce it are CONFIRMED in `docs/doctrine/directory-rules.md`. The **presence** of any specific root in the live repo is **PROPOSED until verified** against mounted-repo evidence (see [Directory Rules §0](docs/doctrine/directory-rules.md) and §5). Domain folders at repo root (e.g., `hydrology/`, `soil/`, `fauna/`) are **anti-patterns** — domains belong as lanes under responsibility roots.

### Where things go (quick map)

| If the file's primary responsibility is… | …it belongs under |
|---|---|
| Explains something to humans | `docs/` |
| Indexes "what governs what" (machine-readable) | `control_plane/` |
| Defines an object's **meaning** | `contracts/` |
| Defines an object's **machine shape** | `schemas/` |
| Decides allow / deny / restrict / abstain | `policy/` |
| Proves a rule is enforceable | `tests/` |
| Golden / valid / invalid sample data for tests | `fixtures/` |
| Repo-wide validator, generator, builder, checker | `tools/` |
| Deployable application | `apps/` |
| Shared library used by multiple deployables | `packages/` |
| Source-specific fetcher / admitter | `connectors/` |
| Executable pipeline logic | `pipelines/` |
| Declarative pipeline configuration | `pipeline_specs/` |
| Lifecycle data (raw, work, processed, catalog, triplets, published, …) | `data/` |
| Release decision, manifest, rollback card, correction notice | `release/` |
| Local runtime adapter / harness | `runtime/` |
| Deployment, host, network, exposure posture | `infra/` |
| Non-secret config defaults / templates | `configs/` |
| Database / schema / graph migration | `migrations/` |
| Worked, runnable example | `examples/` |

Source: [`docs/doctrine/directory-rules.md`](docs/doctrine/directory-rules.md) §4. PROPOSED for this repo until verified.

---

## How a claim travels through KFM

A simplified picture of the lifecycle and the trust membrane. Heavy detail lives in [`docs/architecture/`](docs/architecture/).

```mermaid
flowchart LR
    subgraph Intake["pre-RAW intake (admission edge)"]
        EV["event_envelope"]
        PF["prefilter_output"]
    end

    subgraph Internal["Internal lifecycle (not public-readable)"]
        RAW["RAW<br/>admitted source<br/>under source identity"]
        WORK["WORK"]
        QUAR["QUARANTINE<br/>rights / sensitivity /<br/>validation / source-role /<br/>temporal / evidence defects"]
        PROC["PROCESSED<br/>normalized + validated"]
        CAT["CATALOG / TRIPLET<br/>EvidenceBundle,<br/>graph projections,<br/>release candidates"]
    end

    subgraph Public["Public surface (governed)"]
        PUB["PUBLISHED<br/>ReleaseManifest +<br/>rollback target +<br/>correction path"]
        API["Governed API<br/>ANSWER / ABSTAIN /<br/>DENY / ERROR"]
        UI["MapLibre shell ·<br/>Evidence Drawer ·<br/>Focus Mode"]
    end

    EV --> PF --> RAW
    RAW --> WORK
    WORK -- defects --> QUAR
    WORK --> PROC
    PROC --> CAT
    CAT -- release decision --> PUB
    PUB --> API --> UI

    classDef internal fill:#fef3c7,stroke:#b45309,color:#78350f
    classDef public fill:#dcfce7,stroke:#15803d,color:#14532d
    classDef intake fill:#e0e7ff,stroke:#4338ca,color:#312e81
    class RAW,WORK,QUAR,PROC,CAT internal
    class PUB,API,UI public
    class EV,PF intake
```

**Reading the diagram.** Public clients only touch the green band on the right. Promotion across each arrow is a **governed transition** that requires the artifacts named in the lifecycle invariant — not a file move. The pre-RAW intake (`event_envelope`, `prefilter_output`, `event_run_receipt`) records attempted intake **before** material is admitted into RAW, so watchers, GitOps emission, and live feeds never blur the boundary between observed input and accepted source.

---

## Truth labels you'll see in this repo

KFM docs make confidence visible. Expect these labels in design notes, ADRs, idea cards, and READMEs:

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified in this session from attached docs, workspace evidence, tests, logs, or generated artifacts. |
| **INFERRED** | Reasonably derivable from visible evidence but not directly stated. |
| **PROPOSED** | Design, recommendation, file path, placement, or inference not yet verified in implementation. |
| **UNKNOWN** | Not resolvable without more evidence. |
| **NEEDS VERIFICATION** | Checkable, but not yet checked strongly enough to act as fact. |

> [!TIP]
> Memory is not evidence. Recollection, guessed paths, likely behavior, and generic best practice are not facts. If a section says "the repo contains X" without supporting evidence, treat it as PROPOSED until verified.

---

## Domains

KFM is organized as **domain lanes**, each with object families, source families, viewing modes, sensitivity defaults, and per-domain dossiers. Domains live **under responsibility roots**, never as root-level folders.

| Domain | Status (CONFIRMED doctrine / PROPOSED implementation) | Sensitivity default highlights |
|---|---|---|
| Spatial Foundation | doctrine / PROPOSED | T0 base layers; sensitive geometry fails closed |
| Hydrology | doctrine / PROPOSED | T0; first proof-bearing thin-slice candidate |
| Soil | doctrine / PROPOSED | T0 |
| Habitat | doctrine / PROPOSED | T0 mostly; T1 for stewardship zones |
| Fauna | doctrine / PROPOSED | **T4 default** for sensitive occurrences; T1 generalized |
| Flora | dossier / PROPOSED | **T4 default** for rare-plant records |
| Agriculture | dossier / PROPOSED | T0 aggregate · T1 field candidate · private-join DENY |
| Geology / Natural Resources | doctrine / PROPOSED | T0 unit · T2 sensitive detail |
| Atmosphere / Air | doctrine / PROPOSED | T0; source-role anti-collapse is acute |
| Hazards | doctrine / PROPOSED | T0 historical/context. **KFM is never an alert authority.** |
| Roads / Rail / Trade | doctrine / PROPOSED | T0 mostly; T2 / T4 for sensitive condition detail |
| Settlements / Infrastructure | doctrine / PROPOSED | **Critical-asset DENY lane** |
| Archaeology / Cultural Heritage | doctrine / PROPOSED | **T4 default**; sovereignty review path |
| People / Genealogy / DNA / Land | doctrine / PROPOSED | **Living-person, DNA, person-parcel DENY-default** |
| Frontier Matrix | doctrine / PROPOSED | County-year panels, threshold models, crosswalks |
| Planetary / 3D | doctrine / PROPOSED | 3D admission gate; Reality Boundary Note required |

Sensitivity tiers are CONFIRMED doctrine; specific tier assignments per source are PROPOSED until each lane's policy review records them. Per-domain dossiers live under `docs/domains/<domain>/` (PROPOSED).

---

## Public surfaces

What the **public** interacts with — and what they pointedly **do not**.

| Surface | What it is | Finite outcomes | What it **never** does |
|---|---|---|---|
| **MapLibre shell** | 2D presentation surface for released layers | (renders or shows abstain/deny state) | Read RAW / WORK / QUARANTINE / canonical stores / model runtimes |
| **Evidence Drawer** | Governed projection of `EvidenceBundle`, citations, policy/review/release/stale/correction state | `ANSWER / ABSTAIN / DENY / ERROR` | Display unsupported claims |
| **Focus Mode** (governed AI) | Evidence-bounded request/response | `ANSWER / ABSTAIN / DENY / ERROR` | Return uncited language; bypass `AIReceipt`; act as the truth source |
| **Governed API** | The only browser network path for trust payloads | `ANSWER / ABSTAIN / DENY / ERROR` | Expose internal store identifiers; serve unreleased candidates |
| **Story Nodes** | Evidence-backed narrative units linked to features, time, and sources | `ANSWER / ABSTAIN / DENY / ERROR` | Substitute synthesis for citation |
| **Exports / Reports** | Public artifacts carrying rights, sensitivity, and citation receipts | `ALLOWED / DENY / ERROR` | Carry unredacted sensitive content |
| **Correction submit** | Public-facing correction path | `ACCEPTED / DENY / ERROR` | Erase history; bypass review |
| **Review console** | Read-only steward proof/review queue surface | (queue state) | Provide author self-approval on policy-significant releases |

All surfaces are **CONFIRMED doctrine / PROPOSED implementation** in the supplied corpus. Routes, DTOs, and runtime behavior are **UNKNOWN** until repository inspection.

---

## Getting oriented (no install yet)

If you're new to KFM and the repo isn't checked out, read in this order. Each link is **PROPOSED** until verified against the mounted repo.

1. **Doctrine first.** [`docs/doctrine/directory-rules.md`](docs/doctrine/directory-rules.md), then [`docs/doctrine/lifecycle-law.md`](docs/doctrine/lifecycle-law.md), [`docs/doctrine/trust-membrane.md`](docs/doctrine/trust-membrane.md), [`docs/doctrine/truth-posture.md`](docs/doctrine/truth-posture.md), [`docs/doctrine/authority-ladder.md`](docs/doctrine/authority-ladder.md).
2. **Architecture.** [`docs/architecture/system-context.md`](docs/architecture/system-context.md), [`docs/architecture/governed-api.md`](docs/architecture/governed-api.md), [`docs/architecture/map-shell.md`](docs/architecture/map-shell.md), [`docs/architecture/contract-schema-policy-split.md`](docs/architecture/contract-schema-policy-split.md).
3. **Registers.** [`docs/registers/AUTHORITY_LADDER.md`](docs/registers/AUTHORITY_LADDER.md), [`CANONICAL_LINEAGE_EXPLORATORY.md`](docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md), [`DRIFT_REGISTER.md`](docs/registers/DRIFT_REGISTER.md), [`VERIFICATION_BACKLOG.md`](docs/registers/VERIFICATION_BACKLOG.md).
4. **ADRs.** [`docs/adr/`](docs/adr/) — start with `ADR-0001-schema-home.md`.
5. **Domains.** [`docs/domains/<domain>/`](docs/domains/) — pick the lane you care about.

---

## Quickstart (when the repo is mounted)

> [!NOTE]
> **Illustrative — not a verified pipeline.** The package manager, app entry points, and validator commands are PROPOSED until the actual repo is inspected. Treat this block as a placeholder for the eventual `runbooks/`-backed flow.

```bash
# 1) Clone (PROPOSED URL)
git clone https://github.com/<org>/Kansas-Frontier-Matrix.git
cd Kansas-Frontier-Matrix

# 2) Doctrine pre-flight: read the rules that govern placement
cat docs/doctrine/directory-rules.md

# 3) Install dependencies (PROPOSED — package manager NEEDS VERIFICATION)
# e.g. one of:  pnpm install   |   npm install   |   yarn install

# 4) Validate schemas, fixtures, and policy (PROPOSED command surfaces)
# e.g.:        pnpm run validate:schemas
#              pnpm run validate:fixtures
#              pnpm run policy:test

# 5) Run the governed API locally (PROPOSED path)
# e.g.:        pnpm --filter @kfm/governed-api dev

# 6) Run the explorer web client (PROPOSED path)
# e.g.:        pnpm --filter @kfm/explorer-web dev
```

If your command surface differs from the above, the **mounted repo is the truth source** — update `docs/runbooks/` (and this section) rather than retrofitting reality to the placeholders.

---

## Contributing

KFM treats placement, evidence, and release as governance, not paperwork. Before opening a PR:

- [ ] **Read** [`docs/doctrine/directory-rules.md`](docs/doctrine/directory-rules.md). Use the §4 Placement Protocol to choose a path.
- [ ] **Cite the rule** in your PR description that justifies any new, moved, or renamed path.
- [ ] **Truth-label** uncertain claims (`CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`) rather than smoothing them away.
- [ ] **No parallel authority.** Do not create a sibling home for schemas, contracts, policy, sources, registries, releases, proofs, or receipts without an ADR (Directory Rules §2.4).
- [ ] **Trust content placement.** Receipts, proofs, manifests, and release decisions live in `data/receipts/`, `data/proofs/`, or `release/` — **never** in `artifacts/`.
- [ ] **Public path discipline.** A new route goes through `apps/governed-api/`, not directly to canonical stores.
- [ ] **README contract.** Affected folders carry a README that meets [Directory Rules §15](docs/doctrine/directory-rules.md).
- [ ] **Tests, fixtures, policy, runbook** updates accompany behavioral change. Docs are part of the working system — but they do **not** substitute for validation.
- [ ] **Rollback path** is named for any release-affecting change.

Full contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md) (PROPOSED — verify presence and content).

Security disclosures and exposure-posture concerns: [`SECURITY.md`](SECURITY.md) (PROPOSED — verify presence and content).

---

## Status and maturity

> [!CAUTION]
> **Implementation maturity is bounded by what the mounted repository proves.** The attached corpus is CONFIRMED **doctrine** with PROPOSED implementation patterns. Without a mounted repo, routes, DTOs, branch protections, CI workflows, emitted receipts, deployment posture, and runtime behavior remain **UNKNOWN**. Do not infer maturity from the polish of this document.

| Area | Doctrine | Implementation evidence (this session) |
|---|---|---|
| Lifecycle law | CONFIRMED | UNKNOWN — no mounted repo proof |
| Trust membrane (public clients use governed APIs only) | CONFIRMED | UNKNOWN — route names, branch state, CI proof not verified |
| Cite-or-abstain | CONFIRMED | UNKNOWN — runtime/citation-validator state not verified |
| Sensitivity tiers (T0–T4) | CONFIRMED scheme | PROPOSED per-source assignments |
| Governed AI finite outcomes (`ANSWER / ABSTAIN / DENY / ERROR`) | CONFIRMED | UNKNOWN — adapter/runtime not verified |
| Directory Rules canonical roots | CONFIRMED | PROPOSED presence in live repo |
| ADR discipline | CONFIRMED | UNKNOWN — `docs/adr/` contents not verified |
| Domain dossiers | CONFIRMED doctrine per domain | PROPOSED implementation per domain |

The current-session evidence limit applies: doctrine speaks confidently because attached sources support it; implementation claims are bounded until the repo can be inspected.

---

## FAQ

<details>
<summary><strong>Why isn't this just a regular GIS portal?</strong></summary>

Because the public surface needs to **earn** every claim, and a generic GIS portal is built around layers, not around evidence, policy, review state, release state, and correction lineage. KFM treats those as first-class objects you can inspect, not as metadata the user is expected to take on faith.
</details>

<details>
<summary><strong>Why isn't the AI just answering questions directly?</strong></summary>

Because fluent generation isn't evidence. Focus Mode answers only what `EvidenceBundle` resolution and policy permit. If the evidence is missing, ambiguous, or restricted, the surface returns `ABSTAIN` or `DENY` — with a reason — rather than improvising. Every governed AI exchange emits an `AIReceipt` that records the provider/model adapter, the evidence references, the citation validation result, and the policy decision, without exposing private chain-of-thought.
</details>

<details>
<summary><strong>Why does the directory structure look so strict?</strong></summary>

Because **where a file lives encodes who owns it, what governance it answers to, and what lifecycle phase it belongs to**. A repo whose root drifts into topic folders, parallel schema homes, and "convenience" buckets loses its ability to enforce trust at the boundary. KFM keeps the root **boring**, with stable responsibility roots, and pushes domain depth into lanes. Directory Rules §3 and §13 catalog the anti-patterns that this prevents.
</details>

<details>
<summary><strong>What does "PROPOSED" mean in the docs?</strong></summary>

It means the design, path, placement, or recommendation is sound on paper but **not yet verified in implementation**. PROPOSED is not weak — it's honest. The repo's job is to move PROPOSED items to CONFIRMED through actual files, schemas, tests, and workflows, not through documentation polish.
</details>

<details>
<summary><strong>Can KFM be used as a hazard alert or emergency authority?</strong></summary>

**No.** KFM hazard surfaces are historical, regulatory, and contextual. They carry non-emergency disclaimers and policy DENY for life-safety guidance. Use authoritative emergency services for alerts.
</details>

<details>
<summary><strong>Where do living-person, DNA, exact archaeology, or sensitive infrastructure locations live?</strong></summary>

In **deny-by-default** lanes. Public-safe derivatives only appear after rights, sovereignty, sensitivity, validation, review, and release have all been resolved, often via redaction, generalization, or staged access. Unclear cases prefer quarantine, denial, or delay.
</details>

---

## Related docs

> [!NOTE]
> Links below resolve once the doctrinal and architecture trees are in place. They are **PROPOSED paths**, consistent with Directory Rules §5–§7. Verify against mounted-repo state before treating as canonical.

- **Doctrine** — [`docs/doctrine/`](docs/doctrine/) (directory-rules · lifecycle-law · trust-membrane · truth-posture · authority-ladder)
- **Architecture** — [`docs/architecture/`](docs/architecture/) (system-context · governed-api · map-shell · contract-schema-policy-split)
- **ADRs** — [`docs/adr/`](docs/adr/) (start with `ADR-0001-schema-home.md`)
- **Registers** — [`docs/registers/`](docs/registers/) (`AUTHORITY_LADDER`, `CANONICAL_LINEAGE_EXPLORATORY`, `DRIFT_REGISTER`, `VERIFICATION_BACKLOG`, `OBJECT_FAMILY_MAP`)
- **Domains** — [`docs/domains/`](docs/domains/) (per-domain dossiers and lane plans)
- **Sources & standards** — [`docs/sources/`](docs/sources/), [`docs/standards/`](docs/standards/)
- **Runbooks** — [`docs/runbooks/`](docs/runbooks/) (`ui_LOCAL_DEV`, `ui_VALIDATION`, `ui_ROLLBACK`, `governed_ai_*`)
- **Contributing & security** — [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), [`CODEOWNERS`](CODEOWNERS)

[Back to top ↑](#kansas-frontier-matrix)

---

## Appendix: glossary

<details>
<summary><strong>Trust & evidence terms</strong></summary>

| Term | Definition |
|---|---|
| **Inspectable claim** | A public/semi-public statement reconstructable to evidence, scope, source role, policy posture, review state, release state, and correction lineage. |
| **EvidenceRef** | Pointer from a claim, feature, answer, layer, or proof item to evidence that must resolve before consequential release. |
| **EvidenceBundle** | Resolved evidence package supporting a claim, including source, scope, provenance, policy, citation, and review context. Outranks maps, tiles, and generated text. |
| **EvidenceDrawerPayload** | Governed UI projection of `EvidenceBundle`, citations, policy/review/release state, stale state, and correction links. |
| **SourceDescriptor** | Machine-readable source identity, source role, rights, cadence, access, steward, sensitivity, and release posture. |
| **PolicyDecision** | Explicit allow / deny / restrict / abstain / error decision tied to user, purpose, release class, evidence, and sensitivity. |
| **DecisionEnvelope / RuntimeResponseEnvelope** | Finite-outcome wrappers used by APIs, runtime surfaces, and UI/AI payloads to avoid ambiguous truth states. |
| **AIReceipt** | Runtime accountability record for bounded AI use; provider/model adapter, evidence refs, citation validation, policy result. Never a substitute for `EvidenceBundle`. |
| **CitationValidationReport** | Pass/fail citation closure object for Focus Mode, Story Nodes, popups, and exports. |
| **RunReceipt / PromotionReceipt** | Build/run receipts for pipeline or tile artifact generation; promotion-gate receipts for state transitions. |
| **ReleaseManifest** | The release-decision artifact (lives under `release/manifests/`). |
| **RollbackCard** | Rollback decision artifact (lives under `release/rollback_cards/`). |
| **CorrectionNotice** | Public notice of a corrected claim, listing invalidated derivatives. |
| **LayerManifest** | Released-layer descriptor; resolved by the layer manifest resolver under `apps/governed-api/`. |
| **MapContextEnvelope** | Bounded context carrying map camera, layer IDs, feature IDs, temporal snapshot, release refs, and selected evidence refs. |
| **Authority root / Compatibility root** | Responsibility-bearing canonical root vs. legacy/mirror/transitional root, per Directory Rules §5 / §8. |
| **Promotion** | Governed state transition between lifecycle phases. **Not a file move.** |
| **Trust membrane** | The boundary that prevents raw / unreviewed / model-generated / internal state from becoming public truth. Operational form: `apps/governed-api/`. |

</details>

<details>
<summary><strong>Finite outcome cheat-sheet</strong></summary>

| Outcome | When | Public effect |
|---|---|---|
| `ANSWER` | Evidence sufficient · policy permits · release state allows · review state recorded (if required) | Substantive answer with Evidence Drawer and citation |
| `ABSTAIN` | Evidence insufficient/incomplete · AI surface cannot cite · evidence stale and no released alternative | Non-substantive note with reason; **never invents** |
| `DENY` | Policy, rights, sensitivity, or release state forbids the answer (sensitive lanes default here) | Denial reason; offer alternative non-restricted surface where possible |
| `ERROR` | Governed API cannot evaluate — missing schema, malformed query, contract violation, infra failure | Finite, actionable error; **never silently falls through** to a different lane |
| `HOLD` | Promotion / release / correction paused pending steward, rights-holder, or policy review | Surface remains in prior state; no silent rollback or replacement |
| `PASS / FAIL` | Validator-class outcomes (not direct public answers) | Promotion gating; quarantine on FAIL |

</details>

<details>
<summary><strong>Sensitivity tiers (T0–T4)</strong></summary>

| Tier | Public posture (default) | Typical content |
|---|---|---|
| **T0** | Public-safe | Base layers, aggregate observations, historical/regulatory context |
| **T1** | Generalized public | Range polygons, stewardship zones, generalized footprints |
| **T2** | Restricted | Sensitive condition detail, sensitive resource detail |
| **T3** | Heavily restricted | Cross-lane joins requiring steward review |
| **T4** | **DENY default** | Exact sensitive coordinates, living-person fields, DNA, exact archaeology, critical-asset detail |

Tier upgrades (toward more public) require both a transform receipt **and** a review record. Tier downgrades (toward less public) need correction alone. CONFIRMED scheme; per-source tier assignments PROPOSED.

</details>

---

### Last updated

`2026-05-11` — initial polished draft authored from project doctrine (Directory Rules, KFM Encyclopedia, Domains Culmination Atlas v1.1, Unified Implementation Architecture Build Manual, Whole-UI + Governed AI Expansion Report, Master MapLibre Components Manual, Pass-18 Idea Index). Repository was not mounted during drafting; all repo-state claims are **PROPOSED / NEEDS VERIFICATION** until inspection.

[Back to top ↑](#kansas-frontier-matrix)
