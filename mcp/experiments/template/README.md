# 🔬 MCP Experiment — TEMPLATE

> Copy this folder and rename to `mcp/experiments/EXP-YYYYMMDD-<slug>/`.

## 0) Metadata

- **Experiment ID:** `EXP-YYYYMMDD-<slug>`
- **Owner(s):** @you
- **Status:** ☐ Planned ☐ Running ☐ Completed ☐ Abandoned
- **Scope areas:** `data` | `stac` | `web` | `src` | `scripts` | `ci` | `docker`
- **Related issues/PRs:** Fixes #…, Relates #…
- **Milestone:** `m1-data` | `m2-analytics` | `m3-story` | `m4-tech` | `m5-mcp`

## 1) Objective / Hypothesis

- **Question:** …
- **Hypothesis:** …
- **Success criteria:** …

## 2) Inputs & Bounds

- **STAC inputs:** list item/collection IDs or paths
- **Source descriptors:** `data/sources/*.json`
- **AOI / timeframe:** bbox / dates
- **Licenses / provenance:** notes + citations

## 3) Method (SOP)

- Controls/treatments/params noted in `params.yaml`
- Deterministic commands live in `commands.sh`

## 4) Repro Commands

Run from repo root (or this dir) after activating your venv:

```bash
bash mcp/experiments/EXP-YYYYMMDD-<slug>/commands.sh
