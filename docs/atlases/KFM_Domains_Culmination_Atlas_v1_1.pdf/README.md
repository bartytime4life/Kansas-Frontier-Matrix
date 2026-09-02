<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/atlas-v1-1-pdf-sidecar-readme
title: Atlas v1.1 PDF — Sidecar README (PATH CONFLICT — RECONCILIATION REQUIRED)
type: standard
version: v1
status: draft
owners: OWNER_TBD  # NEEDS VERIFICATION: docs steward + atlas editors
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - kfm://doc/atlas-v1-1                                    # PROPOSED: docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf (the PDF, NOT this directory)
  - kfm://doc/atlas-v1-0                                    # PROPOSED: docs/atlases/KFM_Domains_Culmination_Atlas_v1_0.pdf
  - kfm://doc/atlas-v1-1-chapter-extracts-readme            # CONFIRMED authored: docs/atlases/master-atlas-v1.1/README.md
  - kfm://doc/atlas-v1-1-ch24-5-sensitivity-tier-reference  # CONFIRMED authored sibling
  - kfm://doc/atlas-v1-1-ch24-6-pipeline-gate-reference     # CONFIRMED authored sibling
  - kfm://doc/directory-rules                               # CONFIRMED: docs/doctrine/directory-rules.md
tags: [kfm, atlas, pdf, sidecar, readme, path-conflict, reconciliation]
notes:
  - This README sits at a PATH-CONFLICTED location. The literal requested path treats `KFM_Domains_Culmination_Atlas_v1_1.pdf` as a directory, but the Atlas v1.1 front matter explicitly proposes the same name as the PDF file location. These two cannot coexist.
  - The body of this file is portable. Migrate it to whichever alternative path the docs steward selects (§1 lists candidates). Then delete this directory.
  - All substantive content (PDF metadata, regeneration commands, supersession lineage, verification checklist) is grounded in Atlas v1.1 front matter, §23.1, and Appendix G.
[/KFM_META_BLOCK_V2] -->

# Atlas v1.1 PDF — Sidecar README

