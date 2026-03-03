# Configs README comparison audit

This document summarizes high-confidence structure expectations discovered by comparing README files under `configs/`.

## Areas that were under-built before this audit

- `configs/ui/` described `defaults`, `env`, `theme`, `map`, `story`, and `focus` config surfaces, but those directories and baseline files were missing.
- `configs/pipelines/` described `schemas`, `env`, `schedules`, `policy`, and `fixtures`; only top-level stubs existed.
- `configs/policy/` described a `decisions/` ADR area and concrete schema family files, but only placeholder files were present.

## What was added

- Initial directory trees and README files for the missing surfaces.
- Baseline non-secret config examples and minimal JSON Schemas to make each surface concrete.
- Policy index + starter policy bundles linked to concrete schema filenames.

These are conservative starter artifacts intended to be tightened by owning teams.
