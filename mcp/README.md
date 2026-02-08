# MCP — Methods & Computational Experiments (KFM)

This directory is the **MCP workspace** for Kansas Frontier Matrix (KFM): the place to document and reproduce computational methods, analyses, experiments, model training/evaluation, and repeatable SOPs.

> **Why this exists:** KFM is designed so that outputs used in maps, story nodes, or user-facing UI can be traced to **versioned evidence** and reproduced end-to-end. MCP is where we keep the “lab notebook” and method lineage for that work.

---

## Quick links (project-level)

From here, you will most often jump to:

- **KFM Master Guide (v13):** `../docs/MASTER_GUIDE_v13.md`
- **Architecture:** `../docs/ARCHITECTURE.md`
- **Operating contract:** `../docs/OPERATING_CONTRACT.md`
- **Standards (contracts):**
  - `../docs/standards/KFM_DATA_LIFECYCLE.md`
  - `../docs/standards/KFM_STAC_PROFILE.md`
  - `../docs/standards/KFM_DCAT_PROFILE.md`
  - `../docs/standards/KFM_PROV_PROFILE.md`
  - `../docs/standards/KFM_GRAPH_SCHEMA.md`
  - `../docs/standards/KFM_API_CONTRACT.md`
  - `../docs/standards/KFM_UI_CONTRACT.md`
  - `../docs/standards/KFM_GOVERNANCE_POLICY.md`