<!-- [doc: kfm://doc/atlas-v1-1-pdf-sidecar-readme] -->
<a id="top"></a>

> Companion documentation for the **Kansas Frontier Matrix Domains Culmination Atlas, v1.1** PDF — its provenance, supersession lineage, regeneration commands, and integrity verification. **This file currently sits at a path-conflicted location** and should be migrated before merge. See §1.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-blue">
  <img alt="Path: CONFLICT" src="https://img.shields.io/badge/path-CONFLICT-critical">
  <img alt="Migration: required" src="https://img.shields.io/badge/migration-required-red">
  <img alt="Edition: Atlas v1.1" src="https://img.shields.io/badge/edition-Atlas%20v1.1-informational">
  <img alt="PDF authored: 2026-05-12" src="https://img.shields.io/badge/PDF%20authored-2026--05--12-purple">
  <img alt="Supersedes: v1.0" src="https://img.shields.io/badge/supersedes-v1.0-yellow">
</p>

> [!CAUTION]
> **PATH CONFLICT — DO NOT MERGE AT THIS LOCATION.**
> This file currently lives at `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf/README.md`, which treats `KFM_Domains_Culmination_Atlas_v1_1.pdf` as a **directory**. But the Atlas v1.1 front matter (CONFIRMED doctrine) explicitly proposes the **same path string** as the location of the **PDF file** itself. A filesystem path can be a file *or* a directory at a given name, not both. Keeping this directory in place will **block** the PDF from landing at its documented home. See §1 for reconciliation options.

> [!NOTE]
> **Anti-collapse rule (inherited from Atlas v1.1 front matter).** This sidecar README does not substitute for the PDF, the EvidenceBundle, the PolicyDecision, or the ReviewRecord. It documents the PDF; it has no authority over it.

---

## Contents

1. [Path conflict — reconciliation required](#1-path-conflict--reconciliation-required)
2. [Scope of this sidecar](#2-scope-of-this-sidecar)
3. [The PDF artifact](#3-the-pdf-artifact)
4. [Edition lineage — v1.0 → v1.1](#4-edition-lineage--v10--v11)
5. [Chapter structure](#5-chapter-structure)
6. [Regeneration & assembly](#6-regeneration--assembly)
7. [Integrity & verification](#7-integrity--verification)
8. [Migration plan](#8-migration-plan)
9. [Open questions & ADR cross-reference](#9-open-questions--adr-cross-reference)
10. [Evidence basis & citations](#10-evidence-basis--citations)

---

## 1. Path conflict — reconciliation required

### 1.1 The conflict, stated plainly

| Item | Value |
|:---|:---|
| **Literal path of this README** | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf/README.md` |
| **Atlas v1.1's proposed PDF location** | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` |
| **Filesystem reality** | A path can be a **file** or a **directory**, not both. |
| **Source of the PDF-path proposal** | Atlas v1.1 front matter — *"PROPOSED file home: `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` per Directory Rules §5 / §6.1."* (CONFIRMED doctrine; NEEDS VERIFICATION final repo home) |
| **Severity** | High. Keeping this directory in place silently overwrites a documented PDF home. |

### 1.2 Reconciliation options

Pick one. The body of this README (§2 – §7, §9 – §10) is portable to any of them.

| # | Alternative path | Trade-off |
|:---|:---|:---|
| **A** | `docs/atlases/README.md` *(recommended)* | Parent-folder README for the entire `docs/atlases/` lane. Documents the PDF, the chapter-extracts subfolder, the v1.0 PDF, and any other atlas artifacts in one place. Natural complement to the existing `master-atlas-v1.1/README.md`. **No path collision.** |
| **B** | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf.md` | Flat sidecar Markdown adjacent to the PDF — common pattern for PDF-companion docs. No collision because the `.pdf.md` suffix is distinct from `.pdf`. The two files sort together alphabetically. |
| **C** | `docs/atlases/atlas-v1-1.companion/README.md` | Companion folder with a dot-suffix naming convention. Allows a structured companion (multiple files: README + figures + manifests) without colliding with the PDF. |
| **D** | `docs/atlases/master-atlas-v1.1/PDF.md` | Place the PDF documentation inside the existing chapter-extracts folder. Treats the PDF as one node of the v1.1 master-atlas set. Trade-off: conflates "PDF artifact" with "Markdown chapter extracts" which currently have distinct purposes. |

> [!TIP]
> **Recommendation.** Option **A** (`docs/atlases/README.md`) is the cleanest fit: it parallels the already-authored `master-atlas-v1.1/README.md` one level down, documents the whole atlases lane (not just one PDF), and avoids inventing a new naming convention. Option **B** is the runner-up if the docs steward wants a dedicated per-PDF sidecar.

### 1.3 What to do with this file

Once an alternative is chosen:

1. **Copy** the body of this file (sections 2 – 10) to the chosen path.
2. **Update** the `doc_id`, `title`, and the §1 path-conflict notice (delete or rephrase it — once migrated, there is no conflict to flag).
3. **Delete** the directory `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf/` so the PDF's proposed home is unblocked.
4. **Place** the actual PDF at `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` per Atlas v1.1 front matter.
5. **Log** the migration in `docs/registers/DRIFT_REGISTER.md` so the path-conflict moment is auditable.

The remainder of this README is the body that migrates.

[↑ back to top](#top)

---

## 2. Scope of this sidecar

Once migrated to a non-conflicted path, this document documents:

- **What the PDF is** (edition, author, date, supersession status) — §3.
- **How it relates to v1.0** (supersession-by-extension; reversibility) — §4.
- **What's in it** (chapter structure summary; cross-link to the Markdown chapter extracts) — §5.
- **How to regenerate it** (Pandoc assembly procedure from Atlas §23.1) — §6.
- **How to verify its integrity** (SHA-256 prefix, embedded manifest, signing posture) — §7.

It does **not** restate the chapter content — that lives in the PDF and (selectively) in `docs/atlases/master-atlas-v1.1/`. The sidecar is metadata about the artifact, not a replacement for it.

[↑ back to top](#top)

---

## 3. The PDF artifact

**Status:** the metadata below is CONFIRMED from the Atlas v1.1 front matter and the consolidation wrapper. Mounted-repo presence of the PDF at the proposed home is NEEDS VERIFICATION.

| Field | Value | Source |
|:---|:---|:---|
| **Title** | Kansas Frontier Matrix Domains Culmination Atlas, v1.1 | Atlas v1.1 front matter |
| **Author** | KFM Domain Synthesizer | Atlas v1.1 front matter |
| **Edition** | v1.1 — current edition | Atlas v1.1 Edition note (CONFIRMED) |
| **Authoring date** | 2026-05-12 | Atlas v1.1 cover |
| **Supersedes** | v1.0 (dated 2026-05-11) — by integrated extension | Atlas v1.1 Edition note (CONFIRMED) |
| **Reversibility** | Full. Removing front matter + Ch. 24 + App. G yields v1.0 unchanged. | Atlas v1.1 cover supersession block (CONFIRMED) |
| **PDF format** | PDF 1.5 | Atlas v1.1 consolidation wrapper |
| **Size** | 7,899,514 bytes *(Atlas v1.1 source PDF, prior to consolidation with Pass 23/32 corpus)* | Atlas v1.1 consolidation wrapper, p. 5 |
| **SHA-256 prefix** | `a0dda5f85fc7787642c38605…` | Atlas v1.1 consolidation wrapper, p. 5 |
| **Embedded files** | None detected in v1.1 source | Atlas v1.1 consolidation wrapper |
| **Truth-label set** | CONFIRMED, PROPOSED, NEEDS VERIFICATION, UNKNOWN *(same four as v1.0; v1.1 introduces no new labels)* | Atlas v1.1 Edition note (CONFIRMED) |
| **Citation short names** | ENCY, DIRRULES, MAP-MASTER, GAI, DDD, UNIFIED, UIAI, INDEX-18, DOM-* *(v1.0 set reused; v1.1 adds none)* | Atlas v1.1 §G.6 self-check (CONFIRMED) |
| **Proposed file home** | `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` per Directory Rules §5 / §6.1 | Atlas v1.1 cover Version block (PROPOSED; NEEDS VERIFICATION final repo home) |

> [!NOTE]
> The SHA-256 **prefix only** is recorded in the consolidation wrapper. A full SHA-256 of the placed PDF should be captured into `docs/registers/DRIFT_REGISTER.md` or a sidecar `MANIFEST.md` when the PDF is committed to the canonical home.

[↑ back to top](#top)

---

## 4. Edition lineage — v1.0 → v1.1

**CONFIRMED supersession mode.** Integrated extension — v1.1 retains every page of v1.0 verbatim as its doctrinal core, then adds Chapter 24 and Appendix G. Removal of v1.1's additions yields v1.0 unchanged.

| Aspect | Status under v1.1 |
|:---|:---|
| **v1.0 chapters 1–23** | CONFIRMED unchanged. Page numbering, internal references, figure-to-generate IDs all remain valid. |
| **v1.0 Appendices A–F** | CONFIRMED unchanged (glossary, source family, object family, directory rules, supersession, self-check). |
| **v1.0 truth labels and citation conventions** | CONFIRMED unchanged. |
| **Source dossiers** (encyclopedia, directory rules, MapLibre master, governed AI, DDD, INDEX-18, DOM-*) | CONFIRMED unchanged — v1.1 cites them; does not edit them. |
| **Chapter 24 — Extended Master Atlases (14 registers)** | Net addition. Positioned after the v1.0 interior. |
| **Appendix G — v1.0 → v1.1 Lineage and Supersession Record** | Net addition. Complements (does not replace) v1.0 Appendix E. |
| **PDF metadata title** | Updated to "Kansas Frontier Matrix Domains Culmination Atlas, v1.1". |

### 4.1 What v1.1 explicitly does NOT change

Per Atlas v1.1 §G.3 (CONFIRMED):

- No v1.0 chapter rewritten, deleted, or contradicted.
- No new domain introduced.
- No new lifecycle phase.
- No new authority root.
- No new object family.
- No new glossary terms.

> [!IMPORTANT]
> Any of the above changes would require an ADR per Directory Rules §2.4 and are explicitly out of scope for v1.1. They remain available for a future v1.2 / v2.0 edition under separate governance.

### 4.2 v1.0 retention

The v1.0 PDF is **retained at its existing path as historical record** (Atlas v1.1 cover Version block, NEEDS VERIFICATION on the exact path). v1.0 remains a standalone, citable artifact in its own right — removal of v1.1 returns the system cleanly to v1.0.

[↑ back to top](#top)

---

## 5. Chapter structure

**CONFIRMED structure** (Atlas v1.1 Integrated Contents, p. 5). One row per major section.

### 5.1 v1.0 interior (retained verbatim, chapters 1–23 plus appendices A–F)

| § | Chapter | Origin |
|:---|:---|:---|
| 1 | Executive Summary and Operating Law | v1.0 |
| 2 | Master Source Ledger and Cross-Domain Object Index | v1.0 |
| 3 | Spatial Foundation | v1.0 |
| 4 | Hydrology | v1.0 |
| 5 | Soil | v1.0 |
| 6 | Habitat | v1.0 |
| 7 | Fauna | v1.0 |
| 8 | Flora | v1.0 |
| 9 | Agriculture | v1.0 |
| 10 | Geology / Natural Resources | v1.0 |
| 11 | Atmosphere / Air | v1.0 |
| 12 | Hazards | v1.0 |
| 13 | Roads / Rail / Trade Routes | v1.0 |
| 14 | Settlements / Infrastructure | v1.0 |
| 15 | Archaeology / Cultural Heritage | v1.0 |
| 16 | People / Genealogy / DNA / Land Ownership | v1.0 |
| 17 | Frontier Matrix | v1.0 |
| 18 | Planetary / 3D / Digital Twin / Synthetic | v1.0 |
| 19 | Cross-Domain Systems | v1.0 |
| 20 | Master Atlases (viewing, capability, API, validator, deny) | v1.0 |
| 21 | Roadmap and Dependency Graph | v1.0 |
| 22 | Appendices A–F | v1.0 |
| 23 | Assembly Instructions | v1.0 |

### 5.2 v1.1 additions (Chapter 24 + Appendix G)

Chapter 24 contains fourteen master registers plus an Appendix G lineage record. **Per-chapter detail and Markdown extracts** live in [`master-atlas-v1.1/`](../master-atlas-v1.1/) — see that subfolder's README for the chapter inventory, naming conventions, and authoring status.

| § | Chapter | Markdown extract status |
|:---|:---|:---:|
| 24.1 | Source-Role Anti-Collapse Register | ⏳ |
| 24.2 | Master Receipt Catalog | ⏳ |
| 24.3 | Decision Outcome Envelope Reference | ⏳ |
| 24.4 | Cross-Lane Relation Atlas | ⏳ |
| 24.5 | Sensitivity / Rights Tier Reference (T0–T4) | ✅ |
| 24.6 | Pipeline Gate Reference (RAW → PUBLISHED) | ✅ |
| 24.7 | Reviewer Role and Separation-of-Duties Matrix | ⏳ |
| 24.8 | Stale-State and Supersession Reference | ⏳ |
| 24.9 | Failure-Mode and Anti-Pattern Register | ⏳ |
| 24.10 | Risk Register and Threat Posture | ⏳ |
| 24.11 | Governance Health Indicators | ⏳ |
| 24.12 | Open-ADR Backlog | ⏳ |
| 24.13 | Atlas ↔ Dossier ↔ Responsibility-Root Crosswalk | ⏳ |
| 24.14 | Object Family × Domain Reference Matrix | ⏳ |
| App. G | v1.0 → v1.1 Lineage and Supersession Record | ⏳ |

The PDF carries **all** of these sections regardless of Markdown extract status. The Markdown extracts are review-granularity aids over the authoritative PDF.

[↑ back to top](#top)

---

## 6. Regeneration & assembly

**CONFIRMED procedure** (Atlas v1.0 §23.1, inherited by v1.1).

### 6.1 Recommended Pandoc command

```bash
pandoc KFM_Domains_Culmination_Atlas_v1.1.md \
  --from markdown+pipe_tables+raw_tex \
  --toc --toc-depth=2 \
  --pdf-engine=xelatex \
  -V geometry:margin=0.62in \
  -V fontsize=11pt \
  -V colorlinks=true \
  -o KFM_Domains_Culmination_Atlas_v1_1.pdf
```

> [!NOTE]
> The command above is Atlas v1.0's recommended Pandoc command adapted for the v1.1 source. The v1.0 source-file naming uses `v1.0` (dot-separator); the proposed PDF output uses `v1_1` (underscore-separator) per Directory Rules §6.1 conventions. Confirm the source-file naming when the v1.1 Markdown master is finalized.

### 6.2 LaTeX alternative (PROPOSED, per Atlas §23.2)

```bash
pandoc KFM_Domains_Culmination_Atlas_v1.1.md \
  --from markdown+pipe_tables+raw_tex \
  --toc --toc-depth=2 \
  -o KFM_Domains_Culmination_Atlas_v1.1.tex
latexmk -xelatex KFM_Domains_Culmination_Atlas_v1.1.tex
```

### 6.3 Typst alternative (PROPOSED, per Atlas §23.2)

```bash
pandoc KFM_Domains_Culmination_Atlas_v1.1.md -t typst -o KFM_Domains_Culmination_Atlas_v1.1.typ
typst compile KFM_Domains_Culmination_Atlas_v1.1.typ KFM_Domains_Culmination_Atlas_v1_1.pdf
```

> [!WARNING]
> Both alternatives require verification of table wrapping and page breaks because the manuscript uses Markdown `\pagebreak` markers. The Atlas v1.0 source notes the first LaTeX command overflows/clips at the right edge of the source PDF at p. 149 — preserve that observation when regenerating.

### 6.4 Figures to generate separately

Atlas §23.3 lists figures intended for separate generation (CONFIRMED in source). These are not embedded in the Markdown master; they must be produced and either embedded in the PDF or linked from it:

- **KFM lifecycle spine** — `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED` with promotion / correction / rollback gates. (See `master-atlas-v1.1/24.6-pipeline-gate-reference.md` §5 for a Mermaid version.)
- **Evidence-to-public-surface membrane** — layered diagram (SourceDescriptor → EvidenceBundle → PolicyDecision → ReleaseManifest → governed API).
- **Sensitive-domain fail-closed map** — matrix figure for archaeology, fauna, flora, infrastructure, living-person/DNA, 3D exposure.
- **Cross-domain dependency graph** — directed graph from Directory Rules to all domain lanes.
- **Hydrology proof-lane exemplar** — flow from WBD/HUC fixture through validation, EvidenceBundle, LayerManifest, Evidence Drawer, Focus Mode, rollback.
- **Source-role anti-collapse diagram** — observed / regulatory / modeled / aggregate / administrative / candidate / synthetic as separate source-role channels.

[↑ back to top](#top)

---

## 7. Integrity & verification

**Status:** posture description is PROPOSED until the PDF is committed to its canonical home and signing infrastructure is in place. Mounted-repo signing posture is NEEDS VERIFICATION.

### 7.1 Hash verification

When the PDF lands at `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf`, capture its full SHA-256 (not just prefix):

```bash
sha256sum docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
```

Record the hash in:

- This sidecar's `## 3. The PDF artifact` table (replace the prefix-only row);
- `docs/registers/DRIFT_REGISTER.md` as a supersession entry;
- A `MANIFEST.md` adjacent to the PDF if one exists at this lane.

The consolidation-wrapper prefix `a0dda5f85fc7787642c38605…` is a starting checkpoint; it should reproduce against the final committed PDF if the same source-Markdown and Pandoc command are used.

### 7.2 Signing posture (PROPOSED)

Per KFM operating-law invariant 4 (deterministic identity), the PDF is a candidate for:

- **DSSE-envelope** signing of the PDF bytes;
- **Cosign / Rekor** transparency log entry recording the release;
- A **ReleaseManifest** at `release/manifests/atlas-v1-1.json` referencing the PDF, its hash, its signing envelope, and the prior-release rollback target.

None of the above is CONFIRMED as currently implemented — it is the posture the doctrine recommends. NEEDS VERIFICATION against mounted-repo `release/` lane.

### 7.3 Reproducibility check

Reproducibility is a precondition for the supersession-reversibility guarantee in §4. Concretely:

| Check | What to confirm |
|:---|:---|
| **Source Markdown matches** | The v1.1 master Markdown file produces the v1.1 PDF deterministically under the §6.1 Pandoc command. |
| **v1.0 reverse-build** | Removing front matter, Chapter 24, and Appendix G from the v1.1 Markdown master produces the **byte-identical v1.0 source** (or at minimum, a v1.0 PDF whose retained-body hash matches the v1.0 historical hash). |
| **Per-section integrity** | The v1.0 retained-body SHA-256 reproduces if v1.1 supersession was non-destructive. *(See the Pass 23/32 consolidated atlas §5 "v1.3 retained-body SHA-256 verification" for the procedural pattern.)* |

[↑ back to top](#top)

---

## 8. Migration plan

If this file is migrated to one of the alternative paths from §1.2, follow these steps.

### 8.1 Migration steps

1. **Pick a target.** Decide between options A, B, C, or D in §1.2.
2. **Copy the body.** Sections 2 – 7 and 9 – 10 of this file are portable. Section 1 (path conflict) should be **deleted** at the destination — once migrated, there is no conflict.
3. **Rewrite the meta block.** Update `doc_id`, `title`, `status` (`draft` → still `draft` until reviewed), `notes` (remove path-conflict callouts), and `related` URIs as needed.
4. **Delete this directory.** Once the body has migrated, delete `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf/` (the directory) so the PDF's proposed home is unblocked.
5. **Place the PDF.** Move or commit the actual PDF to `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` per Atlas v1.1 front matter.
6. **Log the migration.** Add a drift-register entry to `docs/registers/DRIFT_REGISTER.md` recording: the original (conflicted) path; the chosen destination; the deletion of the conflicting directory; the placement of the PDF; the date.
7. **Update cross-references.** Any file that linked to `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf/README.md` (there should be none currently) must be updated to the new path.

### 8.2 Files currently linking back to this README

| Linking file | Link target | Action |
|:---|:---|:---|
| *(none currently)* | — | — |

If the path conflict goes unnoticed and future files come to depend on the conflicted path, this table grows — adding to migration cost. **Reconcile early.**

[↑ back to top](#top)

---

## 9. Open questions & ADR cross-reference

| # | Question | Class | Cross-reference |
|:---|:---|:---|:---|
| **OPEN-PDF-01** | What is the canonical naming/placement convention for PDF-companion sidecars in `docs/atlases/`? Flat `<name>.pdf.md`, dot-suffix folder `<name>.companion/README.md`, parent-folder README, or per-PDF inside `master-atlas-v<X.Y>/`? | Naming class | New candidate ADR; relates to **ADR-S-02** (doctrine artifact placement under `docs/`). |
| **OPEN-PDF-02** | Should the Atlas v1.1 PDF be signed (DSSE / Cosign) before commit, after commit, or never? | Release class | New candidate ADR; relates to operating-law invariant 4 (deterministic identity) and `release/` lane. |
| **OPEN-PDF-03** | Where does the full SHA-256 of the placed PDF live — sidecar README, `MANIFEST.md`, `release/manifests/`, or all three? | Provenance class | Relates to §24.2 (Receipt Catalog) and `release/` placement. |
| **OPEN-PDF-04** | What is the canonical path for the v1.0 PDF retention? Atlas v1.1 says "retained at its existing path" but does not name it. | Directory class | NEEDS VERIFICATION; resolve in per-root README at `docs/atlases/` or via ADR. |
| **OPEN-PDF-05** | Should the **PDF master Markdown source** (the file fed to Pandoc in §6.1) live in `docs/atlases/` next to the PDF, in `docs/sources/`, or in a build-time only location? | Source-of-truth class | New candidate ADR. |
| **OPEN-PDF-06** | Does the `docs/atlases/master-atlas-v1.1/` subfolder ADR question (OPEN-ENC-02 / OPEN-TIER-02 / OPEN-GATE-02 / OPEN-CHEXT-01) **also** decide PDF-sidecar placement? Or are they separate ADRs? | Scoping class | Resolve in the paired-ADR drafting process. |

[↑ back to top](#top)

---

## 10. Evidence basis & citations

<details>
<summary><strong>Source ledger</strong></summary>

| Source | Status | Supports | Limits |
|:---|:---|:---|:---|
| Atlas v1.1 front matter — Version block (cover, consolidated PDF) | CONFIRMED (manuscript) | §3 PDF artifact metadata; §1 path-conflict statement (the PDF's proposed home). | Manuscript is doctrine; final repo home remains NEEDS VERIFICATION. |
| Atlas v1.1 Edition note (PDF p. 8) | CONFIRMED (manuscript) | §4 edition lineage; reversibility rule; non-collapse rule. | — |
| Atlas v1.1 Integrated Contents (PDF p. 5) | CONFIRMED (manuscript) | §5 chapter structure (both v1.0 interior and v1.1 additions). | Verbatim chapter titles preserved. |
| Atlas v1.1 §G.3 — "What v1.1 does not change" (PDF, App. G) | CONFIRMED (manuscript) | §4.1 explicit non-changes. | — |
| Atlas v1.1 §G.7 — Forward verification backlog (PDF, App. G) | CONFIRMED (manuscript) | §7 verification posture; sidecar's NEEDS VERIFICATION items. | Backlog is PROPOSED for action. |
| Atlas v1.0 §23.1 / §23.2 / §23.3 — Assembly instructions | CONFIRMED (manuscript) | §6 regeneration commands (Pandoc / LaTeX / Typst); figures-to-generate list. | Source-file naming uses `v1.0`; the v1.1 equivalent file naming is NEEDS VERIFICATION. |
| Atlas v1.1 consolidation wrapper (PDF, pp. 5–6) | CONFIRMED (manuscript) | §3 PDF format, size, SHA-256 prefix; preservation-and-deduplication rule. | Hash is prefix-only; full hash NEEDS VERIFICATION against placed PDF. |
| `directory-rules.md` §5, §6.1, §13.5 | CONFIRMED (prior-session authored) | §1 reconciliation options; §8 migration plan. | Mounted-repo presence NEEDS VERIFICATION. |
| `docs/atlases/master-atlas-v1.1/README.md` | CONFIRMED (prior-session authored) | §5.2 chapter-extract cross-reference; §1.2 Option A precedent (parent-folder README rationale). | — |
| Pass 23/32 consolidated atlas §5 (v1.3 retained-body SHA-256 verification) | CONFIRMED (project doc) | §7.3 reproducibility-check procedural pattern. | Procedure applies to source-Markdown body; PDF byte-hash is a separate check. |

</details>

### 10.1 Citation key

The Atlas corpus uses dossier-shorthand citations. They appear inside individual chapter files and in the PDF; this sidecar does not reproduce them in body text:

| Tag | Refers to |
|:---|:---|
| `[ENCY]` | KFM Encyclopedia |
| `[DIRRULES]` | Directory Rules |
| `[GAI]` | Governed AI doctrine |
| `[MAP-MASTER]` | Master MapLibre Components-Functions-Features |
| `[UNIFIED]` | KFM Unified Implementation Architecture Build Manual |

> [!NOTE]
> **Anti-collapse rule (reaffirmed).** This sidecar README documents an artifact; it is not the artifact. The PDF is one carrier of Atlas doctrine; the doctrine itself rests on the source dossiers and the EvidenceBundle / PolicyDecision / ReviewRecord chain — not on any single PDF or its sidecar.

[↑ back to top](#top)

---

<sub>Sidecar README for the Atlas v1.1 PDF. **Currently at a path-conflicted location.** Migration required before merge — see §1. Authoritative artifact is the PDF itself, intended location `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf`.</sub>
