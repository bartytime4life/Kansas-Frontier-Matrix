# Experiments — Kansas Frontier Matrix

This directory is the **lab notebook** for the Kansas Frontier Matrix.  
Each subfolder holds a **self-contained, reproducible experiment** following the [MCP Experiment Template](../docs/templates/experiment.md).

---

## Folder Structure

```

experiments/
README.md                 # This index
templates/                # Optional: local copy of experiment.md template
001_treaty_boundaries/    # Example experiment
experiment.md           # Filled-in template (required)
config.yaml             # Run configuration / parameters
data/                   # Small inputs/outputs (heavier data → `data/` + STAC)
inputs/
outputs/
notebooks/              # Jupyter or R notebooks
logs/                   # JSONL + Markdown logs
artifacts/              # Figures, maps, charts
002_usgs_topo_alignment/
...

```

### Naming Convention

- **`<ID>_<slug>`** — numeric ID + short descriptive slug, for traceability and sorting.  
  Example: `003_kansas_river_floodplain`.

### Required Contents

- `experiment.md` — filled template, must include `[[Glossary:...]]` references.  
- `config.yaml` (or JSON) — parameters, seeds, environment config.  
- `logs/` — execution logs, checksums, environment notes.  
- `artifacts/` — visual or tabular results linked from `experiment.md`.

---

## Index

| ID   | Slug                    | Description                               | Link |
|------|-------------------------|-------------------------------------------|------|
| 001  | treaty_boundaries       | Time-aware map of Kansas treaty lines     | [experiment.md](001_treaty_boundaries/experiment.md) |
| 002  | usgs_topo_alignment     | Georeferencing historic USGS topo maps    | [experiment.md](002_usgs_topo_alignment/experiment.md) |
| 003  | kansas_river_floodplain | Reconstructing 1890s Kansas River floodplains | [experiment.md](003_kansas_river_floodplain/experiment.md) |

_Add new experiments below as they are created._

---

## Contribution Rules

1. **Clone Template**  
   Copy [`docs/templates/experiment.md`](../docs/templates/experiment.md) into a new subfolder.

2. **Fill Required Sections**  
   Complete all headings; include glossary links (`[[Glossary:...]]`).

3. **Track Data Properly**  
   - Small files: keep in `data/inputs` or `data/outputs`.  
   - Large/binary: track via DVC or Git LFS in `/data`, reference from STAC.  

4. **Logs and Checksums**  
   Save run logs in `logs/` and generate SHA-256 for inputs/outputs.  
   Use `scripts/gen_sha256.sh` where possible.

5. **Artifacts**  
   Store maps, charts, or summary tables in `artifacts/` and link them in `experiment.md`.

6. **Pre-Commit Hooks**  
   Experiments must pass:
   - Heading structure validation  
   - At least one glossary reference  
   - No broken contentReference artifacts  

---

✅ Following these rules keeps the experiment record **consistent, auditable, and reproducible** across the Kansas Frontier Matrix.
```

---