- **Templates:**
  - `../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
  - `../docs/templates/TEMPLATE__STORY_NODE.md`
- **Glossary (canonical):** `../docs/glossary.md`

> Paths above reflect the **v13 layout** described in the KFM master guide. If your branch differs, update links in this README to match the repo structure.

---

## Non-negotiables (MCP inside KFM)

### 1) Follow the canonical pipeline order

KFM’s canonical ordering is:

**ETL → Catalogs (STAC/DCAT/PROV) → Graph → APIs → UI/Map → Story Nodes → Focus Mode**

MCP work **must not “skip” boundaries** if it will impact user-facing outputs.

### 2) Evidence must be publishable as an artifact, not a screenshot

If an MCP experiment produces results intended for a map layer, a story node claim, or an API response, the result must be captured as an **evidence artifact** that can be:

- versioned,
- validated,
- traced to provenance,
- and served through policy-aware interfaces.

### 3) Respect governance & data sovereignty

If data has community-defined access constraints, sensitivity, or requires redaction, that constraint must be reflected in the artifact’s metadata and in downstream exposure (graph/API/UI).

---

## What belongs in `mcp/`

**Put in `mcp/`:**
- Experiment protocols & reports (think “electronic lab notebook”)
- Run logs / parameters / metrics for computational experiments
- Curated notebooks (with an accompanying experiment report)
- Model cards for any model trained, evaluated, or used in the system
- SOPs for recurring workflows (OCR → NER → geocoding; georeferencing; QA checks; etc.)
- Small, reviewable outputs (figures, small tables) tied to an experiment report

**Do NOT put in `mcp/`:**
- Canonical datasets (those belong in `../data/**` and must be cataloged)
- Production pipeline code (belongs in the app/pipeline source tree)
- Untracked “random” notebooks without context (pair notebooks with an experiment report)

---

## Recommended directory layout

A practical MCP layout (compatible with KFM docs and experiment-tracking practices):

```text
mcp/
  README.md                  # you are here
  experiments/               # experiment reports + per-experiment artifacts
    EXP-0001__YYYY-MM-DD__short_slug/
      README.md              # experiment report (required)
      protocol.md            # protocol / preregistration (optional but recommended)
      configs/               # parameter files, prompts, query specs
      src/                   # small experiment scripts (or links to repo scripts)
      notebooks/             # optional; must be referenced by README.md
      results/               # plots/tables (small). Publish real datasets via ../data
      provenance/            # pointers or exports for PROV activities/entities
  notebooks/                 # curated, reusable notebooks (must link to an experiment)
  runs/                      # run outputs/logs (optional; may be too large for Git)
  model_cards/               # model documentation + registry
  sops/                      # standard operating procedures
```

> If a “run output” is large, treat it as a dataset release and publish via the data lifecycle (see “Publishing evidence artifacts” below), rather than burying it under `mcp/`.

---

## Experiment IDs & naming conventions

### Experiment ID format

Use a stable ID that can appear in:
- file paths,
- commit messages,
- graph provenance edges,
- and story node citations.

**Recommended pattern:**
- `EXP-0001` (monotonic counter) or
- `EXP-<DOMAIN>-0001` (if you need domain scoping)

### Folder naming

Use:

`EXP-0001__YYYY-MM-DD__short_slug/`

Example:

`mcp/experiments/EXP-0007__2026-02-08__georef-qaqc/`

### Commit message convention

Include the experiment ID in commits that materially affect the experiment.

Example:

`EXP-0007: add georef QA metrics + provenance pointers`

---

## Starting a new experiment (workflow)

1. **Create the experiment folder** under `mcp/experiments/`.
2. **Write the experiment report** (`README.md`) using the template below.
3. Ensure **inputs are traceable**:
   - Prefer inputs from `../data/processed/...` with catalog references.
   - If you must start from raw sources, document the path through the data lifecycle.
4. Run the experiment with **captured parameters** (configs, prompts, versions, seeds).
5. Save **results and interpretation**, plus validation notes.
6. If outputs should become system evidence, **publish them as evidence artifacts** (next section).

---

## Publishing evidence artifacts (data → catalog → graph → API → UI)

If an experiment output should be “real” KFM evidence (map layer, story node support, API-exposed resource), promote it into the KFM evidence chain instead of leaving it in `mcp/`.

### Evidence artifact checklist

- [ ] **Data** written to `../data/processed/<domain>/...`
- [ ] **STAC** record created/updated (collection + item as appropriate) under `../data/stac/**`
- [ ] **DCAT** dataset entry created/updated under `../data/catalog/dcat/**`
- [ ] **PROV** activity/entity records created/updated under `../data/prov/**`
- [ ] **Governance metadata** present (classification, redaction policy, access constraints)
- [ ] **Graph** ingest updated (stable IDs, provenance edges)
- [ ] **API** exposure uses published IDs (no hard-coded file paths)
- [ ] **UI/Story Nodes** cite stable IDs (STAC/DCAT/PROV), not local filenames
- [ ] Validation gates pass (schema + integrity + policy checks)

---

## Templates (copy/paste)

### A) Experiment report template (`mcp/experiments/.../README.md`)

> Use this for every “significant” analysis or method test. Keep it specific enough that another contributor can reproduce the result.

```markdown
# EXP-0000 — <short title>

## Metadata
- **Status:** planned | running | complete | archived
- **Date started:** YYYY-MM-DD
- **Date completed:** YYYY-MM-DD (if complete)
- **Owner(s):** <name(s)>
- **Related work:** <Issue/PR links, related EXP IDs>

## Research question / problem statement
- What decision does this experiment support?

## Background & prior work
- What is already known?
- References:
  - <links to docs, prior experiments, external references (as applicable)>

## Hypothesis / expected outcome
- What do you expect to see, and why?

## Protocol (write before running, update only with tracked deviations)
- **Objective**
- **Materials / tools**
  - datasets (include catalog IDs if available)
  - software versions / environment notes
  - hardware notes (if relevant)
- **Variables**
  - independent variables
  - dependent variables
  - controls
- **Procedure**
  1.
  2.
  3.
- **Expected outcome**
- **Deviations from protocol**
  - (log any changes here with timestamps)

## Inputs (traceability)
List every input and how to retrieve it.
- Dataset(s):
  - Path(s): `../data/...`
  - Catalog IDs: (STAC/DCAT IDs if available)
  - Versioning notes: (dataset v#, commit hash, etc.)
  - Classification / access constraints:

## Method (implementation details)
- Code pointers:
  - script(s): `<path>`
  - commit hash: `<hash>`
- Config / parameters:
  - files: `configs/...`
  - key settings:
- Randomness control:
  - seeds:
- Reproduction command(s)
  - exact commands to run:

## Data collection & logging
- What gets logged, where, and in what format?

## Analysis
- How are results computed? (metrics, statistics, validation rules)

## Results
- Primary metrics:
- Figures / tables:
  - `results/...`
- Unexpected observations:

## Validation / QA
- What checks confirm this result is correct and not an artifact?
- If applicable: comparison vs baseline or prior EXP IDs.

## Interpretation & decision
- What does this mean for KFM?
- Decision / recommendation:
- Limitations / known failure modes:

## Outputs (and where they live)
- MCP outputs (small artifacts): `results/...`
- Published evidence artifacts (if promoted):
  - data: `../data/processed/...`
  - STAC: `../data/stac/...`
  - DCAT: `../data/catalog/dcat/...`
  - PROV: `../data/prov/...`

## Next steps
- Follow-up experiments:
- SOP candidate? (yes/no; link if created)

## Change log
- YYYY-MM-DD — created
- YYYY-MM-DD — updated <what/why>
```

### B) SOP template (`mcp/sops/<SOP_NAME>.md`)

```markdown
# SOP — <title>

## Purpose
- What recurring workflow does this SOP standardize?

## Scope
- What’s included / excluded?

## Preconditions / access
- Required tools
- Required credentials or datasets
- Governance constraints (classification, redaction, access)

## Inputs
- Input datasets (paths + catalog IDs)
- Config files / parameters

## Procedure
1.
2.
3.

## Outputs
- Output files and where they belong (mcp vs data lifecycle)
- Required metadata updates (STAC/DCAT/PROV)

## Verification / QA
- How to confirm success?
- Expected metrics or spot checks

## Troubleshooting
- Common failure modes
- Recovery steps

## Provenance notes
- What must be captured for reproducibility (hashes, versions, run IDs)?
```

### C) Model card template (`mcp/model_cards/<MODEL_ID>.md`)

> Required for any ML/NLP model that is trained, evaluated, or used to produce user-facing outputs.

```markdown
# Model Card — <MODEL_ID> (vX.Y)

## Overview
- What is this model? What task does it perform?

## Intended use
- Primary use cases
- Out-of-scope uses

## Training data
- Sources + traceability (STAC/DCAT IDs, paths, licenses)
- Sensitivity / governance constraints

## Training procedure
- Code pointer(s) + commit hash
- Hyperparameters
- Random seeds
- Environment details (framework versions, hardware)

## Evaluation
- Evaluation datasets (traceable)
- Metrics
- Baselines compared

## Ethical considerations / bias
- Known bias risks
- Mitigations or tests performed

## Limitations
- Failure modes
- Confidence boundaries

## Change log
- vX.Y — <what changed and why>
```

---

## Reproducibility checklist (use for every experiment)

- [ ] Research question & hypothesis documented **before** running
- [ ] Inputs listed with stable references (paths + IDs + versions)
- [ ] Code pointers included (file paths + commit hash)
- [ ] Parameters documented (configs checked in or captured)
- [ ] Random seeds recorded (if applicable)
- [ ] Environment recorded (dependencies, versions)
- [ ] Results linked to generated artifacts (plots/tables) with clear provenance
- [ ] Validation performed (sanity checks, baseline comparison, QA steps)
- [ ] If promoted to evidence: STAC/DCAT/PROV + governance metadata complete

---

## When an MCP change requires governance review

Escalate for governance review when MCP work:
- introduces new Indigenous knowledge sources or culturally sensitive material,
- changes classification/redaction rules for outputs,
- adds a new public-facing map layer or story node evidence dependency,
- modifies policies affecting access control or safe exposure.

(See the project governance policy and master guide for specifics.)

---

## Suggested indexes (optional but recommended)

To make MCP discoverable as it grows:

- `mcp/experiments/_index.md` — table of all EXP IDs, titles, status, and links
- `mcp/model_cards/_registry.md` — table of models, versions, uses, and links
- `mcp/sops/_index.md` — table of SOPs and their owners

---

## FAQ

### “Can I just commit a notebook?”
You can commit notebooks, but **notebooks should be paired** with an experiment report explaining purpose, inputs, parameters, results, and provenance.

### “Where do I put datasets produced by an experiment?”
If it’s a real dataset that may be referenced elsewhere: publish via `../data/processed/...` and create the required catalog/provenance records. Keep `mcp/` for documentation and small artifacts.

### “How do MCP experiments connect to Story Nodes?”
Story Nodes should cite stable artifact IDs (catalog/prov IDs), not raw file paths. MCP provides the traceable experimental lineage that justifies those citations.

