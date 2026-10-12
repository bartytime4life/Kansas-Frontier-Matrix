<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/temporal/src
title: Temporal package source envelope
type: source-readme
version: v1.2.0
status: proposed; fixture-first
updated: 2026-09-05
responsibility_root: packages/
[/KFM_META_BLOCK_V2] -->

# Temporal source envelope

packages/temporal/src contains the importable implementation for the proposed shared temporal view-state profile. It is renderer-independent and has no source acquisition, persistence, policy, evidence, release, or publication side effects.

The current source surface is the temporal module:

- temporal/core.py: typed boundary normalization, query identity, frame-context checks, and generation-guarded reducer.
- temporal/__init__.py: documented public exports only.

The module preserves the lifecycle and responsibility boundaries established by docs/doctrine/directory-rules.md and ADR-0029. It does not create a second temporal contract or translate the unresolved TemporalWindow.time_kind vocabulary.
