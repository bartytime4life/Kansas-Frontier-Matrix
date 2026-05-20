<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/artifacts-docs-readme
title: artifacts/docs/ — Generated Documentation Outputs
type: readme
version: v0.1
status: draft
owners: TODO-docs-build-steward
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - artifacts/README.md
  - docs/
  - data/published/reports/
  - data/published/stories/
  - release/manifests/
  - data/proofs/
  - data/receipts/
tags: [kfm, artifacts, compatibility-root, generated, docs-build]
notes:
  - "Folder is a SUBFOLDER of the artifacts/ compatibility root, not its own root."
  - "Authored doctrine lives under docs/; this folder holds generated outputs only."
  - "Open Directory Rules question §18.a: whether artifacts/ is kept or retired."
[/KFM_META_BLOCK_V2] -->

# `artifacts/docs/`

> **Generated documentation outputs only — the rendered mkdocs site, API reference, and exported PDF builds. Authored doctrine lives under [`docs/`](../../docs/); released public-safe documents live under [`data/published/`](../../data/published/). This folder is a build product, never an authority surface.**

<p align="left">
  <a href="../../docs/doctrine/directory-rules.md"><img alt="Directory Rules v1.1" src="https://img.shields.io/badge/Directory_Rules-v1.1-1f6feb"></a>
  <a href="#-authority-and-status"><img alt="Authority: compatibility · transitional" src="https://img.shields.io/badge/Authority-compatibility%20%C2%B7%20transitional-bf8700"></a>
  <a href="#-authority-and-status"><img alt="Status: PROPOSED" src="https://img.shields.io/badge/Status-PROPOSED-bf8700"></a>
  <a href="#-what-belongs-here"><img alt="Trust content: forbidden" src="https://img.shields.io/badge/Trust_content-forbidden-cf222e"></a>
  <!-- TODO: CI badge once `docs-build` workflow is named and verified -->
  <a href="#"><img alt="docs-build: TODO" src="https://img.shields.io/badge/docs--build-TODO-lightgrey"></a>
  <!-- TODO: last-updated badge once shields endpoint is pointed at this file -->
  <a href="#"><img alt="last-updated: TODO" src="https://img.shields.io/badge/last--updated-TODO-lightgrey"></a>
</p>

