# Ecology Domain Guide

This domain lane defines how ecological evidence is represented, validated, and published inside Kansas Frontier Matrix (KFM).

## Purpose

The ecology domain exists to keep a strict separation between:

- **Observed records** (field observations, specimen records, sensor measurements)
- **Derived products** (vegetation layers, interpolated surfaces, model outputs)
- **Publication-safe records** (generalized or redacted for sensitive locations)

This separation prevents model output from being mistaken as direct observation and ensures privacy controls are applied before publication.

## Core Objects

The ecology lane uses four primary contract objects in `schemas/contracts/v1/ecology/`:

1. `taxon_record` — a normalized taxonomic identity record.
2. `observation_plot` — plot/site level observations with methods and provenance.
3. `derived_vegetation_layer` — raster/vector derivative layers plus lineage.
4. `sensitive_occurrence_record` — restricted object for high-risk occurrence data.

## Required Trust Signals

Every ecology object should make these fields explicit:

- Evidence references
- Source registry references
- Spatial precision served to public
- Rights/license posture
- Sensitivity posture
- Review/publication state

## Data Registry Inputs

The ecology registry (`data/registry/ecology/`) has three catalogs:

- `sources.yaml` for steward/source definitions and trust posture
- `datasets.yaml` for known datasets and schema bindings
- `sensitivity_policies.yaml` for domain policy rules

## Publication and Geoprivacy

Publication is fail-closed:

- Unknown rights => not publishable
- Unknown sensitivity => not publishable
- Restricted species with exact coordinates => not publishable
- Missing evidence bundle refs => not publishable for consequential claims

See `SENSITIVITY_AND_GEOPRIVACY.md` for concrete public/generalized/restricted handling.

## Validator

`tools/validators/ecology/validate_ecology_bundle.py` validates an ecology bundle descriptor (JSON) that references:

- one or more source definitions from the registry,
- one or more datasets from the registry,
- and a declared policy id.

The validator emits a deterministic pass/fail result and can be used as a pre-publication gate in CI.
