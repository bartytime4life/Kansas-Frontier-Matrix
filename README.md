# Kansas Frontier Matrix (KFM)

**Kansas Frontier Matrix (KFM)** is a research-and-engineering workspace for building a **Frontier Matrix**: a living, versioned map of relationships between

- **phenomena** (what we observe),
- **models** (what we compute),
- **hypotheses/claims** (what we assert),
- **datasets** (what we measure), and
- **experiments** (what we can do next),

with strict emphasis on **validated math**, **error checking**, **reproducibility**, and **real-world application**.

KFM treats scientific progress as a *computable process*: we continuously ingest evidence, update belief weights, run simulations, score knowledge gaps (“frontiers”), and rank the next best experiments.

---

## Project status

This README is intentionally written as a **high-quality scaffold**. If you already have code and a concrete directory layout, replace the “recommended layout” and command examples with your repo’s actual structure.

---

## Table of contents

- [What is the Frontier Matrix?](#what-is-the-frontier-matrix)
- [Core data model](#core-data-model)
- [Evidence update and scoring](#evidence-update-and-scoring)
- [Frontier detection](#frontier-detection)
- [Recommended repository layout](#recommended-repository-layout)
- [Quickstart](#quickstart)
- [Reproducibility standards](#reproducibility-standards)
- [Simulation workflow](#simulation-workflow)
- [Experiment design workflow](#experiment-design-workflow)
- [Validation and testing](#validation-and-testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

## What is the Frontier Matrix?

The Frontier Matrix is a structured way to answer questions like:

- Which models explain which phenomena, under what assumptions, and with what empirical support?
- Where are the “gaps” between regimes (quantum/classical, micro/macro, deterministic/stochastic, weak/strong coupling, etc.)?
- Which experiments or simulations would reduce uncertainty fastest per unit cost?

Instead of holding this in people’s heads or scattered notes, KFM represents it as a typed, evidence-weighted relational system that can be queried and optimized.

---

## Core data model

### Typed nodes

KFM treats the world as a set of **typed entities**:

- \(\mathcal{P}\): phenomena
- \(\mathcal{M}\): models
- \(\mathcal{H}\): hypotheses / claims
- \(\mathcal{D}\): datasets
- \(\mathcal{E}\): experiments

Define the universe of nodes:

\[
\mathcal{V} = \mathcal{P} \cup \mathcal{M} \cup \mathcal{H} \cup \mathcal{D} \cup \mathcal{E}
\]

Each node has:

- stable `id`
- `type`
- human-readable `name`
- `description`
- optional regime/scale metadata
- citations / provenance

### Typed relations as a multi-relational graph (or adjacency tensor)

Let \(\mathcal{R}\) be the set of relation types, e.g.

- `EXPLAINS`, `PREDICTS`, `CONSTRAINS`, `USES_DATASET`, `SUPPORTED_BY`, `CONTRADICTS`, `DEPENDS_ON`

Represent relations as a family of adjacency matrices—equivalently, an adjacency tensor:

\[
A_r(i,j) \in \mathbb{R}, \quad r \in \mathcal{R},\; i,j \in \mathcal{V}
\]

In practice, each edge stores a *structured weight*:

\[
A_r(i,j) = (w,\; \sigma,\; s_{rep},\; \text{evidence},\; \text{notes})
\]

Where:

- \(w\) is the current strength of support (or signed support if you allow negative evidence)
- \(\sigma\) is uncertainty/dispersion
- \(s_{rep}\) is a reproducibility score (repeatability, cross-lab support, data availability)

This yields a computable object for:

- coverage analysis (what is unexplained / weakly supported)
- contradiction discovery (cycles, inconsistent assumption sets)
- experiment prioritization (expected information gain)

---

## Evidence update and scoring

A simple, auditable update mechanism is **log-odds accumulation**.

Maintain log-odds \(\ell\) for an edge being “true/useful”:

\[
\ell = \log\frac{P(\text{edge true})}{1 - P(\text{edge true})}
\]

Each new evidence item \(e\) contributes \(\Delta\ell(e)\) (positive or negative):

\[
\ell \leftarrow \ell + \sum_e \Delta\ell(e)
\]

Then convert back to a bounded score with the logistic function:

\[
 w = \sigma(\ell) = \frac{1}{1 + e^{-\ell}}
\]

Why this is useful:

- updates are monotonic unless explicitly overridden
- contributions are explainable (“this paper moved \(\ell\) by +0.7”)
- it composes across heterogeneous evidence sources

If you prefer Bayesian updates with explicit likelihood functions, store them per evidence type and use a shared interface; log-odds is still a convenient summary.

---

## Frontier detection

A **frontier** is a region of the matrix with:

- low coverage (few strong edges)
- high uncertainty
- high contradiction density

One practical per-phenomenon frontier score:

\[
F(p) = \alpha\,(1-\max_m w_{m\to p}) + \beta\,\mathrm{Uncertainty}(p) + \gamma\,\mathrm{Contradictions}(p)
\]

High \(F\) means “this is where new simulations/experiments are likely to matter.”

---

## Recommended repository layout

If you want a clean, scalable structure for compute-heavy R\&D, this layout works well:

```
Kansas-Frontier-Matrix/
  README.md
  pyproject.toml              # or requirements.txt
  kfm/                        # python package (core library)
    __init__.py
    cli.py                    # command line entry points
    matrix/                   # data model + storage
    evidence/                 # scoring, Bayesian/log-odds updates
    simulate/                 # simulation drivers
    experiments/              # experiment cards + planning
    validate/                 # invariants, schema checks
    viz/                      # plotting / dashboards
  schemas/                    # JSONSchema / pydantic models exported
  evidence/                   # evidence records (json/yaml)
  data/
    raw/
    processed/
  configs/
  notebooks/
  runs/                       # output artifacts, organized by run id
  tests/
  docs/
```

If your repo already exists with different paths, keep the **concepts** and update the **paths/commands**.

---

## Quickstart

### Install

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
```

Install dependencies:

- If using `pyproject.toml`:

```bash
pip install -e .
```

- If using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Validate and build the matrix (example CLI)

If you provide a CLI (recommended), you’ll typically want the following commands:

```bash
# 1) Validate schemas + invariants
python -m kfm.cli validate

# 2) Build/update the frontier matrix from evidence records
python -m kfm.cli build-matrix --in evidence/ --out runs/latest/

# 3) Generate a human-readable report
python -m kfm.cli report --run runs/latest/ --out docs/report.md
```

### Run a small simulation campaign (example)

```bash
python -m kfm.cli simulate --config configs/demo.yaml --out runs/sim_demo/
```

---

## Reproducibility standards

KFM aims to be “low entropy” by default. Each run artifact should record:

- code version (git commit hash or equivalent)
- dependency lock (e.g., `pip freeze`, `uv lock`, or `poetry.lock`)
- random seeds
- machine / runtime metadata (CPU/GPU, OS)
- full config used

Recommended pattern:

- every run produces a **run manifest** (JSON)
- outputs are content-addressed or at least uniquely named
- report generation is deterministic from `(inputs, config, code)`

---

## Simulation workflow

A robust simulation system naturally separates into:

1. **Model layer** (pure, testable): deterministic functions/solvers that map inputs → outputs
2. **Campaign layer** (orchestration): sweeps, sensitivity analysis, caching, regression comparisons

Minimum deliverables:

- parameter schemas + bounds
- seed control
- run manifests (inputs/outputs)
- metrics extraction
- regression tests for known scenarios

If you later add accelerators (JAX/Numba/CUDA), keep the model layer reference implementation intact for validation.

---

## Experiment design workflow

Treat experiments as *versioned proposals* with explicit hypotheses and predicted outcomes.

An “experiment card” should include:

- objective (which frontier score are we reducing?)
- target edges to update (which claims should move?)
- measurement protocol
- predicted effect size and uncertainty
- power / sensitivity estimate
- cost and feasibility notes
- failure modes

Then compute an **expected information gain (EIG)** (or a proxy score) to rank candidate experiments.

---

## Validation and testing

Validation is not optional in a matrix-of-claims project.

### Suggested invariants

- no dangling references (`src` and `dst` must exist)
- relation types must be in an allowlist
- schema-valid nodes/edges only
- contradictions must be explicit (no “silent” inconsistency)
- evidence updates must be auditable (each delta recorded)

### Suggested test layers

- unit tests for scoring and aggregation
- property tests for invariants (e.g., random graphs still validate)
- regression tests for simulation outputs

Tooling suggestions (optional):

- `pytest` (tests)
- `ruff` (lint)
- `black` (format)
- `pre-commit` (automation)

---

## Roadmap

### Milestone 1 — Minimal matrix engine

- [ ] Node/edge schema (JSONSchema or pydantic)
- [ ] Graph/tensor builder + validation
- [ ] Evidence aggregation (log-odds or Bayesian)
- [ ] CLI: `validate`, `build-matrix`

### Milestone 2 — Frontier scoring + reporting

- [ ] Frontier score definitions
- [ ] Contradiction detection
- [ ] Report generator (Markdown/HTML)
- [ ] Basic visualization

### Milestone 3 — Simulation campaigns

- [ ] Config-driven runs
- [ ] Parameter sweeps + caching
- [ ] Regression suite for sim outputs

### Milestone 4 — Experiment planner

- [ ] Experiment cards
- [ ] EIG ranking
- [ ] “next best experiment” suggestions

---

## Contributing

A suggested contribution loop:

1. Add/update nodes, edges, and evidence records.
2. Run validation.
3. Run tests.
4. Rebuild the matrix and regenerate reports.

Keep changes **small and reviewable**: in a project like this, provenance and auditability matter.

---

## Citation

If you publish results derived from this repository, cite it as:

```text
Kansas Frontier Matrix (KFM), version <commit>, <year>.
```

---

## License

Choose one and add a `LICENSE` file:

- Apache-2.0 (permissive, patent-friendly)
- MIT (simple permissive)
- GPL-3.0 (copyleft)