| Field | Value |
|---|---|
| **Folder** | `artifacts/docs/` |
| **Parent root** | [`artifacts/`](../README.md) — **compatibility** root, optional, tightly scoped (Directory Rules §8.2). |
| **Authority level** | **Compatibility** · class **`transitional`** (default per Directory Rules §8.1). |
| **Status** | **PROPOSED** — folder *usage* is CONFIRMED doctrine; folder *presence* in the current repo is **NEEDS VERIFICATION**. |
| **Owners** | _TODO_ — docs-build steward. _(Placeholder; assign via `CODEOWNERS` before this README moves out of draft.)_ |
| **Last reviewed** | _TODO_ — set to ISO date when this README is first merged. |
| **Open question** | Directory Rules §18.a — **OPEN:** whether `artifacts/` is kept as compatibility or fully retired. See [§ Open questions](#-open-questions). |

---

## 📑 Contents

1. [Purpose](#-purpose)
2. [Repo fit](#-repo-fit)
3. [Authority and status](#-authority-and-status)
4. [What belongs here](#-what-belongs-here)
5. [What does **NOT** belong here](#-what-does-not-belong-here)
6. [Directory tree](#-directory-tree)
7. [Diagram — where this folder sits](#-diagram--where-this-folder-sits)
8. [Inputs](#-inputs)
9. [Outputs](#-outputs)
10. [Quickstart / usage](#-quickstart--usage)
11. [Validation](#-validation)
12. [Review burden](#-review-burden)
13. [Related folders](#-related-folders)
14. [ADRs](#-adrs)
15. [Open questions](#-open-questions)
16. [FAQ](#-faq)
17. [Appendix — § 8.2 substructure (verbatim)](#-appendix---82-substructure-verbatim)
18. [Footer](#-footer)

---

## 🎯 Purpose

`artifacts/docs/` holds **generated documentation outputs**: the rendered documentation site (e.g. mkdocs build), generated API references, and exported PDF builds of authored documents. It is a **build product**, not authored content.

> [!IMPORTANT]
> **The authored sources live elsewhere.** Authored doctrine, runbooks, ADRs, standards profiles, architecture pages, and domain dossiers are owned by [`docs/`](../../docs/) (canonical control plane). This folder only renders those sources into shipped formats.

The folder exists because the KFM corpus treats documentation as a build artifact subject to the same evidence-first discipline as data products — pinned toolchains, deterministic inputs, content-addressed outputs (`ARTIFACT_DIGEST`). See [Pass-10 §6.13 Reproducible Documentation and Build Artifacts](../../docs/doctrine/directory-rules.md) (CONFIRMED doctrine; cards `C13-01` … `C13-04`).

[Back to top ↑](#contents)

---

## 🧭 Repo fit

```
<repo root>/
├── artifacts/               # compatibility root (Directory Rules §8.2)
│   ├── README.md            # declares class; forbids trust content
│   ├── build/               # compiled outputs, distributables
│   ├── docs/   ⬅ THIS FOLDER
│   ├── qa/                  # QA reports, lint output, test coverage
│   └── temporary/           # ephemeral; gitignored or pruned
└── …
```

- **Upstream (authoritative sources):** [`docs/`](../../docs/), [`schemas/`](../../schemas/) (when an API ref is generated from schemas), in-repo source comments.
- **Sibling (parent README):** [`artifacts/README.md`](../README.md) — declares the parent root's class and the cross-cutting "what does NOT belong" list.
- **Downstream (consumers):** local previewers, CI publish steps, documentation hosting, [`release/`](../../release/) decisions that *cite* a built doc by its `ARTIFACT_DIGEST` (citations live in `release/`, not here).

[Back to top ↑](#contents)

---

## 🪪 Authority and status

| Question | Answer | Truth label |
|---|---|---|
| Is `artifacts/` a canonical root? | **No.** It is a **compatibility** root. | CONFIRMED — Directory Rules §5, §8. |
| Is `artifacts/` optional? | **Yes.** It MAY exist; if it exists, it MUST be tightly scoped. | CONFIRMED — Directory Rules §8.2. |
| What is the default compatibility class for `artifacts/`? | `transitional` | CONFIRMED — Directory Rules §8.1. |
| Is `artifacts/docs/` named in doctrine? | **Yes** — as the subfolder for "generated documentation (mkdocs site, API ref)". | CONFIRMED — Directory Rules §8.2 substructure. |
| Does this folder exist in the current mounted repo? | Unknown in this session. | **NEEDS VERIFICATION** — no mounted-repo inspection. |
| Can this folder hold receipts, proofs, or release manifests? | **No.** Doing so is an explicit anti-pattern. | CONFIRMED — Directory Rules §13.2 and §13.5 ("Trust content in `artifacts/`"). |

> [!NOTE]
> The §8.2 substructure is **recommended**, not invented here. It is reproduced verbatim in the [appendix](#-appendix---82-substructure-verbatim) so any drift between this README and the governing document is reviewable at a glance.

[Back to top ↑](#contents)

---

## ✅ What belongs here

The accepted contents are **regenerable, build-time outputs** of documentation tooling. Concretely:

- **Rendered documentation site** — the static-site build of [`docs/`](../../docs/) (e.g. mkdocs site output, HTML tree, search index, asset bundle). _PROPOSED tool_: mkdocs; specific tool **NEEDS VERIFICATION** until repo inspection.
- **Generated API references** — auto-generated reference output (e.g. schema-derived, code-derived, OpenAPI-derived). Treat the rendered output as build product; the **source of truth** is the schema/contract/code under [`schemas/`](../../schemas/), [`contracts/`](../../contracts/), and [`apps/`](../../apps/).
- **Exported PDF builds** — pinned-toolchain PDF renders of authored docs (Pandoc + XeLaTeX + Ghostscript + qpdf per Pass-10 `C13-01`; `SOURCE_DATE_EPOCH` per `C13-02`; PDF/UA preflight per `C13-03` _PROPOSED_; `ARTIFACT_DIGEST` per `C13-04`).
- **`ARTIFACT_DIGEST` sidecars** — for PDFs and other content-addressable rendered outputs, the SHA-256 sidecar manifest **may co-locate here** if it is purely the local build's verification anchor. See [§ FAQ](#-faq) for the rule about sidecars that *cross* into release citation.

> [!TIP]
> If the rendered output is what a consumer downloads or links to as a citable public artifact, it does **not** belong here — it belongs under [`data/published/reports/`](../../data/published/) or [`data/published/stories/`](../../data/published/) per Directory Rules §9.1, and its release decision lives in [`release/`](../../release/). `artifacts/docs/` is the *intermediate* build product.

[Back to top ↑](#contents)

---

## 🚫 What does **NOT** belong here

The following are **explicit anti-patterns** for `artifacts/` (and therefore for `artifacts/docs/`). All are CONFIRMED doctrine per Directory Rules §8.2, §13.2, and §13.5.

| ❌ Do NOT place here | ✔ Correct home | Why |
|---|---|---|
| **Authored** documentation (doctrine, ADRs, runbooks, standards, architecture pages, domain dossiers, encyclopedia, atlases) | [`docs/`](../../docs/) | Authored docs are the **canonical control plane**, not a build product. |
| **Released, public-safe documents** that consumers link to as citable artifacts | [`data/published/reports/`](../../data/published/), [`data/published/stories/`](../../data/published/) | Released artifacts are governed outputs; they sit on the lifecycle invariant, not in compatibility. |
| **Release decisions, release manifests** | [`release/manifests/`](../../release/) | Release is a governed state transition (Directory Rules §9). |
| **Rollback cards, correction notices** | [`release/rollback_cards/`](../../release/), [`release/correction_notices/`](../../release/) | Decisions live in `release/`. |
| **Receipts** (`RunReceipt`, `AIReceipt`, `GENERATED_RECEIPT.json`, validation reports, citation validation reports) | [`data/receipts/`](../../data/receipts/) | Receipts are trust-bearing process memory. |
| **Proofs** (`EvidenceBundle`, proof packs, validation reports) | [`data/proofs/`](../../data/proofs/) | Proofs are evidence, not build output. |
| **Evidence bundles cited by claims** | [`data/proofs/evidence_bundle/`](../../data/proofs/) | `EvidenceRef` resolves to `EvidenceBundle`, never to `artifacts/`. |
| **Signed attestations, sidecars used as release citation anchors** | Alongside the released artifact under [`data/published/`](../../data/published/) and referenced from [`release/manifests/`](../../release/) | If a sidecar is cited from release, the citation must point at the release lane, not at `artifacts/`. |
| **Catalog records** (STAC, DCAT, PROV) | [`data/catalog/`](../../data/catalog/) | Catalog is governed lifecycle output. |
| **Published map layers, tiles, PMTiles, GeoParquet** | [`data/published/layers/`](../../data/published/), [`data/published/pmtiles/`](../../data/published/), [`data/published/geoparquet/`](../../data/published/) | Public-safe artifacts have their own lifecycle home. |
| **Secrets, credentials, API tokens** | Not in the repo at all (`configs/` holds non-secret templates only — Directory Rules §5). | Repo posture is deny-by-default; secrets never land here. |

> [!WARNING]
> Trust content placed in `artifacts/` is named as an anti-pattern in **two** places in Directory Rules — §13.2 ("Trust content in `artifacts/`") and §13.5 row "Trust content in `artifacts/`". Migrate per §8.2 if discovered; add a `DRIFT_REGISTER` entry.

[Back to top ↑](#contents)

---

## 🌲 Directory tree

> **PROPOSED.** Subfolder layout below follows the principle that build outputs are organized by *what tool produced them* and *what they render*, not by topic. Specific subfolder names below are PROPOSED until either an authoring-session convention or a mounted-repo inspection confirms them.

```text
artifacts/docs/
├── README.md                 # THIS FILE
├── site/                     # PROPOSED — rendered static-site build (e.g. mkdocs)
│   └── …                     # HTML tree, search index, assets — regenerable
├── api/                      # PROPOSED — generated API references
│   └── …                     # schema/code-derived reference — regenerable
├── pdf/                      # PROPOSED — exported PDF builds
│   ├── <doc-id>/
│   │   ├── <doc-id>.pdf      # linearized PDF/A-2u (Pass-10 C13-01..04)
│   │   └── <doc-id>.sha256   # ARTIFACT_DIGEST sidecar (local build anchor only)
│   └── …
└── _tmp/                     # PROPOSED — local-only scratch; gitignored
```

> [!NOTE]
> The PDF subfolder layout is **PROPOSED**. The Pass-10 `C13-04` sidecar pattern is **CONFIRMED doctrine**; whether the sidecar physically lives at `artifacts/docs/pdf/<doc-id>/<doc-id>.sha256` or beside the released copy under `data/published/reports/<doc-id>/` is **NEEDS VERIFICATION**. If a sidecar is *cited from release*, the citation MUST point at the `data/published/` copy (see [§ FAQ — sidecar duplication](#-faq)).

[Back to top ↑](#contents)

---

## 🧩 Diagram — where this folder sits

```mermaid
flowchart LR
  subgraph AUTH["Authoritative (canonical roots)"]
    DOCS["docs/<br/>authored doctrine, ADRs,<br/>runbooks, standards"]
    SCH["schemas/ · contracts/<br/>shape & meaning"]
    DATAPUB["data/published/<br/>reports/ · stories/<br/>(released, public-safe)"]
    REL["release/<br/>manifests, rollback cards,<br/>correction notices"]
    PROOF["data/proofs/ · data/receipts/<br/>evidence bundles, run receipts"]
  end

  subgraph COMP["Compatibility (Directory Rules §8)"]
    ARTROOT["artifacts/<br/>(transitional)"]
    THIS["artifacts/docs/<br/>generated outputs<br/>⬅ THIS FOLDER"]
    BUILD["artifacts/build/"]
    QA["artifacts/qa/"]
    TMP["artifacts/temporary/"]
  end

  DOCS -- "rendered by docs-build" --> THIS
  SCH -- "rendered as API ref" --> THIS
  THIS -. "regenerable; not authoritative" .-> THIS
  THIS -. "promotion (governed)" .-> DATAPUB
  DATAPUB -- "cited by" --> REL
  PROOF -. "never lands in" .x ARTROOT

  ARTROOT --> THIS
  ARTROOT --> BUILD
  ARTROOT --> QA
  ARTROOT --> TMP

  classDef auth fill:#1f6feb,stroke:#0a2e6b,color:#fff;
  classDef comp fill:#bf8700,stroke:#5c4400,color:#fff;
  classDef this fill:#2da44e,stroke:#0e4429,color:#fff;
  classDef forbid fill:#cf222e,stroke:#82071e,color:#fff;
  class DOCS,SCH,DATAPUB,REL auth;
  class ARTROOT,BUILD,QA,TMP comp;
  class THIS this;
  class PROOF auth;
```

> [!NOTE]
> Arrows are **flow of content**, not authority. The crossed-out arrow (`-.x`) marks the forbidden direction: trust-bearing proofs and receipts **never** flow into `artifacts/`. Promotion from `artifacts/docs/` into `data/published/` is a **governed state transition**, not a file copy.

[Back to top ↑](#contents)

---

## 🔌 Inputs

| Input | Source | Notes |
|---|---|---|
| Authored Markdown / source files | [`docs/`](../../docs/) | Authoritative; never edited from this folder. |
| Schemas, contracts, code | [`schemas/`](../../schemas/), [`contracts/`](../../contracts/), [`apps/`](../../apps/), [`packages/`](../../packages/) | Source-of-truth for generated API references. |
| Build tooling | [`tools/`](../../tools/) — _PROPOSED_: docs build orchestrator (specific path NEEDS VERIFICATION) | Pinned per `tool-versions.yaml` (Pass-10 `C13-01`). |
| Deterministic inputs | `SOURCE_DATE_EPOCH` (git commit time); embedded fonts (Noto family); `LC_ALL=C.UTF-8` | Pass-10 `C13-02`. PROPOSED implementation. |
| CI workflows | `.github/workflows/<docs-build>.yml` — _name and path **NEEDS VERIFICATION**_ | Workflow MUST call the canonical build entry point, not an ad-hoc command. |

[Back to top ↑](#contents)

---

## 📤 Outputs

| Output | Form | Where it goes after promotion |
|---|---|---|
| Rendered site (HTML tree) | `artifacts/docs/site/…` | Optionally served by a hosting target. Not promoted to `data/published/` unless a release decision says so. |
| Generated API reference | `artifacts/docs/api/…` | Same — regenerable, not citable as-is. |
| Exported PDF | `artifacts/docs/pdf/<doc-id>/<doc-id>.pdf` (linearized PDF/A-2u) | If released, a copy under [`data/published/reports/<doc-id>/`](../../data/published/) with a `ReleaseManifest` in [`release/manifests/`](../../release/). |
| `ARTIFACT_DIGEST` sidecar | `<doc-id>.sha256` co-located with the PDF | Cited from `release/` only via the `data/published/` copy. |

> [!IMPORTANT]
> **Promotion is governed, not a `cp`.** A file does not become "released" by being copied from `artifacts/docs/` into `data/published/`. Promotion requires a `ReleaseManifest`, a `PromotionDecision`, a rollback target, a correction path, and the applicable policy gates per Directory Rules §9. See [`release/`](../../release/) and the lifecycle invariant in Directory Rules §3.

[Back to top ↑](#contents)

---

## ⚡ Quickstart / usage

> [!NOTE]
> Commands below are **illustrative, PROPOSED**. The actual build orchestrator and Make/Just target are **NEEDS VERIFICATION** until repo inspection.

```bash
# 1. Build the documentation site (illustrative — verify actual target)
make docs-build       # PROPOSED target name
# or, equivalently if mkdocs is the chosen tool:
mkdocs build          # PROPOSED tool; verify

# 2. Build an exported PDF using the pinned toolchain (Pass-10 C13-01)
#    The build script MUST verify tool versions against tool-versions.yaml.
make docs-pdf DOC=<doc-id>   # PROPOSED

# 3. Compute the ARTIFACT_DIGEST (Pass-10 C13-04) — after linearization
qpdf --linearize artifacts/docs/pdf/<doc-id>/<doc-id>.pdf \
                 artifacts/docs/pdf/<doc-id>/<doc-id>.linear.pdf
sha256sum artifacts/docs/pdf/<doc-id>/<doc-id>.linear.pdf \
        > artifacts/docs/pdf/<doc-id>/<doc-id>.sha256

# 4. Clean local build (destructive — only this folder)
rm -rf artifacts/docs/site artifacts/docs/api artifacts/docs/_tmp
```

> [!WARNING]
> Step 4 is **destructive** but **safe within this folder** because contents are regenerable. Never run a destructive command that touches `data/`, `release/`, or `docs/` from a `docs-build` workflow.

[Back to top ↑](#contents)

---

## 🛡️ Validation

How this folder is checked.

- **Forbidden-content scan.** A scan that fails if any file matching `*.receipt.json`, `*evidence-bundle*.json`, `*release-manifest*.json`, `*rollback-card*`, or other trust-object patterns lands under `artifacts/`. _PROPOSED validator_; specific tool **NEEDS VERIFICATION**. Anchors anti-pattern §13.5 row "Trust content in `artifacts/`".
- **README presence.** Every canonical and compatibility root MUST carry a README meeting §15. This README is that contract for `artifacts/docs/`.
- **Build determinism.** Two clean builds from the same source MUST produce byte-identical outputs (Pass-10 `C13-01`/`C13-02`). _PROPOSED_ check: rebuild-and-diff in CI.
- **`ARTIFACT_DIGEST` recomputation.** A consumer-side script SHOULD recompute the sidecar and fail closed on mismatch (Pass-10 `C13-04`). _PROPOSED_; aligns with `KFM-P29-PROG-0011` (`verify_sidecar.mjs`).
- **Validator orchestrator entry point.** CI workflows that touch this folder SHOULD route through `tools/validators/validate_all.py` per Directory Rules §7.5.a — exit `0` pass, `1` any fail, `2` system error (exit-code contract is **PROPOSED**, ADR-class per §18 OPEN-DR-03).

> [!NOTE]
> Validators MUST exercise **DENY / ABSTAIN / ERROR** paths, not only the happy case (Directory Rules §7.5.a negative-state rule). A "did the docs build?" check that only proves success is incomplete.

[Back to top ↑](#contents)

---

## 👀 Review burden

- **Docs build steward** — _TODO assign via `CODEOWNERS`_. Owns the docs-build orchestrator, pinned tool versions, and the regeneration cadence.
- **Docs steward** (owner of [`docs/`](../../docs/)) — reviews any change to *what* is rendered (because source authority is in `docs/`).
- **Release steward** (owner of [`release/`](../../release/)) — reviews any path-change that touches how a built PDF is cited from a `ReleaseManifest`.
- **Reviewer of any PR adding/moving files here** — runs the Directory Rules §16 Path-Validation Checklist. Particular attention to checklist row "Trust content placement."

> [!TIP]
> If a PR adds a file under `artifacts/docs/` that *looks* like a receipt, manifest, or proof, the reviewer SHOULD request changes and link Directory Rules §13.5 ("Trust content in `artifacts/`"). The fix is migration, not exception.

[Back to top ↑](#contents)

---

## 🔗 Related folders

- [`artifacts/README.md`](../README.md) — parent root README; declares class and the cross-cutting "do not put X here" list.
- [`docs/`](../../docs/) — **authoritative** source for what is rendered into this folder.
- [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) — governing document. **Most relevant sections:** §5 (root tree), §8 (compatibility roots), §8.2 (`artifacts/` rule), §13.2 / §13.5 (anti-patterns), §15 (README contract), §16 (path-validation checklist), §18.a (open question on `artifacts/`).
- [`data/published/reports/`](../../data/published/) and [`data/published/stories/`](../../data/published/) — where **released** documents live, not here.
- [`release/manifests/`](../../release/) — release decisions; cite the `data/published/` copy of a document, not the `artifacts/docs/` copy.
- [`data/receipts/`](../../data/receipts/), [`data/proofs/`](../../data/proofs/) — trust-bearing process memory; never here.
- [`tools/`](../../tools/) — docs-build orchestrator and validators (specific paths NEEDS VERIFICATION).

[Back to top ↑](#contents)

---

## 📜 ADRs

- [`ADR-0001` — schema home](../../docs/adr/) — _TODO link once filename verified._ Establishes `schemas/contracts/v1/<…>` as canonical, which is the authoritative source for any generated API reference rendered into this folder.
- **OPEN — ADR on `artifacts/` treatment.** Directory Rules §18.a flags whether `artifacts/` is kept as a compatibility root or fully retired in favor of `data/receipts/`, `data/proofs/`, `release/`, and `data/published/`. An ADR resolving this affects the long-term existence of this folder. Status: **OPEN**.
- **OPEN — ADR-class exit-code contract.** Directory Rules §18 OPEN-DR-03 — validator orchestrator exit-code contract (`0` pass / `1` fail / `2` system error). Status: **PROPOSED**, ADR-class.

[Back to top ↑](#contents)

---

## ❓ Open questions

- **Does `artifacts/docs/` exist in the current mounted repo, and at what entrenchment?** **NEEDS VERIFICATION** — no mounted-repo inspection in the authoring session.
- **Is mkdocs the chosen documentation site tool?** **NEEDS VERIFICATION** — corpus uses "mkdocs site" illustratively (Directory Rules §8.2); the actual chosen tool, theme, plugins, and configuration are not inspected here.
- **What is the canonical `docs-build` workflow name and entry point?** **UNKNOWN** until repo inspection. Until then, the [Quickstart](#-quickstart--usage) commands are PROPOSED placeholders.
- **Where do `ARTIFACT_DIGEST` sidecars physically live for *released* documents?** **NEEDS VERIFICATION** — the local-build sidecar may co-locate with the PDF under `artifacts/docs/pdf/<doc-id>/`, but the *citable* sidecar for a released document SHOULD live with the released copy under `data/published/reports/<doc-id>/`. Whether the release-side sidecar is *also* mirrored back to `artifacts/docs/` is open.
- **PDF/UA conformance level.** Pass-10 `C13-03` records PDF/UA conformance as **PROPOSED** (preflight tool not yet named). The accepted conformance level (full PDF/UA vs. partial vs. structure tags only) is OPEN.
- **Should `artifacts/docs/` be removed when `artifacts/` is retired?** Tied to Directory Rules §18.a OPEN. If `artifacts/` is fully retired, this folder ceases to exist; generated documentation outputs would either move into a hosting target outside the repo, or into a renamed compatibility lane.

[Back to top ↑](#contents)

---

## 💬 FAQ

<details>
<summary><b>Why isn't this folder under <code>docs/</code>?</b></summary>

Because [`docs/`](../../docs/) is the **canonical control plane** for *authored* doctrine — what humans write and review. `artifacts/docs/` holds the **rendered build outputs** of that authoring. Mixing them would collapse "what we wrote" with "what the build produced," and that collapse is exactly what Directory Rules §13.2 warns against. The sources are in `docs/`; the rendered outputs are here; the *released* outputs (when promoted) go under `data/published/`.

</details>

<details>
<summary><b>If I want to publish a PDF, do I drop it in here?</b></summary>

No. The intermediate build product MAY land here, but the **released** copy goes under [`data/published/reports/<doc-id>/`](../../data/published/) with a `ReleaseManifest` entry under [`release/manifests/`](../../release/). Releasing is a governed state transition, not a file copy.

</details>

<details>
<summary><b>Sidecar duplication — should the <code>ARTIFACT_DIGEST</code> sidecar live here, in <code>data/published/</code>, or both?</b></summary>

**NEEDS VERIFICATION.** The doctrine (Pass-10 `C13-04`) is that the sidecar is the citation anchor — receipts cite the digest, and consumers verify it. The **citable** sidecar therefore needs to live alongside the **released** copy under `data/published/reports/<doc-id>/` so that the citation path from `release/` is consistent with the lifecycle home. Whether a *local-only* copy of the sidecar also lives at `artifacts/docs/pdf/<doc-id>/<doc-id>.sha256` for build-time verification is implementation-dependent and OPEN. The hard rule: a sidecar cited from `release/` MUST resolve into `data/published/`, never into `artifacts/`.

</details>

<details>
<summary><b>Can a CI workflow write directly to <code>artifacts/docs/</code>?</b></summary>

Yes — that is what this folder is for. Build workflows MAY write here freely. The constraint is on **content**, not write access: trust-bearing objects (receipts, proofs, manifests, rollback cards, correction notices) MUST NOT land here even if a CI step has the permission to write them. Drift between "what a workflow can write" and "what doctrine allows here" is precisely what the §13.5 anti-pattern row exists to catch.

</details>

<details>
<summary><b>What if <code>artifacts/</code> is retired entirely?</b></summary>

Then `artifacts/docs/` retires with it. Directory Rules §18.a flags this as **OPEN**. Until an ADR resolves the question, treat `artifacts/docs/` as `transitional` (its parent's default compatibility class) and avoid hardening it into authority. If the retirement ADR lands, expect a migration with rollback per Directory Rules §14.

</details>

<details>
<summary><b>Why is the parent folder a "compatibility" root and not "canonical"?</b></summary>

Because canonical roots own a *responsibility* (authority, lifecycle, governance). `artifacts/` owns no responsibility that isn't already owned by a canonical root — `docs/` owns authored doctrine; `data/published/` owns released artifacts; `release/` owns release decisions; `data/proofs/` and `data/receipts/` own trust-bearing process memory; `tools/` and `pipelines/` own the build logic. What's left for `artifacts/` is *scratch space for build outputs*, which is a compatibility-class responsibility at best. Hence: optional, tightly scoped, class default `transitional`.

</details>

[Back to top ↑](#contents)

---

## 📎 Appendix — §8.2 substructure (verbatim)

The substructure below is reproduced verbatim from [`docs/doctrine/directory-rules.md` §8.2](../../docs/doctrine/directory-rules.md) so any drift between this README and the governing document is reviewable side-by-side.

```text
artifacts/
├── README.md       # declares class and what does NOT belong
├── build/          # compiled outputs, distributables
├── docs/           # generated documentation (mkdocs site, API ref)
├── qa/             # QA reports, lint output, test coverage
└── temporary/      # ephemeral; gitignored or pruned regularly
```

> `artifacts/` MUST NOT be the canonical home for: receipts, proofs, evidence bundles, release manifests, promotion decisions, rollback cards, correction notices, catalog records, published layers. Those belong in `data/receipts/`, `data/proofs/`, `release/`, `data/catalog/`, and `data/published/`. — Directory Rules §8.2.

[Back to top ↑](#contents)

---

## 🦶 Footer

**Related docs**

- [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) — governing document (§5, §8, §13, §15, §16, §18).
- [`artifacts/README.md`](../README.md) — parent compatibility-root README.
- [`docs/`](../../docs/) — authored doctrine, the source for what gets rendered here.
- [`data/published/`](../../data/published/) — released public-safe artifacts.
- [`release/`](../../release/) — release decisions, manifests, rollback cards.
- _TODO_ — link `docs/doctrine/lifecycle-law.md` once verified present.
- _TODO_ — link the docs-build runbook once authored.

**Last updated:** _TODO_ (ISO date — set on first merge).

[⬆ Back to top](#-artifactsdocs)
