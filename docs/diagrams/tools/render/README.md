<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c98ca62e-910d-4a56-8aa9-a5de946ed684
title: Diagram render tooling
type: standard
version: v1
status: draft
owners: TBD
created: 2026-03-02
updated: 2026-03-02
policy_label: public
related:
  - docs/diagrams/README.md
tags: [kfm, diagrams, tooling, render]
notes:
  - Source-of-truth diagrams should be text-defined; rendered assets should be reproducible.
  - Keep outputs deterministic and CI-verifiable; avoid hand-editing generated images.
[/KFM_META_BLOCK_V2] -->

# Diagram render tooling

> Text-defined diagrams → deterministic rendered assets for KFM docs (and downstream Story/Map surfaces).

![Status](https://img.shields.io/badge/status-draft-orange)
![Scope](https://img.shields.io/badge/scope-docs%2Fdiagrams-blue)
![Output](https://img.shields.io/badge/output-svg%2Fpng-informational)
![Principle](https://img.shields.io/badge/principle-rebuildable-success)
![Governance](https://img.shields.io/badge/governance-evidence--first%20%26%20policy--aware-critical)

**This folder exists to make diagram rendering boring:** repeatable, reviewable, and hard to “accidentally” drift.

---

## Navigation

- [Overview](#overview)
- [Where this fits](#where-this-fits)
- [Directory layout](#directory-layout)
- [Inputs and outputs](#inputs-and-outputs)
- [Quick start](#quick-start)
- [Render contract](#render-contract)
- [Determinism and governance](#determinism-and-governance)
- [CI integration](#ci-integration)
- [Troubleshooting](#troubleshooting)
- [Appendix](#appendix)

---

## Overview

KFM documentation uses **text-defined diagrams** (Mermaid, PlantUML, Graphviz DOT, etc.) as the *source of truth*.
This directory defines (or will define) the **rendering workflow** that converts those sources into **static assets**
(SVG preferred, PNG when needed) that can be embedded in:

- GitHub READMEs and docs
- Documentation sites (MkDocs / Docusaurus / etc.)
- PDFs (where Mermaid/PlantUML may not render)

> **Rule of thumb:** edit the text source; re-render; commit the generated asset.

---

## Where this fits

- **Domain:** documentation toolchain
- **Layer:** “docs infrastructure” (not runtime code)
- **Trust posture:** generated artifacts must be **reproducible** and **reviewable** (CI should detect drift)

---

## Directory layout

> ⚠️ **Repo reality check:** the exact layout below is a **recommended** structure.  
> If your repo differs, update this section to match reality and keep the invariants.

```text
docs/
  diagrams/
    README.md                     # Top-level docs/diagrams overview (recommended)
    src/                          # Text-defined sources (e.g., .mmd/.puml/.dot)
    rendered/                     # Generated assets (e.g., .svg/.png) — do not hand-edit
    tools/
      render/
        README.md                 # (this file)
        manifest.yaml             # Render manifest (recommended; optional)
        render.sh                 # Single entrypoint (recommended)
        docker/                   # Optional pinned toolchain image(s)
          Dockerfile
          README.md
```

---

## Inputs and outputs

### Accepted inputs

| Kind | Typical extensions | When to use |
|---|---|---|
| Mermaid | `.mmd`, `.mermaid` | Flowcharts, sequences, small-ish architecture diagrams; best when GitHub rendering is sufficient |
| PlantUML | `.puml` | UML-style diagrams; sequence/class/component; when you want stronger UML semantics |
| Graphviz | `.dot` | Graphs (especially when layout control matters) |
| SVG source | `.svg` | Only when you truly need hand-authored vector artwork (rare) |

### Produced outputs

| Output | Preferred? | Why |
|---|---:|---|
| `.svg` | ✅ | Diffable-ish, scales cleanly, better for docs sites and PDFs |
| `.png` | ⚠️ | Fallback for platforms that don’t handle SVG well; larger + less diff-friendly |

> **Exclusions:** do **not** commit screenshots of diagrams as the “source of truth” unless there is no text-defined source available.

---

## Quick start

This directory is intentionally compatible with *either* local installs *or* a pinned container toolchain.

### Option A: Local toolchain (developer machine)

1. Install renderers (examples):
   - Mermaid CLI
   - Graphviz (dot)
   - Java + PlantUML

2. Run the renderer entrypoint.

```bash
# TODO: replace with the real command once implemented in this repo
./docs/diagrams/tools/render/render.sh --all
```

### Option B: Container toolchain (preferred for CI + determinism)

```bash
# TODO: replace with the real command once implemented in this repo
./docs/diagrams/tools/render/render.sh --all --use-docker
```

---

## Render contract

To keep rendering predictable (and CI-friendly), the renderer should implement these rules:

1. **Single entrypoint** (one command to render everything)
2. **Manifest-driven** rendering (optional but recommended)
3. **Deterministic outputs**
   - pinned tool versions
   - stable fonts where possible
   - stable output formatting
4. **No side effects outside `docs/diagrams/rendered/`**
5. **Fail closed**
   - syntax errors fail the job
   - missing inputs fail the job

### Manifest template (recommended)

Create `manifest.yaml` to declare all diagrams and their outputs:

```yaml
# docs/diagrams/tools/render/manifest.yaml
version: v1
items:
  - id: kfm_arch_overview
    engine: mermaid
    input: ../../src/kfm_arch_overview.mmd
    outputs:
      - ../../rendered/kfm_arch_overview.svg
    policy_label: public

  - id: evidence_resolver_sequence
    engine: plantuml
    input: ../../src/evidence_resolver_sequence.puml
    outputs:
      - ../../rendered/evidence_resolver_sequence.svg
    policy_label: public
```

> **Why a manifest?** It makes rendering auditable, avoids “magic globbing,” and allows policy labeling per diagram.

---

## Determinism and governance

KFM is **governed and evidence-first**. Diagram rendering should follow the same posture:

### Governance rules for diagrams

- **No “trust-breaking” diagrams:** if a diagram implies behavior, it must match the repo reality (or be explicitly labeled *PROPOSED*).
- **No sensitive targeting:** diagrams must not leak precise sensitive locations or restricted datasets.
- **Policy-aware outputs:** if a diagram is derived from restricted material, the rendered output should not be committed in public docs.

### “Truth labeling” in diagrams

Use explicit labels in diagram text (or captions):

- **CONFIRMED**: implemented and verified in repo
- **PROPOSED**: design intent / plan
- **UNKNOWN**: needs verification

### Example: Mermaid diagram (pipeline view)

```mermaid
flowchart LR
  A[Text-defined diagram source\n.mmd/.puml/.dot] --> B[Renderer toolchain\n(local or container)]
  B --> C[Rendered assets\n.svg/.png]
  C --> D[Docs pages\nREADME / architecture / runbooks]
  B --> E[CI gate\nfail on drift or syntax error]
  E --> C
```

> If the Mermaid block doesn’t render in your viewer, open the file on GitHub or use a Mermaid viewer.

---

## CI integration

**Recommended CI behavior**:

1. Run `render --all`
2. Verify the worktree is clean (no uncommitted diffs)
3. Fail if any diagram cannot be rendered

```bash
# Pseudocode CI step
./docs/diagrams/tools/render/render.sh --all
git diff --exit-code
```

---

## Troubleshooting

### Mermaid renders locally but not on GitHub

- Confirm the code fence is exactly ` ```mermaid `
- Validate Mermaid syntax (prefer small sub-diagrams over mega-diagrams)

### PlantUML renders differently across machines

- Pin the PlantUML version (and Java) via container or lockfile
- Ensure fonts are available in CI

### Graphviz “dot” layout drift

- Pin Graphviz version
- Keep graph stable: avoid relying on implicit node ordering

---

## Appendix

### Adding a new diagram (checklist)

- [ ] Add the **source** file in `docs/diagrams/src/`
- [ ] Add a manifest entry (if using `manifest.yaml`)
- [ ] Render and commit the **output** in `docs/diagrams/rendered/`
- [ ] Embed the output with meaningful **alt text** in the consuming doc
- [ ] If the diagram makes claims, label it CONFIRMED/PROPOSED and link to the relevant doc/ADR

### Definition of Done for diagram tooling changes

- [ ] Rendering is deterministic on CI (container or pinned versions)
- [ ] CI fails on drift (`git diff --exit-code`)
- [ ] New engines/adapters include a minimal test fixture
- [ ] Documentation updated (this README + top-level `docs/diagrams/README.md` if present)
